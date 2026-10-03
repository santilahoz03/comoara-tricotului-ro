# SOP · Qué necesita cada kit

El kit 00 instala **una base mínima para todos** y, arriba de eso, **solo lo que piden los kits que vas a usar**.
Lo demás se instala **a demanda** cuando llegues a ese kit: no hay que rehacer nada.

Fuente: los `LEEME.md` y `GUIA.md` de cada kit (requisitos y prompt de instalación), revisados el 2026-09-29.
Si un kit cambia sus requisitos, esta tabla se actualiza junto con `scripts/instalar_herramientas.*` y
`scripts/verificar_stack.py` (las tres usan el mismo mapa).

## La base (para todos, sin claves ni cuentas pagas)

| Qué | Por qué es base |
|---|---|
| Claude Code (app de escritorio → pestaña **Code**) + su **navegador propio** | Todos los kits trabajan ahí; `/cazar` y el QC navegan con ese navegador |
| Carpeta del negocio: `RAW/ WIKI/ OUTPUTS/ procesos/ memoria/ tools/ work/`, `CLAUDE.md`, `memoria.md`, `stack.md`, `.gitignore`, `.env` (puede quedar vacío) | Es el contrato y el cerebro que leen todos los kits |
| Skills `/bibliotecario`, `/guardar-regla`, `/instalar-skill`, `/verificar-stack` | Mantener el cerebro, aprender de tus correcciones, instalar los kits siguientes |
| **git** y **Python 3** (+ pip) | Extraer los kits, correr los scripts de todos los kits, `git init` local |
| **Windows:** Git for Windows (trae **Git Bash**) + Python 3.12 + `PYTHONUTF8=1` | Los scripts de todos los kits corren en Git Bash y Python; sin UTF-8 se rompen tildes y emojis |

**No es base:** ffmpeg, whisper, edge-tts, yt-dlp, Node, gh, Chrome, claves de IA, Telegram, conectores de Google
o Meta, MCP locales ni las rutinas del kit 00. Todo eso entra según la tabla de abajo.

## Tabla por kit

`opc.` = opcional dentro de ese kit. Los paquetes van con el nombre que usa el instalador (`--solo <paquete>`).

| Kit | Programas (además de la base) | Claves del `.env` | Cuentas / servicios | Conectores / MCP / navegador |
|---|---|---|---|---|
| **00** Configuración inicial | — (rutinas opc.: ninguna necesita programas) | `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` solo si querés avisos de la rutina de salud (opc.) | Cuenta de Google solo para la auditoría de suscripciones (opc.) | Navegador propio de Claude · Gmail solo para la auditoría (opc.) |
| **01** Cazar (`/cazar`) | — | — | — | Navegador propio de Claude (sin login de Facebook, sin conector de Meta) |
| **01** `/watch` (opc.) | `yt-dlp`, `ffmpeg`, `whisper` (atajo: `--solo watch`) | — | — | — |
| **02** Modelar | `chrome` (QC headless de landings + extensión Claude in Chrome). `curl`. `beautifulsoup4` (lo instala el kit). `gh` opc. si publicás la entrega en GitHub Pages | `KIE_API_KEY` · opc.: `GODADDY_KEY`/`GODADDY_SECRET` o `CLOUDFLARE_TOKEN`/`CLOUDFLARE_ZONE_ID` (+ `DNS_PROVEEDOR`, `DOMINIO_RAIZ`) | kie.ai con saldo · ImpulTienda (o Shopify) · dominio propio · procesador de pago (Stripe, Whop o Mercado Pago) | Navegador propio de Claude · **Claude in Chrome** con tu sesión de la tienda |
| **03** Creación de ads | `ffmpeg` (con libass), `yt-dlp`, `whisper`, `edge-tts`, `node` (para `npx` / HyperFrames). Librerías de `tools/requirements.txt` (las instala el kit). Windows: Visual C++ (va con whisper) | `KIE_API_KEY`, `GEMINI_API_KEY` · `VMAKE_AK` + `VMAKE_SK` para réplicas/doblajes (+ SDK de Vmake) · opc.: `ELEVENLABS_API_KEY`, `FFMPEG=` | kie.ai con saldo (~USD 5) · Vmake (panel de desarrolladores) · ElevenLabs opc. | — (HyperFrames como skill) |
| **04** Lanzamiento Meta Ads | `node` 18+ (CLI de AdsUploader por `npm`). `tzdata` en Windows (lo instala el kit) | `UTMIFY_MCP_URL` / `UTMIFY_MCP_TOKEN` · IDs de Meta van en `cuentas.md` (opc. `META_AD_ACCOUNT_ID`, `META_PIXEL_ID`) | Business Manager verificado, cuenta publicitaria, página, píxel + CAPI · **AdsUploader con plan pago** · Utmify | **MCP AdsUploader** + CLI (`ads login`) · **MCP Utmify** |
| **05** Embudo post-pago | `ffmpeg` (con libass), `whisper`, `node` (`npx skills add` de DreamAPI), `requests` | `ELEVENLABS_API_KEY` (+ `ELEVENLABS_VOICE_ID`), `DREAMAPI_KEY`, `KIE_API_KEY` · opc.: `PANDA_API_KEY` | ElevenLabs (plan pago para voces de biblioteca) · DreamAPI con créditos · kie.ai · ImpulTienda · hosting de video (Panda, Vturb…) | Claude in Chrome opc. (armar el funnel en ImpulTienda) · MCP Panda opc. |
| **06** Entregables y hub | `chrome` (bonos HTML → PDF; en Windows sirve Edge), `gh`, `requests` (+ `pillow`, lo instala el kit) | `KIE_API_KEY` · opc.: `GEMINI_API_KEY` (chat IA, solo en el proxy), `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY` | kie.ai con saldo · **cuenta de GitHub dedicada** (`gh auth login`) · Supabase opc. (chat IA) | — |
| **07** Soporte automático | — (scripts con librería estándar de Python) | `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` · `STRIPE_SECRET_KEY` (restringida `rk_`) si cobrás con Stripe · opc.: `WHOP_API_KEY` | Casilla de soporte en Gmail · Stripe y/o Whop · Telegram en el celu | **Gmail** (casilla de soporte) · conector de Whop opc. |

**Nadie necesita el conector de Meta.** El scouting va por el navegador propio de Claude y los lanzamientos por
AdsUploader. Conectarlo es opcional (solo sirve para `ads_library_search`, solo lectura).
**Google Calendar y Drive:** ningún kit los exige; se ofrecen como opcionales.

## Perfiles del kit 00

| Perfil (pregunta "¿Qué vas a instalar?") | Kits | Instalador | Claves que pide el kit 00 | Conectores |
|---|---|---|---|---|
| **a · Solo Cazar** | 00, 01 | `--perfil cazar` (= base) · `/watch` se ofrece en el kit 01 | ninguna (el `.env` queda creado y vacío) | navegador propio de Claude |
| **b · Cazar + Modelar + Entregables** | 00, 01, 02, 06 | `--kits 01,02,06` → `chrome`, `gh`, `requests` | `KIE_API_KEY` (opc.: `GEMINI_API_KEY`) | navegador propio · Claude in Chrome lo conecta el kit 02 |
| **c · Todo el sistema** | 00 a 07 | `--perfil todo` | las del día 1 de cada kit (kie, Gemini, Telegram…) y el resto "saltear" | Gmail, (Calendar, Drive opc.), MCP los agrega su kit |
| **d · Kits sueltos** | los que elijas | `--kits 01,03` (por ejemplo) | solo las obligatorias de esos kits | solo las de esos kits |

Las 3 rutinas del kit 00: **revisión del cerebro** se ofrece a todos (no necesita nada) · **salud del stack** solo si
tenés Telegram (si no, no tiene cómo avisarte) · **auditoría de suscripciones** solo si tenés Gmail conectado.

## Instalar a demanda (lo usan los kits 01 a 07)

Parado en la carpeta del negocio (los instaladores quedaron en `tools/` en el kit 00):

```bash
# Mac / Linux
bash tools/instalar_herramientas.sh --solo ffmpeg,whisper          # paquetes sueltos
bash tools/instalar_herramientas.sh --kits 03                      # todo lo del kit 03
bash tools/instalar_herramientas.sh --solo watch --simular         # solo mostrar qué instalaría
```

```bash
# Windows (desde Git Bash o PowerShell)
powershell -ExecutionPolicy Bypass -File tools/instalar_herramientas.ps1 -Solo "ffmpeg,whisper"
powershell -ExecutionPolicy Bypass -File tools/instalar_herramientas.ps1 -Kits "03"
powershell -ExecutionPolicy Bypass -File tools/instalar_herramientas.ps1 -Solo "watch" -Simular
```

Paquetes: `git python node ffmpeg yt-dlp whisper edge-tts requests gh chrome` · atajo `watch` = `yt-dlp ffmpeg whisper`.
Es idempotente (lo que ya está, lo saltea). `whisper` suma `ffmpeg` solo (y en Windows el Visual C++). En Windows,
si instaló algo con winget, hay que **cerrar y abrir la app de Claude** para que tome el PATH nuevo (el resumen lo dice).
En Mac, si falta Homebrew y hace falta, el script muestra el comando y lo corrés vos (pide tu contraseña).

Después de instalar, sumá el kit a la línea `- Kits elegidos:` de tu `CLAUDE.md` (y `watch` si instalaste `/watch`):
así `python3 tools/verificar_stack.py` (Windows: `python`) lo empieza a chequear. Lo que no usás figura como
**NO LO USÁS** y nunca cuenta como error ni dispara avisos.
