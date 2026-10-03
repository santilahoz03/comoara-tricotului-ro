# SOP · Estilo de montaje de los anuncios

Dos estilos según el origen del video. **Nunca mezclarlos en el mismo anuncio.**

## A. Réplicas y doblajes de videos ajenos: clonar al creador original
El anuncio tiene que parecer hecho por el mismo creador en otro idioma.
- Subtítulos con la misma fuente, color, borde y posición que el original (mirá los frames).
- Popups: mismo color, forma (redondeada, festoneada), posición y orden que el original, **texto traducido fiel**.
- Quote cards (texto oscuro centrado sobre fondo liso): subtítulo centrado en pantalla en esos tramos.

## B. Anuncios propios (B-roll + voz, UGC, Ken Burns, iteraciones)
| Elemento | Especificación |
|---|---|
| Subtítulos | Fuente gruesa (Arial Black o similar), amarilla, borde negro grueso (6-7 px) + sombra, **tercio inferior** (nunca centro vertical), palabra por palabra |
| Tamaño | 4 palabras por línea, ~52 px en 720x1280, márgenes laterales ≥ 54 px, WrapStyle 0 |
| Hook en pantalla | Arriba, fondo semioscuro, primeras 6 palabras, primeros ~2 s |
| CTA en pantalla | Últimos ~3 s, mismo estilo que los subtítulos, con flechas ↓↓ o ▼▼ |
| B-roll | Cortes de 1-1,8 s, clips acelerados ~1,5x, cortes secos, sin repetir el mismo clip dos veces seguidas |
| Voz | Levemente acelerada (~1.15x) para ritmo de anuncio |

## Música y efectos (los dos estilos)
- Música con **licencia libre**, a **-22 dB** (volumen lineal ~0.08), fade in y fade out.
- Elegida según el tono del guion: tierna (regalos, bebés, cosas cute), inspiradora (ingreso extra, transformación), urgencia (ofertas con tiempo). **No la misma para toda la tanda.** Nada de música «divertida» si el tono es aspiracional.
- Efectos: **solo 2**: swell/riser en el segundo 0 (0-1,5 s) + impacto sincronizado con la aparición del CTA (~3 s antes del final).
- Guardá tus pistas en `ADS/_assets/musica/` (ej. `tierna.mp3`, `inspiradora.mp3`, `urgencia.mp3`) y los efectos en `ADS/_assets/sfx/` (`swell.wav`, `impacto.wav`).

## CTA final por idioma
| Idioma | Texto en pantalla |
|---|---|
| Español rioplatense | TOCÁ «MÁS INFORMACIÓN» ▼▼ |
| Español neutro | TOCA «MÁS INFORMACIÓN» ▼▼ |
| Inglés | TAP LEARN MORE ▼▼ |
| Italiano | TOCCA «SCOPRI DI PIÙ» ▼▼ |
| Portugués BR | TOQUE EM «SAIBA MAIS» ▼▼ |
| Francés | APPUIE SUR «EN SAVOIR PLUS» ▼▼ |
| Rumano | APASĂ «AFLAȚI MAI MULTE» ▼▼ |
Grande, centrado o en el tercio inferior, con fondo semitransparente si el video de atrás distrae. El karaoke sigue visible durante el CTA.

## Formato de export
- **9:16 explícito**: 720x1280 (o 1080x1920). Verificar con `ffprobe` que ancho < alto.
- H.264, crf 20, AAC 160 kbps, 30 fps. Un anuncio de 40-70 s pesa 10-17 MB.
- Nombres: `ADS/<PRODUCTO>/<FECHA DE PAUTA>/1.mp4 … N.mp4` en el orden de la ficha; variante compliance `<N>b.mp4`.

## Herramienta
- **HyperFrames (`/hyperframes`)** para subtítulos, popups y motion graphics: describís el video y Claude escribe la composición HTML y la renderiza frame por frame. Es la opción recomendada.
- **ffmpeg** (`tools/componer.py`) como opción B y para cortes, mezcla de audio y mux. Siempre un ffmpeg con libass.
