---
name: review_section
description: Protocolo para auditar una sección o subsección ya escrita (libro, apuntes, TPs) contra STYLE.md y DECISIONES.md. Detecta saltos de pasos, pérdidas de intuición, referentes vagos, tics de redacción automática, fraseo torcido, vocabulario fuera de calibración y errores de notación, y reporta hallazgos con propuestas concretas. No reescribe sin pedido explícito.
---

# Revisar una sección

El skill audita una sección ya escrita. No reescribe por su cuenta. Detecta problemas, los reporta con la cita exacta y propone una corrección concreta, que el usuario acepta o rechaza. Sirve para sostener una voz pareja en un libro que se edita en momentos distintos.

---

## Bloque 1. Lecturas previas

1. `STYLE.md` completo. Es el documento contra el que se compara.
2. `DECISIONES.md` completo.
3. `NOTATION.md`.
4. `avance.md`, la entrada de la sección y las vecinas, para verificar que no se invoquen conceptos no introducidos ni se repitan ejemplos.
5. El archivo `.tex` a revisar. En un apunte, además, `fourier_discreto/REDACCION.md`.

---

## Bloque 2. Alcance

Por defecto se revisan todas las dimensiones: estilo y fraseo, vocabulario, notación, coherencia con el resto del libro y estructura de entornos. El usuario puede pedir un subconjunto.

Hay dos niveles de exigencia. La **auditoría completa** reporta todo, incluidas las faltas menores, y se usa al cerrar una sección. El modo **alertas** reporta solo lo que afecta claramente la legibilidad o el rigor, y se usa en iteraciones intermedias. Si no está claro cuál quiere el usuario, se le pregunta.

---

## Bloque 3. Auditoría

### 3.1. Barrido léxico

Se corren los barridos de `STYLE.md §17` sobre el archivo. Los resultados tienen falsos positivos (*"da una vuelta"*, *"hacen falta"*, un dos puntos antes de una fórmula display) y se evalúan uno por uno. Solo se reportan los casos que admiten una forma mejor, con la forma propuesta.

### 3.2. Lectura de las aperturas

Se extraen las primeras oraciones de todos los párrafos y se leen seguidas.

```bash
python3 - archivo.tex <<'EOF'
import re,sys
t=open(sys.argv[1]).read().split(r'\begin{document}')[-1]
t=re.sub(r'(?<!\\)%.*','',t)
for p in re.split(r'\n\s*\n',t):
    p=' '.join(p.split())
    if len(p)<120 or p.startswith('\\'): continue
    m=re.match(r'(.+?[.?!])(\s|$)',p)
    s=m.group(1) if m else p
    print(len(s.split()), s[:160])
EOF
```

Se reporta el patrón si muchas aperturas tienen menos de diez palabras, si empiezan con un sustantivo abstracto (*la maniobra*, *la verificación*, *el recorrido*, *la clave*) o con un demostrativo (*ese*, *esa*, *esos*), o si comparten el mismo molde (`STYLE.md §14.3` y `§15`).

### 3.3. Categorías de hallazgo

**Referentes vagos** (`STYLE.md §14.1`). Pronombres o demostrativos cuyo antecedente está más atrás que la oración anterior o compite con otro. Párrafos que abren apoyados en el párrafo anterior. Sustantivos abstractos en lugar del objeto.

**Oraciones comprimidas** (`STYLE.md §14.2`). Verbo elidido, sintagma sin anclaje, conceptos encadenados sin desarrollar.

**Huella de la redacción automática** (`STYLE.md §15`). Em-dashes, oraciones cortas de intriga, dos puntos de revelación, cierres sentenciosos, negación seguida de corrección, adverbios de refuerzo, verbos figurados, énfasis retórico. Si un tic aparece una sola vez se reporta como menor; si se repite a lo largo de la sección se reporta como crítico, porque la repetición es lo que el lector percibe.

**Fraseo** (`STYLE.md §14.4` a `§14.10`). Oración-percha, dos puntos de más, anuncio o conclusión repetidos, contenido enunciado en negativo, sujeto inestable, dobles lecturas, calcos del inglés.

**Saltos de pasos** (`STYLE.md §3`). Frases como *"es fácil ver que"*, cadenas con un paso oculto, cuentas descriptas en prosa en lugar de escritas, casos omitidos con *"la otra dirección es similar"*.

**Pérdida de intuición** (`STYLE.md §5`). Desarrollos largos sin una oración que diga qué se obtuvo, definiciones sin lectura, cierres que terminan en la última fórmula o que desarrollan la sección siguiente.

**Registro** (`STYLE.md §2` y `§16`). Coloquialismos, construcciones rimbombantes, nominalizaciones forzadas, verbos comodín, vocabulario fijado mal usado.

**Precisión** (`STYLE.md §9`). Términos usados fuera de su definición o en su sentido corriente, perífrasis de un término ya definido, afirmaciones sin cuantificar, propiedades demostradas sobre un caso particular.

**Estructura** (`STYLE.md §11` a `§13`). Tesis prematura en la apertura, ejemplos sin pregunta, dos derivaciones del mismo resultado, formas de una fórmula que no se usan, títulos que nombran el montaje, instrumentos usados antes de su propósito, definiciones duplicadas.

**Figuras en la prosa** (`STYLE.md §12`). Representaciones descriptas sin figura, figuras que llegan después del razonamiento, figuras o tablas no nombradas, paneles citados sin la figura, término del resultado usado antes de derivarlo.

**Cadencia** (`STYLE.md §6`). Dos fórmulas display seguidas sin prosa, fórmulas compuestas escritas en línea, párrafos cargados de casos paralelos que deberían ser tabla.

**Vocabulario disponible** (`STYLE.md §7` y `§9`, `DECISIONES.md §3`). Términos usados antes de su capítulo, términos aplicados que decoran, más de una referencia a capítulos futuros por subsección.

**Notación** (`NOTATION.md`). `i` por `j`, `z^*` por `\bar{z}`, `x_e`/`x_o`, `°` Unicode, paréntesis y corchetes mezclados, soporte como conjunto, caracteres Unicode, `\eqref` suelto.

**Entornos.** Cuadros `resultado` con explicaciones adentro o sin título, demostraciones con marcador de cierre.

**Coherencia con `avance.md`.** Notación que cambia respecto de una sección anterior, ejemplos repetidos, conceptos invocados antes de definirse.

### 3.4. Formato de cada hallazgo

1. **Ubicación**: número de línea y cita textual breve.
2. **Categoría** y regla de `STYLE.md` en juego.
3. **Diagnóstico**: qué problema concreto hay.
4. **Propuesta**: la oración corregida, escrita entera. La propuesta cumple ella misma todas las reglas; una corrección que introduce un em-dash o un dos puntos de presentación no sirve.

### 3.5. Reporte

```markdown
# Revisión de la Sección X.Y

Modo: auditoría completa | alertas
Dimensiones revisadas: ...

## Hallazgos críticos
### 1. Categoría
- Ubicación: línea N, "cita"
- Diagnóstico: ...
- Propuesta: ...

## Hallazgos menores

## Coherencia con el resto del libro

## Resumen
N hallazgos críticos y M menores. Veredicto en una o dos oraciones.
```

---

## Bloque 4. Después de revisar

- Las propuestas no se aplican automáticamente. El usuario decide cuáles acepta.
- Si pide aplicarlas, se aplican de a una o por categoría, para que se pueda seguir el rastro.
- Después de aplicarlas se relee la sección entera y no solo las líneas tocadas, porque una corrección local puede romper un referente o el empalme con el párrafo siguiente.
- Si la sección queda estable, se ofrece `update_avance` sin ejecutarlo.
