# Rutina · Detector de fatiga + propuesta de iteraciones (lunes 9:00)

Los ganadores se cansan. Esta rutina detecta cuáles están en fatiga y te propone cómo exprimirlos sin tocar lo que vende, con costo casi cero. Solo propone.

## Antes de programarla
Claude necesita ver tus números. Opciones (de más simple a más automática):
- Cada lunes exportás desde el Administrador de Anuncios un CSV de los últimos 14 días a nivel anuncio (gasto, compras, costo por compra) y lo dejás en `RAW/metricas/AAAA-MM-DD.csv`.
- O tenés tu herramienta de tracking conectada a Claude Code y la rutina la lee directo.

## Cómo programarla
Pedile a Claude: *"Creá una tarea programada todos los lunes a las 9:00 con este prompt"*.

```text
Rutina semanal de fatiga para [PRODUCTO], campaña [NOMBRE DE LA CAMPAÑA].
1. Leé WIKI/reglas-ads.md y ADS/[PRODUCTO]/registro.csv.
2. Leé las métricas de los últimos 7 días contra los 7 anteriores desde [RAW/metricas/ÚLTIMO CSV | MI HERRAMIENTA DE TRACKING].
3. Analizá a nivel CAMPAÑA primero: si la campaña está en ganancia, no propongas pausar nada (un anuncio que no vende directo puede estar sosteniendo las ventas de otro).
4. Marcá "en fatiga" los ganadores cuyo costo por compra subió más de [30]% contra la semana anterior con gasto comparable. Traducí cada uno a su archivo real (mp4 y audio exactos) con registro.csv y leé sus notas.
5. Para cada ganador en fatiga proponé con /iterar-winner:
   - 5 microvariaciones: qué clips de ADS/[PRODUCTO]/clips/ usaría cada una y 5 wordings del texto del hook en pantalla (mismo mensaje).
   - 5 iteraciones de hook hablado al MISMO dolor (5 puertas distintas), con el resto del guion literal.
   - Presupuesto: debería ser casi cero. Si algo requiere generación, decime qué y cuánto.
6. Guardá la propuesta en OUTPUTS/[AAAA-MM-DD]-fatiga-[PRODUCTO].md.
7. No produzcas nada sin mi OK.
```
