# -*- coding: utf-8 -*-
"""Carrosséis da equipe ja · janeiro de 2027 (02, 06, 08, 11 e 14/01), no formato aprovado em outubro a dezembro
(J/kit/carrossel.py; modelos em novdez/equipes/dc1/posts.py e dc2/posts.py).

Telas reais (build 2026-10-19.5) capturadas por captura.py e guardadas em J/saida/<pasta>/telas/; as caixas (px CSS
da janela, escala 3) ficam em caixas.json. A série "Comece 2027" usa o selo de selo_comece2027.py. Toda conta dos
slides é conferida por assert neste arquivo, contra as telas e os fatos.

python3 posts.py                       renderiza os posts e confere o layout
python3 posts.py <pasta> [<pasta>...]  só os escolhidos
"""
import os, re, sys, json, calendar
from datetime import date, timedelta
from decimal import Decimal as D, ROUND_HALF_UP

J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, J + "/kit")
sys.path.insert(0, AQUI)
from carrossel import *   # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl, sem_quebra...)
from selo_comece2027 import selo, selo_com_nome, sobretitulo, NOMES, PERGUNTAS, DIAS, TINTA_2, TINTA_FIO

CX = json.load(open(os.path.join(AQUI, "caixas.json"), encoding="utf-8"))

P02 = "2027-01-02_comece-2027-organizado"
P06 = "2027-01-06_material-escolar-o-que-a-escola-nao-pode-pedir"
P08 = "2027-01-08_habito-leva-66-dias"
P11 = "2027-01-27_categorias-que-funcionam"
P14 = "2027-01-14_passo-3-os-limites"

NBSP = " "
MENOS = "−"
SEM = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def q2(v):
    return D(v).quantize(D("0.01"), ROUND_HALF_UP)


def px(v):
    """px CSS das capturas (escala 3) para px da imagem."""
    return int(round(v * 3))


def tela(pasta, nome):
    caminho = os.path.join(SAIDA, pasta, "telas", nome)
    assert os.path.isfile(caminho), caminho
    return caminho


def sem_quebra_ja(html):
    """sem_quebra do kit; e mais: número junto da lei e do artigo, "Passo" junto do número."""
    html = sem_quebra(html)
    html = re.sub(r"\b(Lei|Decreto|art\.|arts\.|nº|Passo|passo|PASSO) (\d)", lambda m: m.group(1) + NBSP + m.group(2), html)
    return html


EXTRA_J = EXTRA + f"""<style>
.tab{{font-variant-numeric:tabular-nums}}
.rs{{font-size:22px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTED}}}
.pilula{{display:inline-flex;align-items:center;gap:12px;background:{SOFT};color:{BRAND_DEEP};font-size:27px;font-weight:700;padding:14px 26px;border-radius:999px}}
.linha-item{{display:flex;gap:28px;align-items:center;padding:22px 0}}
.linha-item + .linha-item{{border-top:2px solid {FIO}}}
.nota{{text-wrap:balance}}
</style>"""


def topo(sobre, titulo, apoio=None, cls="h2", estilo_t="", estilo_p=""):
    p = f"<div class='p' style='{estilo_p}'>{apoio}</div>" if apoio else ""
    return f"<div class='eyebrow'>{sobre}</div><div class='{cls}' style='{estilo_t}'>{titulo}</div>{p}"


def pilula(ip, txt):
    return f"<span class='pilula'>{svg_icone(ip, 30, BRAND_DEEP, 2.2)}{txt}</span>"


# ícones de traço próprios (24 × 24, pontas redondas)
I_SETA = '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>'
I_MARCA_SALVAR = '<path d="M7 3.5h10a1 1 0 0 1 1 1V21l-6-4-6 4V4.5a1 1 0 0 1 1-1z"/>'
I_ETIQUETA = '<path d="M3.5 12.2V4.5a1 1 0 0 1 1-1h7.7l8.3 8.3a1.4 1.4 0 0 1 0 2l-6.2 6.2a1.4 1.4 0 0 1-2 0z"/><circle cx="8" cy="8" r="1.6"/>'
I_REVISAO = '<path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v4.5h-4.5"/><path d="M8.5 12.3l2.4 2.4 4.6-4.9"/>'


# ============================================================================ 02/01 · 2027 começa organizado
PASSOS_DIA = {1: date(2027, 1, 4), 2: date(2027, 1, 10), 3: date(2027, 1, 14), 4: date(2027, 1, 18)}
REVISAO = date(2027, 1, 30)
assert {k: v.strftime("%d/%m") for k, v in PASSOS_DIA.items()} == DIAS
assert [SEM[d.weekday()] for d in PASSOS_DIA.values()] == ["seg", "dom", "qui", "seg"] and SEM[REVISAO.weekday()] == "sáb"
# números das telas (caixas.json e o texto das telas, ver captura.py)
PATRIMONIO_0401 = D("112730.86")
CONTAS_0401 = {"Banco na Europa": D("11525.40"), "Conta corrente": D("18230.86"), "Corretora no exterior": D("60000.00"),
               "Reserva": D("22974.60")}
assert sum(CONTAS_0401.values()) == PATRIMONIO_0401
DESP_1001 = {"Casa": D("2300.00"), "Educação": D("1450.00"), "Mercado": D("402.30"), "Transporte": D("392.00"),
             "Bares e restaurantes": D("212.50"), "Saúde": D("63.20")}
assert sum(DESP_1001.values()) == D("4820.00")          # "Despesas R$ 4.820,00 · 6 categorias" no centro da rosca


def capa_comece(T):
    """Os 4 selos numa trilha que sobe, com o nome de cada passo embaixo."""
    S, SOBE, NOME = 186, 104, 62
    PASSO_X = (896 - S) / 3
    blocos = []
    for k in range(1, 5):
        x = (k - 1) * PASSO_X
        y = (4 - k) * SOBE
        blocos.append(f"<div style='position:absolute;left:{x:.1f}px;top:{y}px;width:{S}px'>"
                      f"{selo_com_nome(k, S, 'tinta', tam_nome=34)}</div>")
    # trilha pontilhada ligando os selos (por trás deles)
    pts = " ".join(f"{(k - 1) * PASSO_X + S / 2:.0f},{(4 - k) * SOBE + S / 2:.0f}" for k in range(1, 5))
    trilha = (f"<svg width='896' height='{3 * SOBE + S}' style='position:absolute;left:0;top:0;overflow:visible'>"
              f"<polyline points='{pts}' fill='none' stroke='{MENTA}' stroke-width='7' stroke-linecap='round' "
              f"stroke-dasharray='0.1 19'/></svg>")
    alt = 3 * SOBE + S + NOME
    vis = f"<div class='visual' style='position:relative;height:{alt}px;margin-top:76px'>{trilha}{''.join(blocos)}</div>"
    corpo = f"""<div class='eyebrow'>{sobretitulo()}</div>
<div class='h1' style='font-size:112px'>2027 começa organizado.</div>{vis}"""
    return capa("tinta", EXTRA_J + corpo, 1, T)


def v_agenda():
    def linha(dia, rot, sub, direita, primeira=False):
        borda = "" if primeira else f"border-top:2px solid {FIO};"
        return f"""<div style='display:grid;grid-template-columns:96px 1fr auto;align-items:center;column-gap:28px;padding:15px 0;{borda}'>
  <div style='text-align:center'><div class='tab' style='font-size:52px;font-weight:700;letter-spacing:-.04em;line-height:1;color:{INK}'>{dia.day:02d}</div>
    <div style='font-size:20px;font-weight:700;letter-spacing:.14em;color:{MUTED};margin-top:7px'>{SEM[dia.weekday()].upper()}</div></div>
  <div><div style='font-size:32px;font-weight:700;letter-spacing:-.025em;line-height:1.15'>{rot}</div>
    <div style='font-size:26px;color:{MUTED};margin-top:4px'>{sub}</div></div>
  {direita}</div>"""
    linhas = [linha(PASSOS_DIA[k], f"Passo {k} · {NOMES[k]}", PERGUNTAS[k], selo(k, 76), k == 1) for k in range(1, 5)]
    linhas.append(linha(REVISAO, "Revisão de sábado", "5 minutos por semana", azulejo(I_REVISAO, 76, 40)))
    cab = (f"<div style='display:flex;justify-content:space-between;align-items:baseline;padding:22px 0 14px;border-bottom:2px solid {FIO}'>"
           f"<span class='rs' style='color:{BRAND_DARK}'>Janeiro de 2027</span><span class='rs'>dia do post</span></div>")
    return f"<div class='visual' style='margin-top:36px'><div class='card' style='padding:0 40px 6px'>{cab}{''.join(linhas)}</div></div>"


def passo_slide(k, idx, T, apoio, crop_html, estilo_p=""):
    cab = f"""<div class='eyebrow'>{sobretitulo(k)}</div>
<div style='display:flex;align-items:center;gap:32px'>{selo(k, 118)}
  <div><div style='font-size:30px;font-weight:700;color:{BRAND_DARK};letter-spacing:-.01em'>{NOMES[k]}</div>
    <div class='h3' style='font-size:66px;margin-top:4px'>{PERGUNTAS[k]}</div></div></div>
<div class='p' style='font-size:34px;margin-top:26px;{estilo_p}'>{apoio}</div>"""
    return slide("light", EXTRA_J + cab + f"<div class='visual' style='margin-top:30px'>{crop_html}{NOTA_TELA}</div>", idx, T)


def post_comece():
    T = 7
    s = [capa_comece(T)]
    s.append(slide("light", EXTRA_J + topo(
        "A série de janeiro", "Um passo de cada vez.",
        "Cada passo sai num post:<br>o que fazer e onde fica no site.", estilo_p="font-size:36px;margin-top:24px") + v_agenda(), 2, T))

    contas = tela(P02, "celular-contas-e-carteiras-04-01.png")
    c = CX["0401_contas"]
    y0, y1 = c["4 contas"][1] + 27, c["Nova conta"][1] + c["Nova conta"][3] + 14
    s.append(passo_slide(1, 3, T, "Em <b style='color:#0F1410'>Contas e carteiras</b>, cadastre cada conta com o saldo de hoje. "
                         "O Patrimônio consolidado soma tudo.", recorte(contas, px(y0), px(y1), largura=520)))

    visao = tela(P02, "celular-visao-geral-10-01.png")
    pc = CX["1001_visao"]["painel_por_categoria"]
    s.append(passo_slide(2, 4, T, "Lance cada gasto com a categoria. Na <b style='color:#0F1410'>Visão geral</b>, "
                         "o painel Por categoria mostra para onde foi.",
                         recorte(visao, px(pc[1]), px(CX["1001_visao"]["Top saídas"][1] - 8), largura=520, x0=px(pc[0]), x1=px(pc[0] + pc[2]))))

    orc = tela(P02, "celular-orcamentos-sem-limites-14-01.png")
    cm = CX["1401_sem_limites"]["cartao_media"]
    s.append(passo_slide(3, 5, T, "Em <b style='color:#0F1410'>Orçamentos</b>, dê um limite a cada categoria. "
                         "Comece pela sua média.", recorte(orc, px(cm[1] - 12), px(cm[1] + cm[3] + 12), largura=430, x0=px(cm[0] - 12), x1=px(cm[0] + cm[2] + 12))))

    sim = tela(P02, "celular-simulacao-cenario-base-18-01.png")
    es = CX["1801_sim"]["es"]
    s.append(passo_slide(4, 6, T, "Na <b style='color:#0F1410'>Simulação futura</b>, o E se… testa um susto sobre o cenário, "
                         "sem mudar nada.", recorte(sim, px(es[1] - 6), px(es[1] + es[3] + 8), largura=780, x0=px(es[0] - 10), x1=px(es[0] + es[2] + 10))))

    s.append(fechamento_verde("Comece hoje: crie sua conta com nome, e-mail e senha.",
                              "Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_ja(h) for h in s]


# ============================================================================ 14/01 · Passo 3: os limites
# Orçamentos da conta de base em 14/01/2027 (texto da tela, captura.py): dia 14 de 31, 45% do período.
DIA, DIAS_MES = 14, 31
ORC = {  # categoria: (gasto no mês até 14/01, limite)
    "Bares e restaurantes": (D("284.40"), D("600")), "Mercado": (D("840.10"), D("2000")),
    "Transporte": (D("486.00"), D("1950")), "Saúde": (D("63.20"), D("500")), "Lazer e hobbies": (D("0"), D("400"))}
SEM_LIMITE = {"Educação": D("2390.00"), "Casa": D("2300.00"), "Assinaturas e serviços": D("55.90")}
assert sum(v for v, _ in ORC.values()) == D("1673.70") and sum(l for _, l in ORC.values()) == D("5450")   # "R$ 1.673,70 no orçamento de R$ 5.450,00"
assert sum(SEM_LIMITE.values()) == D("4745.90")                                                       # "R$ 4.745,90 sem limite"


def faixa_de(gasto, limite):
    """A regra do site (_orcRisco): passou do limite; senão, a projeção do ritmo (gasto ÷ fração do mês)."""
    if gasto > limite:
        return "passou"
    proj = gasto / (D(DIA) / D(DIAS_MES))
    return "estouro" if proj > limite * D("1.02") else ("limite" if proj >= limite * D("0.9") else "ok")


FAIXA_JAN = {c: faixa_de(g, l) for c, (g, l) in ORC.items()}
assert FAIXA_JAN == {"Bares e restaurantes": "estouro", "Mercado": "limite", "Transporte": "ok", "Saúde": "ok", "Lazer e hobbies": "ok"}
# a tela trunca os inteiros (fmtBRLInt usa Math.trunc): "no ritmo, fecha em R$ 629" e "R$ 1.860"
assert int(ORC["Bares e restaurantes"][0] / (D(DIA) / D(DIAS_MES))) == 629 and int(ORC["Mercado"][0] / (D(DIA) / D(DIAS_MES))) == 1860
# o cartão "Comece pela sua média" (cópia sem limites) e a média de 12 meses (jan a dez/26) da conta
MEDIA_SUG = {"Casa": D("2600"), "Mercado": D("1600"), "Educação": D("1500"), "Transporte": D("1200"),
             "Bares e restaurantes": D("700"), "Lazer e hobbies": D("370")}
FAIXAS_SITE = [  # chave, nome na tela, cor do título na tela, regra
    ("passou", "Já passaram do limite", RED_TEXT, "o gasto já passou do limite"),
    ("estouro", "Vão estourar no ritmo atual", RED_TEXT, "no ritmo de hoje, o mês fecha acima do limite"),
    ("limite", "No limite", AMBER_TEXT, "no ritmo, fecha entre 90% e 102% do limite"),
    ("ok", "Tranquilas", BRAND_DARK, "no ritmo, fecha abaixo de 90% do limite"),
    ("sem", "Sem limite definido", "#656C62", "a categoria ainda não tem limite"),
]


def mini_barra(k, larg=150):
    """Barrinha no desenho do site: a marca de hoje em 45% (dia 14 de 31) e o preenchimento de cada faixa."""
    hoje = DIA / DIAS_MES * larg
    enche = {"passou": (1.0, RED), "estouro": (0.58, RED), "limite": (0.44, AMBER_BAR), "ok": (0.22, BRAND), "sem": (0, None)}[k]
    trilho = (f"background:{FIO}" if k != "sem" else f"background:#fff;box-shadow:inset 0 0 0 2px {NEUTRO}")
    fill = (f"<div style='position:absolute;left:0;top:0;bottom:0;width:{enche[0] * larg:.0f}px;border-radius:7px;background:{enche[1]}'></div>"
            if enche[1] else "")
    marca = f"<div style='position:absolute;left:{hoje:.0f}px;top:-7px;width:3px;height:28px;border-radius:2px;background:{INK}'></div>"
    return f"<div style='position:relative;flex:none;width:{larg}px;height:14px;border-radius:7px;{trilho}'>{fill}{marca}</div>"


def capa_limites(T):
    """Selo 3 e três barras de categoria com a marca de hoje (como em Progresso por categoria)."""
    W, H, G = 560, 54, 36
    hoje = 0.45 * W
    barras = [(0.62, CORAL), (0.43, AMBER), (0.21, "#fff")]
    linhas = "".join(
        f"<div style='position:relative;width:{W}px;height:{H}px;border-radius:{H / 2}px;background:{BRAND_DARK}'>"
        f"<div style='position:absolute;left:0;top:0;bottom:0;width:{p * W:.0f}px;border-radius:{H / 2}px;background:{c}'></div></div>"
        for p, c in barras)
    alt = 3 * H + 2 * G
    marca = (f"<div style='position:absolute;left:{hoje:.0f}px;top:-26px;width:6px;height:{alt + 44}px;border-radius:3px;background:{INK}'></div>"
             f"<div style='position:absolute;left:{hoje - 60:.0f}px;width:126px;top:-76px;text-align:center;font-size:32px;font-weight:700;color:{INK}'>hoje</div>")
    vis = f"""<div class='visual' style='margin-top:120px;display:flex;align-items:center;justify-content:space-between'>
  {selo(3, 262, 'verde')}
  <div style='position:relative;display:flex;flex-direction:column;gap:{G}px;margin-top:30px'>{linhas}{marca}</div>
</div>"""
    corpo = f"""<div class='eyebrow'>{sobretitulo(3)}</div>
<div class='h1' style='font-size:110px'>Quanto cabe em cada categoria?</div>{vis}"""
    return capa("verde", EXTRA_J + corpo, 1, T)


def v_faixas_janeiro():
    cats = {k: [c for c, f in FAIXA_JAN.items() if f == k] for k, _, _, _ in FAIXAS_SITE}
    cats["sem"] = list(SEM_LIMITE)
    linhas = []
    for i, (k, nome, cor, regra) in enumerate(FAIXAS_SITE):
        chips = ("".join(f"<span style='display:inline-block;padding:4px 14px;border-radius:999px;background:{BG};border:2px solid {FIO};"
                         f"font-size:22px;font-weight:600;color:{INK};margin:7px 8px 0 0'>{c}</span>" for c in cats[k])
                 or f"<span style='display:inline-block;font-size:22px;font-weight:600;color:{MUTED};margin-top:8px'>nenhuma em 14/01</span>")
        borda = f"border-top:2px solid {FIO};" if i else ""
        linhas.append(f"""<div style='display:flex;gap:30px;align-items:flex-start;padding:15px 0;{borda}'>
  <div style='padding-top:15px'>{mini_barra(k)}</div>
  <div style='flex:1'><div style='font-size:28px;font-weight:700;letter-spacing:.01em;color:{cor}'>{nome}</div>
    <div style='font-size:23px;color:{MUTED};margin-top:3px'>{regra}</div><div>{chips}</div></div></div>""")
    return f"""<div class='visual' style='margin-top:30px'><div class='card' style='padding:2px 40px'>{''.join(linhas)}</div>
<div class='nota'>A marca preta é hoje: dia 14 de 31.</div></div>"""


def post_limites():
    T = 6
    s = [capa_limites(T)]

    orc0 = tela(P14, "celular-orcamentos-sem-limites-14-01.png")
    cm = CX["1401_sem_limites"]["cartao_media"]
    s.append(slide("light", EXTRA_J + topo(
        "Orçamentos · sem limites ainda", "Comece pela sua média.",
        "O site sugere um limite por categoria: a sua média dos últimos 12 meses, arredondada para cima.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:30px'>{recorte(orc0, px(cm[1] - 12), px(cm[1] + cm[3] + 12), largura=470, x0=px(cm[0] - 12), x1=px(cm[0] + cm[2] + 12))}{NOTA_TELA}</div>", 2, T))

    orc = tela(P14, "celular-orcamentos-14-01.png")
    c = CX["1401_orc"]
    y0 = c["faixas"]["legenda"][1] - 10
    y1 = c["faixas"]["linhas"]["Mercado"][1] + c["faixas"]["linhas"]["Mercado"][3] + 8
    s.append(slide("light", EXTRA_J + topo(
        "Progresso por categoria · 14/01", "Cada categoria cai numa faixa.",
        "A marca vertical é hoje: a barra à esquerda dela está dentro do ritmo.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:30px'>{recorte(orc, px(y0), px(y1), largura=580, x0=px(14), x1=px(376))}{NOTA_TELA}</div>", 3, T))

    s.append(slide("light", EXTRA_J + topo(
        "As faixas · conta de exemplo em 14/01", "Cinco faixas dizem onde olhar.", cls="h3") + v_faixas_janeiro(), 4, T))

    # só o cabeçalho do painel e a primeira sugestão (Educação): o recorte para antes do fio da linha da Casa, cuja sugestão
    # (R$ 2.500) usa outro arredondamento que o quadro do slide 2 (R$ 2.600), e da linha de Assinaturas
    po = c["painel_onde"]
    edu, casa = c["sug_itens"][0], c["sug_itens"][1]
    assert edu[0].startswith("Educação") and casa[0].startswith("Casa") and c["rolagem"] == 0
    y_fim = casa[2] - 1
    s.append(slide("light", EXTRA_J + topo(
        "Sugestões do site", "Onde definir limite primeiro.",
        "A categoria sem limite que mais pesa no mês vem com um valor pela sua média.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:34px'>{recorte(orc, px(po[1]), px(y_fim), largura=640, x0=px(po[0]), x1=px(po[0] + po[2]))}{NOTA_TELA}</div>", 5, T))

    s.append(fechamento_verde("Passo 3: os limites.",
                              "Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra_ja(h) for h in s]


# ============================================================================ 11/01 · Categorias que funcionam
I_CARRO = ('<path d="M4 15.6v-3.3l1.9-4.6a2 2 0 0 1 1.8-1.2h8.6a2 2 0 0 1 1.8 1.2l1.9 4.6v3.3"/>'
           '<path d="M3.5 15.6h17M4.6 12.2h14.8"/><circle cx="7.8" cy="17.6" r="1.6"/><circle cx="16.2" cy="17.6" r="1.6"/>')
CATS_PADRAO = (21, 4)     # o cadastro começa com 21 categorias de despesa e 4 de receita (FUNCIONALIDADES; conferido na tela)


def etiqueta(txt, alt, fundo, cor, tam, icone=None, extra=""):
    """Etiqueta desenhada: bico à esquerda com o furo, corpo de cantos arredondados (cores da marca)."""
    w_bico = round(alt * .36)
    r = round(alt * .22)
    bico = (f"<svg width='{w_bico + 1}' height='{alt}' viewBox='0 0 {w_bico + 1} {alt}' style='display:block;flex:none'>"
            f"<path d='M{w_bico + 1} 0 L{w_bico * .32:.1f} {alt * .38:.1f} Q0 {alt * .5:.1f} {w_bico * .32:.1f} {alt * .62:.1f} L{w_bico + 1} {alt} Z' fill='{fundo}'/>"
            f"<circle cx='{w_bico * .78:.1f}' cy='{alt / 2:.1f}' r='{alt * .085:.1f}' fill='{BG}'/></svg>")
    ic = svg_icone(icone, round(tam * 1.05), cor, 2.2) if icone else ""
    corpo = (f"<div style='display:flex;align-items:center;gap:{round(tam * .4)}px;height:{alt}px;padding:0 {round(alt * .36)}px 0 {round(alt * .16)}px;"
             f"background:{fundo};border-radius:0 {r}px {r}px 0;color:{cor};font-size:{tam}px;font-weight:700;letter-spacing:-.02em;white-space:nowrap'>{ic}{txt}</div>")
    return f"<div style='display:inline-flex;align-items:center;{extra}'>{bico}{corpo}</div>"


def arvore(pai, icone, filhos, fundo_pai, x, y):
    """Uma categoria com duas subcategorias: etiquetas e os fios que ligam."""
    AP, AF, PASSO, RECUO = 122, 94, 120, 74
    partes = [f"<div style='position:absolute;left:{x}px;top:{y}px'>{etiqueta(pai, AP, fundo_pai, '#fff', 50, icone)}</div>"]
    fx = x + 44
    for i, f in enumerate(filhos):
        fy = y + AP + 28 + i * PASSO
        partes.append(f"<div style='position:absolute;left:{x + RECUO + 44}px;top:{fy}px'>{etiqueta(f, AF, SOFT, BRAND_DEEP, 39)}</div>")
        partes.append(f"<div style='position:absolute;left:{fx}px;top:{fy + AF / 2 - 2:.0f}px;width:{RECUO + 6}px;height:4px;border-radius:2px;background:{NEUTRO}'></div>")
    ult = y + AP + 28 + (len(filhos) - 1) * PASSO + AF / 2
    partes.append(f"<div style='position:absolute;left:{fx}px;top:{y + AP}px;width:4px;height:{ult - y - AP + 2:.0f}px;border-radius:2px;background:{NEUTRO}'></div>")
    return "".join(partes)


def capa_categorias(T):
    vis = (f"<div class='visual' style='position:relative;height:578px;margin-top:72px'>"
           f"{arvore('Casa', I_CASA, ['Aluguel', 'Luz'], BRAND, 0, 0)}"
           f"{arvore('Transporte', I_CARRO, ['Combustível', 'Estacionamento'], INK, 374, 188)}</div>")
    corpo = f"""<div class='eyebrow'>Organização</div>
<div class='h1' style='font-size:112px'>Categorias que funcionam.</div>{vis}"""
    return capa("papel", EXTRA_J + corpo, 1, T)


def regra(n, sobre, titulo, apoio, visual, idx, T, estilo_p=""):
    num = (f"<div style='flex:none;width:96px;height:96px;border-radius:50%;background:{SOFT};color:{BRAND_DEEP};display:flex;"
           f"align-items:center;justify-content:center;font-size:52px;font-weight:700;letter-spacing:-.03em' class='tab'>{n}</div>")
    cab = f"""<div class='eyebrow'>{sobre}</div>
<div style='display:flex;align-items:center;gap:30px'>{num}<div class='h3' style='font-size:62px'>{titulo}</div></div>
<div class='p' style='font-size:34px;margin-top:24px;{estilo_p}'>{apoio}</div>"""
    return slide("light", EXTRA_J + cab + visual, idx, T)


def post_categorias():
    T = 7
    s = [capa_categorias(T)]

    lista = tela(P11, "celular-categorias-despesas-11-01.png")
    cl = CX["1101_lista"]
    numeros = f"""<div style='flex:1;display:flex;flex-direction:column;gap:30px;padding-top:10px'>
  <div><div class='big tab' style='font-size:150px;line-height:.9;color:{INK}'>{CATS_PADRAO[0]}</div>
    <div style='font-size:30px;font-weight:700;color:{CORAL_TXT};margin-top:10px'>categorias de despesa</div></div>
  <div><div class='big tab' style='font-size:150px;line-height:.9;color:{INK}'>{CATS_PADRAO[1]}</div>
    <div style='font-size:30px;font-weight:700;color:{BRAND_DARK};margin-top:10px'>categorias de receita</div></div></div>"""
    crop = recorte(lista, px(cl["lista"][1] - 2), px(cl["Casa"][1] + 46 + 2 * 80), largura=470)
    s.append(regra(1, "Regra 1 · ponto de partida", "Comece pelas que já vêm.",
                   "O cadastro já traz as categorias mais comuns. Use antes de criar outras.",
                   f"<div class='visual' style='margin-top:30px;display:flex;gap:40px;align-items:flex-start'>{numeros}"
                   f"<div style='flex:none;width:470px'>{crop}<div class='nota' style='text-align:center;font-size:21px'>Tela real do timtimcash, com dados de exemplo.</div></div></div>", 2, T))

    subs = tela(P11, "celular-categorias-casa-subcategorias-11-01.png")
    g = CX["1101_casa_subs"]
    s.append(regra(2, "Regra 2 · subcategorias", "Poucas e claras.",
                   "O detalhe vai na subcategoria. Em Casa, Aluguel e Luz viram subcategorias.",
                   f"<div class='visual' style='margin-top:30px'>{recorte(subs, px(g['Bares e restaurantes'][1] - 24), px(g['Compras'][1] + 44), largura=660)}{NOTA_TELA}</div>", 3, T))

    ap = tela(P11, "celular-categorias-aparencia-casa-11-01.png")
    d = CX["1101_aparencia"]["dialogo"]
    s.append(regra(3, "Regra 3 · nome, cor e ícone", "Do seu jeito.",
                   "Toque nos três pontos da categoria: Renomear muda o nome; Aparência, a cor e o ícone.",
                   f"<div class='visual' style='margin-top:30px'>{recorte(ap, px(d[1]), px(d[1] + d[3]), largura=540)}{NOTA_TELA}</div>", 4, T))

    rec = tela(P11, "celular-categorias-receitas-11-01.png")
    r = CX["1101_receitas"]
    s.append(regra(4, "Regra 4 · receitas", "Receitas também.",
                   "Salário, Investimentos, Empréstimos e Outras receitas: o que entra também conta a história.",
                   f"<div class='visual' style='margin-top:30px'>{recorte(rec, px(r['Receitas'][1] - 14), px(r['Salário'][1] + 42), largura=560)}{NOTA_TELA}</div>", 5, T))

    exc = tela(P11, "celular-categorias-excluir-roupas-11-01.png")
    e = CX["1101_excluir"]["modal"]
    s.append(regra(5, "Regra 5 · excluir", "Antes de excluir, mova.",
                   "O site pede um destino para os lançamentos. Aqui, Roupas vai para Compras.",
                   f"<div class='visual' style='margin-top:30px'>{recorte(exc, px(e[1] + 6), px(e[1] + e[3]), largura=560)}{NOTA_TELA}</div>", 6, T))

    s.append(fechamento_verde("Categorias que falam a língua da sua casa.",
                              "Configurar › Categorias no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_ja(h) for h in s]


# ============================================================================ 08/01 · Hábito: 66 dias
HOJE_08 = date(2027, 1, 8)
DIA_66 = HOJE_08 + timedelta(days=66)
assert DIA_66 == date(2027, 3, 15) and SEM[HOJE_08.weekday()] == "sex" and SEM[DIA_66.weekday()] == "seg"
# Visão geral do celular em 08/01/2027 (conta de base, captura.py): Receitas R$ 9.960,00; Despesas R$ 896,00 (Padaria 38,50 +
# Mercado 402,30 + Combustível 392,00 + Farmácia 63,20); "Resultado do período" R$ 9.064,00; "Guardou 91% da receita".
DESP_0801 = D("38.50") + D("402.30") + D("392.00") + D("63.20")
assert DESP_0801 == D("896.00") and D("9960.00") - DESP_0801 == D("9064.00")
assert round((D("9064.00") / D("9960.00")) * 100) == 91
I_MAIS = '<path d="M12 5v14M5 12h14"/>'
I_OLHO_MES = '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M8 14.5h3M8 17h6"/>'
I_SINO = '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>'


def grade_dias(n=66, colunas=11, faltas=(), tam=50, gap=14, cor=BRAND, vazio=FIO, borda_falta=CORAL):
    """Uma bolinha por dia: cheia nos dias feitos, só o contorno nos dias que faltaram."""
    bolas = []
    for i in range(n):
        if i in faltas:
            est = f"background:#fff;box-shadow:inset 0 0 0 4px {borda_falta}"
        else:
            est = f"background:{cor}"
        bolas.append(f"<i style='display:block;width:{tam}px;height:{tam}px;border-radius:50%;{est}'></i>")
    return f"<div style='display:grid;grid-template-columns:repeat({colunas},{tam}px);gap:{gap}px;justify-content:center'>{''.join(bolas)}</div>"


def mes_cal(ano, mes, marcas, cel=96, bola=78, fs=34):
    """Mês que começa no domingo (como o calendário do perfil). marcas: {dia: 'menta' | 'verde' | 'anel'}."""
    off = (date(ano, mes, 1).weekday() + 1) % 7
    ndias = calendar.monthrange(ano, mes)[1]
    cels = [f"<div style='height:{int(fs * 1.45)}px;display:flex;align-items:center;justify-content:center;font-size:{int(fs * .74)}px;"
            f"font-weight:700;color:{MUTED};letter-spacing:.04em'>{s}</div>" for s in ["D", "S", "T", "Q", "Q", "S", "S"]]
    cels += [f"<div style='height:{cel}px'></div>" for _ in range(off)]
    for d in range(1, ndias + 1):
        m = marcas.get(d)
        if m == "verde":
            est, peso = f"background:{BRAND};color:#fff;box-shadow:0 0 0 {bola // 10}px {SOFT}", 700
        elif m == "anel":
            est, peso = f"background:#fff;color:{BRAND_DARK};box-shadow:inset 0 0 0 5px {BRAND}", 700
        else:
            est, peso = f"color:{INK}", 500
        cels.append(f"<div style='display:flex;align-items:center;justify-content:center;height:{cel}px'><span class='tab' style='width:{bola}px;height:{bola}px;"
                    f"border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:{fs}px;font-weight:{peso};{est}'>{d}</span></div>")
    return f"<div style='display:grid;grid-template-columns:repeat(7,1fr);row-gap:2px'>{''.join(cels)}</div>"


def capa_habito(T, sub):
    """O 66 enorme em menta sobre a tinta, com uma fileira de 66 tracinhos (um por dia) embaixo."""
    tracos = "".join(f"<i style='display:block;width:7px;height:{30 if (i + 1) % 11 else 46}px;border-radius:4px;"
                     f"background:{MENTA if i < 65 else '#fff'}'></i>" for i in range(66))
    vis = f"""<div class='visual' style='margin-top:6px'>
  <div style='display:flex;align-items:flex-end;gap:26px'>
    <div class='tab' style='font-size:470px;line-height:.78;font-weight:700;letter-spacing:-.065em;color:{MENTA};margin-left:-14px'>66</div>
    <div style='font-size:118px;line-height:1;font-weight:700;letter-spacing:-.045em;color:#fff;padding-bottom:6px'>dias.</div>
  </div>
  <div style='font-size:46px;line-height:1.18;font-weight:600;letter-spacing:-.025em;color:#fff;margin-top:44px'>{sub}</div>
  <div style='display:flex;align-items:flex-end;justify-content:space-between;margin-top:56px;height:46px'>{tracos}</div>
</div>"""
    corpo = f"<div class='eyebrow'>Hábito</div>{vis}"
    return capa("tinta", EXTRA_J + corpo, 1, T)


# ============================================================================ 06/01 · Material escolar
def folha_lista(itens, titulo="Lista de material", larg=880, linha=74):
    """Folha pautada com a lista: itens de uso coletivo riscados em coral, os de uso individual com visto verde."""
    furos = "".join(f"<i style='position:absolute;left:30px;top:{y}px;width:26px;height:26px;border-radius:50%;background:{BG};"
                    f"box-shadow:inset 0 2px 3px rgba(15,20,16,.10)'></i>" for y in (76, 76 + 3 * linha, 76 + 6 * linha))
    linhas = []
    for txt, riscado in itens:
        if riscado:
            marca = svg_icone(I_X, 34, CORAL, 3)
            texto = (f"<span style='position:relative;color:{MUTED}'>{txt}"
                     f"<i style='position:absolute;left:-6px;right:-6px;top:52%;height:5px;border-radius:3px;background:{CORAL};display:block'></i></span>")
        else:
            marca = svg_icone(I_CHECK, 34, BRAND_DARK, 3)
            texto = f"<span style='color:{INK}'>{txt}</span>"
        linhas.append(f"<div style='display:flex;align-items:center;gap:22px;height:{linha}px;border-bottom:2px solid #DCE9E2;"
                      f"font-size:38px;font-weight:600;letter-spacing:-.02em'>{marca}{texto}</div>")
    return f"""<div style='position:relative;width:{larg}px;background:#fff;border-radius:22px;box-shadow:0 1px 2px rgba(15,20,16,.05),0 26px 50px -24px rgba(15,20,16,.30);
  padding:26px 40px 30px 118px;transform:rotate(-1.6deg);border:1px solid {FIO}'>
  {furos}<i style='position:absolute;left:96px;top:0;bottom:0;width:3px;background:#F1C7B6;display:block'></i>
  <div style='height:{linha}px;display:flex;align-items:center;border-bottom:2px solid #DCE9E2;font-size:26px;font-weight:700;letter-spacing:.16em;
    text-transform:uppercase;color:{BRAND_DARK}'>{titulo}</div>
  {''.join(linhas)}</div>"""


# FATOS.md, seção 4 (Lally, van Jaarsveld, Potts e Wardle, 2010, EJSP 40(6):998-1009, DOI 10.1002/ejsp.674):
# 96 voluntários, um comportamento por dia, no mesmo contexto, por 12 semanas; de 18 a 254 dias até 95% da automaticidade
# (254 é projeção: o acompanhamento durou 84 dias); mediana de 66 dias (Keller e colegas, 2021, com a própria Lally).
# Fora do FATOS, conferido no resumo do registro oficial do DOI (api.crossref.org/works/10.1002/ejsp.674) em 20/10/2026:
# "Missing one opportunity to perform the behaviour did not materially affect the habit formation process."
LALLY = {"voluntarios": 96, "semanas": 12, "min": 18, "mediana": 66, "max": 254}
assert LALLY["semanas"] * 7 == 84 < LALLY["max"]


def v_faixa_estudo():
    L = 816                                    # largura útil do eixo, dentro do cartão
    x = lambda d: d / 270 * L
    mn, md, mx, fim = LALLY["min"], LALLY["mediana"], LALLY["max"], LALLY["semanas"] * 7
    listra = f"repeating-linear-gradient(135deg,{MENTA_CLARA} 0 10px,{SOFT} 10px 20px)"
    BT, BH = 118, 50                           # topo e altura da barra
    rot = "position:absolute;transform:translateX(-50%);white-space:nowrap;text-align:center"
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:36px 40px 28px'>
  <div style='position:relative;width:{L}px;height:262px'>
    <div style='{rot};left:{x(md):.0f}px;top:0'><div class='tab' style='font-size:58px;font-weight:700;letter-spacing:-.04em;line-height:1;color:{INK}'>66 dias</div>
      <div style='font-size:22px;font-weight:700;letter-spacing:.14em;color:{BRAND_DARK};margin-top:6px'>A MEDIANA</div></div>
    <div style='position:absolute;left:{x(mn):.0f}px;width:{x(fim) - x(mn):.0f}px;top:{BT}px;height:{BH}px;border-radius:{BH // 2}px 0 0 {BH // 2}px;background:{BRAND}'></div>
    <div style='position:absolute;left:{x(fim):.0f}px;width:{x(mx) - x(fim):.0f}px;top:{BT}px;height:{BH}px;border-radius:0 {BH // 2}px {BH // 2}px 0;background:{listra}'></div>
    <div style='position:absolute;left:{x(fim) - 1.5:.0f}px;top:{BT - 10}px;height:{BH + 20}px;border-left:3px dashed {INK}'></div>
    <div style='position:absolute;left:{x(md) - 19:.0f}px;top:{BT + BH / 2 - 19:.0f}px;width:38px;height:38px;border-radius:50%;background:{INK};box-shadow:0 0 0 6px #fff'></div>
    <div class='tab' style='position:absolute;left:{x(mn):.0f}px;top:{BT + BH + 18}px;font-size:28px;font-weight:700;color:{INK}'>18 dias</div>
    <div class='tab' style='position:absolute;right:{L - x(mx):.0f}px;top:{BT + BH + 18}px;font-size:28px;font-weight:700;color:{INK}'>254 dias</div>
  </div>
  <div style='display:flex;gap:30px;padding-top:20px;border-top:2px solid {FIO};font-size:24px;font-weight:600;color:{MUTED}'>
    <span style='display:flex;align-items:center;gap:10px'><i style='width:24px;height:24px;border-radius:6px;background:{BRAND};display:block'></i>dentro das 12 semanas (84 dias)</span>
    <span style='display:flex;align-items:center;gap:10px'><i style='width:24px;height:24px;border-radius:6px;background:{listra};display:block'></i>estimado pelo modelo</span></div>
</div>
<div class='nota'>Dias até chegar a 95% do próprio teto de automatismo, entre os 39 cujos dados o modelo descreveu bem. O estudo durou 84 dias: o teto de 254 é uma estimativa do modelo. Lally e colegas, 2010.</div></div>"""


def v_rotina():
    def linha(ip, t, s):
        return f"""<div class='linha-item'>{azulejo(ip, 96, 48)}<div><div style='font-size:38px;font-weight:700;letter-spacing:-.03em'>{t}</div>
  <div style='font-size:28px;color:{MUTED};margin-top:6px;line-height:1.3'>{s}</div></div></div>"""
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:10px 44px'>
  {linha(I_MAIS, 'Lance o que gastou', 'O “+” abre a Nova transação.')}
  {linha(I_OLHO_MES, 'Olhe o mês', 'O Resultado do período fica na Visão geral.')}
  {linha(I_SINO, 'Confira o que vence', 'Pendentes mostra o que vence nos próximos dias.')}
</div></div>"""


def post_habito():
    T = 7
    s = [capa_habito(T, "a mediana para um hábito virar automático.")]

    s.append(slide("light", EXTRA_J + topo(
        "O estudo · Lally e colegas, 2010", "96 pessoas, um hábito novo cada.",
        "Comer, beber ou se exercitar: todo dia, no mesmo contexto, por 12 semanas.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px") + v_faixa_estudo(), 2, T))

    faltas = (17, 40)
    grade = grade_dias(66, 11, faltas, tam=56, gap=16)
    s.append(slide("light", EXTRA_J + topo(
        "O que o estudo viu", "Falhar um dia não zera.", cls="h2") + f"""
<div class='visual' style='margin-top:40px'><div class='card' style='padding:40px 40px 32px'>{grade}
  <div style='display:flex;gap:30px;justify-content:center;margin-top:26px;font-size:23px;font-weight:600;color:{MUTED}'>
    <span style='display:flex;align-items:center;gap:10px'><i style='width:24px;height:24px;border-radius:50%;background:{BRAND};display:block'></i>dia feito</span>
    <span style='display:flex;align-items:center;gap:10px'><i style='width:24px;height:24px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 4px {CORAL};display:block'></i>dia perdido</span></div></div>
  <div style='margin-top:30px;font-size:33px;line-height:1.35;color:{INK};font-weight:500'>“Perder uma oportunidade de repetir o comportamento não afetou de forma relevante a formação do hábito.”</div>
  <div class='nota' style='margin-top:14px'>Lally e colegas, 2010, resumo do artigo (tradução nossa).</div></div>""", 3, T))

    s.append(slide("light", EXTRA_J + topo(
        "Para o seu dinheiro", "Uma rotina de 2 minutos.",
        "Num momento fixo do dia, como no estudo: o mesmo contexto todo dia.", estilo_p="font-size:34px;margin-top:22px") + v_rotina(), 4, T))

    vis = tela(P08, "celular-visao-geral-08-01.png")
    cv = CX["0801_visao"]
    y0 = cv["Movimento de janeiro"][1] - 18
    y1 = 830                                   # o pé da janela (390 × 830): o "+" e a linha "Fev/26 a Jan/27" inteiros
    assert cv["fab_visivel"][1] + cv["fab_visivel"][3] < y1
    s.append(slide("light", EXTRA_J + topo(
        "No timtimcash · 08/01", "Tudo na primeira tela.",
        "O “+” lança um gasto. O Resultado do período mostra como o mês vai.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:30px'>{recorte(vis, px(y0), px(y1), largura=540)}{NOTA_TELA}</div>", 5, T))

    cal = f"""<div class='visual' style='margin-top:36px'><div class='card' style='padding:30px 40px 26px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding-bottom:12px;border-bottom:2px solid {FIO}'>
    <span class='rs' style='color:{BRAND_DARK}'>Março de 2027</span><span class='rs'>daqui a 66 dias</span></div>
  <div style='margin-top:12px'>{mes_cal(2027, 3, {15: 'verde'}, cel=86, bola=70, fs=32)}</div>
</div>
<div class='nota'>66 dias depois de sexta, 08/01/2027: segunda, 15/03/2027.</div></div>"""
    s.append(slide("light", EXTRA_J + topo(
        "Se você começar hoje", "Daqui a 66 dias: 15 de março.",
        "No estudo, 66 foi a mediana: para uns, antes; para outros, depois.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px") + cal, 6, T))

    s.append(fechamento_verde("Comece hoje. Faltar um dia faz parte.",
                              "Visão geral no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_ja(h) for h in s]


# ---------------------------------------------------------------------------- 06/01 · conteúdo
# FATOS.md, seção 1: Lei 12.886/2013 (Lei 9.870/1999, art. 1º, § 7º); Procon-SP, folheto "Material Escolar" (fev/2026) e
# pesquisa de preços de 02/01/2026 (caneta esferográfica de R$ 1,30 a R$ 4,90, 276,92%); Procon Paulistano (jan/2026).
CANETA = (D("1.30"), D("4.90"))
assert ((CANETA[1] / CANETA[0] - 1) * 100).quantize(D("0.01")) == D("276.92")
ITENS_CAPA = [("Caderno", False), ("Papel higiênico", True), ("Lápis e borracha", False), ("Copos descartáveis", True),
              ("Tesoura sem ponta", False), ("Produtos de limpeza", True), ("Material de escritório", True)]
# conta: material escolar R$ 940 em 12/01 (lançado em dezembro, pendente) e o uniforme R$ 286 em 18/01, lançado pela
# "Nova transação" em 06/01 como pendente, na cópia da conta (captura.py); a busca "escolar" soma R$ 1.226,00
assert D("940.00") + D("286.00") == D("1226.00")
I_LOJA = '<path d="M4 9.5 5.5 4.5h13L20 9.5"/><path d="M4 9.5h16v2a2.7 2.7 0 0 1-5.3 0 2.7 2.7 0 0 1-5.4 0 2.7 2.7 0 0 1-5.3 0z"/><path d="M5.5 13v7h13v-7M10 20v-4.5h4V20"/>'
I_CAMISA = '<path d="M8.5 4 4 6.5l1.8 4 1.7-.8V20h9V9.7l1.7.8 1.8-4L15.5 4a3.5 3.5 0 0 1-7 0z"/>'
I_REUSAR = '<path d="M7 7h9.5a3.5 3.5 0 0 1 0 7H6"/><path d="M9.5 10.5 6 14l3.5 3.5"/><path d="M14 4l3 3-3 3"/>'
I_GRUPO = '<circle cx="9" cy="8.5" r="3"/><circle cx="16.5" cy="9.5" r="2.4"/><path d="M3.5 19.5c.6-3.1 2.8-5 5.5-5s4.9 1.9 5.5 5"/><path d="M14.8 14.6c2.6-.4 4.8 1.2 5.7 4.4"/>'


def capa_material(T):
    corpo = f"""<div class='eyebrow'>Volta às aulas</div>
<div class='h1' style='font-size:92px'>Material escolar: o que a escola não pode pedir.</div>
<div class='visual' style='margin-top:52px;display:flex;justify-content:center'>{folha_lista(ITENS_CAPA, larg=820, linha=64)}</div>"""
    return capa("papel", EXTRA_J + corpo, 1, T)


def v_lei():
    aspas = f"<div style='font-size:150px;line-height:.6;font-weight:700;color:{BRAND};height:62px'>“</div>"
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:44px 50px 38px'>
  {aspas}
  <div style='font-size:37px;line-height:1.36;font-weight:500;letter-spacing:-.02em;color:{INK};margin-top:6px'>Será nula cláusula contratual que obrigue o contratante ao pagamento adicional ou ao fornecimento de qualquer material escolar de <b style='color:{BRAND_DARK}'>uso coletivo</b> […]</div>
  <div style='font-size:31px;line-height:1.4;color:{MUTED};margin-top:24px'>[…] devendo os custos correspondentes ser sempre considerados nos cálculos do valor das anuidades ou das semestralidades escolares.</div>
  <div style='margin-top:30px;padding-top:22px;border-top:2px solid {FIO};font-size:24px;font-weight:600;color:{MUTED}'>Lei 9.870/1999, art. 1º, § 7º, incluído pela Lei 12.886/2013</div>
</div></div>"""


def v_pode_nao_pode():
    def item(ip, cor, t):
        return (f"<div style='display:flex;gap:14px;align-items:center;padding:12px 0'><span style='flex:none;display:flex'>{svg_icone(ip, 34, cor, 3)}</span>"
                f"<span style='font-size:31px;line-height:1.2;font-weight:600;color:{INK}'>{t}</span></div>")
    nao = ["Papel higiênico", "Copos descartáveis", "Produtos de limpeza", "Material de escritório"]
    chip = lambda t, cor, fundo: f"<span style='display:inline-block;padding:8px 18px;border-radius:999px;background:{fundo};color:{cor};font-size:24px;font-weight:700;letter-spacing:.12em'>{t}</span>"
    return f"""<div class='visual' style='margin-top:36px'>
  <div class='card' style='padding:28px 36px 22px'>{chip('NÃO PODE', CORAL_TXT, '#FBE7DE')}
    <div style='display:grid;grid-template-columns:1fr 1fr;column-gap:24px;margin-top:10px'>{''.join(item(I_X, CORAL, t) for t in nao)}</div>
    <div style='border-top:2px solid {FIO};margin-top:8px'>{item(I_X, CORAL, 'Taxa para cobrir água, luz e telefone')}</div></div>
  <div class='card' style='padding:24px 36px 20px;margin-top:20px'>{chip('PODE', BRAND_DEEP, SOFT)}
    <div style='margin-top:8px'>{item(I_CHECK, BRAND_DARK, 'O material pedagógico de uso individual do aluno')}</div></div>
<div class='nota'>Não pode: Procon-SP, folheto Material Escolar (fev/2026). Pode: Procon Paulistano, cartilha Volta às aulas (jan/2026). A lei proíbe exigir o material de uso coletivo.</div></div>"""


def v_ao_comprar():
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:10px 44px'>
  <div class='linha-item'>{azulejo(I_LOJA, 96, 48)}<div><div style='font-size:36px;font-weight:700;letter-spacing:-.03em'>A loja</div>
    <div style='font-size:28px;color:{MUTED};margin-top:6px;line-height:1.3'>A escola não pode determinar a loja ou o site de compra.</div></div></div>
  <div class='linha-item'>{azulejo(I_ETIQUETA, 96, 48)}<div><div style='font-size:36px;font-weight:700;letter-spacing:-.03em'>A marca</div>
    <div style='font-size:28px;color:{MUTED};margin-top:6px;line-height:1.3'>Nem exigir marca. Nos dois casos, a exceção são as apostilas do sistema de ensino.</div></div></div>
  <div class='linha-item'>{azulejo(I_CAMISA, 96, 48)}<div><div style='font-size:36px;font-weight:700;letter-spacing:-.03em'>O uniforme</div>
    <div style='font-size:28px;color:{MUTED};margin-top:6px;line-height:1.3'>Em regra, não pode obrigar a comprar numa loja só. Pelo Procon-SP, a exceção é o uniforme de marca registrada.</div></div></div>
</div>
<div class='nota'>Procon-SP, folheto Material Escolar (fev/2026); Procon Paulistano, cartilha Volta às aulas (jan/2026).</div></div>"""


def v_dicas():
    caneta = f"""<div style='display:flex;align-items:baseline;gap:18px;margin-top:14px'>
      <span class='tab' style='font-size:54px;font-weight:700;letter-spacing:-.03em;color:{BRAND_DARK}'>{brl(float(CANETA[0]))}</span>
      <span style='font-size:28px;color:{MUTED};font-weight:600'>ou</span>
      <span class='tab' style='font-size:54px;font-weight:700;letter-spacing:-.03em;color:{CORAL_FORTE}'>{brl(float(CANETA[1]))}</span></div>
      <div style='font-size:26px;color:{MUTED};margin-top:4px'>a mesma caneta esferográfica, em lugares diferentes</div>"""
    return f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:14px 46px'>
  <style>.linha-item{{padding:32px 0}}</style>
  <div class='linha-item'>{azulejo(I_REUSAR, 108, 54)}<div><div style='font-size:40px;font-weight:700;letter-spacing:-.03em'>Reaproveite</div>
    <div style='font-size:30px;color:{MUTED};margin-top:8px;line-height:1.3'>Antes da lista, veja o que sobrou do ano passado.</div></div></div>
  <div class='linha-item' style='align-items:flex-start'>{azulejo(I_BUSCA, 108, 54)}<div><div style='font-size:40px;font-weight:700;letter-spacing:-.03em'>Compare item por item</div>
    <div style='font-size:30px;color:{MUTED};margin-top:8px;line-height:1.3'>Na pesquisa divulgada pelo Procon-SP em janeiro de 2026:</div>{caneta}</div></div>
  <div class='linha-item'>{azulejo(I_GRUPO, 108, 54)}<div><div style='font-size:40px;font-weight:700;letter-spacing:-.03em'>Combine com outras famílias</div>
    <div style='font-size:30px;color:{MUTED};margin-top:8px;line-height:1.3'>Dá para pesquisar preço e comprar junto.</div></div></div>
</div></div>"""


def post_material():
    T = 7
    s = [capa_material(T)]
    s.append(slide("light", EXTRA_J + topo("A lei", "Uso coletivo não entra na lista.", cls="h2") + v_lei(), 2, T))
    s.append(slide("light", EXTRA_J + topo("Na prática", "O que fica fora da lista.", cls="h2") + v_pode_nao_pode(), 3, T))
    s.append(slide("light", EXTRA_J + topo("Ao comprar", "A loja e a marca são escolha sua.", cls="h3") + v_ao_comprar(), 4, T))
    s.append(slide("light", EXTRA_J + topo("Para gastar menos", "Três jeitos de gastar menos.", cls="h3") + v_dicas(), 5, T))

    bus = tela(P06, "celular-transacoes-busca-escolar-06-01.png")
    cb = CX["0601_busca"]
    assert cb["rolagem"] == 0
    topo_card = cb["busca"][1] - 110          # cabeça do cartão "Transações" (título, filtrado e o resumo)
    fim_busca = cb["busca"][1] + cb["busca"][3] + 12
    ini_linhas = cb["seg · 18 de janeiro"][1] - 4
    fim_linhas = cb["Material escolar"][1] + 48
    corte = f"<div style='display:flex;align-items:center;gap:14px;margin:10px auto;width:560px;color:{NEUTRO};font-size:26px;font-weight:700'><i style='flex:1;border-top:3px dashed {NEUTRO}'></i>⋯<i style='flex:1;border-top:3px dashed {NEUTRO}'></i></div>"
    crop = (recorte(bus, px(topo_card), px(fim_busca), largura=560, x0=px(14), x1=px(376))
            + corte + recorte(bus, px(ini_linhas), px(fim_linhas), largura=560, x0=px(14), x1=px(376)))
    s.append(slide("light", EXTRA_J + topo(
        "No timtimcash · 06/01", "Lance antes, com a data.",
        "Material (R$ 940, dia 12) e uniforme (R$ 286, dia 18), em Educação: pendentes até o dia de pagar.",
        cls="h3", estilo_p="font-size:32px;margin-top:18px")
        + f"<div class='visual' style='margin-top:26px'>{crop}{NOTA_TELA}</div>", 6, T))

    s.append(fechamento_verde("Volta às aulas sem susto.",
                              "Transações e Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_ja(h) for h in s]


POSTS = {P02: post_comece, P06: post_material, P08: post_habito, P11: post_categorias, P14: post_limites}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    renderizar(POSTS, so=so)
