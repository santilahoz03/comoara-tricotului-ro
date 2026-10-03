#!/usr/bin/env python3
"""Genera un popup (pastilla redondeada con texto) como PNG transparente, para superponerlo
con tools/componer.py. Es la opción B: con /hyperframes los popups salen mejor (emojis a color,
animación de entrada). Usá esta cuando quieras algo rápido y sin animación.

Uso:
  python3 tools/popup_png.py --texto "50 escarpines en un finde" --fondo "#FFD400" --color "#111111" \
      --ancho 560 --alto 110 --salida work/<slug>/pop1.png
  python3 tools/popup_png.py --texto "TOCÁ «MÁS INFORMACIÓN» ▼▼" --fondo "#000000B0" --color "#FFFFFF" \
      --ancho 640 --alto 150 --salida work/<slug>/cta.png
Opciones: --radio (por defecto alto/2 = pastilla) · --fuente ruta.ttf · multi-línea con \\n en el texto.
Si las flechas ▼ salen como cuadraditos, pasá una fuente con esos símbolos
(Mac: --fuente "/Library/Fonts/Arial Unicode.ttf" · Windows: --fuente "C:/Windows/Fonts/seguisym.ttf").
Medí ancho/alto/posición sobre un frame del ORIGINAL (Gemini suele dar la caja del texto, no de la pastilla).
Requiere: pip install pillow
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFont

import cargar_env  # noqa: F401  (pone la consola en UTF-8 en Windows)

FUENTES = [
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    os.path.join(os.environ.get("WINDIR", "C:/Windows"), "Fonts", "ariblk.ttf"),
    os.path.join(os.environ.get("WINDIR", "C:/Windows"), "Fonts", "arialbd.ttf"),
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def color(hexa):
    h = hexa.lstrip("#")
    if len(h) == 6:
        h += "FF"
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4, 6))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--texto", required=True)
    ap.add_argument("--fondo", default="#FFD400")
    ap.add_argument("--color", default="#111111")
    ap.add_argument("--ancho", type=int, default=560)
    ap.add_argument("--alto", type=int, default=110)
    ap.add_argument("--radio", type=int, default=None)
    ap.add_argument("--fuente", default=None)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    ruta = a.fuente or next((f for f in FUENTES if os.path.exists(f)), None)
    lineas = a.texto.replace("\\n", "\n").split("\n")
    img = Image.new("RGBA", (a.ancho, a.alto), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    radio = a.radio if a.radio is not None else a.alto // (2 * max(1, len(lineas)))
    d.rounded_rectangle([0, 0, a.ancho - 1, a.alto - 1], radius=radio, fill=color(a.fondo))

    # la fuente se achica hasta que todas las líneas entren con margen
    tam = int(a.alto / len(lineas) * 0.62)
    while tam > 10:
        f = ImageFont.truetype(ruta, tam) if ruta else ImageFont.load_default()
        anchos = [d.textbbox((0, 0), l, font=f)[2] for l in lineas]
        if max(anchos) <= a.ancho * 0.88:
            break
        tam -= 2
    alto_linea = a.alto / len(lineas)
    for i, l in enumerate(lineas):
        d.text((a.ancho / 2, alto_linea * (i + 0.5)), l, font=f, fill=color(a.color), anchor="mm")
    img.save(a.salida)
    print(a.salida, f"{a.ancho}x{a.alto}", f"fuente {tam}px")


if __name__ == "__main__":
    main()
