---
name: musica-original-identica
description: La musica de fondo de cada ad replicado debe ser la misma del video original, extraida con htdemucs
metadata:
  type: feedback
---

**Regla:** La musica de fondo de cada anuncio replicado debe ser EXACTAMENTE la misma que el video original. Se extrae con htdemucs (pista `no_vocals.mp3`). Si por alguna razon no se puede usar la original, la reemplazo debe ser IDENTICA en estilo, tempo y energia. Nunca musica generica ni de libreria al azar.

**Por que:** El usuario lo pidio explicito (2026-10-05 y 2026-10-07). La musica es parte del ganador: el ritmo, la energia y los cambios estan sincronizados con el copy y las escenas. Cambiar la musica cambia la sensacion del video.

**Como aplicar:**
1. Para cada video original: correr `htdemucs` y obtener `no_vocals.mp3` (la pista instrumental/ambiental).
2. Usar esa pista como `--musica` en `componer.py` con `--vol-musica 0.20` (de fondo, que no compita con la voz). El default anterior era 0.70, que era demasiado alto.
3. Si la pista no_vocals incluye ruido molesto (aplausos, sonidos ambientales del original), avisar al usuario antes de componer.
4. NUNCA usar `--musica none` ni sustituir por musica de Pixabay/libreria sin preguntar.
5. Si el video original no tiene musica (solo voz y ambiente), no agregar musica.

Relacionado: [[reglas-ads]]
