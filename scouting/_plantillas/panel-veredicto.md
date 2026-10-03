# Plantilla · panel de veredicto Sí / No

Cómo Claude te pide el veredicto de la lista del día. **El feedback se da con clicks, no escribiendo**: si cuesta dar feedback, no lo das, y sin feedback la rutina no aprende.

## Qué tiene que mostrar el panel

Un widget interactivo en el chat (en Claude Code / Claude Desktop, con la herramienta de widgets visuales). Título: `panel_veredicto_scouting_AAAA-MM-DD`.

1. **Grupo «Pasaron los filtros»:** una card por candidato con
   `nombre · mercado · N anuncios · V videos · nicho · score`,
   link **Ver arsenal** (formato arsenal ordenado por impresiones),
   botones **Sí** / **No**, y un campo de motivo que aparece solo al marcar No.
2. **Grupo «Reserva — duda abierta»:** mismas cards y botones, con la duda escrita en la card.
3. **Grupo «Los maté con los filtros — marcá Sí si me pasé»:** los descartes interesantes con el filtro que los mató y un botón **Sí** para rescatarlos.
4. **Botón «Modelar»** en cada card, que aparece **solo si esa card está en Sí**. Claude nunca lo pre-marca ni sugiere cuáles.
5. **Notas libres** (textarea).
6. **Botón «Enviar veredicto»** que manda al chat el texto con el formato de abajo. Si no hay nada marcado, muestra un error y no envía.

Si el entorno no puede renderizar widgets, Claude lo dice explícito y te da la lista numerada para responder por escrito (ver prompt «Veredicto por escrito» del LEEME).

## Formato exacto que devuelve el botón (no cambiarlo: el aprendizaje lo parsea)

```
Veredicto scouting AAAA-MM-DD:
SI: Nombre (MKT) · Nombre (MKT)
NO: Nombre (MKT) — motivo · Nombre (MKT) — motivo
RESCATO: Nombre (MKT) — por qué
SIN MARCAR: Nombre (MKT)
NOTAS: <texto libre>
MODELAR YA: Nombre (MKT)
```

Si no se tocó ningún «Modelar», la última línea es `MODELAR YA: ninguno`.

## Reglas del veredicto

- **Sí = cumple mi criterio.** No es «lo voy a modelar». Son dos decisiones distintas.
- **Modelar = decisión aparte**, tuya, sobre la lista de Sí. Aun con «MODELAR YA», Claude espera tu OK antes de gastar.
- **Un No es dato, no filtro:** lo que rechazaste no vuelve aunque después pase todos los filtros.
- **Un RESCATO es una alarma de calibración:** el filtro que lo mató está demasiado duro y hay que revisarlo.
- Motivos cortos y concretos: «marca personal», «catálogo», «ya la probé», «nicho que no me gusta», «operación rota», «no viaja a mi mercado».
