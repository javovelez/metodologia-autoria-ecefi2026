# -*- coding: utf-8 -*-
"""Ensambla el repositorio de muestras a partir de los repos de cátedra (solo lectura)."""
import io, os, shutil, sys

PROY = os.path.expanduser("~/Documents/proyectos")
DEST = sys.argv[1]

BASURA = (".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz", ".nav",
          ".snm", ".toc", ".bbl", ".blg", ".DS_Store", ".rollback")
DIRS_FUERA = {"archivo", "archivo_ignorar", "_legacy", "__pycache__", ".git"}

def sirve(nombre):
    return not (nombre.endswith(BASURA) or nombre == ".DS_Store")

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

# --- ASyS: figuras 3D del capítulo 2 (fuente TikZ y salida compilada) --------
FIG3D = ["22/fig_espirales_omega", "22/fig_espirales_sigma", "22/fig_vector_giratorio",
         "24/fig_superficie_magnitud", "24/fig_superficies_z2",
         "26/fig_topografia_polos_ceros", "28/taylor_complejo",
         "28/taylor_vs_laurent", "28/fig_regiones_convergencia"]
for ruta in FIG3D:
    sec, fig = ruta.split("/")
    copiar_dir("libro_asys/02capitulo/%s/figures/%s" % (sec, fig),
               "asys/figuras-3d/%s" % fig)

# --- TC2: trabajo práctico 4 (enunciado, resolución y presentación) ----------
copiar_dir("libro-tc2/gabinete/tp4", "tc2/tp4")
for f in os.listdir(os.path.join(DEST, "tc2/tp4")):
    if f.endswith(".docx"): os.remove(os.path.join(DEST, "tc2/tp4", f))

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
for s in ["write_section", "review_section", "create_2d_figures", "3d_figures"]:
    copiar_dir("libro_asys/.claude/skills/%s" % s, "metodo/skills/%s" % s)

# El renombre alcanza a las referencias al brief dentro de lo publicado: si no,
# WORKFLOW.md y los skills apuntarían a un archivo que en el árbol no existe.
# Solo cambia el nombre del archivo; el resto del texto se publica tal cual.
for raiz, _, archivos in os.walk(os.path.join(DEST, "metodo")):
    for a in archivos:
        if not a.endswith(".md"): continue
        ruta = os.path.join(raiz, a)
        with io.open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        if BRIEF_ORIGEN not in texto: continue
        with io.open(ruta, "w", encoding="utf-8") as fh:
            fh.write(texto.replace(BRIEF_ORIGEN, BRIEF))

print("ensamblado en", DEST)
