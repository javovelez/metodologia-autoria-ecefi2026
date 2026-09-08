---
name: review_section
description: Protocolo para auditar una sección o subsección ya escrita contra los principios de STYLE.md y DECISIONES.md. Detecta saltos de pasos, pérdidas de intuición, deriva tonal, fraseo torcido, vocabulario fuera de calibración, y reporta hallazgos con propuestas concretas. No reescribe sin pedido explícito.
---

# Review Book Section — Protocol

Este skill ejecuta una **auditoría de coherencia** sobre una sección o subsección del libro ya escrita. No reescribe el contenido por cuenta propia: detecta problemas, los reporta con cita específica, y propone correcciones que el usuario acepta o rechaza.

El skill es la herramienta para mantener la voz consistente a lo largo de un libro vivo donde las secciones se editan en distintos momentos y el riesgo permanente es la deriva.

---

## Bloque 1 — Pre-flight

1. **`STYLE.md`** completo. Es el documento contra el cual se compara.
2. **`DECISIONES.md`** completo. Es la otra mitad del criterio.
3. **`NOTATION.md`** para chequeos de notación.
4. **`avance.md`** — entrada de la sección a revisar y entradas vecinas, para verificar que no se invocan conceptos no introducidos ni se duplican ejemplos.
5. **El archivo `.tex` a revisar**.

---

## Bloque 2 — Deliberación

### 2.1. Definir el alcance de la revisión

Antes de auditar, declarar qué dimensiones se chequean:

- **Estilo y tono**: pilares, registro natural, no saltear pasos, sostener intuición, cadencia.
- **Vocabulario aplicado**: test del borrado, vocabulario disponible, referencias a capítulos futuros.
- **Notación**: convenciones de `NOTATION.md`.
- **Coherencia con el resto del libro**: contra `avance.md`, sin reintroducir conceptos ya definidos ni invocar los no definidos.
- **Estructura y entornos**: posición evaluada de cuadros `resultado`, fin de demostraciones sin marcador, etc.

Por defecto se revisan las cinco dimensiones. El usuario puede pedir un subconjunto ("solo notación", "solo estilo").

### 2.2. Calibrar el nivel de exigencia

- **Modo "auditoría completa"**: se reporta todo, incluyendo violaciones menores. Útil cuando se cierra una sección.
- **Modo "alertas"**: se reportan solo violaciones que afectan claramente la legibilidad o el rigor. Útil para iteraciones intermedias.

Preguntar al usuario qué modo prefiere si no está claro.

---

## Bloque 3 — Ejecución de la auditoría

Recorrer el archivo y registrar hallazgos por categoría. Cada hallazgo se reporta con:

1. **Localización**: número de línea o cita textual breve.
2. **Categoría**: cuál regla/principio está en juego.
3. **Diagnóstico**: qué problema concreto se observa.
4. **Propuesta**: una alternativa concreta, no abstracta.

### 3.1. Categorías de hallazgo

**Saltos de pasos** (`STYLE.md §3`):

- Frases-señuelo: *"es fácil ver que"*, *"se sigue inmediatamente"*, *"un cálculo directo muestra"*, *"como sabemos"*, *"de forma análoga"* sin caso análogo desarrollado.
- Cadenas algebraicas con un paso oculto entre dos líneas que no es trivial al ojo del lector que aprende.
- Demostraciones donde un caso ("la otra dirección es similar") se omite sin justificación.

**Pérdida de intuición** (`STYLE.md §5`):

- Desarrollos algebraicos de más de tres líneas sin oración de reconexión.
- Definiciones formales sin lectura en prosa inmediatamente después.
- Cierres de subsección que terminan en una fórmula sin retorno a qué se ganó.

**Deriva tonal** (`STYLE.md §2`):

- Construcciones rimbombantes o poéticas: *"pulcra superposición"*, *"monumentales"*, *"mágicas"*.
- Coloquialismos imprecisos: *"integrar sobre la nada"* en lugar de *"integrar curvas nulas"*.
- Nominalizaciones forzadas: *"el acotamiento"* en lugar de *"al acotar"*.

**Fraseo torcido y registro deíctico** (`STYLE.md §13`):

Estructuras que suenan traducidas o coloquiales aunque cada palabra sea correcta. Varias son léxicas y conviene **empezar por un barrido `grep -niE`** (insensible a mayúsculas, para no perder los señuelos que abren oración) antes de la lectura fina:

```
grep -niE "\b(acá|allá)\b" archivo.tex            # deícticos informales (§13.1)
grep -niE "no es tanto|lo que .* no es" archivo.tex  # clivadas antepuestas (§13.2)
grep -niE "\b(es|son|fue|era) (la|el|los|las) que\b" archivo.tex  # perífrasis vacías (§13.4)
grep -niE "deja de .*(siempre|solo)|(siempre|solo|todavía) (se|es|vale)" archivo.tex  # alcance adverbial (§13.5)
grep -niE "\b(da|dan|daba|daban|dará|darán|dio|dieron|dando)\b" archivo.tex  # verbo comodín dar (§13.7)
grep -niE "resulta(n|ndo)? en\b" archivo.tex      # calco "results in" (§13.7)
```

- Deícticos coloquiales *acá/allá*, incluidos los usados como taquigrafía continuo/discreto sin referencia explícita (§13.1).
- Clivadas y comparativos antepuestos: *"Lo que … no es (tanto) X sino/como Y"* (§13.2).
- Sujetos de cláusula nominal pesados: *"Que … habilita/implica algo…"* con sujeto largo o verbo abstracto (§13.3).
- Perífrasis de relativo vacías: *"es la que / son los que"* + verbo que bastaba solo (§13.4).
- Muletillas de realce (*"Conviene…"*, *"Vale la pena…"*) dos veces en oraciones contiguas (§13.4).
- Ambigüedad de alcance adverbial: *siempre/solo/todavía* mal ubicados, p. ej. *"deja de cumplirse siempre"* (§13.5).
- Vocabulario con connotación indebida (*"arrastrando"*) o que colisiona con un tecnicismo del capítulo (*"diferencia discreta"* en un capítulo sobre lo discreto) (§13.6).
- Verbo comodín *dar* expresando resultado: *"la integral da cero"*, *"eso da $y[0]=x[0]$"*, *"la fórmula da…"*, *"da igual"* (§13.7). El barrido `grep` levanta muchos falsos positivos legítimos (*"da una vuelta"*, *"dar lugar a"*): reportar solo los que admiten un verbo más preciso, y proponer cuál (*vale*, *queda*, *produce*, *conduce a*, *arroja*, *muestra*). Incluir aquí el calco *"resultar en"*.

**Cadencia rota** (`STYLE.md §6`):

- Dos o más fórmulas display consecutivas sin prosa intermedia (fuera de cuadros `resultado`).
- Fórmula display sin amarra textual ni antes ni después.

**Vocabulario aplicado mal calibrado** (`STYLE.md §7`, `DECISIONES.md §3`):

- Términos en la lista "prohibido hasta introducción" usados antes de tiempo.
- Términos en la lista "requiere glosa" usados sin contexto autodefinitorio.
- Términos donde el test del borrado sugiere que decoran sin pagar.

**Referencias futuras excesivas** (`STYLE.md §8`):

- Más de una referencia a capítulos futuros por subsección.
- Referencias nominales ("como veremos en el Capítulo 5") en lugar de funcionales.

**Vocabulario no disponible** (`STYLE.md §9`):

- Conceptos invocados como ejemplo o explicación que se definen formalmente más adelante.

**Notación incorrecta** (`NOTATION.md`):

- `i` en lugar de `j`.
- `z^*` en lugar de `\bar{z}`.
- `x_e`/`x_o` en lugar de `x_p`/`x_i`.
- Símbolo Unicode `°` en lugar de `$90^\circ$`.
- Paréntesis en lugar de corchetes para señales discretas (o viceversa).

**Estructura de entornos**:

- Cuadros `resultado` con explicaciones adentro (deben ir afuera, en la prosa).
- Cuadros `resultado` sin título.
- Demostraciones con `\qed` o `$\square$`.

**Coherencia con `avance.md`**:

- Notación introducida en esta sección que ya estaba en una sección anterior con otro símbolo.
- Ejemplo numérico repetido idéntico al de otra sección.
- Concepto invocado que `avance.md` muestra que se define más adelante.

### 3.2. Estructura del reporte

```markdown
# Revisión de [sección/subsección X.Y]

**Modo:** auditoría completa | alertas
**Dimensiones revisadas:** [...]

## Hallazgos críticos

[Hallazgos que afectan claramente la legibilidad o el rigor]

### 1. [Categoría]
- **Localización:** línea N, *"cita textual breve…"*
- **Diagnóstico:** [qué pasa]
- **Propuesta:** [alternativa concreta]

## Hallazgos menores

[Hallazgos de pulido, opcionales]

## Coherencia con el resto del libro
[Verificación contra avance.md]

## Resumen
[N hallazgos críticos, M menores. Veredicto general.]
```

---

## Bloque 4 — Post-revisión

- **No aplicar las propuestas automáticamente.** El skill reporta; el usuario decide cuáles aceptar y cuáles no.
- Si el usuario pide aplicar correcciones, hacerlo de a una o por categoría, no en bloque, para preservar la trazabilidad.
- Si después de las correcciones la sección queda en estado estable, ofrecer ejecutar `update_avance` (sin hacerlo automáticamente).
