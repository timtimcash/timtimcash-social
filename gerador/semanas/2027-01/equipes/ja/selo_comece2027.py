# -*- coding: utf-8 -*-
"""Série "Comece 2027" (janeiro de 2027): o selo do passo e o sobretítulo, iguais em todos os posts da série.

O selo é um quadrado arredondado na tinta (#0F1410) com o número do passo grande em menta (#6EE7B7) e, embaixo do
número, quatro tracinhos que contam o caminho (os passos até o atual em menta, os que faltam apagados). É o mesmo
desenho em qualquer fundo: menta só aparece sobre a tinta, como manda a marca. No fundo tinta, o quadrado ganha um
tom um degrau acima (#1C241D) e um fio (#34413A), para não sumir no fundo.

Medidas (S = lado do quadrado, em px): canto 0,26 S; número 0,56 S, peso 700, espaçamento −0,04 em, algarismos
tabulares, centrado um pouco acima do meio; tracinhos de 0,12 S × 0,042 S, com 0,036 S entre eles, a 0,15 S da base.
Tamanhos de referência: 172 a 200 px na capa de carrossel, 120 a 140 px nos slides, 220 a 260 px na capa de Reel.

Sobretítulo: "COMECE 2027 · PASSO N DE 4" (700, caixa alta, +0,16 em), na cor do sobretítulo de cada fundo
(papel #047857, tinta #6EE7B7, verde suave #065F46, verde #FFFFFF). Nos kits, a classe .eyebrow já faz isso:
basta escrever sobretitulo(n) dentro dela. Para quem não usa a classe, eyebrow(n, fundo) devolve o HTML pronto.

Uso (carrossel ou Reel; o HTML só tem estilos em linha e usa a Inter que a página já carrega):
    import sys; sys.path.insert(0, "<janfev>/equipes/ja")
    from selo_comece2027 import selo, selo_com_nome, sobretitulo, eyebrow, NOMES, PERGUNTAS, DIAS
    selo(3, 180, "verde")                  # só o quadrado
    selo_com_nome(3, 180, "verde")         # o quadrado e o nome do passo embaixo ("Os limites")
    sobretitulo(3)                         # "COMECE 2027 · PASSO 3 DE 4"
    eyebrow(3, "verde", tam=30)            # <div> do sobretítulo com estilo em linha

python3 selo_comece2027.py   grava selo_comece2027.png (os 4 selos nos 4 fundos), para conferir.
"""

INK = "#0F1410"
TINTA_2 = "#1C241D"     # um degrau acima da tinta: o quadrado do selo sobre o fundo tinta
TINTA_FIO = "#34413A"   # fio do quadrado sobre o fundo tinta
MENTA = "#6EE7B7"
APAGADO = "#3A4840"     # tracinhos dos passos que faltam (cor sólida, sem transparência)
BRAND = "#059669"
BRAND_DARK = "#047857"
BRAND_DEEP = "#065F46"
SOFT = "#D1FAE5"
BG = "#FBFAF6"

NOMES = {1: "O retrato", 2: "O caminho", 3: "Os limites", 4: "A rota"}
PERGUNTAS = {1: "Quanto você tem?", 2: "Para onde vai?", 3: "Quanto cabe?", 4: "E se 2027 apertar?"}
DIAS = {1: "04/01", 2: "10/01", 3: "14/01", 4: "18/01"}      # dia do post de cada passo (2027)
TELAS = {1: "Contas e carteiras", 2: "Visão geral", 3: "Orçamentos", 4: "Simulação futura"}

COR_EYEBROW = {"papel": BRAND_DARK, "tinta": MENTA, "suave": BRAND_DEEP, "verde": "#FFFFFF"}
COR_NOME = {"papel": INK, "tinta": "#FFFFFF", "suave": INK, "verde": "#FFFFFF"}
# sem aspas no estilo em linha (o HTML dos kits usa aspas simples nos atributos); cv11 e ss01 vêm do body dos kits
FONTE = "font-family:Inter,sans-serif;font-variant-numeric:tabular-nums"


def sobretitulo(n=None):
    """Texto do sobretítulo da série. Sem número, só "COMECE 2027" (post de abertura)."""
    return "COMECE 2027" if n is None else f"COMECE 2027 · PASSO {n} DE 4"


def eyebrow(n=None, fundo="papel", tam=26, extra=""):
    return (f"<div style='{FONTE};font-size:{tam}px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;"
            f"color:{COR_EYEBROW[fundo]};{extra}'>{sobretitulo(n)}</div>")


def selo(n, tam=160, fundo="papel", extra=""):
    """Quadrado arredondado com o número do passo (1 a 4) e os quatro tracinhos do caminho."""
    assert n in (1, 2, 3, 4), n
    S = float(tam)
    fill = TINTA_2 if fundo == "tinta" else INK
    fio = f"box-shadow:inset 0 0 0 {max(2, round(S * .014))}px {TINTA_FIO};" if fundo == "tinta" else ""
    pw, ph, gap = S * .12, S * .042, S * .036
    tracos = "".join(
        f"<i style='display:block;width:{pw:.1f}px;height:{ph:.1f}px;border-radius:{ph:.1f}px;"
        f"background:{MENTA if k <= n else APAGADO}'></i>" for k in range(1, 5))
    return f"""<div style='{FONTE};position:relative;flex:none;width:{S:.0f}px;height:{S:.0f}px;border-radius:{S * .26:.1f}px;background:{fill};{fio}{extra}'>
  <div style='position:absolute;left:0;right:0;top:{S * .06:.1f}px;height:{S * .70:.1f}px;display:flex;align-items:center;justify-content:center;
    font-size:{S * .56:.1f}px;line-height:1;font-weight:700;letter-spacing:-.04em;color:{MENTA}'>{n}</div>
  <div style='position:absolute;left:0;right:0;bottom:{S * .15:.1f}px;display:flex;justify-content:center;gap:{gap:.1f}px'>{tracos}</div>
</div>"""


def selo_com_nome(n, tam=160, fundo="papel", tam_nome=None, extra=""):
    """O selo e o nome do passo embaixo, centrados."""
    tn = tam_nome or round(tam * .19)
    return f"""<div style='{FONTE};display:flex;flex-direction:column;align-items:center;gap:{tam * .13:.0f}px;{extra}'>{selo(n, tam, fundo)}
  <div style='font-size:{tn}px;font-weight:700;letter-spacing:-.02em;line-height:1.1;color:{COR_NOME[fundo]};white-space:nowrap'>{NOMES[n]}</div></div>"""


def _demo(destino):
    import os
    from playwright.sync_api import sync_playwright
    fontes = "".join(
        f"@font-face{{font-family:'Inter';font-weight:{w};src:url('file:///tmp/inter/extras/ttf/Inter-{f}.ttf')}}"
        for w, f in [(400, "Regular"), (500, "Medium"), (600, "SemiBold"), (700, "Bold")])
    fundos = [("papel", BG), ("tinta", INK), ("suave", SOFT), ("verde", BRAND)]
    linhas = "".join(
        f"<div style='background:{cor};padding:44px 56px;display:flex;flex-direction:column;gap:30px'>"
        f"{eyebrow(3 if f in ('verde', 'suave') else 1, f, 26)}"
        f"<div style='display:flex;gap:48px;align-items:flex-start'>{''.join(selo_com_nome(k, 150, f) for k in range(1, 5))}</div></div>"
        for f, cor in fundos)
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{fontes}*{{margin:0;padding:0;box-sizing:border-box}}"
            f"body{{font-family:'Inter';-webkit-font-smoothing:antialiased;font-feature-settings:'cv11','ss01';width:960px}}"
            f"</style></head><body>{linhas}</body></html>")
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 960, "height": 400})
        pg.set_content(html); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.screenshot(path=destino, full_page=True)
        b.close()
    print(destino)


if __name__ == "__main__":
    import os
    _demo(os.path.join(os.path.dirname(os.path.abspath(__file__)), "selo_comece2027.png"))
