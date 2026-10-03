---
name: tier-mas-barato-siempre
description: antes de disparar cualquier generación con IA (imagen, voz, video, avatar) de más de 3 piezas — confirmar en el catálogo el modelo/tier más barato que cumpla, no confiar en el default anotado
type: feedback
fecha: 2026-10-02
---

**Regla:** en toda generación con IA usar el modelo y el tier más barato que cumpla el objetivo.
Imágenes a 1K, video a 720p, duración mínima útil. Subir de tier solo si el barato falló dos tomas seguidas.

**Por qué:** caso real de la comunidad: una tanda de 18 clips salió con el modelo "rápido" cuando había
uno "lite" a la mitad de precio que servía igual. Y al revés: un modelo de video anotado a 30 créditos
por clip en realidad costaba ~297 (≈ USD 3). Con el precio mal anotado, el presupuesto queda 10 veces abajo.

**Cómo aplicar:**
- Antes de una tanda de más de 3 generaciones: revisar el catálogo del proveedor y el precio real.
- Si un clip se va a usar 2 segundos, generar 4, no 8.
- Antes de generar video, buscar clips reciclables de corridas anteriores (reciclar cuesta cero).
- Mostrar costo estimado y esperar OK si supera `TOPE_GASTO_SIN_AVISO_USD` del `.env`.
- Si aparece una variante más barata que la anotada, actualizar esta regla en el mismo momento.
