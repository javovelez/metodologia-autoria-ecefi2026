# Guía rápida del trabajo con Claude Code

Referencia para el usuario sobre cómo está organizado el trabajo con Claude Code en este proyecto. Actualizada el 2026-09-25.

---

## 1. Qué archivo manda sobre qué

| Archivo | Qué contiene | Cuándo lo lee Claude |
|---|---|---|
| `AGENTS.md` | Resumen del proyecto, reglas esenciales, cómo trabajar con el usuario, sub-proyectos y skills | Automáticamente al iniciar cada sesión |
| `memoria/` | Perfil del usuario, forma de trabajo, estado del proyecto y decisiones que no se deducen de los archivos | Automáticamente (el índice `MEMORY.md`) |
| `STYLE.md` | Todas las reglas de redacción, para todo el proyecto | Antes de redactar o revisar prosa |
| `DECISIONES.md` | La lista previa a redactar una sección y el repertorio de aperturas | Antes de redactar una sección del libro |
| `NOTATION.md` | Símbolos y convenciones LaTeX | Como consulta |
| `avance.md` | Qué se escribió en cada sección: notación, ejemplos, figuras | Antes de redactar contenido nuevo del libro |
| `README.md` | Arquitectura de archivos, compilación, sistema de figuras | Ante dudas técnicas |
| Guía de cada sub-proyecto | Formato y reglas propias (`gabinete.md`, `presentaciones.md`, `REDACCION.md`, `PARCIALES.md`, etc.) | Al trabajar en ese sub-proyecto |
| `.claude/skills/*/SKILL.md` | Protocolos por tipo de tarea | Al invocar el skill |

Una regla nueva de redacción va a `STYLE.md`, una de notación a `NOTATION.md` y una de figuras al skill `create_2d_figures`. La memoria no guarda reglas de estilo, para que no haya dos fuentes que se contradigan.

---

## 2. Skills

| Skill | Cuándo invocarlo |
|---|---|
| `/write_section` | Escribir o reescribir una sección del libro o de un apunte |
| `/review_section` | Auditar una sección ya escrita |
| `/create_2d_figures` | Crear una figura 2D |
| `/3d_figures` | Crear una superficie 3D de una función racional |

Un skill se invoca escribiendo `/nombre` o pidiéndolo en lenguaje natural.

---

## 3. Flujos habituales

### Escribir una sección del libro

1. Pedir la sección e invocar `/write_section`.
2. Claude lee `STYLE.md`, `DECISIONES.md`, `avance.md` y las secciones vecinas.
3. Claude presenta las subsecciones previstas y espera la respuesta.
4. Claude deja la deliberación como comentario en la cabecera del `.tex` y redacta.
5. Claude hace la pasada de fraseo de `STYLE.md §17`.
6. Iterar. Cuando la sección quede estable, pedir `/review_section`.
7. Pedir `/update_avance`, o anunciar que se cierra la sesión, que tiene el mismo efecto.

### Crear una figura

1. Describir qué tiene que mostrar la figura.
2. Invocar `/create_2d_figures`.
3. Claude escribe el standalone en `figures/fig_nombre/fig_nombre.tex`, lo compila, mide el ancho natural y propone el bloque `figure` con la fracción de ancho que deja la letra en 8 pt.

### Resolver un trabajo práctico

1. Pedir el ejercicio e invocar `/write_tp`.
2. Claude lee el enunciado y `gabinete.md`, y resuelve un movimiento por cada pedido del inciso.

### Agregar slides

1. Pedir la clase e invocar `/write_slides`.
2. Claude presenta el esqueleto de frames y espera la respuesta.
3. Claude redacta y mide la densidad de texto con el script del skill.

---

## 4. Reglas que Claude aplica sin que haya que repetirlas

| Regla | Dónde está |
|---|---|
| Sin em-dashes; dos puntos solo para enumerar o anunciar una fórmula | `STYLE.md §14.5` y `§14.6` |
| Cada oración nombra de qué habla; nada de aperturas de anuncio o de intriga | `STYLE.md §14.1` y `§14.3` |
| Sin coloquialismos ni prosa comprimida | `STYLE.md §14.2` y `§16` |
| `avance.md` solo a pedido o al cerrar la sesión | `AGENTS.md` y `memoria/` |
| Cuadros `resultado` con título y solo el enunciado | `STYLE.md §13.5` |
| Notación `j`, `\bar{z}`, `x_p`/`x_i`, `\vect{}` | `NOTATION.md` |
| Referencias con la palabra completa, sin `§` | `STYLE.md §8` |
| Figuras incluidas como PDF precompilado; recompilar después de tocarlas | `README.md §4` |
| `\subimport` en los capítulos, nunca `\input` | `AGENTS.md` |

---

## 5. Estructura de directorios

```text
/
├── AGENTS.md            Brief que Claude carga en cada sesión
├── WORKFLOW.md          Esta guía
├── STYLE.md             Estilo de redacción
├── DECISIONES.md        Deliberación previa a redactar
├── NOTATION.md          Notación
├── README.md            Arquitectura y compilación
├── avance.md            Registro de lo escrito
├── memoria/             Memoria de Claude, versionada
├── setup.tex            Paquetes y estilos globales
├── libro_asys.tex       Archivo maestro
├── XXcapitulo/          Capítulos del libro
├── fourier_discreto/    Apunte de Fourier discreto
├── transformada_z/      Apunte de Transformada Z
├── Gabinete/            Trabajos prácticos
├── Presentaciones/      Clases Beamer
├── evaluaciones/        Parciales
├── animaciones/         Animaciones interactivas
├── Moodle/              Banco de preguntas
└── .claude/skills/      Skills
```

---

## 6. Cómo agregar un skill

1. Crear `.claude/skills/nombre_skill/SKILL.md` con el frontmatter `name` y `description`.
2. Documentar las lecturas previas, la deliberación y la forma, escrito según `STYLE.md` (los modelos imitan el estilo de las instrucciones que leen).
3. Agregarlo a la tabla de skills de `AGENTS.md` y de esta guía.
