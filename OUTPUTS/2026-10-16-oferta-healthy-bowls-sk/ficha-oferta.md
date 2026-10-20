# Ficha oferta — Healthy Bowls SK

**Fecha:** 2026-10-16  
**Pedido original:** Modelar Bowl Formula (CZ ref) para Eslovaquia (SK)  
**Modo:** A · Clonado fiel  
**Temas consultados:** WIKI/negocio.md, WIKI/stack-conectores.md, memoria.md

---

## Señal de mercado

- **Competidor ref:** Bowl Formula (page_id 1477583755427494)
- **Mercados activos del competidor:** CZ, PL, RO, GR, TR, IT, EN, AR, PT
- **Mercado SK:** ✅ vacío confirmado (canario MCP 2026-10-16, 0 resultados)
- **Canario SE/NL también vacíos** en la misma corrida
- **Población SK:** ~5,5M (mercado chico, mismo cluster que CZ)

---

## Oferta (clonado fiel del ref CZ)

| Campo | Valor |
|---|---|
| Producto principal | 208 receptov na zdravé bowly (9 sekcií) |
| Secciones | Rýchle a jednoduché (33) · Meal prep (42) · Fitness (46) · Detox (29) · Superfood (18) · Vegánske (14) · Sladké (14) · Smoothie (5) · Dezertné (13) |
| Bonus 1 | 19 granôl, zmrzlín a posýpok — valor €8,99 |
| Bonus 2 | 13 zdravých omáčok na bowly — valor €6,99 |
| Bonus 3 | 10 zdravých smoothie — valor €5,99 |
| Bonus 4 | 12 omáčok z celého sveta — valor €6,99 |
| Total bonos | €28,96 incluídos |
| Formato entrega | PDF instantáneo |
| Garantía | 7 días devolución |

---

## Tabla de mercado (SK — nuevo, no estaba en CLAUDE.md)

| Campo | Valor propuesto |
|---|---|
| Países | SK |
| Idioma / trato | Eslovaco · tuteo (ty/tvoja) |
| Moneda | EUR |
| Precio de venta | **€14,99** |
| Ancla | **€74,99** (5×) |
| Garantía | 7 días |
| Botón checkout | **ZÍSKAŤ PRÍSTUP HNEĎ** |

> ✅ **Pricing confirmado 2026-10-16. Agregado a CLAUDE.md.**

---

## Título (Fase 5)

- **Título largo:** `200+ receptov na zdravé bowly · 4 bonusové knihy v cene`
- **Título corto (tienda):** `Zdravé bowly`
- **Dominio sugerido:** `zdrave-bowly-sk.impultienda.ar` (o subdominio propio cuando tengas dominio)

---

## Landing

- **Archivo:** `landing-healthy-bowls-sk.html`
- **Generado con:** `clonar.py aplicar` sobre ref CZ + diccionario 217 entradas
- **Prefijo CSS:** `zbs-` (renombrado de `bf-`)
- **Tokens de precio:** `{{price}}` × 8 · `{{original_price}}` × 2
- **Moneda config:** `"currency":"EUR","prefix":"€","locale":"sk-SK"`
- **lang:** `sk`
- **Paleta:**
  - Fondo: `#f8fafc`
  - Fondo alterno: `#fbf6ec`
  - Texto: `#1e293b`
  - CTA: `#f2542d` (naranja-rojo)
  - Checks: `#8cc63f` (verde)
  - Overlays: `rgba(23,48,31,*)`

---

## Imágenes

### Sin texto quemado (re-hospedar en catbox.moe, base CDN Supabase)
- Todas las fotos de bowls de comida (~25 imágenes)
- Tapas de bonusbooks (genéricas, sin texto visible)

### Con texto quemado (requieren image-to-image)
- `cover-book.webp` — tapa principal tiene "200+ receptů na zdravé bowly" en CZ → traducir a SK
- `formula-bowl.webp` — puede tener labels en CZ → verificar y traducir si aplica
- `page-1.webp` — página de muestra en CZ → traducir

> Pendiente: confirmar pricing SK → luego re-hospedar fotos y hacer image-to-image de tapas.

---

## Mockups checkout (Fase 6)

Pendiente producción:
- Hero 3:2 fondo blanco puro — laptop + ebook SK + 4 bonos + props (bowl, verduras)
- Caja 1:1 escena real — caja 3D + tablet + móvil + bonos en abanico

---

## Tienda (Fase 7)

Pendiente: ImpulTienda SK (espera confirmación pricing y preferencia automático/manual).

---

## Ads (Fases 8–9)

Pendiente: post-tienda, réplica de los ads del arsenal CZ/ref.

---

## Panel (Fase 8)

Pendiente: `panel-healthy-bowls-sk.html` (local, no se publica).

---

## Huecos / lo que falta

1. Confirmación pricing SK (€17,99 / €35,99 / 7 días) — **bloquea todo lo demás**
2. Re-hospedaje de imágenes en catbox.moe
3. Image-to-image de las 3 tapas con texto CZ
4. Mockups de checkout
5. Configuración tienda + checkout ImpulTienda
