# V1 — El peine de Dirac y su espectro: qué pasa cuando cambia Δt

## Qué hay en pantalla

La animación muestra el mismo objeto en los dos dominios. Arriba, el peine de Dirac
`δ^Δt(t)`, un impulso de peso 1 en cada múltiplo del período `Δt`. Abajo, su transformada
de Fourier, que es otro peine ---esta vez sobre el eje de frecuencias--- con un impulso de
peso `2π/Δt` en cada múltiplo de `ω_s = 2π/Δt`.

El único control es `Δt`. Todo lo demás queda determinado por él, y la animación existe
para hacer visible esa dependencia.

- **Panel (a), el tiempo.** El eje está en milisegundos, con marcas fijas cada 200 ms para
  que la separación entre impulsos se pueda comparar de una elección de `Δt` a otra. La
  cota roja mide el período entre el impulso del origen y el siguiente. Los impulsos tienen
  todos la misma altura, porque el peso de cada uno vale 1 y no depende de `Δt`.
- **Panel (b), la frecuencia.** El eje está en rad/s, rotulado en múltiplos de π. La cota
  roja mide ahora `ω_s`, la separación entre impulsos consecutivos del espectro. La altura
  de los impulsos representa su peso `2π/Δt`, y la línea punteada horizontal marca ese valor
  sobre el impulso del origen.

En los dos paneles, los puntos suspensivos de los extremos recuerdan que el peine sigue sin
fin en las dos direcciones.

En el panel izquierdo, la tabla *Lo que queda determinado* muestra los tres números que
`Δt` fija: la separación `ω_s` en rad/s, la frecuencia de muestreo en Hz y el peso
`2π/Δt` de cada impulso del espectro.

## Cómo se maneja

- **Δt — período del peine.** El deslizador lo mueve de forma continua entre 40 ms y 250 ms.
  Los ocho botones eligen valores preseleccionados que producen frecuencias de muestreo
  cómodas de leer: 40 ms son 25 Hz, 100 ms son 10 Hz, 250 ms son 4 Hz.
- **▶ Recorrer Δt** barre todo el rango de ida y vuelta, sin que haya que tocar nada. Es
  la forma más rápida de ver los dos peines moviéndose en sentidos opuestos.
- **Altura proporcional al peso 2π/Δt.** Apagada, todos los impulsos del espectro se dibujan
  con la misma altura y solo cambian de posición. Conviene apagarla la primera vez, para
  mirar únicamente la separación, y volver a encenderla después.
- **↺ Volver a Δt = 100 ms** restablece el valor inicial.

## Qué mirar

**Los dos peines se mueven en sentidos opuestos.** Al achicar `Δt`, los impulsos del tiempo
se juntan y los de la frecuencia se separan. Al agrandarlo ocurre lo contrario. La cuenta que
lo explica está a la vista en el panel de control,

```
ω_s = 2π / Δt,
```

y como `Δt` aparece en el denominador, cuanto menor es el período del peine en el tiempo,
más alta es la frecuencia fundamental de su espectro. Poner los impulsos más juntos en un
dominio los separa en el otro.

**El peso también cambia, y en el mismo sentido que la separación.** El impulso del origen
del panel (b) vale `2π/Δt`, el mismo número que mide la separación. Con `Δt = 40 ms` los
impulsos del espectro son pocos, están lejos y son altos; con `Δt = 250 ms` son muchos,
están cerca y son bajos. Los dos efectos aparecen juntos porque los dos salen del mismo
cociente.

**En el tiempo, en cambio, la altura no cambia nunca.** Los impulsos del panel (a) pesan 1
cualquiera sea `Δt`. La asimetría entre los dos paneles viene del peine que estamos
transformando, que es el de pesos unitarios; el factor `2π/Δt` aparece recién en su
transformada.

**El eje de frecuencias no se estira.** Conviene recorrer los botones prestando atención a
las marcas numéricas de abajo, que están fijas. Los impulsos se mueven sobre un eje que no
cambia, así que la separación que se ve en pantalla es la separación real en rad/s, y dos
elecciones de `Δt` se pueden comparar directamente.

## El caso de borde que importa

Elegí `Δt = 40 ms`, el extremo izquierdo del recorrido. En el espectro quedan tres impulsos
a la vista ---el del origen y los de `±ω_s = ±50π`--- y entre ellos hay una franja enorme
de eje vacío. Elegí ahora `Δt = 250 ms`. El espectro se puebla de impulsos separados apenas
`8π` rad/s.

El capítulo entero se juega en esa franja vacía. Cuando el peine multiplica a una señal,
el espectro de la señal termina copiado en cada uno de esos impulsos, y la separación entre
copias es exactamente la separación entre impulsos que esta animación deja medir. Con
`Δt` pequeño hay lugar de sobra entre copia y copia; con `Δt` grande, las copias no tienen
dónde entrar. La segunda animación retoma la escena desde ahí.
