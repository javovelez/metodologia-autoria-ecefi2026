# Estilo de redacción

Versión 3, del 2026-09-25. Este documento es la referencia única de estilo del proyecto. Rige el libro, los apuntes, los trabajos prácticos, las presentaciones y los parciales. Se lee entero antes de redactar prosa nueva y antes de revisar prosa existente.

Las guías de cada sub-proyecto (`fourier_discreto/REDACCION.md`, `Gabinete/gabinete.md`, `Presentaciones/presentaciones.md`, `evaluaciones/PARCIALES.md`) ajustan este documento a su formato y no lo contradicen. Si aparece una contradicción, manda este documento y hay que avisarle al usuario para corregir la guía.

La numeración cambió en esta versión. En los registros históricos (`avance.md`, las bitácoras de los apuntes) las referencias a la versión anterior se traducen así.

| Versión 2 | Versión 3 |
|---|---|
| §13.1 a §13.5, §13.8, §13.11 (calcos, alcance adverbial, sujeto inestable) | §14.9 y §14.10 |
| §13.6 y §13.7 (vocabulario, *dar*) | §16 |
| §13.9 (dos puntos) | §14.6 |
| §13.10 (oraciones telegráficas) | §14.2 |
| §13.12 (apertura de párrafo) | §14.3 |

---

## 0. Alcance

Las reglas aplican al cuerpo principal del libro, del Capítulo 3 en adelante, y a todo el material derivado. Los Capítulos 1 y 2 están escritos en un registro deliberadamente comprimido, porque son una antesala de variable compleja, y no se usan como modelo de nada.

---

## 1. Propósito del libro

El libro busca ser más abordable que la mayoría de los textos de Análisis de Señales y Sistemas. Esa diferencia se sostiene con cuatro decisiones de tono.

- **Lenguaje cercano.** La prosa es la de un docente que explica, no la de un tratado que enuncia. Es conversacional sin ser informal.
- **Explicaciones que no saltean pasos.** Cuando un paso puede parecer obvio para quien ya sabe, se hace explícito para quien está aprendiendo.
- **Ejemplos fáciles de digerir.** Entre dos ejemplos válidos gana el más simple, aunque el otro sea más vistoso.
- **Intuición siempre a la vista.** En ningún punto el lector debería perder el hilo de qué estamos haciendo y por qué.

Cuando una regla de este documento entra en conflicto con alguna de estas cuatro decisiones, gana la decisión de tono.

---

## 2. Los pilares del registro

**Rigor sin pedantería.** Las explicaciones son matemáticamente precisas. Se evitan las construcciones rebuscadas, rimbombantes o poéticas, como *"pulcra superposición"* o *"fatal y rigurosamente dictaminadas"*.

**Amigable sin ser romántico.** El tono es el de un docente que ordena un concepto difícil de forma directa. Las fórmulas no se califican de *"monumentales"*, *"mágicas"* ni *"fascinantes"*, y no se escriben imágenes como *"el monopolio de los polos"*.

**Exactitud sin ambigüedades coloquiales.** La simpleza nunca se consigue a costa de la precisión. *"Integrar sobre la nada da cero"* es informal y además impreciso.

**Registro natural del castellano.** Se prefieren los verbos y sustantivos comunes a las nominalizaciones forzadas (*"al acotar"* y no *"el acotamiento"*; *"la aclaración"* y no *"el aclarado"*). El libro se escribe en castellano y no se redacta en inglés para traducirlo después.

**Pragmático y operativo.** El texto se ocupa del mecanismo de la herramienta y de cómo el lector opera con ella para resolver problemas de ingeniería.

**Cercano pero claro.** La cercanía viene de la voz del docente y de la primera persona del plural (*"veamos"*, *"fijemos $N$"*, *"aumentemos $\lambda$"*). No viene de los modismos. Ante la duda entre una versión coloquial y una explícita, gana la explícita, sin llegar al tono de tratado.

---

## 3. No saltear pasos

Cuando una manipulación algebraica puede no ser inmediata para el lector, se desarrolla. Una cadena de cinco pasos chequeables a ojo está bien. Si uno de los cinco requiere reagrupar, factorizar o aplicar una identidad no trivial, ese paso se muestra.

Estas frases delatan un salto y se reemplazan por el paso real.

| Frase | Qué hacer |
|---|---|
| *"es fácil ver que"* | Mostrar el paso. |
| *"se sigue inmediatamente"* | Desarrollarlo en una línea. |
| *"un cálculo directo muestra"* | Hacer el cálculo. |
| *"de forma análoga"* | Solo si el caso análogo está desarrollado y la analogía es estructural. |
| *"como sabemos"* | Decir dónde se estableció o reponerlo. |

La regla no pide explicar cada paso a la altura del primer año de cálculo. Pide hacer visible el paso que requiere algo que no está en la línea anterior. En los ejemplos numerados y en los trabajos prácticos la regla es estricta, porque ahí el lector aprende a operar.

Cuando una cuenta se puede escribir, se escribe en display con sus pasos. Describirla en prosa obliga al lector a rehacerla de memoria.

---

## 4. Intuición primero, formalización después

La preferencia por defecto es presentar primero la intuición de qué estamos haciendo y por qué, y formalizar después. Así el lector sabe adónde va antes de seguir una definición.

La preferencia es fuerte pero no obligatoria. Otro orden funciona mejor en tres casos.

- Una definición corta y autosuficiente cuyo interés está en sus consecuencias, como la periodicidad o la paridad.
- La continuidad estructural con lo recién visto, cuando un párrafo de motivación sería redundante.
- Un reposicionamiento que abre un capítulo o una sección y necesita declarar primero el cambio de marco.

Intuición primero no significa enunciar la tesis de la sección antes de que el lector tenga el objeto delante (ver la Sección 13.1 de este documento).

---

## 5. Sostener la intuición

La matemática del libro es densa, y el riesgo permanente es que el lector siga las cuentas y pierda el sentido.

- **Después de un desarrollo de más de tres líneas**, una oración dice qué se obtuvo y para qué sirve, nombrando el objeto. Esa oración informa. No es una máxima que resume ni una repetición del resultado con otras palabras.
- **Cuando se introduce un término técnico nuevo**, la oración siguiente dice qué hace ese objeto. La definición formal puede llegar después.
- **El cierre de una subsección** dice qué quedó establecido y, si hace falta, qué pregunta queda abierta. Dos o tres oraciones alcanzan. El cierre no desarrolla el mecanismo de la sección siguiente, porque eso obliga a procesar dos veces lo mismo. Si un cierre sale denso, se recorta en lugar de explicarse más.
- **Si la sección tiene un objeto recurrente** (un circuito RC, el promediador), se vuelve a él al cerrar, para que el lector compruebe que la herramienta nueva dice algo sobre un objeto que ya conocía.

---

## 6. Cadencia y fórmulas

- Toda fórmula display importante va unida a una oración de prosa antes o después que la motiva o la lee.
- No se encadenan dos fórmulas display sin prosa intermedia, salvo dentro de un cuadro `resultado` o cuando la segunda es consecuencia trivial de la primera.
- Después de una definición formal, una oración ofrece una lectura, una consecuencia o un caso de prueba.
- **Cálculo en display, mención en línea.** Va en display toda fórmula con límites, integrales con desarrollo, fracciones compuestas o cadenas de dos o más igualdades. Va en línea lo corto: un valor ($H(0)=1/2$), un par breve, una condición ($\operatorname{Re}\{s\}>a$). Si escribirla en línea obliga a degradar la notación, como poner `1/[(s+a)(s+b)]` en lugar de una fracción, va en display.
- **Muchos casos paralelos van a una tabla.** Si un párrafo acumula varios casos con varias cantidades cada uno (valor, módulo, fase), los datos van a una tabla y la prosa enuncia la regla común y la interpretación.

---

## 7. Vocabulario aplicado y test del borrado

El lector aprende esta matemática sin tener todavía la base aplicada. Nombrar un dominio (filtro pasabajos, modulación, control) puede anclar el concepto o puede agregar carga sin beneficio. Antes de usar un término aplicado se hace una prueba. Si al reemplazarlo por "este sistema" el párrafo sigue funcionando, el término decora y se considera borrarlo. Si el párrafo deja de funcionar, el término trabaja, se conserva y el lector necesita al menos una imagen mínima de qué es.

- Un término que aparece una vez como etiqueta funciona solo. Un término que es sujeto de tres oraciones necesita estar explicado.
- *"El filtro pasabajos del oído deja pasar las frecuencias bajas y atenúa las altas"* se define por contexto. *"Aplicamos un filtro pasabajos"* supone que el lector ya sabe qué es.
- En los capítulos de sistemas, del 4 en adelante, los nombres físicos se justifican más, porque son el objeto de estudio.

La clasificación del vocabulario seguro, del que requiere glosa y del que no está disponible todavía está en `DECISIONES.md §3`.

---

## 8. Referencias

### 8.1. Referencias cruzadas

- Se escriben con la palabra completa y mayúscula inicial: *el Capítulo~\ref{...}*, *la Sección~\ref{...}*, *la Subsección~\ref{...}*, *la Figura~\ref{...}*, *la Tabla~\ref{...}*. La palabra *ecuación* va en minúscula: *la ecuación~\eqref{...}*.
- Las referencias deícticas van en minúscula y sin `\ref`: *esta sección*, *el capítulo anterior*.
- El `\eqref` no cuelga suelto de una preposición o de un verbo. *"que por~\eqref{eq:x} vale $N$"* pasa a *"que por la ecuación~\eqref{eq:x} vale $N$"*. Si ya hay un sustantivo que nombra el objeto (*la fórmula de análisis~\eqref{...}*, *el par~\eqref{...}*), queda como está.
- Un panel se cita con la figura completa, *la Figura~\ref{...}(a)*, y no como *"el panel (a)"* suelto.
- Toda figura y toda tabla se nombran en la prosa en el punto donde el lector tiene que mirarlas.
- El símbolo `§` y las abreviaturas latinas (`cf.`, `e.g.`, `i.e.`, `vs.`) no se usan en el cuerpo del libro, los trabajos prácticos ni las presentaciones. Tampoco en el chat con el usuario al presentar planes. En los archivos meta como este sí se usa `§`.

### 8.2. Referencias a capítulos futuros

Como máximo una por subsección, y solo cuando la conexión es estructural. Se prefiere decir para qué sirve el concepto actual sin nombrar el capítulo de destino. *"Esta propiedad simplifica el cálculo de coeficientes espectrales"* funciona mejor que *"como veremos en el Capítulo 5, la paridad determina los coeficientes nulos"*.

### 8.3. El libro es autónomo

El libro no menciona trabajos prácticos, clases, presentaciones ni el banco de preguntas. *"Como se vio en clase"* o *"una observación del trabajo práctico"* no van. Si una motivación viene de una observación concreta, se incluye como ejemplo propio del texto. Las resoluciones de los trabajos prácticos tampoco citan secciones del libro, porque la estructura del libro puede cambiar.

---

## 9. Precisión del vocabulario técnico

- **Un término se usa según su definición formal.** Antes de usar un término técnico se verifica dónde está definido en el libro. Si solo aparece en un pie de figura o en prosa suelta, no está definido. *Fasor* no está definido en el libro y no se usa. *Vector giratorio* está definido en la Sección 2.2 para $e^{j\omega t}$ y se acepta también para sus versiones escaladas $c_k\,e^{jk\omega_0 t}$.
- **Un término definido se nombra y no se parafrasea.** Tres párrafos después de definir la velocidad de Nyquist, la prosa dice *velocidad de Nyquist* y no *"el doble de la frecuencia más alta de la señal"*.
- **Un término técnico no se usa en su sentido corriente.** *Salida*, *entrada*, *respuesta*, *ganancia*, *orden* y *peso* son términos del libro. *"La salida viene del objeto que medimos"*, con *salida* en el sentido de escapatoria, hace buscar un sistema que no está.
- ***Señal real* significa señal de valores reales.** Para el sentido práctico se escribe *"una señal que proviene de un fenómeno físico"* o *"una señal medida"*. Aplicado a aparatos, *real* se opone a *ideal* y se conserva (*filtro real*, *sistema real*).
- **Una propiedad se demuestra donde vale siempre.** Si se sigue de la fórmula, se afirma sobre la fórmula y no sobre un caso particular. La memoria del promediador está en el término $x[n-1]$ y vale en cualquier instante, no solo cuando la entrada se apagó.
- **Las afirmaciones son completas.** Una magnitud se da con su valor (*"queda libre una franja de ancho $\omega_s-2\omega_M$"*, no *"queda espacio libre"*). Un argumento hecho sobre un caso se generaliza diciendo por qué vale en todos. Si quedan dos casos pendientes, se anuncian los dos.
- **Una metáfora aislada puede servir, una metáfora repetida no.** Una imagen que marca el grado de una analogía laxa se justifica (*"los polos y ceros son primos cercanos de los autovalores"*). Una imagen que se repite tres o cuatro veces en un capítulo se convierte en el término impreciso del capítulo y se reemplaza por la palabra exacta, que casi siempre ya está en el texto.
- **La convergencia de una serie infinita no se da por supuesta.** Se precisa el sentido (puntual, en norma cuadrática, condiciones de Dirichlet) o se difiere explícitamente.

---

## 10. Demostraciones

Una demostración es la cadena de razonamiento que permite al lector verificar el resultado. No se exige el nivel de un tratado, pero sí trazabilidad. Antes de la cadena de igualdades conviene decir en una oración qué observación la guía, para que el lector entre al cálculo sabiendo qué lo sostiene. Una demostración extensa que no aporta a la comprensión puede omitirse con una referencia explícita.

Las demostraciones terminan con la última línea de razonamiento, sin `\qed`, sin $\square$ y sin *"demostrado"*.

---

## 11. Ejemplos

**Dos modalidades.** El ejemplo de fenómeno físico se prefiere cuando el concepto lo admite, y no requiere cálculo; alcanza con nombrar el fenómeno y decir qué aspecto del concepto ilustra. El ejemplo numerado se reserva para conceptos que solo se entienden ejecutando el procedimiento, se resuelve completo y llega a un resultado verificable. Se rotula *Ejemplo*, no *Ejemplo trabajado*.

**Un ejemplo responde una pregunta.** Correr un sistema sobre una entrada concreta funciona si hay una pregunta pendiente (¿es causal?, ¿es estable?). Sin pregunta, el cálculo se lee como material sin propósito. Un ejemplo que quedó huérfano después de un cambio de estructura se reubica o se elimina.

**La apertura del ejemplo va directo a lo que se calcula.** Dice qué se quiere calcular, sobre qué señal y con qué hipótesis. No justifica por qué la configuración elegida es la más simple ni anticipa cuántos casos van a aparecer.

**Se describe lo que se hace, no lo que se descarta.** Una señal se construye sumando un tramo por vez, en lugar de escribirla de una sola vez y repararla después. La prosa presenta el método elegido y no narra el alternativo.

**Un resultado se deriva por un solo camino.** Dos derivaciones del mismo resultado parten la subsección en dos recorridos. Queda la que mejor acompaña a la figura y a lo que el capítulo necesita después.

**No se plantea una forma de la fórmula que después no se usa.** Si el desarrollo, el cuadro y la figura trabajan con una forma, la lectura se presenta sobre esa forma. En la convolución el marco es dejar fija la señal e invertir y desplazar la respuesta al impulso.

**El ejemplo entrega lo que el resultado promete.** Si el coeficiente es complejo, se calculan el módulo y la fase.

---

## 12. Figuras en la prosa

Las convenciones técnicas de las figuras están en los skills `create_2d_figures`, `create_block_diagrams` y `3d_figures`. Esta sección trata de cómo la prosa usa las figuras.

- **Las figuras se usan con generosidad.** Toda gráfica que ayude a seguir un concepto con geometría o evolución temporal se incluye. La pregunta es si ayuda a seguir el concepto, y ante la duda la respuesta es sí. Una figura puramente decorativa no se incluye.
- **Toda representación descripta lleva figura.** Si la prosa describe una región del plano, un diagrama de polos y ceros o la forma de una señal, hay figura en ese punto.
- **La figura va antes del razonamiento.** La prosa recorre lo que se ve panel por panel, sobre un ejemplo con números concretos, y el caso general se enuncia después del ejemplo. En una derivación, la figura entra apenas están presentados los objetos que intervienen y cada paso de la cuenta se relata sobre los paneles.
- **La figura comparativa va donde se comparan los casos**, no adelantada al inicio de la subsección con detalles que el lector todavía no leyó.
- **El nombre del resultado no se usa antes de derivarlo.** Si la figura aparece antes de la cuenta, sus paneles se describen con vocabulario disponible (*"el resultado de convolucionar las dos"*) y el término técnico (*"las copias del espectro"*) se reserva para cuando la cuenta lo establece. El `\caption` describe la figura terminada y ahí sí puede nombrarlo.
- **Los paneles que la prosa compara llevan la misma escala.** Antes de escribir *"pasa de 9 a 5"*, verificar que los paneles compartan la unidad de los ejes.
- **Las observaciones de un caso particular van al `\caption`**, describiendo la figura, sin pretender demostrar nada.

---

## 13. Estructura de secciones y subsecciones

### 13.1. Apertura

La apertura de un capítulo o sección no explica el eje del capítulo. Una afirmación general hecha antes de que el lector haya visto un solo caso no se puede verificar y genera inseguridad. El eje lo plantea el título, lo muestran los ejemplos y lo nombra el cierre como observación de lo que acaba de pasar. En la apertura van el cambio de marco, la lectura de la ecuación que el lector tiene delante y el mapa del recorrido.

Tampoco van inventarios de repaso. Listar lo que trajo el capítulo anterior o las seis propiedades que vienen obliga a retener nombres que todavía no se pueden usar.

### 13.2. El mapa del recorrido agrupa

El párrafo que anticipa el recorrido de una sección agrupa las subsecciones por etapas (*"En la entrada… En la salida…"*). No dedica una oración a cada subsección ni trae las justificaciones, que son el contenido de cada una.

### 13.3. El instrumento después de su propósito

Un filtro o una operación no se usa en un argumento antes de que el texto haya dicho para qué sirve. Si el dispositivo se construye más adelante, el argumento se escribe en términos de la operación (*"quedarse con la copia central"*) y no del dispositivo.

### 13.4. Una sola definición por concepto

Un concepto se define una vez. Una oración informal que define, seguida de un cuadro `resultado` que define lo mismo, es una duplicación. Antes del cuadro va una oración que dice qué pregunta responde la definición, no lo que dice.

### 13.5. Cuadros `resultado` y `nota`

- El cuadro `resultado` lleva título y contiene solo el enunciado o la fórmula. Motivación, aclaraciones y conexiones van en la prosa de afuera. Si un concepto tiene varios resultados, cada uno va en su propio cuadro, unidos por prosa.
- La posición del cuadro se evalúa en cada caso. Por defecto va al final, como resumen de un desarrollo que el lector ya siguió. Va al frente cuando el resultado es corto o funciona como definición desde la cual se construye el resto. Lo que no se permite es decidir por costumbre.

### 13.6. Títulos

El título de una subsección nombra lo que el lector se lleva y no el montaje del ejemplo. *"El efecto del sistema se lee en sus pesos"* nombra el resultado; *"Dos sistemas sobre una misma entrada"* describe la mesa de trabajo. Si el título sigue siendo cierto después de cambiar el ejemplo por otro equivalente, describe el montaje.

### 13.7. Segunda explicación

Cuando una sección vuelve sobre un hecho ya explicado y lo lee desde otro dominio, ofrece una segunda explicación y no la explicación que faltaba. Decir *"la explicación que faltaba"* devalúa el capítulo anterior y describe mal lo que la sección aporta.

### 13.8. El paralelismo con el continuo

En el bloque discreto (Caps. 8 a 13), apoyarse en el tiempo continuo sirve para no rederivar lo que se traslada. Esa economía se conserva. El paralelismo no se usa como marco explicativo, es decir, cada hecho discreto no se presenta como *"el gemelo"* o *"el eco"* de su par continuo. La comparación se nombra una vez, donde ahorra trabajo, y después los hechos discretos se enuncian en sus propios términos.

### 13.9. Cantidad de secciones

La cantidad de secciones de un capítulo la decide el contenido. Los cinco archivos que deja `bootstrap_chapter` son andamiaje y no una decisión.

---

## 14. La oración y el párrafo

**Principio que gobierna esta sección: la estructura más simple que haga el trabajo.** Entre dos armados posibles gana el simple, aunque el otro sea más compacto o suene más elegante. Una afirmación por oración siempre que se pueda. La afirmación principal va en la oración principal, no en un inciso ni en una cola. Si una oración obliga a releer para saber de qué habla, se parte en dos. La compresión no es un valor del libro y la claridad sí.

### 14.1. Cada oración nombra de qué habla

El lector no debería tener que volver a la oración anterior, y mucho menos al párrafo anterior, para saber de qué se habla. Es la falla que más molesta al leer en frío.

- **Un pronombre o un demostrativo solo se usa si su antecedente está en la misma oración o en la inmediatamente anterior, y no hay otro candidato.** En cualquier otro caso se repite el nombre del objeto. Repetir el sustantivo no es un defecto de estilo en este libro.
- **La primera oración de un párrafo nombra su objeto.** No abre con *"Ese rodeo"*, *"Esa fórmula"*, *"Los dos polos"*, *"El cuadro pide"* o *"La división tiene un límite"* cuando el objeto quedó en el párrafo anterior. Escribe *"La descomposición de $X(z)/z$ en fracciones simples"*, *"la fórmula de cobertura~\eqref{...}"*, *"los polos en $z=\rho e^{\pm j\lambda_0}$"*.
- **Se evitan los referentes vagos**: *esto*, *eso*, *lo anterior*, *este resultado*, *el caso*, *las dos*, *la primera*, *la otra*, cuando no llevan el sustantivo que los identifica.
- **Se prefiere el nombre propio del objeto** (el símbolo, la ecuación, el nombre del sistema) a una perífrasis como *"el factor que multiplica a todo"* o *"lo que veníamos viendo"*.
- **Un sustantivo abstracto no reemplaza al objeto.** *La maniobra*, *la verificación*, *la traducción*, *el recorrido*, *la lectura*, *la cuenta*, *el ingrediente*, *la pieza*, *la clave*, *el precio* obligan al lector a reconstruir a qué operación concreta se refieren. Se nombra la operación: *"La verificación es un cambio de índice"* pasa a *"La propiedad se verifica con el cambio de índice $m=n-k$"*.

### 14.2. Nada de oraciones comprimidas

Una oración puede tener todas las palabras correctas y leerse como el resumen de otra oración más completa. Tres formas del defecto.

- **Verbo de actividad elidido.** *"Queda el factor que multiplica a todo"* tiene la gramática de un título. La forma plena es *"Resta interpretar el factor $1/\Delta t$ que multiplica a la suma"*. Prueba del título: si la oración funciona tal cual como `\subsubsection*{}`, está escrita como encabezado y se reescribe.
- **Sintagma sin anclaje.** *"el factor"* sin decir de dónde sale. Se ata a su origen: *"el factor que multiplica a la suma en la ecuación~\eqref{...}"*.
- **Conceptos encadenados sin desarrollar.** *"Que una exponencial oscile no garantiza que la secuencia se repita"* pide desarrollar qué es oscilar (tomar valores que aumentan y disminuyen) y qué es repetirse (reproducir la misma sucesión de muestras). Se devuelven las palabras que dan claridad.

### 14.3. La apertura del párrafo

No hay una fórmula para abrir un párrafo. Hay tres aperturas que no se usan.

1. **El anuncio vacío.** *"Antes de cualquier cuenta, fijemos cómo se lee el cuadro."* La oración promete lo que el párrafo va a decir y no dice nada. Se borra y el párrafo abre con su contenido.
2. **La oración corta de intriga.** *"La división tiene un límite."*, *"Dividir por $z$ tiene una consecuencia."*, *"El álgebra es común a las tres."*, *"Lo nuevo está fuera de ese círculo."*, *"El precio está en el truncamiento."* Es una afirmación breve y abstracta que adelanta algo sin decirlo, para que la oración siguiente lo revele. Repetida a lo largo de una sección es la huella más visible de la redacción automática (ver la Sección 15). Se reemplaza por una oración que diga el contenido completo: *"La división larga entrega las muestras de a una y no produce una fórmula cerrada para $x[n]$."*
3. **La apertura que depende del párrafo anterior**, descripta en la Sección 14.1.

La apertura correcta es una oración completa, de largo normal, cuyo sujeto es el objeto nombrado y que afirma algo que el lector puede verificar. Puede ser corta si dice algo completo y concreto (*"Si $L>N$, las copias se superponen."*), pero la brevedad no es un objetivo.

Tampoco se abre con muletillas de realce: *"Conviene…"*, *"Vale la pena…"*, *"Es importante notar…"*, *"Cabe destacar…"*. *"Conviene"* se conserva cuando afirma una conveniencia real (*"qué frecuencia de muestreo conviene usar"*).

**Prueba de la pasada.** Se leen seguidas las primeras oraciones de todos los párrafos de una sección. Si muchas son de menos de diez palabras, si muchas empiezan con un sustantivo abstracto o un demostrativo, o si todas tienen el mismo molde, el patrón está instalado y se corrige en toda la sección. Después se releen para verificar lo contrario, que ninguna haya quedado de tres líneas, porque la corrección apurada tiende a soldar la apertura con la oración siguiente y fabrica una oración-percha (Sección 14.4).

### 14.4. La oración-percha

Es una afirmación adelante y varios apéndices colgados de un solo eje: un inciso, una coordinada con *y*, una cola con *"con + sustantivo"*. La pieza que cierra el argumento termina en la cola, que es la posición más débil.

Señales para detectarla: una coma seguida de *"con + sustantivo"* al final de la oración; un inciso que repite lo que la oración ya dijo; un sinónimo de refuerzo en la misma oración (*completa/entera*); un pronombre átono lejos de su antecedente. Suele venir con un verbo de proceso donde el sustantivo alcanzaba (*"un punto del plano lo registra"* en lugar de *"un punto del plano es"*).

La salida es partir en varias oraciones, cada una con su afirmación. Ejemplo rechazado: *"El círculo muestra la exponencial completa: cada foto es un número complejo (parte real y parte imaginaria) y un punto del plano la registra entera, con el índice de la foto al lado."* Versión aceptada: *"En el círculo, cada foto es un punto del plano, y la parte real y la parte imaginaria son sus dos coordenadas. Los índices dicen en qué orden el vector pasa por esos puntos. Con la posición y el orden a la vista, el círculo muestra la exponencial completa."*

### 14.5. Sin em-dashes

**El libro no usa em-dashes (`---` en LaTeX, `—` en Unicode) en la prosa, ni sueltos ni en pares.** Tampoco en títulos, rótulos, cuadros, ítems ni pies de figura.

| Uso del em-dash | Reemplazo |
|---|---|
| Inciso breve | Comas: *"las componentes $v_1$ y $v_2$, que no dependen una de otra, …"* |
| Aclaración larga | Una oración propia a continuación. |
| Aclaración de notación o un dato accesorio | Paréntesis. |
| Aposición al final de la oración | Coma, o reescribir para nombrar la relación (*porque*, *es decir*, *de modo que*). |
| Separador en un título o rótulo | Punto (*Ejemplo 1. Sistema lineal*) o dos puntos en el rótulo. |

El en-dash (`--`) sigue usándose en rangos (*pp. 10--16*) y en pares técnicos (*entrada acotada--salida acotada*).

El texto ya escrito del libro tiene em-dashes. No se barren por iniciativa propia. Se corrigen al trabajar el párrafo que los contiene o cuando el usuario pide el barrido.

### 14.6. Dos puntos con moderación

Los dos puntos anuncian que lo que sigue explica, enumera o precisa lo anterior. Usados por costumbre, el texto toma un ritmo de fichas (afirmación, dos puntos, desarrollo) que el lector oye por encima del contenido. Además suelen tapar la relación real entre las dos mitades, que queda insinuada en lugar de dicha.

**La preferencia por defecto es la oración corrida.** Los dos puntos entran en tres lugares.

- Una enumeración real de varios elementos.
- El anuncio de una fórmula display que la oración venía preparando.
- Un rótulo o un título.

**No se usan para presentar ni para concluir.** Estas formas no van en la prosa.

| Forma | Ejemplo a evitar | Preferir |
|---|---|---|
| Presentación | *"La razón es simple: el factor no depende de $k$."* | *"El factor no depende de $k$."* o *"La razón es que el factor no depende de $k$."* |
| Conclusión | *"El resultado es el esperado: el espectro se replica."* | *"El espectro se replica, como se esperaba."* |
| Aposición explicativa | *"Cada aporte es del mismo tipo: el espectro convolucionado con un impulso."* | *"Cada aporte es el espectro convolucionado con un impulso."* |
| Consecuencia | *"Las copias también: el panel (c) es un tren de triángulos."* | *"Las copias también se replican, y la Figura~\ref{...}(c) queda como un tren de triángulos."* |
| Remisión | *"Esa cuenta ya está hecha: la propiedad~\eqref{...} dice que…"* | *"La propiedad~\eqref{...} ya resuelve esa cuenta, porque dice que…"* |
| Anuncio de casos | *"Hay dos casos: …"* | *"Hay dos casos. En el primero…"* |

Dos apariciones en el mismo párrafo son una de más, y en párrafos contiguos también.

### 14.7. Un anuncio y una conclusión

Un párrafo anuncia una vez lo que va a hacer y enuncia una vez el resultado. Dos anuncios de la misma operación, o una conclusión dicha tres veces (el resultado, *"esa es la explicación"*, una versión en cursiva, una imagen), se leen como redacción rebuscada aunque cada oración esté bien. La salida es borrar lo que sobra, no coserlo con un conector. Sobra primero el anuncio genérico y la conclusión metafórica.

### 14.8. Negaciones

- **El contenido no se enuncia en negativo.** *"No hay curva que graficar"* obliga al lector a imaginar un objeto para después borrarlo. Se dice lo que ocurre: *"en $\lambda=0$ la serie suma infinitos unos y crece sin cota"*. Una negación que llega después de una afirmación y la acota (*"No hay contradicción"*, *"Ni la forma ni la información cambiaron"*) es buena prosa y se conserva.
- **Nada de *"no es X: es Y"* ni de sus variantes.** *"La ventaja no es estética: …"*, *"Esto no es arbitrario: …"*, *"No es una metáfora: …"*, *"No hace falta salir a buscarlas: …"*. Niegan un cargo que el lector no hizo y delatan inseguridad. Se afirma directamente: *"La convolución es la respuesta del sistema a la entrada."*

### 14.9. Sujeto estable y lectura única

- **El sujeto no cambia sin aviso bajo una coordinación con *y*.** *"Las copias lo comparten y no depende de $k$"* se lee un instante como *"las copias no dependen de $k$"*. Se escribe una afirmación por oración con su sujeto: *"Como no depende de $k$, el factor escala a todas las copias por igual."*
- **Artículo y pronombre iguales en contacto.** *"La banda base no depende de la señal: la fija el muestreo"* se lee primero *"la fija"* como sustantivo. Se pone el sujeto adelante: *"La frecuencia de muestreo determina la banda base."*
- **Orden sujeto, verbo, objeto**, salvo que haya una razón de énfasis. El orden objeto, verbo, sujeto obliga a esperar al final para saber quién hace qué.

### 14.10. Calcos del inglés

| Calco | Evitar | Preferir |
|---|---|---|
| Clivada antepuesta | *"Lo que importa no es tanto la fórmula como qué es $\lambda$."* | *"Más que la fórmula, importa qué es $\lambda$."* |
| Sujeto de cláusula pesado | *"Que una secuencia sea una lista de números habilita…"* | *"Como una secuencia es una lista de números, se puede…"* |
| Perífrasis de relativo | *"cuál de las dos es la que vamos a estudiar"* | *"cuál de las dos vamos a estudiar"* |
| Alcance adverbial ambiguo | *"esto deja de cumplirse siempre"* | *"esto ya no es siempre cierto"* |
| Orden de palabras | *"entra un número solo"* (*only one number*) | *"un solo número"* |
| Imperativo de manual | *"Note que…"*, *"Observe que…"* | Afirmar directamente, o *"Observemos que…"* |
| Pasiva con *ser* | *"el resultado es obtenido derivando"* | *"el resultado se obtiene derivando"* |
| Gerundio de consecuencia | *"…, resultando en un espectro periódico"* | *"…, y el espectro queda periódico"* |
| *Resultar en* | *"esto resulta en…"* | *"esto produce…"*, *"de aquí resulta que…"* |
| Conectores calcados | *"Adicionalmente"*, *"En orden a"*, *"Esto es debido a"* | *"Además"*, *"Para"*, *"Esto se debe a"* |
| Sujeto explícito | *"Nosotros podemos ver que…"* | *"Vemos que…"* |
| Adjetivo antepuesto | *"la anterior ecuación"* | *"la ecuación anterior"* |

Cuidado con *solo*, *siempre*, *todavía*, *también* e *incluso* entre el verbo y su complemento. La prueba es leer la oración en voz alta y ver si el adverbio parece calificar a la palabra equivocada.

---

## 15. La huella de la redacción automática

Los modelos de lenguaje tienen tics de estilo que, repetidos, funcionan como una marca de agua. El lector no puede señalar la palabra culpable, pero reconoce el texto como fabricado. Ninguno de estos rasgos es un error gramatical aislado; el problema es la repetición. Al redactar se evitan, y al revisar se buscan activamente.

| Tic | Ejemplo | Regla |
|---|---|---|
| Em-dash de inciso | *"la serie ---que converge--- vale…"* | Sección 14.5 |
| Oración corta de intriga al abrir el párrafo | *"La división tiene un límite."* | Sección 14.3 |
| Dos puntos de revelación | *"La razón es simple: …"* | Sección 14.6 |
| Sustantivo abstracto como sujeto | *"La maniobra es…"*, *"La clave está en…"*, *"El precio es…"* | Sección 14.1 |
| Demostrativo que remite lejos | *"Ese rodeo se evita…"*, *"Esos tres ingredientes…"* | Sección 14.1 |
| Negación seguida de corrección | *"No es X, es Y"*, *"no X sino Y"* como molde | Sección 14.8 |
| Cierre sentencioso | *"Eso es todo lo que hace falta."*, *"Ahí está la clave."* | Sección 14.7 |
| Tríadas por ritmo | *"se apaga, oscila, crece"* cuando la enumeración no es exhaustiva | Enumerar solo lo que hay. |
| Adverbios de refuerzo | *exactamente*, *literalmente*, *justamente*, *precisamente*, *de punta a punta*, *de una sola vez* | Se borran salvo que precisen algo. |
| Verbos figurados | *vivir*, *habitar*, *cobrar*, *pagar*, *levantar*, *cargar*, *entrar en escena*, *se agota*, *abre* (una fórmula) | Nombrar la operación real (Sección 16). |
| Cursiva o negrita de énfasis retórico | *"la suma **no cambia en nada**"* | La cursiva marca términos que se definen; la negrita, términos en su definición. |
| Pregunta retórica y respuesta inmediata en serie | *"¿Por qué? Porque…"* varias veces por sección | Una pregunta se usa cuando es la pregunta real del párrafo. |

Estas reglas valen también para las guías y los skills del proyecto. Los modelos imitan la prosa de las instrucciones que leen, así que un archivo de instrucciones lleno de em-dashes y dos puntos enseña a escribir con em-dashes y dos puntos.

---

## 16. Vocabulario

### 16.1. Registro

| Evitar | Preferir | Nota |
|---|---|---|
| *acá*, *allá* | *aquí*, *allí* | Para continuo frente a discreto, nombrarlos: *"en el tiempo continuo…"* |
| *chico*, diminutivos | *pequeño* | |
| *subir* (una magnitud) | *aumentar* | *"El coseno sube y baja"* describe el trazo y se conserva. |
| *armar* | *construir* | |
| *agarrar* | *encontrar*, *tomar* | |
| *un montón de* | *una suma de*, *muchos* | |
| *de un saque* | *de una sola vez*, o reescribir | |
| *tira información a la basura* | *elimina información de forma irreversible* | |
| *la culpa la tiene* | *la razón es* | |
| *se van a infinito* | *divergen* | |
| *a ojo* | *por comparación*, *por inspección* | *A ojo* sugiere una estimación donde el resultado es exacto. |
| *la notación que venimos arrastrando* | *que venimos usando* | |
| *una diferencia discreta* (en un capítulo sobre lo discreto) | *sutil* | Colisión con un término técnico. |

### 16.2. Verbos comodín

**`dar` no expresa el resultado de una cuenta, una operación o una definición.** El mismo *da* cubre *vale*, *produce*, *conduce a* y *queda*, y ninguno de esos matices llega al lector. La corrección consiste en preguntarse qué pasa y nombrarlo.

| Contexto | Evitar | Preferir |
|---|---|---|
| Valor de una cuenta | *"la integral da el ancho"* | *"vale"*, *"es igual a"* |
| Sustitución | *"con $M=2$ eso da $y[0]=x[0]$"* | *"queda"* |
| Efecto de una operación | *"multiplicar por $(-1)^n$ da…"* | *"desplaza el espectro"*, *"produce"* |
| Consecuencia de una fórmula | *"la fórmula da…"* | *"de la fórmula resulta…"* |
| Dos objetos que coinciden | *"dan la misma señal"* | *"corresponden a la misma señal"* |
| Objeto al que se llega | *"da una serie del tipo…"* | *"conduce a"*, *"arroja"* |
| Tabla o figura | *"la columna da la palabra"* | *"muestra"*, *"indica"* |
| Indiferencia | *"da igual"* | *"es indistinto"* |

Se conserva el `dar` que es verbo propio: *"el vector da una vuelta"*, *"dar lugar a"*.

**`hacer` tampoco es comodín.** *"Qué le hace el muestreo al espectro"* pasa a *"el muestreo replica el espectro"*; *"muestrear hace periódico al espectro"* pasa a *"vuelve periódico"*. Se conservan los usos propios (*hacen falta ocho fotos*) y el sustantivo *hecho*.

**`dejar` como verbo de resultado** (*"dejan la misma secuencia"*) tiene el mismo problema y se reemplaza igual.

### 16.3. Vocabulario fijado

| Término | Uso | No usar |
|---|---|---|
| Convolución gráfica | *invertir y desplazar* | *voltear*, *deslizar* |
| Señal movida en el tiempo | *desplazada*, *desplazamiento* | *corrida*, *correr* |
| Integral hasta $t$ | *integral acumulada* | *integral corrida* |
| Llegada de una muestra al sistema | *ingresar* | *entrar* y su familia, porque choca con *entrada* |
| Representar gráficamente | *graficar*, *trazar*; una secuencia invertida se *refleja*; una figura *muestra* | *dibujar*, *dibujo* |
| Escalado por un coeficiente | *ponderado* | *pesado* (el verbo *pesar* como "importar" se conserva) |
| Función $\operatorname{sinc}$ en prosa | *el seno cardinal* (masculino) | *la sinc* como sustantivo |
| Término de una serie | *el armónico*, *los armónicos* (masculino) | *la armónica* como sustantivo; el adjetivo concuerda (*exponencial armónica*) |
| Separación entre copias o bandas | *franja libre*, *espacio libre*, con su ancho | *hueco* (reservado a la ROC y a la interpolación) |
| Integral de $|h|$ finita | *$|h|$ es absolutamente integrable* | *masa finita*, *masa total* |

---

## 17. Pasada de revisión

La pasada de fraseo se hace aparte y al final, leyendo solo la prosa. Los calcos y los tics se detectan mucho mejor oración por oración que mientras se decide el contenido matemático.

Barrido léxico inicial (los falsos positivos se descartan uno por uno):

```bash
f=archivo.tex
grep -nE -- "---" $f                                   # em-dashes (14.5)
grep -nE ":[^$]*$|: [a-záéíóú]" $f | grep -v "^\s*%"   # dos puntos en prosa (14.6)
grep -niE "\b(acá|allá|chic[oa]s?)\b" $f               # registro (16.1)
grep -niE "\b(da|dan|daba|daban|dará|darán|dio|dieron|dando)\b" $f   # dar (16.2)
grep -niE "\bhac(e|en|er|ía)\b" $f                     # hacer (16.2)
grep -niE "resulta(n|ndo)? en\b" $f                    # resultar en (14.10)
grep -niE "\b(entra|entran|entró|entrar)\b" $f         # ingresar (16.3)
grep -niE "\bdibuj" $f                                 # dibujar (16.3)
grep -niE "^(Conviene|Vale la pena|Es importante|Cabe)" $f           # realce (14.3)
grep -niE "\b(exactamente|literalmente|justamente|precisamente)\b" $f # refuerzo (15)
grep -niE "no es (tanto|arbitrari|casual|una metáfora)" $f           # negación (14.8)
```

Después de los barridos, la lectura fina.

1. ¿Las primeras oraciones de los párrafos, leídas seguidas, nombran su objeto y afirman algo completo? (14.1, 14.3)
2. ¿Algún pronombre o demostrativo obliga a buscar el referente fuera de la oración anterior? (14.1)
3. ¿Alguna oración se lee como título o como resumen de otra oración? (14.2)
4. ¿Alguna oración cuelga más de una afirmación? (14.4)
5. ¿Hay más de un dos puntos por párrafo, o alguno que presenta o concluye? (14.6)
6. ¿Se anuncia o se concluye dos veces lo mismo? (14.7)
7. ¿Se saltea algún paso, o una cuenta está descripta en prosa en lugar de escrita? (3)
8. ¿Después de cada desarrollo largo hay una oración que dice qué se obtuvo? (5)
9. ¿Cada figura, tabla y ecuación citada está nombrada con la palabra completa? (8.1)
10. ¿Algún término técnico está usado fuera de su definición o en su sentido corriente? (9)
