#!/usr/bin/env python3
"""
configurar_git_bash.py — SOLO Windows. Plan B si, después de instalar Git y reiniciar la app de Claude,
Claude Code sigue corriendo los comandos en PowerShell en vez de Git Bash.

Qué hace: busca bash.exe de Git for Windows y lo anota en %USERPROFILE%\\.claude\\settings.json como
"env": {"CLAUDE_CODE_GIT_BASH_PATH": "C:\\\\Program Files\\\\Git\\\\bin\\\\bash.exe"}
sin pisar nada de lo que ya tenga ese archivo (hace una copia de respaldo antes).
Después hay que CERRAR y volver a abrir la app de Claude.

Uso (desde PowerShell o desde la terminal que tenga Claude en ese momento):
    python "%USERPROFILE%\\ZEA-kits\\kit-00-configuracion-inicial\\scripts\\configurar_git_bash.py"
    python configurar_git_bash.py --mostrar          # solo muestra qué haría, no escribe nada
    python configurar_git_bash.py --ruta "D:\\Git\\bin\\bash.exe"   # si Git está en otro lado
"""
import argparse
import datetime
import json
import os
import pathlib
import platform
import shutil
import sys

CLAVE = "CLAUDE_CODE_GIT_BASH_PATH"


def buscar_bash():
    cands = []
    for var in ("ProgramFiles", "ProgramFiles(x86)", "ProgramW6432"):
        base = os.environ.get(var)
        if base:
            cands.append(os.path.join(base, "Git", "bin", "bash.exe"))
    local = os.environ.get("LOCALAPPDATA")
    if local:
        cands.append(os.path.join(local, "Programs", "Git", "bin", "bash.exe"))
    git = shutil.which("git")
    if git:  # ...\Git\cmd\git.exe → ...\Git\bin\bash.exe
        cands.append(os.path.join(os.path.dirname(os.path.dirname(git)), "bin", "bash.exe"))
    for c in cands:
        if os.path.isfile(c):
            return c
    return None


def main():
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="Anota Git Bash en settings.json de Claude Code (Windows)")
    ap.add_argument("--ruta", help="ruta a bash.exe si no está en el lugar de siempre")
    ap.add_argument("--mostrar", action="store_true", help="no escribe: solo muestra el resultado")
    args = ap.parse_args()

    if platform.system() != "Windows" and not args.ruta:
        print("Este script es solo para Windows. En Mac/Linux no hace falta.")
        return 0

    bash = args.ruta or buscar_bash()
    if not bash or not os.path.isfile(bash):
        print("No encontré bash.exe de Git for Windows.")
        print("Arreglo: winget install -e --id Git.Git (o git-scm.com), cerrá y abrí la app de Claude.")
        print("Si Git está en otra carpeta, corré de nuevo con --ruta \"<carpeta de Git>\\bin\\bash.exe\".")
        return 1

    carpeta = pathlib.Path.home() / ".claude"
    archivo = carpeta / "settings.json"
    datos = {}
    if archivo.exists():
        texto = archivo.read_text(encoding="utf-8-sig")
        if texto.strip():
            try:
                datos = json.loads(texto)
            except json.JSONDecodeError as e:
                print(f"{archivo} no es JSON válido (línea {e.lineno}). No lo toco.")
                print("Arreglo: abrilo con el Bloc de notas, corregilo o pasáselo a tu mentor.")
                return 1
        if not isinstance(datos, dict):
            print(f"{archivo} no tiene el formato esperado (no es un objeto JSON). No lo toco.")
            return 1

    env = datos.get("env")
    if env is None:
        env = {}
    if not isinstance(env, dict):
        print(f'En {archivo}, "env" no es un objeto. No lo toco: revisalo a mano.')
        return 1

    if env.get(CLAVE) == bash:
        print(f"Ya estaba configurado: {CLAVE} = {bash}")
        print("Si Claude sigue usando PowerShell: cerrá la app DEL TODO (también el ícono junto al reloj) y abrila.")
        return 0

    env[CLAVE] = bash
    datos["env"] = env
    nuevo = json.dumps(datos, indent=2, ensure_ascii=False) + "\n"

    if args.mostrar:
        print(f"(--mostrar) Esto quedaría en {archivo}:")
        print(nuevo)
        return 0

    carpeta.mkdir(parents=True, exist_ok=True)
    if archivo.exists():
        sello = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        respaldo = archivo.with_name(f"settings.json.bak-{sello}")
        shutil.copy2(archivo, respaldo)
        print(f"Respaldo del archivo anterior: {respaldo}")
    archivo.write_text(nuevo, encoding="utf-8")
    print(f"Listo: {CLAVE} = {bash}")
    print(f"Guardado en {archivo} (lo demás que tenía, intacto).")
    print("Ahora cerrá la app de Claude DEL TODO y volvé a abrirla. Después: echo $BASH_VERSION tiene que mostrar un número.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
