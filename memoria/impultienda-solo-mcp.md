---
name: impultienda-solo-mcp
description: operar ImpulTienda solo con el conector MCP (herramientas impultienda_*), solo cuando sea necesario y el usuario lo pida; nunca con Claude in Chrome
type: playbook
fecha: 2026-10-13
---

**Regla:** para todo lo que haya que hacer en ImpulTienda (leer tiendas, productos, ventas, precios; editar textos o HTML; configurar mercados, pagos, tracking) uso **únicamente el conector MCP de ImpulTienda** (herramientas `impultienda_*`), **solo cuando sea necesario y el usuario me lo pida**. **No uso Claude in Chrome** para ImpulTienda. Si el usuario quiere volver a permitirlo, me avisa.

**Por qué:** el usuario conectó el MCP el 2026-10-13 (v0.2.0, 95 herramientas, 4 tiendas) y pidió que sea la única vía.

**Cómo aplicar:** buscar la herramienta por nombre con ToolSearch (los nombres internos cambian). Lectura libre cuando el usuario lo pida; toda **escritura** (precios, textos, HTML, pagos, dominio, tracking, productos) solo con orden explícita y respetando las pausas de `/modelar` (frenar y pedir OK antes de tocar la tienda; Manual = no entro; nunca conectar procesadores de pago sin preguntar). Si una acción no existe en el MCP, lo digo y no la reemplazo con otra herramienta de escritura. Claude in Chrome sigue solo para TikTok/Pinterest/SSSTik. Ver [[impultienda-preguntar-automatico-o-manual]].

**Para eliminarla:** borrar este archivo y su línea en `memoria.md`, y restaurar `~/.claude/skills-backup/modelar-SKILL-2026-10-13-impultienda-mcp.md` e `impultienda-preguntar-2026-10-13.md`.
