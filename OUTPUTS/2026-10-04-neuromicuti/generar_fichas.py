# -*- coding: utf-8 -*-
"""Genera 105 fichas de actividades printables (HTML+SVG) para NeuroMicuți.

7 categorii × 15 activități = 105 pagini A4.
Ieșire: pdf-sources/fichas-core.html
Apoi: Chrome headless → PDF.

Uso:  python3 generar_fichas.py
"""
import base64
import math
import random
import json
import sys
from pathlib import Path

random.seed(42)
sys.setrecursionlimit(10000)

PROJ = Path(__file__).parent
PALETA = json.loads((PROJ / "oferta.json").read_text("utf-8"))["paleta"]

BG      = PALETA["bg"]
PAPER   = PALETA["paper"]
INK     = PALETA["ink"]
INK_SOFT = PALETA["ink_soft"]
ACCENT  = PALETA["accent"]
ACCENT_DARK = PALETA["accent_dark"]
LINE    = PALETA["line"]

# ─── CATEGORY CONFIG ──────────────────────────────────────
# Each category gets its own visual identity

CAT_COLORS = {
    "concentrare": {"accent": "#3B82F6", "light": "#EFF6FF", "dark": "#1D4ED8", "icon": "🎯"},
    "memorie":     {"accent": "#8B5CF6", "light": "#F5F3FF", "dark": "#6D28D9", "icon": "🧠"},
    "forme":       {"accent": "#14B8A6", "light": "#F0FDFA", "dark": "#0D9488", "icon": "🔷"},
    "logica":      {"accent": "#F59E0B", "light": "#FFFBEB", "dark": "#D97706", "icon": "🔢"},
    "pregrafie":   {"accent": "#22C55E", "light": "#F0FDF4", "dark": "#16A34A", "icon": "✏️"},
    "culori":      {"accent": "#EC4899", "light": "#FDF2F8", "dark": "#DB2777", "icon": "🎨"},
    "coordonare":  {"accent": "#EF4444", "light": "#FEF2F2", "dark": "#DC2626", "icon": "🏹"},
}

CATS = [
    ("Concentrare și atenție", "concentrare"),
    ("Memorie", "memorie"),
    ("Forme și secvențe", "forme"),
    ("Secvențe logice", "logica"),
    ("Pregrafie și motricitate fină", "pregrafie"),
    ("Culori și asocieri", "culori"),
    ("Coordonare ochi-mână", "coordonare"),
]

DIFFICULTY_LABELS = ["Ușor", "Mediu", "Avansat"]

# ─── SVG GENERATORS ────────────────────────────────────────

SVG_W, SVG_H = 500, 340


def svg_maze(w, h, cols, rows):
    """Iterative DFS maze generation."""
    cell = min(w // cols, h // rows)
    mw, mh = cols * cell, rows * cell
    ox, oy = (w - mw) // 2, (h - mh) // 2

    walls_h = [[True] * cols for _ in range(rows + 1)]
    walls_v = [[True] * (cols + 1) for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]

    stack = [(0, 0)]
    visited[0][0] = True
    while stack:
        r, c = stack[-1]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(dirs)
        found = False
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                if dr == 1:  walls_h[r + 1][c] = False
                elif dr == -1: walls_h[r][c] = False
                elif dc == 1:  walls_v[r][c + 1] = False
                elif dc == -1: walls_v[r][c] = False
                stack.append((nr, nc))
                found = True
                break
        if not found:
            stack.pop()

    walls_h[0][0] = False
    walls_h[rows][cols - 1] = False

    lines = []
    for r in range(rows + 1):
        for c in range(cols):
            if walls_h[r][c]:
                x1, y1 = ox + c * cell, oy + r * cell
                lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x1 + cell}" y2="{y1}"/>')
    for r in range(rows):
        for c in range(cols + 1):
            if walls_v[r][c]:
                x1, y1 = ox + c * cell, oy + r * cell
                lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x1}" y2="{y1 + cell}"/>')

    col = CAT_COLORS["concentrare"]["accent"]
    lines.append(f'<circle cx="{ox - 2}" cy="{oy + cell // 2}" r="6" fill="{col}"/>')
    lines.append(f'<text x="{ox - 14}" y="{oy + cell // 2 + 4}" text-anchor="end" font-size="11" font-weight="700" fill="{col}">START</text>')
    lines.append(f'<circle cx="{ox + mw + 2}" cy="{oy + mh - cell // 2}" r="6" fill="#22C55E"/>')
    lines.append(f'<text x="{ox + mw + 14}" y="{oy + mh - cell // 2 + 4}" text-anchor="start" font-size="11" font-weight="700" fill="#22C55E">FINAL</text>')

    return f'<g stroke="{INK}" stroke-width="1.8" fill="none" stroke-linecap="round">{"".join(lines)}</g>'


def svg_find_odd(w, h, num_items, shape_type=None):
    """Grid of shapes where one is different."""
    shapes = ["circle", "square", "triangle", "diamond"]
    shape = shape_type or random.choice(shapes)
    odd_idx = random.randint(0, num_items - 1)
    cols = min(num_items, 5)
    rows_n = (num_items + cols - 1) // cols
    cw = w // (cols + 1)
    ch = h // (rows_n + 1)
    sz = min(cw, ch) // 3

    items = []
    for i in range(num_items):
        r, c = divmod(i, cols)
        cx = cw * (c + 1)
        cy = ch * (r + 1)
        is_odd = i == odd_idx
        fill = ACCENT if not is_odd else "#EF4444"
        stroke = ACCENT_DARK if not is_odd else "#DC2626"

        if shape == "circle":
            rx = sz if not is_odd else int(sz * 0.65)
            items.append(f'<circle cx="{cx}" cy="{cy}" r="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2" opacity=".85"/>')
        elif shape == "square":
            s = sz * 2 if not is_odd else int(sz * 1.3)
            items.append(f'<rect x="{cx - s // 2}" y="{cy - s // 2}" width="{s}" height="{s}" fill="{fill}" stroke="{stroke}" stroke-width="2" rx="4" opacity=".85"/>')
        elif shape == "triangle":
            s = sz if not is_odd else int(sz * 0.6)
            if not is_odd:
                pts = f"{cx},{cy - s} {cx - s},{cy + int(s * 0.7)} {cx + s},{cy + int(s * 0.7)}"
            else:
                pts = f"{cx},{cy + s} {cx - s},{cy - int(s * 0.7)} {cx + s},{cy - int(s * 0.7)}"
            items.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2" opacity=".85"/>')
        elif shape == "diamond":
            s = sz if not is_odd else int(sz * 0.6)
            pts = f"{cx},{cy - s} {cx + s},{cy} {cx},{cy + s} {cx - s},{cy}"
            items.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2" opacity=".85"/>')

    return "".join(items)


def svg_counting(w, h, num_shapes, num_types):
    """Mixed shapes to count — kid writes totals."""
    shape_defs = [
        ("circle", ACCENT, lambda cx, cy, s: f'<circle cx="{cx}" cy="{cy}" r="{s}" fill="{ACCENT}" opacity=".8"/>'),
        ("square", "#F59E0B", lambda cx, cy, s: f'<rect x="{cx-s}" y="{cy-s}" width="{s*2}" height="{s*2}" fill="#F59E0B" rx="3" opacity=".8"/>'),
        ("triangle", "#22C55E", lambda cx, cy, s: f'<polygon points="{cx},{cy-s} {cx-s},{cy+int(s*.7)} {cx+s},{cy+int(s*.7)}" fill="#22C55E" opacity=".8"/>'),
        ("star", "#EC4899", lambda cx, cy, s: _svg_star(cx, cy, s, "#EC4899")),
    ]
    chosen = shape_defs[:num_types]
    assignments = [random.choice(range(num_types)) for _ in range(num_shapes)]
    cols = min(num_shapes, 6)
    rows_n = (num_shapes + cols - 1) // cols
    cw = w // (cols + 1)
    ch = (h - 60) // (rows_n + 1)
    sz = min(cw, ch) // 4

    items = []
    for i in range(num_shapes):
        r, c = divmod(i, cols)
        cx = cw * (c + 1)
        cy = ch * (r + 1)
        t = assignments[i]
        items.append(chosen[t][2](cx, cy, sz))

    # Legend at bottom
    ly = h - 40
    gap = w // (num_types + 1)
    for ti, (name, color, fn) in enumerate(chosen):
        x = gap * (ti + 1)
        items.append(fn(x - 30, ly, sz // 2))
        items.append(f'<text x="{x - 8}" y="{ly + 5}" font-size="13" fill="{INK}">= ___</text>')

    return "".join(items)


def _svg_star(cx, cy, s, fill):
    pts = []
    for j in range(10):
        angle = -math.pi / 2 + j * math.pi / 5
        r2 = s if j % 2 == 0 else s * 0.4
        pts.append(f"{cx + r2 * math.cos(angle):.1f},{cy + r2 * math.sin(angle):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" opacity=".8"/>'


def svg_dot_connect(w, h, num_dots):
    """Connect dots in order to reveal shape."""
    num_dots = min(num_dots, 18)
    cx, cy = w // 2, h // 2
    radius = min(w, h) * 0.38
    dots = []
    for i in range(num_dots):
        angle = -math.pi / 2 + i * 2 * math.pi / num_dots
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14" fill="white" stroke="{ACCENT}" stroke-width="2"/>')
        dots.append(f'<text x="{x:.0f}" y="{y + 5:.0f}" text-anchor="middle" font-size="13" font-weight="700" fill="{INK}">{i + 1}</text>')
    return "".join(dots)


def svg_pattern_sequence(w, h, length):
    """Shape sequence with blanks to fill."""
    shapes = ["●", "■", "▲", "◆", "★"]
    colors = [ACCENT, "#F59E0B", "#22C55E", "#EC4899", "#EF4444"]
    pattern_len = random.randint(2, 3)
    pattern_shapes = random.sample(list(range(len(shapes))), pattern_len)
    seq = (pattern_shapes * ((length + pattern_len) // pattern_len))[:length]
    gap = w // (length + 1)
    items = []
    hide_last = random.randint(2, 3)
    for i, si in enumerate(seq):
        x = gap * (i + 1)
        y = h // 2
        if i >= length - hide_last:
            items.append(f'<rect x="{x - 22}" y="{y - 24}" width="44" height="44" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="5 4" rx="8"/>')
            items.append(f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="20" fill="{INK_SOFT}">?</text>')
        else:
            items.append(f'<rect x="{x - 22}" y="{y - 24}" width="44" height="44" fill="white" stroke="{LINE}" stroke-width="1.5" rx="8"/>')
            items.append(f'<text x="{x}" y="{y + 10}" text-anchor="middle" font-size="28" fill="{colors[si]}">{shapes[si]}</text>')
    return "".join(items)


def svg_tracing(w, h, pattern_type):
    """Dotted path for tracing practice."""
    items = []
    stroke_color = "#B0BEC5"
    guide_color = "#E0E7EE"

    if pattern_type == "zigzag":
        pts = []
        n = 8
        step = w // n
        for i in range(n + 1):
            x = i * step
            y = h * 0.25 if i % 2 == 0 else h * 0.75
            pts.append(f"{x:.0f},{y:.0f}")
        items.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{guide_color}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>')
        items.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{stroke_color}" stroke-width="2.5" stroke-dasharray="6 8" stroke-linecap="round"/>')
    elif pattern_type == "wave":
        d = f"M 10,{h // 2}"
        n = 5
        step = (w - 20) // n
        for i in range(n):
            x1 = 10 + i * step + step // 2
            x2 = 10 + (i + 1) * step
            cy1 = h * 0.15 if i % 2 == 0 else h * 0.85
            d += f" Q {x1},{cy1} {x2},{h // 2}"
        items.append(f'<path d="{d}" fill="none" stroke="{guide_color}" stroke-width="16" stroke-linecap="round"/>')
        items.append(f'<path d="{d}" fill="none" stroke="{stroke_color}" stroke-width="2.5" stroke-dasharray="6 8" stroke-linecap="round"/>')
    elif pattern_type == "spiral":
        pts = []
        for t in range(0, 680, 4):
            angle = math.radians(t)
            r = 8 + t * 0.16
            x = w // 2 + r * math.cos(angle)
            y = h // 2 + r * math.sin(angle)
            pts.append(f"{x:.0f},{y:.0f}")
        items.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{guide_color}" stroke-width="14" stroke-linecap="round"/>')
        items.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{stroke_color}" stroke-width="2.5" stroke-dasharray="6 8" stroke-linecap="round"/>')
    elif pattern_type == "loops":
        d = f"M 10,{h // 2}"
        n = 4
        step = (w - 20) // n
        for i in range(n):
            cx = 10 + i * step + step // 2
            d += f" C {cx},{h * 0.05} {cx + step // 3},{h * 0.05} {10 + (i + 1) * step},{h // 2}"
        items.append(f'<path d="{d}" fill="none" stroke="{guide_color}" stroke-width="14" stroke-linecap="round"/>')
        items.append(f'<path d="{d}" fill="none" stroke="{stroke_color}" stroke-width="2.5" stroke-dasharray="6 8" stroke-linecap="round"/>')
    else:
        for i in range(5):
            y = h * (i + 1) // 6
            items.append(f'<line x1="20" y1="{y}" x2="{w - 20}" y2="{y}" stroke="{guide_color}" stroke-width="12" stroke-linecap="round"/>')
            items.append(f'<line x1="20" y1="{y}" x2="{w - 20}" y2="{y}" stroke="{stroke_color}" stroke-width="2" stroke-dasharray="6 8" stroke-linecap="round"/>')

    items.append(f'<circle cx="14" cy="{h // 2}" r="8" fill="{ACCENT}" stroke="white" stroke-width="2"/>')
    items.append(f'<circle cx="{w - 14}" cy="{h // 2}" r="8" fill="#22C55E" stroke="white" stroke-width="2"/>')
    return "".join(items)


def svg_memory_grid(w, h, grid_size):
    """Memory pair-matching grid."""
    cell = min(w // (grid_size + 1), h // (grid_size + 1))
    ox = (w - grid_size * cell) // 2
    oy = (h - grid_size * cell) // 2
    emojis = ["🍎", "🌟", "🐱", "🎈", "🌸", "🦋", "🐟", "🎵", "🌈", "☀️", "🍀", "❤️", "🎯", "🔔", "🌙"]
    need = (grid_size * grid_size + 1) // 2
    chosen = random.sample(emojis, min(need, len(emojis)))
    pairs = (chosen * 2)[:grid_size * grid_size]
    random.shuffle(pairs)

    items = []
    for r in range(grid_size):
        for c in range(grid_size):
            x, y = ox + c * cell, oy + r * cell
            items.append(f'<rect x="{x + 3}" y="{y + 3}" width="{cell - 6}" height="{cell - 6}" fill="white" stroke="{ACCENT}" stroke-width="1.5" rx="8"/>')
            items.append(f'<text x="{x + cell // 2}" y="{y + cell // 2 + 8}" text-anchor="middle" font-size="{cell // 3}">{pairs[r * grid_size + c]}</text>')
    return "".join(items)


def svg_number_sequence(w, h, length, rule_type):
    """Number sequence with missing values."""
    if rule_type == "add":
        step = random.randint(2, 5)
        start = random.randint(1, 10)
        seq = [start + i * step for i in range(length)]
    elif rule_type == "multiply":
        base = random.randint(2, 3)
        seq = [base ** i for i in range(1, length + 1)]
    elif rule_type == "subtract":
        start = random.randint(50, 80)
        step = random.randint(3, 7)
        seq = [start - i * step for i in range(length)]
    else:
        fib = [1, 1]
        while len(fib) < length:
            fib.append(fib[-1] + fib[-2])
        seq = fib[:length]

    gap = w // (length + 1)
    items = []
    hide = sorted(random.sample(range(1, length), min(2, length - 1)))
    for i, n in enumerate(seq):
        x = gap * (i + 1)
        y = h // 2
        if i in hide:
            items.append(f'<rect x="{x - 24}" y="{y - 24}" width="48" height="48" fill="white" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="5 4" rx="10"/>')
            items.append(f'<text x="{x}" y="{y + 7}" text-anchor="middle" font-size="22" font-weight="700" fill="{INK_SOFT}">?</text>')
        else:
            items.append(f'<rect x="{x - 24}" y="{y - 24}" width="48" height="48" fill="white" stroke="{LINE}" stroke-width="1.5" rx="10"/>')
            items.append(f'<text x="{x}" y="{y + 8}" text-anchor="middle" font-size="20" font-weight="700" fill="{INK}">{n}</text>')
        if i < length - 1:
            items.append(f'<text x="{x + gap // 2}" y="{y + 6}" text-anchor="middle" font-size="18" fill="{INK_SOFT}">→</text>')
    return "".join(items)


def svg_color_match(w, h, num_pairs):
    """Match color names to colored circles with lines."""
    colors_named = [
        ("roșu", "#EF4444"), ("albastru", "#3B82F6"), ("verde", "#22C55E"),
        ("galben", "#EAB308"), ("portocaliu", "#F97316"), ("violet", "#8B5CF6"),
        ("roz", "#EC4899"), ("maro", "#92400E"),
    ]
    chosen = random.sample(colors_named, num_pairs)
    items = []
    left_y = h // (num_pairs + 1)
    right = list(range(num_pairs))
    random.shuffle(right)
    for i, (name, color) in enumerate(chosen):
        ly = left_y * (i + 1)
        items.append(f'<rect x="20" y="{ly - 16}" width="110" height="32" fill="{color}" rx="16"/>')
        items.append(f'<text x="75" y="{ly + 5}" text-anchor="middle" font-size="12" font-weight="700" fill="white">{name.upper()}</text>')
        items.append(f'<circle cx="148" cy="{ly}" r="4" fill="{INK}"/>')
        ri = right[i]
        ry = left_y * (ri + 1)
        items.append(f'<circle cx="{w - 60}" cy="{ry}" r="22" fill="{chosen[ri][1]}" stroke="white" stroke-width="3"/>')
        items.append(f'<circle cx="{w - 60}" cy="{ry}" r="22" fill="none" stroke="{INK}" stroke-width="1.2"/>')
        items.append(f'<circle cx="{w - 90}" cy="{ry}" r="4" fill="{INK}"/>')
    return "".join(items)


def svg_eye_hand_path(w, h, path_width):
    """Winding path to trace between borders."""
    items = []
    pts_upper = []
    pts_lower = []
    n = 14
    for i in range(n + 1):
        x = w * i / n
        base_y = h / 2 + math.sin(i * 0.7) * h * 0.28 + math.cos(i * 1.4) * h * 0.12
        pts_upper.append(f"{x:.0f},{base_y - path_width:.0f}")
        pts_lower.append(f"{x:.0f},{base_y + path_width:.0f}")
    items.append(f'<polyline points="{" ".join(pts_upper)}" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round"/>')
    items.append(f'<polyline points="{" ".join(pts_lower)}" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round"/>')
    center_y_start = h / 2 + math.sin(0) * h * 0.28 + math.cos(0) * h * 0.12
    center_y_end = h / 2 + math.sin(n * 0.7) * h * 0.28 + math.cos(n * 1.4) * h * 0.12
    items.append(f'<circle cx="6" cy="{center_y_start:.0f}" r="8" fill="{ACCENT}" stroke="white" stroke-width="2"/>')
    items.append(f'<circle cx="{w - 6}" cy="{center_y_end:.0f}" r="8" fill="#22C55E" stroke="white" stroke-width="2"/>')
    return "".join(items)


def svg_shadow_match(w, h, num_items):
    """Match objects to their silhouettes."""
    shape_fns = [
        lambda cx, cy, s, filled: f'<circle cx="{cx}" cy="{cy}" r="{s}" fill="{filled}" stroke="{INK if filled != "#333" else "none"}" stroke-width="1.5"/>',
        lambda cx, cy, s, filled: f'<rect x="{cx - s}" y="{cy - s}" width="{s * 2}" height="{s * 2}" fill="{filled}" stroke="{INK if filled != "#333" else "none"}" stroke-width="1.5" rx="4"/>',
        lambda cx, cy, s, filled: f'<polygon points="{cx},{cy - s} {cx - s},{cy + int(s * .7)} {cx + s},{cy + int(s * .7)}" fill="{filled}" stroke="{INK if filled != "#333" else "none"}" stroke-width="1.5"/>',
        lambda cx, cy, s, filled: _svg_star(cx, cy, s, filled),
    ]
    chosen_fns = random.sample(shape_fns, min(num_items, len(shape_fns)))
    colors = ["#3B82F6", "#F59E0B", "#22C55E", "#EC4899"]

    items = []
    right_order = list(range(num_items))
    random.shuffle(right_order)

    row_h = h // (num_items + 1)
    sz = min(row_h // 3, 24)
    for i in range(num_items):
        ly = row_h * (i + 1)
        items.append(chosen_fns[i](80, ly, sz, colors[i]))
        items.append(f'<circle cx="130" cy="{ly}" r="4" fill="{INK}"/>')
        ri = right_order[i]
        ry = row_h * (ri + 1)
        items.append(chosen_fns[ri](w - 80, ry, sz, "#CBD5E1"))
        items.append(f'<circle cx="{w - 130}" cy="{ry}" r="4" fill="{INK}"/>')

    items.append(f'<text x="80" y="{h - 8}" text-anchor="middle" font-size="10" fill="{INK_SOFT}">Obiect</text>')
    items.append(f'<text x="{w - 80}" y="{h - 8}" text-anchor="middle" font-size="10" fill="{INK_SOFT}">Umbra</text>')
    return "".join(items)


# ─── ACTIVITY DEFINITIONS ──────────────────────────────────

def _difficulty(idx):
    if idx < 5: return 0
    if idx < 10: return 1
    return 2

def _age(idx):
    ages = ["3-5 ani", "3-5 ani", "4-6 ani", "4-7 ani", "5-7 ani",
            "5-8 ani", "6-8 ani", "6-9 ani", "7-10 ani", "7-10 ani",
            "8-11 ani", "8-12 ani", "9-12 ani", "10-13 ani", "10-14 ani"]
    return ages[idx]


def gen_concentrare(idx):
    d = _difficulty(idx)
    activities = [
        ("Găsește elementul diferit", "Privește cu atenție toate formele. Una dintre ele este diferită. Încercuiește-o cu creionul.",
         lambda: svg_find_odd(SVG_W, SVG_H, 8, "circle")),
        ("Numără formele", "Câte forme de fiecare tip vezi? Numără cu atenție și scrie totalul lângă fiecare formă.",
         lambda: svg_counting(SVG_W, SVG_H, 12, 3)),
        ("Atenție la detalii", "Între toate formele, una este diferită ca mărime. Găsește-o și încercuiește-o.",
         lambda: svg_find_odd(SVG_W, SVG_H, 10, "square")),
        ("Drumul prin labirint", "Trasează cu creionul calea de la START la FINAL. Nu trece prin pereți.",
         lambda: svg_maze(SVG_W, SVG_H, 8, 6)),
        ("Unește numerele", "Unește numerele în ordine crescătoare (1, 2, 3...) trasând o linie continuă.",
         lambda: svg_dot_connect(SVG_W, SVG_H, 10)),
        ("Triunghiul ascuns", "Unul dintre triunghiuri stă cu vârful în jos. Găsește-l și colorează-l.",
         lambda: svg_find_odd(SVG_W, SVG_H, 10, "triangle")),
        ("Câte sunt?", "Numără fiecare tip de formă și scrie totalul. Verifică de două ori!",
         lambda: svg_counting(SVG_W, SVG_H, 16, 4)),
        ("Labirintul castelului", "Găsește drumul prin labirint. Ai un singur drum corect.",
         lambda: svg_maze(SVG_W, SVG_H, 10, 8)),
        ("Conectează punctele", "Unește numerele în ordine. Ce formă apare la final?",
         lambda: svg_dot_connect(SVG_W, SVG_H, 12)),
        ("Diamantul diferit", "Unul dintre diamante nu seamănă cu celelalte. Încercuiește-l.",
         lambda: svg_find_odd(SVG_W, SVG_H, 12, "diamond")),
        ("Numără și compară", "Câte forme de fiecare tip sunt? Care tip are cele mai multe?",
         lambda: svg_counting(SVG_W, SVG_H, 20, 4)),
        ("Labirintul pierdut", "Acest labirint este mai complex. Concentrează-te și găsește ieșirea.",
         lambda: svg_maze(SVG_W, SVG_H, 12, 10)),
        ("Steaua ascunsă", "Între toate stelele, una este mai mică. Găsește-o și încercuiește-o.",
         lambda: svg_find_odd(SVG_W, SVG_H, 15, "circle")),
        ("Marea numărătoare", "Numără fiecare tip de formă. Scrie totalul și verifică suma.",
         lambda: svg_counting(SVG_W, SVG_H, 24, 4)),
        ("Labirintul campionilor", "Cel mai dificil labirint! Găsește singura cale de la START la FINAL.",
         lambda: svg_maze(SVG_W, SVG_H, 14, 12)),
    ]
    title, instr, gen_fn = activities[idx]
    return title, instr, gen_fn()


def gen_memorie(idx):
    sizes = [3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    sz = sizes[idx]
    titles = [
        "Memorează perechile", "Jocul memoriei", "Grila perechilor",
        "Unde sunt perechile?", "Memoria vizuală",
        "Recunoaște perechile", "Amintește-ți poziția", "Perechi ascunse",
        "Grila secretă", "Memoria campionilor",
        "Provocare de memorie", "Perechile invizibile", "Amintește și potrivește",
        "Grila avansată", "Memorie de elită",
    ]
    durations = ["20", "20", "25", "25", "30", "30", "30", "35", "35", "40", "40", "45", "45", "50", "50"]
    return (titles[idx],
            f"Privește grila cu atenție timp de {durations[idx]} de secunde. Apoi acoperă pagina și încearcă să scrii din memorie unde se află fiecare pereche.",
            svg_memory_grid(SVG_W, SVG_H, sz))


def gen_forme(idx):
    lengths = [5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 10, 10]
    titles = [
        "Continuă secvența", "Ce formă urmează?", "Completează tiparul",
        "Regula formelor", "Șirul magic",
        "Descoperă ordinea", "Formele ascunse", "Secvența secretă",
        "Tiparul invizibil", "Ce lipsește?",
        "Secvența avansată", "Provocare de forme", "Ordinea perfectă",
        "Tiparul campionilor", "Secvența de elită",
    ]
    instructions = [
        "Privește secvența de forme. Ce formă vine după ultimele elemente? Desenează-o în spațiul gol.",
        "Observă cum se repetă formele. Completează spațiile goale cu forma corectă.",
        "Formele urmează o regulă. Găsește regula și completează ce lipsește.",
    ]
    return (titles[idx], instructions[idx % len(instructions)],
            svg_pattern_sequence(SVG_W, 160, lengths[idx]))


def gen_logica(idx):
    rules = ["add", "add", "add", "subtract", "subtract",
             "add", "multiply", "subtract", "add", "multiply",
             "fibonacci", "multiply", "subtract", "fibonacci", "multiply"]
    lengths = [5, 5, 6, 5, 6, 6, 5, 6, 7, 6, 6, 7, 7, 7, 8]
    titles = [
        "Găsește regula", "Ce număr urmează?", "Completează seria",
        "Numere descrescătoare", "Seria inversă",
        "Regula ascunsă", "Numere care cresc", "Scade mereu",
        "Seria numerelor", "Puterea numerelor",
        "Secvența lui Fibonacci", "Multiplicarea", "Provocarea inversă",
        "Tiparul matematic", "Seria campionilor",
    ]
    instructions = [
        "Privește numerele. Ce regulă urmează? Completează locurile goale.",
        "Numerele urmează un tipar. Calculează ce trebuie în locul semnului de întrebare.",
        "Analizează cum se schimbă numerele. Scrie numerele lipsă.",
    ]
    return (titles[idx], instructions[idx % len(instructions)],
            svg_number_sequence(SVG_W, 160, lengths[idx], rules[idx]))


def gen_pregrafie(idx):
    patterns = ["zigzag", "wave", "spiral", "loops", "lines",
                "zigzag", "wave", "spiral", "loops", "zigzag",
                "wave", "spiral", "loops", "zigzag", "wave"]
    titles = [
        "Trasează zigzagul", "Urmărește valul", "Spirala magică",
        "Buclele vesele", "Linii drepte",
        "Zigzag rapid", "Valul oceanului", "Spirala melcului",
        "Bucle dansatoare", "Zigzag precis",
        "Valuri mari", "Spirala galaxiei", "Bucle perfecte",
        "Zigzag campion", "Valul final",
    ]
    return (titles[idx],
            "Urmărește linia punctată cu creionul, fără să ridici mâna de pe hârtie. Încearcă să rămâi cât mai aproape de linie.",
            svg_tracing(SVG_W, SVG_H, patterns[idx]))


def gen_culori(idx):
    num_pairs = [4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8]
    titles = [
        "Unește culorile", "Numele culorii", "Perechi de culori",
        "Potrivește culoarea", "Cuvânt și culoare",
        "Culorile potrivite", "Cine e cine?", "Legăturile culorilor",
        "Culorile ascunse", "Unde e culoarea?",
        "Provocare colorată", "Potriviri rapide", "Culorile campionilor",
        "Maestrul culorilor", "Culorile de elită",
    ]
    instructions = [
        "Trage o linie de la fiecare cuvânt (stânga) la cercul de culoarea potrivită (dreapta).",
        "Citește cu atenție numele fiecărei culori. Unește-l cu cercul care i se potrivește.",
        "Privește cercurile colorate din dreapta. Trasează o linie la numele potrivit din stânga.",
    ]
    return (titles[idx], instructions[idx % len(instructions)],
            svg_color_match(SVG_W, SVG_H, num_pairs[idx]))


def gen_coordonare(idx):
    path_widths = [28, 26, 26, 24, 24, 22, 22, 20, 20, 18, 18, 16, 16, 14, 14]
    if idx % 3 == 0:
        maze_sizes = [(8, 6), (10, 8), (10, 8), (12, 10), (12, 10)]
        mi = idx // 3
        cols, rows = maze_sizes[min(mi, len(maze_sizes) - 1)]
        titles = ["Labirintul simplu", "Labirintul grădinii", "Labirintul castelului",
                  "Labirintul muntelui", "Labirintul campionilor"]
        return (titles[min(mi, len(titles) - 1)],
                "Trasează cu creionul drumul de la START la FINAL. Nu trece prin pereți.",
                svg_maze(SVG_W, SVG_H, cols, rows))
    elif idx % 3 == 1:
        num_dots = min(10 + idx, 16)
        titles = ["Unește punctele", "Descoperă forma", "Conectează numerele",
                  "Desenul ascuns", "Forma misterioasă"]
        mi = idx // 3
        return (titles[min(mi, len(titles) - 1)],
                "Unește numerele în ordine (1, 2, 3...) cu linii drepte. Ce formă apare?",
                svg_dot_connect(SVG_W, SVG_H, num_dots))
    else:
        titles = ["Drumul sinuos", "Cărarea îngustă", "Traseul precis",
                  "Drumul provocator", "Traseul de elită"]
        mi = idx // 3
        return (titles[min(mi, len(titles) - 1)],
                "Trasează cu creionul prin mijlocul drumului, fără să atingi marginile.",
                svg_eye_hand_path(SVG_W, SVG_H, path_widths[idx]))


GENERATORS = [gen_concentrare, gen_memorie, gen_forme, gen_logica,
              gen_pregrafie, gen_culori, gen_coordonare]

# ─── PAGE BUILDERS ─────────────────────────────────────────

def build_page(cat_name, cat_tag, act_num, global_num, title, instruction, svg_content, age, difficulty):
    cc = CAT_COLORS[cat_tag]
    stars = "★" * (difficulty + 1) + "☆" * (2 - difficulty)
    diff_label = DIFFICULTY_LABELS[difficulty]

    has_answer = cat_tag in ("forme", "logica", "memorie", "concentrare", "culori")
    answer_html = ""
    if has_answer and cat_tag in ("logica", "forme"):
        answer_html = f"""<div class="answer-area">
    <span class="answer-label">Răspunsul tău:</span>
    <div class="answer-lines"><span class="dotline"></span><span class="dotline"></span></div>
  </div>"""
    elif has_answer and cat_tag == "memorie":
        answer_html = f"""<div class="answer-area">
    <span class="answer-label">Perechile găsite:</span>
    <div class="answer-lines"><span class="dotline"></span><span class="dotline"></span><span class="dotline"></span></div>
  </div>"""

    svg_h = 160 if cat_tag in ("forme", "logica") else SVG_H

    return f"""<div class="page act-page" data-cat="{cat_tag}">
  <div class="cat-ribbon" style="background:{cc['accent']}"></div>
  <div class="page-inner">
    <div class="page-header">
      <div class="header-left">
        <span class="cat-icon">{cc['icon']}</span>
        <span class="cat-badge" style="background:{cc['accent']}">{cat_name}</span>
      </div>
      <div class="header-right">
        <span class="diff-stars" title="{diff_label}">{stars}</span>
        <span class="age-badge" style="border-color:{cc['accent']};color:{cc['dark']}">{age}</span>
      </div>
    </div>
    <h2 class="act-title">{title}</h2>
    <div class="instruction-box" style="background:{cc['light']};border-left-color:{cc['accent']}">
      <p class="act-instruction">{instruction}</p>
    </div>
    <div class="act-area">
      <svg viewBox="0 0 {SVG_W} {svg_h}" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
        {svg_content}
      </svg>
    </div>
    {answer_html}
    <div class="page-footer">
      <span class="brand-small">NeuroMicuți · Sistemul Focus</span>
      <span class="page-num">{global_num}</span>
    </div>
  </div>
</div>"""


def build_cover():
    img_path = PROJ / "img" / "ro" / "g1-tapa.png"
    b64 = base64.b64encode(img_path.read_bytes()).decode()
    return f"""<div class="page cover-page">
  <img src="data:image/png;base64,{b64}" alt="NeuroMicuți · Sistemul Focus" class="cover-img">
</div>"""


def build_guide():
    return f"""<div class="page guide-page">
  <div class="guide-inner">
    <h2 class="guide-title">Ghidul Părintelui</h2>
    <p class="guide-sub">Cum să folosești NeuroMicuți pentru rezultate vizibile</p>

    <div class="guide-section">
      <h3>🎯 Ce este NeuroMicuți?</h3>
      <p>NeuroMicuți este un program de <strong>105 activități printabile</strong> organizate în 7 categorii cognitive. Fiecare activitate este gândită să antreneze concentrarea, memoria, logica și motricitatea fină a copilului tău — fără ecrane, fără pregătire specială.</p>
    </div>

    <div class="guide-section">
      <h3>⏱️ Rutina de 10 minute</h3>
      <p>Nu ai nevoie de mai mult. Așa funcționează:</p>
      <ol class="guide-steps">
        <li><strong>Alege o activitate</strong> potrivită vârstei copilului (vezi simbolul din colțul paginii)</li>
        <li><strong>Citește instrucțiunea</strong> împreună cu copilul</li>
        <li><strong>Lasă-l să lucreze singur</strong> — intervino doar dacă cere ajutor</li>
        <li><strong>Verificați împreună</strong> și bifează activitatea în registrul de progres</li>
      </ol>
    </div>

    <div class="guide-grid">
      <div class="guide-card">
        <h4>★☆☆ Ușor</h4>
        <p>Activitățile 1-5 din fiecare categorie. Perfecte pentru începători și copiii de 3-5 ani.</p>
      </div>
      <div class="guide-card">
        <h4>★★☆ Mediu</h4>
        <p>Activitățile 6-10. Necesită mai multă concentrare. Recomandate de la 5-8 ani.</p>
      </div>
      <div class="guide-card">
        <h4>★★★ Avansat</h4>
        <p>Activitățile 11-15. Provocări care dezvoltă perseverența. Pentru 8-14 ani.</p>
      </div>
    </div>

    <div class="guide-section">
      <h3>💡 Sfaturi pentru rezultate mai bune</h3>
      <ul class="guide-tips">
        <li>Fă din asta un <strong>ritual zilnic</strong> — același moment al zilei, în fiecare zi</li>
        <li>Nu corecta imediat — lasă copilul să descopere singur greșelile</li>
        <li>Laudă <strong>efortul</strong>, nu doar rezultatul: „Bravo că ai încercat!"</li>
        <li>Dacă o activitate e prea grea, treci la alta și revino mai târziu</li>
        <li>Poți printa aceeași activitate de câte ori vrei — repetiția consolidează</li>
      </ul>
    </div>

    <div class="guide-footer-note">
      <p>📚 <strong>Cele 7 categorii cognitive:</strong> Concentrare și atenție · Memorie · Forme și secvențe · Secvențe logice · Pregrafie · Culori și asocieri · Coordonare ochi-mână</p>
    </div>
  </div>
</div>"""


def build_progress_tracker(activities):
    items = []
    current_cat = ""
    for a in activities:
        if a["cat_name"] != current_cat:
            current_cat = a["cat_name"]
            cc = CAT_COLORS[a["cat_tag"]]
            items.append(f'<div class="prog-cat-header">{cc["icon"]} {current_cat}</div>')
        items.append(f'<div class="prog-row"><span class="prog-check">☐</span><span class="prog-num">{a["global_num"]}</span> {a["title"]}</div>')

    return f"""<div class="page progress-page">
  <h2 class="progress-title">Registru de Progres</h2>
  <p class="progress-sub">Bifează (✓) fiecare activitate terminată. Obiectiv: completează toate cele 105!</p>
  <div class="progress-grid">{"".join(items)}</div>
  <div class="progress-summary">
    <span>Total completate: _____ / 105</span>
    <span>Numele copilului: _________________________</span>
  </div>
</div>"""


def build_answer_key(activities):
    items = []
    for a in activities:
        tag = a["cat_tag"]
        if tag == "logica":
            items.append(f'<div class="ans-item"><span class="ans-num">{a["global_num"]}</span> <strong>{a["title"]}</strong>: Regula — {a.get("answer", "vezi secvența")}</div>')
        elif tag == "forme":
            items.append(f'<div class="ans-item"><span class="ans-num">{a["global_num"]}</span> <strong>{a["title"]}</strong>: Tiparul se repetă — completează cu formele lipsă</div>')

    return f"""<div class="page answers-page">
  <h2 class="answers-title">Indicii și Răspunsuri</h2>
  <p class="answers-sub">Folosește această pagină doar după ce copilul a încercat singur.</p>
  <div class="answers-grid">{"".join(items)}</div>
  <div class="answers-note">
    <p><strong>Notă:</strong> Pentru labirinturi, trasări și activitățile de memorie nu există un singur răspuns corect — important este procesul, nu rezultatul final. Laudă efortul!</p>
  </div>
</div>"""


def build_certificate():
    return f"""<div class="page cert-page">
  <div class="cert-box">
    <div class="cert-badge">🏆</div>
    <h2 class="cert-title">Certificat de Excelență</h2>
    <p class="cert-sub">Acest certificat se acordă lui/ei</p>
    <div class="cert-name-line"></div>
    <p class="cert-reason">pentru completarea cu succes a activităților<br><strong>NeuroMicuți · Sistemul Focus</strong></p>
    <div class="cert-details">
      <div class="cert-detail">
        <span class="cert-label">Activități completate</span>
        <span class="cert-value">_____ / 105</span>
      </div>
      <div class="cert-detail">
        <span class="cert-label">Data</span>
        <span class="cert-value">____ / ____ / ________</span>
      </div>
    </div>
    <p class="cert-closing">Felicitări! Ai demonstrat concentrare, răbdare și perseverență.</p>
    <p class="cert-brand">NeuroMicuți · Sistemul Focus</p>
  </div>
</div>"""


def build_toc(activities):
    rows = []
    current_cat = ""
    for a in activities:
        if a["cat_name"] != current_cat:
            current_cat = a["cat_name"]
            cc = CAT_COLORS[a["cat_tag"]]
            rows.append(f'<tr class="toc-cat"><td colspan="3"><span class="toc-cat-icon">{cc["icon"]}</span> {current_cat}</td></tr>')
        rows.append(f'<tr><td class="toc-num">{a["global_num"]}</td><td class="toc-act-name">{a["title"]}</td><td class="toc-pg">{a["global_num"] + 4}</td></tr>')

    return f"""<div class="page toc-wrap">
  <h2 class="toc-heading">Cuprins</h2>
  <p class="toc-sub">105 activități · 7 categorii cognitive · Vârsta 3-14 ani</p>
  <table class="toc-table">{"".join(rows)}</table>
</div>"""


def build_cat_divider(cat_name, cat_tag, cat_idx, count):
    cc = CAT_COLORS[cat_tag]
    descs = [
        "Activități care antrenează focusul vizual și capacitatea de a observa detalii fine.",
        "Exerciții care dezvoltă memoria de lucru și capacitatea de recunoaștere a tiparelor.",
        "Secvențe de forme și culori care antrenează gândirea abstractă și recunoașterea tiparelor.",
        "Serii de numere și ordini logice care dezvoltă raționamentul matematic.",
        "Trasări și desene care pregătesc musculatura fină a mâinii pentru scris.",
        "Exerciții de asociere vizuală și clasificare pe baza culorilor și a numelor lor.",
        "Labirinturi și trasee care antrenează precizia mișcărilor și coordonarea vizuală.",
    ]
    return f"""<div class="page cat-divider-page">
  <div class="cat-divider-box" style="background: linear-gradient(135deg, {cc['accent']}, {cc['dark']})">
    <span class="cat-divider-icon">{cc['icon']}</span>
    <span class="cat-divider-num">Categoria {cat_idx + 1} din 7</span>
    <h2 class="cat-divider-title">{cat_name}</h2>
    <p class="cat-divider-desc">{descs[cat_idx]}</p>
    <div class="cat-divider-meta">
      <span class="cat-divider-count">{count} activități</span>
      <span class="cat-divider-dot">·</span>
      <span class="cat-divider-levels">3 niveluri de dificultate</span>
    </div>
  </div>
</div>"""


# ─── CSS ───────────────────────────────────────────────────

CSS = f"""
:root {{
  --bg: {BG}; --paper: {PAPER}; --ink: {INK}; --ink-soft: {INK_SOFT};
  --accent: {ACCENT}; --accent-dark: {ACCENT_DARK}; --line: {LINE};
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Poppins', 'Segoe UI', sans-serif; color: var(--ink); background: white; }}
@page {{ size: A4 portrait; margin: 14mm 12mm 14mm 12mm; }}

.page {{
  page-break-after: always;
  width: 100%;
  min-height: 90vh;
  position: relative;
  overflow: hidden;
}}
.page:last-child {{ page-break-after: avoid; }}

/* ── COVER ── */
.cover-page {{
  display: flex;
  justify-content: center;
  align-items: center;
  background: white;
  min-height: 100vh;
  padding: 8pt;
}}
.cover-img {{
  max-width: 185mm;
  max-height: 272mm;
  object-fit: contain;
  border-radius: 10pt;
  box-shadow: 0 6pt 32pt rgba(0,0,0,.12);
}}

/* ── TOC ── */
.toc-wrap {{
  padding: 30pt 20pt 20pt;
}}
.toc-heading {{
  font-size: 26pt;
  font-weight: 800;
  color: var(--accent-dark);
  margin-bottom: 4pt;
}}
.toc-sub {{
  font-size: 10pt;
  color: var(--ink-soft);
  margin-bottom: 18pt;
  padding-bottom: 10pt;
  border-bottom: 2pt solid var(--accent);
}}
.toc-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
}}
.toc-table td {{
  padding: 2.5pt 4pt;
}}
.toc-cat td {{
  font-weight: 800;
  color: var(--accent-dark);
  padding-top: 10pt;
  padding-bottom: 4pt;
  font-size: 10pt;
  border-bottom: 1.5pt solid var(--line);
}}
.toc-cat-icon {{
  font-size: 12pt;
  margin-right: 4pt;
}}
.toc-num {{
  width: 24pt;
  color: var(--ink-soft);
  font-weight: 600;
}}
.toc-act-name {{
  color: var(--ink);
}}
.toc-pg {{
  width: 26pt;
  text-align: right;
  color: var(--ink-soft);
  font-weight: 500;
}}

/* ── CATEGORY DIVIDER ── */
.cat-divider-page {{
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 92vh;
  padding: 30pt;
}}
.cat-divider-box {{
  width: 100%;
  max-width: 440pt;
  border-radius: 20pt;
  padding: 50pt 40pt;
  text-align: center;
  color: white;
  box-shadow: 0 8pt 40pt rgba(0,0,0,.1);
}}
.cat-divider-icon {{
  font-size: 48pt;
  display: block;
  margin-bottom: 12pt;
}}
.cat-divider-num {{
  font-size: 10pt;
  text-transform: uppercase;
  letter-spacing: .14em;
  opacity: .8;
  font-weight: 600;
}}
.cat-divider-title {{
  font-size: 30pt;
  font-weight: 800;
  color: white;
  margin: 8pt 0 12pt;
  line-height: 1.15;
}}
.cat-divider-desc {{
  font-size: 11pt;
  opacity: .88;
  line-height: 1.6;
  max-width: 340pt;
  margin: 0 auto 18pt;
}}
.cat-divider-meta {{
  font-size: 12pt;
  font-weight: 700;
  opacity: .9;
}}
.cat-divider-dot {{
  margin: 0 6pt;
  opacity: .5;
}}
.cat-divider-levels {{
  font-weight: 500;
  opacity: .75;
}}

/* ── ACTIVITY PAGE ── */
.act-page {{
  padding: 0;
  position: relative;
}}
.cat-ribbon {{
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 5pt;
  border-radius: 0 3pt 3pt 0;
}}
.page-inner {{
  padding: 16pt 18pt 12pt 22pt;
  min-height: 88vh;
  display: flex;
  flex-direction: column;
}}
.page-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8pt;
  padding-bottom: 6pt;
}}
.header-left {{
  display: flex;
  align-items: center;
  gap: 6pt;
}}
.cat-icon {{
  font-size: 14pt;
}}
.cat-badge {{
  font-size: 7.5pt;
  text-transform: uppercase;
  letter-spacing: .1em;
  font-weight: 700;
  color: white;
  padding: 3pt 10pt;
  border-radius: 99pt;
}}
.header-right {{
  display: flex;
  align-items: center;
  gap: 8pt;
}}
.diff-stars {{
  font-size: 10pt;
  color: #F59E0B;
  letter-spacing: 1pt;
}}
.age-badge {{
  font-size: 7.5pt;
  font-weight: 700;
  border: 1.5pt solid;
  padding: 2pt 8pt;
  border-radius: 99pt;
}}
.act-title {{
  font-size: 17pt;
  font-weight: 800;
  color: var(--ink);
  margin: 2pt 0 8pt;
  line-height: 1.2;
}}
.instruction-box {{
  border-left: 4pt solid;
  border-radius: 0 8pt 8pt 0;
  padding: 8pt 12pt;
  margin-bottom: 12pt;
}}
.act-instruction {{
  font-size: 10pt;
  color: #374151;
  line-height: 1.5;
  margin: 0;
}}
.act-area {{
  flex: 1;
  border: 1.5pt solid var(--line);
  border-radius: 12pt;
  padding: 14pt;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 180pt;
}}
.act-area svg {{
  display: block;
  width: 100%;
  max-height: 100%;
}}

/* Answer area */
.answer-area {{
  margin-top: 10pt;
  padding: 8pt 0;
}}
.answer-label {{
  font-size: 9pt;
  font-weight: 700;
  color: var(--ink-soft);
  text-transform: uppercase;
  letter-spacing: .06em;
}}
.answer-lines {{
  margin-top: 6pt;
  display: flex;
  flex-direction: column;
  gap: 10pt;
}}
.dotline {{
  display: block;
  height: 1pt;
  border-bottom: 1.5pt dotted var(--line);
  width: 100%;
}}

/* Footer */
.page-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 6pt;
  margin-top: auto;
  border-top: 1pt solid var(--line);
}}
.brand-small {{
  font-size: 7.5pt;
  color: var(--ink-soft);
  font-weight: 500;
  letter-spacing: .02em;
}}
.page-num {{
  font-size: 8.5pt;
  color: var(--ink-soft);
  font-weight: 700;
}}

/* ── GUIDE PAGE ── */
.guide-page {{ padding: 24pt 20pt; }}
.guide-inner {{ max-width: 480pt; margin: 0 auto; }}
.guide-title {{
  font-size: 24pt; font-weight: 800; color: var(--accent-dark);
  margin-bottom: 4pt; text-align: center;
}}
.guide-sub {{
  font-size: 10.5pt; color: var(--ink-soft); text-align: center;
  margin-bottom: 18pt; padding-bottom: 10pt; border-bottom: 2pt solid var(--accent);
}}
.guide-section {{ margin-bottom: 14pt; }}
.guide-section h3 {{ font-size: 13pt; font-weight: 700; color: var(--ink); margin-bottom: 5pt; }}
.guide-section p {{ font-size: 9.5pt; line-height: 1.55; color: #374151; }}
.guide-steps {{ margin: 6pt 0 0 18pt; font-size: 9.5pt; line-height: 1.6; }}
.guide-steps li {{ margin-bottom: 3pt; }}
.guide-grid {{
  display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8pt;
  margin: 12pt 0 14pt;
}}
.guide-card {{
  background: var(--paper); border: 1.5pt solid var(--line); border-radius: 8pt;
  padding: 10pt; text-align: center; break-inside: avoid;
}}
.guide-card h4 {{ font-size: 11pt; color: #F59E0B; margin-bottom: 4pt; }}
.guide-card p {{ font-size: 8.5pt; line-height: 1.45; color: var(--ink-soft); margin: 0; }}
.guide-tips {{ margin: 6pt 0 0 18pt; font-size: 9.5pt; line-height: 1.6; }}
.guide-tips li {{ margin-bottom: 3pt; }}
.guide-footer-note {{
  background: var(--paper); border-radius: 8pt; padding: 10pt 14pt;
  margin-top: 10pt;
}}
.guide-footer-note p {{ font-size: 8.5pt; color: var(--ink-soft); line-height: 1.5; margin: 0; }}

/* ── PROGRESS TRACKER ── */
.progress-page {{ padding: 18pt 14pt; }}
.progress-title {{
  font-size: 20pt; font-weight: 800; color: var(--accent-dark);
  margin-bottom: 3pt; text-align: center;
}}
.progress-sub {{
  font-size: 9pt; color: var(--ink-soft); text-align: center;
  margin-bottom: 10pt; padding-bottom: 6pt; border-bottom: 2pt solid var(--accent);
}}
.progress-grid {{
  columns: 2; column-gap: 14pt; font-size: 7pt; line-height: 1.3;
}}
.prog-cat-header {{
  font-weight: 800; color: var(--accent-dark); font-size: 7.5pt;
  padding: 4pt 0 1pt; border-bottom: 1pt solid var(--accent);
  break-after: avoid; column-span: none;
}}
.prog-row {{
  padding: 1.5pt 0; border-bottom: .5pt solid var(--line);
  break-inside: avoid;
}}
.prog-check {{ margin-right: 3pt; font-size: 8pt; }}
.prog-num {{ font-weight: 700; color: var(--ink-soft); margin-right: 2pt; }}
.progress-summary {{
  display: flex; justify-content: space-between; margin-top: 8pt;
  padding-top: 6pt; border-top: 1.5pt solid var(--accent);
  font-size: 8.5pt; font-weight: 600; color: var(--ink);
}}

/* ── ANSWER KEY ── */
.answers-page {{ padding: 24pt 20pt; }}
.answers-title {{
  font-size: 22pt; font-weight: 800; color: var(--accent-dark);
  margin-bottom: 4pt; text-align: center;
}}
.answers-sub {{
  font-size: 9.5pt; color: var(--ink-soft); text-align: center;
  margin-bottom: 14pt; padding-bottom: 8pt; border-bottom: 2pt solid var(--accent);
}}
.answers-grid {{ columns: 2; column-gap: 16pt; }}
.ans-item {{
  font-size: 8pt; line-height: 1.4; padding: 3pt 0;
  border-bottom: 1pt solid var(--line); break-inside: avoid;
}}
.ans-num {{
  display: inline-block; width: 18pt; font-weight: 700; color: var(--accent);
}}
.answers-note {{
  margin-top: 14pt; background: var(--paper); border-radius: 8pt;
  padding: 10pt 14pt; break-inside: avoid;
}}
.answers-note p {{ font-size: 9pt; color: var(--ink-soft); line-height: 1.5; margin: 0; }}

/* ── CERTIFICATE ── */
.cert-page {{
  display: flex; align-items: center; justify-content: center;
  min-height: 94vh; padding: 20pt;
}}
.cert-box {{
  border: 4pt double var(--accent); border-radius: 16pt;
  padding: 40pt 36pt; text-align: center; max-width: 420pt;
  background: white; position: relative;
}}
.cert-badge {{ font-size: 48pt; margin-bottom: 8pt; }}
.cert-title {{
  font-size: 28pt; font-weight: 800; color: var(--accent-dark);
  margin-bottom: 8pt;
}}
.cert-sub {{ font-size: 12pt; color: var(--ink-soft); margin-bottom: 16pt; }}
.cert-name-line {{
  width: 260pt; height: 0; border-bottom: 2pt solid var(--ink);
  margin: 0 auto 16pt;
}}
.cert-reason {{ font-size: 11pt; line-height: 1.6; color: var(--ink); margin-bottom: 20pt; }}
.cert-details {{
  display: flex; justify-content: center; gap: 30pt; margin-bottom: 20pt;
}}
.cert-detail {{ text-align: center; }}
.cert-label {{ display: block; font-size: 8pt; color: var(--ink-soft); text-transform: uppercase; letter-spacing: .08em; margin-bottom: 4pt; }}
.cert-value {{ font-size: 11pt; font-weight: 600; color: var(--ink); }}
.cert-closing {{ font-size: 10pt; color: var(--ink-soft); font-style: italic; margin-bottom: 12pt; }}
.cert-brand {{ font-size: 9pt; color: var(--accent); font-weight: 700; letter-spacing: .06em; }}

@media print {{
  body {{ -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
  .cat-ribbon, .cat-badge, .cat-divider-box, .instruction-box, .cert-box, .guide-card {{
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}
}}
"""

# ─── MAIN ──────────────────────────────────────────────────

def _generate_answer(cat_tag, idx):
    """Generate answer hints for logic/pattern activities."""
    if cat_tag == "logica":
        rules = ["add", "add", "add", "subtract", "subtract",
                 "add", "multiply", "subtract", "add", "multiply",
                 "fibonacci", "multiply", "subtract", "fibonacci", "multiply"]
        r = rules[idx]
        if r == "add": return "adunare (+2 la +5)"
        if r == "subtract": return "scădere (-3 la -7)"
        if r == "multiply": return "multiplicare (×2 sau ×3)"
        return "Fibonacci (fiecare = suma ultimilor doi)"
    return ""


def main():
    activities = []
    global_num = 1
    for cat_idx, (cat_name, cat_tag) in enumerate(CATS):
        gen = GENERATORS[cat_idx]
        for act_idx in range(15):
            title, instruction, svg = gen(act_idx)
            age = _age(act_idx)
            difficulty = _difficulty(act_idx)
            activities.append({
                "cat_name": cat_name,
                "cat_tag": cat_tag,
                "act_num": act_idx + 1,
                "global_num": global_num,
                "title": title,
                "instruction": instruction,
                "svg": svg,
                "age": age,
                "difficulty": difficulty,
                "answer": _generate_answer(cat_tag, act_idx),
            })
            global_num += 1

    pages = [build_cover(), build_guide(), build_toc(activities), build_progress_tracker(activities)]
    for cat_idx, (cat_name, cat_tag) in enumerate(CATS):
        cat_acts = [a for a in activities if a["cat_tag"] == cat_tag]
        pages.append(build_cat_divider(cat_name, cat_tag, cat_idx, len(cat_acts)))
        for a in cat_acts:
            pages.append(build_page(
                a["cat_name"], a["cat_tag"], a["act_num"], a["global_num"],
                a["title"], a["instruction"], a["svg"], a["age"], a["difficulty"]
            ))
    pages.append(build_answer_key(activities))
    pages.append(build_certificate())

    html = f"""<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex,nofollow">
<title>NeuroMicuți · Sistemul Focus · Peste 100 de activități</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{"".join(pages)}
</body>
</html>"""

    out = PROJ / "pdf-sources" / "fichas-core.html"
    out.write_text(html, "utf-8")
    print(f"Generate {len(activities)} activități → {out}")
    print(f"Total pagini (cu portadă, cuprins, ghid, progres, răspunsuri, certificat și separatoare): {len(pages)}")


if __name__ == "__main__":
    main()
