#!/usr/bin/env python3
"""Corta un video limpio (clean.mp4 de Vmake) en clips por cambio de escena, sin audio, en 9:16.
Es tu BIBLIOTECA DE CLIPS: la armás una vez y la reusás en todas las iteraciones (gasto cero).

Uso:  python3 tools/cortar_clips.py work/<slug>/clean.mp4 ADS/<PRODUCTO>/clips v3 [umbral=0.3]
Salida: ADS/<PRODUCTO>/clips/v3-c00.mp4, v3-c01.mp4 ...
Después revisalos y borrá los que tengan restos de texto o manchas.
"""
import os
import re
import subprocess
import sys

from media import ffmpeg, dur

if len(sys.argv) < 4:
    sys.exit(__doc__)
src, outdir, pref = sys.argv[1:4]
umbral = float(sys.argv[4]) if len(sys.argv) > 4 else 0.3
MIN, MAX = 1.0, 6.0          # segundos por clip
os.makedirs(outdir, exist_ok=True)

total = dur(src)
log = subprocess.run([ffmpeg(), "-i", src, "-filter:v", f"select='gt(scene,{umbral})',showinfo",
                      "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
cortes = [0.0] + [float(x) for x in re.findall(r"pts_time:([\d.]+)", log)] + [total]

n = 0
for a, b in zip(cortes, cortes[1:]):
    t = a
    while b - t >= MIN:                      # escenas largas se parten en tramos de MAX
        fin = min(b, t + MAX)
        out = os.path.join(outdir, f"{pref}-c{n:02d}.mp4")
        subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-ss", f"{t + 0.1:.2f}", "-to", f"{fin - 0.1:.2f}",
                        "-i", src, "-an", "-vf", "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1,fps=30",
                        "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", out], check=True)
        n += 1
        t = fin
print(f"{n} clips en {outdir}")
