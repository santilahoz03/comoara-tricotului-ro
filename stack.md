# Mi stack

> Fuente de verdad de qué pago. La usa la auditoría mensual de suscripciones.
> **Nunca pongas claves acá**: las claves viven solo en `.env`.
> Precios de referencia: verificá siempre el vigente en la web de cada herramienta.

| Herramienta | Función | Plan | Costo/mes | Renovación | Estado | Última vez usada |
|---|---|---|---|---|---|---|
| Claude | Cerebro y ejecución | Max | USD 100 | [FECHA: a confirmar] | activa | 2026-10-02 |
| kie.ai | Imagen, video y voz con IA | créditos | USD 5 (única recarga hasta ahora) | sin renovación | activa | 2026-10-02 |
| ImpulTienda | Tienda y checkout | Plan Max, en prueba gratis (44 días al 2026-10-03) | USD 0 durante la prueba; luego USD 100 por mes (confirmado por el usuario) | ~2026-11-16 (se cobra solo al terminar la prueba) | prueba activa; decidir antes del ~16-nov si seguir | 2026-10-03 |
| Utmify | Tracking | [PLAN] | [MONTO] | [FECHA] | todavía no | |
| AdsUploader | Lanzamiento de campañas | [PLAN] | [MONTO] | [FECHA] | todavía no | |
| Procesador de pago | Cobro | Whop | por venta | — | todavía no | |
| Dominio | Landings y entregables | anual | [MONTO/12] | [FECHA] | todavía no | |
| Vmake | Limpiar videos ajenos para replicar anuncios (kit 03) | Pago (probablemente Pro, 4.500 créditos/mes) | USD 29,99 | [FECHA: confirmar en el panel] | activa hasta fin de ciclo; renovación automática DESACTIVADA (2026-10-03); prueba hecha: ~26 créditos por 12 s | 2026-10-03 |
| ElevenLabs | Voces de los videos y embudo (kits 03 y 05) | Creator (121.000 créditos/mes; hoy 131.000) | USD 22 (el primer mes tuvo descuento) | 2026-11-03 | activa; decidir antes del 3-nov si se mantiene | 2026-10-03 |
| DreamAPI | Avatar que habla para las VSL (kit 05) | créditos prepagos | USD 0 (80 créditos de regalo, sin recarga) | sin renovación | activa; auto top-up OFF | 2026-10-03 |
| GitHub | Páginas de entrega (GitHub Pages) | gratis | USD 0 | — | activa | 2026-10-02 |
| Gemini (AI Studio) | Voz y análisis de video | gratis | USD 0 | — | activa | 2026-10-02 |

## Stack por etapa (no contrates todo el día 1)
| Etapa | Qué sumás |
|---|---|
| Semana 1 · sistema + oferta | Claude + créditos kie.ai (carga chica) |
| Semana 2 · producto + landing | ImpulTienda + Utmify + dominio + procesador de pago + GitHub Pages (gratis) |
| Semana 3 · lanzamiento | AdsUploader (opcional al principio) + caja de pauta separada |
| Semana 4 · backend | DreamAPI (créditos) + Panda Video |
| Escala | Vmake + ElevenLabs si hacen falta |

## Costos por uso de referencia (kie.ai, 1 crédito ≈ USD 0,01 — verificá el vigente)
- 1 imagen `gpt-image-2` a 1K ≈ 6 créditos
- 1 clip de video `veo3_lite` 8 s 720p ≈ 297 créditos
- Ebook de 100 páginas ≈ 600 créditos

## Recargas de créditos (revisar que NO tengan auto-recarga)
- kie.ai: 1.068 créditos al 2026-10-02 (≈ USD 10,68). Recargado: USD 5. Auto-recarga: desactivada (confirmado por el usuario)
- DreamAPI: 64 créditos al 2026-10-03 (regalo; la prueba de avatar gastó 16). Auto top-up: OFF

## Reglas
- Una herramienta por función. Antes de sumar una: ¿qué función cubre?, ¿qué se frena sin ella?, ¿hay alternativa gratis?
- La caja de pauta NO se mezcla con la de herramientas.
- Toda clave vive en `.env`, nunca en este archivo.

## Cortadas
| Herramienta | Fecha de corte | Motivo |
|---|---|---|
