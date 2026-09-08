# V2 — Muestrear replica el espectro: la convolución que deposita las copias

## Qué hay en pantalla

La animación arma, paso a paso, el espectro de una señal muestreada. Los tres paneles
siguen el orden de la convolución y comparten un mismo eje de frecuencias, de manera que
una posición vertical cualquiera corresponde a la misma frecuencia en los tres.

- **Panel (a), `X(jω)`.** El espectro de la señal que vamos a muestrear, distinto de cero
  solo en `|ω| < ω_M`. La forma es elegible y no interviene en ninguna cuenta.
- **Panel (b), el peine en frecuencia.** El espectro del peine de muestreo, con un impulso
  de peso `2π/Δt` en cada múltiplo de `ω_s = 2π/Δt`. Los impulsos que ya depositaron su
  copia están en azul; los que todavía no, en gris; el que se acaba de usar, en rojo.
- **Panel (c), `X_s(jω)`.** El resultado de convolucionar (a) con (b). En azul relleno, la
  suma, que es el espectro que el muestreo deja registrado. En rojo discontinuo, cada copia
  por separado, dibujada solo sobre su propio soporte. La franja gris vertical es la banda
  base `|ω| < ω_s/2`, y la línea punteada horizontal marca la altura `1/Δt` que comparten
  todas las copias.

Debajo del panel (c) hay una **regla** que compara los dos bordes de los que depende todo:
el borde derecho de la copia central, `ω_M`, y el borde izquierdo de su vecina,
`ω_s − ω_M`. Según cuál quede a la izquierda, la cota entre los dos se rotula *separación*
(en verde) o *solapamiento* (en rojo). El cartel del pie repite el veredicto con los dos
números comparados.

Cuando dos copias se pisan, la zona donde eso ocurre queda sombreada en rojo bajo la curva.
Ahí el trazo azul se despega del rojo, y ese exceso es contenido que no estaba en el
espectro original.

## Cómo se maneja

- **Δt — período del peine.** Es el control principal, entre 40 ms y 250 ms. Reducirlo
  aumenta `ω_s` y separa las copias; agrandarlo las junta hasta que se pisan. El renglón de
  abajo informa el `ω_s` correspondiente.
- **ω_M — banda de la señal.** Ensancha o angosta el espectro del panel (a), entre `2π` y
  `16π` rad/s. El renglón de abajo informa la velocidad de Nyquist `2ω_M` y, traducida, la
  cota de período que hay que respetar.
- **Copias depositadas.** El deslizador y los botones `◀ una menos` / `una más ▶` controlan
  cuántas copias se dibujan, en el orden en que las va produciendo la suma:
  `k = 0, +1, −1, +2, −2, …`. **▶ Construir** recorre ese orden por su cuenta, y **Todas**
  salta directamente al resultado completo.
- **Forma de X(jω).** *Triángulo* es la forma de la figura del libro. *Cualquiera* es un
  espectro asimétrico y sin picos, que llega también hasta `±ω_M`.
- **Visualización.** Las tres casillas apagan las copias por separado, la suma y la banda
  base, en cualquier combinación.

Conviene empezar con **▶ Construir** y `Δt = 100 ms`, mirando el panel (b) y el panel (c)
a la vez.

## Qué mirar

**Cada impulso deposita una copia, y nada más que eso.** Al construir, el impulso que se
activa en el panel (b) queda en rojo y la flecha del panel (c) muestra la copia viajando
hasta esa misma posición. El rótulo de la flecha anota qué operación está ocurriendo, por
ejemplo `X(jω) ∗ δ(ω − 2ω_s)`. Es la propiedad del Capítulo 4 leída sobre el eje de
frecuencias, que dice que convolucionar una función con un impulso desplazado la traslada
hasta la posición del impulso, sin cambiarle la forma. El primer paso, `k = 0`, deja la
copia donde estaba, porque el impulso del origen no traslada nada.

**Las copias son los sumandos; el espectro muestreado es la suma.** Mientras las copias no
se tocan, cada frecuencia recibe a lo sumo un sumando distinto de cero y sumar no modifica
nada, así que el trazo azul se apoya exactamente sobre el rojo. Ahí las dos lecturas
coinciden y no hace falta distinguirlas.

**Elegir Δt es elegir cuánto espacio queda entre copia y copia.** Con `ω_M = 8π` fijo,
recorré los botones de período. En `Δt = 100 ms` las copias quedan separadas y entre una y
otra sobra eje; en `Δt = 125 ms` se tocan justo en `±ω_M`; de ahí en adelante se pisan, y
la franja sombreada en rojo crece a medida que `Δt` aumenta. La regla de abajo dice lo mismo
con dos marcas, y mientras `ω_M` quede a la izquierda de `ω_s − ω_M` hay separación.

**El daño empieza donde lo anuncia la regla.** Cuando hay solapamiento, la zona sombreada
arranca precisamente en `ω_s − ω_M` ---la marca roja--- y parte de ella cae dentro de la
banda base. Esa porción de la copia central ya no es una réplica fiel del espectro
original, porque lleva sumada la cola de la vecina, y ningún procesamiento posterior puede
volver a separarlas.

**La forma del espectro no interviene.** Cambiá a *cualquiera* y repetí el recorrido. Las
copias son otras, pero se depositan en los mismos lugares, se solapan a partir del mismo
`Δt` y la regla marca los mismos dos bordes. El único dato que interviene es `ω_M`, la
frecuencia donde el espectro termina.

**Todas las copias tienen la misma altura.** El factor `1/Δt` de la fórmula no depende de
`k`, así que escala a todas por igual; la línea punteada horizontal marca ese nivel. Cuando
hay solapamiento la suma trepa por encima de esa marca, y esa diferencia entre el azul y el
rojo es, otra vez, el contenido agregado por el solapamiento.

## Los dos casos de borde

Llevá `ω_M` al mínimo, `2π` rad/s, con `Δt = 250 ms`. Las copias quedan angostas y bien
separadas aunque el muestreo sea el más grueso disponible. Una señal lenta tolera un peine
holgado.

Llevá ahora `ω_M` al máximo, `16π` rad/s, con el mismo `Δt = 250 ms`. El eje se llena de
copias montadas unas sobre otras y el espectro muestreado queda casi plano, sin ningún
parecido con el original. Entre esos dos extremos el mecanismo no cambia; cambia
solamente la relación entre `ω_s` y `2ω_M`.
