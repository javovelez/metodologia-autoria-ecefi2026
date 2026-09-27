---
name: write_section
description: Protocolo para escribir una sección o subsección nueva del libro Análisis de Señales y Sistemas (Capítulo 3 en adelante) o de uno de sus apuntes. Tres bloques, lecturas previas, deliberación antes de redactar, y forma (estructura LaTeX, entornos, convenciones), más una pasada final de fraseo.
---

# Escribir una sección del libro

El skill aplica al libro del Capítulo 3 en adelante y a los apuntes (`fourier_discreto/`, `transformada_z/`). Se ejecuta en tres bloques y una pasada final. El bloque de deliberación no se saltea, porque ahí se decide lo que después sostiene la claridad del texto.

---

## Bloque 1. Lecturas previas

Antes de redactar una línea se lee, en este orden:

1. **`STYLE.md` completo.** Las Secciones 14, 15 y 16 (la oración y el párrafo, la huella de la redacción automática y el vocabulario) son las que más se degradan al redactar y se releen aunque se hayan leído en otra sesión.
2. **`DECISIONES.md`.** La lista previa y el repertorio de aperturas.
3. **`avance.md`**, la entrada del capítulo en curso y las de las secciones vecinas. De ahí salen la notación ya establecida, los ejemplos ya usados (que no se repiten), los conceptos ya definidos (que no se redefinen) y los que se definen más adelante (que no se invocan).
4. **Las secciones `.tex` vecinas**, para verificar densidad, nombres de variables y subíndices.
5. **En un apunte**, además, su guía (`fourier_discreto/fourier_discreto.md` o `transformada_z/transformada_z.md`) y `fourier_discreto/REDACCION.md`.

Se confirma la ruta de destino, `XXcapitulo/XY/secXY.tex` en el libro.

Si la sección es nueva, antes de seguir se presentan al usuario las subsecciones previstas (nombre, alcance breve, figuras) y se espera su respuesta.

---

## Bloque 2. Deliberación

La deliberación queda visible, como comentario LaTeX en la cabecera del archivo o en el chat, para que el usuario pueda corregir el rumbo antes de que se redacte el cuerpo. Las respuestas pueden ser de una línea cada una.

### 2.1. La lista de `DECISIONES.md §1`

Por cada subsección se contestan las cinco familias de preguntas: el lector, el dominio aplicado, la estructura, los pasos y el cierre.

### 2.2. La apertura

Se elige una de las cinco aperturas de `DECISIONES.md §2` y se dice en una frase por qué las otras cuatro no aplican.

### 2.3. Los cuadros `resultado`

Para cada cuadro previsto se decide si va al final, como resumen de un desarrollo, o al frente, como definición de partida (`STYLE.md §13.5`). Lo que no se permite es no decidir.

### 2.4. El vocabulario aplicado

Se listan los términos aplicados que van a aparecer y para cada uno se indica si es vocabulario seguro, si pasó el test del borrado o si no está disponible y hay que reformular (`DECISIONES.md §3`).

### 2.5. Las figuras

Se listan las figuras que la sección necesita y el punto exacto en que entra cada una, con el criterio de `STYLE.md §12`. Ante la duda, la figura se incluye.

---

## Bloque 3. Forma

### 3.1. Estructura del archivo

```latex
\documentclass[crop=false]{standalone}
\input{../../setup.tex}

\begin{document}

% Deliberación del Bloque 2.

\section{Título de la sección}
\label{sec:label_descriptivo}

% Contenido

\end{document}
```

La ruta a `setup.tex` es `../../setup.tex` desde `XXcapitulo/XY/`. En los apuntes los labels llevan el prefijo del apunte (`tz:` en Transformada Z).

### 3.2. Composición

Cada concepto relevante puede llevar apertura, definición en un cuadro `resultado`, demostración, ejemplo y figura. No es una receta lineal; se eligen y se ordenan según la deliberación. La preferencia por defecto es intuición primero (`STYLE.md §4`).

### 3.3. Mientras se redacta

Las reglas completas están en `STYLE.md`. Estas son las que más se rompen al escribir de corrido.

- **Nombrar el objeto en cada oración** (`STYLE.md §14.1`). La primera oración de cada párrafo dice de qué habla con su nombre o su símbolo. Ningún pronombre ni demostrativo apunta más atrás que la oración anterior.
- **Abrir el párrafo con una oración completa** (`STYLE.md §14.3`). Ni anuncio vacío, ni oración corta de intriga, ni *"Conviene…"*.
- **Sin em-dashes** (`STYLE.md §14.5`). Si aparece la tentación de un inciso con guiones, va entre comas, entre paréntesis o en una oración propia.
- **Dos puntos solo para enumerar o anunciar una fórmula display** (`STYLE.md §14.6`).
- **Una afirmación por oración** (`STYLE.md §14.4`).
- **Sin comprimir** (`STYLE.md §14.2`). Se escriben el verbo, el artículo y el conector que la oración necesita.
- **Sin saltear pasos** (`STYLE.md §3`), y la cuenta se escribe en display en lugar de describirse.
- **Después de un desarrollo largo, una oración que dice qué se obtuvo** (`STYLE.md §5`).
- **Vocabulario del libro** (`STYLE.md §16`): nada de *dar*, *hacer* ni *dejar* como verbos de resultado.
- **Referencias con la palabra completa** y como máximo una referencia a capítulos futuros por subsección (`STYLE.md §8`).
- **Demostraciones sin marcador de cierre.**

Si un patrón de calco o de tic aparece y no está en `STYLE.md`, se propone al usuario agregarlo ahí, que es el documento canónico, y no en este skill.

### 3.4. Notación

Consulta en `NOTATION.md`. Lo más frecuente es `j` y no `i`, `\bar{z}` y no `z^*`, `x_p`/`x_i`, `$90^\circ$`, `\vect{v}`, comillas `` ``texto'' `` y ningún carácter matemático Unicode.

### 3.5. Entornos y figuras

El cuadro `resultado` lleva título y solo el enunciado o la fórmula. El cuadro `nota` lleva advertencias, conexiones o aclaraciones de notación.

Las figuras se crean con `create_2d_figures`, `create_block_diagrams` o `3d_figures`, y se incluyen así:

```latex
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

La fracción de ancho va en el `\includestandalone` y el `minipage` se queda en `\linewidth`, para que el epígrafe tenga el ancho de los demás. Toda figura se nombra en la prosa donde el lector tiene que mirarla. Cada figura se compila en su carpeta antes de compilar la sección.

---

## Bloque 4. Después de redactar

1. **Pasada de fraseo, aparte y al final.** Se lee solo la prosa, con los barridos y la lista de `STYLE.md §17`. Se empieza por leer seguidas las primeras oraciones de todos los párrafos. Los tics de la redacción automática (`STYLE.md §15`) se detectan mucho mejor así que durante la redacción.
2. **Compilar** la sección y verificar que no queden referencias sin resolver ni cajas desbordadas.
3. **No actualizar `avance.md`**, salvo pedido del usuario o anuncio de cierre de sesión. En los apuntes se actualiza su propia guía al cerrar cada sección.
4. **Ofrecer una pasada de `review_section`** cuando la sección quede estable.
