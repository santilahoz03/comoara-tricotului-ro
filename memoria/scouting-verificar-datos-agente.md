---
name: scouting-verificar-datos-agente
description: antes de presentar candidatos de scouting, verificar personalmente los datos que reportan los sub-agentes y cruzar con la blocklist completa
metadata:
  type: feedback
---

**Regla:** nunca presentar un candidato basándose solo en lo que reporta un sub-agente. Verificar personalmente: (1) que no esté en la blocklist de `scouting/criterio-aprendido.md`; (2) que los datos (cantidad de anuncios, cantidad de videos, antigüedad) sean correctos abriendo el arsenal en el navegador.

**Por qué:** corrida 2026-10-09 — Gothic Stitch Grimoire fue rechazada el 2026-10-08 ("no tiene videos") y re-presentada el 2026-10-09 porque el sub-agente no cruzó la blocklist. Además, el agente reportó ~17 anuncios con 1 video, pero en realidad eran 6 anuncios todos de imagen. El usuario vio los datos reales y los errores minaron la confianza en el scouting.

**Cómo aplicar:** antes de armar el panel de veredicto: (1) leer la sección Blocklist entera de `scouting/criterio-aprendido.md` y descartar cualquier match; (2) para cada candidato, abrir el arsenal en la Biblioteca y verificar que la cantidad de anuncios, videos y antigüedad coincidan con lo reportado por el agente; si no coinciden, corregir o descartar. Ver también [[scouting-no-repetir-ofertas-vistas]] y [[scouting-verificar-landing-viva]].
