# -*- coding: utf-8 -*-
"""Carrosséis da equipe c1 · novembro de 2026 (01/11, 05/11, 07/11, 11/11 e 13/11), no formato aprovado em outubro
(gerador/semanas/2026-10-05_v2.py e as equipes carrosseis-a e carrosseis-b), com as peças comuns de N/kit/carrossel.py.

Telas reais (conta fictícia, build 2026-10-16.1, recapturadas em 16/10/2026), em N/saida/<pasta>/telas/:
- 01/11 · captura_base.py: Pendentes no celular, relógio em 01/11/2026 10:00 (A pagar R$ 3.869,80 em 5 transações;
  A receber R$ 14.940; "Em 4 dias · 05/11/2026" Salário R$ 9.960,00; 10/11 Aluguel R$ 2.300,00 e Escola R$ 1.450,00).
- 05/11 · captura_base.py: "Atualizar carteira" no celular, relógio em 15/10/2026 15:00, com a resposta real da PTAX de
  15/10/2026 (PTAX_15_10 do kit): "usar a cotação de hoje · R$ 5,0515" e "PTAX de compra do Banco Central, de 15/10/2026 às
  13:00" (a hora é a do boletim de fechamento que o kit responde; FATOS: fechamento PTAX, 13h).
- 07/11 · captura_base.py: Transações no celular, relógio em 07/11/2026 10:00, "Ano 2026" e "Assinaturas e serviços":
  "36 transações · 30 pagas · 6 pendentes · somam R$ 1.437,60 · 713 no histórico"; com o filtro "Pagas", 30 transações,
  R$ 1.198,00 (os 10 meses já pagos de 2026); com "Pendentes", 6 transações, R$ 239,60 (as fixas de novembro e dezembro).
- 11/11 · captura_cartao.py, na cópia da conta (pasta da equipe, equipes/c1): o "Cartão principal" de outubro (fecha 3, vence 10,
  pago pela Conta corrente, limite R$ 8.000) com quatro compras de novembro que já existiam na conta (só o "Pago via"
  muda; conferido em confere_conta.py): fatura atual de R$ 1.093,00 (04/nov a 03/dez, vence 10/dez/26), "Limite usado"
  R$ 1.093,00, "Disponível" R$ 6.907,00 de R$ 8.000,00; em Pendentes de dezembro, "Fatura em aberto · vence 10/dez/26".
Fatos de lei, taxa e data: N/FATOS.md (e CDC, art. 49, conferido no Planalto em 16/10/2026).

python3 posts.py            renderiza os 5 posts em N/saida/<pasta>/01.jpg ... e confere o layout
python3 posts.py 2026-11-05_ptax-o-dolar-do-banco-central   (só um)
"""
import os, sys, calendar
from datetime import date
from decimal import Decimal as D

N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, N + "/kit")
from carrossel import *   # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl, sem_quebra...)

P01 = "2026-11-01_novembro-do-seu-dinheiro"
P05 = "2026-11-05_ptax-o-dolar-do-banco-central"
P07 = "2026-11-07_assinaturas-o-preco-por-ano"
P11 = "2026-11-11_pagou-o-minimo-da-fatura"
P13 = "2026-11-13_black-friday-o-desconto-e-de-verdade"


NBSP = "\u00a0"


def sem_quebra_c1(html):
    """sem_quebra do kit e, nas citações, número junto da lei, do artigo e da resolução; nomes dos Procons inteiros."""
    import re as _re
    html = sem_quebra(html)
    html = _re.sub(r"\b(Lei|Decreto|art\.|arts\.|nº|séries|Res\. CMN|Res\. BCB|Resolução BCB) (\d)", lambda m: m.group(1).replace(" ", NBSP) + NBSP + m.group(2), html)
    html = _re.sub(r"(Procon-SP|Procon-MPMG|Res\. CMN|Res\. BCB|Resolução BCB)", lambda m: "<span style='white-space:nowrap'>" + m.group(1) + "</span>", html)
    html = html.replace("outros posts", "outros" + NBSP + "posts").replace("Black Friday", "Black" + NBSP + "Friday")
    return html


def tela(pasta, nome):
    caminho = os.path.join(SAIDA, pasta, "telas", nome)
    assert os.path.isfile(caminho), caminho
    return caminho


def px(v):
    """px CSS das capturas de celular (escala 3) para px da imagem."""
    return int(round(v * 3))


AMBAR_FUNDO, AMBAR_FIO = "#FBF1DC", "#F3E2BC"
CORAL_FUNDO = "#FBEDE7"
ROXO = None  # (sem cores de categoria nas peças)

EXTRA_C1 = EXTRA + f"""<style>
.tit-num{{font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums;line-height:.92}}
.leg{{display:flex;align-items:center;gap:12px;font-size:28px;font-weight:700;color:{INK};white-space:nowrap}}
.leg i{{display:block;flex:none}}
.aviso{{background:{AMBAR_FUNDO};border:1px solid {AMBAR_FIO};border-radius:28px;padding:30px 36px;display:flex;gap:26px;align-items:flex-start}}
.aviso .ic{{width:76px;height:76px;border-radius:28%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none}}
.aviso b{{display:block;font-size:34px;font-weight:700;letter-spacing:-.03em;color:{INK}}}
.aviso span{{display:block;font-size:29px;line-height:1.36;color:{INK};margin-top:8px}}
.linha-item{{display:flex;gap:30px;align-items:center;padding:28px 0}}
.linha-item + .linha-item{{border-top:2px solid {FIO}}}
.linha-item .t{{font-size:38px;font-weight:700;letter-spacing:-.03em;line-height:1.15}}
.linha-item .s{{font-size:28px;color:{MUTED};margin-top:8px;line-height:1.3}}
</style>"""


def topo(sobre, titulo, apoio=None, cls="h2", estilo_t="", estilo_p=""):
    p = f"<div class='p' style='{estilo_p}'>{apoio}</div>" if apoio else ""
    return f"<div class='eyebrow'>{sobre}</div><div class='{cls}' style='{estilo_t}'>{titulo}</div>{p}"


def item(ip, titulo, sub):
    return f"""<div class='linha-item'>{azulejo(ip, 84, 42)}
  <div><div class='t'>{titulo}</div><div class='s'>{sub}</div></div></div>"""


def aviso(ip, titulo, texto):
    return f"""<div class='aviso'><div class='ic'>{svg_icone(ip, 40, AMBER_TEXT, 2.2)}</div>
  <div><b>{titulo}</b><span>{texto}</span></div></div>"""


# ícones de traço próprios (24 × 24)
I_MARCA = '<path d="M7 3.5h10a1 1 0 0 1 1 1V21l-6-4-6 4V4.5a1 1 0 0 1 1-1z"/>'          # salvar (marcador)
I_ETIQ = '<path d="M3.5 12.2V4.5a1 1 0 0 1 1-1h7.7l8.3 8.3a1.4 1.4 0 0 1 0 2l-6.7 6.7a1.4 1.4 0 0 1-2 0z"/><circle cx="8" cy="8" r="1.6"/>'
I_DOBRO = '<rect x="8" y="8" width="12" height="12" rx="2.5"/><path d="M16 8V5.5A1.5 1.5 0 0 0 14.5 4h-9A1.5 1.5 0 0 0 4 5.5v9A1.5 1.5 0 0 0 5.5 16H8"/>'
I_PLAY = '<circle cx="12" cy="12" r="8.5"/><path d="M10.2 8.8v6.4l5.2-3.2z"/>'
I_DESCE = '<path d="M12 4v15"/><path d="M6.5 13.5 12 19l5.5-5.5"/>'
I_DOC = '<path d="M7 3.5h7l4 4V20a.5.5 0 0 1-.5.5h-10A.5.5 0 0 1 6 20V4a.5.5 0 0 1 .5-.5z"/><path d="M14 3.5V8h4"/>'
I_IMG = '<rect x="3.5" y="5" width="17" height="14" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M20.5 16l-5-5-8 8"/>'
I_CAIXA = '<path d="M3.5 8 12 3.5 20.5 8v8L12 20.5 3.5 16z"/><path d="M3.5 8 12 12.5 20.5 8M12 12.5v8"/>'
I_VOLTA = '<path d="M9 14 4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/>'
I_BANCO = '<path d="M12 3.5 20.5 8h-17z"/><path d="M5 11v6.5M9.7 11v6.5M14.3 11v6.5M19 11v6.5"/><path d="M3.5 20.5h17"/>'
I_LUPA = '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>'


# ============================================================================ calendários
SEMANA = ["D", "S", "T", "Q", "Q", "S", "S"]


def grade_mes(ano, mes, marcas, cel=92, bola=76, fs=34, cab=True, dom_destaque=False):
    """Grade de um mês que começa no domingo. marcas: {dia: 'coral' | 'verde' | 'tinta'}."""
    off = (date(ano, mes, 1).weekday() + 1) % 7          # domingo = coluna 0
    ndias = calendar.monthrange(ano, mes)[1]
    cels = []
    if cab:
        for i, s in enumerate(SEMANA):
            cor = BRAND_DARK if (dom_destaque and i == 0) else MUTED
            cels.append(f"<div style='height:{int(fs * 1.5)}px;display:flex;align-items:center;justify-content:center;"
                        f"font-size:{int(fs * .74)}px;font-weight:700;color:{cor};letter-spacing:.04em'>{s}</div>")
    for _ in range(off):
        cels.append(f"<div style='height:{cel}px'></div>")
    for d in range(1, ndias + 1):
        m = marcas.get(d)
        if m == "coral":
            est, peso = f"background:#fff;color:{CORAL_TXT};box-shadow:inset 0 0 0 {max(4, bola // 15)}px {CORAL}", 700
        elif m == "verde":
            est, peso = f"background:{BRAND};color:#fff;box-shadow:0 0 0 {max(6, bola // 10)}px {SOFT}", 700
        elif m == "tinta":
            est, peso = f"background:{INK};color:#fff", 700
        else:
            est, peso = f"color:{INK if not dom_destaque else MUTED}", 500
        cels.append(f"<div style='display:flex;align-items:center;justify-content:center;height:{cel}px'>"
                    f"<span style='width:{bola}px;height:{bola}px;border-radius:50%;display:flex;align-items:center;justify-content:center;"
                    f"font-size:{fs}px;font-weight:{peso};font-variant-numeric:tabular-nums;{est}'>{d}</span></div>")
    return f"<div style='display:grid;grid-template-columns:repeat(7,1fr);row-gap:2px'>{''.join(cels)}</div>"


def argolas(cor=INK):
    return "".join(f"<i style='position:absolute;top:-17px;left:{x};width:18px;height:46px;border-radius:9px;background:{cor};display:block'></i>"
                   for x in ("21%", "77%"))


# ============================================================================ 01/11 · Novembro do seu dinheiro
SALARIO = D("9960.00")
PARCELA1 = SALARIO / 2
assert PARCELA1 == D("4980.00")


def leg_bola(estilo, txt, cor=INK):
    return f"<span class='leg' style='color:{cor}'><i style='width:28px;height:28px;border-radius:50%;{estilo}'></i>{txt}</span>"


def capa_novembro(T):
    cal = f"""<div class='card' style='position:relative;margin-top:54px;padding:0;overflow:visible'>
  {argolas()}
  <div style='height:30px;border-radius:28px 28px 0 0;background:{FIO}'></div>
  <div style='padding:12px 30px 4px'>{grade_mes(2026, 11, {27: 'coral', 30: 'verde'}, cel=90, bola=78, fs=36)}</div>
  <div style='display:flex;justify-content:center;gap:52px;padding:26px 30px 34px;border-top:2px solid {FIO};margin:10px 34px 0'>
    {leg_bola(f'background:#fff;box-shadow:inset 0 0 0 5px {CORAL}', 'Black Friday', CORAL_TXT)}
    {leg_bola(f'background:{BRAND}', '1ª parcela do 13º', BRAND_DARK)}
  </div>
</div>"""
    corpo = f"""<div class='eyebrow'>Calendário</div>
<div class='h1' style='font-size:104px'>Novembro do seu dinheiro.</div>{cal}"""
    return capa("papel", EXTRA_C1 + corpo, 1, T)


def v_parcela():
    meio = 50
    listra = f"repeating-linear-gradient(135deg,{FIO} 0 14px,#F4F2EA 14px 28px)"
    return f"""<div class='visual' style='margin-top:48px'><div class='card' style='padding:40px 46px 38px'>
  <div style='display:flex;align-items:baseline;gap:20px;flex-wrap:wrap'>
    <span class='big' style='font-size:104px;color:{BRAND_DARK};line-height:1'>R$ 4.980</span>
    <span style='font-size:36px;font-weight:600;color:{MUTED}'>de R$ 9.960</span></div>
  <div style='display:flex;height:66px;border-radius:18px;overflow:hidden;margin-top:30px;gap:6px'>
    <div style='flex:{meio};background:{BRAND};display:flex;align-items:center;padding-left:24px;color:#fff;font-size:28px;font-weight:700'>1ª parcela</div>
    <div style='flex:{100 - meio};background:{listra};display:flex;align-items:center;padding-left:24px;color:{MUTED};font-size:28px;font-weight:700'>2ª parcela</div>
  </div>
  <div style='display:flex;margin-top:22px;gap:6px'>
    <div style='flex:1;padding-right:16px'><div style='font-size:28px;font-weight:700;color:{BRAND_DARK}'>até 30/11</div>
      <div style='font-size:26px;font-weight:500;color:{MUTED};margin-top:4px;line-height:1.3'>sem nenhum desconto</div></div>
    <div style='flex:1;padding-left:16px'><div style='font-size:28px;font-weight:700;color:{INK}'>até 20/12</div>
      <div style='font-size:26px;font-weight:500;color:{MUTED};margin-top:4px;line-height:1.3'>com INSS e IR do 13º inteiro</div></div>
  </div>
</div><div class='nota'>Exemplo: salário de R$ 9.960. Lei 4.749/1965, art. 2º; Lei 8.134/1990, art. 16; Decreto 3.048/1999, art. 214.</div></div>"""


def v_etiqueta_preencher():
    """Etiqueta de preço para a pessoa preencher (salvar o post e comparar no dia 27)."""
    W, H = 870, 372
    forma = (f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='position:absolute;left:0;top:0;overflow:visible'>"
             f"<defs><filter id='sb' x='-10%' y='-10%' width='120%' height='140%'><feDropShadow dx='0' dy='18' stdDeviation='18' flood-color='#0F1410' flood-opacity='.16'/></filter></defs>"
             f"<path d='M120 4 H{W - 28} a26 26 0 0 1 26 26 V{H - 30} a26 26 0 0 1 -26 26 H120 L12 {H / 2 + 48} a42 42 0 0 1 0 -96 Z' "
             f"fill='#fff' stroke='{FIO}' stroke-width='2' filter='url(#sb)'/>"
             f"<circle cx='84' cy='{H / 2}' r='19' fill='{BG}' stroke='{NEUTRO}' stroke-width='3'/>"
             f"<path d='M84 {H / 2 - 19} C 80 {H / 2 - 80}, 40 {H / 2 - 96}, 52 {H / 2 - 140} S 96 {H / 2 - 176}, 70 {H / 2 - 196}' fill='none' stroke='{MUTED}' stroke-width='3' stroke-linecap='round'/>"
             f"</svg>")

    def campo(rot, pre="", forte=False):
        cor = BRAND_DARK if forte else INK
        linha = f"<span style='border-bottom:4px dotted {NEUTRO};height:34px;display:block'></span>"
        return (f"<span style='font-size:32px;font-weight:700;color:{cor};white-space:nowrap'>{rot}</span>"
                f"<span style='font-size:34px;font-weight:700;color:{INK}'>{pre}</span>{linha}")
    return f"""<div class='visual' style='margin-top:50px;position:relative;width:{W}px;height:{H}px;margin-left:26px'>
  {forma}
  <div style='position:absolute;left:170px;right:52px;top:44px'>
    <div style='display:flex;align-items:center;gap:14px'>{svg_icone(I_ETIQ, 36, CORAL_TXT, 2.2)}
      <span style='font-size:25px;font-weight:700;letter-spacing:.16em;color:{CORAL_TXT}'>MINHA LISTA DA BLACK FRIDAY</span></div>
    <div style='display:grid;grid-template-columns:auto 52px 1fr;column-gap:14px;row-gap:30px;align-items:end;margin-top:34px'>
      {campo('O que eu quero')}
      {campo('Preço em 01/11', 'R$', True)}
      {campo('Preço em 27/11', 'R$')}
    </div>
  </div>
</div>"""


def v_dezembro():
    cal = grade_mes(2026, 12, {20: "verde"}, cel=76, bola=62, fs=29, dom_destaque=True)
    return f"""<div class='visual' style='margin-top:46px;display:flex;gap:30px;align-items:center'>
  <div class='card' style='position:relative;flex:none;width:584px;padding:0;overflow:visible'>
    {argolas()}
    <div style='height:26px;border-radius:28px 28px 0 0;background:{FIO}'></div>
    <div style='padding:14px 24px 20px'>
      <div style='font-size:24px;font-weight:700;letter-spacing:.16em;color:{MUTED};text-align:center;margin:4px 0 2px'>DEZEMBRO 2026</div>
      {cal}</div>
  </div>
  <div style='flex:1'>
    <div class='big' style='font-size:96px;line-height:.95;color:{BRAND_DARK}'>20/12</div>
    <div style='font-size:46px;font-weight:700;letter-spacing:-.03em;margin-top:8px'>domingo</div>
    <div style='font-size:28px;font-weight:500;color:{MUTED};margin-top:16px;line-height:1.35'>Confira com a empresa o dia do pagamento.</div>
  </div>
</div>
<div class='nota'>Lei 4.749/1965, art. 1º; Lei 8.134/1990, art. 16; Decreto 3.048/1999, art. 214.</div>"""


def post_novembro():
    T = 6
    s = [capa_novembro(T)]

    s.append(slide("light", EXTRA_C1 + topo(
        "Até 30/11", "1ª parcela do 13º.",
        "Metade do salário do mês anterior, de uma vez. Sem INSS e sem IR: eles ficam para a 2ª parcela.") + v_parcela(), 2, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "27/11 · Black Friday", "Anote hoje o preço.",
        "O Procon-SP orienta pesquisar preços com antecedência. Anote e compare no dia 27.",
        estilo_p="font-size:36px;margin-top:24px") + v_etiqueta_preencher() + f"""
<div style='display:flex;align-items:center;gap:16px;margin-top:40px'>
  <span style='display:inline-flex;align-items:center;gap:14px;background:{SOFT};color:{BRAND_DEEP};font-size:28px;font-weight:700;padding:16px 28px;border-radius:999px'>{svg_icone(I_MARCA, 30, BRAND_DEEP, 2.2)}Salve este post e compare no dia 27.</span></div>
<div class='nota'>Às lojas, o Procon-SP pediu desconto sobre o menor preço dos últimos 60 dias. Fontes: Procon-SP, 26/11/2025 e 06/11/2025.</div>""", 3, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Até 20/12", "2ª parcela, com os descontos.",
        "É nela que saem o INSS e o IR do 13º inteiro. Em 2026, o dia 20 cai num domingo.",
        estilo_p="margin-top:26px") + v_dezembro(), 4, T))

    pend = tela(P01, "celular-pendentes-01-11.png")
    s.append(slide("light", EXTRA_C1 + topo(
        "No timtimcash", "Pendentes, dia a dia.",
        "O que vence e o que você tem a receber no mês, com “Hoje”, “Amanhã” e “Em N dias”.",
        cls="h3", estilo_p="font-size:34px;margin-top:18px")
        + f"<div class='visual' style='margin-top:32px'>{recorte(pend, 1244, 2268, largura=716, x0=36, x1=1134)}{NOTA_TELA}</div>", 5, T))

    s.append(fechamento_verde("Seu novembro, dia a dia.",
        "Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra_c1(h) for h in s]


# ============================================================================ 05/11 · PTAX: o dólar do Banco Central
PTAX_USD = (D("5.0515"), D("5.0521"))   # compra, venda · 15/10/2026 (FATOS; PTAX_15_10 do kit)
PTAX_EUR = (D("5.6592"), D("5.6609"))


def v_horas(cor_linha=BRAND_DEEP, cor_ponto=BRAND, cor_txt=BRAND_DEEP, larg=820):
    xs = [40 + i * (larg - 80) / 3 for i in range(4)]
    pontos = "".join(f"<circle cx='{x:.1f}' cy='34' r='17' fill='{cor_ponto}' stroke='{SOFT}' stroke-width='8'/>" for x in xs)
    rot = "".join(f"<text x='{x:.1f}' y='104' text-anchor='middle' font-family='Inter' font-weight='700' font-size='34' fill='{cor_txt}'>{h}h</text>"
                  for x, h in zip(xs, (10, 11, 12, 13)))
    return (f"<svg width='{larg}' height='118' viewBox='0 0 {larg} 118' style='display:block'>"
            f"<line x1='{xs[0]:.1f}' y1='34' x2='{xs[-1]:.1f}' y2='34' stroke='{cor_linha}' stroke-width='5' stroke-linecap='round'/>{pontos}{rot}</svg>")


def capa_ptax(T):
    corpo = f"""<div class='eyebrow'>Câmbio</div>
<div class='h1' style='font-size:100px'>PTAX: o dólar do Banco Central.</div>
<div style='display:flex;align-items:flex-start;gap:14px;margin-top:62px'>
  <span style='font-size:64px;font-weight:700;letter-spacing:-.03em;color:{BRAND_DEEP};margin-top:30px'>R$</span>
  <span class='tit-num' style='font-size:236px;color:{INK}'>{num(PTAX_USD[0], 4)}</span></div>
<div style='margin-top:30px'><span style='display:inline-flex;align-items:center;gap:14px;background:#fff;color:{BRAND_DEEP};font-size:30px;font-weight:700;padding:16px 30px;border-radius:999px;box-shadow:0 1px 2px rgba(6,95,70,.08),0 14px 30px -18px rgba(6,95,70,.45)'>PTAX de compra · 15/10/2026</span></div>
<div style='margin-top:56px'>{v_horas()}</div>"""
    return capa("suave", EXTRA_C1 + corpo, 1, T)


def v_semana():
    dias = [("seg", True), ("ter", True), ("qua", True), ("qui", True), ("sex", True), ("sáb", False), ("dom", False)]
    tiles = "".join(f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:12px'>
  <div style='width:100%;height:96px;border-radius:20px;display:flex;align-items:center;justify-content:center;
    background:{BRAND if ok else '#F2F1EB'};border:{'none' if ok else '2px dashed ' + NEUTRO}'>
    {svg_icone(I_CHECK, 40, '#fff', 3) if ok else ''}</div>
  <div style='font-size:26px;font-weight:700;color:{INK if ok else MUTED}'>{d}</div></div>""" for d, ok in dias)
    return f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:34px 36px 30px'>
  <div style='display:flex;gap:12px'>{tiles}</div>
  <div style='display:flex;justify-content:space-between;margin-top:18px;font-size:26px;font-weight:600'>
    <span style='color:{BRAND_DARK}'>sai todo dia útil</span><span style='color:{MUTED}'>não sai</span></div>
</div></div>"""


def v_citacao():
    return f"""<div style='margin-top:30px;background:{SOFT};border-radius:28px;padding:34px 40px 30px;position:relative'>
  <svg width='46' height='36' viewBox='0 0 46 36' style='display:block;margin-bottom:16px'><path fill='{BRAND}' d='M0 36V21C0 9.6 5.6 2.6 16.8 0l2.3 4.9C13.6 6.6 10.8 10 10.4 15H18v21H0zm27 0V21c0-11.4 5.6-18.4 16.8-21l2.2 4.9C40.6 6.6 37.8 10 37.4 15H45v21H27z'/></svg>
  <div style='font-size:38px;font-weight:600;letter-spacing:-.02em;line-height:1.3;color:{BRAND_DEEP}'>Na prática, também é a principal referência de cotação para o público em geral.</div>
  <div style='font-size:26px;font-weight:600;color:{BRAND_DEEP};margin-top:16px'>Banco Central, Estudo Especial 42/2019</div>
</div>"""


FORA_COR = "#E7E3D8"


def pilula_fora(w="100%", h=20):
    """Cotação que sai da conta: cinza com um risco escuro."""
    return (f"<div style='position:relative;width:{w};height:{h}px;border-radius:{h // 2}px;background:{FORA_COR}'>"
            f"<i style='position:absolute;left:-5px;right:-5px;top:{h // 2 - 2}px;height:4px;border-radius:2px;background:{MUTED};display:block;transform:rotate(-4deg)'></i></div>")


def v_consultas():
    """As quatro consultas do dia: em cada uma, saem as duas maiores e as duas menores cotações; a PTAX é a média das quatro."""
    def escada():
        larg = [96, 89, 83, 78, 73, 68, 62, 55]   # ilustração: cotações da maior para a menor (sem valores)
        out = []
        for i, w in enumerate(larg):
            if i < 2 or i >= len(larg) - 2:
                out.append(pilula_fora(f"{w}%", 18))
            else:
                out.append(f"<div style='width:{w}%;height:18px;border-radius:9px;background:{BRAND}'></div>")
        return f"<div style='display:flex;flex-direction:column;align-items:center;gap:7px;margin-top:16px'>{''.join(out)}</div>"
    cols = "".join(f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center'>
  <div style='font-size:40px;font-weight:700;letter-spacing:-.03em;color:{INK}'>{h}h</div>
  <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:2px;white-space:nowrap'>{h}h00 a {h}h10</div>
  <div style='width:100%;padding:0 4px'>{escada()}</div>
</div>""" for h in (10, 11, 12, 13))
    return f"""<div class='visual' style='margin-top:38px'><div class='card' style='padding:26px 34px 26px'>
  <div style='display:flex;gap:22px'>{cols}</div>
  <div style='display:flex;justify-content:center;gap:30px;margin-top:16px;font-size:24px;font-weight:600;color:{MUTED}'>
    <span style='display:flex;align-items:center;gap:10px'><i style='width:34px;height:16px;border-radius:8px;background:{BRAND};display:block'></i>entram na conta</span>
    <span style='display:flex;align-items:center;gap:10px'><span style='width:34px'>{pilula_fora('34px', 16)}</span>as 2 maiores e as 2 menores saem</span>
  </div>
  <div class='fio' style='margin:18px 0 16px'></div>
  <div style='display:flex;align-items:center;justify-content:center;gap:20px'>
    <span style='font-size:30px;font-weight:600;color:{MUTED}'>PTAX do dia</span>
    <span style='font-size:34px;font-weight:700;color:{INK}'>=</span>
    <span style='display:inline-flex;align-items:center;background:{BRAND};color:#fff;font-size:32px;font-weight:700;padding:16px 30px;border-radius:999px'>a média das 4 consultas</span></div>
</div><div class='nota'>Ilustração, sem valores. Dealers são instituições credenciadas para operar câmbio com o Banco Central (Resolução BCB nº 45/2020).</div></div>"""


def v_compra_venda():
    def lin(moeda, simb, c, v, ultimo=False):
        return f"""<div style='display:grid;grid-template-columns:1.25fr 1fr 1fr;align-items:center;padding:26px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div style='display:flex;align-items:center;gap:18px'><span style='width:70px;height:70px;border-radius:50%;background:{SOFT};color:{BRAND_DEEP};display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700'>{simb}</span>
    <span style='font-size:34px;font-weight:700'>{moeda}</span></div>
  <div class='big' style='font-size:50px;text-align:right'>{num(c, 4)}</div>
  <div class='big' style='font-size:50px;text-align:right;color:{MUTED}'>{num(v, 4)}</div></div>"""
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:20px 44px 10px'>
  <div style='display:grid;grid-template-columns:1.25fr 1fr 1fr;font-size:24px;font-weight:700;letter-spacing:.14em;color:{MUTED};padding:10px 0 4px'>
    <span>EM R$</span><span style='text-align:right;color:{BRAND_DARK}'>COMPRA</span><span style='text-align:right'>VENDA</span></div>
  {lin('Dólar', 'US$', *PTAX_USD)}
  {lin('Euro', '€', *PTAX_EUR, ultimo=True)}
</div><div class='nota'>Fonte: Banco Central, sistema PTAX, boletim de fechamento de 15/10/2026.</div></div>"""


def post_ptax():
    T = 6
    s = [capa_ptax(T)]

    s.append(slide("light", EXTRA_C1 + topo(
        "O que é", "A taxa de câmbio de referência do Banco Central.",
        "Calculada todo dia útil, para o dólar e para outras moedas. Base atual: Resolução BCB nº 45/2020.",
        estilo_t="font-size:72px", estilo_p="font-size:36px;margin-top:24px") + v_semana() + v_citacao(), 2, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Como sai o número", "Quatro consultas, uma média.",
        "Das 10h às 13h, uma consulta por hora aos dealers de câmbio, numa janela de 10 minutos.",
        estilo_p="font-size:36px;margin-top:24px") + v_consultas(), 3, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Compra e venda", "Saem duas taxas por moeda.",
        "Exemplo real de 15/10/2026, no boletim de fechamento.", estilo_p="font-size:36px;margin-top:20px") + v_compra_venda()
        + f"<div style='margin-top:34px'>{aviso(I_ALERT, 'Não é o câmbio que você paga.', 'Na sua operação entram o spread da instituição, a tarifa e o IOF: é o câmbio efetivo.')}</div>", 4, T))

    cart = tela(P05, "celular-atualizar-carteira-ptax-15-10.png")
    s.append(slide("light", EXTRA_C1 + topo(
        "No timtimcash", "A PTAX chega sozinha, com data e hora.",
        "Ao atualizar a carteira, o site sugere a PTAX de compra. Para fechar o ano, busca a do último dia útil.",
        cls="h3", estilo_p="font-size:32px;margin-top:18px")
        + f"<div class='visual' style='margin-top:36px'>{recorte(cart, 1584, 2262, largura=820, x0=30, x1=1140)}{NOTA_TELA}</div>", 5, T))

    s.append(fechamento_verde("O dólar de hoje, com a fonte certa.",
        "Remessas ao exterior no timtimcash, no computador ou no celular.", 6, T))
    return [sem_quebra_c1(h) for h in s]


# ============================================================================ 07/11 · Assinaturas: o preço por ano
ASSIN = [("Vídeo", D("55.90")), ("Música", D("21.90")), ("Nuvem", D("42.00"))]
MES_TOTAL = sum(v for _, v in ASSIN)
ANO_TOTAL = MES_TOTAL * 12
assert MES_TOTAL == D("119.80") and ANO_TOTAL == D("1437.60")
assert [v * 12 for _, v in ASSIN] == [D("670.80"), D("262.80"), D("504.00")]
PAGO_2026, PENDENTE_2026 = D("1198.00"), D("239.60")      # tela de 07/11: 30 pagas e 6 pendentes
assert MES_TOTAL * 10 == PAGO_2026 and MES_TOTAL * 2 == PENDENTE_2026 and PAGO_2026 + PENDENTE_2026 == ANO_TOTAL


def capa_assinaturas(T):
    meses = "JFMAMJJASOND"
    tiles = "".join(f"<div style='flex:1;height:78px;border-radius:16px;background:#fff;display:flex;align-items:center;justify-content:center;"
                    f"font-size:28px;font-weight:700;color:{BRAND_DARK}'>{m}</div>" for m in meses)
    corpo = f"""<div class='eyebrow'>Assinaturas</div>
<div style='display:flex;align-items:center;gap:24px'>
  <span style='display:inline-flex;align-items:center;background:#fff;color:{BRAND_DARK};font-size:42px;font-weight:700;padding:20px 38px;border-radius:999px;letter-spacing:-.02em'>R$ 119,80 por mês</span>
  <span style='font-size:56px;font-weight:700;color:#fff;letter-spacing:-.02em'>× 12</span></div>
<div style='display:flex;gap:9px;margin-top:44px'>{tiles}</div>
<div style='display:flex;align-items:flex-start;gap:14px;margin-top:70px'>
  <span style='font-size:72px;font-weight:700;color:#fff;letter-spacing:-.03em;margin-top:24px'>R$</span>
  <span class='tit-num' style='font-size:186px;color:#fff'>1.437,60</span></div>
<div style='font-size:80px;font-weight:700;letter-spacing:-.045em;color:#fff;margin-top:14px'>por ano</div>"""
    return capa("verde", EXTRA_C1 + corpo, 1, T)


def v_barras_ano():
    """Cada assinatura numa barra do ano com 12 pedaços: o primeiro, mais escuro, é o mês."""
    larg_max = 600
    vmax = max(v for _, v in ASSIN)
    linhas = []
    for i, (nome, v) in enumerate(ASSIN):
        w = larg_max * float(v / vmax)
        pedacos = "".join(f"<div style='flex:1;background:{CORAL_FORTE if k == 0 else CORAL};border-radius:5px'></div>" for k in range(12))
        linhas.append(f"""<div style='padding:28px 0 30px;{'' if i == len(ASSIN) - 1 else f'border-bottom:2px solid {FIO};'}'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span style='font-size:38px;font-weight:700;letter-spacing:-.02em'>{nome}</span>
    <span style='font-size:28px;font-weight:600;color:{MUTED}'>R$ {num(v)} por mês</span></div>
  <div style='display:flex;align-items:center;gap:20px;margin-top:18px'>
    <div style='width:{w:.1f}px;height:34px;display:flex;gap:3px'>{pedacos}</div>
    <span class='big' style='font-size:42px;color:{CORAL_FORTE};white-space:nowrap'>R$ {num(v * 12)}</span></div>
</div>""")
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:6px 44px 6px'>{''.join(linhas)}</div>
<div style='display:flex;align-items:center;gap:30px;margin-top:24px;padding:0 6px;font-size:26px;font-weight:600;color:{MUTED}'>
  <span style='display:flex;align-items:center;gap:10px'><i style='width:22px;height:22px;border-radius:5px;background:{CORAL_FORTE};display:block'></i>um mês</span>
  <span style='display:flex;align-items:center;gap:10px'><i style='width:22px;height:22px;border-radius:5px;background:{CORAL};display:block'></i>os outros 11</span>
  <span style='margin-left:auto'>valor por ano, em R$</span></div>
<div class='nota'>Exemplo: as assinaturas de vídeo, de música e de nuvem da conta dos outros posts.</div></div>"""


def v_conta_x12():
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:36px 44px 34px'>
  <div style='display:flex;align-items:flex-end;justify-content:space-between;gap:10px'>
    <div><div class='rot'>Por mês</div><div class='big' style='font-size:58px;margin-top:4px'>R$ 119,80</div></div>
    <div class='big' style='font-size:52px;color:{MUTED};padding-bottom:4px'>× 12</div>
    <div class='big' style='font-size:52px;color:{MUTED};padding-bottom:4px'>=</div>
    <div style='text-align:right'><div class='rot'>Por ano</div><div class='big' style='font-size:58px;margin-top:4px;color:{CORAL_FORTE}'>R$ 1.437,60</div></div>
  </div>
  <div class='fio' style='margin:30px 0 26px'></div>
  <div style='font-size:24px;font-weight:700;letter-spacing:.16em;color:{MUTED}'>PLANO ANUAL? COMPARE ASSIM</div>
  <div style='display:flex;align-items:center;gap:18px;margin-top:18px'>
    <div style='flex:1;background:#F6F5EF;border-radius:20px;padding:20px 24px'>
      <div style='font-size:26px;font-weight:700;color:{MUTED}'>Mensal × 12</div>
      <div class='big' style='font-size:46px;margin-top:4px'>R$ 262,80</div></div>
    <div style='font-size:32px;font-weight:700;color:{MUTED}'>vs</div>
    <div style='flex:1;background:{SOFT};border-radius:20px;padding:20px 24px'>
      <div style='font-size:26px;font-weight:700;color:{BRAND_DEEP}'>Anual</div>
      <div class='big' style='font-size:46px;margin-top:4px;color:{BRAND_DEEP}'>R$ ?</div></div>
  </div>
  <div style='font-size:28px;line-height:1.35;color:{INK};margin-top:20px'>O anual compensa se custar menos que R$ 262,80 e você usar o ano todo.</div>
</div><div class='nota'>Exemplo: a assinatura de música da conta dos outros posts (R$ 21,90 por mês).</div></div>"""


def post_assinaturas():
    T = 6
    s = [capa_assinaturas(T)]

    s.append(slide("light", EXTRA_C1 + topo(
        "Por mês parece pouco", "No ano, cada uma é 12 vezes maior.") + v_barras_ano(), 2, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "A conta × 12", "Multiplique por 12 antes de assinar.",
        "Plano anual com desconto também se compara assim: o preço do ano contra 12 vezes o do mês.",
        estilo_p="font-size:36px;margin-top:24px") + v_conta_x12(), 3, T))

    tx = tela(P07, "celular-transacoes-assinaturas-ano-2026.png")
    s.append(slide("light", EXTRA_C1 + topo(
        "Ache as suas", "Em Transações, o ano inteiro numa soma.",
        "Escolha o período “Ano” e a categoria “Assinaturas e serviços”: a soma do filtrado aparece no topo.",
        cls="h3", estilo_p="font-size:34px;margin-top:18px")
        + f"<div class='visual' style='margin-top:34px'>{recorte(tx, 930, 1745, largura=720, x0=36, x1=1134)}"
        + f"<div class='nota' style='text-align:center'>Tela real do timtimcash, com dados de exemplo. Nos filtros “Pagas” e “Pendentes”: R$ 1.198,00 e R$ 239,60 (novembro e dezembro).</div></div>", 4, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Uma vez por ano", "Faça três perguntas a cada assinatura.") + f"""
<div class='visual' style='margin-top:48px'><div class='card' style='padding:6px 44px'>
  {item(I_PLAY, 'Ainda uso?', 'Se faz meses que não abre, é hora de cancelar.')}
  {item(I_ETIQ, 'Tem plano mais barato?', 'Plano básico, anual ou com anúncios: compare pelo preço do ano.')}
  {item(I_DOBRO, 'Está em dobro?', 'Duas contas de música, dois serviços de nuvem: fique com um.')}
</div></div>""", 5, T))

    s.append(fechamento_verde("Seu gasto fixo, em reais por ano.",
        "Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra_c1(h) for h in s]


# ============================================================================ 11/11 · Pagou o mínimo. E o resto?
ROT_AM, ROT_AA = D("15.18"), D("444.89")      # rotativo, agosto de 2026 (BCB, nota de 29/9/2026)
CHE_AM, CHE_AA, CHE_TETO = D("7.43"), D("136.41"), D("8")
DIVIDA = D("1000.00")
JUROS_1_MES = DIVIDA * ROT_AM / 100
assert JUROS_1_MES == D("151.80")
TETO_TOTAL = DIVIDA * 2
assert TETO_TOTAL == D("2000.00")


def barra_fatura(pago=14, h=70, rotulos=True):
    return f"""<div style='display:flex;height:{h}px;border-radius:18px;overflow:hidden;gap:6px'>
    <div style='flex:{pago};background:{BRAND}'></div>
    <div style='flex:{100 - pago};background:{CORAL}'></div></div>
  {f'''<div style='display:flex;justify-content:space-between;margin-top:20px'>
    <span class='leg' style='color:{BRAND_DARK}'><i style='width:26px;height:26px;border-radius:8px;background:{BRAND}'></i>o que você pagou</span>
    <span class='leg' style='color:{CORAL_TXT}'><i style='width:26px;height:26px;border-radius:8px;background:{CORAL}'></i>vai para o rotativo</span></div>''' if rotulos else ''}"""


def capa_minimo(T):
    cartao_svg = (f"<svg width='150' height='100' viewBox='0 0 150 100' fill='none'><rect x='1' y='1' width='148' height='98' rx='14' fill='{SOFT}' stroke='{BRAND}' stroke-width='2'/>"
                  f"<rect x='18' y='26' width='34' height='26' rx='5' fill='{MENTA}'/><rect x='18' y='70' width='80' height='8' rx='4' fill='{MENTA_CLARA}'/></svg>")
    card = f"""<div class='card sombra' style='margin-top:66px;padding:44px 48px 40px'>
  <div style='display:flex;align-items:flex-start;justify-content:space-between'>
    <div><div style='font-size:30px;font-weight:600;color:{MUTED}'>Total da fatura</div>
      <div class='big' style='font-size:112px;line-height:1;margin-top:12px'>R$ 1.000,00</div></div>
    {cartao_svg}</div>
  <div style='margin-top:42px'>{barra_fatura()}</div>
</div>"""
    corpo = f"""<div class='eyebrow'>Cartão de crédito</div>
<div class='h1' style='font-size:108px'>Pagou o mínimo. E o resto?</div>{card}"""
    return capa("papel", EXTRA_C1 + corpo, 1, T)


def v_rotativo_fluxo():
    juros = f"repeating-linear-gradient(135deg,{CORAL_FORTE} 0 12px,#B65A3A 12px 24px)"
    seta_baixo = svg_icone('<path d="M12 4v15"/><path d="M6.5 13.5 12 19l5.5-5.5"/>', 44, MUTED, 2.4)

    def rotulo(txt, cor, alinhar="left"):
        return f"<span style='font-size:27px;font-weight:700;color:{cor};text-align:{alinhar}'>{txt}</span>"
    return f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:36px 44px 36px'>
  <div style='font-size:24px;font-weight:700;letter-spacing:.16em;color:{MUTED}'>ESTA FATURA</div>
  <div style='display:flex;height:64px;gap:6px;margin-top:18px;width:78%'>
    <div style='flex:14;background:{BRAND};border-radius:16px 0 0 16px'></div>
    <div style='flex:86;background:{CORAL};border-radius:0 16px 16px 0'></div></div>
  <div style='display:flex;justify-content:space-between;margin-top:14px;width:78%'>{rotulo('pagou uma parte', BRAND_DARK)}{rotulo('o resto', CORAL_TXT, 'right')}</div>
  <div style='display:flex;align-items:center;gap:16px;margin:16px 0 4px;padding-left:44%'>{seta_baixo}
    <span style='font-size:26px;font-weight:600;color:{MUTED}'>vira rotativo, com juros</span></div>
  <div style='font-size:24px;font-weight:700;letter-spacing:.16em;color:{MUTED};margin-top:10px'>A PRÓXIMA FATURA</div>
  <div style='display:flex;height:64px;gap:6px;margin-top:18px;width:84%'>
    <div style='flex:67;background:{CORAL};border-radius:16px 0 0 16px'></div>
    <div style='flex:17;background:{juros};border-radius:0 16px 16px 0'></div></div>
  <div style='display:flex;gap:6px;margin-top:14px;width:84%'>
    <div style='flex:67'>{rotulo('o resto', CORAL_TXT)}</div>
    <div style='flex:17;white-space:nowrap'>{rotulo('+ juros', CORAL_FORTE)}</div></div>
</div><div class='nota'>Ilustração, sem valores: o pagamento mínimo depende do emissor do cartão.</div></div>"""


def v_taxa_rotativo():
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:44px 48px 42px'>
  <div style='display:flex;align-items:baseline;gap:20px'>
    <span class='tit-num' style='font-size:220px;color:{CORAL_FORTE}'>{num(ROT_AM)}%</span></div>
  <div style='font-size:46px;font-weight:700;letter-spacing:-.03em;margin-top:14px'>ao mês</div>
  <div class='fio' style='margin:34px 0 28px'></div>
  <div style='display:flex;align-items:baseline;justify-content:space-between;gap:20px'>
    <span style='font-size:34px;font-weight:600;color:{MUTED}'>No ano</span>
    <span class='big' style='font-size:86px;color:{INK}'>{num(ROT_AA)}%</span></div>
  <div style='margin-top:26px;background:{CORAL_FUNDO};border-radius:20px;padding:22px 28px;font-size:29px;line-height:1.35;color:{INK}'>
    Na taxa média, R$ 1.000 no rotativo geram <b style='color:{CORAL_FORTE}'>R$ 151,80</b> de juros em um mês.</div>
</div><div class='nota'>Taxa média do rotativo do cartão, pessoa física, agosto de 2026. Fonte: Banco Central, nota de 29/9/2026 (séries 25477 e 22022).</div></div>"""


def v_teto():
    listra = f"repeating-linear-gradient(135deg,{CORAL_CLARO} 0 14px,#F6D2C4 14px 28px)"
    return f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:40px 46px 40px'>
  <div style='display:flex;gap:6px'>
    <div style='flex:1;font-size:27px;font-weight:700;color:{CORAL_TXT}'>a dívida</div>
    <div style='flex:1;font-size:27px;font-weight:700;color:{CORAL_FORTE};padding-left:4px'>juros e encargos, somados</div></div>
  <div style='display:flex;height:96px;gap:6px;margin-top:14px'>
    <div style='flex:1;background:{CORAL};border-radius:20px 0 0 20px;display:flex;align-items:center;padding-left:28px;color:#fff;font-size:40px;font-weight:700;letter-spacing:-.02em'>R$ 1.000</div>
    <div style='flex:1;background:{listra};border-radius:0 20px 20px 0;display:flex;align-items:center;padding-left:28px;color:{CORAL_FORTE};font-size:40px;font-weight:700;letter-spacing:-.02em'>até R$ 1.000</div>
  </div>
  <div style='height:36px;margin-top:14px;border:4px solid {INK};border-top:none;border-radius:0 0 16px 16px'></div>
  <div style='display:flex;justify-content:center;margin-top:-4px'><div style='width:4px;height:26px;background:{INK}'></div></div>
  <div style='display:flex;justify-content:center'>
    <span style='display:inline-flex;align-items:baseline;gap:14px;background:{INK};color:#fff;padding:16px 34px;border-radius:999px'>
      <span style='font-size:30px;font-weight:600'>no máximo</span><span class='big' style='font-size:50px;color:#fff'>R$ 2.000</span></span></div>
</div><div class='nota'>Para o rotativo e o parcelamento da fatura contratados desde 3/1/2024. Lei 14.690/2023, art. 28; Res. CMN 4.549/2017, com a Res. CMN 5.112/2023.</div></div>"""


def v_cheque():
    pos = float(CHE_AM / CHE_TETO) * 100
    return f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:44px 48px 40px'>
  <div style='display:flex;align-items:baseline;justify-content:space-between'>
    <div><div class='rot'>Média de agosto de 2026</div><div class='big' style='font-size:92px;color:{CORAL_FORTE};margin-top:4px'>{num(CHE_AM)}%</div></div>
    <div style='text-align:right'><div class='rot'>Teto</div><div class='big' style='font-size:92px;margin-top:4px'>8%</div></div></div>
  <div style='position:relative;height:120px;margin-top:30px'>
    <div style='position:absolute;left:0;right:0;top:34px;height:40px;border-radius:20px;background:{FIO}'></div>
    <div style='position:absolute;left:0;top:34px;height:40px;width:{pos:.2f}%;border-radius:20px 0 0 20px;background:{CORAL}'></div>
    <i style='position:absolute;right:0;top:14px;width:8px;height:80px;border-radius:4px;background:{INK};display:block'></i>
    <div style='position:absolute;left:0;top:90px;font-size:24px;font-weight:600;color:{MUTED}'>0%</div>
    <div style='position:absolute;right:0;top:94px;font-size:24px;font-weight:700;color:{INK}'>8% ao mês</div>
  </div>
  <div class='fio' style='margin:10px 0 24px'></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span style='font-size:30px;font-weight:600;color:{MUTED}'>A média, no ano</span>
    <span class='big' style='font-size:54px'>{num(CHE_AA)}%</span></div>
</div><div class='nota'>Teto desde 6/1/2020: Res. CMN 4.765/2019, art. 3º. Fonte das médias: Banco Central, nota de 29/9/2026 (séries 25463 e 20741).</div></div>"""


def post_minimo():
    T = 7
    s = [capa_minimo(T)]

    s.append(slide("light", EXTRA_C1 + topo(
        "O resto", "O que não é pago vira rotativo.",
        "Pagou menos que o total? O saldo vira um financiamento: o crédito rotativo, com juros.",
        estilo_p="margin-top:28px") + v_rotativo_fluxo(), 2, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Quanto custa", "A taxa média do rotativo em agosto de 2026.", estilo_t="font-size:72px") + v_taxa_rotativo(), 3, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Tem teto", "Os juros não passam do valor da dívida.",
        "Rotativo e parcelamento da fatura somados: R$ 1.000 viram, no máximo, R$ 2.000.",
        estilo_p="font-size:34px;margin-top:26px") + v_teto(), 4, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Cheque especial", "Também tem teto: 8% ao mês.",
        "E a média de agosto ficou perto dele.", estilo_p="margin-top:26px") + v_cheque(), 5, T))

    det = tela(P11, "celular-cartao-principal-11-11.png")
    pend = tela(P11, "celular-pendentes-dezembro-11-11.png")
    s.append(slide("light", EXTRA_C1 + topo(
        "No timtimcash", "A fatura antes de vencer.",
        "Cada cartão mostra a fatura atual, o “Limite usado” e o “Disponível”. A fatura não paga aparece em Pendentes.",
        cls="h3", estilo_p="font-size:33px;margin-top:16px")
        + f"""<div class='visual' style='margin-top:28px'>{recorte(det, 765, 1574, largura=660, x0=3, x1=1167, raio=32)}
<div style='height:14px'></div>{recorte(pend, 1466, 1748, largura=660, x0=45, x1=1125)}{NOTA_TELA}</div>""", 6, T))

    s.append(fechamento_verde("Veja a fatura antes que ela vire rotativo.",
        "Cartões de crédito no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_c1(h) for h in s]


# ============================================================================ 13/11 · Black Friday: o desconto é de verdade?
ANTES, VESPERA = D("200"), D("400")
BF = VESPERA * D("0.5")
assert BF == ANTES          # metade do dobro


def riscado(txt, fs, cor, traco):
    return (f"<span style='position:relative;display:inline-block;font-size:{fs}px;font-weight:700;color:{cor};letter-spacing:-.035em;line-height:1.05'>{txt}"
            f"<i style='position:absolute;left:-10px;right:-10px;top:50%;height:{traco}px;margin-top:-{traco // 2}px;background:{cor};border-radius:{traco}px;display:block;transform:rotate(-7deg)'></i></span>")


def etiqueta_bf():
    """Uma etiqueta só, com a história do preço: R$ 200 riscado, R$ 400 riscado e −50% = R$ 200."""
    W, H = 556, 560
    forma = (f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='position:absolute;left:0;top:0;overflow:visible'>"
             f"<defs><filter id='sv' x='-20%' y='-15%' width='140%' height='140%'><feDropShadow dx='0' dy='26' stdDeviation='24' flood-color='#032e21' flood-opacity='.38'/></filter></defs>"
             f"<path d='M24 126 L{W / 2} 10 L{W - 24} 126 V{H - 30} a26 26 0 0 1 -26 26 H50 a26 26 0 0 1 -26 -26 Z' fill='#fff' filter='url(#sv)'/>"
             f"<circle cx='{W / 2}' cy='94' r='21' fill='{BRAND}' stroke='{SOFT}' stroke-width='7'/>"
             f"</svg>")
    return f"""<div style='position:relative;width:{W}px;height:{H}px;transform:rotate(-5deg)'>
  {forma}
  <div style='position:absolute;left:24px;right:24px;top:152px;display:flex;flex-direction:column;align-items:center'>
    {riscado('R$ 200', 46, MUTED, 5)}
    <div style='margin-top:10px'>{riscado('R$ 400', 76, INK, 7)}</div>
    <span style='margin-top:22px;background:{INK};color:#fff;font-size:38px;font-weight:700;padding:8px 20px;border-radius:14px;letter-spacing:-.02em'>−50%</span>
    <span class='big' style='font-size:112px;color:{BRAND_DARK};line-height:1;margin-top:10px'>R$ 200</span>
  </div>
</div>"""


def capa_bf(T):
    corpo = f"""<div class='eyebrow'>Black Friday</div>
<div class='h1' style='font-size:108px'>O desconto é de verdade?</div>
<div style='display:flex;align-items:center;gap:24px;margin-top:40px'>
  <div style='flex:none;margin-left:4px'>{etiqueta_bf()}</div>
  <div style='flex:1;font-size:62px;font-weight:700;letter-spacing:-.045em;line-height:1.04;color:#fff'>“metade do dobro”</div>
</div>"""
    return capa("verde", EXTRA_C1 + corpo, 1, T)


def v_metade_do_dobro():
    """Preço ao longo do tempo: R$ 200, sobe para R$ 400 antes da Black Friday e cai 50% no dia: R$ 200 de novo."""
    W, Hc = 808, 300
    base = 262                                            # linha do tempo
    y = lambda v: {200: 196, 400: 70}[v]                  # alturas da ilustração (sem escala de valores)
    x_sobe, x_bf = 452, 662
    pts = f"0,{y(200)} {x_sobe},{y(200)} {x_sobe},{y(400)} {x_bf},{y(400)} {x_bf},{y(200)} {W},{y(200)}"
    area = f"0,{base} 0,{y(200)} {x_sobe},{y(200)} {x_sobe},{y(400)} {x_bf},{y(400)} {x_bf},{y(200)} {W},{y(200)} {W},{base}"
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:38px 40px 30px'>
  <svg width='{W}' height='{Hc}' viewBox='0 0 {W} {Hc}' style='display:block;overflow:visible'>
    <polygon points='{area}' fill='#F6F5EF'/>
    <line x1='0' y1='{base}' x2='{W}' y2='{base}' stroke='{NEUTRO}' stroke-width='3'/>
    <line x1='{x_sobe}' y1='{y(200)}' x2='{x_bf}' y2='{y(200)}' stroke='{NEUTRO}' stroke-width='3' stroke-dasharray='6 10'/>
    <polyline points='{pts}' fill='none' stroke='{INK}' stroke-width='7' stroke-linejoin='round' stroke-linecap='round'/>
    <line x1='{x_bf}' y1='{y(200) + 16}' x2='{x_bf}' y2='{base}' stroke='{BRAND}' stroke-width='3' stroke-dasharray='5 8'/>
    <circle cx='{x_bf}' cy='{y(200)}' r='17' fill='{BRAND}' stroke='#fff' stroke-width='6'/>
    <text x='18' y='{y(200) - 24}' font-family='Inter' font-weight='700' font-size='34' fill='{INK}'>R$ 200</text>
    <text x='{(x_sobe + x_bf) / 2:.0f}' y='{y(400) - 22}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='34' fill='{CORAL_FORTE}'>R$ 400</text>
    <text x='{(x_sobe + x_bf) / 2:.0f}' y='{y(400) + 64}' text-anchor='middle' font-family='Inter' font-weight='600' font-size='25' fill='{MUTED}'>sobe antes</text>
    <rect x='{x_bf + 22}' y='{(y(400) + y(200)) / 2 - 27:.0f}' width='118' height='54' rx='14' fill='{INK}'/>
    <text x='{x_bf + 81}' y='{(y(400) + y(200)) / 2 + 11:.0f}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='31' fill='#fff'>−50%</text>
    <text x='{x_bf}' y='{base + 34}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='25' fill='{BRAND_DARK}'>Black Friday</text>
    <text x='0' y='{base + 34}' font-family='Inter' font-weight='600' font-size='24' fill='{MUTED}'>semanas antes</text>
  </svg>
  <div class='fio' style='margin:30px 0 22px'></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span style='font-size:30px;font-weight:600;color:{MUTED}'>Preço na Black Friday</span>
    <span><span class='big' style='font-size:52px'>R$ 200</span><span style='font-size:28px;font-weight:700;color:{CORAL_TXT}'> o mesmo de antes</span></span></div>
</div><div class='nota'>Exemplo ilustrativo. Alertas do Procon de Suzano (19/08/2026) e do Procon-MPMG (“Tudo pela metade do dobro?”).</div></div>"""


def v_sessenta_dias():
    W, Hc = 808, 300
    import math
    n = 61
    vals = []
    for i in range(n):
        v = 255 + 22 * math.sin(i / 6.5) + 14 * math.sin(i / 2.3 + 1.1) - (34 if 30 <= i <= 33 else 0) * (1 - abs(i - 31.5) / 2.5)
        vals.append(v)
    imin = min(range(n), key=lambda i: vals[i])
    xi = lambda i: 20 + i * (W - 240) / (n - 1)
    yv = lambda v: 40 + (300 - v) / 100 * 200
    linha = " ".join(f"{xi(i):.1f},{yv(v):.1f}" for i, v in enumerate(vals))
    xh, yh = xi(n - 1), yv(vals[-1])
    xbf = W - 40
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:36px 40px 28px'>
  <svg width='{W}' height='{Hc}' viewBox='0 0 {W} {Hc}' style='display:block;overflow:visible'>
    <rect x='20' y='20' width='{xh - 20:.1f}' height='230' rx='14' fill='#F6F5EF'/>
    <text x='34' y='54' font-family='Inter' font-weight='700' font-size='22' letter-spacing='3' fill='{MUTED}'>ÚLTIMOS 60 DIAS</text>
    <polyline points='{linha}' fill='none' stroke='{INK}' stroke-width='5' stroke-linejoin='round' stroke-linecap='round'/>
    <circle cx='{xi(imin):.1f}' cy='{yv(vals[imin]):.1f}' r='14' fill='{BRAND}' stroke='#fff' stroke-width='5'/>
    <text x='{xi(imin):.1f}' y='{yv(vals[imin]) + 50:.1f}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='26' fill='{BRAND_DARK}'>menor preço</text>
    <circle cx='{xh:.1f}' cy='{yh:.1f}' r='16' fill='{INK}' stroke='#fff' stroke-width='6'/>
    <line x1='{xbf}' y1='20' x2='{xbf}' y2='250' stroke='{CORAL}' stroke-width='4' stroke-dasharray='8 10' stroke-linecap='round'/>
    <text x='{xbf}' y='{Hc - 6}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='26' fill='{CORAL_TXT}'>27/11</text>
    <text x='{xh:.1f}' y='{Hc - 6}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='26' fill='{INK}'>hoje, 13/11</text>
    <text x='20' y='{Hc - 6}' font-family='Inter' font-weight='600' font-size='24' fill='{MUTED}'>14/09</text>
  </svg>
  <div class='fio' style='margin:22px 0 22px'></div>
  <div style='display:flex;gap:22px;align-items:center'>{azulejo(I_ESCUDO, 76, 38)}
    <div style='font-size:30px;line-height:1.35'>O Procon-SP pediu às lojas desconto sobre o menor preço dos últimos 60 dias.</div></div>
</div><div class='nota'>Gráfico ilustrativo. Procon-MPMG, folder “Tudo pela metade do dobro?”; Procon-SP, 06/11/2025.</div></div>"""


def v_lista_procon():
    linhas = "".join(f"""<div style='display:flex;align-items:center;gap:22px;padding:20px 0;{'' if i == 2 else f'border-bottom:2px solid {FIO};'}'>
  <span style='width:46px;height:46px;border-radius:50%;background:#FBEAEA;display:flex;align-items:center;justify-content:center;flex:none'>{svg_icone(I_X, 24, RED_TEXT, 3)}</span>
  <span class='sk' style='width:{w}px;height:20px'></span><span class='sk' style='width:{w2}px;height:20px;margin-left:auto'></span></div>""" for i, (w, w2) in enumerate([(300, 120), (360, 90), (250, 140)]))
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:34px 44px 14px'>
  <div style='display:flex;align-items:center;gap:22px'>{azulejo(I_ESCUDO, 84, 42)}
    <div><div style='font-size:40px;font-weight:700;letter-spacing:-.03em'>“Evite esses sites”</div>
      <div style='font-size:27px;font-weight:600;color:{MUTED};margin-top:4px'>a lista do Procon-SP</div></div></div>
  <div style='display:flex;align-items:center;gap:16px;margin-top:28px;height:78px;border-radius:999px;background:#F6F5EF;border:2px solid {FIO};padding:0 28px'>
    {svg_icone(I_LUPA, 34, MUTED, 2.4)}<span style='font-size:30px;font-weight:500;color:{MUTED}'>a loja que você não conhece</span></div>
  <div style='margin-top:8px'>{linhas}</div>
</div><div class='nota'>Ilustração. Fonte: Procon-SP, Guia de Comércio Eletrônico.</div></div>"""


def v_sete_dias():
    tiles = []
    for d in range(0, 8):
        if d == 0:
            tiles.append(f"""<div style='flex:1.25;display:flex;flex-direction:column;align-items:center;gap:12px'>
  <div style='width:100%;height:136px;border-radius:22px;background:{INK};display:flex;align-items:center;justify-content:center'>{svg_icone(I_CAIXA, 58, '#fff', 2)}</div>
  <div style='font-size:24px;font-weight:700;color:{INK};white-space:nowrap'>chegou</div></div>""")
        else:
            ultimo = d == 7
            tiles.append(f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:12px'>
  <div style='width:100%;height:136px;border-radius:22px;background:{BRAND if ultimo else SOFT};display:flex;align-items:center;justify-content:center;
    font-size:52px;font-weight:700;color:{'#fff' if ultimo else BRAND_DEEP};font-variant-numeric:tabular-nums'>{d}</div>
  <div style='font-size:24px;font-weight:700;color:{BRAND_DARK if ultimo else MUTED};white-space:nowrap'>{'7º dia' if ultimo else ''}&nbsp;</div></div>""")
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:36px 34px 30px'>
  <div style='display:flex;gap:10px'>{''.join(tiles)}</div>
  <div class='fio' style='margin:22px 0 26px'></div>
  <div style='display:flex;gap:22px;align-items:center'>{azulejo(I_VOLTA, 76, 38)}
    <div style='font-size:30px;line-height:1.35'>O dinheiro volta de imediato. E dá para desistir pelo mesmo canal em que você comprou.</div></div>
</div><div class='nota'>CDC (Lei 8.078/1990), art. 49; Decreto 7.962/2013, art. 5º.</div></div>"""


def v_guarde():
    def doc(ip, nome, sub, rot):
        return f"""<div style='flex:1;background:#fff;border:1px solid {FIO};border-radius:26px;padding:30px 26px 28px;transform:rotate({rot}deg);
    box-shadow:0 1px 2px rgba(15,20,16,.05),0 24px 40px -26px rgba(15,20,16,.35);position:relative'>
  <span style='position:absolute;right:-14px;top:-14px;width:54px;height:54px;border-radius:50%;background:{BRAND};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px {BG}'>{svg_icone(I_CHECK, 28, '#fff', 3)}</span>
  {azulejo(ip, 80, 40)}
  <div style='font-size:34px;font-weight:700;letter-spacing:-.03em;margin-top:24px'>{nome}</div>
  <div style='font-size:24px;font-weight:500;color:{MUTED};margin-top:6px;line-height:1.3'>{sub}</div>
  <div class='sk' style='width:85%;margin-top:22px'></div><div class='sk' style='width:60%;margin-top:12px'></div></div>"""
    return f"""<div class='visual' style='margin-top:52px;display:flex;gap:24px;padding:0 22px 0 4px'>
  {doc(I_IMG, 'Anúncio', 'o print do preço', -2.5)}
  {doc(I_DOC, 'Pedido', 'a confirmação', 0)}
  {doc(I_RECIBO, 'Comprovante', 'do pagamento', 2.5)}
</div><div class='nota' style='margin-top:40px'>CDC (Lei 8.078/1990), art. 30. Procon-SP, Guia de Comércio Eletrônico.</div>"""


def post_bf():
    T = 7
    s = [capa_bf(T)]

    s.append(slide("light", EXTRA_C1 + topo(
        "Metade do dobro", "Sobe antes, cai pela metade.",
        "Subir o preço antes e dar 50% na Black Friday: você paga o mesmo de antes.",
        estilo_p="margin-top:24px") + v_metade_do_dobro(), 2, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Anote o preço hoje", "Faltam duas semanas.",
        "O Procon-MPMG orienta monitorar o preço. Anote o de hoje e compare no dia 27.",
        estilo_p="font-size:36px;margin-top:24px") + v_sessenta_dias(), 3, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Loja confiável", "Antes de pagar, consulte a lista.",
        "Comprando numa loja que você não conhece? Veja se ela está na lista “Evite esses sites”, do Procon-SP.",
        estilo_p="font-size:36px;margin-top:24px") + v_lista_procon(), 4, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Comprou pela internet?", "7 dias para desistir.",
        "O prazo conta da compra ou do recebimento do produto.",
        estilo_p="margin-top:26px") + v_sete_dias(), 5, T))

    s.append(slide("light", EXTRA_C1 + topo(
        "Guarde tudo", "A oferta anunciada vale.",
        "Guarde o anúncio, a confirmação do pedido e o comprovante: a oferta obriga a loja.",
        estilo_p="margin-top:26px") + v_guarde(), 6, T))

    s.append(fechamento_verde("Compre com a lista e com um teto.",
        "Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_c1(h) for h in s]


POSTS = {
    P01: post_novembro,
    P05: post_ptax,
    P07: post_assinaturas,
    P11: post_minimo,
    P13: post_bf,
}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    renderizar(POSTS, so=so)
