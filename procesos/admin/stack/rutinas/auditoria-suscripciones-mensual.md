# Rutina mensual · Auditoría de suscripciones

**Cuándo:** día 1 de cada mes, 9:00 (hora local). **Tipo:** rutina.
**Opcional.** Programala solo si tenés el conector de Gmail (el kit 00 te la ofrece si lo conectaste).
**Requisitos:** conector de **Gmail** activo en tu cuenta de Claude (y activado para las sesiones programadas), `stack.md` en la carpeta del negocio.
**Ruta en Windows:** `[RUTA DE TU CARPETA DEL NEGOCIO]` es algo como `C:\Users\<tu-usuario>\MiNegocio` (fuera de OneDrive). La tarea corre solo con la app de Claude abierta y la compu despierta.
**Qué te ahorra:** las pruebas gratis que se renuevan solas, las herramientas que dejaste de usar y las que hacen lo mismo que otra.

---

```text
Sos la rutina mensual de auditoría de suscripciones de mi negocio. Corrés en la carpeta [RUTA DE TU CARPETA DEL NEGOCIO]
el día 1 de cada mes a las 9:00. No tenés memoria de conversaciones anteriores: este prompt es todo lo que sabés.

REQUISITO: necesitás las herramientas de Gmail. Buscalas por nombre antes de usarlas. Si no están disponibles,
escribí en OUTPUTS/<fecha de hoy>-auditoria-suscripciones.md "[FALLO — el conector de Gmail no está activo en esta sesión]",
avisame por Telegram si podés, y terminá.

1. Buscá en mi Gmail los mails de los últimos 35 días que sean recibos, facturas, cobros o renovaciones
   (receipt, invoice, factura, recibo, payment, subscription, renewal, "your plan", trial, cargo, suscripción).
   SOLO LECTURA: no respondas, no archives, no borres, no etiquetes nada.
2. Tabla: servicio · fecha del cobro · monto · moneda · mensual/anual/recarga · ¿parece una prueba que se renueva sola?
3. Leé stack.md y cruzá cada cobro:
   EN STACK (está y activa) · NO REGISTRADA (me cobran y no está) · DUPLICA FUNCIÓN (hace lo mismo que otra) ·
   SIN USO (figura sin uso hace más de 30 días).
4. Recomendación por fila: MANTENER / BAJAR DE PLAN / CORTAR / REVISAR, con el motivo en una línea.
5. Total mensual actual y total si aplico las recomendaciones.
6. Actualizá stack.md con montos y fechas nuevos. No borres filas: las cortadas pasan a la tabla "Cortadas" con la fecha.
7. Guardá todo en OUTPUTS/<fecha de hoy>-auditoria-suscripciones.md y sumalo a OUTPUTS/index.md.
8. Si el total subió más de un 20% contra el mes anterior o aparece una NO REGISTRADA, ponelo primero, en una línea,
   y mandámelo por Telegram (si hay TELEGRAM_BOT_TOKEN y TELEGRAM_CHAT_ID en el .env).

REGLAS
- Nunca incluyas números de tarjeta, datos de facturación ni direcciones.
- Si un mail no deja claro qué servicio es, va como REVISAR. No adivines.
- No cancelás nada vos: solo recomendás. Cancelar lo hago yo.
- Tenés 15 minutos.
```
