# SOP · Costos y tiers: gastar lo mínimo que cumpla

> **Windows:** `python` en vez de `python3` (si no existe, `py`); los `.sh` van igual con `bash`; `yt-dlp`/`whisper` sueltos → `python -m yt_dlp` / `python -m whisper`; abrir un archivo → `cmd //c start "" <archivo>`. Subtítulos siempre con `tools/componer.py` (nunca `ass=`/`subtitles=` con una ruta `C:\...`).

## Referencias medidas (verificá las tuyas: los precios de tabla pueden fallar hasta 10x)
| Recurso | Costo aproximado medido | Alternativa gratis |
|---|---|---|
| Imagen 1K (modelo con texto legible) | ~USD 0,06 | Reusar fotos del producto |
| Clip de video IA de 8 s, modelo barato, 720p | ~USD 3 | Biblioteca de clips de Vmake (`ADS/<PRODUCTO>/clips/`) |
| 20 clips de video IA | ~USD 60 | Idem |
| Lipsync sobre video real | ~USD 0,08 por segundo (falla en clips < 8 s) | Tapar la cara con B-roll del mismo video |
| Voz TTS | Centavos (ElevenLabs) | edge-tts (gratis) o cuota gratis diaria de Gemini |
| Limpieza con Vmake (`videoscreenclear`, vía `tools/vmake_limpiar.py`) | Remover · 0 créditos en la cuenta de Gero (20 corridas, 25-26/09/2026); verificá en tu export de órdenes | Reusar los `clean.mp4` guardados |

Cómo medir el costo real: `python3 tools/kie.py saldo` antes y después de la tanda (y el saldo del panel de Vmake). Anotalo en `WIKI/reglas-ads.md` → «Costos medidos».

## Reglas de gasto
1. **Siempre el modelo, la resolución y la duración más baratos que cumplan:** 720p en video, 1K en imagen, 4 s si el clip se va a ver 1-2 s.
2. **Una variante por prompt**, no tres «por las dudas».
3. **Subís de tier solo después de que el barato falló dos veces seguidas**, nunca por precaución.
4. **Probá con 1 anuncio antes de tirar la tanda entera.**
5. **Avisá antes de cualquier tanda de más de USD 5.**
6. **Reciclá antes de generar:** clips cortados, `clean.mp4`, fotos, audios de ganadores.
7. Antes de una tanda grande, **revisá el catálogo vigente del proveedor**: aparecen tiers más baratos que el que tenés anotado. Si encontrás uno, actualizá `WIKI/reglas-ads.md` en el momento.
8. Los archivos generados en kie.ai duran ~14 días: bajalos siempre.
9. **Vmake: solo `videoscreenclear`** con `tools/vmake_limpiar.py`. Otras tareas (enhancer `hdvideoallinone`, upscale) y la web de Vmake consumen créditos: no se usan.

## Qué formato cuesta qué (de más barato a más caro)
Imagen estática → voz en off + Ken Burns (cero) → B-roll reciclado + voz (cero) → B-roll generado + voz → UGC con avatar solo en el hook → split → talking-head completo.
Producí en ese orden y frená después de cada uno.

## Presupuesto de una tanda (pegalo antes de generar)
| Ítem | Reuso o generación | Modelo / tier | Cantidad | Costo unitario | Subtotal |
|---|---|---|---|---|---|
| | | | | | |
| **Total** | | | | | **USD** |
Versión alternativa a mitad de precio (reemplazando generación por reuso): [ ]
