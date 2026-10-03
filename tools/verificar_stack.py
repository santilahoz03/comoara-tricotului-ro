#!/usr/bin/env python3
"""
verificar_stack.py — prueba de humo de tu stack de ZEA (herramientas + claves del .env).

No gasta créditos: cada clave se prueba con la llamada más barata posible (saldo, cuenta o listado).
No imprime ninguna clave completa: solo los primeros 4 caracteres.
Solo usa la librería estándar de Python (no hace falta instalar nada).

Uso (desde la carpeta de tu negocio). En Windows, "python" (o "py") en vez de "python3":
    python3 tools/verificar_stack.py                    # todo
    python3 tools/verificar_stack.py --solo-herramientas
    python3 tools/verificar_stack.py --solo-claves
    python3 tools/verificar_stack.py --solo KIE_API_KEY # una sola clave (sirve durante la instalación)
    python3 tools/verificar_stack.py --prueba-telegram  # además te manda un mensaje de prueba
    python3 tools/verificar_stack.py --chat-id          # te dice tu TELEGRAM_CHAT_ID (mandale antes un mensaje a tu bot)
    python3 tools/verificar_stack.py --avisar-telegram  # si algo falla o el saldo de kie.ai está bajo, te avisa por Telegram
    python3 tools/verificar_stack.py --env /ruta/.env   # usar otro .env
    python3 tools/verificar_stack.py --perfil cazar     # chequea solo lo de tus kits (base | cazar | todo)
    python3 tools/verificar_stack.py --kits 01,02,06    # idem, eligiendo los kits (sumá "watch" si usás /watch)

Qué kits usás: si no pasás --perfil ni --kits, lo lee de la línea "- Kits elegidos: 00, 01" de tu CLAUDE.md.
Si no la encuentra, chequea todo (como antes). Lo que tus kits no usan sale como "NO LO USÁS": nunca es error
ni dispara avisos por Telegram. Se instala a demanda cuando llegues a ese kit (ver tools/instalar_herramientas.*).

Código de salida: 0 si no hubo ERROR, 1 si hubo al menos uno.
"""
import argparse
import base64
import glob
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

TIMEOUT = 20
RESULTADOS = []  # (seccion, nombre, estado, detalle, arreglo)


# ── utilidades ──────────────────────────────────────────────────────────────────

def leer_texto(ruta):
    """Lee un archivo de texto venga como venga: UTF-8 (con o sin BOM), UTF-16 (el Bloc de notas viejo
    lo guarda así si elegís "Unicode") o ANSI. Los finales de línea de Windows (CRLF) no molestan."""
    with open(ruta, "rb") as f:
        crudo = f.read()
    if crudo.startswith((b"\xff\xfe", b"\xfe\xff")):
        return crudo.decode("utf-16", "replace")
    try:
        return crudo.decode("utf-8-sig")
    except UnicodeDecodeError:
        return crudo.decode("cp1252", "replace")


def cargar_env(ruta):
    """Parser simple de .env: KEY=valor, ignora comentarios y comentarios al final de línea."""
    valores = {}
    if not os.path.exists(ruta):
        return valores
    for linea in leer_texto(ruta).splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        valor = valor.strip()
        # comentario al final: "VALOR   # comentario"
        if " #" in valor:
            valor = valor.split(" #", 1)[0].strip()
        if valor.startswith("#"):
            valor = ""
        valor = valor.strip('"').strip("'")
        valores[clave.strip().lstrip("\ufeff")] = valor
    return valores


def enmascarar(valor):
    return (valor[:4] + "…") if valor else "(vacía)"


def http(url, headers=None, data=None, method=None):
    req = urllib.request.Request(url, headers=headers or {}, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            cuerpo = r.read().decode("utf-8", "replace")
            return r.status, cuerpo
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except Exception as e:  # red caída, DNS, timeout
        return 0, str(e)


def registrar(seccion, nombre, estado, detalle="", arreglo=""):
    RESULTADOS.append((seccion, nombre, estado, detalle, arreglo))


# ── qué usa cada kit (ver sops/que-necesita-cada-kit.md del kit 00) ─────────────────────────────
NO_USA = "NO LO USÁS"
TODOS_KITS = ("00", "01", "02", "03", "04", "05", "06", "07", "watch")
PAQUETES_KIT = {   # la base (git, python, pip; en Windows Git Bash y PYTHONUTF8) la usan todos
    "02": {"chrome"},
    "03": {"ffmpeg", "yt-dlp", "whisper", "edge-tts", "node"},
    "04": {"node"},
    "05": {"ffmpeg", "whisper", "node"},
    "06": {"chrome", "gh"},
    "watch": {"yt-dlp", "ffmpeg", "whisper"},
}
# nombre de la fila de herramientas → paquete (las que no están acá son base: siempre se chequean)
FILA_PAQUETE = {
    "node": "node", "npm": "node", "gh (GitHub CLI)": "gh", "yt-dlp": "yt-dlp",
    "ffmpeg": "ffmpeg", "ffmpeg + libass": "ffmpeg", "openai-whisper": "whisper",
    "Visual C++ Redistributable": "whisper", "edge-tts (opcional)": "edge-tts", "Google Chrome": "chrome",
}
# variable del .env → (kits donde es obligatoria, kits donde es opcional)
CLAVE_KITS = {
    "KIE_API_KEY": (("02", "03", "05", "06"), ()),
    "GEMINI_API_KEY": (("03",), ("06",)),
    "ELEVENLABS_API_KEY": (("05",), ("03",)),
    "DREAMAPI_KEY": (("05",), ()),
    "VMAKE_AK": (("03",), ()),
    "VMAKE_SK": (("03",), ()),
    "STRIPE_SECRET_KEY": (("07",), ()),
    "WHOP_API_KEY": ((), ("02", "07")),
    "MERCADOPAGO_ACCESS_TOKEN": ((), ("02",)),
    "UTMIFY_MCP_TOKEN": (("04",), ()),
    "META_AD_ACCOUNT_ID": (("04",), ()),
    "META_PIXEL_ID": (("04",), ()),
    "PANDA_API_KEY": ((), ("05",)),
    "SUPABASE_SERVICE_ROLE_KEY": ((), ("06",)),
    "TELEGRAM_BOT_TOKEN": (("07",), ("00",)),
}
KITS = None          # None = no sé qué kits usás → chequeo todo (comportamiento de siempre)
ORIGEN_KITS = ""


def normalizar_kits(texto):
    """'00, 1, watch' → {'00', '01', 'watch'}. 'todo'/'todos' → todos. Ignora lo que esté entre [corchetes]."""
    texto = re.sub(r"\[.*?\]", " ", (texto or "").lower())
    kits = set()
    if re.search(r"\btodos?\b", texto):
        return set(TODOS_KITS)
    for num in re.findall(r"\b0?([0-7])\b", texto):
        kits.add("0" + num)
    if re.search(r"\bwatch\b", texto):
        kits.add("watch")
    if kits:
        kits.add("00")
    return kits


def kits_de_claude_md(rutas):
    """Busca la línea '- Kits elegidos: 00, 01' en el CLAUDE.md de la carpeta del negocio."""
    for ruta in rutas:
        if not os.path.isfile(ruta):
            continue
        for linea in leer_texto(ruta).splitlines():
            m = re.match(r"\s*[-*]?\s*\**kits elegidos\**\s*:\s*(.*)$", linea, re.IGNORECASE)
            if m:
                kits = normalizar_kits(m.group(1))
                if kits:
                    return kits, ruta
    return None, ""


def paquetes_requeridos():
    req = set()
    for k in KITS or ():
        req |= PAQUETES_KIT.get(k, set())
    return req


def kits_que_usan(paquete):
    return [k for k, paqs in PAQUETES_KIT.items() if paquete in paqs]


def texto_kits(kits):
    nums = [k for k in kits if k != "watch"]
    if nums == ["00"] and "watch" not in kits:
        return "avisos de las rutinas del kit 00"
    partes = []
    if nums:
        partes.append(("kit " if len(nums) == 1 else "kits ") + ", ".join(sorted(nums)))
    if "watch" in kits:
        partes.append("/watch (kit 01)")
    return " y ".join(partes)


def aplicar_perfil_herramientas():
    """Lo que tus kits no usan y no está instalado pasa a NO LO USÁS (no es error, no avisa)."""
    if KITS is None:
        return
    req = paquetes_requeridos()
    for i, (seccion, nombre, estado, detalle, arr) in enumerate(RESULTADOS):
        if seccion != "herramientas" or estado == "OK":
            continue
        if nombre == "brew":
            if req:
                continue
            RESULTADOS[i] = (seccion, nombre, NO_USA, "todavía · solo hace falta para instalar programas", "")
            continue
        paq = FILA_PAQUETE.get(nombre)
        if paq is None:
            continue
        if paq in req:
            if paq == "gh" and estado == "OPCIONAL":   # el kit 06 lo necesita para publicar
                RESULTADOS[i] = (seccion, nombre, "FALTA", "lo usa el kit 06 (publicar entregables)", arr)
            continue
        usan = texto_kits(kits_que_usan(paq))
        RESULTADOS[i] = (seccion, nombre, NO_USA, f"todavía · lo usa: {usan}" if usan else "todavía", "")


ES_WINDOWS = platform.system() == "Windows"
ES_MAC = platform.system() == "Darwin"


def arreglo(mac, windows):
    """El arreglo que corresponde al sistema donde corre el script."""
    return windows if ES_WINDOWS else mac


def correr(cmd):
    # En Windows hay que pasar la ruta completa: así también corren npm.cmd y similares.
    exe = shutil.which(cmd[0]) or cmd[0]
    try:
        p = subprocess.run([exe] + list(cmd[1:]), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=60)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return 1, str(e)


def es_alias_tienda(ruta):
    """El "python.exe" de WindowsApps es un alias que abre la Microsoft Store, no Python."""
    return bool(ruta) and "\\windowsapps\\" in ruta.lower()


def encontrar(nombre, extras=()):
    """Ruta de un programa: primero el PATH, después rutas conocidas (Windows)."""
    ruta = shutil.which(nombre)
    if ruta and not es_alias_tienda(ruta):
        return ruta
    for patron in extras:
        for r in sorted(glob.glob(os.path.expandvars(patron))):
            if os.path.isfile(r):
                return r
    return None


# ── herramientas ────────────────────────────────────────────────────────────────

def ffmpeg_con_libass():
    """Devuelve (ruta, tiene_libass, en_path). En Mac prueba primero ffmpeg-full de Homebrew;
    en Windows, también el FFmpeg de gyan.dev que instala winget aunque todavía no esté en el PATH."""
    candidatos = []
    if ES_MAC:
        for base in ("/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg", "/usr/local/opt/ffmpeg-full/bin/ffmpeg"):
            if os.path.exists(base):
                candidatos.append(base)
    en_path = shutil.which("ffmpeg")
    if en_path:
        candidatos.append(en_path)
    if ES_WINDOWS:
        for patron in (r"%LOCALAPPDATA%\Microsoft\WinGet\Links\ffmpeg.exe",
                       r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\ffmpeg.exe",
                       r"%ProgramFiles%\WinGet\Packages\Gyan.FFmpeg*\*\bin\ffmpeg.exe"):
            candidatos += [r for r in sorted(glob.glob(os.path.expandvars(patron))) if r not in candidatos]
    for ruta in candidatos:
        _, salida = correr([ruta, "-hide_banner", "-filters"])
        lineas = salida.splitlines()
        if any(l.split()[1:2] in (["ass"], ["subtitles"]) for l in lineas if len(l.split()) > 1):
            return ruta, True, ruta == en_path
    return (candidatos[0] if candidatos else None), False, bool(en_path)


def vcredist_instalado():
    """Windows: ¿está el Microsoft Visual C++ Redistributable x64 (lo necesita torch/whisper)?"""
    try:
        import winreg
    except ImportError:
        return None
    for sub in (r"SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64",
                r"SOFTWARE\WOW6432Node\Microsoft\VisualStudio\14.0\VC\Runtimes\x64"):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub) as k:
                if winreg.QueryValueEx(k, "Installed")[0] == 1:
                    return True
        except OSError:
            continue
    return False


def verificar_herramientas():
    so = platform.system()
    herramientas = [
        ("git", ["git", "--version"], arreglo("brew install git", "winget install -e --id Git.Git")),
        ("pip", [sys.executable, "-m", "pip", "--version"],
         arreglo("python3 -m ensurepip --upgrade", "python -m ensurepip --upgrade")),
        ("node", ["node", "--version"], arreglo("brew install node", "winget install -e --id OpenJS.NodeJS.LTS")),
        ("npm", ["npm", "--version"], "viene con node (si recién lo instalaste, reabrí la app de Claude)"),
        ("gh (GitHub CLI)", ["gh", "--version"],
         arreglo("brew install gh", "winget install -e --id GitHub.cli") + " (opcional, para páginas estáticas)"),
    ]
    if ES_MAC:
        herramientas.insert(0, ("brew", ["brew", "--version"], "https://brew.sh (un comando en la terminal)"))

    # Python: el que está corriendo este script
    registrar("herramientas", "python", "OK",
              f"{platform.python_version()} · {sys.executable}"[:90])

    # Si faltan estas, no es error (no disparan el aviso semanal por Telegram)
    opcionales = {"gh (GitHub CLI)", "claude"}
    extras_win = {
        "git": (r"%ProgramFiles%\Git\cmd\git.exe", r"%LOCALAPPDATA%\Programs\Git\cmd\git.exe"),
        "node": (r"%ProgramFiles%\nodejs\node.exe",),
        "npm": (r"%ProgramFiles%\nodejs\npm.cmd",),
        "gh": (r"%ProgramFiles%\GitHub CLI\gh.exe",),
    }
    for nombre, cmd, fix in herramientas:
        if cmd[0] != sys.executable:
            ruta = encontrar(cmd[0], extras_win.get(cmd[0], ()) if ES_WINDOWS else ())
            if not ruta:
                registrar("herramientas", nombre, "OPCIONAL" if nombre in opcionales else "FALTA", "", fix)
                continue
            fuera_de_path = not shutil.which(cmd[0])
            cmd = [ruta] + cmd[1:]
        else:
            fuera_de_path = False
        code, salida = correr(cmd)
        version = salida.strip().splitlines()[0][:60] if salida.strip() else ""
        if code == 0 and fuera_de_path:
            registrar("herramientas", nombre, "REVISAR", f"instalado pero fuera del PATH: {cmd[0]}",
                      "Cerrá la app de Claude del todo y volvé a abrirla")
        else:
            registrar("herramientas", nombre, "OK" if code == 0 else "ERROR", version, "" if code == 0 else fix)

    # yt-dlp: sirve el ejecutable o el módulo de Python (python -m yt_dlp)
    ruta = encontrar("yt-dlp")
    if ruta:
        code, salida = correr([ruta, "--version"])
        registrar("herramientas", "yt-dlp", "OK" if code == 0 else "ERROR", salida.strip()[:60],
                  "" if code == 0 else arreglo("brew install yt-dlp", "python -m pip install -U yt-dlp"))
    else:
        code, salida = correr([sys.executable, "-m", "yt_dlp", "--version"])
        if code == 0:
            registrar("herramientas", "yt-dlp", "OK", f"{salida.strip()[:20]} (usalo como: python -m yt_dlp)")
        else:
            registrar("herramientas", "yt-dlp", "FALTA", "",
                      arreglo("brew install yt-dlp", "python -m pip install -U yt-dlp"))

    # claude (comando de terminal; opcional si usás solo la app de escritorio)
    ruta = encontrar("claude", (r"%USERPROFILE%\.local\bin\claude.exe",) if ES_WINDOWS else
                     (os.path.expanduser("~/.local/bin/claude"),))
    if ruta:
        code, salida = correr([ruta, "--version"])
        registrar("herramientas", "claude", "OK" if code == 0 else "OPCIONAL", salida.strip()[:60])
    else:
        registrar("herramientas", "claude", "OPCIONAL", "",
                  "Solo para 'claude mcp add'. Con la app de escritorio alcanza (ver sops/conectores-y-permisos.md)")

    # ffmpeg con libass (crítico para subtítulos)
    ruta, libass, en_path = ffmpeg_con_libass()
    if not ruta:
        registrar("herramientas", "ffmpeg", "FALTA", "",
                  arreglo("brew install ffmpeg-full", "winget install -e --id Gyan.FFmpeg (el build 'full' trae libass)"))
    elif not libass:
        registrar("herramientas", "ffmpeg + libass", "ERROR", f"{ruta} no tiene filtro ass/subtitles",
                  arreglo("brew install ffmpeg-full y usá /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg para subtítulos",
                          "winget install -e --id Gyan.FFmpeg y reabrí la app de Claude"))
    elif ES_WINDOWS and not en_path:
        registrar("herramientas", "ffmpeg + libass", "REVISAR", f"instalado pero fuera del PATH: {ruta}",
                  "Cerrá la app de Claude del todo y volvé a abrirla (winget lo agrega al PATH para las apps nuevas)")
    else:
        registrar("herramientas", "ffmpeg + libass", "OK", ruta)

    # whisper (paquete de Python openai-whisper)
    code, salida = correr([sys.executable, "-c", "import whisper"])
    if code == 0:
        registrar("herramientas", "openai-whisper", "OK", "")
    elif ES_WINDOWS and any(s in salida for s in ("DLL", "WinError 126", "c10.dll", "fbgemm")):
        registrar("herramientas", "openai-whisper", "ERROR", "torch no carga (falta una DLL)",
                  "winget install -e --id Microsoft.VCRedist.2015+.x64 y reabrí la app de Claude")
    else:
        registrar("herramientas", "openai-whisper", "FALTA", "",
                  arreglo("python3 -m pip install -U openai-whisper", "python -m pip install -U openai-whisper"))

    # edge-tts (voz gratis de respaldo, opcional)
    code, _ = correr([sys.executable, "-c", "import edge_tts"])
    registrar("herramientas", "edge-tts (opcional)", "OK" if code == 0 else "OPCIONAL", "",
              "" if code == 0 else arreglo("python3 -m pip install -U edge-tts", "python -m pip install -U edge-tts"))

    # Chrome (QC visual de landings)
    chrome = None
    if ES_MAC:
        p = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome = p if os.path.exists(p) else None
    elif ES_WINDOWS:
        chrome = encontrar("chrome", (r"%ProgramFiles%\Google\Chrome\Application\chrome.exe",
                                      r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe",
                                      r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"))
    else:
        chrome = shutil.which("google-chrome") or shutil.which("chromium")
    registrar("herramientas", "Google Chrome", "OK" if chrome else "FALTA", chrome or "",
              "" if chrome else arreglo("google.com/chrome (se usa para capturas de QC)",
                                        "winget install -e --id Google.Chrome"))

    # Solo Windows: Git Bash, PYTHONUTF8 y Visual C++ Redistributable
    if ES_WINDOWS:
        bash = encontrar("__no__", (r"%ProgramFiles%\Git\bin\bash.exe",
                                    r"%ProgramFiles(x86)%\Git\bin\bash.exe",
                                    r"%LOCALAPPDATA%\Programs\Git\bin\bash.exe"))
        corrida = "esta corrida: Git Bash" if os.environ.get("MSYSTEM") else "esta corrida: no es Git Bash"
        registrar("herramientas", "Git Bash", "OK" if bash else "FALTA", f"{bash or ''} · {corrida}".strip(" ·"),
                  "" if bash else "winget install -e --id Git.Git y reabrí la app de Claude")
        utf8 = os.environ.get("PYTHONUTF8") == "1" or sys.flags.utf8_mode
        registrar("herramientas", "PYTHONUTF8=1", "OK" if utf8 else "REVISAR", "",
                  "" if utf8 else "setx PYTHONUTF8 1 y cerrá y abrí la app de Claude (evita UnicodeEncodeError 'charmap')")
        vc = vcredist_instalado()
        if vc is not None:
            registrar("herramientas", "Visual C++ Redistributable", "OK" if vc else "FALTA", "",
                      "" if vc else "winget install -e --id Microsoft.VCRedist.2015+.x64 (lo necesita whisper)")


# ── claves ──────────────────────────────────────────────────────────────────────

def chk_kie(env):
    k = env["KIE_API_KEY"]
    code, cuerpo = http("https://api.kie.ai/api/v1/chat/credit", {"Authorization": f"Bearer {k}"})
    if code != 200:
        return "ERROR", f"HTTP {code}", "Revisá la clave en kie.ai → API Keys"
    try:
        d = json.loads(cuerpo)
        creditos = d.get("data")
        if d.get("code") != 200:
            return "ERROR", d.get("msg", "respuesta rara"), "Revisá la clave en kie.ai → API Keys"
        minimo = float(env.get("KIE_CREDITOS_MINIMOS") or 0)
        if minimo and float(creditos) < minimo:
            return "BAJO", f"créditos: {creditos} (mínimo {int(minimo)})", "Cargá créditos en kie.ai (revisá que no tenga auto-recarga)"
        return "OK", f"créditos: {creditos}", ""
    except Exception:
        return "ERROR", "respuesta no es JSON", "Reintentá en un rato"


def chk_gemini(env):
    k = env["GEMINI_API_KEY"]
    aviso = ""
    if not k.startswith("AIza"):
        aviso = " · OJO: no empieza con 'AIza'. Si es un token de Gemini CLI ('AQ.'), no sirve para generar: creá una API key en aistudio.google.com/apikey"
    code, cuerpo = http("https://generativelanguage.googleapis.com/v1beta/models?pageSize=50",
                        {"x-goog-api-key": k})
    if code != 200:
        return "ERROR", f"HTTP {code}{aviso}", "Creá una API key nueva en aistudio.google.com/apikey"
    n = len(json.loads(cuerpo).get("models", []))
    return ("OK" if not aviso else "REVISAR"), f"{n} modelos visibles{aviso}", ""


def chk_eleven(env):
    k = env["ELEVENLABS_API_KEY"]
    code, cuerpo = http("https://api.elevenlabs.io/v1/user/subscription", {"xi-api-key": k})
    if code == 200:
        d = json.loads(cuerpo)
        return "OK", f"caracteres {d.get('character_count')}/{d.get('character_limit')} · plan {d.get('tier')}", ""
    # claves con permisos limitados: probar listado de voces
    code2, _ = http("https://api.elevenlabs.io/v1/voices", {"xi-api-key": k})
    if code2 == 200:
        return "OK", "clave válida (sin permiso para ver la suscripción)", ""
    return "ERROR", f"HTTP {code}", "Generá una clave nueva en elevenlabs.io → Developers → API Keys"


def chk_stripe(env):
    k = env["STRIPE_SECRET_KEY"]
    aviso = ""
    if k.startswith("sk_live_"):
        aviso = " · OJO: es la clave secreta completa. Mejor una restringida (rk_live_) de solo lectura"
    auth = base64.b64encode(f"{k}:".encode()).decode()
    code, cuerpo = http("https://api.stripe.com/v1/balance", {"Authorization": f"Basic {auth}"})
    if code == 200:
        d = json.loads(cuerpo)
        modo = "LIVE" if d.get("livemode") else "TEST"
        return ("OK" if not aviso else "REVISAR"), f"modo {modo}{aviso}", ""
    if code == 403:
        return "REVISAR", "clave válida pero sin permiso 'Balance: Read'", "En la clave restringida activá Balance → Read"
    return "ERROR", f"HTTP {code}", "Stripe → Developers → API keys"


def chk_mercadopago(env):
    k = env["MERCADOPAGO_ACCESS_TOKEN"]
    code, _ = http("https://api.mercadopago.com/users/me", {"Authorization": f"Bearer {k}"})
    if code == 200:
        return "OK", "cuenta accesible", ""
    return "ERROR", f"HTTP {code}", "Mercado Pago → Tus integraciones → Credenciales de producción"


def chk_telegram(env, prueba=False):
    tok = env["TELEGRAM_BOT_TOKEN"]
    code, cuerpo = http(f"https://api.telegram.org/bot{tok}/getMe")
    if code != 200:
        return "ERROR", f"HTTP {code}", "Pedile un token nuevo a @BotFather"
    bot = json.loads(cuerpo).get("result", {}).get("username", "?")
    if not env.get("TELEGRAM_CHAT_ID"):
        return "REVISAR", f"bot @{bot} OK, falta TELEGRAM_CHAT_ID", "Mandale un mensaje a tu bot y corré --chat-id"
    if prueba:
        ok = enviar_telegram(env, "Prueba de conexión OK (verificar_stack.py)")
        if not ok:
            return "ERROR", f"bot @{bot} OK pero no pudo mandarte el mensaje", "Revisá TELEGRAM_CHAT_ID y que le hayas escrito primero al bot"
        return "OK", f"bot @{bot} · mensaje de prueba enviado", ""
    return "OK", f"bot @{bot}", ""


def chk_panda(env):
    k = env["PANDA_API_KEY"]
    code, _ = http("https://api-v2.pandavideo.com.br/videos?limit=1", {"Authorization": k})
    if code == 200:
        return "OK", "API accesible", ""
    return "ERROR", f"HTTP {code}", "Panda → Configuraciones → API. Si el endpoint cambió, verificá en su documentación"


def chk_supabase(env):
    url = env.get("SUPABASE_URL", "").rstrip("/")
    k = env["SUPABASE_SERVICE_ROLE_KEY"]
    if not url:
        return "REVISAR", "falta SUPABASE_URL", "Supabase → Project Settings → API"
    code, _ = http(f"{url}/rest/v1/", {"apikey": k, "Authorization": f"Bearer {k}"})
    if code == 200:
        return "OK", "proyecto accesible", ""
    return "ERROR", f"HTTP {code}", "Revisá URL y service_role en Supabase → Project Settings → API"


def solo_cargada(detalle):
    def _f(env):
        return "CARGADA", detalle, ""
    return _f


CHEQUEOS = [
    ("kie.ai", "KIE_API_KEY", chk_kie),
    ("Gemini", "GEMINI_API_KEY", chk_gemini),
    ("ElevenLabs", "ELEVENLABS_API_KEY", chk_eleven),
    ("DreamAPI", "DREAMAPI_KEY", solo_cargada("sin prueba gratis: mirá el saldo en su panel")),
    ("Vmake (AK)", "VMAKE_AK", solo_cargada("se prueba sin gastar con el kit 03: python3 tools/vmake_limpiar.py --probar (Windows: python)")),
    ("Vmake (SK)", "VMAKE_SK", solo_cargada("idem")),
    ("Stripe", "STRIPE_SECRET_KEY", chk_stripe),
    ("Whop", "WHOP_API_KEY", solo_cargada("se verifica con el conector/CLI de Whop")),
    ("Mercado Pago", "MERCADOPAGO_ACCESS_TOKEN", chk_mercadopago),
    ("Utmify (MCP)", "UTMIFY_MCP_TOKEN", solo_cargada("se verifica con /mcp en Claude Code")),
    ("Meta ad account", "META_AD_ACCOUNT_ID", solo_cargada("ID, no clave")),
    ("Meta píxel", "META_PIXEL_ID", solo_cargada("ID, no clave")),
    ("Panda Video", "PANDA_API_KEY", chk_panda),
    ("Supabase", "SUPABASE_SERVICE_ROLE_KEY", chk_supabase),
    ("Telegram", "TELEGRAM_BOT_TOKEN", None),  # especial
]


# Variables que se prueban junto con otra (--solo TELEGRAM_CHAT_ID prueba el bot, etc.)
ALIAS_SOLO = {
    "TELEGRAM_CHAT_ID": "TELEGRAM_BOT_TOKEN",
    "SUPABASE_URL": "SUPABASE_SERVICE_ROLE_KEY",
}


def verificar_claves(env, solo=None, prueba_telegram=False):
    if solo:
        solo = ALIAS_SOLO.get(solo, solo)
        if solo not in [v for _, v, _ in CHEQUEOS]:
            estado = "CARGADA" if env.get(solo) else "VACÍA"
            registrar("claves", solo, estado, "variable sin prueba automática (revisá que el nombre esté bien escrito)")
            return
    for nombre, var, fn in CHEQUEOS:
        if solo and var != solo:
            continue
        valor = env.get(var, "")
        if not valor:
            if KITS is None or solo:
                registrar("claves", nombre, "VACÍA", "no la usás todavía", "")
                continue
            oblig, opc = CLAVE_KITS.get(var, ((), ()))
            mios_oblig = [k for k in oblig if k in KITS]
            mios_opc = [k for k in opc if k in KITS]
            if mios_oblig:
                registrar("claves", nombre, "VACÍA", f"la vas a necesitar ({texto_kits(mios_oblig)})", "")
            elif mios_opc:
                registrar("claves", nombre, "VACÍA", f"opcional ({texto_kits(mios_opc)})", "")
            else:
                usan = texto_kits(list(oblig) + [k for k in opc if k != "00"])
                registrar("claves", nombre, NO_USA, f"todavía · la usa: {usan}" if usan else "todavía", "")
            continue
        try:
            if var == "TELEGRAM_BOT_TOKEN":
                estado, detalle, arreglo = chk_telegram(env, prueba_telegram)
            else:
                estado, detalle, arreglo = fn(env)
        except Exception as e:
            estado, detalle, arreglo = "ERROR", f"{type(e).__name__}: {e}", "Reintentá; si sigue, revisá la clave"
        registrar("claves", f"{nombre} [{enmascarar(valor)}]", estado, detalle, arreglo)


# ── telegram ────────────────────────────────────────────────────────────────────

def enviar_telegram(env, texto):
    tok, chat = env.get("TELEGRAM_BOT_TOKEN"), env.get("TELEGRAM_CHAT_ID")
    if not tok or not chat:
        return False
    data = urllib.parse.urlencode({"chat_id": chat, "text": texto[:4000]}).encode()
    code, _ = http(f"https://api.telegram.org/bot{tok}/sendMessage", data=data, method="POST")
    return code == 200


def mostrar_chat_id(env):
    tok = env.get("TELEGRAM_BOT_TOKEN")
    if not tok:
        print("Primero completá TELEGRAM_BOT_TOKEN en el .env.")
        return
    code, cuerpo = http(f"https://api.telegram.org/bot{tok}/getUpdates")
    if code != 200:
        print(f"Error HTTP {code}: revisá el token.")
        return
    chats = {}
    for u in json.loads(cuerpo).get("result", []):
        msg = u.get("message") or u.get("edited_message") or {}
        c = msg.get("chat", {})
        if c.get("id") is not None:
            chats[c["id"]] = c.get("first_name") or c.get("title") or ""
    if not chats:
        print("No hay mensajes. Abrí Telegram, buscá tu bot, mandale 'hola' y volvé a correr --chat-id.")
        return
    for cid, nombre in chats.items():
        print(f"TELEGRAM_CHAT_ID={cid}   ({nombre})")
    print("Copiá ese valor en tu .env.")


# ── salida ──────────────────────────────────────────────────────────────────────

def imprimir():
    seccion_actual = None
    for seccion, nombre, estado, detalle, arreglo in RESULTADOS:
        if seccion != seccion_actual:
            print(f"\n== {seccion.upper()} " + "=" * (60 - len(seccion)))
            seccion_actual = seccion
        linea = f"{nombre:34} {estado:10} {detalle}"
        print(linea)
        if arreglo:
            print(f"{'':34} → {arreglo}")
    errores = [r for r in RESULTADOS if r[2] in ("ERROR", "FALTA")]
    avisos = [r for r in RESULTADOS if r[2] in ("BAJO", "REVISAR")]
    no_usa = [r for r in RESULTADOS if r[2] == NO_USA]
    print(f"\nResumen: {len(errores)} error(es)/faltante(s), {len(avisos)} aviso(s)"
          + (f", {len(no_usa)} que no usás todavía." if no_usa else "."))
    if KITS is not None:
        print(f"Kits que usás: {', '.join(sorted(KITS))} ({ORIGEN_KITS}).")
    else:
        print("Chequeé TODO (no sé qué kits usás: agregá '- Kits elegidos: 00, 01' a tu CLAUDE.md o usá --perfil).")
    if any(r[0] == "herramientas" for r in no_usa):
        print("Lo que dice NO LO USÁS se instala a demanda cuando llegues a ese kit, por ejemplo:")
        print("  " + ('powershell -ExecutionPolicy Bypass -File tools/instalar_herramientas.ps1 -Solo "ffmpeg,whisper"'
                      if ES_WINDOWS else "bash tools/instalar_herramientas.sh --solo ffmpeg,whisper"))
    return errores, avisos


def main():
    # En Windows, con la salida capturada (Claude Code), la consola usa cp1252 y "→" rompía el script.
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="Prueba de humo del stack de ZEA")
    ap.add_argument("--env", default=".env")
    ap.add_argument("--solo-herramientas", action="store_true")
    ap.add_argument("--solo-claves", action="store_true")
    ap.add_argument("--solo", help="probar una sola variable del .env, ej. KIE_API_KEY")
    ap.add_argument("--prueba-telegram", action="store_true")
    ap.add_argument("--avisar-telegram", action="store_true", help="avisar por Telegram solo si hay errores o saldo bajo")
    ap.add_argument("--chat-id", action="store_true")
    ap.add_argument("--perfil", choices=["base", "cazar", "todo"],
                    help="chequear solo lo de tus kits: base (kit 00), cazar (kit 01) o todo")
    ap.add_argument("--kits", help='kits que usás, ej. "01,02,06" (sumá "watch" si usás /watch)')
    args = ap.parse_args()

    global KITS, ORIGEN_KITS
    if args.perfil or args.kits:
        KITS = set()
        if args.perfil:
            KITS |= {"base": {"00"}, "cazar": {"00", "01"}, "todo": set(TODOS_KITS)}[args.perfil]
        if args.kits:
            elegidos = normalizar_kits(args.kits)
            if not elegidos:
                print(f"No entiendo --kits {args.kits!r}: usá números de kit (00 a 07) y/o watch.")
                return 2
            KITS |= elegidos
        ORIGEN_KITS = "--perfil/--kits"
    else:
        base = os.path.dirname(os.path.abspath(args.env))
        KITS, ORIGEN_KITS = kits_de_claude_md([os.path.join(base, "CLAUDE.md"), "CLAUDE.md"])
        if KITS is not None:
            ORIGEN_KITS = "leído de " + os.path.relpath(ORIGEN_KITS)

    env = cargar_env(args.env)
    if not env and not args.solo_herramientas:
        if not os.path.exists(args.env) and os.path.exists(args.env + ".txt"):
            print(f"Encontré {args.env}.txt: el Bloc de notas le agregó .txt. Renombralo a {args.env} y corré de nuevo.")
        else:
            print(f"No encontré {args.env}. Copiá .env.example como .env (en la raíz de tu negocio) y corré de nuevo.")

    if args.chat_id:
        mostrar_chat_id(env)
        return 0

    if args.solo:
        verificar_claves(env, solo=args.solo, prueba_telegram=args.prueba_telegram)
    else:
        if not args.solo_claves:
            verificar_herramientas()
            aplicar_perfil_herramientas()
        if not args.solo_herramientas:
            verificar_claves(env, prueba_telegram=args.prueba_telegram)

    errores, avisos = imprimir()

    if args.avisar_telegram and (errores or avisos):
        lineas = ["Salud del stack: hay cosas para revisar"]
        for _, nombre, estado, detalle, arreglo in errores + avisos:
            lineas.append(f"- {nombre}: {estado} {detalle}".strip())
        enviar_telegram(env, "\n".join(lineas))

    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
