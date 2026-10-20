---
name: kie-imagen-costo-real
description: El costo real de una imagen 1K en kie.ai es ~USD 0.03, no 0.06
metadata:
  type: feedback
---

Una imagen 1K en kie.ai (GPT Image 2, text-to-image o image-to-image) cuesta ~USD 0,03.

**Why:** El usuario corrigió el costo que figuraba en `tools/kie.py` (decía $0.06). Ya se actualizó el script.

**How to apply:** Al estimar costos de tandas de imágenes, usar USD 0,03 por imagen 1K. Verificar siempre con `python3 tools/kie.py saldo` antes y después de cada tanda para medir el gasto real.
