#!/usr/bin/env python3
"""
gen_cards.py — Genera cards PNG de texto (formato mármol) + concat.txt para ffmpeg.

Uso:
  python3 tools/gen_cards.py \\
    voces/adN.ass \\        # ASS con timing por palabra (de karaoke_ass.py)
    voces/adN.txt \\        # guion en sentence case (define el texto de las cards)
    cards/adN/ \\           # carpeta de salida
    cards/fondo_marmol.png  # fondo para las content cards

Opciones:
  --cta "IGEN, HOZZÁFÉRÉST KÉREK"   texto de la CTA card (fondo oscuro)
  --fondo-cta "#2C2A28"             color del fondo de la CTA card
  --pausa-cta 2.5                   duración en segundos de la CTA al final
  --font /ruta/fuente.ttf
  --font-bold /ruta/fuente-bold.ttf
  --tam 75                           tamaño de fuente content cards
  --tam-cta 72                       tamaño de fuente CTA card
  --color-texto "#17130E"
  --padding-h 90                     padding horizontal en píxeles
  --max-ancho 540                    ancho máximo del bloque de texto en px
  --construir-video                  genera base.mp4 además del concat.txt
"""
import argparse
import difflib
import os
import re
import subprocess
import sys
import textwrap
from pathlib import Path


# ── helpers ─────────────────────────────────────────────────────────────────

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("ass")
    ap.add_argument("guion")
    ap.add_argument("salida_dir")
    ap.add_argument("fondo_marmol")
    ap.add_argument("--cta", default="")
    ap.add_argument("--fondo-cta", default="#2C2A28")
    ap.add_argument("--pausa-cta", type=float, default=2.5)
    ap.add_argument("--font", default="")
    ap.add_argument("--font-bold", default="")
    ap.add_argument("--tam", type=int, default=75)
    ap.add_argument("--tam-cta", type=int, default=72)
    ap.add_argument("--color-texto", default="#17130E")
    ap.add_argument("--padding-h", type=int, default=90)
    ap.add_argument("--max-ancho", type=int, default=540)
    ap.add_argument("--construir-video", action="store_true")
    return ap.parse_args()


def ts_to_sec(ts):
    """'0:00:03.04' → 3.04"""
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def norm(w):
    return re.sub(r"[^\w]", "", w.lower())


# ── ASS parsing ──────────────────────────────────────────────────────────────

def parse_ass(path):
    """
    Returns list of (start_sec, end_sec, [words]) for each dialogue line.
    Strips {\\kf...} karaoke tags.
    """
    lines = []
    strip = re.compile(r"\{[^}]+\}")
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            raw = raw.rstrip()
            if not raw.startswith("Dialogue:"):
                continue
            parts = raw.split(",", 9)
            if len(parts) < 10:
                continue
            start = ts_to_sec(parts[1])
            end   = ts_to_sec(parts[2])
            text  = strip.sub("", parts[9])
            words = text.split()
            if words:
                lines.append((start, end, words))
    return lines


def ass_word_list(dialogues):
    """Flatten dialogues → [(start_sec, word), ...]"""
    result = []
    for start, end, words in dialogues:
        n = len(words)
        span = max(end - start, 0.01)
        for i, w in enumerate(words):
            t = start + span * i / n
            result.append((t, w))
    return result


# ── script parsing ───────────────────────────────────────────────────────────

def load_paragraphs(path):
    text = Path(path).read_text(encoding="utf-8").strip()
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paras


# ── paragraph → timing ───────────────────────────────────────────────────────

def align_paragraphs(paragraphs, ass_words):
    """
    Returns [(start_sec, end_sec)] for each paragraph.
    Uses difflib to align script words with ASS words (handles case/accent diffs).
    """
    # Build flat word lists
    script_words = []
    para_starts  = []   # index in script_words where each paragraph begins
    for para in paragraphs:
        para_starts.append(len(script_words))
        script_words.extend(para.split())

    ass_norms  = [norm(w) for _, w in ass_words]
    scr_norms  = [norm(w) for w in script_words]

    # Align script words → ASS words
    sm = difflib.SequenceMatcher(None, scr_norms, ass_norms, autojunk=False)
    mapping = {}   # script_word_idx → ass_word_idx
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                mapping[i1 + k] = j1 + k
        elif tag == "replace":
            for k in range(i2 - i1):
                mapping[i1 + k] = j1 + min(k, j2 - j1 - 1)

    # Fill gaps
    last_j = 0
    for i in range(len(script_words)):
        if i in mapping:
            last_j = mapping[i]
        else:
            mapping[i] = last_j

    # Paragraph timings
    total_words = len(script_words)
    last_time   = ass_words[-1][0] if ass_words else 0.0
    results = []
    for pi, start_idx in enumerate(para_starts):
        end_idx = para_starts[pi + 1] if pi + 1 < len(para_starts) else total_words
        start_sec = ass_words[mapping[start_idx]][0]
        if pi + 1 < len(para_starts):
            next_start_sec = ass_words[mapping[para_starts[pi + 1]]][0]
        else:
            # Last paragraph: use end of last ASS line
            # Find end time from dialogue
            next_start_sec = last_time + 1.0  # will be overridden below
        results.append((start_sec, next_start_sec))

    # Adjust last card to end of audio (add hold)
    if results:
        start_last, _ = results[-1]
        results[-1] = (start_last, last_time + 0.8)

    return results


# ── font loading ──────────────────────────────────────────────────────────────

FONT_CANDIDATES = [
    "/Library/Fonts/Georgia.ttf",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/Library/Fonts/Georgia Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
]

FONT_BOLD_CANDIDATES = [
    "/Library/Fonts/Georgia Bold.ttf",
    "/Library/Fonts/GeorgiaBold.ttf",
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/Library/Fonts/Times New Roman Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
]


def load_font(size, path="", candidates=None):
    from PIL import ImageFont
    if path and os.path.exists(path):
        return ImageFont.truetype(path, size)
    for c in (candidates or FONT_CANDIDATES):
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    print("AVISO: no se encontró fuente TTF, usando fuente por defecto (calidad baja)")
    return ImageFont.load_default()


# ── text wrapping ─────────────────────────────────────────────────────────────

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = " ".join(current + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        w = bbox[2] - bbox[0]
        if w > max_width and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


def text_block_size(lines, font, draw, line_gap=18):
    if not lines:
        return 0, 0
    widths, heights = [], []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
    total_h = sum(heights) + line_gap * (len(lines) - 1)
    max_w   = max(widths)
    return max_w, total_h


# ── card rendering ────────────────────────────────────────────────────────────

def render_content_card(text, bg_path, font, max_width, color_rgb, draw_ref):
    from PIL import Image, ImageDraw
    bg = Image.open(bg_path).convert("RGB")
    W, H = bg.size
    draw = ImageDraw.Draw(bg)

    lines = wrap_text(text, font, max_width, draw)
    if not lines:
        return bg

    line_gap = 20
    bboxes = [draw.textbbox((0, 0), l, font=font) for l in lines]
    heights = [b[3] - b[1] for b in bboxes]
    total_h = sum(heights) + line_gap * (len(lines) - 1)

    y = (H - total_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        lw = bbox[2] - bbox[0]
        x = (W - lw) // 2
        draw.text((x, y), line, font=font, fill=color_rgb)
        y += heights[i] + line_gap

    return bg


def render_cta_card(text, bg_color_hex, font_bold, W=720, H=1280, font_bold_path="", font_bold_size=72):
    from PIL import Image, ImageDraw, ImageFont
    bg_rgb = hex_to_rgb(bg_color_hex)
    img  = Image.new("RGB", (W, H), bg_rgb)
    draw = ImageDraw.Draw(img)

    max_text_w = int(W * 0.88)  # 88% of card width
    upper_text = text.upper()
    line_gap = 16

    # Auto-reduce font size until text fits on one line (or use word-wrap at current size)
    font = font_bold
    cur_size = font_bold_size
    if font_bold_path:
        while True:
            bbox = draw.textbbox((0, 0), upper_text, font=font)
            if bbox[2] - bbox[0] <= max_text_w or cur_size <= 36:
                break
            cur_size -= 4
            font = ImageFont.truetype(font_bold_path, cur_size)

    # Word-wrap (in case single line still doesn't fit after min size)
    lines = wrap_text(upper_text, font, max_text_w, draw)
    bboxes = [draw.textbbox((0, 0), l, font=font) for l in lines]
    heights = [b[3] - b[1] for b in bboxes]
    total_h = sum(heights) + line_gap * (len(lines) - 1)

    y = (H - total_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        lw = bbox[2] - bbox[0]
        x = (W - lw) // 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += heights[i] + line_gap

    return img


# ── concat.txt & base.mp4 ─────────────────────────────────────────────────────

def write_concat(out_dir, entries):
    """entries: [(path, duration_sec), ...]"""
    lines = []
    for path, dur in entries:
        lines.append(f"file '{path}'")
        lines.append(f"duration {dur:.2f}")
    # ffmpeg concat: repeat last file without duration
    lines.append(f"file '{entries[-1][0]}'")
    p = os.path.join(out_dir, "concat.txt")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return p


def build_video(concat_path, out_path):
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_path,
        "-vf", "scale=720:1280",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-r", "30",
        out_path,
    ]
    subprocess.run(cmd, check=True)


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    from PIL import ImageDraw
    a = parse_args()
    out_dir = Path(a.salida_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Leyendo ASS:", a.ass)
    dialogues = parse_ass(a.ass)
    if not dialogues:
        sys.exit("Error: el ASS está vacío o no tiene líneas Dialogue.")
    words = ass_word_list(dialogues)
    total_duration = dialogues[-1][1]  # end time of last dialogue line

    print("Leyendo guion:", a.guion)
    paragraphs = load_paragraphs(a.guion)
    print(f"  {len(paragraphs)} párrafos detectados")

    print("Alineando párrafos con ASS...")
    timings = align_paragraphs(paragraphs, words)

    # Durations
    durations = []
    for i, (t_start, t_end) in enumerate(timings):
        dur = t_end - t_start
        durations.append(max(dur, 0.5))
    print(f"  Duraciones: {[f'{d:.2f}' for d in durations]}")
    print(f"  Total video: {sum(durations):.2f}s  |  Audio: {total_duration:.2f}s")

    # Load fonts
    font      = load_font(a.tam,     a.font,      FONT_CANDIDATES)
    font_bold = load_font(a.tam_cta, a.font_bold,  FONT_BOLD_CANDIDATES)

    color_rgb = hex_to_rgb(a.color_texto)

    # Dummy draw for text measurement
    from PIL import Image, ImageDraw
    dummy = Image.new("RGB", (720, 1280))
    draw_ref = ImageDraw.Draw(dummy)

    entries = []

    # Content cards
    for i, (para, dur) in enumerate(zip(paragraphs, durations)):
        card_name = f"c{i:02d}.png"
        card_path = str(out_dir / card_name)
        print(f"  Generando {card_name} ({dur:.2f}s) ...")
        img = render_content_card(
            para, a.fondo_marmol, font,
            a.max_ancho, color_rgb, draw_ref
        )
        img.save(card_path)
        entries.append((card_path, dur))

    # CTA card (optional)
    if a.cta:
        cta_path = str(out_dir / "cta.png")
        print(f"  Generando cta.png ...")
        resolved_bold_path = a.font_bold
        if not resolved_bold_path:
            for c in FONT_BOLD_CANDIDATES:
                if os.path.exists(c):
                    resolved_bold_path = c
                    break
        img = render_cta_card(
            a.cta, a.fondo_cta, font_bold,
            font_bold_path=resolved_bold_path,
            font_bold_size=a.tam_cta,
        )
        img.save(cta_path)
        # CTA is not added to concat.txt by default (matches CZ pipeline)

    # concat.txt
    concat_path = write_concat(str(out_dir), entries)
    print(f"concat.txt escrito en {concat_path}")

    # base.mp4
    if a.construir_video:
        video_path = str(out_dir / "base.mp4")
        print(f"Construyendo {video_path} ...")
        build_video(concat_path, video_path)
        print(f"base.mp4 listo: {video_path}")
    else:
        print("(Pasá --construir-video para generar base.mp4 automáticamente)")

    print("Listo.")


if __name__ == "__main__":
    main()
