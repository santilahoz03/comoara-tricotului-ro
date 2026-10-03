# Rutina · Renovación diaria de creativos (todos los días a las 8:00)

Con la oferta ya validada, la campaña se alimenta con tandas nuevas a ritmo constante. Esta rutina te deja cada mañana el lote de 10 guiones del día siguiente, listo para aprobar.

## Cómo programarla
1. Completá los `[CAMPOS]` del bloque de abajo.
2. En Claude Code, con la carpeta de tu proyecto abierta, pedile: *"Creá una tarea programada que corra todos los días a las 8:00 con este prompt"* y pegale el bloque (o usá `/schedule`).
3. Si tenés varias ofertas activas, una tarea por oferta, separadas por 15 minutos.

```text
Rutina diaria de renovación de creativos para [PRODUCTO].
1. Leé WIKI/reglas-ads.md, WIKI/patron-[PRODUCTO].md (si no existe, armalo con los ganadores de abajo) y ADS/[PRODUCTO]/combos-usados.md.
2. Corré /guiones-diarios con:
   - Landing: [LINK O RUTA AL TEXTO DE LA LANDING]
   - Ganadores actuales: [RUTAS A LOS guion.txt DE LOS 2-3 GANADORES, O "los marcados como ganador en ADS/[PRODUCTO]/registro.csv"]
   - Mercado, trato y acento: [EJ: LATAM, español neutro con tú, acento neutro]
   - Fecha de pauta: mañana (fecha absoluta AAAA-MM-DD).
3. Reglas: 10 combos únicos con 6 ejes, ningún combo ya usado, al menos 3 niveles de conciencia, texto corrido de un narrador, CTA distinto en cada uno, sin precios en moneda, sin signos sueltos, variante compliance <n>b si hay cifras sensibles, copy de Meta para cada guion.
4. Guardá ADS/[PRODUCTO]/[FECHA DE MAÑANA]/guiones.md y sumá los combos a ADS/[PRODUCTO]/combos-usados.md.
5. NO generes voces, imágenes ni videos. No gastes nada.
6. Al terminar, dejame un resumen de 10 líneas (una por guion: ángulo + hook) y decime cuáles tienen variante compliance.
```

## Tu parte (10 minutos a la mañana)
1. Leé el resumen y los guiones.
2. Aprobá, corregí o descartá. Cada corrección terminala con **"guardalo en reglas-ads"**.
3. Pasá los aprobados a producción con los prompts del LEEME («VO + Ken Burns barato», «iterar un winner», «replicar un anuncio»).
4. Revisá la grilla, subí la tanda como **conjunto nuevo en la misma campaña**.
