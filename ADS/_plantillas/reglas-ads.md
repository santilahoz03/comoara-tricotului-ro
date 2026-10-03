# Reglas de ads (aprendidas)

> Estado: vivo · Lo lee Claude antes de cualquier tarea de anuncios.
> Cada corrección del usuario se agrega acá como regla corta: **qué hacer · por qué · cómo aplicarlo · fecha**.
> Si una regla nueva contradice una vieja, la vieja pasa a "Historial / superado" con la fecha y qué la reemplazó.

## Reglas de base (vienen con el kit)

1. **Pipeline completo en réplicas y doblajes:** limpieza con Vmake + voz + karaoke + popups traducidos + música -22 dB + swell + impacto en el CTA. Voz sola sobre video limpio suena a boceto. Excepción: el usuario pide "solo la voz" o "sin música".
2. **Nunca precios en moneda** en guiones multi-país (porcentajes o "mirá el precio abajo"). Anglo de un solo país: ganancias en dólares concretas y altas, inversión "just $20".
3. **Preguntar acento** de guion y de voz antes de escribir o generar. No se arregla editando texto.
4. **Voz del género de quien se ve** (mirando el video); sin nadie en pantalla, del género del comprador.
5. **Nunca desacelerar la voz.** Voz larga: acelerar la voz hasta 1.4x. Voz corta: acelerar el video con F = duración_voz / duración_video.
6. **Karaoke por palabra** (openai-whisper word_timestamps sobre el audio final, alineado al guion), 4 palabras por línea, fuente ~52 en 720x1280, línea hasta la siguiente, centrado en quote cards.
7. **Sin guiones largos ni puntos suspensivos sueltos** en los guiones: duplican subtítulos.
8. **Popups del original recreados y traducidos**, sincronizados con la voz nueva (Vmake también los borra).
9. **Hook con clips de video reales**, nunca fotos con zoom. Ken Burns solo en el cuerpo.
10. **Todo 9:16 con el parámetro explícito**; verificar con ffprobe.
11. **Anuncios cortos sin avatar por default** (voz en off sobre B-roll). Avatar solo en los segundos de cara, con su audio nativo.
12. **Deduplicar arsenales por guion hablado**, nunca por caption.
13. **Variante compliance en el mismo lote** para cifras de kilos, ingresos o salud.
14. **Iterar = mismo ángulo y mensaje.** Cambiar la objeción es un concepto nuevo.
15. **Tier más barato que cumpla; reciclar antes de generar; avisar antes de tandas de más de USD 5; probar 1 antes de la tanda.**
16. **2 rondas del pipeline automático; a la tercera, manual.**
17. **Previsualización = grilla HTML**, nunca lista de links.
18. **Tanda nueva = conjunto nuevo en la misma campaña.** No se edita un anuncio que ya corre.

## Reglas aprendidas (las agrega Claude con cada corrección)

| Fecha | Regla | Por qué | Cómo aplicarla |
|---|---|---|---|
| | | | |

## Costos medidos (actualizar con cada tanda)

| Fecha | Recurso | Modelo / tier | Costo real medido | Cómo se midió |
|---|---|---|---|---|
| | | | | saldo antes / después |

## Historial / superado

_(vacío)_
