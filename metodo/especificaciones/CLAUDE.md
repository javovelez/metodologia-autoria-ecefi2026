# Análisis de Señales y Sistemas — Contexto del Proyecto

Libro de cátedra en Análisis de Señales y Sistemas, orientado a estudiantes de ingeniería de 1.º–2.º año con formación en Cálculo I/II, Álgebra Lineal y Física Clásica (mecánica).

---

## 1. Propósito del libro

El libro busca ser **más abordable** que la mayoría de los textos existentes en la materia. Las cuatro decisiones tonales que sostienen esa diferencia son:

- **Lenguaje cercano**: prosa de docente, no de tratado.
- **Explicaciones didácticas que no saltean pasos**.
- **Ejemplos fáciles de digerir** (gana el más simple cuando hay opciones).
- **Intuición siempre a la vista**: el lector nunca debería perder el hilo de qué estamos haciendo y por qué.

Estas son el norte. Cuando una regla específica entra en conflicto con cualquiera de ellas, gana la decisión tonal. Guía completa: `STYLE.md §1`.

---

## 2. Alcance de las reglas de estilo

Las reglas de estilo y la voz que describe `STYLE.md` aplican al **cuerpo principal del libro: del Capítulo 3 en adelante**, y al material derivado.

Los Capítulos 1 y 2 ya están escritos en un registro deliberadamente comprimido (introducción y antesala de variable compleja) y **no se usan como referencia tonal ni como modelo de aperturas**. Para escribir o iterar contenido del Cap. 3 en adelante, no mirar Cap. 1 ni Cap. 2 como modelo.

---

## 3. Antes de redactar prosa: leer siempre

| Archivo | Cuándo leerlo |
|---|---|
| `STYLE.md` | **Obligatorio** antes de redactar prosa nueva. Define propósito, pilares, no-saltear-pasos, sostener intuición, cadencia, test del borrado. |
| `DECISIONES.md` | **Obligatorio** antes de redactar una sección o subsección del libro. Checklist de deliberación pre-redacción. |
| `NOTATION.md` | Lookup de convenciones de símbolos. |
| `avance.md` | **Obligatorio** antes de redactar contenido nuevo del libro. Verificar notación ya establecida, ejemplos ya usados y conceptos ya definidos en secciones vecinas. **No actualizar nunca de forma automática**: solo cuando el usuario lo pida explícitamente. |

---

## 4. Pilares de estilo (resumen — guía completa en `STYLE.md`)

- **Rigor sin pedantería**: precisión matemática exacta, sin construcciones rimbombantes ni poéticas.
- **Amigable sin ser romántico**: tono de docente directo y conversacional, sin metáforas emocionales o lúdicas.
- **Exactitud sin ambigüedades coloquiales**: simpleza nunca a costa de imprecisión matemática.
- **Registro natural del castellano**: formas verbales y sustantivos comunes, no nominalizaciones forzadas.
- **Pragmático y operativo**: foco en el mecanismo y en cómo el estudiante opera con la herramienta.

Reglas operativas adicionales (todas detalladas en `STYLE.md`):

- **Intuición primero, formalización después** (preferencia por defecto): cuando es viable, presentar primero la intuición de qué estamos haciendo y por qué, y recién después formalizar. Apartarse solo cuando hay un camino claramente mejor.
- **No saltear pasos**: cuando un paso requiere algo que no está a la vista en la línea anterior, hacerlo visible. Frases como *"es fácil ver que"*, *"se sigue inmediatamente"*, *"un cálculo directo muestra"* son señales de salto y se reemplazan por el paso real.
- **Sostener la intuición**: después de un desarrollo de más de tres líneas, una oración que reconecta con qué estamos haciendo y para qué.
- **Cadencia**: toda fórmula display importante va amarrada a prosa antes o después; no encadenar dos display sin texto intermedio fuera de cuadros `resultado`.
- **Nada de *dar* como verbo de resultado** (`STYLE.md §13.7`): *"la integral da cero"* → *"vale cero"*; *"eso da $y[0]=x[0]$"* → *"queda"*; según el caso *produce*, *conduce a*, *arroja*, *equivale a*, *muestra*. Se conserva el `dar` que es verbo propio (*"da una vuelta"*, *"dar lugar a"*). *"Resultar en"* es calco del inglés.
- **Dos puntos con moderación** (`STYLE.md §13.9`): los dos puntos ordenan una vez y se vuelven muletilla repetidos. La preferencia por defecto es la oración corrida; entran cuando su claridad es superadora, no por costumbre. Dos en el mismo párrafo o en párrafos contiguos son uno de más.
- **Nada de oraciones telegráficas** (`STYLE.md §13.10`): con el verbo de actividad elidido y el sintagma nominal sin anclaje (*"Queda el factor que multiplica a todo"*), la oración se lee como título, no como prosa. Prueba del título: si funciona como `\subsubsection*{}`, reescribir.
- **Test del borrado** para vocabulario aplicado: si al reemplazar el término por "este sistema" el párrafo sigue funcionando, el término decora y se considera borrar.
- **Referencias a capítulos futuros**: máximo una por subsección, solo cuando sea estructuralmente necesaria.
- **Vocabulario disponible**: no invocar categorías que se definen más adelante.
- **Fin de demostración**: sin `\qed`, sin `$\square$`, sin marcador de cierre.

---

## 5. Convenciones de notación (lookup en `NOTATION.md`)

| Elemento | Correcto | Incorrecto |
|---|---|---|
| Unidad imaginaria | `j` | `i` |
| Conjugado | `\bar{z}`, `\overline{z}` | `z^*` |
| Componente par | `x_p(t)` | `x_e(t)` |
| Componente impar | `x_i(t)` | `x_o(t)` |
| Grado sexagesimal | `$90^\circ$` | símbolo Unicode `°` |
| Variable de Laplace | `s = \sigma + j\omega` | — |
| Variable Z | `z = re^{j\theta}` | — |
| Ángulos | radianes (con equivalencia en grados entre paréntesis cuando aporta) | — |
| Referencias cruzadas | `el Capítulo~\ref{...}`, `la Sección~\ref{...}`, `la Subsección~\ref{...}` | `§\ref{...}`, `§5.2`, `(cf.~\ref{...})` |

---

## 6. Entornos LaTeX (`tcolorbox`)

```latex
\begin{resultado}[Título obligatorio]   % azul: definiciones formales, fórmulas clave
\begin{nota}[Título opcional]           % gris: advertencias, conexiones, notación
```

- **Contenido del cuadro `resultado`**: solo enunciado y/o fórmula. Las explicaciones, demostraciones y comentarios van en la prosa **afuera** del cuadro.
- **Posición del cuadro `resultado`**: la evaluación es obligatoria en cada caso. Por defecto, desarrollar el tema primero y poner el cuadro al final como resumen-referencia. La opción alternativa (cuadro al frente como pivote) aplica cuando el resultado es corto/inmediato. Lo prohibido es saltarse la evaluación.

---

## 7. Sub-proyectos

| Sub-proyecto | Directorio raíz | Guía completa |
|---|---|---|
| **Libro** | `01capitulo/` … `13capitulo/` | `README.md` |
| **Trabajos Prácticos** | `Gabinete/tp1/` … `tp7/` | `Gabinete/gabinete.md` |
| **Presentaciones Beamer** | `Presentaciones/clase01/` … | `Presentaciones/presentaciones.md` |
| **Animaciones interactivas** | `animaciones/` | `animaciones/animaciones.md` |
| **Apunte de Fourier discreto** | `fourier_discreto/` | `fourier_discreto/fourier_discreto.md` |

El **apunte de Fourier discreto** es un documento aparte, no incluido en `libro_asys.tex`: condensa los Capítulos 11 y 12 (91 pp) en ~25 pp para un curso de menor alcance. No los reemplaza y el libro no se toca. Reglas propias en su guía, y la principal es que **compila autónomo, sin `\ref` a capítulos del libro**.

Arquitectura de archivos del libro: `libro_asys.tex` → `XXcapitulo/CapituloXX.tex` → `XXcapitulo/XY/secXY.tex`. Figuras TikZ standalone en `XXcapitulo/XY/figures/fig_nombre/fig_nombre.tex`. `setup.tex` (raíz) se importa en todos los archivos hijos con ruta relativa ajustada según profundidad. En capítulos usar siempre `\subimport` (nunca `\input`) para preservar rutas relativas de figuras.

---

## 8. Skills disponibles

| Skill | Cuándo usarlo |
|---|---|
| `write_section` | Escribir una sección o subsección del libro (Cap. 3+). |
| `write_tp` | Resolver un Trabajo Práctico del sub-proyecto Gabinete. |
| `write_slides` | Agregar slides Beamer a una presentación. |
| `create_2d_figures` | Crear una figura 2D con TikZ/pgfplots como standalone. |
| `create_block_diagrams` | Crear un diagrama de bloques (signal flow) o realización directa de EDLCC. |
| `3d_figures` | Crear una superficie 3D de magnitud de función racional. |
| `review_section` | Auditar una sección ya escrita contra `STYLE.md` y `DECISIONES.md`. |
| `map_section` | Mapear la estructura de ideas de una sección párrafo por párrafo; diagnostica qué temas se mezclan y cómo organizar más claro. Corre con un agente por sección en paralelo. |
| `update_avance` | Actualizar `avance.md` después de cerrar una sección (solo cuando el usuario lo pide). |
| `bootstrap_chapter` | Crear la estructura de archivos para un capítulo nuevo. |

Cada skill carga las lecturas obligatorias correspondientes (ver §3) antes de proceder.

---

## 9. Iteración

El usuario trabaja en múltiples iteraciones sobre cada sección. No asumir que el contenido está finalizado hasta que lo indique. Después de cada cambio sustancial, ofrecer hacer una pasada de coherencia contra `STYLE.md` antes de cerrar.

---

## 10. Referencias de profundidad

| Sección | Contiene |
|---|---|
| `STYLE.md` | Reglas canónicas de estilo y tono de redacción, propósito del libro |
| `DECISIONES.md` | Checklist de deliberación y repertorio de aperturas |
| `NOTATION.md` | Convenciones de notación detalladas |
| `README.md §1–§4` | Arquitectura de archivos, compilación, sistema de figuras |
| `WORKFLOW.md` | Cheatsheet operativo del proyecto |
| `animaciones/animaciones.md` | Anatomía de una animación, flujo de armado y verificación, página de Moodle |
