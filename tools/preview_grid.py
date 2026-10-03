#!/usr/bin/env python3
"""Arma la página de previsualización de una tanda: grilla de <video> (y de imágenes) agrupada por lote.
Nunca revises una tanda como lista de links: en la grilla ves los errores juntos.

Uso:
  python3 tools/preview_grid.py ADS/<PRODUCTO>/<FECHA> --titulo "<PRODUCTO> · tanda <FECHA> (<MERCADO>)"
Genera ADS/<PRODUCTO>/<FECHA>/preview.html. Cada subcarpeta (ej. EN/, IT/, microvariaciones/) sale como un lote aparte.
Para verla:  cd ADS/<PRODUCTO>/<FECHA> && python3 -m http.server 8743   ->  http://127.0.0.1:8743/preview.html
(o abrí el archivo directo en el navegador: Mac `open preview.html` · Windows `cmd //c start "" preview.html`;
en Windows el servidor es `python -m http.server 8743`). Es local: no se publica en ningún lado.
Si existe notas.txt en la carpeta, cada línea "1.mp4 | texto" se muestra debajo del video.
"""
import argparse
import html
import os
import subprocess
from pathlib import Path

from cargar_env import leer_texto   # además pone la consola en UTF-8 (Windows)

VID = {".mp4", ".mov", ".webm"}
IMG = {".png", ".jpg", ".jpeg", ".webp"}


def _ffprobe():
    try:                                  # el mismo ffprobe que encuentran los otros scripts (ffmpeg-full incluido)
        from media import ffprobe
        return ffprobe()
    except BaseException:
        return "ffprobe"


FFPROBE = _ffprobe()


def duracion(p):
    try:
        return float(subprocess.check_output([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                                              "-of", "csv=p=0", str(p)], text=True,
                                             encoding="utf-8", errors="replace").strip())
    except Exception:
        return None


def orden(p):
    return (0, int(p.stem)) if p.stem.isdigit() else (1, p.stem)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta"); ap.add_argument("--titulo", default=None)
    a = ap.parse_args()
    raiz = Path(a.carpeta)
    notas = {}
    if (raiz / "notas.txt").exists():
        for l in leer_texto(raiz / "notas.txt").splitlines():
            if "|" in l:
                k, v = l.split("|", 1); notas[k.strip()] = v.strip()

    lotes = {}
    for p in sorted(raiz.rglob("*")):
        if p.suffix.lower() in VID | IMG and "_frames" not in str(p.parent) and not p.name.startswith("."):
            lote = p.parent.relative_to(raiz).as_posix() if p.parent != raiz else "Tanda principal"
            lotes.setdefault(lote, []).append(p)

    tarjetas, total = [], 0
    for lote, archivos in lotes.items():
        tarjetas.append(f'<div class="batch">{html.escape(lote)} · {len(archivos)} piezas</div>')
        for p in sorted(archivos, key=orden):
            rel_posix = p.relative_to(raiz).as_posix()       # "EN/1.mp4" también en Windows (no "EN\\1.mp4")
            rel = html.escape(rel_posix)
            nota = html.escape(notas.get(rel_posix, notas.get(p.name, "")))
            if p.suffix.lower() in VID:
                d = duracion(p)
                meta = f"{nota} · {d:.0f}s" if d else nota
                media = f'<video controls preload="metadata" playsinline src="{rel}"></video>'
            else:
                meta, media = nota, f'<img src="{rel}" alt="{rel}">'
            tarjetas.append(f'<div class="card"><h3>{html.escape(p.stem)}</h3><div class="meta">{meta}</div>{media}</div>')
            total += 1

    titulo = html.escape(a.titulo or f"{raiz.parent.name} · {raiz.name}")
    pagina = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<style>
  html, body {{ background:#1a1a1a; color:#eee; }}
  body {{ font-family:-apple-system, Segoe UI, Roboto, sans-serif; margin:0; padding:24px 16px; }}
  h1 {{ font-size:20px; margin:0 0 4px; }}
  p.sub {{ color:#999; margin:0 0 24px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(240px, 1fr)); gap:20px; }}
  .card {{ background:#242424; border-radius:10px; padding:12px; }}
  .card h3 {{ margin:0 0 6px; font-size:15px; }}
  .card .meta {{ color:#999; font-size:12px; margin-bottom:8px; min-height:14px; }}
  video, img {{ width:100%; border-radius:6px; background:#000; max-height:480px; object-fit:contain; display:block; }}
  .batch {{ grid-column:1 / -1; margin-top:12px; font-size:13px; text-transform:uppercase; letter-spacing:.5px;
           color:#888; border-top:1px solid #333; padding-top:16px; }}
</style></head>
<body>
<h1>{titulo}</h1>
<p class="sub">{total} piezas · preview local, no está publicado en ningún lado.</p>
<div class="grid">
{chr(10).join(tarjetas)}
</div>
</body></html>
"""
    out = raiz / "preview.html"
    out.write_text(pagina, encoding="utf-8")
    print(f"{out} ({total} piezas)")


if __name__ == "__main__":
    main()
