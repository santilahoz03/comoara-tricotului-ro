# Oferta modelada · Playful Music Method PL

> **Fecha:** 2026-10-07
> **Modo:** clonado fiel — la oferta corre activamente en 5 mercados con ~140 ads; se replica al polaco sin cambios
> **Mercado destino:** Europa (PL) · idioma: polaco · trato: formal "ty" (2ª persona polaca) · moneda: EUR
> **Fuentes:** landing [ref-playful-music.html (guardado)] · arsenal [búsqueda keyword "playfulmusicmethod" en Biblioteca, page ID 61595171693453]
> **Plataforma:** ImpulTienda · subdominio: [pendiente — dominio raíz sin definir]
> **Estado:** en armado

## 1 · Señal de ganador (medida, no supuesta)

| Dato | Valor |
|---|---|
| Anuncios activos del arsenal | ~140 |
| Anuncio activo más antiguo (días) | 1 día (desde 6 oct 2026) |
| Conceptos únicos (dedupe por guion) | por determinar (lanzamiento masivo, 16 h de actividad) |
| Mercados activos | IT, ES, FR, EN (www), DE |
| ¿Ya se modeló antes? | no (verificado en `OUTPUTS/` y `scouting/ofertas-probadas.md`) |

**Nota:** señal débil — la oferta tiene solo 1 día de pauta con un lanzamiento muy agresivo (~140 ads simultáneos). No hay datos de longevidad todavía. El operador (CSD DIGITAL PRODUCTS LLC) maneja varios productos en ImpulTienda.

## 2 · La oferta

### Modo A · Clonado fiel (cero bonos nuevos)

| Componente | Nombre original (IT) | Nombre traducido (PL) | Qué es | Valor original | Valor en EUR |
|---|---|---|---|---|---|
| Producto principal | Il Metodo Musicale Ludico | Zabawowa Metoda Muzyczna | 180+ páginas imprimibles de actividades musicales para niños 3-7, en 5 módulos + diploma | US$ 39 (implícito) | — |
| Bono 1 | Planner Settimanale delle Lezioni | Tygodniowy Planer Lekcji | Mini-planes semanales para rotar actividades | €15 | €15 |
| Bono 2 | Carte del Ritmo a Colori | Kolorowe Karty Rytmu | Cartas extra de ritmo con señales visuales | €9 | €9 |
| Bono 3 | Pack di Motricità Fine Musicale | Pakiet Motoryki Drobnej Muzycznej | Fichas de pregrafismo, emparejamiento y recorta-y-juega | €9 | €9 |
| **Total declarado** | | | | US$ 72 | ~€66 |

- Precio tachado del original: US$ 72 · Precio final del original: US$ 22
- **Mi precio de venta** (tabla del mercado Europa): EUR 17,99 · Ancla: EUR 53,97 (3×) · Ahorro: EUR 35,98
- Garantía: 7 días (consistente con tabla del usuario para Europa)
- ¿El checkout original vende dos ofertas? No — una sola oferta + 1 upsell inline (Quaderno di Teoria Musicale e Compositori, US$ 13). El upsell se descarta en el clonado (no tiene entregable definido para PL).
- Acceso / entrega que promete: acceso inmediato, de por vida, digital PDF, sin suscripción. Link por email.

### 5 módulos del producto principal

1. **Benvenuto e Guida all'Uso** → Powitanie i Przewodnik — guía rápida + programa de 4 semanas
2. **Attività Pratiche (+30 schede)** → Ćwiczenia Praktyczne (+30 kart) — pregrafismo, emparejamiento, creatividad
3. **Carte Musicali** → Karty Muzyczne — instrumentos, sonidos, acciones para juegos rápidos
4. **Giochi Stampabili** → Gry do Druku — tableros, memory, bingo sonoro
5. **Spartiti Illustrati** → Ilustrowane Partytury — método de notas a colores, notas reales sin teoría
6. **🏆 Diploma di Completamento** → Dyplom Ukończenia — diploma imprimible

## 3 · Título único (Fase 5)

- **Título largo** (mockups, checkout, producto): `Zabawowa Metoda Muzyczna · Ponad 180 Gotowych Kart Muzycznych + 3 Darmowe Bonusy`
- **N real** que se entrega: 180+ páginas · **K bonos**: 3
- **Título corto** (nombre de la tienda, máx. 5 palabras): Zabawowa Metoda Muzyczna
- Title Case polaco (artículos y preposiciones cortas en minúscula).

## 4 · Hero

- Headline: Zabawowa Metoda Muzyczna: Utrzymaj Dzieci Zmotywowane w 100% i Zachwycone Muzyką — Bez Potrzeby Umiejętności Gry na Instrumencie
- Subtítulo: 180+ stron gotowych do druku aktywności muzycznych, gier i system kolorowych nut, który pozwala dzieciom grać prawdziwą muzykę bez czytania nut. Zero przygotowań. Zero dyplomu muzycznego.
- Botón del hero (baja a la oferta, con ↓): 🎶 CHCĘ METODĘ MUZYCZNĄ ↓
- Botón de la oferta (con el precio en el texto): 🎶 CHCĘ METODĘ MUZYCZNĄ — {{price}}

## 5 · Landing

- Prefijo CSS: `pmpl-` · ancla de la oferta: `#pmpl-offer`
- Paleta (medida con CSS variables + paleta.sh):

| Rol | Variable | Hex |
|---|---|---|
| Fondo principal | --cream | #FBF3E6 |
| Fondo alterno / cards | --cream-card | #FFFDF8 |
| Fondo profundo | --cream-deep | #F2E4CB |
| Texto principal | --ink | #241D16 |
| Texto medio | --ink-mid | #4A3F33 |
| Texto muted | --muted | #8C8172 |
| Acento/CTA (teal) | --teal | #2E6E68 |
| CTA secundario (coral) | --coral | #F0592C |
| Bordes | --border | #E7DAC0 |
| Urgencia (darkbg) | --darkbg | #B8471F |
| Urgencia 2 | --darkbg2 | #9E3B19 |
| Highlight/gold | --gold | #F0B93D |
| Notas arcoíris | --n1..n6 | #E5533A, #EF8C2C, #EFC13F, #4FA37B, #4A90C4, #F28A6B |

- Fuentes: Fraunces (display/serif), Baloo 2 (accent), Karla (body/sans)
- ¿La paleta la fijan imágenes propias? No — se mantiene la paleta original.

| # | Sección del original | Layout | Qué se adapta |
|---|---|---|---|
| 1 | Urgency Bar | barra full-width, flex center | texto → polaco |
| 2 | Hero | grid 2 cols (texto izq, video der) | texto → polaco, video se mantiene (sin voz, solo visual) |
| 3 | Stats Strip | 3 columnas centradas sobre darkbg | números se mantienen, labels → polaco |
| 4 | Marquee Carousel | track horizontal infinito, 4 imgs | imágenes se re-suben a nuestro hosting (tienen texto IT quemado → traducir) |
| 5 | Problem | eyebrow + h2 + lista ✕ + callout | texto → polaco |
| 6 | Solution | imagen arriba + eyebrow + h2 + lista ✓ | texto → polaco, imagen tiene texto IT quemado → traducir |
| 7 | Inside (5 módulos + diploma) | eyebrow + h2 + lista con badges colores | texto → polaco |
| 8 | Compare (antes/después) | grid 2 cols sobre darkbg | texto → polaco |
| 9 | Reviews (3 text) | eyebrow + h2 + 3 cards | nombres/ciudades → polacos (no copiar italianos). Roles → polaco |
| 10 | Offer | darkbg + countdown + offer card | texto → polaco, precio → tokens {{price}}/{{original_price}}/{{savings}} |
| 11 | Bonuses (3 cards) | headline banner + grid 2+1 | texto → polaco, imágenes tienen texto IT → traducir |
| 12 | Video Preview | eyebrow + h2 + video | texto → polaco, video se mantiene (visual, sin texto quemado) |
| 13 | Post-offer Photo Reviews (3) | eyebrow + h2 + 3 cards grid | nombres/ciudades → polacos |
| 14 | Expert | eyebrow + h2 + card grid 132px+1fr | nombre "Team di Little Notes Co." → se mantiene o se adapta. Texto → polaco. Chips → polaco |
| 15 | Method (6 cards) | eyebrow + h2 + p + grid 2 cols | texto → polaco |
| 16 | Summary | card con lista + precio + CTA | texto → polaco, precio → tokens |
| 17 | FAQ (5 items) | eyebrow + h2 + details/summary | texto → polaco |
| 18 | Final CTA | teal bg + headline + btn | texto → polaco, precio → token |
| 19 | Footer | texto legal | → polaco, empresa se mantiene |
| 20 | Social Proof Popup | popup fijo bottom-left | nombres/ciudades → polacos (Warszawa, Kraków, Wrocław, etc.) |
| 21 | Sticky Mobile CTA | barra fija bottom | texto → polaco, precio → tokens |

**Adaptaciones culturales** (lo que no viaja y su reemplazo):

| Original | Reemplazo en PL | Por qué |
|---|---|---|
| Nombres italianos (Francesca G., Valentina R., etc.) | Nombres polacos (Katarzyna W., Marta K., Anna S., etc.) | Los testimonios no se copian como propios |
| Ciudades italianas (Milano, Roma, Bologna, etc.) | Ciudades polacas (Warszawa, Kraków, Wrocław, etc.) | Localización |
| "Maestra di Scuola dell'Infanzia" | "Nauczycielka przedszkolna" | Rol profesional equivalente |
| "Mamma Homeschool" | "Mama edukująca w domu" | Concepto existe en PL |
| "Musicoterapeuta" | "Muzykoterapeutka" | Rol equivalente |
| 14 nombres italianos en social proof popup | 14 nombres polacos con ciudades polacas | Localización |
| "4,9/5 · 5.000+ educatori e famiglie" | "4,9/5 · 5 000+ nauczycieli i rodzin" | Separador de miles en polaco: espacio |

**Lo que cambia sí o sí**: marcas del original (links a su dominio) → nuestros links · testimonios → nombres polacos · popup social proof → nombres/ciudades polacos · precios → tokens ImpulTienda.

**Imágenes**

| # | Imagen | Tipo | Acción | HTTP | Tamaño |
|---|---|---|---|---|---|
| 1 | carousel-1 (chatgpt-image-21-12-07) | `texto quemado` (IT) | traducir image-to-image → PL, re-subir | 200 | 207 KB |
| 2 | carousel-2 (chatgpt-image-21-12-01) | `texto quemado` (IT) | traducir image-to-image → PL, re-subir | 200 | 207 KB |
| 3 | carousel-3 (chatgpt-image-21-11-29) | `texto quemado` (IT) | traducir image-to-image → PL, re-subir | 200 | 182 KB |
| 4 | carousel-4 (chatgpt-image-21-06-50) | `texto quemado` (IT) | traducir image-to-image → PL, re-subir | 200 | 184 KB |
| 5 | solution (chatgpt-image-21-18-38) | `decorativa` (niños con materiales) | re-subir tal cual (sin texto quemado visible) | 200 | 163 KB |
| 6 | expert (chatgpt-image-21-23-18) | `persona identificable` (foto generada IA) | regenerar foto similar para nuestro uso | 200 | 146 KB |
| 7 | offer mockup (chatgpt-image-16-sept) | `texto quemado` (IT) | no se usa — reemplazado por mockup propio en Fase 6 | 200 | 218 KB |
| 8 | bonus-1 (chatgpt-image-25-sept-11-04) | `texto quemado` (IT) | traducir image-to-image → PL, re-subir | 200 | 111 KB |
| 9 | bonus-2 (chatgpt-image-25-sept-11-06) | `texto quemado` (IT) | traducir image-to-image → PL, re-subir | 200 | 115 KB |
| 10 | bonus-3 (chatgpt-image-25-sept-11-08) | `texto quemado` (IT) | traducir image-to-image → PL, re-subir | 200 | 114 KB |

**Videos** (2 videos, ambos autoplay muted loop):
1. Hero video (hero-tpmm-1.mp4) — visual de producto, sin voz → se mantiene tal cual
2. Preview video (mockups-4.mp4) — mockups del producto, visual → se mantiene tal cual

## 6 · Mockups de checkout

- Hero 3:2 fondo blanco: [pendiente — Fase 6]
- Caja 1:1 con escena: [pendiente — Fase 6]

## 7 · Tienda

- URL tienda: [pendiente]
- Subdominio con SSL activo: [pendiente — dominio raíz sin definir]
- Página de entrega (URL fija): [pendiente — GitHub Pages]
- Procesador: ImpulPay (multidivisa) · métodos locales ON: sí
- Checkout default aplicado: [pendiente]

## 8 · Suposiciones (nunca en el texto que ve el cliente)

- (suposición, no confirmado) Los videos del hero y preview no tienen texto en italiano quemado visible, se pueden usar directamente.
- (suposición, no confirmado) La foto de "expert" es generada por IA (nombre del archivo "chatgpt-image"), no es una persona real con derechos de imagen.
- (suposición, no confirmado) El operador CSD DIGITAL PRODUCTS LLC es un competidor tipo "micro store", no una marca con IP protegida sobre el concepto.
- (suposición, no confirmado) El número "5.000+ educatori e famiglie" es copy de marketing, no un dato verificado.

## 9 · Historial de decisiones

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-10-07 | Mercado: Polonia (PL) | 4× más usuarios de Facebook que Hungría, 9,5× más mercado e-commerce; no hay versión PL de la oferta |
| 2026-10-07 | Modo: clonado fiel | Landing real + arsenal activo con ~140 ads; el usuario lo pidió explícito |
| 2026-10-07 | Upsell descartado | El upsell (Quaderno di Teoria Musicale) no se clona — se lanza solo con la oferta principal + 3 bonos |
| 2026-10-07 | Videos se mantienen | Sin voz ni texto quemado en italiano — son puramente visuales |
