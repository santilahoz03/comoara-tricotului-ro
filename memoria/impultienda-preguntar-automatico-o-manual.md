---
name: impultienda-preguntar-automatico-o-manual
description: al terminar de modelar una landing (después del QC, antes de tocar ImpulTienda): preguntar al usuario si quiere el modo automático (conector MCP de ImpulTienda) o manual (le entrego todo para que lo haga él)
type: feedback
fecha: 2026-10-08
---

**OBLIGATORIO:** la pregunta se hace SIEMPRE con la herramienta de selector de clic (`AskUserQuestion`), con las dos opciones. **Está prohibido escribir la pregunta como texto del chat.** Si `AskUserQuestion` no figura entre las herramientas cargadas, cargarla primero con `ToolSearch` (`select:AskUserQuestion`). Solo si la herramienta realmente falla o no existe, preguntar por texto y **decir explícitamente** que el selector no estuvo disponible.

**Regla:** nunca me conecto a la ImpulTienda del usuario sin preguntar antes. Cuando la landing modelada está lista y pasó el QC, hago esta pregunta **con el selector de opciones con clic (AskUserQuestion)**, con dos opciones: **Automático** (uso el conector MCP de ImpulTienda y dejo la tienda lista) y **Manual** (no entro a tu cuenta; te paso todo para que la configures vos). Solo si el selector no está disponible, hago la misma pregunta por texto.

- **Si elige automático:** sigo el SOP de modelar (`sops/impultienda.md`, pasos 1 a 7) con el conector MCP de ImpulTienda (regla `impultienda-solo-mcp`), frenando donde el SOP pide su OK (conectar pagos, generar tokens). Nunca escribo contraseñas.
- **Si elige manual:** NO abro su ImpulTienda y **no le envío nada de ImpulTienda al terminar la landing** (se saltea la Fase 7 en ese momento). Seguimos con **los anuncios y los entregables** (Fases 8 a 11) y, **recién cuando ambos estén terminados** (cierre, Fase 12), le entrego **TODO junto** en un archivo en la carpeta de la oferta (por ejemplo `paquete-impultienda-manual.md`) y resumido en el chat. Incluye el **enlace final del hub de entrega** ya publicado y probado, el diseño del checkout, los colores #HEX, todas las URLs, el HTML de la landing y la propuesta de dominio/subdominio. Antes de que lance campañas, la tienda tiene que estar lista: se lo recuerdo al entregar el paquete. Contenido del paquete:
  1. El HTML de la landing modelada como fragmento listo para pegar en *Diseño → Contenido → "HTML completo de la tienda"* (`fragmento.py`, con imágenes hosteadas, sin DOCTYPE/html/head/body).
  2. Datos de la tienda: idioma del contenido, nombre, subdominio y email de contacto (según las reglas guardadas).
  3. Datos del producto: título completo, precios, link de entrega, imagen mockup a subir.
  4. Diseño del checkout bloque por bloque: plantilla de diseño, arriba (cuenta regresiva, imagen), abajo (cupos), botón (texto y color), garantía, order bumps, barra superior y de compradores, datos del comprador (la regla `memoria/datos-comprador-checkout.md` prevalece sobre el default del SOP).
  5. Qué procesador de pagos conectar para ese mercado, según la regla guardada.
  6. **Colores exactos (hex) y URLs completas** en una tabla aparte, sin que falte ninguno (agregado 2026-10-09):
     - **Colores en #HEX:** fondo del botón de pago y color de su texto; color del banner de la cuenta regresiva (rojo oscuro) y de su texto; color del badge de cupos. Salen del `PALETTE.md` de la oferta (el verde oscuro de marca para el botón); si la paleta no trae un verde oscuro, propongo un hex de verde oscuro con contraste suficiente con texto blanco y pido su OK. Nunca escribir solo "verde oscuro" ni "rojo oscuro": siempre el #HEX.
     - **URLs, todas, probadas con respuesta 200:** imagen hero del checkout hosteada en catbox.moe (URL directa) **más la ruta del archivo local**, porque el bloque "Imagen" de ImpulTienda solo acepta archivo y no URL; imágenes de la landing y del producto (catbox); fragmento `.txt` hosteado si se usa para pegar la landing; link de entrega (hub en GitHub Pages con su slug); URL pública de la tienda y su subdominio; landing de referencia y arsenal. Si falta una, avisar cuál y por qué en lugar de omitirla.
  7. Una lista de verificación para que él compruebe que quedó bien.

**Por qué:** pedido del usuario el 2026-10-08: quiere decidir en cada oferta si deja que Claude opere su cuenta o si prefiere hacerlo él, y en ese caso necesita todo el material para no depender de mí.

**Cómo aplicar:** se pregunta una vez por oferta, siempre después del QC de la landing y antes de abrir ImpulTienda. Verificación: no hay ninguna pestaña de ImpulTienda abierta por mí sin que el usuario haya elegido "automático".

**Actualización 2026-10-08:** la pregunta pasó de texto a selector de clic, a pedido del usuario.

**Actualización 2026-10-09 (informe manual):** el usuario pidió que el informe incluya los colores exactos en #HEX de los botones y todas las URLs necesarias (por ejemplo la de la imagen del checkout en catbox).

**Actualización 2026-10-09 (orden del modo manual):** el paquete completo se entrega al cierre, después de anuncios y entregables, no después de la landing.

**Para eliminarla:** borrar este archivo y su línea en `memoria.md` (nada más se modificó).
