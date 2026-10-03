#!/usr/bin/env python3
"""Control de calidad de un anuncio terminado. Devuelve una tabla OK / FALLA.

Chequea:
  1. Formato: ancho < alto (9:16), video h264, audio aac.
  2. Duración voz vs video final (más de 1 s de diferencia = bug de timing, típico: factor invertido).
  3. CTA entero: re-transcribe los últimos 8 s con whisper y los compara con el final del guion.
  4. Karaoke: líneas con el mismo inicio o superpuestas (señal de un signo suelto en el guion).
  5. Frames cada 2 s en <video>_frames/ para que los mires (subtítulos cortados, popups faltantes,
     restos de texto del original, CTA final presente).

Uso: python3 tools/qc_video.py ADS/<PRODUCTO>/<FECHA>/1.mp4 --voz work/<slug>/voz_final.wav \
        --guion work/<slug>/guion.txt --ass work/<slug>/karaoke.ass --idioma es
"""
import argparse
import difflib
import os
import re
import subprocess
import tempfile

from cargar_env import leer_texto
from media import ffmpeg, dur, info


def seg(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--voz"); ap.add_argument("--guion"); ap.add_argument("--ass")
    ap.add_argument("--idioma", default=None)
    ap.add_argument("--sin-frames", action="store_true")
    a = ap.parse_args()
    filas = []

    s = info(a.video)
    v = next((x for x in s if x["codec_type"] == "video"), {})
    au = next((x for x in s if x["codec_type"] == "audio"), {})
    vertical = v.get("width", 1) < v.get("height", 0)
    filas.append(("9:16 vertical", vertical, f"{v.get('width')}x{v.get('height')}"))
    filas.append(("códecs h264 + aac", v.get("codec_name") == "h264" and au.get("codec_name") == "aac",
                  f"{v.get('codec_name')} / {au.get('codec_name')}"))

    dv = dur(a.video)
    if a.voz:
        da = dur(a.voz)
        filas.append(("duración voz ≈ video (±1 s)", abs(dv - da) <= 1.0, f"voz {da:.2f}s · video {dv:.2f}s"))

    if a.guion:
        import whisper
        tmp = tempfile.mktemp(suffix=".wav")
        subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-ss", f"{max(0, dv - 8):.2f}", "-i", a.video,
                        "-vn", "-ac", "1", "-ar", "16000", tmp], check=True)
        oido = whisper.load_model("small").transcribe(tmp, language=a.idioma)["text"]
        norm = lambda t: re.sub(r"[^\w\s]", "", t.lower()).split()
        final_guion = norm(leer_texto(a.guion))[-8:]
        oido_n = norm(oido)
        ratio = difflib.SequenceMatcher(None, final_guion, oido_n[-len(final_guion):]).ratio()
        filas.append(("CTA entero al final", ratio >= 0.6, f"guion: …{' '.join(final_guion)} | audio: …{' '.join(oido_n[-8:])}"))

    if a.ass:
        lineas = [l for l in leer_texto(a.ass).splitlines() if l.startswith("Dialogue:")]
        tiempos = [(seg(l.split(",")[1]), seg(l.split(",")[2])) for l in lineas]
        malas = sum(1 for (s0, e0), (s1, _) in zip(tiempos, tiempos[1:]) if abs(s1 - s0) < 0.05 or e0 > s1 + 0.01)
        filas.append(("karaoke sin líneas duplicadas/superpuestas", malas == 0, f"{malas} problemas en {len(lineas)} líneas"))

    if not a.sin_frames:
        carpeta = os.path.splitext(a.video)[0] + "_frames"
        os.makedirs(carpeta, exist_ok=True)
        subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-i", a.video, "-vf", "fps=1/2,scale=360:-2",
                        os.path.join(carpeta, "f_%03d.jpg")], check=True)
        filas.append(("frames cada 2 s para revisar a ojo", True, carpeta))

    print(f"\nQC · {a.video}")
    for nombre, ok, det in filas:
        print(f"  [{'OK   ' if ok else 'FALLA'}] {nombre:45s} {det}")
    print("\nMirá los frames: subtítulos cortados en los bordes, dos líneas a la vez, restos del original, popups que faltan, CTA final.")


if __name__ == "__main__":
    main()
