#!/usr/bin/env python3
"""Helpers de ffmpeg compartidos por los scripts de tools/.

- ffmpeg(): devuelve el ffmpeg que tiene libass (el filtro `ass` de subtítulos).
  Orden: variable FFMPEG del .env > ffmpeg-full de Homebrew (Mac) > build de gyan.dev
  instalado con winget (Windows) > ffmpeg del PATH.
- dur(ruta): duración en segundos con ffprobe.
- tamano(ruta): (ancho, alto) del primer stream de video.

Correr solo para diagnosticar:  python3 tools/media.py   (Windows: python tools/media.py)
"""
import glob
import json
import os
import shutil
import subprocess
import sys

from cargar_env import cargar

WINDOWS = os.name == "nt"
EXE = ".exe" if WINDOWS else ""


def _candidatos():
    lista = [
        "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg",   # Mac Apple Silicon (brew install ffmpeg-full)
        "/usr/local/opt/ffmpeg-full/bin/ffmpeg",      # Mac Intel
    ]
    if WINDOWS:
        lad = os.environ.get("LOCALAPPDATA", "")
        if lad:
            # winget install Gyan.FFmpeg -> ...\WinGet\Packages\Gyan.FFmpeg_<id>\ffmpeg-<versión>-full_build\bin\ffmpeg.exe
            lista += sorted(glob.glob(os.path.join(lad, "Microsoft", "WinGet", "Packages", "Gyan.FFmpeg*",
                                                   "*", "bin", "ffmpeg.exe")), reverse=True)
            lista.append(os.path.join(lad, "Microsoft", "WinGet", "Links", "ffmpeg.exe"))
        for base in (os.environ.get("ProgramFiles", r"C:\Program Files"), "C:\\"):
            lista.append(os.path.join(base, "ffmpeg", "bin", "ffmpeg.exe"))     # instalación manual del zip
        lista.append(r"C:\ProgramData\chocolatey\bin\ffmpeg.exe")
    return lista


def _run_texto(cmd):
    # encoding explícito: en Windows el default es cp1252 y la salida de ffmpeg viene en UTF-8
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


def _tiene_ass(binario):
    try:
        out = _run_texto([binario, "-hide_banner", "-filters"])
    except OSError:
        return False
    return any(l.split()[1:2] == ["ass"] for l in out.splitlines() if len(l.split()) > 1)


def _normalizar(b):
    """FFMPEG= del .env puede venir con comillas, con barras de Windows o apuntando a la carpeta bin."""
    b = (b or "").strip().strip('"').strip("'")
    if b and os.path.isdir(b):
        b = os.path.join(b, "ffmpeg" + EXE)
    if b and WINDOWS and not b.lower().endswith(".exe") and os.path.exists(b + ".exe"):
        b += ".exe"
    return b


def ffmpeg():
    cargar()
    lista = [_normalizar(os.environ.get("FFMPEG", ""))] + _candidatos() + [shutil.which("ffmpeg") or ""]
    probados = []
    for b in lista:
        if b and os.path.exists(b):
            if _tiene_ass(b):
                # whisper y yt-dlp llaman a "ffmpeg" por nombre: si no está en el PATH (en Mac, ffmpeg-full
                # no se agrega solo; en Windows, winget a veces no refresca el PATH), lo sumamos para este proceso.
                carpeta = os.path.dirname(os.path.abspath(b))
                if carpeta not in os.environ.get("PATH", "").split(os.pathsep):
                    os.environ["PATH"] = carpeta + os.pathsep + os.environ.get("PATH", "")
                return b
            probados.append(b)
    extra = f" Probé sin libass: {', '.join(probados)}." if probados else ""
    sys.exit("No encontré un ffmpeg con libass (filtro 'ass')." + extra +
             " Mac: brew install ffmpeg-full. Windows: winget install Gyan.FFmpeg (el build 'full' de gyan.dev; "
             "después cerrá y abrí Claude Code). "
             "Si igual no lo encuentra, poné FFMPEG=<ruta al ffmpeg o ffmpeg.exe> en tu .env.")


def ffprobe():
    b = ffmpeg()
    for nombre in ("ffprobe", "ffprobe.exe"):                  # .exe = Windows
        vecino = os.path.join(os.path.dirname(b), nombre)
        if os.path.exists(vecino):
            return vecino
    return shutil.which("ffprobe") or "ffprobe"


def dur(ruta):
    out = subprocess.check_output([ffprobe(), "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", ruta], text=True, encoding="utf-8", errors="replace").strip()
    return float(out)


def info(ruta):
    out = subprocess.check_output([ffprobe(), "-v", "error", "-show_entries",
                                   "stream=codec_type,codec_name,width,height", "-of", "json", ruta],
                                  text=True, encoding="utf-8", errors="replace")
    return json.loads(out).get("streams", [])


def tamano(ruta):
    for s in info(ruta):
        if s.get("codec_type") == "video":
            return int(s["width"]), int(s["height"])
    return None


if __name__ == "__main__":
    b = ffmpeg()
    print("ffmpeg con libass:", b)
    print("ffprobe:", ffprobe())
