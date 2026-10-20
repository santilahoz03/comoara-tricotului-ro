# Oferta modelada · Clay Blueprints MX

> **Fecha:** 2026-10-13
> **Modo:** clonado fiel — landing real + arsenal real con 29 días y ~40 ads activos
> **Mercado destino:** MX · idioma: español neutro · trato: tú · moneda: MXN
> **Fuentes:** landing [theclayblueprints.com](https://theclayblueprints.com/) · arsenal [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&is_targeted_country=false&media_type=all&search_type=page&sort_data[mode]=total_impressions&sort_data[direction]=desc&view_all_page_id=1343302345522178)
> **Plataforma:** ImpulTienda · subdominio: pendiente
> **Estado:** Post-PAUSA 1 — landing con imágenes reales, mockups de checkout listos, pendiente QC y anuncios

## 1 · Señal de ganador (medida, no supuesta)

| Dato | Valor |
|---|---|
| Anuncios activos del arsenal | ~40 |
| Anuncio activo más antiguo (días) | 29 (14 sep 2026) |
| Conceptos únicos (dedupe por guion) | ~3-4 ángulos de copy, videos: al menos 2 (0:08 y 0:39) |
| ¿Ya se modeló antes? | no |

## 2 · La oferta

### Modo A · Clonado fiel (cero bonos nuevos)

| Componente | Nombre original | Nombre traducido | Qué es (formato y cantidad) | Valor original | Valor en USD |
|---|---|---|---|---|---|
| Producto principal | The Clay Blueprints Master Library | La Biblioteca Maestra de Plantillas de Cerámica | 150+ plantillas PDF imprimibles, 900+ páginas, 5 categorías (Cocina 70+, Hogar 30+, Jarrones 25+, Macetas 15+, Iluminación 10+), técnicas slab/coil/pinch | ~USD 47 | incluido |
| Bono 1 | Handbuilding Handbook | Manual de Construcción a Mano | Guía práctica de técnicas slab, coil y pinch, uniones, secado, horneado y esmaltado | incluido | incluido |
| Bono 2 | Potter's Project Planner | Planificador de Proyectos del Ceramista | Páginas de planificación, bocetos, registro de arcilla/esmalte/horneado | incluido | incluido |
| Bono 3 | Firing Log & Kiln Tracker | Registro de Horneado y Seguimiento del Horno | Registro de horno, arcilla, esmalte, temperatura, resultados, defectos | incluido | incluido |
| (Incluido) | Commercial Maker License | Licencia Comercial para Artesanos | Permiso para vender piezas hechas con las plantillas | incluido | incluido |

- Precio tachado del original: ~USD 79 (mostrado como ARS 104.189 desde Argentina) · Precio final del original: ~USD 47 (ARS 62.112)
- **Mi precio de venta**: **MXN 219** · Ancla: **MXN 999** (~4.6×) · Ahorro: MXN 780 (78% off)
- Garantía (del original no está explícita, uso la mía): **7 días**
- ¿El checkout original vende dos ofertas? no — es un solo bundle
- Acceso / entrega que promete: "Instant access after purchase — download immediately" → Acceso instantáneo después de la compra

## 3 · Título único (Fase 5)

- **Título largo** (mockups, checkout, producto): `La Biblioteca Maestra de Cerámica · 150+ Plantillas Profesionales Listas Para Imprimir + 3 Guías Bonus Incluidas`
- **N real** que se entrega: 150+ plantillas · **K bonos**: 3
- **Título corto** (nombre de la tienda, máx. 5 palabras): `Plantillas de Cerámica`
- Title Case, nunca todo en mayúsculas.

## 4 · Hero

- Headline (modo A, traducido del original): Deja de medir. Empieza a crear.
- Subtítulo: Plantillas descargables e imprimibles diseñadas para eliminar las dudas en tu trabajo con arcilla. Solo imprime, traza y crea.
- Botón del hero (baja a la oferta, con ↓): VER LA OFERTA ↓
- Botón de la oferta (con el precio en el texto): QUIERO MI ACCESO AHORA — {{price}}

## 5 · Landing

- Prefijo CSS: `cb-` · ancla de la oferta: `#cb-offer`
- Paleta (medida con `paleta.sh`):
  - Fondo principal: `#f4f4f4` (gris claro), `#ffffff` (blanco)
  - Fondo alterno (oscuro): `#1a0f08` (marrón muy oscuro)
  - Fondos cremosos: `#fdf8f2`, `#f5ede0`
  - Texto principal: `#121212` (sobre claro), `#ffffff` (sobre oscuro)
  - Acento/CTA: `#c8722a` (terracota/cobre)
  - CTA hover: `#e4893a` (naranja cobre)
  - Éxito/check: `#22a06b` (verde)
  - Urgencia: `#e05555` (rojo)
  - Bordes/marrón: `#4a3020`
- ¿La paleta la fijan imágenes propias? no — se replica la paleta del ref

| # | Sección del original | Layout (columnas, lado de la imagen, alineación) | Qué se adaptó |
|---|---|---|---|
| 1 | Hero | Full-width foto background (blueprint en mesa) + texto centrado overlay + 3 pasos con íconos | Traducir todo el texto; generar imagen hero con texto en español |
| 2 | Offer Block 1 | 2 cols: izq mockup stack, der bullets + precio + CTA naranja | Traducir bullets, precio a USD 19, ancla pendiente, CTA naranja |
| 3 | Testimonial Carousel | Cards horizontales con foto + 5★ + quote + nombre/lugar | Reemplazar por sección "Qué vas a lograr" (no tengo testimonios reales) |
| 4 | How It Works | H2 + 4 fotos grid (fondo oscuro) + 4 pasos numerados (fondo blanco) | Traducir pasos, fotos decorativas se reusan |
| 5 | What's Included | H2 + 4 cards de producto (imagen + bullets alternando) | Traducir nombres de bonos y bullets, regenerar tapas de bonos en español |
| 6 | Template Preview | Visor interactivo con tabs (Pinch Bowl / Phone Stand) | Traducir tabs y labels; las páginas de ejemplo tienen texto quemado → regenerar |
| 7 | Full Breakdown | 5 cards de categoría + totales por técnica | Traducir categorías e iconos |
| 8 | Comparison Table | Tabla 2 columnas "Otros" vs "The Clay Blueprints" | Traducir todo, checkmarks/X se mantienen |
| 9 | Customer Results | 3-4 fotos UGC con nombre + bandera + estrellas | Reemplazar por "Qué vas a lograr" o quitar (sin UGC real) |
| 10 | Offer Block 2 | Copia exacta del #2 | Mismo que #2 traducido |
| 11 | FAQ | 10 preguntas accordion, fondo oscuro | Traducir las 10 preguntas y respuestas |
| 12 | Reviews Widget (Judge.me) | 4.9★, 85 reviews, barras + cards | Quitar — no tengo reviews reales propias |
| 13 | Footer | Email signup + social + copyright | Traducir, quitar redes del original |

**Adaptaciones culturales** (lo que no viaja y su reemplazo):

| Original | Reemplazo en MX/LATAM | Por qué |
|---|---|---|
| Nombres de testimonios US (Beth H Florida, Diane R Orlando, etc.) | Sección "Qué vas a lograr" con bullets | No tenemos testimonios reales; inventarlos está prohibido |
| Reviews Judge.me (85 reviews reales) | Se quita la sección completa | No se copian reviews ajenas |
| Flags 🇺🇸🇳🇱🇵🇱 en Customer Results | Se quita o reemplaza por "Qué vas a lograr" | Sin UGC real |
| "Commercial Maker License" | "Licencia Comercial para Artesanos" | Adaptar al español |
| Precios en USD 47/79 | USD 19 / ancla pendiente | Precio fijo MX/LATAM |
| "GBP" currency selector | Se quita | ImpulTienda maneja la moneda |
| "10% OFF" floating badge | Se quita | No aplica a nuestra oferta |

**Lo que cambia sí o sí**: marcas "The Clay Blueprints" → nuestro brand · testimonios → sección "Qué vas a lograr" · paquetes → uno solo (ya es uno) · hero con botón.

**Imágenes**

| Imagen | Tipo | Acción | URL final |
|---|---|---|---|
| Hero (blueprint en mesa marrón) | texto quemado → image-to-image ES | Generada con kie.ai GPT Image 2 | `https://files.catbox.moe/krgpmn.png` |
| Mockup stack Offer Block (5 covers + bonus covers) | texto quemado → image-to-image ES | Generada con kie.ai GPT Image 2 | `https://files.catbox.moe/rri1dk.png` |
| Cover Master Library (cerámica en mesa) | decorativa sin texto | Reusada del original | `https://files.catbox.moe/tgbpkm.png` |
| Cover Handbook (tazas esmaltadas) | decorativa sin texto | Reusada del original | `https://files.catbox.moe/ac11k1.png` |
| Cover Planner (taza roja esmaltada) | decorativa sin texto | Reusada del original | `https://files.catbox.moe/ib28ih.png` |
| Cover Firing Log (tazas crudas en taller) | decorativa sin texto | Reusada del original | `https://files.catbox.moe/co95l5.png` |
| Costo total imágenes | — | 12 créditos kie.ai (~USD 0,06) | — |

## 6 · Mockups de checkout

- Hero 3:2 fondo blanco: `https://files.catbox.moe/dua020.png` · local: `mockups/1-hero-clay-blueprints-mx.png` (2.0 MB)
- Caja 1:1 con escena: `https://files.catbox.moe/wdn6bm.png` · local: `mockups/2-caja-clay-blueprints-mx.png` (2.5 MB)
- Costo mockups: 12 créditos kie.ai (~USD 0,06)
- Costo total imágenes (landing + mockups): 24 créditos (~USD 0,12)

## 7 · Tienda

- URL tienda: pendiente · subdominio con SSL activo: no
- Página de entrega (URL fija): pendiente
- Procesador: ImpulPay · métodos locales ON: sí
- Checkout default aplicado: no · QC local: pendiente · QC publicado: pendiente

## 8 · Suposiciones (nunca en el texto que ve el cliente)

- (suposición, no confirmado) El precio original es ~USD 47 (el Shopify muestra ARS 62.112 por geolocalización, no se puede verificar el USD real sin VPN)
- (suposición, no confirmado) El anunciante es probablemente europeo (reviews en alemán, francés, polaco; una review menciona "Jana")

## 9 · Historial de decisiones

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-10-13 | Modo A (clonado fiel) | Landing real + arsenal real de 29 días con ~40 ads activos |
| 2026-10-13 | Mercado MX/LATAM, USD 19, español neutro con "tú" | El usuario lo indicó explícito |
| 2026-10-13 | Testimonios → "Qué vas a lograr" | No tenemos testimonios reales; inventar está prohibido |
| 2026-10-13 | Reviews Judge.me se quitan | No se copian reviews ajenas |
| 2026-10-13 | Procesador ImpulPay | Regla para todo mercado fuera de AR |

## 10 · Arsenal (rankeado por señal de ganador)

| # | ID biblioteca | Desde | Ángulo / Headline | Copy (primeras palabras) | Formato | Varias versiones |
|---|---|---|---|---|---|---|
| 1 | 1845134713123061 | 14 sep | Stop Guessing. Start Building. | "You can do everything right with the clay—and still end up with a piece that's too small…" | Imagen | Sí (varias versiones) |
| 2 | 3331787370543297 | 14 sep | Stop Guessing. Start Building. | "You can do everything right…" | Imagen | Sí |
| 3 | 959314543147950 | 14 sep | Stop Guessing. Start Building. | "You can do everything right…" | Imagen | Sí |
| 4 | 1063137903277083 | 15 sep | Stop Guessing. Start Building. | "You can do everything right…" | Imagen | Sí |
| 5 | 1386091006445009 | 16 sep | Professional Pottery Starts… | "Tired of pottery projects that just don't fit?…" | Imagen | No |
| 6 | 1250029288201316 | 17 sep | Stop Guessing. Start Building. | "You can do everything right…" | Imagen | Sí |
| 7 | 1428055599389671 | 23 sep | Professional Pottery Starts… | "Tired of pottery projects that just don't turn out right?…" | Imagen | No |
| 8 | 960085836520740 | 28 sep | Measure Less. Make More. | "The expensive part isn't the template…" | Imagen | No |
| 9 | 1115288701008782 | 28 sep | Stop Guessing. Start Building. | "You can do everything right…" | Imagen | Sí |
| 10 | 1128198326323984 | 30 sep | — | "The expensive part isn't the template…" | Imagen | 2 anuncios |
| 11 | 1101129838948781 | 30 sep | Measure Less. Make More. | "The expensive part isn't the template…" | Imagen | No |
| 12 | 1647353513402960 | 30 sep | Professional Pottery Starts… | "Tired of pottery projects…" | Imagen | No |
| 13 | 2168111383744291 | 5 oct | — | "There's something so satisfying about watching…" | Video (0:08) | No |
| 14 | 1094180196934111 | 5 oct | Professional Pottery Starts… | "Tired of pottery projects gone wrong?…" | Imagen | No |
| 15 | 1121455616894621 | 10 oct | — | "There's something so satisfying…" | Video (0:08?) | No |
| 16 | 2307438826687420 | 10 oct | — (page follow ad) | "Love slab pottery? 🤎Follow Clay Blueprints…" | — | No |
| 17 | 4697469815902 | 10 oct | — | (no leído, truncado) | — | No |

Ángulos deduplicados por guion:
- **A (ganador):** "You can do everything right with the clay — and still end up with a piece that's too small, badly proportioned…" → "Stop Guessing. Start Building." (repetido en ~8 ads desde el 14 sep, el más viejo y más duplicado)
- **B:** "Tired of pottery projects that just don't fit? Mistakes often happen before you start building…" → "Professional Pottery Starts With Better Proportions"
- **C:** "The expensive part isn't the template. It's remaking the piece. Wrong proportions, resizing, lids that don't fit…" → "Measure Less. Make More."
- **D:** "There's something so satisfying about watching a simple form come to life 🏺💙" → video corto (0:08), más emocional/awareness
