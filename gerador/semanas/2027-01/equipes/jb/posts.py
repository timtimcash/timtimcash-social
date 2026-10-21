# -*- coding: utf-8 -*-
"""Carrosséis da equipe jb (janeiro de 2027): 16/01, 20/01, 22/01, 27/01 e 29/01.

Peças do kit (J/kit/carrossel.py), no formato aprovado em outubro, novembro e dezembro. Telas reais capturadas por
captura.py (cópia local do site, build 2026-10-19.5, conta fictícia), guardadas em J/saida/<pasta>/telas/; as caixas
(px CSS) dos recortes ficam em caixas.json. Toda conta dos slides é conferida por assert neste arquivo, contra as telas.

python3 posts.py [pasta ...]      grava J/saida/<pasta>/01.jpg ... e confere o layout
"""
import json, math, os, sys
from decimal import Decimal as D, ROUND_HALF_UP

J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
sys.path.insert(0, J + "/kit")
from carrossel import *          # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl...)

AQUI = os.path.dirname(os.path.abspath(__file__))
CX = json.loads(open(os.path.join(AQUI, "caixas.json"), encoding="utf-8").read().replace(" ", " "))

P16 = "2027-01-11_remessas-quanto-foi-para-fora"
P20 = "2027-01-20_traga-3-meses-de-historico"
P22 = "2027-01-22_seus-dados-guardados"
P27 = "2027-01-29_fechamento-de-2026-la-fora"
P29 = "2027-01-16_o-que-se-repete-todo-mes"

MENOS = "−"
CINZA_CLARO = "#E6E3DA"
CINZA_MEDIO = "#D4D2C8"
CINZA_ESCURO = "#B9B5A8"
VERMELHO_SUAVE = "#FBEAEA"
AMBAR_SUAVE = "#FBF1DC"
CORAL_PALIDO = "#F6D9CD"
FONTE_SVG = "font-family='Inter' style='font-feature-settings:\"tnum\",\"cv11\",\"ss01\"'"


def tela(pasta, nome):
    return os.path.join(SAIDA, pasta, "telas", nome)


def corte(pasta, nome, caixa, largura, sy=0, esc=3, pad=(0, 0, 0, 0), raio=22):
    """Recorte de uma tela real a partir de uma caixa em px CSS do documento (x0, y0, x1, y1).
    sy: rolagem da página na hora da foto; pad: folga (cima, direita, baixo, esquerda) em px CSS."""
    x0, y0, x1, y1 = caixa[:4]
    pt, pr, pb, pl = pad
    return recorte(tela(pasta, nome), round((y0 - pt - sy) * esc), round((y1 + pb - sy) * esc), largura=largura,
                   x0=round((x0 - pl) * esc), x1=round((x1 + pr) * esc), raio=raio)


def alt_corte(caixa, largura, pad=(0, 0, 0, 0)):
    """Altura (px do slide) que um recorte vai ocupar."""
    x0, y0, x1, y1 = caixa[:4]
    pt, pr, pb, pl = pad
    return (y1 + pb - y0 + pt) * largura / (x1 + pr - x0 + pl)


def q2(v):
    return D(v).quantize(D("0.01"), rounding=ROUND_HALF_UP)


def q1(v):
    return D(v).quantize(D("0.1"), rounding=ROUND_HALF_UP)


def reais(v, casas=2):
    return brl(float(v), casas > 0)


def numbr(v, casas=2):
    return num(float(v), casas)


def nota(txt, centro=False, extra=""):
    estilo = f" style='{'text-align:center;' if centro else ''}{extra}'"
    return f"<div class='nota'{estilo}>{txt}</div>"


def nota_tela(extra=""):
    return f"<div class='nota' style='text-align:center;{extra}'>Tela real do timtimcash, com dados de exemplo.</div>"


def sobre(txt, cor=MUTED, tam=24, extra=""):
    """Rótulo pequeno em caixa alta (sobre um recorte ou um número)."""
    return f"<div style='font-size:{tam}px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:{cor};{extra}'>{txt}</div>"


def pilula(txt, fundo=SOFT, cor=BRAND_DEEP, tam=24, extra=""):
    return (f"<span style='display:inline-flex;align-items:center;gap:10px;padding:8px 18px;border-radius:999px;background:{fundo};"
            f"color:{cor};font-size:{tam}px;font-weight:700;white-space:nowrap;{extra}'>{txt}</span>")


def num_bola(n, cor=BRAND, tam=50, fonte=26):
    return (f"<div style='width:{tam}px;height:{tam}px;border-radius:50%;background:{cor};color:#fff;display:flex;align-items:center;"
            f"justify-content:center;font-size:{fonte}px;font-weight:700;flex:none'>{n}</div>")


# ícones de traço extras (24 x 24)
I_SETA_DIR = '<path d="M5 12h14M13 6l6 6-6 6"/>'
I_SETA_BAIXO = '<path d="M12 4v16M6 14l6 6 6-6"/>'
I_GLOBO2 = I_GLOBO
I_PASTA = '<path d="M3.5 7.5A2 2 0 0 1 5.5 5.5h4l2 2.5h7a2 2 0 0 1 2 2v7.5a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2z"/>'
I_UPLOAD = '<path d="M12 15V4M7 9l5-5 5 5"/><path d="M4.5 14.5v4a1.5 1.5 0 0 0 1.5 1.5h12a1.5 1.5 0 0 0 1.5-1.5v-4"/>'
I_PLANILHA = '<rect x="4" y="3.5" width="16" height="17" rx="2"/><path d="M4 9h16M4 14.5h16M10 3.5v17"/>'
I_BANCO = '<path d="M12 3.5 20.5 8h-17z"/><path d="M5 11v6.5M9.7 11v6.5M14.3 11v6.5M19 11v6.5"/><path d="M3.5 20.5h17"/>'
I_CADEADO = '<rect x="5" y="10.5" width="14" height="10" rx="2.2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>'
I_REPETE = '<path d="M17 3.5l3 3-3 3"/><path d="M20 6.5H8a4 4 0 0 0-4 4V12"/><path d="M7 20.5l-3-3 3-3"/><path d="M4 17.5h12a4 4 0 0 0 4-4V12"/>'
I_RAIO = '<path d="M13 3 5.5 13.5H12L11 21l7.5-10.5H12z"/>'
I_LAPIS = '<path d="M4 20l1-4.5L16 4.5l3.5 3.5L8.5 19z"/><path d="M14 7l3 3"/>'
I_ALVO = '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.6"/>'
I_CARTEIRA = '<path d="M4 7.5A2.5 2.5 0 0 1 6.5 5H18v3"/><rect x="3.5" y="8" width="17" height="11.5" rx="2.5"/><path d="M16 13.75h.01"/>'
I_NUVEM = '<path d="M7 18.5h10a4 4 0 0 0 .6-7.96A6 6 0 0 0 6.1 9.6 4.5 4.5 0 0 0 7 18.5z"/>'
I_ARQUIVO = '<path d="M6.5 3.5h7l4 4v13h-11z"/><path d="M13.5 3.5v4h4"/>'


def item(ip, titulo, sub, ultimo=False, tam_t=34, tam_s=27, pad=24):
    """Linha com ícone em azulejo, título e apoio (desenho dos modelos de outubro)."""
    return f"""<div style='display:flex;gap:28px;align-items:center;padding:{pad}px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  {azulejo(ip)}
  <div><div style='font-size:{tam_t}px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{titulo}</div>
  <div style='font-size:{tam_s}px;color:{MUTED};margin-top:6px;line-height:1.3;text-wrap:balance'>{sub}</div></div></div>"""


# ================================================================ 16/01 · Quanto foi para fora, ano a ano?
# Remessas, relógio em 16/01/2027 10:00. Computador 1024 px: tabela "Remessas" em "Por ano" (dólar). Celular: os quatro
# indicadores do euro. A conta de base tem 3 remessas de US$ 4.000 (2023 e 2024) e € 2.000 em 01/12/2026.
_c16 = CX["16"]
_td = [t[0] for t in _c16["tab_usd"]["td"]]
assert _td[:5] == ["2024 | 2 envios · mar a abr", "Conta corrente→Corretora no exterior", "8.000,00", "5,0500", "40.400,00"], _td[:5]
assert _td[7:12] == ["2023 | 1 envio · jul", "Conta corrente→Corretora no exterior", "4.000,00", "4,9000", "19.600,00"], _td[7:12]
assert _td[14:19] == ["Total | 2 anos · 3 envios", "", "12.000,00", "5,0000", "60.000,00"], _td[14:19]
assert [t[0] for t in _c16["tab_usd"]["th"]][4:6] == ["CUSTO | R$", "HOJE | R$ · a 5,0515"]
ANO_USD = {2023: (D("4000"), D("19600")), 2024: (D("8000"), D("40400"))}
assert q2(D("40400") / 8000) == D("5.05") and q2(D("19600") / 4000) == D("4.90") and q2(D("60000") / 12000) == D("5.00")
_eur = _c16["cel_EUR"]["cartao_ind"][5]
assert _eur.split("\n") == ["Remetido", "€ 2.000,00", "1 remessa · desde dez/26", "Custo total", "R$ 11.525,40",
                            "tudo que saiu do Brasil, com IOF", "Câmbio médio efetivo", "R$ 5,7627", "com IOF · sem IOF R$ 5,7000",
                            "IOF pago", "R$ 125,40", "1,10% do valor enviado"], _eur
EUR_ENV, EUR_CUSTO, EUR_IOF = D("2000"), D("11525.40"), D("125.40")
assert (EUR_CUSTO / EUR_ENV).quantize(D("0.0001")) == D("5.7627")
assert ((EUR_CUSTO - EUR_IOF) / EUR_ENV).quantize(D("0.0001")) == D("5.7000")
assert q2(EUR_IOF / (EUR_CUSTO - EUR_IOF) * 100) == D("1.10")
CUSTO_ANO = {2023: D("19600"), 2024: D("40400"), 2025: D("0"), 2026: EUR_CUSTO}
CUSTO_TOTAL = sum(CUSTO_ANO.values())
assert CUSTO_TOTAL == D("71525.40")       # o mesmo "lá fora" do patrimônio de 18/12 (60.000 + 11.525,40)


def bandeira(simbolo, cor, x, y, alto=86):
    """Mastro com uma flâmula de moeda (US$ ou €), desenhada; sem bandeira de país."""
    larg = 118 if len(simbolo) > 1 else 92
    return (f"<line x1='{x}' y1='{y}' x2='{x}' y2='{y - alto}' stroke='{INK}' stroke-width='4' stroke-linecap='round'/>"
            f"<path d='M{x + 2} {y - alto} h{larg} l-16 24 l16 24 h-{larg} z' fill='{cor}'/>"
            f"<text x='{x + 2 + (larg - 14) / 2}' y='{y - alto + 34}' text-anchor='middle' {FONTE_SVG} font-weight='700' font-size='29' "
            f"letter-spacing='-.5' fill='#FFFFFF'>{simbolo}</text>")


def barras_por_ano(W=896, H=700, capa=True):
    """Colunas por ano com um bloco por remessa (altura pelo custo em reais) e a flâmula da moeda."""
    base = H - 74
    esc = 440 / 40400
    col, gap = 168, (W - 4 * 168) / 3
    blocos = {2023: [("USD", D("19600"))], 2024: [("USD", D("20000")), ("USD", D("20400"))], 2025: [], 2026: [("EUR", EUR_CUSTO)]}
    rot = {2023: "US$ 4.000", 2024: "US$ 8.000", 2025: "", 2026: "€ 2.000"}
    cor = {"USD": INK, "EUR": BRAND}
    el = [f"<line x1='0' y1='{base}' x2='{W}' y2='{base}' stroke='{CINZA_MEDIO}' stroke-width='3'/>"]
    for i, ano in enumerate((2023, 2024, 2025, 2026)):
        x = i * (col + gap)
        y = base
        for k, (m, v) in enumerate(blocos[ano]):
            h = float(v) * esc
            r = 16 if k == len(blocos[ano]) - 1 else 6
            y -= h
            el.append(f"<path d='M{x} {y + h} V{y + r} Q{x} {y} {x + r} {y} H{x + col - r} Q{x + col} {y} {x + col} {y + r} V{y + h} Z' fill='{cor[m]}'/>")
            y -= 6
        if blocos[ano]:
            topo = y + 6
            m = blocos[ano][0][0]
            el.append(f"<text x='{x + col / 2}' y='{topo + 52}' text-anchor='middle' {FONTE_SVG} font-weight='700' font-size='31' "
                      f"letter-spacing='-.8' fill='#FFFFFF'>{rot[ano]}</text>")
            el.append(bandeira("US$" if m == "USD" else "€", cor[m], x + 22, topo - 14))
        else:
            el.append(f"<rect x='{x + 3}' y='{base - 92}' width='{col - 6}' height='88' rx='16' fill='none' stroke='{CINZA_ESCURO}' "
                      f"stroke-width='3' stroke-dasharray='9 9'/>")
            el.append(f"<text x='{x + col / 2}' y='{base - 56}' text-anchor='middle' {FONTE_SVG} font-weight='600' font-size='23' fill='{MUTED}'>nenhum</text>")
            el.append(f"<text x='{x + col / 2}' y='{base - 27}' text-anchor='middle' {FONTE_SVG} font-weight='600' font-size='23' fill='{MUTED}'>envio</text>")
        el.append(f"<text x='{x + col / 2}' y='{base + 52}' text-anchor='middle' {FONTE_SVG} font-weight='700' font-size='38' "
                  f"letter-spacing='-1' fill='{INK}'>{ano}</text>")
    return f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='display:block;overflow:visible'>{''.join(el)}</svg>"


def capa_16(T):
    corpo = f"""<div class='eyebrow'>Investimento no exterior</div>
<div class='h1' style='font-size:100px'>Quanto foi para fora, ano a ano?</div>
<div style='margin-top:40px'>{barras_por_ano()}</div>"""
    return capa("papel", corpo, 1, T)


def post_16():
    T = 6
    s = [capa_16(T)]
    c = _c16["tab_usd"]
    th = c["th"]
    # 2 · a tabela Por ano (dólar): colunas de Ano a Custo (a coluna Hoje fica de fora)
    caixa_tab = [th[0][1] - 12, max(th[0][2] - 8, c["nota"][3] + 2), th[4][3] + 9, c["td"][-1][4] + 8]
    larg = 896
    seg = corte(P16, "computador-remessas-por-ano-dolar.png", c["seg"], 330, pad=(5, 5, 5, 5), raio=40)
    tab = corte(P16, "computador-remessas-por-ano-dolar.png", caixa_tab, larg)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em Remessas · Por ano</div>
<div class='h3'>Cada ano numa linha.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Quantos envios, quanto foi, o câmbio e o custo em reais. No exemplo, US$ 12.000 em dois anos.</div>
<div class='visual' style='margin-top:40px'>
  <div style='display:flex;justify-content:flex-end;margin-bottom:22px'>{seg}</div>
  {tab}{NOTA_TELA}</div>""", 2, T))

    # 3 · os quatro números do topo, no euro (2026)
    e = _c16["cel_EUR"]
    larg = 640
    card = corte(P16, "celular-remessas-euro.png", e["cartao_ind"][1:5], larg, raio=24)
    bm = e["botoes_moeda"]
    assert [b[0] for b in bm] == ["🇺🇸 USD", "🇪🇺 EUR"]
    chips = corte(P16, "celular-remessas-euro.png", [bm[0][1], bm[0][2], bm[1][3], bm[1][4]], 330, pad=(6, 8, 6, 8), raio=26)
    linhas = [("1", "Remetido", "quanto saiu, na moeda"), ("2", "Custo total", "o que saiu em reais, com IOF"),
              ("3", "Câmbio médio efetivo", "custo ÷ remetido"), ("4", "IOF pago", "em reais e em % do envio")]
    lado = "".join(f"""<div style='display:flex;gap:16px;align-items:flex-start'>
  {num_bola(n, BRAND, 42, 23)}
  <div><div style='font-size:27px;font-weight:700;letter-spacing:-.02em;color:{INK};line-height:1.15'>{t}</div>
    <div style='font-size:24px;line-height:1.3;color:{MUTED};margin-top:3px'>{d}</div></div></div>""" for i, (n, t, d) in enumerate(linhas))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Moeda por moeda</div>
<div class='h3'>Quatro números no topo.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Os botões USD e EUR trocam a moeda. No euro, € 2.000 em dezembro de 2026.</div>
<div class='visual' style='margin-top:36px'>
  <div style='display:flex;justify-content:center;margin-bottom:22px'>{chips}</div>
  {card}
  <div class='card' style='margin-top:24px;padding:26px 34px;display:grid;grid-template-columns:1fr 1fr;column-gap:28px;row-gap:22px'>{lado}</div>
  {NOTA_TELA}</div>""", 3, T))

    # 4 · em reais, ano a ano (o custo de cada ano, das duas moedas)
    maxv = float(max(CUSTO_ANO.values()))
    linhas = []
    for ano, v in CUSTO_ANO.items():
        w = float(v) / maxv * 400
        moeda = {2023: "US$ 4.000 · 1 envio", 2024: "US$ 8.000 · 2 envios", 2025: "nenhum envio", 2026: "€ 2.000 · 1 envio"}[ano]
        cor = BRAND if ano == 2026 else INK
        barra = (f"<i style='display:block;width:{w:.1f}px;height:40px;border-radius:10px;background:{cor}'></i>" if v
                 else f"<i style='display:block;width:150px;height:40px;border-radius:10px;border:3px dashed {CINZA_ESCURO};box-sizing:border-box'></i>")
        linhas.append(f"""<div style='display:grid;grid-template-columns:118px 1fr;align-items:center;column-gap:22px;padding:20px 0;{'' if ano == 2026 else f'border-bottom:2px solid {FIO};'}'>
  <div class='big' style='font-size:42px'>{ano}</div>
  <div><div style='display:flex;align-items:center;gap:18px'>{barra}<span class='big' style='font-size:34px;color:{INK if v else MUTED}'>{reais(v) if v else 'R$ 0'}</span></div>
    <div style='font-size:24px;font-weight:600;color:{MUTED};margin-top:8px'>{moeda}</div></div></div>""")
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em reais</div>
<div class='h3'>O custo de cada ano.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Em reais dá para somar as moedas: é o que saiu das suas contas aqui.</div>
<div class='visual' style='margin-top:38px'><div class='card' style='padding:12px 44px 14px'>{''.join(linhas)}
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding:22px 0 10px;border-top:3px solid {INK};margin-top:6px'>
    <span style='font-size:30px;font-weight:700'>Total · 4 remessas</span><span class='big' style='font-size:46px'>{reais(CUSTO_TOTAL)}</span></div></div>
{nota('Custos da tabela de cada moeda: R$ 60.000,00 em dólar (2023 e 2024) e R$ 11.525,40 em euro (2026).')}</div>""", 4, T))

    # 5 · por que olhar por ano
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Para 2027</div>
<div class='h2'>Por que olhar por ano?</div>
<div class='visual' style='margin-top:44px'><div class='card' style='padding:6px 44px'>
  {item(I_CAL, 'O ritmo', 'Em que anos você mandou e quanto. No exemplo, 2025 ficou sem envio.')}
  {item(I_SETAS, 'O câmbio de cada ano', 'R$ 4,90 em 2023 e R$ 5,05 em 2024, no dólar. No euro, R$ 5,7627 com IOF.')}
  {item(I_ALVO, 'O plano de 2027', 'Quanto mandar e quando, com o histórico na mão.', ultimo=True)}
</div>{nota('Exemplo: a conta fictícia dos nossos posts. O timtimcash organiza os números; não recomenda investimento.')}</div>""", 5, T))

    s.append(fechamento_verde("Veja quanto foi para fora, ano a ano.",
                              "Remessas ao exterior no timtimcash, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]



# ================================================================ 20/01 · Traga 3 meses do passado
# A mesma pessoa da conta de exemplo, como se tivesse começado no timtimcash em 02/01/2027 (estado_jb.py, gerar_novo):
# relógio em 20/01/2027 10:00, celular. Antes: só janeiro. Depois: o extrato .ofx de exemplo da Conta corrente
# (out a dez/2026, os mesmos lançamentos da conta de base), sem as 3 aplicações na reserva, e o saldo ajustado ao extrato.
_c20 = CX["20"]
_antes = {c[0]: c[5] for c in _c20["visao_antes"]["cards"]}
_depois = {c[0]: c[5] for c in _c20["visao_depois"]["cards"]}
assert _antes == {"Receitas": "Receitas | R$ 9.960 | 1º mês", "Despesas": "Despesas | R$ 9.018 | 1º mês",
                  "Resultado": "Resultado | R$ 941 | 1º mês"}, _antes
assert _depois == {"Receitas": "Receitas | R$ 9.960 | queda de | 20,6%", "Despesas": "Despesas | R$ 9.018 | queda de | 3,5%",
                   "Resultado": "Resultado | R$ 941 | queda de | 70,5%"}, _depois
assert "Comparado com a média por mês de Jan/26 a Dez/26" in _c20["visao_depois"]["texto"]
assert "Jan/26 a Dez/26 · 3 de 12 meses ativos" in _c20["visao_depois"]["texto"]
assert "O diagnóstico compara o mês com a sua média. Ele começa quando houver 3 meses de histórico antes deste (faltam 3)." in _c20["rel_antes"]["texto"].replace("\n", " ")
assert "47 de 93 linhas vieram com categoria sugerida pelo nome do estabelecimento" in _c20["revisar"]["faixa_caixa"][4]
assert _c20["revisar90"]["resumo"].split("\n") == ["90", "SELECIONADAS", "R$ 37.613,36", "RECEITAS", "R$ 28.043,30", "DESPESAS", "R$ 9.570,06", "RESULTADO"]
assert _c20["revisar90"]["botao"] == ["Importar 90 linhas"]
assert [l[0] for l in _c20["revisar"]["linhas"][1:4]] == ["CONTA DE LUZ", "HOSPEDAGEM NO ANO-NOVO", "SUPERMERCADO DA VILA"]
assert "28/12/2026 | Mercado | sugerida | Pago" in _c20["revisar"]["linhas"][3][2]
assert "termina com R$ 19.063,66 em 31/12/2026. No timtimcash, a conta ficou com R$ 28.633,72 nessa data." in _c20["saldo"]["modal"][4]
assert D("28633.72") - D("19063.66") == D("9570.06")
# a conferência com a conta de base: as receitas e despesas de out a dez/2026 na Conta corrente
import importlib
sys.path.insert(0, os.path.join(AQUI, "ap" "p"))
_E = importlib.import_module("estado")
_b20, _ = _E.gerar("2027-01-20")
_od = [t for t in _b20["txs"] if "2026-10-01" <= t["data"] <= "2026-12-31" and t["conciliado"] and t["tipo"] in ("receita", "despesa")]
REC_3M = sum(D(str(t["valor"])) for t in _od if t["tipo"] == "receita")
DES_3M = sum(D(str(t["valor"])) for t in _od if t["tipo"] == "despesa")
assert all(t["contaId"] == 1 for t in _od) and (REC_3M, DES_3M) == (D("37613.36"), D("28043.30"))
MED_REC, MED_DES = REC_3M / 3, DES_3M / 3
assert q1((D("9960") / MED_REC - 1) * 100) == D("-20.6") and q1((D("9018.50") / MED_DES - 1) * 100) == D("-3.5")
assert q1((D("941.50") / ((REC_3M - DES_3M) / 3) - 1) * 100) == D("-70.5")


def folha_extrato(mes, linhas, larg=250, alto=318):
    """Folha de extrato desenhada: o mês no alto e linhas de lançamento (traço e valor em verde ou coral)."""
    rows = "".join(f"""<div style='display:flex;align-items:center;gap:12px;height:34px;border-top:2px solid {FIO}'>
  <i style='display:block;width:{w}px;height:10px;border-radius:5px;background:{CINZA_CLARO}'></i><span style='flex:1'></span>
  <i style='display:block;width:{v}px;height:10px;border-radius:5px;background:{BRAND if rec else CORAL}'></i></div>"""
                   for w, v, rec in linhas)
    return f"""<div style='width:{larg}px;height:{alto}px;border-radius:22px;background:#fff;box-shadow:0 2px 3px rgba(15,20,16,.06),0 26px 50px -24px rgba(15,20,16,.40);padding:24px 24px 0;box-sizing:border-box;overflow:hidden'>
  <div style='display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px'>
    <span class='big' style='font-size:54px;line-height:1;letter-spacing:-.04em'>{mes}</span><span style='font-size:21px;font-weight:700;color:{MUTED}'>2026</span></div>
  {rows}</div>"""


def capa_20(T):
    lin = [[(96, 44, True), (120, 30, False), (80, 38, False), (110, 26, False), (70, 34, False), (100, 22, False), (84, 30, False)],
           [(110, 30, False), (76, 44, True), (120, 26, False), (90, 36, False), (104, 22, False), (72, 30, False), (98, 34, False)],
           [(88, 26, False), (118, 34, False), (100, 44, True), (76, 30, False), (112, 40, True), (92, 24, False), (80, 32, False)]]
    folhas = [("OUT", -13, 70, 74), ("NOV", -1, 323, 34), ("DEZ", 12, 576, 76)]
    els = "".join(f"<div style='position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg);transform-origin:50% 100%'>{folha_extrato(m, l)}</div>"
                  for (m, r, x, y), l in zip(folhas, lin))
    seta = svg_icone(I_SETA_BAIXO, 54, BRAND_DEEP, 2.6)
    corpo = f"""<div class='eyebrow'>Comece 2027</div>
<div class='h1' style='font-size:104px'>Traga 3 meses do passado.</div>
<div style='position:relative;width:896px;height:600px;margin-top:40px'>
  <div style='position:absolute;left:40px;top:258px;width:816px;height:330px;border-radius:34px;background:{BRAND_DEEP}'></div>
  <div style='position:absolute;left:40px;top:226px;width:250px;height:60px;border-radius:26px 26px 0 0;background:{BRAND_DEEP}'></div>
  {els}
  <div style='position:absolute;left:10px;top:380px;width:876px;height:220px;border-radius:30px;background:{INK};box-shadow:0 -10px 30px -18px rgba(15,20,16,.5);display:flex;align-items:center;justify-content:center;gap:22px'>
    <div style='width:84px;height:84px;border-radius:24px;background:#1C241D;display:flex;align-items:center;justify-content:center'>{svg_icone(I_UPLOAD, 46, MENTA, 2.2)}</div>
    <span style='font-size:52px;font-weight:700;letter-spacing:-.03em;color:#fff'>Importar</span></div>
</div>"""
    return capa("suave", corpo, 1, T)


def post_20():
    T = 7
    s = [capa_20(T)]
    va, ra = _c20["visao_antes"], _c20["rel_antes"]
    cards_antes = [va["cards"][0][1], va["cards"][0][2], va["cards"][2][3], va["cards"][2][4]]

    # 2 · sem histórico, não há média
    cA = corte(P20, "celular-visao-geral-antes.png", cards_antes, 860, pad=(8, 8, 8, 8), raio=26)
    cB = corte(P20, "celular-relatorios-antes.png", ra["bloco"][1:5], 860, pad=(10, 10, 10, 10), raio=26)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Por que 3 meses</div>
<div class='h3'>A média começa com 3 meses de histórico.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Sem passado, o site mostra só o mês: cada número vem com o selo 1º mês.</div>
<div class='visual' style='margin-top:36px'>{cA}<div style='height:22px'></div>{cB}{NOTA_TELA}</div>""", 2, T))

    # 3 · dois caminhos no Importar
    seg = corte(P20, "celular-importar-planilha.png", _c20["imp_planilha"]["seg"], 860, pad=(6, 6, 6, 6), raio=40)
    def caminho(ip, titulo, sub, linhas):
        lis = "".join(f"<div style='display:flex;gap:12px;align-items:flex-start;margin-top:18px'>{svg_icone(I_CHECK, 32, BRAND_DARK, 2.6)}"
                      f"<span style='font-size:29px;line-height:1.3;color:{INK}'>{t}</span></div>" for t in linhas)
        return f"""<div class='card' style='flex:1;padding:30px 30px 34px'>
  {azulejo(ip, 76, 38)}
  <div style='font-size:34px;font-weight:700;letter-spacing:-.025em;line-height:1.1;margin-top:18px'>{titulo}</div>
  <div style='font-size:25px;font-weight:600;color:{MUTED};margin-top:6px'>{sub}</div>
  <div class='fio' style='margin-top:20px'></div>{lis}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No menu, Importar</div>
<div class='h3'>Extrato do banco ou planilha.</div>
<div class='visual' style='margin-top:40px'>{seg}
  <div style='display:flex;gap:22px;margin-top:26px'>
    {caminho(I_BANCO, 'Extrato do banco', 'arquivo .ofx', ['Você escolhe a conta de destino.', 'As categorias chegam sugeridas.', 'O que já entrou vem desmarcado.'])}
    {caminho(I_PLANILHA, 'Sua planilha', '.xlsx ou .csv', ['6 colunas, em qualquer ordem.', 'Há um modelo pronto em Excel.', 'Conta nova vem marcada como Nova.'])}
  </div>{nota_tela('margin-top:20px')}</div>""", 3, T))

    # 4 · a revisão
    rv = _c20["revisar"]
    faixa = corte(P20, "celular-revisar-importacao.png", rv["faixa_caixa"][:4], 660, pad=(4, 4, 4, 4), raio=24)
    linha = corte(P20, "celular-revisar-importacao.png", rv["linhas"][3][3:7], 660, pad=(0, 0, 0, 0), raio=24)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Antes de confirmar</div>
<div class='h3'>Você revisa cada linha.</div>
<div class='p' style='margin-top:16px;font-size:34px'>No exemplo, 47 de 93 linhas vieram com categoria. As 3 aplicações na reserva saíram: não são gasto.</div>
<div class='visual' style='margin-top:30px'>{faixa}<div style='height:16px'></div>{linha}{NOTA_TELA}</div>""", 4, T))

    # 5 · o saldo que não bate
    md = corte(P20, "celular-saldo-nao-bate.png", _c20["saldo"]["modal"][:4], 600, pad=(2, 2, 2, 2), raio=30)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Se o saldo não bater</div>
<div class='h3'>O site confere com o banco.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Se a conta foi criada com o saldo de hoje, o site oferece o ajuste. As transações não mudam.</div>
<div class='visual' style='margin-top:34px'>{md}{NOTA_TELA}</div>""", 5, T))

    # 6 · antes e depois
    vd = _c20["visao_depois"]
    cards_depois = [vd["cards"][0][1], vd["cards"][0][2], vd["cards"][2][3], vd["comparado"][3]]
    cD = corte(P20, "celular-visao-geral-depois.png", cards_depois, 780, pad=(8, 8, 8, 8), raio=26)
    cA2 = corte(P20, "celular-visao-geral-antes.png", cards_antes, 780, pad=(8, 8, 8, 8), raio=26)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Depois de importar</div>
<div class='h3'>Pronto: janeiro ganha uma média.</div>
<div class='visual' style='margin-top:30px'>
  {sobre('Antes · só janeiro', MUTED, 24, 'margin:0 0 12px 58px')}{cA2}
  <div style='display:flex;justify-content:center;margin:12px 0 6px'>{svg_icone(I_SETA_BAIXO, 42, BRAND_DARK, 2.6)}</div>
  {sobre('Depois · com out, nov e dez', BRAND_DEEP, 24, 'margin:0 0 12px 58px')}{cD}
  {nota('A média usa os meses com lançamento: no exemplo, out, nov e dez. Janeiro até o dia 20.', centro=True, extra='margin-top:18px')}
  {nota_tela('margin-top:4px')}</div>""", 6, T))

    s.append(fechamento_verde("Comece 2027 com uma média.",
                              "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 22/01 · Seus dados, guardados todo dia
# Preferências, relógio em 22/01/2027 10:00, celular, conta de base com a lista de cópias de exemplo (estado_jb.py,
# gerar_22): uma cópia por dia em que a pessoa abriu o site, com o número de lançamentos de cada dia.
_c22 = CX["22"]
_lin22 = [l[0] for l in _c22["pref"]["linhas"]]
assert _lin22[:3] == ["HojeMAIS NOVA | 795 lançamentos · 4 contas · 0,1 MB · 10:00 | Restaurar",
                      "Ontem | 794 lançamentos · 4 contas · 0,1 MB · 19:42 | Restaurar",
                      "20/01, quarta | 793 lançamentos · 4 contas · 0,1 MB · 08:15 | Restaurar"], _lin22[:3]
assert _lin22[7] == "31/12/2026FIM DE DEZEMBRO | 770 lançamentos · 4 contas · 0,1 MB · 10:05 | Restaurar"
assert len(_lin22) == 10
assert "Uma por dia, guardada sozinha quando você abre o timtimcash, à parte da versão em uso." in _c22["pref"]["texto"]
assert "Restaurar substitui os dados atuais. Antes de trocar, o timtimcash guarda uma cópia de agora, então dá para voltar atrás." in _c22["pref"]["texto"]
assert "Arquivo JSON com contas, transações, categorias e orçamentos." in _c22["pref"]["texto"]
assert _c22["restaurar"]["modal"][4].startswith("Restaurar a cópia de ontem\nOs dados de agora (795 lançamentos) serão substituídos pelos de 794 lançamentos daquele dia. Uma cópia de agora é guardada antes, então dá para voltar atrás.")
assert _c22["aviso"]["relogio"].startswith("Fri Jan 22 2027 10:29")       # 29 minutos sem nenhum toque


def calendario_escudos(W=896):
    """Janeiro de 2027 (começa na sexta) com um escudo em cada dia: verde até hoje (22), em traço depois."""
    hoje = 22
    cel = 112
    alt = 66
    gap = (W - 64 - 7 * cel) / 6
    dias = ["D", "S", "T", "Q", "Q", "S", "S"]
    cab = "".join(f"<div style='width:{cel}px;text-align:center;font-size:24px;font-weight:700;color:{MUTED}'>{d}</div>" for d in dias)
    celulas = []
    for k in range(5):
        celulas.append(f"<div style='width:{cel}px;height:{alt}px'></div>")
    for dia in range(1, 32):
        passou = dia <= hoje
        if dia == hoje:
            esc = svg_icone(I_ESCUDO, 42, "#FFFFFF", 2.2)
            fundo, borda, cor_n = BRAND, BRAND, "#FFFFFF"
        elif passou:
            esc = svg_icone(I_ESCUDO, 40, BRAND_DARK, 2.2)
            fundo, borda, cor_n = SOFT, SOFT, BRAND_DEEP
        else:
            esc = ""
            fundo, borda, cor_n = "#FFFFFF", FIO, CINZA_ESCURO
        celulas.append(f"""<div style='width:{cel}px;height:{alt}px;border-radius:18px;background:{fundo};border:2px solid {borda};box-sizing:border-box;position:relative;display:flex;align-items:center;justify-content:flex-end;padding-right:16px'>
  <span style='position:absolute;left:12px;top:50%;transform:translateY(-50%);font-size:22px;font-weight:700;color:{cor_n};font-variant-numeric:tabular-nums'>{dia}</span>{esc}</div>""")
    grade = "".join(celulas)
    return f"""<div style='background:#fff;border-radius:34px;padding:0 32px 30px;box-shadow:0 2px 3px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.35);overflow:hidden'>
  <div style='margin:0 -32px;height:70px;background:{INK};display:flex;align-items:center;justify-content:space-between;padding:0 36px'>
    <span style='font-size:32px;font-weight:700;letter-spacing:.2em;color:#fff'>JANEIRO</span>
    <span style='font-size:28px;font-weight:700;color:{MENTA};font-variant-numeric:tabular-nums'>2027</span></div>
  <div style='display:flex;gap:{gap:.1f}px;margin:16px 0 10px'>{cab}</div>
  <div style='display:flex;flex-wrap:wrap;gap:10px {gap:.1f}px'>{grade}</div></div>"""


def capa_22(T):
    corpo = f"""<div class='eyebrow'>Segurança</div>
<div class='h1' style='font-size:98px'>Seus dados, guardados todo dia.</div>
<div style='margin-top:36px'>{calendario_escudos()}</div>"""
    return capa("papel", corpo, 1, T)


def post_22():
    T = 7
    s = [capa_22(T)]
    p = _c22["pref"]
    nome = "celular-preferencias-copias.png"
    cart = p["cartoes"]["Cópias no servidor"]
    linhas = p["linhas"]

    # 2 · uma cópia por dia
    topo = corte(P22, nome, [cart[1], cart[2], cart[3], linhas[1][4] + 1], 540, raio=26)
    dez = corte(P22, nome, [cart[1], linhas[7][2] - 1, cart[3], linhas[7][4] + 1], 540, raio=26)
    meio = f"""<div style='display:flex;justify-content:center;gap:10px;margin:12px 0'>{''.join(f"<i style='width:9px;height:9px;border-radius:50%;background:{CINZA_ESCURO};display:block'></i>" for _ in range(3))}</div>"""
    lado = f"""<div style='flex:1;padding-top:6px'>
  {sobre('Na lista', BRAND_DEEP, 23)}
  <div style='font-size:28px;line-height:1.34;color:{INK};margin-top:10px'>As cópias dos últimos dias e a do fim de dezembro, novembro e outubro.</div>
  <div class='fio' style='margin:24px 0'></div>
  {sobre('Em cada uma', BRAND_DEEP, 23)}
  <div style='font-size:28px;line-height:1.34;color:{INK};margin-top:10px'>Baixar como arquivo ou Restaurar.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em Preferências</div>
<div class='h3'>Uma cópia por dia, sozinha.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Guardada quando você abre o site, à parte da versão em uso.</div>
<div class='visual' style='margin-top:30px;display:flex;gap:32px;align-items:flex-start'>
  <div style='width:540px;flex:none'>{topo}{meio}{dez}</div>{lado}</div>
{NOTA_TELA}""", 2, T))

    # 3 · restaurar tem volta
    r = _c22["restaurar"]
    md = corte(P22, "celular-restaurar-copia-de-ontem.png", [r["modal"][0], r["modal"][1], r["modal"][2], r["campo"][3] + 14], 760, raio=30)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Restaurar</div>
<div class='h3'>Restaurar tem volta.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Antes de trocar, o site guarda uma cópia de agora. E pede para você digitar RESTAURAR.</div>
<div class='visual' style='margin-top:36px'>{md}{NOTA_TELA}</div>""", 3, T))

    # 4 · o backup completo
    exp = p["cartoes"]["Exportar backup completo"]
    rst = p["cartoes"]["Restaurar de backup"]
    cE = corte(P22, nome, exp[1:5], 760, raio=26)
    cR = corte(P22, nome, rst[1:5], 760, raio=26)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Backup completo</div>
<div class='h3'>E um arquivo com tudo, quando quiser.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Guarde onde preferir. Para voltar, é só restaurar dele.</div>
<div class='visual' style='margin-top:36px'>{cE}<div style='height:22px'></div>{cR}{NOTA_TELA}</div>""", 4, T))

    # 5 · a sessão
    a = _c22["aviso"]
    av = corte(P22, "celular-aviso-30-minutos.png", a["dialogo"], 540, pad=(2, 2, 2, 2), raio=30)
    fatos = f"""<div style='display:flex;gap:18px;margin-top:28px'>
  <div class='card' style='flex:1;padding:22px 26px;display:flex;gap:16px;align-items:center'>{azulejo(I_CLOCK, 64, 32)}<div><div class='big' style='font-size:40px;line-height:1'>30 min</div><div style='font-size:24px;color:{MUTED};margin-top:4px'>sem uso</div></div></div>
  <div class='card' style='flex:1;padding:22px 26px;display:flex;gap:16px;align-items:center'>{azulejo(I_CAL, 64, 32)}<div><div class='big' style='font-size:40px;line-height:1'>24 h</div><div style='font-size:24px;color:{MUTED};margin-top:4px'>mesmo em uso</div></div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Sessão</div>
<div class='h3'>A sessão se fecha sozinha.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Depois de 30 minutos sem uso, com aviso um minuto antes. E a cada 24 horas.</div>
<div class='visual' style='margin-top:32px'>{av}{fatos}{NOTA_TELA}</div>""", 5, T))

    # 6 · mais cuidados
    o = _c22["ocultar"]
    oc = corte(P22, "celular-ocultar-valores.png", [0, 0, 390, 478], 380, raio=26)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Mais cuidados</div>
<div class='h3'>Na tela e no servidor.</div>
<div class='visual' style='margin-top:40px;display:flex;gap:30px;align-items:center'>
  <div style='width:380px;flex:none'>{oc}</div>
  <div style='flex:1'>
    {item(I_EYE, 'Ocultar valores', 'O olho no topo esconde os números, até nos gráficos.', tam_t=31, tam_s=25, pad=20)}
    {item(I_CADEADO, 'Dados criptografados', 'No envio e no armazenamento.', tam_t=31, tam_s=25, pad=20)}
    {item(I_BANCO, 'Sem conexão com o banco', 'Você decide o que entra.', ultimo=True, tam_t=31, tam_s=25, pad=20)}
  </div></div>
{NOTA_TELA}""", 6, T))

    s.append(fechamento_verde("Seus dados, guardados todo dia.",
                              "Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]



# ================================================================ 27/01 · 2026 fechou. Informe o saldo de 31/12.
# Remessas (dólar), relógio em 27/01/2027 10:00, celular, na cópia jb com a atualização de janeiro da carteira em 27/01
# (estado_jb.py, gerar_27). O saldo de 31/12/2026 (US$ 13.380) é o da carteira atualizada em 31/12 na conta de base.
# A PTAX de 31/12/2026 ainda não existe: o câmbio de 2026 fica vazio e o botão PTAX não é tocado.
_c27 = CX["27"]
_ant = {l[0].split(" | ")[0]: l for l in _c27["antes"]["linhas"] if l[0][:4].isdigit()}
_dep = {l[0].split(" | ")[0]: l for l in _c27["depois"]["linhas"] if l[0][:4].isdigit()}
assert _ant["2025"][0] == "2025 | +3,9% | +480,00 | −7,7% | −R$ 5.969,09 | fim 12.960,00"
assert _ant["2026"][0] == "2026 | falta o saldo de 31/12 | falta o saldo de 31/12"
assert _dep["2026"][0] == "2026 | +3,2% | +420,00 | falta o câmbio de 31/12 | fim 13.380,00"
assert _c27["form"]["valores"] == [["2023", "4.120,00", "4,8407", "0,0000"], ["2024", "12.480,00", "6,1917", "0,0000"],
                                   ["2025", "12.960,00", "5,5018", "0,0000"], ["2026", "13.380,00", "", "0,0000"]]
assert _c27["depois"]["fechamentos"]["2026"] == {"valor": 13380, "cambio": 0}
assert "O botão ao lado de cada câmbio busca o PTAX de compra do fecho daquele ano no Banco Central." in _c27["form"]["texto"].replace("\n", " ")
FIM = {2023: D("4120"), 2024: D("12480"), 2025: D("12960"), 2026: D("13380")}
GANHO_26 = FIM[2026] - FIM[2025]
assert GANHO_26 == D("420") and q1(GANHO_26 / FIM[2025] * 100) == D("3.2")
# taxa ao ano pelas datas (como o site): de 01/01 a 31/12/2026, 364 dias
assert q1((D(str((13380 / 12960) ** (365 / 364))) - 1) * 100) == D("3.2")
# 2026 sem envio em dólar (a remessa de 2026 é a do euro)
assert all(r["moeda"] == "EUR" for r in _E.gerar("2027-01-27")[0]["remessas"] if r["data"].startswith("2026"))


def capa_27(T):
    W, H = 896, 600
    def folha(mes, dia, rodape, cor_faixa, tam=208):
        return f"""<div style='position:absolute;inset:0;border-radius:32px;background:#fff;border:2px solid {FIO};box-shadow:0 2px 3px rgba(15,20,16,.05),0 34px 64px -28px rgba(15,20,16,.42);overflow:hidden'>
    <div style='height:90px;background:{cor_faixa};display:flex;align-items:flex-end;justify-content:center;padding-bottom:16px'>
      <span style='font-size:30px;font-weight:700;letter-spacing:.2em;color:#fff'>{mes}</span></div>
    <div class='big' style='text-align:center;font-size:{tam}px;line-height:1;margin-top:22px;letter-spacing:-.07em;color:{INK}'>{dia}</div>
    <div style='text-align:center;font-size:28px;font-weight:600;color:{MUTED};margin-top:6px'>{rodape}</div></div>"""
    argolas = "".join(f"<i style='position:absolute;top:-20px;left:{x}px;width:22px;height:52px;border-radius:11px;background:{CINZA_MEDIO};border:5px solid {SOFT};display:block'></i>" for x in (82, 236))
    tras = f"""<div style='position:absolute;left:520px;top:24px;width:340px;height:400px'>{folha('JANEIRO', '1', 'sexta-feira · 2027', BRAND_DEEP)}{argolas}</div>"""
    frente = f"""<div style='position:absolute;left:48px;top:40px;width:340px;height:400px;transform:rotate(-8deg);transform-origin:50% 50%'>{folha('DEZEMBRO', '31', 'quinta-feira · 2026', INK)}</div>"""
    seta = f"""<svg width='150' height='90' viewBox='0 0 150 90' style='position:absolute;left:378px;top:-6px;overflow:visible'>
    <path d='M8 70 C 40 6, 104 2, 138 40' fill='none' stroke='{BRAND_DEEP}' stroke-width='6' stroke-linecap='round'/>
    <path d='M118 34 L140 44 L142 20' fill='none' stroke='{BRAND_DEEP}' stroke-width='6' stroke-linecap='round' stroke-linejoin='round'/></svg>"""
    fio = f"""<svg width='120' height='110' viewBox='0 0 120 110' style='position:absolute;left:196px;top:404px;overflow:visible'>
    <path d='M28 8 C 10 40, 30 92, 70 104' fill='none' stroke='{INK}' stroke-width='4' stroke-linecap='round'/></svg>"""
    etiqueta = f"""<div style='position:absolute;left:236px;top:452px;width:420px;transform:rotate(-3deg)'>
  <div style='position:relative;background:#fff;border-radius:22px 30px 30px 22px;padding:24px 30px 24px 58px;box-shadow:0 22px 40px -20px rgba(15,20,16,.45);clip-path:polygon(0 50%,9% 0,100% 0,100% 100%,9% 100%)'>
    <i style='position:absolute;left:26px;top:50%;width:18px;height:18px;margin-top:-9px;border-radius:50%;background:{SOFT};display:block'></i>
    <div style='font-size:22px;font-weight:700;letter-spacing:.14em;color:{BRAND_DEEP}'>SALDO EM 31/12</div>
    <div class='big' style='font-size:60px;line-height:1.05;margin-top:6px;color:{INK}'>US$ 13.380</div></div></div>"""
    corpo = f"""<div class='eyebrow'>Investimento no exterior</div>
<div class='h1' style='font-size:96px'>2026 fechou. Informe o saldo de 31/12.</div>
<div style='position:relative;width:{W}px;height:{H}px;margin-top:34px'>{tras}{frente}{seta}{fio}{etiqueta}</div>"""
    return capa("suave", corpo, 1, T)


def post_27():
    T = 7
    s = [capa_27(T)]
    nome_a, nome_f, nome_d = "celular-rendimento-ano-a-ano-antes.png", "celular-editar-fechamentos-2026.png", "celular-rendimento-ano-a-ano-depois.png"

    # 2 · os saldos de 31/12, ano a ano
    marcos = [("31/12/2023", FIM[2023], False), ("31/12/2024", FIM[2024], False), ("31/12/2025", FIM[2025], False), ("31/12/2026", FIM[2026], True)]
    linhas = []
    for i, (d, v, novo) in enumerate(marcos):
        ponto = (f"<i style='width:30px;height:30px;border-radius:50%;background:{BRAND if novo else INK};border:7px solid {SOFT if novo else INK};"
                 f"box-shadow:{'0 0 0 4px ' + BRAND if novo else 'none'};box-sizing:border-box;display:block;position:relative;z-index:2'></i>")
        valor = f"<span class='big' style='font-size:{48 if novo else 42}px;color:{BRAND_DARK if novo else INK}'>US$ {numbr(v, 0)}</span>"
        selo = pilula("anotado em 31/12", SOFT, BRAND_DEEP, 23) if novo else ""
        linhas.append(f"""<div style='display:flex;align-items:center;gap:24px;height:116px;position:relative'>
  <div style='width:30px;display:flex;justify-content:center;flex:none'>{ponto}</div>
  <div style='width:196px;flex:none;font-size:30px;font-weight:700;color:{BRAND_DEEP if novo else INK}'>{d}</div>
  <div style='flex:1'>{valor}</div>{selo}</div>""")
    trilho = f"<div style='position:absolute;left:{44 + 14}px;top:{30 + 58}px;height:{116 * 3}px;border-left:5px solid {CINZA_MEDIO}'></div>"
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O saldo de 31/12</div>
<div class='h2'>No exemplo, US$&nbsp;13.380.</div>
<div class='p' style='margin-top:20px;font-size:35px'>Com o saldo de 31/12, cada ano ganha a sua taxa. Sem ele, só dá para medir o período inteiro.</div>
<div class='visual' style='margin-top:36px'><div class='card' style='padding:30px 44px;position:relative'>{trilho}{''.join(linhas)}</div>
{nota('Exemplo: a carteira em dólar da conta fictícia dos nossos posts, no último dia de cada ano.')}</div>""", 2, T))

    # 3 · em janeiro, 2026 espera o fechamento
    a = _c27["antes"]
    pn = a["painel"]
    cab = corte(P27, nome_a, [pn[0], pn[1], pn[2], a["editar"][3] + 14], 680, raio=24)
    rows = corte(P27, nome_a, [pn[0], _ant["2025"][2] - 2, pn[2], _ant["2026"][4] + 4], 680, raio=24)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em janeiro</div>
<div class='h3'>2026 espera o seu saldo.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Atualize a carteira em 2027: aí 2026 vira um ano fechado e o Rendimento ano a ano pede o 31/12.</div>
<div class='visual' style='margin-top:32px'>{cab}<div style='height:14px'></div>{rows}{NOTA_TELA}</div>""", 3, T))

    # 4 · Editar fechamentos: o saldo de 2026 (sem o câmbio)
    f = _c27["form"]
    tit = corte(P27, nome_f, [0, f["titulo"][1] - 14, 390, f["sub"][3] + 12], 760, raio=24)
    r26 = corte(P27, nome_f, [f["r2026"][0], f["r2026"][1], f["r2026"][2], f["s2026"][3] + 7], 760, raio=24)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Editar fechamentos</div>
<div class='h3'>Digite o saldo de 31/12/2026.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Na moeda, como estava na conta lá fora no último dia do ano.</div>
<div class='visual' style='margin-top:34px'>{tit}<div style='height:16px'></div>{r26}{NOTA_TELA}</div>""", 4, T))

    # 5 · em dólar, o ano já fecha
    dp = _c27["depois"]
    pd_ = dp["painel"]
    rows = corte(P27, nome_d, [pd_[0], _dep["2025"][2] - 2, pd_[2], _dep["2026"][4] + 4], 700, raio=24)
    conta = f"""<div class='card' style='margin-top:24px;padding:24px 34px;display:flex;align-items:center;gap:20px'>
  <div><div style='font-size:22px;font-weight:700;letter-spacing:.1em;color:{MUTED}'>31/12/2025</div><div class='big' style='font-size:40px;margin-top:4px'>US$ 12.960</div></div>
  {svg_icone(I_SETA_DIR, 40, CINZA_ESCURO, 2.4)}
  <div><div style='font-size:22px;font-weight:700;letter-spacing:.1em;color:{MUTED}'>31/12/2026</div><div class='big' style='font-size:40px;margin-top:4px'>US$ 13.380</div></div>
  <div style='margin-left:auto;padding:12px 22px;border-radius:18px;background:{SOFT};text-align:right'>
    <div class='big' style='font-size:40px;color:{BRAND_DARK}'>+3,2%</div><div style='font-size:22px;font-weight:700;color:{BRAND_DEEP}'>+US$ 420</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em dólar</div>
<div class='h3'>2026 rendeu 3,2% em dólar.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Sem envios em dólar no ano. Sem o câmbio, o site mostra 2026 só em US$.</div>
<div class='visual' style='margin-top:32px'>{rows}{conta}{NOTA_TELA}</div>""", 5, T))

    # 6 · em reais: o botão PTAX
    bt = corte(P27, nome_f, f["ptax2026"], 300, pad=(5, 5, 5, 5), raio=40)
    dica = corte(P27, nome_f, f["dica"], 860, pad=(2, 2, 2, 2), raio=24)
    passo = f"""<div style='display:flex;align-items:center;gap:34px;margin-bottom:28px'>
  <div style='width:300px;flex:none'>{bt}</div>
  <div style='flex:1'>{sobre('Toque aqui', BRAND_DEEP, 23)}
    <div style='font-size:29px;line-height:1.34;color:{INK};margin-top:8px'>O site busca a PTAX de compra do último boletim de 2026 e diz a data.</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em reais</div>
<div class='h3'>Para o ano em reais, toque em PTAX.</div>
<div class='visual' style='margin-top:40px'>{passo}{dica}{NOTA_TELA}</div>""", 6, T))

    s.append(fechamento_verde("Feche 2026 lá fora.",
                              "Remessas ao exterior no timtimcash, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 29/01 · Quanto do seu gasto se repete?
# Relatórios, relógio em 29/01/2027 10:00, celular, "Ano atual" e a seta para Ano 2026: "Recorrentes vs pontuais"
# (jan/26 a dez/26) e as listas que um toque nas barras abre.
_c29 = CX["29"]
_rp = _c29["rp"]
REC = [q2(D(str(v))) for v in _rp["rec"]]
PON = [q2(D(str(v))) for v in _rp["pon"]]
TOT_REC, TOT_PON = sum(REC), sum(PON)
assert _c29["periodo"][0] == "Ano 2026" and _rp["labels"][0] == "Jan/26" and _rp["labels"][-1] == "Dez/26"
assert (TOT_REC, TOT_PON, TOT_REC + TOT_PON) == (D("95791.20"), D("6063.50"), D("101854.70"))
assert "R$ 101.854,70" in _c29["diag"]                      # Despesas do período (Ano 2026), no Diagnóstico
assert _rp["pct"] == 94 and round(TOT_REC / (TOT_REC + TOT_PON) * 100) == 94 and q2(D(str(_rp["media"]))) == D("7982.60")
assert q2(TOT_REC / 12) == D("7982.60") and _rp["maior"] == "Aluguel"
assert PON == [D("1390.00"), 0, 0, 0, 0, 0, D("640.00"), 0, D("264.00"), D("276.00"), D("519.00"), D("2974.50")]
PCT_PON = 100 - _rp["pct"]
assert PCT_PON == 6
_t29 = _c29["dez_rec"]["texto"]
for trecho in ["Recorrente\n94%", "Recorrente/mês\nR$ 7.982,60", "Maior compromisso\nAluguel",
               "Entram como recorrentes as despesas lançadas como Fixa ou Parcelada e as que se repetem com a mesma descrição em 3 ou mais meses, com valor na mesma ordem de grandeza."]:
    assert trecho in _t29, trecho
_dr = {l[0].split(" | ")[0]: l for l in _c29["dez_rec"]["det_linhas"]}
assert _dr["AluguelFIXA"][0] == "AluguelFIXA | 10/12 · Casa | R$ 2.300,00"
assert _dr["NotebookPARCELA 2/10"][0] == "NotebookPARCELA 2/10 | 27/12 · Compras | R$ 360,00"
assert _c29["dez_rec"]["det_linhas"][2][0] == "Mercado da VilaREPETIDA | 10/12 · Mercado | R$ 452,30"
assert _c29["jan_pon"]["det_texto"].split("\n")[:2] == ["Pontual · Jan/26", "R$ 1.390,0015% do mês"]
assert [l[0] for l in _c29["jan_pon"]["det_linhas"]] == ["IPVA · parcela única | 20/01 · Impostos e Taxas | R$ 1.180,00",
                                                         "IPTU · 1ª parcela | 12/01 · Impostos e Taxas | R$ 210,00"]
JJD = PON[0] + PON[6] + PON[11]
assert JJD == D("5004.50") and JJD / TOT_PON > D("0.8")      # janeiro, julho e dezembro: mais de 80% do pontual


def anel_29(W=896, H=600):
    cx, cy, r, w = 300, 292, 236, 92
    circ = 2 * math.pi * r
    gap = 7
    rec = circ * 0.94 - gap
    pon = circ * 0.06 - gap
    el = [f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{BRAND}' stroke-width='{w}' stroke-dasharray='{rec:.1f} {circ - rec:.1f}' "
          f"transform='rotate({-90 + 360 * 0.06 + gap / circ * 180:.2f} {cx} {cy})'/>",
          f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{CORAL}' stroke-width='{w}' stroke-dasharray='{pon:.1f} {circ - pon:.1f}' "
          f"transform='rotate({-90 + gap / circ * 180:.2f} {cx} {cy})'/>",
          f"<text x='{cx}' y='{cy + 40}' text-anchor='middle' {FONTE_SVG} font-weight='700' font-size='150' letter-spacing='-8' fill='{INK}'>94%</text>",
          f"<text x='{cx}' y='{cy + 92}' text-anchor='middle' {FONTE_SVG} font-weight='600' font-size='32' fill='{MUTED}'>se repete</text>"]
    leg = f"""<div style='position:absolute;left:600px;top:150px;width:296px'>
  <div style='display:flex;gap:16px;align-items:flex-start'><i style='width:30px;height:30px;border-radius:9px;background:{BRAND};display:block;flex:none;margin-top:8px'></i>
    <div><div class='big' style='font-size:56px;line-height:1'>94%</div><div style='font-size:27px;font-weight:600;color:{MUTED};margin-top:6px;line-height:1.25'>recorrente: volta todo mês</div></div></div>
  <div style='display:flex;gap:16px;align-items:flex-start;margin-top:44px'><i style='width:30px;height:30px;border-radius:9px;background:{CORAL};display:block;flex:none;margin-top:8px'></i>
    <div><div class='big' style='font-size:56px;line-height:1;color:{CORAL_FORTE}'>6%</div><div style='font-size:27px;font-weight:600;color:{MUTED};margin-top:6px;line-height:1.25'>pontual: veio uma vez</div></div></div></div>"""
    return (f"<div style='position:relative;width:{W}px;height:{H}px'><svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='display:block;overflow:visible'>"
            f"{''.join(el)}</svg>{leg}</div>")


def capa_29(T):
    corpo = f"""<div class='eyebrow'>Planejamento</div>
<div class='h1' style='font-size:100px'>Quanto do seu gasto se repete?</div>
<div style='margin-top:52px'>{anel_29()}</div>"""
    return capa("papel", corpo, 1, T)


def post_29():
    T = 6
    s = [capa_29(T)]
    sy = _c29["dez_rec"]["scrollY"]
    pn = _c29["dez_rec"]["painel"]
    nome_r = "celular-recorrentes-vs-pontuais-dez-rec.png"

    # 2 · o painel no Ano 2026
    k = _c29["dez_rec"]
    painel = corte(P29, nome_r, [pn[0], k["kpis"][1] - 12, pn[2], k["grafico"][3] + 8], 600, sy=sy, raio=24)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Relatórios · Ano 2026</div>
<div class='h3'>Em 2026, 94% se repetiu.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Em Recorrentes vs pontuais, a parte cheia de cada barra volta todo mês; a clara veio uma vez.</div>
<div class='visual' style='margin-top:30px'>{painel}{NOTA_TELA}</div>""", 2, T))

    # 3 · o que entra como recorrente
    tipos = [("Fixa", "Lançada como Fixa: aluguel, escola, assinaturas.", _dr["AluguelFIXA"]),
             ("Parcela", "Compra parcelada: o notebook em 10 vezes.", _dr["NotebookPARCELA 2/10"]),
             ("Repetida", "Mesma descrição em 3 ou mais meses: mercado, combustível.", _c29["dez_rec"]["det_linhas"][2])]
    blocos = []
    for i, (t, d, lin) in enumerate(tipos):
        crop = corte(P29, nome_r, [lin[1] - 6, lin[2], lin[3] + 6, lin[4]], 520, sy=sy, raio=18)
        blocos.append(f"""<div style='display:flex;gap:30px;align-items:center;{'' if i == 0 else 'margin-top:26px;'}'>
  <div style='width:520px;flex:none'>{crop}</div>
  <div style='flex:1'><div style='font-size:32px;font-weight:700;letter-spacing:-.02em;color:{INK}'>{t}</div>
    <div style='font-size:25px;line-height:1.3;color:{MUTED};margin-top:4px'>{d}</div></div></div>""")
    regra = corte(P29, nome_r, k["nota"], 860, sy=sy, pad=(10, 12, 10, 12), raio=22)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O que se repete</div>
<div class='h3'>Fixa, parcela e o que se repete.</div>
<div class='visual' style='margin-top:40px'>{''.join(blocos)}
  <div style='margin-top:30px'>{regra}</div>{NOTA_TELA}</div>""", 3, T))

    # 4 · o pontual tem data
    meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
    mx = float(max(PON))
    cols = []
    for m, v in zip(meses, PON):
        h = float(v) / mx * 200
        forte = m in ("jan", "jul", "dez")
        cols.append(f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:10px'>
  <span class='big' style='font-size:{18 if v % 1 else 20}px;color:{CORAL_FORTE if forte else MUTED};white-space:nowrap'>{(numbr(v, 2) if v % 1 else numbr(v, 0)) if v else ''}</span>
  <i style='display:block;width:46px;height:{max(h, 4):.0f}px;border-radius:10px 10px 4px 4px;background:{CORAL if v else CINZA_CLARO}'></i>
  <span style='font-size:22px;font-weight:700;color:{INK if forte else MUTED}'>{m}</span></div>""")
    jan = _c29["jan_pon"]
    lista = corte(P29, "celular-recorrentes-vs-pontuais-jan-pon.png", jan["det"], 700, sy=jan["scrollY"], pad=(0, 0, 0, 0), raio=22)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O pontual</div>
<div class='h3'>O pontual tem data.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Em 2026, R$ 6.063,50 vieram uma vez só. Janeiro, julho e dezembro levaram a maior parte.</div>
<div class='visual' style='margin-top:32px'>
  <div class='card' style='padding:26px 30px 20px'>{sobre('Pontual por mês · 2026 · R$', MUTED, 22, 'margin-bottom:14px')}
    <div style='display:flex;align-items:flex-end;height:270px;gap:4px'>{''.join(cols)}</div></div>
  <div style='margin-top:24px'>{lista}</div>{NOTA_TELA}</div>""", 4, T))

    # 5 · por que separar
    def bloco(cor, fundo, pct, titulo, valor, texto):
        return f"""<div class='card' style='flex:1;padding:30px 30px 34px'>
  <div style='display:flex;align-items:center;gap:14px'><i style='width:26px;height:26px;border-radius:8px;background:{cor};display:block;flex:none'></i>
    <span style='font-size:30px;font-weight:700;letter-spacing:-.02em'>{titulo}</span></div>
  <div class='big' style='font-size:76px;line-height:1;margin-top:18px;color:{INK}'>{pct}</div>
  <div style='font-size:24px;font-weight:600;color:{MUTED};margin-top:6px'>{valor}</div>
  <div style='margin-top:22px;padding:20px 22px;border-radius:18px;background:{fundo};font-size:27px;line-height:1.36;color:{INK}'>{texto}</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Por que separar</div>
<div class='h3'>Cada parte pede um cuidado.</div>
<div class='visual' style='margin-top:40px;display:flex;gap:22px'>
  {bloco(BRAND, SOFT, '94%', 'Recorrente', 'R$ 7.982,60 por mês', 'Entra no plano do mês. E um ajuste nele vale 12 vezes: R$ 50 a menos por mês são R$ 600 no ano.')}
  {bloco(CORAL, CORAL_PALIDO, '6%', 'Pontual', 'R$ 6.063,50 no ano', 'Não vem todo mês, mas vem. Separe antes: no exemplo, janeiro, julho e dezembro.')}
</div>{nota('Exemplo: a conta fictícia dos nossos posts, despesas pagas de janeiro a dezembro de 2026.')}""", 5, T))

    s.append(fechamento_verde("Veja o que se repete no seu ano.",
                              "Relatórios no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]


POSTS = {
    P16: post_16,
    P20: post_20,
    P22: post_22,
    P27: post_27,
    P29: post_29,
}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    if so:
        so = [p for p in POSTS if any(p.startswith(x) or x in p for x in so)]
    renderizar(POSTS, so=so)
