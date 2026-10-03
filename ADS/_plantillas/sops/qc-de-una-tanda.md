# SOP · Control de calidad antes de subir una tanda

> **Windows:** `python` en vez de `python3` (si no existe, `py`); los `.sh` van igual con `bash`; `yt-dlp`/`whisper` sueltos → `python -m yt_dlp` / `python -m whisper`; abrir un archivo → `cmd //c start "" <archivo>`. Subtítulos siempre con `tools/componer.py` (nunca `ass=`/`subtitles=` con una ruta `C:\...`).

No se sube nada sin pasar por acá. Un error de pipeline multiplicado por 10 anuncios es caro.

## 1. Automático, por video
```bash
python3 tools/qc_video.py ADS/<PRODUCTO>/<FECHA>/<N>.mp4 --voz work/<slug>/voz_final.wav \
  --guion work/<slug>/guion.txt --ass work/<slug>/karaoke.ass --idioma <es>
```
| Chequeo | Falla típica | Arreglo |
|---|---|---|
| 9:16 (ancho < alto), h264 + aac | Salió 16:9 porque el formato iba solo en el prompt | Regenerar con `aspect_ratio: "9:16"` explícito |
| Duración voz ≈ video (±1 s) | Video más corto: factor setpts invertido, se comió el CTA | F = duración_voz / duración_video |
| CTA entero al final | Voz truncada (Gemini TTS con texto largo) | Partir en frases de < 25 palabras o pasar a edge-tts |
| Karaoke sin líneas duplicadas | Un «—» o «…» suelto en el guion | Cambiarlo por coma o punto y regenerar el karaoke |

## 2. A ojo, frames cada 2 s (el primer video de la tanda, entero)
- [ ] Subtítulos cortados en los bordes o dos líneas a la vez.
- [ ] Subtítulos que parpadean en las pausas.
- [ ] Restos de texto del original (subtítulos, marcas, cartel final en el idioma viejo).
- [ ] Popups del original que no se recrearon (zona vacía donde había una pastilla).
- [ ] Popups en el momento equivocado (no coinciden con la frase de la voz nueva).
- [ ] Hook con clips de video (no fotos con zoom) y sin clips repetidos en el cuerpo.
- [ ] Voz del género de quien se ve.
- [ ] CTA final en pantalla, en el idioma del anuncio.
- [ ] Música de fondo baja (no tapa la voz), un swell al inicio, un impacto en el CTA.

## 3. De contenido
- [ ] Ningún precio en moneda (salvo anglo de un país con ganancias en dólares).
- [ ] Nada falso sobre el producto (idioma del contenido, formato físico, bonos).
- [ ] Producto digital: nadie sostiene un libro físico que no existe.
- [ ] Cifras de kilos, ingresos o salud → existe la variante `b`.
- [ ] CTA hablado distinto en cada anuncio de la tanda.

## 4. Revisión final
- `python3 tools/preview_grid.py ADS/<PRODUCTO>/<FECHA>` y mirar la grilla completa.
- Tabla por video: OK / FALLA + qué arreglar. No re-renderizar nada sin mostrar la tabla.
- Si un video falla dos veces seguidas con el pipeline automático: dejarlo en `work/revisar/` y hacerlo manual.

## 5. Subida
- Todos los anuncios de la tanda en **un conjunto nuevo dentro de la misma campaña**. Nunca campaña nueva por tanda, nunca editar un anuncio que ya corre.
- Copy de Meta de cada uno desde `guiones.md`.
- Registrar en `ADS/<PRODUCTO>/registro.csv` (id, número, concepto, origen, parent/batch si es iteración, archivo, audio, costo, estado).
