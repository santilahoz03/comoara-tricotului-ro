# Oferta modelada · Cuir et Atelier DE

> **Fecha:** 2026-10-10
> **Modo:** clonado fiel — oferta con ~77 ads activos (FR+IT+ES), zero competencia en DE para patrones de cuero digitales
> **Mercado destino:** Alemania · idioma: alemán · trato: du (informell) · moneda: EUR
> **Fuentes:** landing `scratchpad/ref-cuir-fr.html` (curl de ImpulTienda) · arsenal [Pablo Gutierrez — Biblioteca de Anuncios FR](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=FR&is_targeted_country=false&media_type=all&search_type=page&view_all_page_id=450583766503936)
> **Plataforma:** ImpulTienda · subdominio: [pendiente — dominio raíz sin definir]
> **Estado:** en armado

## 1 · Señal de ganador (medida, no supuesta)

| Dato | Valor |
|---|---|
| Anuncios activos del arsenal | ~77 (FR + IT + ES) |
| Anuncio activo más antiguo (días) | 4 días (desde 2026-10-06) |
| Conceptos únicos (dedupe por guion) | ~10 hooks, 1 winner claro |
| Mercados activos del anunciante | FR (principal), IT (fuerte), ES (recién arrancó 2026-10-10) |
| Plataforma del anunciante | ImpulTienda (cuir-et-atelier, cuoio-e-bottega, cuero-y-oficio) |
| Hook ganador (#1, ~50% de los ads) | "¿Funciona si nunca trabajé el cuero? Sí." (FR/IT/ES) |
| ¿Ya se modeló antes? (`OUTPUTS/`, `scouting/ofertas-probadas.md`) | sí, IT (2026-10-10) — esta es la versión DE |

## 2 · La oferta

### Modo A · Clonado fiel (cero bonos nuevos)

| Componente | Nombre original | Nombre traducido | Qué es (formato y cantidad) | Valor original | Valor en EUR |
|---|---|---|---|---|---|
| Producto principal | Collection de Patrons Maîtres en Cuir · 170+ patrons | Meister-Schnittmusterkollektion für Leder · über 170 Schnittmuster | 170+ PDF de patrones profesionales con medidas exactas (mm + pulgadas), lista de materiales, formatos A4/A1/Letter | — | — |
| Licencia comercial | Licence commerciale (incluse) | Kommerzielle Lizenz (inklusive) | Permiso para fabricar y vender sin regalías | (incluida) | (incluida) |
| Bono 1 | Guide pour bien choisir son cuir | Ratgeber zur Lederwahl | Guía PDF sobre tipos y espesores de cuero | €19 | €19 |
| Bono 2 | Masterclass de couture du cuir (5 techniques essentielles) | Masterclass Leder nähen (5 wesentliche Techniken) | Curso en PDF/video con 5 técnicas de costura | €24 | €24 |
| **Total declarado** | | | | **€43 en bonos** | **€43 en bonos** |

Bonos ocultos en checkout (no visibles en landing):
- Bono 3: Le Parcours de l'Artisan · 60 projets (valor 6) → Der Weg des Handwerkers · 60 Projekte
- Bono 4: Planches à taille réelle (1:1) à imprimer (valor 0) → Schablonen in Originalgröße (1:1) zum Ausdrucken

- Precio tachado del original: US$ 49.99 · Precio final del original: US$ 24.99
- **Mi precio de venta** (tabla del mercado Europa): **EUR 17,99** · Ancla: **EUR 37,99** · Ahorro: **EUR 20,00**
- Garantía (días del original): **7 días**
- ¿El checkout original vende dos ofertas? **No** — una sola oferta con 2 upsells inline (descartados por ahora)
- Acceso / entrega que promete: descarga inmediata tras la compra, email con link

## 3 · Título único (Fase 5)

- **Título largo** (mockups, checkout, producto): `Meister-Schnittmusterkollektion für Leder · über 170 Professionelle Schnittmuster + 2 Bonus-Anleitungen Inklusive`
- **N real** que se entrega: 170+ · **K bonos**: 2
- **Título corto** (nombre de la tienda, máx. 5 palabras): Leder & Werkstatt
- Title Case adaptado al alemán (sustantivos en mayúscula como corresponde al idioma).

## 4 · Hero

- Headline (modo A: el del original traducido): **170+ Professionelle Leder-Schnittmuster** / **Mit exakten Maßen, Materialliste und Schritt-für-Schritt-Anleitung.**
- Subtítulo: Herunterladen, ausdrucken und präzise zuschneiden — vom ersten Tag an der Werkbank. Mit kommerzieller Lizenz und 7-Tage-Garantie.
- Botón del hero (baja a la oferta, con ↓): `ZUM ANGEBOT ↓`
- Botón de la oferta (con el precio en el texto): `ICH WILL MEINEN ZUGANG JETZT →`

## 5 · Landing

- Prefijo CSS: `lw-` (conservado del original) · ancla de la oferta: `#lw-offer`
- Paleta (medida del CSS del HTML, idéntica a IT):

| Rol | Hex |
|---|---|
| Fondo oscuro principal | `#1A0F08` |
| Fondo oscuro secundario | `#241510` |
| Fondo claro/crema | `#F5EDE0` |
| Fondo claro secundario | `#FDF8F2` |
| Texto principal (oscuro) | `#1A0F08` |
| Texto secundario | `#5A4232` |
| Texto terciario | `#7A5A44` |
| Texto oscuro alt | `#3A2618` |
| Acento dorado | `#E0A15E` |
| CTA cobre (gradiente) | `#D6823A` → `#B5611F` |
| Cobre medio | `#C8722A` |
| Borde dashed | `rgba(200,114,42,.55)` |
| Verde éxito (badges) | `#3E8E5A` |
| Verde verificado | `#7FC79A` |
| Verde ahorro | `#2F7A4A` |
| Rojo tabla | `#C0413D` |
| Borde claro | `#E6D5C0` |
| Texto muted | `#9A8270` |
| Card bg crema | `#EDE3D4` |
| Card bg oscuro | `#4A3020` |
| Fuentes | DM Sans (body), Playfair Display (serif/headings) |

- ¿La paleta la fijan imágenes propias? **no** — se conserva la paleta del original

| # | Sección del original | Layout (columnas, lado de la imagen, alineación) | Qué se adaptó |
|---|---|---|---|
| 1 | Barra marquee sticky (`lwbar`) | 1 col, ticker horizontal | Texto traducido al alemán |
| 2 | Hero con video + badges (`lwhero`) | 1 col centrada, video 16:9, badges flotantes | Headline + subtítulo traducidos, botón agrega ↓ a la oferta |
| 3 | So funktioniert es — 4 pasos (`lwhow`) | 1 col, imagen panorámica arriba, 4 cards abajo en grid 2×2 | Texto traducido; imagen panorámica decorativa se reutiliza |
| 4 | Was enthalten ist — 4 cards (`lwinc`) | Grid de 4 cards; imagen a la izquierda, texto a la derecha | Texto traducido; imágenes cuir-fr-* → image-to-image DE |
| 5 | Schau dir an, was drin steckt — 3 filas (`lwin`) | 3 filas alternas (img izq/der/izq), 2 cols | Texto traducido; imágenes cuir-fr-* → image-to-image DE |
| 6 | Die komplette Übersicht — 6 categorías (`lwcat`) | Grid 3×2, imagen arriba, texto abajo | Texto traducido; imágenes ChatGPT decorativas se reutilizan |
| 7 | Tabla comparativa (`lwcmp`) | 1 col, tabla con 2 columnas (nosotros vs. otros) | Texto traducido |
| 8 | Was du erreichen wirst — 4 cards (`lwach`) | Grid 2×2, icono + título + texto | **REEMPLAZAR** reviews por "Was du erreichen wirst" (no hay testimonios reales) |
| 9 | Caja de oferta con countdown (`lwof`) | 1 col centrada, card con mockup, lista, precio, timer | Texto traducido; tokens ImpulTienda; imagen cuir-fr-15 → DE |
| 9b | Garantía 7 días (`lwgar`) | 1 col, sello + texto | Texto traducido |
| 10 | Lerne den Macher kennen — Thomas Weber (`lwme`) | 2 cols (foto izq, texto der), foto 4:5, badge, stats | **Jorge Gutiérrez → Thomas Weber**, foto → image-to-image |
| 11 | FAQ — 9 preguntas (`lwfaq`) | 1 col, acordeón | 9 preguntas traducidas fielmente |
| 12 | CTA final + sticky mobile (`lwfin` + `lwsticky`) | 1 col centrada + barra fija | Texto traducido; botones → `#lw-offer`; sticky → `/checkout` |

**Adaptaciones culturales** (lo que no viaja y su reemplazo):

| Original | Reemplazo en Alemania | Por qué |
|---|---|---|
| Jorge Gutiérrez (persona ficticia del ref) | **Thomas Weber** | Nombre alemán creíble para artesano ~55-60 años; elegido por el usuario |
| 4 reviews con video (Miguel S., Diego V., Lucas M., Santiago T.) | Sección "Was du erreichen wirst" (qué vas a lograr) | No hay testimonios reales; no se copian los del ref |
| "Achat vérifié" | eliminado | Sin testimonios |
| Moneda USD y "US$" | EUR con tokens `{{price}}`, `{{original_price}}`, `{{savings}}` | Mercado DE usa EUR |
| "reprographie" (francés) | "Copyshop" (alemán) | Equivalente cultural |
| "établi" (banco de trabajo) | "Werkbank" | Equivalente cultural |
| "copisteria" (italiano) | "Copyshop" | Equivalente cultural alemán |
| 2 upsells inline | descartados (por ahora) | Se simplifica a una sola oferta |

**Lo que cambia sí o sí**: Jorge Gutiérrez → Thomas Weber · testimonios → sección "Was du erreichen wirst" · paquetes → uno solo · hero con botón que baja a la oferta · links al dominio original → eliminados.

**Imágenes**

| # | Archivo | Tipo | Acción | HTTP | Tamaño |
|---|---|---|---|---|---|
| 1 | `bos-sochi-pindown-io-*.mp4` | decorativa (video crafting) | reutilizar, re-subir a hosting propio | 200 | 10.6 MB |
| 2 | `imagen-chatgpt-07-58-43.webp` | decorativa (panorama herramientas) | reutilizar, re-subir | 200 | 195 KB |
| 3 | `whatsapp-image-17-46-59.webp` | **persona identificable** (Jorge Gutiérrez) | **REEMPLAZAR** → image-to-image: Thomas Weber, alemán ~55-60, taller de cuero, composición 4:5 | 200 | 141 KB |
| 4 | `imagen-chatgpt-08-05-20.webp` | decorativa (categoría Taschen) | reutilizar, re-subir | 200 | 191 KB |
| 5 | `imagen-chatgpt-08-05-54.webp` | decorativa (categoría Rucksäcke) | reutilizar, re-subir | 200 | 174 KB |
| 6 | `imagen-chatgpt-08-06-38.webp` | decorativa (categoría Geldbörsen) | reutilizar, re-subir | 200 | 234 KB |
| 7 | `imagen-chatgpt-08-07-14.webp` | decorativa (categoría Umhängetaschen) | reutilizar, re-subir | 200 | 191 KB |
| 8 | `imagen-chatgpt-08-07-49.webp` | decorativa (categoría Reise) | reutilizar, re-subir | 200 | 215 KB |
| 9 | `7b15129f*.mp4` | **persona identificable** (review video 4) | **ELIMINAR** → sección reviews se reemplaza | 200 | 5.2 MB |
| 10 | `dfa8f1f6*.mp4` | **persona identificable** (review video 3) | **ELIMINAR** → sección reviews se reemplaza | 200 | 2.7 MB |
| 11 | `f71be231*.mp4` | **persona identificable** (review video 2) | **ELIMINAR** → sección reviews se reemplaza | 200 | 12.2 MB |
| 12 | `b33cab5d*.mp4` | **persona identificable** (review video 1) | **ELIMINAR** → sección reviews se reemplaza | 200 | 16.8 MB |
| 13 | `imagen-chatgpt-08-10-18.webp` | decorativa (categoría Accessoires) | reutilizar, re-subir | 200 | 254 KB |
| 14 | `cuir-fr-08.webp` | **texto quemado** (mockup detalle: biblioteca) | **image-to-image** FR→DE | 200 | 169 KB |
| 15 | `cuir-fr-09.webp` | **texto quemado** (mockup detalle: material) | **image-to-image** FR→DE | 200 | 157 KB |
| 16 | `cuir-fr-10.webp` | **texto quemado** (mockup detalle: medidas) | **image-to-image** FR→DE | 200 | 137 KB |
| 17 | `cuir-fr-11.webp` | **texto quemado** (mockup bono 2: masterclass) | **image-to-image** FR→DE | 200 | 169 KB |
| 18 | `cuir-fr-12.webp` | **texto quemado** (mockup licencia comercial) | **image-to-image** FR→DE | 200 | 160 KB |
| 19 | `cuir-fr-13.webp` | **texto quemado** (mockup bono 1: guía cuero) | **image-to-image** FR→DE | 200 | 171 KB |
| 20 | `cuir-fr-14.webp` | **texto quemado** (mockup producto principal) | **image-to-image** FR→DE | 200 | 143 KB |
| 21 | `cuir-fr-15.webp` | **texto quemado** (mockup oferta completa) | **image-to-image** FR→DE | 200 | 159 KB |

**Resumen de acciones sobre imágenes:**
- **8 decorativas** (1 video + 7 webp): reutilizar, re-subir a hosting propio (catbox.moe)
- **8 texto quemado** (cuir-fr-08 a 15): image-to-image FR→DE, re-subir
- **1 persona identificable** (Jorge): image-to-image → Thomas Weber
- **4 videos persona** (reviews): eliminar (sección reemplazada por "Was du erreichen wirst")

## 6 · Mockups de checkout

- Hero 3:2 fondo blanco: (pendiente Fase 6)
- Caja 1:1 con escena: (pendiente Fase 6)

## 7 · Tienda

- URL tienda: (pendiente) · subdominio con SSL activo: pendiente (dominio raíz sin definir)
- Página de entrega (URL fija): (pendiente — GitHub Pages)
- Procesador: ImpulPay (multidivisa) · métodos locales ON: sí
- Checkout default aplicado: pendiente · QC local pendiente · QC publicado pendiente

## 8 · Suposiciones (nunca en el texto que ve el cliente)

- (suposición, no confirmado) Los nombres de los bonos "Le Parcours de l'Artisan" y "Planches à taille réelle" aparecen solo en el checkout, no en la landing. Se traducen igualmente para el checkout DE.
- (suposición, no confirmado) El video del hero es genérico de crafting sin texto ni persona identificable. Se reutiliza.
- (suposición, no confirmado) Las imágenes "cuir-fr-*" tienen texto en francés quemado; se confirmará al descargarlas y revisarlas.

## 9 · Historial de decisiones

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-10-10 | Mercado Alemania, EUR 17,99 | Cero competencia en DE para patrones de cuero digitales (verificado en Biblioteca de Anuncios); mayor mercado europeo con tradición de Handwerk y cuero (Braun Büffel, Tandy Leather EU) |
| 2026-10-10 | Modo A · Clonado fiel | Landing real + arsenal real con ~77 ads activos (FR+IT+ES) |
| 2026-10-10 | Jorge Gutiérrez → Thomas Weber | Pedido del usuario: nombre alemán de señor ~55-60 |
| 2026-10-10 | Sección reviews → "Was du erreichen wirst" | No hay testimonios reales; los del ref no se copian |
| 2026-10-10 | Upsells descartados | Se simplifica a una sola oferta para el lanzamiento |
| 2026-10-10 | Ancla EUR 37,99 | Ratio ~2.1× sobre precio de venta, consistente con el ratio del original ($49.99/$24.99 = 2×) |
