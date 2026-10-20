---
name: scouting-volumen-moderado
description: Scouting diario con ~80 queries y 2-3 agentes, no barridos masivos que queman el rate limit
metadata:
  type: feedback
---

El scouting diario debe usar un volumen moderado de queries (~80-100), con 2-3 agentes a la vez como máximo, igual que las corridas del 2 al 6 de octubre que funcionaron bien.

**Why:** La corrida del 2026-10-08 hizo 400+ queries con 15+ agentes y 5 olas. Quemó el rate limit de Meta y dejó el navegador inutilizable por horas. Además, la calidad bajó (2/9 = 22% vs 50-67% en las primeras corridas): más queries no trajo mejores candidatos, trajo más borderline.

**How to apply:** En cada corrida de la rutina `scouting-diario`: nunca más de 2-3 agentes simultáneos sobre la Biblioteca, máximo ~100 queries totales, nichos productivos probados primero (craft patterns, imprimibles infantiles, material profesional, recetas), y expandir mercados/keywords solo si sobra margen. Nunca hacer "barrido masivo" de 15+ agentes ni 5 olas ni 300+ keywords. Relacionado con [[scouting-calidad-sobre-cantidad]].

**Actualización 2026-10-09:** tope subido a ~100 búsquedas por corrida a pedido del usuario (como los primeros días); sigue prohibido el barrido masivo de 300+.
