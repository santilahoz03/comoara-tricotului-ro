---
name: claves-nunca-en-frontend
description: al escribir cualquier HTML/JS que se publica (landing, entregable, chat embebido) o al subir código a GitHub — ninguna clave de API adentro, ni partida en pedazos; va detrás de un proxy del lado del servidor
type: feedback
fecha: 2026-10-02
---

**Regla:** ninguna clave de API (Gemini, kie.ai, ElevenLabs, etc.) va en HTML o JavaScript que vea
el cliente, ni en un repo. Si una página necesita llamar a una API con clave, la llamada pasa por un
proxy del lado del servidor (por ejemplo una edge function de Supabase con lista de orígenes permitidos).
Única excepción: claves "publicables" hechas para el frontend (Stripe publishable, Supabase anon).

**Por qué:** caso real: una clave de Gemini metida en un entregable publicado en GitHub Pages fue
detectada por el escáner de Google y revocada en horas, rompiendo el entregable. El truco de partirla
en pedazos y concatenarla en JS no sirvió: los escáneres la reconstruyen igual.

**Cómo aplicar:** antes de publicar cualquier página o hacer `git push`, buscar en los archivos
`key`, `Bearer`, `sk-`, `AIza` y cadenas largas de letras y números. Verificar que `.env` está en `.gitignore`.
