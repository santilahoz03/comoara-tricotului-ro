---
name: scouting-siempre-panel-con-botones
description: al terminar cualquier corrida de /cazar o de la rutina scouting-diario: mostrar siempre el panel de veredicto con botones Sí/No/Modelar, campo "por qué" en los No, aunque la corrida sea automática
type: feedback
fecha: 2026-10-11
---

**Regla:** al final de cada corrida del scouting, armar el panel interactivo con la herramienta de widgets. El panel tiene que incluir:
1. Botones **Sí / No** en cada candidato.
2. Cuando el usuario vota **Sí**: mostrar botón adicional **"Modelar ya"** para marcar esa oferta como prioritaria.
3. Cuando el usuario vota **No**: mostrar un campo de texto **"Por qué"** para que escriba el motivo del rechazo.
4. Campo de notas general al final.
La lista numerada para responder por escrito es solo el plan B cuando la herramienta falla de verdad.

**Por qué:** el 2026-10-02 la primera corrida mostró el panel con botones, pero la segunda lo salteó. El 2026-10-11 (corrida #17) el usuario pidió explícitamente las dos mejoras: "La próxima vez dame la opción para modelar si voto SI, y si voto NO, dejame escribir el POR QUÉ". Sin el motivo del No, el criterio aprendido pierde la razón del rechazo y tiene que inferirla.

**Cómo aplicar:** la rutina cierra con una VERIFICACIÓN FINAL (sub-agentes terminados, archivo escrito, show_widget llamado). Nunca saltear el panel por ser una corrida automática; el panel queda esperando en la sesión. Si el widget falla, citar el error textual en "Errores" y dar la lista numerada. El sendPrompt del veredicto debe incluir el motivo de cada No y cuáles marcaron "Modelar ya". Verificación: la corrida termina con el widget renderizado.
