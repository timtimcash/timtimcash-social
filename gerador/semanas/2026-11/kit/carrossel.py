# -*- coding: utf-8 -*-
"""Peças comuns dos carrosséis de novembro e dezembro de 2026 (1080 × 1350, 4:5), no formato aprovado em outubro
(gerador/semanas/2026-10-05_v2.py e as equipes carrosseis-a e carrosseis-b).

Uso num gerador de posts (posts.py da equipe):
    import sys; sys.path.insert(0, "<novdez>/kit"); from carrossel import *
    def post_x():
        T = 6
        s = [capa("tinta", corpo_da_capa, 1, T)]
        s.append(slide("light", EXTRA + "...", 2, T))
        ...
        s.append(fechamento_verde("Título.", "Apoio.", T, T))
        return [sem_quebra(h) for h in s]
    POSTS = {"2026-11-05_ptax": post_x}
    if __name__ == "__main__": renderizar(POSTS)      # grava <novdez>/saida/<pasta>/01.jpg ... e confere o layout

Fundos da capa: "papel" (light), "tinta" (dark, logotipo de fundo escuro), "suave" (verde suave), "verde" (green, negativo).
Slides internos: papel. Último slide: fechamento verde com "Link na bio".
"""
import os, re, io, sys, glob
sys.path.insert(0, "/home/claude/timtimcash-social/gerador")
from artes import *          # cores, logo_horizontal, page, slide, footer, ARROW, v_cta_pill...

NOVDEZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(NOVDEZ, "saida")
TELAS_REPO = "/home/claude/timtimcash-social/gerador/telas"

CORAL_TXT = "#B4532F"     # coral escuro: texto pequeno em coral (4,8:1 sobre o papel)
CORAL_FORTE = "#9A3F22"   # números grandes de despesa
CORAL_CLARO = "#EBAA90"
DARK_TEXTO = "#C9D1C8"    # apoio sobre a tinta

EXTRA = f"""<style>
.nota{{margin-top:18px;font-size:24px;font-weight:500;color:{MUTED}}}
.sombra{{box-shadow:0 1px 2px rgba(15,20,16,.05),0 22px 48px -22px rgba(15,20,16,.30)}}
.rot{{font-size:28px;font-weight:600;color:{MUTED}}}
.big{{font-weight:700;letter-spacing:-.04em;font-variant-numeric:tabular-nums;color:{INK}}}
.fio{{height:2px;background:{FIO}}}
</style>"""

EXTRA_CAPA = f"""<style>
.dark{{background:{INK};color:#fff}}
.dark .count,.dark .foot{{color:{DARK_TEXTO}}}
.dark .eyebrow{{color:{MENTA}}}
.dark .big{{color:#fff}}
.soft{{background:{SOFT};color:{INK}}}
.soft .count,.soft .foot{{color:{BRAND_DEEP}}}
.soft .eyebrow{{color:{BRAND_DEEP}}}
.green .big{{color:#fff}}
</style>"""

TEMA = {"papel": ("light", "color"), "tinta": ("dark", "dark"), "suave": ("soft", "color"), "verde": ("green", "white")}

NOTA_TELA = "<div class='nota' style='text-align:center'>Tela real do timtimcash, com dados de exemplo.</div>"


def capa(fundo, corpo, idx, total):
    """Capa no fundo do calendário: só sobretítulo, título curto e um visual forte (sem parágrafo)."""
    tema, logo_var = TEMA[fundo]
    head = f"<div class='head'><div class='brand'>{logo_horizontal(logo_var, 44)}</div><div class='count'>{idx}/{total}</div></div>"
    return page(EXTRA + EXTRA_CAPA + head + f"<div class='body'>{corpo}</div>" + footer(), tema)


def fechamento_verde(titulo, lead, idx, total):
    return slide("green", EXTRA + f"""
<div class='h2'>{titulo}</div>
<div class='lead'>{lead}</div>{v_cta_pill()}""", idx, total)


def recorte(caminho, y0, y1, largura=760, x0=0, x1=None, raio=24):
    """Recorte real de uma tela (caminho absoluto): a faixa [y0, y1) da imagem original, na largura dada."""
    from PIL import Image
    w = Image.open(caminho).size[0]
    x1 = x1 or w
    esc = largura / (x1 - x0)
    alt = (y1 - y0) * esc
    return f"""<div class='sombra' style='width:{largura}px;height:{alt:.0f}px;overflow:hidden;border-radius:{raio}px;background:#fff;border:1px solid {FIO};margin:0 auto'>
  <img src="file://{caminho}" style='display:block;width:{w * esc:.1f}px;height:auto;margin-top:{-y0 * esc:.1f}px;margin-left:{-x0 * esc:.1f}px'></div>"""


def svg_icone(caminhos, tam=42, cor=BRAND_DARK, traco=2):
    return f"<svg width='{tam}' height='{tam}' viewBox='0 0 24 24' fill='none' stroke='{cor}' stroke-width='{traco}' stroke-linecap='round' stroke-linejoin='round'>{caminhos}</svg>"


def azulejo(caminhos, tam=84, icone=42):
    return f"<div class='azulejo' style='width:{tam}px;height:{tam}px;flex:none'>{svg_icone(caminhos, icone)}</div>"


# ícones de traço (24 × 24), pontas redondas
I_CAL = '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'
I_CLOCK = '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>'
I_ALERT = '<path d="M12 4 21 19.5H3z"/><path d="M12 10v4.2M12 17.2v.1"/>'
I_QUEDA = '<path d="M3 7l6 6 4-4 8 8"/><path d="M21 12v5h-5"/>'
I_ALTA = '<path d="M3 17l6-6 4 4 8-8"/><path d="M21 12V7h-5"/>'
I_EYE = '<path d="M2.5 12C4 8.5 7.5 6 12 6s8 2.5 9.5 6c-1.5 3.5-5 6-9.5 6s-8-2.5-9.5-6z"/><circle cx="12" cy="12" r="2.8"/>'
I_CHECK = '<path d="M5 12.5l4.2 4.2L19 7"/>'
I_X = '<path d="M6 6l12 12M18 6L6 18"/>'
I_BUSCA = '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>'
I_GLOBO = '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 3.6 5.4 3.6 8.5s-1.1 5.9-3.6 8.5c-2.5-2.6-3.6-5.4-3.6-8.5S9.5 6.1 12 3.5z"/>'
I_SETAS = '<path d="M7 7h11l-3-3M17 17H6l3 3"/>'
I_RECIBO = '<path d="M6 3.5h12v17l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/>'
I_CARTAO = '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M3 10h18M7 15h4"/>'
I_CASA = '<path d="M4 11l8-6.5 8 6.5"/><path d="M6 9.5V20h12V9.5"/>'
I_ESCUDO = '<path d="M12 3.5l7 3v5c0 4.5-3 8-7 9.5-4-1.5-7-5-7-9.5v-5z"/><path d="M9 12l2 2 4-4"/>'
I_SACOLA = '<path d="M6 8h12l-1 12.5H7z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/>'
I_PRESENTE = '<rect x="4" y="9" width="16" height="11.5" rx="1.5"/><path d="M3 9h18v3.5H3zM12 9v11.5M12 9c-1.5-3.5-5-4-5.5-2S9 9 12 9zM12 9c1.5-3.5 5-4 5.5-2S15 9 12 9z"/>'
I_GRAFICO = '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'
I_RELOGIO_AREIA = '<path d="M7 3.5h10M7 20.5h10M8 3.5c0 4 8 5 8 8.5s-8 4.5-8 8.5M16 3.5c0 4-8 5-8 8.5s8 4.5 8 8.5"/>'


def brl(v, cent=True):
    s = f"{v:,.2f}" if cent else f"{v:,.0f}"
    return ("−" if v < 0 else "") + "R$ " + s.replace("-", "").replace(",", "X").replace(".", ",").replace("X", ".")


def num(v, casas=2):
    s = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" if v < 0 else "") + s


def pct(v, casas=1):
    return num(v, casas) + "%"


def sem_quebra(html):
    """Não separa "R$" do número, nem o número da unidade, no fim de uma linha."""
    html = html.replace("R$ ", "R$\u00a0").replace("US$ ", "US$\u00a0").replace("\u20ac ", "\u20ac\u00a0")
    html = re.sub(r"(\d) (meses|mês|dias|dia|anos|ano|vezes|parcelas|pedidos|categorias)\b", "\\1\u00a0\\2", html)
    html = re.sub(r"\b(dia|dias) (\d)", "\\1\u00a0\\2", html)
    html = re.sub(r"(\d)x de", "\\1x\u00a0de", html)
    return html


# ---------------------------------------------------------------- renderizar e conferir
MEDIR = """() => {
  const q = s => document.querySelector(s);
  const head = q('.head'), foot = q('.foot'), body = q('.body');
  const hb = head.getBoundingClientRect(), fb = foot.getBoundingClientRect();
  let topo = 1e9, fundo = -1e9, dir = -1e9, esq = 1e9;
  for (const el of body.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    if (el.tagName === 'IMG' && getComputedStyle(el.parentElement).overflow === 'hidden') continue;
    topo = Math.min(topo, r.top); fundo = Math.max(fundo, r.bottom);
    dir = Math.max(dir, r.right); esq = Math.min(esq, r.left);
  }
  return {head: Math.round(hb.height), foot: Math.round(fb.height), sobra: body.scrollHeight - body.clientHeight,
          folga_topo: Math.round(topo - hb.bottom), folga_base: Math.round(fb.top - fundo),
          dir: Math.round(dir), esq: Math.round(esq)};
}"""


def renderizar(posts, saida=SAIDA, so=None):
    """Grava cada slide em <saida>/<pasta>/NN.jpg (JPEG 92) e confere o layout. so: lista de pastas (opcional)."""
    from PIL import Image
    from playwright.sync_api import sync_playwright
    html_dir = os.path.join(saida, "_html"); os.makedirs(html_dir, exist_ok=True)
    problemas = 0
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for nome, fn in posts.items():
            if so and nome not in so:
                continue
            destino = os.path.join(saida, nome); os.makedirs(destino, exist_ok=True)
            for velho in glob.glob(os.path.join(destino, "[0-9][0-9].jpg")):
                os.remove(velho)
            for i, html in enumerate(fn(), 1):
                hp = os.path.join(html_dir, f"{nome}_{i:02d}.html")
                open(hp, "w", encoding="utf-8").write(html)
                pg.goto("file://" + hp); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(200)
                m = pg.evaluate(MEDIR)
                ruim = (m["head"] < 63 or m["foot"] < 39 or m["sobra"] > 0 or m["folga_topo"] < 36
                        or m["folga_base"] < 36 or m["dir"] > 1080 - 60 or m["esq"] < 60)
                problemas += ruim
                png = pg.screenshot()
                Image.open(io.BytesIO(png)).convert("RGB").save(os.path.join(destino, f"{i:02d}.jpg"), "JPEG",
                                                                 quality=92, optimize=True, subsampling=0)
                print(("PROBLEMA " if ruim else "ok       ") + f"{nome} {i:02d}", m)
        b.close()
    print("problemas de layout:", problemas)
    return problemas
