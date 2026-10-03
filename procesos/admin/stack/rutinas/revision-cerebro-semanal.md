# Rutina semanal · Revisión del cerebro

**Cuándo:** domingo 20:00 (hora local). **Tipo:** rutina (usa IA: lee, resume y detecta huecos).
**Para todos** (opcional, pero no necesita claves ni conectores). Telegram al final solo si lo configuraste.
**Requisitos:** la skill `/bibliotecario` instalada y la carpeta del negocio con `CLAUDE.md`, `RAW/`, `WIKI/`, `OUTPUTS/`.
**Ruta en Windows:** `[RUTA DE TU CARPETA DEL NEGOCIO]` es algo como `C:\Users\<tu-usuario>\MiNegocio` (fuera de OneDrive). La tarea corre solo con la app de Claude abierta y la compu despierta.
**Truco:** grabá notas de voz durante la semana, transcribilas y tiralas a `RAW/` con la fecha en el nombre. El domingo esta rutina las procesa sola.

---

```text
Sos la rutina semanal del segundo cerebro de mi negocio. Corrés en la carpeta [RUTA DE TU CARPETA DEL NEGOCIO]
todos los domingos a las 20:00. No tenés memoria de conversaciones anteriores: este prompt es todo lo que sabés.

PASO 0 · Leé el CLAUDE.md de la carpeta (es tu contrato) y memoria.md.

PASO 1 · Procesá RAW (solo lo nuevo según WIKI/changelog.md), siguiendo la skill /bibliotecario, modo A.
(Para transcribir audios hace falta whisper; si no está instalado, no transcribas: anotá el audio como pendiente en
el resumen. En Windows: python -m whisper <archivo> --model small --language es.)
Si no hay nada nuevo, anotalo y seguí.

PASO 2 · Revisión semanal (skill /bibliotecario, modo C):
- temas "semilla" o "parcial" consultados esta semana,
- [[enlaces]] a temas que no existen,
- contradicciones entre temas,
- los 3 mayores huecos en WIKI/index.md → ## Huecos (qué falta · por qué duele · qué archivo meter en RAW).

PASO 3 · Guardá el resumen en OUTPUTS/<fecha de hoy>-revision-semanal.md (máximo 20 líneas) y sumalo a OUTPUTS/index.md.

PASO 4 · Si en .env hay TELEGRAM_BOT_TOKEN y TELEGRAM_CHAT_ID, mandame por Telegram los 3 huecos en 3 líneas.

REGLAS
- RAW es solo lectura. No borres nada de la WIKI: lo viejo va a "Historial / superado".
- No inventes cifras. Fechas absolutas.
- Tenés 20 minutos. Si no terminás, escribí arriba del archivo "Corté por tiempo: procesé N de M archivos".
  Nunca lo presentes como corrida completa.
```
