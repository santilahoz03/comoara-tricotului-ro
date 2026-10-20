#!/usr/bin/env python3
"""Genera la voz en off de un guion, SIEMPRE a velocidad natural.
(Si después no calza con el video, usá tools/calzar_duracion.py: nunca se desacelera la voz.)

Motores (del más barato al más caro):
  edge        gratis, sin clave. No trunca textos largos. Default.
  gemini      cuota gratis diaria. Trunca EN SILENCIO textos de más de ~25 palabras:
              este script parte el guion en frases cortas y las concatena.
  elevenlabs  pago. Solo si querés voz premium o clonada (necesita el voice_id).

Uso:
  python3 tools/voz.py --motor edge --voz es-MX-DaliaNeural --texto guion.txt --salida voz.wav
  python3 tools/voz.py --motor gemini --voz Sulafat --texto guion.txt --salida voz.wav
  python3 tools/voz.py --motor elevenlabs --voz <VOICE_ID> --texto guion.txt --salida voz.wav

Voces edge-tts útiles: es-AR-ElenaNeural / es-AR-TomasNeural · es-MX-DaliaNeural / es-MX-JorgeNeural ·
en-US-JennyNeural / en-US-GuyNeural · it-IT-ElsaNeural / it-IT-DiegoNeural ·
pt-BR-FranciscaNeural / pt-BR-AntonioNeural · fr-FR-DeniseNeural / fr-FR-HenriNeural ·
ro-RO-AlinaNeural / ro-RO-EmilNeural.   Lista completa: edge-tts --list-voices
Voces Gemini: femeninas cálidas Sulafat, Aoede, Vindemiatrix · masculinas Orus, Achird (revisá el catálogo vigente).
"""
import argparse
import asyncio
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import wave

from cargar_env import clave, leer_texto
from media import ffmpeg, dur


def a_wav(origen, destino):
    subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-i", origen, "-ar", "44100", "-ac", "1", destino], check=True)


def edge(texto, voz, salida, rate):
    import edge_tts
    tmp = tempfile.mktemp(suffix=".mp3")
    asyncio.run(edge_tts.Communicate(texto, voz, rate=rate).save(tmp))
    a_wav(tmp, salida)


def frases(texto, max_palabras=25):
    """Parte el texto en trozos de <= max_palabras respetando el final de las frases."""
    oraciones = re.split(r"(?<=[.!?])\s+", texto.strip())
    trozos, actual = [], []
    for o in oraciones:
        palabras = o.split()
        if len(palabras) > max_palabras:            # oración larga: cortar en comas
            partes = re.split(r"(?<=,)\s+", o)
        else:
            partes = [o]
        for p in partes:
            pal = p.split()
            while len(pal) > max_palabras:               # sin comas: corte duro
                if actual:
                    trozos.append(" ".join(actual)); actual = []
                trozos.append(" ".join(pal[:max_palabras])); pal = pal[max_palabras:]
            if actual and len(actual) + len(pal) > max_palabras:
                trozos.append(" ".join(actual)); actual = []
            actual += pal
    if actual:
        trozos.append(" ".join(actual))
    return trozos


def gemini(texto, voz, salida):
    api_key = clave("GEMINI_API_KEY")
    modelo = os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"
    pcm = b""
    for i, trozo in enumerate(frases(texto)):
        cuerpo = {"contents": [{"parts": [{"text": trozo}]}],
                  "generationConfig": {"responseModalities": ["AUDIO"],
                                       "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voz}}}}}
        for intento in range(4):
            req = urllib.request.Request(url, data=json.dumps(cuerpo).encode(),
                                         headers={"Content-Type": "application/json", "x-goog-api-key": api_key})
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = json.load(r)
                break
            except urllib.error.HTTPError as e:
                if e.code == 429 and intento < 3:
                    time.sleep(5 * (intento + 1)); continue
                sys.exit(f"Gemini TTS falló ({e.code}). Si es cuota diaria, pasá a --motor edge ahora, no esperes.")
        parte = data["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
        pcm += base64.b64decode(parte)
        print(f"  trozo {i + 1}: {len(trozo.split())} palabras")
        time.sleep(1.5)
    tmp = tempfile.mktemp(suffix=".wav")
    with wave.open(tmp, "wb") as w:                     # Gemini devuelve PCM 16-bit 24 kHz mono
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm)
    a_wav(tmp, salida)


def elevenlabs(texto, voz, salida):
    api_key = clave("ELEVENLABS_API_KEY")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voz}?output_format=mp3_44100_128"
    cuerpo = {"text": texto, "model_id": os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2"),
              "voice_settings": {"stability": 0.45, "similarity_boost": 0.75,
                                 "style": 0.40, "use_speaker_boost": True}}
    req = urllib.request.Request(url, data=json.dumps(cuerpo).encode(),
                                 headers={"Content-Type": "application/json", "xi-api-key": api_key})
    tmp = tempfile.mktemp(suffix=".mp3")
    with urllib.request.urlopen(req, timeout=300) as r, open(tmp, "wb") as fh:
        fh.write(r.read())
    a_wav(tmp, salida)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--motor", choices=["edge", "gemini", "elevenlabs"], default="edge")
    ap.add_argument("--voz", required=True)
    ap.add_argument("--texto", required=True, help="archivo .txt con el guion (texto corrido, un narrador)")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--rate", default="+0%", help="solo edge: +0%% natural; solo valores POSITIVOS")
    a = ap.parse_args()

    texto = leer_texto(a.texto).strip()
    if re.search(r"\s[—–]\s|\s\.\.\.\s|\s…\s", texto):
        print("AVISO: el guion tiene guiones largos o puntos suspensivos sueltos. Cambialos por coma o punto: duplican subtítulos.")
    if a.rate.startswith("-"):
        sys.exit("No se desacelera la voz (suena a cámara lenta). Si la voz queda corta, se acelera el VIDEO.")

    if a.motor == "edge":
        edge(texto, a.voz, a.salida, a.rate)
    elif a.motor == "gemini":
        gemini(texto, a.voz, a.salida)
    else:
        elevenlabs(texto, a.voz, a.salida)
    print(f"{a.salida}: {dur(a.salida):.2f} s · {len(texto.split())} palabras")
    print("Verificá que no se cortó: re-transcribí el final con whisper (tools/qc_video.py lo hace).")


if __name__ == "__main__":
    main()
