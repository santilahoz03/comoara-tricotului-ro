---
name: subtitulos-mayusculas-color-marca
description: Los subtítulos de ads van siempre en MAYUSCULAS y con el color principal de la marca (sacado de la landing/PALETTE.md)
metadata:
  type: feedback
---

**Regla:** Los subtítulos de cada ad van en MAYUSCULAS (imprenta) y con un color "lindo" que sea el principal de la marca/landing. El color se saca de la paleta medida de la landing (`PALETTE.md`), nunca un blanco genérico.

**Por qué:** El usuario lo pidió explícito (2026-10-07). Las mayusculas son mas legibles en video corto y el color de marca refuerza la identidad visual del producto. Un blanco genérico se pierde.

**Como aplicar:**
1. Antes de componer, leer `PALETTE.md` de la oferta y elegir el color principal (tipicamente el fondo claro o el acento).
2. Convertir a formato ASS `&HAABBGGRR` y aplicar como `PrimaryColour` en el estilo del .ass.
3. `.upper()` sobre el texto visible del ASS (solo el contenido despues de la 9a coma, NUNCA sobre "Dialogue:" ni tags `{}`). Ver regla [[subtitulos-ass-dialogue-keyword]].
4. Outline grueso (8-10px) en color oscuro de la paleta + shadow 4px para contraste.

Relacionado: [[subtitulos-sobre-zona-vmake]], [[reglas-ads]]
