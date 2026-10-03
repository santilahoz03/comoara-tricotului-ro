---
name: gemini-clave-aiza-y-tts
description: al configurar o usar GEMINI_API_KEY (TTS, análisis de video, imágenes) o cuando Gemini devuelve 401/429 — la clave tiene que ser de AI Studio ("AIza…"), el TTS se trocea por frases y hay respaldo gratis con edge-tts
type: reference
fecha: 2026-10-02
---

**Regla:**
- `GEMINI_API_KEY` tiene que ser una API key de aistudio.google.com/apikey (empieza con `AIza`).
  Un token de login de Gemini CLI (empieza con `AQ.`) no sirve para generar por API: da 401.
- Gemini TTS corta el audio en silencio con textos de más de ~25 palabras por pedido o con
  instrucciones de "leé muy lento". Se trocea por frases y se pide ritmo natural.
- El tier gratis de TTS tiene tope diario. Si da `429 RESOURCE_EXHAUSTED`, pasar a `edge-tts`
  (gratis, sin clave, voces por idioma) en vez de esperar.

**Por qué:** los tres casos pasaron en producción y costaron horas: audios de VSL cortados a la mitad
sin error visible, y una clave equivocada que parecía "caída".

**Cómo aplicar:** la prueba de humo avisa si la clave no empieza con `AIza`. Después de generar un
audio largo, verificar con `ffmpeg -af volumedetect` que no haya silencio al final.

**Actualización 2026-10-02:** una clave de AI Studio que empieza con `AQ.` (creada desde aistudio.google.com/apikey) sí funcionó: lista 50 modelos y generó una voz con `tools/voz.py --motor gemini`. El verificador la marca "REVISAR" por el prefijo, pero no es un error. Antes de descartar una `AQ.`, probarla con una frase de voz gratis.
