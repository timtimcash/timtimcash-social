# -*- coding: utf-8 -*-
"""Carrosséis da equipe dc1 · dezembro de 2026 (02, 04, 07, 10 e 12/12), no formato aprovado em outubro e novembro
(N/kit/carrossel.py; modelos em N/equipes/c1/posts.py e N/equipes/c2/posts.py).

Telas reais (conta de base, N/base_app sem mudança, build 2026-10-16.1), capturadas por captura.py em 16/10/2026 e
guardadas em N/saida/<pasta>/telas/:
- 02/12 · Pendentes, relógio em 02/12/2026 10:00 (A pagar R$ 4.229,80; A receber R$ 12.393,36; 18/12 "13º salário ·
  2ª parcela" +R$ 2.433,36; 20/12 nuvem −R$ 42,00; 27/12 "Notebook (2/10)" −R$ 360,00) e Remessas › "Editar
  fechamentos" ("Quanto havia no fim de cada ano": 2025 US$ 12.960,00 a R$ 5,5018; 2026 em curso US$ 13.310,00 a R$ 5,0515).
- 04/12 · "Nova transação" › Receita R$ 2.433,36, 18/12/2026, "Marcar como recebido" desligado, Salário, sem salvar.
- 07/12 · Visão geral de Janeiro 2027 em "Previsto" (Receitas R$ 9.960,00; Despesas R$ 6.405,80; Resultado previsto
  R$ 3.554,20) e Relatórios › "Sazonalidade" com o toque em janeiro ("R$ 9.420,00 (jan/26)"; dezembro R$ 9.860).
- 10/12 · "Nova transação" › Despesa R$ 1.462,08, 10/01/2027, "Dívidas e empréstimos", "Parcelada" 12 meses
  ("12× de R$ 121,84 · mensal"), sem salvar.
- 12/12 · Remessas em EUR: "Câmbio médio efetivo R$ 5,7627 com IOF · sem IOF R$ 5,7000", "IOF pago R$ 125,40 · 1,10%".
Fatos: N/FATOS.md; taxas de agosto de 2026 e definições das siglas pesquisadas em fontes oficiais em 16/10/2026
(URLs nos dados de cada post).

python3 posts.py                       renderiza os 5 posts e confere o layout
python3 posts.py <pasta> [<pasta>...]  só os escolhidos
"""
import os, re, sys, calendar
from datetime import date
from decimal import Decimal as D, ROUND_HALF_UP

N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, N + "/kit")
from carrossel import *   # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl, sem_quebra...)

P02 = "2026-12-02_dezembro-do-seu-dinheiro"
P04 = "2026-12-04_por-que-a-segunda-parcela-vem-menor"
P07 = "2026-12-07_janeiro-caro-o-que-chega-junto"
P10 = "2026-12-10_o-preco-do-dinheiro-emprestado"
P12 = "2026-12-12_oito-siglas-do-seu-dinheiro"

NBSP = " "


def q2(v):
    return D(v).quantize(D("0.01"), ROUND_HALF_UP)


def sem_quebra_dc1(html):
    """sem_quebra do kit; nas citações, número junto da lei, do artigo e da resolução."""
    html = sem_quebra(html)
    html = re.sub(r"\b(Lei|Decreto|art\.|arts\.|nº|Res\. CMN|Res\. BCB|Resolução BCB|Estudo Especial|SGS) (\d)",
                  lambda m: m.group(1).replace(" ", NBSP) + NBSP + m.group(2), html)
    html = html.replace("Black Friday", "Black" + NBSP + "Friday").replace("% ao ", "%" + NBSP + "ao" + NBSP)
    return html


def tela(pasta, nome):
    caminho = os.path.join(SAIDA, pasta, "telas", nome)
    assert os.path.isfile(caminho), caminho
    return caminho


EXTRA_D = EXTRA + f"""<style>
.leg{{display:flex;align-items:center;gap:12px;font-size:27px;font-weight:700;white-space:nowrap}}
.leg i{{display:block;flex:none}}
.linha-item{{display:flex;gap:28px;align-items:center;padding:24px 0}}
.linha-item + .linha-item{{border-top:2px solid {FIO}}}
.linha-item .t{{font-size:36px;font-weight:700;letter-spacing:-.03em;line-height:1.15}}
.linha-item .s{{font-size:27px;color:{MUTED};margin-top:6px;line-height:1.32}}
.pilula{{display:inline-flex;align-items:center;gap:12px;background:{SOFT};color:{BRAND_DEEP};font-size:27px;font-weight:700;padding:15px 28px;border-radius:999px}}
.tab{{font-variant-numeric:tabular-nums}}
.rs{{font-size:22px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTED}}}
.preencher{{border-bottom:4px dotted {NEUTRO};height:34px;display:block}}
</style>"""


def topo(sobre, titulo, apoio=None, cls="h2", estilo_t="", estilo_p=""):
    p = f"<div class='p' style='{estilo_p}'>{apoio}</div>" if apoio else ""
    return f"<div class='eyebrow'>{sobre}</div><div class='{cls}' style='{estilo_t}'>{titulo}</div>{p}"


def item(ip, titulo, sub, tam=84, ic=42):
    return f"""<div class='linha-item'>{azulejo(ip, tam, ic)}
  <div><div class='t'>{titulo}</div><div class='s'>{sub}</div></div></div>"""


def pilula(ip, txt):
    return f"<span class='pilula'>{svg_icone(ip, 30, BRAND_DEEP, 2.2)}{txt}</span>"


# ícones de traço próprios (24 × 24, pontas redondas)
I_CARRO = ('<path d="M4 15.6v-3.3l1.9-4.6a2 2 0 0 1 1.8-1.2h8.6a2 2 0 0 1 1.8 1.2l1.9 4.6v3.3"/>'
           '<path d="M3.5 15.6h17M4.6 12.2h14.8"/><circle cx="7.8" cy="17.6" r="1.6"/><circle cx="16.2" cy="17.6" r="1.6"/>')
I_LIVRO = '<path d="M12 6.6C10 5.1 7 4.6 4 5.1v13c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5v-13c-3-.5-6 0-8 1.5z"/><path d="M12 6.6v13"/>'
I_PCT = '<path d="M18.5 5.5l-13 13"/><circle cx="7.2" cy="7.2" r="2.4"/><circle cx="16.8" cy="16.8" r="2.4"/>'
I_BANCO = '<path d="M12 3.5 20.5 8h-17z"/><path d="M5 11v6.5M9.7 11v6.5M14.3 11v6.5M19 11v6.5"/><path d="M3.5 20.5h17"/>'
I_SETA = '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>'
I_CADEADO = '<rect x="5" y="10.5" width="14" height="10" rx="2.2"/><path d="M8.2 10.5V7.8a3.8 3.8 0 0 1 7.6 0v2.7"/>'


# ============================================================================ calendário (mesmo desenho do 01/11)
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


# ============================================================================ números do 13º (FATOS.md, dezembro)
SALARIO = D("9960.00")
PARCELA1 = SALARIO / 2
INSS = D("988.09")
IR = D("1558.55")
PARCELA2 = PARCELA1 - INSS - IR
assert PARCELA1 == D("4980.00") and PARCELA2 == D("2433.36")
DESCONTOS = INSS + IR
assert DESCONTOS == D("2546.64")
FAIXAS_INSS = [(D("1621.00"), D("0.075")), (D("2902.84"), D("0.09")), (D("4354.27"), D("0.12")), (D("8475.55"), D("0.14"))]


def inss_de(s):
    tot, ant = D(0), D(0)
    for lim, al in FAIXAS_INSS:
        if s > ant:
            tot += (min(s, lim) - ant) * al
        ant = lim
    return q2(tot)


def ir_tabela(base):
    for lim, al, ded in [(D("2428.80"), D(0), D(0)), (D("2826.65"), D("0.075"), D("182.16")), (D("3751.05"), D("0.15"), D("394.16")),
                         (D("4664.68"), D("0.225"), D("675.49")), (None, D("0.275"), D("908.73"))]:
        if lim is None or base <= lim:
            return q2(max(D(0), base * al - ded))


assert inss_de(SALARIO) == INSS and ir_tabela(SALARIO - INSS) == IR
BASE_IR = SALARIO - INSS
assert BASE_IR == D("8971.91")
# exemplos da Lei 15.270/2025 (FATOS.md): R$ 6.000 e R$ 4.500, sem dependentes
EX6_INSS, EX6_IR_TAB = inss_de(D("6000")), ir_tabela(D("6000") - inss_de(D("6000")))
EX6_RED = q2(D("978.62") - D("0.133145") * D("6000"))
EX6_IR = EX6_IR_TAB - EX6_RED
EX6_P2 = D("3000") - EX6_INSS - EX6_IR
assert (EX6_INSS, EX6_IR_TAB, EX6_RED, EX6_IR, EX6_P2) == (D("641.51"), D("564.85"), D("179.75"), D("385.10"), D("1973.39"))
EX45_INSS = inss_de(D("4500"))
EX45_IR_TAB = ir_tabela(D("4500") - EX45_INSS)
assert EX45_IR_TAB <= D("312.89")          # a redução cobre o imposto todo até R$ 5.000
EX45_P2 = D("2250") - EX45_INSS
assert (EX45_INSS, EX45_P2) == (D("431.51"), D("1818.49"))


# ============================================================================ 02/12 · Dezembro do seu dinheiro
def capa_dezembro(T):
    cal = f"""<div class='card' style='position:relative;margin-top:50px;padding:0;overflow:visible'>
  {argolas()}
  <div style='height:30px;border-radius:28px 28px 0 0;background:{FIO}'></div>
  <div style='padding:10px 30px 2px'>{grade_mes(2026, 12, {18: 'verde', 20: 'anel', 25: 'coral', 31: 'tinta'}, cel=82, bola=70, fs=33)}</div>
  <div style='display:grid;grid-template-columns:auto auto;justify-content:center;column-gap:56px;row-gap:18px;padding:24px 30px 30px;border-top:2px solid {FIO};margin:8px 34px 0'>
    {leg_bola(f'background:{BRAND}', '2ª parcela, no exemplo', BRAND_DARK)}
    {leg_bola(f'background:#fff;box-shadow:inset 0 0 0 5px {BRAND}', 'Prazo da lei', BRAND_DARK)}
    {leg_bola(f'background:#fff;box-shadow:inset 0 0 0 5px {CORAL}', 'Natal', CORAL_TXT)}
    {leg_bola(f'background:{INK}', 'Fim do ano lá fora', INK)}
  </div>
</div>"""
    corpo = f"""<div class='eyebrow'>Calendário</div>
<div class='h1' style='font-size:100px'>Dezembro do seu dinheiro.</div>{cal}"""
    return capa("papel", EXTRA_D + corpo, 1, T)


def v_segunda_parcela():
    return f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:40px 46px 36px'>
  <div class='rs' style='color:{BRAND_DARK}'>2ª parcela · 18/12, no exemplo</div>
  <div class='big' style='font-size:106px;line-height:1;color:{BRAND_DARK};margin-top:12px'>R$ 2.433,36</div>
  <div style='display:grid;grid-template-columns:1fr auto;row-gap:16px;margin-top:30px;padding-top:26px;border-top:2px solid {FIO};font-size:29px'>
    <span style='color:{MUTED};font-weight:500'>A 1ª parcela, em 27/11</span><span class='tab' style='font-weight:700;color:{INK}'>R$ 4.980,00</span>
    <span style='color:{MUTED};font-weight:500'>INSS e IR do 13º inteiro</span><span class='tab' style='font-weight:700;color:{CORAL_TXT}'>−R$ 2.546,64</span>
  </div>
</div>
<div style='margin-top:30px'>{pilula(I_CAL, 'Sexta (04/12): a conta, passo a passo.')}</div>
<div class='nota'>Exemplo: salário de R$ 9.960, sem dependentes. Lei 4.749/1965, art. 1º; Lei 8.134/1990, art. 16; Decreto 3.048/1999, art. 214.</div></div>"""


def v_teto_festas():
    linhas = ["Presentes e doações", "Ceia (Mercado)", "Bares e restaurantes", "Roupas", "Viagem"]

    def linha(rot, forte=False):
        cor = INK if not forte else BRAND_DARK
        peso = 600 if not forte else 700
        return (f"<span style='font-size:29px;font-weight:{peso};color:{cor};white-space:nowrap'>{rot}</span>"
                f"<span style='font-size:29px;font-weight:700;color:{cor}'>R$</span><span class='preencher'></span>")
    corpo = "".join(linha(r) for r in linhas)
    return f"""<div class='visual' style='margin-top:36px'><div class='card' style='padding:28px 44px 28px'>
  <div style='display:flex;align-items:center;gap:14px'>{svg_icone(I_PRESENTE, 36, CORAL_TXT, 2.2)}
    <span style='font-size:25px;font-weight:700;letter-spacing:.16em;color:{CORAL_TXT}'>MEU TETO DAS FESTAS</span></div>
  <div style='display:grid;grid-template-columns:auto 44px 1fr;column-gap:16px;row-gap:14px;align-items:end;margin-top:22px'>
    {corpo}
  </div>
  <div style='display:grid;grid-template-columns:auto 44px 1fr;column-gap:16px;align-items:end;margin-top:20px;padding-top:18px;border-top:2px solid {FIO}'>
    {linha('Total', True)}
  </div>
</div>
<div style='margin-top:24px'>{pilula(I_MARCA_SALVAR, 'Salve este post e preencha.')}</div>
<div class='nota'>Os nomes são das categorias do timtimcash: em Orçamentos, cada uma pode ter um limite por mês.</div></div>"""


I_MARCA_SALVAR = '<path d="M7 3.5h10a1 1 0 0 1 1 1V21l-6-4-6 4V4.5a1 1 0 0 1 1-1z"/>'


def v_janeiro_vem():
    def bloco(ip, t, s):
        return f"""<div class='card' style='padding:28px 30px;display:flex;gap:22px;align-items:center'>{azulejo(ip, 80, 40)}
  <div><div style='font-size:34px;font-weight:700;letter-spacing:-.03em'>{t}</div><div style='font-size:25px;color:{MUTED};margin-top:4px;line-height:1.3'>{s}</div></div></div>"""
    return f"""<div class='visual' style='margin-top:44px;display:grid;grid-template-columns:1fr 1fr;gap:22px'>
  {bloco(I_CARRO, 'IPVA', 'à vista ou parcelado')}
  {bloco(I_CASA, 'IPTU', 'em SP, a partir de fevereiro')}
  {bloco(I_LIVRO, 'Escola', 'material e matrícula')}
  {bloco(I_CARTAO, 'Parcelas', 'das compras de novembro')}
</div>
<div style='margin-top:34px'>{pilula(I_CAL, 'Segunda (07/12): o que chega junto.')}</div>"""


def post_dezembro():
    T = 7
    s = [capa_dezembro(T)]

    s.append(slide("light", EXTRA_D + topo(
        "Até 20/12 · 2ª parcela do 13º", "Menor que a 1ª, e tem motivo.",
        "É nela que saem o INSS e o IR do 13º inteiro. A lei diz até 20/12, um domingo em 2026: confira a data com a empresa.",
        estilo_p="font-size:36px;margin-top:24px") + v_segunda_parcela(), 2, T))

    s.append(slide("light", EXTRA_D + topo(
        "25/12 · Natal e festas", "Decida o teto antes das compras.",
        "Presentes, ceia, confraternização, roupa e viagem: escreva quanto cabe em cada um.",
        estilo_p="margin-top:24px") + v_teto_festas(), 3, T))

    fech = tela(P02, "celular-fechamentos-02-12.png")
    s.append(slide("light", EXTRA_D + topo(
        "31/12 · Lá fora", "Anote o saldo da carteira no último dia.",
        "Cada ano fecha com o saldo de 31/12 e a PTAX de compra do último dia útil.",
        cls="h3", estilo_p="font-size:36px;margin-top:20px")
        + f"<div class='visual' style='margin-top:34px'>{recorte(fech, 1702, 2633, largura=620, x0=51, x1=1119)}"
          f"<div class='nota' style='text-align:center'>Tela real do timtimcash (Remessas), com dados de exemplo.</div></div>", 4, T))

    s.append(slide("light", EXTRA_D + topo(
        "Logo depois · Janeiro", "Janeiro chega com as contas do ano.",
        "IPVA, IPTU, material escolar e as parcelas das compras de fim de ano.",
        estilo_p="margin-top:24px") + v_janeiro_vem(), 5, T))

    pend = tela(P02, "celular-pendentes-02-12.png")
    s.append(slide("light", EXTRA_D + topo(
        "No timtimcash", "A 2ª parcela já espera nos Pendentes.",
        "Lançada com a data, ela aparece no dia certo.",
        cls="h3", estilo_p="font-size:36px;margin-top:18px")
        + f"<div class='visual' style='margin-top:34px'>{recorte(pend, 2880, 3797, largura=690, x0=36, x1=1134)}{NOTA_TELA}</div>", 6, T))

    s.append(fechamento_verde("Dezembro, com data marcada.",
        "Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_dc1(h) for h in s]


# ============================================================================ 04/12 · Por que a 2ª parcela vem menor
def capa_parcela(T):
    W, H = 896, 100
    w2 = float(W * PARCELA2 / PARCELA1)          # 437,8 px
    wi = float(W * INSS / PARCELA1)              # 177,8 px
    wr = float(W * IR / PARCELA1)                # 280,4 px
    top2 = 236
    rot = f"font-size:30px;font-weight:700;color:{BRAND_DEEP}"
    val = f"font-size:40px;font-weight:700;letter-spacing:-.03em;color:{INK};font-variant-numeric:tabular-nums"
    vis = f"""<div class='visual' style='position:relative;height:{top2 + H + 176}px;margin-top:70px'>
  <div style='position:absolute;left:0;right:0;top:0;display:flex;justify-content:space-between;align-items:baseline'>
    <span style='{rot}'>1ª parcela</span><span style='{val}'>R$ 4.980</span></div>
  <div style='position:absolute;left:0;top:58px;width:{W}px;height:{H}px;border-radius:24px;background:{BRAND}'></div>
  <div style='position:absolute;left:0;top:{top2 - 58}px;display:flex;gap:18px;align-items:baseline'>
    <span style='{rot}'>2ª parcela</span><span style='{val};color:{BRAND_DARK}'>R$ 2.433,36</span></div>
  <div style='position:absolute;left:0;top:{top2}px;width:{w2:.1f}px;height:{H}px;border-radius:24px 6px 6px 24px;background:{BRAND}'></div>
  <div style='position:absolute;left:{w2 + 6:.1f}px;top:{top2}px;width:{W - w2 - 6:.1f}px;height:{H}px;border-radius:6px 24px 24px 6px;border:3px dashed {CORAL_CLARO};box-sizing:border-box'></div>
  <div style='position:absolute;left:{w2 + 10:.1f}px;top:{top2}px;width:{wi - 12:.1f}px;height:{H}px;border-radius:10px;background:{CORAL};transform:translate(-4px,66px) rotate(7deg);display:flex;align-items:center;justify-content:center;color:#fff;font-size:32px;font-weight:700'>INSS</div>
  <div style='position:absolute;left:{w2 + wi + 6:.1f}px;top:{top2}px;width:{wr - 10:.1f}px;height:{H}px;border-radius:10px 24px 24px 10px;background:{CORAL};transform:translate(8px,98px) rotate(-5deg);display:flex;align-items:center;justify-content:center;color:#fff;font-size:32px;font-weight:700'>IR</div>
  <div style='position:absolute;left:{w2 - 4:.1f}px;top:{top2 + H + 104}px;width:{wi + 20:.1f}px;text-align:center;font-size:28px;font-weight:700;color:{CORAL_TXT};font-variant-numeric:tabular-nums'>−R$ 988,09</div>
  <div style='position:absolute;left:{w2 + wi + 10:.1f}px;top:{top2 + H + 134}px;width:{wr - 10:.1f}px;text-align:center;font-size:28px;font-weight:700;color:{CORAL_TXT};font-variant-numeric:tabular-nums'>−R$ 1.558,55</div>
</div>"""
    corpo = f"""<div class='eyebrow'>13º salário</div>
<div class='h1' style='font-size:100px'>Por que a 2ª parcela vem menor?</div>{vis}"""
    return capa("suave", EXTRA_D + corpo, 1, T)


def v_cascata():
    """Cascata do 13º do exemplo: R$ 9.960 → − 1ª parcela − INSS − IR = 2ª parcela."""
    HC, W, G = 330, 136, 34
    esc = HC / float(SALARIO)
    apos1 = SALARIO - PARCELA1
    apos_inss = apos1 - INSS
    assert apos_inss - IR == PARCELA2
    passos = [  # rótulo, sub, de, até, valor, cor da barra, cor do valor
        ("13º inteiro", "salário do mês", D(0), SALARIO, "R$ 9.960", INK, INK),
        ("1ª parcela", "paga em 27/11", apos1, SALARIO, "−R$ 4.980", MENTA_CLARA, BRAND_DARK),
        ("INSS", "do 13º inteiro", apos_inss, apos1, "−R$ 988,09", CORAL, CORAL_TXT),
        ("IR", "do 13º inteiro", PARCELA2, apos_inss, "−R$ 1.558,55", CORAL, CORAL_TXT),
        ("2ª parcela", "em 18/12", D(0), PARCELA2, "R$ 2.433,36", BRAND, BRAND_DARK),
    ]
    colunas, fios = [], []
    for i, (rot, sub, de, ate, valor, cor, cor_v) in enumerate(passos):
        x = i * (W + G)
        y_base = HC - float(ate) * esc
        alt = float(ate - de) * esc
        forte = i == len(passos) - 1
        colunas.append(f"""<div style='position:absolute;left:{x}px;top:{y_base:.1f}px;width:{W}px;height:{alt:.1f}px;border-radius:12px;background:{cor}'></div>
<div style='position:absolute;left:{x - G / 2:.0f}px;width:{W + G}px;top:{y_base - 46:.1f}px;text-align:center;font-size:{28 if forte else 26}px;font-weight:700;color:{cor_v};font-variant-numeric:tabular-nums;white-space:nowrap'>{valor}</div>
<div style='position:absolute;left:{x - G / 2:.0f}px;width:{W + G}px;top:{HC + 20}px;text-align:center'>
  <div style='font-size:28px;font-weight:700;color:{INK}'>{rot}</div><div style='font-size:22px;font-weight:500;color:{MUTED};margin-top:4px'>{sub}</div></div>""")
        if i < len(passos) - 1:
            nivel = de if i > 0 else PARCELA1 * 2
            y = HC - float(de if i > 0 else SALARIO) * esc
            if i == 0:
                y = HC - float(SALARIO) * esc
            fios.append(f"<div style='position:absolute;left:{x + W}px;width:{G}px;top:{y:.1f}px;border-top:3px dashed {NEUTRO}'></div>")
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:64px 40px 30px'>
  <div style='position:relative;height:{HC + 92}px;width:{5 * W + 4 * G}px;margin:0 auto'>
    <div style='position:absolute;left:-10px;right:-10px;top:{HC}px;border-top:2px solid {FIO}'></div>
    {''.join(fios)}{''.join(colunas)}
  </div>
</div>
<div class='nota'>Exemplo: salário de R$ 9.960, sem dependentes. INSS e IR pelas tabelas de 2026 (gov.br/inss; Receita Federal).</div></div>"""


def v_escada_inss():
    alturas = [(D("7.5"), "7,5%", "até R$ 1.621,00", SOFT, BRAND_DEEP), (D("9"), "9%", "até R$ 2.902,84", MENTA_CLARA, BRAND_DEEP),
               (D("12"), "12%", "até R$ 4.354,27", BRAND, "#fff"), (D("14"), "14%", "até R$ 8.475,55", BRAND_DARK, "#fff")]
    W, G, K = 188, 14, 16
    degraus = []
    for i, (al, txt, faixa, cor, cor_t) in enumerate(alturas):
        h = float(al) * K
        degraus.append(f"""<div style='display:flex;flex-direction:column;justify-content:flex-end;width:{W}px'>
  <div style='height:{h:.0f}px;border-radius:16px 16px 6px 6px;background:{cor};display:flex;align-items:flex-start;justify-content:center;padding-top:18px;
    font-size:42px;font-weight:700;letter-spacing:-.03em;color:{cor_t}'>{txt}</div>
  <div style='font-size:23px;font-weight:600;color:{MUTED};text-align:center;margin-top:12px;white-space:nowrap'>{faixa}</div></div>""")
    teto_y = 14 * K
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:40px 40px 30px'>
  <div style='position:relative;display:flex;gap:{G}px;align-items:flex-end;justify-content:center;height:{teto_y + 62 + 44}px'>
    <div style='position:absolute;left:0;right:0;top:20px;border-top:3px dashed {INK}'></div>
    <div style='position:absolute;right:0;top:-18px;font-size:22px;font-weight:700;letter-spacing:.14em;color:{INK}'>TETO · R$ 8.475,55</div>
    {''.join(degraus)}
  </div>
  <div style='display:flex;justify-content:space-between;align-items:center;margin-top:24px;padding-top:22px;border-top:2px solid {FIO}'>
    <span style='font-size:29px;font-weight:600;color:{INK};line-height:1.3'>R$ 9.960 passa do teto:<br><span style='color:{MUTED};font-weight:500'>o INSS do 13º para no máximo.</span></span>
    <span class='big' style='font-size:64px;color:{CORAL_FORTE}'>R$ 988,09</span></div>
</div>
<div class='nota'>Tabela de 2026 (Portaria Interministerial MPS/MF nº 13/2026; gov.br/inss). Lei 8.620/1993, art. 7º, §2º; Decreto 3.048/1999, art. 214.</div></div>"""


def v_conta_ir():
    def linha(sinal, rot, valor, cor=INK, forte=False, borda=False):
        b = f"border-top:2px solid {FIO};padding-top:20px;margin-top:6px;" if borda else ""
        tam = 56 if forte else 38
        return f"""<div style='display:grid;grid-template-columns:54px 1fr auto;align-items:baseline;{b}'>
  <span style='font-size:38px;font-weight:700;color:{MUTED}'>{sinal}</span>
  <span style='font-size:{30 if not forte else 32}px;font-weight:{700 if forte else 500};color:{INK if forte else MUTED}'>{rot}</span>
  <span class='tab' style='font-size:{tam}px;font-weight:700;letter-spacing:-.03em;color:{cor}'>{valor}</span></div>"""
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:36px 46px 36px;display:flex;flex-direction:column;gap:18px'>
  {linha('', '13º inteiro', 'R$ 9.960,00')}
  {linha('−', 'INSS do 13º', 'R$ 988,09')}
  {linha('=', 'base do IR', 'R$ 8.971,91', borda=True)}
  {linha('×', 'alíquota da faixa de cima', '27,5%')}
  {linha('−', 'parcela a deduzir', 'R$ 908,73')}
  {linha('=', 'IR do 13º', 'R$ 1.558,55', CORAL_FORTE, True, True)}
</div>
<div class='nota'>Tabela mensal de 2026 (Receita Federal), sem dependentes. Acima de R$ 7.350, a redução de 2026 não vale. Lei 8.134/1990, art. 16.</div></div>"""


def v_novidade():
    def cartao(sal, ir_txt, cor_ir, extra, p2):
        return f"""<div class='card' style='flex:1;padding:34px 34px 30px'>
  <div class='rs'>Salário de {sal}</div>
  <div class='big' style='font-size:84px;line-height:1;color:{cor_ir};margin-top:18px'>{ir_txt}</div>
  <div style='font-size:27px;font-weight:600;color:{INK};margin-top:10px'>de IR no 13º</div>
  <div style='font-size:25px;font-weight:500;color:{MUTED};margin-top:8px;min-height:34px'>{extra}</div>
  <div style='margin-top:22px;padding-top:20px;border-top:2px solid {FIO};font-size:25px;color:{MUTED}'>2ª parcela<br>
    <b class='tab' style='font-size:36px;color:{INK};letter-spacing:-.02em'>{p2}</b></div></div>"""
    return f"""<div class='visual' style='margin-top:44px;display:flex;gap:24px'>
  {cartao('R$ 4.500', 'R$ 0', BRAND_DARK, 'a redução zera o imposto', brl(EX45_P2))}
  {cartao('R$ 6.000', brl(EX6_IR), CORAL_FORTE, f"sem a redução, <s>{brl(EX6_IR_TAB)}</s>", brl(EX6_P2))}
</div>
<div class='nota'>Exemplos sem dependentes. Lei 15.270/2025 (Lei 9.250/1995, art. 3º-A, §3º); Receita Federal, tabelas de 2026.</div>"""


def post_parcela():
    T = 7
    s = [capa_parcela(T)]

    s.append(slide("light", EXTRA_D + topo(
        "A conta do exemplo", "Os descontos do 13º inteiro saem da 2ª.",
        "A 1ª parcela vem sem desconto. A\u00a02ª paga o INSS e o IR do 13º todo.",
        estilo_p="font-size:36px;margin-top:22px") + v_cascata(), 2, T))

    s.append(slide("light", EXTRA_D + topo(
        "INSS do 13º", "Uma conta só dele, com teto.",
        "Não se soma ao salário do mês: cada alíquota vale na sua faixa.",
        estilo_p="font-size:36px;margin-top:22px") + v_escada_inss(), 3, T))

    s.append(slide("light", EXTRA_D + topo(
        "IR do 13º", "Na fonte, sem somar com o salário.",
        "O imposto do 13º é calculado sozinho, na 2ª parcela.",
        estilo_p="font-size:36px;margin-top:22px") + v_conta_ir(), 4, T))

    s.append(slide("light", EXTRA_D + topo(
        "Novidade de 2026", "Até R$ 5 mil, IR zero também no 13º.",
        "Entre R$ 5 mil e R$ 7.350, o imposto diminui.",
        estilo_p="font-size:36px;margin-top:22px") + v_novidade(), 5, T))

    form = tela(P04, "celular-nova-receita-2a-parcela-04-12.png")
    s.append(slide("light", EXTRA_D + topo(
        "No timtimcash", "Lance a 2ª parcela antes de ela cair.",
        "Com a data e sem marcar como recebida: fica em Pendentes e já entra no Previsto do mês.",
        cls="h3", estilo_p="font-size:34px;margin-top:18px")
        + f"<div class='visual' style='margin-top:32px'>{recorte(form, 1305, 2510, largura=560)}{NOTA_TELA}</div>", 6, T))

    s.append(fechamento_verde("A 2ª parcela, sem surpresa.",
        "Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_dc1(h) for h in s]


# ============================================================================ 07/12 · Janeiro caro: o que chega junto
FIXAS_JAN = D("2300.00") + D("1450.00") + D("55.90") + D("21.90") + D("42.00")
IPVA27, MATERIAL27, NOTEBOOK_PARC = D("1236.00"), D("940.00"), D("360.00")
JAN27 = FIXAS_JAN + IPVA27 + MATERIAL27 + NOTEBOOK_PARC
DESP_MEDIA = D("8419.65")                  # Visão geral, "Despesa média" (Dez/25 a Nov/26), relógio em 07/12/2026
assert FIXAS_JAN == D("3869.80") and JAN27 == D("6405.80")
PCT_JAN = (JAN27 / DESP_MEDIA * 100).quantize(D("1"), ROUND_HALF_UP)
assert PCT_JAN == D("76")
SOBRA_13 = PARCELA2 - IPVA27 - MATERIAL27
assert SOBRA_13 == D("257.36")


def capa_janeiro(T):
    """Um "J" grande feito de blocos empilhados ao longo do traço: IPVA, IPTU, escola, parcelas e fatura."""
    import math
    S, R = 150, 172                      # largura do traço e raio da curva
    cx, cy = 288, 418                    # centro da curva; a haste fica em x = cx + R
    hx = cx + R
    caminho = f"M{hx} 0 V{cy} A{R} {R} 0 0 1 {cx - R} {cy} V{cy - 92}"
    haste, arco, ponta = cy, math.pi * R, 92
    total = haste + arco + ponta
    gap = 12
    cortes = [(0, 150, CORAL, "IPVA", "#fff", 44), (150, 292, AMBER, "IPTU", INK, 40), (292, 470, INK, "Escola", "#fff", 38),
              (470, 805, CORAL_FORTE, "Parcelas", "#fff", 38), (805, total, CORAL_CLARO, "Fatura", INK, 32)]

    def ponto(d):
        if d <= haste:
            return hx, d
        if d <= haste + arco:
            a = (d - haste) / R
            return cx + R * math.cos(a), cy + R * math.sin(a)
        return cx - R, cy - (d - haste - arco)
    tracos, textos = [], []
    for i, (a, b, cor, txt, cor_t, tam) in enumerate(cortes):
        a2 = a + (gap / 2 if i else 0)
        b2 = b - (gap / 2 if i < len(cortes) - 1 else 0)
        tracos.append(f"<path d='{caminho}' fill='none' stroke='{cor}' stroke-width='{S}' stroke-dasharray='{b2 - a2:.1f} {total + 400:.1f}' stroke-dashoffset='{-a2:.1f}'/>")
        x, y = ponto((a + b) / 2)
        if txt == "Escola":
            x, y = ponto(372)
        if txt == "Fatura":
            x, y = ponto(total - 40)
        textos.append(f"<text x='{x:.1f}' y='{y + tam * .36:.1f}' text-anchor='middle' fill='{cor_t}' "
                      f"style='font-family:Inter;font-weight:700;font-size:{tam}px;letter-spacing:-.02em'>{txt}</text>")
    alt = cy + R + S / 2
    larg = hx + S / 2
    svg = (f"<svg width='{larg:.0f}' height='{alt:.0f}' viewBox='0 0 {larg:.0f} {alt:.0f}' style='display:block'>"
           f"{''.join(tracos)}{''.join(textos)}</svg>")
    corpo = f"""<div class='eyebrow'>Começo do ano</div>
<div class='h1' style='font-size:98px'>Janeiro caro:<br>o que chega junto.</div>
<div class='visual' style='margin-top:44px;display:flex;justify-content:flex-end;padding-right:30px'>{svg}</div>"""
    return capa("papel", EXTRA_D + corpo, 1, T)


def v_impostos():
    meses = ["jan", "fev", "mar", "abr", "mai", "jun"]
    C = 136

    def opcao(ini, n, cor, txt, seta=False):
        ponta = (f"<span style='position:absolute;right:-38px;top:-7px;color:{CORAL_TXT}'>{svg_icone(I_SETA, 30, CORAL_TXT, 2.4)}</span>"
                 if seta else "")
        return f"""<div style='position:relative'>
  <div style='margin-left:{ini * C + 2}px;font-size:25px;font-weight:600;color:{INK};white-space:nowrap'>{txt}</div>
  <div style='position:relative;margin:8px 0 0 {ini * C}px;width:{n * C - (46 if seta else 6)}px;height:16px;border-radius:8px;background:{cor}'>{ponta}</div></div>"""

    def grupo(titulo, sub, linhas):
        return f"""<div style='margin-top:24px'>
  <div style='display:flex;align-items:baseline;gap:14px'><span style='font-size:34px;font-weight:700;letter-spacing:-.03em'>{titulo}</span>
    <span style='font-size:23px;font-weight:600;color:{MUTED}'>{sub}</span></div>
  <div style='display:flex;flex-direction:column;gap:14px;margin-top:12px'>{''.join(linhas)}</div></div>"""
    cab = "".join(f"<span style='width:{C}px;padding-left:4px;font-size:22px;font-weight:700;letter-spacing:.12em;color:{MUTED}'>{m.upper()}</span>" for m in meses)
    return f"""<div class='visual' style='margin-top:36px'><div class='card' style='padding:28px 40px 32px'>
  <div style='display:flex;border-bottom:2px solid {FIO};padding-bottom:12px'>{cab}</div>
  {grupo('IPVA', 'estado de São Paulo, 2026', [opcao(0, 1, BRAND, 'à vista, com 3% de desconto'), opcao(1, 1, MENTA_CLARA, 'à vista, sem desconto'),
                                                  opcao(0, 5, CORAL_CLARO, '5 parcelas, de janeiro a maio')])}
  {grupo('IPTU', 'cidade de São Paulo, 2026', [opcao(1, 1, BRAND, 'à vista, com 3% de desconto'),
                                                 opcao(1, 5, CORAL_CLARO, '10 parcelas, a primeira em fevereiro', seta=True)])}
</div>
<div class='nota'>Regras de 2026: Decreto estadual 70.087/2025 (IPVA) e Prefeitura de São Paulo (IPTU). Confira o calendário de 2027 do seu estado e da sua cidade.</div></div>"""


def v_tambem():
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:14px 44px'>
  <style>.linha-item{{padding:30px 0}} .linha-item .t{{font-size:40px}} .linha-item .s{{font-size:29px}}</style>
  {item(I_LIVRO, 'Material escolar e matrícula', 'No exemplo, R$ 940 de material, com vencimento em 12/01.', 100, 50)}
  {item(I_CARTAO, 'Parcelas da Black Friday', 'O notebook em 10x: a 3ª parcela, R$ 360, cai em 27/01.', 100, 50)}
  {item(I_PRESENTE, 'Fatura das festas', 'O que vai no cartão em dezembro pode vencer só em janeiro.', 100, 50)}
</div></div>"""


def v_janeiro_previsto(caminho):
    partes = [("Fixas", FIXAS_JAN, INK, "#fff"), ("IPVA", IPVA27, CORAL, "#fff"), ("Material", MATERIAL27, AMBER, INK),
              ("Notebook", NOTEBOOK_PARC, CORAL_FORTE, "#fff")]
    W = 816
    esc = W / float(DESP_MEDIA)
    segs = "".join(f"<div style='width:{float(v) * esc:.1f}px;height:58px;background:{c};display:flex;align-items:center;justify-content:center;"
                   f"color:{ct};font-size:22px;font-weight:700;white-space:nowrap;overflow:hidden'>{r if float(v) * esc > 96 else ''}</div>"
                   for r, v, c, ct in partes)
    leg = " + ".join(f"<b style='color:{INK}'>{r.lower() if r != 'IPVA' else r}</b> {brl(v, cent=False) if v == int(v) else brl(v)}" for r, v, _, _ in partes)
    return f"""<div class='visual' style='margin-top:28px'>{recorte(caminho, 1252, 1878, largura=600, x0=42, x1=1128)}
  <div style='font-size:22px;font-weight:500;color:{MUTED};text-align:center;margin-top:12px'>Tela real do timtimcash, com dados de exemplo.</div>
  <div class='card' style='padding:24px 40px 22px;margin-top:20px'>
    <div style='display:flex;justify-content:space-between;align-items:baseline'><span class='rs'>Janeiro de 2027, visto em 07/12</span>
      <span style='font-size:24px;font-weight:700;color:{MUTED}'>{PCT_JAN}% da despesa média</span></div>
    <div style='position:relative;margin-top:16px;height:58px;border-radius:14px;background:{FIO};overflow:hidden;display:flex;gap:3px'>{segs}</div>
    <div style='font-size:23px;line-height:1.4;color:{MUTED};margin-top:14px'>{leg} = <b style='color:{INK}'>R$ 6.405,80</b>, contra uma despesa média de R$ 8.419,65 por mês.</div>
  </div></div>"""


def v_cobre():
    W = 816
    esc = W / float(PARCELA2)
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:36px 40px 34px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'><span style='font-size:29px;font-weight:700'>2ª parcela do 13º · 18/12</span>
    <span class='tab' style='font-size:34px;font-weight:700;color:{BRAND_DARK}'>R$ 2.433,36</span></div>
  <div style='height:62px;border-radius:16px;background:{BRAND};margin-top:14px'></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;margin-top:34px'><span style='font-size:29px;font-weight:700'>IPVA + material · janeiro</span>
    <span class='tab' style='font-size:34px;font-weight:700;color:{CORAL_TXT}'>R$ 2.176,00</span></div>
  <div style='display:flex;gap:4px;margin-top:14px'>
    <div style='width:{float(IPVA27) * esc:.1f}px;height:62px;border-radius:16px 6px 6px 16px;background:{CORAL};color:#fff;font-size:24px;font-weight:700;display:flex;align-items:center;padding-left:20px'>IPVA R$ 1.236</div>
    <div style='width:{float(MATERIAL27) * esc - 4:.1f}px;height:62px;border-radius:6px 16px 16px 6px;background:{AMBER};color:{INK};font-size:24px;font-weight:700;display:flex;align-items:center;padding-left:20px'>Material R$ 940</div>
  </div>
  <div style='display:flex;justify-content:space-between;align-items:center;margin-top:30px;padding-top:24px;border-top:2px solid {FIO}'>
    <span style='font-size:29px;font-weight:600;color:{INK}'>Sobra, se ela for para janeiro</span>
    <span class='big' style='font-size:56px;color:{BRAND_DARK}'>R$ 257,36</span></div>
</div>
<div class='nota'>Conta do exemplo: 2ª parcela de R$ 2.433,36; IPVA 2027 de R$ 1.236 e material escolar de R$ 940, lançados em dezembro.</div></div>"""


def post_janeiro():
    T = 7
    s = [capa_janeiro(T)]

    saz = tela(P07, "celular-relatorios-sazonalidade-07-12.png")
    s.append(slide("light", EXTRA_D + topo(
        "Na conta do exemplo", "Janeiro só perde para dezembro.",
        "Na Sazonalidade, janeiro de 2026 levou R$ 9.420, com IPVA e IPTU.",
        cls="h3", estilo_p="font-size:36px;margin-top:20px")
        + f"<div class='visual' style='margin-top:30px'>{recorte(saz, 0, 1038, largura=600, raio=28)}{NOTA_TELA}</div>", 2, T))

    s.append(slide("light", EXTRA_D + topo(
        "IPVA e IPTU", "À vista com desconto, ou em parcelas.") + v_impostos(), 3, T))

    s.append(slide("light", EXTRA_D + topo(
        "Também no começo do ano", "Escola, parcelas e a fatura das festas.",
        estilo_t="margin-bottom:0") + v_tambem(), 4, T))

    vis = tela(P07, "celular-visao-geral-janeiro-2027-previsto-07-12.png")
    s.append(slide("light", EXTRA_D + topo(
        "No timtimcash", "Veja janeiro antes de ele chegar.",
        "Em Previsto, a Visão geral soma o que já tem data em janeiro de 2027.",
        cls="h3", estilo_p="font-size:34px;margin-top:16px") + v_janeiro_previsto(vis), 5, T))

    s.append(slide("light", EXTRA_D + topo(
        "Antes de gastar o 13º", "A 2ª parcela cobre o IPVA e o material.",
        "Na conta do exemplo, com sobra. Olhar janeiro antes ajuda a decidir.",
        estilo_p="font-size:36px;margin-top:22px") + v_cobre(), 6, T))

    s.append(fechamento_verde("Janeiro chega. Você já sabe quanto.",
        "Previsto no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_dc1(h) for h in s]


# ============================================================================ 10/12 · O preço do dinheiro emprestado
# Banco Central, estatísticas monetárias e de crédito, agosto de 2026 (nota de 29/9/2026), pessoa física; séries SGS
# lidas em api.bcb.gov.br em 16/10/2026 (% ao mês e % ao ano). Imobiliário: crédito direcionado, taxas de mercado.
TAXAS = [  # curto, completo, % a.m., % a.a., SGS a.m., SGS a.a.
    ("Rotativo do cartão", "Cartão de crédito rotativo", D("15.18"), D("444.89"), 25477, 22022),
    ("Parcelado do cartão", "Cartão de crédito parcelado", D("9.34"), D("192.08"), 25478, 22023),
    ("Cheque especial", "Cheque especial", D("7.43"), D("136.41"), 25463, 20741),
    ("Crédito pessoal", "Crédito pessoal não consignado", D("6.39"), D("110.22"), 25464, 20742),
    ("Consignado privado", "Consignado para trabalhadores do setor privado", D("3.79"), D("56.34"), 25466, 20744),
    ("Veículos", "Aquisição de veículos", D("1.97"), D("26.42"), 25471, 20749),
    ("Consignado público", "Consignado para trabalhadores do setor público", D("1.82"), D("24.14"), 25467, 20745),
    ("Consignado INSS", "Consignado para aposentados e pensionistas do INSS", D("1.82"), D("24.12"), 25468, 20746),
    ("Imobiliário", "Financiamento imobiliário com taxas de mercado", D("1.12"), D("14.24"), 25497, 20772),
]
assert [t[3] for t in TAXAS] == sorted([t[3] for t in TAXAS], reverse=True)
MAX_AA, MIN_AA = TAXAS[0][3], TAXAS[-1][3]
VEZES = int(MAX_AA / MIN_AA)
assert VEZES == 31
MIL = D("1000")
ROT_12 = MIL * (1 + MAX_AA / 100)            # R$ 5.448,90 pela taxa
IMOB_12 = MIL * (1 + MIN_AA / 100)           # R$ 1.142,40
TETO_ROT = MIL * 2                           # juros e encargos até o valor da dívida
assert (ROT_12, IMOB_12, TETO_ROT - IMOB_12) == (D("5448.90"), D("1142.40"), D("857.60"))
# exemplo do slide 6: R$ 1.000 em 12 parcelas iguais à taxa média do crédito pessoal (6,39% ao mês), sem IOF e tarifas
_i = D("0.0639")
PARC_PESSOAL = q2(MIL * _i / (1 - (1 + _i) ** -12))
TOTAL_PESSOAL = PARC_PESSOAL * 12
assert (PARC_PESSOAL, TOTAL_PESSOAL) == (D("121.84"), D("1462.08"))


def capa_juros(T):
    W, H, G = 896, 44, 16
    barras = []
    for i, (curto, _, am, aa, _, _) in enumerate(TAXAS):
        w = float(aa / MAX_AA) * W
        if i == 0:
            barras.append(f"<div style='width:{w:.0f}px;height:{H + 22}px;border-radius:16px;background:{CORAL};display:flex;align-items:center;justify-content:flex-end;"
                          f"padding-right:24px;color:#fff;font-size:32px;font-weight:700;letter-spacing:-.02em'>444,89% ao ano</div>")
        elif i == len(TAXAS) - 1:
            barras.append(f"<div style='display:flex;align-items:center;gap:16px'><div style='width:{w:.0f}px;height:{H}px;border-radius:12px;background:{BRAND}'></div>"
                          f"<span style='font-size:30px;font-weight:700;color:{BRAND_DEEP}'>14,24%</span></div>")
        else:
            barras.append(f"<div style='width:{max(w, 24):.0f}px;height:{H}px;border-radius:12px;background:{BRAND_DEEP}'></div>")
    corpo = f"""<div class='eyebrow'>Juros do crédito</div>
<div class='h1' style='font-size:100px'>O preço do dinheiro emprestado.</div>
<div class='visual' style='margin-top:60px;display:flex;flex-direction:column;gap:{G}px'>{''.join(barras)}</div>"""
    return capa("suave", EXTRA_D + corpo, 1, T)


def v_ranking():
    trilho = 360
    linhas = []
    for i, (curto, _, am, aa, _, _) in enumerate(TAXAS):
        w = float(aa / MAX_AA) * trilho
        cor = CORAL if i == 0 else (BRAND if i == len(TAXAS) - 1 else NEUTRO)
        cor_v = CORAL_FORTE if i == 0 else (BRAND_DARK if i == len(TAXAS) - 1 else INK)
        borda = f"border-top:2px solid {FIO};" if i else ""
        linhas.append(f"""<div style='display:grid;grid-template-columns:270px {trilho}px 1fr;align-items:center;column-gap:20px;padding:7px 0;{borda}'>
  <div><div style='font-size:26px;font-weight:700;letter-spacing:-.02em;line-height:1.15'>{curto}</div>
    <div style='font-size:21px;font-weight:500;color:{MUTED};margin-top:2px'>{pct(am, 2)} ao mês</div></div>
  <div style='height:24px'><div style='width:{max(w, 6):.1f}px;height:24px;border-radius:7px;background:{cor}'></div></div>
  <div class='tab' style='text-align:right;font-size:{32 if i in (0, len(TAXAS) - 1) else 28}px;font-weight:700;letter-spacing:-.02em;color:{cor_v}'>{pct(aa, 2)}</div></div>""")
    return f"""<div class='visual' style='margin-top:30px'><div class='card' style='padding:12px 40px 12px'>{''.join(linhas)}</div>
<div class='nota'>Pessoa física, agosto de 2026. Banco Central, nota de 29/9/2026. Imobiliário: taxas de mercado.</div></div>"""


def v_mes_ano():
    exemplos = [TAXAS[3], TAXAS[2], TAXAS[0]]
    linhas = []
    for i, (curto, _, am, aa, _, _) in enumerate(exemplos):
        borda = f"border-top:2px solid {FIO};" if i else ""
        linhas.append(f"""<div style='padding:20px 0;{borda}'>
  <div class='rs'>{curto}</div>
  <div style='display:flex;align-items:center;gap:22px;margin-top:10px'>
    <span class='tab' style='font-size:44px;font-weight:700;letter-spacing:-.03em;color:{INK};white-space:nowrap'>{pct(am, 2)} <span style='font-size:26px;color:{MUTED};font-weight:600'>ao mês</span></span>
    {svg_icone(I_SETA, 40, MUTED, 2.2)}
    <span class='tab' style='font-size:58px;font-weight:700;letter-spacing:-.04em;color:{CORAL_FORTE};white-space:nowrap'>{pct(aa, 2)} <span style='font-size:26px;color:{CORAL_TXT};font-weight:600;letter-spacing:0'>ao ano</span></span></div>
  <div style='font-size:24px;color:{MUTED};margin-top:6px'>e não 12 × {pct(am, 2)} = {pct(am * 12, 2)}</div></div>""")
    return f"""<div class='visual' style='margin-top:36px'><div class='card' style='padding:4px 44px'>{''.join(linhas)}</div>
<div class='nota'>Taxas médias de agosto de 2026, pessoa física (Banco Central).</div></div>"""


def v_mil_reais():
    W = 816
    esc = W / float(ROT_12)
    p_mil = float(MIL) * esc
    j_imob = float(IMOB_12 - MIL) * esc
    teto = float(TETO_ROT) * esc
    resto = float(ROT_12 - TETO_ROT) * esc
    listra = f"repeating-linear-gradient(135deg,{CORAL_CLARO} 0 12px,#F6D9CC 12px 24px)"
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:34px 40px 30px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'><span style='font-size:28px;font-weight:700'>Imobiliário <span style='color:{MUTED};font-weight:500'>· 14,24% ao ano</span></span>
    <span class='tab' style='font-size:36px;font-weight:700;color:{BRAND_DARK}'>R$ 1.142,40</span></div>
  <div style='display:flex;gap:3px;margin-top:12px'><div style='width:{p_mil:.1f}px;height:50px;border-radius:12px 4px 4px 12px;background:{INK}'></div>
    <div style='width:{j_imob:.1f}px;height:50px;border-radius:4px 12px 12px 4px;background:{BRAND}'></div></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;margin-top:34px'><span style='font-size:28px;font-weight:700'>Rotativo <span style='color:{MUTED};font-weight:500'>· 444,89% ao ano</span></span>
    <span class='tab' style='font-size:26px;font-weight:600;color:{MUTED}'>pela taxa, <s>R$ 5.448,90</s></span></div>
  <div style='position:relative;margin-top:12px;height:50px;display:flex;gap:3px'>
    <div style='width:{p_mil:.1f}px;height:50px;border-radius:12px 4px 4px 12px;background:{INK}'></div>
    <div style='width:{teto - p_mil - 3:.1f}px;height:50px;border-radius:4px;background:{CORAL}'></div>
    <div style='width:{resto - 3:.1f}px;height:50px;border-radius:4px 12px 12px 4px;background:{listra}'></div>
    <div style='position:absolute;left:{teto - 1:.1f}px;top:-14px;height:78px;border-left:4px solid {INK}'></div>
  </div>
  <div style='position:relative;height:40px;margin-top:8px'>
    <span style='position:absolute;left:{teto + 12:.1f}px;white-space:nowrap;font-size:24px;font-weight:700;color:{INK}'>teto: R$ 2.000</span></div>
  <div style='display:flex;gap:26px;margin-top:10px;font-size:22px;font-weight:600;color:{MUTED}'>
    <span style='display:flex;align-items:center;gap:8px'><i style='width:20px;height:20px;border-radius:5px;background:{INK};display:block'></i>a dívida, R$ 1.000</span>
    <span style='display:flex;align-items:center;gap:8px'><i style='width:20px;height:20px;border-radius:5px;background:{CORAL};display:block'></i>juros até o teto</span>
    <span style='display:flex;align-items:center;gap:8px'><i style='width:20px;height:20px;border-radius:5px;background:{listra};display:block'></i>o que o teto corta</span></div>
  <div style='display:flex;justify-content:space-between;align-items:center;margin-top:24px;padding-top:22px;border-top:2px solid {FIO}'>
    <span style='font-size:29px;font-weight:600;line-height:1.3'>Mesmo com o teto,<br><span style='color:{MUTED};font-weight:500'>o rotativo custa a mais</span></span>
    <span class='big' style='font-size:60px;color:{CORAL_FORTE}'>R$ 857,60</span></div>
</div>
<div class='nota'>Conta simples: só juros, sem IOF e tarifas. No contrato, compare o CET, que soma tudo (Res. CMN 4.881/2020).</div></div>"""


def v_tetos():
    def cartao(ip, rot, grande, texto, rodape, extra=""):
        return f"""<div class='card' style='padding:28px 40px 26px'>
  <div style='display:flex;align-items:center;gap:18px'>{azulejo(ip, 72, 36)}<span style='font-size:30px;font-weight:700;letter-spacing:-.02em'>{rot}</span></div>
  <div style='display:flex;align-items:baseline;gap:20px;margin-top:14px'>
    <span class='big' style='font-size:68px;line-height:1;color:{CORAL_FORTE}'>{grande}</span>
    <span style='font-size:28px;line-height:1.3;color:{INK}'>{texto}</span></div>{extra}
  <div style='font-size:23px;font-weight:600;color:{MUTED};margin-top:12px'>{rodape}</div></div>"""
    regua = f"""<div style='position:relative;margin-top:22px;height:30px;border-radius:15px;background:{FIO}'>
    <div style='position:absolute;left:0;top:0;bottom:0;width:{7.43 / 8 * 100:.2f}%;border-radius:15px;background:{CORAL}'></div>
    <div style='position:absolute;right:0;top:-8px;height:46px;border-left:4px solid {INK}'></div></div>
  <div style='display:flex;justify-content:space-between;margin-top:10px;font-size:23px;font-weight:700'>
    <span style='color:{CORAL_TXT}'>média de agosto de 2026: 7,43%</span><span style='color:{INK}'>teto: 8%</span></div>"""
    return f"""<div class='visual' style='margin-top:34px;display:flex;flex-direction:column;gap:18px'>
  {cartao(I_CARTAO, 'Rotativo e parcelamento da fatura', 'R$ 1.000', 'de dívida viram,<br>no máximo, R$ 2.000.', 'Juros e encargos, somados, até o valor da dívida · desde 3/1/2024 · Lei 14.690/2023, art. 28')}
  {cartao(I_BANCO, 'Cheque especial', '8%', 'ao mês,<br>no máximo.', 'Desde 6/1/2020 · Res. CMN 4.765/2019, art. 3º', regua)}
</div>"""


def post_juros():
    T = 7
    s = [capa_juros(T)]

    s.append(slide("light", EXTRA_D + topo(
        "Taxa média ao ano · agosto de 2026", f"A mais cara é {VEZES} vezes a mais barata.", cls="h3") + v_ranking(), 2, T))

    s.append(slide("light", EXTRA_D + topo(
        "Ao mês e ao ano", "Ao mês parece pouco. No ano, não.",
        "Os juros de um mês entram na dívida do mês seguinte.",
        estilo_p="font-size:36px;margin-top:22px") + v_mes_ano(), 3, T))

    s.append(slide("light", EXTRA_D + topo(
        "R$ 1.000 por 12 meses", "O mais barato e o mais caro, em reais.",
        "Sem pagar nada no meio, só com os juros de cada taxa média.",
        estilo_p="font-size:36px;margin-top:22px") + v_mil_reais(), 4, T))

    s.append(slide("light", EXTRA_D + topo("Os tetos", "Dois limites que já estão na lei.") + v_tetos(), 5, T))

    form = tela(P10, "celular-nova-despesa-parcelada-10-12.png")
    esq = f"""<div style='flex:1;padding-top:6px'>
  <div class='eyebrow'>No timtimcash</div>
  <div class='h3' style='font-size:52px'>Lance o total. As parcelas aparecem mês a mês.</div>
  <div class='p' style='font-size:28px;margin-top:20px'>Em “Dívidas e empréstimos”, com Recorrência “Parcelada”, cada parcela fica em Pendentes no mês dela.</div>
  <div style='margin-top:26px;padding:20px 22px;border-radius:22px;background:{SOFT};font-size:24px;line-height:1.38;color:{BRAND_DEEP}'>
    <b>Exemplo:</b> R$ 1.000 no crédito pessoal, à taxa média (6,39% ao mês), em 12 parcelas: 12 × {brl(PARC_PESSOAL)} = <b>{brl(TOTAL_PESSOAL)}</b>.</div>
</div>"""
    dir_ = f"<div style='flex:none;width:500px'>{recorte(form, 1015, 2765, largura=500)}<div class='nota' style='text-align:center;font-size:21px'>Tela real do timtimcash, com dados de exemplo.</div></div>"
    s.append(slide("light", EXTRA_D + f"<div style='display:flex;gap:36px;align-items:center'>{esq}{dir_}</div>", 6, T))

    s.append(fechamento_verde("Antes de assinar, faça a conta inteira.",
        "Dívidas e empréstimos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_dc1(h) for h in s]


# ============================================================================ 12/12 · 8 siglas do seu dinheiro
SIGLAS = ["PTAX", "CDI", "Selic", "IPCA", "IOF", "VET", "TIR", "CET"]
# revisão 16/10: "rotativo" não é sigla; no lugar dele, o CET (custo efetivo total, Res. CMN 4.881/2020)
I_CONTRATO = '<path d="M6.5 3.5h8l3 3v14h-11z"/><path d="M14.5 3.5v3h3"/><path d="M9 11h6M9 14.5h6M9 18h3.5"/>'


def capa_siglas(T):
    linhas = [["PTAX", "CDI", "Selic"], ["IPCA", "IOF", "VET"], ["TIR", "CET"]]
    pilulas = []
    for i, ln in enumerate(linhas):
        itens = "".join(f"<span style='display:inline-flex;align-items:center;height:128px;padding:0 46px;border-radius:999px;"
                        f"background:#fff;color:{BRAND_DEEP};font-size:76px;font-weight:700;letter-spacing:-.035em'>{s}</span>" for s in ln)
        recuo = [0, 62, 24][i]
        pilulas.append(f"<div style='display:flex;gap:22px;margin-left:{recuo}px'>{itens}</div>")
    corpo = f"""<div class='eyebrow'>Glossário para salvar</div>
<div class='h1' style='font-size:100px'>8 siglas do seu dinheiro.</div>
<div class='visual' style='margin-top:64px;display:flex;flex-direction:column;gap:24px'>{''.join(pilulas)}</div>"""
    return capa("verde", EXTRA_D + corpo, 1, T)


def sigla(nome, extenso, ip, frase, exemplo):
    return f"""<div class='card' style='padding:30px 38px 30px;display:flex;gap:28px;align-items:flex-start'>
  {azulejo(ip, 92, 46)}
  <div style='flex:1'>
    <div style='display:flex;align-items:baseline;gap:16px;flex-wrap:wrap'>
      <span style='font-size:62px;font-weight:700;letter-spacing:-.04em;line-height:1;color:{INK}'>{nome}</span>
      <span style='font-size:23px;font-weight:600;color:{MUTED}'>{extenso}</span></div>
    <div style='font-size:30px;line-height:1.36;color:{INK};margin-top:14px'>{frase}</div>
    <div style='font-size:26px;line-height:1.38;color:{MUTED};margin-top:12px'><b style='color:{BRAND_DARK}'>No dia a dia:</b> {exemplo}</div>
  </div></div>"""


def par(sobre, titulo, a, b, fonte):
    return EXTRA_D + topo(sobre, titulo, cls="h3", estilo_t="font-size:58px") + f"""
<div class='visual' style='margin-top:32px;display:flex;flex-direction:column;gap:20px'>{a}{b}</div>
<div class='nota'>{fonte}</div>"""


def v_onde(caminho):
    linhas = [("PTAX", "Remessas: “Atualizar carteira” e o fechamento de cada ano"),
              ("TIR", "Remessas: “Ritmo do retorno”"),
              ("CDI", "Remessas: “Contra o CDI”"),
              ("IOF", "Nova remessa e “IOF pago”"),
              ("VET", "a mesma ideia do “Câmbio médio efetivo”")]
    itens = "".join(f"""<div style='display:flex;align-items:center;gap:20px;padding:12px 0;{"border-top:2px solid " + FIO + ";" if i else ""}'>
  <span style='flex:none;width:118px;text-align:center;padding:8px 0;border-radius:999px;background:{SOFT};color:{BRAND_DEEP};font-size:26px;font-weight:700'>{s}</span>
  <span style='font-size:27px;font-weight:600;color:{INK};line-height:1.3'>{t}</span></div>""" for i, (s, t) in enumerate(linhas))
    return f"""<div class='visual' style='margin-top:30px'><div class='card' style='padding:10px 36px'>{itens}</div>
  <div style='margin-top:24px'>{recorte(caminho, 5062, 5578, largura=700, x0=42, x1=1128)}</div>
  <div class='nota' style='text-align:center'>Tela real do timtimcash (Remessas em euro), com dados de exemplo.</div></div>"""


def post_siglas():
    T = 7
    s = [capa_siglas(T)]

    s.append(slide("light", par("Juros", "As taxas que servem de régua.",
        sigla("Selic", "taxa básica de juros", I_BANCO,
              "Sai das operações de um dia entre instituições, com títulos federais de garantia. O Copom, do Banco Central, define a meta.",
              "quando a notícia diz que o Copom manteve os juros, fala da meta da Selic."),
        sigla("CDI", "a taxa DI, da B3", I_SETAS,
              "A taxa dos depósitos de um dia entre bancos de grupos diferentes, calculada e divulgada pela B3.",
              "um CDB que rende 100% do CDI acompanha essa taxa."),
        "Fontes: Banco Central (Resolução BCB 46/2020; Copom); B3 (metodologia da Taxa DI)."), 2, T))

    s.append(slide("light", par("Preços e retorno", "Quanto os preços sobem. Quanto o dinheiro rende.",
        sigla("IPCA", "índice de preços ao consumidor, do IBGE", I_SACOLA,
              "Mede os preços do que as famílias com renda de 1 a 40 salários mínimos compram no varejo.",
              "é o índice da meta de inflação do país."),
        sigla("TIR", "taxa interna de retorno", I_ALTA,
              "A taxa que leva em conta quando cada real entrou e saiu: o que ficou mais tempo aplicado pesa mais.",
              "remessas em datas diferentes viram uma só taxa de retorno."),
        "Fontes: IBGE; Banco Central (Estudo Especial 56/2019)."), 3, T))

    s.append(slide("light", par("Câmbio", "A cotação de referência e o custo de verdade.",
        sigla("PTAX", "câmbio de referência", I_GLOBO,
              "A média de quatro consultas do Banco Central aos dealers de câmbio, todo dia útil, para compra e venda.",
              "é a principal referência de cotação para o público."),
        sigla("VET", "valor efetivo total", I_RECIBO,
              "O custo do câmbio em reais por moeda estrangeira, com a taxa, as tarifas e os tributos.",
              "a mesma cotação pode dar VET diferente. O Banco Central publica um ranking."),
        "Fontes: Banco Central (Resolução BCB 45/2020; Estudo Especial 42/2019; Ranking do VET)."), 4, T))

    s.append(slide("light", par("Custos", "Um imposto e o custo total do crédito.",
        sigla("IOF", "imposto sobre operações financeiras", I_PCT,
              "Incide sobre crédito, câmbio, seguro e títulos e valores mobiliários.",
              "3,5% numa compra com cartão no exterior; 1,10% numa remessa para investir."),
        sigla("CET", "custo efetivo total", I_CONTRATO,
              "Soma juros, tarifas, tributos, seguros e outras despesas de um crédito, numa taxa ao ano. O banco informa antes de contratar.",
              "duas propostas com os mesmos juros podem ter CET diferente. Compare pelo CET."),
        "Fontes: Decreto 6.306/2007, art. 15-B (Decreto 12.499/2025); Res. CMN 4.881/2020, arts. 3º, 4º e 7º."), 5, T))

    eur = tela(P12, "celular-remessas-euro-12-12.png")
    s.append(slide("light", EXTRA_D + topo("No timtimcash", "Onde elas aparecem no site.", cls="h3") + v_onde(eur), 6, T))

    s.append(fechamento_verde("Salve este glossário.",
        "PTAX, TIR, CDI e IOF aparecem nas Remessas ao exterior do timtimcash, no computador ou no celular.", 7, T))
    return [sem_quebra_dc1(h) for h in s]


POSTS = {P02: post_dezembro, P04: post_parcela, P07: post_janeiro, P10: post_juros, P12: post_siglas}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    renderizar(POSTS, so=so)
