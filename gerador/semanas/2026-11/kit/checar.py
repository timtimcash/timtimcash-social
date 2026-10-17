# -*- coding: utf-8 -*-
"""Conferências antes de mandar para aprovação.

python3 checar.py textos <arquivos...>        travessão, meia-risca, "app", "gratuito" fora da frase, superlativos, IA
python3 checar.py reel <reel.html> [capa.html] zona segura do Reel em vários instantes e da capa da grade
python3 checar.py tudo                         textos de dados/*.py e equipes/*/*.py, e todos os Reels de saida/*/

Zona segura (gerador/MARCA.md): nada importante acima de 270 px nem abaixo de 1600 px; nada encostado na borda
direita (x > 1000) na metade de baixo. Capa da grade: texto entre 285 e 1635 px (recortes 4:5 e 3:4).
"""
import os, re, sys, glob, asyncio

AQUI = os.path.dirname(os.path.abspath(__file__))
NOVDEZ = os.path.dirname(AQUI)

PROIBIDOS = [
    ("—", "travessão"), ("–", "meia-risca"),
    (r"\bapp\b", "app (é site)"), (r"\baplicativo\b", "aplicativo (é site)"), (r"\bbaix(e|ar) o\b", "baixar (é site)"),
    (r"\bo melhor\b|\ba melhor\b|\bmais completo\b|\bo único\b|\bnúmero 1\b|\blíder\b", "superlativo"),
    (r"intelig[eê]ncia artificial|\bIA\b", "inteligência artificial"),
    (r"\bgr[aá]tis\b", "grátis (use: Gratuito para o controle financeiro)"),
]


def textos(arquivos):
    problemas = 0
    for arq in arquivos:
        txt = open(arq, encoding="utf-8").read()
        for padrao, nome in PROIBIDOS:
            for m in re.finditer(padrao, txt, flags=re.I if padrao.startswith("\\b") or "intelig" in padrao else 0):
                linha = txt.count("\n", 0, m.start()) + 1
                print(f"PROBLEMA {nome}: {os.path.basename(arq)}:{linha}: …{txt[max(0, m.start() - 40):m.end() + 40]!r}…")
                problemas += 1
        for m in re.finditer(r"[Gg]ratuit[oa]", txt):
            trecho = txt[m.start():m.start() + 40]
            if not re.match(r"[Gg]ratuit[oa] para o controle financeiro", trecho):
                linha = txt.count("\n", 0, m.start()) + 1
                print(f"PROBLEMA gratuito fora da frase: {os.path.basename(arq)}:{linha}: {trecho!r}")
                problemas += 1
    print("textos conferidos:", len(arquivos), "· problemas:", problemas)
    return problemas


MEDIR_REEL = r"""() => {
  const out = [];
  const opac = e => { let o = 1; while (e && e.nodeType === 1) { const s = getComputedStyle(e); o *= parseFloat(s.opacity);
      if (s.visibility === 'hidden' || s.display === 'none') return 0; e = e.parentElement; } return o; };
  for (const e of document.querySelectorAll('body *')) {
    const proprio = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
    const svgTxt = e.tagName.toLowerCase() === 'text';
    if (!proprio && !svgTxt) continue;
    const r = e.getBoundingClientRect();
    if (r.width < 2 || r.height < 2 || r.bottom < 0 || r.top > 1920 || r.right < 0 || r.left > 1080) continue;
    const o = opac(e); if (o < 0.3) continue;
    const ruim = [];
    if (r.top < 270) ruim.push('topo ' + Math.round(r.top));
    if (r.bottom > 1600) ruim.push('base ' + Math.round(r.bottom));
    if (r.right > 1000 && r.top > 960) ruim.push('borda direita ' + Math.round(r.right));
    if (r.left < 0 || r.right > 1080) ruim.push('fora da largura');
    if (ruim.length) out.push([ruim.join(', '), (proprio || e.textContent).trim().slice(0, 50)]);
  }
  return out;
}"""

MEDIR_CAPA = r"""() => {
  const out = [];
  for (const e of document.querySelectorAll('body *')) {
    const proprio = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
    if (!proprio && e.tagName.toLowerCase() !== 'text') continue;
    const r = e.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    if (r.top < 285 || r.bottom > 1635) out.push([Math.round(r.top), Math.round(r.bottom), (proprio || e.textContent).trim().slice(0, 50)]);
  }
  return out;
}"""


async def _reel(html, capa=None, tempos=None, dur=None):
    from playwright.async_api import async_playwright
    html = os.path.abspath(html); capa = os.path.abspath(capa) if capa else None
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--font-render-hinting=none"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto("file://" + html); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(500)
        if tempos is None:
            dur = dur or 24
            tempos = [round(x * 0.25, 2) for x in range(int(dur * 4) + 1)]
        achados = {}
        for t in tempos:
            await pg.evaluate(f"render({t})")
            for motivo, texto in await pg.evaluate(MEDIR_REEL):
                achados.setdefault((motivo.split(' ')[0], texto), []).append(t)
        res_capa = []
        if capa:
            await pg.goto("file://" + capa); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
            res_capa = await pg.evaluate(MEDIR_CAPA)
        await b.close()
        return achados, res_capa


def reel(html, capa=None, dur=None):
    achados, res_capa = asyncio.run(_reel(html, capa, dur=dur))
    n = 0
    for (motivo, texto), ts in sorted(achados.items(), key=lambda x: x[1][0]):
        # transições (uma cena subindo, um título saindo) passam pela borda por um instante: só conta o que fica
        # 0,5 s ou mais (3 amostras seguidas de 0,25 s)
        maior, atual = 1, 1
        for a, b in zip(ts, ts[1:]):
            atual = atual + 1 if abs(b - a - 0.25) < 0.01 else 1
            maior = max(maior, atual)
        if maior < 3:
            continue
        print(f"PROBLEMA zona segura ({motivo}) em {ts[0]:.2f} a {ts[-1]:.2f} s: {texto!r}")
        n += 1
    for topo, base, texto in res_capa:
        print(f"PROBLEMA capa fora da faixa 285 a 1635 px ({topo} a {base}): {texto!r}")
        n += 1
    print(os.path.basename(os.path.dirname(html)), "· zona segura:", "ok" if not n else f"{n} problemas")
    return n


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    if modo == "textos":
        sys.exit(1 if textos(sys.argv[2:]) else 0)
    if modo == "reel":
        sys.exit(1 if reel(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None) else 0)
    arqs = sorted(glob.glob(os.path.join(NOVDEZ, "dados", "*.py")) + glob.glob(os.path.join(NOVDEZ, "equipes", "*", "*.py")))
    n = textos(arqs)
    for h in sorted(glob.glob(os.path.join(NOVDEZ, "equipes", "*", "trabalho", "*", "reel.html"))):
        c = os.path.join(os.path.dirname(h), "capa.html")
        n += reel(h, c if os.path.isfile(c) else None)
    sys.exit(1 if n else 0)
