#!/usr/bin/env python3
"""Detecta TODO el texto en pantalla de un video (subtítulos, popups, CTA, cartel final,
marcas de agua, insignias) con su tiempo, posición y colores.

NO sirve para tapar nada (eso lo hace Vmake). Sirve para saber QUÉ decía cada texto y CUÁNDO,
así lo recreás traducido.

Uso:     python3 tools/detectar_textos_gemini.py work/<slug>/original.mp4
Salida:  work/<slug>/original.detecciones.json
Requiere: pip install google-genai   ·   GEMINI_API_KEY en .env
Modelo:  GEMINI_MODEL en .env (por defecto gemini-2.5-flash; usá el Flash vigente más barato).
"""
import json
import os
import sys
import time

from cargar_env import clave

PROMPT = """Analizá este video vertical cuadro por cuadro. Listá TODOS los elementos de texto
superpuestos: subtítulos, popups decorativos (frases en cajas de color), CTA, cartel final,
marcas de agua, insignias circulares en las esquinas. NO incluyas texto que es parte física
del producto filmado (portadas, páginas, cajas). Si un mismo popup aparece varias veces,
listá cada aparición por separado. Devolvé SOLO JSON:
{"video_duration_s": float,
 "detections": [{"type": "subtitle|popup_decorative|popup_cta|endcard|watermark|badge",
   "t_start_s": float, "t_end_s": float,
   "bbox": {"x": int, "y": int, "w": int, "h": int},
   "text_original": str, "language": str,
   "bg_color_hex": str, "text_color_hex": str, "shape": str}]}"""


def main(path):
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=clave("GEMINI_API_KEY"))
    modelo = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    f = client.files.upload(file=path)
    while f.state.name == "PROCESSING":
        time.sleep(3)
        f = client.files.get(name=f.name)
    r = client.models.generate_content(
        model=modelo, contents=[f, PROMPT],
        config=types.GenerateContentConfig(response_mime_type="application/json"))
    data = json.loads(r.text)
    dur = data.get("video_duration_s") or 0
    for d in data.get("detections", []):
        if dur and d.get("t_end_s", 0) > dur:        # Gemini a veces se pasa del final
            d["t_end_s"] = dur
    out = os.path.splitext(path)[0] + ".detecciones.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    tipos = {}
    for d in data.get("detections", []):
        tipos[d.get("type")] = tipos.get(d.get("type"), 0) + 1
    print(out, tipos)
    print("Ojo: Gemini se pierde insignias y el CTA final (lo reporta cortito). Revisá frames cada 2 s igual.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
