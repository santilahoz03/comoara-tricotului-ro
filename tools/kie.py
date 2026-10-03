#!/usr/bin/env python3
"""Generación en kie.ai (imágenes y clips de video), siempre en el tier más barato que cumpla.

  saldo                      -> créditos disponibles (anotalo antes y después de cada tanda: así medís el costo REAL)
  imagen                     -> imagen 1K 9:16 (GPT Image 2). Con --ref URL(s): image-to-image sobre una referencia
                                (para iterar un ganador o para que el producto sea el real, no uno inventado)
  video                      -> clip Veo (modelo barato, 720p, 9:16 explícito, duración mínima útil)

Uso:
  python3 tools/kie.py saldo
  python3 tools/kie.py imagen --prompt "..." --salida work/x/img.png
  python3 tools/kie.py imagen --prompt "Same composition... change only: ..." --ref https://.../ganador.png --salida work/x/v1.png
  python3 tools/kie.py video --prompt "..." --salida work/x/clip.mp4 [--duracion 4] [--modelo veo3_lite] [--img URL]

Referencias de costo MEDIDAS (verificá las tuyas con `saldo`, los precios de tabla fallan hasta 10x):
  imagen 1K ≈ USD 0,06 · clip Veo barato 8 s 720p ≈ USD 3.
Los modelos cambian: antes de una tanda grande, revisá el catálogo de kie.ai por un tier más barato.
Los archivos de kie viven ~14 días: descargá siempre el resultado (este script lo hace).
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from cargar_env import clave

BASE = "https://api.kie.ai/api/v1"


def llamar(metodo, ruta, cuerpo=None):
    req = urllib.request.Request(BASE + ruta, method=metodo,
                                 data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
                                 headers={"Authorization": f"Bearer {clave('KIE_API_KEY')}",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"kie.ai respondió HTTP {e.code} ({e.reason}). 401 = revisá la KIE_API_KEY del .env · "
                 "402 = suele ser saldo insuficiente · 429 = demasiados pedidos juntos, esperá y reintentá.")
    if data.get("code") not in (200, None):
        sys.exit(f"kie.ai respondió {data.get('code')}: {data.get('msg')}")
    return data.get("data")


def bajar(url, salida):
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, salida)
    print(f"Listo: {salida}")


def buscar_urls(obj):
    if isinstance(obj, str):
        try:
            return buscar_urls(json.loads(obj))
        except (ValueError, TypeError):
            return [obj] if obj.startswith("http") else []
    if isinstance(obj, dict):
        for k in ("resultUrls", "result_urls"):
            if obj.get(k):
                return list(obj[k])
        return [u for v in obj.values() for u in buscar_urls(v)]
    if isinstance(obj, list):
        return [u for v in obj for u in buscar_urls(v)]
    return []


def imagen(a):
    modelo = "gpt-image-2-image-to-image" if a.ref else "gpt-image-2-text-to-image"
    entrada = {"prompt": a.prompt, "aspect_ratio": a.aspecto, "resolution": "1K"}
    if a.ref:
        entrada["input_urls"] = a.ref
    tid = llamar("POST", "/jobs/createTask", {"model": modelo, "input": entrada})["taskId"]
    print(f"tarea {tid} ({modelo}, 1K, {a.aspecto})")
    for _ in range(150):
        d = llamar("GET", f"/jobs/recordInfo?taskId={tid}") or {}
        if d.get("state") == "success":
            return bajar(buscar_urls(d.get("resultJson"))[0], a.salida)
        if d.get("state") == "fail":
            sys.exit(f"Falló: {d.get('failMsg')}")
        time.sleep(6)
    sys.exit("Timeout esperando la imagen.")


def video(a):
    cuerpo = {"prompt": a.prompt, "model": a.modelo, "aspect_ratio": "9:16",
              "resolution": "720p", "duration": a.duracion, "enableTranslation": False}
    if a.img:
        cuerpo["imageUrls"] = a.img
        cuerpo["generationType"] = "REFERENCE_2_VIDEO"
    tid = llamar("POST", "/veo/generate", cuerpo)["taskId"]
    print(f"tarea {tid} ({a.modelo}, 720p, 9:16, {a.duracion}s)")
    for _ in range(200):
        d = llamar("GET", f"/veo/record-info?taskId={tid}") or {}
        flag = d.get("successFlag")
        if flag == 1:
            return bajar(buscar_urls(d.get("response") or d)[0], a.salida)
        if flag in (2, 3):
            sys.exit(f"Falló: {d.get('errorMessage') or d}")
        time.sleep(10)
    sys.exit("Timeout esperando el clip.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("saldo")
    i = sub.add_parser("imagen")
    i.add_argument("--prompt", required=True); i.add_argument("--salida", required=True)
    i.add_argument("--ref", nargs="*", default=None); i.add_argument("--aspecto", default="9:16")
    v = sub.add_parser("video")
    v.add_argument("--prompt", required=True); v.add_argument("--salida", required=True)
    v.add_argument("--modelo", default="veo3_lite"); v.add_argument("--duracion", type=int, default=4)
    v.add_argument("--img", nargs="*", default=None)
    a = ap.parse_args()
    if a.cmd == "saldo":
        print("créditos:", llamar("GET", "/chat/credit"))
    elif a.cmd == "imagen":
        imagen(a)
    else:
        video(a)


if __name__ == "__main__":
    main()
