# Índice del cerebro

> **Actualizado:** 2026-10-11
> Mapa de todos los temas por área, con su estado. Lo mantiene Claude. Vos no lo editás a mano.
> Estados: `semilla` (apenas identificado) · `parcial` (base, faltan piezas) · `sólido` (escrito y probado) · `obsoleto`.

## Negocio
| Tema | Estado | De qué va |
|---|---|---|
| [[negocio]] | parcial | Infoproductos digitales replicados; 3 ofertas activas, 5+ modeladas; tickets definidos, anclas pendientes |

## Ofertas
| Tema | Estado | De qué va |
|---|---|---|
| [[criterios-oferta]] | sólido | Filtros, puntaje y criterios para elegir ofertas (ver también carpeta `scouting/`) |
| NeuroMicuți (RO) | activo | Primera oferta lanzada: actividades cognitivas para niños, EUR 17,99, mercado Rumania. Campaña activa desde 2026-10-07. Ver `OUTPUTS/2026-10-04-neuromicuti/oferta.json` |
| Crochet Home Patterns (ANGLO) | activo | Crochet home decor, USD 27, mercado ANGLO (US/UK/CA/AU/NZ). Campañas lanzadas 2026-10-07. 10 réplicas + landing + hub + 5 PDFs. Ver `OUTPUTS/2026-10-06-crochet-home/panel-crochet-home.html` |
| Arteterapia IT | activo | Il Manuale Definitivo di Arteterapia, EUR 17,99, mercado Italia. Campaña lanzada 2026-10-12. 6 ads + landing + hub + 8 PDFs. Ver `OUTPUTS/2026-10-10-arteterapia-it/proyecto/panel-arteterapia-it.html` |

## Marketing
| Tema | Estado | De qué va |
|---|---|---|
| [[sop-creativos-y-vsl]] | parcial | SOP ZEA de creativos y VSL: ad1 + cinco, compuertas de aprobación, WATCH, presupuestos y reedición de VSL |
| [[renovacion-creativos-70-30]] | parcial | Sistema 70/30 de renovación de anuncios (6 piezas por tanda) y su base en ADS/_base-renovacion/ |
| [[reglas-ads]] | sólido | Reglas de creación de anuncios (kit 03) |

## Ventas
| Tema | Estado | De qué va |
|---|---|---|

## Operación
| Tema | Estado | De qué va |
|---|---|---|

## Stack
| Tema | Estado | De qué va |
|---|---|---|
| [[stack-conectores]] | parcial | Conectores, MCP, navegador y herramientas con clave: qué uso, cuál lee y cuál escribe |

## Huecos
Los 3 mayores huecos: qué falta, por qué me limita y qué archivo concreto meto en RAW para taparlo.
> Revisado: 2026-10-11 (revisión semanal).

1. **Métricas de rendimiento de las ofertas activas** — NeuroMicuți (RO), Crochet Home (ANGLO) y Arteterapia IT llevan días en pauta y no hay datos de gasto, CPA, ROAS ni ventas en el cerebro. Por qué duele: no se puede aplicar el sistema 70/30 de renovación (requiere métricas por ID para dar veredictos), ni decidir qué ofertas modeladas lanzar a continuación, ni calibrar presupuesto. Tapalo con: `RAW/2026-10-AA-metricas-semana-1.md` (exportar de Meta Ads Manager: gasto, impresiones, clics, compras, CPA y ROAS por ad, con el período y la ventana de atribución).
2. **Objetivo de 30 días y contexto maestro** — [[negocio]] pasó a `parcial` pero sigue sin un objetivo concreto (cifra de ventas, hito, nicho preferido). Por qué duele: con 40+ ofertas Sí y 5+ modeladas, las decisiones de qué lanzar primero son a ojo; los rankings se hacen sin brújula. Tapalo con: `RAW/2026-10-AA-contexto-maestro.md` (nota de voz de 15-20 min respondiendo las 10 preguntas de `RAW/00-guia-contexto-maestro.md`).
3. **Precios ancla y cobro en Argentina** — ancla sin definir en LATAM, Europa, Anglo y Brasil; AR (ARS 19.990) sin procesador de pago. Por qué duele: no se puede cerrar la landing ni la tienda de ningún mercado sin ancla, y AR hoy no tiene cómo cobrar. Tapalo con: `RAW/2026-10-AA-precios-y-cobro-por-mercado.md` (ancla por mercado + decisión MercadoPago/Stripe para AR).
