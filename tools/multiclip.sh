#!/usr/bin/env bash
# Arma un video SIN audio con varios clips de la biblioteca, repetidos en orden hasta cubrir la duración del audio.
# Uso:  bash tools/multiclip.sh audio.m4a salida_sin_audio.mp4 clip1.mp4 clip2.mp4 clip3.mp4 ...
# Después: python3 tools/componer.py --video salida_sin_audio.mp4 --voz audio.m4a --factor 1 ...
#   (microvariación: el audio del ganador ya trae música → --musica none)
# Regla: los clips del hook tienen que ser VIDEO real (nunca fotos con zoom) y no repetirse en el cuerpo.
set -euo pipefail
AUDIO="$1"; OUT="$2"; shift 2
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
FF="${FFMPEG:-$(command -v ffmpeg || true)}"
[ -n "$FF" ] || { echo "No encuentro ffmpeg. Mac: brew install ffmpeg (o ffmpeg-full) · Windows: winget install Gyan.FFmpeg y reiniciá Claude Code"; exit 1; }
FP="$(dirname "$FF")/ffprobe"
[ -x "$FP" ] || [ -x "$FP.exe" ] || FP="$(command -v ffprobe)"
# tr -d '\r': en Windows ffprobe.exe termina la línea con CRLF y "-t 12.3\r" rompe ffmpeg
DA=$("$FP" -v error -show_entries format=duration -of csv=p=0 "$AUDIO" | tr -d '\r')
LIST=$(mktemp)
for i in 1 2 3 4 5 6 7 8; do
  for c in "$@"; do
    # pwd -W (Git Bash) da C:/Users/... que es lo que entiende ffmpeg.exe; en Mac/Linux falla y usamos pwd.
    DIRABS="$(cd "$(dirname "$c")" && { pwd -W 2>/dev/null || pwd; })"
    RUTA="$DIRABS/$(basename "$c")"
    RUTA="$(printf '%s' "$RUTA" | sed "s/'/'\\\\''/g")"    # un apóstrofo en la ruta se escribe '\''
    echo "file '$RUTA'" >> "$LIST"
  done
done
"$FF" -y -loglevel error -f concat -safe 0 -i "$LIST" -t "$DA" \
  -vf "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1,fps=30" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p -an "$OUT"
echo "$OUT = ${DA}s"
