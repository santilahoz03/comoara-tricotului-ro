# Rutina semanal · Salud del stack

**Cuándo:** lunes 9:00 (hora local). **Tipo:** cron disfrazado de rutina: casi no usa IA, solo corre el script y decide si avisar.
**Opcional.** Solo tiene sentido si configuraste Telegram (si no, no tiene cómo avisarte): el kit 00 te la ofrece una vez y, si decís que no, no se programa.
**Requisitos:** `tools/verificar_stack.py` en la carpeta del negocio, `.env` con `TELEGRAM_BOT_TOKEN` y `TELEGRAM_CHAT_ID`.
**Chequea solo tus kits:** el script lee la línea "Kits elegidos" de tu `CLAUDE.md`. Lo de otros kits sale "NO LO USÁS" y nunca dispara un aviso.
**Ruta en Windows:** `[RUTA DE TU CARPETA DEL NEGOCIO]` es algo como `C:\Users\<tu-usuario>\MiNegocio` (fuera de OneDrive). La tarea corre solo con la app de Claude abierta y la compu despierta.
**Cómo se programa:** lo hace el prompt de instalación del kit-00. A mano: pedile a Claude
*"Creá una tarea programada que corra todos los lunes a las 9:00 en esta carpeta con este prompt"* y pegale el bloque.

---

```text
Sos la rutina semanal de salud del stack de mi negocio. Corrés en la carpeta [RUTA DE TU CARPETA DEL NEGOCIO]
todos los lunes a las 9:00. No tenés memoria de conversaciones anteriores: este prompt es todo lo que sabés.

1. Corré: python3 tools/verificar_stack.py --avisar-telegram
   (en Windows: python tools/verificar_stack.py --avisar-telegram — con "python" y "/", nunca python3)
   El script ya te manda un Telegram si hay algo en ERROR, FALTA, BAJO o REVISAR. Si todo está OK, no manda nada.
   Las filas "NO LO USÁS" (kits que no elegí) no son problemas: no las reportes.
2. Si hubo al menos un ERROR/FALTA/BAJO/REVISAR:
   - Escribí OUTPUTS/<fecha de hoy>-salud-stack.md con la tabla completa y, por cada problema, el arreglo sugerido.
   - Agregá una línea en procesos/admin/stack/historico.md: fecha · qué falló.
3. Si todo está OK: no escribas ningún archivo y terminá.

REGLAS
- Nunca imprimas ni copies una clave completa.
- No generes nada, no instales nada, no cambies el .env. Solo diagnosticás y avisás.
- Si el script no existe o Python falla, mandame un Telegram que diga "La rutina de salud no pudo correr: <error>"
  (si podés) y dejalo escrito en OUTPUTS/<fecha>-salud-stack.md.
- Tenés 5 minutos.
```
