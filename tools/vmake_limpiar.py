#!/usr/bin/env python3
"""Limpia un video ajeno con Vmake: devuelve el video sin subtítulos, popups, cartel final ni marcas de agua,
con el fondo reconstruido. ~25 s de proceso por cada 12 s de video (medido el 2026-10-03).

ADAPTADO al SDK 2.0.1 de Vmake (paquete `action_api_sdk`, tareas por `material_id`). El original del kit está en
tools/vmake_limpiar.py.orig-kit (esperaba el SDK viejo con SkillClient y la tarea `videoscreenclear`).

Requisitos:
  1. SDK 2.0.1 instalado en tools/vmake/.venv (wheel en tools/vmake/action_api_sdk-2.0.1-py3-none-any.whl):
       python3 -m venv tools/vmake/.venv && tools/vmake/.venv/bin/python -m pip install tools/vmake/action_api_sdk-2.0.1-py3-none-any.whl
  2. En .env: VMAKE_AK=... y VMAKE_SK=... (el par Access Key / Secret Key del panel de Vmake).

Uso:
  python3 tools/vmake_limpiar.py work/<slug>/original.mp4 work/<slug>/clean.mp4              (muestra el costo y NO gasta)
  python3 tools/vmake_limpiar.py work/<slug>/original.mp4 work/<slug>/clean.mp4 --confirmar  (limpia y descuenta créditos)
  python3 tools/vmake_limpiar.py --probar      (verifica claves, SDK y la tarea; no gasta)

COSTO: esta tarea CONSUME CRÉDITOS (el kit decía 0 y ya no es así). Medido: 26 créditos por 12,4 s ≈ 2,1 créditos por
segundo. Antes de cada video mostrá el costo estimado y esperá el OK del usuario. Antes de lotes de más de 5 videos,
mirá el saldo en el panel de Vmake.

GUARDÁ SIEMPRE el clean.mp4: es tu biblioteca de B-roll para iterar sin volver a pagar.

REGLA DURA: este script usa SOLO la tarea SKM0003 («Smart - Video Smart Removal», que internamente es
`videoscreenclear`). No se cambia por otra tarea de Vmake ni se reemplaza por la web de Vmake. Si falla, se para
y se muestra el error textual.
"""
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

from cargar_env import clave

AQUI = Path(__file__).resolve().parent
TAREA = "SKM0003"                                # NO CAMBIAR
NOMBRE_TAREA = "Smart - Video Smart Removal"     # el catálogo tiene que seguir diciendo esto para esa tarea
CREDITOS_POR_SEGUNDO = 2.1                       # medido 2026-10-03: 26 créditos por 12,4 s
USD_POR_CREDITO = 29.99 / 4500                   # referencia: plan de USD 29,99 con 4.500 créditos por mes


def cli_sdk():
    base = AQUI / "vmake" / ".venv"
    for r in (base / "bin" / "action-api-sdk", base / "Scripts" / "action-api-sdk.exe"):
        if r.exists():
            return str(r)
    sys.exit("No encuentro el SDK de Vmake en tools/vmake/.venv. Instalalo con:\n"
             "  python3 -m venv tools/vmake/.venv && tools/vmake/.venv/bin/python -m pip install "
             "tools/vmake/action_api_sdk-2.0.1-py3-none-any.whl\n"
             "(Windows: python -m venv tools\\vmake\\.venv y tools\\vmake\\.venv\\Scripts\\python.exe -m pip install ...)")


def entorno():
    env = dict(os.environ)
    env["MT_AK"] = clave("VMAKE_AK")
    env["MT_SK"] = clave("VMAKE_SK")
    env["PYTHONUTF8"] = "1"
    env["PYTHONWARNINGS"] = "ignore"
    return env


def correr(args):
    """Corre el CLI del SDK y devuelve el JSON que imprime. Si falla, muestra el error textual y corta."""
    p = subprocess.run([cli_sdk()] + args, capture_output=True, text=True, env=entorno())
    texto = p.stdout.strip()
    try:
        datos = json.loads(texto)
    except ValueError:
        datos = None
    if p.returncode != 0 or datos is None:
        err = (p.stderr or "").strip().splitlines()
        err = [l for l in err if "Warning" not in l and "warnings.warn" not in l]
        sys.exit("Vmake falló. Error textual:\n" + ("\n".join(err[-8:]) or texto[:1500]) +
                 "\nNo pruebes otra tarea de Vmake ni la web: pasale este error tal cual al mentor.")
    return datos


def verificar_tarea():
    """Chequea que SKM0003 siga siendo la tarea de limpieza (si Vmake cambia el catálogo, frena antes de gastar)."""
    cat = correr(["catalog", "--media-type", "video"])
    for t in cat.get("tasks", []):
        if t.get("material_id") == TAREA:
            if t.get("name") != NOMBRE_TAREA:
                sys.exit(f"El catálogo de Vmake cambió: {TAREA} ahora se llama «{t.get('name')}» "
                         f"(esperaba «{NOMBRE_TAREA}»). No gasto nada: avisale al mentor.")
            return
    sys.exit(f"La tarea {TAREA} ya no está en el catálogo de Vmake. No gasto nada: avisale al mentor.")


def duracion(ruta):
    ff = os.environ.get("FFPROBE") or "ffprobe"
    for cand in (ff, "/opt/homebrew/opt/ffmpeg-full/bin/ffprobe", "/opt/homebrew/bin/ffprobe"):
        try:
            out = subprocess.run([cand, "-v", "error", "-show_entries", "format=duration",
                                  "-of", "default=nw=1:nk=1", str(ruta)], capture_output=True, text=True)
            if out.returncode == 0 and out.stdout.strip():
                return float(out.stdout.strip())
        except FileNotFoundError:
            continue
    return None


def urls(obj):
    """Busca URLs de video en cualquier parte de la respuesta."""
    if isinstance(obj, str):
        return [obj] if obj.startswith("http") and ".mp4" in obj.lower() else []
    if isinstance(obj, dict):
        return [u for v in obj.values() for u in urls(v)]
    if isinstance(obj, list):
        return [u for v in obj for u in urls(v)]
    return []


def main():
    args = [a for a in sys.argv[1:] if a != "--confirmar"]
    confirmar = "--confirmar" in sys.argv[1:]
    if args == ["--probar"]:
        entorno()                                  # valida que estén VMAKE_AK y VMAKE_SK en el .env
        verificar_tarea()
        print(f"SDK y claves OK: Vmake respondió y {TAREA} («{NOMBRE_TAREA}») sigue disponible. "
              "No se ejecutó ninguna tarea ni se gastó nada.")
        return
    if len(args) != 2:
        sys.exit(__doc__)
    entrada, salida = args
    if not Path(entrada).exists():
        sys.exit(f"No encuentro el video de entrada: {entrada}")
    seg = duracion(entrada)
    if seg is None:
        print("No pude medir la duración del video (falta ffprobe): no puedo estimar el costo.")
    else:
        cred = seg * CREDITOS_POR_SEGUNDO
        print(f"Video: {seg:.1f} s · costo estimado ≈ {cred:.0f} créditos de Vmake "
              f"(≈ USD {cred * USD_POR_CREDITO:.2f}; referencia: ~{CREDITOS_POR_SEGUNDO} créditos por segundo).")
    if not confirmar:
        print("No gasté nada. Si el usuario está de acuerdo con el costo, repetí el comando agregando --confirmar.")
        return
    verificar_tarea()
    print("Subiendo a Vmake y esperando el resultado (puede tardar unos minutos)...")
    res = correr(["run-task", "--task", TAREA, "--input", str(entrada)])
    encontradas = urls(res)
    if not encontradas:
        print(json.dumps(res, indent=2, ensure_ascii=False)[:2000])
        sys.exit("Vmake no devolvió un video. Mirá la respuesta de arriba (cuota, formato o error).")
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(encontradas[0], salida)
    print(f"Listo: {salida} ({Path(salida).stat().st_size // 1024} KB). Anotá cuántos créditos descontó en tu panel de Vmake.")


if __name__ == "__main__":
    main()
