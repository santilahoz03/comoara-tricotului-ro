---
name: velocidad-natural-video
description: Los videos replicados deben correr a velocidad natural, lo mas parecida posible al original
metadata:
  type: feedback
---

**Regla:** Los videos replicados deben correr a velocidad natural, como el video original. El factor de `componer.py` (`--factor auto`) debe quedar lo mas cerca posible de 1.0. Un video acelerado (F<0.75) o ralentizado (F>1.15) se nota artificial.

**Por que:** El usuario lo pidio explicito (2026-10-07). Un video acelerado se ve raro: las manos se mueven demasiado rapido, los gestos parecen comicos. Un video ralentizado se arrastra. El ritmo natural del original es parte de lo que convierte.

**Como aplicar:**
1. Generar la voz con duracion similar a la del audio original (comparar `dur(vocals.mp3)` original con `dur(voz.wav)` nueva).
2. Si F queda fuera de [0.75, 1.15], ajustar el guion (acortar o alargar ligeramente) o el `--rate` de edge-tts para que la voz calce mejor. Nunca forzar el video.
3. En ElevenLabs: `stability=0.45` produce duraciones naturales. Valores mas bajos (0.35) aceleran la voz y fuerzan F demasiado bajo.
4. Antes de entregar: verificar visualmente que las manos/gestos del video se mueven a velocidad creible.

Relacionado: [[reglas-ads]]
