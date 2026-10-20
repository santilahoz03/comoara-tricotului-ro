---
name: dashboard-horas-agregar-paises
description: al modelar una oferta para un país nuevo (o al cerrar el paso de mercado de /modelar): agregar el país y TODAS sus zonas horarias al dashboard de horas
type: project
fecha: 2026-10-08
---

**Regla:** cada vez que modelemos una oferta en un país que todavía no está en `OUTPUTS/dashboard-horas/index.html`, lo agrego al arreglo `PAISES` con todas sus zonas horarias (nombre IANA). Nunca repito un país que ya está.

**Por qué:** Santi (Argentina, UTC-3) quiere ver la hora actual de cada mercado modelado para coordinar pauta y soporte. Pedido el 2026-10-08; arrancó con México (4 zonas), Rumania y Polonia.

**Cómo aplicar:** al terminar el modelado de un país nuevo, revisar el arreglo `PAISES`; si falta, sumar `{pais, cod, agregado, zonas:[{nombre, tz}]}` con todas las zonas del país, y avisar en el resumen final. Agregar también su bandera SVG a `FLAGS` (clave = código ISO de 2 letras, viewBox 0 0 30 20, más `colores` para la franja de las tarjetas). Para países multi-zona (US, BR, CA, AU, MX, etc.) incluir cada zona.
