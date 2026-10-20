# Checklist tienda ImpulTienda — Biblia Wykrojów PL

> Fecha: 2026-10-09
> Todo lo que necesitás para armar la tienda a mano.

## Archivos preparados (en esta carpeta)

| Archivo | Para qué |
|---|---|
| `fragmento-impultienda.html` | Pegar en Diseño → Contenido → "HTML completo de la tienda" |
| `mockups/1-hero-costura-en-casa-pl.png` | Imagen del producto + bloque Imagen del checkout |
| `mockups/2-caja-costura-en-casa-pl.png` | Solo referencia (NO va en el checkout) |
| `entrega-en-preparacion.html` | Publicar en GitHub Pages como página de entrega provisoria |

## 1 · Crear la tienda

- [ ] Dashboard → Crear nueva tienda
- **Idioma del contenido:** Español (Argentina) ← siempre, sin importar el mercado (según regla `impultienda-idioma-contenido`)
- **Nombre:** `Biblia Wykrojów`
- **Subdominio interno:** `wykroje` (o lo que prefieras, una palabra)
- **Email de contacto:** `customersupport.santi@gmail.com`
- En "Contenido de tu ebook": **"Omitir: voy a pegar mi propio HTML"**

## 2 · Pegar la landing

- [ ] Diseño → Contenido → "HTML completo de la tienda"
- Abrí `fragmento-impultienda.html`, copiá todo (Cmd+A, Cmd+C), pegá en el campo, Guardar
- **Verificar recargando** que el largo sea ~41.600 caracteres

## 3 · Producto principal

- [ ] Crear UN solo producto (toda la oferta junta, NO usar "Agregar bono")
- **Título:** `Biblia Wykrojów Krawiectwa · Ponad 150 Gotowych Wykrojów + 5 Darmowych Poradników`
- **Precio:** `17.99` EUR
- **Precio original (tachado):** `54` EUR
- **Imagen:** subir `mockups/1-hero-costura-en-casa-pl.png`
- **Entrega:** "Pegar link" → la URL de GitHub Pages donde publiques `entrega-en-preparacion.html`
  - URL sugerida: `https://<tu-dominio-github-pages>/wykroje/80fae6p2ko/`
  - Si no tenés dominio todavía: publicá en un repo y después conectás el dominio

## 4 · Dominio propio

- [ ] Elegir subdominio: **una palabra, sin guiones** (ej. `wykroje`)
- [ ] CNAME en tu DNS: nombre `wykroje` → valor `ssl.impultienda.ar` → TTL 3600
- [ ] Verificar propagación: `nslookup -type=CNAME wykroje.<tu-dominio> 8.8.8.8`
- [ ] En ImpulTienda: Configuraciones → Dominio → cargar `wykroje.<tu-dominio>` → "Ya lo hice"
- [ ] Esperar hasta que diga **"SSL activo"** (5-30 min)

⚠️ Todavía no tenés dominio raíz configurado. Cuando lo tengas, sumalo a `CLAUDE.md` → `## Modelar — mis datos`.

## 5 · Pagos

- [ ] Configuraciones → Pagos → moneda **EUR**
- [ ] Procesador: **ImpulPay** (según regla `procesador-pagos-por-mercado`)
- [ ] **Métodos de pago locales: ON** (BLIK, Przelewy24 para Polonia)
- ⚠️ El OAuth a tu cuenta real lo hacés vos

## 6 · Diseño de checkout

| Bloque | Valor |
|---|---|
| Plantilla de diseño | "Impultienda" (la que viene) |
| **Arriba: Cuenta regresiva** | 10 min · texto automático · estilo Banner · color rojo oscuro · barra de tiempo OFF · Margen arriba -6 |
| **Arriba: Imagen** | `1-hero-costura-en-casa-pl.png` (el hero 3:2 blanco, **NO** la caja) · tamaño móvil 90% · espacio arriba 12 px |
| **Abajo: Cupos restantes** | Iniciales 20 · mínimo 3 · texto automático · estilo Badge |
| Texto del botón | `CHCĘ DOSTĘP TERAZ` |
| Color del botón | **Verde oscuro** (nunca azul) |
| Resumen de compra | **Oculto** |
| Anuncio de bonos | **Cantidad** ("+5 bonusów gratis") |
| Sellos de confianza | **Clásico** |
| Garantía | **ON**, **15 días** (igual que la landing) |
| Order bumps | Estilo Clásica · timer ON · mostrar descripción ON |
| Barra superior | ON, texto automático, candado ON |
| Barra de compradores | **ON**, posición **"Bajo el botón"** (cambiarla del default "Arriba de todo") |
| **Datos del comprador** | Solo **Email** ON · Teléfono OFF · Nombre OFF · Apellido OFF · Títulos ON · "Aquí recibirás…" ON · Dirección OFF |

## 7 · Verificación

- [ ] Hacer diagnóstico (botón en la tienda)
- [ ] Recorrer: landing carga → botón hero baja a la oferta → botón oferta va a /checkout → checkout muestra mockup, título, precio y garantía correctos
- [ ] Compra de prueba desde el celular (por dominio propio) → mail con UN solo link → entrega abre
- [ ] Reembolsar la compra de prueba

## Tracking (NO ahora — se hace al lanzar, Fase 10)

Meta Pixel, CAPI token y Utmify se configuran cuando elijas la cuenta publicitaria.
