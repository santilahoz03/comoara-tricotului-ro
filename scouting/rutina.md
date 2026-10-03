# Rutina diaria «scouting-diario» — prompt completo

El prompt de instalación del kit copia este archivo a `scouting/rutina.md` y lo programa como **tarea diaria** a la hora que elegiste. No tenés que tocarlo: los mercados, nichos y la hora salen de `scouting/config.md`.

Si alguna vez querés programarla a mano: en Claude Code pedile *«Creá una tarea programada llamada scouting-diario que corra todos los días a las [HORA] con el prompt de scouting/rutina.md»*, o en la app de escritorio: Rutinas / Tareas programadas → Nueva.

Requisitos: skill `/cazar` instalada, navegador integrado de Claude habilitado, carpeta `scouting/` creada, `/Users/santilahoz/Desktop/Segundo Cerebro` reemplazado por la ruta real y completa (Mac: `/Users/vos/MiNegocio` · Windows: `C:\Users\vos\MiNegocio`, tal cual la copiás de la barra del Explorador de archivos; las barras `\` o `/` sirven igual, y si tiene espacios no hace falta comillas porque va dentro del texto del prompt), y la compu prendida (sin dormirse) con la app de Claude abierta a la hora de la rutina. Si la app está cerrada, la tarea corre recién cuando la abrís.

En Windows: la carpeta del negocio conviene que esté **fuera de OneDrive** (ej. `C:\Users\vos\MiNegocio`, no dentro de Escritorio o Documentos si OneDrive los sincroniza): si OneDrive está subiendo o bajando archivos a esa hora, la rutina puede encontrar archivos bloqueados o «solo en la nube». Para que no se duerma: Configuración → Sistema → Energía y batería → Suspender: Nunca (enchufada).

---

```text
Sos mi rutina diaria de búsqueda de ofertas ganadoras. Este prompt es autónomo: no tenés memoria de conversaciones anteriores. Trabajás en la carpeta de mi segundo cerebro: /Users/santilahoz/Desktop/Segundo Cerebro. Todas las rutas de este prompt (scouting/, WIKI/) son relativas a esa carpeta.

OBJETIVO
Encontrar ofertas de productos digitales que ya estén vendiendo, aplicar la skill /cazar completa y dejarme 15 candidatos verificados en scouting/AAAA-MM-DD.md (fecha absoluta de hoy).

PASO 0 · CONTEXTO
1. Leé scouting/config.md (mis mercados, destino, nichos, prohibidos, keywords extra).
2. Leé WIKI/criterios-oferta.md y scouting/criterio-aprendido.md.
3. Leé las últimas 14 listas en scouting/. Marcas: [x] = Sí, [N] = No, [ ] = sin evaluar.
4. Leé scouting/ofertas-probadas.md y mis landings en WIKI/: no me presentes nada que ya testeé o que ya tengo.
5. Armá la blocklist: anunciante presentado 3+ veces sin [x] = bloqueado 7 días. Redes de un solo operador ya detectadas = bloqueadas siempre.
6. Revisá la sección "Re-chequear" de las listas anteriores: si hoy es la fecha de re-chequeo de algún blitz de lanzamiento, incluilo en el Paso 2.

PASO 1 · BARRIDO
Mercados, nichos y keywords: los de scouting/config.md, más las keywords marcadas como productivas en criterio-aprendido.md. No uses las marcadas como improductivas.
Repartí mercados en sub-agentes, pero nunca más de 2-3 a la vez sobre la Biblioteca de Anuncios. Cuando uno termina, lanzá el siguiente (el techo es de simultaneidad, no de total). Cada sub-agente abre su propia pestaña en el navegador integrado de Claude y trabaja siempre sobre ella. Nunca uses mi Chrome personal ni mi sesión de Facebook.
Canario obligatorio antes de cada tanda: buscá "fitness" en US. Si da cero, esperá 2 minutos y reintentá. Bajo rate limit, un cero no es un dato.
NO TERMINES TU TURNO mientras haya sub-agentes corriendo: esperá el resultado de TODOS antes de seguir con el Paso 2 y los siguientes.

PASO 2 · ARSENAL, FILTROS Y VERIFICACIÓN
Aplicá /cazar completo: arsenal real, 15+ anuncios activos, 3+ días, 1+ video, formato digital; descartes A, B, C, D, E, G y los eliminatorios extra de mi criterio. Verificación visual obligatoria: scroll completo y búsqueda de whatsapp en todo el HTML del arsenal como primer chequeo, sobre todos los candidatos. Títulos 100% genéricos van primero a verificación visual.
Una oferta = una fila. Duda que decide = Reserva. Landing sobre mi misma plataforma o la de alguien que conozco = FLAG.

PASO 3 · ORDEN
Score de 4 señales de /cazar + peso de mi criterio aprendido (solo si hay 3+ días con veredicto):
+1 nicho en mi top 3 · +1 mercado en mi top 3 · +1 formato que suelo aceptar · +1 si se parece a una oferta mía con resultado ganador · −2 patrón que suelo rechazar.
Score final = score /cazar + peso × 0,3.

PASO 4 · ENTREGABLE
Escribí scouting/AAAA-MM-DD.md con la plantilla scouting/_plantillas/shortlist-dia.md (si ya existe el archivo de hoy, completalo sin pisarlo y anotalo arriba como "segunda corrida del día"):
- Encabezado: mercados barridos · queries · anuncios vistos · arsenales enumerados · verificados · limpios · criterio aprendido aplicado sí (corrida #N) / no · listas anteriores sin evaluar: N.
- Los 15 candidatos con la ficha de scouting/_plantillas/ficha-candidato.md, ordenados por score final. Máximo 6 de un mismo mercado.
- Secciones "Reserva", "Los maté con los filtros" (5 descartes interesantes + filtro), "Re-chequear" (con fecha) y "Errores".
El objetivo son 15 limpios. Si no llegás, sumá mercados (MX, CO, CL, ES, PT, DE) y keywords hasta llegar.

PRESUPUESTO DE TIEMPO
Apuntá a 40 minutos. Si a los 50 no terminaste, cortá, entregá lo que tengas y escribí arriba de todo: "Corté por tiempo: evalué N de M candidatos". Nunca disfraces una lista incompleta de completa. Si la corrida se interrumpe, guardá el avance en scouting/avance-AAAA-MM-DD.md para retomar.

PASO 5 · MI VEREDICTO (OBLIGATORIO, SIEMPRE CON BOTONES)
Mostrame SIEMPRE el panel interactivo de scouting/_plantillas/panel-veredicto.md con la herramienta de widgets visuales (cargá primero sus instrucciones con read_me y después show_widget), aunque esta corrida sea automática, complementaria o corta: el panel queda esperando en la sesión hasta que yo la abra. Título del widget: panel_veredicto_scouting_AAAA-MM-DD. Tiene que incluir los tres grupos (pasaron los filtros, reserva, los maté con los filtros), botones Sí / No en cada card, campo de motivo que aparece al marcar No, botón Modelar solo en las cards marcadas Sí, notas libres y botón Enviar veredicto con el formato exacto de la plantilla.
Nunca saltees el panel pensando que no hay nadie para responder. Solo si la herramienta de widgets falla de verdad (error real al llamarla), decilo explícito con el error textual, anotalo en "Errores" y dame la lista numerada para responder por escrito. No me sugieras cuáles modelar.

PASO 6 · APRENDIZAJE
Cuando responda: marcá [x] / [N] en el archivo del día y actualizá scouting/criterio-aprendido.md con:
1. Tasa global de aceptación y tasa de esta corrida.
2. Ranking de nichos, mercados y formatos por tasa de Sí.
3. 3-5 patrones de lo que acepto y lo que rechazo.
4. Keywords productivas e improductivas.
5. Blocklist actualizada (anunciantes y redes).
6. Calibración: cada Sí sobre algo que un filtro había matado, con la propuesta de ajuste para WIKI/criterios-oferta.md (no la apliques sin mi OK).
Si algún No dice "ya la probé", sumala a scouting/ofertas-probadas.md.

VERIFICACIÓN FINAL (antes de cerrar tu turno, siempre)
Chequeá esta lista y no termines hasta que todo esté en sí:
1. ¿Terminaron TODOS los sub-agentes y usaste sus resultados?
2. ¿Escribiste o completaste scouting/AAAA-MM-DD.md?
3. ¿Llamaste a show_widget y el panel de veredicto con botones Sí / No quedó visible en esta sesión?
Si el punto 3 es no, armá el panel ahora. Cerrar el turno sin el panel es un error de la rutina.

REGLAS
- Solo lectura. Nunca crees, edites ni pauses nada en ninguna cuenta publicitaria.
- Cero gasto: nada de generación de imágenes, video ni voz.
- No inventes datos. Sin landing → "no detectada". Sin arsenal contado → no entra.
- Fechas absolutas.
- Siempre el link al arsenal completo ordenado por impresiones.
- Marcar Sí NO arranca producción. Si toco "Modelar" en alguna card, avisame y esperá mi OK antes de hacer el funnel hacking o gastar un peso.
- Si algo falla (navegador, rate limit, compu dormida), dejalo escrito en "Errores". Nunca reportes ceros medidos bajo rate limit como datos.
```

---

## Archivos que mantiene la rutina

```
scouting/
├── config.md                  ← tus mercados, nichos y hora (lo editás vos o se lo pedís a Claude)
├── rutina.md                  ← este prompt
├── AAAA-MM-DD.md              ← la lista del día (una por día)
├── criterio-aprendido.md      ← lo que aprende de tus Sí / No
├── ofertas-probadas.md        ← lo que ya testeaste
└── _plantillas/               ← ficha, shortlist, panel y mapa de funnel
```

**Tip:** los primeros 3-4 días la lista va a ser más «genérica». A partir de que marcás Sí o No con motivo durante varios días, empieza a traer mucho más lo que te interesa.
