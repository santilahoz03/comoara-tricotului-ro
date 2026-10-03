#!/usr/bin/env python3
"""Carga las claves del archivo .env del proyecto (sin imprimirlas nunca).

Uso desde otro script de tools/:
    from cargar_env import clave
    api_key = clave("KIE_API_KEY")

Busca el .env subiendo desde la carpeta actual hasta la raíz.
Las variables que ya existan en el entorno tienen prioridad.

Windows: acepta .env guardado con el Bloc de notas (BOM, fin de línea CRLF) y, al importarse,
pone la consola en UTF-8 para que los prints con acentos/flechas no rompan con 'charmap'.
"""
import os
import sys
from pathlib import Path


def consola_utf8():
    """En Windows sin PYTHONUTF8=1 la salida a un pipe usa cp1252 y un «≈» o «→» rompe con
    UnicodeEncodeError 'charmap'. Pasamos stdout/stderr a UTF-8 (en Mac/Linux no cambia nada)."""
    for s in (sys.stdout, sys.stderr):
        try:
            if s is not None and (s.encoding or "").lower().replace("-", "") != "utf8":
                s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


consola_utf8()


def leer_texto(ruta):
    """Lee un .txt/.md/.json del usuario: UTF-8 con o sin BOM (Bloc de notas) y, si no es UTF-8,
    cp1252 (Windows viejo). Normaliza CRLF."""
    datos = Path(ruta).read_bytes()
    try:
        texto = datos.decode("utf-8-sig")
    except UnicodeDecodeError:
        texto = datos.decode("cp1252", errors="replace")
    return texto.replace("\r\n", "\n").replace("\r", "\n")


def _buscar_env():
    for carpeta in [Path.cwd(), *Path.cwd().parents]:
        candidato = carpeta / ".env"
        if candidato.is_file():
            return candidato
    return None


def cargar():
    ruta = _buscar_env()
    if not ruta:
        return None
    for linea in leer_texto(ruta).splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        nombre, valor = linea.split("=", 1)
        nombre = nombre.strip().removeprefix("export ").strip()
        valor = valor.strip()
        if valor.startswith("#"):              # línea vacía con comentario: KEY=   # comentario
            valor = ""
        if " #" in valor:                      # comentario al final de la línea
            valor = valor.split(" #", 1)[0].strip()
        valor = valor.strip('"').strip("'")
        if valor:
            os.environ.setdefault(nombre, valor)
    return ruta


def clave(nombre, obligatoria=True):
    cargar()
    valor = os.environ.get(nombre, "").strip()
    if not valor and obligatoria:
        sys.exit(f"Falta {nombre} en tu .env. Agregá la línea {nombre}=tu_clave y volvé a correr.")
    return valor


if __name__ == "__main__":
    # Chequeo rápido: dice qué claves hay cargadas, sin mostrar su valor.
    ruta = cargar()
    print(f".env encontrado: {ruta}" if ruta else "No encontré ningún .env")
    for n in ["KIE_API_KEY", "GEMINI_API_KEY", "ELEVENLABS_API_KEY", "VMAKE_AK", "VMAKE_SK"]:
        print(f"{n:20s} {'OK' if os.environ.get(n) else 'falta'}")
