# Stack: conectores y navegador

> **Estado:** parcial
> **Actualizado:** 2026-10-04
> **Fuentes:** instalación kit 00 (`procesos/admin/stack/que-necesita-cada-kit.md`), `CLAUDE.md` (kits instalados), `procesos/admin/stack/pendientes.md`, `stack.md`
> **Relacionado:** [[negocio]]

## En corto
Kits 00, 01, 02, 03, 05 y 06 instalados (2026-10-02). La Biblioteca de Anuncios se navega con el navegador propio de Claude; ImpulTienda se ve con Claude in Chrome (solo lectura). Las herramientas con clave están en `.env` y el detalle de planes en `stack.md`. (`CLAUDE.md`, `procesos/admin/stack/pendientes.md`)

## Qué sé
- Navegador propio de Claude (pestaña Code de la app de escritorio): disponible. Es el que se usa para Facebook y la biblioteca de anuncios, nunca el Chrome personal. (instalación kit 00)
- Gmail, Calendar, Drive, Meta (conector): no los uso todavía. Gmail lo pide el kit 07 o la auditoría mensual de suscripciones; el resto son opcionales.
- MCP locales: **Utmify conectado el 2026-10-12**, solo lectura (herramientas `get_dashboards`, `get_dashboard_summary`, `get_meta_ad_objects`, `get_utms_ad_objects`; recursos habilitados: resumen, Meta y UTMs). Configurado en `.mcp.json` (gitignored) y con `tools/utmify.py` como respaldo. Dashboard «Principal» (zona -3, plataforma ImpultiendaDigital, cuentas Meta activas: CP 0.0 y CP 1.0). AdsUploader y Panda: no los uso todavía. (verificado con consulta real, 2026-10-12)
- Conector de Meta, si algún día se activa: solo lectura de la biblioteca de anuncios.

- Herramientas con clave activas: kie.ai, Gemini (AI Studio), GitHub (`gh`), Vmake (solo `tools/vmake_limpiar.py`), ElevenLabs, DreamAPI. (`stack.md`, `procesos/admin/stack/pendientes.md`)
- ImpulTienda: cuenta creada, Claude in Chrome ve el panel (solo lectura); Whop conectado en la tienda «Prueba». (`procesos/admin/stack/pendientes.md` #5)
- Telegram: las variables TELEGRAM_BOT_TOKEN y TELEGRAM_CHAT_ID figuran en `.env` pero sin valor (solo un comentario) al 2026-10-04: no hay bot configurado. Coincide con `pendientes.md` #9 («sin Telegram»). (verificado por la rutina semanal sin imprimir valores)

## Decisiones tomadas
| Fecha | Decisión | Motivo | Fuente |
|---|---|---|---|
| 2026-10-02 | Perfil Solo Cazar, sin conectores | El kit 01 usa solo el navegador integrado | instalación kit 00 |

## Abierto / pendiente
- Sumar conectores y claves cuando llegue a cada kit.

## Historial / superado
- 2026-10-04: «Perfil Solo Cazar: no hace falta ningún conector ni clave» y la decisión «Perfil Solo Cazar, sin conectores» (2026-10-02) → superados al instalar los kits 02, 03, 05 y 06 (`CLAUDE.md`).

## Salidas relacionadas
- [2026-10-04 · Revisión semanal](../OUTPUTS/2026-10-04-revision-semanal.md)
