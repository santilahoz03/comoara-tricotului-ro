#!/usr/bin/env bash
# instalar_herramientas.sh — instala las herramientas de ZEA en Mac (Homebrew) o Linux (apt), SOLO las que
# necesitan los kits que vas a usar. Idempotente: si algo ya está, lo saltea. No instala nada fuera de esta lista.
#
# Uso (desde la carpeta de tu negocio; en el kit 00, desde la carpeta del kit):
#   bash tools/instalar_herramientas.sh --perfil base        # git + python (lo mínimo para todos)
#   bash tools/instalar_herramientas.sh --perfil cazar       # kit 01 (/cazar): igual que base
#   bash tools/instalar_herramientas.sh --perfil todo        # todo el sistema (kits 01 a 07)
#   bash tools/instalar_herramientas.sh --kits 01,02,06      # lo que necesitan esos kits
#   bash tools/instalar_herramientas.sh --solo ffmpeg,whisper,yt-dlp   # INSTALAR A DEMANDA (lo usan los kits 01-07)
#   bash tools/instalar_herramientas.sh --solo watch         # atajo: yt-dlp + ffmpeg + whisper (para /watch)
#   ... --simular                                            # muestra qué instalaría, sin instalar nada
# Sin argumentos = --perfil todo (así funcionaba antes). Los prompts de los kits pasan siempre el perfil explícito.
# --perfil, --kits y --solo se pueden combinar: se instala la unión.
#
# Paquetes: git python node ffmpeg yt-dlp whisper edge-tts requests gh chrome
#   (whisper suma ffmpeg solo: sin ffmpeg no transcribe. La base git + python se chequea siempre.)
set -u

ok()   { printf "  %-22s OK   %s\n" "$1" "${2:-}"; }
inst() { printf "  %-22s ...  instalando\n" "$1"; }
fail() { printf "  %-22s FALLÓ %s\n" "$1" "${2:-}"; FALLOS=$((FALLOS+1)); }
sim()  { printf "  %-22s FALTA → instalaría: %s\n" "$1" "$2"; }
FALLOS=0

TODOS="git python node ffmpeg yt-dlp whisper edge-tts requests gh chrome"

paquetes_de_kit() {  # kit → paquetes (ver sops/que-necesita-cada-kit.md del kit 00)
  case "$1" in
    00|0|01|1|07|7) echo "" ;;                         # base alcanza
    02|2) echo "chrome" ;;                              # QC de landings + Claude in Chrome
    03|3) echo "ffmpeg yt-dlp whisper edge-tts node" ;; # ads: video, subtítulos, voz, HyperFrames (npx)
    04|4) echo "node" ;;                                # CLI de AdsUploader (npm)
    05|5) echo "ffmpeg whisper node requests" ;;        # VSL post-pago (npx skills add dreamapi)
    06|6) echo "chrome gh requests" ;;                  # bonos a PDF + GitHub Pages
    watch) echo "yt-dlp ffmpeg whisper" ;;
    todos|todo) echo "$TODOS" ;;
    *) echo "__desconocido__" ;;
  esac
}

PEDIDO=""; SIMULAR=0; HUBO_ARG=0
agregar() { PEDIDO="$PEDIDO $*"; }
lista() { echo "$1" | tr ',;' '  '; }
while [ $# -gt 0 ]; do
  case "$1" in
    --perfil|--kits|--solo)
      [ $# -lt 2 ] && { echo "Falta el valor después de $1"; exit 2; }
      op="$1"; val="$2"; shift 2; HUBO_ARG=1 ;;
    --perfil=*|--kits=*|--solo=*) op="${1%%=*}"; val="${1#*=}"; shift; HUBO_ARG=1 ;;
    --simular|--dry-run) SIMULAR=1; shift; continue ;;
    -h|--help) sed -n '2,17p' "$0"; exit 0 ;;
    *) echo "No entiendo '$1'. Mirá: bash $0 --help"; exit 2 ;;
  esac
  case "$op" in
    --perfil)
      case "$val" in
        base|cazar|solo-cazar) ;;
        todo|todos) agregar "$TODOS" ;;
        *) echo "Perfil '$val' no existe. Usá base, cazar o todo (o --kits / --solo)."; exit 2 ;;
      esac ;;
    --kits)
      for k in $(lista "$val"); do
        p="$(paquetes_de_kit "$k")"
        [ "$p" = "__desconocido__" ] && { echo "Kit '$k' no existe (00 a 07, o watch)."; exit 2; }
        agregar "$p"
      done ;;
    --solo)
      for s in $(lista "$val"); do
        case "$s" in
          watch) agregar "$(paquetes_de_kit watch)" ;;
          base) ;;
          yt_dlp|ytdlp) agregar yt-dlp ;;
          edge_tts|edgetts) agregar edge-tts ;;
          openai-whisper) agregar whisper ;;
          ffmpeg-full|libass) agregar ffmpeg ;;
          google-chrome) agregar chrome ;;
          nodejs|npm) agregar node ;;
          *) if echo " $TODOS " | grep -q " $s "; then agregar "$s"; else
               echo "Paquete '$s' no existe. Disponibles: $TODOS (o watch)."; exit 2; fi ;;
        esac
      done ;;
  esac
done
[ "$HUBO_ARG" = 0 ] && { echo "(Sin perfil: instalo TODO, como antes. Para instalar solo lo que usás: --perfil base|cazar|todo, --kits o --solo)"; agregar "$TODOS"; }

quiero() { echo " $PEDIDO " | grep -q " $1 "; }
quiero whisper && agregar ffmpeg        # whisper sin ffmpeg no transcribe
EXTRA=""; for p in $TODOS; do quiero "$p" && [ "$p" != git ] && [ "$p" != python ] && EXTRA="$EXTRA $p"; done
echo "Base (siempre): git python · Además:${EXTRA:- nada}"
[ "$SIMULAR" = 1 ] && echo "MODO SIMULACIÓN: no se instala nada, solo te digo qué haría."

SO="$(uname -s)"
echo "Sistema: $SO"

# ── Mac ──────────────────────────────────────────────────────────────────────────────────────────────
mac_git_ok() {
  local g; g="$(command -v git 2>/dev/null)" || return 1
  # /usr/bin/git sin las herramientas de línea de comandos abre un cartel: no cuenta como instalado
  if [ "$g" = "/usr/bin/git" ] && ! xcode-select -p >/dev/null 2>&1; then return 1; fi
  git --version >/dev/null 2>&1
}
py_ok() {  # $1 = python; ¿es 3.9 o más?
  [ -n "$1" ] || return 1
  if [ "$1" = "/usr/bin/python3" ] && [ "$SO" = "Darwin" ] && ! xcode-select -p >/dev/null 2>&1; then return 1; fi
  "$1" -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)" >/dev/null 2>&1
}
pip_mod() { case "$1" in whisper) echo whisper ;; edge-tts) echo edge_tts ;; requests) echo requests ;; yt-dlp) echo yt_dlp ;; esac; }
pip_pkg() { case "$1" in whisper) echo openai-whisper ;; *) echo "$1" ;; esac; }

pip_instalar() {  # $1 = paquete lógico (whisper, edge-tts, requests, yt-dlp)
  local pkg imp nom; pkg="$(pip_pkg "$1")"; imp="$(pip_mod "$1")"; nom="$pkg"
  [ "$pkg" = yt-dlp ] && nom="yt-dlp (módulo Python)"
  if "$PY" -c "import $imp" >/dev/null 2>&1; then ok "$nom"; return; fi
  if [ "$SIMULAR" = 1 ]; then sim "$nom" "$PY -m pip install -U $pkg"; return; fi
  inst "$nom"
  "$PY" -m pip install -U "$pkg" >/dev/null 2>&1 \
    || "$PY" -m pip install -U --user "$pkg" >/dev/null 2>&1 \
    || "$PY" -m pip install -U --break-system-packages "$pkg" >/dev/null 2>&1
  "$PY" -c "import $imp" >/dev/null 2>&1 && ok "$nom" || fail "$nom" "probá: $PY -m pip install -U $pkg"
}

if [ "$SO" = "Darwin" ]; then
  # 1. Homebrew: solo hace falta si hay algo para instalar con brew.
  if ! command -v brew >/dev/null 2>&1; then
    # ZEA_BREW_RUTAS solo sirve para probar el script sin tocar el Homebrew real.
    for B in ${ZEA_BREW_RUTAS-/opt/homebrew/bin/brew /usr/local/bin/brew}; do
      if [ -x "$B" ]; then
        eval "$("$B" shellenv)"
        echo "Homebrew está instalado pero no en tu PATH. Para que quede fijo, corré una vez:"
        echo "  echo 'eval \"\$($B shellenv)\"' >> ~/.zprofile"
        break
      fi
    done
  fi
  HAY_BREW=0; command -v brew >/dev/null 2>&1 && HAY_BREW=1
  PREFIX=""; [ "$HAY_BREW" = 1 ] && PREFIX="$(brew --prefix)"

  # ¿Qué falta? (sin instalar nada todavía)
  FF_FULL=""
  for c in "${PREFIX:+$PREFIX/opt/ffmpeg-full/bin/ffmpeg}" /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg /usr/local/opt/ffmpeg-full/bin/ffmpeg; do
    [ -n "$c" ] && [ -x "$c" ] && { FF_FULL="$c"; break; }
  done
  falta_brew() {  # ¿este paquete necesita brew para instalarse?
    case "$1" in
      git) mac_git_ok && return 1 ;;
      python) { py_ok "${PREFIX:+$PREFIX/bin/python3}" || py_ok "$(command -v python3 2>/dev/null)"; } && return 1 ;;
      node) command -v node >/dev/null 2>&1 && return 1 ;;
      ffmpeg) [ -n "$FF_FULL" ] && command -v ffmpeg >/dev/null 2>&1 && return 1 ;;
      yt-dlp) command -v yt-dlp >/dev/null 2>&1 && return 1 ;;
      gh) command -v gh >/dev/null 2>&1 && return 1 ;;
      chrome) [ -d "/Applications/Google Chrome.app" ] && return 1 ;;
      *) return 1 ;;
    esac
    return 0
  }
  NECESITA_BREW=0
  for p in git python $EXTRA; do falta_brew "$p" && NECESITA_BREW=1; done
  if [ "$HAY_BREW" = 0 ] && [ "$NECESITA_BREW" = 1 ]; then
    if [ "$SIMULAR" = 1 ]; then
      echo "  (haría falta Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\")"
    else
      echo "Falta Homebrew. Instalalo con este comando (te va a pedir tu contraseña de la Mac, la escribís VOS):"
      echo '  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
      echo "Después volvé a correr este script."
      exit 1
    fi
  fi
  [ "$HAY_BREW" = 1 ] && ok brew "$(brew --version | head -1)"

  brew_pkg() {  # $1 = nombre para mostrar, $2 = fórmula (o "--cask x")
    if [ "$SIMULAR" = 1 ]; then sim "$1" "brew install $2"; return; fi
    inst "$1"
    # shellcheck disable=SC2086
    brew install $2 >/dev/null 2>&1 && ok "$1" || fail "$1" "probá: brew install $2"
  }

  # 2. Base: git + python
  if mac_git_ok; then ok git "$(git --version 2>/dev/null)"; else brew_pkg git git; fi
  PY=""
  for c in "${PREFIX:+$PREFIX/bin/python3}" "$(command -v python3 2>/dev/null)"; do py_ok "$c" && { PY="$c"; break; }; done
  if [ -n "$PY" ]; then ok python "$("$PY" --version 2>&1) · $PY"; else
    brew_pkg python python
    PY="${PREFIX:+$PREFIX/bin/python3}"; py_ok "$PY" || PY="python3"
  fi

  # 3. Programas de brew que pidieron tus kits
  for p in $EXTRA; do
    case "$p" in
      node|gh) if command -v "$p" >/dev/null 2>&1; then ok "$p" "$("$p" --version 2>/dev/null | head -1)"; else brew_pkg "$p" "$p"; fi ;;
      yt-dlp)  if command -v yt-dlp >/dev/null 2>&1; then ok yt-dlp "$(yt-dlp --version 2>/dev/null)"; else brew_pkg yt-dlp yt-dlp; fi ;;
      chrome)  if [ -d "/Applications/Google Chrome.app" ]; then ok "Google Chrome"; else brew_pkg "Google Chrome" "--cask google-chrome"; fi ;;
      ffmpeg)
        # ffmpeg-full (con libass) para subtítulos. No se agrega solo al PATH: whisper y yt-dlp necesitan
        # además un "ffmpeg" en el PATH, así que si no hay ninguno se instala también el común.
        if [ -n "$FF_FULL" ]; then ok ffmpeg-full; else brew_pkg ffmpeg-full ffmpeg-full; fi
        if [ "$SIMULAR" = 0 ]; then
          FF="${PREFIX:-/opt/homebrew}/opt/ffmpeg-full/bin/ffmpeg"
          [ -x "$FF" ] || FF="${FF_FULL:-$FF}"
          if [ -x "$FF" ] && "$FF" -hide_banner -filters 2>/dev/null | grep -qE " (ass|subtitles) "; then
            ok "libass" "$FF"
            echo "  → Para subtítulos usá SIEMPRE esta ruta: $FF"
          else
            fail "libass" "el filtro ass/subtitles no aparece"
          fi
        fi
        if command -v ffmpeg >/dev/null 2>&1; then ok "ffmpeg (PATH)" "$(command -v ffmpeg)"; else brew_pkg "ffmpeg (PATH)" ffmpeg; fi ;;
    esac
  done

elif [ "$SO" = "Linux" ]; then
  APT="git python3 python3-pip"
  quiero node && APT="$APT nodejs npm"
  quiero ffmpeg && APT="$APT ffmpeg"
  if [ "$SIMULAR" = 1 ]; then sim "apt" "sudo apt-get install -y $APT"; else
    sudo apt-get update -y >/dev/null
    # shellcheck disable=SC2086
    sudo apt-get install -y $APT >/dev/null && ok "apt" "$APT" || fail "apt" "sudo apt-get install -y $APT"
  fi
  PY="python3"
  if quiero ffmpeg && [ "$SIMULAR" = 0 ]; then
    if ffmpeg -hide_banner -filters 2>/dev/null | grep -qE " (ass|subtitles) "; then ok libass; else fail libass "instalá un build de ffmpeg con libass"; fi
  fi
  quiero gh && echo "  gh: instalalo siguiendo cli.github.com (no viene en apt por defecto)"
  quiero chrome && echo "  Chrome: bajalo de google.com/chrome"
else
  echo "Este script es para Mac o Linux. En Windows usá: powershell -ExecutionPolicy Bypass -File tools/instalar_herramientas.ps1"
  exit 1
fi

# 4. Paquetes de Python que pidieron tus kits
for p in whisper edge-tts yt-dlp requests; do
  quiero "$p" && pip_instalar "$p"
done

echo
if [ "$SIMULAR" = 1 ]; then echo "Simulación terminada: no se instaló nada."; else
  echo "Listo. Verificá con: python3 tools/verificar_stack.py --solo-herramientas"
  echo "(lee los kits que elegiste de la línea 'Kits elegidos' de tu CLAUDE.md; lo que no usás sale como NO LO USÁS)"
fi
[ "$FALLOS" -gt 0 ] && exit 1
exit 0
