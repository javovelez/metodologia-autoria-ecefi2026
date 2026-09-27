---
name: create_2d_figures
description: Protocolo para crear figuras 2D con TikZ/pgfplots como archivos standalone, garantizando coherencia visual y técnica (colores con significado pedagógico, layering, tipografía, sizing, multi-panel). Aplica al libro, TPs y presentaciones.
---

# Create 2D Figure. Standard Protocol

Este skill aplica a la creación de **una figura 2D** como archivo standalone. Cubre desde la decisión de qué muestra la figura hasta la receta técnica para que se vea correctamente cuando se incluye en el documento padre.

El skill se ejecuta en tres bloques.

---

## Bloque 1. Pre-flight

### 1.0. Triaje

Clasificar la figura antes de leer nada más. El tipo determina qué partes del skill se aplican:

| Tipo | Caso | Lecturas | Deliberación |
|---|---|---|---|
| **A. Simple** | 1 panel, 1–2 curvas, dominio/imagen conocidos | NOTATION + prosa adyacente | Saltar Bloque 2; ir directo a Bloque 5 |
| **B. Geométrica** | Plano complejo, regiones, mapeos, fasores | NOTATION + prosa adyacente | Solo Bloque 2.1; luego Bloque 5 |
| **C. Multipanel** | 2+ paneles relacionados | Las cuatro lecturas de §1.1 | Bloques 2 y 4 completos |

### 1.1. Lecturas obligatorias

Antes de escribir una sola línea TikZ (con el alcance que marca el tipo en §1.0):

1. **`STYLE.md §12`**, sobre cómo la prosa usa las figuras. El criterio del libro es generoso: toda gráfica que ayude a seguir un concepto con geometría o evolución temporal se incluye. Si después de leer la prosa que la rodea no se puede decir qué ayuda a ver la figura, se aclara eso antes de trazarla.
2. **`NOTATION.md`**: las convenciones de notación aplican también a etiquetas de la figura: `j` no `i`, `\bar{z}` no `z^*`, `$90^\circ$` no `°`, `x_p / x_i` para par/impar, paréntesis para tiempo continuo y corchetes para discreto.
3. **El texto que rodea a la figura**: la figura no se diseña en el vacío. Leer el párrafo que la introduce y el que la sigue para alinear lo que la figura muestra con lo que el texto dice.
4. **Figuras vecinas existentes** en el mismo capítulo o sección para mantener coherencia visual: rangos de ejes comparables, paleta, escala tipográfica, convenciones de etiquetas.

Confirmar la ruta de destino: `XXcapitulo/XY/figures/fig_nombre/fig_nombre.tex` para libro, o la equivalente para TP o presentación.

---

## Bloque 2. Deliberación

### 2.1. ¿Qué resuelve esta figura?

Contestar en una frase: *"Esta figura existe para que el lector vea \_\_\_, que el texto solo describe en palabras."* Si no podés llenar el blanco con algo concreto, la figura es decorativa y no se hace.

Casos típicos donde la figura paga:

- **Geometría**: un mapeo, una región del plano complejo, un fasor, una distancia entre puntos.
- **Evolución temporal**: cómo varía una señal con el tiempo, especialmente cuando hay parámetros (amplitud, fase, frecuencia).
- **Comparación visual**: dos señales lado a lado donde el contraste es lo que enseña.
- **Estructura**: un diagrama de bloques que muestra cómo se conectan partes.

### 2.2. Test del borrado visual

Listar los elementos que pensás incluir y, para cada uno que no sea imprescindible (cuadrículas, ejes secundarios, anotaciones, leyendas), preguntar: ¿la figura sigue contando lo mismo si lo saco? Si sí, sacarlo.

Elementos prohibidos por defecto:

- **Texto descriptivo dentro de los paneles**: títulos tipo "Plano Z", "Dominio", "Salida", o leyendas explicativas. Los paneles se identifican únicamente con un marcador `(a)`, `(b)`, `(c)` (ver §3.8). La descripción de cada panel va en el `\caption` del documento padre, en la forma "(a) Plano Z. (b) Plano W. ...".
- **Decoraciones que no aporten información** (sombras, bordes redondeados, fondos).
- **Colores sin significado**: ver §2 más abajo, "cada color debe tener un significado pedagógico".

### 2.3. Coherencia con figuras vecinas

Si la sección o capítulo tiene figuras previas que comparten objeto (por ejemplo, varias representaciones del mismo sistema), mantener:

- Rangos de ejes consistentes cuando sea posible.
- Misma convención de colores (ver §2).
- Misma escala tipográfica.

### 2.4. ¿Color o escala de grises?

Diseñar primero **sin depender del color**: las curvas se distinguen también por estilo (sólida, punteada, trazo) además del color. El proyecto usa una opción global para conmutar a gris (`\PassOptionsToPackage{gray}{xcolor}`); la figura debe seguir siendo legible cuando se aplica.

Si la figura **necesita** color para funcionar (ej. mapa de calor), aceptarlo. Pero la mayoría de las figuras 2D del libro no lo necesitan.

---

## Bloque 3. Forma técnica

### 3.1. Estructura del archivo standalone

Toda figura es un archivo standalone en su propio directorio `figures/fig_nombre/fig_nombre.tex`. Siempre incluir el `setup.tex` global para heredar paquetes y definiciones de color.

```latex
\documentclass[border=5mm]{standalone}
\input{../../../../setup.tex}
% \PassOptionsToPackage{gray}{xcolor}

\begin{document}
    \begin{tikzpicture}[>=Latex, scale=1.0, font=\small, auto]
        % Código aquí
    \end{tikzpicture}
\end{document}
```

- Ruta a `setup.tex`: `../../../../setup.tex` (cuatro niveles arriba desde `figures/fig_nombre/`).
- `border=5mm` previene recortes de etiquetas que se extienden más allá del área principal.
- La línea `\PassOptionsToPackage{gray}{xcolor}` queda comentada; se activa puntualmente para previsualizar en escala de grises.

### 3.2. Convención de naming

El nombre de carpeta y archivo coincide con el `\label{}` reemplazando los dos puntos por guión bajo:

| Label | Carpeta y archivo |
|---|---|
| `\label{fig:semiplanos}` | `fig_semiplanos/fig_semiplanos.tex` |
| `\label{fig:mapeo_polar}` | `fig_mapeo_polar/fig_mapeo_polar.tex` |

### 3.3. Colores con significado pedagógico

**Cada color debe tener un significado pedagógico. Nunca agregar variedad por razones estéticas.**

| Color | Significado |
|---|---|
| `utnblue` | Señal original o de referencia; entrada de un sistema |
| `red!80!black` | Señal transformada (desplazada, escalada, rebatida); salida de un sistema; respuesta al impulso $h$ en la convolución |
| `black` | Señal resultado de una operación (suma, producto, etc.) |
| `gray` | Anotaciones, flechas auxiliares |
| `cyan!15` | Regiones sombreadas |

En la prosa y en los epígrafes, `red!80!black` se nombra *rojo*, nunca *naranja*. La pareja entrada azul y salida roja viene de `fig_bibo` (Sección 4.1) y se mantiene en todo el libro.

Solo usar un tercer color (`orange!80!black`) si **dos señales transformadas distintas aparecen en el mismo panel** y deben distinguirse. Paneles apilados verticalmente **no** necesitan colores distintos entre sí.

### 3.4. ylabel horizontal

En `pgfplots`, el `ylabel` siempre va horizontal en la esquina superior izquierda del panel. Nunca rotado ni en posición vertical default:

```latex
ylabel style={font=\small, rotate=0, anchor=south east,
              at={(axis description cs:0,1)}}
```

Nunca usar `rotate=-90` ni el ylabel vertical por defecto.

### 3.5. Ejes y trazo

- **Estilo de ejes**: `[->, thin, black]` (grosor `thin` ≈ 0.4 pt). **No usar `thick`**, porque los ejes se ven gruesos frente al cuerpo del texto.
- **Cabeza de flecha**: `>={Latex[length=3pt,width=3pt]}` en las opciones del `tikzpicture` (cabezas chicas que no compitan visualmente con la curva).
- **Etiquetas en los extremos**: `node[right] {Re}`, `node[above] {Im}`.

### 3.5.1. Trazo de curvas y rampas

- **Curvas funcionales** (`\addplot` con `samples` y `domain`): `semithick` (≈ 0.6 pt). **No usar `thick` ni `very thick`**, porque distrae frente al texto.
- **Curvas con saltos / rampas piecewise** (`\addplot coordinates`): igual, `semithick`.
- Si una curva debe destacar como protagonista frente a otra de referencia, **diferenciar por color** (paleta de §3.3), no por grosor.

### 3.6. Layering (Painter's Algorithm)

Los objetos se dibujan en este orden estricto:

1. **Backgrounds / grids**: líneas de coordenadas o cuadrículas base.
2. **Regiones / fills**: comandos `\fill` para áreas (regiones de estabilidad, discos unitarios, etc.).
3. **Axes y curvas principales**: comandos `\draw` para ejes ($x, y, \sigma, j\omega$) y curvas de funciones primarias. **Los ejes deben ser visibles por encima de los fills.**
4. **Anotaciones**: puntos (`\fill circle`), etiquetas (`\node`), vectores (`\draw[->]`).

### 3.7. Geometría y composición

- **Consistencia de ejes**: ejes con longitudes comparables entre subfiguras (si Panel A usa `[-2.5, 2.5]`, Panel B idealmente lo mismo) para mantener escala visual.
- **Regiones infinitas**: al representar regiones infinitas (semiplanos), alinear el borde del sombreado exactamente con los límites del eje para crear un efecto de "ventana" limpio. Evitar que el sombreado se extienda más allá de las flechas de los ejes.

### 3.8. Tipografía y marcador de panel

- **Un solo cuerpo en toda la figura: `\footnotesize`.** Van en `\footnotesize` los ticks, el marcador de panel, `label style`, los nodos internos y el `font` global del `tikzpicture`. Tener los ticks en `\scriptsize` y el marcador en `\footnotesize` es el defecto habitual y se nota. Esta regla (fijada el 2026-09-10) reemplaza a la anterior, que variaba el cuerpo según la densidad de paneles. El tamaño de la figura se ajusta con las dimensiones de pgfplots y no con el cuerpo de letra (ver §4.1).
- Modo matemático para todas las variables: `$z$`, `$w$`, `$\omega$`.
- **Marcador de panel**: en figuras multi-panel, cada panel se identifica con un marcador `(a)`, `(b)`, `(c)`. Reglas duras:
    - **Solo el marcador**: nunca texto descriptivo dentro del panel ("Plano Z", "Dominio", "Salida"). La descripción va en el `\caption` con la convención `(a) Plano Z. (b) Plano W. ...`.
    - **Posición según geometría**:
        - **Pocos paneles, separados (1–3 paneles, o columnas con holgura)**: **arriba y centrado horizontalmente** respecto al área de la gráfica. Realización en pgfplots: `title style={font=\footnotesize, yshift=-2pt}`.
        - **Grid 2×N apilado (N≥4 filas), o cualquier figura compacta donde el marker arriba se confundiría entre filas**: **dentro del panel, esquina superior derecha**. Es inequívoco a qué panel pertenece. Realización en pgfplots: `title style={font=\scriptsize, at={(axis description cs:1.0, 1.0)}, anchor=north east, xshift=-3pt, yshift=-2pt}`.
    - **Estilo plano**: sin negrita, sin caja, sin color.
    - **Consistencia**: la misma posición en todos los paneles de la figura.

### 3.9. Detalles técnicos de pgfplots

- **Impulsos.** Se trazan como flechas finas con `\draw[impulso] (axis cs:x,0) -- (axis cs:x,h);`, definiendo `impulso/.style={<color>, line width=0.7pt, -{Latex[length=2.8pt,width=2.4pt]}}` (requiere `arrows.meta`). La punta `Latex` por defecto y `very thick` quedan gruesas.
- **Nunca `\foreach` para trazar dentro de un `axis` o `\nextgroupplot`.** pgfplots difiere los `\draw` hasta cerrar el eje y la variable del ciclo ya no existe. Se escriben los `\draw` uno por uno.
- **`axis on top`** cuando hay `\fill` que taparía los ejes.
- **Nombres de estilos propios** sin colisión con claves de TikZ (nada de `step`, `grid`, `arc`).
- **`height` incluye título y etiquetas**, no solo la caja de datos. En un `groupplot` apilado con título y `xlabel` por panel, `height=2.7cm` deja una caja de 1,33 cm. Si los paneles se ven como tiras, medir la caja real antes de tocar el `width`. Un `ymax` muy por encima del máximo tiene el mismo efecto.
- **Grilla horizontal sin eje de ordenadas.** `axis y line=none` suprime también la grilla. Se usa `axis y line=left` con `y axis line style={draw=none}`, `ytick style={draw=none}`, `yticklabels={}`, `ymajorgrids=true` y `ytick` explícito.
- **Línea vertical de referencia en el origen.** Se traza con `\draw[gray!55, thin, dashed] (axis cs:0,0) -- (axis cs:0,\pgfkeysvalueof{/pgfplots/ymax});`, desde $y=0$ hacia arriba. Un `extra x ticks` tapa el `0`.
- **Stems negativos que cruzan las etiquetas del eje.** Hacen falta `axis on top` y un relleno opaco en la etiqueta (`inner sep=0.9pt`) del color del fondo local, que no siempre es blanco (dentro de una franja `cyan!15` es `cyan!15`).

### 3.10. Convenciones de contenido

- **Escalón.** $u(0)=1$, con disco lleno en el valor 1 en $t=0$ y sin círculo abierto.
- **Ejes con números.** La figura lleva valores numéricos reales en los ejes (por ejemplo $8\pi$, $16\pi$ rad/s), el origen marcado con $0$, el eje de ordenadas trazado y visibles las cantidades de referencia que la prosa nombra. Símbolo y número pueden convivir, con el número en la marca y el símbolo como etiqueta.
- **Paneles que la prosa compara llevan la misma escala.** Si el texto compara entrada con salida, los paneles comparten la unidad de los dos ejes (`x=0.62cm, y=0.24cm` en un estilo común) y cada uno recorta su rango vertical. Eso obliga a dejar `groupplot` y encadenar ejes con `at={($(pa.south west)+(0,-1.15cm)$)}, anchor=north west`. Con rangos negativos, la etiqueta del eje $x$ se ancla con `xlabel style={at={(axis cs:<xmax>,0)}}`.
- **Catálogo de aportes de polos.** Una figura por caso, con el polo en el plano a la izquierda, el conector $\mathcal{L}^{-1}$ en gris y la forma de onda a la derecha. Nada de grillas combinadas. Las curvas crecientes o inestables llenan el cuadro y llegan cerca del borde superior, sin flecha de continuación ni `\clip`.
- **Figuras para el banco de Moodle.** No se reutiliza una figura del libro si sus etiquetas o su epígrafe revelan la respuesta; se crea una propia (ver `Moodle/README.md`).

---

## Bloque 4. Sizing y multi-panel (crítico)

### 4.1. Tipografía consistente: por qué importa el tamaño

El libro tiene `\textwidth` de 472 pt. Para que la letra de todas las figuras se imprima del mismo tamaño, la escala de inclusión tiene que ser 1,0, es decir que el ancho natural del PDF standalone coincida con el ancho con que se incluye. Con el standalone a 10 pt de base y `\footnotesize`, eso imprime 8 pt, que es el objetivo.

**El procedimiento es medir, no calcular.** Se compila el standalone, se lee `pdfinfo fig.pdf | grep "Page size"` y se fija la fracción de `\linewidth` como ancho natural dividido 472 pt. Después se verifica en el `.log` del documento, que trae el tamaño natural y el pedido de cada figura. Subir la letra declarada y bajar el ancho de inclusión en la misma proporción no cambia nada; lo que manda es la razón entre el cuerpo declarado y las dimensiones en cm del trazado.

Dos trampas verificadas. Una figura puede estar compartida entre el libro y un apunte o una clase por ruta relativa, así que un cambio de letra se ve en todos lados y hay que preguntar antes el alcance. Y con la letra en 8 pt, una fracción en un tick puede chocar con la vecina; se sube el `height` del panel, que no afecta el ancho.

Los presets siguientes son un punto de partida, y la fracción final sale de la medición.

**Presets cerrados** (elegir, no calcular):

| Preset | Caso | width pgfplots | height por panel | Aspect por panel | Inclusión |
|---|---|---|---|---|---|
| **S1** | Panel único, ancho completo | 13 cm | 5–6 cm | ~2.3:1 | `width=0.85\linewidth` |
| **S2** | 2 paneles en columnas | 6 cm c/u | 5 cm | ~1.2:1 | `width=0.85\linewidth` |
| **S3** | 2 paneles apilados | 10 cm | 4.5 cm | ~2.2:1 | `width=0.65\linewidth` |
| **S4** | 3 paneles apilados | 9 cm | 4 cm | ~2.3:1 | `width=0.6\linewidth` |
| **S5** | 4+ paneles apilados | 8 cm | 3.5 cm | ~2.3:1 | `width=0.55\linewidth` |
| **S6** | Lateral angosta | 8 cm | 5 cm | ~1.6:1 | `width=0.55\linewidth` |
| **S7** | Grid 2 cols × 5–6 filas | 5.5 cm c/u | 3.6 cm | ~1.5:1 | `width=0.70\linewidth` |

Con estos valores el ancho del PDF standalone queda cerca del ancho de inclusión y la escala cerca de 1,0.

**Regla anti-apaisado en apilados**: cuando hay varias filas, **no** usar `width=13cm` con altura pequeña por panel, porque deforma cada panel en una tira horizontal. Mantener aspect por panel ≤ 2.5:1 y achicar el ancho de inclusión en consecuencia (S3–S5). El cumplimiento de §4.2 ("evitar tiras horizontales alargadas") se da por construcción si se respeta el preset.

**Multi-panel con rangos distintos** (ver §4.3 Regla B): la **escala vertical del preset es la misma para todos los paneles**; solo varían los límites $y_\text{top}, y_\text{bottom}$ ajustados a cada función. La igualdad de altura sale por construcción, sin calcular cm/unidad caso por caso.

**Nunca** usar `width=\linewidth` cuando el ancho del pgfplots es mucho menor que `\textwidth`: una figura de 9 cm incluida a `\linewidth` = 16 cm escala fuentes 1.8×, haciéndolas más grandes que los títulos.

### 4.2. Orientación: columnas vs apilado

Cuando una figura tiene múltiples paneles, la orientación por defecto es **lado a lado (columnas)**. La orientación **apilada (vertical)** solo se justifica cuando la figura requiere que el lector lea un mismo instante temporal $t$ simultáneamente en varias señales, alineándolas verticalmente.

| Orientación | Cuándo usarla |
|---|---|
| **Columnas (default)** | Contrastar situaciones independientes (estable vs inestable, lineal vs no lineal, antes vs después), comparar regímenes de un parámetro, diagramas espaciales/geométricos, o cualquier figura cuyos paneles cuenten historias relacionadas pero separadas. |
| **Apilado** | Solo cuando la alineación temporal es el mensaje: mostrar una entrada junto a su respuesta, o varias versiones desplazadas de una misma señal donde el corrimiento se lee verticalmente. |

Esta regla es independiente del número de paneles: una figura de dos paneles también se orienta así. Las tiras horizontales alargadas (paneles apilados de mucho ancho y poca altura) desperdician espacio y se ven poco profesionales. Se evitan salvo que la alineación temporal lo exija.

### 4.3. Multi-panel: igualdad de área visual

Cuando una figura tiene múltiples paneles lado a lado, todos deben tener **igual área visual** (mismo ancho × misma altura en cm). Como el ancho horizontal suele ser igual (mismo dominio), la igualdad de área se reduce a **igualdad de altura**.

#### Regla A. Dominios e imágenes similares → mismo plano

Si todas las funciones tienen dominios y rangos de imagen comparables, usar **los mismos límites de eje** en todos los paneles. Esto permite comparación directa.

#### Regla B. Rangos distintos → ejes ajustados, igual altura

Si un panel tiene un rango de imagen muy distinto (una función siempre positiva frente a una antisimétrica, o magnitudes que difieren más de 2×):

1. **Escala de amplitud única**: usar el mismo factor cm/unidad en todos los paneles.
2. **Límites del eje ajustados por función**: cada panel cubre el rango de su función con un margen pequeño, sin espacio en blanco artificial.
3. **Misma altura total**: elegir los límites de eje superior e inferior de cada panel de modo que `(y_top − y_bottom)` sea idéntico en cm para todos.
4. **El eje de abscisas puede quedar en distinta altura dentro de cada panel.** Por ejemplo, en una función positiva el eje t queda cerca del borde inferior; en una función antisimétrica queda en el centro. Esto es correcto y no hace falta alinear el eje t entre paneles.
5. **Nunca agregar espacio vacío** para igualar los ejes entre paneles; ajustar los límites en cambio.

#### Ejemplo trabajado

| Panel | Función | Rango en valor | Escala | y-eje (cm) | Altura |
|---|---|---|---|---|---|
| (a) | $e^t$ | $[0,\ e^{2.2}]$ | 0.5 | $-0.25$ a $4.75$ | 5.0 cm |
| (b) | $\cosh t$ | $[1,\ \cosh 2.2]$ | 0.5 | $-0.25$ a $4.75$ | 5.0 cm |
| (c) | $\sinh t$ | $[-\sinh 2.2,\ \sinh 2.2]$ | 0.5 | $-2.5$ a $2.5$ | 5.0 cm |

Los paneles (a) y (b) comparten el mismo plano (mismo rango de imagen efectivo y misma escala). El panel (c) usa el eje t centrado. Los tres miden 5.0 cm de alto.

#### Checklist rápido

| ¿Dominios e imágenes similares? | Acción |
|---|---|
| Sí | Mismos límites de eje y escala en todos los paneles |
| No | Misma escala de amplitud; límites del eje ajustados por función; alturas iguales |

---

## Bloque 5. Plantilla y compilación

### 5.1. Esqueleto con layering pre-cocido

Los cuatro niveles del Painter's Algorithm (§3.6) ya van rotulados. El modelo rellena, no decide el orden.

```latex
\begin{tikzpicture}[>=Latex, font=\footnotesize]
    \tikzset{
        region_style/.style={fill=utnblue!20, draw=none},
        axis_style/.style={->, thin, black},
    }

    % Panel (a)
    \begin{scope}
        % --- 1. Grids / backgrounds ---
        % --- 2. Fills / regiones ---
        \fill[region_style] ... ;
        % --- 3. Ejes y curvas principales ---
        \draw[axis_style] (-2,0) -- (2,0) node[right] {$x$};
        \draw[axis_style] (0,-2) -- (0,2) node[above] {$y$};
        % --- 4. Anotaciones ---
        \node[anchor=south] at (0, 2.3) {(a)};   % marcador arriba, centrado
    \end{scope}

    % Panel (b), variante en columnas (lado a lado)
    \begin{scope}[shift={(6,0)}]
        % --- 1. Grids / backgrounds ---
        % --- 2. Fills / regiones ---
        \fill[region_style] ... ;
        % --- 3. Ejes y curvas principales ---
        \draw[axis_style] (-2,0) -- (2,0) node[right] {$u$};
        \draw[axis_style] (0,-2) -- (0,2) node[above] {$v$};
        % --- 4. Anotaciones ---
        \node[anchor=south] at (0, 2.3) {(b)};
    \end{scope}

    % Variante apilada (alineación temporal):
    %   \begin{scope}[shift={(0,-5)}]   % Panel (b) abajo del (a)
    %       ...
    %       \node[anchor=south] at (0, 2.3) {(b)};
    %   \end{scope}
\end{tikzpicture}
```

**Marcador en pgfplots** (cuando el panel es un `axis` o `groupplot`):

```latex
\nextgroupplot[
    title={(a)},
    title style={font=\footnotesize, yshift=-2pt, anchor=south},
    ...
]
```

La descripción de cada panel ("Plano Z", "Plano W", "Entrada", "Salida", etc.) va en el `\caption` del documento padre, **nunca** dentro del panel.

### 5.2. Compilación

```bash
cd XXcapitulo/XY/figures/fig_nombre/
pdflatex fig_nombre.tex
```

Verificar el PDF resultante:

- Que no haya recortes de etiquetas.
- Que las proporciones sean razonables.
- Que el tamaño visual sea apropiado al rol (figura grande para protagonistas, chica para auxiliares).
- En modo gris (descomentar `\PassOptionsToPackage{gray}{xcolor}` y recompilar), que las curvas sigan distinguiéndose.

### 5.3. Inclusión en el documento padre

**Siempre colocar `\caption` y `\label` dentro del `minipage`.** Esto asegura que la figura y su caption se mantengan juntos en la misma página.

```latex
\begin{figure}[H]
    \centering
    \begin{minipage}{\linewidth}
        \centering
        \includestandalone[width=0.85\linewidth]{figures/fig_nombre/fig_nombre}
        \caption{Descripción de la figura.}
        \label{fig:fig_nombre}
    \end{minipage}
\end{figure}
```

**¿Por qué dentro del `minipage`?** El `minipage` actúa como contenedor inseparable. Al colocar la imagen y el caption adentro, LaTeX los trata como una unidad y nunca los corta entre páginas.

**La fracción de ancho va en el `\includestandalone` y el `minipage` se queda en `\linewidth`.** Un `\begin{minipage}{0.62\linewidth}` achica también el epígrafe, que queda en una columna angosta desalineada con los demás. Para buscar el defecto, `grep -rn "minipage}{0\." --include="*.tex"`.

**Tablas.** En un `table[H]` el `\caption` y el `\label` van arriba del `tabular` (en las figuras van abajo), y todo va dentro de un `minipage` de `\linewidth` para que la tabla no se parta. Con celdas `p{}` de dos líneas, `\renewcommand{\arraystretch}{1.25}` y `\\[10pt]` entre filas.

Toda figura debe tener `\label{}` y ser referenciada explícitamente desde el texto con `\ref{}` o `\autoref{}`.

### 5.4. Errores frecuentes y corrección rápida

Antes de iniciar otro ciclo de compilación, chequear esta tabla:

| Síntoma | Fix |
|---|---|
| Etiqueta recortada en el borde | Subir `border=5mm` a `8mm` o `10mm` |
| Eje invisible bajo un fill | Reordenar: fill antes que draw (Bloque 3.6) |
| Fuentes 1.5–2× más grandes que el cuerpo | Bajar la fracción de `\linewidth` o subir `width` pgfplots según preset (§4.1) |
| Paneles apilados con aspecto deforme (tira horizontal) | Usar preset S3–S5: achicar `width` y la fracción de `\linewidth` |
| Paneles con alturas distintas | Verificar que la escala cm/unidad coincide entre paneles (§4.3 Regla B) |
| Texto descriptivo "Plano Z" en panel | Reemplazar por marcador `(a)` arriba centrado; mover descripción al `\caption` |
| Marcador `(a)` en posición distinta entre paneles | Unificar la posición en todos los paneles (§3.8) |
| `Undefined control sequence: axis cs:\x` | Un `\foreach` dibuja dentro de un eje; desenrollarlo (§3.9) |
| `The key '/tikz/step' requires a value` | Un estilo propio se llama `step`, `grid` o `arc`; renombrarlo (§3.9) |
| Epígrafe angosto | La fracción va en el `\includestandalone`, no en el `minipage` (§5.3) |
| Letra de tamaño distinto entre figuras | Medir la escala de inclusión y llevarla a 1,0 (§4.1) |

---

## Bloque 6. Post-creación

- Confirmar que el PDF de la figura existe en `figures/fig_nombre/fig_nombre.pdf` (precompilado).
- Si la figura va a usarse también en una presentación, verificar que la ruta relativa desde `Presentaciones/claseXX/` resuelve correctamente.
- Si la figura cambió rangos, etiquetas o convenciones respecto a una versión anterior, verificar que las referencias del texto siguen siendo correctas (un eje renombrado puede romper la prosa que lo describía).
