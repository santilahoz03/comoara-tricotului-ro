# Material para configurar ImpulTienda — Arteterapia IT

> Fecha: 2026-10-11
> Oferta: Il Manuale Definitivo di Arteterapia
> Mercado: Italia · EUR 17,99

---

## 1 · Producto

| Campo | Valor |
|---|---|
| **Nombre corto** (nombre de la tienda) | Manuale di Arteterapia |
| **Nombre largo** (título del producto) | Il Manuale Definitivo di Arteterapia · 100+ Attività Guidate + 7 Guide Bonus Incluse |
| **Precio de venta** | EUR 17,99 |
| **Precio tachado** | EUR 138 |
| **Moneda** | EUR |
| **Imagen del producto** | Mockup hero 3:2 → [descargar](https://files.catbox.moe/gm1r2t.png) · [archivo local](mockups/1-hero-arteterapia-it.png) |
| **Link de entrega** | https://santilahoz03.github.io/arteterapia-it/acceso/wqkfq2m9xl/ |

**Importante:** un solo producto que representa toda la oferta (manual + 7 bonos). NO usar "Agregar bono" para los bonos — ya están incluidos en el hub de entrega.

---

## 2 · Fragmento HTML (landing)

Copiar TODO el contenido de este archivo y pegarlo en el bloque de código personalizado de ImpulTienda:

**URL raw para copiar:** https://raw.githubusercontent.com/santilahoz03/arteterapia-it/main/fragmento.txt

O abrirlo desde: [fragmento local](landing-arteterapia-it-fragmento.html)

**Después de pegar:** recargar la página de la tienda y verificar que se vea bien.

---

## 3 · Checkout — Colores exactos

| Elemento | Color HEX |
|---|---|
| **Botón de compra** (fondo) | `#5BAA7A` (verde oscuro) |
| **Botón de compra** (texto) | `#FFFFFF` |
| **Cuenta regresiva** (fondo) | `#4E4036` (marrón oscuro) |
| **Cuenta regresiva** (texto) | `#FFFFFF` |
| **Badge / cinta** | `#C9A84C` (dorado) |
| **Fondo del checkout** | `#FFF8F4` (crema) |
| **Texto principal** | `#4E4036` |

---

## 4 · Checkout — Configuración

| Campo | Valor |
|---|---|
| Cuenta regresiva | 10 minutos |
| Imagen arriba | Mockup hero 3:2 (la misma del producto) |
| Cupos (abajo) | "Solo X rimasti a questo prezzo" |
| Texto del botón | **VOGLIO IL MIO ACCESSO ORA** |
| Campos | Solo email + teléfono (opcional) |
| Garantía visible | Sí — "Garanzia 30 giorni soddisfatti o rimborsati" |
| Resumen de orden | Oculto |
| Barra de compradores | Bajo el botón |

---

## 5 · Procesador de pagos

| Campo | Valor |
|---|---|
| Procesador | **ImpulPay** (multidivisa) |
| Moneda | EUR |
| Métodos de pago locales | **ON** (tarjeta, Bancontact, iDEAL, Klarna según país) |

---

## 6 · Subdominio

Elegir una palabra corta sin guiones para el subdominio. Ejemplos:
- `arteterapia`
- `artcreativo`
- `manualeart`

---

## 7 · Idioma del contenido

Configurar el idioma del contenido de la tienda en: **Español (Argentina)** (regla fija, sin importar el mercado destino).

---

## 8 · Verificación post-configuración

Después de configurar todo:
1. Abrir la tienda en el celular y verificar que la landing se vea bien
2. Verificar que el botón de la oferta lleve al checkout (uno solo)
3. Verificar que la imagen del checkout sea el mockup hero
4. Verificar que el precio sea EUR 17,99
5. Hacer un checkout de prueba (sin completar) para ver que todo funcione

---

## 9 · URLs de referencia

| Recurso | URL |
|---|---|
| Hub de entrega (publicado) | https://santilahoz03.github.io/arteterapia-it/acceso/wqkfq2m9xl/ |
| Repo GitHub | https://github.com/santilahoz03/arteterapia-it |
| Mockup hero (catbox) | https://files.catbox.moe/gm1r2t.png |
| Landing completa (local) | [landing-arteterapia-it.html](landing-arteterapia-it.html) |
| Fragmento (local) | [landing-arteterapia-it-fragmento.html](landing-arteterapia-it-fragmento.html) |
| Panel de operaciones | [panel-arteterapia-it.html](proyecto/panel-arteterapia-it.html) |

---

## 10 · Lo que NO tocar desde acá

- **Tracking (píxel + CAPI):** lo conectás vos cuando elijas la cuenta publicitaria
- **Lanzamiento:** solo con orden explícita con cuenta y píxel elegidos
- **Entregables:** ya están publicados, no cambiar la URL del hub
