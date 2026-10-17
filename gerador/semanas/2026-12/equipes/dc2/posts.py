# -*- coding: utf-8 -*-
"""Carrosséis da equipe dc2 (dezembro de 2026): 16/12, 18/12, 21/12, 23/12 e 28/12.

Peças do kit (N/kit/carrossel.py), no formato aprovado em outubro e novembro. Telas reais capturadas por captura.py
(conta fictícia de N/base_app, build 2026-10-16.1), guardadas em N/saida/<pasta>/telas/; as caixas (px CSS) dos
recortes ficam em caixas.json. Toda conta dos slides é conferida por assert neste arquivo, contra as telas e os fatos.

python3 posts.py [pasta ...]      grava N/saida/<pasta>/01.jpg ... e confere o layout
"""
import json, math, os, sys
from decimal import Decimal as D, ROUND_HALF_UP

N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, N + "/kit")
from carrossel import *          # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl...)

AQUI = os.path.dirname(os.path.abspath(__file__))
CX = json.loads(open(os.path.join(AQUI, "caixas.json"), encoding="utf-8").read().replace(" ", " "))

P16 = "2026-12-16_sua-inflacao-nao-e-a-do-ipca"
P18 = "2026-12-18_patrimonio-quanto-voce-tem"
P21 = "2026-12-21_metas-de-2027-que-da-para-medir"
P23 = "2026-12-23_viagem-para-fora-o-iof"
P28 = "2026-12-28_anote-quanto-ha-la-fora"


def tela(pasta, nome):
    return os.path.join(SAIDA, pasta, "telas", nome)


def px(v):
    """px CSS das capturas (escala 3) para px da imagem."""
    return int(round(v * 3))


def q2(v):
    return D(v).quantize(D("0.01"), rounding=ROUND_HALF_UP)


def q1(v):
    return D(v).quantize(D("0.1"), rounding=ROUND_HALF_UP)


def pct1(parte, todo):
    """porcentagem com uma casa, como o site (toFixed(1))."""
    return (D(parte) / D(todo) * 100).quantize(D("0.1"), rounding=ROUND_HALF_UP)


def reais(v, casas=2):
    return brl(float(v), casas > 0)


def numbr(v, casas=2):
    return num(float(v), casas)


def pc(v, casas=1):
    """"21,5%" a partir de Decimal."""
    return numbr(v, casas) + "%"


MENOS = "−"
CINZA_CLARO = "#E6E3DA"
CINZA_MEDIO = "#D4D2C8"
CINZA_ESCURO = "#B9B5A8"
VERMELHO_SUAVE = "#FBEAEA"
AMBAR_SUAVE = "#FBF1DC"
CORAL_PALIDO = "#F6D9CD"
TINTA_2 = "#1C241D"       # um degrau acima da tinta (azulejos sobre o fundo escuro)
TINTA_FIO = "#2E382F"

# ícones de traço extras (24 x 24)
I_LIVRO = '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v14.5H6.5A2.5 2.5 0 0 0 4 20z"/><path d="M4 20a2.5 2.5 0 0 0 2.5 2H20v-4.5"/>'
I_BANCO = '<path d="M12 3.5 20.5 8h-17z"/><path d="M5 11v6.5M9.7 11v6.5M14.3 11v6.5M19 11v6.5"/><path d="M3.5 20.5h17"/>'
I_CARRO = '<path d="M5 16.5V12l1.8-4.6A2 2 0 0 1 8.7 6h6.6a2 2 0 0 1 1.9 1.4L19 12v4.5"/><path d="M3.5 12h17v4.5h-17z"/><circle cx="7.5" cy="17.5" r="1.6"/><circle cx="16.5" cy="17.5" r="1.6"/>'
I_CESTA = '<path d="M3.5 9.5h17l-1.6 9.2a2 2 0 0 1-2 1.8H7.1a2 2 0 0 1-2-1.8z"/><path d="M8 9.5 11 4M16 9.5 13 4M9 13.5v3.5M15 13.5v3.5M12 13.5v3.5"/>'
I_SAUDE = '<path d="M12 20s-7.5-4.4-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.6-7.5 10-7.5 10z"/><path d="M12 10.5v5M9.5 13h5"/>'
I_ALVO = '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.6"/>'
I_COFRE = '<rect x="3.5" y="5" width="17" height="14" rx="2.5"/><circle cx="12" cy="12" r="3.2"/><path d="M12 8.8v1M12 14.2v1M8.8 12h1M14.2 12h1M6.5 19v1.5M17.5 19v1.5"/>'
I_SETA_DIR = '<path d="M5 12h14M13 6l6 6-6 6"/>'
I_NOTAS = '<rect x="2.5" y="6.5" width="19" height="11" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5M18 9.5v5"/>'
I_PREPAGO = '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M3 10h18"/><path d="M15.5 15h2.5"/><path d="M6.5 15h.01M9 15h.01"/>'
I_SAQUE = '<rect x="3.5" y="3.5" width="17" height="11" rx="2"/><path d="M7 8h10"/><path d="M8.5 14.5v6h7v-6"/><path d="M12 16.5v2"/>'
I_TRANSF = '<path d="M4 8h13l-3.5-3.5"/><path d="M20 16H7l3.5 3.5"/>'
I_AVIAO = '<path d="M21 4 3 11l7 2.5L12.5 21z"/><path d="M10 13.5 21 4"/>'
I_LUPA = '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>'
I_CARTEIRA = '<path d="M4 7.5A2.5 2.5 0 0 1 6.5 5H18v3"/><rect x="3.5" y="8" width="17" height="11.5" rx="2.5"/><path d="M16 13.75h.01"/>'
I_LAPIS = '<path d="M4 20l1-4.5L16 4.5l3.5 3.5L8.5 19z"/><path d="M14 7l3 3"/>'


def item(ip, titulo, sub, ultimo=False, tam_t=36, tam_s=28):
    """Linha com ícone em azulejo, título e apoio (desenho dos modelos de outubro)."""
    return f"""<div style='display:flex;gap:28px;align-items:center;padding:26px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  {azulejo(ip)}
  <div><div style='font-size:{tam_t}px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{titulo}</div>
  <div style='font-size:{tam_s}px;color:{MUTED};margin-top:8px;line-height:1.32;text-wrap:balance'>{sub}</div></div></div>"""


def nota(txt, centro=False, extra=""):
    estilo = f" style='{'text-align:center;' if centro else ''}{extra}'"
    return f"<div class='nota'{estilo}>{txt}</div>"


def fonte(txt):
    """Linha de fonte no pé do visual, com o rótulo em negrito."""
    return f"<div class='nota'><b style='font-weight:700;color:{INK}'>Fonte:</b> {txt}</div>"


def leg(cor, txt, borda=None, tam=26):
    b = f"border:2px solid {borda};box-sizing:border-box;" if borda else ""
    return (f"<span style='display:inline-flex;align-items:center;gap:12px;font-size:{tam}px;font-weight:600;color:{INK}'>"
            f"<i style='width:24px;height:24px;border-radius:7px;background:{cor};{b}display:block;flex:none'></i>{txt}</span>")


# ================================================================ 16/12 · Sua inflação não é a do IPCA
# IBGE, IPCA de setembro de 2026 (divulgado em 09/10/2026): peso mensal de cada grupo (SIDRA, quadro do IPCA Brasil,
# https://sidra.ibge.gov.br/home/ipca/brasil) e variação acumulada em 12 meses (Indicadores IBGE, IPCA setembro de 2026,
# tabela "Variações acumuladas em 12 meses por grupos e itens", p. 15).
IPCA = {   # grupo: (peso mensal em %, variação em 12 meses em %)
    "Alimentação e bebidas": (D("21.5090"), D("4.66")),
    "Habitação": (D("15.2611"), D("4.22")),
    "Artigos de residência": (D("3.4843"), D("2.08")),
    "Vestuário": (D("4.6171"), D("3.34")),
    "Transportes": (D("20.1607"), D("3.94")),
    "Saúde e cuidados pessoais": (D("13.8408"), D("5.75")),
    "Despesas pessoais": (D("10.4075"), D("5.90")),
    "Educação": (D("6.2085"), D("5.95")),
    "Comunicação": (D("4.5111"), D("2.79")),
}
IPCA_12M = D("4.58")
IPCA_SET = D("0.82")
assert abs(sum(p for p, _ in IPCA.values()) - 100) < D("0.001")
PESO = {k: q1(p) for k, (p, _) in IPCA.items()}
assert sum(PESO.values()) == D("100.0")
assert [PESO[k] for k in ("Alimentação e bebidas", "Transportes", "Habitação", "Saúde e cuidados pessoais", "Educação")] == \
    [D("21.5"), D("20.2"), D("15.3"), D("13.8"), D("6.2")]

# a conta do exemplo: despesas de novembro de 2026 (Relatórios > Despesas por categoria, relógio em 16/12/2026)
NOV = {"Casa": D("2501.80"), "Mercado": D("1844.90"), "Educação": D("1450.00"), "Transporte": D("1210.00"),
       "Bares e restaurantes": D("928.60"), "Compras": D("659.00"), "Lazer e hobbies": D("308.00"), "Saúde": D("127.30"),
       "Assinaturas e serviços": D("119.80")}
NOV_TOTAL = sum(NOV.values())
assert NOV_TOTAL == D("9149.40")
_l16 = {l[0]: l[1] for l in CX["16"]["linhas"]}
for k, v in NOV.items():
    assert _l16[k] == f"{k} | {reais(v)} | {pc(pct1(v, NOV_TOTAL))}", (k, _l16[k])
assert "9 categorias · Total R$ 9.149,40" in CX["16"]["texto"]
# os grupos do IPCA mais próximos de cada categoria do exemplo
SUA = {"Alimentação e bebidas": NOV["Mercado"] + NOV["Bares e restaurantes"], "Habitação": NOV["Casa"],
       "Transportes": NOV["Transporte"], "Educação": NOV["Educação"], "Saúde e cuidados pessoais": NOV["Saúde"]}
SUA_OUTROS = NOV["Compras"] + NOV["Lazer e hobbies"] + NOV["Assinaturas e serviços"]
assert sum(SUA.values()) + SUA_OUTROS == NOV_TOTAL
PSUA = {k: pct1(v, NOV_TOTAL) for k, v in SUA.items()}
assert PSUA == {"Alimentação e bebidas": D("30.3"), "Habitação": D("27.3"), "Transportes": D("13.2"), "Educação": D("15.8"),
                "Saúde e cuidados pessoais": D("1.4")}, PSUA
assert pct1(SUA_OUTROS, NOV_TOTAL) == D("11.9")
VEZES_EDU = (SUA["Educação"] / NOV_TOTAL * 100) / IPCA["Educação"][0]
assert D("2.5") < VEZES_EDU < D("2.6")                    # "duas vezes e meia"
CURTO = {"Alimentação e bebidas": "Alimentação", "Habitação": "Habitação", "Transportes": "Transportes", "Educação": "Educação",
         "Saúde e cuidados pessoais": "Saúde", "Despesas pessoais": "Despesas pessoais", "Vestuário": "Vestuário",
         "Comunicação": "Comunicação", "Artigos de residência": "Artigos de residência"}


def sankey_cestas(W=896, H=590, col=172, gap=7):
    """Duas colunas empilhadas (a cesta do IPCA e a do exemplo) e as faixas que ligam cada grupo; Educação em coral."""
    ordem = ["Alimentação e bebidas", "Habitação", "Transportes", "Saúde e cuidados pessoais", "outros", "Educação"]
    nomes = {"Alimentação e bebidas": "Alimentação", "Habitação": "Habitação", "Transportes": "Transportes",
             "Saúde e cuidados pessoais": "Saúde", "outros": "outros", "Educação": "Educação"}
    esq = {k: IPCA[k][0] for k in ordem if k != "outros"}
    esq["outros"] = 100 - sum(esq.values())
    dir_ = {k: SUA[k] / NOV_TOTAL * 100 for k in ordem if k != "outros"}
    dir_["outros"] = SUA_OUTROS / NOV_TOTAL * 100
    util = H - gap * (len(ordem) - 1)
    tons = {"Alimentação e bebidas": INK, "Habitação": "#2C352D", "Transportes": INK, "Saúde e cuidados pessoais": "#2C352D", "outros": "#4A534B"}
    faixa = "#E8E4DA"
    def pos(m):
        y, out = 0.0, {}
        for k in ordem:
            h = float(m[k]) / 100 * util
            out[k] = (y, h); y += h + gap
        return out
    pe, pd = pos(esq), pos(dir_)
    xa, xb = col, W - col
    fonte_ = "font-family='Inter' style='font-feature-settings:\"tnum\",\"cv11\",\"ss01\"'"
    el = []
    for k in ordem:
        (y0, h0), (y1, h1) = pe[k], pd[k]
        cor = CORAL_PALIDO if k == "Educação" else faixa
        c1, c2 = xa + (xb - xa) * .42, xa + (xb - xa) * .58
        el.append(f"<path d='M{xa} {y0:.1f} C{c1:.1f} {y0:.1f} {c2:.1f} {y1:.1f} {xb} {y1:.1f} L{xb} {y1 + h1:.1f} "
                  f"C{c2:.1f} {y1 + h1:.1f} {c1:.1f} {y0 + h0:.1f} {xa} {y0 + h0:.1f} Z' fill='{cor}'/>")
        if k != "Educação":
            ym = (y0 + h0 / 2 + y1 + h1 / 2) / 2
            el.append(f"<text x='{W / 2}' y='{ym + 9:.1f}' text-anchor='middle' {fonte_} font-weight='600' font-size='25' fill='{MUTED}'>{nomes[k]}</text>")
    for k in ordem:
        for x, (y, h) in ((0, pe[k]), (xb, pd[k])):
            cor = CORAL if k == "Educação" else tons[k]
            el.append(f"<rect x='{x}' y='{y:.1f}' width='{col}' height='{h:.1f}' rx='9' fill='{cor}'/>")
    # os números de cada coluna, dentro dos blocos que têm altura para isso
    for k in ordem:
        if k in ("outros", "Educação"):
            continue
        for x, (y, h), v in ((0, pe[k], PESO[k]), (xb, pd[k], PSUA[k])):
            if h >= 40:
                el.append(f"<text x='{x + col / 2}' y='{y + h / 2 + 10:.1f}' text-anchor='middle' {fonte_} font-weight='700' font-size='28' letter-spacing='-.5' fill='#FFFFFF'>{pc(v)}</text>")
    ye, he = pe["Educação"]; yd, hd = pd["Educação"]
    el.append(f"<text x='{col / 2}' y='{ye + he / 2 + 10:.1f}' text-anchor='middle' {fonte_} font-weight='700' font-size='29' letter-spacing='-.5' fill='#FFFFFF'>6,2%</text>")
    el.append(f"<text x='{xb + col / 2}' y='{yd + hd / 2 + 17:.1f}' text-anchor='middle' {fonte_} font-weight='700' font-size='50' letter-spacing='-2' fill='#FFFFFF'>15,8%</text>")
    ym = (ye + he / 2 + yd + hd / 2) / 2
    el.append(f"<text x='{W / 2}' y='{ym + 11:.1f}' text-anchor='middle' {fonte_} font-weight='700' font-size='31' letter-spacing='-.5' fill='{CORAL_FORTE}'>Educação</text>")
    return (f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='display:block;overflow:visible'>{''.join(el)}</svg>")


def capa_inflacao(T):
    rot = f"font-size:27px;font-weight:700;letter-spacing:.12em;text-transform:uppercase"
    corpo = f"""<div class='eyebrow'>Inflação</div>
<div class='h1' style='font-size:104px'>Sua inflação não é a do IPCA</div>
<div style='margin-top:58px'>
  <div style='display:flex;justify-content:space-between;margin-bottom:18px'>
    <span style='{rot};color:{MUTED}'>a cesta do IPCA</span><span style='{rot};color:{CORAL_TXT}'>a sua cesta</span></div>
  {sankey_cestas()}
</div>"""
    return capa("papel", corpo, 1, T)


def post_inflacao():
    T = 7
    s = [capa_inflacao(T)]

    # 2 · a cesta do IPCA, como um cupom
    ordem = sorted(PESO, key=lambda k: -PESO[k])
    linhas = []
    for i, k in enumerate(ordem):
        w = float(PESO[k]) / 21.5 * 230
        linhas.append(f"""<div style='display:flex;align-items:center;gap:18px;height:50px;{'' if i == len(ordem) - 1 else f'border-bottom:2px dashed {FIO};'}'>
  <span style='flex:1;font-size:29px;font-weight:600;letter-spacing:-.015em;color:{INK}'>{CURTO[k]}</span>
  <span style='width:230px;display:flex;justify-content:flex-end'><i style='display:block;width:{w:.1f}px;height:14px;border-radius:7px;background:{CINZA_ESCURO if k != "Educação" else CORAL}'></i></span>
  <span class='big' style='width:112px;text-align:right;font-size:31px'>{pc(PESO[k])}</span></div>""")
    zig = "".join(f"<i style='display:block;width:28px;height:28px;background:#fff;transform:rotate(45deg);margin:-14px 0 0 0;flex:none'></i>" for _ in range(28))
    cupom = f"""<div class='visual' style='margin-top:44px;display:flex;justify-content:center'>
<div style='width:800px;filter:drop-shadow(0 18px 26px rgba(15,20,16,.13)) drop-shadow(0 1px 1px rgba(15,20,16,.06))'>
  <div style='background:#fff;border-radius:22px 22px 0 0;padding:30px 44px 8px'>
    <div style='display:flex;justify-content:space-between;align-items:baseline;padding-bottom:18px;border-bottom:3px solid {INK}'>
      <span style='font-size:28px;font-weight:700;letter-spacing:.14em;color:{INK}'>CESTA DO IPCA</span>
      <span style='font-size:25px;font-weight:600;color:{MUTED}'>peso de cada grupo · set/26</span></div>
    {''.join(linhas)}
    <div style='display:flex;justify-content:space-between;align-items:baseline;padding:14px 0 10px;border-top:3px solid {INK}'>
      <span style='font-size:28px;font-weight:700;letter-spacing:.14em'>TOTAL</span><span class='big' style='font-size:34px'>100%</span></div>
  </div>
  <div style='height:16px;overflow:hidden;display:flex;justify-content:center;gap:0'><div style='display:flex;margin-top:2px'>{zig}</div></div>
</div></div>
<div class='nota' style='text-align:center'>Famílias com renda de 1 a 40 salários mínimos; pesos da POF 2017-2018. Fonte: IBGE.</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O que é o IPCA</div>
<div class='h2'>A inflação oficial é uma cesta média.</div>{cupom}""", 2, T))

    # 3 · em 12 meses, cada grupo subiu de um jeito (pontos sobre uma régua, com a linha do índice)
    ordem = sorted(IPCA, key=lambda k: -IPCA[k][1])
    assert ordem[0] == "Educação" and ordem[-1] == "Artigos de residência"
    W, x0, x1 = 896, 292, 736          # régua de 1,5% a 6,5%; os valores ficam numa coluna à direita
    vmin, vmax = 1.5, 6.5
    X = lambda v: x0 + (float(v) - vmin) / (vmax - vmin) * (x1 - x0)
    rows = []
    alt = 61
    for i, k in enumerate(ordem):
        v = IPCA[k][1]
        acima = v > IPCA_12M
        forte = k == "Educação"
        cor = CORAL_FORTE if forte else (CORAL if acima else CINZA_ESCURO)
        tam = 34 if forte else 24
        y = i * alt + alt / 2
        if i:
            rows.append(f"<div style='position:absolute;left:0;right:0;top:{i * alt:.1f}px;border-top:2px solid {FIO}'></div>")
        rows.append(f"<div style='position:absolute;left:0;top:{y - 18:.1f}px;width:{x0 - 24}px;font-size:28px;font-weight:{700 if forte else 600};"
                    f"letter-spacing:-.015em;color:{CORAL_FORTE if forte else INK};white-space:nowrap'>{CURTO[k]}</div>")
        rows.append(f"<div style='position:absolute;left:{x0}px;top:{y - 1.5:.1f}px;width:{X(v) - x0:.1f}px;height:3px;border-radius:2px;background:{cor}'></div>")
        rows.append(f"<i style='position:absolute;left:{X(v):.1f}px;top:{y:.1f}px;width:{tam}px;height:{tam}px;border-radius:50%;background:{cor};"
                    f"transform:translate(-50%,-50%);display:block;{'box-shadow:0 0 0 8px ' + CORAL_PALIDO + ';' if forte else ''}'></i>")
        rows.append(f"<div class='big' style='position:absolute;right:0;top:{y - (23 if forte else 19):.1f}px;"
                    f"font-size:{38 if forte else 30}px;color:{CORAL_FORTE if (acima or forte) else MUTED}'>{pc(v, 2)}</div>")
    H = len(ordem) * alt
    xi = X(IPCA_12M)
    linha_ipca = (f"<div style='position:absolute;left:{xi:.1f}px;top:-30px;height:{H + 30}px;border-left:3px dashed {INK}'></div>"
                  f"<div style='position:absolute;left:{xi:.1f}px;top:-74px;transform:translateX(-50%);background:{INK};color:#fff;font-size:24px;"
                  f"font-weight:700;padding:6px 16px;border-radius:999px;white-space:nowrap;font-variant-numeric:tabular-nums'>IPCA 4,58%</div>")
    grafico = f"<div style='position:relative;width:{W}px;height:{H}px;margin-top:92px'>{linha_ipca}{''.join(rows)}</div>"
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em 12 meses</div>
<div class='h2'>Cada grupo subiu de um jeito.</div>
<div class='visual' style='margin-top:40px'>{grafico}
{nota('Variação acumulada em 12 meses até setembro de 2026. Fonte: IBGE.', extra='margin-top:26px')}</div>""", 3, T))

    # 4 · a sua cesta tem outros pesos (barras em par: IPCA e o exemplo)
    grupos = ["Alimentação e bebidas", "Habitação", "Educação", "Transportes", "Saúde e cuidados pessoais"]
    larg = 470
    def par(k):
        a, b = PESO[k], PSUA[k]
        forte = k == "Educação"
        wa, wb = float(a) / 30.3 * larg, float(b) / 30.3 * larg
        return f"""<div style='display:flex;align-items:center;gap:22px;padding:15px 0;{'' if k == grupos[-1] else f'border-bottom:2px solid {FIO};'}'>
  <div style='width:250px;flex:none;font-size:31px;font-weight:{700 if forte else 600};letter-spacing:-.02em;color:{CORAL_FORTE if forte else INK}'>{CURTO[k]}</div>
  <div style='flex:1'>
    <div style='display:flex;align-items:center;gap:14px'><i style='display:block;width:{wa:.1f}px;height:24px;border-radius:6px;background:{CINZA_ESCURO}'></i>
      <span class='big' style='font-size:26px;color:{MUTED}'>{pc(a)}</span></div>
    <div style='display:flex;align-items:center;gap:14px;margin-top:8px'><i style='display:block;width:{wb:.1f}px;height:24px;border-radius:6px;background:{CORAL_FORTE if forte else CORAL}'></i>
      <span class='big' style='font-size:{32 if forte else 28}px;color:{CORAL_FORTE if forte else INK}'>{pc(b)}</span></div>
  </div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No exemplo</div>
<div class='h2'>A sua cesta tem outros pesos.</div>
<div class='visual' style='margin-top:40px'><div class='card' style='padding:26px 44px 22px'>
  <div style='display:flex;gap:34px;padding-bottom:14px'>{leg(CINZA_ESCURO, 'IPCA, setembro de 2026')}{leg(CORAL, 'exemplo, novembro de 2026')}</div>
  {''.join(par(k) for k in grupos)}
</div>{nota('Em % do gasto. No exemplo (novembro de 2026), Alimentação soma mercado e bares e restaurantes; Habitação, aluguel e luz.')}</div>""", 4, T))

    # 5 · leia assim: Educação pesa 2,5 vezes mais na cesta do exemplo
    citacao = f"""<div style='margin-top:30px;display:flex;gap:26px;align-items:flex-start;padding:32px 38px;border-radius:24px;background:{SOFT}'>
  <div class='big' style='font-size:96px;line-height:.7;color:{BRAND_DARK};margin-top:14px'>“</div>
  <div><div style='font-size:34px;font-weight:600;letter-spacing:-.02em;line-height:1.3;color:{INK}'>O seu índice pessoal de inflação pode ser maior ou menor do que o IPCA.</div>
    <div style='font-size:25px;font-weight:700;color:{BRAND_DEEP};margin-top:12px'>IBGE, “Inflação”, na série IBGE Explica</div></div></div>"""
    bloco = f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:34px 44px 36px'>
  <div style='display:flex;align-items:flex-end;gap:26px'>
    <div style='flex:1'><div class='rot' style='font-size:25px'>Educação no IPCA</div><div class='big' style='font-size:76px;line-height:1;margin-top:8px;color:{MUTED}'>6,2%</div></div>
    <div style='padding-bottom:16px'>{svg_icone(I_SETA_DIR, 46, CINZA_ESCURO, 2.4)}</div>
    <div style='flex:1'><div class='rot' style='font-size:25px'>no exemplo</div><div class='big' style='font-size:76px;line-height:1;margin-top:8px;color:{CORAL_FORTE}'>15,8%</div></div>
    <div style='padding:14px 24px;border-radius:20px;background:{VERMELHO_SUAVE};text-align:center'>
      <div class='big' style='font-size:64px;line-height:1;color:{CORAL_FORTE}'>2,5×</div>
      <div style='font-size:23px;font-weight:700;color:{CORAL_TXT};margin-top:4px'>o peso</div></div>
  </div>
  <div class='fio' style='margin:28px 0 22px'></div>
  <div style='font-size:31px;line-height:1.38;color:{INK}'>Em 12 meses, Educação subiu <b>5,95%</b>, mais que o índice (4,58%). Nessa casa, a alta da escola pesa duas vezes e meia o que pesa no IPCA.</div>
</div>{citacao}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Leia assim</div>
<div class='h2'>Onde a sua cesta pesa mais, a alta pesa mais.</div>{bloco}""", 5, T))

    # 6 · tela real: Relatórios > Despesas por categoria, novembro de 2026 (relógio em 16/12/2026)
    c = CX["16"]
    rel = tela(P16, "celular-relatorios-novembro.png")
    xa, xb = c["painel"][0], c["painel"][2]
    larg = 560
    cab = recorte(rel, px(c["painel"][1] + 4), px(c["sub"][3] + 14), largura=larg, x0=px(xa), x1=px(xb), raio=22)
    l5 = [l for l in c["linhas"] if l[0] in ("Casa", "Mercado", "Educação", "Transporte", "Bares e restaurantes")]
    ya, yb = l5[0][3] - 2, l5[-1][5] + 2
    linhas = recorte(rel, px(ya), px(yb), largura=larg, x0=px(xa), x1=px(xb), raio=22)
    esc = larg / (xb - xa)
    mapa = {"Casa": "Habitação", "Mercado": "Alimentação", "Educação": "Educação", "Transporte": "Transportes", "Bares e restaurantes": "Alimentação"}
    tags = []
    for l in l5:
        yc = ((l[3] + l[5]) / 2 - ya) * esc
        forte = l[0] == "Educação"
        tags.append(f"<div style='position:absolute;left:0;top:{yc - 25:.1f}px;height:50px;display:flex;align-items:center;gap:12px'>"
                    f"{svg_icone(I_SETA_DIR, 30, CORAL if forte else CINZA_ESCURO, 2.4)}"
                    f"<span style='height:50px;padding:0 20px;border-radius:25px;display:flex;align-items:center;font-size:25px;font-weight:700;white-space:nowrap;"
                    f"background:{CORAL if forte else '#fff'};color:{'#fff' if forte else INK};border:2px solid {CORAL if forte else FIO}'>{mapa[l[0]]}</span></div>")
    alt_l = (yb - ya) * esc
    visual = f"""<div class='visual' style='margin-top:38px;display:flex;gap:18px;align-items:flex-start'>
  <div style='width:{larg}px;flex:none'>{cab}<div style='height:14px'></div>{linhas}</div>
  <div style='flex:1;position:relative'>
    <div style='font-size:22px;font-weight:700;letter-spacing:.12em;color:{MUTED};padding-left:42px;height:{(c["sub"][3] + 14 - c["painel"][1] - 4) * esc + 14:.0f}px;display:flex;align-items:flex-end;padding-bottom:20px;box-sizing:border-box'>GRUPO DO IPCA</div>
    <div style='position:relative;height:{alt_l:.0f}px'>{''.join(tags)}</div></div>
</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>Veja quanto cada categoria leva do seu gasto.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Em Relatórios, Despesas por categoria, no período que você escolher.</div>
{visual}{NOTA_TELA}""", 6, T))

    s.append(fechamento_verde("Conheça a sua cesta.",
                              "Relatórios no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 18/12 · Patrimônio: quanto você tem de verdade
# Contas e carteiras, relógio em 18/12/2026 (celular)
CONTAS = {"Conta corrente": D("22551.46"), "Reserva": D("22974.60"), "Corretora no exterior": D("60000.00"), "Banco na Europa": D("11525.40")}
PATRIMONIO = sum(CONTAS.values())
assert PATRIMONIO == D("117051.46")
_t18 = CX["18a"]["texto"]
assert "PATRIMÔNIO CONSOLIDADO\nR$ 117.051,46" in _t18 and "4 contas · todas no total do patrimônio" in _t18
for k, v in CONTAS.items():
    assert f"{k}\n" in _t18 and reais(v) in _t18, k
LA_FORA = CONTAS["Corretora no exterior"] + CONTAS["Banco na Europa"]
assert LA_FORA == D("71525.40")
P_CONTA, P_RESERVA, P_FORA = (pct1(CONTAS["Conta corrente"], PATRIMONIO), pct1(CONTAS["Reserva"], PATRIMONIO), pct1(LA_FORA, PATRIMONIO))
assert (P_CONTA, P_RESERVA, P_FORA) == (D("19.3"), D("19.6"), D("61.1")) and P_CONTA + P_RESERVA + P_FORA == 100
# o que deve: as parcelas do notebook (10x de R$ 360,00 desde 27/11/2026); em 18/12 a 2/10 está pendente (vence 27/12)
PARCELAS = 9
DEVE = PARCELAS * D("360.00")
LIQUIDO = PATRIMONIO - DEVE
assert DEVE == D("3240.00") and LIQUIDO == D("113811.46")
# Remessas (relógio em 18/12/2026): cada moeda na sua, com o câmbio salvo na carteira
USD_HOJE, EUR_HOJE = D("13310") * D("5.0515"), D("2012") * D("5.6592")
assert q2(USD_HOJE) == D("67235.47") and q2(EUR_HOJE) == D("11386.31")
for trecho in ["US$13.310 na carteira hoje", "R$ 67.235,47 ao câmbio de hoje (R$ 5,0515)", "+R$ 7.235,46", "+12,1% em R$", "no patrimônio · conta de destino"]:
    assert trecho in CX["18c"]["texto"], trecho
for trecho in ["€2.012 na carteira hoje", "R$ 11.386,31 ao câmbio de hoje (R$ 5,6592)", "−R$ 139,09", "−1,2% em R$"]:
    assert trecho in CX["18d"]["texto"], trecho
assert q2(EUR_HOJE) - CONTAS["Banco na Europa"] == D("-139.09")
assert "Incluir no patrimônio total\no saldo soma ao total geral de contas" in CX["18b"]["texto"] and "Corretora no exterior" in CX["18b"]["texto"]


def pilha_iso(W=896, H=640):
    """Três lajes em perspectiva isométrica (2:1), da base ao topo: lá fora, reserva e conta corrente; alturas pelo valor."""
    ox = 268
    total_h = 318
    lajes = [  # (nome, valor, meia-largura, cores topo/esquerda/direita, contorno)
        ("lá fora", LA_FORA, 128, ("#3A443B", "#1E261F", "#0F1410"), None),
        ("reserva", CONTAS["Reserva"], 112, (VERDE_LUZ, BRAND, BRAND_DARK), None),
        ("conta corrente", CONTAS["Conta corrente"], 96, ("#FFFFFF", "#EFECE4", "#DCD8CC"), "#D8D4C8"),
    ]
    base_y = H - 6 - 128        # oy: centro do losango da base
    z = 0.0
    el, rot = [], []
    for nome, v, s, (ct, ce, cd), borda in lajes:
        h = float(v / PATRIMONIO) * total_h
        z0, z1 = z, z + h
        oy = base_y
        P = lambda x, y, zz: (ox + (x - y), oy + (x + y) / 2 - zz)
        def poli(pts, cor):
            d = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
            st = f" stroke='{borda}' stroke-width='1.5' stroke-linejoin='round'" if borda else ""
            return f"<polygon points='{d}' fill='{cor}'{st}/>"
        el.append(poli([P(-s, s, z1), P(s, s, z1), P(s, s, z0), P(-s, s, z0)], ce))      # face esquerda
        el.append(poli([P(s, -s, z1), P(s, s, z1), P(s, s, z0), P(s, -s, z0)], cd))      # face direita
        el.append(poli([P(-s, -s, z1), P(s, -s, z1), P(s, s, z1), P(-s, s, z1)], ct))   # topo
        # rótulo à direita, na meia altura da face direita
        xr, yr = P(s, -s, (z0 + z1) / 2)
        rot.append((nome, v, xr, yr))
        z = z1
    xl = 620
    fonte_ = "font-family='Inter' style='font-feature-settings:\"tnum\",\"cv11\",\"ss01\"'"
    # rótulos de baixo para cima, com 92 px de distância no mínimo (as lajes de cima são finas)
    ys = []
    for i, (nome, v, xr, yr) in enumerate(rot):
        y = yr if not ys else min(yr, ys[-1] - 92)
        ys.append(y)
    for (nome, v, xr, yr), y in zip(rot, ys):
        xm = xl - 46
        el.append(f"<polyline points='{xr + 12:.1f},{yr:.1f} {xm - 20:.1f},{yr:.1f} {xm:.1f},{y:.1f} {xl - 16},{y:.1f}' fill='none' stroke='{CINZA_ESCURO}' stroke-width='2.5' stroke-linejoin='round' stroke-linecap='round'/>")
        el.append(f"<circle cx='{xr + 6:.1f}' cy='{yr:.1f}' r='6.5' fill='{INK}'/>")
        el.append(f"<text x='{xl}' y='{y - 8:.1f}' {fonte_} font-weight='700' font-size='25' letter-spacing='2.5' fill='{MUTED}'>{nome.upper()}</text>")
        el.append(f"<text x='{xl}' y='{y + 32:.1f}' {fonte_} font-weight='700' font-size='38' letter-spacing='-1' fill='{INK}'>{reais(v, 0)}</text>")
    return f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='display:block;overflow:visible'>{''.join(el)}</svg>"


def capa_patrimonio(T):
    corpo = f"""<div class='eyebrow'>Patrimônio</div>
<div class='h1' style='font-size:104px'>Quanto você tem de verdade?</div>
<div style='position:relative;margin-top:40px'>
  <div style='position:absolute;left:0;top:0;z-index:2'>
    <div style='font-size:25px;font-weight:700;letter-spacing:.12em;color:{MUTED}'>TOTAL DAS CONTAS</div>
    <div class='big' style='font-size:66px;line-height:1;margin-top:8px'>R$ 117.051</div></div>
  {pilha_iso()}
</div>"""
    return capa("papel", corpo, 1, T)


def post_patrimonio():
    T = 7
    s = [capa_patrimonio(T)]

    # 2 · a conta: o que você tem menos o que deve
    larg = 760
    w_deve = float(DEVE / PATRIMONIO) * larg
    conta = f"""<div class='visual' style='margin-top:48px'><div class='card' style='padding:30px 46px 34px'>
  <div style='display:flex;align-items:center;gap:26px;padding:20px 0;border-bottom:2px solid {FIO}'>
    {azulejo(I_CARTEIRA)}
    <div style='flex:1'><div style='font-size:34px;font-weight:700;letter-spacing:-.02em'>O que você tem</div>
      <div style='font-size:26px;color:{MUTED};margin-top:4px'>as 4 contas do exemplo</div></div>
    <div class='big' style='font-size:46px'>{reais(PATRIMONIO)}</div></div>
  <div style='display:flex;align-items:center;gap:26px;padding:20px 0;border-bottom:2px solid {FIO}'>
    <div class='azulejo' style='width:84px;height:84px;flex:none;background:{VERMELHO_SUAVE}'>{svg_icone(I_RECIBO, 42, CORAL_FORTE)}</div>
    <div style='flex:1'><div style='font-size:34px;font-weight:700;letter-spacing:-.02em'>O que você deve</div>
      <div style='font-size:26px;color:{MUTED};margin-top:4px'>9 parcelas de R$ 360</div></div>
    <div class='big' style='font-size:46px;color:{CORAL_FORTE}'>{MENOS}{reais(DEVE)}</div></div>
  <div style='display:flex;align-items:baseline;justify-content:space-between;padding:26px 0 18px'>
    <div style='font-size:34px;font-weight:700;letter-spacing:-.02em'>Patrimônio líquido</div>
    <div class='big' style='font-size:66px;color:{BRAND_DARK}'>{reais(LIQUIDO)}</div></div>
  <div style='display:flex;height:34px;border-radius:12px;overflow:hidden;gap:4px'>
    <div style='flex:1;background:{BRAND}'></div><div style='width:{w_deve:.1f}px;background:{CORAL}'></div></div>
</div>{nota('Exemplo: a conta fictícia dos nossos posts em 18/12/2026; faltam 9 das 10 parcelas do notebook.')}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta</div>
<div class='h2'>Patrimônio é o que você tem menos o que deve.</div>{conta}""", 2, T))

    # 3 · ter não é poder usar amanhã (liquidez)
    partes = [("Conta corrente", CONTAS["Conta corrente"], P_CONTA, "#FFFFFF", INK, "na hora", I_BANCO),
              ("Reserva", CONTAS["Reserva"], P_RESERVA, BRAND, "#fff", "depende da aplicação", I_COFRE),
              ("Lá fora", LA_FORA, P_FORA, INK, "#fff", "depende de vender, do câmbio do dia e do prazo da volta", I_GLOBO)]
    barra = "".join(
        f"<div style='flex:{float(p)} 1 0;min-width:0;background:{cor};{'border:2px solid ' + CINZA_MEDIO + ';' if cor == '#FFFFFF' else ''}display:flex;align-items:center;justify-content:center'>"
        f"<span class='big' style='font-size:34px;color:{tc}'>{pc(p)}</span></div>"
        for _, _, p, cor, tc, _, _ in partes)
    linhas = "".join(f"""<div style='display:flex;align-items:center;gap:24px;padding:20px 0;{'' if i == 2 else f'border-bottom:2px solid {FIO};'}'>
  <i style='width:22px;height:22px;border-radius:7px;background:{cor};{'border:2px solid ' + CINZA_ESCURO + ';box-sizing:border-box;' if cor == '#FFFFFF' else ''}display:block;flex:none'></i>
  <div style='flex:1;min-width:0'><div style='display:flex;justify-content:space-between;align-items:baseline;gap:16px'>
      <span style='font-size:33px;font-weight:700;letter-spacing:-.02em'>{nome}</span><span class='big' style='font-size:36px'>{reais(v)}</span></div>
    <div style='display:flex;align-items:center;gap:10px;margin-top:6px;font-size:26px;color:{MUTED}'>{svg_icone(I_CLOCK, 26, MUTED, 2.2)}<span>{prazo}</span></div></div></div>"""
                     for i, (nome, v, p, cor, tc, prazo, ic) in enumerate(partes))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Liquidez</div>
<div class='h2'>Ter não é o mesmo que usar amanhã.</div>
<div class='p' style='margin-top:22px;font-size:36px'>Liquidez é o quanto vira dinheiro rápido. No exemplo, 61% está lá fora.</div>
<div class='visual' style='margin-top:36px'><div class='card' style='padding:30px 44px 12px'>
  <div style='display:flex;height:84px;border-radius:18px;overflow:hidden;gap:5px'>{barra}</div>
  <div style='margin-top:8px'>{linhas}</div></div></div>""", 3, T))

    # 4 · lá fora entra pelo custo; o valor de hoje fica em Remessas, em cada moeda
    def moeda(simbolo, qtd, custo, hoje, dif, dif_pct, cambio, positivo):
        cor = BRAND_DARK if positivo else CORAL_FORTE
        fundo = SOFT if positivo else VERMELHO_SUAVE
        return f"""<div class='card' style='padding:26px 38px 26px'>
  <div style='display:flex;align-items:baseline;justify-content:space-between'>
    <span class='big' style='font-size:52px'>{simbolo}&nbsp;{qtd}</span>
    <span style='font-size:25px;font-weight:600;color:{MUTED}'>câmbio salvo: R$ {cambio}</span></div>
  <div style='display:flex;align-items:stretch;gap:18px;margin-top:18px'>
    <div style='flex:1;padding:18px 22px;border-radius:18px;background:{BG};border:2px solid {FIO}'>
      <div style='font-size:24px;font-weight:700;letter-spacing:.1em;color:{MUTED}'>NO PATRIMÔNIO</div>
      <div class='big' style='font-size:40px;margin-top:6px'>{custo}</div>
      <div style='font-size:24px;color:{MUTED};margin-top:2px'>o custo das remessas</div></div>
    <div style='display:flex;align-items:center'>{svg_icone(I_SETA_DIR, 40, CINZA_ESCURO, 2.4)}</div>
    <div style='flex:1;padding:18px 22px;border-radius:18px;background:{fundo}'>
      <div style='font-size:24px;font-weight:700;letter-spacing:.1em;color:{cor}'>HOJE, EM REMESSAS</div>
      <div class='big' style='font-size:40px;margin-top:6px'>{hoje}</div>
      <div style='font-size:24px;font-weight:700;color:{cor};margin-top:2px;font-variant-numeric:tabular-nums'>{dif} · {dif_pct}</div></div>
  </div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Lá fora</div>
<div class='h2'>No patrimônio, lá&nbsp;fora entra pelo custo.</div>
<div class='p' style='margin-top:20px;font-size:36px'>O valor de hoje fica em Remessas.</div>
<div class='visual' style='margin-top:36px;display:flex;flex-direction:column;gap:22px'>
  {moeda('US$', '13.310', reais(CONTAS['Corretora no exterior']), reais(q2(USD_HOJE)), '+R$ 7.235,46', '+12,1%', '5,0515', True)}
  {moeda('€', '2.012', reais(CONTAS['Banco na Europa']), reais(q2(EUR_HOJE)), MENOS + 'R$ 139,09', MENOS + '1,2%', '5,6592', False)}
</div>""", 4, T))

    # 5 · tela real: Contas e carteiras e o interruptor da conta (relógio em 18/12/2026)
    a, b_ = CX["18a"], CX["18b"]
    cc = tela(P18, "celular-contas-e-carteiras.png")
    ed = tela(P18, "celular-editar-conta-corretora.png")
    sy = a["scrollY"]
    larg = 560
    lista = recorte(cc, px(a["total"][1] - 12 - sy), px(a["linhas"][-1][4] + 6 - sy), largura=larg, x0=px(10), x1=px(380))
    li = b_["linha_incluir"]
    chave = recorte(ed, px(li[2] - 4 - b_["scrollY"]), px(li[4] + 4 - b_["scrollY"]), largura=larg, x0=px(li[1] - 6), x1=px(li[3] + 6))
    seta = f"""<div style='display:flex;justify-content:center;align-items:center;gap:14px;margin:12px 0 10px;font-size:26px;font-weight:600;color:{MUTED}'>
  {svg_icone('<path d="M12 4v16M6 14l6 6 6-6"/>', 32, CINZA_ESCURO, 2.4)}<span>e em cada conta, você escolhe</span></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>Contas e carteiras: tudo somado.</div>
<div class='visual' style='margin-top:34px'>{lista}{seta}{chave}{NOTA_TELA}</div>""", 5, T))

    # 6 · tela real: Remessas, dólar e euro (relógio em 18/12/2026)
    usd, eur = CX["18c"], CX["18d"]
    rd, re_ = tela(P18, "celular-remessas-dolar.png"), tela(P18, "celular-remessas-euro.png")
    larg = 600
    c_usd = recorte(rd, px(usd["investido"][1] - 12), px(usd["cambio_hoje"][3] + 7), largura=larg, x0=px(17), x1=px(373))
    c_eur = recorte(re_, px(eur["investido"][1] - 12), px(eur["cambio_hoje"][3] + 5), largura=larg, x0=px(17), x1=px(373))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em Remessas</div>
<div class='h3'>O valor de hoje, em cada moeda.</div>
<div class='visual' style='margin-top:34px'>{c_usd}<div style='height:22px'></div>{c_eur}{NOTA_TELA}</div>""", 6, T))

    s.append(fechamento_verde("Saiba quanto você tem, de verdade.",
                              "Contas, carteiras e remessas no timtimcash, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 21/12 · Metas de 2027 que dá para medir
# telas reais com o relógio em 21/12/2026: Relatórios > Ajustar cálculo; Orçamentos de dezembro; Simulação > Cenário base,
# "1 ano" e "Definir uma meta" de R$ 35.000 (só na sessão do navegador)
_t21a = CX["21a"]["texto"]
for trecho in ["SUAS METAS", "Receita guardada", "20%", "Reserva de emergência", "6 meses", "Sua média\n18,1%\nda receita",
               "Reserva\n13,8m\nmeta 6m", "R$ 1.862,02 ÷ R$ 10.281,67 = 18,1%"]:
    assert trecho in _t21a, trecho
assert q1(D("1862.02") / D("10281.67") * 100) == D("18.1")
_m21 = CX["21b"]["itens"][0]
assert _m21[0] == "Mercado | R$ 1.307 de R$ 2.000 | 65% | no ritmo, fecha em | R$ 1.930 | NO LIMITE", _m21
assert "21 de 31 dias · 68% do período" in CX["21b"]["texto"]
_t21c = CX["21c"]["texto"]
for trecho in ["Cenário base", "Novembro de 2027", "Saldo em nov/27\nR$35.540", "+R$ 1.780 por mês · 12 me"]:
    assert trecho in _t21c, trecho
META_SALDO = "R$ 35 mil"
META_MES = "nov/27"
METAS = [("20%", "da receita guardada", "Guardar mais", "Guardar 20% da receita", "Relatórios › Diagnóstico"),
         ("6 meses", "de reserva", "Ter uma reserva", "Reserva de 6 meses de gastos", "Relatórios › Diagnóstico"),
         ("R$ 2.000", "no mercado", "Gastar menos no mercado", "Mercado até R$ 2.000 por mês", "Orçamentos"),
         ("R$ 35 mil", "de saldo", "Juntar dinheiro", "R$ 35 mil até novembro de 2027", "Simulação futura")]


def alvo(W=896, H=680):
    cx, cy = 448, 356
    raios = [318, 238, 158, 78]
    cores = ["#FFFFFF", SOFT, BRAND, INK]
    fonte_ = "font-family='Inter' style='font-feature-settings:\"tnum\",\"cv11\",\"ss01\"'"
    el = []
    for r, cor in zip(raios, cores):
        borda = f" stroke='{CINZA_MEDIO}' stroke-width='3'" if cor == "#FFFFFF" else ""
        el.append(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{cor}'{borda}/>")
    # número no alto de cada anel e o rótulo embaixo, no mesmo anel
    aneis = [(METAS[3], 278, INK, MUTED), (METAS[2], 198, BRAND_DEEP, BRAND_DEEP), (METAS[1], 118, "#FFFFFF", "#FFFFFF")]
    for (num_, rot, *_), r, cor_n, cor_r in aneis:
        el.append(f"<text x='{cx}' y='{cy - r + 13}' text-anchor='middle' {fonte_} font-weight='700' font-size='38' letter-spacing='-1.2' fill='{cor_n}'>{num_}</text>")
        el.append(f"<text x='{cx}' y='{cy + r + 9}' text-anchor='middle' {fonte_} font-weight='700' font-size='25' letter-spacing='.5' fill='{cor_r}'>{rot}</text>")
    el.append(f"<text x='{cx}' y='{cy + 12}' text-anchor='middle' {fonte_} font-weight='700' font-size='58' letter-spacing='-2' fill='#FFFFFF'>20%</text>")
    el.append(f"<text x='{cx}' y='{cy + 44}' text-anchor='middle' {fonte_} font-weight='700' font-size='19' letter-spacing='.5' fill='{MENTA}'>guardar</text>")
    # a flecha cravada: haste em tinta, penas em coral, vinda do alto à direita
    x0, y0, x1, y1 = cx + 322, cy - 322, cx + 64, cy - 64
    el.append(f"<line x1='{x0}' y1='{y0}' x2='{x1}' y2='{y1}' stroke='{INK}' stroke-width='10' stroke-linecap='round'/>")
    ux, uy = (x1 - x0) / math.hypot(x1 - x0, y1 - y0), (y1 - y0) / math.hypot(x1 - x0, y1 - y0)
    nx, ny = -uy, ux
    for t in (6, 30, 54):
        px_, py_ = x0 + ux * t, y0 + uy * t
        for sinal in (1, -1):
            ex, ey = px_ - ux * 24 + nx * 24 * sinal, py_ - uy * 24 + ny * 24 * sinal
            el.append(f"<line x1='{px_:.1f}' y1='{py_:.1f}' x2='{ex:.1f}' y2='{ey:.1f}' stroke='{CORAL}' stroke-width='8' stroke-linecap='round'/>")
    el.append(f"<circle cx='{x1}' cy='{y1}' r='9' fill='{INK}'/>")
    return f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='display:block;overflow:visible'>{''.join(el)}</svg>"


def capa_metas(T):
    corpo = f"""<div class='eyebrow'>Planejamento</div>
<div class='h1' style='font-size:100px'>Metas de 2027 que dá para medir</div>
<div style='display:flex;justify-content:center;margin-top:30px'>{alvo()}</div>"""
    return capa("papel", corpo, 1, T)


def post_metas():
    T = 7
    s = [capa_metas(T)]

    # 2 · meta boa tem número e prazo: do vago ao medível
    def linha(i, vago, medivel, onde, ultimo=False):
        return f"""<div style='display:flex;align-items:center;gap:24px;padding:17px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div style='width:54px;height:54px;border-radius:50%;background:{SOFT};color:{BRAND_DEEP};display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;flex:none'>{i}</div>
  <div style='flex:1;min-width:0'>
    <div style='font-size:26px;font-weight:500;color:{MUTED};text-decoration:line-through;text-decoration-color:{CORAL};text-decoration-thickness:3px'>{vago}</div>
    <div style='font-size:34px;font-weight:700;letter-spacing:-.025em;color:{INK};margin-top:2px'>{medivel}</div>
    <div style='display:inline-flex;align-items:center;gap:8px;margin-top:8px;padding:4px 14px;border-radius:999px;background:{BG};border:2px solid {FIO};font-size:22px;font-weight:600;color:{BRAND_DEEP}'>{svg_icone(I_ALVO, 22, BRAND_DARK, 2.2)}{onde}</div>
  </div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A regra</div>
<div class='h2'>Meta boa tem número e prazo.</div>
<div class='visual' style='margin-top:40px'><div class='card' style='padding:4px 42px'>
  {''.join(linha(i + 1, m[2], m[3], m[4], i == 3) for i, m in enumerate(METAS))}
</div>{nota('Exemplos da conta fictícia dos nossos posts.')}</div>""", 2, T))

    # 3 · metas 1 e 2: Relatórios > Ajustar cálculo (relógio em 21/12/2026)
    c = CX["21a"]
    aj = tela(P21, "celular-ajustar-calculo.png")
    sy = c["scrollY"]
    rec = recorte(aj, px(c["metas"][1] - 16 - sy), px(c["previa_caixa"][4] + 8 - sy), largura=520, x0=px(10), x1=px(380))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Metas 1 e 2 · em Relatórios</div>
<div class='h3'>Quanto guardar e quantos meses de reserva.</div>
<div class='visual' style='margin-top:30px;display:flex;gap:26px;align-items:center'>
  <div style='width:520px;flex:none'>{rec}</div>
  <div style='flex:1'>
    <div style='font-size:24px;font-weight:700;letter-spacing:.1em;color:{MUTED}'>NO EXEMPLO</div>
    <div class='big' style='font-size:60px;line-height:1;margin-top:10px;color:{CORAL_FORTE}'>18,1%</div>
    <div style='font-size:26px;line-height:1.3;color:{INK};margin-top:6px'>guardados, na média de 12 meses. A meta é 20%.</div>
    <div class='fio' style='margin:24px 0'></div>
    <div class='big' style='font-size:60px;line-height:1;color:{BRAND_DARK}'>13,8</div>
    <div style='font-size:26px;line-height:1.3;color:{INK};margin-top:6px'>meses de reserva. A meta é&nbsp;6.</div>
  </div></div>
{NOTA_TELA}""", 3, T))

    # 4 · meta 3: Orçamentos de dezembro (relógio em 21/12/2026)
    c = CX["21b"]
    orc = tela(P21, "celular-orcamentos-dezembro.png")
    m = c["itens"][0]
    rec = recorte(orc, px(c["progresso"][1] - 16), px(m[4] + 6), largura=660, x0=px(14), x1=px(376))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Meta 3 · em Orçamentos</div>
<div class='h3'>Um limite por categoria.</div>
<div class='p' style='margin-top:16px;font-size:34px'>No dia 21, o mercado do exemplo está em R$ 1.307. No ritmo, fecha dezembro em R$ 1.930, dentro dos R$ 2.000.</div>
<div class='visual' style='margin-top:34px'>{rec}{NOTA_TELA}</div>""", 4, T))

    # 5 · meta 4: Simulação futura, Definir uma meta (relógio em 21/12/2026; a meta fica só na sessão)
    c = CX["21c"]
    sim = tela(P21, "celular-simulacao-meta.png")
    painel = c["cadeia"][3]
    rec = recorte(sim, px(painel[3] + 2), px(c["grafico"][3] + 8), largura=560, x0=px(painel[2] + 2), x1=px(painel[4] - 2))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Meta 4 · na Simulação futura</div>
<div class='h3'>Um saldo e o mês em que ele chega.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Em Definir uma meta, o cenário mostra quando chega lá.</div>
<div class='visual' style='margin-top:34px'>{rec}{NOTA_TELA}</div>""", 5, T))

    # 6 · salve este post: as suas 4 metas, para preencher
    branco = lambda w: f"<span style='display:inline-block;width:{w}px;border-bottom:3px dotted {CINZA_ESCURO};height:34px;vertical-align:-8px;margin:0 6px'></span>"
    folha = [("Guardar " + branco(92) + "% da receita", "Relatórios › Diagnóstico"),
             ("Reserva de " + branco(92) + " meses de gastos", "Relatórios › Diagnóstico"),
             (branco(190) + " até R$ " + branco(120) + " por mês", "Orçamentos"),
             ("R$ " + branco(150) + " até " + branco(110) + "/2027", "Simulação futura")]
    linhas = "".join(f"""<div style='display:flex;gap:24px;align-items:flex-start;padding:26px 0;{'' if i == 3 else f'border-bottom:2px solid {FIO};'}'>
  <div style='width:50px;height:50px;border-radius:50%;background:{BRAND};color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700;flex:none'>{i + 1}</div>
  <div><div style='font-size:36px;font-weight:600;letter-spacing:-.02em;color:{INK};line-height:1.25'>{t}</div>
    <div style='font-size:24px;font-weight:600;color:{BRAND_DEEP};margin-top:10px'>mede em: {onde}</div></div></div>""" for i, (t, onde) in enumerate(folha))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Salve este post</div>
<div class='h2'>As suas 4 metas de 2027.</div>
<div class='visual' style='margin-top:42px'><div class='card' style='padding:4px 44px;background:#fff'>{linhas}</div></div>""", 6, T))

    s.append(fechamento_verde("Meça as suas metas de 2027.",
                              "Relatórios, Orçamentos e Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 23/12 · Viagem: o IOF é igual. O câmbio, não.
# Decreto 6.306/2007, art. 15-B, com a redação do Decreto 12.499/2025 (FATOS.md e o texto compilado do Planalto, lido em 16/10/2026):
# 3,5% no cartão no exterior (VII), no saque (IX), no pré-pago e nos cheques de viagem (X), na moeda em espécie (XX) e na remessa
# para disponibilidade própria (XXI); 1,10% só na remessa para investimento (XXI-A).
IOF_VIAGEM, IOF_INVEST = D("0.035"), D("0.011")
GASTO_USD, CAMBIO_EX = D("1000"), D("5.05")
EM_REAIS_V = GASTO_USD * CAMBIO_EX
IOF_V = q2(EM_REAIS_V * IOF_VIAGEM)
TOTAL_V = EM_REAIS_V + IOF_V
assert EM_REAIS_V == D("5050.00") and IOF_V == D("176.75") and TOTAL_V == D("5226.75")
CAMBIOS = [D("5.05"), D("5.15"), D("5.25")]
TOTAIS = [q2(GASTO_USD * c * (1 + IOF_VIAGEM)) for c in CAMBIOS]
assert TOTAIS == [D("5226.75"), D("5330.25"), D("5433.75")]
A_MAIS = [t - TOTAIS[0] for t in TOTAIS]
assert A_MAIS == [D("0"), D("103.50"), D("207.00")]
# tela real (relógio em 23/12/2026): Orçamentos > Definir limites > busca "Viagem" > R$ 5.300,00, sem salvar
LIMITE_VIAGEM = D("5300.00")
assert CX["23"]["campo_valor"] == "R$ 5.300,00" and LIMITE_VIAGEM >= TOTAL_V and LIMITE_VIAGEM - TOTAL_V < 100
assert "Viagem\nmédia R$ 640" in CX["23"]["texto"] and "Definir orçamentos" in CX["23"]["texto"]
FORMAS = [(I_CARTAO, "Cartão no exterior", "crédito ou débito"), (I_SAQUE, "Saque no exterior", ""),
          (I_PREPAGO, "Cartão pré-pago", "e cheques de viagem"), (I_NOTAS, "Dinheiro em espécie", ""),
          (I_TRANSF, "Remessa para uma conta sua lá fora", "")]


def capa_viagem(T):
    def tile(ip, rotulo):
        return f"""<div style='background:{TINTA_2};border:2px solid {TINTA_FIO};border-radius:30px;padding:30px 32px 26px;display:flex;flex-direction:column;justify-content:space-between;height:226px'>
  <div style='display:flex;align-items:center;gap:18px'>
    <div style='width:66px;height:66px;border-radius:20px;background:#13261C;display:flex;align-items:center;justify-content:center;flex:none'>{svg_icone(ip, 38, MENTA, 2)}</div>
    <div style='font-size:27px;font-weight:600;color:{DARK_TEXTO};line-height:1.15'>{rotulo}</div></div>
  <div class='big' style='font-size:104px;line-height:.9;color:#fff;letter-spacing:-.05em'>3,5%</div></div>"""
    corpo = f"""<div class='eyebrow'>Viagem ao exterior</div>
<div class='h1' style='font-size:100px'>Viagem:<br>o IOF é igual.<br><span style='color:{MENTA}'>O câmbio, não.</span></div>
<div style='display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:56px'>
  {tile(I_CARTAO, 'cartão')}{tile(I_NOTAS, 'dinheiro em espécie')}{tile(I_PREPAGO, 'cartão pré-pago')}{tile(I_TRANSF, 'conta sua lá fora')}
</div>"""
    return capa("tinta", corpo, 1, T)


def post_viagem():
    T = 7
    s = [capa_viagem(T)]

    # 2 · o IOF de cada forma de pagar
    def linha(ip, t, sub, ultimo=False):
        return f"""<div style='display:flex;align-items:center;gap:24px;padding:14px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div class='azulejo' style='width:64px;height:64px;flex:none;background:{VERMELHO_SUAVE}'>{svg_icone(ip, 34, CORAL_FORTE, 2)}</div>
  <div style='flex:1'><div style='font-size:32px;font-weight:700;letter-spacing:-.02em'>{t}</div>{f"<div style='font-size:25px;color:{MUTED};margin-top:2px'>{sub}</div>" if sub else ''}</div>
  <div class='big' style='font-size:46px;color:{CORAL_FORTE}'>3,5%</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>IOF no câmbio</div>
<div class='h2'>Para gastar lá fora, 3,5% em todas.</div>
<div class='visual' style='margin-top:40px'><div class='card' style='overflow:hidden'>
  <div style='padding:6px 42px 4px'>{''.join(linha(ip, t, sub, i == len(FORMAS) - 1) for i, (ip, t, sub) in enumerate(FORMAS))}</div>
  <div style='display:flex;align-items:center;gap:24px;padding:18px 42px;background:{SOFT}'>
    <div class='azulejo' style='width:64px;height:64px;flex:none;background:#fff'>{svg_icone(I_ALTA, 34, BRAND_DARK, 2)}</div>
    <div style='flex:1'><div style='font-size:31px;font-weight:700;letter-spacing:-.02em;color:{INK}'>Remessa para investir</div>
      <div style='font-size:25px;color:{BRAND_DEEP};margin-top:2px'>não é dinheiro para gastar na viagem</div></div>
    <div class='big' style='font-size:46px;color:{BRAND_DARK}'>1,10%</div></div>
</div>{nota('Decreto 6.306/2007, art. 15-B (incisos VII, IX, X, XX, XXI e XXI-A), com a redação do Decreto 12.499/2025.')}</div>""", 2, T))

    # 3 · a conta: US$ 1.000 a R$ 5,05
    chips = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:10px;padding:18px 8px;border-radius:20px;background:{BG};border:2px solid {FIO}'>"
                    f"{svg_icone(ip, 38, CORAL_FORTE, 2)}<span style='font-size:23px;font-weight:600;color:{MUTED}'>{t}</span>"
                    f"<span class='big' style='font-size:28px;color:{CORAL_FORTE}'>R$ 176,75</span></div>"
                    for ip, t in [(I_CARTAO, "cartão"), (I_NOTAS, "espécie"), (I_PREPAGO, "pré-pago"), (I_TRANSF, "conta lá fora")])
    conta = f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:32px 46px 34px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding-bottom:20px;border-bottom:2px solid {FIO}'>
    <span style='font-size:31px;font-weight:600;color:{MUTED}'>US$ 1.000 × R$ 5,05</span><span class='big' style='font-size:46px'>{reais(EM_REAIS_V)}</span></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding:20px 0;border-bottom:2px solid {FIO}'>
    <span style='font-size:31px;font-weight:600;color:{CORAL_TXT}'>+ IOF de 3,5%</span><span class='big' style='font-size:46px;color:{CORAL_FORTE}'>{reais(IOF_V)}</span></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding:22px 0 26px'>
    <span style='font-size:34px;font-weight:700'>Total</span><span class='big' style='font-size:66px'>{reais(TOTAL_V)}</span></div>
  <div style='font-size:24px;font-weight:700;letter-spacing:.12em;color:{MUTED};margin-bottom:14px'>O MESMO IOF EM QUALQUER FORMA</div>
  <div style='display:flex;gap:14px'>{chips}</div>
</div>{nota('Exemplo: câmbio de R$ 5,05, sem tarifas.')}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta do IOF</div>
<div class='h2'>US$ 1.000 a R$ 5,05: R$ 176,75 de IOF.</div>{conta}""", 3, T))

    # 4 · o que muda: o câmbio (e as tarifas)
    larg = 330
    def deg(c, total, mais, i):
        w = float(mais) / 207 * larg
        return f"""<div style='display:flex;align-items:center;gap:24px;padding:24px 0;{'' if i == 2 else f'border-bottom:2px solid {FIO};'}'>
  <div style='width:170px;flex:none'><div style='font-size:22px;font-weight:700;letter-spacing:.1em;color:{MUTED}'>CÂMBIO</div>
    <div class='big' style='font-size:46px;margin-top:2px'>R$ {numbr(c)}</div></div>
  <div style='flex:1'><div style='font-size:22px;font-weight:700;letter-spacing:.1em;color:{MUTED}'>TOTAL COM IOF</div>
    <div class='big' style='font-size:40px;margin-top:4px'>{reais(total)}</div></div>
  <div style='width:{larg + 20}px;flex:none'>
    <div style='display:flex;align-items:center;gap:12px'>{f"<i style='display:block;width:{w:.1f}px;height:30px;border-radius:9px;background:{CORAL}'></i>" if mais else f"<i style='display:block;width:4px;height:30px;border-radius:2px;background:{CINZA_ESCURO}'></i>"}</div>
    <div class='big' style='font-size:30px;margin-top:6px;color:{CORAL_FORTE if mais else MUTED}'>{('+' + reais(mais)) if mais else 'a base'}</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O que muda</div>
<div class='h2'>O câmbio e as tarifas.</div>
<div class='p' style='margin-top:22px;font-size:36px'>Cada R$ 0,10 a mais no câmbio custa R$ 103,50 a mais em US$ 1.000, já com o IOF.</div>
<div class='visual' style='margin-top:36px'><div class='card' style='padding:4px 44px'>
  {''.join(deg(c, t, m, i) for i, (c, t, m) in enumerate(zip(CAMBIOS, TOTAIS, A_MAIS)))}
</div>{nota('Câmbios hipotéticos, só para comparar; sem tarifas.')}</div>""", 4, T))

    # 5 · compare o VET (Banco Central)
    def peca(t, cor_f, cor_t, borda=None):
        b = f"border:2px solid {borda};" if borda else ""
        return f"<div style='padding:20px 30px;border-radius:22px;background:{cor_f};{b}font-size:38px;font-weight:700;letter-spacing:-.02em;color:{cor_t};white-space:nowrap'>{t}</div>"
    sinal = lambda t: f"<span style='font-size:52px;font-weight:700;color:{CINZA_ESCURO}'>{t}</span>"
    vet = f"""<div class='visual' style='margin-top:44px'>
  <div style='display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:nowrap'>
    {peca('câmbio', '#fff', INK, FIO)}{sinal('+')}{peca('tarifas', '#fff', INK, FIO)}{sinal('+')}{peca('IOF', VERMELHO_SUAVE, CORAL_FORTE)}{sinal('=')}{peca('VET', INK, '#fff')}</div>
  <div class='card' style='margin-top:34px;padding:32px 40px 30px'>
    <div style='font-size:33px;font-weight:600;letter-spacing:-.015em;line-height:1.36;color:{INK}'>“O Valor Efetivo Total (VET) representa o custo de uma operação de câmbio em reais por moeda estrangeira, englobando a taxa de câmbio, as tarifas e tributos incidentes sobre essa operação.”</div>
    <div style='font-size:25px;font-weight:700;color:{BRAND_DEEP};margin-top:14px'>Banco Central, Ranking do VET</div></div>
  <div style='display:flex;gap:22px;align-items:flex-start;margin-top:24px;padding:24px 30px;border-radius:22px;background:{AMBAR_SUAVE}'>
    {svg_icone(I_LUPA, 40, AMBER_TEXT, 2.2)}
    <div style='font-size:28px;line-height:1.36;color:{INK}'>No ranking, o Banco Central mostra o VET médio de cada instituição. Os valores são de meses anteriores: confira o de hoje antes de comprar.</div></div>
</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Antes de comprar</div>
<div class='h2'>Compare o VET.</div>{vet}""", 5, T))

    # 6 · tela real: Definir orçamentos com a Viagem em R$ 5.300,00 (relógio em 23/12/2026, sem salvar)
    c = CX["23"]
    bd = tela(P23, "celular-definir-orcamentos-viagem.png")
    sy = c["scrollY"]
    rec = recorte(bd, px(c["titulo"][1] - 20 - sy), px(c["semmov"][3] + 12 - sy), largura=650, x0=px(4), x1=px(386))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>Um teto para a viagem.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Em Orçamentos, Definir limites: busque Viagem. Os US$ 1.000 com IOF, e uma folga, dão R$ 5.300.</div>
<div class='visual' style='margin-top:34px'>{rec}{NOTA_TELA}</div>""", 6, T))

    s.append(fechamento_verde("Viaje com um teto.",
                              "Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 28/12 · 31/12: anote quanto há lá fora
# Remessas (dólar), relógio em 28/12/2026: "Rendimento ano a ano" e "Editar fechamentos" ("Quanto havia no fim de cada ano")
ANOS = {l[1].split(" | ")[0]: l[1] for l in CX["28a"]["linhas"] if l[0].startswith("rya-r")}
assert ANOS["2023"] == "2023 | +6,5% | +120,00 | +3,8% | +R$ 343,68 | aportes 4.000,00 · a R$ 4,90 · fim 4.120,00"
assert ANOS["2024"] == "2024 | +3,6% | +360,00 | +34,4% | +R$ 16.928,73 | aportes 8.000,00 · a R$ 5,05 · fim 12.480,00"
assert ANOS["2025"] == "2025 | +3,9% | +480,00 | −7,7% | −R$ 5.969,09 | fim 12.960,00"
assert ANOS["2026"] == "2026 | até hoje | +3,0% | +350,00 | −6,2% | −R$ 4.067,86 | hoje 13.310,00"
assert CX["28b"]["valores"] == [["2023", "4.120,00", "4,8407"], ["2024", "12.480,00", "6,1917"], ["2025", "12.960,00", "5,5018"]]
_t28 = CX["28b"]["texto"]
for trecho in ["Quanto havia no fim de cada ano", "Com o saldo de 31 de dezembro, o timtimcash separa o rendimento ano a ano. Sem ele, só dá para medir o período inteiro.",
               "2026hoje, em curso\n13.310,00", "busca o PTAX de compra do fecho daquele ano no Banco Central"]:
    assert trecho in _t28, trecho
# o dólar de fechamento caiu 11,1% de 2024 para 2025 (por isso o mesmo rendimento em US$ virou queda em R$)
assert q1((D("5.5018") / D("6.1917") - 1) * 100) == D("-11.1")


def capa_31(T):
    W, H = 896, 640
    folha = f"""<div style='position:absolute;left:24px;top:34px;width:410px;height:550px;transform:rotate(-3deg);transform-origin:50% 0'>
  <div style='position:absolute;inset:0;border-radius:34px;background:#fff;border:2px solid {FIO};box-shadow:0 2px 3px rgba(15,20,16,.05),0 30px 60px -28px rgba(15,20,16,.35);overflow:hidden'>
    <div style='height:122px;background:{INK};display:flex;align-items:flex-end;justify-content:center;padding-bottom:22px'>
      <span style='font-size:36px;font-weight:700;letter-spacing:.2em;color:#fff'>DEZEMBRO</span></div>
    <div class='big' style='text-align:center;font-size:290px;line-height:1;margin-top:26px;letter-spacing:-.07em;color:{INK}'>31</div>
    <div style='text-align:center;font-size:36px;font-weight:600;color:{MUTED};margin-top:6px'>quinta-feira · 2026</div>
  </div>
  {''.join(f"<i style='position:absolute;top:-24px;left:{x}px;width:24px;height:60px;border-radius:12px;background:{CINZA_MEDIO};border:5px solid {BG};display:block'></i>" for x in (104, 282))}
</div>"""
    etiqueta = f"""<div style='position:absolute;left:482px;top:392px;width:396px;transform:rotate(6deg);transform-origin:0 50%'>
  <svg width='120' height='90' viewBox='0 0 120 90' style='position:absolute;left:-104px;top:-30px;overflow:visible'>
    <path d='M0 4 C 44 0, 60 96, 122 80' fill='none' stroke='{INK}' stroke-width='4' stroke-linecap='round'/></svg>
  <div style='position:relative;background:{SOFT};border-radius:22px 34px 34px 22px;padding:36px 40px 34px 64px;box-shadow:0 22px 40px -24px rgba(15,20,16,.45);clip-path:polygon(0 50%,9% 0,100% 0,100% 100%,9% 100%)'>
    <i style='position:absolute;left:30px;top:50%;width:22px;height:22px;margin-top:-11px;border-radius:50%;background:{BG};display:block'></i>
    <div style='font-size:25px;font-weight:700;letter-spacing:.14em;color:{BRAND_DEEP}'>SALDO LÁ FORA</div>
    <div style='display:flex;align-items:baseline;gap:12px;margin-top:12px'>
      <span class='big' style='font-size:64px;color:{INK}'>US$</span>
      <span style='flex:1;border-bottom:5px dotted {BRAND_DARK};height:44px'></span></div>
  </div></div>"""
    corpo = f"""<div class='eyebrow'>Investimento no exterior</div>
<div class='h1' style='font-size:100px'>31/12: anote quanto há lá fora</div>
<div style='position:relative;width:{W}px;height:{H}px;margin-top:30px'>{folha}{etiqueta}</div>"""
    return capa("papel", corpo, 1, T)


def post_31():
    T = 7
    s = [capa_31(T)]

    # 2 · o ano fecha num dia: os saldos de 31/12 numa linha do tempo vertical, com a taxa de cada ano
    marcos = [("31/12/2023", "US$ 4.120", "2023", "+6,5%"), ("31/12/2024", "US$ 12.480", "2024", "+3,6%"),
              ("31/12/2025", "US$ 12.960", "2025", "+3,9%"), ("31/12/2026", None, "2026", "+3,0% até hoje")]
    linhas = []
    for i, (d, v, ano, tx) in enumerate(marcos):
        aberto = v is None
        ponto = (f"<i style='width:30px;height:30px;border-radius:50%;background:{'#fff' if aberto else INK};border:7px solid {CORAL if aberto else INK};"
                 f"box-sizing:border-box;display:block;position:relative;z-index:2'></i>")
        valor = (f"<span style='display:inline-block;padding:4px 18px;border-radius:14px;border:3px dashed {CORAL};font-size:36px;font-weight:700;color:{CORAL_FORTE}'>US$ ?</span>"
                 if aberto else f"<span class='big' style='font-size:42px'>{v}</span>")
        linhas.append(f"""<div style='display:flex;align-items:center;gap:28px;height:112px;position:relative'>
  <div style='width:30px;display:flex;justify-content:center;flex:none'>{ponto}</div>
  <div style='width:220px;flex:none;font-size:30px;font-weight:700;color:{CORAL_TXT if aberto else INK}'>{d}</div>
  <div style='flex:1'>{valor}</div>
  <div style='text-align:right'><div style='font-size:23px;font-weight:700;letter-spacing:.08em;color:{MUTED}'>TAXA DE {ano}</div>
    <div class='big' style='font-size:{34 if not aberto else 28}px;color:{BRAND_DARK}'>{tx}</div></div></div>""")
    trilho = (f"<div style='position:absolute;left:{44 + 14}px;top:{30 + 56}px;height:{112 * 2}px;border-left:5px solid {BRAND}'></div>"
              f"<div style='position:absolute;left:{44 + 14}px;top:{30 + 56 + 224}px;height:112px;border-left:5px dashed {BRAND}'></div>")
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Por que 31/12</div>
<div class='h2'>O ano fecha num dia.</div>
<div class='p' style='margin-top:22px;font-size:36px'>Com o saldo de 31 de dezembro, cada ano ganha a sua taxa. Sem ele, só dá para medir o período inteiro.</div>
<div class='visual' style='margin-top:34px'><div class='card' style='padding:30px 44px;position:relative'>{trilho}{''.join(linhas)}</div>
{nota('Exemplo: a carteira em dólar da conta fictícia dos nossos posts; taxas ao ano em US$, como o site mostra.')}</div>""", 2, T))

    # 3 · em reais, o câmbio do último dia útil muda o ano
    def ano_card(ano, cambio, usd, brl, v_usd, v_brl):
        esc = 300 / 34.4
        def barra(rot, v, txt):
            w = abs(v) * esc
            neg = v < 0
            cor = CORAL if neg else BRAND
            return f"""<div style='display:flex;align-items:center;gap:16px;margin-top:16px'>
  <span style='width:56px;font-size:24px;font-weight:700;color:{MUTED}'>{rot}</span>
  <div style='position:relative;flex:1;height:40px'>
    <div style='position:absolute;left:96px;top:-6px;bottom:-6px;border-left:3px solid {INK}'></div>
    <div style='position:absolute;{'right' if neg else 'left'}:{'calc(100% - 96px)' if neg else '96px'};top:4px;width:{w:.1f}px;height:32px;border-radius:8px;background:{cor}'></div>
    <span class='big' style='position:absolute;left:{(96 + w + 12) if not neg else 108}px;top:0;font-size:32px;color:{CORAL_FORTE if neg else BRAND_DARK}'>{txt}</span></div></div>"""
        return f"""<div class='card' style='padding:28px 36px 30px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span class='big' style='font-size:54px'>{ano}</span>
    <span style='font-size:25px;font-weight:600;color:{MUTED}'>dólar no fechamento: <b style='color:{INK};font-variant-numeric:tabular-nums'>R$ {cambio}</b></span></div>
  {barra('US$', v_usd, usd)}{barra('R$', v_brl, brl)}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em reais</div>
<div class='h2'>O câmbio do último dia muda o ano.</div>
<div class='p' style='margin-top:22px;font-size:36px'>Quase o mesmo rendimento em dólar. Em reais, anos opostos.</div>
<div class='visual' style='margin-top:34px;display:flex;flex-direction:column;gap:20px'>
  {ano_card('2024', '6,1917', '+3,6%', '+34,4%', 3.6, 34.4)}
  {ano_card('2025', '5,5018', '+3,9%', MENOS + '7,7%', 3.9, -7.7)}
{nota('Taxas ao ano do exemplo. O site usa a PTAX de compra do último dia útil de cada ano.')}</div>""", 3, T))

    # 4 · tela real: Rendimento ano a ano (relógio em 28/12/2026)
    c = CX["28a"]
    rd = tela(P28, "celular-remessas-dolar.png")
    linhas = {l[1].split(" | ")[0]: l for l in c["linhas"] if l[0].startswith("rya-r")}
    larg = 700
    xa, xb = c["painel"][0], c["painel"][2]
    cab = recorte(rd, px(c["painel"][1] + 2), px(c["editar"][3] + 14), largura=larg, x0=px(xa), x1=px(xb))
    anos = recorte(rd, px(linhas["2024"][3] - 2), px(linhas["2025"][5] + 2), largura=larg, x0=px(xa), x1=px(xb))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>Cada ano, em US$ e em reais.</div>
<div class='visual' style='margin-top:34px'>{cab}<div style='height:14px'></div>{anos}{NOTA_TELA}</div>""", 4, T))

    # 5 · tela real: Editar fechamentos (relógio em 28/12/2026)
    c = CX["28b"]
    fe = tela(P28, "celular-fechamentos.png")
    sy = c["scrollY"]
    larg = 500
    rot = recorte(fe, px(c["titulo"][1] - 14 - sy), px(c["sub"][3] + 12 - sy), largura=larg, x0=px(6), x1=px(384))
    linhas2 = recorte(fe, px(c["r2025"][1] - 6 - sy), px(c["hoje"][3] + 6 - sy), largura=larg, x0=px(6), x1=px(384))
    passos = [("1", "Em 31/12", "anote o saldo de cada conta lá fora, na moeda."),
              ("2", "Em janeiro", "atualize a carteira e informe o saldo de 31/12 em Editar fechamentos."),
              ("3", "Toque em PTAX", "e o site busca o câmbio de compra do último boletim do ano. 31/12 nem sempre tem boletim.")]
    lado = "".join(f"""<div style='display:flex;gap:16px;align-items:flex-start;{'' if i == 0 else 'margin-top:26px;'}'>
  <div style='width:44px;height:44px;border-radius:50%;background:{BRAND};color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;flex:none'>{n}</div>
  <div><div style='font-size:29px;font-weight:700;letter-spacing:-.02em;color:{INK}'>{t}</div>
    <div style='font-size:25px;line-height:1.32;color:{MUTED};margin-top:4px'>{d}</div></div></div>""" for i, (n, t, d) in enumerate(passos))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Como fazer</div>
<div class='h3'>Anote em 31/12. Informe depois.</div>
<div class='visual' style='margin-top:34px;display:flex;gap:30px;align-items:center'>
  <div style='width:{larg}px;flex:none'>{rot}<div style='height:12px'></div>{linhas2}</div>
  <div style='flex:1'>{lado}</div></div>
{NOTA_TELA}""", 5, T))

    # 6 · e a declaração? (Receita Federal e Lei 14.754/2023, sem consultoria)
    def fato(ip, titulo, txt, fonte_):
        return f"""<div class='card' style='padding:28px 36px;display:flex;gap:26px;align-items:flex-start'>
  {azulejo(ip, 78, 38)}
  <div><div style='font-size:24px;font-weight:700;letter-spacing:.12em;color:{BRAND_DEEP}'>{titulo}</div>
    <div style='font-size:31px;line-height:1.34;color:{INK};margin-top:8px'>{txt}</div>
    <div style='font-size:23px;font-weight:600;color:{MUTED};margin-top:10px'>{fonte_}</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>E a declaração?</div>
<div class='h2'>O IR também olha para 31/12.</div>
<div class='visual' style='margin-top:40px;display:flex;flex-direction:column;gap:20px'>
  {fato(I_CAL, 'BENS E DIREITOS', 'A declaração relaciona os bens e direitos, no Brasil ou no exterior, que formam o seu patrimônio em 31 de dezembro.', 'Receita Federal, Perguntas e Respostas IRPF 2026, pergunta&nbsp;007')}
  {fato(I_GLOBO, 'APLICAÇÕES NO EXTERIOR', 'Desde 2024, os rendimentos entram na declaração anual, separados dos demais, com 15% sobre a parcela anual.', 'Lei 14.754/2023, art. 2º')}
  <div style='display:flex;gap:22px;align-items:center;padding:24px 32px;border-radius:22px;background:{AMBAR_SUAVE}'>
    {svg_icone(I_ALERT, 40, AMBER_TEXT, 2.2)}
    <div style='font-size:28px;line-height:1.36;color:{INK}'>O timtimcash organiza os números; não faz a declaração. Para o seu caso, confira com um contador.</div></div>
</div>""", 6, T))

    s.append(fechamento_verde("Feche o ano com o saldo anotado.",
                              "Remessas ao exterior no timtimcash, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]


POSTS = {
    P16: post_inflacao,
    P18: post_patrimonio,
    P21: post_metas,
    P23: post_viagem,
    P28: post_31,
}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    if so:
        so = [p for p in POSTS if any(p.startswith(x) or x in p for x in so)]
    renderizar(POSTS, so=so)
