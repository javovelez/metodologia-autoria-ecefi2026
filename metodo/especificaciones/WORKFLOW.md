# Cheatsheet de Trabajo — ASyS con Claude Code

Referencia rápida del protocolo de trabajo con Claude Code en este proyecto.

---

## 1. Mapa de archivos meta

| Archivo | Rol | Se carga… |
|---|---|---|
| `AGENTS.md` | Brief de arranque: estructura del proyecto, convenciones, reglas operativas | **Automático** al inicio de cada conversación |
| `README.md` | Referencia técnica completa: arquitectura, figuras, estilo (§8), convenciones LaTeX (§9) | A pedido, cuando hay dudas de profundidad |
| `avance.md` | Registro de lo ya escrito: temas, notación, ejemplos, figuras por sección | A pedido, antes de redactar contenido nuevo |
| `Gabinete/gabinete.md` | Especificaciones de TPs: formato, estilo, figuras | A pedido al trabajar en TPs |
| `Presentaciones/presentaciones.md` | Especificaciones de slides: distribución de contenido por clase | A pedido al trabajar en presentaciones |
| `.claude/skills/*/SKILL.md` | Protocolos invocables: instrucciones detalladas por tipo de tarea | Al invocar el skill correspondiente |

---

## 2. Skills disponibles y cuándo invocarlos

| Skill | Invocar cuando… | Qué hace |
|---|---|---|
| `write_section` | Vas a escribir o reescribir una sección del libro | Lee `avance.md`, aplica estilo §8, estructura LaTeX, protocolo de figuras |
| `write_tp` | Vas a resolver un ejercicio de TP | Lee el enunciado, aplica formato gabinete.md, doble camino polar/rectangular |
| `write_slides` | Vas a agregar slides a una clase Beamer | Aplica estilo telegráfico, incluye PDFs del libro por ruta relativa |
| `create_2d_figures` | Vas a crear una figura 2D con TikZ/pgfplots | Aplica colores semánticos, capas, tamaños, ylabel horizontal |
| `3d_figures` | Vas a crear una superficie 3D de función racional | Aplica escalado no-lineal de color, clipping de polos, etiquetas externas |

### Cómo invocar un skill

En el chat de Claude Code, simplemente escribir `/nombre_del_skill` o pedirlo en lenguaje natural:

```
/write_section
escribir sección 4.3 sobre convolución discreta
```

```
/create_2d_figures
necesito una figura que muestre la respuesta al impulso h[n] para n = -2..5
```

---

## 3. Flujo de trabajo por tipo de tarea

### 3a. Escribir una sección del libro

```
1. [automático] AGENTS.md cargado → Claude conoce el proyecto
2. [tú] "Escribir sección X.Y: [tema]" (+ invocar /write_section)
3. [Claude] Lee avance.md → verifica notación y contenido existente
4. [Claude] Lee README.md §8 → aplica reglas de estilo
5. [Claude] Lee secciones vecinas .tex → verifica coherencia
6. [Claude] Redacta el contenido en secXY.tex
7. [tú] Iteras / corregís / pedís ajustes
8. [tú] Cuando la sección está lista: "actualizar avance.md con sección X.Y"
9. [Claude] Actualiza avance.md (SOLO cuando vos lo pedís)
```

**Nota clave:** Claude NO toca `avance.md` hasta el paso 8.

### 3b. Crear una figura TikZ

```
1. [tú] Describir la figura: señales, ejes, rangos, qué debe mostrar
2. [tú] Invocar /create_2d_figures (o /3d_figures para superficies)
3. [Claude] Genera el código standalone en figures/fig_nombre/fig_nombre.tex
4. [tú] Compilar la figura individualmente:
        cd XXcapitulo/XY/figures/fig_nombre/ && pdflatex fig_nombre.tex
5. [tú] Revisar el PDF → pedir ajustes si hace falta
6. [Claude] Proporciona también el bloque \begin{figure}...\end{figure} para insertar en la sección
```

### 3c. Resolver un TP

```
1. [tú] "Resolver TP N, ejercicio X [inciso Y]" (+ invocar /write_tp)
2. [Claude] Lee Gabinete/tpN/tpN.tex → entiende el enunciado
3. [Claude] Lee gabinete.md → aplica formato y estilo
4. [Claude] Redacta resolución_tpN.tex
          - Una columna (sin multicols)
          - Doble camino rectangular + polar cuando aplica
          - Ángulos en radianes con equivalencia en grados entre paréntesis
          - Figuras solo si el enunciado las requiere o aportan valor didáctico genuino
```

### 3d. Agregar slides a una presentación

```
1. [tú] "Agregar slides sobre [tema/sección] a claseN" (+ invocar /write_slides)
2. [Claude] Lee presentaciones.md → verifica distribución de contenido
3. [Claude] Lee las secciones del libro correspondientes (o avance.md)
4. [Claude] Agrega frames a Presentaciones/claseN/claseN.tex
          - Una idea por slide
          - Texto telegráfico
          - Figuras vía ruta relativa al PDF del libro
5. [tú] Compilar: cd Presentaciones/claseN && pdflatex claseN.tex
```

---

## 4. Reglas que Claude ya conoce (no necesitás repetirlas)

Están en `AGENTS.md` y en cada skill. Se aplican automáticamente:

| Regla | Qué hace Claude |
|---|---|
| `avance.md` solo se actualiza cuando vos lo pedís | No lo toca al terminar una sección |
| Estilo del libro: rigor sin pedantería, amigable sin ser romántico, exactitud sin ambigüedades coloquiales, pragmático y operativo | Aplica los cuatro pilares de `README.md §8` |
| Sin `\qed` ni `$\square$` al final de demostraciones | Omite el símbolo de cierre |
| `j` no `i`, `\bar{z}` no `z^*` | Usa la notación correcta en todo el código LaTeX |
| `x_p(t)` / `x_i(t)` (no `x_e`/`x_o`) | Subíndice en español para par/impar |
| Referencias a cap. futuros: máx. 1 por subsección | No llena el texto de forward-references |
| Figuras del libro compiladas con `mode=image` | No recompila; asume que el PDF ya existe |
| `\subimport` en CapituloXX.tex (no `\input`) | Preserva rutas relativas de figuras |

---

## 5. Mapa de referencia rápida

**¿Dónde está la regla sobre…?**

| Duda | Dónde leer |
|---|---|
| Estilo de redacción del libro | `README.md §8` |
| Convenciones LaTeX del libro | `README.md §9` |
| Arquitectura de archivos y compilación | `README.md §1–§4` |
| Formato y estilo de resoluciones de TP | `Gabinete/gabinete.md` |
| Distribución de contenido por clase | `Presentaciones/presentaciones.md` |
| Qué se ha escrito en cada sección | `avance.md` |
| Colores, capas y tamaños de figuras 2D | `.claude/skills/create_2d_figures/SKILL.md` |
| Visualización 3D de funciones racionales | `.claude/skills/3d_figures/SKILL.md` |

---

## 6. Estructura de directorios de referencia

```text
/ (Raíz)
├── AGENTS.md                        ← Brief auto-cargado (no editar a mano salvo cambios de protocolo)
├── WORKFLOW.md                      ← Este archivo
├── README.md                        ← Referencia técnica completa del libro
├── avance.md                        ← Registro de contenido ya escrito
├── setup.tex                        ← Paquetes y estilos globales (importar en todos los hijos)
├── libro_asys.tex                   ← Archivo maestro del libro
│
├── XXcapitulo/
│   ├── CapituloXX.tex               ← Conductor del capítulo (usa \subimport)
│   └── XY/
│       ├── secXY.tex                ← Sección (standalone, \input{../../setup.tex})
│       └── figures/
│           └── fig_nombre/
│               ├── fig_nombre.tex   ← Figura standalone (\input{../../../../setup.tex})
│               └── fig_nombre.pdf   ← PDF pre-compilado (requerido antes de compilar el libro)
│
├── Gabinete/
│   ├── gabinete.md
│   └── tpN/
│       ├── tpN.tex                  ← Enunciado
│       └── resolucion/
│           ├── resolucion_tpN.tex
│           └── figures/
│
├── Presentaciones/
│   ├── presentaciones.md
│   └── claseN/
│       └── claseN.tex               ← Beamer (NO importa setup.tex)
│
└── .claude/
    └── skills/
        ├── create_2d_figures/SKILL.md
        ├── 3d_figures/SKILL.md
        ├── write_section/SKILL.md
        ├── write_tp/SKILL.md
        └── write_slides/SKILL.md
```

---

## 7. Cómo agregar un nuevo skill

Si surge un nuevo tipo de tarea recurrente (p. ej. "escribir ejercicios de TP" o "escribir prefacio"):

1. Crear carpeta `.claude/skills/nombre_skill/`
2. Crear `SKILL.md` con el frontmatter:
   ```markdown
   ---
   name: nombre_skill
   description: Una línea que describe cuándo usarlo.
   ---
   ```
3. Documentar: pre-flight, estructura de archivo, estilo, convenciones.
4. Agregar el skill a la tabla de skills en `AGENTS.md`.
