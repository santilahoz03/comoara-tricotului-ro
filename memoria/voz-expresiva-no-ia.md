---
name: voz-expresiva-no-ia
description: La voz en off de los ads debe sonar expresiva, emotiva y humana, nunca robotica ni plana
metadata:
  type: feedback
---

**Regla:** La voz en off de cada anuncio debe ser expresiva y sonar como un humano real. Las preguntas deben sonar como preguntas (entonacion ascendente), las exclamaciones con enfasis, los momentos emotivos con emocion. Nunca puede sonar a IA, robot o lectura plana.

**Por que:** El usuario lo pidio explicito (2026-10-07). Una voz plana o robotica mata la conversion: el espectador desconecta en los primeros 3 segundos. El copy original convierte porque suena a alguien real contando su experiencia.

**Como aplicar:**
1. En ElevenLabs: `voice_settings` con `stability=0.45`, `similarity_boost=0.75`, `style=0.40`, `use_speaker_boost=True`. No subir `stability` por encima de 0.50 (aplana la voz). No bajar por debajo de 0.40 (la voz se vuelve inestable y muy rapida).
2. En edge-tts: usar voces Neural de la region correcta (ej. `es-MX-DaliaNeural` para Mexico).
3. Despues de generar: escuchar los primeros 10 segundos y verificar que las preguntas suenan como preguntas. Si suena plano, regenerar con `style` mas alto (max 0.50).
4. Verificar que la duracion de la voz no sea 10-15s mas corta de lo esperado (sintoma de `stability` muy baja que acelera la voz).

Relacionado: [[reglas-ads]]
