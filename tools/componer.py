#!/usr/bin/env python3
"""Montaje final con ffmpeg (opción B; la opción A es /hyperframes).

Hace, en un solo render:
  video limpio  -> acelerado/estirado con F = (duración_voz + cola) / duración_video, recortado a 9:16 720x1280
  + popups PNG  -> cada uno en su posición y tramo de tiempo (popups.json)
  + karaoke ASS -> subtítulos por palabra
  + voz final + música a -22 dB (volumen 0.08) con fade in/out
  + efectos: swell al inicio y un impacto ~3 s antes del final (opcionales)
Export: 720x1280, H.264 crf 20, AAC 160k, 30 fps.

Uso típico (réplica / doblaje):
  python3 tools/componer.py --video work/<slug>/clean.mp4 --voz work/<slug>/voz_final.wav \
     --ass work/<slug>/karaoke.ass --musica ADS/_assets/musica/inspirador.mp3 \
     --popups work/<slug>/popups.json --sfx-inicio ADS/_assets/sfx/swell.wav --sfx-cta ADS/_assets/sfx/impacto.wav \
     --salida ADS/<PRODUCTO>/<FECHA>/1.mp4

Microvariación (el audio del ganador ya trae música): --musica none --factor 1
Video multi-clip ya armado a la duración del audio: --factor 1

popups.json = [{"png": "work/<slug>/pop1.png", "x": 80, "y": 220, "t0": 1.2, "t1": 3.8}, ...]
  Tiempos en el video FINAL, sincronizados con la VOZ NUEVA (fin de la frase en el karaoke),
  no el tiempo viejo multiplicado por el factor.
"""
import argparse
import json
import os
import shutil
import subprocess
import tempfile

from cargar_env import leer_texto
from media import ffmpeg, dur

# Windows: el ffmpeg de gyan.dev a veces no encuentra las fuentes del sistema (fontconfig sin config) y los
# subtítulos salen invisibles o con otra letra. Copiamos las fuentes típicas a la carpeta temporal y se las
# pasamos con una ruta RELATIVA (fontsdir=fuentes): nada de "C:\..." dentro del filtro, que rompe el filtergraph.
FUENTES_WINDOWS = ["ariblk.ttf", "arialbd.ttf", "arial.ttf", "impact.ttf", "seguisym.ttf", "seguiemj.ttf"]


def _fuentes_windows(tmp):
    if os.name != "nt":
        return False
    origen = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
    destino = os.path.join(tmp, "fuentes")
    os.makedirs(destino, exist_ok=True)
    copiadas = 0
    for f in FUENTES_WINDOWS:
        if os.path.exists(os.path.join(origen, f)):
            shutil.copyfile(os.path.join(origen, f), os.path.join(destino, f))
            copiadas += 1
    return copiadas > 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--voz", required=True)
    ap.add_argument("--ass", default=None)
    ap.add_argument("--musica", default="none")
    ap.add_argument("--popups", default=None)
    ap.add_argument("--sfx-inicio", default=None)
    ap.add_argument("--sfx-cta", default=None)
    ap.add_argument("--factor", default="auto", help="auto = (voz+cola)/video · o un número")
    ap.add_argument("--cola", type=float, default=0.4, help="segundos de video después de la última palabra")
    ap.add_argument("--vol-musica", type=float, default=0.20, help="volumen música 0-1 (0.20 = fondo suave)")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    ab = lambda p: os.path.abspath(p) if p and p != "none" else None
    video, voz, musica = ab(a.video), ab(a.voz), ab(a.musica)
    dv, da = dur(video), dur(voz)
    total = da + a.cola
    F = total / dv if a.factor == "auto" else float(a.factor)
    print(f"video={dv:.2f}s voz={da:.2f}s factor F={F:.4f} final≈{total:.2f}s")

    entradas = ["-i", video, "-i", voz]
    idx = 2
    filtros = [f"[0:v]setpts={F:.5f}*PTS,scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1,fps=30[v0]"]
    vult = "v0"

    popups = json.loads(leer_texto(a.popups)) if a.popups else []
    for k, p in enumerate(popups):
        entradas += ["-loop", "1", "-i", ab(p["png"])]
        nuevo = f"v{k + 1}"
        filtros.append(f"[{vult}][{idx}:v]overlay={int(p['x'])}:{int(p['y'])}:shortest=1:"
                       f"enable='between(t,{float(p['t0']):.2f},{float(p['t1']):.2f})'[{nuevo}]")
        vult, idx = nuevo, idx + 1

    tmp = tempfile.mkdtemp()
    if a.ass:
        # ffmpeg corre con cwd=tmp y el .ass se llama k.ass: la ruta dentro del filtro no tiene espacios,
        # acentos ni "C:" (en Windows los ":" y "\\" de una ruta absoluta rompen el filtergraph).
        shutil.copyfile(a.ass, os.path.join(tmp, "k.ass"))
        extra = ":fontsdir=fuentes" if _fuentes_windows(tmp) else ""
        filtros.append(f"[{vult}]ass=k.ass{extra}[vout]")
    else:
        filtros.append(f"[{vult}]null[vout]")

    mezcla = ["[vo]"]
    filtros.append("[1:a]aresample=48000,aformat=channel_layouts=stereo[vo]")
    if musica:
        entradas += ["-stream_loop", "-1", "-i", musica]
        filtros.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,volume={a.vol_musica:.2f},"
                       f"afade=t=in:d=1.5,afade=t=out:st={max(0, total - 1.8):.2f}:d=1.5[mu]")
        mezcla.append("[mu]"); idx += 1
    if a.sfx_inicio:
        entradas += ["-i", ab(a.sfx_inicio)]
        filtros.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,volume=0.5[si]")
        mezcla.append("[si]"); idx += 1
    if a.sfx_cta:
        ms = int(max(0, total - 3.0) * 1000)
        entradas += ["-i", ab(a.sfx_cta)]
        filtros.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms},volume=0.6[sc]")
        mezcla.append("[sc]"); idx += 1
    filtros.append(f"{''.join(mezcla)}amix=inputs={len(mezcla)}:duration=first:normalize=0,apad[a]")

    salida = ab(a.salida)
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    cmd = [ffmpeg(), "-y", "-loglevel", "error", *entradas, "-filter_complex", ";".join(filtros),
           "-map", "[vout]", "-map", "[a]", "-t", f"{total:.3f}",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", salida]
    subprocess.run(cmd, check=True, cwd=tmp)
    df = dur(salida)
    estado = "OK" if abs(df - total) <= 1.0 else "REVISAR: la duración no coincide con la voz (bug de timing)"
    print(f"{salida}: {df:.2f}s (esperado ~{total:.2f}s) {estado}")


if __name__ == "__main__":
    main()
