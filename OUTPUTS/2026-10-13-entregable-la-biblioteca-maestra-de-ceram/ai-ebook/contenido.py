# -*- coding: utf-8 -*-
"""Ejemplo minimo y funcional de contenido.py para generador-ebooks.

Ebook de muestra: "Huerta en Casa" (3 paginas de contenido + portada + indice + cierre).
Copialo a la carpeta de tu proyecto, renombralo a contenido.py y reemplaza:
  - PALETA  -> los hex de TU landing (PALETTE.md)
  - IDIOMA  -> el idioma del libro
  - PAGINAS -> una tupla por pagina con tu contenido real

Probar sin gastar:   python generar.py --contenido contenido_ejemplo.py --estimar
Probar 1 pagina:     python generar.py --contenido contenido_ejemplo.py --salida paginas --solo 1
"""

IDIOMA = "Spanish"
MARCA = "Huerta en Casa"

# 3 colores alcanzan: oscuro dominante, acento, fondo claro. Siempre hex exactos.
PALETA = ("deep green #1F3D2B, terracotta accent #C8643B, warm cream background #FBF7F1, "
          "professional editorial magazine quality, A4 vertical 2:3")

CIERRE_PROMPT = f"All text in correct {IDIOMA} with proper accents. {PALETA}"

# (numero, titulo, categoria, descripcion, materiales[5], pasos[6], consejo)
PAGINAS = [
    (1, "Lechuga en maceta", "Hojas",
     "La planta ideal para empezar: crece rápido y se cosecha hoja por hoja.",
     ["Maceta de 20 cm", "Sustrato con compost", "Semillas de lechuga", "Regadera", "Etiqueta"],
     ["Llenar la maceta", "Sembrar a 1 cm", "Regar suave", "Luz 5 horas", "Ralear plantines", "Cosechar hojas"],
     "Cosechá siempre las hojas de afuera: la planta sigue produciendo semanas."),
    (2, "Albahaca", "Aromáticas",
     "Aromática de verano que se multiplica si cortás las puntas a tiempo.",
     ["Maceta de 15 cm", "Sustrato liviano", "Plantín de albahaca", "Plato", "Tijera"],
     ["Trasplantar", "Regar abundante", "Sol directo", "Cortar puntas", "Quitar flores", "Cosechar"],
     "Si aparecen flores, cortalas: la planta vuelve a dar hojas."),
    (3, "Tomate cherry", "Frutos",
     "Rinde mucho en poco espacio si le das tutor y sol de mañana.",
     ["Maceta de 30 cm", "Sustrato rico", "Plantín de tomate", "Tutor de caña", "Hilo de algodón"],
     ["Trasplantar hondo", "Clavar el tutor", "Atar sin apretar", "Regar parejo", "Quitar brotes", "Cosechar rojos"],
     "Regá siempre a la misma hora: los cambios bruscos rajan los frutos."),
]

PORTADA = (
    "Elegant editorial book cover, A4 vertical, deep green #1F3D2B background "
    "with subtle terracotta line ornaments in the corners. "
    'Large elegant cream serif title on two lines: "Huerta" then "en Casa". '
    'Terracotta subtitle below: "Cultivos paso a paso para balcón y patio". '
    "Center: refined photorealistic still life of small pots with lettuce, basil and cherry tomatoes "
    "on a wooden shelf, warm soft lighting. "
    f'Bottom small cream text "{MARCA}". Thin terracotta border frame around the whole cover. '
    + CIERRE_PROMPT
)

INDICE = (
    "Elegant editorial table of contents page, A4 vertical, cream background. "
    'Deep green header band with cream serif title "Índice". '
    "Below, an elegant list of 3 numbered entries in dark serif, each with a small terracotta "
    "line icon and a page number on the right: "
    + "; ".join(f"{p[0]} {p[1]} ({p[2]}) página {i + 3}" for i, p in enumerate(PAGINAS))
    + ". Thin terracotta dividing lines between entries. "
    'Small page number "2" centered at the very bottom. '
    + CIERRE_PROMPT
)

CIERRE = (
    "Elegant editorial closing page, A4 vertical, deep green #1F3D2B background. "
    'Centered cream serif title "¡A cosechar!". '
    "Below, a short cream paragraph encouraging the reader to start with one pot this week. "
    'Then a terracotta-bordered box titled "Recordatorios" with 4 short bullet points: '
    "Regá a la misma hora; Buscá 5 horas de sol; Cosechá seguido; Anotá lo que funciona. "
    f'Bottom small cream text "{MARCA}". '
    + CIERRE_PROMPT
)


def build_prompt(p):
    num, titulo, categoria, desc, materiales, pasos, consejo = p
    pasos_txt = ", ".join(f"{i} {t}" for i, t in enumerate(pasos, 1))
    return (
        "Editorial home gardening guide page, A4 vertical, cream #FBF7F1 background. "
        f'Deep green rounded badge with terracotta border reading "{categoria} · {num}". '
        f'Large bold dark serif title "{titulo}". '
        "Top right: photorealistic photo of the plant growing in a pot on a sunny balcony, soft natural light. "
        f'Short intro paragraph: "{desc}" '
        f"Bordered box titled \"Materiales\" with 5 small terracotta line icons, 5 items: {'; '.join(materiales)}. "
        "Horizontal band titled \"Paso a paso\": 6 circular outline icons connected by terracotta arrows, "
        f"numbered {pasos_txt}, each with a short caption underneath. "
        f'Bottom deep green box with a terracotta star icon reading "Consejo: {consejo}" '
        f'Small page number "{num + 2}" centered at the very bottom. '
        + CIERRE_PROMPT
    )


def build_all():
    """[(nombre_archivo, prompt)] en orden del libro.

    El prefijo es la POSICION en el libro (000, 001, ...), no el numero de contenido.
    """
    paginas = [("000_portada", PORTADA), ("001_indice", INDICE)]
    for i, p in enumerate(PAGINAS, start=2):
        paginas.append((f"{i:03d}_pagina_{p[0]:03d}", build_prompt(p)))
    paginas.append((f"{len(PAGINAS) + 2:03d}_cierre", CIERRE))
    return paginas


# Falla temprano si la cantidad no coincide con lo que promete la landing.
assert len(PAGINAS) == 3, f"Esperaba 3 páginas, hay {len(PAGINAS)}"
