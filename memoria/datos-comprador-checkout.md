---
name: datos-comprador-checkout
description: Configuración exacta de "Datos del comprador" en el checkout de ImpulTienda para todas las landings
metadata:
  type: feedback
---

En el diseño de checkout de ImpulTienda, la sección "Datos del comprador" siempre queda así:

- Mostrar títulos de los campos: **ON**
- Mostrar "Aquí recibirás tu producto...": **ON**
- Pedir dirección (Entrega/Facturación): **OFF**
- Email (obligatorio): **ON**
- Teléfono: **OFF**
- Nombre: **OFF**
- Apellido: **OFF**

**Why:** El usuario lo definió explícito como estándar para todas las tiendas. Solo email, sin teléfono ni nombre, para reducir fricción en el checkout.

**How to apply:** Al configurar el checkout de cualquier tienda nueva en ImpulTienda (Fase 6 del SOP), usar esta configuración exacta. No importa el procesador de pagos ni el mercado: siempre solo email. Esto reemplaza lo que decía el SOP anterior ("Email + Teléfono").
