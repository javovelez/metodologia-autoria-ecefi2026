# Convenciones de Notación — Análisis de Señales y Sistemas

Documento de referencia (lookup). Las convenciones son **estrictas**: las alternativas listadas como incorrectas no se usan en ninguna parte del proyecto.

---

## Símbolos básicos

| Elemento | Correcto | Incorrecto | Notas |
|---|---|---|---|
| Unidad imaginaria | `j` | `i` | Convención de ingeniería; `i` se reserva para corriente eléctrica. |
| Conjugado complejo | `\bar{z}` o `\overline{z}` | `z^*` | El asterisco se evita en todo el libro. |
| Parte real | `\operatorname{Re}\{z\}` o `\text{Re}\{z\}` | `Re(z)` con paréntesis | — |
| Parte imaginaria | `\operatorname{Im}\{z\}` o `\text{Im}\{z\}` | `Im(z)` con paréntesis | — |
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
| Frecuencia digital | `\lambda` | Frecuencia de una secuencia, en radianes por muestra: **es un ángulo** (el que avanza el vector giratorio entre muestra y muestra). Relación con el muestreo: `\lambda = \omega \Delta t`. Vive en un intervalo de longitud `2\pi`. Introducida en el Capítulo 8 (tiempo discreto). |
| Intervalo de muestreo | `\Delta t` | Tiempo entre muestras consecutivas. Símbolo primario del proyecto. También llamado `T_s` (*sampling time*) en la literatura en inglés; aclararlo la primera vez que aparece. |

---

## Variables complejas

| Variable | Forma | Contexto |
|---|---|---|
| Laplace | `s = \sigma + j\omega` | Tiempo continuo. |
| Z | `z = re^{j\lambda}` | Tiempo discreto. El argumento es la **frecuencia digital** $\lambda$, el mismo símbolo que en el resto del bloque discreto: sobre el círculo unidad ($r=1$), $z = e^{j\lambda}$ es el punto donde vive la transformada de Fourier de tiempo discreto. Nunca `\theta`. |
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

Un vector en sentido discreto —lista finita de coordenadas, $\mathbb{R}^n$ o $\mathbb{C}^n$— se escribe con **negrita y flecha arriba**.

| Elemento | Correcto | Incorrecto | Notas |
|---|---|---|---|
| Vector | `\vect{v}` | `\mathbf{v}`, `\vec{v}` solo | Macro definido en `setup.tex` que produce `\vec{\mathbf{v}}`. |
| Versor de base | `\vect{e}_k` | `\mathbf{e}_k` | El subíndice queda fuera del macro. |
| Vector nulo | `\vect{0}` | `\mathbf{0}` | — |

La convención aplica solo a vectores discretos (álgebra lineal). Las señales —funciones de tiempo continuo o discreto— se escriben con su notación habitual: `x(t)`, `x[n]`, sin negrita ni flecha.

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
| Sección | `la Sección~\ref{sec:serie_fourier}` | `§\ref{sec:...}`, `Sec.~5.2`, `§5.2` | — |
| Subsección | `la Subsección~\ref{subsec:prop_conjugacion}` | `§\ref{subsec:...}`, `§5.3.6` | — |
| Referencia genérica | `esta sección`, `el capítulo anterior` | — | Minúscula y sin `\ref{}` cuando es deíctica. |

El símbolo `§` queda reservado para archivos meta del proyecto (`STYLE.md`, `DECISIONES.md`, `WORKFLOW.md`, `avance.md`, comentarios `%` de figuras). **No se usa en prosa del libro.** Detalle: `STYLE.md §8`.
