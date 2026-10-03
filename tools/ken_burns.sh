#!/usr/bin/env bash
# Video de costo cero desde fotos: zoom lento alternando acercar / alejar, 720x1280.
# SOLO PARA EL CUERPO del anuncio. El hook (primeros 2-3 s) va con clips de VIDEO real.
#
# Uso:  bash tools/ken_burns.sh carpeta_fotos 2.5 salida.mp4      (segundos por foto)
# Para poner un hook de clips reales adelante:
#   bash tools/multiclip.sh (o un clip suelto) y después concatenás hook + ken burns con el demuxer concat.
set -euo pipefail
DIR="$1"; SEG="${2:-2.5}"; OUT="$3"; FPS=30
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
FR=$(awk "BEGIN{print int($SEG*$FPS)}")   # awk y no python3: en Windows "python3" suele no existir
TMP=$(mktemp -d); i=0
for IMG in "$DIR"/*.jpg "$DIR"/*.jpeg "$DIR"/*.png "$DIR"/*.JPG "$DIR"/*.PNG; do
  [ -e "$IMG" ] || continue
  if (( i % 2 == 0 )); then Z="min(zoom+0.0015,1.15)"; else Z="if(lte(zoom,1.0),1.15,max(1.001,zoom-0.0015))"; fi
  "$FF" -y -loglevel error -loop 1 -i "$IMG" -vf \
    "scale=1440:2560:force_original_aspect_ratio=increase,crop=1440:2560,zoompan=z='$Z':d=$FR:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=720x1280:fps=$FPS,setsar=1" \
    -frames:v "$FR" -c:v libx264 -pix_fmt yuv420p "$TMP/c_$(printf %03d $i).mp4"
  # nombre RELATIVO: ffmpeg lo resuelve contra la carpeta de lista.txt. Una ruta /tmp/... de Git Bash
  # adentro de la lista no la entiende el ffmpeg.exe de Windows.
  echo "file 'c_$(printf %03d $i).mp4'" >> "$TMP/lista.txt"; i=$((i+1))
done
[ "$i" -gt 0 ] || { echo "No encontré fotos en $DIR"; exit 1; }
"$FF" -y -loglevel error -f concat -safe 0 -i "$TMP/lista.txt" -c copy "$OUT"
echo "$OUT listo ($i fotos, ${SEG}s c/u)"
