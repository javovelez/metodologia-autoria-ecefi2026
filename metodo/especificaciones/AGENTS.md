# Análisis de Señales y Sistemas

Libro de cátedra en Análisis de Señales y Sistemas para estudiantes de ingeniería de primero y segundo año, con Cálculo I y II, Álgebra Lineal y Física Clásica. Alrededor del libro hay trabajos prácticos, presentaciones, apuntes condensados, parciales, animaciones y un banco de preguntas de Moodle.

## 1. Qué leer antes de trabajar

| Archivo | Cuándo |
|---|---|
| `STYLE.md` | Siempre antes de redactar o revisar prosa, en cualquier sub-proyecto. Es la referencia única de estilo. |
| `DECISIONES.md` | Antes de redactar una sección o subsección del libro. |
| `NOTATION.md` | Consulta de símbolos y convenciones LaTeX. |
| `avance.md` | Antes de redactar contenido nuevo del libro, para ver notación, ejemplos y conceptos ya establecidos en las secciones vecinas. Es largo; se lee la entrada del capítulo en curso y las vecinas. |
| La guía del sub-proyecto | Ver la Sección 5 de este archivo. |

Las reglas de estilo aplican del Capítulo 3 en adelante y al material derivado. Los Capítulos 1 y 2 están escritos en un registro deliberadamente comprimido y no se usan como modelo.

## 2. Lo esencial del estilo

`STYLE.md` tiene el detalle. Estas son las reglas que más se violan al redactar.

- **Lenguaje cercano, sin saltear pasos, con ejemplos simples y la intuición siempre a la vista.** Cuando una regla choca con esos cuatro objetivos, ganan ellos.
- **La estructura más simple que haga el trabajo.** Una afirmación por oración. Si hay que releer, se parte.
- **Cada oración nombra de qué habla.** Nada de pronombres ni demostrativos cuyo referente esté más atrás que la oración anterior. Repetir el sustantivo está bien.
- **Sin em-dashes en la prosa**, ni sueltos ni en pares. Incisos con comas, aclaraciones largas en oración propia, notación entre paréntesis.
- **Los dos puntos no presentan ni concluyen.** Entran en enumeraciones reales, antes de una fórmula display y en rótulos.
- **El párrafo abre con una oración completa que nombra su objeto.** Nada de anuncios vacíos, de oraciones cortas de intriga (*"La división tiene un límite."*) ni de muletillas (*"Conviene…"*).
- **Ni coloquial ni comprimido.** *Aquí* y no *acá*; *aumentar* y no *subir*; nada de *dar* ni *hacer* como verbos comodín. Se devuelven las palabras que dan claridad.
- **Cuadros `resultado`** con título y solo el enunciado o la fórmula; su posición se evalúa en cada caso.
- **Referencias con la palabra completa**: *el Capítulo~\ref{}*, *la Sección~\ref{}*, *la ecuación~\eqref{}*. Nunca `§` ni `cf.` en el cuerpo.
- **Notación**: `j` y no `i`; `\bar{z}` y no `z^*`; `x_p`/`x_i` para par e impar; `$90^\circ$`; `\vect{v}` para vectores discretos. Nunca caracteres matemáticos Unicode en un `.tex`.

## 3. Cómo trabajar con el usuario

- **Consultar antes de empezar una sección nueva.** Presentar las subsecciones previstas (nombre, alcance breve, figuras) y esperar su respuesta antes de redactar. No aplica a correcciones puntuales ni a una sección ya en marcha.
- **El usuario itera.** Nada está terminado hasta que él lo diga. Después de un cambio sustancial, ofrecer una pasada contra `STYLE.md`.
- **`avance.md` se actualiza a pedido**, con el skill `update_avance`. Anunciar el cierre de la sesión cuenta como pedido.
- **Conservar sus ediciones a mano** cuando pide mejorar un párrafo, y corregir solo el defecto señalado.
- **Responder con análisis propio**, discrepar cuando corresponde y contestar en prosa las preguntas reflexivas.
- **No reabrir decisiones cerradas** sin un motivo nuevo (ver `memoria/project_decisiones_contenido.md`).
- **Git**: nunca sobrescribir el working tree con HEAD; commits solo a pedido.

## 4. Memoria

La memoria de Claude para este proyecto vive en `memoria/`, versionada con el repositorio. Guarda el perfil del usuario, cómo trabajar con él, el estado del proyecto y las decisiones que no se deducen de los archivos. Las reglas de redacción, notación y figuras no van a la memoria: van a `STYLE.md`, `NOTATION.md`, `DECISIONES.md` o al skill que corresponda.

## 5. Sub-proyectos

| Sub-proyecto | Carpeta | Guía |
|---|---|---|
| Libro | `01capitulo/` a `13capitulo/` | `README.md` |
| Trabajos prácticos | `Gabinete/tp1/` a `tp8/` | `Gabinete/gabinete.md` |
| Presentaciones Beamer | `Presentaciones/clase01/` a `clase18/` | `Presentaciones/presentaciones.md` |
| Apunte de Fourier discreto (cerrado el 2026-09-15) | `fourier_discreto/` | `fourier_discreto/fourier_discreto.md` y `fourier_discreto/REDACCION.md` |
| Apunte de Transformada Z | `transformada_z/` | `transformada_z/transformada_z.md` y `fourier_discreto/REDACCION.md` |
| Parciales | `evaluaciones/` | `evaluaciones/PARCIALES.md` |
| Animaciones interactivas | `animaciones/` | `animaciones/animaciones.md` |
| Banco de preguntas Moodle | `Moodle/` | `Moodle/README.md` |

Los apuntes son documentos aparte que no entran en `libro_asys.tex`, compilan autónomos y no llevan `\ref` a capítulos del libro. Si el apunte de Fourier discreto se reabre, hay que avisarlo en la cabecera de su guía, porque las clases 17 y 18 se derivan de él.

Arquitectura del libro: `libro_asys.tex` importa `XXcapitulo/CapituloXX.tex`, que importa `XXcapitulo/XY/secXY.tex`. Las figuras TikZ son standalone en `XXcapitulo/XY/figures/fig_nombre/fig_nombre.tex`. `setup.tex` se importa en todos los archivos hijos con la ruta relativa que corresponde a su profundidad. En los capítulos se usa siempre `\subimport` y nunca `\input`, para preservar las rutas de las figuras. Las figuras se incluyen como PDF precompilado (`mode=image`), así que después de tocar una figura hay que recompilarla en su carpeta.

## 6. Skills

| Skill | Para qué |
|---|---|
| `write_section` | Escribir una sección o subsección del libro o de un apunte. |
| `review_section` | Auditar prosa ya escrita contra `STYLE.md` y `DECISIONES.md`. |
| `create_2d_figures` | Crear una figura 2D con TikZ o pgfplots. |
| `3d_figures` | Crear una superficie 3D de magnitud de una función racional. |

## 7. Referencias

| Archivo | Contiene |
|---|---|
| `README.md` | Arquitectura de archivos, compilación, sistema de figuras. |
| `WORKFLOW.md` | Guía rápida del trabajo con Claude Code, pensada para el usuario. |
| `memoria/` | Memoria del proyecto. |
