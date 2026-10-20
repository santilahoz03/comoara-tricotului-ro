# Oferta modelada · Crochet Home

> **Fecha:** 2026-10-06
> **Modo:** clonado fiel — hay landing real + arsenal real, el usuario no pidió hipertrofiar
> **Mercado destino:** ANGLO · idioma: inglés · trato: inglés US · moneda: USD
> **Fuentes:** landing https://www.uncinetto.shop/ · arsenal https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&is_targeted_country=false&media_type=all&search_type=page&sort_data[mode]=total_impressions&sort_data[direction]=desc&view_all_page_id=1307643689096334
> **Plataforma:** ImpulTienda · subdominio: pendiente
> **Estado:** en armado

## 1 · Señal de ganador (medida, no supuesta)

| Dato | Valor |
|---|---|
| Anuncios activos del arsenal | ~67 |
| Anuncio activo más antiguo (días) | 18 (desde 2026-09-18) |
| Conceptos únicos (dedupe por guion) | 6 |
| ¿Ya se modeló antes? | no — scouteada 2026-10-04, marcada Sí, nunca modelada |

## 2 · La oferta

### Modo A · Clonado fiel (cero bonos nuevos)

| Componente | Nombre original (IT) | Nombre traducido (EN) | Qué es | Valor original | Valor en USD |
|---|---|---|---|---|---|
| Producto principal | Uncinetto per la tua casa · 30 schemi passo passo | Crochet for Your Home · 30 Step-by-Step Patterns | PDF con 30 patrones en 6 categorías (cojines, mantas, caminos de mesa, individuales, posavasos, organizadores) | — | — |
| Bono 1 | Glossario illustrato e guida ai materiali | Illustrated Glossary & Materials Guide | PDF guía de materiales y terminología | €6 | $8 |
| Bono 2 | Guida all'abbinamento dei colori | Color Matching Guide | PDF guía de combinación de colores | €5 | $7 |
| Bono 3 | Guida alla decorazione d'interni | Interior Decoration Guide | PDF guía de decoración | €5 | $7 |
| Bono 4 | Programma per 4 fine settimana | 4-Weekend Program | PDF plan de 4 fines de semana | €6 | $8 |
| **Total declarado** | | | | €22 | **$30** |

- Precio tachado del original: ARS 71.405 (geolocalizado) · Precio final del original: ARS 30.385 (geolocalizado)
- **Mi precio de venta** (tabla del mercado): USD 27 · Ancla: ~$81 (3×) · Ahorro: $54
- Garantía (días del original): 30
- ¿El checkout original vende dos ofertas? no — una sola oferta + 1 upsell post-compra ("Guida alla cura delle coperte", no se incluye en el clon)
- Acceso / entrega que promete: acceso inmediato por email, descarga digital

## 3 · Título único (Fase 5)

- **Título largo** (mockups, checkout, producto): `The Ultimate Crochet Home Decor Vault · 30+ Tested Patterns + 4 Free Bonus Guides`
- **N real** que se entrega: 30 patrones · **K bonos**: 4
- **Título corto** (nombre de la tienda, máx. 5 palabras): Crochet Home Patterns
- Title Case, nunca todo en mayúsculas.

## 4 · Hero

- Headline: Transform Your Home, One Corner at a Time
- Subtítulo: With your own hands, without spending a fortune.
- Botón del hero (baja a la oferta, con ↓): See the Collection ↓
- Botón de la oferta (con el precio en el texto): I Want to Transform My Home · {{price}}

## 5 · Landing

- Prefijo CSS: `chp-` · ancla de la oferta: `#chp-offer`
- Paleta (medida con `paleta.sh`):
  - Fondo: `#FAF8F5` (cream)
  - Fondo alterno: `#FFF` (white)
  - Texto: `#2E2820` (charcoal)
  - Texto secundario: `#6B5F54` (brown)
  - Acento/CTA: `#3D7A5A` (green)
  - CTA hover: `#2F5E44` (dark green)
  - Bordes: `#C4B8AA` (beige)
  - Decorativo: `#EFE8DE` (pill), `#EEF7F0` (guarantee), `#EDE8E1` (dividers)
  - Stars: `#F5A623`
- ¿La paleta la fijan imágenes propias? no — se usa la paleta del ref

| # | Sección del original | Layout | Qué se adaptó |
|---|---|---|---|
| 1 | Banner scrolling (beneficios) | Full width, dark bg, marquee | Texto traducido |
| 2 | Hero (pill + h1 + imagen + social proof + título producto) | Centrado, 1 columna | Texto, social proof "3,500+ customers" |
| 3 | Pain points (carrusel fotos + cards + bridge) | Marquee + cards apiladas + puente italic | Texto, "Pinterest" se mantiene (universal) |
| 4 | Benefits grid (6 cards con lightbox) | Grid 2×3, imagen arriba, texto abajo | Texto traducido, "merceria" → "local yarn store" |
| 5 | What's included (2 cards) | Grid 2 columnas | Texto |
| 6 | Categories (6 cards: Cushions, Blankets, Table Runners, Placemats, Coasters, Organizers) | Grid 2×3 | Nombres de categoría traducidos |
| 7 | Bonuses (4 cards carousel) | Flex horizontal, scroll-snap | Nombres traducidos, valores en USD, tapas con image-to-image |
| 8 | Promise & proof (4 checks) | Box centrado, 1 columna | Texto |
| 9 | Offer/price (CTA al checkout) | Box centrado | Tokens {{price}}, {{original_price}}, botón al checkout |
| 10 | Testimonials (6 cards) | Grid 2×2 | Nombres anglosajones, ciudades US/UK, texto traducido |
| 11 | Summary & guarantee | Box + guarantee box | Tokens precio, "30-Day Money-Back Guarantee" |
| 12 | FAQ (7 preguntas) | Accordion | Texto traducido |
| 13 | Final CTA + imagen Pinterest | Centrado, 1 columna + imagen | Texto traducido |
| 14 | Floating bar | Fixed bottom | Texto + token {{price}} |

**Adaptaciones culturales:**

| Original (IT) | Reemplazo (ANGLO) | Por qué |
|---|---|---|
| Sofia, 27 anni · Milano | Sophie · Portland, OR | Nombre anglo, sin edad |
| Luciana, 41 anni · Roma | Lucy · London, UK | Nombre anglo, sin edad |
| Marina | Emily · Austin, TX | Nombre anglo, sin edad |
| Giulia D. | Jessica D. · Sydney, AU | Nombre anglo, sin edad |
| Camilla R. | Hannah R. · Toronto, CA | Nombre anglo, sin edad |
| Paola M. | Rachel M. · Nashville, TN | Nombre anglo, sin edad |
| "merceria di fiducia" | "local yarn store" | Referencia cultural |
| "fine settimana" | "weekend" | Término local |
| EUR / ARS precios | USD con tokens ImpulTienda | Moneda del mercado |
| "Acquisto verificato" | "Verified Purchase" | Idioma |

**Lo que cambia sí o sí**: testimonios → nombres y ciudades anglo, paquetes → ya es uno solo, hero con botón → ya lo tiene.

**Imágenes**

| Imagen | Tipo | Acción | URL final |
|---|---|---|---|
| Hero packshot | **texto quemado** (IT→EN) | Image-to-image | `https://files.catbox.moe/d888db.png` |
| 5 imágenes marquee patrones | **texto quemado** (IT→EN) | Image-to-image | mq1: `ayti0t.png` · mq2: `mwqic2.png` · mq3: `dracep.png` · mq4: `mnywov.png` · mq5: `xs5pvq.png` |
| 7 imágenes marquee inferior (proyectos) | decorativa | Re-subidas a catbox | listo (48 URLs catbox, 0 supabase/shopify) |
| 6 imágenes benefits grid | decorativa | Re-subidas a catbox | listo |
| 6 imágenes categorías | decorativa | Re-subidas a catbox | listo |
| 4 tapas de bonos | **texto quemado** (IT→EN) | Image-to-image | bonus1: `4wd3ie.png` · bonus2: `llwta3.png` · bonus3: `o4vud2.png` · bonus4: `cuilk2.png` |
| 6 imágenes testimonios | decorativa | Re-subidas a catbox | listo |
| 1 imagen Pinterest final | decorativa | Re-subida a catbox | listo |

Costo total image-to-image: 72 créditos kie.ai (10 traducciones + 2 mockups a 6 cr c/u).

## 6 · Mockups de checkout

- Hero 3:2 fondo blanco: `mockups/1-hero-crochet-home.png` · catbox: `https://files.catbox.moe/hsebxh.png`
- Caja 1:1 con escena: `mockups/2-caja-crochet-home.png` · catbox: `https://files.catbox.moe/kpabu9.png`

## 7 · Tienda

- URL tienda: pendiente · subdominio con SSL activo: pendiente
- Página de entrega (URL fija): pendiente
- Procesador: Whop · métodos locales ON: pendiente
- Checkout default aplicado: pendiente · QC local: pendiente · QC publicado: pendiente

## 8 · Suposiciones (nunca en el texto que ve el cliente)

- (suposición, no confirmado) Los valores declarados de los bonos (€5-€6) se convierten libremente a USD $7-$8 para mantener proporcionalidad; el total declarado no es un precio real sino valor percibido.
- (suposición, no confirmado) El upsell post-compra ("Guida alla cura delle coperte") NO se incluye en el clon porque es un producto separado con precio propio, no un bono incluido.

## 9 · Historial de decisiones

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-10-06 | Modo A (clonado fiel) | Landing real + arsenal real, el usuario no pidió hipertrofiar |
| 2026-10-06 | Prefijo CSS `chp-` (crochet-home-patterns) | Evitar colisión con el original `tct-` |
| 2026-10-06 | Upsell "Guida alla cura delle coperte" excluido | Es producto separado con precio propio, no bono incluido |

## Arsenal · Conceptos deduplicados por guion

| # | Concepto (inicio del texto) | Duración video | Copias estimadas | Señal |
|---|---|---|---|---|
| 1 | "A volte basta un piccolo dettaglio per cambiare l'atmosfera di una stanza…" | 0:42–0:59 (varias versiones) | ~35-40 | **GANADOR** — más duplicado, más viejos (sep 18-19) |
| 2 | "Hai iniziato più di 3 progetti e non ne hai finito nessuno?" | 0:58-0:59 | ~10 | Segundo por volumen (carrusel con 8+ variantes) |
| 3 | "Hai già le basi. Ora immagina cosa potresti creare…" | 0:27 | ~10 | Tercer concepto (agrupado como "10 anuncios" por Meta) |
| 4 | "Ti innamori del colore di un gomitolo… ma sarà quello giusto?" | 0:12 (carousel) | ~3-5 | Concepto bono colores, carrouseles |
| 5 | "Hai tante idee salvate, ma non sai da quale iniziare?" | carousel | ~3-5 | Pinterest angle |
| 6 | "Perché i tuoi progetti all'uncinetto non vengono mai come su Pinterest" | carousel | ~3-5 | Pinterest frustración |
