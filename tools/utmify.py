#!/usr/bin/env python3
"""Cliente de SOLO LECTURA del MCP de Utmify. Lee UTMIFY_MCP_TOKEN del .env; nunca imprime el token.
Uso: python3 tools/utmify.py tools | call <herramienta> '<json args>'
Herramientas: get_dashboards, get_dashboard_summary, get_meta_ad_objects, get_utms_ad_objects."""
import json, sys, urllib.request
from pathlib import Path

SOLO_LECTURA = {"get_dashboards", "get_dashboard_summary", "get_meta_ad_objects", "get_utms_ad_objects"}

def token():
    for l in (Path(__file__).resolve().parent.parent / ".env").read_text().splitlines():
        if l.startswith("UTMIFY_MCP_TOKEN="):
            v = l.split("=", 1)[1].split("#")[0].strip()
            if v:
                return v
    sys.exit("Falta UTMIFY_MCP_TOKEN en .env")

def rpc(method, params=None, id=1):
    url = "https://mcp.utmify.com.br/mcp/?token=" + token() + "&resources=gs,gm,gu"
    body = json.dumps({"jsonrpc": "2.0", "id": id, "method": method, "params": params or {}}).encode()
    req = urllib.request.Request(url, body, {"Content-Type": "application/json", "Accept": "application/json, text/event-stream", "User-Agent": "segundo-cerebro/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=60))

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("tools", "call"):
        sys.exit(__doc__)
    if sys.argv[1] == "tools":
        for t in rpc("tools/list")["result"]["tools"]:
            print(t["name"])
    else:
        n = sys.argv[2]
        if n not in SOLO_LECTURA:
            sys.exit("Herramienta no permitida (solo lectura): " + n)
        args = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
        r = rpc("tools/call", {"name": n, "arguments": args})
        print(r["result"]["content"][0]["text"] if "result" in r else json.dumps(r.get("error")))
