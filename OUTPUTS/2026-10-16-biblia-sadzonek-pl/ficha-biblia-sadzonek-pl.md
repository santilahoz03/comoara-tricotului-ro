# Oferta modelada · Biblia Sadzonek

> **Fecha:** 2026-10-16
> **Modo:** Clonado fiel — landing real + arsenal activo disponibles
> **Mercado destino:** Polonia (PL) · idioma: polaco · trato: ty/twój · moneda: PLN
> **Fuentes:** landing `ref.html` (https://bibliadelesqueje.impultienda.ar/) · arsenal page_id=562179073644202
> **Plataforma:** ImpulTienda · subdominio: [pendiente]
> **Estado:** en armado — Fase 3 completada

## 1 · Señal de ganador

| Dato | Valor |
|---|---|
| Anuncios activos del arsenal | ~5 (cuenta nueva, pero ángulo validado en LATAM) |
| Anuncio activo más antiguo (días) | ~14 días |
| Conceptos únicos | 3 (dolor raíz, método, vender) |
| ¿Ya se modeló antes? | no — PL está libre en `scouting/ofertas-probadas.md` |

**Decisión del usuario:** modelar aunque no alcanza el umbral de 15 ads — el ángulo (propagación de plantas + micro-negocio) tiene demanda comprobada en PL (KytkaSem.cz, Allegro, OLX tienen mercado físico activo).

## 2 · La oferta

### Modo A · Clonado fiel

| Componente | Nombre original (ES) | Nombre traducido (PL) | Formato | Valor orig. (ARS) | Valor (PLN) |
|---|---|---|---|---|---|
| Producto principal | La Biblia del Esqueje | Biblia Sadzonek | PDF 121 páginas | AR$74.183 | 349 zł |
| Bono 1 | Plantas seguras en casa | Bezpieczne rośliny w domu | PDF | AR$9.084 | 39 zł |
| Bono 2 | La Calculadora del Vivero | Kalkulator Szkółki | Hoja de cálculo/PDF | AR$10.598 | 49 zł |
| Bono 3 | Dónde vender tu primera tanda | Gdzie sprzedać pierwszą partię | PDF | AR$9.084 | 49 zł |
| Bono 4 | Los 10 errores que matan el esqueje | 10 błędów, które niszczą sadzonkę | PDF | AR$13.626 | 39 zł |
| Bono 5 | Enraizantes naturales caseros | Domowe naturalne ukorzeniacze | PDF | AR$10.598 | 39 zł |
| Bono 6 | Guía para multiplicar suculentas | Poradnik mnożenia sukulentów | PDF | AR$9.084 | 39 zł |
| Bono 7 | Calendario de esquejes por estación | Kalendarz sadzonek według pór roku | PDF | AR$13.626 | 39 zł |
| Bono 8 | Emprender desde cero | Zacznij od zera | PDF | AR$10.598 | 49 zł |
| Bono 9 | Esquejes en agua | Sadzonki w wodzie | PDF | AR$9.084 | 39 zł |
| Bono 10 | Sustratos caseros | Domowe podłoża | PDF | AR$10.598 | 39 zł |
| Bono 11 | Plagas y hongos en la bandeja | Szkodniki i grzyby w tacce | PDF | AR$9.084 | 39 zł |
| Bono 12 | Tu vivero con cero inversión | Twoja szkółka bez inwestycji | PDF | AR$13.626 | 39 zł |
| Bono 13 | Aromáticas que se venden | Zioła, które się sprzedają | PDF | AR$10.598 | 39 zł |
| Bono 14 | Planilla de producción | Arkusz produkcji | PDF/Excel | AR$7.570 | 29 zł |
| Bono 15 | Mensajes que venden plantas | Wiadomości, które sprzedają rośliny | PDF | AR$9.084 | 39 zł |
| **Total declarado** | | | | **AR$157.456 + libro** | **605 zł + 349 zł = 954 zł** |

- Precio tachado original: AR$74.183 → `{{original_price}}` = **349 zł**
- **Mi precio de venta:** 69 zł → `{{price}}`
- Ancla: 349 zł (~5×)
- Ahorro: 280 zł (80%)
- Total declarado: 954 zł (ratio 13.8×)
- Garantía: **7 días** (igual que el original)
- Checkout original: una sola oferta → sin colapso necesario
- Acceso: PDF inmediato por email + 15 guías en el mismo correo

## 3 · Título único

- **Título largo:** `Biblia Sadzonek · Kompletny Przewodnik Rozmnażania Roślin w Domu + 15 Poradników w Prezencie`
- **N real:** 121 páginas · **K bonos:** 15
- **Título corto:** `Biblia Sadzonek`
- Title Case polaco aplicado (artículos y preposiciones cortas en minúscula)

## 4 · Hero

- Headline: `Rozmnóż 100 roślin i sprzedaj swoją pierwszą partię` (traducción fiel)
- Subtítulo: `Biblia Sadzonek · Kompletny Przewodnik Rozmnażania Roślin + 15 Poradników w Prezencie`
- Botón hero (baja a oferta): `Chcę Biblię Sadzonek →`
- Botón de la oferta (con precio): `Chcę Dostęp za {{price}} →`

## 5 · Landing

- Archivo: `landing-biblia-sadzonek-pl.html`
- Prefijo CSS: heredado del original (ImpulTienda)
- Paleta medida: ver `PALETTE.md`
  - Fondo: `#f3eee2` · Fondo alt: `#ffffff` · Texto: `#2b241c`
  - Acento/CTA: `#a33b26` · Marca: `#24402a` · Urgencia: `#c0392b`

**Adaptaciones culturales:**

| Original | Reemplazo en PL | Por qué |
|---|---|---|
| `🇦🇷 +10.000 en Argentina` | `🌍 Sprzedana w wielu krajach` | No usar bandera AR en mercado PL |
| ARS precios | Tokens `{{price}}` / `{{original_price}}` | Moneda del mercado |
| Metadato de moneda ARS | `{"currency":"EUR","locale":"pl-PL"}` | Formato local |
| "Malvón o geranio" | "Pelargonia" | Nombre correcto en polaco |
| "vecinos, ferias, plataformas" | "sąsiedzi, targi, platformy jak OLX" | OLX es la plataforma C2C líder en PL |
| "WhatsApp" | "WhatsApp i platformy sprzedażowe jak OLX" | En PL se usa WhatsApp + OLX para vender |
| `¿Sirve en mi país?` FAQ | `Czy sprawdzi się w moim kraju?` | Adaptado con referencias hemisferio norte/sur |

## 6 · Mockups de checkout

- Hero 3:2 fondo blanco: pendiente (Fase 6)
- Caja 1:1 con escena: pendiente (Fase 6)

## 7 · Tienda

- URL: pendiente
- Subdominio: pendiente
- Procesador: ImpulPay (multidivisa) para EUR
- Métodos locales: ON (BLIK, tarjetas PL)
- Checkout: pendiente (Fase 7)

## 8 · Suposiciones

- (inferencia, no confirmado) El calendario de esquejes por estación incluye ambos hemisferios, lo que lo hace válido para PL (hemisferio norte).
- (inferencia, no confirmado) Las 15 especies mencionadas en el libro crecen también en clima polaco (templado continental): el comprador polaco puede aplicar el método.

## 9 · Historial de decisiones

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-10-16 | Modelar en PL aunque arsenal < 15 ads | Usuario decidió avanzar; ángulo validado por mercado físico activo en PL |
| 2026-10-16 | Modo A clonado fiel | Hay landing real + arsenal real |
| 2026-10-16 | Precio EUR 17,99 / ancla EUR 39,99 | Tabla de mercados del usuario (precio inicial) |
| 2026-10-16 | `🌍 Sprzedana w wielu krajach` en lugar de bandera AR | No tiene sentido la bandera argentina para compradores polacos |
| 2026-10-16 | Cambio a PLN: 69 zł / ancla 349 zł (~5×) | Usuario eligió precio en moneda local (PLN), no en EUR |
