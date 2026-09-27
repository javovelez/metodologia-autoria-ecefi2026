# -*- coding: utf-8 -*-
"""Ensambla el repositorio de muestras a partir de los repos de cátedra (solo lectura)."""
import io, os, shutil, sys

PROY = os.path.expanduser("~/Documents/proyectos")
DEST = sys.argv[1]

BASURA = (".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz", ".nav",
          ".snm", ".toc", ".bbl", ".blg", ".DS_Store", ".rollback")
DIRS_FUERA = {"archivo", "archivo_ignorar", "_legacy", "__pycache__", ".git"}

def sirve(nombre):
    # Los .synctex aparecen con sufijos variables —.gz, (busy)— mientras compila
    # el repo de origen, así que se descartan por nombre y no por extensión.
    return not (nombre.endswith(BASURA) or nombre == ".DS_Store" or ".synctex" in nombre)

def copiar_dir(src, dst, solo=None):
    src = os.path.join(PROY, src); dst = os.path.join(DEST, dst)
    for raiz, dirs, archivos in os.walk(src):
        dirs[:] = [d for d in dirs if d not in DIRS_FUERA]
        rel = os.path.relpath(raiz, src)
        for a in archivos:
            if not sirve(a): continue
            if solo and not a.endswith(solo): continue
            d = os.path.join(dst, rel) if rel != "." else dst
            os.makedirs(d, exist_ok=True)
            shutil.copy2(os.path.join(raiz, a), os.path.join(d, a))

def copiar(src, dst):
    src = os.path.join(PROY, src); dst = os.path.join(DEST, dst)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)

# --- ASyS: capítulo 5 completo (texto + figuras como código fuente) ----------
# Solo las figuras que el texto del capítulo incluye: las que quedaron en la
# carpeta sin estar referenciadas no se publican.
import re as _re
_INC = _re.compile(r"\\include(?:standalone|graphics)(?:\[[^\]]*\])?\{[^}]*?figures/([^/}]+)/")
EXCLUIDAS = {"fig_exponencial_general"}

def figuras_usadas(dir_cap):
    usadas = set()
    for raiz, dirs, archivos in os.walk(dir_cap):
        dirs[:] = [d for d in dirs if d != "figures"]
        for a in archivos:
            if a.endswith(".tex"):
                usadas |= set(_INC.findall(
                    open(os.path.join(raiz, a), encoding="utf-8", errors="replace").read()))
    return usadas - EXCLUIDAS

copiar("libro_asys/05capitulo/Capitulo05.pdf", "asys/capitulo-05/Capitulo05.pdf")
copiar("libro_asys/05capitulo/Capitulo05.tex", "asys/capitulo-05/Capitulo05.tex")
for s in "12345":
    copiar_dir("libro_asys/05capitulo/5%s" % s, "asys/capitulo-05/5%s" % s)
copiar("libro_asys/setup.tex", "asys/setup.tex")

_usadas = figuras_usadas(os.path.join(PROY, "libro_asys/05capitulo"))
for s in "12345":
    d = os.path.join(DEST, "asys/capitulo-05/5%s/figures" % s)
    if not os.path.isdir(d): continue
    for fig in sorted(os.listdir(d)):
        r = os.path.join(d, fig)
        if os.path.isdir(r) and fig not in _usadas:
            shutil.rmtree(r)

# --- ASyS: guías de trabajos prácticos 1 a 7, con sus resoluciones -----------
for n in range(1, 8):
    copiar_dir("libro_asys/Gabinete/tp%d" % n, "asys/guias/tp%d" % n)
# El TP4 viene partido en dos en el repo de origen, bajo nombres con mayúscula y
# espacio que no sirven para una URL. Se publican en minúscula y con guion.
for viejo, nuevo in [("Parte a", "parte-a"), ("Parte b", "parte-b")]:
    origen = os.path.join(DEST, "asys/guias/tp4", viejo)
    if os.path.isdir(origen):
        os.rename(origen, os.path.join(DEST, "asys/guias/tp4", nuevo))
# La carpeta del TP4 lleva adentro una copia del capítulo 6 del libro, como
# material de consulta. Del libro se publica el capítulo 5 y ningún otro.
_cap6 = os.path.join(DEST, "asys/guias/tp4/parte-a/Capitulo06.pdf")
if os.path.isfile(_cap6): os.remove(_cap6)

# --- ASyS: animaciones (se excluyen las del capítulo 10, aún sin terminar) ---
ANIM = ["convolucion_dos_pulsos", "convolucion_pulso_exp", "convolucion_dos_exp",
        "exponencial_copleja", "muestreo_espectro", "serie_fourier_cuadrada"]
for a in ANIM:
    copiar_dir("libro_asys/animaciones/%s" % a, "asys/animaciones/%s" % a)
    for raiz, _, archivos in os.walk(os.path.join(DEST, "asys/animaciones", a)):
        for f in archivos:
            # el .js de las carpetas viejas no está sincronizado con el HTML publicado
            if f.endswith(".js"):
                os.remove(os.path.join(raiz, f))
            # los lanzadores de Moodle enlazan al campus, que es privado, y uno ni
            # siquiera tiene las URL cargadas: fuera del campus no sirven
            elif f.startswith("moodle_"):
                os.remove(os.path.join(raiz, f))

# --- ASyS: presentaciones de clase, solo la salida compilada -----------------
# Las dieciséis clases cubren los capítulos 1 a 10, así que ninguna cae en el
# material sin revisar. La fuente Beamer no se publica: incluye figuras del libro
# por ruta relativa y fuera de su repo esos \includegraphics no resolverían.
for n in range(1, 17):
    clase = "clase%02d" % n
    copiar("libro_asys/Presentaciones/%s/%s.pdf" % (clase, clase),
           "asys/presentaciones/%s.pdf" % clase)

# --- TC2: trabajo práctico 4 (enunciado, resolución y presentación) ----------
# El subárbol espeja la raíz del repo de origen para que los \input relativos
# de las fuentes resuelvan donde quedan publicadas.
copiar("libro-tc2/setup.tex", "tc2/setup.tex")
copiar_dir("libro-tc2/gabinete/tp4", "tc2/gabinete/tp4")
# El enunciado no se publica: está en revisión. Se publican la resolución y la
# presentación con que se dicta.
_tp4 = os.path.join(DEST, "tc2/gabinete/tp4")
for f in os.listdir(_tp4):
    if f.endswith(".docx") or f.startswith("TC-TP4-24-enunciado"):
        os.remove(os.path.join(_tp4, f))

# --- RNP: cuaderno entregable, sin resolver ---------------------------------
# La fuente .lab.md queda fuera: lleva adentro los bloques ```python solution```.
for lab in ["3a", "4a", "5a"]:
    copiar("RNP-labs/_TPS/Laboratorios/Laboratorio_%s.ipynb" % lab,
           "rnp/laboratorios/Laboratorio_%s.ipynb" % lab)

# --- El método: especificaciones e instrucciones modulares de ASyS -----------
# El brief de arranque se publica como AGENTS.md. En el repo de cátedra lleva el
# nombre que carga por defecto la herramienta con la que se trabaja; ese nombre es
# de la herramienta y no del método, así que acá no se arrastra. README.md queda
# libre para lo que nombra en el repo de origen: la referencia técnica del libro.
BRIEF_ORIGEN, BRIEF = "CLAUDE.md", "AGENTS.md"
ESPECIFICACIONES = [(BRIEF_ORIGEN, BRIEF), ("STYLE.md", "STYLE.md"),
                    ("NOTATION.md", "NOTATION.md"), ("WORKFLOW.md", "WORKFLOW.md")]
for origen, publicado in ESPECIFICACIONES:
    copiar("libro_asys/%s" % origen, "metodo/especificaciones/%s" % publicado)
SKILLS = ["write_section", "review_section", "create_2d_figures", "3d_figures"]
for s in SKILLS:
    copiar_dir("libro_asys/.claude/skills/%s" % s, "metodo/skills/%s" % s)

# Las tablas de skills del brief y de WORKFLOW.md enumeran todos los del repo de
# origen, y de las instrucciones modulares se dice que son algunas, sin declarar
# cuántas hay. De esas tablas se quitan las filas de los skills que no se
# publican; las menciones sueltas en la prosa quedan, porque no cuentan nada.
_TODOS = set(os.listdir(os.path.join(PROY, "libro_asys/.claude/skills")))
_FILA_SKILL = _re.compile(r"^\|\s*`/?([\w-]+)`\s*\|")

def fila_fuera(linea):
    m = _FILA_SKILL.match(linea)
    return bool(m) and m.group(1) in _TODOS and m.group(1) not in SKILLS

# Un párrafo con una ruta del equipo del autor describe su instalación local y
# no el método, así que tampoco se publica.
def parrafo_local(p):
    return "~/.claude/" in p or "/Users/" in p

# El renombre alcanza a las referencias al brief dentro de lo publicado: si no,
# WORKFLOW.md y los skills apuntarían a un archivo que en el árbol no existe.
# Fuera de ese renombre y de los dos filtros de arriba, el texto se publica tal cual.
for raiz, _, archivos in os.walk(os.path.join(DEST, "metodo")):
    for a in archivos:
        if not a.endswith(".md"): continue
        ruta = os.path.join(raiz, a)
        with io.open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        nuevo = texto.replace(BRIEF_ORIGEN, BRIEF)
        nuevo = "".join(l for l in nuevo.splitlines(True) if not fila_fuera(l))
        nuevo = "\n\n".join(p for p in nuevo.split("\n\n") if not parrafo_local(p))
        if nuevo == texto: continue
        with io.open(ruta, "w", encoding="utf-8") as fh:
            fh.write(nuevo)

print("ensamblado en", DEST)
