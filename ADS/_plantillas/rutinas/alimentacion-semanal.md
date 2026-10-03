# Rutina · Alimentación semanal desde el arsenal de tu referencia

Una vez por semana, Claude revisa el arsenal de tu referencia y te propone la próxima tanda de 10 conceptos con lo que apareció de nuevo. Solo propone: no produce ni gasta.

## Cómo programarla
Pedile a Claude: *"Creá una tarea programada todos los [DÍA] a las 9:00 con este prompt"* y pegá el bloque completo.

```text
Rutina semanal de alimentación para [PRODUCTO].
1. Leé WIKI/reglas-ads.md, ADS/[PRODUCTO]/registro.csv y todos los ADS/[PRODUCTO]/*/arsenal.md anteriores.
2. Abrí el arsenal de mi referencia: [LINK DEL ARSENAL CON search_type=page, view_all_page_id Y ORDEN POR IMPRESIONES].
   Si la Biblioteca devuelve vacío o frena, esperá y reintentá con menos pedidos en paralelo. No concluyas "arsenal vacío" a la primera.
3. Listá los anuncios que aparecieron desde la última revisión. Para los que tengan más señal (versiones, días activo, orden), bajá el audio y transcribilo con tools/transcribir_arsenal.sh. Deduplicá por GUION HABLADO, nunca por caption.
4. Marcá cuáles son conceptos NUEVOS (guion hablado distinto a todo lo ya relevado y a todo lo ya pautado en registro.csv).
5. Proponeme la próxima tanda de 10 conceptos para un conjunto nuevo con /conceptos-zebra: [replicado]/[inventado], nivel de conciencia, hook de 3 s, formato y chequeo de diversidad.
6. Guardá la propuesta en ADS/[PRODUCTO]/[FECHA DE PAUTA PROPUESTA]/conceptos.md y el relevamiento en arsenal.md.
7. No produzcas nada. Avisame con un resumen: cuántos conceptos nuevos encontraste y la tabla de 10.
```
