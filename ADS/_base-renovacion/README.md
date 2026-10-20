# Base de renovación de creativos (sistema 70/30)

> Base común para todas las ofertas. Sistema: `WIKI/renovacion-creativos-70-30.md`. Fuente: `RAW/zea-sistema-renovacion-creativos.pdf`.

| Archivo | Qué es | Una fila por… |
|---|---|---|
| `fichas-anuncios.csv` | Identidad y desglose de cada anuncio | versión de anuncio |
| `metricas.csv` | Resultados | corte (anuncio + período) |
| `aprendizajes.csv` | Hallazgos | hallazgo |

## Reglas
- **ID único** por anuncio: prefijo de la oferta + número (`CHA` Crochet Anglo, `CHMX` Crochet MX, `NMRO` NeuroMicuți RO, `PMPL` Playful Music PL). Cada variante nueva lleva un ID nuevo y `parent_id` apunta a su origen. Si el origen es un anuncio ajeno (réplica), se anota `externo:<id>`.
- **Nunca** sobrescribir guiones ni borrar perdedores. Los registros originales `ADS/<OFERTA>/registro.csv` no se tocan: acá solo se lee de ellos.
- Un dato que no consta se escribe **`no observado`**; si el divisor es cero o falta, **`N/D`**. No se inventa nada.
- Cálculos: CPA = gasto / compras · ROAS = ingresos atribuidos / gasto · CTR enlace = clics / impresiones × 100.
- No sumar períodos que se solapan ni mezclar monedas o fuentes de atribución.
- `tipo_RIM`: R (concepto nuevo, 2+ dimensiones macro distintas) · I (una dimensión macro cambiada) · M (microvariación de un ganador reciente).

## Estado inicial (2026-10-08)
- 32 anuncios importados de los 4 registros de lanzamiento. Guion, ángulo, formatos, hook, prueba, CTA, tipo e hipótesis figuran **no observado**: se completan en el primer *Analizar*.
- `fuente` guarda de dónde salió cada fila (registro, id original, origen, audio y, si la ruta cambió, la ruta anterior).
- `metricas.csv` y `aprendizajes.csv` están vacíos: faltan las métricas por ID de Meta/Utmify.
- Columna agregada al final: `fuente` (no figura en el PDF; sirve para trazabilidad).
