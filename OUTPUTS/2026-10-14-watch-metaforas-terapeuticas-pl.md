---
fecha: 2026-10-14
pedido: /watch sobre 4 videos originales del anunciante Metáforas Terapéuticas (PL)
temas: ads, metaforas-terapeuticas-pl, watch
---

# /watch — Metáforas Terapéuticas Ilustradas (ES→PL)

## Videos analizados

| Slug | ID Meta | Duración | Guion propio |
|---|---|---|---|
| pl-v2623 | 2623242251431673 | 37s | A1 (V4) |
| pl-v1395 | 1395230399238355 | 69s | A2 (V5) |
| pl-v1426 | 1426495279281222 | 72s | A3 (V2) |
| pl-v9879 | 987919614152469 | 110s | A4 (V3) |

Frames extraídos cada 2s → `work/pl-v*/frames/`

---

## ADN Visual (aplica a los 4 videos)

### Formato
- 9:16 vertical, 720×1280, 30 fps
- Sin cara de locutor: voz en off sobre B-roll + ilustraciones

### Hook (0-3s)
- **Pill card púrpura** (badge redondeado violeta) en el TERCIO SUPERIOR de pantalla
- Línea 1 en la pill (blanca, negrita): tema de la metáfora o nombre del psicólogo
- Línea 2 en caja blanca debajo (texto oscuro): subtítulo del hook
- Fondo del hook: la primera escena de B-roll (no negro sólido)

### B-Roll
- **Primario**: imágenes generadas por IA en estilo ilustración histórica (óleo/acuarela) o anime/watercolor — escenas de consultorios, naturaleza simbólica, figuras históricas escribiendo en estudios
- **Secundario**: footage real de persona leyendo/usando el producto (solo en la parte de reveal del producto)
- **Pacing**: 2-3 segundos por toma, sin excepción
- No hay B-roll de footage real de terapia (solo los competidores con IA)

### Subtítulos — ESTILO EXACTO
- **BorderStyle=3**: caja negra semi-opaca detrás de cada línea
- **Texto**: MAYÚSCULAS, blanco, Arial Bold, ~48px
- **Keyword amarilla**: la última palabra de cada chunk de 4 palabras, en amarillo (`&H0000FFFF` en ASS)
- **Posición**: MarginV=150 (sobre el borde inferior, no en el límite)
- **Sin swell ni efecto de apertura**

### Overlays progresivos (V4 específico)
- Iconos emoji 3D dorados (🌳 árbol, 🔑 llave, 🌊 ola) que aparecen y se acumulan sobre el personaje
- Se añaden uno por uno a medida que se introducen conceptos
- Estilo: brillante, dorado, flotando sobre el personaje

### Reveal del producto (últimos 5-7s en ads cortos)
- Transition de fade cálido (naranja/durazno) hacia footage real
- Popup de mockup del producto: card flotante con el mockup visible sobre la persona que lee
- En V3: muestra páginas físicas del libro real
- En V4/V5: mockup digital (card overlay con tapa del producto)
- Estilo mockup en V4: fondo borroso del mismo mockup + mockup nítido encima

### Música
- Extraída con htdemucs (`no_vocals.mp3`) del video original V3 (110s)
- Volumen relativo: 0.18 (fondo suave)
- NO usar música genérica de librería

---

## Por video

### V4 (A1, 37s) — Hook: "Carl Jung hizo un descubrimiento"
- Estilo: ilustración al óleo, paleta cálida (marrones, dorados, verdes oscuros)
- Personajes: mujer victoriana en estudio → hombre victoriano escribiendo diario
- Overlay: iconos emoji dorados (🌳→🔑→🌊) acumulándose en el pecho del personaje
- Reveal: fade naranja → mujer moderna leyendo tablet → mockup card flotando sobre ella
- Interior del producto: páginas con metáforas animadas (anime style, 2 columnas)

### V5 (A2, 69s) — Hook: "El Barco Sin Ancla"
- Hook card con fondo: pulpo AI-gen leyendo libro en biblioteca oscura (muy creativo)
- Mezcla footage real (hombre ~40 en sofá) + escenas IA de barco en mar (tranquilo→tormentoso)
- Subtítulos: barra negra + amarillo en keyword, idéntico a V4
- Reveal: páginas del producto (scrolling por metáforas, "X de 102")

### V2 (A3, 72s) — Hook: "La observación clínica de Carl Jung"
- Estilo: acuarela/anime, colores pasteles y azulados
- Consultorio terapéutico ilustrado con planetas flotando
- Personajes anime smiling (producto tiene ilustraciones anime)

### V3 (A4, 110s) — Hook: "La paciente con lista infinita"
- Footage REAL del libro físico impreso (manos sobre el libro en mesa)
- Scrolling por páginas físicas impresas con illus. anime + texto
- Revela el libro físico como producto (el producto se puede imprimir también)

---

## Reglas adaptadas para nuestra producción (PL)

1. **Siempre pill card púrpura** en los primeros 3-4s (texto en PL)
2. **Subtítulos**: BorderStyle=3 negro + MAYÚSCULAS blancas + última palabra del chunk en amarillo
3. **Música**: `work/pl-v9879/no_vocals.mp3`, vol=0.18
4. **Mockup**: popup con fondo borroso del mismo mockup + mockup nítido, últimos 6s
5. **Sin sfx de apertura**: sin swell, sin whoosh al inicio
6. **Pacing**: 2.5s por corte de B-roll (mínimo 2.0, máximo 3.0)
7. **Sin barrel de B-roll de chroma key** (therapy_01, therapy_02 = EXCLUIDOS)

---

## Prompts de producción

### 6a. Guiones adaptados al polaco
→ Ver `ADS/METAFORAS-TERAPEUTICAS-PL/2026-10-14/guiones.md`

### 6b. Técnico
- Formato: réplica B-roll + voz en off
- Voz: Sarah (ElevenLabs, eleven_multilingual_v2)
- B-roll: clips reales del nicho (therapy, stressed, writing, brain, boat, river, flowers)
- Producido con: `producir_ads_v2.py` (script en scratchpad)
- Hook card: PNG PIL (pill púrpura + caja blanca)
- Mockup popup: PNG PIL (blurred bg + sharp fg)
