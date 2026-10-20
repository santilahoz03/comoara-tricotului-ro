# Oferta modelada · Comoara Tricotului (RO)

> **Fecha:** 2026-10-14
> **Modo:** Clonado fiel (A) — hay landing real + arsenal activo con 43 ads desde oct-13
> **Mercado destino:** Rumania · idioma: rumano · trato: formal/tú implícito · moneda: EUR
> **Fuentes:** landing `https://the-knitter-s-treasure-chest.impultienda.ar/` · arsenal [page 1289737737563235](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&is_targeted_country=false&media_type=all&search_type=page&sort_data[mode]=total_impressions&sort_data[direction]=desc&view_all_page_id=1289737737563235)
> **Plataforma:** ImpulTienda · subdominio: `tricotat` (slug sugerido; confirmar al crear tienda)
> **Estado:** en armado · Fase 3 completa (landing HTML) · pendiente Fase 6 (mockups) + Fase 7 (tienda)

---

## 1 · Señal de ganador

| Dato | Valor |
|---|---|
| Anuncios activos del arsenal | ~43 (oct-13 a oct-14) |
| Anuncio activo más antiguo (días) | ~4 (arsenal reciente, lanzado ~oct-10) |
| Conceptos únicos | ~6–8 (variantes de testimonios, problema/solución) |
| ¿Ya se modeló antes? | **No** — verificado en `OUTPUTS/` y `scouting/ofertas-probadas.md` |
| Competencia en Rumania (búsquedas reales, oct-14) | **0 competidores directos** — 4 búsquedas en rumano/inglés, todas vacías |

**Por qué Rumania (vs. PL, CZ, HU):** Polonia y Rep. Checa tienen anunciantes activos (wzory_na_drutach, kötésminták). Hungría vacía pero pequeña. Rumania: 0 competidores, ~5M de usuarios de Facebook adultos, interés en artesanías alto, EUR compatible.

---

## 2 · La oferta (Modo A · Clonado fiel)

| Componente | Nombre original (EN) | Nombre traducido (RO) | Qué es | Valor orig. (USD) | Valor (EUR) |
|---|---|---|---|---|---|
| Producto principal | Pattern Library — 5,200+ patterns | Biblioteca de Tipare — 5.200+ tipare | Colecție PDF digital, toate categoriile | $72 | 220 lei |
| Incluido | The Great Stitch Library | Marea Bibliotecă de Împletituri | Ghid vizual tehnici de tricotat | $35 | 90 lei |
| Incluido | Special Libraries (By Time / To Sell / Trending) | Biblioteci Speciale (Pe Durată / De Vânzare / Trending) | 3 sub-colecții tematice | $30 | 80 lei |
| Bonus 1 | First Stitches Guide | Ghidul Primelor Împletituri | Ghid tehnici de bază | $32 | 80 lei |
| Bonus 2 | The Knitter's Toolkit | Setul de Unelte al Tricotezei | Ghid andrele, accesorii, organizare | $32 | 80 lei |
| Bonus 3 | Our Knitters' Favorite Patterns | Tiparele Preferate ale Tricotezelor Noastre | Selecție top 50 tipare votate | $27 | 70 lei |
| Bonus 4 | Patterns for Your Pet | Tipare pentru Animale de Companie | Hăinuțe câini/pisici | $22 | 60 lei |
| Bonus 5 | Lifetime Collection Updates | Actualizări pe Viață ale Colecției | Actualizări fără cost suplimentar | $32 | 80 lei |
| Bonus 6 | Extra Crochet Patterns | Tipare Suplimentare de Croșetat | Colecție croșetat bonus | $27 | 70 lei |
| Bonus 7 | Knitter's Certificate | Certificatul Tricotezei | Certificat personalizat | $19 | 60 lei |
| **Total items** | | | | **$328** | **890 lei** |
| Regalo hoy 1 | Year Knitting Plan | Planul de Tricotat al Anului | 52 săptămâni de proiecte | ~$35 | ~€12 |
| Regalo hoy 2 | Knitter's Shopping List | Lista de Cumpărături a Tricotezei | Materiale esențiale | ~$27 | ~€9 |
| Regalo hoy 3 | Knitted Gift Guide | Ghidul de Cadouri Tricotate | Idei cadouri pe sezoane | ~$41 | ~€12 |
| **Total con regalos** | | | | **~$431** | **~€122** |

- Precio tachado del original: USD $328 → Precio final: USD $27 (92% off)
- **Mi precio de venta:** 89 lei (RON) · Ancla: 890 lei · Ahorro: 801 lei (90% off) · ratio 10× (fiel al espíritu del original)
- Token ImpulTienda: `{{price}}` = 89 lei · `{{original_price}}` = 890 lei · `{{savings}}` = 801 lei
- Moneda tienda: RON (leu rumano)
- Persona de marca: **Elena** (fue Margaret en el original — cambiado por nombre rumano clásico)
- Garantía: **7 días** (fiel al original)
- Checkout original: una sola oferta (ya colapsada) — no hay split básico/premium
- Acceso / entrega: email inmediato post-pago con link a colección PDF

---

## 3 · Título único (Fase 5)

- **Título corto** (tienda, máx. 5 palabras): `Comoara Tricotului`
- **Título largo** (mockups, checkout, producto en tienda):
  `Comoara Tricotului™ · 5.200+ Tipare Premium de Tricotat + 7 Ghiduri Bonus`
- N real que se entrega: 5.200+ tipare | K bonos: 7 + 3 cadouri
- Title Case ✓ | en rumano: sustantivos con mayúscula por énfasis, artículos en minúscula ✓

---

## 4 · Hero

- Headline (original traducido): `5.200+ Tipare Premium de Tricotat — și Creează Piese Superbe`
- Número hero (modo original): **5.200+** (enorme, serif)
- Subtítulo: `Tipare Premium de Tricotat · 7 Ghiduri Bonus Incluse`
- Botón hero (baja a oferta): `↓ Vreau acces imediat`
- Botón de la oferta (va a /checkout): `VREAU ACCES IMEDIAT`
- Botón mobile sticky: `VREAU ACCES IMEDIAT · {{price}}`
- CTA final: `↓ VREAU ACCES IMEDIAT`

---

## 5 · Landing

- Prefijo CSS: `ct-` · ancla de la oferta: `#ct-offer`
- **Paleta medida** (`scripts/paleta.sh` sobre `the-knitter-s-treasure-chest.impultienda.ar`):
  - Fondo: `#f6f1e7` (crema cálida)
  - Fondo alterno: `#f6e9df` (beige cálido)
  - Texto: `#4a4238` (marrón oscuro, 22 ocurrencias)
  - Acento/CTA: `#b0714a` (cobre, 18 ocurrencias)
  - Acento oscuro: `#a8603f` (botón CTA)
  - Bordes: `#d8cdb8` (arena)
  - Texto secundario: `#8a8378` (gris cálido)
  - Urgencia/estrellas: `#f59e0b` (ámbar)
- Paleta fijada por el original (no por imágenes propias) ✓

### Mapa de secciones

| # | Sección del original | Layout | Adaptado en RO |
|---|---|---|---|
| 1 | Barra urgencia fija (sticky top) | 1 col centrado | Día en rumano (JS dinámico), 80% savings |
| 2 | Hero: número + producto + badges + botón | Centrado, imagen del producto | Placeholder imagen (Fase 6); número 5.200+ |
| 3 | Video "See how it works 2 min" | Centrado, embed video | Placeholder video |
| 4 | Pain copy + Two groups (Buscando vs Creando) | 2 cols | Texto fiel traducido |
| 5 | Social proof bar (4.9/5, 5k users, etc.) | Flex row | Cifras mantenidas |
| 6 | Offer box (precio, countdown, items, CTA → /checkout) | 1 col centrado | Tokens {{price}}, etc.; CTA → /checkout |
| 7 | Pain re-agitation quote | Border-left | Fiel |
| 8 | Trust badges row | Flex | Iconos estándar |
| 9 | Full what-you-get (10 items con valor) | Cards grid | Con valores en EUR |
| 10 | Price recap / value stack | Table | Total {{original_price}} → {{price}} |
| 11 | Margaret's today-only gifts (3 regalos) | Card destacada | "Cadourile Margaret" |
| 12 | Vision / "30 days from now" | 4 bloques border-left | Fiel traducido |
| 13 | Guarantee | Card verde | 7 zile, fiel |
| 14 | **Ce vei crea** (reemplaza testimonials) | Grid 2x3 | Sin testimonios Anglo; escenarios de logros |
| 15 | About Margaret | Foto + texto | Persona ficticia conservada, nombre Margaret |
| 16 | FAQ (6 preguntas) | Accordion | Fiel traducido |
| 17 | Final CTA | Dark bg centrado | Con precio grande y botón → #ct-offer |
| 18 | Mobile sticky bar | Fixed bottom | → #ct-offer |

### Adaptaciones culturales

| Original | Reemplazo en RO | Por qué |
|---|---|---|
| Testimonios (Sarah Portland, Emily Manchester…) | "Ce vei crea" — 6 escenarios de logro | Sin testimonios reales en RO; evita credibilidad falsa |
| "TODAY WEDNESDAY" en barra | JS dinámico → día en rumano + fecha | Mantiene urgencia sin hardcodear |
| USD $27 / $328 | EUR 17,99 / EUR 89,99 con tokens | Mercado europeo, moneda local |
| "92% off" | "80% off" | Ahorro real con nuestros precios EUR |
| "44 people viewing" | "44 de persoane vizualizează acum" (JS fluctuante) | Fiel |

**Imágenes:**

| Imagen | Tipo | Acción |
|---|---|---|
| Portada del libro "The Knitter's Treasure Chest" | texto quemado + copyright | Reemplazar con mockup propio (Fase 6) — placeholder en HTML |
| Foto de Margaret (mujer tejiendo) | persona identificable | Placeholder → foto stock libre (Fase 4) o IA |
| Tapas de los bonos | texto quemado EN | Traducir a RO en Fase 4 (si se usan) |
| Decorativos (yarn, flores) | decorativa | Usar originales o equivalentes libres |

---

## 6 · Mockups de checkout (Fase 6 — ✅ COMPLETA)

- Hero 3:2 fondo blanco: `OUTPUTS/2026-10-14-comoara-tricotului-ro/mockups/1-hero-comoara-ro.webp`
  → catbox: https://files.catbox.moe/un1zn0.webp — **en landing ✓**
- Escena 1:1: `OUTPUTS/2026-10-14-comoara-tricotului-ro/mockups/2-caja-comoara-ro.webp`
  → catbox: https://files.catbox.moe/ecn16i.webp — (para ads/tienda)
- Foto Elena: `OUTPUTS/2026-10-14-comoara-tricotului-ro/imgs-ro/foto-elena.webp`
  → catbox: https://files.catbox.moe/xxokok.webp — **en landing ✓**
- Hero access (banner acceso): `OUTPUTS/2026-10-14-comoara-tricotului-ro/imgs-ro/hero-access-ro.webp`
  → catbox: https://files.catbox.moe/zbqt37.webp — (para ads)

---

## 7 · Tienda (Fase 7 — pendiente, esperando respuesta usuario: Automático / Manual)

- URL tienda: pendiente · subdominio sugerido: `tricotat.impultienda.ar`
- Página de entrega (URL fija): pendiente — publicar `entrega-en-preparacion.html` antes de crear producto
- Procesador: Stripe (mercado RO, EUR) · métodos locales ON (iDEAL, etc.)
- Checkout default: verde oscuro, solo email, cuenta regresiva 10min rojo, cupos bajo botón
- Texto botón checkout (tabla CLAUDE.md): `VREAU ACCES IMEDIAT`

---

## 8 · Suposiciones

- (inferencia, no confirmado) El original no tiene geo-blocking — el operador usa `impultienda.ar` y no restringe acceso por país
- (inferencia, no confirmado) Las tapas de los bonos del original están en inglés; si se muestran en la landing RO habrá que traducirlas
- (inferencia, no confirmado) El video de la sección 3 es el propio ad video del anunciante — en nuestra versión será el primer ad producido

---

## 9 · Historial de decisiones

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-10-14 | Mercado: Rumania (EUR 17,99) | 0 competidores verificados; PL y CZ tienen anunciantes activos |
| 2026-10-14 | Modo A (Clonado Fiel) | Landing real + arsenal real con 43 ads activos |
| 2026-10-14 | Nombre: Comoara Tricotului™ | Evocador, completamente rumano; "comoara" = tesoro |
| 2026-10-14 | Sin testimonios → "Ce vei crea" | No hay testimonios reales de tricoteze române |
| 2026-10-14 | Ancla EUR 89,99 (no 328 USD) | 5× precio de venta, creíble en mercado europeo |
| 2026-10-14 | Persona "Margaret" conservada | Nombre válido en Europa; personaje ficticio sin copyright |
