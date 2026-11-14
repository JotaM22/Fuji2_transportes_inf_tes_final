# Informe de tesis de maestría · Simbal, 2026

Informe de la Maestría en Transportes y Conservación Vial de la Universidad Privada Antenor Orrego. Esta primera versión incluye la carátula, las páginas preliminares y los índices automáticos. La declaración de originalidad y la acreditación están redactadas como borradores para revisión y firma. La presentación, la dedicatoria y el agradecimiento se adaptaron del modelo de Gerencia. El resumen y el abstract se completarán cuando esté redactado el cuerpo del informe.

## Compilación

Ejecutar desde la raíz del repositorio con una distribución LaTeX que incluya XeLaTeX y los paquetes de la plantilla:

    latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex

En Overleaf, seleccionar XeLaTeX y configurar main.tex como documento principal. En VS Code, la receta incluida usa XeLaTeX mediante latexmk.

El documento es A4, con margen izquierdo de 3 cm y los otros márgenes de 2,5 cm. Para la entrega formal, compilar con Times New Roman instalada. Tinos y Liberation Serif son alternativas para las compilaciones de prueba.

## Archivos

- **main.tex** integra las páginas y genera los índices.
- **datos-tesis.tex** contiene el título y los datos editables de la carátula.
- **preliminares/** contiene la carátula y las páginas preliminares.
- **estilos.sty**, **estructura.sty** y **tablas.sty** conservan los componentes de formato para las siguientes etapas.
- **NORMAS_FORMATO.md** y **AUDITORIA_FORMATO_REFERENCIA.md** documentan el formato de la plantilla.
- **Informe_Tesis_Simbal_2026_Preliminares.pdf** permite revisar la primera compilación.

El título, la línea y la sublínea siguen el proyecto corregido. Los datos del autor y del asesor se contrastaron con el registro institucional de la tesis. Completar el jurado y la resolución con la designación oficial y verificar por separado el ORCID del autor.

Las páginas de firma conservan espacios para completar en la versión institucional. Registrar el porcentaje y la fecha del reporte de similitud cuando se disponga del informe correspondiente.
