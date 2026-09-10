# -*- coding: utf-8 -*-
"""Cataloga las figuras del libro de ASyS: copia fuentes, rasteriza miniaturas y
genera catalogo.html. El libro se lee, nunca se modifica."""
import html, json, os, re, shutil, subprocess, sys

LIBRO = os.path.expanduser("~/Documents/proyectos/libro_asys")
DEST  = sys.argv[1]
REPO  = "https://github.com/javovelez/metodologia-autoria-ecefi2026/blob/main"

# ------------------------------------------------------------------ LaTeX -> HTML
LLAVES = re.compile(r"\\(textbf|textit|emph|text|mathrm|si|unit)\{")

def sacar_llave(s, i):
    """Devuelve (contenido, posición tras la llave de cierre) para s[i] == '{'."""
    prof, j = 0, i
    while j < len(s):
        if s[j] == "{" and (j == 0 or s[j-1] != "\\"): prof += 1
        elif s[j] == "}" and s[j-1] != "\\":
            prof -= 1
            if prof == 0: return s[i+1:j], j + 1
        j += 1
    return s[i+1:], len(s)

def limpiar_leyenda(t):
    """Deja texto plano con el math entre $...$ intacto, para que KaTeX lo componga."""
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\\(label|ref|autoref|cref)\{[^}]*\}", "", t)
    # las llaves de énfasis se disuelven; el contenido queda
    while True:
        m = LLAVES.search(t)
        if not m: break
        dentro, fin = sacar_llave(t, m.end() - 1)
        t = t[:m.start()] + dentro + t[fin:]
    t = t.replace("\\\\", " ").replace("~", "\u00a0")
    t = t.replace("\\%", "%").replace("\\&", "&").replace("\\_", "_")
    t = re.sub(r"\\(par|centering|small|footnotesize|normalsize)\b", "", t)
    return re.sub(r"\s+", " ", t).strip(" .") + "."

def leyendas_de(ruta_sec):
    """{id_de_figura: leyenda} para un archivo .tex cualquiera."""
    try:
        s = open(ruta_sec, encoding="utf-8", errors="replace").read()
    except OSError:
        return {}
    s = re.sub(r"(?m)(?<!\\)%.*$", "", s)
    salida = {}
    for bloque in re.findall(r"\\begin\{figure\}.*?\\end\{figure\}", s, re.S):
        figs = re.findall(r"\\include(?:standalone|graphics)(?:\[[^\]]*\])?\{[^}]*?figures/([^/}]+)/",
                          bloque)
        m = re.search(r"\\caption\{", bloque)
        if not (figs and m): continue
        cap = limpiar_leyenda(sacar_llave(bloque, m.end() - 1)[0])
        for f in figs:
            salida.setdefault(f, cap)
    return salida

# ------------------------------------------------------------------ recorrido
BASURA = (".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz", ".DS_Store")
# Del capítulo 11 en adelante no se publica nada: no está revisado.
ULTIMO_CAPITULO = 10
CAPS = [(("%02d" % n) + "capitulo", n) for n in range(1, ULTIMO_CAPITULO + 1)]

# Figuras que quedan fuera por decisión del autor, aunque el libro las use.
EXCLUIDAS = {"fig_exponencial_general"}

INCLUSION = re.compile(r"\\include(?:standalone|graphics)(?:\[[^\]]*\])?\{[^}]*?figures/([^/}]+)/")

def figuras_usadas(dir_cap):
    """Las que el texto del capítulo efectivamente incluye. Se ignoran los .tex de
    las propias figuras, que se incluyen a sí mismos."""
    usadas = set()
    for raiz, dirs, archivos in os.walk(dir_cap):
        dirs[:] = [d for d in dirs if d != "figures"]
        for a in archivos:
            if a.endswith(".tex"):
                usadas |= set(INCLUSION.findall(
                    open(os.path.join(raiz, a), encoding="utf-8", errors="replace").read()))
    return usadas

catalogo = []
raiz_fig  = os.path.join(DEST, "asys", "figuras")
raiz_mini = os.path.join(DEST, "asys", "miniaturas")

for carpeta, num in CAPS:
    dir_cap = os.path.join(LIBRO, carpeta)
    if not os.path.isdir(dir_cap): continue
    tex_cap = [f for f in os.listdir(dir_cap) if re.fullmatch(r"Capitulo\d+\.tex", f)]
    titulo = "Capítulo %d" % num
    if tex_cap:
        m = re.search(r"\\chapter\{([^}]*)\}",
                      open(os.path.join(dir_cap, tex_cap[0]), encoding="utf-8",
                           errors="replace").read())
        if m: titulo = m.group(1).strip()

    usadas = figuras_usadas(dir_cap) - EXCLUIDAS

    figuras = []
    for sec in sorted(d for d in os.listdir(dir_cap) if re.fullmatch(r"\d+", d)):
        dir_sec = os.path.join(dir_cap, sec)
        leyendas = leyendas_de(os.path.join(dir_sec, "sec%s.tex" % sec))
        dir_figs = os.path.join(dir_sec, "figures")
        if not os.path.isdir(dir_figs): continue
        for fig in sorted(os.listdir(dir_figs)):
            origen = os.path.join(dir_figs, fig)
            if not os.path.isdir(origen) or fig not in usadas: continue
            pdf = os.path.join(origen, fig + ".pdf")
            tex = os.path.join(origen, fig + ".tex")
            if not (os.path.exists(pdf) and os.path.exists(tex)): continue

            destino = os.path.join(raiz_fig, "cap%02d" % num, "sec" + sec, fig)
            os.makedirs(destino, exist_ok=True)
            for a in sorted(os.listdir(origen)):
                # los .synctex llevan sufijos variables —.gz, (busy)— mientras
                # el repo de origen compila, así que se descartan por nombre
                if a.endswith(BASURA) or ".synctex" in a: continue
                if os.path.isdir(os.path.join(origen, a)): continue
                shutil.copy2(os.path.join(origen, a), os.path.join(destino, a))

            os.makedirs(os.path.join(raiz_mini, "cap%02d" % num), exist_ok=True)
            mini = os.path.join(raiz_mini, "cap%02d" % num, fig)
            if not os.path.exists(mini + ".png"):
                subprocess.run(["pdftoppm", "-png", "-r", "150", "-scale-to-x", "560",
                                "-scale-to-y", "-1", "-singlefile", pdf, mini], check=True)

            figuras.append({
                "id": fig,
                "seccion": "%d.%s" % (num, sec[1:]) if sec.startswith(str(num)) else sec,
                "leyenda": leyendas.get(fig, ""),
                "mini": "asys/miniaturas/cap%02d/%s.png" % (num, fig),
                "pdf":  "asys/figuras/cap%02d/sec%s/%s/%s.pdf" % (num, sec, fig, fig),
                "tex":  "asys/figuras/cap%02d/sec%s/%s/%s.tex" % (num, sec, fig, fig),
            })

    if figuras:
        catalogo.append({"num": num, "titulo": titulo, "figuras": figuras})
        print("cap%02d  %-52s %3d figuras" % (num, titulo[:52], len(figuras)))

total = sum(len(c["figuras"]) for c in catalogo)
print("total:", total)
json.dump(catalogo, open(os.path.join(DEST, "asys", "catalogo.json"), "w"),
          ensure_ascii=False, indent=1)

# ------------------------------------------------------------------ página
def e(t): return html.escape(t, quote=True)

nav = "\n".join(
  '    <a href="#cap%02d"><span class="n">%d</span> %s <span class="c">%d</span></a>'
  % (c["num"], c["num"], e(c["titulo"]), len(c["figuras"])) for c in catalogo)

cuerpo = []
for c in catalogo:
    tarjetas = []
    for f in c["figuras"]:
        ley = ('<p class="leyenda">%s</p>' % e(f["leyenda"])) if f["leyenda"] else \
              '<p class="leyenda sin">Sin leyenda en el texto.</p>'
        tarjetas.append(f"""      <figure class="tarjeta">
        <a class="lienzo" href="{f['pdf']}" title="Abrir el PDF vectorial">
          <img src="{f['mini']}" alt="{e(f['id'])}" loading="lazy" decoding="async">
        </a>
        <figcaption>
          <p class="id">{e(f['id'])}<span class="sec">§{e(f['seccion'])}</span></p>
          {ley}
          <p class="enlaces"><a href="{f['pdf']}">PDF</a><a href="{REPO}/{f['tex']}">fuente TikZ</a></p>
        </figcaption>
      </figure>""")
    cuerpo.append(f"""  <section id="cap{c['num']:02d}">
    <h2><span class="num">Capítulo {c['num']}</span> {e(c['titulo'])}</h2>
    <p class="conteo">{len(c['figuras'])} figuras</p>
    <div class="rejilla">
{chr(10).join(tarjetas)}
    </div>
  </section>""")

PAGINA = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Catálogo de figuras — Análisis de Señales y Sistemas</title>
<meta name="description" content="Figuras del libro de Análisis de Señales y Sistemas, cada una con su fuente TikZ y su salida vectorial.">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
<style>
:root{{
  --fondo:#fbfaf7; --panel:#ffffff; --borde:#e2ded4; --borde-fuerte:#cfc9ba;
  --texto:#26231e; --tenue:#6a6459; --acento:#7a4a1e; --acento-suave:#f4ece1;
  --lienzo:#ffffff; --radio:10px;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    --fondo:#16150f; --panel:#1e1c16; --borde:#33302a; --borde-fuerte:#4a463d;
    --texto:#e9e5db; --tenue:#a09a8c; --acento:#e0a366; --acento-suave:#2a251c;
    --lienzo:#f7f5f0;
  }}
}}
:root[data-theme="dark"]{{
  --fondo:#16150f; --panel:#1e1c16; --borde:#33302a; --borde-fuerte:#4a463d;
  --texto:#e9e5db; --tenue:#a09a8c; --acento:#e0a366; --acento-suave:#2a251c;
  --lienzo:#f7f5f0;
}}
*{{box-sizing:border-box}}
body{{margin:0; background:var(--fondo); color:var(--texto);
  font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  font-size:16px; line-height:1.55; -webkit-font-smoothing:antialiased}}
.envoltura{{max-width:1180px; margin:0 auto; padding:0 22px 90px}}
a{{color:var(--acento); text-decoration:none}}
a:hover{{text-decoration:underline}}
.sans{{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}}

header{{padding:56px 0 28px}}
.migas{{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:12px; letter-spacing:.11em; text-transform:uppercase; color:var(--acento);
  font-weight:600; margin:0 0 14px}}
h1{{font-size:clamp(27px,4vw,37px); margin:0 0 16px; font-weight:600; letter-spacing:-.01em}}
.bajada{{font-size:17.5px; color:var(--tenue); margin:0; max-width:64ch}}

nav{{margin:34px 0 8px; padding:20px 0 4px; border-top:1px solid var(--borde);
  border-bottom:1px solid var(--borde); display:flex; flex-wrap:wrap; gap:8px}}
nav a{{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:13px; padding:6px 12px; border:1px solid var(--borde); border-radius:999px;
  background:var(--panel); color:var(--texto); margin-bottom:16px; display:inline-flex;
  align-items:baseline; gap:7px}}
nav a:hover{{border-color:var(--acento); text-decoration:none}}
nav .n{{font-weight:700; color:var(--acento)}}
nav .c{{color:var(--tenue); font-size:12px}}

section{{padding-top:46px; scroll-margin-top:14px}}
h2{{font-size:22px; font-weight:600; margin:0 0 2px; letter-spacing:-.01em}}
h2 .num{{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:12px; letter-spacing:.1em; text-transform:uppercase; color:var(--acento);
  font-weight:700; display:block; margin-bottom:6px}}
.conteo{{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:13px; color:var(--tenue); margin:0 0 20px}}

.rejilla{{display:grid; gap:20px; grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}}
.tarjeta{{margin:0; background:var(--panel); border:1px solid var(--borde);
  border-radius:var(--radio); overflow:hidden; display:flex; flex-direction:column}}
.lienzo{{display:block; background:var(--lienzo); padding:14px; border-bottom:1px solid var(--borde)}}
.lienzo img{{display:block; width:100%; height:auto}}
figcaption{{padding:13px 16px 15px; display:flex; flex-direction:column; gap:7px; flex:1}}
.id{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12.5px;
  color:var(--texto); margin:0; display:flex; justify-content:space-between; gap:10px;
  align-items:baseline; word-break:break-all}}
.id .sec{{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  color:var(--tenue); font-size:12px; white-space:nowrap}}
.leyenda{{margin:0; font-size:14.5px; line-height:1.5; color:var(--texto)}}
.leyenda.sin{{color:var(--tenue); font-style:italic}}
.enlaces{{margin:4px 0 0; display:flex; gap:8px; flex-wrap:wrap}}
.enlaces a{{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:12.5px; font-weight:600; padding:3px 10px; border-radius:999px;
  border:1px solid var(--borde-fuerte); background:var(--acento-suave)}}
.enlaces a:hover{{border-color:var(--acento); text-decoration:none}}

footer{{margin-top:64px; padding-top:26px; border-top:1px solid var(--borde);
  font-size:14.5px; color:var(--tenue)}}
footer p{{margin:0 0 10px; max-width:70ch}}
.katex{{font-size:1em}}
</style>
</head>
<body>
<div class="envoltura">

<header>
  <p class="migas"><a href="index.html">Material de respaldo</a> · ECEFI 2026</p>
  <h1>Catálogo de figuras</h1>
  <p class="bajada">{total} figuras del libro de <strong>Análisis de Señales y
  Sistemas</strong>, al 7 de septiembre de 2026. Ninguna es una imagen insertada desde otra
  aplicación: cada una es un programa TikZ que se compila, de modo que cambiar un parámetro y
  recompilar la regenera. La miniatura abre el PDF vectorial; al lado está el código que lo
  produce.</p>
</header>

<nav class="sans">
{nav}
</nav>

{chr(10).join(cuerpo)}

<footer>
  <p>El libro sigue en redacción y el catálogo se rearma con él, de modo que lo que se ve acá
  corresponde a la fecha indicada. El resto del material de muestra está en
  <a href="index.html">la página principal</a>.</p>
  <p>Javier Ignacio Velez · Departamento de Ingeniería en Tecnologías Electrónicas ·
  Universidad Tecnológica Nacional, Facultad Regional Mendoza ·
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es">CC BY-NC-SA 4.0</a></p>
  <p>Las visitas de esta página se cuentan con <a href="https://www.goatcounter.com/">GoatCounter</a>, sin cookies ni rastreo entre sitios.</p>
</footer>

</div>
<script data-goatcounter="https://javovelez.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
<script>
  // Los PDF, los cuadernos y las animaciones los sirve GitHub Pages sin pasar por
  // esta página, así que no generan una visita: se cuentan al hacer clic. El mismo
  // bloque está en la otra página; si se toca acá, tocarlo allá.
  document.addEventListener("click", function (e) {{
    var a = e.target && e.target.closest ? e.target.closest("a[href]") : null;
    if (!a) return;
    var h = a.getAttribute("href");
    if (!h || /^(https?:|mailto:|#)/i.test(h)) return;
    if (!/\.(pdf|ipynb)$/i.test(h) && h.indexOf("asys/animaciones/") !== 0) return;
    if (window.goatcounter && window.goatcounter.count) {{
      window.goatcounter.count({{path: h, title: a.textContent.trim(), event: true}});
    }}
  }});
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {{
    if (window.renderMathInElement) {{
      renderMathInElement(document.body, {{
        delimiters: [{{left: "$", right: "$", display: false}}],
        throwOnError: false
      }});
    }}
  }});
</script>
</body>
</html>
"""

open(os.path.join(DEST, "catalogo.html"), "w", encoding="utf-8").write(PAGINA)
print("catalogo.html ->", total, "figuras en", len(catalogo), "capítulos")
