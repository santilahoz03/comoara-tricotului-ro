---
name: sop-creativos-compuertas
description: antes de analizar referencias, producir, gastar, publicar o reeditar una VSL: aplicar el SOP ZEA de creativos con sus 6 compuertas de aprobación (en modo réplica y en producción propia)
type: playbook
fecha: 2026-10-08
---

**Regla:** aplico el SOP ZEA de creativos y VSL (`WIKI/sop-creativos-y-vsl.md`). Antes de operar recupero oferta, referencias, permisos, presupuestos y estado del proyecto, propongo la siguiente fase y **pregunto antes de ejecutarla**. Cada aprobación cubre solo el alcance y el máximo comunicados.

**Dos modos, mismas compuertas:**
- **Réplica** de un anuncio ajeno: se mantiene el pipeline y las reglas actuales (`WIKI/reglas-ads.md`: guion fiel, música del original, Vmake con `--confirmar`, subtítulos).
- **Producción propia** (modo nuevo o modo fiel con recursos propios): el flujo del SOP, con ad1 y luego cinco.

**Elección de modo (pregunta fija, con selector de clic — OBLIGATORIO, nunca como texto del chat; si `AskUserQuestion` no está cargada, cargarla con `ToolSearch`):** si el usuario me pasa referencias o pide anuncios **sin dejar claro el modo**, pregunto una sola vez con el **selector de opciones con clic** (herramienta AskUserQuestion), con estas opciones: **Réplica** (copio el anuncio ajeno con tu pipeline: Vmake + voz + karaoke + música original) y **Producción propia** (armo anuncios nuevos con ad1 y después cinco, con las compuertas del SOP). Solo si ese selector no está disponible (por ejemplo en una rutina automática) hago la misma pregunta por texto. Si el modo ya está claro (`/replicar-ad`, `/doblar-ad`, "replicá" = réplica; `/ad-creator`, "producí anuncios propios" = producción propia), no pregunto. Nunca asumo el modo.

**Compuertas (A a F):**
1. **A · Configurar:** presento los cambios y espero OK antes de instalar, conectar o escribir reglas.
2. **B · Analizar y elegir:** confirmo qué referencias analizar (WATCH), muestro el análisis y la propuesta; OK antes de buscar recursos o producir. Mantengo el orden visible del arsenal; no invento ranking ni vistas.
3. **C · Ad1 y gasto:** storyboard y presupuesto desglosado (créditos, USD, extras, reserva, tope). Sin OK explícito del monto no inicio tareas pagas. "Quiero probar" o "me gusta" no aprueban un gasto.
4. **D · Revisar ad1:** entrego una pieza terminada y reproducible con costo real y pregunto qué mantener y qué corregir. No genero las otras cinco con la prueba pendiente.
5. **E · Cinco adicionales:** presupuesto incremental de ads 2 a 6 y total acumulado; segundo OK de gasto. **Cantidad total = la que elija el usuario** (por defecto 6: ad1 + cinco; ad1 cuenta). Con otro N: ad1 + (N-1).
6. **F · Entregar y publicar:** revisión de las seis y entrega. Publicar, lanzar campañas o comprar herramientas requiere una orden aparte.

**Reglas duras:**
- El silencio, el paso del tiempo y los pedidos generales no son aprobación. Un cambio de guion, formato, proveedor, gasto o alcance que exceda lo aprobado se consulta de nuevo.
- Antes de gastar: busco primero en `BIBLIOTECA/`, después clips reales y recién al final Kie; comparo modelos y resoluciones con **tarifas vigentes** (nunca la tarifa de una clase ni el ejemplo del PDF) y uso el costo efectivo del crédito del plan actual. Elijo lo más barato que pase calidad. Tope por tanda por defecto: USD 5 (`TOPE_GASTO_SIN_AVISO_USD`).
- **Vmake siempre con costo y OK:** cada vez que proponga Vmake como solución (limpiar subtítulos, marcas o textos de un video), digo su costo estimado (~2,1 créditos por segundo de video, unos USD 0,014 por segundo con el plan actual; mostrar el total si el video es largo) y pido aprobación **antes** de usarlo. Nunca lo ofrezco como si fuera gratis. En VSL, una limpieza paga se presupuesta antes (SOP, pág. 13).
- Antes de reenviar una tarea, consulto su estado; no repito tareas ya cobradas. No lanzo una tarea que pueda superar el tope. Registro todo en `ADS/_base-renovacion/ledger-gastos.csv`.
- No inventar métricas, evidencia, testimonios, resultados ni funciones. Todo claim debe corresponder al producto. No presentar un personaje generado como cliente real.
- Derechos: guardo autor, URL, licencia y restricciones por recurso. Un clip sin permiso verificado queda como prueba interna.
- **VSL:** conservo el plano original completo y proporcional (sin crop ni zoom sobre la narradora), la voz íntegra y el orden de argumentos; dinamismo con b-roll, gráficos y placas breves; **una sola capa de subtítulos**; no recorto para esconder texto sin una excepción explícita.
- Entrega con QA del MP4 exportado (audio y técnico incluidos), declarando los límites reales de inspección. 9:16 por defecto.
- Cierre: catalogo los recursos en `BIBLIOTECA/`, guardo prompts, costo, QA, feedback y proyecto en `PROYECTOS/`.

**SOP v2 (2026-10-11):** la ejecución de Producción propia sigue `~/.claude/skills/ad-creator/references/sop-claude-exacto.md` (sección «Adaptaciones locales» prevalece): sourcing TikTok/Pinterest/SSSTik antes de generar, `scripts/kie.py` con `aprobacion-adNN.json`, proyecto pesado en `~/Renovaciones-local/<slug>/`, voz ElevenLabs directo, sin Envato, Vmake solo en Réplica.

**Por qué:** el usuario instaló el SOP el 2026-10-08 desde `RAW/zea-sop-creativos-y-vsl.pdf` y aprobó que las compuertas rijan en los dos modos.

**Cómo aplicar:** al recibir un pedido de ads, VSL o gasto, releo esta regla y `WIKI/sop-creativos-y-vsl.md`. Verificación: el pedido "Hacé seis ya" debe terminar en una propuesta de prueba y presupuesto, sin ninguna tarea paga.

**Para eliminarla:** borrar este archivo, su línea en `memoria.md` y el punto 12 de "Cómo trabajás con anuncios" en `CLAUDE.md`.
