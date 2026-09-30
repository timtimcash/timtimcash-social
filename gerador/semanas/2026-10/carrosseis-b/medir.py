# -*- coding: utf-8 -*-
"""Mede o respiro de cada slide já renderizado (HTML em /tmp/tt_html): altura útil do corpo, altura do conteúdo,
sobra em cima e embaixo, e elementos que passam da largura do pai ou quebram linha sem querer.
python3 medir.py <prefixo da pasta> [<prefixo> ...]"""
import glob, os, sys
from playwright.sync_api import sync_playwright

JS = """() => {
  const b = document.querySelector('.body');
  const kids = [...b.children].filter(e => e.getBoundingClientRect().height > 0);
  const rb = b.getBoundingClientRect();
  let top = Infinity, bot = -Infinity;
  for (const k of kids) { const r = k.getBoundingClientRect(); top = Math.min(top, r.top); bot = Math.max(bot, r.bottom); }
  // descendentes que saem da caixa do slide (1080) ou da área útil lateral (92..988)
  const fora = [];
  for (const e of b.querySelectorAll('*')) {
    const r = e.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    if (r.right > 988.5 || r.left < 91.5) fora.push((e.className || e.tagName) + ' ' + Math.round(r.left) + '..' + Math.round(r.right) + ' ' + (e.textContent || '').trim().slice(0, 30));
  }
  // textos com overflow horizontal (scrollWidth > clientWidth)
  const estouro = [];
  for (const e of b.querySelectorAll('*')) {
    if (e.children.length === 0 && e.scrollWidth > e.clientWidth + 1 && getComputedStyle(e).overflow !== 'visible') estouro.push((e.textContent||'').trim().slice(0,30));
  }
  // linhas de cada bloco de texto grande
  const linhas = [];
  for (const e of b.querySelectorAll('.h1,.h2,.h3,.p,.lead,.nota')) {
    const lh = parseFloat(getComputedStyle(e).lineHeight);
    linhas.push(e.className.split(' ')[0] + ':' + Math.round(e.getBoundingClientRect().height / lh));
  }
  return {util: Math.round(rb.height), conteudo: Math.round(bot - top), cima: Math.round(top - rb.top), baixo: Math.round(rb.bottom - bot), fora: fora.slice(0, 6), estouro: estouro.slice(0,4), linhas: linhas.join(' ')};
}"""

def main(prefixos):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for pre in prefixos:
            for hp in sorted(glob.glob(f"/tmp/tt_html/{pre}*.html")):
                pg.goto("file://" + hp); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(120)
                r = pg.evaluate(JS)
                print(os.path.basename(hp)[:-5], "| util", r["util"], "conteudo", r["conteudo"], "cima", r["cima"], "baixo", r["baixo"], "|", r["linhas"])
                if r["fora"]: print("   FORA:", r["fora"])
                if r["estouro"]: print("   ESTOURO:", r["estouro"])
        b.close()

if __name__ == "__main__":
    main(sys.argv[1:])
