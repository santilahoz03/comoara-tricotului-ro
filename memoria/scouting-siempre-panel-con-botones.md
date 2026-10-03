---
name: scouting-siempre-panel-con-botones
description: al terminar cualquier corrida de /cazar o de la rutina scouting-diario: mostrar siempre el panel de veredicto con botones Sí/No, aunque la corrida sea automática o complementaria
type: feedback
fecha: 2026-10-02
---

**Regla:** al final de cada corrida del scouting, armar el panel interactivo de `scouting/_plantillas/panel-veredicto.md` con la herramienta de widgets. La lista numerada para responder por escrito es solo el plan B cuando la herramienta falla de verdad.

**Por qué:** el 2026-10-02 la primera corrida mostró el panel con botones, pero la segunda (complementaria, automática) lo salteó diciendo "no hay nadie para responderlo" y dejó la lista numerada. El usuario quiere votar con clics: sin feedback fácil la rutina no aprende.

**Cómo aplicar:** la rutina cierra con una VERIFICACIÓN FINAL (sub-agentes terminados, archivo escrito, show_widget llamado). Nunca saltear el panel por ser una corrida automática; el panel queda esperando en la sesión. Si el widget falla, citar el error textual en "Errores" y dar la lista numerada. Verificación: la corrida termina con el widget renderizado.
