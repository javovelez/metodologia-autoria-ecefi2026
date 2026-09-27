# Convenciones de notación

Documento de consulta. Las convenciones son estrictas, y las alternativas marcadas como incorrectas no se usan en ninguna parte del proyecto.

---

## Símbolos básicos

| Elemento | Correcto | Incorrecto | Notas |
|---|---|---|---|
| Unidad imaginaria | `j` | `i` | Convención de ingeniería; `i` se reserva para corriente eléctrica. |
| Conjugado complejo | `\bar{z}` o `\overline{z}` | `z^*` | El asterisco se evita en todo el libro. |
| Parte real | `\operatorname{Re}\{z\}` o `\text{Re}\{z\}` | `Re(z)` con paréntesis | |
| Parte imaginaria | `\operatorname{Im}\{z\}` o `\text{Im}\{z\}` | `Im(z)` con paréntesis | |
| Argumento principal | `\operatorname{Arg}(z)` | `arg(z)` | Mayúscula para principal. |

---

## Variables y subíndices

| Concepto | Notación | Notas |
|---|---|---|
| Componente par | `x_p(t)` | Subíndice en español; nunca `x_e`. |
| Componente impar | `x_i(t)` | Subíndice en español; nunca `x_o`. |
| Funciones auxiliares en demostraciones | `a(t)`, `b(t)` | Cuando se necesitan funciones par/impar auxiliares en pruebas de unicidad, usar `a` y `b` para evitar conflicto con los subíndices `p`/`i` y con `p`, `q` enteros en condiciones de racionalidad. |
| Período fundamental | `T_0` | Subíndice cero. |
| Frecuencia angular | `\omega_0` | Preferido sobre `2\pi f_0` en el cuerpo del libro. |
| Frecuencia digital | `\lambda` | Frecuencia de una secuencia, en radianes por muestra. Es el ángulo que avanza el vector giratorio entre una muestra y la siguiente. Se relaciona con el muestreo por `\lambda = \omega \Delta t` (`eq:frecuencia_digital`). El espectro de una secuencia es periódico de período `2\pi` y se grafica y se razona sobre el intervalo `[-\pi,\pi]`; el círculo se nombra pero no es la representación de trabajo. Introducida en el Capítulo 8. |
| Intervalo de muestreo | `\Delta t` | Tiempo entre muestras consecutivas. Símbolo primario del proyecto. También llamado `T_s` (*sampling time*) en la literatura en inglés; aclararlo la primera vez que aparece. |

---

## Variables complejas

| Variable | Forma | Contexto |
|---|---|---|
| Laplace | `s = \sigma + j\omega` | Tiempo continuo. |
| Z | `z = re^{j\lambda}` | Tiempo discreto. El argumento es la frecuencia digital $\lambda$, el mismo símbolo que en el resto del bloque discreto. Sobre la circunferencia de radio uno ($r=1$), $z = e^{j\lambda}$ es el punto donde se evalúa la transformada de Fourier de tiempo discreto. Nunca `\theta`. |
| Plano complejo general | `z = x + jy` | Capítulo de variable compleja. |

---

## Ángulos

- Por defecto **radianes**, expresados como fracciones de `\pi` cuando es natural (ej. `\pi/4`, `2\pi/3`).
- Cuando se calcula un resultado numérico, **aclarar la equivalencia en grados entre paréntesis** si aporta intuición geométrica (ej. *"$\theta = \pi/3$ rad ($60^\circ$)"*).
- Grado sexagesimal en modo matemático: `$90^\circ$`. **Nunca** el símbolo Unicode `°` directo.

---

## Paréntesis vs. corchetes en señales

| Tipo | Notación | Ejemplo |
|---|---|---|
| Tiempo continuo | paréntesis redondos | `x(t)` |
| Tiempo discreto | corchetes | `x[n]` |

La convención es estricta y aparece desde la sección 1.1. Nunca mezclar.

### Enumeración de una secuencia por sus valores

Una secuencia de soporte finito puede escribirse por extensión, encerrando sus valores entre llaves y marcando con una flecha (`\underset{\uparrow}{...}`) cuál corresponde a `n=0`. **Sin comas**: los elementos se separan solo con espacios (`\quad`). **Llaves comunes** `\{ \}`, no `\left\{ \right\}` (no deben crecer respecto a los números):

```latex
x[n] = \{\, 2 \quad \underset{\uparrow}{3} \quad -1 \quad 4 \,\}
```

La flecha señala `x[0]`; a la derecha van los índices positivos, a la izquierda los negativos. Fuera de los valores listados la secuencia vale cero. Es una diferencia con el tiempo continuo, que no admite enumeración directa. Introducida en el Capítulo 8 (Subsección `subsec:secuencia_clasificacion`).

---

## Codificación y formato

- Codificación de archivo: **UTF-8**.
- Comillas en LaTeX: ` ``texto'' ` (dos backticks abren, dos apóstrofos cierran). Nunca comillas rectas `"texto"`.
- Tildes y `ñ` directamente en UTF-8, no escapadas.

---

## Vectores (sentido discreto)

Un vector en sentido discreto, es decir una lista finita de coordenadas en $\mathbb{R}^n$ o $\mathbb{C}^n$, se escribe con negrita y flecha arriba.

| Elemento | Correcto | Incorrecto | Notas |
|---|---|---|---|
| Vector | `\vect{v}` | `\mathbf{v}`, `\vec{v}` solo | Macro definido en `setup.tex` que produce `\vec{\mathbf{v}}`. |
| Versor de base | `\vect{e}_k` | `\mathbf{e}_k` | El subíndice queda fuera del macro. |
| Vector nulo | `\vect{0}` | `\mathbf{0}` | |

La convención aplica solo a vectores discretos de álgebra lineal. Las señales, sean de tiempo continuo o discreto, se escriben con su notación habitual, `x(t)` o `x[n]`, sin negrita ni flecha. En los trabajos prácticos `\mathbf{...}` resalta resultados numéricos y no se toca.

---

## Operadores matemáticos personalizados

Definidos en `setup.tex`:

| Operador | Comando | Significado |
|---|---|---|
| `vect` | `\vect{x}` | Vector discreto: negrita + flecha arriba. |

---

## Entornos LaTeX

| Entorno | Color | Uso |
|---|---|---|
| `resultado` | Azul (utnblue) | Definiciones formales, fórmulas clave, resultados importantes. **Título obligatorio.** Solo enunciado/fórmula adentro. |
| `nota` | Gris | Advertencias, aplicaciones, conexiones, notación. Título opcional (por defecto: "Nota"). |

---

## Demostraciones

- **Sin símbolo de cierre**: ni `\qed`, ni `$\square$`, ni "Q.E.D.", ni "demostrado".
- Las demostraciones terminan con la última línea de razonamiento.

---

## Referencias cruzadas

En el cuerpo del libro (y en TPs y presentaciones derivadas), las referencias a partes del texto se escriben con la palabra completa.

| Elemento | Correcto | Incorrecto | Notas |
|---|---|---|---|
| Capítulo | `el Capítulo~\ref{cap05}` | `§\ref{cap05}`, `Cap.~5`, `(cf.~\ref{cap05})` | Palabra completa + `\ref{}`. |
| Sección | `la Sección~\ref{sec:serie_fourier}` | `§\ref{sec:...}`, `Sec.~5.2`, `§5.2` | |
| Subsección | `la Subsección~\ref{subsec:prop_conjugacion}` | `§\ref{subsec:...}`, `§5.3.6` | |
| Ecuación | `la ecuación~\eqref{eq:x}` | `por~\eqref{eq:x}` suelto | Minúscula. Si ya hay un sustantivo (*la fórmula de análisis~\eqref{}*), se deja. |
| Referencia genérica | `esta sección`, `el capítulo anterior` | | Minúscula y sin `\ref{}` cuando es deíctica. |

El símbolo `§` queda reservado para archivos meta del proyecto (`STYLE.md`, `DECISIONES.md`, `WORKFLOW.md`, `avance.md`, comentarios `%` de figuras). **No se usa en prosa del libro.** Detalle: `STYLE.md §8`.

---

## Señales y funciones con convención fija

| Objeto | Convención | Notas |
|---|---|---|
| Escalón unitario | $u(0)=1$ | En las figuras, disco lleno en el valor 1 en $t=0$, sin círculo abierto. |
| Peine de Dirac | $\delta^{T_0}(t)=\sum_n \delta(t-nT_0)$; en frecuencia $\delta^{\omega_0}(\omega)$ | No se usa `\sha` ni un símbolo especial. En prosa, *peine de Dirac* o *tren de impulsos*. |
| Seno cardinal | `\operatorname{sinc}(\cdot)` en las ecuaciones | En prosa *el seno cardinal*, nunca *la sinc*. |
| Soporte | Intervalo cerrado: *soporte $[-2,2]$* | Nunca como conjunto por extensión, tampoco en tiempo discreto. Con coma decimal, punto y coma como separador: $(471{,}2;\,500)$. El soporte se da siempre explícito. |
| Cociente de polinomios | Numerador $P$, denominador $Q$ | Uniforme en todo el libro, en $s$ y en $z$. |
| Residuos de fracciones simples | Una letra por polo: $A$, $B$, $C$ | Polo múltiple con subíndice de potencia; par complejo $A$ y $\bar A$. |
| Ganancia de la forma factorizada | $K$ | |
| Cociente de una división impropia | $E(s)$, con resto $R(s)$ | $Q$ queda para el denominador. |
| Coeficientes de una ecuación diferencial o en diferencias | $a_k$ (salida), $b_k$ (entrada) | |
| Coeficientes de Fourier | $c_k$; $d_k$ para la salida de un sistema | $a_k$, $b_k$ solo dentro de la serie trigonométrica. |
| Abreviaturas | SFTC, TFTC, TL, TFTD, DFT, FFT | La transformada Z no lleva abreviatura en el apunte. |

---

## Caracteres y codificación en los `.tex`

Nunca se pegan caracteres matemáticos Unicode (flechas, $\leq$, $\infty$, $\pi$, el símbolo de grado). El proyecto compila con `T1 fontenc`, que no los representa, y el error aparece recién al compilar el capítulo entero. Se usa la macro de LaTeX (`\leftrightarrow`, `\to`, `\leq`, `\infty`, `\pi`, `^\circ`) o se dice con palabras. Tampoco se usa el em-dash Unicode; ver `STYLE.md §14.5`.
