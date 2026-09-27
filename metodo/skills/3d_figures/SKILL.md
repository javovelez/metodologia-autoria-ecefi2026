---
name: 3d_figures
description: Protocolo para visualizar funciones racionales (polos y ceros) en 3D con pgfplots, con escalado no lineal de color para que los ceros sean visibles junto a polos. Cubre clipping de polos, layout multi-panel apilado y dominios mixtos (agujeros circulares en dominios cuadrados).
---

# Rational Function 3D Visualization Protocol

Este skill se especializa en visualizar funciones racionales de transferencia $H(z)$ o $H(s)$ en 3D. El objetivo es mostrar **polos** (picos infinitos) y **ceros** (nivel del suelo) en el mismo plot, lo que requiere técnicas específicas de escalado.

---

## Bloque 1. Pre-flight

1. **`STYLE.md §12`** y **`NOTATION.md`**, igual que en las figuras 2D.
2. **El texto que rodea a la figura.** La superficie 3D casi siempre va junto a un diagrama de polos y ceros 2D y un par de cortes 2D. Confirmar qué cuenta cada figura del conjunto para no duplicar.
3. **La función racional concreta.** Hay que saber cuáles son los polos, cuáles los ceros, dónde está cada singularidad, qué rango del plano captura la información relevante.

---

## Bloque 2. Deliberación

### 2.1. ¿La superficie 3D paga su lugar?

Si la información que aportaría ya está clara desde un diagrama de polos y ceros 2D, **no se hace la superficie 3D**. La superficie es costosa en atención del lector y en tiempo de compilación; debe pagar.

Casos donde paga:

- El lector está aprendiendo a "leer" funciones racionales por primera vez y la superficie es el puente entre el diagrama PZ y la magnitud.
- Hay simetrías o valles entre polos que un PZ no captura.
- La figura se usa como referencia recurrente: vale el costo si se vuelve a ella.

### 2.2. Coherencia entre figuras del mismo conjunto

Si una sección presenta varias superficies (por ejemplo, $H_1$ y $H_2$), mantener:

- **Misma `zmax`**: para que las alturas relativas sean comparables visualmente.
- **Mismo rango del plano**: para que los polos en posiciones distintas sean comparables.
- **Mismo `view`**: para que el lector no tenga que reorientarse entre figuras.

---

## Bloque 3. Forma técnica

### 3.1. Escalado no lineal de color (crítico)

Para que los ceros sean visibles contra el terreno alto que rodea los polos, **es obligatorio** un escalado no lineal del color map. Una raíz de potencia (por ejemplo $z^{0.25}$) expande el rango de color para valores bajos de magnitud.

**Uso:**

```latex
\addplot3[
    surf,
    opacity=0.85,
    point meta={pow(z,0.25)} % <--- CRÍTICO PARA VISIBILIDAD DE CEROS
] { ... };
```

Sin esto, los ceros quedan indistinguibles del fondo y el lector pierde la mitad del mensaje.

### 3.2. Configuración del axis

```latex
\begin{axis}[
    name=plotA,
    view={55}{25},
    width=10cm, height=8cm,
    zmin=0, zmax=10,
    axis lines=box,
    xtick={...}, ytick={...}, ztick={...},
    colormap/viridis,
    shader=interp,
]
    \addplot3[surf, opacity=0.85, point meta={pow(z,0.25)}] {
        min(10, abs_funcion_formula)
    };
\end{axis}
```

Puntos clave:

- **`view={55}{25}`** es el ángulo estándar del proyecto.
- **`colormap/viridis`** y **`shader=interp`** dan el aspecto visual del libro.
- **Clipping**: `min(zmax, expression)` corta los polos infinitos a una altura plana.

### 3.3. Implementación de la matemática

- **Fórmula de magnitud**: calcularla explícitamente con `sqrt((x-x0)^2 + (y-y0)^2)`.
- **Suavizado anti-singularidad**: agregar un epsilon pequeño (ej. `+0.001`) en el denominador para prevenir errores de división por cero al muestrear sobre polos exactos.
- **Resolución**: `samples=65` o más para una superficie suave. Bajar la resolución es **arriesgado en superficies con polos**: un cero puede caer entre puntos de muestreo y desaparecer visualmente, o los picos pueden verse dentados. Si la compilación es lenta, antes de bajar `samples` considerar reducir el rango del dominio o usar `\pgfplotsset{compat=1.18}` (ya en `setup.tex`) para optimizaciones del renderer.

### 3.4. Etiquetas externas

Las etiquetas estándar de `pgfplots` 3D (`xlabel`, `ylabel`, `zlabel`) se renderizan rotadas e ilegibles. Usar nodos externos posicionados respecto a los anclajes del axis:

```latex
\node[anchor=north east, font=\footnotesize] at (plotA.outer south west)
    [xshift=2cm, yshift=0.3cm] {Re};
```

Si una etiqueta queda recortada o solapada, ajustar los offsets `xshift` y `yshift` en lugar de cambiar el método.

### 3.5. Layout multi-panel

Si se muestran múltiples casos (por ejemplo (a) y (b)), apilarlos **verticalmente** para que entren en los márgenes de la página:

```latex
% Panel A
\begin{axis}[name=plotA, ... ] ... \end{axis}

% Panel B (apilado debajo)
\begin{axis}[
    name=plotB,
    at={($(plotA.south)-(0,1.5cm)$)}, % gap de 1.5cm bajo plotA
    anchor=north,
    ...
] ... \end{axis}
```

El gap de 1.5cm es el estándar del proyecto. Mantener ese valor para coherencia entre figuras 3D del libro.

### 3.6. Bordes mixtos: agujero circular en dominio cuadrado

Cuando se grafica una función sobre un dominio rectangular con un agujero circular (por ejemplo, convergencia exterior de Laurent), las cuadrículas polares o rectangulares estándar fallan en producir bordes limpios en ambas fronteras simultáneamente.

**Solución: parametrización por interpolación transfinita.**

Usar `\addplot3` con `variable=u` (radial) y `variable y=v` (angular), extrayendo la lógica de coordenadas para mapear suavemente un círculo a un cuadrado.

- **`u`**: factor de interpolación radial (0 a 1).
- **`v`**: ángulo (0 a 360).
- **Math**: transformar el círculo unitario ($r=1$) al borde de un cuadrado (radio máximo en las esquinas).

```latex
\addplot3[
    surf,
    opacity=0.85,
    samples=30,      % Resolución radial
    samples y=72,    % Resolución angular (alta para esquinas)
    domain=0:1,      % u: 0 = círculo interior, 1 = cuadrado exterior
    domain y=0:360,  % v: ángulo
    z buffer=sort,
    variable=u,
    variable y=v
] (
    % Coordenada X por interpolación transfinita
    % Mapea r=1 a [-L, L] (donde L=2 en este ejemplo)
    { (1 + u * (L/max(abs(cos(v)), abs(sin(v))) - 1)) * cos(v) },

    % Coordenada Y
    { (1 + u * (L/max(abs(cos(v)), abs(sin(v))) - 1)) * sin(v) },

    % Coordenada Z (función)
    % Recalcular 'x' y 'y' o 'r' usando la fórmula de interpolación de arriba
    { f(x, y) }
);
```

---

## Bloque 4. Compilación e inclusión

### 4.1. Compilación

```bash
cd XXcapitulo/XY/figures/fig_nombre/
pdflatex fig_nombre.tex
```

Las superficies 3D pueden tomar tiempo significativo de compilación. Aceptable: 5–60 segundos. Si tarda demasiado, **antes de tocar `samples`** (que puede degradar la visibilidad de ceros), reducir el rango del dominio o desactivar temporalmente otros plots de la sesión.

### 4.2. Inclusión en el documento padre

Igual que figuras 2D, con `\caption` y `\label` dentro del `minipage`:

```latex
\begin{figure}[H]
    \centering
    \begin{minipage}{\linewidth}
        \centering
        \includestandalone[width=0.85\linewidth]{figures/fig_nombre/fig_nombre}
        \caption{Descripción de la superficie.}
        \label{fig:fig_nombre}
    \end{minipage}
\end{figure}
```

---

## Bloque 5. Post-creación

- Verificar que el PDF muestra los polos como picos legibles **y** los ceros como valles claros (no como fondo plano).
- Si la superficie va acompañada de cortes 2D o de un diagrama PZ, verificar que el conjunto cuenta una historia coherente: el lector debe poder mirar el 3D, mirar el corte, y ver la correspondencia.
- Si la figura cambia, regenerar el PDF antes de compilar el documento padre.
