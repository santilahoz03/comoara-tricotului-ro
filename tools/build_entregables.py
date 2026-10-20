#!/usr/bin/env python3
"""Genera PDFs de los entregables HTML usando Chrome headless.
Uso: python3 build_entregables.py [ruta/a/proyecto]
  Si no se pasa ruta, busca oferta.json en el directorio actual.
"""
import json, os, subprocess, sys, http.server, threading, time, shutil

CHROME = shutil.which("google-chrome") or shutil.which("chromium")
if not CHROME:
    mac_chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.isfile(mac_chrome):
        CHROME = mac_chrome
if not CHROME:
    sys.exit("No se encontró Chrome. Instalá Google Chrome.")

def find_free_port():
    import socket
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port

def start_server(directory, port):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer(("127.0.0.1", port), handler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd

def html_to_pdf(url, output_path):
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=10000",
        f"--print-to-pdf={output_path}",
        "--no-pdf-header-footer",
        url,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f"  ERROR: {r.stderr[:200]}")
        return False
    return os.path.isfile(output_path) and os.path.getsize(output_path) > 0

def main():
    project_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    project_dir = os.path.abspath(project_dir)
    oferta_path = os.path.join(project_dir, "oferta.json")
    if not os.path.isfile(oferta_path):
        sys.exit(f"No se encontró oferta.json en {project_dir}")

    with open(oferta_path, "r", encoding="utf-8") as f:
        oferta = json.load(f)

    pdf_sources = os.path.join(project_dir, "pdf-sources")
    docs_dir = os.path.join(project_dir, "docs")

    port = find_free_port()
    httpd = start_server(pdf_sources, port)
    time.sleep(0.5)

    results = []
    for ent in oferta["entregables"]:
        fuente = ent.get("fuente", "")
        if not fuente.startswith("pdf-sources/"):
            print(f"  Saltando {ent['nombre']} (fuente: {fuente})")
            continue

        html_file = os.path.basename(fuente)
        html_path = os.path.join(pdf_sources, html_file)
        if not os.path.isfile(html_path):
            print(f"  FALTA: {html_path}")
            results.append((ent["nombre"], "FALTA HTML"))
            continue

        carpeta = ent["carpeta"]
        random_code = ent["random"]
        pdf_name = ent["pdf"]
        dest_dir = os.path.join(docs_dir, carpeta, random_code)
        os.makedirs(dest_dir, exist_ok=True)
        dest_pdf = os.path.join(dest_dir, pdf_name)

        url = f"http://127.0.0.1:{port}/{html_file}"
        print(f"  Generando: {ent['nombre']}")
        print(f"    {url} → {dest_pdf}")

        ok = html_to_pdf(url, dest_pdf)
        if ok:
            size_kb = os.path.getsize(dest_pdf) / 1024
            results.append((ent["nombre"], f"OK ({size_kb:.0f} KB)"))
            print(f"    OK — {size_kb:.0f} KB")
        else:
            results.append((ent["nombre"], "ERROR"))

    httpd.shutdown()

    print("\n=== Resumen ===")
    for nombre, estado in results:
        print(f"  {estado:>12}  {nombre}")

if __name__ == "__main__":
    main()
