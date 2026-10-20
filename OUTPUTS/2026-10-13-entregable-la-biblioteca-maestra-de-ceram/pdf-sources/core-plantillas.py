#!/usr/bin/env python3
"""Genera core-plantillas.html con 155 páginas de plantillas de cerámica (SVG técnico).
Costo: $0. Todo es HTML + SVG inline → PDF con Chrome headless."""

import math, random, textwrap

# ── Paleta ──
BG      = "#ffffff"
PAPER   = "#fdf8f2"
INK     = "#121212"
INK_S   = "#555555"
ACCENT  = "#c8722a"
ACC_DK  = "#1a0f08"
SUCCESS = "#22a06b"
LINE    = "#e7e1da"

# ── Catálogo: 155 piezas ──
# Cada pieza: (nombre, categoría, técnica, alto_mm, ancho_sup_mm, ancho_inf_mm, tipo_forma)
# tipo_forma: bowl, mug, plate, vase, pot, pitcher, jar, lid, box, lamp, tray, cup, bottle, candle

CATEGORIAS = {
    "Cocina": "kitchen",
    "Hogar": "home",
    "Jarrones": "vases",
    "Macetas": "pots",
    "Iluminación": "lighting",
}

CAT_COLORS = {
    "Cocina": "#c8722a",
    "Hogar": "#1a0f08",
    "Jarrones": "#555555",
    "Macetas": "#22a06b",
    "Iluminación": "#888888",
}

TECNICAS = {"Losa": "slab", "Rollo": "coil", "Pellizco": "pinch"}

# Distribución de técnicas por categoría para coincidir con la landing:
# Total: Losa 68, Rollo 44, Pellizco 43 = 155
TECH_DIST = {
    "Cocina":      (31, 20, 19),   # 70
    "Hogar":       (13,  9,  8),   # 30
    "Jarrones":    (11,  7,  7),   # 25
    "Macetas":     ( 7,  4,  4),   # 15
    "Iluminación": ( 6,  4,  5),   # 15
}

def _tech_seq(cat, count):
    nl, nr, np = TECH_DIST[cat]
    seq = ["Losa"]*nl + ["Rollo"]*nr + ["Pellizco"]*np
    assert len(seq) == count
    random.seed(hash(cat) & 0xFFFFFFFF)
    random.shuffle(seq)
    return seq

def _items():
    """Return list of 155 pottery items."""
    items = []
    n = 0

    # ── COCINA (70 items) ──
    cocina = [
        # Tazones
        ("Tazón de Cereal Clásico", 80, 140, 65, "bowl"),
        ("Tazón Sopero Hondo", 100, 160, 70, "bowl"),
        ("Tazón para Ramen", 90, 180, 80, "bowl"),
        ("Tazón de Ensalada Individual", 70, 150, 65, "bowl"),
        ("Tazón para Mezclar Grande", 150, 260, 100, "bowl"),
        ("Tazón para Mezclar Mediano", 120, 200, 85, "bowl"),
        ("Tazón para Mezclar Pequeño", 90, 150, 70, "bowl"),
        ("Tazón para Fruta", 85, 200, 90, "bowl"),
        ("Tazón para Servir Ovalado", 80, 220, 95, "bowl"),
        ("Tazón para Arroz", 65, 120, 55, "bowl"),
        ("Tazón para Matcha", 75, 120, 50, "bowl"),
        ("Tazón para Granola", 70, 130, 60, "bowl"),
        # Tazas
        ("Taza de Café Clásica", 90, 80, 55, "mug"),
        ("Taza de Café Grande", 105, 90, 60, "mug"),
        ("Taza de Té Japonesa", 70, 75, 50, "mug"),
        ("Taza para Espresso", 55, 60, 40, "mug"),
        ("Taza de Viaje (sin tapa)", 130, 85, 60, "mug"),
        ("Taza Campestre", 100, 95, 65, "mug"),
        ("Taza para Capuchino", 75, 90, 55, "mug"),
        # Platos
        ("Plato Llano Grande", 25, 260, 260, "plate"),
        ("Plato Llano Mediano", 22, 220, 220, "plate"),
        ("Plato de Postre", 20, 190, 190, "plate"),
        ("Plato Hondo para Pasta", 45, 240, 240, "plate"),
        ("Plato para Pan", 18, 160, 160, "plate"),
        ("Plato Ovalado para Servir", 30, 300, 200, "plate"),
        ("Plato para Sushi", 20, 280, 120, "plate"),
        ("Plato para Pizza", 15, 300, 300, "plate"),
        # Jarras
        ("Jarra de Agua 1L", 200, 100, 75, "pitcher"),
        ("Jarra para Leche", 120, 80, 55, "pitcher"),
        ("Jarra para Crema", 90, 60, 40, "pitcher"),
        ("Jarra para Jugo", 180, 95, 70, "pitcher"),
        # Contenedores
        ("Azucarera con Tapa", 80, 90, 60, "jar"),
        ("Salero de Mesa", 60, 50, 40, "jar"),
        ("Pimentero de Mesa", 70, 45, 35, "jar"),
        ("Mantequillera", 60, 120, 80, "box"),
        ("Aceitera con Vertedor", 150, 70, 55, "bottle"),
        ("Vinagrera", 140, 65, 50, "bottle"),
        # Bandejas y fuentes
        ("Fuente Rectangular para Horno", 60, 280, 200, "tray"),
        ("Bandeja para Tapas", 25, 300, 150, "tray"),
        ("Tabla para Quesos", 15, 250, 150, "tray"),
        ("Fuente para Gratín", 55, 220, 160, "tray"),
        # Cuencos y cazuelas
        ("Cazuela Individual con Tapa", 90, 140, 80, "jar"),
        ("Cuenco para Dip", 50, 100, 50, "bowl"),
        ("Cuenco para Salsas", 40, 80, 40, "bowl"),
        ("Cuenco Apilable", 60, 110, 55, "bowl"),
        # Utensilios
        ("Reposa Cucharas", 20, 200, 80, "tray"),
        ("Soporte para Huevos (6)", 35, 180, 180, "tray"),
        ("Tapa Universal 20 cm", 30, 200, 200, "lid"),
        ("Tapa Universal 16 cm", 25, 160, 160, "lid"),
        # Varios cocina
        ("Mortero con Mano", 80, 120, 70, "bowl"),
        ("Bol para Aceitunas", 55, 100, 50, "bowl"),
        ("Cuchara Medidora Set", 30, 50, 30, "cup"),
        ("Huevera Individual", 35, 50, 35, "cup"),
        ("Porta Servilletas", 100, 130, 80, "box"),
        ("Porta Palillos", 60, 40, 30, "jar"),
        ("Quesera con Tapa", 100, 180, 120, "jar"),
        ("Tetera Clásica", 130, 140, 80, "pitcher"),
        ("Tetera Japonesa", 100, 120, 70, "pitcher"),
        ("Infusor de Té Individual", 80, 70, 45, "cup"),
        ("Cuenco para Fondue", 100, 160, 80, "bowl"),
        ("Plato para Torta con Pie", 90, 260, 120, "plate"),
        ("Copa para Helado", 100, 100, 55, "cup"),
        ("Platillo para Taza", 20, 140, 140, "plate"),
        ("Cuenco para Palomitas", 120, 200, 90, "bowl"),
        ("Dispensador de Miel", 120, 70, 50, "jar"),
        ("Recipiente para Sal Gruesa", 70, 90, 60, "jar"),
        ("Olla de Barro Mediana", 160, 180, 100, "pot"),
        ("Olla de Barro Pequeña", 120, 140, 80, "pot"),
        ("Cuenco con Vertedor", 80, 130, 65, "bowl"),
        ("Plato Dividido para Niños", 30, 200, 200, "plate"),
    ]
    tseq = _tech_seq("Cocina", len(cocina))
    for i, (nom, h, ws, wi, forma) in enumerate(cocina):
        items.append((nom, "Cocina", tseq[i], h, ws, wi, forma))

    # ── HOGAR (30 items) ──
    hogar = [
        ("Portavelas Cilíndrico", 80, 70, 70, "candle"),
        ("Portavelas Cónico", 60, 80, 50, "candle"),
        ("Portavelas Bajo", 40, 90, 90, "candle"),
        ("Porta Incienso", 15, 200, 40, "tray"),
        ("Cenicero Moderno", 35, 120, 80, "bowl"),
        ("Joyero con Tapa", 50, 100, 70, "jar"),
        ("Jabonera", 20, 120, 80, "tray"),
        ("Dispensador de Jabón", 160, 70, 55, "bottle"),
        ("Vaso para Cepillos", 110, 75, 60, "mug"),
        ("Bandeja para Llaves", 20, 180, 100, "tray"),
        ("Porta Lápices", 110, 80, 65, "mug"),
        ("Organizador de Escritorio", 80, 150, 100, "box"),
        ("Florero de Mesa Bajo", 120, 100, 60, "vase"),
        ("Florero de Mesa Alto", 200, 80, 55, "vase"),
        ("Caja de Recuerdos", 80, 140, 100, "box"),
        ("Plato Decorativo de Pared", 30, 250, 250, "plate"),
        ("Cuenco Decorativo Grande", 100, 250, 100, "bowl"),
        ("Porta Velas Votivas (set 3)", 50, 60, 50, "candle"),
        ("Marco de Foto", 150, 130, 130, "box"),
        ("Campana Decorativa", 120, 80, 80, "jar"),
        ("Difusor de Aromas", 100, 80, 55, "bottle"),
        ("Posavasos (set 4)", 8, 100, 100, "plate"),
        ("Reloj de Pared (base)", 20, 250, 250, "plate"),
        ("Portalibros (par)", 130, 100, 80, "box"),
        ("Maceta de Interior Pequeña", 100, 100, 70, "pot"),
        ("Maceta de Interior Mediana", 130, 140, 90, "pot"),
        ("Colgador de Pared Maceta", 150, 120, 80, "pot"),
        ("Tiesto Suculentas Mini", 50, 70, 50, "pot"),
        ("Bandeja Baño", 25, 250, 120, "tray"),
        ("Portacepillos Familiar", 100, 100, 80, "mug"),
    ]
    tseq = _tech_seq("Hogar", len(hogar))
    for i, (nom, h, ws, wi, forma) in enumerate(hogar):
        items.append((nom, "Hogar", tseq[i], h, ws, wi, forma))

    # ── JARRONES (25 items) ──
    jarrones = [
        ("Jarrón Clásico Alto", 280, 120, 70, "vase"),
        ("Jarrón Clásico Mediano", 220, 110, 65, "vase"),
        ("Jarrón Botella Estrecho", 300, 60, 60, "bottle"),
        ("Jarrón Bud (una flor)", 150, 40, 35, "bottle"),
        ("Jarrón Cilíndrico", 250, 100, 100, "vase"),
        ("Jarrón Esférico", 200, 180, 70, "vase"),
        ("Jarrón Cónico Invertido", 200, 80, 140, "vase"),
        ("Jarrón con Cuello Largo", 320, 50, 80, "vase"),
        ("Jarrón Ánfora", 260, 60, 60, "vase"),
        ("Jarrón Ondulado", 240, 130, 70, "vase"),
        ("Jarrón Cuadrado", 200, 100, 100, "box"),
        ("Jarrón de Piso Grande", 400, 160, 90, "vase"),
        ("Jarrón de Piso Mediano", 350, 140, 80, "vase"),
        ("Jarrón para Ramas Secas", 350, 80, 60, "vase"),
        ("Jarrón Trompeta", 280, 160, 50, "vase"),
        ("Jarrón Gota", 180, 140, 40, "vase"),
        ("Jarrón Ikebana Bajo", 80, 200, 100, "bowl"),
        ("Jarrón Doble Boca", 200, 100, 60, "vase"),
        ("Jarrón Texturizado", 220, 120, 65, "vase"),
        ("Jarrón Asimétrico", 240, 130, 60, "vase"),
        ("Jarrón Rústico", 200, 130, 75, "vase"),
        ("Jarrón Minimalista", 250, 90, 70, "vase"),
        ("Jarrón con Asas", 220, 120, 65, "vase"),
        ("Jarrón Colección (set 3)", 180, 80, 50, "vase"),
        ("Jarrón Decorativo Bajo", 120, 160, 80, "vase"),
    ]
    tseq = _tech_seq("Jarrones", len(jarrones))
    for i, (nom, h, ws, wi, forma) in enumerate(jarrones):
        items.append((nom, "Jarrones", tseq[i], h, ws, wi, forma))

    # ── MACETAS (15 items) ──
    macetas = [
        ("Maceta Cónica Estándar", 160, 180, 110, "pot"),
        ("Maceta Cilíndrica", 180, 150, 150, "pot"),
        ("Maceta Cuadrada", 150, 140, 140, "box"),
        ("Maceta Colgante con 3 Orificios", 120, 160, 100, "pot"),
        ("Maceta Baja para Bonsái", 80, 250, 180, "pot"),
        ("Maceta Alta para Bambú", 300, 140, 120, "pot"),
        ("Maceta con Plato Integrado", 140, 160, 100, "pot"),
        ("Maceta Escalonada", 200, 180, 100, "pot"),
        ("Maceta para Hierbas (triple)", 120, 300, 100, "tray"),
        ("Maceta Autoregante", 150, 140, 100, "pot"),
        ("Maceta de Pared", 130, 140, 60, "pot"),
        ("Maceta Mini Suculenta", 60, 80, 60, "pot"),
        ("Jardinera Rectangular", 120, 300, 120, "box"),
        ("Maceta con Patas", 180, 160, 120, "pot"),
        ("Maceta Hexagonal", 140, 150, 130, "pot"),
    ]
    tseq = _tech_seq("Macetas", len(macetas))
    for i, (nom, h, ws, wi, forma) in enumerate(macetas):
        items.append((nom, "Macetas", tseq[i], h, ws, wi, forma))

    # ── ILUMINACIÓN (15 items) ──
    iluminacion = [
        ("Lámpara de Mesa Cilíndrica", 250, 150, 120, "lamp"),
        ("Lámpara de Mesa Cónica", 280, 180, 100, "lamp"),
        ("Lámpara Colgante Campana", 200, 250, 50, "lamp"),
        ("Lámpara Colgante Esférica", 200, 200, 40, "lamp"),
        ("Farol de Jardín", 300, 150, 120, "lamp"),
        ("Portavelas de Pared", 120, 100, 60, "candle"),
        ("Candelabro de 3 Brazos", 150, 250, 80, "candle"),
        ("Lámpara Difusora Perforada", 220, 140, 100, "lamp"),
        ("Pantalla Cilíndrica", 200, 160, 160, "lamp"),
        ("Luminaria de Piso", 400, 180, 140, "lamp"),
        ("Portavelas Farolito", 150, 100, 80, "candle"),
        ("Lámpara con Calado", 250, 160, 110, "lamp"),
        ("Aplique de Pared Semicircular", 120, 180, 180, "lamp"),
        ("Lámpara Botella", 350, 120, 90, "lamp"),
        ("Portavelas Linterna", 180, 110, 90, "candle"),
    ]
    tseq = _tech_seq("Iluminación", len(iluminacion))
    for i, (nom, h, ws, wi, forma) in enumerate(iluminacion):
        items.append((nom, "Iluminación", tseq[i], h, ws, wi, forma))

    return items

ITEMS = _items()
assert len(ITEMS) == 155, f"Expected 155 items, got {len(ITEMS)}"

# ── SVG generators ──

def _mm_to_in(mm):
    return round(mm / 25.4, 1)

def _dim_line(x1, y1, x2, y2, label, side="right", color=ACCENT):
    """Dimension line with arrows and label."""
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    vertical = abs(x1 - x2) < 2
    parts = []
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="0.8" stroke-dasharray="3,2"/>')
    if vertical:
        # arrows
        parts.append(f'<polygon points="{x1-3},{y1+6} {x1+3},{y1+6} {x1},{y1}" fill="{color}"/>')
        parts.append(f'<polygon points="{x2-3},{y2-6} {x2+3},{y2-6} {x2},{y2}" fill="{color}"/>')
        tx = x1 + (12 if side == "right" else -12)
        anchor = "start" if side == "right" else "end"
        parts.append(f'<text x="{tx}" y="{mid_y}" fill="{color}" font-size="9" text-anchor="{anchor}" dominant-baseline="middle" font-family="Inter, Arial, sans-serif">{label}</text>')
    else:
        parts.append(f'<polygon points="{x1+6},{y1-3} {x1+6},{y1+3} {x1},{y1}" fill="{color}"/>')
        parts.append(f'<polygon points="{x2-6},{y2-3} {x2-6},{y2+3} {x2},{y2}" fill="{color}"/>')
        parts.append(f'<text x="{mid_x}" y="{y1 - 8}" fill="{color}" font-size="9" text-anchor="middle" font-family="Inter, Arial, sans-serif">{label}</text>')
    return "\n".join(parts)

def _profile_path(h, wt, wb, forma, cx=200, base_y=280):
    """Generate SVG path for pottery profile (front view, symmetric).
    Returns (path_d, top_y, bot_y, left_top, right_top, left_bot, right_bot)"""
    top_y = base_y - h * 0.7  # scale factor for SVG
    bot_y = base_y
    hw_top = wt * 0.7 / 2
    hw_bot = wb * 0.7 / 2
    lt = cx - hw_top
    rt = cx + hw_top
    lb = cx - hw_bot
    rb = cx + hw_bot

    if forma in ("bowl", "cup"):
        # curved sides
        cp1x_l = lt - (lb - lt) * 0.3
        cp1x_r = rt + (rt - rb) * 0.3
        cpy = top_y + (bot_y - top_y) * 0.6
        d = f"M {lt},{top_y} C {cp1x_l},{cpy} {lb},{bot_y-5} {lb},{bot_y} L {rb},{bot_y} C {rb},{bot_y-5} {cp1x_r},{cpy} {rt},{top_y} Z"
    elif forma == "mug":
        # straight sides with slight taper + handle
        cpy = top_y + (bot_y - top_y) * 0.5
        d = f"M {lt},{top_y} L {lb},{bot_y} L {rb},{bot_y} L {rt},{top_y} Z"
    elif forma == "plate":
        # very shallow
        rim = 15
        d = f"M {lt},{top_y} L {lt+rim},{bot_y} L {rt-rim},{bot_y} L {rt},{top_y} Z"
    elif forma == "vase":
        # hourglass with neck
        neck_y = top_y + (bot_y - top_y) * 0.15
        belly_y = top_y + (bot_y - top_y) * 0.55
        neck_hw = hw_top * 0.7
        belly_hw = max(hw_top, hw_bot) * 1.15
        d = (f"M {cx - hw_top},{top_y} "
             f"C {cx - hw_top},{top_y+5} {cx - neck_hw},{neck_y-5} {cx - neck_hw},{neck_y} "
             f"C {cx - neck_hw},{neck_y+10} {cx - belly_hw},{belly_y-15} {cx - belly_hw},{belly_y} "
             f"C {cx - belly_hw},{belly_y+15} {cx - hw_bot},{bot_y-10} {cx - hw_bot},{bot_y} "
             f"L {cx + hw_bot},{bot_y} "
             f"C {cx + hw_bot},{bot_y-10} {cx + belly_hw},{belly_y+15} {cx + belly_hw},{belly_y} "
             f"C {cx + belly_hw},{belly_y-15} {cx + neck_hw},{neck_y+10} {cx + neck_hw},{neck_y} "
             f"C {cx + neck_hw},{neck_y-5} {cx + hw_top},{top_y+5} {cx + hw_top},{top_y} Z")
    elif forma == "pot":
        # truncated cone with rim
        rim = 8
        d = (f"M {lt-rim},{top_y-3} L {lt},{top_y} L {lb},{bot_y} L {rb},{bot_y} L {rt},{top_y} L {rt+rim},{top_y-3} "
             f"L {rt+rim},{top_y+2} L {rt},{top_y+5} L {rt},{top_y} L {lt},{top_y} L {lt},{top_y+5} L {lt-rim},{top_y+2} Z")
    elif forma == "pitcher":
        # tapered with spout indication
        spout_y = top_y
        d = (f"M {lt},{top_y+8} L {lt},{top_y} C {lt},{top_y-5} {lt-8},{top_y-8} {lt-12},{top_y-5} "
             f"L {lt},{top_y} L {lb},{bot_y} L {rb},{bot_y} L {rt},{top_y} Z")
    elif forma == "jar":
        neck_y = top_y + (bot_y - top_y) * 0.12
        neck_hw = hw_top * 0.8
        d = (f"M {cx - hw_top},{top_y} L {cx - neck_hw},{neck_y} "
             f"C {cx - neck_hw},{neck_y+8} {cx - hw_bot*1.1},{bot_y-20} {cx - hw_bot},{bot_y} "
             f"L {cx + hw_bot},{bot_y} "
             f"C {cx + hw_bot*1.1},{bot_y-20} {cx + neck_hw},{neck_y+8} {cx + neck_hw},{neck_y} "
             f"L {cx + hw_top},{top_y} Z")
    elif forma == "bottle":
        neck_y = top_y + (bot_y - top_y) * 0.35
        neck_hw = hw_top * 0.5
        belly_hw = hw_bot * 1.1
        d = (f"M {cx - neck_hw},{top_y} L {cx - neck_hw},{neck_y} "
             f"C {cx - neck_hw},{neck_y+15} {cx - belly_hw},{neck_y+25} {cx - belly_hw},{neck_y+35} "
             f"L {cx - hw_bot},{bot_y} L {cx + hw_bot},{bot_y} "
             f"L {cx + belly_hw},{neck_y+35} "
             f"C {cx + belly_hw},{neck_y+25} {cx + neck_hw},{neck_y+15} {cx + neck_hw},{neck_y} "
             f"L {cx + neck_hw},{top_y} Z")
    elif forma in ("box", "tray"):
        d = f"M {lt},{top_y} L {lb},{bot_y} L {rb},{bot_y} L {rt},{top_y} Z"
    elif forma == "lid":
        knob_w = 15
        d = (f"M {lt},{bot_y} L {lt},{top_y+10} C {lt},{top_y} {cx-knob_w},{top_y-5} {cx-knob_w},{top_y-10} "
             f"L {cx-knob_w},{top_y-15} L {cx+knob_w},{top_y-15} L {cx+knob_w},{top_y-10} "
             f"C {cx+knob_w},{top_y-5} {rt},{top_y} {rt},{top_y+10} L {rt},{bot_y} Z")
    elif forma == "lamp":
        neck_y = top_y + (bot_y - top_y) * 0.08
        d = (f"M {cx - hw_top},{top_y} L {cx - hw_top*0.9},{neck_y} "
             f"L {cx - hw_bot},{bot_y} L {cx + hw_bot},{bot_y} "
             f"L {cx + hw_top*0.9},{neck_y} L {cx + hw_top},{top_y} Z")
    elif forma == "candle":
        d = f"M {lt},{top_y} C {lt},{bot_y} {lb},{bot_y} {lb},{bot_y} L {rb},{bot_y} C {rb},{bot_y} {rt},{bot_y} {rt},{top_y} Z"
    else:
        d = f"M {lt},{top_y} L {lb},{bot_y} L {rb},{bot_y} L {rt},{top_y} Z"

    return d, top_y, bot_y, lt, rt, lb, rb

def _handle_svg(cx, top_y, bot_y, rt):
    """Optional mug handle."""
    hy1 = top_y + (bot_y - top_y) * 0.2
    hy2 = top_y + (bot_y - top_y) * 0.7
    hx = rt + 20
    return (f'<path d="M {rt},{hy1} C {hx+10},{hy1} {hx+10},{hy2} {rt},{hy2}" '
            f'fill="none" stroke="{INK}" stroke-width="1.5"/>')

def _top_view(cx, cy, wt, forma):
    """Top-view circle/ellipse."""
    r = wt * 0.7 / 2 * 0.5  # smaller for top view
    if forma in ("box", "tray"):
        rw = r
        rh = r * 0.7
        return (f'<rect x="{cx-rw}" y="{cy-rh}" width="{rw*2}" height="{rh*2}" rx="4" '
                f'fill="none" stroke="{INK}" stroke-width="1.2"/>')
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.45}" '
            f'fill="none" stroke="{INK}" stroke-width="1.2"/>')

def _scale_bar(x, y):
    """50mm scale reference bar."""
    bar_w = 50 * 0.7  # same scale as profile
    return (f'<g>'
            f'<line x1="{x}" y1="{y}" x2="{x+bar_w}" y2="{y}" stroke="{INK}" stroke-width="1.5"/>'
            f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" stroke="{INK}" stroke-width="1.5"/>'
            f'<line x1="{x+bar_w}" y1="{y-4}" x2="{x+bar_w}" y2="{y+4}" stroke="{INK}" stroke-width="1.5"/>'
            f'<text x="{x+bar_w/2}" y="{y+14}" text-anchor="middle" font-size="8" fill="{INK_S}" '
            f'font-family="Inter, Arial, sans-serif">50 mm</text>'
            f'</g>')

def generate_svg(nombre, categoria, tecnica, h_mm, wt_mm, wb_mm, forma, numero):
    """Full SVG for one pottery template page."""
    cx = 200
    base_y = 280
    d, top_y, bot_y, lt, rt, lb, rb = _profile_path(h_mm, wt_mm, wb_mm, forma, cx, base_y)
    cat_color = CAT_COLORS.get(categoria, ACCENT)

    parts = []
    parts.append(f'<svg viewBox="0 0 400 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px">')

    # grid background
    parts.append(f'<defs><pattern id="grid{numero}" width="14" height="14" patternUnits="userSpaceOnUse">'
                 f'<path d="M 14 0 L 0 0 0 14" fill="none" stroke="{LINE}" stroke-width="0.4"/>'
                 f'</pattern></defs>')
    parts.append(f'<rect width="400" height="380" fill="url(#grid{numero})"/>')

    # center line
    parts.append(f'<line x1="{cx}" y1="{top_y-15}" x2="{cx}" y2="{bot_y+10}" stroke="{INK_S}" stroke-width="0.5" stroke-dasharray="5,3" opacity="0.4"/>')

    # profile shape
    parts.append(f'<path d="{d}" fill="{PAPER}" stroke="{INK}" stroke-width="1.8"/>')

    # handle for mugs
    if forma == "mug":
        parts.append(_handle_svg(cx, top_y, bot_y, rt))

    # dimension lines
    h_label = f"{h_mm} mm ({_mm_to_in(h_mm)}″)"
    wt_label = f"{wt_mm} mm ({_mm_to_in(wt_mm)}″)"

    # height (right side)
    dim_x = max(rt, rb) + 25
    parts.append(_dim_line(dim_x, top_y, dim_x, bot_y, h_label, "right"))

    # width top (above)
    parts.append(_dim_line(lt, top_y - 18, rt, top_y - 18, wt_label))

    # width bottom if different
    if abs(wt_mm - wb_mm) > 5:
        wb_label = f"{wb_mm} mm ({_mm_to_in(wb_mm)}″)"
        parts.append(_dim_line(lb, bot_y + 15, rb, bot_y + 15, wb_label))

    # top view (small, upper right)
    tv_cx = 340
    tv_cy = 55
    parts.append(f'<text x="{tv_cx}" y="{tv_cy-28}" text-anchor="middle" font-size="8" fill="{INK_S}" font-family="Inter, Arial, sans-serif">VISTA SUPERIOR</text>')
    parts.append(_top_view(tv_cx, tv_cy, wt_mm, forma))

    # scale bar
    parts.append(_scale_bar(20, 360))

    # technique badge
    parts.append(f'<rect x="20" y="15" width="{len(tecnica)*8+16}" height="20" rx="10" fill="{cat_color}" opacity="0.15"/>')
    parts.append(f'<text x="28" y="29" font-size="9" fill="{cat_color}" font-weight="700" font-family="Inter, Arial, sans-serif">{tecnica.upper()}</text>')

    parts.append('</svg>')
    return "\n".join(parts)

# ── Page generation ──

def _shrinkage_note(h, w):
    """Nota de contracción: ~12% estándar."""
    sh = round(h * 0.12)
    sw = round(w * 0.12)
    return f"Contracción estimada (~12%): altura {sh} mm, ancho {sw} mm. Medidas en el dibujo = tamaño final deseado."

def generate_page(item, idx):
    """Generate one A4 page as HTML section."""
    nombre, cat, tec, h, wt, wb, forma = item
    svg = generate_svg(nombre, cat, tec, h, wt, wb, forma, idx)
    cat_color = CAT_COLORS.get(cat, ACCENT)
    shrink = _shrinkage_note(h, wt)

    return f"""<div class="template-page" style="break-before:page">
  <div class="tp-header">
    <div class="tp-number" style="background:{cat_color}">{idx:03d}</div>
    <div class="tp-info">
      <h2 class="tp-name">{nombre}</h2>
      <div class="tp-meta">
        <span class="tp-cat" style="color:{cat_color}">{cat}</span>
        <span class="tp-sep">&middot;</span>
        <span class="tp-tec">{tec}</span>
        <span class="tp-sep">&middot;</span>
        <span class="tp-dims">{h} &times; {wt} mm</span>
      </div>
    </div>
  </div>
  <div class="tp-drawing">{svg}</div>
  <table class="tp-specs">
    <tr><td class="sp-label">Altura</td><td>{h} mm ({_mm_to_in(h)}″)</td></tr>
    <tr><td class="sp-label">Ancho superior</td><td>{wt} mm ({_mm_to_in(wt)}″)</td></tr>
    <tr><td class="sp-label">Ancho inferior</td><td>{wb} mm ({_mm_to_in(wb)}″)</td></tr>
    <tr><td class="sp-label">Técnica</td><td>{tec}</td></tr>
    <tr><td class="sp-label">Categoría</td><td>{cat}</td></tr>
  </table>
  <p class="tp-shrink">{shrink}</p>
</div>"""

def _toc_section(cat, items_in_cat, start_page):
    """TOC entry for a category."""
    count = len(items_in_cat)
    return f'<li><span>{cat} ({count})</span><span>{start_page}</span></li>'

def _category_divider(cat, count, desc):
    """Category divider page."""
    color = CAT_COLORS.get(cat, ACCENT)
    return f"""<div class="section-heading" style="break-before:page;background:linear-gradient(135deg,{ACC_DK},{color})">
  <span class="num">{cat.upper()}</span>
  <h2 style="color:{PAPER}">{cat}</h2>
  <p style="color:{PAPER};opacity:.92">{count} plantillas &middot; {desc}</p>
</div>"""

CAT_DESCRIPTIONS = {
    "Cocina": "Tazones, tazas, platos, jarras, fuentes y utensilios para el uso diario",
    "Hogar": "Decoración, organización, portavelas y accesorios para cada ambiente",
    "Jarrones": "Desde jarrones de mesa hasta piezas de piso, clásicos y contemporáneos",
    "Macetas": "Para interior, exterior, colgantes y de pared, en todos los tamaños",
    "Iluminación": "Lámparas de mesa, colgantes, faroles y portavelas con calado",
}

def generate_html(sample_mode=False):
    """Generate the complete HTML. If sample_mode, only cover + 1 page."""
    items = ITEMS
    if sample_mode:
        items = items[:1]

    # Group by category
    by_cat = {}
    for i, item in enumerate(items):
        cat = item[1]
        by_cat.setdefault(cat, []).append((i, item))

    # Build TOC
    toc_entries = []
    page_num = 3  # after cover + toc
    cat_order = ["Cocina", "Hogar", "Jarrones", "Macetas", "Iluminación"]
    for cat in cat_order:
        if cat in by_cat:
            toc_entries.append(_toc_section(cat, by_cat[cat], page_num))
            page_num += 1 + len(by_cat[cat])  # divider + items

    toc_html = "\n".join(toc_entries)

    # Build pages
    pages = []
    for cat in cat_order:
        if cat not in by_cat:
            continue
        cat_items = by_cat[cat]
        pages.append(_category_divider(cat, len(cat_items), CAT_DESCRIPTIONS.get(cat, "")))
        for seq, (global_idx, item) in enumerate(cat_items, 1):
            pages.append(generate_page(item, global_idx + 1))

    pages_html = "\n".join(pages)
    total = len(items)

    # Technique counts
    tec_counts = {}
    for item in items:
        tec_counts[item[2]] = tec_counts.get(item[2], 0) + 1
    tec_str = " · ".join(f"{t}: {c}" for t, c in sorted(tec_counts.items(), key=lambda x: -x[1]))

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>La Biblioteca Maestra de Cerámica · {total}+ Plantillas Profesionales</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:{BG}; --paper:{PAPER}; --ink:{INK}; --ink-soft:{INK_S};
  --accent:{ACCENT}; --accent-dark:{ACC_DK}; --success:{SUCCESS}; --line:{LINE};
  --f-titulo:'Inter', Georgia, serif; --f-texto:'Inter', -apple-system, Arial, sans-serif;
}}
@page{{size:A4;margin:14mm 15mm 16mm}}
@page :first{{margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{font-family:var(--f-texto);color:var(--ink);background:var(--bg);font-size:10pt;line-height:1.5;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1,h2,h3{{font-family:var(--f-titulo);line-height:1.15}}

/* Cover */
.cover{{height:297mm;width:210mm;background:linear-gradient(155deg,{ACC_DK} 0%,{ACCENT} 60%,#e4893a 100%);
  color:{PAPER};display:flex;flex-direction:column;justify-content:space-between;padding:28mm 22mm;break-after:page;position:relative;overflow:hidden}}
.cover .kicker{{display:inline-block;background:{PAPER};color:{ACC_DK};padding:5pt 14pt;border-radius:99pt;
  font-size:9pt;font-weight:800;letter-spacing:.14em;text-transform:uppercase}}
.cover h1{{color:{PAPER};font-size:42pt;line-height:1.05;margin:18pt 0 14pt}}
.cover .sub{{font-size:13pt;opacity:.92;max-width:140mm;line-height:1.5}}
.cover .stats{{display:flex;gap:24pt;margin-top:20pt}}
.cover .stat{{text-align:center}}
.cover .stat .num{{font-size:28pt;font-weight:900;display:block}}
.cover .stat .lbl{{font-size:9pt;opacity:.8;text-transform:uppercase;letter-spacing:.08em}}
.cover .brand{{font-family:var(--f-titulo);font-size:12pt;font-weight:700;opacity:.85;border-top:1pt solid rgba(255,255,255,.3);padding-top:10pt}}
.cover::after{{content:"";position:absolute;right:-40mm;bottom:40mm;width:140mm;height:140mm;border-radius:50%;
  background:radial-gradient(circle,rgba(255,255,255,.12),transparent 70%)}}

/* TOC */
.toc-page{{break-after:page;padding-top:8mm}}
.toc-page h2{{font-size:26pt;margin:0 0 6pt;color:var(--accent-dark)}}
.toc-page .toc-sub{{color:var(--ink-soft);font-size:10.5pt;margin-bottom:14pt}}
.toc{{list-style:none;margin:0;padding:0}}
.toc li{{display:flex;justify-content:space-between;gap:12pt;padding:10pt 0;border-bottom:1pt dashed var(--line);font-size:11.5pt}}
.toc li span:first-child{{font-weight:700}}
.toc li span:last-child{{color:var(--accent);font-family:var(--f-titulo);font-weight:700}}
.toc-legend{{margin-top:16pt;display:flex;gap:20pt;flex-wrap:wrap}}
.toc-legend .tl{{display:flex;align-items:center;gap:6pt;font-size:9pt}}
.toc-legend .dot{{width:10pt;height:10pt;border-radius:50%}}

/* Section headings */
.section-heading{{border-radius:8pt;padding:22pt 22pt 18pt;margin-bottom:0}}
.section-heading .num{{display:inline-block;background:{PAPER};color:var(--accent-dark);border-radius:99pt;padding:3pt 11pt;
  font-size:8.5pt;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-bottom:8pt}}
.section-heading h2{{margin:0 0 4pt;font-size:23pt}}
.section-heading p{{margin:0}}

/* Template page */
.template-page{{page-break-inside:avoid}}
.tp-header{{display:flex;align-items:flex-start;gap:12pt;margin-bottom:8pt;padding-top:4pt}}
.tp-number{{color:{PAPER};font-size:13pt;font-weight:900;min-width:38pt;height:38pt;border-radius:8pt;
  display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.tp-name{{font-size:16pt;margin:0;color:var(--ink)}}
.tp-meta{{font-size:9pt;color:var(--ink-soft);margin-top:2pt;display:flex;gap:6pt;align-items:center}}
.tp-sep{{opacity:.4}}
.tp-drawing{{display:flex;justify-content:center;margin:4pt 0}}
.tp-specs{{width:100%;border-collapse:collapse;margin:6pt 0;font-size:9.5pt}}
.tp-specs td{{padding:4pt 8pt;border-bottom:1pt solid var(--line)}}
.tp-specs .sp-label{{font-weight:700;color:var(--ink-soft);width:120pt}}
.tp-shrink{{font-size:8pt;color:var(--ink-soft);font-style:italic;margin-top:4pt;padding:4pt 8pt;
  background:var(--paper);border-radius:4pt;border-left:3pt solid var(--accent)}}

/* End page */
.endcover{{break-before:page;min-height:250mm;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20mm}}
.endcover h2{{font-size:28pt;margin-bottom:10pt;color:var(--accent-dark)}}
.endcover .box{{border:2pt solid var(--accent);border-radius:12pt;padding:20pt 24pt;max-width:140mm;background:var(--paper)}}
</style>
</head>
<body>

<!-- PORTADA -->
<div class="cover">
  <div>
    <span class="kicker">Edición Completa</span>
    <h1>La Biblioteca Maestra<br>de Cerámica</h1>
    <p class="sub">{total}+ plantillas profesionales con medidas exactas en milímetros y pulgadas, contracción incorporada y dibujos técnicos listos para imprimir.</p>
    <div class="stats">
      <div class="stat"><span class="num">{total}+</span><span class="lbl">Plantillas</span></div>
      <div class="stat"><span class="num">5</span><span class="lbl">Categorías</span></div>
      <div class="stat"><span class="num">3</span><span class="lbl">Técnicas</span></div>
    </div>
  </div>
  <div class="brand">La Biblioteca Maestra de Cerámica</div>
</div>

<!-- ÍNDICE -->
<div class="toc-page">
  <h2>Contenido</h2>
  <p class="toc-sub">{total} plantillas organizadas en 5 categorías &middot; {tec_str}</p>
  <ul class="toc">{toc_html}</ul>
  <div class="toc-legend">
    <div class="tl"><span class="dot" style="background:{CAT_COLORS['Cocina']}"></span> Cocina</div>
    <div class="tl"><span class="dot" style="background:{CAT_COLORS['Hogar']}"></span> Hogar</div>
    <div class="tl"><span class="dot" style="background:{CAT_COLORS['Jarrones']}"></span> Jarrones</div>
    <div class="tl"><span class="dot" style="background:{CAT_COLORS['Macetas']}"></span> Macetas</div>
    <div class="tl"><span class="dot" style="background:{CAT_COLORS['Iluminación']}"></span> Iluminación</div>
  </div>
</div>

<!-- PLANTILLAS -->
{pages_html}

<!-- CIERRE -->
<div class="endcover">
  <h2>Próximo Paso</h2>
  <div class="box">
    <p style="font-size:12pt;margin-bottom:8pt"><strong>Elige una plantilla, imprímela al 100% y empieza a crear.</strong></p>
    <p style="color:{INK_S}">Cada plantilla incluye las medidas finales con contracción ya calculada. Verifica con la barra de escala de 50 mm antes de cortar.</p>
  </div>
</div>

</body>
</html>"""
    return html

# ── Main ──
if __name__ == "__main__":
    import sys, os
    sample = "--muestra" in sys.argv
    html = generate_html(sample_mode=sample)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "core-plantillas.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    mode = "MUESTRA (portada + 1 página)" if sample else f"COMPLETO ({len(ITEMS)} plantillas)"
    print(f"✓ {out}\n  Modo: {mode}")
