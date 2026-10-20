---
name: scouting-ritmo-sin-rate-limit
description: la rutina de rastrear (scouting diario) es secuencial sin sub-agentes en el Paso 1, con 45 s entre mercados, canario crochet por mercado y máximo 1 sub-agente en el Paso 2; el paralelismo era la causa del rate limit silencioso de Meta
metadata:
  type: feedback
---

**Regla:** el Paso 1 (barrido) es **secuencial**: el agente principal recorre los mercados uno por uno, sin sub-agentes. Pausa de **45 segundos entre mercados** y **8-15 s entre búsquedas** dentro de cada mercado. En el Paso 2 (arsenales), máximo **1 sub-agente a la vez** (esperar que termine antes de lanzar el siguiente). No hay paralelismo en el Paso 1.

**Canario:** búsqueda de "crochet" en `country=ALL` antes de cada mercado. Si da cero → rate limit activo → pausar todo, esperar 3 minutos y reintentar. Si sigue en cero → esperar 5 minutos más. Tras 2 esperas seguidas con cero → guardar avance y cerrar con lo que haya.

**Keywords:** de formato ("instant download", "printable", "scaricabile", etc.), no de nicho. Las keywords de formato descubren cualquier nicho sin cerrar el barrido. Ver `scouting/config.md` para la tabla completa.

**Why:** la versión anterior lanzaba 2-3 sub-agentes en paralelo, cada uno con su pestaña de Ad Library. Meta veía docenas de requests simultáneos al mismo IP, detectaba bot y aplicaba rate limit silencioso: la página cargaba normalmente pero devolvía 0 resultados sin ningún error visible. Los agentes interpretaban el vacío como "no hay ofertas" cuando en realidad Meta no las mostraba. El canario también fallaba si ya había rate limit activo. Las keywords de nicho (recipe book, woodworking plans) cerraban el barrido a esos nichos y nunca encontraban nada nuevo.

**How to apply:** vive en el prompt de la tarea `scouting-diario` (SKILL.md). La rutina tarda ~2 horas en lugar de ~40 min, pero como corre a las 09:20 sin supervisión, el panel está listo antes de empezar el día. Verificación: si el encabezado del Paso 1 dice "SECUENCIAL, agente principal (sin sub-agentes)" y las keywords de config.md son de formato (no de nicho), está bien. Si termina en 15 min con 0 resultados, algo no está aplicado.

**Para volver a como estaba:** el prompt anterior sigue en `~/ZEA-kits/kit-01-cazar/rutinas/scouting-diario.md` (versión de fábrica).

**Actualización 2026-10-11:** reescrita desde cero según la guía de reparación. Reemplaza la versión anterior (2026-10-08/09) que permitía 2-3 sub-agentes en paralelo.
