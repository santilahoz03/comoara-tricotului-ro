# Renovación de creativos (sistema 70/30)

> **Estado:** parcial
> **Actualizado:** 2026-10-08
> **Fuentes:** `RAW/zea-sistema-renovacion-creativos.pdf` (mentoría ZEA, "Sistema 70/30" v1.0, 07/10/2026)
> **Relacionado:** [[reglas-ads]], [[negocio]], [[criterios-oferta]]

## En corto
Ciclo **cargar → analizar → guardar → iterar → medir → aprender**. Cada tanda son **6 piezas**: normalmente 4 macro (R/I) y 2 micro (M), para llegar a **70% macro / 30% micro** acumulado. Todo se registra en una base con IDs y `parent_id`: `ADS/_base-renovacion/`.

## Qué sé
- **Macro** = cambia ángulo (razón principal de compra), formato creativo (demo, UGC, b-roll con voz, estática, comparativa, historia animada) o formato de guion (problema-solución, tutorial, historia, lista, objeción-respuesta, comparación). **Micro** = ejecución: wording del hook, primer clip dentro del mismo recurso, texto en pantalla, ritmo, subtítulos, CTA equivalente; se varía una sola cosa por pieza. (`RAW/zea-sistema-renovacion-creativos.pdf`, pág. 3)
- **Tipos:** R = concepto nuevo con 2+ dimensiones macro distintas (explorar). I = cambiar una dimensión macro y mantener las demás (investigar una hipótesis). M = variación de un ganador reciente y verificado, con una sola microvariable. (pág. 6)
- **Insumos:** paquete creativo (ID, archivo, guion literal, texto en pantalla), paquete de métricas por ID y período (gasto, impresiones, clics, visitas, compras, ingresos; moneda, fuente, ventana de atribución) y contexto de negocio (producto, país, precio, CPA objetivo). Con solo métricas no se deduce ángulo ni guion; con solo anuncios no se declaran ganadores. (pág. 4)
- **Diagnóstico en tres capas:** hecho, hipótesis, próximo test. Nunca correlación como causa. (pág. 4)
- **Veredictos:** ganador (cumple criterio con evidencia suficiente) · prometedor (señal favorable por validar) · no funcionó en este test (exposición suficiente y criterio incumplido) · sin veredicto (poco gasto, muestra corta o datos incompletos). Gasto bajo y cero ventas no bastan para declarar perdedor. (pág. 6)
- **Calibración:** el usuario define CPA objetivo, mínimo de compras, período y gasto mínimo de evaluación; si faltan, se proponen para revisar y las conclusiones quedan provisionales. (pág. 6)
- **Mix:** 6 piezas por tanda, aproximadamente 4 macro + 2 micro. Para 70/30 en cinco tandas: tres de 4/2 y dos de 5/1 = 21 macro y 9 micro. El reparto es por piezas, no por presupuesto. Sin ganador reciente, se prioriza explorar y se registra la excepción. (pág. 6)
- **Ejemplo didáctico:** de un ganador (A001) salen 6 ideas: I (formato), I (guion), I (ángulo regalo), R (comparativa), y 2 micro (hook, primer clip) con `parent_id=A001`. (pág. 7)

## Decisiones tomadas
| Fecha | Decisión | Motivo | Fuente |
|---|---|---|---|
| 2026-10-08 | Base común para todas las ofertas en `ADS/_base-renovacion/` | Comparar aprendizajes entre productos y mantener un historial único | pedido de instalación del usuario |
| 2026-10-08 | Este sistema (6 piezas por tanda) prevalece sobre la rutina `renovacion-diaria` del kit 03 (lote de 10) | El PDF figura como instrucción vigente al 07/10/2026 y la rutina del kit no está programada | `RAW/zea-sistema-renovacion-creativos.pdf`, pág. 10 |
| 2026-10-08 | Los 32 anuncios de lanzamiento se importan con los campos de análisis en "no observado" | No inventar ángulo, formato ni guion que no se hayan analizado | `RAW/zea-sistema-renovacion-creativos.pdf`, pág. 8 |

## Abierto / pendiente
- Entregar **métricas por ID y período** (gasto, impresiones, clics, visitas, compras, ingresos; moneda, fuente, atribución) para poder dar veredictos.
- Definir los **criterios de evaluación**: CPA objetivo, mínimo de compras, período y gasto mínimo.
- Correr el primer **Analizar** para completar el desglose de los 32 anuncios.

## Historial / superado

## Salidas relacionadas
