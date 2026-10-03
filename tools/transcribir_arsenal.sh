#!/usr/bin/env bash
# Transcribe en lote los anuncios candidatos de un arsenal de la Biblioteca de Anuncios.
# Sirve para DEDUPLICAR POR GUION HABLADO (la caption se recicla, el guion no).
#
# Uso:   bash tools/transcribir_arsenal.sh ids.txt en
#        ids.txt = un ID de anuncio de la Biblioteca por línea
#        segundo argumento = idioma del anunciante (en, es, pt, it, fr, de, ro, pl...)
# Salida: work/arsenal/<ID>.mp3 + <ID>.txt  y un resumen con los primeros 300 caracteres de cada uno.
set -euo pipefail
# Si "ffmpeg" no está en el PATH (Mac: ffmpeg-full no se agrega solo; Windows: winget a veces no refresca
# el PATH hasta reiniciar Claude Code), lo buscamos donde lo dejan Homebrew y winget (Gyan.FFmpeg).
if ! command -v ffmpeg >/dev/null 2>&1; then
  CANDS=(/opt/homebrew/opt/ffmpeg-full/bin /usr/local/opt/ffmpeg-full/bin)
  if [ -n "${LOCALAPPDATA:-}" ] && command -v cygpath >/dev/null 2>&1; then   # Windows (Git Bash)
    LAD="$(cygpath -u "$LOCALAPPDATA")"
    for D in "$LAD"/Microsoft/WinGet/Links "$LAD"/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin; do CANDS+=("$D"); done
  fi
  for D in "${CANDS[@]}"; do
    if [ -x "$D/ffmpeg" ] || [ -x "$D/ffmpeg.exe" ]; then PATH="$D:$PATH"; export PATH; break; fi
  done
fi
# Python: en Windows el comando es "python" o "py" (python3 suele no existir o abre la Microsoft Store).
PY=""
for C in python3 python py; do
  if command -v "$C" >/dev/null 2>&1 && "$C" -c "import sys" >/dev/null 2>&1; then PY="$C"; break; fi
done
# Windows sin PYTHONUTF8: whisper imprime el texto y un acento raro (ș, ł...) lo rompe con 'charmap'.
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
# whisper: el comando suelto, o como módulo de Python si pip no lo dejó en el PATH.
if command -v whisper >/dev/null 2>&1; then WHISPER=(whisper)
else WHISPER=("${PY:-python}" -m whisper); fi
if command -v yt-dlp >/dev/null 2>&1; then YTDLP=(yt-dlp); else YTDLP=("${PY:-python}" -m yt_dlp); fi
IDS="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"; LANG_REF="${2:-en}"
mkdir -p work/arsenal
cd work/arsenal
while read -r ID <&3 || [ -n "$ID" ]; do   # fd 3: que yt-dlp/ffmpeg no se coman la lista de IDs
  ID="$(echo "$ID" | tr -d '[:space:]')"   # también saca el \r de un ids.txt guardado en Windows
  [ -z "$ID" ] && continue
  if [ ! -f "${ID}.mp3" ]; then
    "${YTDLP[@]}" -q -x --audio-format mp3 -o "${ID}.%(ext)s" \
      "https://www.facebook.com/ads/library/?id=${ID}" || { echo "sin video: $ID (puede ser imagen: se analiza copy + imagen)"; continue; }
    sleep 5   # la Biblioteca frena si le pegás muy rápido; si devuelve vacío, esperá y reintentá
  fi
  [ -f "${ID}.txt" ] || "${WHISPER[@]}" "${ID}.mp3" --model small --language "$LANG_REF" --output_format txt --verbose False >/dev/null 2>&1 \
    || { echo "whisper falló con $ID (¿está instalado? ${PY:-python} -m pip install openai-whisper)"; continue; }
  echo "== $ID"; head -c 300 "${ID}.txt"; echo
done 3< "$IDS"
