# -*- coding: utf-8 -*-
"""Carrosséis da equipe fa · fevereiro de 2027 (01, 04, 06, 11 e 13/02), no formato aprovado de outubro a dezembro
(J/kit/carrossel.py; modelos em novdez/equipes/dc1/posts.py e dc2/posts.py).

Telas reais: build 2026-10-19.5, capturadas por captura.py na cópia da conta (a pasta copiada de J/base_app, com o
estado.py igual ao da base; no 04/02, a variante "sem-remessas-usd" de variantes.py, que a importação devolve à base) e
guardadas em J/saida/<pasta>/telas/. As caixas (px CSS) e os textos lidos em cada tela ficam em caixas.json.
Cada número dos slides é conferido por assert neste arquivo: contra caixas.json (o que a tela mostrou), contra a conta
(estado.py da cópia) e contra J/FATOS.md.

python3 posts.py                       renderiza os 5 posts e confere o layout
python3 posts.py <pasta> [<pasta>...]  só os escolhidos
"""
import os, re, sys, json, calendar
from datetime import date
from decimal import Decimal as D, ROUND_HALF_UP

J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, J + "/kit")
from carrossel import *   # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl, sem_quebra...)
sys.path.insert(0, os.path.join(AQUI, "ap" "p"))     # a pasta da cópia da conta
import estado as CONTA
sys.path.insert(0, AQUI)
from planilha_0402 import CAB as CAB_MODELO, LINHAS as LINHAS_PLANILHA

CX = json.load(open(os.path.join(AQUI, "caixas.json"), encoding="utf-8"))

P01 = "2027-02-01_fevereiro-do-seu-dinheiro"
P04 = "2027-02-04_remessas-da-planilha-para-o-site"
P06 = "2027-02-06_gasto-anual-vira-mensal"
P11 = "2027-02-11_ir-saude-e-educacao-o-que-deduz"
P13 = "2027-02-13_transferencia-nao-e-gasto"

NBSP = " "
MENOS = "−"


def q2(v):
    return D(v).quantize(D("0.01"), ROUND_HALF_UP)


def pct1(v):
    return num(q2(v * 100).quantize(D("0.1"), ROUND_HALF_UP), 1) + "%"


def tela(pasta, nome):
    caminho = os.path.join(SAIDA, pasta, "telas", nome)
    assert os.path.isfile(caminho), caminho
    return caminho


def rec(pasta, nome, y0, y1, largura, x0=0, x1=None, esc=3, rolagem=0, raio=24):
    """Recorte por coordenadas CSS da janela (as das caixas), convertidas para pixels da imagem (escala da captura)."""
    return recorte(tela(pasta, nome), int((y0 - rolagem) * esc), int((y1 - rolagem) * esc), largura=largura,
                   x0=int(x0 * esc), x1=int(x1 * esc) if x1 is not None else None, raio=raio)


def texto(chave):
    """O texto lido na tela (espaço inseparável trocado por espaço comum, para conferir)."""
    return CX[chave]["_texto"].replace(NBSP, " ")


def caixa(chave, texto):
    c = CX[chave][texto]
    assert c, (chave, texto)
    return c


def resumo(chave):
    """(quantidade, soma) do resumo da lista de Transações ("N transações · N pagas · 0 pendentes · somam R$ X")."""
    m = re.fullmatch(r"(\d+) transaç(?:ão|ões) · \d+ pagas? · 0 pendentes · somam R\$ ([\d.]+,\d\d)", CX[chave]["_resumo"])
    assert m, CX[chave]["_resumo"]
    return int(m.group(1)), D(m.group(2).replace(".", "").replace(",", "."))


def sem_quebra_fa(html):
    """sem_quebra do kit; e mais: número junto da lei e do artigo; "US$" e "€" junto do valor."""
    html = sem_quebra(html)
    html = re.sub(r"\b(Lei|Decreto|art\.|IN RFB|IN SRF|Portaria MGI|nº) (\d)", lambda m: m.group(1).replace(" ", NBSP) + NBSP + m.group(2), html)
    html = html.replace("1/12 ", "1/12" + NBSP)
    return html


EXTRA_F = EXTRA + f"""<style>
.tab{{font-variant-numeric:tabular-nums}}
.rs{{font-size:22px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTED}}}
.pilula{{display:inline-flex;align-items:center;gap:12px;background:{SOFT};color:{BRAND_DEEP};font-size:27px;font-weight:700;padding:14px 26px;border-radius:999px}}
.leg{{display:flex;align-items:center;gap:12px;font-size:27px;font-weight:700;white-space:nowrap}}
.leg i{{display:block;flex:none}}
.nota{{text-wrap:balance}}
.selo{{display:inline-flex;align-items:center;gap:10px;font-size:25px;font-weight:700;padding:10px 20px;border-radius:999px}}
.selo.sim{{background:{SOFT};color:{BRAND_DEEP}}}
.selo.nao{{background:#FBE7DF;color:{CORAL_FORTE}}}
</style>"""


def topo(sobre, titulo, apoio=None, cls="h2", estilo_t="", estilo_p=""):
    p = f"<div class='p' style='{estilo_p}'>{apoio}</div>" if apoio else ""
    return f"<div class='eyebrow'>{sobre}</div><div class='{cls}' style='{estilo_t}'>{titulo}</div>{p}"


def pilula(ip, txt):
    return f"<span class='pilula'>{svg_icone(ip, 30, BRAND_DEEP, 2.2)}{txt}</span>"


def selo(sim, txt):
    ic = svg_icone(I_CHECK if sim else I_X, 26, BRAND_DEEP if sim else CORAL_FORTE, 2.8)
    return f"<span class='selo {'sim' if sim else 'nao'}'>{ic}{txt}</span>"


def dois(esq, dir_, larg_dir, gap=40):
    """Duas colunas: texto à esquerda, recorte de tela à direita (para telas altas do celular)."""
    return (f"<div style='display:flex;gap:{gap}px;align-items:center'><div style='flex:1;min-width:0'>{esq}</div>"
            f"<div style='flex:none;width:{larg_dir}px'>{dir_}</div></div>")


NOTA_TELA_P = "<div class='nota' style='text-align:center;font-size:21px;margin-top:14px'>Tela real do timtimcash, com dados de exemplo.</div>"

# ícones de traço próprios (24 × 24, pontas redondas)
I_CARRO = ('<path d="M4 15.6v-3.3l1.9-4.6a2 2 0 0 1 1.8-1.2h8.6a2 2 0 0 1 1.8 1.2l1.9 4.6v3.3"/>'
           '<path d="M3.5 15.6h17M4.6 12.2h14.8"/><circle cx="7.8" cy="17.6" r="1.6"/><circle cx="16.2" cy="17.6" r="1.6"/>')
I_LIVRO = '<path d="M12 6.6C10 5.1 7 4.6 4 5.1v13c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5v-13c-3-.5-6 0-8 1.5z"/><path d="M12 6.6v13"/>'
I_BANCO = '<path d="M12 3.5 20.5 8h-17z"/><path d="M5 11v6.5M9.7 11v6.5M14.3 11v6.5M19 11v6.5"/><path d="M3.5 20.5h17"/>'
I_SETA = '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>'
I_SOBE = '<path d="M12 15.5V4M7.5 8.5 12 4l4.5 4.5"/><path d="M4.5 15v4.5h15V15"/>'
I_DESCE = '<path d="M12 4v11.5M7.5 11 12 15.5l4.5-4.5"/><path d="M4.5 15v4.5h15V15"/>'
I_MARCA_SALVAR = '<path d="M7 3.5h10a1 1 0 0 1 1 1V21l-6-4-6 4V4.5a1 1 0 0 1 1-1z"/>'
I_COFRE = '<rect x="3.5" y="5" width="17" height="14.5" rx="2.5"/><circle cx="12" cy="12.2" r="3.4"/><path d="M12 8.8v1.2M12 14.4v1.2M7 19.5v1.5M17 19.5v1.5"/>'
I_ENVELOPE = '<rect x="3" y="5.5" width="18" height="13" rx="2.2"/><path d="M3.6 6.5 12 13l8.4-6.5"/>'


# ============================================================================ calendário (o mesmo desenho de 01/11 e 02/12)
SEMANA = ["D", "S", "T", "Q", "Q", "S", "S"]


def grade_mes(ano, mes, marcas, cel=92, bola=76, fs=34, cab=True):
    """Grade de um mês que começa no domingo. marcas: {dia: 'verde' | 'anel' | 'coral' | 'tinta'}."""
    off = (date(ano, mes, 1).weekday() + 1) % 7          # domingo = coluna 0
    ndias = calendar.monthrange(ano, mes)[1]
    cels = []
    if cab:
        for s in SEMANA:
            cels.append(f"<div style='height:{int(fs * 1.5)}px;display:flex;align-items:center;justify-content:center;"
                        f"font-size:{int(fs * .74)}px;font-weight:700;color:{MUTED};letter-spacing:.04em'>{s}</div>")
    for _ in range(off):
        cels.append(f"<div style='height:{cel}px'></div>")
    anel = max(4, bola // 15)
    for d in range(1, ndias + 1):
        m = marcas.get(d)
        if m == "coral":
            est, peso = f"background:#fff;color:{CORAL_TXT};box-shadow:inset 0 0 0 {anel}px {CORAL}", 700
        elif m == "anel":
            est, peso = f"background:#fff;color:{BRAND_DARK};box-shadow:inset 0 0 0 {anel}px {BRAND}", 700
        elif m == "verde":
            est, peso = f"background:{BRAND};color:#fff;box-shadow:0 0 0 {max(6, bola // 10)}px {SOFT}", 700
        elif m == "tinta":
            est, peso = f"background:{INK};color:#fff", 700
        else:
            est, peso = f"color:{INK}", 500
        cels.append(f"<div style='display:flex;align-items:center;justify-content:center;height:{cel}px'>"
                    f"<span style='width:{bola}px;height:{bola}px;border-radius:50%;display:flex;align-items:center;justify-content:center;"
                    f"font-size:{fs}px;font-weight:{peso};font-variant-numeric:tabular-nums;{est}'>{d}</span></div>")
    return f"<div style='display:grid;grid-template-columns:repeat(7,1fr);row-gap:2px'>{''.join(cels)}</div>"


def argolas(cor=INK):
    return "".join(f"<i style='position:absolute;top:-17px;left:{x};width:18px;height:46px;border-radius:9px;background:{cor};display:block'></i>"
                   for x in ("21%", "77%"))


def leg_bola(estilo, txt, cor=INK):
    return f"<span class='leg' style='color:{cor}'><i style='width:28px;height:28px;border-radius:50%;{estilo}'></i>{txt}</span>"


# ============================================================================ 01/02 · Fevereiro do seu dinheiro
# Calendário de 2027 (FATOS 5a.4, 6.1 e 7.4): 01/02 é segunda e 28/02 é domingo (4 semanas exatas); Carnaval em 08 e 09
# (segunda e terça); Cinzas em 10/02 (quarta); 26/02 (sexta) é o último dia útil, prazo do comprovante de rendimentos.
assert date(2027, 2, 1).weekday() == 0 and date(2027, 2, 28).weekday() == 6 and calendar.monthrange(2027, 2)[1] == 28
assert [date(2027, 2, d).weekday() for d in (8, 9, 10, 26, 27)] == [0, 1, 2, 4, 5]
# Pendentes em 01/02/2027 (tela real): A pagar R$ 4.444,80 em 7 transações; A receber R$ 9.960 (o salário de 05/02).
T01 = texto("0102_pendentes")
assert "A pagar | R$ | 4.444 | ,80 | 7 transações | A receber | R$ | 9.960 | Total pendente | 8 | Nada vencido. Tudo dentro do prazo." in T01
DIA10 = [("Aluguel", D("2300.00")), ("Escola", D("1450.00")), ("IPTU 2027, 1ª parcela", D("215.00"))]
for trecho in ("10/02/2027 | Editar | Excluir | Aluguel | FIXA·Casa·Conta corrente | −R$ 2.300,00",
               "Escola | FIXA·Educação·Conta corrente | −R$ 1.450,00", "IPTU 2027 · 1ª parcela | Impostos e Taxas·Conta corrente | −R$ 215,00"):
    assert trecho in T01, trecho
TOTAL_DIA10 = sum(v for _, v in DIA10)
assert TOTAL_DIA10 == D("3965.00")
A_PAGAR_FEV = TOTAL_DIA10 + D("55.90") + D("21.90") + D("42.00") + D("360.00")      # vídeo, música, nuvem e Notebook (4/10)
assert A_PAGAR_FEV == D("4444.80")
_e0102 = CONTA.gerar("2027-02-01")[0]
assert sum(D(str(t["valor"])) for t in _e0102["txs"] if t["tipo"] == "despesa" and not t["conciliado"] and t["data"].startswith("2027-02")) == A_PAGAR_FEV
MERCADO = D(str(_e0102["budgets"]["Mercado"]))
assert MERCADO == D("2000") and MERCADO / 4 == D("500")


def capa_fevereiro(T):
    cal = f"""<div class='card' style='position:relative;margin-top:50px;padding:0;overflow:visible'>
  {argolas()}
  <div style='height:30px;border-radius:28px 28px 0 0;background:{FIO}'></div>
  <div style='padding:10px 30px 2px'>{grade_mes(2027, 2, {8: 'coral', 9: 'coral', 10: 'verde', 26: 'anel'}, cel=82, bola=70, fs=33)}</div>
  <div style='display:flex;flex-wrap:wrap;justify-content:center;column-gap:48px;row-gap:16px;padding:24px 30px 30px;border-top:2px solid {FIO};margin:8px 34px 0'>
    {leg_bola(f'background:#fff;box-shadow:inset 0 0 0 5px {CORAL}', 'Carnaval', CORAL_TXT)}
    {leg_bola(f'background:{BRAND}', 'Dia 10, no exemplo', BRAND_DARK)}
    {leg_bola(f'background:#fff;box-shadow:inset 0 0 0 5px {BRAND}', 'Prazo do informe de rendimentos', BRAND_DARK)}
  </div>
</div>"""
    corpo = f"""<div class='eyebrow'>Calendário</div>
<div class='h1' style='font-size:100px'>Fevereiro do seu dinheiro.</div>{cal}"""
    return capa("papel", EXTRA_F + corpo, 1, T)


def v_quatro_semanas():
    """As 4 semanas exatas de fevereiro de 2027 (segunda a domingo) e o limite do mercado dividido por 4."""
    linhas = []
    for k in range(4):
        dias = []
        for j in range(7):
            d = 7 * k + j + 1
            fim = j >= 5
            dias.append(f"<span style='width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center;"
                        f"font-size:23px;font-weight:{600 if not fim else 500};font-variant-numeric:tabular-nums;"
                        f"background:{SOFT if not fim else BG};color:{BRAND_DEEP if not fim else MUTED};"
                        f"{'box-shadow:inset 0 0 0 2px ' + FIO + ';' if fim else ''}'>{d}</span>")
        borda = f"border-top:2px solid {FIO};" if k else ""
        linhas.append(f"""<div style='display:flex;align-items:center;gap:22px;padding:18px 0;{borda}'>
  <div style='width:150px;flex:none'><div style='font-size:30px;font-weight:700;letter-spacing:-.02em'>Semana {k + 1}</div>
    <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:2px'>{7 * k + 1:02d} a {7 * k + 7:02d}/02</div></div>
  <div style='display:flex;gap:8px'>{''.join(dias)}</div>
  <div class='tab' style='margin-left:auto;font-size:38px;font-weight:700;letter-spacing:-.03em;color:{BRAND_DARK}'>R$ 500</div></div>""")
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:26px 40px 22px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding-bottom:8px'>
    <span class='rs'>Mercado · limite de R$ 2.000 no mês</span><span class='rs' style='color:{BRAND_DARK}'>÷ 4</span></div>
  {''.join(linhas)}
</div>
<div class='nota'>Fevereiro de 2027 começa numa segunda e termina num domingo. Limite do mercado da conta de exemplo, em Orçamentos.</div></div>"""


def v_envelope():
    W, H = 620, 360
    env = f"""<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='display:block;overflow:visible'>
  <defs><filter id='se' x='-10%' y='-10%' width='120%' height='140%'><feDropShadow dx='0' dy='20' stdDeviation='20' flood-color='#0F1410' flood-opacity='.16'/></filter></defs>
  <rect x='2' y='2' width='{W - 4}' height='{H - 4}' rx='30' fill='#fff' stroke='{FIO}' stroke-width='3' filter='url(#se)'/>
  <path d='M14 22 L{W / 2} {H * .52} L{W - 14} 22' fill='none' stroke='{CORAL_CLARO}' stroke-width='5' stroke-linejoin='round' stroke-linecap='round'/>
  <path d='M14 {H - 18} L{W * .38} {H * .5}M{W - 14} {H - 18} L{W * .62} {H * .5}' fill='none' stroke='{FIO}' stroke-width='4' stroke-linecap='round'/>
</svg>"""
    return f"""<div class='visual' style='margin-top:46px;display:flex;justify-content:center'>
  <div style='position:relative;width:{W}px;height:{H}px'>{env}
    <div style='position:absolute;left:0;right:0;top:{H * .55:.0f}px;text-align:center'>
      <div class='rs' style='color:{CORAL_TXT}'>Carteira do Carnaval</div>
      <div class='big' style='font-size:88px;line-height:1.05;color:{INK}'>R$ 500</div></div>
  </div></div>
<div style='margin-top:40px;text-align:center'>{pilula(I_CAL, 'Sexta (05/02): o envelope no timtimcash.')}</div>
<div class='nota' style='text-align:center'>Carnaval não é feriado nacional: no governo federal, é ponto facultativo (regra de 2026, Portaria MGI 11.460/2025). Feriado só onde a lei local disser.</div>"""


def v_dia10():
    W = 816
    cores = [CORAL_FORTE, CORAL, AMBER]
    segs = "".join(f"<div style='width:{float(v / TOTAL_DIA10) * W - 4:.1f}px;height:70px;background:{c};"
                   f"border-radius:{'18px 5px 5px 18px' if i == 0 else ('5px 18px 18px 5px' if i == 2 else '5px')}'></div>"
                   for i, ((_, v), c) in enumerate(zip(DIA10, cores)))
    legs = "".join(f"""<div style='display:flex;align-items:center;gap:14px;padding:14px 0;{"border-top:2px solid " + FIO + ";" if i else ""}'>
  <i style='width:22px;height:22px;border-radius:6px;background:{c};display:block;flex:none'></i>
  <span style='font-size:30px;font-weight:600'>{n}</span>
  <span class='tab' style='margin-left:auto;font-size:32px;font-weight:700;color:{CORAL_TXT}'>{brl(v, cent=False)}</span></div>"""
                   for i, ((n, v), c) in enumerate(zip(DIA10, cores)))
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:34px 40px 22px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span class='rs'>Quarta, 10/02 · no exemplo</span>
    <span class='big' style='font-size:84px;line-height:1;color:{CORAL_FORTE}'>R$ 3.965</span></div>
  <div style='display:flex;gap:4px;margin-top:24px'>{segs}</div>
  <div style='margin-top:14px'>{legs}</div>
</div>
<div style='margin-top:30px'>{pilula(I_CAL, 'Deixe o saldo pronto antes da folia.')}</div></div>"""


def v_informe():
    dias = []
    for d, sem in zip(range(22, 29), ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]):
        alvo = d == 26
        fim = d >= 27
        est = (f"background:{BRAND};color:#fff;box-shadow:0 0 0 7px {SOFT}" if alvo
               else (f"background:{BG};color:{MUTED};box-shadow:inset 0 0 0 2px {FIO}" if fim else f"background:#fff;color:{INK};box-shadow:inset 0 0 0 2px {FIO}"))
        dias.append(f"""<div style='display:flex;flex-direction:column;align-items:center;gap:10px'>
  <span style='font-size:22px;font-weight:700;letter-spacing:.06em;color:{BRAND_DARK if alvo else MUTED}'>{sem}</span>
  <span class='tab' style='width:86px;height:86px;border-radius:24px;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:{700 if alvo else 500};{est}'>{d}</span></div>""")
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:34px 40px 30px'>
  <div style='display:flex;align-items:center;gap:26px'>
    {azulejo(I_ENVELOPE, 96, 48)}
    <div><div class='big' style='font-size:88px;line-height:1;color:{BRAND_DARK}'>26/02</div>
      <div style='font-size:30px;font-weight:600;color:{INK};margin-top:6px'>sexta, o último dia útil de fevereiro</div></div></div>
  <div style='display:flex;justify-content:space-between;margin-top:32px;padding-top:26px;border-top:2px solid {FIO}'>{''.join(dias)}</div>
</div>
<div style='margin-top:30px'>{pilula(I_CAL, 'Quinta (11/02): saúde e educação no IR.')}</div>
<div class='nota'>Regras da Receita Federal para o comprovante de rendimentos: IN RFB 2.060/2021, art. 3º, e IN SRF 698/2006, art. 2º, I.</div></div>"""


def post_fevereiro():
    T = 7
    s = [capa_fevereiro(T)]

    s.append(slide("light", EXTRA_F + topo(
        "01 a 28/02 · O mês mais curto", "28 dias, as mesmas contas.",
        "Aluguel, escola e assinaturas vêm inteiros. O resto cabe em 4 semanas exatas.",
        estilo_p="font-size:36px;margin-top:22px") + v_quatro_semanas(), 2, T))

    s.append(slide("light", EXTRA_F + topo(
        "08 e 09/02 · Carnaval", "Separe o dinheiro da folia.",
        "Uma carteira só para o Carnaval: quando acabar, acabou.",
        estilo_p="font-size:36px;margin-top:22px") + v_envelope(), 3, T))

    s.append(slide("light", EXTRA_F + topo(
        "10/02 · Quarta-feira de Cinzas", "As contas do dia 10 vêm logo depois.",
        "No exemplo, aluguel, escola e a 1ª parcela do IPTU vencem juntos.",
        estilo_p="font-size:36px;margin-top:22px") + v_dia10(), 4, T))

    s.append(slide("light", EXTRA_F + topo(
        "Até 26/02 · Imposto de renda", "O informe de rendimentos chega.",
        "Empresa e banco entregam até o último dia útil de fevereiro.",
        estilo_p="font-size:36px;margin-top:22px") + v_informe(), 5, T))

    y0 = caixa("0102_pendentes", "A vencer")["y"] - 14
    y1 = caixa("0102_pendentes", "IPTU 2027")["y"] + 46
    crop = rec(P01, "celular-pendentes-01-02.png", y0, y1, 600, x0=14, x1=376)
    s.append(slide("light", EXTRA_F + topo(
        "No timtimcash", "O mês inteiro, já com data.",
        "Em Pendentes: R$ 4.444,80 a pagar em 7 contas, e o salário no dia 5.", cls="h3",
        estilo_p="font-size:33px;margin-top:16px") + f"<div class='visual' style='margin-top:28px'>{crop}{NOTA_TELA}</div>", 6, T))

    s.append(fechamento_verde("Seu fevereiro, com data marcada.",
        "Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_fa(h) for h in s]


# ============================================================================ 04/02 · Remessas: da planilha para o site
REM = [(d, D(v.replace(".", "").replace(",", ".")), D(t.replace(".", "").replace(",", "."))) for d, _, _, v, _, _, t, _ in LINHAS_PLANILHA]
CAMBIOS = [t / v for _, v, t in REM]
assert [str(q2(c)) for c in CAMBIOS] == ["4.90", "5.00", "5.10"]
assert sum(v for _, v, _ in REM) == D("12000") and sum(t for _, _, t in REM) == D("60000")
assert tuple(CAB_MODELO) == ("Data", "Conta de origem", "Conta de destino", "Valor em moeda", "Valor em R$", "IOF", "TOTAL", "Moeda")
_rev = texto("0402_revisao")
for trecho in ("Revisar importação | 3 linhas lidas de minhas-remessas.csv · confira antes de confirmar",
               "3 linhas ficam vinculadas às transferências que já existem no timtimcash, sem mudar o saldo.",
               "Importar 3 remessas"):
    assert trecho in _rev, trecho
_dep = texto("0402_depois")
for trecho in ("Remetido | US$ 12.000,00 | 3 remessas · desde jul/23", "Câmbio médio efetivo | R$ 5,0000 | com IOF · sem IOF R$ 5,0000",
               "aportes 4.000,00 · a R$ 4,90 · fim 4.120,00", "aportes 8.000,00 · a R$ 5,05 · fim 12.480,00", "fim 12.960,00",
               "2026 | +3,2% | +420,00 | falta o câmbio de 31/12 | fim 13.380,00"):      # base de 29/01 em diante: 2026 sem câmbio
    assert trecho in _dep, trecho
_mod = texto("0402_modal")
assert "As cinco primeiras são obrigatórias" in _mod and "Sem a coluna Moeda, tudo entra como dólar." in _mod and "Aceita .xlsx, .xls e .csv" in _mod


def capa_remessas(T):
    """Uma planilha desenhada cujas linhas viram cartões de remessa (com o câmbio efetivo que o site calcula)."""
    LS, LH, TOPO = 430, 70, 46            # largura da planilha, altura da linha, faixa das letras
    cols = [("Data", 168), ("US$", 106), ("Total R$", 156)]
    letras = "".join(f"<div style='width:{w}px;height:{TOPO}px;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700;color:{MUTED};"
                     f"border-left:2px solid {FIO}'>{l}</div>" for l, (_, w) in zip("ABC", cols))
    cab = "".join(f"<div style='width:{w}px;height:{LH}px;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;color:#fff;"
                  f"border-left:2px solid rgba(255,255,255,.35)'>{n}</div>" for n, w in cols)
    linhas = []
    for i, (d, v, t) in enumerate(REM):
        cel = [d, num(v, 0), num(t, 0)]
        linhas.append("<div style='display:flex;border-top:2px solid " + FIO + "'>" + "".join(
            f"<div class='tab' style='width:{w}px;height:{LH}px;display:flex;align-items:center;justify-content:{'flex-start' if j == 0 else 'flex-end'};"
            f"padding:0 16px;font-size:25px;font-weight:600;color:{INK};border-left:2px solid {FIO}'>{c}</div>"
            for j, (c, (_, w)) in enumerate(zip(cel, cols))) + "</div>")
    vazia = "<div style='display:flex;border-top:2px solid " + FIO + "'>" + "".join(
        f"<div style='width:{w}px;height:{LH}px;border-left:2px solid {FIO}'></div>" for _, w in cols) + "</div>"
    planilha = f"""<div class='sombra' style='position:absolute;left:0;top:30px;width:{LS}px;border-radius:22px;overflow:hidden;background:#fff;border:2px solid {FIO}'>
  <div style='display:flex;background:{BG}'>{letras}</div>
  <div style='display:flex;background:{BRAND}'>{cab}</div>
  {''.join(linhas)}{vazia}
</div>"""
    CW, CH, CG, CX0 = 330, 120, 26, 566
    cartoes, setas = [], []
    for i, ((d, v, t), c) in enumerate(zip(REM, CAMBIOS)):
        y = i * (CH + CG)
        cartoes.append(f"""<div class='sombra' style='position:absolute;left:{CX0}px;top:{y}px;width:{CW}px;height:{CH}px;border-radius:24px;background:#fff;
  border:2px solid {FIO};display:flex;align-items:center;gap:18px;padding:0 22px'>
  {azulejo(I_GLOBO, 64, 32)}
  <div><div class='tab' style='font-size:38px;font-weight:700;letter-spacing:-.03em;line-height:1.05'>US$ 4.000</div>
    <div class='tab' style='font-size:23px;font-weight:600;color:{MUTED};margin-top:6px;white-space:nowrap'>câmbio <b style='color:{BRAND_DARK}'>R$ {num(c, 2)}</b></div></div></div>""")
        ya = 30 + TOPO + LH + i * LH + LH / 2 + 2 * (i + 1)
        yb = y + CH / 2
        setas.append(f"<path d='M{LS + 10} {ya:.0f} C {LS + 70} {ya:.0f}, {CX0 - 80} {yb:.0f}, {CX0 - 16} {yb:.0f}' fill='none' stroke='{BRAND}' stroke-width='5' stroke-linecap='round'/>"
                     f"<path d='M{CX0 - 30} {yb - 11:.0f} L{CX0 - 14} {yb:.0f} L{CX0 - 30} {yb + 11:.0f}' fill='none' stroke='{BRAND}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/>")
    alt = 3 * CH + 2 * CG
    svg = f"<svg width='896' height='{alt + 60}' style='position:absolute;left:0;top:0;overflow:visible'>{''.join(setas)}</svg>"
    vis = f"<div class='visual' style='position:relative;height:{max(alt, 30 + TOPO + 5 * LH + 10) + 10}px;margin-top:58px'>{planilha}{svg}{''.join(cartoes)}</div>"
    corpo = f"""<div class='eyebrow'>Investimento no exterior</div>
<div class='h1' style='font-size:94px'>Anos de remessas numa planilha? Traga todas.</div>{vis}"""
    return capa("suave", EXTRA_F + corpo, 1, T)


def v_menu_remessas():
    c = CX["0402_menu_pc"]
    m, bt, ac = c["menu"], c["botao"], c["acoes"]
    x0, x1 = ac[0] - 18, bt[0] + bt[2] + 30
    y0, y1 = ac[1] - 22, m[1] + m[3] + 26
    crop = rec(P04, "computador-remessas-menu-04-02.png", y0, y1, 760, x0=x0, x1=x1, esc=2)

    def item(ip, t, s):
        return f"""<div style='display:flex;gap:22px;align-items:flex-start;padding:18px 0'>{azulejo(ip, 66, 32)}
  <div><div style='font-size:31px;font-weight:700;letter-spacing:-.02em'>{t}</div><div style='font-size:26px;color:{MUTED};margin-top:6px;line-height:1.35'>{s}</div></div></div>"""
    return f"""<div class='visual' style='margin-top:40px'>{crop}{NOTA_TELA}
  <div class='card' style='margin-top:24px;padding:4px 36px'>
    {item(I_DESCE, '“Baixar planilha modelo”', 'Um Excel com as colunas certas e uma aba que explica cada uma.')}
    <div class='fio'></div>
    {item(I_SOBE, '“Importar planilha”', 'Aceita .xlsx, .xls e .csv, inclusive a planilha que você já usa.')}
  </div></div>"""


def v_colunas():
    ex = LINHAS_PLANILHA[0]
    obrig = {"Data", "Conta de origem", "Conta de destino", "Valor em moeda", "TOTAL"}
    ordem = ["Data", "Conta de origem", "Conta de destino", "Valor em moeda", "TOTAL", "Valor em R$", "IOF", "Moeda"]
    valor = dict(zip(CAB_MODELO, ex))
    linhas = []
    for i, col in enumerate(ordem):
        ob = col in obrig
        v = valor[col] or "em branco"
        vazio = not valor[col]
        borda = f"border-top:2px solid {FIO};" if i else ""
        linhas.append(f"""<div style='display:flex;align-items:stretch;{borda}'>
  <div style='width:300px;flex:none;padding:16px 22px;background:{BRAND if ob else BG};color:{'#fff' if ob else MUTED};font-size:27px;font-weight:700'>{col}</div>
  <div class='tab' style='flex:1;padding:16px 22px;font-size:27px;font-weight:{500 if vazio else 600};color:{MUTED if vazio else INK};{"font-style:italic;" if vazio else ""}'>{v}</div>
  <div style='width:190px;flex:none;display:flex;align-items:center;justify-content:flex-end;padding-right:20px;font-size:21px;font-weight:700;letter-spacing:.1em;
    color:{BRAND_DARK if ob else MUTED}'>{'OBRIGATÓRIA' if ob else 'OPCIONAL'}</div></div>""")
    if i == 4:
        pass
    return f"""<div class='visual' style='margin-top:36px'><div class='sombra' style='border-radius:24px;overflow:hidden;background:#fff;border:2px solid {FIO}'>
  {''.join(linhas)}</div>
<div class='nota'>No lugar do TOTAL, dá para pôr o Valor em R$ e o IOF: o timtimcash soma. Moeda em branco entra como dólar. Exemplo: a 1ª remessa da conta de exemplo.</div></div>"""


def post_remessas():
    T = 6
    s = [capa_remessas(T)]

    s.append(slide("light", EXTRA_F + topo(
        "Em Remessas", "Comece pelo menu “Mais ações”.", cls="h3") + v_menu_remessas(), 2, T))

    s.append(slide("light", EXTRA_F + topo(
        "Uma linha por remessa", "5 colunas obrigatórias.",
        "Faltando as contas, dá para escolher na revisão.", estilo_p="font-size:36px;margin-top:20px") + v_colunas(), 3, T))

    c = CX["0402_revisao_celular"]
    l1 = c["linhas"][0]
    y0 = l1[1] - 6
    y1 = caixa("0402_revisao_celular", "vincula à transferência")["y"] - 6       # até o câmbio efetivo da 1ª linha
    crop = rec(P04, "celular-revisar-importacao-04-02.png", y0, y1, 640, x0=10, x1=380)
    chips = "".join(f"<div class='tab' style='flex:1;text-align:center;padding:14px 10px;border-radius:18px;background:#fff;border:2px solid {FIO}'>"
                    f"<div style='font-size:22px;font-weight:600;color:{MUTED}'>{d}</div><div style='font-size:32px;font-weight:700;color:{BRAND_DARK};margin-top:2px'>R$ {num(cb, 2)}</div></div>"
                    for (d, _, _), cb in zip(REM, CAMBIOS))
    s.append(slide("light", EXTRA_F + topo(
        "Antes de importar", "Você revisa linha por linha.",
        "O câmbio efetivo de cada remessa aparece na hora.", cls="h3",
        estilo_p="font-size:33px;margin-top:16px") + f"""<div class='visual' style='margin-top:28px'>{crop}{NOTA_TELA}
  <div style='display:flex;gap:14px;margin-top:22px'>{chips}</div></div>""", 4, T))

    c = CX["0402_depois"]
    pa = c["painel_ano"]
    y0 = caixa("0402_depois", "2023")["y"] - 16
    y1 = caixa("0402_depois", "2025")["y"] - 12          # as linhas de 2023 e 2024, os anos com remessa
    crop = rec(P04, "celular-remessas-depois-04-02.png", y0, y1, 760, x0=pa[0] + 2, x1=pa[0] + pa[2] - 2)
    s.append(slide("light", EXTRA_F + topo(
        "Depois", "Cada ano com o seu câmbio.",
        "No rendimento ano a ano, os aportes de cada ano e o câmbio médio deles.", cls="h3",
        estilo_p="font-size:33px;margin-top:16px") + f"""<div class='visual' style='margin-top:28px'>
  <div class='rs' style='margin-bottom:14px'>Remessas · Rendimento ano a ano</div>{crop}{NOTA_TELA}
  <div style='margin-top:22px'>{pilula(I_GLOBO, 'Câmbio médio efetivo das 3: R$ 5,0000')}</div></div>""", 5, T))

    s.append(fechamento_verde("Seu histórico lá fora, num lugar só.",
        "Remessas ao exterior no timtimcash, no computador ou no celular.", 6, T))
    return [sem_quebra_fa(h) for h in s]


# ============================================================================ 06/02 · O gasto do ano, dividido por 12
_e0602 = CONTA.gerar("2027-02-06")[0]


def _soma(est, pred):
    return sum(D(str(t["valor"])) for t in est["txs"] if t["tipo"] == "despesa" and pred(t))


IPVA = _soma(_e0602, lambda t: t["descricao"] == "IPVA 2027")
IPTU = _soma(_e0602, lambda t: t["descricao"].startswith("IPTU 2027"))
MATERIAL = _soma(_e0602, lambda t: t["descricao"] == "Material escolar" and t["data"].startswith("2027"))
UNIFORME = _soma(_e0602, lambda t: t["descricao"] == "Uniforme escolar" and t["data"].startswith("2027"))
assert (IPVA, IPTU, MATERIAL, UNIFORME) == (D("1236.00"), D("2150.00"), D("940.00"), D("286.00"))
assert len([t for t in _e0602["txs"] if t["descricao"].startswith("IPTU 2027")]) == 10
N_PRES, PRESENTES = resumo("0602_presentes")                  # tela real: Transações, Ano 2026, busca "presentes de natal"
assert (N_PRES, PRESENTES) == (3, D("852.40"))
assert _soma(_e0602, lambda t: t["descricao"] == "Presentes de Natal" and t["data"].startswith("2026")) == PRESENTES
ANUAIS = [("IPVA", I_CARRO, "IPVA 2027 · à vista em janeiro", IPVA, CORAL),
          ("IPTU", I_CASA, "IPTU 2027 · 10 × R$ 215, de fevereiro a novembro", IPTU, AMBER),
          ("Material", I_LIVRO, "Material e uniforme · janeiro", MATERIAL + UNIFORME, INK),
          ("Presentes", I_PRESENTE, "Presentes de Natal · dezembro de 2026", PRESENTES, CORAL_CLARO)]
TOTAL_ANO = sum(v for *_, v, _ in ANUAIS)
assert TOTAL_ANO == D("5464.40")
POR_MES = q2(TOTAL_ANO / 12)
assert POR_MES == D("455.37")
# o fundo: R$ 455,37 por mês a partir de fevereiro de 2027, pagando cada conta no mês dela (os valores de 2027 repetidos)
SAIDAS = {2: IPTU / 10, 3: IPTU / 10, 4: IPTU / 10, 5: IPTU / 10, 6: IPTU / 10, 7: IPTU / 10, 8: IPTU / 10, 9: IPTU / 10,
          10: IPTU / 10, 11: IPTU / 10, 12: PRESENTES, 1: IPVA + MATERIAL + UNIFORME}
MESES_FUNDO = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1]
FUNDO, _s = [], D(0)
for _m in MESES_FUNDO:
    _s += POR_MES - SAIDAS[_m]
    FUNDO.append(_s)
assert min(FUNDO) >= 0 and FUNDO[-1] == D("0.04") and FUNDO[9] == D("2403.70") and FUNDO[10] == D("2006.67")
assert sum(SAIDAS.values()) == TOTAL_ANO
_rg = texto("0602_regra")
assert "Todo mês de janeiro" in _rg and "Resultado nos 24 meses | 22 meses em R$ 0 · 2 em R$ 1.236 | fev/27 | jan/29" in _rg
assert q2(IPVA) == D("1236.00")
_fx = CX["0602_fixa"]
assert _fx["_valor"] == "1.236,00" and "20/01/2028" in texto("0602_fixa") and "Lançamentos automáticos · anual" in texto("0602_fixa")
assert "Marcar como pago | Fica como pendente até você confirmar | Categoria | Impostos e Taxas" in texto("0602_fixa")


def capa_anual(T):
    """4 blocos (IPVA, IPTU, material, presentes), cada um partido em 12 fatias, e o que cabe em cada mês."""
    WMAX = 640
    linhas = []
    for nome, ip, _, v, cor in ANUAIS:
        w = float(v / IPTU) * WMAX
        fat = "".join(f"<i style='display:block;flex:1;height:100%;background:{cor};border-radius:{'14px 4px 4px 14px' if k == 0 else ('4px 14px 14px 4px' if k == 11 else '4px')}'></i>"
                      for k in range(12))
        linhas.append(f"""<div style='display:flex;align-items:center;gap:24px'>
  <div style='width:200px;flex:none;font-size:34px;font-weight:700;letter-spacing:-.02em'>{nome}</div>
  <div style='width:{w:.0f}px;height:66px;display:flex;gap:5px'>{fat}</div></div>""")
    meses = "JFMAMJJASOND"
    cols = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:10px'>"
                   f"<i style='display:block;width:100%;height:78px;border-radius:10px;background:{BRAND}'></i>"
                   f"<span style='font-size:21px;font-weight:700;color:{MUTED}'>{m}</span></div>" for m in meses)
    vis = f"""<div class='visual' style='margin-top:56px'>
  <div style='display:flex;flex-direction:column;gap:18px'>{''.join(linhas)}</div>
  <div style='display:flex;align-items:center;gap:20px;margin:34px 0 22px'>
    <div style='flex:1;height:3px;background:{FIO}'></div>
    <span class='pilula' style='font-size:30px;padding:12px 26px'>÷ 12</span>
    <div style='flex:1;height:3px;background:{FIO}'></div></div>
  <div style='display:flex;gap:10px'>{cols}</div>
</div>"""
    corpo = f"""<div class='eyebrow'>Planejamento</div>
<div class='h1' style='font-size:100px'>O gasto do ano, dividido por 12.</div>{vis}"""
    return capa("papel", EXTRA_F + corpo, 1, T)


def v_lista_anual():
    itens = "".join(f"""<div style='display:flex;align-items:center;gap:22px;padding:13px 0;{"border-top:2px solid " + FIO + ";" if i else ""}'>
  {azulejo(ip, 62, 31)}
  <div style='flex:1'><div style='font-size:31px;font-weight:700;letter-spacing:-.02em'>{n}</div>
    <div style='font-size:23px;color:{MUTED};margin-top:4px'>{sub.split(' · ')[1]}</div></div>
  <span class='tab' style='font-size:34px;font-weight:700;color:{CORAL_TXT}'>{brl(v)}</span></div>"""
                    for i, (n, ip, sub, v, _) in enumerate([(a[2].split(' · ')[0], a[1], a[2], a[3], a[4]) for a in ANUAIS]))
    return f"""<div class='visual' style='margin-top:30px'><div class='card' style='padding:6px 40px 24px'>
  {itens}
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding:16px 0 2px;border-top:3px solid {INK}'>
    <span style='font-size:31px;font-weight:700'>No ano</span><span class='tab' style='font-size:38px;font-weight:700'>{brl(TOTAL_ANO)}</span></div>
  <div style='display:flex;justify-content:space-between;align-items:center;margin-top:12px;padding:14px 24px;border-radius:20px;background:{SOFT}'>
    <span style='font-size:31px;font-weight:700;color:{BRAND_DEEP}'>÷ 12 meses</span>
    <span class='big' style='font-size:56px;color:{BRAND_DARK}'>{brl(POR_MES)}</span></div>
</div>
<div class='nota'>Conta de exemplo. Presentes de Natal de 2026: busca em Transações, no Ano 2026.</div></div>"""


def v_fundo():
    H = 330
    mx = float(max(FUNDO))
    rot = {"2": "fev", "3": "mar", "4": "abr", "5": "mai", "6": "jun", "7": "jul", "8": "ago", "9": "set", "10": "out", "11": "nov", "12": "dez", "1": "jan"}
    barras = []
    for m, v in zip(MESES_FUNDO, FUNDO):
        h = max(6.0, float(v) / mx * (H - 46))
        destaque = m in (12, 1)
        cor = BRAND if not destaque else BRAND_DARK
        valor = ""
        if m == 11:
            valor = f"<span class='tab' style='position:absolute;bottom:{h + 10:.0f}px;left:50%;transform:translateX(-50%);font-size:22px;font-weight:700;color:{BRAND_DARK};white-space:nowrap'>R$ 2.403,70</span>"
        barras.append(f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:10px'>
  <div style='position:relative;width:100%;height:{H}px;display:flex;align-items:flex-end'>{valor}
    <i style='display:block;width:100%;height:{h:.0f}px;border-radius:10px 10px 4px 4px;background:{cor}'></i></div>
  <span style='font-size:20px;font-weight:700;color:{MUTED}'>{rot[str(m)]}</span></div>""")
    return f"""<div class='visual' style='margin-top:38px'><div class='card' style='padding:30px 36px 24px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span class='rs'>O fundo do ano, mês a mês</span><span class='rs' style='color:{BRAND_DARK}'>+ R$ 455,37 todo mês</span></div>
  <div style='display:flex;gap:10px;margin-top:8px;align-items:flex-end'>{''.join(barras)}</div>
  <div style='display:flex;gap:16px;margin-top:22px;padding-top:20px;border-top:2px solid {FIO}'>
    <div style='flex:1;font-size:24px;line-height:1.35;color:{MUTED}'><b style='color:{INK}'>fev a nov:</b> paga o IPTU e cresce</div>
    <div style='flex:1;font-size:24px;line-height:1.35;color:{MUTED}'><b style='color:{INK}'>dez:</b> paga o Natal</div>
    <div style='flex:1;font-size:24px;line-height:1.35;color:{MUTED}'><b style='color:{INK}'>jan:</b> paga IPVA, material e uniforme</div></div>
</div>
<div class='nota'>Conta de exemplo, com os valores de 2027 repetidos até janeiro de 2028, quando o fundo paga a última conta do ciclo.</div></div>"""


def post_anual():
    T = 6
    s = [capa_anual(T)]

    s.append(slide("light", EXTRA_F + topo(
        "Na conta de exemplo", "Os gastos que voltam todo ano.",
        "Não são surpresa: só não vêm todo mês.", estilo_p="font-size:36px;margin-top:20px") + v_lista_anual(), 2, T))

    s.append(slide("light", EXTRA_F + topo(
        "A regra", "Guarde 1/12 por mês.",
        "Começando em fevereiro, o dinheiro de janeiro fica pronto antes de janeiro chegar.",
        estilo_p="font-size:36px;margin-top:20px") + v_fundo(), 3, T))

    c = CX["0602_regra"]
    y0 = caixa("0602_regra", "Regras")["y"] - 14
    y1 = c["res"][1] + c["res"][3] + 8
    crop = rec(P06, "celular-simulacao-regra-ipva-06-02.png", y0, y1, 640, x0=12, x1=378, rolagem=c.get("_rolagem", 0))
    s.append(slide("light", EXTRA_F + topo(
        "No timtimcash · Simulação futura", "Um gasto em todo janeiro.",
        "Em “Ajustar por mês”, a regra “+ Um mês do ano” põe o IPVA em cada janeiro do cenário.", cls="h3",
        estilo_p="font-size:33px;margin-top:18px") + f"<div class='visual' style='margin-top:32px'>{crop}{NOTA_TELA}</div>", 4, T))

    c = CX["0602_fixa"]
    y0 = caixa("0602_fixa", "Valor")["y"] - 16
    y1 = caixa("0602_fixa", "Lançamentos automáticos")["y"] + 34
    esq = f"""<div class='eyebrow'>No timtimcash · Nova transação</div>
<div class='h3' style='font-size:54px'>Ou lance o IPVA como Fixa anual.</div>
<div class='p' style='font-size:30px;margin-top:22px'>O de 2028 já fica em Pendentes, com a data. E todo janeiro aparece de novo.</div>"""
    dir_ = rec(P06, "celular-nova-despesa-fixa-anual-06-02.png", y0, y1, 520, x0=4, x1=386, rolagem=c.get("_rolagem", 0)) + NOTA_TELA_P
    s.append(slide("light", EXTRA_F + dois(esq, dir_, 520, gap=36), 5, T))

    s.append(fechamento_verde("Janeiro sem susto.",
        "Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra_fa(h) for h in s]


# ============================================================================ 11/02 · Saúde e educação: o que entra no IR
N_EXAME, EXAME = resumo("1102_exame")                # Transações, Ano 2026, busca "exame"
N_FARM, FARMACIA = resumo("1102_farmacia")           # busca "farmácia"
N_EDU, EDUCACAO = resumo("1102_educacao")            # categoria Educação
assert (N_EXAME, EXAME) == (1, D("150.00")) and (N_FARM, FARMACIA) == (23, D("3279.44")) and (N_EDU, EDUCACAO) == (12, D("17400.00"))
_e1102 = CONTA.gerar("2027-02-11")[0]
assert EDUCACAO == 12 * D("1450.00") == _soma(_e1102, lambda t: t["categoria"] == "Educação" and t["data"].startswith("2026") and t["conciliado"])
LIMITE_EDU = D("3561.50")                             # FATOS 5c.1 e 5c.2 (Lei 9.250/1995, art. 8º, II, "b", 10; vale para 2026)
ACIMA = EDUCACAO - LIMITE_EDU
assert ACIMA == D("13838.50")
SAUDE_LISTA = ["Médicos", "Dentistas", "Psicólogos", "Fisioterapeutas", "Fonoaudiólogos", "Terapeutas ocupacionais", "Hospitais",
               "Exames laboratoriais", "Serviços radiológicos", "Aparelhos ortopédicos", "Próteses ortopédicas e dentárias", "Plano de saúde"]


def recibo(titulo, itens, ok, ang, W=360, H=470):
    """Recibo desenhado (borda de baixo picotada), com o visto verde ou riscado em coral."""
    dentes = 12
    passo = W / dentes
    borda = " ".join(f"L{(k + .5) * passo:.1f} {H - 18} L{(k + 1) * passo:.1f} {H}" for k in range(dentes))
    forma = f"M0 18 Q0 0 18 0 L{W - 18} 0 Q{W} 0 {W} 18 L{W} {H} {borda.replace('L' + f'{W:.1f} {H}', 'L' + f'{W} {H}')} Z"
    caminho = f"M0 18 Q0 0 18 0 L{W - 18} 0 Q{W} 0 {W} 18 L{W} {H} " + " ".join(
        f"L{W - (k + .5) * passo:.1f} {H - 18} L{W - (k + 1) * passo:.1f} {H}" for k in range(dentes)) + " Z"
    linhas = "".join(f"""<div style='display:flex;justify-content:space-between;align-items:center;padding:16px 0;border-top:2px dashed {FIO}'>
  <span style='font-size:30px;font-weight:700;{"text-decoration:line-through;text-decoration-thickness:4px;text-decoration-color:" + CORAL + ";color:" + MUTED + ";" if not ok else ""}'>{t}</span>
  <i style='display:block;width:70px;height:12px;border-radius:6px;background:{FIO}'></i></div>""" for t in itens)
    badge_cor, badge_ic = (BRAND, I_CHECK) if ok else (CORAL, I_X)
    risco = "" if ok else f"<div style='position:absolute;left:-26px;right:-26px;top:{H * .52:.0f}px;height:12px;border-radius:6px;background:{CORAL};transform:rotate(-24deg)'></div>"
    return f"""<div style='position:relative;width:{W}px;height:{H}px;transform:rotate({ang}deg)'>
  <svg width='{W}' height='{H}' style='position:absolute;left:0;top:0;overflow:visible'>
    <defs><filter id='sr{int(ok)}' x='-15%' y='-10%' width='130%' height='130%'><feDropShadow dx='0' dy='18' stdDeviation='18' flood-color='#0F1410' flood-opacity='.16'/></filter></defs>
    <path d='{caminho}' fill='#fff' stroke='{FIO}' stroke-width='2' filter='url(#sr{int(ok)})'/></svg>
  <div style='position:absolute;left:34px;right:34px;top:34px'>
    <div class='rs' style='letter-spacing:.2em'>{titulo}</div>
    <div style='margin-top:18px'>{linhas}</div>
    <div style='display:flex;gap:12px;margin-top:22px'><i style='display:block;width:120px;height:12px;border-radius:6px;background:{FIO}'></i>
      <i style='display:block;width:60px;height:12px;border-radius:6px;background:{FIO}'></i></div>
  </div>{risco}
  <div style='position:absolute;right:-30px;top:-30px;width:104px;height:104px;border-radius:50%;background:{badge_cor};display:flex;align-items:center;justify-content:center;
    box-shadow:0 0 0 10px {SOFT if ok else "#FBE7DF"}'>{svg_icone(badge_ic, 56, "#fff", 3)}</div>
</div>"""


def capa_ir(T):
    vis = f"""<div class='visual' style='position:relative;height:540px;margin-top:64px'>
  <div style='position:absolute;left:40px;top:10px'>{recibo('Recibo', ['Consulta', 'Exame'], True, -5)}</div>
  <div style='position:absolute;left:470px;top:56px'>{recibo('Recibo', ['Farmácia', 'Remédio'], False, 5)}</div>
</div>"""
    corpo = f"""<div class='eyebrow'>Imposto de renda</div>
<div class='h1' style='font-size:96px'>Saúde e educação: o que entra no IR?</div>{vis}"""
    return capa("suave", EXTRA_F + corpo, 1, T)


def v_saude_lista():
    chips = "".join(f"<span style='display:inline-flex;align-items:center;gap:12px;padding:14px 22px;border-radius:999px;background:#fff;border:2px solid {FIO};"
                    f"font-size:27px;font-weight:600'>{svg_icone(I_CHECK, 26, BRAND_DARK, 3)}{n}</span>" for n in SAUDE_LISTA)
    return f"""<div class='visual' style='margin-top:38px'>
  <div style='display:flex;flex-wrap:wrap;gap:14px'>{chips}</div>
  <div class='card' style='margin-top:30px;padding:24px 30px;display:flex;gap:22px;align-items:center'>
    {azulejo(I_ALERT, 72, 36)}
    <div style='font-size:28px;line-height:1.35'><b>Só o seu tratamento e o dos seus dependentes</b> <span style='color:{MUTED}'>na declaração.</span></div></div>
<div class='nota'>Lei 9.250/1995, art. 8º, II, “a”, e § 2º, I a IV.</div></div>"""


def v_fora_lista():
    def linha(t, s, i):
        return f"""<div style='display:flex;gap:24px;align-items:center;padding:26px 0;{"border-top:2px solid " + FIO + ";" if i else ""}'>
  <div style='width:76px;height:76px;flex:none;border-radius:24px;background:#FBE7DF;display:flex;align-items:center;justify-content:center'>{svg_icone(I_X, 40, CORAL_FORTE, 2.8)}</div>
  <div><div style='font-size:34px;font-weight:700;letter-spacing:-.02em'>{t}</div><div style='font-size:25px;color:{MUTED};margin-top:6px;line-height:1.35'>{s}</div></div></div>"""
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:26px 40px 8px'>
  <div class='rs' style='color:{CORAL_TXT}'>Também ficam de fora</div>
  {linha('Teste de Covid feito em farmácia', 'Diz a Receita Federal.', 0)}
  {linha('O que o plano reembolsou', 'Despesa ressarcida não entra.', 1)}
</div>
<div style='margin-top:30px'>{pilula(I_BUSCA, f'Na conta de exemplo, {brl(FARMACIA)} em farmácia em 2026.')}</div>
<div class='nota'>Lei 9.250/1995, art. 8º, II, “a”, e § 2º, IV; Receita Federal, perguntas frequentes do IRPF.</div></div>"""


def v_educacao():
    W = 816
    wv = float(LIMITE_EDU / EDUCACAO) * W
    listra = f"repeating-linear-gradient(135deg,{FIO} 0 12px,#F4F2EA 12px 24px)"
    nao = ["Material", "Uniforme", "Transporte escolar", "Idioma", "Cursinho", "Música, dança e esportes"]
    chips = "".join(f"<span style='display:inline-flex;align-items:center;gap:10px;padding:10px 18px;border-radius:999px;background:#FBE7DF;color:{CORAL_FORTE};"
                    f"font-size:24px;font-weight:700'>{svg_icone(I_X, 22, CORAL_FORTE, 3)}{n}</span>" for n in nao)
    return f"""<div class='visual' style='margin-top:36px'><div class='card' style='padding:30px 40px 30px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span class='rs'>Escola em 2026 · conta de exemplo</span><span class='tab' style='font-size:34px;font-weight:700'>{brl(EDUCACAO)}</span></div>
  <div style='display:flex;gap:4px;margin-top:18px'>
    <div style='width:{wv:.1f}px;height:64px;border-radius:16px 5px 5px 16px;background:{BRAND}'></div>
    <div style='flex:1;height:64px;border-radius:5px 16px 16px 5px;background:{listra}'></div></div>
  <div style='display:flex;justify-content:space-between;margin-top:14px'>
    <span style='font-size:26px;font-weight:700;color:{BRAND_DARK}'>entra: {brl(LIMITE_EDU)}</span>
    <span style='font-size:26px;font-weight:600;color:{MUTED}'>acima do limite: {brl(ACIMA)}</span></div>
  <div style='margin-top:26px;padding-top:22px;border-top:2px solid {FIO}'>
    <div class='rs' style='color:{CORAL_TXT}'>Não entra</div>
    <div style='display:flex;flex-wrap:wrap;gap:10px;margin-top:14px'>{chips}</div></div>
</div>
<div class='nota'>Declare o valor total, mesmo acima do limite (Receita Federal). Lei 9.250/1995, art. 8º, II, “b”. Escola de 2026: Transações, categoria Educação.</div></div>"""


def v_duas_buscas():
    def bloco(chave, nome, sim, rotulo):
        c = CX[chave]
        y0 = 292
        y1 = c["busca"][1] + c["busca"][3] + 8
        crop = rec(P11, nome, y0, y1, 560, x0=16, x1=374)
        return f"""<div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:14px'>
  {selo(sim, rotulo)}</div>{crop}"""
    return f"""<div class='visual' style='margin-top:26px;display:flex;flex-direction:column;gap:22px;align-items:center'>
  <div>{bloco('1102_exame', 'celular-busca-exame-2026-11-02.png', True, f'Exame, {brl(EXAME, cent=False)}: entra')}</div>
  <div>{bloco('1102_farmacia', 'celular-busca-farmacia-2026-11-02.png', False, f'Farmácia, {brl(FARMACIA)}: fora da lista')}</div>
</div>{NOTA_TELA}"""


def v_faz_nao_faz():
    def item(ok, t):
        ic = svg_icone(I_CHECK if ok else I_X, 30, BRAND_DEEP if ok else CORAL_FORTE, 3)
        fundo = SOFT if ok else "#FBE7DF"
        return f"""<div style='display:flex;gap:18px;align-items:flex-start;padding:16px 0'>
  <span style='width:52px;height:52px;flex:none;border-radius:16px;background:{fundo};display:flex;align-items:center;justify-content:center'>{ic}</span>
  <span style='font-size:29px;font-weight:600;line-height:1.3;padding-top:6px'>{t}</span></div>"""
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:24px 40px 22px'>
  <div class='rs' style='color:{BRAND_DARK}'>O timtimcash faz</div>
  {item(True, 'Soma por busca e por categoria, no ano que você escolher.')}
  {item(True, 'Exporta a lista filtrada em Excel ou CSV, para levar ao contador.')}
  <div class='fio' style='margin:12px 0 16px'></div>
  <div class='rs' style='color:{CORAL_TXT}'>Não faz</div>
  {item(False, 'A declaração do imposto de renda.')}
</div></div>"""


def post_ir():
    T = 7
    s = [capa_ir(T)]

    s.append(slide("light", EXTRA_F + topo(
        "Saúde · sem limite de valor", "Entra o que está na lista da lei.", cls="h3",
        estilo_t="font-size:62px") + v_saude_lista(), 2, T))

    s.append(slide("light", EXTRA_F + topo(
        "Saúde · o que fica de fora", "Remédio de farmácia não entra.",
        "Ele não está entre as despesas médicas da lei.", cls="h3", estilo_t="font-size:64px",
        estilo_p="font-size:36px;margin-top:20px") + v_fora_lista(), 3, T))

    s.append(slide("light", EXTRA_F + topo(
        "Educação · com limite", "Até R$ 3.561,50 por pessoa no ano.",
        "Escola entra até esse teto. Material e uniforme, não.", cls="h3", estilo_t="font-size:62px",
        estilo_p="font-size:34px;margin-top:18px") + v_educacao(), 4, T))

    s.append(slide("light", EXTRA_F + topo(
        "No timtimcash", "O seu 2026 em duas buscas.",
        "Em Transações, no Ano 2026: “exame” e “farmácia”.", cls="h3",
        estilo_p="font-size:33px;margin-top:16px") + v_duas_buscas(), 5, T))

    s.append(slide("light", EXTRA_F + topo(
        "Antes de declarar", "Confira com um contador.",
        "O timtimcash organiza os números. A declaração é sua.", estilo_p="font-size:36px;margin-top:20px") + v_faz_nao_faz(), 6, T))

    s.append(fechamento_verde("Seu ano de saúde e escola, somado.",
        "Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_fa(h) for h in s]


# ============================================================================ 13/02 · Guardar não é gastar
_vf = texto("1302_visao_fev")
assert "Guardou 33,6% da receita" in _vf and "Receitas R$ 9.960,00 | Despesas R$ 6.610,10 | Resultado do período | R$ 3.349,90" in _vf
_va = texto("1302_visao_2026")
assert "Guardou 19,4% da receita" in _va and "Receitas R$ 126.293,36 | Despesas R$ 101.854,70 | Resultado do período | R$ 24.438,66" in _va
REC_FEV, DESP_FEV, RES_FEV = D("9960.00"), D("6610.10"), D("3349.90")
REC_26, DESP_26, RES_26 = D("126293.36"), D("101854.70"), D("24438.66")
assert REC_FEV - DESP_FEV == RES_FEV and REC_26 - DESP_26 == RES_26
assert pct1(RES_FEV / REC_FEV) == "33,6%" and pct1(RES_26 / REC_26) == "19,4%"      # a conta do site: resultado ÷ receitas
RESERVA = D("1500.00")
DESP_FEV2, RES_FEV2 = DESP_FEV + RESERVA, RES_FEV - RESERVA                        # se a reserva fosse lançada como despesa
assert (DESP_FEV2, RES_FEV2, pct1(RES_FEV2 / REC_FEV)) == (D("8110.10"), D("1849.90"), "18,6%")
N_RES26, RESERVA_26 = resumo("1302_reserva_2026")
assert (N_RES26, RESERVA_26) == (12, D("18000.00")) and RESERVA_26 == 12 * RESERVA
RES_262 = RES_26 - RESERVA_26
assert (RES_262, pct1(RES_262 / REC_26)) == (D("6438.66"), "5,1%")
# a volta da reserva (slide 5): R$ 1.000 de exemplo, Reserva → Conta corrente, na "Nova transação" de 13/02 (não salva)
VOLTA = D("1000.00")
assert CX["1302_volta"]["_valor"] == "1.000,00"
assert "Hoje 13/02 | Já foi feita | Afeta o saldo das duas contas agora | De | Reserva | Para | Conta corrente" in texto("1302_volta")
REC_FEV3, RES_FEV3 = REC_FEV + VOLTA, RES_FEV + VOLTA                              # se a volta fosse lançada como receita
assert (REC_FEV3, RES_FEV3, pct1(RES_FEV3 / REC_FEV3)) == (D("10960.00"), D("4349.90"), "39,7%")
_tr = texto("1302_transferencia")
assert "Data | 05/03/2027 | Marcar como feita | Fica como pendente até você confirmar | De | Conta corrente | Para | Reserva" in _tr


def conta_badge(ip, nome, cor_fundo=SOFT, cor_ic=BRAND_DARK):
    return f"""<div style='display:flex;flex-direction:column;align-items:center;gap:22px;width:270px;flex:none'>
  <div style='width:240px;height:240px;border-radius:30%;background:{cor_fundo};display:flex;align-items:center;justify-content:center'>{svg_icone(ip, 124, cor_ic, 1.6)}</div>
  <div style='font-size:40px;font-weight:700;letter-spacing:-.02em;text-align:center;white-space:nowrap'>{nome}</div></div>"""


def capa_guardar(T):
    seta = f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:14px;margin-top:-66px'>
  <div class='big' style='font-size:66px;color:{BRAND_DARK}'>R$ 1.500</div>
  <svg width='330' height='48' viewBox='0 0 330 48' style='display:block'><path d='M8 24 H300' stroke='{BRAND}' stroke-width='12' stroke-linecap='round'/>
    <path d='M284 6 L316 24 L284 42' fill='none' stroke='{BRAND}' stroke-width='12' stroke-linecap='round' stroke-linejoin='round'/></svg>
  <div style='font-size:26px;font-weight:700;letter-spacing:.14em;color:{MUTED}'>TRANSFERÊNCIA</div></div>"""
    vis = f"""<div class='visual' style='margin-top:84px'>
  <div style='display:flex;align-items:center'>{conta_badge(I_BANCO, 'Conta corrente')}{seta}{conta_badge(I_COFRE, 'Reserva')}</div>
  <div style='display:flex;justify-content:center;margin-top:60px'>
    <span style='display:inline-flex;align-items:center;gap:16px;padding:18px 36px;border-radius:999px;background:#fff;border:2px solid {FIO};font-size:36px;font-weight:700'>
      {svg_icone(I_X, 36, CORAL_FORTE, 3)}<span style='color:{CORAL_FORTE};text-decoration:line-through;text-decoration-thickness:4px'>despesa</span></span></div>
</div>"""
    corpo = f"""<div class='eyebrow'>Organização</div>
<div class='h1' style='font-size:118px'>Guardar não é gastar.</div>{vis}"""
    return capa("papel", EXTRA_F + corpo, 1, T)


def v_mes_com_e_sem():
    c = CX["1302_visao_fev"]
    y0 = caixa("1302_visao_fev", "Movimento de fevereiro 2027")["y"] - 4
    y1 = caixa("1302_visao_fev", "Resultado do período")["y"] + 32
    crop = rec(P13, "celular-visao-geral-fevereiro-13-02.png", y0, y1, 760, x0=16, x1=374)

    def lin(r, v, cor=INK, forte=False):
        return (f"<div style='display:flex;justify-content:space-between;align-items:baseline;padding:8px 0'><span style='font-size:27px;font-weight:{700 if forte else 500};color:{MUTED if not forte else INK}'>{r}</span>"
                f"<span class='tab' style='font-size:{34 if forte else 29}px;font-weight:700;color:{cor}'>{v}</span></div>")
    return f"""<div class='visual' style='margin-top:30px'>
  <div style='margin-bottom:12px'>{selo(True, 'Como transferência, como está na tela')}</div>
  {crop}
  <div style='margin:26px 0 12px'>{selo(False, 'Se os R$ 1.500 fossem despesa')}</div>
  <div class='card' style='padding:14px 34px 16px;display:flex;gap:34px;align-items:center'>
    <div style='flex:none;text-align:center;padding-right:30px;border-right:2px solid {FIO}'>
      <div class='big' style='font-size:66px;line-height:1;color:{CORAL_FORTE}'>18,6%</div>
      <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:6px'>guardado da receita</div></div>
    <div style='flex:1'>{lin('Despesas', brl(DESP_FEV2), CORAL_TXT)}{lin('Resultado', brl(RES_FEV2), INK, True)}</div></div>
</div>
<div class='nota'>Fevereiro até o dia 13, na conta de exemplo. Tela real do timtimcash, com dados de exemplo.</div>"""


def v_transferencia():
    c = CX["1302_transferencia"]
    y0 = caixa("1302_transferencia", "Nova transação")["y"] - 18
    y1 = caixa("1302_transferencia", "Para")["y"] + 38
    return f"""<div class='visual' style='margin-top:30px'>{rec(P13, 'celular-nova-transferencia-13-02.png', y0, y1, 530, x0=4, x1=386, rolagem=c.get('_rolagem', 0))}{NOTA_TELA}</div>"""


def post_guardar():
    T = 6
    s = [capa_guardar(T)]

    s.append(slide("light", EXTRA_F + topo(
        "O erro comum", "Como despesa, a reserva encolhe o mês.", cls="h3",
        estilo_t="font-size:62px") + v_mes_com_e_sem(), 2, T))

    s.append(slide("light", EXTRA_F + topo(
        "No timtimcash", "Guardar é Transferência.",
        "De uma conta para a outra, sem categoria. O patrimônio fica igual.", cls="h3",
        estilo_p="font-size:33px;margin-top:16px") + v_transferencia(), 3, T))

    c = CX["1302_reserva_2026"]
    y0, y1 = 309, caixa("1302_reserva_2026", "Agir sobre")["y"] - 134        # do título "Transações" ao fim da busca "reserva"
    crop = rec(P13, "celular-transferencias-reserva-2026-13-02.png", y0, y1, 760, x0=14, x1=376)
    comp = f"""<div class='card' style='margin-top:26px;padding:22px 34px;display:flex;align-items:center;gap:30px'>
  <div style='flex:1'><div style='font-size:28px;font-weight:700'>Guardado da receita em 2026</div>
    <div style='font-size:24px;color:{MUTED};margin-top:4px'>na Visão geral, com a reserva como transferência</div></div>
  <div style='text-align:right'><div class='big' style='font-size:60px;line-height:1;color:{BRAND_DARK}'>19,4%</div>
    <div style='font-size:22px;font-weight:600;color:{CORAL_TXT};margin-top:6px'>como despesa, seria 5,1%</div></div></div>"""
    s.append(slide("light", EXTRA_F + topo(
        "Todo mês, R$ 1.500", "Em 2026, R$ 18.000 guardados.",
        "Doze transferências para a Reserva. Nenhum real como despesa.", cls="h3",
        estilo_p="font-size:33px;margin-top:16px") + f"<div class='visual' style='margin-top:28px'>{crop}{NOTA_TELA}{comp}</div>", 4, T))

    c = CX["1302_volta"]
    y0 = caixa("1302_volta", "Nova transação")["y"] - 18
    y1 = caixa("1302_volta", "Para")["y"] + 38
    dir_ = rec(P13, "celular-nova-transferencia-volta-13-02.png", y0, y1, 420, x0=4, x1=386, rolagem=c.get("_rolagem", 0)) + NOTA_TELA_P

    def lin(r, v, cor=INK, forte=False):
        return (f"<div style='display:flex;justify-content:space-between;align-items:baseline;padding:6px 0'><span style='font-size:25px;font-weight:{700 if forte else 500};color:{INK if forte else MUTED}'>{r}</span>"
                f"<span class='tab' style='font-size:{29 if forte else 26}px;font-weight:700;color:{cor}'>{v}</span></div>")
    esq = f"""<div class='eyebrow'>Na volta também</div>
<div class='h3' style='font-size:50px'>Tirou da reserva?<br>Não é receita.</div>
<div class='p' style='font-size:29px;margin-top:18px'>A volta para a Conta corrente também é Transferência.</div>
<div style='margin-top:26px'>{selo(False, 'Se fosse receita')}</div>
<div class='card' style='margin-top:14px;padding:20px 26px 14px'>
  <div class='big' style='font-size:62px;line-height:1;color:{CORAL_FORTE}'>{pct1(RES_FEV3 / REC_FEV3)}</div>
  <div style='font-size:23px;font-weight:600;color:{INK};margin-top:8px'>guardado da receita</div>
  <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:2px'>em vez de {pct1(RES_FEV / REC_FEV)}</div>
  <div style='margin-top:10px;padding-top:8px;border-top:2px solid {FIO}'>{lin('Receitas', brl(REC_FEV3), BRAND_DARK)}{lin('Resultado', brl(RES_FEV3), INK, True)}</div></div>
<div class='nota' style='font-size:21px'>Fevereiro até o dia 13, na conta de exemplo: o mês pareceria ter guardado mais do que guardou.</div>"""
    s.append(slide("light", EXTRA_F + dois(esq, dir_, 420, gap=40), 5, T))

    s.append(fechamento_verde("Guardou? É transferência.",
        "Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra_fa(h) for h in s]


POSTS = {P01: post_fevereiro, P04: post_remessas, P06: post_anual, P11: post_ir, P13: post_guardar}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    renderizar(POSTS, so=so)
