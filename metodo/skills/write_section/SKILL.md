---
name: write_section
description: Protocolo para escribir una sección o subsección nueva del libro Análisis de Señales y Sistemas (Capítulo 3 en adelante). Estructura en tres bloques: pre-flight (lecturas obligatorias), deliberación (checklist de decisiones antes de redactar) y forma (estructura LaTeX, entornos, convenciones).
---

# Write Book Section — Protocol

El skill aplica al **cuerpo principal del libro: Capítulo 3 en adelante**. Los Caps. 1 y 2 ya están escritos en un registro deliberadamente comprimido y no se usan como referencia tonal.

El skill se ejecuta en tres bloques. **No saltearse el bloque de deliberación**: es donde se sostiene el rigor pedagógico del libro.

---

## Bloque 1 — Pre-flight: leer antes de pensar

Antes de redactar una sola línea, leer en este orden:

1. **`STYLE.md`** — propósito del libro, pilares de estilo, no saltear pasos, sostener intuición, cadencia, test del borrado. Aplica a todo el proyecto desde Cap. 3 en adelante. **Leer §2 y §13 completos**: son el registro y el catálogo de fraseo, y son la parte del estilo que más se degrada al redactar (ver 3.3.1).
2. **`DECISIONES.md`** — checklist de deliberación pre-redacción y repertorio de aperturas. Específico del libro.
3. **`avance.md`** — sección que corresponde al capítulo en curso, más secciones vecinas (anterior y posterior si existen). Identificar:
   - Notación ya establecida.
   - Ejemplos ya usados (no repetir).
   - Conceptos ya definidos (no redefinir).
   - Conceptos que se definen más adelante (no invocar).
4. **La sección `.tex` vecina** (anterior y/o posterior si está escrita y es del Cap. 3 en adelante) — verificar tono, densidad y coherencia de subíndices y nombres de variables al nivel de prosa.

Confirmar la ruta de destino: `XXcapitulo/XY/secXY.tex`.

---

## Bloque 2 — Deliberación: decidir antes de escribir

Este bloque es donde se sostiene la diferencia entre prosa pedagógica y prosa densa. **Hacerlo visible**: dejar la deliberación como comentario LaTeX al inicio del archivo, o reportarla en el chat antes de redactar el cuerpo de la sección, para que el usuario pueda corregir el rumbo.

### 2.1. Contestar la checklist de `DECISIONES.md §1`

Por cada subsección a redactar, contestar las cinco familias de preguntas:

- ¿Qué objeto ya conoce el lector que se parece a este?
- ¿Voy a nombrar un dominio aplicado? Si sí, ¿pasa el test del borrado?
- ¿La formalización va primero o necesita andamiaje previo?
- ¿Qué pasos podría tentarme a saltar y dónde podría perderse la intuición?
- ¿Qué prueba de consistencia le voy a dejar al lector al cerrar?

Las respuestas pueden ser breves (una línea cada una). Lo importante es que la decisión exista, no que la justificación sea larga.

### 2.2. Declarar el modo de apertura (`DECISIONES.md §2`)

Elegir uno de los cinco modos —problema concreto, geometría pura, continuidad estructural, definición seguida de pregunta, reposicionamiento— y declararlo explícitamente. Mencionar por qué los otros cuatro no aplican, aunque sea en una frase.

### 2.3. Decidir la posición de cada cuadro `resultado`

Por cada cuadro `resultado` previsto en la subsección, decidir explícitamente:

- **Al final como resumen-referencia** (opción por defecto): el desarrollo viene primero, el cuadro queda como cierre.
- **Al frente como pivote**: cuando el resultado es corto/inmediato o cuando el cuadro funciona mejor como definición pivote desde la cual se construye el resto.

Lo prohibido es saltarse esta evaluación.

### 2.4. Identificar términos de vocabulario aplicado a usar

Listar los términos aplicados que aparecerán y, para cada uno, indicar:

- Si es vocabulario "seguro" (parte de la base del lector — `DECISIONES.md §3`): puede usarse libremente.
- Si requiere test del borrado: indicar si pasó o no, y por qué se conserva.
- Si está en la lista "prohibido": reformular.

---

## Bloque 3 — Forma: estructura, entornos, convenciones

### 3.1. Estructura del archivo

```latex
\documentclass[crop=false]{standalone}
\input{../../setup.tex}

\begin{document}

% [opcional] Comentario con la deliberación del Bloque 2.

\section{Título de la Sección}
\label{sec:label_descriptivo}

% Contenido

\end{document}
```

La ruta a `setup.tex` es siempre `../../setup.tex` (dos niveles arriba desde `XXcapitulo/XY/`).

### 3.2. Composición de contenido

A partir del Capítulo 3, cada concepto relevante puede acompañarse de:

1. **Apertura** según el modo declarado en 2.2.
2. **Definición formal** en entorno `resultado` (con la posición decidida en 2.3).
3. **Demostración** trazable, sin marcador de cierre. Aplicar `STYLE.md §3` (no saltear pasos) con énfasis.
4. **Ejemplo** según las dos modalidades de `STYLE.md §11`:
   - *Fenómeno físico o aplicación real* (preferible cuando aplica): nombrar y explicar, sin cálculo.
   - *Ejemplo numerado*: cuando la utilidad operativa solo se entiende ejecutando. Resolver completamente. Título escueto *Ejemplo*, no *Ejemplo trabajado*. **No saltear pasos** (regla estricta en ejemplos numerados).
5. **Figura** solo cuando la geometría o la evolución temporal no se transmite igual de bien con texto. Ver §3.5.

Estos cinco elementos no son una receta lineal: se eligen y ordenan según la deliberación del Bloque 2. La preferencia por defecto del libro es **intuición primero, formalización después** (`STYLE.md §4`): cuando no hay razón clara para apartarse, ese es el camino. Apartarse es válido cuando un concepto particular se beneficia de definición corta primero, continuidad estructural o reposicionamiento de marco.

### 3.3. Estilo de redacción

Aplicar `STYLE.md`. En particular durante la redacción:

- **No saltear pasos** (`STYLE.md §3`): cuando una manipulación algebraica no es inmediata, desarrollarla. Las frases tipo *"es fácil ver que"* son señales de salto y se reemplazan.
- **Sostener intuición** (`STYLE.md §5`): después de un desarrollo de más de tres líneas, una oración que reconecta con qué estamos haciendo y para qué.
- **Cadencia** (`STYLE.md §6`): no encadenar dos fórmulas display sin prosa intermedia.
- **Vocabulario aplicado**: aplicar el test del borrado en tiempo real, no solo en la deliberación previa.
- **Fraseo natural** (`STYLE.md §2` y `§13`): ver 3.3.1, abajo. Es la regla que más se degrada en la práctica.
- **Referencias a capítulos futuros**: máximo una por subsección, solo si es estructuralmente necesaria.
- **Vocabulario disponible**: no invocar categorías que se definen más adelante.
- **Fin de demostración**: sin `\qed`, sin `$\square$`, sin marcador.

### 3.3.1. Escribir en castellano, no traducir del inglés

**Este libro se escribe en castellano; no se redacta en inglés y se traduce.** Es la regla que más silenciosamente se rompe: cada palabra puede ser correcta y la oración sonar igual ajena, porque el problema está en el armado. El lector lo percibe como prosa "rara" o "de manual traducido", y eso choca de frente con el primer pilar del libro —lenguaje cercano, prosa de docente— antes que con cualquier regla técnica.

El catálogo canónico es `STYLE.md §13` (fraseo) y `§2` (vocabulario y registro). No reemplazarlo por esta lista: leerlo. Lo que sigue son las alarmas que hay que tener presentes **mientras se escribe**, no solo al revisar.

| Alarma | Ejemplo a evitar | Preferir | Ref. |
|---|---|---|---|
| Clivada antepuesta | *"Lo que importa no es tanto la fórmula como qué es $\lambda$."* | *"Más que la fórmula, importa qué es $\lambda$."* | §13.2 |
| Sujeto de cláusula nominal pesado | *"Que una secuencia sea una lista de números habilita…"* | *"Como una secuencia es una lista de números, se puede…"* | §13.3 |
| Deícticos coloquiales | *acá*, *allá* | *aquí*, *allí*; o *"en el continuo"* / *"en el discreto"* | §13.1 |
| Perífrasis de relativo vacía | *"cuál de las dos es la que vamos a estudiar"* | *"cuál de las dos vamos a estudiar"* | §13.4 |
| Alcance adverbial ambiguo | *"deja de cumplirse siempre"* | *"ya no es siempre cierto"* | §13.5 |
| Verbo comodín *dar* | *"la integral da cero"*, *"eso da $y[0]=x[0]$"* | *"la integral vale cero"*, *"eso queda…"*, *"produce"*, *"conduce a"* | §13.7 |
| Nominalización forzada | *"el acotamiento"*, *"el aclarado"* | *"al acotar"*, *"la aclaración"* | §2 |
| Abreviatura latina | `cf.`, `e.g.`, `i.e.`, `vs.` | *"ver"*, *"por ejemplo"*, *"es decir"*, *"frente a"* | §2 |

Calcos sintácticos que hay que vigilar además del catálogo, por ser los que más se cuelan al redactar prosa técnica:

- **Imperativo de manual traducido**: *"Note que…"*, *"Observe que…"*, *"Recuerde que…"* (de *note that*). El libro le habla al lector en primera persona del plural o en impersonal: *"Conviene notar que…"*, *"Vale observar que…"*, o directamente afirmar sin preámbulo.
- **Pasiva perifrástica donde el castellano usa `se`**: *"el resultado es obtenido derivando"* → *"el resultado se obtiene derivando"*. En castellano la pasiva con *ser* es marcada; la pasiva refleja es la forma natural.
- **Gerundio de consecuencia**: *"…, resultando en un espectro periódico"* (de *resulting in*) → *"…, y el espectro queda periódico"*. El gerundio castellano expresa simultaneidad o modo, no resultado.
- **Conectores calcados**: *"Adicionalmente"* (→ *"Además"*), *"En orden a"* (→ *"Para"*), *"Esto es debido a"* (→ *"Esto se debe a"*), *"En términos de"* usado como relleno (→ reformular).
- **Sujeto explícito innecesario**: *"Nosotros podemos ver que…"* → *"Se ve que…"* o *"Vemos que…"*. El castellano marca la persona en el verbo.
- **Adjetivo antepuesto sistemático**: *"la anterior ecuación"*, *"el mencionado sistema"* → *"la ecuación anterior"*, *"el sistema mencionado"*.

**Prueba operativa**, análoga al test del borrado: releer el párrafo en voz alta preguntando *"¿lo diría así un docente explicando en el pizarrón?"*. Si suena a manual traducido, el problema es el armado de la oración, no el término técnico. Reescribir la oración entera antes que reemplazar palabras sueltas.

Si aparece un patrón de calco recurrente que este catálogo no cubre, agregarlo a `STYLE.md §13` —es el documento canónico— en lugar de dejarlo solo en este skill.

### 3.4. Convenciones LaTeX

Lookup en `NOTATION.md`. Resumen rápido:

| Elemento | Correcto |
|---|---|
| Unidad imaginaria | `j` |
| Conjugado | `\bar{z}`, `\overline{z}` |
| Componente par/impar | `x_p(t)` / `x_i(t)` |
| Grado sexagesimal | `$90^\circ$` |
| Comillas | `` ``texto'' `` |

### 3.5. Entornos y figuras

Entornos `resultado` y `nota`: ver `AGENTS.md §6` para uso, y `NOTATION.md` para reglas de contenido.

Figuras: usar `create_2d_figures` para 2D, `create_block_diagrams` para diagramas de flujo de señal, y `3d_figures` para superficies 3D. Convenciones técnicas en `README.md §4`.

```latex
% Inclusión en secXY.tex:
\begin{figure}[H]
    \centering
    \begin{minipage}{\linewidth}
        \centering
        \includestandalone[width=0.85\linewidth]{figures/fig_nombre/fig_nombre}
        \caption{Descripción de la figura.}
        \label{fig:nombre}
    \end{minipage}
\end{figure}
```

Toda figura debe tener `\label{}` y ser referenciada explícitamente en el texto. Compilarla individualmente antes de compilar la sección o el libro.

---

## Bloque 4 — Post-escritura

- **NO actualizar `avance.md`**. Solo cuando el usuario lo pida explícitamente.
- El usuario trabaja en iteraciones; no asumir que una sección está terminada.
- Si se agregan figuras, verificar que los PDFs precompilados existen antes de compilar la sección.
- **Ofrecer una pasada de coherencia contra `STYLE.md`** antes de cerrar la sección, especialmente revisando: pasos saltados, intuición sostenida, cadencia, test del borrado, **fraseo natural (`STYLE.md §13` y 3.3.1 de este skill)**, referencias a capítulos futuros, fin de demostraciones sin marcador.
- La pasada de fraseo conviene hacerla **por separado y al final**, leyendo solo la prosa: los calcos se detectan mucho mejor releyendo oración por oración que mientras se decide contenido matemático.
- En esa pasada, barrer el verbo comodín *dar* (`STYLE.md §13.7`) con `grep -niE "\b(da|dan|daba|daban|dará|darán|dio|dieron|dando)\b" secXY.tex` y revisar caso por caso: se corrige el `dar` que expresa resultado, se deja el que es verbo propio (*"da una vuelta"*).
