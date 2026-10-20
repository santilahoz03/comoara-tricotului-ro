---
name: subtitulos-sobre-zona-vmake
description: Los subtítulos en videos replicados deben posicionarse exactamente sobre la zona borrosa que dejó Vmake al eliminar los subtítulos originales
metadata:
  type: feedback
---

Los subtítulos del video deben ir sobre la zona borrosa de Vmake para disimular lo que eliminaste.

**Por qué:** Vmake deja artefactos visibles (barras oscuras, zonas borrosas) al eliminar subtítulos quemados. Si los subtítulos nuevos quedan arriba o abajo de esa zona, el artefacto se ve y el video parece amateur.

**Cómo aplicar:**
1. Antes de componer, extraer un frame del video original con subtítulos visibles y medir la posición vertical del texto (en % desde arriba del frame).
2. Extraer el mismo frame del video limpio (clean.mp4) para confirmar dónde quedó la zona borrosa.
3. Calcular el MarginV para el .ass: `MarginV ≈ (1 - posicion_%) × altura_frame_final`. En un frame de 1280px, si el texto original estaba al 75%, MarginV ≈ 320.
4. Cada video tiene su propia posición de subtítulos → MarginV DISTINTO para cada uno. Nunca un valor fijo.
5. Después de componer, verificar con un frame extraído que el texto inglés cubre la zona borrosa.

Relacionado: [[reglas-ads]]
