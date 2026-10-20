# -*- coding: utf-8 -*-
"""Genera core.html con 175 páginas de patrones técnicos de cuero (SVG).
Cada página: header, SVG con piezas acotadas, lista de materiales, pasos de montaje, cuadrado de control.
Uso: python3 generar_core.py > core.html
"""
import random
import textwrap

random.seed(42)

# ── Paleta (de la landing) ──────────────────────────────────────────────
BG      = "#FFFFFF"       # fondo de impresión
INK     = "#1A0F08"
ACCENT  = "#E0A15E"
COPPER  = "#C8722A"
SOFT    = "#5A4232"
LINE    = "#E6D5C0"
CREAM   = "#F5EDE0"
GREEN   = "#3E8E5A"

# ── Datos de los 175 patrones ───────────────────────────────────────────
CATEGORIES = [
    ("Taschen und Handtaschen", "👜", [
        ("Klassische Tote-Tasche", 2, [("Vorderteil","A1",380,320),("Rückteil","A2",380,320),("Seitenteil","A3",80,320,2),("Boden","A4",380,80),("Henkel","A5",500,35,2)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Polyester-Garn, gewachst","0,8 mm"),("Nieten","9 mm, Messing, ×8"),("D-Ringe","25 mm, ×4")],
         ["Alle Teile zuschneiden und Kanten brechen","Seitenteile an Vorder- und Rückteil nähen","Boden einsetzen und mit Sattlernaht befestigen","Henkel doppelt legen, heften und annähen","Kanten mit Tokonole versiegeln und polieren"]),
        ("Mini-Tote", 1, [("Vorderteil","A1",260,220),("Rückteil","A2",260,220),("Seitenteil","A3",60,220,2),("Boden","A4",260,60),("Henkel","A5",350,25,2)],
         [("Vegetabil gegerbtes Leder","1,5–2,0 mm"),("Leinengarn, gewachst","0,6 mm"),("Nieten","7 mm, Messing, ×4")],
         ["Teile zuschneiden","Seiten an Vorder-/Rückteil nähen","Boden einsetzen","Henkel befestigen","Kanten versiegeln"]),
        ("Strukturierte Handtasche", 3, [("Vorderteil","A1",300,240),("Rückteil","A2",300,240),("Seitenzwickel","A3",70,240,2),("Boden","A4",300,70),("Klappe","A5",300,140),("Henkel","A6",420,30,2),("Taschenfutter","A7",290,230)],
         [("Chromgegerbtes Rindsleder","1,8–2,2 mm"),("Polyester-Garn","0,8 mm"),("Magnetverschluss","18 mm, ×1"),("D-Ringe","20 mm, ×4"),("Nieten","9 mm, ×6")],
         ["Alle Teile zuschneiden","Futter an Klappe nähen","Seitenzwickel an Vorder-/Rückteil","Boden einsetzen","Klappe anbringen und Verschluss setzen","Henkel befestigen","Kanten versiegeln"]),
        ("Markttasche mit offenem Rand", 1, [("Hauptteil","A1",450,380),("Verstärkung oben","A2",450,40,2),("Henkel","A3",550,40,2)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Leinengarn","0,6 mm"),("Nieten","9 mm, ×8")],
         ["Hauptteil zuschneiden","Verstärkung oben umklappen und nähen","Henkel doppelt legen und befestigen","Seiten zusammennähen","Kanten ölen"]),
        ("Schultertasche mit Klappe", 3, [("Vorderteil","A1",280,220),("Rückteil mit Klappe","A2",280,340),("Seitenzwickel","A3",60,220,2),("Boden","A4",280,60),("Schulterriemen","A5",1200,25),("Tasche innen","A6",260,120)],
         [("Pflanzlich gegerbtes Leder","1,8–2,0 mm"),("Polyester-Garn","0,8 mm"),("Drehverschluss","×1"),("D-Ringe","25 mm, ×2"),("Karabiner","25 mm, ×2")],
         ["Teile zuschneiden","Innentasche auf Rückteil nähen","Seitenteile und Boden einsetzen","Klappe umklappen, Verschluss setzen","Riemen anfertigen und einhaken","Kanten versiegeln"]),
        ("Hobo-Tasche", 2, [("Hauptteil","A1",400,350),("Seitenteil","A2",100,350,2),("Henkel","A3",500,30),("Innentasche","A4",200,150)],
         [("Weiches Ziegenleder","1,0–1,4 mm"),("Baumwollgarn","0,6 mm"),("Reißverschluss","20 cm, ×1"),("D-Ringe","20 mm, ×2")],
         ["Innentasche mit Reißverschluss auf Rückteil","Seitenteile annähen","Hauptteile zusammennähen","Henkel befestigen","Kanten versiegeln"]),
        ("Beuteltasche", 2, [("Hauptteil","A1",380,360),("Boden (rund)","A2",200,200),("Zugband-Kanal","A3",380,40),("Kordelzug","A4",800,8,2)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Leinengarn","0,6 mm"),("Ösen","10 mm, ×6")],
         ["Hauptteil zuschneiden","Zugband-Kanal oben annähen","Seitennaht schließen","Runden Boden einsetzen","Ösen setzen und Kordelzug einfädeln","Kanten ölen"]),
        ("Clutch mit Reißverschluss", 1, [("Vorderteil","A1",280,180),("Rückteil","A2",280,180),("Futter","A3",270,170,2),("Seitenfalte","A4",30,180,2)],
         [("Chromgegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","25 cm, ×1"),("Zuglasche Leder","50×10 mm")],
         ["Teile zuschneiden","Reißverschluss zwischen Außen- und Futter nähen","Seitenfalten einsetzen","Unten zusammennähen und wenden","Kanten versiegeln"]),
        ("Laptop-Tasche 15 Zoll", 3, [("Vorderteil","A1",400,300),("Rückteil","A2",400,300),("Boden","A4",400,40),("Klappe","A5",400,180),("Seitenzwickel","A3",40,300,2),("Henkel","A6",350,30,2),("Schulterriemen","A7",1300,30),("Polsterung innen","A8",390,290,2)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Polyester-Garn","1,0 mm"),("Magnetverschluss","18 mm, ×2"),("Nieten","9 mm, ×8"),("D-Ringe","25 mm, ×2"),("Schaumstoffpolster","3 mm, 390×290 mm")],
         ["Polsterung auf Innenteile kleben","Seitenteile und Boden an Rückteil nähen","Vorderteil annähen","Klappe befestigen, Magnete setzen","Henkel und Schulterriemen anbringen","Kanten versiegeln und polieren"]),
        ("Aktentasche klassisch", 4, [("Vorderteil","A1",420,300),("Rückteil","A2",420,300),("Boden","A3",420,100),("Seitenzwickel","A4",100,300,2),("Klappe","A5",420,200),("Steckfach vorne","A6",400,180),("Henkel","A7",160,30,2),("Schulterriemen","A8",1300,25),("Trennwand innen","A9",400,290)],
         [("Pflanzlich gegerbtes Rindsleder","2,5–3,0 mm"),("Leinengarn","0,8 mm"),("Steckverschluss","×2"),("Nieten","9 mm, ×12"),("D-Ringe","25 mm, ×2"),("Füße","15 mm, Messing, ×4")],
         ["Alle 9 Teile zuschneiden und Nählinien anreißen","Steckfach auf Vorderteil nähen","Trennwand vorbereiten","Boden und Seitenteile an Rückteil","Vorderteil annähen","Klappe befestigen, Verschlüsse setzen","Henkel und Riemen anbringen","Füße einsetzen","Kanten versiegeln"]),
        ("Shopper mit breitem Boden", 2, [("Vorderteil","A1",400,340),("Rückteil","A2",400,340),("Boden","A3",400,120),("Seitenteil","A4",120,340,2),("Henkel","A5",600,35,2)],
         [("Pflanzlich gegerbtes Leder","2,0–2,2 mm"),("Polyester-Garn","0,8 mm"),("Nieten","9 mm, ×8")],
         ["Teile zuschneiden","Seitenteile an Vorder-/Rückteil","Boden einsetzen","Henkel befestigen","Kanten versiegeln"]),
        ("Kleine Abendtasche", 2, [("Vorderteil","A1",220,150),("Rückteil","A2",220,150),("Klappe","A3",220,100),("Kette/Riemen","A4",1000,8)],
         [("Chromgegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Magnetverschluss","14 mm"),("Kette","100 cm, ×1")],
         ["Teile zuschneiden","Klappe an Rückteil nähen","Vorder- und Rückteil zusammennähen","Verschluss setzen","Kette/Riemen befestigen","Kanten polieren"]),
        ("Umschlagtasche", 2, [("Hauptteil","A1",350,480),("Innentasche","A2",340,120),("Riemenbefestigung","A3",40,60,2)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Leinengarn","0,6 mm"),("Druckknopf","15 mm, ×1"),("D-Ringe","15 mm, ×2")],
         ["Hauptteil zuschneiden","Innentasche aufnähen","Druckknopf setzen","Umschlag falten und Seiten nähen","Riemenbefestigung anbringen","Kanten versiegeln"]),
        ("Dokumententasche A4", 2, [("Vorderteil","A1",340,260),("Rückteil","A2",340,260),("Boden/Seite (U-Form)","A3",340,50)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","35 cm, ×1")],
         ["Teile zuschneiden","Reißverschluss oben einnähen","U-förmiges Bodenteil einsetzen","Kanten versiegeln"]),
        ("Wickeltasche", 3, [("Hauptteil","A1",420,360),("Wickelklappe","A2",420,180),("Seitenteil","A3",100,360,2),("Innenfach","A4",400,200),("Reißverschlusstasche","A5",300,180),("Henkel","A6",450,35,2)],
         [("Pflanzlich gegerbtes Leder","1,8–2,0 mm"),("Polyester-Garn","0,8 mm"),("Reißverschluss","25 cm, ×1"),("Druckknöpfe","12 mm, ×3"),("Nieten","9 mm, ×6")],
         ["Innenfächer vorbereiten","Reißverschlusstasche nähen","Seitenteile an Hauptteil","Wickelklappe befestigen","Druckknöpfe und Henkel anbringen","Kanten versiegeln"]),
        ("Einkaufstasche faltbar", 1, [("Hauptteil","A1",400,360),("Henkel","A2",450,30,2),("Druckknopflasche","A3",60,40)],
         [("Weiches Leder","1,0–1,2 mm"),("Leinengarn","0,4 mm"),("Druckknopf","12 mm, ×1")],
         ["Hauptteil zuschneiden","Seiten und Boden nähen","Henkel befestigen","Druckknopflasche anbringen","Kanten ölen"]),
        ("Bucket-Tasche", 2, [("Hauptteil (Zylinder)","A1",440,280),("Boden (rund)","A2",140,140),("Zugband-Kanal","A3",440,35),("Kordelzug","A4",900,6,2),("Schulterriemen","A5",1200,20)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Ösen","8 mm, ×6"),("D-Ringe","20 mm, ×2")],
         ["Hauptteil zuschneiden","Zugband-Kanal oben annähen","Seitennaht schließen","Runden Boden einsetzen","Ösen setzen, Kordel einfädeln","Riemen befestigen","Kanten versiegeln"]),
        ("Tasche mit Fransen", 2, [("Vorderteil","A1",300,250),("Rückteil","A2",300,250),("Klappe mit Fransen","A3",300,180),("Fransenstreifen","A4",280,80),("Riemen","A5",1100,20)],
         [("Weiches Wildleder","1,0–1,4 mm"),("Baumwollgarn","0,6 mm"),("Magnetverschluss","14 mm, ×1"),("D-Ringe","20 mm, ×2")],
         ["Teile zuschneiden","Fransen in 5mm-Streifen schneiden","Fransenstreifen an Klappe nähen","Vorder-/Rückteil zusammennähen","Klappe befestigen","Riemen anbringen"]),
        ("Tragetasche mit Reißverschluss oben", 3, [("Vorderteil","A1",380,300),("Rückteil","A2",380,300),("Boden","A3",380,80),("Seitenteil","A4",80,300,2),("Reißverschluss-Einfassung","A5",380,30,2),("Henkel","A6",500,30,2),("Innentasche","A7",250,180)],
         [("Pflanzlich gegerbtes Leder","2,0–2,2 mm"),("Polyester-Garn","0,8 mm"),("Reißverschluss","40 cm, ×1"),("Nieten","9 mm, ×8"),("D-Ringe","25 mm, ×2")],
         ["Innentasche auf Rückteil nähen","Reißverschluss-Einfassung vorbereiten","Seitenteile und Boden einsetzen","Vorder-/Rückteil zusammennähen","Reißverschluss einsetzen","Henkel befestigen","Kanten versiegeln"]),
        ("Handtasche mit Bambushenkel", 3, [("Vorderteil","A1",300,240),("Rückteil","A2",300,240),("Seitenteil","A3",60,240,2),("Boden","A4",300,60),("Henkelschlaufe","A5",100,40,2),("Innentasche","A6",280,140)],
         [("Chromgegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Bambus-Henkel","×2"),("Nieten","9 mm, ×4")],
         ["Teile zuschneiden","Innentasche aufnähen","Seitenteile und Boden einsetzen","Zusammennähen","Henkelschlaufen um Bambus-Henkel befestigen","Kanten versiegeln"]),
        ("Wendetasche", 2, [("Außenteil","A1",360,300,2),("Innenteil","A2",350,290,2),("Henkel","A3",450,30,2)],
         [("Zwei verschiedene Leder","je 1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Nieten","7 mm, ×4")],
         ["Außen- und Innenteile separat nähen","Henkel an Außenteil befestigen","Außen- und Innentasche verbinden (oben)","Durch Öffnung wenden","Wendeöffnung schließen"]),
        ("Tasche mit Webmuster", 4, [("Grundplatte","A1",300,260),("Webestreifen vertikal","A2",15,260,10),("Webestreifen horizontal","A3",300,15,9),("Rückteil","A4",300,260),("Seitenteil","A5",60,260,2),("Boden","A6",300,60),("Henkel","A7",450,30,2)],
         [("Pflanzlich gegerbtes Leder (2 Farben)","1,2–1,5 mm"),("Lederkleber","×1"),("Polyester-Garn","0,8 mm"),("Nieten","9 mm, ×8")],
         ["Webestreifen zuschneiden","Vertikale Streifen auf Grundplatte kleben","Horizontale Streifen durchflechten","Enden fixieren und Grundplatte trimmen","Rückteil, Seiten und Boden zusammennähen","Gewebtes Vorderteil einsetzen","Henkel befestigen"]),
        ("Tabletttasche", 2, [("Vorderteil","A1",280,210),("Rückteil mit Klappe","A2",280,310),("Futter","A3",270,200,2),("Schaumstoff","A4",260,190,2)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","18 mm"),("Schaumstoff","3 mm")],
         ["Schaumstoff auf Futter kleben","Außen- und Futterteile vorbereiten","Klappe zusammennähen und wenden","Seitenteile nähen","Magnetverschluss setzen","Kanten versiegeln"]),
        ("Arzttasche / Reisetasche", 4, [("Vorderteil","A1",450,260),("Rückteil","A2",450,260),("Boden","A3",450,140),("Seitenteil","A4",140,260,2),("Rahmeneinfassung","A5",450,30,2),("Henkel","A6",350,30,2),("Innentasche","A7",300,180),("Reißverschlusstasche","A8",250,160)],
         [("Pflanzlich gegerbtes Rindsleder","2,5–3,0 mm"),("Leinengarn","1,0 mm"),("Rahmenverschluss","45 cm, ×1"),("Nieten","12 mm, ×10"),("Füße","15 mm, ×4")],
         ["Innentaschen vorbereiten","Rahmeneinfassung an Vorder-/Rückteil","Seitenteile und Boden zusammennähen","Rahmenverschluss einsetzen","Henkel mit Nieten befestigen","Füße einsetzen","Kanten versiegeln und polieren"]),
        ("Eimer-Handtasche", 2, [("Hauptteil","A1",380,300),("Boden (oval)","A2",180,120),("Henkel","A3",400,25,2),("Innentasche","A4",360,140)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Nieten","9 mm, ×4")],
         ["Innentasche aufnähen","Seitennaht schließen","Ovalen Boden einsetzen","Henkel befestigen","Kanten versiegeln"]),
        ("Kosmetiktasche", 1, [("Vorderteil","A1",240,160),("Rückteil","A2",240,160),("Boden","A3",240,60),("Seitenteil","A4",60,160,2)],
         [("Weiches Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","25 cm, ×1")],
         ["Reißverschluss oben einnähen","Seitenteile und Boden einsetzen","Zusammennähen","Kanten versiegeln"]),
        ("Bauchtasche / Gürteltasche", 2, [("Vorderteil","A1",260,160),("Rückteil","A2",260,160),("Klappe","A3",260,100),("Gürtelschlaufe","A4",80,40,2),("Innenfach","A5",240,100)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Druckknopf","15 mm, ×1"),("Gürtelclip oder Schlaufe","×2")],
         ["Teile zuschneiden","Innenfach aufnähen","Vorder-/Rückteil zusammennähen","Klappe befestigen, Druckknopf setzen","Gürtelschlaufen anbringen","Kanten versiegeln"]),
        ("Handtasche mit Kette", 3, [("Vorderteil","A1",280,180),("Rückteil","A2",280,180),("Klappe","A3",280,120),("Seitenzwickel","A4",50,180,2),("Boden","A5",280,50),("Kettenschlaufe","A6",60,30,2)],
         [("Chromgegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Drehverschluss","×1"),("Kette mit Ledergeflecht","120 cm, ×1")],
         ["Seitenteile und Boden an Rückteil","Vorderteil annähen","Klappe befestigen, Verschluss setzen","Kettenschlaufen anbringen","Kette einfädeln","Kanten polieren"]),
        ("Doppeltasche (Twin Bag)", 3, [("Vorderteil A","A1",220,200),("Rückteil A","A2",220,200),("Vorderteil B","B1",220,200),("Rückteil B","B2",220,200),("Verbindungsriemen","C1",60,30),("Henkel","C2",400,25,2)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Reißverschlüsse","20 cm, ×2"),("Nieten","9 mm, ×6")],
         ["Beide Taschen separat nähen","Reißverschlüsse einsetzen","Verbindungsriemen zwischen Taschen","Henkel befestigen","Kanten versiegeln"]),
        ("Wickelclutch", 1, [("Hauptteil","A1",320,420),("Klappe","A2",320,150),("Lederband","A3",600,8)],
         [("Weiches Ziegenleder","0,8–1,0 mm"),("Leinengarn","0,4 mm"),("Druckknopf","10 mm, ×1")],
         ["Hauptteil zuschneiden","Klappe annähen","Seitennaht schließen","Lederband befestigen zum Umwickeln","Kanten ölen"]),
        ("Korbtasche mit Leder", 3, [("Lederklappe","A1",300,180),("Lederriemen","A2",1100,20),("Lederrand oben","A3",600,30),("Lederhenkel","A4",350,25,2)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,8 mm"),("Rattan- oder Strohkorb","×1"),("Nieten","9 mm, ×6")],
         ["Lederrand an Korb nähen/nieten","Klappe befestigen","Riemen und Henkel anbringen","Kanten versiegeln"]),
        ("Tasche mit Holzrahmen", 4, [("Vorderteil","A1",320,260),("Rückteil","A2",320,260),("Seitenteil","A3",60,260,2),("Boden","A4",320,60),("Rahmenhalterung","A5",320,40,2)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Leinengarn","0,8 mm"),("Holzrahmen mit Verschluss","32 cm, ×1"),("Nieten","9 mm, ×8")],
         ["Seitenteile und Boden zusammennähen","Vorder-/Rückteil einsetzen","Rahmenhalterung oben annähen","Leder um Holzrahmen falten und befestigen","Kanten versiegeln"]),
        ("Zeitschriftentasche", 2, [("Vorderteil","A1",350,280),("Rückteil","A2",350,280),("Henkel","A3",500,30,2),("Innentasche","A4",340,150)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","18 mm, ×1")],
         ["Innentasche aufnähen","Vorder-/Rückteil zusammennähen","Magnetverschluss setzen","Henkel befestigen","Kanten versiegeln"]),
        ("Tasche mit Quaste", 2, [("Vorderteil","A1",260,200),("Rückteil","A2",260,200),("Seitenteil","A3",50,200,2),("Boden","A4",260,50),("Quaste","A5",80,120),("Riemen","A6",1100,20)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","25 cm"),("D-Ringe","15 mm, ×2")],
         ["Reißverschluss oben einnähen","Seitenteile und Boden einsetzen","Zusammennähen","Quaste anfertigen und befestigen","Riemen anbringen","Kanten versiegeln"]),
        ("Werkzeugtasche (Tool Roll)", 2, [("Hauptteil","A1",500,300),("Fächer-Streifen","A2",480,120),("Binderiemen","A3",600,10),("Verschlussriemen","A4",200,15)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Leinengarn","0,8 mm"),("Druckknopf","12 mm, ×1")],
         ["Fächer-Streifen auf Hauptteil nähen","Fächertrennungen nähen (6-8 Fächer)","Binderiemen befestigen","Verschlussriemen mit Druckknopf","Kanten versiegeln","Aufrollen und testen"]),
        ("Strandtasche", 2, [("Vorderteil","A1",440,380),("Rückteil","A2",440,380),("Henkel (geflochten)","A3",600,20,6),("Innentasche mit Reißverschluss","A4",300,200)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Baumwollgarn","0,8 mm"),("Reißverschluss","25 cm"),("Nieten","9 mm, ×4")],
         ["Innentasche mit Reißverschluss vorbereiten","Vorder-/Rückteil zusammennähen","Geflochtene Henkel anfertigen (3×2 Streifen)","Henkel befestigen","Kanten ölen"]),
        ("Trapeztasche", 3, [("Vorderteil (Trapez)","A1",340,260),("Rückteil (Trapez)","A2",340,260),("Seitenteil (Dreieck)","A3",80,260,2),("Boden","A4",260,80),("Henkel","A5",350,30,2),("Reißverschluss-Einfassung","A6",260,25,2)],
         [("Pflanzlich gegerbtes Leder","1,8–2,2 mm"),("Polyester-Garn","0,8 mm"),("Reißverschluss","30 cm"),("Nieten","9 mm, ×4")],
         ["Trapezform zuschneiden (oben schmaler)","Reißverschluss-Einfassung vorbereiten","Seiten und Boden einsetzen","Zusammennähen","Reißverschluss oben einsetzen","Henkel befestigen","Kanten versiegeln"]),
        ("Multifunktionstäschchen", 1, [("Hauptteil","A1",200,140),("Klappe","A2",200,80)],
         [("Lederreste","1,0–1,5 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","10 mm")],
         ["Hauptteil falten","Seiten nähen","Klappe befestigen","Druckknopf setzen","Kanten versiegeln"]),
        ("Tasche mit Nieten-Dekor", 3, [("Vorderteil","A1",300,240),("Rückteil","A2",300,240),("Seitenteil","A3",60,240,2),("Boden","A4",300,60),("Klappe","A5",300,140),("Henkel","A6",400,30,2),("Nieten-Streifen","A7",280,20)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Ziennieten","9 mm, Messing, ×20"),("Magnetverschluss","18 mm"),("D-Ringe","25 mm, ×4")],
         ["Teile zuschneiden","Nieten-Streifen auf Klappe setzen","Seitenteile und Boden einsetzen","Zusammennähen","Klappe befestigen, Magnet setzen","Henkel anbringen","Kanten versiegeln"]),
        ("Projektmappe (Portfolio)", 3, [("Vorderteil","A1",360,270),("Rückteil","A2",360,270),("Klappe","A3",360,160),("Innenfach links","A4",170,260),("Innenfach rechts","A5",170,260),("Stiftschlaufe","A6",20,80),("Binderiemen","A7",300,12)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","18 mm, ×2"),("Druckknopf","12 mm")],
         ["Innenfächer auf Innenseite nähen","Stiftschlaufe befestigen","Vorder-/Rückteil zusammennähen","Klappe mit Magneten","Binderiemen anbringen","Kanten versiegeln"]),
    ]),
    ("Rucksäcke", "🎒", [
        ("Mini-Rucksack", 2, [("Vorderteil","A1",240,280),("Rückteil","A2",240,280),("Seitenteil","A3",60,280,2),("Boden","A4",240,60),("Klappe","A5",240,140),("Trageriemen","A6",600,25,2),("Griff oben","A7",120,25)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×2"),("D-Ringe","20 mm, ×4"),("Magnetverschluss","18 mm")],
         ["Teile zuschneiden","Seitenteile und Boden an Rückteil","Vorderteil annähen","Klappe befestigen, Magnet setzen","Trageriemen mit Schnallen","Griff oben anbringen","Kanten versiegeln"]),
        ("Urban Rucksack", 3, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("Seitenteil","A3",100,400,2),("Boden","A4",300,100),("Klappe","A5",300,200),("Trageriemen","A6",700,30,2),("Griff oben","A7",140,30),("Vortasche","A8",280,180),("Laptopfach","A9",280,360)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Polyester-Garn","1,0 mm"),("Schnallen","30 mm, ×2"),("D-Ringe","25 mm, ×4"),("Magnetverschluss","18 mm, ×2"),("Reißverschluss","25 cm, ×1"),("Schaumstoff","3 mm")],
         ["Laptopfach mit Schaumstoff polstern","Vortasche mit Reißverschluss vorbereiten","Seitenteile und Boden zusammennähen","Vorder-/Rückteil einsetzen","Klappe befestigen","Trageriemen mit Schnallen","Griff anbringen","Kanten versiegeln"]),
        ("Laptop-Rucksack 15 Zoll", 4, [("Vorderteil","A1",320,440),("Rückteil (gepolstert)","A2",320,440),("Seitenteil","A3",120,440,2),("Boden","A4",320,120),("Klappe","A5",320,220),("Trageriemen (gepolstert)","A6",750,40,2),("Griff oben","A7",160,30),("Laptopfach gepolstert","A8",310,400),("Reißverschlusstasche vorne","A9",300,200)],
         [("Pflanzlich gegerbtes Rindsleder","2,5–3,0 mm"),("Polyester-Garn","1,0 mm"),("Schnallen","30 mm, ×2"),("Brustgurt-Schnalle","20 mm"),("D-Ringe","25 mm, ×4"),("Reißverschluss","30 cm, ×1"),("Schaumstoff","5 mm"),("Füße","15 mm, ×4")],
         ["Rückteil polstern","Laptopfach polstern und einnähen","Vortasche mit Reißverschluss","Seitenteile und Boden einsetzen","Vorder-/Rückteil zusammennähen","Klappe und Verschlüsse","Gepolsterte Trageriemen mit Schnallen","Brustgurt, Griff, Füße","Kanten versiegeln und polieren"]),
        ("Klassischer Rucksack", 3, [("Vorderteil","A1",320,400),("Rückteil","A2",320,400),("Seitenteil","A3",100,400,2),("Boden","A4",320,100),("Klappe","A5",320,220),("Trageriemen","A6",700,30,2),("Griff oben","A7",140,30),("Kordelzug","A8",800,6,2)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Leinengarn","0,8 mm"),("Schnallen","25 mm, ×2"),("D-Ringe","25 mm, ×4"),("Ösen","10 mm, ×4")],
         ["Seitenteile und Boden zusammennähen","Vorder-/Rückteil einsetzen","Ösen oben setzen, Kordelzug einfädeln","Klappe befestigen","Trageriemen mit Schnallen","Griff anbringen","Kanten versiegeln"]),
        ("Trekking-Rucksack", 5, [("Vorderteil","A1",340,500),("Rückteil","A2",340,500),("Seitenteil","A3",140,500,2),("Boden","A4",340,140),("Deckplatte","A5",340,240),("Trageriemen","A6",800,40,2),("Hüftgurt","A7",400,60,2),("Brustgurt","A8",300,20),("Seitentaschen","A9",120,200,2),("Griff oben","A10",160,30)],
         [("Pflanzlich gegerbtes Büffelleder","3,0–3,5 mm"),("Leinengarn","1,0 mm"),("Schnallen","40 mm, ×2"),("Steckverschlüsse","30 mm, ×4"),("D-Ringe","30 mm, ×6"),("Füße","18 mm, ×4"),("Schaumstoff","8 mm")],
         ["Rückteil polstern","Seitentaschen vorbereiten","Hauptkörper zusammennähen","Seitentaschen anbringen","Deckplatte mit Verschlüssen","Gepolsterte Trageriemen","Hüftgurt und Brustgurt","Griff und Füße","Alle Kanten versiegeln"]),
        ("Daypack (leicht)", 2, [("Vorderteil","A1",280,360),("Rückteil","A2",280,360),("Seitenteil","A3",80,360,2),("Boden","A4",280,80),("Reißverschluss-Einfassung","A5",280,25,2),("Trageriemen","A6",650,25,2),("Griff","A7",120,25)],
         [("Weiches Rindsleder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","30 cm"),("D-Ringe","20 mm, ×4"),("Karabiner","20 mm, ×2")],
         ["Reißverschluss-Einfassung vorbereiten","Seitenteile und Boden einsetzen","Zusammennähen","Reißverschluss einsetzen","Trageriemen und Griff befestigen","Kanten versiegeln"]),
        ("Roll-Top Rucksack", 3, [("Vorderteil","A1",320,480),("Rückteil","A2",320,480),("Seitenteil","A3",100,400,2),("Boden","A4",320,100),("Rollkante","A5",320,80,2),("Trageriemen","A6",700,30,2),("Griff","A7",140,30),("Schnallenbefestigung","A8",60,40,2)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×2"),("D-Ringe","25 mm, ×4"),("Druckknöpfe","12 mm, ×4")],
         ["Seitenteile und Boden zusammennähen","Vorder-/Rückteil einsetzen","Rollkante oben annähen","Druckknöpfe setzen","Schnallenbefestigung anbringen","Trageriemen mit Schnallen","Griff anbringen","Kanten versiegeln"]),
        ("Sling-Rucksack (ein Riemen)", 2, [("Vorderteil","A1",260,380),("Rückteil","A2",260,380),("Seitenteil","A3",70,380,2),("Boden","A4",260,70),("Sling-Riemen","A5",1200,35),("Reißverschlusstasche","A6",240,160)],
         [("Pflanzlich gegerbtes Leder","1,8–2,0 mm"),("Polyester-Garn","0,8 mm"),("Reißverschluss","30 cm + 20 cm"),("D-Ringe","25 mm, ×2"),("Karabiner","25 mm, ×1")],
         ["Vortasche mit Reißverschluss","Seitenteile und Boden einsetzen","Zusammennähen","Reißverschluss oben","Sling-Riemen befestigen (diagonal)","Kanten versiegeln"]),
        ("Kinderrucksack", 2, [("Vorderteil","A1",220,260),("Rückteil","A2",220,260),("Seitenteil","A3",60,260,2),("Boden","A4",220,60),("Klappe","A5",220,140),("Trageriemen","A6",500,20,2),("Griff","A7",100,20)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","15 mm, ×4"),("Schnallen","15 mm, ×2")],
         ["Seitenteile und Boden zusammennähen","Vorder-/Rückteil einsetzen","Klappe befestigen, Magnet setzen","Trageriemen mit Schnallen","Griff oben anbringen","Kanten versiegeln"]),
        ("Vintage-Rucksack mit Schnallen", 4, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("Seitenteil","A3",110,400,2),("Boden","A4",300,110),("Klappe","A5",300,220),("Schnallenriemen","A6",200,20,2),("Trageriemen","A7",700,30,2),("Griff","A8",140,30),("Vortasche","A9",280,180)],
         [("Pflanzlich gegerbtes Leder (Vintage-Finish)","2,0–2,5 mm"),("Leinengarn","0,8 mm"),("Messing-Schnallen","25 mm, ×4"),("D-Ringe","25 mm, ×4"),("Nieten","12 mm, ×8")],
         ["Vortasche vorbereiten und auf Vorderteil","Seitenteile und Boden zusammennähen","Vorder-/Rückteil einsetzen","Klappe mit Schnallenriemen","Trageriemen und Griff","Alle Nieten setzen","Kanten versiegeln und Vintage-Finish"]),
        ("Rucksack mit Seitentaschen", 3, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("Seitenteil","A3",100,400,2),("Boden","A4",300,100),("Klappe","A5",300,200),("Seitentasche","A6",100,200,2),("Trageriemen","A7",700,30,2),("Griff","A8",140,30)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×2"),("Druckknöpfe","12 mm, ×2"),("D-Ringe","25 mm, ×4")],
         ["Seitentaschen vorbereiten","An Seitenteile nähen","Seitenteile und Boden einsetzen","Vorder-/Rückteil zusammennähen","Klappe befestigen","Trageriemen und Griff","Kanten versiegeln"]),
        ("Rucksack Flap-Style", 3, [("Vorderteil","A1",280,380),("Rückteil","A2",280,440),("Seitenteil","A3",90,380,2),("Boden","A4",280,90),("Trageriemen","A6",700,30,2),("Griff","A7",130,30),("Innenfach","A8",260,300)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×2"),("D-Ringe","25 mm, ×4"),("Druckknopf","15 mm")],
         ["Innenfach auf Rückteil nähen","Seitenteile und Boden einsetzen","Zusammennähen","Rückteil-Klappe umklappen","Schnallen befestigen","Trageriemen und Griff","Kanten versiegeln"]),
        ("Rucksack mit Reißverschluss", 3, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("U-Zwickel","A3",100,900),("Reißverschluss-Einfassung","A4",400,25,2),("Trageriemen","A5",700,30,2),("Griff","A6",140,30)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Reißverschluss","45 cm"),("D-Ringe","25 mm, ×4"),("Schnallen","25 mm, ×2")],
         ["U-Zwickel zuschneiden","Reißverschluss-Einfassung einsetzen","U-Zwickel an Rückteil nähen","Vorderteil einsetzen","Trageriemen und Griff","Kanten versiegeln"]),
        ("Wanderrucksack (30L)", 5, [("Vorderteil","A1",340,480),("Rückteil (gepolstert)","A2",340,480),("Seitenteil","A3",130,480,2),("Boden","A4",340,130),("Deckplatte","A5",340,200),("Trageriemen","A6",800,40,2),("Hüftgurt","A7",400,50,2),("Brustgurt","A8",300,20),("Griff","A9",150,30)],
         [("Pflanzlich gegerbtes Büffelleder","2,5–3,0 mm"),("Leinengarn","1,0 mm"),("Schnallen","35 mm, ×2"),("Steckverschlüsse","25 mm, ×2"),("D-Ringe","30 mm, ×6"),("Schaumstoff","5 mm"),("Füße","15 mm, ×4")],
         ["Rückteil polstern","Seitenteile und Boden einsetzen","Vorder-/Rückteil zusammennähen","Deckplatte mit Verschlüssen","Gepolsterte Trageriemen","Hüftgurt und Brustgurt","Griff und Füße einsetzen","Kanten versiegeln"]),
        ("Fahrradrucksack", 3, [("Vorderteil","A1",280,380),("Rückteil","A2",280,380),("Seitenteil","A3",80,380,2),("Boden","A4",280,80),("Rollkante","A5",280,100),("Trageriemen","A6",700,30,2),("Brustgurt","A7",300,20),("Reflektorstreifen-Halter","A8",40,30,2)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×4"),("D-Ringe","25 mm, ×4"),("Druckknöpfe","12 mm, ×4")],
         ["Seitenteile und Boden einsetzen","Zusammennähen","Rollkante oben","Trageriemen und Brustgurt","Reflektorstreifen-Halter anbringen","Kanten versiegeln"]),
        ("Leder-Canvas-Rucksack", 3, [("Leder-Klappe","A1",300,200),("Leder-Boden","A2",300,100),("Leder-Trageriemen","A3",700,30,2),("Leder-Griff","A4",140,30),("Leder-Verstärkung","A5",300,40,2),("Leder-Schnallenriemen","A6",180,20,2)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Gewachstes Canvas","500g/m²"),("Leinengarn","0,8 mm"),("Messing-Schnallen","25 mm, ×2"),("D-Ringe","25 mm, ×4"),("Nieten","12 mm, ×8")],
         ["Canvas-Körper zuschneiden und nähen","Lederboden an Canvas befestigen","Lederverstärkung oben anbringen","Klappe mit Schnallenriemen","Trageriemen und Griff","Nieten setzen","Kanten versiegeln"]),
        ("Flacher Rucksack (Slim)", 2, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("U-Zwickel (schmal)","A3",40,900),("Trageriemen","A4",650,25,2),("Griff","A5",120,25),("Reißverschluss-Einfassung","A6",350,20,2)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","35 cm"),("D-Ringe","20 mm, ×4"),("Schnallen","20 mm, ×2")],
         ["U-Zwickel zuschneiden","Reißverschluss einsetzen","U-Zwickel an Rückteil","Vorderteil einsetzen","Trageriemen und Griff","Kanten versiegeln"]),
        ("Rucksack mit Außentasche", 3, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("Seitenteil","A3",100,400,2),("Boden","A4",300,100),("Klappe","A5",300,200),("Außentasche","A6",280,200),("Außentasche-Klappe","A7",280,120),("Trageriemen","A8",700,30,2),("Griff","A9",140,30)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×3"),("D-Ringe","25 mm, ×4"),("Magnetverschluss","14 mm")],
         ["Außentasche vorbereiten","Außentasche-Klappe mit Magnet","Außentasche auf Vorderteil nähen","Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Schnallen","Trageriemen und Griff","Kanten versiegeln"]),
        ("Seesack-Rucksack (Duffel)", 3, [("Hauptteil (Zylinder)","A1",600,400),("Boden (rund)","A2",190,190),("Deckel (rund)","A3",190,190),("Trageriemen","A4",700,30,2),("Henkel seitlich","A5",300,25,2),("Kordelzug","A6",800,6,2),("Reißverschluss-Panel","A7",300,60)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Leinengarn","0,8 mm"),("Reißverschluss","30 cm"),("Ösen","10 mm, ×6"),("D-Ringe","25 mm, ×4"),("Schnallen","25 mm, ×2")],
         ["Zylinderform nähen","Boden einsetzen","Reißverschluss-Panel einsetzen","Ösen oben setzen, Kordelzug einfädeln","Deckel anbringen","Trageriemen und Henkel","Kanten versiegeln"]),
        ("Lederrucksack im japanischen Stil", 3, [("Vorderteil","A1",260,380),("Rückteil","A2",260,380),("Seitenteil","A3",80,380,2),("Boden","A4",260,80),("Klappe (lang)","A5",260,280),("Trageriemen","A6",650,25,2),("Griff","A7",120,25),("Lederband-Verschluss","A8",400,10)],
         [("Pflanzlich gegerbtes Leder","1,8–2,0 mm"),("Leinengarn","0,6 mm"),("Holzperle","30 mm, ×1"),("D-Ringe","20 mm, ×4")],
         ["Seitenteile und Boden einsetzen","Zusammennähen","Lange Klappe befestigen","Lederband mit Holzperle","Trageriemen und Griff","Kanten versiegeln"]),
        ("Drawstring-Rucksack", 1, [("Hauptteil","A1",380,440),("Trageriemen-Schlaufe unten","A2",40,40,2),("Zugband-Kanal","A3",380,40),("Kordelzug","A4",1000,6,2)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Ösen","8 mm, ×4"),("Kordelstopper","×2")],
         ["Hauptteil zuschneiden","Schlaufen unten befestigen","Seitennaht schließen","Zugband-Kanal oben","Ösen setzen, Kordelzug einfädeln","Kordel dient als Trageriemen"]),
        ("Rucksack mit Klappe und Kordelzug", 3, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("Seitenteil","A3",90,400,2),("Boden","A4",300,90),("Klappe","A5",300,180),("Zugband-Kanal","A6",300,40),("Kordelzug","A7",800,6,2),("Trageriemen","A8",700,30,2),("Griff","A9",130,30)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×2"),("D-Ringe","25 mm, ×4"),("Ösen","10 mm, ×4")],
         ["Seitenteile und Boden einsetzen","Zusammennähen","Zugband-Kanal, Ösen und Kordelzug","Klappe mit Schnallen","Trageriemen und Griff","Kanten versiegeln"]),
        ("Rucksack mit Frontreißverschluss", 3, [("Vorderteil","A1",300,400),("Rückteil","A2",300,400),("Seitenteil","A3",90,400,2),("Boden","A4",300,90),("Reißverschluss-Panel","A5",300,400),("Trageriemen","A6",700,30,2),("Griff","A7",140,30)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Reißverschluss","50 cm"),("D-Ringe","25 mm, ×4"),("Schnallen","25 mm, ×2")],
         ["Reißverschluss in Vorderteil einsetzen","Seitenteile und Boden einsetzen","Zusammennähen","Trageriemen und Griff","Kanten versiegeln"]),
        ("Rucksack mit Laptopfach (13 Zoll)", 3, [("Vorderteil","A1",280,380),("Rückteil","A2",280,380),("Seitenteil","A3",80,380,2),("Boden","A4",280,80),("Klappe","A5",280,180),("Trageriemen","A6",680,30,2),("Griff","A7",130,25),("Laptopfach gepolstert","A8",270,340)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×2"),("D-Ringe","25 mm, ×4"),("Schaumstoff","3 mm"),("Magnetverschluss","18 mm")],
         ["Laptopfach mit Schaumstoff polstern","Auf Rückteil nähen","Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Magnet","Trageriemen und Griff","Kanten versiegeln"]),
        ("Rucksack-Tasche Hybrid", 3, [("Vorderteil","A1",300,380),("Rückteil","A2",300,380),("Seitenteil","A3",80,380,2),("Boden","A4",300,80),("Klappe","A5",300,180),("Abnehmbare Trageriemen","A6",700,30,2),("Henkel oben","A7",350,30,2),("Griff","A8",130,30)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","25 mm, ×2"),("Karabiner","25 mm, ×4"),("D-Ringe","25 mm, ×4"),("Magnetverschluss","18 mm")],
         ["Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Magnet","D-Ringe seitlich für Henkel","Abnehmbare Trageriemen mit Karabinern","Griff oben befestigen","Kanten versiegeln"]),
    ]),
    ("Geldbörsen und Kartenetuis", "💳", [
        ("Einfaches Kartenetui", 1, [("Außenteil","A1",100,70),("Innenteil","A2",95,65),("Kartenfach","A3",90,40,3)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn, gewachst","0,6 mm"),("Druckknopf","12 mm, Messing")],
         ["Alle Teile zuschneiden und Kanten abrunden","Kartenfächer auf Innenteil kleben und heften","Außen- und Innenteil zusammennähen (Sattlernaht)","Kanten mit Tokonole versiegeln und polieren"]),
        ("Slim Kartenetui", 1, [("Außenteil","A1",100,70),("Mittelteil","A2",95,65),("Kartenfach","A3",90,35,2)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Leinengarn","0,4 mm")],
         ["Teile zuschneiden","Kartenfächer auf Mittelteil nähen","Außenteil umfalten und nähen","Kanten versiegeln"]),
        ("Klassische Geldbörse (zweifach)", 2, [("Außenteil","A1",200,100),("Innenteil","A2",195,95),("Kartenfach","A3",90,60,4),("Scheinfach","A4",190,85),("Münzfach Klappe","A5",90,50)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,6 mm"),("Druckknopf","10 mm"),("Münzrahmen","9 cm, ×1")],
         ["Kartenfächer auf Innenteil stufeln und nähen","Scheinfach einsetzen","Münzfach mit Klappe und Druckknopf","Außen- und Innenteil zusammennähen","Mittelfalte anbringen","Kanten versiegeln"]),
        ("Dreifach-Geldbörse", 3, [("Außenteil","A1",280,100),("Innenteil links","A2",90,95),("Innenteil rechts","A3",90,95),("Kartenfach","A4",85,55,6),("Scheinfach","A5",85,90,2),("Münzfach mit Reißverschluss","A6",85,60)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","8 cm"),("Druckknopf","10 mm")],
         ["Kartenfächer stufeln und nähen","Scheinfächer einsetzen","Münzfach mit Reißverschluss vorbereiten","Innenteile zusammennähen","Außenteil umfalten und befestigen","Druckknopf setzen","Kanten versiegeln"]),
        ("Geldbörse mit Reißverschluss rundum", 2, [("Außenteil","A1",210,110),("Innenteil","A2",200,100),("Kartenfach","A3",95,55,4),("Scheinfach","A4",195,90),("Münzfach","A5",195,50)],
         [("Chromgegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","25 cm")],
         ["Reißverschluss an Außenteil nähen","Kartenfächer stufeln","Scheinfach und Münzfach einsetzen","Innenteil einsetzen und fixieren","Kanten versiegeln"]),
        ("Münzbörse mit Rahmenverschluss", 1, [("Hauptteil","A1",100,80,2),("Futter","A2",95,75,2)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Rahmenverschluss (Clip)","8 cm")],
         ["Außen- und Futterteile zusammennähen","Durch Öffnung wenden","Rahmen einnähen (von Hand)","Kanten versiegeln"]),
        ("Münzbörse mit Druckknopf", 1, [("Hauptteil","A1",90,90),("Klappe","A2",90,50)],
         [("Lederreste","1,0–1,5 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","12 mm")],
         ["Hauptteil falten","Seiten nähen","Klappe befestigen","Druckknopf setzen","Kanten versiegeln"]),
        ("Reisepasshülle", 1, [("Außenteil","A1",140,105),("Steckfach links","A2",65,100),("Steckfach rechts","A3",65,100),("Kartenfach","A4",60,45,2)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm")],
         ["Kartenfächer auf Steckfach rechts nähen","Steckfächer links und rechts positionieren","Außenteil umfalten, Steckfächer einnähen","Kanten versiegeln und polieren"]),
        ("Reisepasshülle mit Boarding-Pass-Fach", 2, [("Außenteil","A1",200,105),("Steckfach links","A2",65,100),("Steckfach rechts","A3",65,100),("Kartenfach","A4",60,45,2),("Boarding-Pass-Fach","A5",130,100)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Gummiband","15 cm")],
         ["Kartenfächer nähen","Boarding-Pass-Fach vorbereiten","Steckfächer einsetzen","Gummiband als Verschluss","Kanten versiegeln"]),
        ("Geldbörse lang (Damen)", 2, [("Außenteil","A1",200,110),("Innenteil","A2",195,105),("Kartenfach","A3",90,50,8),("Scheinfach","A4",190,100),("Münzfach mit Reißverschluss","A5",190,60),("Handyfach","A6",80,140)],
         [("Chromgegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","18 cm"),("Druckknopf","10 mm")],
         ["Kartenfächer stufeln und nähen","Münzfach mit Reißverschluss","Handyfach einsetzen","Scheinfach einsetzen","Innen- und Außenteil zusammennähen","Druckknopf setzen","Kanten versiegeln"]),
        ("Mini-Geldbörse", 1, [("Außenteil","A1",120,80),("Kartenfach","A2",55,35,2),("Scheinfach","A3",115,70)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Leinengarn","0,4 mm"),("Druckknopf","10 mm")],
         ["Kartenfächer auf Innenseite nähen","Scheinfach einsetzen","Außenteil falten und nähen","Druckknopf setzen","Kanten versiegeln"]),
        ("Geldklammer (Money Clip)", 1, [("Außenteil","A1",90,70),("Innenteil","A2",85,65),("Kartenfach","A3",80,35,2)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Geldklammer (Metall)","×1")],
         ["Kartenfächer auf Innenteil nähen","Geldklammer einsetzen","Außen-/Innenteil zusammennähen","Kanten versiegeln"]),
        ("RFID-Kartenetui", 1, [("Außenteil","A1",105,75),("Innenteil","A2",100,70),("Kartenfach","A3",95,40,3),("RFID-Schutzfolie","A4",100,70)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("RFID-Schutzfolie","×1")],
         ["RFID-Folie zwischen Außen- und Innenteil","Kartenfächer stufeln","Zusammennähen","Kanten versiegeln"]),
        ("Ausweishülle", 1, [("Außenteil","A1",110,80),("Klarsichtfenster","A2",85,55),("Steckfach","A3",55,75)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Klarsichtfolie","85×55 mm")],
         ["Klarsichtfenster in Außenteil einsetzen","Steckfach auf Innenseite nähen","Zusammennähen","Kanten versiegeln"]),
        ("Visitenkartenetui", 1, [("Außenteil","A1",100,65),("Klappe","A2",100,40),("Innenteil","A3",95,60)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Magnetverschluss","10 mm")],
         ["Innenteil auf Außenteil nähen","Klappe befestigen","Magnetverschluss setzen","Kanten versiegeln"]),
        ("Akkordeon-Geldbörse", 3, [("Außenteil","A1",200,100),("Akkordeon-Falten","A2",195,90,4),("Kartenfach","A3",90,50,4),("Reißverschluss-Einfassung","A4",200,15,2)],
         [("Chromgegerbtes Leder","0,6–0,8 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","20 cm")],
         ["Akkordeon-Falten vorbereiten","Kartenfächer einsetzen","Falten zusammennähen","Reißverschluss rundum einsetzen","Außenteil befestigen","Kanten versiegeln"]),
        ("Geldbörse mit Kette", 2, [("Außenteil","A1",200,100),("Innenteil","A2",195,95),("Kartenfach","A3",90,55,4),("Scheinfach","A4",190,85),("Ketten-Schlaufe","A5",40,30)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Kette mit Karabiner","40 cm"),("D-Ring","20 mm")],
         ["Kartenfächer stufeln","Scheinfach einsetzen","Innen-/Außenteil zusammennähen","Ketten-Schlaufe mit D-Ring anbringen","Kante an Kante befestigen","Kanten versiegeln"]),
        ("Portemonnaie mit Reißverschluss (Herren)", 2, [("Außenteil","A1",200,110),("Innenteil","A2",195,105),("Kartenfach","A3",90,55,4),("Scheinfach","A4",190,95),("Münzfach","A5",190,50)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","20 cm")],
         ["Reißverschluss an Außenteil","Kartenfächer stufeln","Scheinfach und Münzfach einsetzen","Innenteil fixieren","Kanten versiegeln"]),
        ("Kartenhülle vertikal", 1, [("Außenteil","A1",70,100),("Kartenfach","A2",65,45,3)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Leinengarn","0,4 mm")],
         ["Kartenfächer stufeln","Auf Innenseite nähen","Außenteil falten und nähen","Kanten versiegeln"]),
        ("Geldbörse mit Fotorahmen", 2, [("Außenteil","A1",200,100),("Innenteil","A2",195,95),("Kartenfach","A3",90,55,4),("Scheinfach","A4",190,85),("Fotofenster","A5",80,60),("Klarsichtfolie","A6",75,55)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,6 mm"),("Klarsichtfolie","×1"),("Druckknopf","10 mm")],
         ["Kartenfächer stufeln","Fotofenster ausschneiden und Folie einsetzen","Scheinfach einsetzen","Innen-/Außenteil zusammennähen","Druckknopf setzen","Kanten versiegeln"]),
        ("Geldbörse im Envelope-Stil", 2, [("Hauptteil","A1",240,100),("Kartenfach","A2",90,55,4),("Scheinfach","A3",110,90)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","10 mm")],
         ["Kartenfächer auf Innenseite","Scheinfach einsetzen","Hauptteil in 3 Teile falten","Seiten nähen","Klappe mit Druckknopf","Kanten versiegeln"]),
        ("Schlüsseletui mit Kartenfach", 2, [("Außenteil","A1",110,70),("Innenteil","A2",105,65),("Schlüsselhalter-Streifen","A3",100,15),("Kartenfach","A4",50,60)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Druckknöpfe","10 mm, ×2"),("Schlüsselring","25 mm"),("Niet","9 mm")],
         ["Schlüsselhalter mit Ring und Niet vorbereiten","Kartenfach auf Innenteil nähen","Schlüsselhalter auf Innenteil","Außen-/Innenteil zusammennähen","Druckknöpfe setzen","Kanten versiegeln"]),
        ("Scheckbuchhülle", 2, [("Außenteil","A1",180,90),("Steckfach links","A2",60,85),("Steckfach rechts","A3",60,85),("Stiftehalter","A4",20,85)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm")],
         ["Steckfächer positionieren","Stiftehalter-Schlaufe nähen","Alles zusammennähen","Kanten versiegeln"]),
        ("Geldbörse zweifarbig", 2, [("Außenteil (Farbe 1)","A1",200,100),("Innenteil (Farbe 2)","A2",195,95),("Kartenfach","A3",90,55,4),("Scheinfach","A4",190,85)],
         [("Leder Farbe 1","1,0–1,2 mm"),("Leder Farbe 2","1,0–1,2 mm"),("Kontrastgarn","0,6 mm"),("Druckknopf","10 mm")],
         ["Kartenfächer (Farbe 2) auf Innenteil","Scheinfach einsetzen","Außen-/Innenteil zusammennähen mit Kontrastgarn","Druckknopf setzen","Kanten versiegeln"]),
        ("Zip-Around Clutch Wallet", 3, [("Außenteil","A1",220,120),("Innenteil","A2",215,115),("Kartenfach","A3",100,55,6),("Scheinfach","A4",210,100,2),("Münzfach mit Reißverschluss","A5",210,55),("Handyfach","A6",85,150)],
         [("Chromgegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss rundum","30 cm"),("Reißverschluss Münzfach","18 cm"),("Handschlaufe","×1")],
         ["Kartenfächer stufeln","Scheinfächer und Münzfach vorbereiten","Handyfach einsetzen","Reißverschluss rundum einsetzen","Handschlaufe anbringen","Kanten versiegeln"]),
        ("Kreditkarten-Organizer", 2, [("Außenteil","A1",110,80),("Kartenfach","A2",100,40,6),("Trennwand","A3",105,75,2)],
         [("Pflanzlich gegerbtes Leder","0,6–0,8 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","10 mm")],
         ["Kartenfächer auf Trennwände stufeln","Trennwände zusammennähen","Außenteil umfalten und befestigen","Druckknopf setzen","Kanten versiegeln"]),
        ("Front-Pocket-Geldbörse", 1, [("Außenteil","A1",110,80),("Kartenfach","A2",100,40,3),("Geldscheinfach","A3",105,70)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Leinengarn","0,4 mm")],
         ["Kartenfächer stufeln","Geldscheinfach einsetzen","Zusammennähen","Kanten versiegeln"]),
        ("Münzbeutel mit Kordelzug", 1, [("Hauptteil (rund)","A1",120,120),("Kordelzugband","A2",300,5)],
         [("Weiches Leder","0,8–1,0 mm"),("Leinengarn","0,4 mm"),("Ösen","5 mm, ×6")],
         ["Runde Form zuschneiden","Ösen am Rand setzen","Kordelzug einfädeln","Kanten ölen"]),
        ("Geldbörse mit Gürtelschlaufe", 2, [("Außenteil","A1",200,100),("Innenteil","A2",195,95),("Kartenfach","A3",90,55,4),("Scheinfach","A4",190,85),("Gürtelschlaufe","A5",80,40)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Druckknopf","12 mm"),("Druckknopf Schlaufe","10 mm")],
         ["Kartenfächer stufeln und nähen","Scheinfach einsetzen","Gürtelschlaufe auf Rückteil","Innen-/Außenteil zusammennähen","Druckknopf setzen","Kanten versiegeln"]),
        ("Kartenetui mit Zugband", 1, [("Außenteil","A1",100,70),("Innenteil","A2",95,65),("Zugband","A3",120,8)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Leinengarn","0,4 mm"),("Perle/Stopper","×1")],
         ["Innenteil auf Außenteil nähen","Karten-Schlitz einschneiden","Zugband befestigen","Zusammennähen","Kanten versiegeln"]),
    ]),
    ("Umhängetaschen und Crossbody", "📦", [
        ("Einfache Crossbody-Tasche", 2, [("Vorderteil","A1",220,170),("Rückteil","A2",220,170),("Klappe","A3",220,120),("Seitenzwickel","A4",40,170,2),("Boden","A5",220,40),("Schulterriemen","A6",1200,20)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","20 mm, ×2"),("Karabiner","20 mm, ×2")],
         ["Seitenteile und Boden an Rückteil","Vorderteil annähen","Klappe befestigen, Magnet setzen","Riemen anfertigen","D-Ringe und Karabiner","Kanten versiegeln"]),
        ("Satteltasche (Saddle Bag)", 3, [("Vorderteil","A1",240,200),("Rückteil","A2",240,200),("Klappe (halbrund)","A3",240,160),("Seitenzwickel","A4",60,200,2),("Boden","A5",240,60),("Schulterriemen","A6",1200,25),("Innentasche","A7",220,120)],
         [("Pflanzlich gegerbtes Leder","1,8–2,2 mm"),("Leinengarn","0,8 mm"),("Drehverschluss","×1"),("D-Ringe","25 mm, ×2"),("Karabiner","25 mm, ×2")],
         ["Innentasche aufnähen","Seitenteile und Boden einsetzen","Vorder-/Rückteil zusammennähen","Halbrunde Klappe befestigen","Drehverschluss setzen","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Messenger-Tasche", 3, [("Vorderteil","A1",360,260),("Rückteil","A2",360,260),("Klappe","A3",360,200),("Seitenzwickel","A4",80,260,2),("Boden","A5",360,80),("Schulterriemen","A6",1300,30),("Steckfach vorne","A7",340,160),("Reißverschlusstasche hinten","A8",340,200)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Steckverschluss","×2"),("D-Ringe","25 mm, ×2"),("Karabiner","25 mm, ×2"),("Reißverschluss","30 cm")],
         ["Steckfach und Reißverschlusstasche vorbereiten","Seitenteile und Boden einsetzen","Vorder-/Rückteil zusammennähen","Klappe mit Steckverschlüssen","Schulterriemen mit D-Ringen","Kanten versiegeln"]),
        ("Mini-Crossbody-Tasche", 1, [("Vorderteil","A1",160,120),("Rückteil","A2",160,120),("Klappe","A3",160,80),("Schulterriemen","A4",1200,15)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,4 mm"),("Magnetverschluss","10 mm"),("D-Ringe","15 mm, ×2")],
         ["Vorder-/Rückteil zusammennähen","Klappe befestigen, Magnet setzen","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Handytasche zum Umhängen", 1, [("Vorderteil","A1",90,170),("Rückteil","A2",90,170),("Klappe","A3",90,60),("Schulterriemen","A4",1300,12)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Magnetverschluss","10 mm"),("D-Ringe","12 mm, ×2")],
         ["Vorder-/Rückteil zusammennähen (3 Seiten)","Klappe befestigen, Magnet setzen","Riemen mit D-Ringen befestigen","Kanten versiegeln"]),
        ("Sling-Tasche (Brusttasche)", 2, [("Vorderteil","A1",200,300),("Rückteil","A2",200,300),("Seitenteil","A3",50,300,2),("Schulterriemen","A4",1100,25),("Reißverschlusstasche vorne","A5",180,150)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","25 cm + 20 cm"),("D-Ringe","25 mm, ×2"),("Schnalle","25 mm")],
         ["Vortasche mit Reißverschluss","Seitenteile einsetzen","Zusammennähen","Reißverschluss oben","Sling-Riemen (diagonal)","Kanten versiegeln"]),
        ("Umhängetasche mit Quaste", 2, [("Vorderteil","A1",240,180),("Rückteil","A2",240,180),("Klappe","A3",240,130),("Seitenzwickel","A4",50,180,2),("Boden","A5",240,50),("Schulterriemen","A6",1200,20),("Quaste","A7",60,100)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Drehverschluss","×1"),("D-Ringe","20 mm, ×2")],
         ["Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Drehverschluss","Quaste anfertigen und befestigen","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Vertikale Crossbody-Tasche", 2, [("Vorderteil","A1",180,260),("Rückteil","A2",180,260),("Klappe","A3",180,140),("Seitenzwickel","A4",40,260,2),("Boden","A5",180,40),("Schulterriemen","A6",1200,20)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","20 mm, ×2"),("Karabiner","20 mm, ×2")],
         ["Seitenteile und Boden an Rückteil","Vorderteil annähen","Klappe befestigen","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Postboten-Tasche", 3, [("Vorderteil","A1",300,220),("Rückteil","A2",300,220),("Klappe (lang)","A3",300,260),("Seitenzwickel","A4",80,220,2),("Boden","A5",300,80),("Schulterriemen","A6",1300,30),("Steckfach","A7",280,140),("Schnallenriemen","A8",120,20,2)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Leinengarn","0,8 mm"),("Schnallen","25 mm, ×2"),("D-Ringe","25 mm, ×2"),("Nieten","9 mm, ×6")],
         ["Steckfach auf Vorderteil","Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Schnallenriemen","Schulterriemen mit D-Ringen","Kanten versiegeln"]),
        ("Halbmond-Tasche (Crescent)", 2, [("Vorderteil (halbrund)","A1",300,180),("Rückteil (halbrund)","A2",300,180),("Seitenzwickel","A3",50,260),("Reißverschluss-Einfassung","A4",300,20,2),("Schulterriemen","A5",1200,20)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","30 cm"),("D-Ringe","20 mm, ×2")],
         ["Halbmond-Form zuschneiden","Reißverschluss-Einfassung vorbereiten","Seitenzwickel einsetzen","Zusammennähen","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Barrel-Tasche (Fass-Form)", 2, [("Hauptteil (Zylinder)","A1",400,220),("Seitenteil (rund)","A2",140,140,2),("Reißverschluss-Panel","A3",400,50),("Schulterriemen","A4",1200,25)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","35 cm"),("D-Ringe","25 mm, ×2")],
         ["Zylinderform nähen","Reißverschluss-Panel einsetzen","Runde Seitenteile einsetzen","Riemen befestigen","Kanten versiegeln"]),
        ("Umhängetasche mit Fransen", 2, [("Vorderteil","A1",260,200),("Rückteil","A2",260,200),("Klappe mit Fransen","A3",260,150),("Fransenstreifen","A4",240,80),("Schulterriemen","A5",1200,20)],
         [("Weiches Wildleder","1,0–1,4 mm"),("Baumwollgarn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","20 mm, ×2")],
         ["Fransen in 5mm-Streifen schneiden","Fransenstreifen an Klappe nähen","Zusammennähen","Klappe befestigen","Riemen anbringen","Kanten ölen"]),
        ("Flache Dokumententasche", 2, [("Vorderteil","A1",360,280),("Rückteil","A2",360,280),("Klappe","A3",360,160),("Schulterriemen","A4",1300,25),("Stiftschlaufe","A5",20,80)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","18 mm, ×2"),("D-Ringe","25 mm, ×2")],
         ["Stiftschlaufe auf Innenseite nähen","Vorder-/Rückteil zusammennähen (3 Seiten)","Klappe mit Magneten","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Crossbody-Tasche mit Kartenfächern", 2, [("Vorderteil","A1",200,140),("Rückteil","A2",200,140),("Klappe","A3",200,100),("Kartenfach außen","A4",90,50,3),("Seitenzwickel","A5",30,140,2),("Schulterriemen","A6",1200,18)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,4 mm"),("Magnetverschluss","12 mm"),("D-Ringe","18 mm, ×2")],
         ["Kartenfächer auf Rückteil stufeln","Seitenzwickel einsetzen","Zusammennähen","Klappe mit Magnet","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Convertible Crossbody/Clutch", 3, [("Vorderteil","A1",260,170),("Rückteil","A2",260,170),("Klappe","A3",260,120),("Seitenzwickel","A4",40,170,2),("Boden","A5",260,40),("Abnehmbarer Riemen","A6",1200,20),("Handschlaufe","A7",200,15)],
         [("Chromgegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Drehverschluss","×1"),("D-Ringe","20 mm, ×2"),("Karabiner","20 mm, ×2")],
         ["Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Drehverschluss","Handschlaufe befestigen","Abnehmbarer Riemen mit Karabinern","Kanten versiegeln"]),
        ("Kuriertasche (Courier)", 3, [("Vorderteil","A1",380,280),("Rückteil","A2",380,280),("Klappe","A3",380,220),("Seitenzwickel","A4",80,280,2),("Boden","A5",380,80),("Schulterriemen","A6",1300,35),("Steckfach vorne","A7",360,160),("Reißverschlusstasche innen","A8",340,180)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Leinengarn","0,8 mm"),("Steckverschluss","×2"),("Schnallen","30 mm, ×2"),("D-Ringe","30 mm, ×2"),("Reißverschluss","30 cm")],
         ["Steckfach und Reißverschlusstasche vorbereiten","Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Steckverschlüssen","Schulterriemen mit D-Ringen","Kanten versiegeln"]),
        ("Reporter-Tasche", 2, [("Vorderteil","A1",240,200),("Rückteil","A2",240,200),("Klappe","A3",240,130),("Seitenzwickel","A4",50,200,2),("Boden","A5",240,50),("Schulterriemen","A6",1200,25),("Vortasche","A7",220,120)],
         [("Pflanzlich gegerbtes Leder","1,8–2,0 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","25 mm, ×2"),("Druckknopf","12 mm")],
         ["Vortasche auf Vorderteil nähen","Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Magnet","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Umhängetasche mit 2 Fächern", 3, [("Vorderteil","A1",240,180),("Trennwand","A2",240,180),("Rückteil","A3",240,180),("Klappe","A4",240,130),("Seitenzwickel","A5",70,180,2),("Boden","A6",240,70),("Schulterriemen","A7",1200,25)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","20 mm, ×2"),("Reißverschluss","20 cm")],
         ["Trennwand mit Reißverschlusstasche","Seitenteile und Boden einsetzen","Vorder-/Trennwand/Rückteil zusammennähen","Klappe mit Magnet","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Sattel-Crossbody klein", 2, [("Vorderteil","A1",180,150),("Rückteil","A2",180,150),("Halbrunde Klappe","A3",180,120),("Seitenzwickel","A4",40,150,2),("Schulterriemen","A5",1200,15)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,4 mm"),("Drehverschluss","×1"),("D-Ringe","15 mm, ×2")],
         ["Seitenzwickel einsetzen","Vorder-/Rückteil zusammennähen","Halbrunde Klappe befestigen","Drehverschluss setzen","Riemen mit D-Ringen","Kanten versiegeln"]),
        ("Tabak-/Zippo-Beutel", 1, [("Hauptteil","A1",150,120),("Klappe","A2",150,70),("Innentasche","A3",140,60)],
         [("Weiches Rindsleder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","12 mm")],
         ["Innentasche aufnähen","Seiten zusammennähen","Klappe befestigen","Druckknopf setzen","Kanten versiegeln"]),
        ("Crossbody mit Klappe und Reißverschluss", 3, [("Vorderteil","A1",230,180),("Rückteil","A2",230,180),("Klappe","A3",230,140),("Seitenzwickel","A4",50,180,2),("Boden","A5",230,50),("Reißverschluss-Panel innen","A6",220,30),("Schulterriemen","A7",1200,20)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("Reißverschluss","20 cm"),("D-Ringe","20 mm, ×2"),("Karabiner","20 mm, ×2")],
         ["Reißverschluss-Panel innen vorbereiten","Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Magnet","Riemen mit D-Ringen und Karabinern","Kanten versiegeln"]),
        ("Umhängetasche mit Flechtriemen", 3, [("Vorderteil","A1",240,180),("Rückteil","A2",240,180),("Klappe","A3",240,130),("Seitenzwickel","A4",50,180,2),("Boden","A5",240,50),("Flechtriemen-Streifen","A6",1300,8,3)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","20 mm, ×2"),("Karabiner","20 mm, ×2")],
         ["Seitenteile und Boden einsetzen","Zusammennähen","Klappe mit Magnet","3 Streifen zu Riemen flechten","Riemen mit D-Ringen befestigen","Kanten versiegeln"]),
        ("Crossbody-Tasche Boho-Stil", 2, [("Hauptteil (rund/oval)","A1",220,220),("Rückteil (rund/oval)","A2",220,220),("Seitenzwickel","A3",50,350),("Klappe (halbrund)","A4",220,130),("Schulterriemen","A5",1200,20),("Fransen-Anhänger","A6",40,80)],
         [("Weiches Wildleder","1,0–1,4 mm"),("Baumwollgarn","0,6 mm"),("Magnetverschluss","12 mm"),("D-Ringe","20 mm, ×2")],
         ["Rundform zuschneiden","Seitenzwickel einsetzen","Zusammennähen","Halbrunde Klappe befestigen","Fransen-Anhänger anbringen","Riemen mit D-Ringen","Kanten ölen"]),
        ("Gürteltasche zum Umhängen", 2, [("Vorderteil","A1",240,140),("Rückteil","A2",240,140),("Klappe","A3",240,90),("Seitenzwickel","A4",40,140,2),("Abnehmbarer Riemen","A5",1200,20),("Gürtelschlaufe","A6",80,40,2)],
         [("Pflanzlich gegerbtes Leder","1,5–1,8 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm"),("D-Ringe","20 mm, ×2"),("Karabiner","20 mm, ×2")],
         ["Seitenzwickel einsetzen","Zusammennähen","Klappe mit Magnet","Gürtelschlaufen auf Rückteil","Abnehmbarer Riemen mit Karabinern","Kanten versiegeln"]),
        ("Umhängetasche mit Außentasche", 3, [("Vorderteil","A1",260,200),("Rückteil","A2",260,200),("Klappe","A3",260,140),("Seitenzwickel","A4",50,200,2),("Boden","A5",260,50),("Außentasche vorne","A6",240,120),("Außentasche-Klappe","A7",240,80),("Schulterriemen","A8",1200,25)],
         [("Pflanzlich gegerbtes Leder","1,8–2,0 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm, ×2"),("D-Ringe","25 mm, ×2"),("Karabiner","25 mm, ×2")],
         ["Außentasche mit Klappe vorbereiten","Auf Vorderteil nähen","Seitenteile und Boden einsetzen","Zusammennähen","Hauptklappe mit Magnet","Riemen mit D-Ringen","Kanten versiegeln"]),
    ]),
    ("Reise und Weekender", "✈️", [
        ("Weekender-Tasche klassisch", 4, [("Vorderteil","A1",500,300),("Rückteil","A2",500,300),("Boden","A3",500,180),("Seitenteil (halbrund)","A4",180,300,2),("Reißverschluss-Panel","A5",500,50,2),("Henkel","A6",400,30,2),("Schulterriemen","A7",1300,30),("Innentasche","A8",300,200)],
         [("Pflanzlich gegerbtes Rindsleder","2,5–3,0 mm"),("Leinengarn","1,0 mm"),("Reißverschluss","55 cm"),("D-Ringe","30 mm, ×2"),("Nieten","12 mm, ×10"),("Füße","15 mm, ×4")],
         ["Innentasche vorbereiten","Reißverschluss-Panels an Vorder-/Rückteil","Seitenteile und Boden einsetzen","Zusammennähen","Reißverschluss einsetzen","Henkel und Schulterriemen befestigen","Füße einsetzen","Kanten versiegeln und polieren"]),
        ("Sporttasche", 3, [("Hauptteil (Zylinder)","A1",600,360),("Seitenteil (rund)","A2",200,200,2),("Reißverschluss-Panel","A3",600,50),("Henkel","A4",350,30,2),("Schulterriemen","A5",1300,30),("Schuhfach","A6",200,180)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","1,0 mm"),("Reißverschluss","60 cm + 20 cm"),("D-Ringe","30 mm, ×2"),("Nieten","12 mm, ×8"),("Füße","15 mm, ×4")],
         ["Schuhfach mit Reißverschluss vorbereiten","Zylinderform nähen","Reißverschluss-Panel einsetzen","Runde Seitenteile einsetzen","Henkel und Riemen befestigen","Füße einsetzen","Kanten versiegeln"]),
        ("Kulturbeutel (Dopp Kit)", 2, [("Hauptteil","A1",280,180),("Seitenteil","A2",120,120,2),("Reißverschluss-Einfassung","A3",280,25,2),("Henkel","A4",100,20)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","25 cm"),("Nieten","7 mm, ×2")],
         ["Reißverschluss oben einnähen","Seitenteile einsetzen","Zusammennähen","Henkel mit Nieten befestigen","Kanten versiegeln"]),
        ("Kulturbeutel zum Aufhängen", 3, [("Hauptteil","A1",300,400),("Innentasche","A2",280,120,3),("Reißverschlusstasche","A3",280,150),("Aufhängehaken","A4",60,120),("Binderiemen","A5",200,15)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Reißverschlüsse","20 cm, ×2"),("Druckknopf","12 mm"),("Haken","×1")],
         ["Innentaschen auf Hauptteil nähen","Reißverschlusstaschen einsetzen","Aufhängehaken befestigen","Hauptteil falten und Seiten nähen","Binderiemen mit Druckknopf","Kanten versiegeln"]),
        ("Kleidersack", 4, [("Hauptteil (lang)","A1",600,1000),("Henkelschlaufe","A2",120,30),("Reißverschluss-Einfassung","A3",600,25,2),("Innentasche","A4",400,250),("Klettverschluss-Fach","A5",300,200)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","100 cm"),("Kleiderbügel-Loch-Verstärkung","×1"),("Klettverschluss","×1")],
         ["Innentaschen auf Hauptteil nähen","Reißverschluss-Einfassung vorbereiten","Hauptteil falten","Reißverschluss einsetzen","Henkelschlaufe oben befestigen","Bügelloch verstärken","Kanten versiegeln"]),
        ("Schuhbeutel (Reise)", 1, [("Hauptteil","A1",350,280),("Kordelzugband","A2",600,6),("Trennwand","A3",340,140)],
         [("Weiches Leder","1,0–1,2 mm"),("Leinengarn","0,4 mm"),("Ösen","8 mm, ×4")],
         ["Trennwand in die Mitte nähen","Hauptteil falten, Seitennaht","Ösen oben setzen","Kordelzug einfädeln","Kanten ölen"]),
        ("Kofferanhänger", 1, [("Außenteil","A1",90,55),("Innenteil","A2",85,50),("Sichtfenster-Rahmen","A3",80,45),("Riemen","A4",160,15)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,4 mm"),("Klarsichtfolie","×1"),("Schnalle","15 mm")],
         ["Sichtfenster ausschneiden und Folie einsetzen","Innen-/Außenteil zusammennähen","Riemen mit Schnalle anfertigen","Kanten versiegeln"]),
        ("Reise-Organizer", 2, [("Außenteil","A1",260,180),("Fächer","A2",250,80,3),("Reißverschlusstasche","A3",240,120),("Stiftschlaufe","A4",20,80),("Gummiband-Halterung","A5",240,30)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Reißverschluss","20 cm"),("Gummiband","×4"),("Druckknopf","12 mm")],
         ["Fächer auf Innenseite nähen","Reißverschlusstasche einsetzen","Stiftschlaufe und Gummiband-Halterung","Außenteil umfalten und Seiten nähen","Druckknopf setzen","Kanten versiegeln"]),
        ("Passport-Wallet (Reise)", 2, [("Außenteil","A1",240,120),("Passfach","A2",65,110),("Kartenfach","A3",60,55,4),("Boarding-Pass-Fach","A4",230,110),("Stiftschlaufe","A5",20,80),("Gummiband","A6",200,5)],
         [("Pflanzlich gegerbtes Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Gummiband","×1"),("Druckknopf","10 mm")],
         ["Kartenfächer stufeln","Passfach einsetzen","Boarding-Pass-Fach einsetzen","Stiftschlaufe nähen","Außenteil falten und zusammennähen","Gummiband als Verschluss","Kanten versiegeln"]),
        ("Reisetasche mit Rollen", 5, [("Vorderteil","A1",500,340),("Rückteil","A2",500,340),("Boden","A3",500,180),("Seitenteil","A4",180,340,2),("Reißverschluss-Panel","A5",500,50,2),("Henkel","A6",350,30,2),("Teleskopgriff-Verstärkung","A7",100,60),("Rollenverstärkung","A8",80,60,2)],
         [("Pflanzlich gegerbtes Rindsleder","3,0–3,5 mm"),("Leinengarn","1,0 mm"),("Reißverschluss","60 cm"),("Rollen","50 mm, ×2"),("Teleskopgriff","×1"),("Füße","18 mm, ×4"),("Nieten","12 mm, ×12")],
         ["Rollenverstärkungen vorbereiten","Rollen montieren","Teleskopgriff-Verstärkung einsetzen","Reißverschluss-Panels vorbereiten","Seitenteile und Boden einsetzen","Zusammennähen","Henkel befestigen","Füße einsetzen","Kanten versiegeln und polieren"]),
        ("Necessaire (Handgelenk)", 1, [("Hauptteil","A1",220,150),("Reißverschluss-Einfassung","A2",220,20,2),("Handschlaufe","A3",180,15)],
         [("Weiches Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","22 cm"),("D-Ring","15 mm")],
         ["Reißverschluss oben einnähen","Hauptteil falten und Seiten nähen","Handschlaufe mit D-Ring","Kanten versiegeln"]),
        ("Kabel-Organizer (Reise)", 1, [("Hauptteil","A1",260,180),("Gummiband-Halterung","A2",240,30,2),("Reißverschlusstasche","A3",240,100)],
         [("Weiches Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","20 cm"),("Gummiband","×6"),("Druckknopf","12 mm")],
         ["Gummiband-Halterungen auf Innenseite","Reißverschlusstasche einsetzen","Hauptteil falten und Seiten nähen","Druckknopf setzen","Kanten versiegeln"]),
        ("Reise-Schmuckrolle", 2, [("Hauptteil","A1",300,200),("Ringhalter-Polster","A2",280,40),("Ohrringe-Fach","A3",280,60),("Kette-Fach","A4",280,80),("Binderiemen","A5",400,10)],
         [("Weiches Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Wildleder für Polster","×1"),("Druckknöpfe","8 mm, ×3")],
         ["Ringhalter-Polster vorbereiten","Fächer auf Hauptteil nähen","Druckknöpfe für Fachklappen","Binderiemen befestigen","Aufrollen und testen","Kanten versiegeln"]),
        ("Wäschebeutel (Reise)", 1, [("Hauptteil","A1",400,350),("Kordelzugband","A2",700,6),("Verstärkung oben","A3",400,30)],
         [("Weiches Leder","1,0–1,2 mm"),("Leinengarn","0,4 mm"),("Ösen","8 mm, ×4")],
         ["Verstärkung oben umklappen und nähen","Seitennaht schließen","Boden nähen","Ösen setzen, Kordelzug einfädeln","Kanten ölen"]),
        ("Medikamententasche (Reise)", 1, [("Hauptteil","A1",200,140),("Fächer","A2",90,60,3),("Reißverschluss-Einfassung","A3",200,20,2)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","20 cm")],
         ["Fächer auf Innenseite nähen","Reißverschluss oben einnähen","Hauptteil falten und Seiten nähen","Kanten versiegeln"]),
        ("Flachmann-Hülle", 1, [("Hauptteil","A1",130,160),("Schlaufe","A2",30,40)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Leinengarn","0,6 mm"),("Druckknopf","10 mm")],
         ["Hauptteil um Flachmann formen","Seitennaht nähen","Schlaufe oben befestigen","Druckknopf setzen","Kanten versiegeln"]),
        ("Landkarten-/Tablet-Hülle (Reise)", 2, [("Vorderteil","A1",280,210),("Rückteil","A2",280,210),("Klappe","A3",280,100),("Innentasche","A4",260,140)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm"),("Magnetverschluss","14 mm")],
         ["Innentasche auf Rückteil nähen","Vorder-/Rückteil zusammennähen","Klappe befestigen, Magnet setzen","Kanten versiegeln"]),
        ("Handgepäck-Tasche (Under-Seat)", 4, [("Vorderteil","A1",400,280),("Rückteil","A2",400,280),("Boden","A3",400,150),("Seitenteil","A4",150,280,2),("Reißverschluss-Panel","A5",400,50,2),("Henkel","A6",350,30,2),("Trolley-Schlaufe","A7",130,60),("Innentasche","A8",380,200)],
         [("Pflanzlich gegerbtes Rindsleder","2,0–2,5 mm"),("Polyester-Garn","0,8 mm"),("Reißverschluss","45 cm"),("Nieten","9 mm, ×8"),("Füße","12 mm, ×4")],
         ["Innentasche vorbereiten","Reißverschluss-Panels vorbereiten","Seitenteile und Boden einsetzen","Zusammennähen","Reißverschluss einsetzen","Henkel und Trolley-Schlaufe","Füße einsetzen","Kanten versiegeln"]),
        ("Packtasche / Packing Cube", 1, [("Hauptteil","A1",350,250),("Reißverschluss-Einfassung","A2",350,20,2),("Seitenteil","A3",100,250,2)],
         [("Weiches Rindsleder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Reißverschluss","35 cm"),("Henkelschlaufe","40×15 mm")],
         ["Reißverschluss oben einnähen","Seitenteile einsetzen","Zusammennähen","Henkelschlaufe befestigen","Kanten versiegeln"]),
        ("Reise-Etikettenhülle (2er Set)", 1, [("Außenteil","A1",100,65,2),("Innenteil","A2",95,60,2),("Sichtfenster","A3",85,50,2),("Riemen","A4",180,15,2)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,4 mm"),("Klarsichtfolie","×2"),("Schnalle","15 mm, ×2")],
         ["Sichtfenster ausschneiden, Folie einsetzen","Innen-/Außenteil zusammennähen","Riemen mit Schnalle","Kanten versiegeln"]),
    ]),
    ("Accessoires", "🔑", [
        ("Einfacher Schlüsselanhänger", 1, [("Hauptstreifen","A1",120,20),("Schlaufe","A2",40,15)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,6 mm"),("Schlüsselring","25 mm"),("Niet","9 mm")],
         ["Streifen zuschneiden","Um Ring falten","Mit Niet fixieren","Kanten versiegeln und polieren"]),
        ("Schlüsselanhänger mit Karabiner", 1, [("Hauptstreifen","A1",150,20),("Schlaufe","A2",50,20)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,6 mm"),("Karabiner","×1"),("Niet","9 mm")],
         ["Streifen zuschneiden","Um Karabiner falten","Mit Niet fixieren","Kanten versiegeln"]),
        ("Klassischer Gürtel", 2, [("Gürtelstreifen","A1",1100,35),("Schlaufe","A2",50,40),("Spitze","A3",80,35)],
         [("Pflanzlich gegerbtes Rindsleder","3,5–4,0 mm"),("Leinengarn","0,8 mm"),("Dornschließe","35 mm"),("Ovalöse","×1")],
         ["Streifen auf richtige Länge zuschneiden","Löcher stanzen (5 Stück, 25mm Abstand)","Spitze formen und Kanten brechen","Schnalle einsetzen, Schlaufe fixieren","Ovalöse setzen","Kanten versiegeln und polieren"]),
        ("Gürtel mit Doppelschnalle", 3, [("Gürtelstreifen","A1",1100,40),("Schlaufe","A2",55,45,2),("Spitze","A3",90,40)],
         [("Pflanzlich gegerbtes Rindsleder","3,5–4,0 mm"),("Leinengarn","0,8 mm"),("Doppeldornschließe","40 mm"),("Ovalösen","×2")],
         ["Streifen zuschneiden","Doppellöcher stanzen","Spitze formen","Schnalle einsetzen, Schlaufen fixieren","Ovalösen setzen","Kanten versiegeln"]),
        ("Schmaler Gürtel (Damen)", 2, [("Gürtelstreifen","A1",950,20),("Schlaufe","A2",35,25),("Spitze","A3",60,20)],
         [("Pflanzlich gegerbtes Leder","2,5–3,0 mm"),("Polyester-Garn","0,6 mm"),("Dornschließe","20 mm")],
         ["Streifen zuschneiden","Löcher stanzen","Spitze formen","Schnalle einsetzen","Kanten versiegeln"]),
        ("Brillenetui", 1, [("Hauptteil","A1",180,80),("Klappe","A2",180,50)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,6 mm"),("Druckknopf","12 mm"),("Wildleder-Futter","180×80 mm")],
         ["Futter auf Innenseite kleben","Hauptteil falten, Seiten nähen","Klappe befestigen","Druckknopf setzen","Kanten versiegeln"]),
        ("Stiftetui (Einzelstift)", 1, [("Hauptteil","A1",160,50),("Druckknopflasche","A2",30,20)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","10 mm")],
         ["Hauptteil um Stift rollen","Seitennaht nähen","Druckknopflasche befestigen","Kanten versiegeln"]),
        ("Stiftetui (Rollup, 5 Stifte)", 2, [("Hauptteil","A1",250,160),("Stiftfächer","A2",240,40),("Binderiemen","A3",400,8)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Leinengarn","0,6 mm"),("Druckknopf","8 mm")],
         ["Stiftfächer auf Hauptteil nähen","Trennungen nähen (5 Fächer)","Binderiemen befestigen","Kanten versiegeln","Aufrollen und testen"]),
        ("Uhrenrolle (3 Uhren)", 2, [("Hauptteil","A1",300,180),("Uhr-Kissen","A2",90,80,3),("Binderiemen","A3",400,10)],
         [("Weiches Rindsleder","1,2–1,5 mm"),("Polyester-Garn","0,4 mm"),("Schaumstoff für Kissen","×3"),("Druckknopf","10 mm")],
         ["Uhren-Kissen mit Schaumstoff nähen","Kissen auf Hauptteil befestigen","Trennungen markieren","Binderiemen anbringen","Kanten versiegeln","Aufrollen und testen"]),
        ("Untersetzer-Set (4 Stück)", 1, [("Untersetzer (rund)","A1",100,100,4)],
         [("Pflanzlich gegerbtes Leder","3,0–4,0 mm")],
         ["4 runde Formen zuschneiden (100mm Durchmesser)","Kanten brechen und abrunden","Mit Tokonole versiegeln und polieren","Optional: Monogramm prägen"]),
        ("Lesezeichen", 1, [("Hauptteil","A1",200,40),("Spitze (Pfeil)","A2",30,30)],
         [("Lederreste","1,0–1,5 mm"),("Leinengarn","0,4 mm")],
         ["Streifen zuschneiden","Pfeilspitze formen","Optional: Prägung oder Punzierung","Kanten versiegeln"]),
        ("Mousepad", 1, [("Hauptteil","A1",260,220)],
         [("Pflanzlich gegerbtes Leder","2,5–3,0 mm"),("Kork-Unterlage","260×220 mm")],
         ["Form zuschneiden","Kork auf Unterseite kleben","Kanten brechen und abrunden","Oberfläche mit Lederbalsam behandeln"]),
        ("Notizbuchhülle A5", 2, [("Außenteil","A1",340,250),("Steckfach links","A2",80,240),("Steckfach rechts","A3",80,240),("Stiftschlaufe","A4",20,80)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,6 mm")],
         ["Stiftschlaufe auf Innenseite nähen","Steckfächer positionieren und nähen","Außenteil falten","Kanten versiegeln"]),
        ("Notizbuchhülle mit Verschluss", 3, [("Außenteil","A1",350,260),("Steckfach links","A2",80,250),("Steckfach rechts","A3",80,250),("Stiftschlaufe","A4",20,80),("Verschlussriemen","A5",200,15),("Kartenfach","A6",60,50,2)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Leinengarn","0,6 mm"),("Druckknopf","12 mm")],
         ["Kartenfächer auf Steckfach rechts","Stiftschlaufe und Steckfächer einsetzen","Verschlussriemen befestigen","Zusammennähen","Druckknopf setzen","Kanten versiegeln"]),
        ("Armband (Leder)", 1, [("Armband-Streifen","A1",220,20),("Verschlusslasche","A2",40,15)],
         [("Pflanzlich gegerbtes Leder","2,0–3,0 mm"),("Druckknöpfe","8 mm, ×2")],
         ["Streifen zuschneiden","Druckknöpfe setzen (2 Weiten)","Kanten brechen und versiegeln","Optional: Prägung"]),
        ("Hundeleine", 2, [("Hauptstreifen","A1",1500,18),("Handschlaufe","A2",200,18),("Karabiner-Schlaufe","A3",60,18)],
         [("Pflanzlich gegerbtes Rindsleder","3,0–3,5 mm"),("Polyester-Garn","0,8 mm"),("Karabiner","18 mm"),("Nieten","9 mm, ×4")],
         ["Hauptstreifen zuschneiden","Handschlaufe formen und nieten","Karabiner-Schlaufe formen und nieten","Kanten versiegeln und polieren"]),
        ("Hundehalsband", 2, [("Halsband-Streifen","A1",500,25),("Schlaufe","A2",40,30),("Spitze","A3",60,25)],
         [("Pflanzlich gegerbtes Rindsleder","3,0–3,5 mm"),("Polyester-Garn","0,6 mm"),("Dornschließe","25 mm"),("D-Ring","25 mm"),("Ovalöse","×1")],
         ["Streifen zuschneiden (Halsumfang + 15cm)","Löcher stanzen","Schnalle und D-Ring einsetzen","Schlaufe fixieren","Kanten versiegeln"]),
        ("Tabaksbeutel", 2, [("Hauptteil","A1",200,150),("Innentasche (Papier)","A2",180,60),("Binderiemen","A3",300,8)],
         [("Weiches Rindsleder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","10 mm")],
         ["Innentasche aufnähen","Hauptteil falten","Seiten nähen","Binderiemen mit Druckknopf","Kanten versiegeln"]),
        ("Blumentopf-Hülle", 1, [("Hauptteil (Zylinder)","A1",400,160),("Boden (rund)","A2",130,130)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Leinengarn","0,8 mm")],
         ["Zylinderform nähen","Runden Boden einsetzen","Rand oben umklappen","Kanten versiegeln"]),
        ("Taschentuchtasche", 1, [("Hauptteil","A1",140,100),("Öffnungsschlitz","A2",80,10)],
         [("Weiches Leder","0,8–1,0 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","8 mm")],
         ["Schlitz in die Mitte schneiden und Kanten versiegeln","Hauptteil falten","Seiten nähen","Druckknopf setzen"]),
        ("AirPods-Hülle", 1, [("Hauptteil","A1",70,55),("Klappe","A2",70,30),("Karabiner-Schlaufe","A3",30,15)],
         [("Pflanzlich gegerbtes Leder","1,2–1,5 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","8 mm"),("Karabiner","10 mm")],
         ["Hauptteil um Case formen","Seiten nähen","Klappe befestigen, Druckknopf setzen","Karabiner-Schlaufe anbringen","Kanten versiegeln"]),
        ("Feuerzeughülle", 1, [("Hauptteil","A1",75,55),("Schlaufe","A2",30,15)],
         [("Pflanzlich gegerbtes Leder","1,5–2,0 mm"),("Polyester-Garn","0,4 mm"),("Druckknopf","8 mm")],
         ["Hauptteil um Feuerzeug formen","Seitennaht nähen","Schlaufe befestigen","Kanten versiegeln"]),
        ("Lederschürze", 3, [("Hauptteil","A1",700,600),("Brustlatz","A2",300,200),("Nackenriemen","A3",600,20),("Hüftriemen","A4",800,20,2),("Werkzeugtasche","A5",200,150)],
         [("Pflanzlich gegerbtes Rindsleder","1,5–2,0 mm"),("Polyester-Garn","0,8 mm"),("Schnallen","20 mm, ×2"),("Nieten","9 mm, ×8"),("Ösen","12 mm, ×4")],
         ["Brustlatz an Hauptteil nähen","Werkzeugtasche aufnähen","Nackenriemen oben befestigen","Hüftriemen seitlich befestigen","Schnallen einsetzen","Ösen für Aufhänger","Kanten versiegeln"]),
        ("Buchhülle (Paperback)", 2, [("Außenteil","A1",300,210),("Steckfach links","A2",70,200),("Steckfach rechts","A3",70,200),("Lesezeichen","A4",200,10)],
         [("Pflanzlich gegerbtes Leder","1,0–1,2 mm"),("Polyester-Garn","0,4 mm")],
         ["Steckfächer positionieren","Lesezeichen befestigen","Zusammennähen","Kanten versiegeln"]),
        ("Kabelbinder (Set von 5)", 1, [("Kabelbinder","A1",100,15,5)],
         [("Lederreste","1,5–2,0 mm"),("Druckknöpfe","8 mm, ×5")],
         ["5 Streifen zuschneiden","Druckknöpfe setzen","Kanten brechen und versiegeln"]),
        ("Tischset (Platzdeckchen)", 1, [("Hauptteil","A1",450,350)],
         [("Pflanzlich gegerbtes Leder","2,5–3,0 mm")],
         ["Rechteck zuschneiden","Ecken abrunden","Kanten brechen und mit Tokonole versiegeln","Optional: Prägung oder Steppnaht am Rand"]),
        ("Einkaufschip-Halter", 1, [("Hauptteil","A1",50,40),("Ring-Schlaufe","A2",30,15)],
         [("Lederreste","2,0–2,5 mm"),("Schlüsselring","25 mm"),("Niet","7 mm")],
         ["Münzfach ausschneiden","Ring-Schlaufe mit Niet befestigen","Kanten versiegeln"]),
        ("Gepäckgurt", 2, [("Gurtstreifen","A1",600,40),("Schnalle-Ende","A2",80,40),("Namensschildfenster","A3",80,50)],
         [("Pflanzlich gegerbtes Rindsleder","3,0–3,5 mm"),("Polyester-Garn","0,8 mm"),("Steckschnalle","40 mm"),("Klarsichtfolie","×1")],
         ["Namensschildfenster ausschneiden und Folie einsetzen","Streifen zuschneiden","Schnalle einsetzen","Zusammennähen","Kanten versiegeln"]),
        ("Kopfhörer-Halter", 1, [("Hauptteil","A1",80,100),("Verschlussband","A2",120,12)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Druckknopf","10 mm"),("Niet","7 mm")],
         ["Hauptteil um Kopfhörer formen","Verschlussband mit Druckknopf","Mit Niet fixieren","Kanten versiegeln"]),
        ("Kamera-Handschlaufe", 1, [("Hauptstreifen","A1",250,20),("Befestigungsschlaufe","A2",80,12,2),("Polsterung","A3",200,18)],
         [("Pflanzlich gegerbtes Leder","2,0–2,5 mm"),("Polyester-Garn","0,6 mm"),("Splitringe","10 mm, ×2"),("Wildleder für Polsterung","×1")],
         ["Polsterung auf Hauptstreifen kleben und nähen","Befestigungsschlaufen um Splitringe","Enden zusammennähen","Kanten versiegeln"]),
    ]),
]

def count_patterns():
    return sum(len(pats) for _, _, pats in CATEGORIES)

NUM = 0
for _, _, pats in CATEGORIES:
    NUM += len(pats)

# ── HTML-Generierung ────────────────────────────────────────────────────

def svg_pattern(pieces, pid, max_w=660, max_h=400):
    """SVG mit Piezas, Cotas und Labels."""
    margin = 30
    gap = 20
    scale = 1.0

    rects = []
    for p in pieces:
        name, label = p[0], p[1]
        pw, ph = p[2], p[3]
        qty = p[4] if len(p) > 4 else 1
        rects.append((name, label, pw, ph, qty))

    total_w = sum(r[2] for r in rects) + gap * (len(rects) - 1) + margin * 2
    max_piece_h = max(r[3] for r in rects)
    total_h = max_piece_h + margin * 2 + 60

    if total_w > max_w:
        scale = (max_w - margin * 2) / (total_w - margin * 2)
    if total_h * scale > max_h:
        scale = min(scale, (max_h - margin * 2 - 60) / max_piece_h)

    vw = max(total_w * scale, max_w)
    vh = max(total_h * scale, max_h)
    vw = max_w
    vh = max_h

    lines = []
    lines.append(f'<svg viewBox="0 0 {vw} {vh}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:{max_w}px;display:block;margin:0 auto">')

    # Grid de fondo
    lines.append(f'<defs><pattern id="grid-{pid}" width="20" height="20" patternUnits="userSpaceOnUse">'
                 f'<path d="M20 0L0 0 0 20" fill="none" stroke="{LINE}" stroke-width="0.5"/>'
                 f'</pattern></defs>')
    lines.append(f'<rect width="{vw}" height="{vh}" fill="{BG}" stroke="{LINE}" stroke-width="1" rx="8"/>')
    lines.append(f'<rect x="1" y="1" width="{vw-2}" height="{vh-2}" fill="url(#grid-{pid})"/>')

    # Cuadrado de control (abajo derecha)
    sq_size = 30
    sq_x = vw - sq_size - 15
    sq_y = vh - sq_size - 15
    lines.append(f'<rect x="{sq_x}" y="{sq_y}" width="{sq_size}" height="{sq_size}" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    lines.append(f'<line x1="{sq_x}" y1="{sq_y+sq_size//2}" x2="{sq_x+sq_size}" y2="{sq_y+sq_size//2}" stroke="{INK}" stroke-width="0.5"/>')
    lines.append(f'<line x1="{sq_x+sq_size//2}" y1="{sq_y}" x2="{sq_x+sq_size//2}" y2="{sq_y+sq_size}" stroke="{INK}" stroke-width="0.5"/>')
    lines.append(f'<text x="{sq_x+sq_size//2}" y="{sq_y-4}" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="7" fill="{SOFT}">20 mm / 1 Zoll</text>')

    # Piezas
    x_cursor = margin
    y_base = margin + 20
    for i, (name, label, pw, ph, qty) in enumerate(rects):
        sw = pw * scale
        sh = ph * scale

        if x_cursor + sw > vw - margin:
            x_cursor = margin
            y_base += sh + gap + 30

        if y_base + sh > vh - 50:
            sh = vh - y_base - 50
            if sh < 20:
                continue

        rx = 4 if pw > 100 else 2

        # Pieza
        lines.append(f'<rect x="{x_cursor:.1f}" y="{y_base:.1f}" width="{sw:.1f}" height="{sh:.1f}" '
                     f'fill="{CREAM}" stroke="{INK}" stroke-width="1.5" rx="{rx}"/>')

        # Línea de costura interior (dashed)
        inset = 4 * scale
        if sw > inset * 4 and sh > inset * 4:
            lines.append(f'<rect x="{x_cursor+inset:.1f}" y="{y_base+inset:.1f}" '
                         f'width="{sw-inset*2:.1f}" height="{sh-inset*2:.1f}" '
                         f'fill="none" stroke="{COPPER}" stroke-width="0.5" stroke-dasharray="4 3" rx="{rx}"/>')

        # Label de pieza
        lines.append(f'<text x="{x_cursor+sw/2:.1f}" y="{y_base+sh/2+3:.1f}" text-anchor="middle" '
                     f'font-family="DM Sans,sans-serif" font-weight="700" font-size="11" fill="{COPPER}">'
                     f'{label}{"×"+str(qty) if qty>1 else ""}</text>')

        # Cota horizontal (abajo)
        cy = y_base + sh + 12
        lines.append(f'<line x1="{x_cursor:.1f}" y1="{cy}" x2="{x_cursor+sw:.1f}" y2="{cy}" stroke="{ACCENT}" stroke-width="0.8"/>')
        # Flechitas
        lines.append(f'<polygon points="{x_cursor:.1f},{cy} {x_cursor+4:.1f},{cy-2.5} {x_cursor+4:.1f},{cy+2.5}" fill="{ACCENT}"/>')
        lines.append(f'<polygon points="{x_cursor+sw:.1f},{cy} {x_cursor+sw-4:.1f},{cy-2.5} {x_cursor+sw-4:.1f},{cy+2.5}" fill="{ACCENT}"/>')
        lines.append(f'<text x="{x_cursor+sw/2:.1f}" y="{cy-3:.1f}" text-anchor="middle" '
                     f'font-family="DM Sans,sans-serif" font-size="8" font-weight="600" fill="{ACCENT}">{pw} mm</text>')

        # Cota vertical (derecha)
        cx = x_cursor + sw + 10
        lines.append(f'<line x1="{cx}" y1="{y_base:.1f}" x2="{cx}" y2="{y_base+sh:.1f}" stroke="{ACCENT}" stroke-width="0.8"/>')
        lines.append(f'<polygon points="{cx},{y_base:.1f} {cx-2.5},{y_base+4:.1f} {cx+2.5},{y_base+4:.1f}" fill="{ACCENT}"/>')
        lines.append(f'<polygon points="{cx},{y_base+sh:.1f} {cx-2.5},{y_base+sh-4:.1f} {cx+2.5},{y_base+sh-4:.1f}" fill="{ACCENT}"/>')
        # Texto vertical
        lines.append(f'<text x="{cx+4:.1f}" y="{y_base+sh/2:.1f}" text-anchor="start" '
                     f'font-family="DM Sans,sans-serif" font-size="8" font-weight="600" fill="{ACCENT}" '
                     f'transform="rotate(90,{cx+4:.1f},{y_base+sh/2:.1f})">{ph} mm</text>')

        # Flecha de dirección de grano
        if sw > 40 and sh > 40:
            gx = x_cursor + sw/2
            gy = y_base + sh - 15 * scale
            gl = min(20, sh * 0.3)
            lines.append(f'<line x1="{gx:.1f}" y1="{gy:.1f}" x2="{gx:.1f}" y2="{gy-gl:.1f}" stroke="{SOFT}" stroke-width="0.7"/>')
            lines.append(f'<polygon points="{gx:.1f},{gy-gl:.1f} {gx-2.5:.1f},{gy-gl+5:.1f} {gx+2.5:.1f},{gy-gl+5:.1f}" fill="{SOFT}"/>')

        x_cursor += sw + gap + 18

    lines.append('</svg>')
    return "\n".join(lines)


def difficulty_stars(level):
    return "★" * level + "☆" * (5 - level)


def materials_table(mats):
    rows = "".join(f'<tr><td>{m[0]}</td><td>{m[1]}</td></tr>' for m in mats)
    return f'<table class="mat"><thead><tr><th>Material</th><th>Spezifikation</th></tr></thead><tbody>{rows}</tbody></table>'


def steps_list(steps):
    items = "".join(f'<li>{s}</li>' for s in steps)
    return f'<ol class="steps">{items}</ol>'


def pattern_page(cat_name, cat_icon, pat, idx, total):
    name, diff, pieces, mats, steps = pat
    pid = f"p{idx}"
    svg = svg_pattern(pieces, pid)
    stars = difficulty_stars(diff)
    mat_table = materials_table(mats)
    step_list = steps_list(steps)

    piece_count = sum(p[4] if len(p) > 4 else 1 for p in pieces)

    return f'''<div class="page">
<div class="ph">
  <div class="ph-top">
    <div class="ph-cat"><span class="ph-icon">{cat_icon}</span> {cat_name}</div>
    <div class="ph-id">LW-{idx:03d}</div>
  </div>
  <h2 class="ph-name">{name}</h2>
  <div class="ph-meta">
    <span class="ph-diff" title="Schwierigkeit {diff}/5">{stars}</span>
    <span class="ph-pcs">{piece_count} Teile</span>
  </div>
</div>
<div class="ph-svg">{svg}</div>
<div class="ph-bottom">
  <div class="ph-col">{mat_table}</div>
  <div class="ph-col">{step_list}</div>
</div>
<div class="ph-footer">
  <span>Leder &amp; Werkstatt · Meister-Schnittmusterkollektion</span>
  <span>Schnittmuster {idx} von {total} · Kontrollquadrat: 20 mm</span>
</div>
</div>'''


def toc_page(categories, counts):
    rows = []
    running = 1
    for (cat_name, icon, pats), count in zip(categories, counts):
        rows.append(f'<tr><td class="toc-icon">{icon}</td><td class="toc-cat">{cat_name}</td>'
                    f'<td class="toc-count">{count} Schnittmuster</td>'
                    f'<td class="toc-range">LW-{running:03d} – LW-{running+count-1:03d}</td></tr>')
        running += count
    table = "".join(rows)
    return f'''<div class="page toc-page">
<h2 class="toc-title">Inhaltsverzeichnis</h2>
<p class="toc-sub">Über {sum(counts)} professionelle Leder-Schnittmuster in 6 Kategorien</p>
<table class="toc-table"><tbody>{table}</tbody></table>
<div class="toc-legend">
  <div><b>Jedes Schnittmuster enthält:</b></div>
  <div class="toc-items">
    <span>📐 Exakte Maße (mm + Zoll)</span>
    <span>📋 Vollständige Materialliste</span>
    <span>🔢 Nummerierte Montageschritte</span>
    <span>📏 Kontrollquadrat (20 mm / 1 Zoll)</span>
    <span>↕ Richtung des Leders (Grain)</span>
    <span>- - Nahtlinien markiert</span>
  </div>
</div>
</div>'''


def cover_page(total):
    return f'''<div class="page cover">
<div class="cover-bg"></div>
<div class="cover-inner">
  <div class="cover-top">
    <div class="cover-badge">PROFESSIONELLE KOLLEKTION</div>
  </div>
  <h1 class="cover-title">Meister-Schnitt&shy;muster&shy;kollektion<br><em>für Leder</em></h1>
  <p class="cover-sub">Über {total} professionelle Schnittmuster mit exakten Maßen,<br>
  Materiallisten und Schritt-für-Schritt-Anleitung</p>
  <div class="cover-cats">
    <span>👜 Taschen</span><span>🎒 Rucksäcke</span><span>💳 Geldbörsen</span>
    <span>📦 Umhängetaschen</span><span>✈️ Reise</span><span>🔑 Accessoires</span>
  </div>
  <div class="cover-features">
    <div class="cover-feat"><b>PDF</b><small>A4 · A1 · Letter</small></div>
    <div class="cover-feat"><b>mm + Zoll</b><small>Exakte Maße</small></div>
    <div class="cover-feat"><b>Kommerziell</b><small>Lizenz inklusive</small></div>
  </div>
  <div class="cover-brand">Leder &amp; Werkstatt</div>
</div>
</div>'''


def license_page():
    return '''<div class="page license-page">
<h2 class="lic-title">Kommerzielle Lizenz</h2>
<div class="lic-seal">✓</div>
<p class="lic-text">Mit dem Kauf dieser Kollektion erhältst du eine <b>unbefristete, nicht-exklusive kommerzielle Lizenz</b> zur Nutzung aller enthaltenen Schnittmuster.</p>
<div class="lic-grid">
  <div class="lic-box lic-yes">
    <h3>✓ Das darfst du</h3>
    <ul>
      <li>Lederwaren aus den Schnittmustern herstellen und verkaufen</li>
      <li>Auf Märkten, online, in sozialen Medien oder in deinem Laden verkaufen</li>
      <li>Unbegrenzte Stückzahl produzieren</li>
      <li>Schnittmuster für dich ausdrucken (beliebig oft)</li>
      <li>100 % deiner Einnahmen behalten — keine Lizenzgebühren</li>
    </ul>
  </div>
  <div class="lic-box lic-no">
    <h3>✗ Das darfst du nicht</h3>
    <ul>
      <li>Die Schnittmuster-Dateien weiterverkaufen oder weitergeben</li>
      <li>Die Dateien online teilen oder öffentlich zugänglich machen</li>
      <li>Behaupten, du hättest die Schnittmuster selbst entworfen</li>
    </ul>
  </div>
</div>
<p class="lic-footer">Diese Lizenz gilt für alle Schnittmuster dieser Kollektion, ohne Ablaufdatum.</p>
</div>'''


def generate():
    total = count_patterns()
    counts = [len(pats) for _, _, pats in CATEGORIES]

    parts = []

    # CSS
    parts.append(f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Meister-Schnittmusterkollektion für Leder · {total} Schnittmuster</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700;1,900&display=swap" rel="stylesheet">
<style>
@page {{ size: A4 portrait; margin: 12mm 10mm; }}
*,*::before,*::after {{ box-sizing: border-box; }}
html {{ font-size: 14px; }}
body {{ margin: 0; padding: 0; font-family: 'DM Sans', sans-serif; color: {INK}; background: #fff; }}

/* ── Page container ── */
.page {{ page-break-after: always; position: relative; min-height: 100vh; padding: 0; display: flex; flex-direction: column; }}
.page:last-child {{ page-break-after: auto; }}

/* ── Cover ── */
.cover {{ background: {INK}; color: {CREAM}; justify-content: center; align-items: center; text-align: center; padding: 40px 24px; }}
.cover-bg {{ position: absolute; inset: 0; background: radial-gradient(60% 50% at 80% 20%, rgba(200,114,42,.25), transparent 70%), radial-gradient(40% 40% at 10% 80%, rgba(122,59,30,.3), transparent 70%); }}
.cover-inner {{ position: relative; max-width: 500px; }}
.cover-badge {{ display: inline-block; background: {COPPER}; color: #fff; font-size: 10px; font-weight: 800; letter-spacing: .2em; padding: 6px 16px; border-radius: 50px; margin-bottom: 24px; }}
.cover-title {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 38px; line-height: 1.05; margin: 0 0 16px; }}
.cover-title em {{ color: {ACCENT}; font-style: italic; }}
.cover-sub {{ font-size: 15px; line-height: 1.6; color: rgba(245,237,224,.8); margin: 0 0 28px; }}
.cover-cats {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin: 0 0 28px; }}
.cover-cats span {{ font-size: 12px; font-weight: 700; padding: 6px 12px; border: 1px dashed rgba(224,161,94,.5); border-radius: 8px; }}
.cover-features {{ display: flex; justify-content: center; gap: 20px; margin: 0 0 32px; }}
.cover-feat {{ text-align: center; padding: 12px 16px; border-radius: 12px; background: rgba(245,237,224,.06); border: 1px solid rgba(224,161,94,.3); }}
.cover-feat b {{ display: block; font-size: 16px; color: {ACCENT}; }}
.cover-feat small {{ font-size: 11px; color: rgba(245,237,224,.65); }}
.cover-brand {{ font-family: 'Playfair Display', serif; font-style: italic; font-size: 22px; color: {ACCENT}; }}

/* ── TOC ── */
.toc-page {{ padding: 40px 24px; justify-content: flex-start; }}
.toc-title {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 30px; margin: 0 0 6px; text-align: center; }}
.toc-sub {{ text-align: center; color: {SOFT}; font-size: 14px; margin: 0 0 28px; }}
.toc-table {{ width: 100%; border-collapse: collapse; margin: 0 0 24px; }}
.toc-table td {{ padding: 14px 12px; border-bottom: 1px solid {LINE}; font-size: 14px; }}
.toc-icon {{ font-size: 20px; width: 36px; text-align: center; }}
.toc-cat {{ font-weight: 700; }}
.toc-count {{ color: {COPPER}; font-weight: 700; text-align: center; }}
.toc-range {{ color: {SOFT}; font-size: 12px; text-align: right; }}
.toc-legend {{ background: {CREAM}; border-radius: 12px; padding: 16px 20px; border: 1px dashed {COPPER}; }}
.toc-legend b {{ font-size: 13px; margin-bottom: 8px; }}
.toc-items {{ display: flex; flex-wrap: wrap; gap: 8px 16px; margin-top: 8px; }}
.toc-items span {{ font-size: 12px; color: {SOFT}; }}

/* ── Pattern page ── */
.ph {{ padding: 4px 0 0; border-bottom: 2px solid {INK}; margin: 0 0 8px; }}
.ph-top {{ display: flex; justify-content: space-between; align-items: center; margin: 0 0 4px; }}
.ph-cat {{ font-size: 12px; font-weight: 700; color: {COPPER}; display: flex; align-items: center; gap: 6px; }}
.ph-icon {{ font-size: 16px; }}
.ph-id {{ font-family: 'DM Sans', monospace; font-size: 11px; font-weight: 700; color: {SOFT}; letter-spacing: .1em; }}
.ph-name {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 22px; margin: 0 0 4px; line-height: 1.15; }}
.ph-meta {{ display: flex; gap: 16px; margin: 0 0 8px; font-size: 12px; }}
.ph-diff {{ color: {ACCENT}; letter-spacing: 2px; }}
.ph-pcs {{ color: {SOFT}; font-weight: 600; }}
.ph-svg {{ flex: 1; display: flex; align-items: center; justify-content: center; padding: 4px 0; min-height: 200px; }}
.ph-bottom {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 0 0 4px; }}
.ph-col {{ min-width: 0; }}

/* Materials table */
.mat {{ width: 100%; border-collapse: collapse; font-size: 11.5px; }}
.mat th {{ text-align: left; padding: 5px 6px; background: {INK}; color: {CREAM}; font-size: 10px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }}
.mat td {{ padding: 4px 6px; border-bottom: 1px solid {LINE}; }}
.mat tr:last-child td {{ border-bottom: 0; }}

/* Steps */
.steps {{ margin: 0; padding: 0 0 0 18px; font-size: 11.5px; line-height: 1.5; }}
.steps li {{ padding: 2px 0; }}
.steps li::marker {{ color: {COPPER}; font-weight: 700; }}

/* Footer */
.ph-footer {{ display: flex; justify-content: space-between; padding: 6px 0 0; border-top: 1px solid {LINE}; font-size: 9px; color: {SOFT}; }}

/* ── License page ── */
.license-page {{ padding: 40px 24px; justify-content: flex-start; }}
.lic-title {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 30px; text-align: center; margin: 0 0 16px; }}
.lic-seal {{ width: 64px; height: 64px; border-radius: 50%; background: {GREEN}; color: #fff; font-size: 30px; font-weight: 900; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; }}
.lic-text {{ text-align: center; font-size: 15px; line-height: 1.65; color: {SOFT}; margin: 0 0 24px; max-width: 500px; margin-left: auto; margin-right: auto; }}
.lic-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 0 0 24px; }}
.lic-box {{ border-radius: 14px; padding: 20px; }}
.lic-box h3 {{ margin: 0 0 10px; font-size: 15px; }}
.lic-box ul {{ margin: 0; padding: 0 0 0 18px; font-size: 13px; line-height: 1.6; }}
.lic-yes {{ background: #EAF3EC; border: 1px solid {GREEN}; }}
.lic-yes h3 {{ color: {GREEN}; }}
.lic-no {{ background: #FDF0EF; border: 1px solid #C0413D; }}
.lic-no h3 {{ color: #C0413D; }}
.lic-footer {{ text-align: center; font-size: 12px; color: {SOFT}; }}

/* ── Category divider ── */
.cat-div {{ padding: 40px 24px; justify-content: center; align-items: center; text-align: center; background: {CREAM}; }}
.cat-div-icon {{ font-size: 48px; margin: 0 0 12px; }}
.cat-div-title {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 32px; margin: 0 0 8px; }}
.cat-div-count {{ font-size: 16px; color: {COPPER}; font-weight: 700; }}

@media print {{
  .page {{ min-height: auto; height: auto; }}
  body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
}}
</style>
</head>
<body>
''')

    # Cover
    parts.append(cover_page(total))

    # TOC
    parts.append(toc_page(CATEGORIES, counts))

    # License
    parts.append(license_page())

    # Patterns by category
    idx = 1
    for cat_name, cat_icon, pats in CATEGORIES:
        # Category divider page
        parts.append(f'''<div class="page cat-div">
<div class="cat-div-icon">{cat_icon}</div>
<h2 class="cat-div-title">{cat_name}</h2>
<p class="cat-div-count">{len(pats)} Schnittmuster · LW-{idx:03d} – LW-{idx+len(pats)-1:03d}</p>
</div>''')

        for pat in pats:
            parts.append(pattern_page(cat_name, cat_icon, pat, idx, total))
            idx += 1

    parts.append('</body></html>')
    return "\n".join(parts)


if __name__ == "__main__":
    print(generate())
