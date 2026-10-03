# Stack — framework.md

> **Área:** admin
> **Estado:** parcial
> **Nivel de automatización actual:** 3 (salud semanal y auditoría mensual corren solas)
> **Actualizado:** AAAA-MM-DD
> **WIKI relacionada:** [[stack-conectores]]
> **Procesos que dependen de este:** todos

## Objetivo del proceso
Que todas las herramientas, claves, conectores y skills del negocio funcionen, cuesten lo mínimo y
avisen solas cuando algo se rompe.

## Cómo trabajamos hoy
1. **Claves:** viven solo en `.env` (raíz del proyecto). `.env.example` tiene la lista completa sin valores.
   Clave nueva → se agrega primero a `.env.example`, después a `.env`, y se prueba con
   `python3 tools/verificar_stack.py --solo <VARIABLE>` (Windows: `python`).
2. **Herramientas:** base para todos = git + Python 3 (Windows: + Git Bash y `PYTHONUTF8=1`). El resto (Node,
   ffmpeg con libass, yt-dlp, openai-whisper, edge-tts, gh, Chrome) solo según los kits de "Kits elegidos" en
   `CLAUDE.md` (matriz: `procesos/admin/stack/que-necesita-cada-kit.md`).
   Instalación y a demanda: `bash tools/instalar_herramientas.sh --solo <paquetes>` (Mac/Linux) o
   `powershell -ExecutionPolicy Bypass -File tools/instalar_herramientas.ps1 -Solo "<paquetes>"` (Windows; si instaló
   algo con winget, reiniciar la app de Claude para que tome el PATH). `--perfil base|cazar|todo` / `--kits 01,02`.
   Windows: Claude corre en Git Bash, Python es `python` (no `python3`), `PYTHONUTF8=1` como variable de usuario y
   la carpeta del negocio fuera de OneDrive. Plan B si sigue en PowerShell: `python tools/configurar_git_bash.py`.
3. **Skills:** se instalan con `/instalar-skill` o `bash tools/instalar_skill.sh <zip|.skill|carpeta>`.
   Todo `.skill` es un zip. Antes de instalar, escaneo de claves. Backup en `OUTPUTS/skills-backup/`.
4. **Conectores:** Gmail, Calendar, Drive y Meta (solo biblioteca de anuncios) desde claude.ai →
   Configuración → Conectores. Utmify, AdsUploader y Panda como MCP con `claude mcp add` (sin comando `claude`:
   Conectores de la app, ver `sops/conectores-y-permisos.md`).
   Mapa vivo en `WIKI/stack-conectores.md`.
5. **Suscripciones:** `stack.md` es la fuente de verdad de qué pago. Una herramienta por función.

## Reglas duras
- Nunca una clave en HTML/JS público, ni partida en pedazos — los escáneres la detectan y la revocan.
- Siempre el tier más barato que cumpla; subir solo si el barato falló dos veces.
- ffmpeg para subtítulos = el que tiene libass (en Mac, `ffmpeg-full`; en Windows, `Gyan.FFmpeg`).
- Facebook y la biblioteca de anuncios, solo en el navegador propio de Claude.
- Meta: conector solo para leer la biblioteca; lanzar, solo por AdsUploader y con orden explícita.

## Inputs
`.env`, `stack.md`, mails de cobro (Gmail), respuestas de las APIs.

## Outputs
- `OUTPUTS/AAAA-MM-DD-salud-stack.md` (semanal, solo si algo falló)
- `OUTPUTS/AAAA-MM-01-auditoria-suscripciones.md` (mensual)
- Aviso por Telegram si algo necesita atención.

## Automatizaciones actuales
- **Nivel 2:** `/verificar-stack`, `/instalar-skill`.
- **Nivel 3:** rutina de salud del stack (lunes 9:00) · auditoría de suscripciones (día 1, 9:00).

## Métricas del proceso
- Claves en ERROR: 0. Saldo de kie.ai arriba de `KIE_CREDITOS_MINIMOS`.
- Gasto mensual en herramientas: (completar desde `stack.md`).

## Huecos del proceso
1. …
