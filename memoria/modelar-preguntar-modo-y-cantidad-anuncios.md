---
name: modelar-preguntar-modo-y-cantidad-anuncios
description: en /modelar, al llegar a la fase de anuncios, preguntar con selector de clic el modo (réplica / producción propia) y después la cantidad (10 / 6 / otro)
type: playbook
fecha: 2026-10-10
---

**Regla:** cada vez que modelamos una oferta y, terminada la landing y los pasos siguientes, digo "ahora continuamos con los anuncios" (Fase 9 de `/modelar`), hago dos preguntas seguidas con el selector de clic (AskUserQuestion; ToolSearch si no está cargado; texto solo si el selector no existe, p. ej. rutina automática): (1) modo: **Réplica** o **Producción propia**; (2) cantidad: **10**, **6** u **Otro número** que escribe el usuario. Esa cantidad N rige previsualización, panel y lanzamiento.

**Por qué:** el usuario quiere decidir en cada oferta cómo producir y cuántos anuncios, sin que yo lo asuma; pidió que quedara como regla el 2026-10-10.

**Cómo aplicar:** réplica = pipeline con Vmake y `WIKI/reglas-ads.md`; producción propia = `/ad-creator` (ad1, revisión, segundo OK, ads 2 a N). Vmake siempre con costo y OK; tope USD 5 por tanda con aviso. Ver [[sop-creativos-compuertas]]. Vive en `~/.claude/skills/modelar/SKILL.md` Fase 9.

**Para eliminarla:** borrar este archivo, su línea en `memoria.md` y restaurar `~/.claude/skills-backup/modelar-SKILL-2026-10-10.md`.
