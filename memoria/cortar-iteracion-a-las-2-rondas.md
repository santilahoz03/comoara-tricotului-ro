---
name: cortar-iteracion-a-las-2-rondas
description: cuando un pipeline automático (videos, landings, scripts) sale con defectos y ya hubo dos rondas de corrección — no empezar la tercera, cambiar de enfoque
type: feedback
fecha: 2026-10-02
---

**Regla:** dos rondas de corrección sobre un pipeline automático. Si a la tercera sigue mal, se para
y se propone otro camino (manual o distinto) con estimación de tiempo real.

**Por qué:** caso real: 4 horas perdidas en 6 rondas de ajuste de un pipeline de videos; cada ronda
arreglaba 2 cosas y rompía 3. El método manual tardaba 10 minutos por video.

**Cómo aplicar:** ronda 1 falla → un arreglo puntual. Ronda 2 falla → buscar la causa de fondo del
enfoque. Ronda 3 no se empieza: se muestra la alternativa y se espera el OK.
