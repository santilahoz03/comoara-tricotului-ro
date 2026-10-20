---
name: modelar-set-definitivo-ads
description: en /modelar, tras la Pausa 2 y antes del tracking/lanzamiento, entregar el Set Definitivo para Ads (texto primario, título, descripción) con el estilo del arsenal de la tienda original
type: playbook
fecha: 2026-10-11
---

**Regla:** al terminar el modelado (anuncios aprobados) y antes del tracking (píxel + CAPI) y el lanzamiento, analizo el arsenal de la tienda original (navegador de Claude, link ordenado por impresiones), leo el texto, título y descripción reales de sus anuncios empezando por los de mayor señal, extraigo cómo escribe y entrego un **Set Definitivo para Ads** (Texto Primario + Título + Descripción) para VENDER, en su mismo estilo, adaptado a nuestra oferta, mercado e idioma (no copiado literal).

**Por qué:** el usuario pidió el 2026-10-11 tener un copy de pauta que venda y suene como el de la tienda que funciona. Su ejemplo en italiano (arteterapia) era solo un ejemplo de formato: **la estructura depende de cómo escribe cada tienda original**.

**Cómo aplicar:** vive en `~/.claude/skills/modelar/SKILL.md`, Fase 9b. Entrega en el chat (copiable) y en `OUTPUTS/AAAA-MM-DD-<slug>/set-definitivo-ads.md`, con nota de patrones usados. Cifras, bonos, formato y garantía salen de lo que la landing promete y entrega (nunca del original ni de un ejemplo). Sin precios en moneda multi-país, sin claims de salud/peso/ingresos sin variante compliance, sin testimonios inventados. Un set por oferta salvo pedido. Ver [[modelar-preguntar-modo-y-cantidad-anuncios]].

**Para eliminarla:** borrar este archivo, su línea en `memoria.md` y restaurar `~/.claude/skills-backup/modelar-SKILL-2026-10-11-set-definitivo.md`.
