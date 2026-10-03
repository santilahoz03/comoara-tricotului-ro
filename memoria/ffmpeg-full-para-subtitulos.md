---
name: ffmpeg-full-para-subtitulos
description: al quemar subtítulos (ASS/karaoke) con ffmpeg, o ante el error "No option name near" / "Error parsing a filter description" — usar el ffmpeg con libass (en Mac, ffmpeg-full; en Windows, Gyan.FFmpeg) y cuidar la ruta del .ass
type: reference
fecha: 2026-10-02
---

**Regla:** para cualquier composición con subtítulos usar el ffmpeg que tiene libass. En Mac con
Homebrew: `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` (el `ffmpeg` común del PATH no trae libass).
En Windows, el FFmpeg "full" de gyan.dev (`winget install -e --id Gyan.FFmpeg`) ya trae libass y queda
como `ffmpeg` en el PATH. Para operaciones simples (extraer audio, cambiar tamaño, acelerar) sirve cualquiera.

**Por qué:** sin libass, los filtros `ass` y `subtitles` no existen y ffmpeg tira un error engañoso
(`No option name near '/ruta/x.ass'`) que parece un problema de comillas. Se pierde tiempo peleando
con el escapado cuando el filtro directamente no está. Segunda causa del mismo error: la ruta del
`.ass` tiene espacios.

**Cómo aplicar:**
1. `ffmpeg -hide_banner -filters | grep -E " (ass|subtitles) "` — si no devuelve nada, es libass.
2. Si la ruta tiene espacios: usar `ass=filename=/ruta con espacios/x.ass` o copiar el `.ass` a una
   carpeta temporal sin espacios.
3. En Windows, la letra de unidad (`C:`) también rompe el filtro. Pararse en la carpeta del `.ass` y pasar
   solo el nombre (`-vf "ass=subs.ass"`), o escapar los dos puntos: `ass='C\:/ruta/subs.ass'`.
