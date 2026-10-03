#!/usr/bin/env bash
# instalar_skill.sh — instala una skill (o un pack de skills) en Claude Code.
#
# Acepta: un .zip, un .skill (ES UN ZIP con otra extensión) o una carpeta con SKILL.md adentro
# (o una carpeta "skills/" con varias skills, como las de los kits de ZEA).
#
# Uso:
#   bash tools/instalar_skill.sh <archivo.zip|archivo.skill|carpeta>            # para todas tus sesiones (~/.claude/skills)
#   bash tools/instalar_skill.sh <archivo|carpeta> --proyecto                    # solo este proyecto (.claude/skills)
#
# Qué hace, en orden:
#   1. Lista el contenido sin instalar.
#   2. Busca claves/tokens hardcodeados. Si encuentra algo, NO instala (salvo --forzar).
#   3. Si ya existe una skill con el mismo nombre, hace backup en OUTPUTS/skills-backup/<nombre>-<fecha>/.
#   4. Instala y muestra el name + description de cada SKILL.md instalado.
#
# Windows: correr desde Git Bash (la terminal de Claude Code después del kit 00). ~/.claude/skills es
# C:\Users\<usuario>\.claude\skills. Si Git Bash no trae unzip, usa Python (python -m zipfile).
set -euo pipefail

ORIGEN="${1:-}"
[ -z "$ORIGEN" ] && { echo "Uso: bash tools/instalar_skill.sh <archivo.zip|.skill|carpeta> [--proyecto] [--forzar]"; exit 1; }
shift || true
DESTINO="$HOME/.claude/skills"
FORZAR=0
for a in "$@"; do
  case "$a" in
    --proyecto) DESTINO="$(pwd)/.claude/skills" ;;
    --forzar)   FORZAR=1 ;;
  esac
done
mkdir -p "$DESTINO"
HOY="$(date +%Y-%m-%d)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Python que funcione de verdad (en Windows "python3" puede ser el alias que abre la Microsoft Store)
PY=""
for c in python3 python py; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c "import sys" >/dev/null 2>&1; then PY="$c"; break; fi
done

# 1. Descomprimir o copiar a una carpeta temporal
if [ -f "$ORIGEN" ]; then
  echo "== Contenido de $(basename "$ORIGEN") (se trata como zip aunque diga .skill):"
  if command -v unzip >/dev/null 2>&1; then
    { unzip -l "$ORIGEN" | sed -n '4,200p' | head -60; } || true
    unzip -oq "$ORIGEN" -d "$TMP"
  elif [ -n "$PY" ]; then
    { "$PY" -m zipfile -l "$ORIGEN" | head -60; } || true
    "$PY" -m zipfile -e "$ORIGEN" "$TMP"
  else
    echo "No tengo unzip ni Python para abrir el zip. Instalá Python (kit 00) y corré de nuevo."; exit 1
  fi
elif [ -d "$ORIGEN" ]; then
  if [ -f "$ORIGEN/SKILL.md" ]; then
    # la carpeta de UNA skill: se instala con el nombre de la carpeta
    cp -R "$ORIGEN" "$TMP/$(basename "$ORIGEN")"
  else
    # una carpeta con varias skills adentro (ej. la carpeta skills/ de un kit)
    cp -R "$ORIGEN"/. "$TMP"/
  fi
else
  echo "No existe: $ORIGEN"; exit 1
fi

# si vino una carpeta contenedora "skills/", bajar un nivel
if [ -d "$TMP/skills" ] && [ "$(find "$TMP" -maxdepth 2 -name SKILL.md | wc -l)" -eq 0 ]; then
  TMP_SK="$TMP/skills"
else
  TMP_SK="$TMP"
fi
# ignorar basura de macOS
rm -rf "$TMP_SK/__MACOSX" 2>/dev/null || true

# lista de carpetas de skills (una por línea; soporta espacios en las rutas)
SKILLS=()
while IFS= read -r d; do SKILLS+=("$d"); done < <(find "$TMP_SK" -mindepth 2 -maxdepth 2 -name SKILL.md -exec dirname {} \; | sort)
[ "${#SKILLS[@]}" -eq 0 ] && { echo "No encontré ningún <carpeta>/SKILL.md adentro. ¿Es una skill?"; exit 1; }

# 2. Escaneo de secretos
echo; echo "== Buscando claves hardcodeadas…"
PATRON='(sk-[A-Za-z0-9_-]{16,}|sk_live_[A-Za-z0-9]{10,}|rk_live_[A-Za-z0-9]{10,}|EAA[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|Bearer [A-Za-z0-9._-]{20,}|[0-9]{8,10}:AA[A-Za-z0-9_-]{30,}|api[_-]?key *[:=] *["'"'"'][A-Za-z0-9_-]{16,})'
if grep -rEn "$PATRON" "${SKILLS[@]}" 2>/dev/null | grep -v '<TU_' ; then
  echo "!! Hay posibles claves adentro (arriba). No instalo. Revisalas y corré de nuevo con --forzar si son falsos positivos."
  [ "$FORZAR" -eq 1 ] || exit 2
else
  echo "   Nada sospechoso."
fi

# 3 y 4. Backup + instalación
echo
for S in "${SKILLS[@]}"; do
  N="$(basename "$S")"
  if [ -d "$DESTINO/$N" ]; then
    BK="$(pwd)/OUTPUTS/skills-backup/$N-$HOY"
    mkdir -p "$(dirname "$BK")"
    rm -rf "$BK"; cp -R "$DESTINO/$N" "$BK"
    echo "   backup de la versión anterior de /$N → $BK"
    rm -rf "$DESTINO/$N"
  fi
  cp -R "$S" "$DESTINO/$N"
  DESC="$(grep -m1 '^description:' "$DESTINO/$N/SKILL.md" | tr -d '\r' | cut -c14-140 || true)"
  echo "   /$N instalada en $DESTINO/$N"
  echo "      $DESC…"
  # variables de entorno que usa (sin mostrar valores)
  # (|| true: si la skill no usa ninguna variable, grep devuelve 1 y con set -e cortaba el loop)
  VARS=$(grep -rhoE '\b[A-Z][A-Z0-9_]{3,}(_KEY|_TOKEN|_AK|_SK|_ID)\b' "$DESTINO/$N" 2>/dev/null | sort -u | tr '\n' ' ' || true)
  if [ -n "$VARS" ]; then echo "      usa del .env: $VARS"; fi
done

echo
echo "Listo. Abrí una sesión nueva de Claude Code (o reiniciala) y escribí / para ver los comandos nuevos."
