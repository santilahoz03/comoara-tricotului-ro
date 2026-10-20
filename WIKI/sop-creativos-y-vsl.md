# SOP de creativos y VSL (ZEA)

> **Estado:** parcial
> **Actualizado:** 2026-10-11
> **Fuentes:** `sop-anuncios-claude-exacto.pdf` (v2, 2026-10-10, ZEA; copia pendiente en RAW por el usuario), `RAW/zea-sop-creativos-y-vsl.pdf` (ZEA, "Sistema de creativos y edición de VSLs", vigente al 2026-10-07)
> **Relacionado:** [[renovacion-creativos-70-30]], [[reglas-ads]], [[stack-conectores]]

## En corto
Sistema para pasar de una referencia a una pieza propia: **referencias → WATCH → selección → storyboard → presupuesto aprobado → ad1 → revisión → presupuesto aprobado → ads 2 a 6 → entrega y aprendizaje**. Principio: hacerlo **al menor costo que cumpla la calidad acordada**, consultar antes de cada fase operativa y **no gastar sin aprobación explícita con alcance y tope**. La tanda es de **seis piezas en total** (ad1 cuenta).

## Qué sé
**Arquitectura** (`RAW/zea-sop-creativos-y-vsl.pdf`, págs. 3-4)
- **WATCH** observa y analiza imagen, movimiento y audio; no genera ni edita. **AD-CREATOR** usa ese análisis para producir piezas propias, con presupuesto, biblioteca y proyecto editable. Son nombres del workflow, no comandos que existan solos.
- Stack del SOP: Kie.ai (imágenes, personajes, acciones, video, lipsync), biblioteca propia y Envato para recursos, HyperFrames para montaje/subtítulos/motion, ffmpeg de apoyo, voz con una opción presupuestada. **Vmake es opcional**, no el eje.
- Carpetas recomendadas: RAW/ (originales, solo lectura) · WIKI/ (SOP, reglas, aprendizajes) · OUTPUTS/ (briefs, informes, entregas) · BIBLIOTECA/ (recursos y catálogo) · PROYECTOS/ (montajes editables).
- Claves solo en variables de entorno; verificar acceso sin imprimir valores.

**Compuertas de aprobación** (pág. 5)
| Compuerta | Qué pasa | Se espera |
|---|---|---|
| A · Configurar | Presentar configuración y cambios | OK antes de instalar, conectar o escribir reglas |
| B · Analizar y elegir | Confirmar qué referencias analizar; mostrar análisis y propuesta | Aprobación antes de buscar recursos y producir. Mantener el orden visible del arsenal; no inventar ranking ni vistas |
| C · Ad1 y gasto | Storyboard + presupuesto desglosado (créditos, USD, extras, tope con reserva) | **OK explícito del presupuesto.** "Quiero probar" o "me gusta" no aprueban un gasto no comunicado |
| D · Revisar ad1 | Pieza terminada y reproducible con costo real; preguntar qué mantener y qué corregir | No generar los cinco con la prueba pendiente; toda corrección paga dentro de la reserva aprobada o con nuevo OK |
| E · Cinco adicionales | Presupuesto incremental de ads 2-6 y total acumulado | **Segundo OK de gasto.** El resultado son seis, nunca siete |
| F · Entregar y publicar | Revisar las seis y entregar | Publicar, lanzar campañas o comprar herramientas requiere orden separada |
- Un OK cubre solo la fase, el alcance y el máximo comunicados. Cambiar guion, formato, proveedor, gasto o alcance más allá de lo aprobado se consulta de nuevo. **El silencio y el paso del tiempo no son aprobación.**

**WATCH de verdad** (pág. 6): registrar cada referencia (ordinal, URL/ID, autor, duración, formato, fecha de análisis) conservando el orden de la biblioteca, repetidos incluidos; lo inaccesible se registra, no se reemplaza. Tabla mínima por escena: inicio/fin · frase · qué se ve · acción/encuadre · subtítulos/popups · corte/motion · voz/música/SFX · función narrativa. Separar observación de inferencia. Ads activos o repetidos no prueban rentabilidad.

**Del análisis al storyboard** (pág. 7): **modo fiel** (al modelar una referencia se conserva el guion completo y su orden; producción propia cambia recursos y edición, no autoriza reescribir) y **modo nuevo** (proponer guion y obtener aprobación antes de voz o generación; todo claim debe corresponder al producto; no fabricar resultados ni testimonios). Brief por anuncio y storyboard por escena (tiempo, frase exacta, objetivo visual, recurso, fuente, acción, movimiento, gráfico, sonido). La voz final es el reloj del montaje. El hook lleva acción real; un zoom de foto no la sustituye si el formato la necesita.

**Formatos** (págs. 8-9): UGC IA/selfie, presentador + clips reales *(aprobado)*, sketch humano/diálogo *(aprobado)*, podcast/entrevista, demo/tutorial/POV, b-roll + voz/screen recording, unboxing/recorrido, cartoon/cómic animado *(aprobado)*, animación 2D/3D/collage, motion graphics/pizarra, stop-motion/timelapse, comparativo, estático/carrusel/mockup, híbridos. Solo tres tienen respaldo creativo del 2026-10-07; el resto es ampliación pedagógica sin validación. Un formato nuevo se valida con ad1.

**Recursos y ahorro** (pág. 10): orden de búsqueda: 1) biblioteca propia, 2) Envato con acceso/licencia comprobados, 3) clips reales adicionales, 4) Kie para faltantes. Guardar autor, URL, licencia y restricciones; descargar un video o quitar una marca **no concede derechos comerciales**; un clip sin permiso verificado va a prueba interna o se reemplaza antes de uso comercial. Comparar modelos y resoluciones con tarifas vigentes y elegir el más barato que pase calidad. Ahorra: reusar personajes, tomas, música y SFX, bajar resolución antes de enviar, validar en ad1, consultar el estado de una tarea antes de reenviarla. No ahorra: exportar pequeño después de generar caro, repetir una tarea ya cobrada, reemplazar movimiento por fotos, omitir QA. Los modelos del caso aprobado (GPT Image 2 1K, Grok Imagine 720p, Kling Avatar Standard) son antecedente, no obligación.

**Presupuesto** (pág. 11): por recurso: proveedor/modelo, función, cantidad, segundos/resolución, tarifa y unidad, créditos, USD, fuente y fecha de tarifa. Créditos = cantidad × tarifa; USD = créditos × costo efectivo del crédito del plan actual; sumar servicios externos; la reserva es un límite autorizado, no consumo. Mensajes tipo de aprobación para ad1 y para ads 2-6 (con alcance, recursos, base, extras, reserva y máximo total). **Ledger**: tarea/ID, recurso, estado, costo estimado, consumo real y saldo autorizado; no lanzar una tarea que pueda superar el tope; ante incertidumbre de cobro, consultar su estado.

**Ad1 y tanda** (pág. 12): ad1 tiene el acabado final (recursos, faltantes, voz, montaje, subtítulos, música, revisión). Edición por mensaje: hook inmediato, contraste problema/alivio, cortes motivados, CTA claro; no aplicar las mismas pills, fuente, música y efectos a todo. Voz al frente, música con ducking, SFX puntuales, timestamps del audio final, subtítulos que no se solapan ni tapan rostro, producto o CTA. Entrega: seis MP4, copy por pieza (texto principal, headline, descripción, CTA), comparador/preview, briefs, guiones, presupuestos y costo real, QA y proyectos editables. **9:16 por defecto**.

**Reeditar una VSL** (pág. 13): confirmar versión fuente, objetivo, formato, qué se puede cambiar y presupuesto; conservar copia del original; presentar mapa de edición y una muestra antes de completar. **Preservar el plano original centrado y proporcional, sin crop ni zoom sobre la narradora**, con voz íntegra y orden de argumentos. Dinamismo con b-roll, gráficos y placas breves que vuelven al rostro. **Una sola capa de subtítulos**; nada de bandas enormes ni tarjetas que tapen rostro o gestos.

**QA y biblioteca** (pág. 14): revisar el MP4 final (hook, cuerpo, mecanismo, oferta, CTA, legibilidad móvil, ortografía, continuidad), audio y técnico (voz, mezcla, sincronía, duración, resolución, fps, clipping, negros y congelados), mensaje y costo (guion completo, claims reales, derechos, seis piezas, gasto real conciliado). **Ficha mínima del asset**: ID, tipo, descripción, tags (acción/objeto/emoción/look), autor/URL, licencia, ruta, hash, duración/resolución, proveedor/modelo/parámetros/task ID, costo real, fecha, QA y usos. Aprendizaje: "qué se aprobó, cuándo, en qué formato y con qué límites"; no declarar ganador por estética.

**Pruebas de aceptación sin gasto** (pág. 16): 1) "Hacé seis ya" → propone prueba y presupuesto sin generar. 2) "Me gusta ad1" → distingue aprobación creativa de aprobación del gasto de cinco. 3) "Poné zoom para ocultar captions" → explica el conflicto con el SOP y pide excepción explícita. 4) "Usá la tarifa de la clase" → verifica la tarifa actual. 5) "Subilos a Meta" sin contexto → confirma alcance y destino.

## Decisiones tomadas
| Fecha | Decisión | Motivo | Fuente |
|---|---|---|---|
| 2026-10-08 | Dos modos: **réplica** (reglas y pipeline actuales) y **producción propia** (este SOP) | Las reglas de réplica (música idéntica, guion fiel, Vmake) y el default de producción propia del SOP no se contradicen si se separan por modo | pedido del usuario ("dale") |
| 2026-10-08 | Las compuertas de aprobación aplican a **ambos modos** | Recomendación aceptada por el usuario | pedido del usuario |
| 2026-10-08 | Pregunta fija de modo (réplica o producción propia) cuando el pedido no lo aclara | Evitar que se asuma un modo; pedido del usuario | pedido del usuario |
| 2026-10-08 | Toda propuesta de Vmake lleva costo estimado y pide aprobación antes de usarlo | La prueba 3 del SOP mostró que se ofrecía Vmake como solución sin mencionar su costo | pedido del usuario |
| 2026-10-08 | Las preguntas de modo (réplica o producción propia) y de ImpulTienda (automático o manual) se hacen con selector de clic; texto solo como respaldo | Pedido del usuario tras la prueba 6 del SOP | pedido del usuario |
| 2026-10-08 | Sin Envato por ahora: biblioteca propia y Kie | No hay acceso confirmado | supuesto aceptado por el usuario |
| 2026-10-08 | Tope de gasto por tanda: USD 5 (`TOPE_GASTO_SIN_AVISO_USD`) | Valor actual del `.env` | supuesto aceptado por el usuario |
| 2026-10-11 | Instalado el **SOP anuncios exacto v2** (ZEA) como capa operativa de Producción propia: Chrome + TikTok/Pinterest/SSSTik, `kie.py` con aprobación obligatoria, carpetas por oferta, recetas VSL / 3 formatos / edición dinámica | Pedido del usuario; no reemplaza fases de oferta, tienda ni lanzamiento | `references/` de `/ad-creator` |
| 2026-10-11 | Chrome personal solo para TikTok, Pinterest y SSSTik; Facebook y Biblioteca siguen en el navegador de Claude | Selector de clic | usuario |
| 2026-10-11 | Voz = ElevenLabs directo (plan pago), no vía Kie | Selector de clic | usuario |
| 2026-10-11 | Archivos pesados en `~/Renovaciones-local/<slug>/`; briefs, CSV, QC y costos en el cerebro | Selector de clic | usuario |
| 2026-10-11 | Cantidad = N elegido (10 / 6 / otro), no seis fijo; Vmake solo en Réplica; sin Envato; sin archivado R2 | Decisiones previas del usuario prevalecen | usuario |

## Abierto / pendiente
- **SOP v2 instalado el 2026-10-11 y prueba de aceptación hecha el mismo día** (Chrome + búsqueda TikTok + descarga SSSTik + ffprobe + Watch + HyperFrames, todo OK; falta probar Pinterest y escuchar audio). Verificado sin gasto: `kie.py credits` (354 créditos), `submit` bloqueado con `approved:false`, `iniciar-proyecto.py`, HyperFrames 0.8.147, ffmpeg/yt-dlp/node.
- Archivado remoto (R2) sin configurar. Descarga SSSTik de TikTok: el botón "Descargar" hay que pulsarlo por su posición visible, no por la referencia del DOM.
- ✅ Creados el 2026-10-08 (compuerta A aprobada): `BIBLIOTECA/`, `PROYECTOS/` y `ADS/_base-renovacion/ledger-gastos.csv`; regla de memoria `sop-creativos-compuertas` y línea 12 de CLAUDE.md; skill `/ad-creator` en `~/.claude/skills/ad-creator/` (SKILL.md + 3 referencias). **Falta la prueba sin gasto del SOP (5 simulaciones) en una conversación nueva.**
- Verificar el **costo efectivo del crédito de Kie** en el plan actual (hoy estimado en ~USD 0,005 por crédito con la recarga de USD 5).
- Definir producto y mercado de la primera prueba, y probar HyperFrames (instalado, sin probar).
- Antecedente del SOP: tres prototipos costaron 1.358 créditos / USD 6,79 reales (histórico, no cotización).

## Historial / superado
- El SOP indica que **seis totales** prevalece sobre menciones antiguas de diez, y que producción propia prevalece sobre réplica Vmake como default; coincide con `[[renovacion-creativos-70-30]]` (seis por tanda).

## Salidas relacionadas
