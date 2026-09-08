# Estilo de Redacción — Análisis de Señales y Sistemas

Este documento es la **referencia única de estilo** para todo el proyecto: libro, trabajos prácticos y presentaciones. Debe leerse antes de redactar cualquier prosa nueva.

---

## 0. Alcance

Las reglas y la voz que este documento describe aplican al **cuerpo principal del libro: del Capítulo 3 en adelante**, y a todo el material derivado (TPs, presentaciones).

Los Capítulos 1 y 2 (introducción y variable compleja) ya están escritos y deben tratarse como **antesala compacta**, no como modelo tonal del resto del libro. Capítulo 2 en particular está deliberadamente comprimido: se presenta como obligatorio porque la materia lo exige, pero el autor priorizó dar peso a los conceptos que reaparecen y mantener el resto en bajo perfil. **No usar el estilo del Cap. 2 como referencia para nada de redacción nueva.**

---

## 1. Propósito del libro

El libro busca ser **más abordable** que la mayoría de los textos existentes en Análisis de Señales y Sistemas. La diferencia se construye con cuatro decisiones tonales sostenidas:

- **Lenguaje cercano**: prosa de docente que explica, no de tratado que enuncia. Conversacional sin ser informal.
- **Explicaciones didácticas que no saltean pasos**: cuando un paso algebraico o un argumento puede parecer obvio para alguien que ya sabe, **se hace explícito** para el lector que está aprendiendo. La ausencia de "es fácil ver que" es una decisión activa, no un descuido.
- **Ejemplos fáciles de digerir**: los ejemplos no se eligen por elegancia matemática sino por accesibilidad. Cuando hay dos ejemplos posibles, gana el más simple, aunque el otro sea más impresionante.
- **Intuición siempre a la vista**: en ningún punto del desarrollo el lector debería perder el hilo de **qué estamos haciendo y por qué**. Si un pasaje matemático corre el riesgo de hacer que el lector pierda la intuición, se intercala una oración que la rescata.

Estas cuatro decisiones son el **norte**. Cuando una regla específica de este documento entra en conflicto con cualquiera de ellas, gana la decisión tonal.

---

## 2. Los cuatro pilares (cómo, no qué)

### Rigor sin pedantería

Las explicaciones deben ser matemáticamente precisas y correctas en su base teórica (ej. "región de analiticidad", "singularidad dentro del contorno"). Sin embargo, **deben evitarse rotundamente** construcciones semánticas innecesariamente rebuscadas, rimbombantes o de literatura poética/metafísica.

- Evitar: *"pulcra superposición"*, *"fatal y rigurosamente dictaminadas"*.

### Amigable sin ser romántico

El tono debe asemejarse al de un docente estructurando un concepto complejo de forma directa, ágil y conversacional, pero sin caer en un exceso de metáforas emocionales o lúdicas.

- Evitar calificar fórmulas matemáticas de *"monumentales"*, *"mágicas"*, *"fascinantes"*.
- Evitar formulaciones como *"el monopolio de los polos"*.

### Exactitud sin ambigüedades coloquiales

Se busca simpleza, pero **jamás a costa de volver impreciso el concepto matemático**. Deben evitarse frases excesivamente informales que deformen u omitan la teoría subyacente.

- Evitar: *"integrar sobre la nada da cero"*.
- Preferir: *"integrar curvas nulas de singularidades"*.

### Registro natural del castellano

Preferir formas verbales o sustantivos comunes; evitar nominalizaciones forzadas que suenan rebuscadas aunque sean gramaticalmente correctas. Este pilar cubre el **vocabulario**; el fraseo a nivel de oración (clivadas antepuestas, sujetos nominales pesados, deícticos informales, ambigüedad de alcance) tiene su propio catálogo en **§13**.

- Preferir *"la aclaración"* o *"el calificativo"*, no *"el aclarado"*.
- Preferir *"al acotar"*, no *"el acotamiento"*.
- **No usar abreviaturas latinas** (`cf.`, `e.g.`, `i.e.`, `vs.`, `etc.` cuando sustituye razonamiento). Reemplazar por construcciones en castellano natural: *"ver"*, *"como en"*, *"introducido en"*, *"por ejemplo"*, *"es decir"*, *"frente a"*. Caso típico: `(cf. capítulo~\ref{capXX})` → `(ver capítulo~\ref{capXX})` o `(como en el capítulo~\ref{capXX})`.
- **No usar el símbolo `§`** para referenciar capítulos, secciones o subsecciones en prosa. Escribir la palabra completa: *"el Capítulo~\ref{...}"*, *"la Sección~\ref{...}"*, *"la Subsección~\ref{...}"*. El detalle de la regla y el formato canónico están en §8.

### Pragmático y operativo

El texto debe focalizarse directamente en el mecanismo topológico o algebraico de la herramienta y en cómo el estudiante debe operar con ella para resolver problemas de ingeniería.

---

## 3. No saltear pasos

Esta regla amerita su propia sección porque es la más fácil de violar sin darse cuenta.

**Cuando una manipulación algebraica corre el riesgo de no ser inmediata para el lector, se desarrolla.** No se asume que el lector "lo va a ver". Si la cadena tiene cinco pasos y los cinco son chequeables a ojo, está bien. Si tiene cinco pasos y uno requiere reagrupar, factorizar o aplicar una identidad no trivial, ese paso se muestra.

Frases que delatan un salto y deberían reemplazarse por el paso real:

- *"es fácil ver que"* → mostralo.
- *"se sigue inmediatamente"* → desarrollalo en una línea.
- *"un cálculo directo muestra"* → hacelo.
- *"de forma análoga"* → bien si el caso análogo está completamente desarrollado y la analogía es estructural; mal si oculta el segundo caso por cansancio.

Esto no significa explicar todo paso a la altura del primer año de cálculo. Significa: cuando el paso requiere algo que no está a la vista en la línea anterior, hacerlo visible.

---

## 4. Intuición primero, formalización después (preferencia por defecto)

**Cuando es viable, presentar primero la intuición de qué estamos haciendo y por qué, y recién después formalizar.** Esta es la preferencia por defecto del libro porque ayuda a que el lector sepa qué está haciendo con motivación, en vez de seguir una definición sin saber adónde va.

La preferencia es **fuerte pero no obligatoria**: cuando otro camino resulta claramente mejor para un concepto particular, ese se elige sin culpa. La regla es **no forzar intuición-primero cuando hay un camino mejor**, no "siempre intuición-primero".

Casos donde otro camino suele funcionar mejor:

- **Definición corta y autosuficiente** cuyo trabajo está en explorar consecuencias (ej. periodicidad, paridad). La motivación gana fuerza llegando después porque ya se tiene el objeto definido.
- **Continuidad estructural** con lo recién visto, donde el lector llega con suficiente contexto y un párrafo de motivación previa sería redundante.
- **Reposicionamiento** que abre un capítulo o sección y necesita primero declarar el cambio de marco antes de motivar dentro de él.

En todos los demás casos, considerar primero la apertura por intuición. Si no hay razón clara para apartarse, ese es el camino.

---

## 5. Sostener la intuición

La matemática del libro es densa por naturaleza (ecuaciones diferenciales, transformadas, análisis en frecuencia). El riesgo permanente es que el lector siga las cuentas y pierda el sentido. Reglas operativas para evitarlo:

- **Después de un desarrollo algebraico de más de tres líneas**, una oración que vuelva a poner sobre la mesa qué estamos calculando y para qué. No "lo que hicimos fue X" como muletilla, sino una frase corta que reconecta.
- **Cuando se introduce un nombre técnico nuevo** (transformada, función propia, etc.), una oración inmediatamente posterior que dice qué hace, no qué es. La definición formal puede llegar después.
- **En cierres de subsección**, dejar al lector con la imagen mental de qué se ganó. No con la última fórmula del desarrollo.
- **El cierre no adelanta el mecanismo de lo que viene.** Nombrar la pregunta que queda abierta orienta; desarrollar por anticipado el procedimiento que la sección siguiente va a construir obliga al lector a procesar dos veces lo mismo y le quita su lugar a esa sección. Un cierre de dos o tres oraciones que señala qué imagen queda en pie y qué falta resolver es suficiente.
- **Si una sección tiene un objeto recurrente** (un sistema RC, un masa-resorte), volver a él al cerrar para que el lector compruebe que la herramienta nueva dice algo sobre el objeto que ya conocía.

---

## 6. Cadencia y densidad

El "punto dulce" entre intuición y rigor se sostiene más con cadencia que con cantidad de explicación.

- **Toda fórmula display importante** va precedida o seguida (o ambas) por una oración en prosa que la motiva, la lee o la interpreta. Una fórmula display sin amarra textual queda flotando.
- **Dos fórmulas display consecutivas sin prosa intermedia están desaconsejadas** salvo dentro de cuadros `resultado` o cuando una es consecuencia inmediata y trivial de la anterior.
- **Después de una definición formal**, una oración debe ofrecer una lectura, una consecuencia o un caso de prueba antes de pasar al siguiente bloque. La definición sin lectura inmediata queda inerte.

---

## 7. Vocabulario aplicado: test del borrado

El lector aprende esta matemática **sin** la base aplicada todavía. Nombrar dominios (filtro pasabajos, modulación AM, control PID, etc.) puede anclar o puede agregar carga cognitiva sin pagarla. Antes de soltar un término aplicado, aplicar este test:

> Si borro el término aplicado y digo "este sistema" (o equivalente genérico), ¿el párrafo sigue funcionando? Si sí, el término estaba decorando: considerar borrarlo. Si no, el término estaba haciendo trabajo: dejarlo, y asegurarse de que el lector tenga al menos una imagen mental mínima de qué es.

Tres criterios prácticos:

- **Carga vs. trabajo.** Si el término aparece una vez como etiqueta y se sigue, funciona. Si es sujeto de tres oraciones, el lector necesita el concepto explicado.
- **Autodefinición por contexto.** "El filtro pasabajos del oído humano deja pasar las frecuencias bajas y atenúa las altas" se autodefine. "Aplicamos un filtro pasabajos para suavizar la señal" supone que el lector ya sabe qué es eso.
- **Asimetría con la matemática.** Los nombres físicos son opcionales en desarrollos puramente matemáticos. En cambio, en capítulos de sistemas (Cap. 4 en adelante) los nombres físicos pagan más, porque son el objeto de estudio.

---

## 8. Referencias cruzadas

### 8.1. Forma tipográfica

En prosa del libro, las referencias a partes del texto se escriben con la **palabra completa** seguida de `\ref{}`:

- *"el Capítulo~\ref{cap05}"*, *"la Sección~\ref{sec:serie_fourier}"*, *"la Subsección~\ref{subsec:prop_conjugacion}"*.
- En minúscula cuando el sustantivo común (*"esta sección"*, *"el capítulo anterior"*) y va sin `\ref{}`. Mayúscula inicial cuando se nombra una unidad específica con `\ref{}`.

**Prohibido el símbolo `§`** como abreviatura tipográfica:

- Evitar: `§\ref{...}`, `en~§\ref{...}`, `§5.3.6`.
- Reemplazar por: `la sección~\ref{...}`, `en la sección~\ref{...}`, `la Sección~5.3.6`.

El símbolo `§` se usa libremente en archivos meta del proyecto (`STYLE.md`, `DECISIONES.md`, `WORKFLOW.md`, `avance.md`, comentarios `%` de figuras, este documento) — pero no en el cuerpo del libro ni en presentaciones ni TPs.

**Tampoco** apostillas latinas como *"cf."* (ver §2): `(cf. capítulo~\ref{capXX})` → `(ver el capítulo~\ref{capXX})` o integrar la referencia en la prosa.

### 8.2. Referencias a capítulos futuros

Mantenerlas al mínimo estricto, máximo una por subsección, y solo cuando la conexión sea **estructuralmente necesaria** para el concepto, no meramente recordatoria. Preferir formulaciones que establezcan la relevancia del concepto actual sin nombrar explícitamente el capítulo destino.

- Correcto: *"esta propiedad simplifica el cálculo de coeficientes espectrales"*.
- Evitar: *"como veremos en el Capítulo 5, la paridad determina los coeficientes de Fourier nulos"*.

---

## 9. Vocabulario disponible

Los ejemplos y referencias se construyen con los conceptos **ya introducidos** hasta ese punto del libro. No invocar categorías que se definen más adelante.

- Evitar: usar "sistema no invariante en el tiempo" como ejemplo en una subsección que todavía no definió la invariancia temporal.
- Si el concepto a usar viene más adelante, reformular sin nombrarlo o elegir otro ejemplo.

---

## 10. Demostraciones

- La cadena de razonamiento que justifica el resultado presentado.
- No se exige el nivel de un tratado matemático, pero sí la trazabilidad lógica que permite al estudiante verificar la afirmación.
- Aplicar §3 (no saltear pasos) con énfasis: una demostración con saltos es la principal fuente de pérdida de lector.
- Cuando la demostración es extensa y no agrega valor pedagógico inmediato, puede omitirse con una referencia explícita.
- **Fin de demostración**: sin `\qed`, sin `$\square$`, sin "Q.E.D.", sin "demostrado". Las demostraciones terminan con la última línea de razonamiento, sin marcador.

---

## 11. Ejemplos: dos modalidades

Cada concepto relevante debe estar acompañado, **cuando sea pertinente y natural**, de un ejemplo. No se fuerzan cuando resultan obvios o redundantes con el texto principal.

**Criterio de selección entre ejemplos posibles**: cuando hay dos ejemplos válidos, gana el más simple. La simplicidad no es debilidad pedagógica; es respeto por el ancho de banda cognitivo del lector que está aprendiendo.

### Fenómeno físico o aplicación real

Siempre preferible cuando el concepto lo admite. El objetivo es que el estudiante reconozca el concepto en algo tangible antes de abstraerlo.

- Ej.: "el ruido térmico en un resistor es una señal aleatoria; la tensión de red eléctrica es determinista".
- Esta modalidad **no requiere cálculo**: alcanza con nombrar el fenómeno y explicar en qué aspecto ilustra el concepto.

### Ejemplo numerado

Reservado para conceptos cuya utilidad operativa solo se comprende ejecutando el procedimiento paso a paso.

- Ej.: descomponer una señal en sus partes par e impar.
- Debe resolverse completamente y llegar a un resultado verificable.
- En el texto se introduce con el título escueto *Ejemplo* (y numeración cuando hay varios en la misma sección), no *Ejemplo trabajado*.
- En ejemplos numerados, la regla §3 (no saltear pasos) es **estricta**: el ejemplo es el lugar donde el lector aprende a operar.

---

## 12. Figuras

Una ilustración del comportamiento descrito, especialmente cuando existe **geometría o evolución temporal** que el texto no puede transmitir con la misma claridad.

- Cada figura debe tener un `\label{}` y ser referenciada desde el texto.
- No se incluyen figuras decorativas: cada figura paga su lugar resolviendo algo que la prosa no resuelve.
- Convenciones técnicas de figuras: ver `README.md §4`.

---

## 13. Fraseo natural: estructuras que suenan traducidas

El registro del §2 apunta al **vocabulario**; esta sección apunta a la **estructura de la oración**. Una oración puede sonar rebuscada o ajena al castellano aunque cada palabra sea correcta: el lector la percibe como "rara" sin poder señalar la palabra culpable, porque el problema está en el armado. Este es el catálogo de los patrones recurrentes, para buscarlos explícitamente en una pasada de revisión.

**Principio que gobierna toda la sección: la estructura más simple que haga el trabajo.** Ante dos armados posibles, gana el simple, aunque el otro sea más compacto o suene más elegante. En la práctica: una predicación por oración siempre que se pueda; la afirmación principal en la oración principal, no colgada de un inciso o de una cola; y si una oración obliga a releerla para saber quién es el sujeto o a qué se refiere un pronombre, se parte en dos. La compresión no es un valor del libro; la claridad sí.

Caso frecuente de este vicio: la **oración-percha**, una afirmación adelante y varios apéndices colgando de un solo eje ---inciso con guiones, coordinada con *"y"*, cola con *"con + sustantivo"*---. Señales para cazarla: coma seguida de *"con + sustantivo"* al final de la oración; inciso con guiones que repite lo que la oración ya dijo; sinónimo de refuerzo en la misma oración (*completa/entera*, *todo/entero*); pronombre átono (*la*, *lo*, *le*) a más de una cláusula de su antecedente o con dos candidatos del mismo género compitiendo. Suele venir con un verbo de proceso donde el sustantivo ya hacía el trabajo (*"un punto del plano lo registra"* → *"un punto del plano es"*), que es el mismo vicio del `dar` comodín de §13.7.

### 13.1. Deícticos informales de lugar

El par **acá/allá** es de registro coloquial. En el cuerpo del libro:

- *acá* → *aquí*; *allá* → *allí*.
- Cuando *acá/allá* funcionan como taquigrafía de tiempo discreto frente a continuo (*"Allá $e^{j\omega t}$ era periódica… Acá el período es entero"*), preferir la referencia explícita: *"En el continuo…"*, *"En el discreto, en cambio,…"*. Es menos informal y, de paso, más claro.

### 13.2. Clivadas y comparativos antepuestos

Construcciones de foco antepuesto con sabor a traducción del inglés:

- Evitar: *"Lo que importa, sin embargo, no es tanto la fórmula como qué es $\lambda$."*
- Preferir: *"Ahora bien, más que la fórmula, importa qué es $\lambda$."*

La alarma es el molde *"Lo que + verbo + no es (tanto) X sino/como Y"*. Casi siempre sale más directo invirtiendo a *"Más que X, importa Y"* o *"X importa menos que Y"*. (Es distinto de la negación retórica *"no es arbitrario: sino…"*, tratada aparte en `DECISIONES.md`.)

### 13.3. Sujetos de cláusula nominal pesados

Una oración cuyo sujeto es una subordinada larga con *"Que + subjuntivo"* tiende a leerse pesada:

- Evitar: *"Que una secuencia sea, literalmente, una lista de números habilita algo imposible…"*
- Preferir: *"Como una secuencia es, literalmente, una lista de números, se puede…"* (causal con *como* + verbo activo).

No toda cláusula *"Que…"* antepuesta es mala: si es corta y el predicado es natural (*"Que el período deba ser entero es la fuente de todo"*), pasa. Se corrige cuando el sujeto es largo o el verbo principal es abstracto (*habilita*, *implica*, *conlleva*).

### 13.4. Perífrasis vacías y muletillas de realce

- Perífrasis de relativo que no aporta: *"cuál de las dos es la que vamos a estudiar"* → *"cuál de las dos vamos a estudiar"*. Señal: *"es la que / son los que / fue el que"* seguido de un verbo que ya bastaba solo.
- Muletillas de realce (*"Conviene…"*, *"Vale la pena…"*): son parte del registro docente y **no se prohíben**, pero se controla su densidad. Dos en la misma oración, o en oraciones contiguas, es una de más: reescribir una.

### 13.5. Ambigüedad de alcance adverbial

Un adverbio mal ubicado puede invertir el sentido:

- Evitar: *"esto deja de cumplirse siempre"* (¿"ya no siempre se cumple" o "siempre deja de cumplirse"?).
- Preferir: *"esto ya no es siempre cierto"*.

Revisar en particular *siempre*, *solo*, *todavía* y *también* cuando quedan entre el verbo y su complemento.

### 13.6. Vocabulario con connotación indebida

Palabras correctas cuyo matiz distrae:

- *"la notación que venimos arrastrando"* (*arrastrar* carga un tono de fastidio) → *"que venimos usando"*.
- Un término que colisiona con un tecnicismo del capítulo: *"una diferencia discreta pero importante"* en un capítulo sobre señales **discretas** → *"sutil pero importante"*.
- **Las muestras *ingresan*, no *entran*.** Para la llegada de una muestra o de un valor al sistema, el verbo es *ingresar*: *"la muestra que ingresa en $n$"*, *"desde ahí solo ingresan ceros"*. *Entrar* es de registro hablado y, además, choca con *entrada*, que es término definido. Vale para toda la familia (*entra*, *entró*, *entrar*).
- **Nada de *dibujar* ni *dibujo*.** La familia entera queda fuera del cuerpo del libro, de los TP y de las presentaciones. Es de registro escolar y casi siempre tapa la operación real. El reemplazo por defecto es *graficar*, y *trazar* sirve igual. Según lo que se esté diciendo: una curva, una secuencia o un diagrama se *grafican*; una secuencia invertida se *refleja* (no *se dibuja al revés*); una figura *muestra*, *exhibe* o *pone* algo; un eje *va con línea punteada*. El sustantivo *dibujo* como sinónimo de *lo que se ve en el panel* se reemplaza por *la figura*, *el panel* o el nombre del objeto graficado.

### 13.7. El verbo comodín *dar*

**`dar` no se usa para expresar el resultado de una cuenta, una operación o una definición.** Es el verbo que aparece cuando no se nombró la relación real entre lo que se hace y lo que se obtiene: el mismo *da* cubre *"vale"*, *"produce"*, *"conduce a"* y *"queda"*, y ninguno de esos matices llega al lector. Además es de registro hablado, y en prosa técnica se lee dejado.

La corrección **no es reemplazar mecánicamente por *resulta***: es preguntarse qué pasa exactamente y nombrarlo.

| Contexto | Evitar | Preferir |
|---|---|---|
| Valor numérico de una cuenta | *"la integral da el ancho de la banda"* | *"la integral vale el ancho de la banda"*, *"es igual a"* |
| Sustitución en una expresión | *"con $M=2$ eso da $y[0]=x[0]$"* | *"con $M=2$ queda $y[0]=x[0]$"* |
| Efecto de una operación | *"multiplicar por $(-1)^n$ da…"* | *"multiplicar por $(-1)^n$ desplaza el espectro"* (nombrar el efecto), *"produce"* |
| Consecuencia de aplicar una fórmula | *"la fórmula da $\delta[n-n_0]\leftrightarrow\ldots$"* | *"de la fórmula resulta…"*, *"la fórmula entrega…"* |
| Dos objetos que coinciden | *"$\lambda=0$ y $\lambda=2\pi$ dan la misma señal"* | *"corresponden a la misma señal"*, *"producen"* |
| Objeto al que se llega | *"sumar sus cuadrados da una serie del tipo $\sum 1/n^2$"* | *"sumar sus cuadrados conduce a una serie…"*, *"arroja"* |
| Una tabla o figura que exhibe algo | *"la columna de la derecha da la palabra de cuatro bits"* | *"muestra"*, *"lista"*, *"indica"* |
| Indiferencia | *"da igual"* | *"es indistinto"*, *"no importa"* |

Repertorio de reemplazo: *valer, quedar, ser igual a, equivaler a, obtenerse, producir, arrojar, conducir a, llevar a, resultar, entregar, mostrar*.

Dos precisiones:

- ***resultar en* es calco del inglés** (*results in*). Escribir *"de aquí resulta que…"*, *"esto produce…"*, *"esto conduce a…"*, no *"esto resulta en…"*. Es la misma alarma que el gerundio de consecuencia *"resultando en"*.
- **`dar` es legítimo** cuando no es comodín sino el verbo propio: *"el vector da una vuelta entera cada tres muestras"* (giro), *"dar lugar a"* (locución fija). Ahí se deja. Lo que se corrige es el `dar` que podría reemplazarse por un verbo más preciso sin perder nada.

---

### 13.8. Orden de palabras calcado del inglés

Además de los moldes de oración, hay calcos de **orden de palabras** que producen una lectura distinta de la buscada. El caso más traicionero es el *solo* posposado:

- Evitar: *"en ese eje entra un número solo"* (calco de *only one number*; en castellano *un número solo* se lee como *un número solitario*).
- Preferir: *"un solo número"*, *"solo un número"*, *"un único número"*.

Mismo cuidado con *también*, *siempre*, *todavía* e *incluso* cuando quedan detrás del sustantivo o entre el verbo y su complemento (ver §13.5). La prueba rápida es leer la oración en voz alta: si el adverbio parece calificar a la palabra equivocada, está mal ubicado.

---

### 13.9. Los dos puntos como muletilla de estructura

Los dos puntos anuncian que lo que sigue explica, enumera o precisa lo que se acaba de decir. Una vez en un párrafo, ordenan. Repetidos, se vuelven el molde por defecto de la prosa y el texto adquiere un ritmo de fichas ---afirmación, dos puntos, desarrollo--- que el lector termina oyendo por encima del contenido. Además suelen tapar un problema real: la relación entre las dos mitades quedó sin nombrar, y los dos puntos la insinúan en lugar de decirla, que es el mismo vicio del `dar` comodín de §13.7.

**La preferencia por defecto es la oración corrida. Los dos puntos entran cuando su claridad es superadora, no por costumbre.**

Dónde pagan su lugar:

- **Enumeración real** de varios elementos que vienen después.
- **Anuncio de una fórmula display** que el párrafo estaba preparando.
- **Definición o nombre** que se introduce inmediatamente después del objeto.

Dónde sobran, y por dónde salir:

| Función | Evitar | Preferir |
|---|---|---|
| Aposición explicativa | *"Cada aporte es del mismo tipo: el espectro convolucionado con un impulso."* | *"Cada aporte es el espectro convolucionado con un impulso."* |
| Remisión a algo ya visto | *"esa cuenta ya está hecha: la propiedad~\eqref{...} dice que…"* | *"esa cuenta ya está hecha en la propiedad~\eqref{...}, que dice…"* |
| Consecuencia | *"las copias también: el panel (c) es un tren infinito de triángulos."* | *"las copias también, y el panel (c) queda como un tren infinito de triángulos."* |
| Refuerzo de lo ya dicho | *"el resultado es el esperado: el espectro se replica."* | *"el resultado esperado es que el espectro se replique."* |

Prueba rápida en revisión: dos apariciones en el mismo párrafo, o en párrafos contiguos, son una de más. Reescribir la menos necesaria, no las dos.

---

### 13.10. Oraciones telegráficas: verbo elidido y sintagma desnudo

Una oración puede tener todas las palabras correctas y aun así leerse como el resumen de otra oración más completa, como si le faltaran conectores o artículos. El lector percibe una nota al margen donde esperaba prosa. El origen no es el vocabulario sino la **compresión sintáctica**: se eliden las articulaciones que la prosa académica hace explícitas.

Caso canónico: *"Queda el factor que multiplica a todo."* Tiene los tres huecos a la vez.

- **Verbo de actividad elidido.** La forma plena es *"Resta interpretar el factor…"*, *"Falta discutir…"*, *"Queda por examinar…"*. El verbo que dice qué se va a hacer con el objeto desapareció y quedó el existencial solo, sosteniendo un sustantivo. Eso es la gramática de un **título**, no de una frase.
- **Sintagma nominal sin anclaje.** *"el factor"* llega sin decir de dónde sale. La forma plena lo ata a su origen: *"el factor que multiplica a la suma en~\eqref{...}"*. Cuando el anclaje falta, suele aparecer en su lugar una perífrasis vaga (*"que multiplica a todo"*, *"lo que veníamos viendo"*), que identifica peor que el nombre propio del objeto ---aquí, $1/\Delta t$---.
- **Sin conector con lo anterior.** La oración aterriza sin bisagra. La forma plena dice de dónde viene: *"De las tres piezas…"*, *"De la ecuación anterior…"*.

**Prueba del título**: si la oración se puede pegar tal cual como `\subsubsection*{}` y funciona, está escrita como encabezado. Reescribirla como prosa.

Tres salidas, de menor a mayor intervención:

| Salida | Resultado |
|---|---|
| Reponer el verbo de actividad | *"Resta interpretar el factor $1/\Delta t$ que multiplica a la suma."* |
| Reponer verbo y conector | *"De la ecuación~\eqref{...} falta discutir el factor $1/\Delta t$."* |
| Eliminar el anuncio y abrir con el contenido | *"Las copias comparten el mismo factor $1/\Delta t$…"* |

La tercera es la preferida cuando el anuncio no orienta (ver §13.9): abrir un párrafo con su oración de menor densidad entierra la afirmación principal en segunda posición. La primera y la segunda valen cuando el pendiente sí orienta ---un tramo largo, varias piezas anunciadas---, porque ahí el anuncio hace trabajo de navegación.

---

### 13.11. Sujeto inestable y dobles lecturas

Dos fallas distintas con el mismo síntoma: el lector tiene que volver atrás y releer.

**Sujeto que cambia sin aviso bajo una coordinación con *y*.** La *y* promete continuidad, así que el lector arrastra el sujeto de la cláusula anterior. Si la siguiente tiene otro sujeto tácito, se produce un desvío de lectura real, no una incomodidad estética.

- Evitar: *"Las copias lo comparten y no depende de $k$, así que afecta a cada una por igual."* El sujeto va copias → factor → factor, y se lee por un instante *"las copias no dependen de $k$"*.
- Preferir: una predicación por oración, sujeto estable en cada una, premisa al frente. *"Como no depende de $k$, el factor escala a todas las copias por igual."*

**Artículo y pronombre homófonos en contacto.** Secuencias como *la fija*, *la que la marca*, *lo que lo determina*: el lector parsea el primer elemento como artículo y el segundo como sustantivo o adjetivo, y descubre tarde que eran pronombre más verbo.

- Evitar: *"La banda base no depende de la señal: la fija el muestreo."* (*la fija* se lee primero como sintagma nominal, *la fija* frente a *la móvil*).
- Preferir: el sujeto adelante. *"La frecuencia de muestreo $\omega_s$ determina la banda base."*

El orden objeto-verbo-sujeto agrava las dos, porque obliga a esperar al final para saber quién hace qué. Preferir sujeto-verbo-objeto salvo que haya una razón de énfasis que lo justifique.
