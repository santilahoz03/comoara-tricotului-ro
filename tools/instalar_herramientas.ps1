# instalar_herramientas.ps1 - herramientas de ZEA en Windows 10 (1809+) / 11, con winget. Instala SOLO lo que
# necesitan los kits que vas a usar.
#
# Uso (lo corre Claude). En el kit 00, desde PowerShell, ANTES de tener Git Bash:
#   powershell -ExecutionPolicy Bypass -File "$HOME\ZEA-kits\kit-00-configuracion-inicial\scripts\instalar_herramientas.ps1" -Perfil cazar
# Despues, desde la carpeta de tu negocio (en Git Bash o PowerShell), para INSTALAR A DEMANDA:
#   powershell -ExecutionPolicy Bypass -File tools/instalar_herramientas.ps1 -Solo "ffmpeg,whisper"
#
# Parametros (se pueden combinar: se instala la union):
#   -Perfil base|cazar|todo   base = Git (trae Git Bash) + Python 3.12 + PYTHONUTF8=1. cazar = base. todo = todo.
#   -Kits "01,02,06"          lo que necesitan esos kits (00 a 07; "watch" = lo de /watch)
#   -Solo "ffmpeg,whisper"    paquetes sueltos: git python node ffmpeg yt-dlp whisper edge-tts requests gh chrome
#                             (o "watch" = yt-dlp + ffmpeg + whisper)
#   -Simular                  muestra que instalaria, sin instalar ni cambiar nada
# Sin parametros = -Perfil todo (asi funcionaba antes). Los prompts de los kits pasan siempre el perfil.
# La base (Git + Python + PYTHONUTF8) se chequea siempre. whisper suma ffmpeg y Visual C++ solos (los necesita).
#
# Paquetes: Git (trae Git Bash), Python 3.12, Node.js LTS, FFmpeg full de gyan.dev (trae libass), GitHub CLI,
# Google Chrome y Microsoft Visual C++ Redistributable (lo necesita torch/whisper). Con pip: openai-whisper,
# edge-tts, requests, yt-dlp.
#
# Idempotente: lo que ya esta instalado se saltea. Si se corta (por tiempo o porque dijiste "No" a un cartel),
# se vuelve a correr y sigue desde donde quedo.
# Compatible con Windows PowerShell 5.1. El archivo esta en ASCII a proposito (sin tildes): asi PowerShell 5.1
# lo lee bien en cualquier configuracion regional, tenga o no BOM.
#
# Al terminar, si instalo algo: CERRAR la app de Claude del todo y volver a abrirla (para que tome Git Bash,
# el PATH nuevo y PYTHONUTF8).

param(
  [string]$Perfil = '',
  [string]$Kits = '',
  [string]$Solo = '',
  [switch]$Simular
)

$ErrorActionPreference = 'Continue'
$ProgressPreference = 'SilentlyContinue'

$Resumen = New-Object System.Collections.ArrayList
$Log = Join-Path $HOME 'ZEA-kits\instalar_herramientas-resumen.txt'

function Add-Resultado([string]$Nombre, [string]$Estado, [string]$Detalle) {
  [void]$Resumen.Add([pscustomobject]@{ Nombre = $Nombre; Estado = $Estado; Detalle = $Detalle })
}

function Update-SessionPath {
  $m = [System.Environment]::GetEnvironmentVariable('Path', 'Machine')
  $u = [System.Environment]::GetEnvironmentVariable('Path', 'User')
  $links = "$env:LOCALAPPDATA\Microsoft\WinGet\Links"
  $env:Path = "$m;$u;$links;$env:Path"
}

# Devuelve la ruta de un ejecutable del PATH, ignorando los "alias" de la Microsoft Store (WindowsApps),
# que para python abren la Store en vez de correr Python.
function Get-Exe([string]$Nombre) {
  $cmds = @(Get-Command $Nombre -CommandType Application -ErrorAction SilentlyContinue)
  foreach ($c in $cmds) {
    if ($c.Path -and ($c.Path -notlike '*\WindowsApps\*')) { return $c.Path }
  }
  return $null
}

function Test-Archivo([string]$Ruta) {
  if (-not $Ruta) { return $false }
  return (Test-Path -LiteralPath $Ruta -PathType Leaf)
}

function Find-GitBash {
  $cands = @(
    "$env:ProgramFiles\Git\bin\bash.exe",
    "${env:ProgramFiles(x86)}\Git\bin\bash.exe",
    "$env:LOCALAPPDATA\Programs\Git\bin\bash.exe"
  )
  $git = Get-Exe 'git'
  if ($git) {
    # git.exe suele estar en ...\Git\cmd\git.exe -> bash en ...\Git\bin\bash.exe
    $raiz = Split-Path (Split-Path $git -Parent) -Parent
    $cands += "$raiz\bin\bash.exe"
  }
  foreach ($c in $cands) { if (Test-Archivo $c) { return $c } }
  return $null
}

function Test-Python([string]$Ruta) {
  if (-not (Test-Archivo $Ruta)) { return $false }
  try {
    $out = & $Ruta -c "import sys;print(sys.version_info[0]*100+sys.version_info[1])" 2>$null
    if ($LASTEXITCODE -eq 0 -and $out) {
      $v = [int](@($out)[0])
      return ($v -ge 310)
    }
  } catch { }
  return $false
}

function Find-Python {
  $cands = @(
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
    "$env:ProgramFiles\Python312\python.exe"
  )
  foreach ($c in $cands) { if (Test-Python $c) { return $c } }
  $py = Get-Exe 'py'
  if ($py) {
    foreach ($ver in @('-3.12', '-3')) {
      try {
        $out = & $py $ver -c "import sys;print(sys.executable)" 2>$null
        if ($LASTEXITCODE -eq 0 -and $out) {
          $ruta = [string](@($out)[0])
          if (Test-Python $ruta) { return $ruta }
        }
      } catch { }
    }
  }
  $p = Get-Exe 'python'
  if (Test-Python $p) { return $p }
  return $null
}

function Find-Node {
  $n = Get-Exe 'node'
  if ($n) { return $n }
  $c = "$env:ProgramFiles\nodejs\node.exe"
  if (Test-Archivo $c) { return $c }
  return $null
}

function Find-FFmpeg {
  $f = Get-Exe 'ffmpeg'
  if ($f) { return $f }
  $c = "$env:LOCALAPPDATA\Microsoft\WinGet\Links\ffmpeg.exe"
  if (Test-Archivo $c) { return $c }
  foreach ($base in @("$env:LOCALAPPDATA\Microsoft\WinGet\Packages", "$env:ProgramFiles\WinGet\Packages")) {
    if (Test-Path -LiteralPath $base) {
      $dirs = @(Get-ChildItem -LiteralPath $base -Directory -ErrorAction SilentlyContinue | Where-Object { $_.Name -like 'Gyan.FFmpeg*' })
      foreach ($d in $dirs) {
        $exe = Get-ChildItem -LiteralPath $d.FullName -Recurse -Filter 'ffmpeg.exe' -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($exe) { return $exe.FullName }
      }
    }
  }
  return $null
}

function Find-Gh {
  $g = Get-Exe 'gh'
  if ($g) { return $g }
  $c = "$env:ProgramFiles\GitHub CLI\gh.exe"
  if (Test-Archivo $c) { return $c }
  return $null
}

function Find-Chrome {
  $cands = @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
  )
  foreach ($c in $cands) { if (Test-Archivo $c) { return $c } }
  return $null
}

function Find-VCRedist {
  $claves = @(
    'HKLM:\SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64',
    'HKLM:\SOFTWARE\WOW6432Node\Microsoft\VisualStudio\14.0\VC\Runtimes\x64'
  )
  foreach ($k in $claves) {
    $v = Get-ItemProperty -Path $k -ErrorAction SilentlyContinue
    if ($v -and $v.Installed -eq 1) { return ("version " + $v.Version) }
  }
  return $null
}

# Agrega una carpeta AL PRINCIPIO del PATH de tu usuario (antes de WindowsApps, para que "python" no abra
# la Microsoft Store). Respeta las entradas con %VARIABLES%. No toca el PATH del sistema.
function Add-UserPathFront([string]$Dir) {
  if (-not $Dir) { return }
  if (-not (Test-Path -LiteralPath $Dir)) { return }
  $key = [Microsoft.Win32.Registry]::CurrentUser.OpenSubKey('Environment', $true)
  if ($null -eq $key) { return }
  try {
    $raw = [string]$key.GetValue('Path', '', [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames)
    $partes = @($raw -split ';' | Where-Object { $_ -ne '' })
    $objetivo = $Dir.TrimEnd('\')
    $iDir = -1
    $iApps = -1
    for ($i = 0; $i -lt $partes.Count; $i++) {
      $exp = [System.Environment]::ExpandEnvironmentVariables($partes[$i]).TrimEnd('\')
      if ($iDir -lt 0 -and $exp -eq $objetivo) { $iDir = $i }
      if ($iApps -lt 0 -and $exp -like '*\Microsoft\WindowsApps') { $iApps = $i }
    }
    if ($iDir -ge 0 -and ($iApps -lt 0 -or $iDir -lt $iApps)) { return }
    $resto = @()
    for ($i = 0; $i -lt $partes.Count; $i++) {
      $exp = [System.Environment]::ExpandEnvironmentVariables($partes[$i]).TrimEnd('\')
      if ($exp -ne $objetivo) { $resto += $partes[$i] }
    }
    $nuevo = (@($Dir) + $resto) -join ';'
    $key.SetValue('Path', $nuevo, [Microsoft.Win32.RegistryValueKind]::ExpandString)
    $script:Cambios = $true
    Write-Host "  (agregado al principio del PATH de tu usuario: $Dir)"
  } catch {
    Write-Host "  No pude actualizar el PATH de tu usuario: $($_.Exception.Message)"
  } finally {
    $key.Close()
  }
}

function Install-Winget([string]$Id, [string]$Nombre) {
  $script:Cambios = $true
  Write-Host ("  {0,-30} instalando con winget..." -f $Nombre)
  $out = & winget install --id $Id -e --source winget --accept-source-agreements --accept-package-agreements --silent
  $code = $LASTEXITCODE
  if ($code -ne 0) {
    $hex = '0x{0:X8}' -f $code
    $motivo = ''
    switch ($hex) {
      '0x8A15002B' { $motivo = 'ya estaba instalado (sin actualizacion)' }
      '0x8A150061' { $motivo = 'ya estaba instalado' }
      '0x8A150014' { $motivo = 'winget no encontro el paquete: actualiza "Instalador de aplicacion" desde la Microsoft Store' }
      '0x80070642' { $motivo = 'se cancelo: probablemente tocaste "No" en el cartel de permiso de Windows' }
      '0x00000642' { $motivo = 'se cancelo: probablemente tocaste "No" en el cartel de permiso de Windows' }
      '0x000004C7' { $motivo = 'se cancelo: probablemente tocaste "No" en el cartel de permiso de Windows' }
      '0x00000BC2' { $motivo = 'instalado, pide reiniciar Windows' }
      default      { $motivo = 'winget devolvio ' + $hex }
    }
    Write-Host ("  {0,-30} {1}" -f '', $motivo)
    if ($hex -notin @('0x8A15002B', '0x8A150061', '0x00000BC2')) {
      $ultimas = @($out | Where-Object { $_ -match '[A-Za-z]{3,}' } | Select-Object -Last 3)
      foreach ($l in $ultimas) { Write-Host ("  {0,-30} winget: {1}" -f '', $l.Trim()) }
    }
  }
  Update-SessionPath
}

# --- 0. Que hay que instalar (segun perfil / kits / paquetes sueltos) -------------------------------------
$Todos = @('git', 'python', 'node', 'ffmpeg', 'yt-dlp', 'whisper', 'edge-tts', 'requests', 'gh', 'chrome')
# kit -> paquetes (ver sops/que-necesita-cada-kit.md del kit 00). La base (git + python) va siempre.
$MapaKits = @{
  '00' = @(); '0' = @(); '01' = @(); '1' = @(); '07' = @(); '7' = @()
  '02' = @('chrome'); '2' = @('chrome')
  '03' = @('ffmpeg', 'yt-dlp', 'whisper', 'edge-tts', 'node'); '3' = @('ffmpeg', 'yt-dlp', 'whisper', 'edge-tts', 'node')
  '04' = @('node'); '4' = @('node')
  '05' = @('ffmpeg', 'whisper', 'node', 'requests'); '5' = @('ffmpeg', 'whisper', 'node', 'requests')
  '06' = @('chrome', 'gh', 'requests'); '6' = @('chrome', 'gh', 'requests')
  'watch' = @('yt-dlp', 'ffmpeg', 'whisper')
  'todo' = $Todos; 'todos' = $Todos
}
$Alias = @{
  'yt_dlp' = 'yt-dlp'; 'ytdlp' = 'yt-dlp'; 'edge_tts' = 'edge-tts'; 'openai-whisper' = 'whisper'
  'ffmpeg-full' = 'ffmpeg'; 'libass' = 'ffmpeg'; 'google-chrome' = 'chrome'; 'nodejs' = 'node'; 'npm' = 'node'
}

$Pedido = @{}
function Split-Lista([string]$Texto) {
  return @($Texto -split '[,; ]+' | ForEach-Object { $_.Trim().ToLower() } | Where-Object { $_ -ne '' })
}

$huboParametro = ($Perfil -ne '') -or ($Kits -ne '') -or ($Solo -ne '')
if ($Perfil -ne '') {
  switch ($Perfil.Trim().ToLower()) {
    'base' { }
    'cazar' { }
    'solo-cazar' { }
    'todo' { foreach ($x in $Todos) { $Pedido[$x] = $true } }
    'todos' { foreach ($x in $Todos) { $Pedido[$x] = $true } }
    default { Write-Host ("Perfil '{0}' no existe. Usa base, cazar o todo (o -Kits / -Solo)." -f $Perfil); exit 2 }
  }
}
foreach ($k in (Split-Lista $Kits)) {
  if (-not $MapaKits.ContainsKey($k)) { Write-Host ("Kit '{0}' no existe (00 a 07, o watch)." -f $k); exit 2 }
  foreach ($x in $MapaKits[$k]) { $Pedido[$x] = $true }
}
foreach ($s in (Split-Lista $Solo)) {
  if ($Alias.ContainsKey($s)) { $s = $Alias[$s] }
  if ($s -eq 'base') { continue }
  if ($s -eq 'watch') { foreach ($x in $MapaKits['watch']) { $Pedido[$x] = $true }; continue }
  if ($Todos -notcontains $s) {
    Write-Host ("Paquete '{0}' no existe. Disponibles: {1} (o watch)." -f $s, ($Todos -join ' '))
    exit 2
  }
  $Pedido[$s] = $true
}
if (-not $huboParametro) {
  Write-Host "(Sin perfil: instalo TODO, como antes. Para instalar solo lo que usas: -Perfil base|cazar|todo, -Kits o -Solo)"
  foreach ($x in $Todos) { $Pedido[$x] = $true }
}
$Pedido['git'] = $true
$Pedido['python'] = $true
if ($Pedido.ContainsKey('whisper')) { $Pedido['ffmpeg'] = $true; $Pedido['vcredist'] = $true }  # whisper sin ffmpeg no transcribe

function Test-Quiero([string]$Paq) { return $Pedido.ContainsKey($Paq) }

$Cambios = $false
$extras = @($Todos | Where-Object { ($_ -ne 'git') -and ($_ -ne 'python') -and (Test-Quiero $_) })
$txtExtras = 'nada'
if ($extras.Count -gt 0) { $txtExtras = $extras -join ' ' }

# --- 1. Chequeos previos ----------------------------------------------------------------------------------
Write-Host "Instalador de herramientas de ZEA para Windows"
Write-Host ("Base (siempre): Git + Python + PYTHONUTF8 - Ademas: {0}" -f $txtExtras)
if ($Simular) { Write-Host "MODO SIMULACION: no se instala ni se cambia nada, solo te digo que haria." }
Write-Host ""
$ver = [System.Environment]::OSVersion.Version
$arq = $env:PROCESSOR_ARCHITECTURE
if ($env:PROCESSOR_ARCHITEW6432) { $arq = $env:PROCESSOR_ARCHITEW6432 }
Write-Host ("Windows {0}.{1} build {2} - {3}" -f $ver.Major, $ver.Minor, $ver.Build, $arq)
if ($ver.Build -lt 17763) {
  Write-Host "OJO: Claude Code necesita Windows 10 version 1809 (build 17763) o mas nuevo. Actualiza Windows primero."
}
if (($arq -eq 'ARM64') -and (Test-Quiero 'whisper')) {
  Write-Host "OJO: tu compu es ARM64. Todo deberia instalarse, pero openai-whisper (torch) puede fallar en ARM."
  Write-Host "     No bloquea la instalacion: whisper se usa en /watch y en los kits de ads y post-pago."
}

Update-SessionPath
$hayWinget = [bool](Get-Command winget -ErrorAction SilentlyContinue)
if (-not $hayWinget) {
  Write-Host ""
  Write-Host "FALTA winget (el instalador de programas de Windows)."
  Write-Host "Arreglo: abri la Microsoft Store, busca 'Instalador de aplicacion' (App Installer), instalalo o"
  Write-Host "actualizalo, cerra y volve a abrir la app de Claude, y corre este script de nuevo."
  Add-Resultado 'winget' 'FALTA' 'Microsoft Store -> Instalador de aplicacion (App Installer)'
} else {
  $wv = & winget --version 2>$null
  Write-Host ("winget {0}" -f (@($wv)[0]))
}
Write-Host ""
if (-not $Simular) {
  Write-Host "Puede aparecer un cartel de Windows pidiendo permiso (Control de cuentas de usuario): toca 'Si'."
  Write-Host "Si no lo ves, buscalo en la barra de tareas (icono con escudo que parpadea)."
  Write-Host ""
}

# --- 2. Programas con winget ------------------------------------------------------------------------------
$paquetes = @(
  @{ Paq = 'git';      Id = 'Git.Git';                      Nombre = 'Git (trae Git Bash)';        Buscar = { Find-GitBash } },
  @{ Paq = 'python';   Id = 'Python.Python.3.12';           Nombre = 'Python 3.12';                Buscar = { Find-Python } },
  @{ Paq = 'node';     Id = 'OpenJS.NodeJS.LTS';            Nombre = 'Node.js LTS';                Buscar = { Find-Node } },
  @{ Paq = 'ffmpeg';   Id = 'Gyan.FFmpeg';                  Nombre = 'FFmpeg full (gyan.dev)';     Buscar = { Find-FFmpeg } },
  @{ Paq = 'gh';       Id = 'GitHub.cli';                   Nombre = 'GitHub CLI (gh)';            Buscar = { Find-Gh } },
  @{ Paq = 'chrome';   Id = 'Google.Chrome';                Nombre = 'Google Chrome';              Buscar = { Find-Chrome } },
  @{ Paq = 'vcredist'; Id = 'Microsoft.VCRedist.2015+.x64'; Nombre = 'Visual C++ Redistributable'; Buscar = { Find-VCRedist } }
)

foreach ($p in $paquetes) {
  if (-not (Test-Quiero $p.Paq)) { continue }
  $encontrado = & $p.Buscar
  if (-not $encontrado -and $Simular) {
    Write-Host ("  {0,-30} FALTA -> instalaria: winget install -e --id {1}" -f $p.Nombre, $p.Id)
    Add-Resultado $p.Nombre 'SIMULADO' ("winget install -e --id " + $p.Id)
    continue
  }
  if (-not $encontrado -and $hayWinget) {
    Install-Winget $p.Id $p.Nombre
    $encontrado = & $p.Buscar
  }
  if ($encontrado) {
    Write-Host ("  {0,-30} OK    {1}" -f $p.Nombre, $encontrado)
    Add-Resultado $p.Nombre 'OK' $encontrado
  } else {
    Write-Host ("  {0,-30} FALTA" -f $p.Nombre)
    Add-Resultado $p.Nombre 'FALTA' ("winget install -e --id " + $p.Id)
  }
}

# --- 3. Python en el PATH + paquetes de Python que pidieron tus kits ---------------------------------------
$env:PYTHONUTF8 = '1'
$pipPedidos = @()
foreach ($par in @(@('whisper', 'openai-whisper', 'whisper'), @('edge-tts', 'edge-tts', 'edge_tts'), @('requests', 'requests', 'requests'), @('yt-dlp', 'yt-dlp', 'yt_dlp'))) {
  if (Test-Quiero $par[0]) { $pipPedidos += , $par }
}
$py = Find-Python
if ($py) {
  $pyDir = Split-Path $py -Parent
  if ((-not $Simular) -and ($pyDir -like "$env:LOCALAPPDATA\Programs\Python\*")) {
    # Python instalado para tu usuario: que "python" y sus Scripts queden en el PATH, antes de WindowsApps.
    Add-UserPathFront "$pyDir\Scripts"
    Add-UserPathFront $pyDir
  }
  $env:Path = "$pyDir;$pyDir\Scripts;$env:Path"
}
if ($pipPedidos.Count -gt 0) {
  $nombresPip = @($pipPedidos | ForEach-Object { $_[1] })
  if ($py) {
    # Verificacion real: importar cada modulo (antes y despues de instalar)
    $chequeo = Join-Path $env:TEMP 'zea_chequeo_python.py'
    $tuplas = @($pipPedidos | ForEach-Object { '("' + $_[2] + '", "' + $_[1] + '")' }) -join ', '
    $codigo = "import importlib`r`nfor mod, nombre in (" + $tuplas + ",):`r`n    try:`r`n        importlib.import_module(mod)`r`n        print(nombre + '|OK|')`r`n    except Exception as e:`r`n        print(nombre + '|FALTA|' + type(e).__name__ + ': ' + str(e).replace('|', '/')[:160])`r`n"
    Set-Content -LiteralPath $chequeo -Value $codigo -Encoding ASCII

    $faltanPip = @()
    foreach ($l in @(& $py $chequeo 2>$null)) {
      $partes = ([string]$l) -split '\|', 3
      if (($partes.Count -ge 2) -and ($partes[1] -ne 'OK')) { $faltanPip += $partes[0] }
    }
    if ($Simular) {
      foreach ($n in $nombresPip) {
        if ($faltanPip -contains $n) {
          Write-Host ("  {0,-30} FALTA -> instalaria: python -m pip install -U {0}" -f $n)
          Add-Resultado $n 'SIMULADO' ("python -m pip install -U " + $n)
        } else {
          Write-Host ("  {0,-30} OK" -f $n)
          Add-Resultado $n 'OK' ''
        }
      }
    } else {
      if ($faltanPip.Count -gt 0) {
        Write-Host ""
        Write-Host ("  Paquetes de Python: {0}." -f ($faltanPip -join ', '))
        if ($faltanPip -contains 'openai-whisper') {
          Write-Host "  whisper baja torch (varios cientos de MB): 5-20 minutos sin mostrar nada es normal."
        }
        & $py -m pip --version 2>$null | Out-Null
        if ($LASTEXITCODE -ne 0) {
          Write-Host "  pip no estaba: lo instalo con ensurepip..."
          & $py -m ensurepip --upgrade 2>$null | Out-Null
        }
        & $py -m pip install -U -q --disable-pip-version-check --progress-bar off @faltanPip
        if ($LASTEXITCODE -ne 0) {
          Write-Host "  Reintento con --user (instalacion solo para tu usuario)..."
          & $py -m pip install -U -q --user --disable-pip-version-check --progress-bar off @faltanPip
          $userScripts = & $py -c "import sysconfig;print(sysconfig.get_path('scripts','nt_user'))" 2>$null
          if ($LASTEXITCODE -eq 0 -and $userScripts) { Add-UserPathFront ([string](@($userScripts)[0])) }
        }
      }
      foreach ($l in @(& $py $chequeo 2>$null)) {
        $partes = ([string]$l) -split '\|', 3
        if ($partes.Count -lt 2) { continue }
        $det = ''
        if ($partes.Count -ge 3) { $det = $partes[2] }
        if ($partes[1] -eq 'FALTA' -and $partes[0] -eq 'openai-whisper' -and ($det -match 'DLL|WinError 126|c10|fbgemm')) {
          $det = 'falta Microsoft Visual C++ Redistributable: winget install -e --id Microsoft.VCRedist.2015+.x64 y reabri la app'
        }
        Write-Host ("  {0,-30} {1,-5} {2}" -f $partes[0], $partes[1], $det)
        Add-Resultado $partes[0] $partes[1] $det
      }
    }
    Remove-Item -LiteralPath $chequeo -ErrorAction SilentlyContinue
  } elseif ($Simular) {
    foreach ($n in $nombresPip) {
      Write-Host ("  {0,-30} FALTA -> instalaria con pip, despues de Python" -f $n)
      Add-Resultado $n 'SIMULADO' 'primero Python'
    }
  } else {
    Write-Host ""
    Write-Host "  Python FALTA: no instalo los paquetes de Python. Corre este script de nuevo cuando Python este instalado."
    Add-Resultado 'paquetes de Python' 'FALTA' 'primero Python (winget install -e --id Python.Python.3.12)'
  }
}

# --- 4. libass (subtitulos) --------------------------------------------------------------------------------
$ff = $null
if (Test-Quiero 'ffmpeg') { $ff = Find-FFmpeg }
if ($ff) {
  $filtros = & $ff -hide_banner -filters 2>$null
  if ($filtros -and ($filtros | Select-String -Pattern ' (ass|subtitles) ' -Quiet)) {
    Write-Host ("  {0,-30} OK    filtro ass/subtitles presente" -f 'libass (subtitulos)')
    Add-Resultado 'libass (subtitulos)' 'OK' ''
  } else {
    Write-Host ("  {0,-30} FALTA ese ffmpeg no trae libass" -f 'libass (subtitulos)')
    Add-Resultado 'libass (subtitulos)' 'FALTA' ("$ff no trae libass: winget install -e --id Gyan.FFmpeg")
  }
}

# --- 5. PYTHONUTF8=1 (al final: setx avisa a Windows que cambiaron las variables, incluido el PATH) --------
$utf8Antes = [System.Environment]::GetEnvironmentVariable('PYTHONUTF8', 'User')
if ($utf8Antes -eq '1') {
  # Si tocamos el PATH, setx avisa a Windows que cambiaron las variables (los programas nuevos lo ven)
  if ($Cambios -and (-not $Simular)) { & setx PYTHONUTF8 1 | Out-Null }
  Write-Host ("  {0,-30} OK    (variable de usuario)" -f 'PYTHONUTF8=1')
  Add-Resultado 'PYTHONUTF8=1' 'OK' 'variable de usuario'
} elseif ($Simular) {
  Write-Host ("  {0,-30} FALTA -> haria: setx PYTHONUTF8 1" -f 'PYTHONUTF8=1')
  Add-Resultado 'PYTHONUTF8=1' 'SIMULADO' 'setx PYTHONUTF8 1'
} else {
  & setx PYTHONUTF8 1 | Out-Null
  $Cambios = $true
  if ([System.Environment]::GetEnvironmentVariable('PYTHONUTF8', 'User') -eq '1') {
    Write-Host ("  {0,-30} OK    (variable de usuario)" -f 'PYTHONUTF8=1')
    Add-Resultado 'PYTHONUTF8=1' 'OK' 'variable de usuario'
  } else {
    Write-Host ("  {0,-30} FALTA" -f 'PYTHONUTF8=1')
    Add-Resultado 'PYTHONUTF8=1' 'FALTA' 'corre: setx PYTHONUTF8 1'
  }
}

# --- 6. Resumen ----------------------------------------------------------------------------------------------
$faltan = @($Resumen | Where-Object { ($_.Estado -ne 'OK') -and ($_.Estado -ne 'SIMULADO') })
$simulados = @($Resumen | Where-Object { $_.Estado -eq 'SIMULADO' })
$texto = New-Object System.Collections.ArrayList
[void]$texto.Add('')
[void]$texto.Add('===== RESUMEN (' + (Get-Date -Format 'yyyy-MM-dd HH:mm') + ') =====')
foreach ($r in $Resumen) { [void]$texto.Add(("  {0,-8} {1,-30} {2}" -f $r.Estado, $r.Nombre, $r.Detalle)) }
[void]$texto.Add('')
if ($Simular) {
  [void]$texto.Add(("SIMULACION: no se instalo nada. Instalaria {0} cosa(s)." -f $simulados.Count))
} else {
  if ($faltan.Count -eq 0) {
    [void]$texto.Add('TODO OK.')
  } else {
    [void]$texto.Add(("{0} cosa(s) en FALTA. Volve a correr este script (retoma solo lo que falta)." -f $faltan.Count))
  }
  if ($Cambios) {
    [void]$texto.Add('SIGUIENTE PASO: cerra la app de Claude DEL TODO y volvela a abrir (si queda un icono de Claude')
    [void]$texto.Add('junto al reloj, clic derecho -> Salir). Asi toma Git Bash, el PATH nuevo y PYTHONUTF8.')
    [void]$texto.Add('Despues escribi "sigamos".')
  } else {
    [void]$texto.Add('No se instalo nada nuevo: no hace falta reiniciar la app de Claude.')
  }
}
foreach ($l in $texto) { Write-Host $l }
if (-not $Simular) {
  try {
    $dirLog = Split-Path $Log -Parent
    if (-not (Test-Path -LiteralPath $dirLog)) { New-Item -ItemType Directory -Path $dirLog -Force | Out-Null }
    Set-Content -LiteralPath $Log -Value $texto -Encoding ASCII
    Write-Host ("(resumen guardado en {0})" -f $Log)
  } catch { }
}

if ($faltan.Count -eq 0) { exit 0 } else { exit 1 }
