---
name: popup-extender-mas-alla-del-video
description: El popup de mockup debe extenderse más allá de la duración del video compuesto, porque atempo lo estira respecto al original
metadata:
  type: feedback
---

El t1 del popup en popups.json debe ser MAYOR que la duración del video compuesto, no solo igual a la del video original.

**Por qué:** Al componer con `componer.py`, la voz nueva casi nunca dura lo mismo que el video original. El factor F (atempo) estira o comprime el video para sincronizarlo. Si F < 1.0 (lo más común), el video compuesto dura más que el original. Un popup con t1 = duración del original deja los últimos 0.3-0.5s sin cubrir, y el mockup/libro original queda visible al final.

**Cómo aplicar:**
1. Después de componer por primera vez, anotar la duración real del video compuesto (la imprime componer.py).
2. Para cada popup, verificar que t1 >= duración_compuesta + 0.5s (margen de seguridad).
3. Si t1 era menor, actualizar popups.json y recomponer.
4. Verificar con ffmpeg extrayendo un frame a (duración - 0.5s) y confirmando que el popup cubre el original.
5. Regla general: si el popup aparece en los últimos 10s del video, poner t1 = duración_compuesta + 1.0 directamente.

Relacionado: [[subtitulos-sobre-zona-vmake]], [[musica-original-identica]]
