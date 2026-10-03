#!/usr/bin/env python3
"""Calza la voz con el video SIN cámara lenta.

  Voz MÁS LARGA que el video  -> acelera la voz (atempo, hasta 1.4x suena natural).
                                 Si hiciera falta más de 1.4x: recortá el guion.
  Voz MÁS CORTA que el video  -> la voz queda igual y se acelera el VIDEO.
                                 Nunca se desacelera la voz.

El factor del video es  F = duración_voz / duración_video  (F < 1 acelera el video).
Si invertís la fracción, ffmpeg no avisa: el video sale corto y se come el CTA.
tools/componer.py ya aplica este factor solo; este script te lo muestra y deja la voz lista.

Uso: python3 tools/calzar_duracion.py voz.wav work/<slug>/clean.mp4 voz_final.wav [--max 1.4]
"""
import argparse
import shutil
import subprocess
import sys

from media import ffmpeg, dur


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("voz"); ap.add_argument("video"); ap.add_argument("salida")
    ap.add_argument("--max", type=float, default=1.4)
    a = ap.parse_args()

    dv, da = dur(a.video), dur(a.voz)
    print(f"video = {dv:.2f} s · voz natural = {da:.2f} s")
    if da > dv:
        tempo = da / dv
        if tempo > a.max:
            print(f"AVISO: la voz necesitaría {tempo:.2f}x. Tope {a.max}x: recortá el guion y volvé a generar.")
            tempo = a.max
        subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-i", a.voz, "-filter:a", f"atempo={tempo:.4f}", a.salida], check=True)
        print(f"voz acelerada {tempo:.2f}x -> {dur(a.salida):.2f} s")
    else:
        shutil.copyfile(a.voz, a.salida)
        print("voz sin cambios (más corta que el video: se acelera el VIDEO, no se frena la voz)")
    df = dur(a.salida)
    print(f"factor setpts del video F = {df / dv:.4f}  (F < 1 = video más rápido)")
    print("Después: karaoke sobre ESTE audio final (tools/karaoke_ass.py). Nunca reciclar tiempos de otra versión.")


if __name__ == "__main__":
    main()
