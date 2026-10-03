---
name: skill-es-un-zip
description: cuando el usuario pasa un archivo .skill o .zip para instalar o reemplazar una skill — tratarlo siempre como zip (unzip -l para ver, unzip -o -d para instalar), nunca abrirlo como texto
type: playbook
fecha: 2026-10-02
---

**Regla:** un archivo `.skill` es un zip con otra extensión. Adentro trae `<nombre>/SKILL.md` y
opcionalmente `scripts/` y `references/`.

**Por qué:** si se intenta leer como texto devuelve binario ilegible y se pierde tiempo creyendo que
el archivo está roto.

**Cómo aplicar:** `bash tools/instalar_skill.sh <archivo>` (o `/instalar-skill`). A mano:
`unzip -l archivo.skill` para ver el contenido y `unzip -o archivo.skill -d ~/.claude/skills/` para
instalar (el zip ya trae la carpeta con el nombre). En Windows (Git Bash) sin `unzip`:
`python -m zipfile -l archivo.skill` y `python -m zipfile -e archivo.skill ~/.claude/skills/`. Reemplazar = backup de la vieja, instalar la nueva,
verificar el SKILL.md. Reiniciar la sesión para que aparezca.
