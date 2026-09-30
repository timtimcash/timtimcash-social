# -*- coding: utf-8 -*-
"""Confere o layout dos slides gerados pelo render.py (HTML em /tmp/tt_html): cabeçalho e rodapé sem
esmagar, corpo sem estourar, folga entre o conteúdo e o rodapé, nada saindo da largura do slide.
Confere também travessão e meia-risca no posts.py e nos arquivos de dados.

python3 checar.py
"""
import glob, os, re, sys
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
O = os.path.dirname(AQUI)
PASTAS = ["2026-10-15_reserva-em-meses", "2026-10-19_cartao-fechamento-e-vencimento", "2026-10-26_parcela-que-cabe-hoje"]

MEDIR = """() => {
  const q = s => document.querySelector(s);
  const head = q('.head'), foot = q('.foot'), body = q('.body');
  const hb = head.getBoundingClientRect(), fb = foot.getBoundingClientRect(), bb = body.getBoundingClientRect();
  let topo = 1e9, fundo = -1e9, dir = -1e9, esq = 1e9;
  for (const el of body.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    // a imagem de um recorte fica dentro de uma caixa com overflow:hidden: mede-se a caixa, não a imagem
    if (el.tagName === 'IMG' && getComputedStyle(el.parentElement).overflow === 'hidden') continue;
    topo = Math.min(topo, r.top); fundo = Math.max(fundo, r.bottom);
    dir = Math.max(dir, r.right); esq = Math.min(esq, r.left);
  }
  return {head: hb.height, foot: fb.height, sobra: body.scrollHeight - body.clientHeight,
          folga_topo: Math.round(topo - hb.bottom), folga_base: Math.round(fb.top - fundo),
          dir: Math.round(dir), esq: Math.round(esq)};
}"""

def main():
    problemas = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for pasta in PASTAS:
            for hp in sorted(glob.glob(f"/tmp/tt_html/{pasta}_*.html")):
                pg.goto("file://" + hp); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(120)
                m = pg.evaluate(MEDIR)
                ruim = (m["head"] < 63.5 or m["foot"] < 39.5 or m["sobra"] > 0 or m["folga_topo"] < 40
                        or m["folga_base"] < 40 or m["dir"] > 1080 - 60 or m["esq"] < 60)
                problemas += ruim
                print(("PROBLEMA " if ruim else "ok       ") + os.path.basename(hp), m)
        b.close()
    for arq in [os.path.join(AQUI, "posts.py")] + glob.glob(os.path.join(O, "dados", "2026-10-1[59]_*.py")) + glob.glob(os.path.join(O, "dados", "2026-10-26_*.py")):
        txt = open(arq, encoding="utf-8").read()
        for ch, nome in (("\u2014", "travessão"), ("\u2013", "meia-risca")):
            if ch in txt:
                problemas += 1
                print("PROBLEMA", nome, "em", arq)
    print("problemas:", problemas)
    return problemas

if __name__ == "__main__":
    sys.exit(1 if main() else 0)
