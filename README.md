# Informe de tesis de maestría · Simbal, 2026

Informe de la Maestría en Transportes y Conservación Vial de la Universidad Privada Antenor Orrego. El documento incluye la carátula, las páginas preliminares, los índices automáticos y el capítulo de Introducción hasta la justificación práctica. La presentación, la dedicatoria y el agradecimiento se adaptaron del modelo de Gerencia.

## Compilación

Ejecutar desde la raíz del repositorio con una distribución LaTeX que incluya XeLaTeX y los paquetes de la plantilla:

    latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex

En Overleaf, seleccionar XeLaTeX y configurar main.tex como documento principal. En VS Code, la receta incluida usa XeLaTeX mediante latexmk.

El documento es A4, con margen izquierdo de 3 cm y los otros márgenes de 2,5 cm. Para la entrega formal, compilar con Times New Roman instalada. Tinos y Liberation Serif son alternativas para las compilaciones de prueba.

## Archivos

- **main.tex** integra las páginas y genera los índices.
- **datos-tesis.tex** contiene el título y los datos editables de la carátula.
- **preliminares/** contiene la carátula y las páginas preliminares.
- **capitulos/introduccion.tex** contiene la Introducción hasta la justificación práctica.
- **referencias.tex** reúne las referencias citadas.
- **estilos.sty**, **estructura.sty** y **tablas.sty** conservan los componentes de formato para las siguientes etapas.
- **NORMAS_FORMATO.md** y **AUDITORIA_FORMATO_REFERENCIA.md** documentan el formato de la plantilla.
- **Informe_Tesis_Simbal_2026_Preliminares.pdf** contiene la compilación del informe.

El título, la línea y la sublínea siguen el proyecto corregido. Los datos del autor y del asesor se contrastaron con el registro institucional de la tesis. Completar el jurado y la resolución con la designación oficial y verificar por separado el ORCID del autor.

La declaración usa X% como marcador del índice de similitud. Sustituir X% con el índice que figure en el informe de Turnitin. Las afirmaciones de la declaración y la acreditación se incluyen para revisión de quienes deban firmarlas.
