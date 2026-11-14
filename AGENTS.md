# Instrucciones obligatorias para el agente — Informe de tesis (v1.0 inicial)

## Base documental
Usar `AUDITORIA_FORMATO_REFERENCIA.md` y el informe Word proporcionado por el usuario únicamente para reproducir el formato, **nunca** para copiar resultados, citas, tablas de datos ni información personal. Es un ejemplo, no un reglamento oficial.

## Tres capas
1. **Estructura**, en `estructura.sty`: páginas divisorias, jerarquía de capítulos y títulos, numeración, listas y preliminares.
2. **Presentación**, en `estilos.sty` y `tablas.sty`: fuente, tamaños, interlineados, márgenes, sangrías, notas, tablas y figuras.
3. **Contenido**, en `datos-tesis.tex` y los archivos que carga el documento principal: redacción, título, identidades, datos, resultados, referencias, figuras y anexos. Todo ello cambia entre tesis.

## Comandos semánticos
- `\capituloTesis{...}`: capítulo con página divisoria, numeración romana en divisoria y encabezado al iniciar el cuerpo.
- `\seccionTesis{...}`, `\subseccionTesis{...}`, `\apartadoTesis{...}`: títulos con numeración **automática**.
- `\subtituloSinNumero{...}`: apartado semántico sin numerar.
- `listaTrasTitulo`: solo cuando una lista sigue directamente a un título; el espacio adicional pertenece a la lista.
- `listaTesis`: lista dentro de párrafos normales.
- `\preliminarTesis{...}`: página preliminar.
- `\notaTabla{...}` y `\fuenteTabla{...}`: nota o fuente **debajo** de tabla o figura.

No escribir números manuales, tabulaciones o `\vspace` individuales para imitar un encabezado; resolver los cambios globalmente en el componente adecuado.

## Reglas de tablas y figuras
- Número en negrita, título en cursiva, ambos **arriba**.
- Nota o fuente debajo, separada visualmente del elemento.
- Tablas de resultados preferentemente con líneas horizontales; matrices e instrumentos pueden requerir cuadrículas.
- Numeración consecutiva de tablas y figuras en todo el informe, no reiniciada por capítulo.
- Ajustar tablas a `\linewidth`; en páginas horizontales revisar pie y numeración.
- Los enlaces usan `\urlstyle{same}` para mantener la familia tipográfica.

## Contenido y evidencia
- Prohibido inventar datos, p-valores, hipótesis confirmadas, fuentes o referencias.
- Dejar en blanco los campos sin información confirmada. Usar comentarios de LaTeX para indicar dónde incorporar el contenido pendiente.
- Los resultados se basan solo en datos suministrados; la discusión interpreta resultados efectivamente obtenidos.

## Cohesión de la redacción

- Antes de redactar o corregir, identifica la idea central de cada párrafo y el papel de las demás ideas como evidencia, explicación, condición, contraste o aplicación.
- Integra las ideas dependientes mediante subordinación, referentes explícitos y conexiones que expresen su relación. Si un bloque cumple dos funciones distintas, distribúyelo en párrafos.
- Conserva el punto seguido cuando la oración siguiente avance el mismo argumento y su relación con la anterior sea inequívoca. No lo uses para yuxtaponer afirmaciones ni lo sustituyas mecánicamente por otra puntuación o por conectores.
- Antes de entregar, comprueba en cada párrafo el referente de las expresiones, el fundamento de las afirmaciones y la continuidad del argumento. Conserva citas, cifras, tiempos verbales y decisiones metodológicas en una revisión de estilo.

## Control de calidad
- Compilar siempre con **XeLaTeX**, nunca pdfLaTeX, por `fontspec`.
- Revisar visualmente carátula, preliminares, índice, divisorias, jerarquía, cuerpo, leyendas, notas, referencias, horizontales y anexos.
- No declarar equivalencia exacta con Microsoft Word sin comparación verificable.
- Confirmar las exigencias institucionales vigentes antes de dar la plantilla por definitiva.
