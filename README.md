# Material de respaldo — ECEFI 2026

Muestra del material didáctico producido con la metodología de autoría que presenta el trabajo
**«Una metodología agéntica y reproducible para producir material didáctico en ingeniería: tres
cátedras, un mismo método»**, IX Congreso Internacional de Educadores en Ciencias Empíricas en
Facultades de Ingeniería (ECEFI 2026), Valparaíso, 28 al 30 de octubre de 2026.

Javier Ignacio Velez; Enrique Puliafito — Departamento de Ingeniería en Tecnologías
Electrónicas, Universidad Tecnológica Nacional, Facultad Regional Mendoza.

**Página de navegación:** https://javovelez.github.io/metodologia-autoria-ecefi2026/

---

## Esto es una muestra parcial de un trabajo en proceso

El material de las tres asignaturas está en producción. Acá se publica solo una selección,
elegida para que el lector pueda examinar el método y sus resultados sin acceder a los
repositorios completos. **Falta la mayor parte** de los capítulos, de las guías, de las
animaciones y de los bancos de evaluación. Lo publicado corresponde al
estado de avance del **7 de septiembre de 2026** y está sujeto a revisión.

Tampoco se publica material resuelto que esté en uso: las fuentes `.lab.md` de los
laboratorios de Redes Neuronales Profundas, sus resoluciones y sus rúbricas quedan fuera
porque llevan las respuestas adentro.

Las especificaciones e instrucciones modulares que se publican son **las del libro de Análisis
de Señales y Sistemas**, el caso de elaboración original, y no rigen el material de las otras
dos asignaturas, que tienen las suyas y no se publican. Es además una selección: no están
todos los archivos en vigencia.

**Del capítulo 11 del libro en adelante no se publica nada** —ni texto ni figuras—, porque ese
material todavía no está revisado. Del resto del libro se publican únicamente las figuras que
el texto referencia; las que quedaron en las carpetas de trabajo sin llegar a usarse quedan
fuera.

---

## Qué hay acá

| Carpeta | Contenido |
|---|---|
| `metodo/especificaciones/` | Algunas de las especificaciones en vigencia **del libro de Análisis de Señales y Sistemas**: estilo, notación, circuito de trabajo y ruteo del proyecto |
| `metodo/skills/` | Algunas de las instrucciones modulares **de ese mismo libro**: redactar una sección, revisarla, construir figuras 2D y 3D |
| `asys/figuras/` | Las 201 figuras que el texto de los capítulos 1 a 10 referencia, cada una con su fuente TikZ y su PDF vectorial |
| `asys/miniaturas/` | Rasterizaciones de esas figuras, para el catálogo |
| `asys/capitulo-05/` | Un capítulo completo: PDF, las cinco secciones en LaTeX y sus figuras |
| `asys/presentaciones/` | Las presentaciones Beamer de las dieciséis clases, en PDF. La fuente no se publica: incluye figuras del libro por ruta relativa y fuera de su repositorio esas rutas no resolverían |
| `asys/guias/` | Las siete guías de trabajos prácticos con sus resoluciones, fuente y PDF |
| `asys/animaciones/` | Diez animaciones interactivas, cada una una página HTML autónoma que no pide nada a la red |
| `tc2/gabinete/tp4/` | Teoría de los Circuitos II: resolución y presentación de un trabajo práctico, con los `.sch` que alimentan la biblioteca de esquemáticos. El enunciado no se publica: está en revisión |
| `rnp/laboratorios/` | Tres cuadernos de laboratorio de Redes Neuronales Profundas, sin resolver |
| `herramientas/` | Los dos scripts que arman este repositorio a partir de los repos de cátedra |

Las páginas `index.html` y `catalogo.html` se sirven con GitHub Pages.

## Herramientas que no se duplican acá

Tienen repositorio público propio:

- [netlist2tikz](https://github.com/javovelez/netlist2tikz) — biblioteca de 51 módulos que
  traduce una descripción textual de un circuito al código de su esquemático.
- [Curso de introducción a Python](https://github.com/ASyS-utn-frm/python) — nueve módulos y
  seis laboratorios de apoyo para Análisis de Señales y Sistemas.
- [lab-corrector](https://github.com/javovelez/lab-corrector) — aplicación de apoyo a la
  corrección de laboratorios y contrato de autoría de los cuadernos.

## Cómo se arma este repositorio

Los repositorios de cátedra son la fuente y **se leen, nunca se modifican**. Los dos scripts de
`herramientas/` copian el material seleccionado, descartan los archivos intermedios de LaTeX,
rasterizan las miniaturas y generan el catálogo:

```bash
python3 herramientas/armar_muestra.py   <destino>
python3 herramientas/armar_catalogo.py  <destino>
```

## Cómo citar

> Velez, J. I., y Puliafito, E. (2026). *Una metodología agéntica y reproducible para producir
> material didáctico en ingeniería: tres cátedras, un mismo método* [Trabajo presentado]. IX
> Congreso Internacional de Educadores en Ciencias Empíricas en Facultades de Ingeniería
> (ECEFI 2026), Valparaíso, Chile.

## Licencia

Material didáctico bajo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es).
Las herramientas enlazadas conservan la licencia de su propio repositorio. Ver [LICENSE](LICENSE).
