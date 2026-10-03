#!/usr/bin/env python3
"""Subtítulos karaoke (.ass) con tiempos POR PALABRA, alineados al guion.

- El TEXTO sale del guion que le pasaste a la voz (fuente de la verdad).
- Los TIEMPOS salen de openai-whisper (word_timestamps=True) sobre el AUDIO FINAL.
- Se alinean con difflib. Nunca se reparte el texto proporcional al tiempo (se desincroniza).
- 4 palabras por línea, fuente 52 en 720x1280, márgenes 60, WrapStyle 0.
- Cada línea queda en pantalla hasta que arranca la siguiente (no parpadea).
- Tramos "quote card" (texto sobre fondo liso): subtítulo centrado en pantalla.

Uso:
  python3 tools/karaoke_ass.py voz_final.wav guion.txt karaoke.ass --idioma es      (Windows: python en vez de python3)
  python3 tools/karaoke_ass.py voz_final.wav guion.txt karaoke.ass --idioma en --quote-card 0-4.5,12-20
  python3 tools/karaoke_ass.py audio_avatar.wav guion_hook.txt hook.ass --modelo medium   (audio real de un avatar)
Opciones: --palabras 4 · --fuente "Arial Black" · --tam 52 · --margen-v 380 · --modelo small
Idiomas con palabras largas (pl, de, cs, ru): probá --palabras 3.
"""
import argparse
import difflib
import re

from cargar_env import leer_texto   # además pone la consola en UTF-8 (Windows)


def ts(x):
    x = max(0.0, x)
    h, m = int(x // 3600), int(x % 3600 // 60)
    return f"{h}:{m:02d}:{x % 60:05.2f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("guion"); ap.add_argument("salida")
    ap.add_argument("--idioma", default=None)
    ap.add_argument("--palabras", type=int, default=4)
    ap.add_argument("--fuente", default="Arial Black")
    ap.add_argument("--tam", type=int, default=52)
    ap.add_argument("--margen-v", type=int, default=380, help="distancia al borde inferior (tercio inferior)")
    ap.add_argument("--modelo", default="small")
    ap.add_argument("--quote-card", default="", help="tramos a centrar, ej: 0-4.5,12-20 (segundos del video final)")
    a = ap.parse_args()

    from media import ffmpeg
    ffmpeg()          # deja un ffmpeg en el PATH: whisper lo necesita para leer el audio
    import whisper

    norm = lambda s: re.sub(r"[^\w]", "", s.lower())

    # 1. palabras del guion (un signo suelto se pega a la palabra anterior)
    tokens = []
    for t in re.findall(r"\S+", leer_texto(a.guion)):
        if norm(t) == "" and tokens:
            tokens[-1] += " " + t
        elif norm(t) != "":
            tokens.append(t)

    # 2. palabras que escuchó whisper, con tiempos
    res = whisper.load_model(a.modelo).transcribe(a.audio, word_timestamps=True, language=a.idioma)
    heard = [w for s in res["segments"] for w in s.get("words", [])]
    if not heard:
        raise SystemExit("Whisper no devolvió palabras. ¿El audio está vacío o cortado?")

    # 3. alinear guion <-> audio
    times = [None] * len(tokens)
    sm = difflib.SequenceMatcher(None, [norm(t) for t in tokens], [norm(w["word"]) for w in heard], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                times[i1 + k] = (heard[j1 + k]["start"], heard[j1 + k]["end"])
        elif tag == "replace":
            st, en, n = heard[j1]["start"], heard[j2 - 1]["end"], i2 - i1
            for k in range(n):
                times[i1 + k] = (st + (en - st) * k / n, st + (en - st) * (k + 1) / n)
    for i in range(len(times)):                       # palabras que whisper no oyó
        if times[i] is None:
            prev = times[i - 1][1] if i else 0.0
            times[i] = (prev, prev + 0.15)
    faltantes = sum(op[2] - op[1] for op in sm.get_opcodes() if op[0] == "delete")
    if faltantes > max(3, len(tokens) * 0.1):
        print(f"AVISO: {faltantes} palabras del guion no aparecen en el audio. ¿La voz se truncó?")

    tramos = []
    for r in filter(None, a.quote_card.split(",")):
        t0, t1 = r.split("-")
        tramos.append((float(t0), float(t1)))
    centrado = lambda t: any(t0 <= t < t1 for t0, t1 in tramos)

    # 4. líneas de N palabras; cada línea dura hasta que empieza la siguiente
    n = a.palabras
    lines = [list(range(i, min(i + n, len(tokens)))) for i in range(0, len(tokens), n)]
    ev = []
    for li, idx in enumerate(lines):
        start = times[idx[0]][0]
        end = times[lines[li + 1][0]][0] if li + 1 < len(lines) else times[idx[-1]][1] + 0.4
        end = max(end, start + 0.3)
        parts = []
        for k, i in enumerate(idx):
            nxt = times[idx[k + 1]][0] if k + 1 < len(idx) else end
            cs = max(1, round((nxt - times[i][0]) * 100))
            parts.append(f"{{\\kf{cs}}}{tokens[i]}")
        pos = "{\\an5\\pos(360,640)}" if centrado(start) else ""
        ev.append(f"Dialogue: 0,{ts(start)},{ts(end)},K,,0,0,0,,{pos}{' '.join(parts)}")

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: K,{a.fuente},{a.tam},&H0000F0FF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,2,60,60,{a.margen_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(a.salida, "w", encoding="utf-8") as fh:
        fh.write(header + "\n".join(ev) + "\n")
    print(a.salida, len(ev), "líneas ·", len(tokens), "palabras")


if __name__ == "__main__":
    main()
