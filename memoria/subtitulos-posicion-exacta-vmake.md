---
name: subtitulos-posicion-exacta-vmake
description: Los subtitulos nuevos deben ir en la posicion EXACTA de los originales que borro Vmake, medida pixel por pixel
metadata:
  type: feedback
---

**Regla:** Los subtitulos nuevos deben posicionarse en la MISMA posicion exacta que los subtitulos originales que Vmake borro. Medir pixel por pixel desde los frames originales, no estimar a ojo.

**Por que:** Si los subtitulos no cubren la zona exacta donde estaban los originales, los artefactos de Vmake (manchas borrosas, restos de color) quedan visibles y el video se ve desprolijo. El usuario lo corrigio explicitamente (2026-10-10): "IMPORTANTISIMO QUE QUEDE JUSTO EN EL MISMO LUGAR DE LOS ORIGINALES ASI NO SE NOTA NADA DE LO QUE BORRASTE".

**Como aplicar:**
1. Extraer frames del video ORIGINAL (HD) a 3-4 timestamps donde se vean subtitulos claros.
2. Detectar la posicion Y del highlight karaoke (naranja/rojo) filtrando solo la mitad inferior del frame y buscando bandas horizontales con >30px de ancho de color significativo.
3. Tomar las mediciones CONFIABLES (donde detecta una sola palabra, no falsos positivos por objetos del mismo color). Descartar outliers.
4. Calcular MarginV = PlayResY - Y_bottom_del_texto (incluyendo ~20px de padding).
5. Confirmar comparando con frames del video CLEAN: los artefactos de Vmake deben estar en la misma zona Y.
6. El MarginV debe ser UNICO por lote si los originales usan la misma plantilla de subtitulos (ej: todos los ads de un mismo anunciante suelen tener MarginV identico).
7. Subtitulos en maximo 2 renglones, font 44 (para idiomas con palabras largas como aleman).
8. Si hay overlays tipo badges (DA REGALARE/DA VENDERE), crear PNGs equivalentes traducidos y agregarlos como popups en componer.py para cubrir los artefactos de esos elementos tambien.

**Ejemplo concreto (Cuir et Atelier, 2026-10-10):**
- Todos los videos originales: subtitulos karaoke a ~65% desde arriba (Y=800-860 en frame de 1280px).
- MarginV correcto = 420 para los 5 videos (antes tenia 310-380, que era demasiado bajo).
- El artefacto de Vmake queda exactamente en Y=800-860, confirmado visualmente en los frames clean.

Relacionado: [[subtitulos-sobre-zona-vmake]], [[musica-original-identica]], [[reglas-ads]]
