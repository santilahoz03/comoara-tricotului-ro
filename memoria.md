# Memoria — índice de reglas

Una línea por regla: `[nombre](memoria/slug.md) — cuándo aplica, en pocas palabras`.
Claude la lee al empezar y, antes de cada tarea, abre ENTERAS las reglas que aplican.
Para sumar una: corregí a Claude y terminá con "guardalo en memoria".

## Stack y generación
- [Tier más barato siempre](memoria/tier-mas-barato-siempre.md) — antes de generar: catálogo, 1K/720p, reciclar, avisar costo
- [Claves nunca en frontend](memoria/claves-nunca-en-frontend.md) — nada de keys en HTML/JS/repos, proxy del lado del servidor
- [Costo real imagen 1K en kie.ai](memoria/kie-imagen-costo-real.md) — ~USD 0,03 por imagen 1K (no 0,06), verificar con saldo antes/después
- [ffmpeg-full para subtítulos](memoria/ffmpeg-full-para-subtitulos.md) — "No option name near" = falta libass o ruta con espacios
- [Una .skill es un zip](memoria/skill-es-un-zip.md) — unzip -l / unzip -o -d ~/.claude/skills/ (Windows sin unzip: python -m zipfile)
- [Gemini: clave AIza + TTS troceado](memoria/gemini-clave-aiza-y-tts.md) — token AQ. no sirve, >25 palabras corta, 429 → edge-tts

## Meta
- [Facebook solo en el navegador de Claude](memoria/facebook-solo-navegador-de-claude.md) — nunca el Chrome personal logueado

## Landings y ofertas
- [Dashboard de horas: sumar países](memoria/dashboard-horas-agregar-paises.md) — al modelar un país nuevo, agregarlo (con todas sus zonas) a OUTPUTS/dashboard-horas
- [Testimonios sin edad](memoria/testimonios-sin-edad.md) — solo nombre + lugar, nunca la edad
- [Datos comprador checkout](memoria/datos-comprador-checkout.md) — solo email ON, todo lo demás OFF (teléfono, nombre, apellido)
- [ImpulTienda: preguntar automático o manual](memoria/impultienda-preguntar-automatico-o-manual.md) — tras el QC de la landing y antes de tocar ImpulTienda: preguntar si lo hago yo (Claude in Chrome) o se lo entrego para hacerlo él

## Ads y réplicas
- [Subtítulos sobre zona Vmake](memoria/subtitulos-sobre-zona-vmake.md) — MarginV distinto por video, medido contra el original, para cubrir artefactos de Vmake
- [Subtítulos posición exacta Vmake](memoria/subtitulos-posicion-exacta-vmake.md) — medir pixel por pixel la posición de los subs originales; max 2 renglones; font 44 para idiomas largos; badges traducidos como popups
- [Guiones fieles al original](memoria/guiones-fieles-al-original.md) — traducción 100% fiel del guión hablado, vocabulario del mercado destino, sin nombres propios del original
- [Subtítulos en MAYÚSCULAS + color marca](memoria/subtitulos-mayusculas-color-marca.md) — siempre MAYÚSCULAS, color principal sacado de PALETTE.md, nunca blanco genérico
- [Voz expresiva, no IA](memoria/voz-expresiva-no-ia.md) — voz en off emotiva y humana; preguntas que suenen a preguntas; ElevenLabs stability=0.45/style=0.40
- [Voz mismo género que el original](memoria/voz-mismo-genero-que-original.md) — escuchar vocals.mp3 antes de elegir voz; hombre→hombre, mujer→mujer
- [Música original idéntica](memoria/musica-original-identica.md) — la música de cada ad = la del original (htdemucs no_vocals), volume=0.70, nunca genérica
- [Velocidad natural del video](memoria/velocidad-natural-video.md) — factor cerca de 1.0; si F sale de [0.75, 1.15] ajustar guion/voz, no forzar el video
- [Renovación de creativos 70/30](memoria/renovacion-creativos-70-30.md) — al analizar anuncios/métricas o armar una tanda: 6 piezas (4 macro + 2 micro), base en ADS/_base-renovacion/, sin gastar ni generar sin orden
- [SOP creativos: compuertas de aprobación](memoria/sop-creativos-compuertas.md) — antes de analizar, producir, gastar, publicar o reeditar una VSL: 6 compuertas, ad1 + cinco = seis, sin gasto sin OK con tope

## Forma de trabajar
- [Cortar la iteración a las 2 rondas](memoria/cortar-iteracion-a-las-2-rondas.md) — a la tercera, otro enfoque
- [Hablar rioplatense y directo](memoria/hablar-rioplatense-y-directo.md) — en toda respuesta: vos, directo, sin jerga
- [Scouting: contar creativos distintos](memoria/scouting-contar-creativos-distintos.md) — antes de dar un candidato por limpio: videos distintos (no anuncios), físico y marca personal a ojo, comida atada a un país
- [Scouting: siempre el panel con botones](memoria/scouting-siempre-panel-con-botones.md) — panel Sí/No + "Modelar ya" en Sí + campo "Por qué" en No, siempre
- [Scouting: ritmo sin rate limit](memoria/scouting-ritmo-sin-rate-limit.md) — antes de lanzar sub-agentes sobre la Biblioteca: máx. 2-3 a la vez, pausas, canario por ola, alcance de config; 15 limpios estrictos
- [Scouting: exigir múltiples videos](memoria/scouting-exigir-videos-multiples.md) — anotar cantidad de videos en la ficha y reflejarlo en el score, pero NO es filtro eliminatorio (filtro E = 1+ video)
- [Scouting: no repetir ofertas vistas](memoria/scouting-no-repetir-ofertas-vistas.md) — nunca presentar como candidato algo de corridas anteriores
- [Scouting: verificar landing viva](memoria/scouting-verificar-landing-viva.md) — visitar la landing antes de presentar; si no carga, no va a candidato
- [Scouting: marca personal estricto](memoria/scouting-marca-personal-estricto.md) — instructora nombrada en landing/ads = marca personal aunque el brand sea genérico
- [Scouting: calidad sobre cantidad](memoria/scouting-calidad-sobre-cantidad.md) — usar los filtros originales de criterios-oferta.md (15 ads / 3 días / 1 video), NUNCA subir el piso internamente; el usuario decide con el veredicto
- [Scouting: volumen moderado](memoria/scouting-volumen-moderado.md) — máximo ~80 queries y 2-3 agentes; nunca barridos masivos de 400+ queries que queman el rate limit
- [Scouting: verificar datos del agente](memoria/scouting-verificar-datos-agente.md) — cruzar blocklist completa y verificar datos (ads, videos, antigüedad) en el navegador antes de presentar
- [Scouting: variedad de nichos y arbitraje](memoria/scouting-variedad-nichos-arbitraje.md) — 40%+ queries en nichos nuevos, priorizar señal A, máx ~4-5 del mismo nicho por corrida
- [Modelar: preguntar modo y cantidad de anuncios](memoria/modelar-preguntar-modo-y-cantidad-anuncios.md) — en la Fase 9 de /modelar, selector de clic: réplica o producción propia, y luego 10 / 6 / otro número
- [Modelar: Set Definitivo para Ads](memoria/modelar-set-definitivo-ads.md) — antes del tracking/lanzamiento, texto primario + título + descripción con el estilo del arsenal de la tienda original
- [Popup: extender más allá del video](memoria/popup-extender-mas-alla-del-video.md) — t1 del popup > duración compuesta (atempo estira el video, el original queda visible al final)
- [Subtítulos: sin overlaps de Whisper](memoria/subtitulos-sin-overlaps-whisper.md) — corregir overlaps del ASS antes de componer (start >= prev_end), si no aparece doble texto
- [ImpulTienda: solo con el MCP](memoria/impultienda-solo-mcp.md) — usar solo el conector MCP de ImpulTienda, cuando haga falta y el usuario lo pida; nunca Claude in Chrome
- [Akvarellakademien SE estado](memoria/akvarellakademien-se-estado.md) — tienda ImpulTienda configurada 2026-10-14, campaña lanza 2026-10-15, 6 ads + hub 9 PDFs, 0 USD producción
