---
name: renovacion-creativos-70-30
description: antes de analizar anuncios o métricas, proponer una tanda de anuncios nuevos, o cargar resultados: aplicar el sistema de renovación 70/30 (6 piezas por tanda) y llevar la base ADS/_base-renovacion/
type: playbook
fecha: 2026-10-08
---

**Regla:** la renovación de creativos sigue el sistema 70/30 de `WIKI/renovacion-creativos-70-30.md` y se registra en `ADS/_base-renovacion/` (fichas, métricas, aprendizajes). Leer el tema de la WIKI entero antes de cada tarea de renovación.

**Ciclo y pedidos que lo activan:**
1. **Analizar** ("analizá estos anuncios y este corte de métricas"): desglosar cada anuncio (ángulo, formato creativo, formato de guion, hook, narrador, prueba, oferta, CTA), guion literal separado del análisis, hechos / hipótesis / confianza, actualizar fichas y veredictos. **No proponer guiones todavía.**
2. **Renovar** ("preparé la próxima tanda"): 6 piezas, normalmente 4 macro (R/I) + 2 micro (M), buscando 70/30 acumulado. Por pieza: ID, parent, tipo, variable que cambia, variables fijas, hipótesis y métrica de evaluación; después hook, guion listo, escenas, prueba real y CTA. Se registra como **pendiente de producción**.
3. **Aprender** ("resultados de la tanda [ID], período [desde/hasta]"): vincular por ID, guardar el corte nuevo sin duplicar acumulados, revisar hipótesis y decir qué explorar, explotar o volver a medir.

**Reglas fijas:**
- **No generar ni publicar piezas ni gastar sin instrucción explícita** del usuario (se suma a la regla de costos de CLAUDE.md).
- IDs únicos, `parent_id`, tanda. No sobrescribir guiones, no borrar perdedores, no tocar los `registro.csv` originales.
- Un dato que no consta es `no observado` o `N/D`; no inventar escenas, testimonios, resultados ni beneficios. Si no puedo ver un video, lo digo.
- No mezclar monedas ni sumar atribuciones de distintas fuentes ni períodos que se solapan.
- Los M salen de ganadores **recientes y verificados**; si no hay, informar la excepción y priorizar explorar. No llenar el 70% con cambios cosméticos.
- No afirmar que voy a monitorear solo: no hay rutina programada de renovación.

**Por qué:** el usuario instaló el sistema el 2026-10-08 desde el PDF de la mentoría (`RAW/zea-sistema-renovacion-creativos.pdf`) para que cada tanda parta de lo aprendido en la anterior. Prevalece sobre la rutina `renovacion-diaria` del kit 03.

**Cómo aplicar:** al recibir anuncios o métricas, abrir primero `ADS/_base-renovacion/` y la ficha del tema. Verificación antes de dar una tanda por lista: cada pieza tiene ID y fuente, los parents están vigentes, el 70% tiene cambios macro reales, las micro conservan el concepto, hay hipótesis y criterio de evaluación, y la base quedó guardada.

**Para eliminarla:** borrar este archivo y su línea en `memoria.md`, la línea de CLAUDE.md que la nombra y, si se quiere, `ADS/_base-renovacion/` y el tema de la WIKI.
