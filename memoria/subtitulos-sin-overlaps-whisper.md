---
name: subtitulos-sin-overlaps-whisper
description: Los timestamps de Whisper generan overlaps en el ASS que muestran doble subtítulo — corregir antes de componer
metadata:
  type: feedback
---

Al generar subtítulos karaoke con Whisper (word_timestamps), los timestamps de las palabras naturalmente se superponen. Cuando se agrupan en bloques de ~28 chars y se mapean proporcionalmente a la traducción, los overlaps se conservan. Resultado: dos bloques de texto visibles al mismo tiempo en el video, que parece un error de posición (el texto "salta" arriba y abajo).

**Por qué:** El usuario reportó que "los subtítulos aparecen más arriba, después más abajo". No era un problema de MarginV (todos usaban el mismo). Era que dos Dialogue events con tiempos solapados renderizan uno arriba del otro en libass/ffmpeg. El ad1 aprobado no tenía overlaps; los ads 2-6 tenían entre 19 y 35 cada uno.

**Cómo aplicar:**
1. Después de generar el ASS, verificar overlaps: para cada par de Dialogue events consecutivos, el start del evento N+1 debe ser >= end del evento N.
2. Si hay overlap: `start_N+1 = max(start_N+1, end_N)`.
3. Script de corrección rápido:
   ```python
   prev_end = 0
   for event in events:
       if event.start < prev_end:
           event.start = prev_end
       prev_end = event.end
   ```
4. Hacer esto SIEMPRE después de generar el ASS y ANTES de componer. No esperar a que el usuario lo note.
5. Verificar visualmente el primer video compuesto: si en algún momento se ven dos líneas de texto separadas (no dos renglones de un mismo bloque), hay un overlap que se escapó.

Relacionado: [[subtitulos-posicion-exacta-vmake]], [[subtitulos-sobre-zona-vmake]]
