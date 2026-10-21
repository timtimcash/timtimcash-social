# -*- coding: utf-8 -*-
"""Carrosséis da equipe fb · fevereiro de 2027 (17, 19, 22, 24 e 26/02), no formato aprovado de outubro a dezembro
(J/kit/carrossel.py; modelos em novdez/equipes/dc1/posts.py e dc2/posts.py).

Telas reais (build 2026-10-19.5) capturadas por captura.py e guardadas em J/saida/<pasta>/telas/; as caixas (px CSS da
janela, escala 3) ficam em caixas.json. Os números da conta são refeitos aqui a partir de J/base_app/estado.py (e da
variante de 24/02, variantes.py) e conferidos por assert contra o texto das telas. Os fatos vêm de J/FATOS.md e
J/FATOS_2.md (e de fonte oficial, quando faltou; ver os dados de cada post).

python3 posts.py                       renderiza os posts e confere o layout
python3 posts.py <pasta> [<pasta>...]  só os escolhidos
"""
import os, re, sys, json, importlib.util
from decimal import Decimal as D, ROUND_HALF_UP

J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, J + "/kit")
from carrossel import *   # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl, sem_quebra...)

CX = json.load(open(os.path.join(AQUI, "caixas.json"), encoding="utf-8"))

P17 = "2027-02-17_realizado-previsto-e-ambos"     # trocado com 19/02 na revisão de 20/10/2026 (capa verde suave)
P19 = "2027-02-19_la-fora-na-declaracao"          # trocado com 17/02 na revisão de 20/10/2026 (capa papel)
P22 = "2027-02-22_informe-de-rendimentos-o-que-conferir"
P24 = "2027-02-24_dividas-qual-pagar-primeiro"
P26 = "2027-02-26_fevereiro-fechou-5-perguntas"

NBSP = " "
MENOS = "−"


def _modulo(pasta, nome):
    sys.modules.pop("estado", None)
    spec = importlib.util.spec_from_file_location(f"{nome}_{abs(hash(pasta))}", os.path.join(pasta, nome + ".py"))
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, pasta); spec.loader.exec_module(m); sys.path.remove(pasta)
    return m


ESTADO = _modulo(J + "/base_app", "estado")
VAR = _modulo(os.path.join(AQUI, "ap" "p"), "variantes")


def q2(v):
    return D(v).quantize(D("0.01"), ROUND_HALF_UP)


def px(v):
    """px CSS das capturas (escala 3) para px da imagem."""
    return int(round(v * 3))


def tela(pasta, nome):
    caminho = os.path.join(SAIDA, pasta, "telas", nome)
    assert os.path.isfile(caminho), caminho
    return caminho


def reais(v, cent=True):
    return brl(float(v), cent)


def no_texto(chave, *trechos):
    """Confere que cada trecho aparece no texto da tela guardado em caixas.json (sem quebras de linha)."""
    t = re.sub(r"[ \t\u00a0]+", " ", CX[chave]["texto"]).replace("\n", " | ")
    for tr in trechos:
        assert tr in t, (chave, tr)


def sem_quebra_fb(html):
    """sem_quebra do kit; e mais: número junto da lei, do artigo e do parágrafo; "% ao mês" sem quebra."""
    html = sem_quebra(html)
    html = re.sub(r"\b(Lei|Leis|Decreto|art\.|arts\.|nº|IN RFB|IN|§|Res\. CMN) (\d)", lambda m: m.group(1) + NBSP + m.group(2), html)
    html = html.replace("% ao mês", "%" + NBSP + "ao" + NBSP + "mês").replace("% ao ano", "%" + NBSP + "ao" + NBSP + "ano")
    html = re.sub(r"(\d)º mês", "\\1º" + NBSP + "mês", html)
    return html


EXTRA_F = EXTRA + f"""<style>
.tab{{font-variant-numeric:tabular-nums}}
.rs{{font-size:22px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTED}}}
.pilula{{display:inline-flex;align-items:center;gap:12px;background:{SOFT};color:{BRAND_DEEP};font-size:27px;font-weight:700;padding:14px 26px;border-radius:999px}}
.nota{{text-wrap:balance}}
.dupla{{display:flex;flex-direction:column;align-items:center;gap:14px}}
</style>"""


def topo(sobre, titulo, apoio=None, cls="h2", estilo_t="", estilo_p=""):
    p = f"<div class='p' style='{estilo_p}'>{apoio}</div>" if apoio else ""
    return f"<div class='eyebrow'>{sobre}</div><div class='{cls}' style='{estilo_t}'>{titulo}</div>{p}"


def pilula(ip, txt):
    return f"<span class='pilula'>{svg_icone(ip, 30, BRAND_DEEP, 2.2)}{txt}</span>"


def aviso(txt, ip=None, cor_fundo="#FBF1DC", cor_txt=AMBER_TEXT, cor_icone=AMBER_TEXT):
    """Caixa de aviso (âmbar por padrão), uma ou duas linhas."""
    ic = svg_icone(ip or I_ALERT, 34, cor_icone, 2.2)
    return (f"<div style='display:flex;gap:18px;align-items:flex-start;margin-top:26px;padding:20px 26px;border-radius:22px;"
            f"background:{cor_fundo};font-size:27px;line-height:1.36;color:{cor_txt};font-weight:500'>"
            f"<span style='flex:none;margin-top:1px'>{ic}</span><span>{txt}</span></div>")


# ícones de traço próprios (24 × 24, pontas redondas)
I_SETA = '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>'
I_LISTA = '<path d="M9 6.5h11M9 12h11M9 17.5h11"/><circle cx="4.8" cy="6.5" r="1.2"/><circle cx="4.8" cy="12" r="1.2"/><circle cx="4.8" cy="17.5" r="1.2"/>'
I_BALANCA = '<path d="M12 4v16M7 20h10M5 7h14"/><path d="M5 7l-2.5 6a2.5 2.5 0 0 0 5 0zM19 7l-2.5 6a2.5 2.5 0 0 0 5 0z"/>'
I_LEI = '<path d="M6.5 3.5h8l3 3v14h-11z"/><path d="M14.5 3.5v3h3"/><path d="M9 11h6M9 14.5h6M9 18h3.5"/>'
I_TROFEU = '<path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 6H5a3 3 0 0 0 3 4M16 6h3a3 3 0 0 1-3 4M12 13v4M8.5 20.5h7M9.5 17h5"/>'
I_DESCE = '<path d="M12 4v15"/><path d="M6 13l6 6 6-6"/>'
I_META = '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1.2"/>'
I_MEIO = '<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor" stroke="none"/>'
I_RELOGIO = I_CLOCK


# ============================================================================ números da conta (estado.py)
def totais_mes(dia, mes="2027-02"):
    """Receitas e despesas de um mês na conta de base vista em `dia`: (pagas, pendentes)."""
    est, _ = ESTADO.gerar(dia)
    r = d = dp = D(0)
    for t in est["txs"]:
        if not t["data"].startswith(mes) or t["tipo"] not in ("receita", "despesa"):
            continue
        v = D(str(t["valor"]))
        if t["tipo"] == "receita" and t["conciliado"]:
            r += v
        elif t["tipo"] == "despesa":
            if t["conciliado"]:
                d += v
            else:
                dp += v
    return r, d, dp, est


# ---- 17/02: o mês em três modos (o post era de 19/02 e foi para 17/02; telas refeitas com o relógio em 17/02)
DIA_M = 17
R_M, D_M, PEND_M, EST_M = totais_mes("2027-02-17")
assert (R_M, D_M, PEND_M) == (D("9960.00"), D("6904.40"), D("402.00"))
PEND_M_ITENS = sorted((t["data"], t["descricao"], D(str(t["valor"]))) for t in EST_M["txs"]
                      if t["data"].startswith("2027-02") and t["tipo"] == "despesa" and not t["conciliado"])
assert PEND_M_ITENS == [("2027-02-20", "Armazenamento na nuvem", D("42.00")), ("2027-02-27", "Notebook (4/10)", D("360.00"))]
RES_M_REAL = R_M - D_M
RES_M_PREV = R_M - D_M - PEND_M
assert (RES_M_REAL, RES_M_PREV) == (D("3055.60"), D("2653.60"))
GUARDOU_M = (RES_M_REAL / R_M * 100).quantize(D("0.1"), ROUND_HALF_UP)
DEVE_M = (RES_M_PREV / R_M * 100).quantize(D("0.1"), ROUND_HALF_UP)
assert (GUARDOU_M, DEVE_M) == (D("30.7"), D("26.6"))
assert int(D_M / (D_M + PEND_M) * 100) == 94                    # "94% já aconteceu" (a tela trunca 94,5%)
no_texto("1702_realizado", "Realizado", "Guardou 30,7% da receita", "Receitas R$ 9.960,00", "Despesas R$ 6.904,40",
         "Resultado do período", "R$ 3.055,60")
no_texto("1702_previsto", "PREVISTO", "Deve guardar 26,6% da receita", "Despesas R$ 7.306,40", "Resultado previsto", "R$ 2.653,60")
no_texto("1702_ambos", "Com os pendentes, R$ 115.037,36", "−R$ 402,00 pendentes", "Concluído", "100% já aconteceu",
         "Faltam R$ 402,00", "94% já aconteceu", "Deve fechar em R$ 2.653,60")
# "em março, aluguel e escola já aparecem" (slide 5): Previsto de março, visto em 17/02 (as Fixas já estão pendentes)
no_texto("1702_marco_previsto", "Março 2027", "PREVISTO", "Despesas R$ 4.444,80", "Casa | R$ 2.300,00", "Educação | R$ 1.450,00")

# ---- 26/02: o fim do mês
R26, D26, PEND26, EST26 = totais_mes("2027-02-26")
assert (R26, D26, PEND26) == (D("9960.00"), D("8823.10"), D("360.00"))
RES26_REAL, RES26_PREV = R26 - D26, R26 - D26 - PEND26
assert (RES26_REAL, RES26_PREV) == (D("1136.90"), D("776.90"))
GUARDOU26 = (RES26_REAL / R26 * 100).quantize(D("0.1"), ROUND_HALF_UP)
assert GUARDOU26 == D("11.4") and (RES26_PREV / R26 * 100).quantize(D("0.1"), ROUND_HALF_UP) == D("7.8")
no_texto("2602_ambos", "Com os pendentes, R$ 113.160,66", "Faltam R$ 360,00", "96% já aconteceu", "Deve fechar em R$ 776,90")
no_texto("2602_pendentes", "A pagar", "1 transação", "Nada vencido. Tudo dentro do prazo.", "AMANHÃ", "27/02/2027",
         "Notebook (4/10)", "−R$ 360,00")
no_texto("2602_relatorios", "Abaixo do seu padrão", "−6,9 pontos percentuais", "Você costuma guardar 18,3% da receita.",
         "O maior desvio veio de Mercado: +R$ 453,50 em relação à média.", "sua média (12m): 18,3% · meta: 20%", "11,4%",
         "Mercado | média R$ 1.646,10 · agora R$ 2.099,60 | +R$ 453,50 | +28%",
         "Saúde | média R$ 268,11 · agora R$ 129,90 | −R$ 138,21 | −52%")
MERC26 = sum(D(str(t["valor"])) for t in EST26["txs"] if t["data"].startswith("2027-02") and t.get("categoria") == "Mercado" and t["conciliado"])
assert MERC26 == D("2099.60") and MERC26 - D("1646.10") == D("453.50")
ORC26 = {}
for t in EST26["txs"]:
    if t["data"].startswith("2027-02") and t["tipo"] == "despesa" and t["conciliado"] and t.get("categoria") in EST26["budgets"]:
        ORC26[t["categoria"]] = ORC26.get(t["categoria"], D(0)) + D(str(t["valor"]))
LIM26 = {k: D(v) for k, v in EST26["budgets"].items()}
assert ORC26 == {"Mercado": D("2099.60"), "Transporte": D("1212.40"), "Bares e restaurantes": D("701.20"),
                 "Lazer e hobbies": D("353.90"), "Saúde": D("129.90")}, ORC26
assert ORC26["Bares e restaurantes"] - LIM26["Bares e restaurantes"] == D("101.20")      # a tela trunca: "Excedeu em R$ 101"
assert ORC26["Mercado"] - LIM26["Mercado"] == D("99.60")                                  # "Excedeu em R$ 99"
assert sorted(k for k in ORC26 if ORC26[k] <= LIM26[k]) == ["Lazer e hobbies", "Saúde", "Transporte"]   # "as outras 3 ficaram dentro"
assert (ORC26["Lazer e hobbies"] / LIM26["Lazer e hobbies"] * 100).quantize(D("1")) == D("88")
no_texto("2602_orcamentos", "Bares e restaurantes | R$ 701 de R$ 600 | 117% | Excedeu em R$ 101",
         "Mercado | R$ 2.099 de R$ 2.000 | 105% | Excedeu em R$ 99", "Lazer e hobbies | R$ 353 de R$ 400 | 88%",
         "Sobra do limite | R$ 953,00")
# o Carnaval (gastos pagos pela Carteira do Carnaval) também conta nas categorias
CARNAVAL_BARES = sum(D(str(t["valor"])) for t in EST26["txs"] if "Carnaval" in t["descricao"] and t.get("categoria") == "Bares e restaurantes")
assert CARNAVAL_BARES == D("112.50") and ORC26["Bares e restaurantes"] - CARNAVAL_BARES < LIM26["Bares e restaurantes"]


# ============================================================================ 17/02 · Realizado, Previsto e Ambos (era 19/02)
MODOS = [("real", "Realizado", BRAND), ("prev", "Previsto", AMBER_BAR), ("comp", "Ambos", MUTED)]


def chip_modo(nome, cor, tam=32, ativo=True):
    fundo = "#fff" if ativo else "transparent"
    sombra = "box-shadow:0 1px 2px rgba(15,20,16,.06),0 6px 16px -8px rgba(15,20,16,.25);" if ativo else ""
    return (f"<span style='display:inline-flex;align-items:center;gap:14px;height:{int(tam * 2)}px;padding:0 {int(tam * .95)}px;border-radius:999px;"
            f"background:{fundo};{sombra}font-size:{tam}px;font-weight:600;color:{INK};letter-spacing:-.01em;white-space:nowrap'>"
            f"<i style='display:block;width:{int(tam * .42)}px;height:{int(tam * .42)}px;border-radius:50%;background:{cor}'></i>{nome}</span>")


def regua_mes(modo, cel=26, gap=6, alt=46):
    """Fevereiro de 2027 em 28 quadradinhos: verde até hoje (17); no Previsto e no Ambos, os 2 pendentes (dias 20 e 27)
    em âmbar; no Ambos, o resto do mês com contorno tracejado ("falta")."""
    pend = {int(d[8:10]) for d, _, _ in PEND_M_ITENS}
    cels = []
    for d in range(1, 29):
        if d <= DIA_M:
            est = f"background:{BRAND}"
        elif modo != "real" and d in pend:
            est = f"background:{AMBER}"
        elif modo == "comp":
            est = f"background:#fff;box-shadow:inset 0 0 0 3px {AMBER}"
        else:
            est = f"background:{FIO}"
        cels.append(f"<i style='display:block;width:{cel}px;height:{alt}px;border-radius:7px;{est}'></i>")
    return f"<div style='display:flex;gap:{gap}px'>{''.join(cels)}</div>"


def capa_modos(T):
    cel, gap, alt = 26, 6, 50
    larg = 28 * cel + 27 * gap                      # 890 px: os 28 dias de fevereiro de 2027
    chip_h, g1, g2 = 68, 18, 30
    bloco = chip_h + g1 + alt
    topos = [i * (bloco + g2) + chip_h + g1 for i in range(3)]
    altura = 3 * bloco + 2 * g2
    x_hoje = DIA_M * (cel + gap) - gap / 2           # entre o dia 17 e o dia 18
    blocos = "".join(f"<div style='display:flex;flex-direction:column;align-items:flex-start;gap:{g1}px'>{chip_modo(nome, cor, 34)}{regua_mes(m, cel, gap, alt)}</div>"
                     for m, nome, cor in MODOS)
    marca = (f"<div style='position:absolute;left:{x_hoje - 2:.0f}px;top:{topos[0] - 16}px;height:{topos[2] + alt - topos[0] + 32}px;"
             f"width:4px;border-radius:2px;background:{INK}'></div>")
    rot = f"position:absolute;top:{altura + 26}px;font-size:25px;font-weight:600;color:{MUTED}"
    rotulos = (f"<div style='{rot};left:0'>1º/02</div><div style='{rot};right:0'>28/02</div>"
               f"<div style='{rot};left:{x_hoje - 100:.0f}px;width:200px;text-align:center;font-weight:700;color:{INK}'>hoje · {DIA_M:02d}/02</div>")
    vis = f"""<div class='visual' style='margin-top:60px;display:flex;justify-content:center'>
  <div style='position:relative;width:{larg}px;height:{altura + 62}px'>
    <div style='display:flex;flex-direction:column;gap:{g2}px'>{blocos}</div>{marca}{rotulos}
  </div></div>"""
    corpo = f"""<div class='eyebrow'>Visão geral</div>
<div class='h1' style='font-size:104px'>3 jeitos de ver o mesmo mês.</div>{vis}"""
    return capa("suave", EXTRA_F + corpo, 1, T)


def recorte_modo(arq, chave, y0, y1, largura=600):
    """O seletor de cálculo (Realizado | Previsto | Ambos) em cima, e embaixo um pedaço da mesma tela, na mesma escala."""
    sx, sy, sw, sh = CX[chave]["sel:seg"]
    esc = largura / (sw + 8)
    sel = recorte(arq, px(sy - 4), px(sy + sh + 4), largura=largura, x0=px(sx - 4), x1=px(sx + sw + 4), raio=36)
    w2 = (376 - 14) * esc
    corpo = recorte(arq, px(y0), px(y1), largura=round(w2), x0=px(14), x1=px(376), raio=26)
    return f"<div class='dupla'>{sel}{corpo}</div>"


def v_quando():
    linhas = [
        ("Realizado", BRAND, "Quanto já sobrou?", "Para conferir com o extrato do banco: é o dinheiro que já se mexeu."),
        ("Previsto", AMBER_BAR, "Quanto vai sobrar?", "Para planejar. Vale para o mês que vem: em março, aluguel e escola já aparecem."),
        ("Ambos", MUTED, "Quanto ainda falta?", "No meio do mês, para saber o que já foi e o que ainda vai sair."),
    ]
    itens = []
    for i, (nome, cor, perg, txt) in enumerate(linhas):
        borda = f"border-top:2px solid {FIO};" if i else ""
        itens.append(f"""<div style='padding:30px 0;{borda}'>
  <div style='display:flex;align-items:center;justify-content:space-between;gap:20px'>
    <span style='font-size:44px;font-weight:700;letter-spacing:-.035em;color:{INK}'>{perg}</span>{chip_modo(nome, cor, 26)}</div>
  <div style='font-size:29px;line-height:1.38;color:{MUTED};margin-top:12px'>{txt}</div></div>""")
    return f"<div class='visual' style='margin-top:40px'><div class='card' style='padding:6px 44px'>{''.join(itens)}</div></div>"


def post_modos():
    T = 6
    s = [capa_modos(T)]
    arq = tela(P17, "celular-visao-geral-realizado-17-02.png")
    s.append(slide("light", EXTRA_F + topo(
        "Realizado · o padrão", "Só o que já entrou e saiu.",
        f"É assim que o site abre. Em {DIA_M:02d}/02, o resultado de fevereiro era {reais(RES_M_REAL)}.",
        cls="h3", estilo_p="font-size:36px;margin-top:22px")
        + f"<div class='visual' style='margin-top:36px'>{recorte_modo(arq, '1702_realizado', 416, 627, 760)}{NOTA_TELA}</div>", 2, T))

    arq = tela(P17, "celular-visao-geral-previsto-17-02.png")
    s.append(slide("light", EXTRA_F + topo(
        "Previsto", "Inclui o que ainda vai vencer.",
        f"Entram as contas que já têm data no mês: a nuvem, no dia 20, e a parcela do notebook, no dia 27.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:30px'>{recorte_modo(arq, '1702_previsto', 416, 627, 680)}{NOTA_TELA}"
        + aviso("O Previsto soma o que está lançado. O gasto do dia a dia entra quando você lança.") + "</div>", 3, T))

    arq = tela(P17, "celular-visao-geral-ambos-17-02.png")
    s.append(slide("light", EXTRA_F + topo(
        "Ambos", "O que já foi e o que falta.",
        "Cada número mostra quanto já aconteceu, e o resultado diz onde o mês deve fechar.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:30px'>{recorte_modo(arq, '1702_ambos', 778, 1066, 660)}{NOTA_TELA}</div>", 4, T))

    s.append(slide("light", EXTRA_F + topo("Quando usar cada um", "Um modo para cada pergunta.", cls="h3") + v_quando(), 5, T))

    s.append(fechamento_verde("Realizado, Previsto ou Ambos: um toque.",
                              "Visão geral no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra_fb(h) for h in s]


# ============================================================================ 24/02 · Qual dívida pagar primeiro?
# Dívidas de exemplo (as mesmas da variante da conta, variantes.py da cópia): nome curto, saldo, taxa ao mês, parcelas
DIV = [(d.split(" · ")[0], s, i, n) for d, s, i, n, _ in VAR.DIVIDAS]
PARC = {nome: VAR.parcela(s, i, n) for nome, s, i, n in DIV}
assert [nome for nome, _, _, _ in DIV] == ["Crediário da loja", "Empréstimo pessoal", "Financiamento do carro"]
assert PARC == {"Crediário da loja": D("93.78"), "Empréstimo pessoal": D("377.71"), "Financiamento do carro": D("317.23")}
JUROS_1M = {nome: q2(s * i) for nome, s, i, n in DIV}
assert JUROS_1M == {"Crediário da loja": D("24.00"), "Empréstimo pessoal": D("210.00"), "Financiamento do carro": D("120.00")}
SALDO_TOTAL = sum(s for _, s, _, _ in DIV)
SO_PARCELAS = sum(PARC[n] * k for n, _, _, k in DIV)
JUROS_SO_PARCELAS = SO_PARCELAS - SALDO_TOTAL
assert (SALDO_TOTAL, SO_PARCELAS, JUROS_SO_PARCELAS) == (D("9800.00"), D("13083.84"), D("3283.84"))
EXTRA_MES = D("300")


def quitar(ordem, extra=EXTRA_MES):
    """Mês a mês: juros sobre o saldo, a parcela de cada dívida aberta e o resto do orçamento (parcelas + extra) na
    dívida da vez; quando uma acaba, a parcela dela segue para a próxima. Devolve (meses, juros pagos, mês em que
    cada uma acabou). Conta simplificada: sem IOF, tarifas, seguros nem atraso."""
    saldo = {n: s for n, s, _, _ in DIV}
    taxa = {n: i for n, _, i, _ in DIV}
    orc = sum(PARC.values()) + extra
    juros, mes, fim = D(0), 0, {}
    while any(v > 0 for v in saldo.values()):
        mes += 1
        caixa = orc
        for n in saldo:
            if saldo[n] > 0:
                j = q2(saldo[n] * taxa[n]); juros += j; saldo[n] += j
        for n in saldo:
            if saldo[n] > 0:
                p = min(PARC[n], saldo[n]); saldo[n] -= p; caixa -= p
        for n in ordem:
            if saldo[n] > 0 and caixa > 0:
                p = min(caixa, saldo[n]); saldo[n] -= p; caixa -= p
        for n in saldo:
            if saldo[n] <= 0 and n not in fim:
                fim[n] = mes
        assert mes < 400
    return mes, juros, fim


ORDEM_CARA = [n for n, _, i, _ in sorted(DIV, key=lambda d: -d[2])]
ORDEM_MENOR = [n for n, s, _, _ in sorted(DIV, key=lambda d: d[1])]
assert ORDEM_CARA == ["Empréstimo pessoal", "Crediário da loja", "Financiamento do carro"]
assert ORDEM_MENOR == ["Crediário da loja", "Empréstimo pessoal", "Financiamento do carro"]
MESES_CARA, JUROS_CARA, FIM_CARA = quitar(ORDEM_CARA)
MESES_MENOR, JUROS_MENOR, FIM_MENOR = quitar(ORDEM_MENOR)
assert (MESES_CARA, JUROS_CARA, FIM_CARA) == (11, D("1764.35"), {"Empréstimo pessoal": 6, "Crediário da loja": 7, "Financiamento do carro": 11})
assert (MESES_MENOR, JUROS_MENOR, FIM_MENOR) == (11, D("1893.32"), {"Crediário da loja": 3, "Empréstimo pessoal": 7, "Financiamento do carro": 11})
DIF_JUROS = JUROS_MENOR - JUROS_CARA
assert DIF_JUROS == D("128.97")
FIM_SO = {n: k for n, _, _, k in DIV}                 # só com as parcelas: cada uma no seu prazo
assert max(FIM_SO.values()) == 24


def r0(v):
    """R$ sem centavos, arredondado (para o exemplo)."""
    return brl(float(D(v).quantize(D("1"), ROUND_HALF_UP)), False)


assert (r0(JUROS_CARA), r0(JUROS_MENOR), r0(DIF_JUROS), r0(JUROS_SO_PARCELAS)) == ("R$ 1.764", "R$ 1.893", "R$ 129", "R$ 3.284")
# tela de 24/02 numa conta separada (variantes.py, so_dividas): só a Conta corrente e as 3 dívidas, nada da conta principal
no_texto("2402_pendentes", "A pagar | R$ | 788 | ,72 | 3 transações", "Nada vencido. Tudo dentro do prazo.", "3 transações ainda no prazo",
         "Crediário da loja · 3% ao mês (1/10)", "−R$ 93,78", "Empréstimo pessoal · 7% ao mês (1/12)", "−R$ 377,71",
         "Financiamento do carro · 2% ao mês (1/24)", "−R$ 317,23")
assert "Notebook" not in CX["2402_pendentes"]["texto"]
assert sum(PARC.values()) == D("788.72")

COR_DIV = {"Crediário da loja": INK, "Empréstimo pessoal": CORAL, "Financiamento do carro": INK}


def capa_dividas(T):
    """Três colunas de dívida na altura do saldo, cada uma com a etiqueta dos juros; a mais cara em coral."""
    H = 430
    maior = max(s for _, s, _, _ in DIV)
    cols = []
    for nome, s, i, n in DIV:
        h = float(s / maior) * H
        cara = nome == ORDEM_CARA[0]
        cor = CORAL if cara else INK
        tag = (f"<span style='display:inline-flex;align-items:center;height:70px;padding:0 26px;border-radius:999px;"
               f"background:{CORAL if cara else '#fff'};box-shadow:{'none' if cara else 'inset 0 0 0 4px ' + NEUTRO};"
               f"font-size:34px;font-weight:700;letter-spacing:-.02em;color:{'#fff' if cara else INK};white-space:nowrap'>{num(float(i * 100), 0)}% ao mês</span>")
        cols.append(f"""<div style='width:236px;display:flex;flex-direction:column;align-items:center'>
  {tag}
  <div style='width:100%;height:{h:.0f}px;border-radius:22px 22px 8px 8px;background:{cor};margin-top:18px'></div>
  <div style='margin-top:20px;text-align:center;font-size:26px;font-weight:600;color:{MUTED};line-height:1.25'>{nome}</div>
  <div class='tab' style='text-align:center;font-size:34px;font-weight:700;letter-spacing:-.02em;color:{INK};margin-top:4px'>{brl(float(s), False)}</div></div>""")
    vis = f"""<div class='visual' style='margin-top:56px;display:flex;justify-content:space-between;align-items:flex-end;padding:0 10px;
  border-bottom:0'>{''.join(cols)}</div>"""
    corpo = f"""<div class='eyebrow'>Dívidas</div>
<div class='h1' style='font-size:108px'>Qual dívida pagar primeiro?</div>{vis}"""
    return capa("papel", EXTRA_F + corpo, 1, T)


def v_lista():
    cab = (f"<div style='display:grid;grid-template-columns:1.5fr 1fr 1.1fr .9fr 1fr;column-gap:14px;padding:18px 0 14px;border-bottom:2px solid {FIO}'>"
           + "".join(f"<span class='rs' style='text-align:{al}'>{t}</span>" for t, al in
                     [("Dívida", "left"), ("Saldo", "right"), ("Parcela", "right"), ("Juros", "right"), ("Em 1 mês", "right")]) + "</div>")
    linhas = []
    for nome, s, i, n in DIV:
        cara = nome == ORDEM_CARA[0]
        cor = CORAL_FORTE if cara else INK
        fundo = "background:#FDF1EC;margin:0 -20px;padding-left:20px;padding-right:20px;border-radius:16px;" if cara else ""
        linhas.append(f"""<div style='display:grid;grid-template-columns:1.5fr 1fr 1.1fr .9fr 1fr;column-gap:14px;align-items:center;padding:22px 0;border-bottom:2px solid {FIO};{fundo}'>
  <span style='font-size:29px;font-weight:700;line-height:1.15;color:{INK}'>{nome}</span>
  <span class='tab' style='text-align:right;font-size:29px;font-weight:600;color:{INK}'>{brl(float(s), False)}</span>
  <span class='tab' style='text-align:right;font-size:24px;font-weight:500;color:{MUTED};line-height:1.25'>{n} ×<br>{brl(float(PARC[nome]))}</span>
  <span class='tab' style='text-align:right;font-size:29px;font-weight:700;color:{cor}'>{num(float(i * 100), 0)}%</span>
  <span class='tab' style='text-align:right;font-size:34px;font-weight:700;letter-spacing:-.02em;color:{cor}'>{brl(float(JUROS_1M[nome]), False)}</span></div>""")
    return f"""<div class='visual' style='margin-top:34px'><div class='card' style='padding:6px 40px 10px'>{cab}{''.join(linhas)}
  <div style='font-size:26px;line-height:1.38;color:{INK};padding:22px 0 14px'><b style='color:{CORAL_FORTE}'>O tamanho engana:</b> a dívida de R$ 3.000 custa mais por mês que a de R$ 6.000.</div></div>
<div class='nota'>Dívidas e taxas de exemplo, com juros ao mês. Em 1 mês: saldo × taxa.</div></div>"""


def v_metodos():
    def coluna(titulo, apelido, criterio, ordem, rotulo, frase, ip, destaque):
        itens = []
        for k, n in enumerate(ordem, 1):
            s, i = next((s, i) for nn, s, i, _ in DIV if nn == n)
            val = f"{num(float(i * 100), 0)}% ao mês" if rotulo == "taxa" else brl(float(s), False)
            itens.append(f"""<div style='display:flex;align-items:center;gap:16px;padding:12px 0;{"border-top:2px solid " + FIO + ";" if k > 1 else ""}'>
  <span style='flex:none;width:46px;height:46px;border-radius:50%;background:{destaque if k == 1 else BG};color:{"#fff" if k == 1 else INK};
    box-shadow:{"none" if k == 1 else "inset 0 0 0 2px " + NEUTRO};display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700'>{k}</span>
  <span style='flex:1;font-size:25px;font-weight:600;line-height:1.2;color:{INK}'>{n}</span>
  <span class='tab' style='font-size:25px;font-weight:700;color:{CORAL_FORTE if rotulo == "taxa" and k == 1 else INK};white-space:nowrap'>{val}</span></div>""")
        return f"""<div class='card' style='flex:1;padding:28px 30px 22px'>
  <div style='display:flex;align-items:center;gap:14px'>{azulejo(ip, 64, 32)}
    <div><div style='font-size:31px;font-weight:700;letter-spacing:-.025em;line-height:1.1'>{titulo}</div>
      <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:4px'>{apelido}</div></div></div>
  <div style='font-size:23px;font-weight:600;color:{MUTED};margin-top:18px'>{criterio}</div>
  <div style='margin-top:4px'>{''.join(itens)}</div>
  <div style='margin-top:12px;padding:16px 18px;border-radius:16px;background:{SOFT};font-size:25px;font-weight:700;color:{BRAND_DEEP};line-height:1.3'>{frase}</div></div>"""
    return f"""<div class='visual' style='margin-top:34px;display:flex;gap:22px'>
  {coluna("A mais cara primeiro", "o método avalanche", "pela taxa, da maior à menor", ORDEM_CARA, "taxa", "Paga menos juros.", I_DESCE, CORAL)}
  {coluna("A menor primeiro", "a bola de neve", "pelo saldo, do menor ao maior", ORDEM_MENOR, "saldo", "Uma dívida some antes.", I_TROFEU, INK)}
</div>"""


I_ESTUDO = '<path d="M12 6.6C10 5.1 7 4.6 4 5.1v13c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5v-13c-3-.5-6 0-8 1.5z"/><path d="M12 6.6v13"/>'


def v_estudo():
    """Gal e McShane (2012), FATOS_2.md 1.2, 1.3 e 1.7: fechar contas inteiras previu a quitação, qualquer que fosse o
    saldo delas; é associação em dados de uma empresa, não experimento (checagem de fatos de 20/10/2026)."""
    return f"""<div style='margin-top:24px;display:flex;gap:22px;align-items:flex-start;padding:24px 30px;border-radius:24px;background:#fff;border:1px solid {FIO}'>
  {azulejo(I_ESTUDO, 64, 32)}
  <div><div style='font-size:26px;line-height:1.38;color:{INK}'>Num estudo com cerca de 6 mil clientes de uma empresa de renegociação de dívidas, quem fechava mais dívidas inteiras, qualquer que fosse o valor, tinha mais chance de quitar tudo.</div>
    <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:10px'>Gal e McShane, 2012 · uma associação, não uma garantia</div></div></div>"""


def v_exemplo():
    """Três linhas do tempo na mesma escala (24 meses), com o mês em que cada dívida acaba e os juros pagos."""
    W = 790
    um = W / 24
    linhas = [("Só as parcelas", FIM_SO, JUROS_SO_PARCELAS, MUTED, max(FIM_SO.values())),
              ("A mais cara primeiro", FIM_CARA, JUROS_CARA, CORAL_FORTE, MESES_CARA),
              ("A menor primeiro", FIM_MENOR, JUROS_MENOR, INK, MESES_MENOR)]
    cor_div = {"Crediário da loja": AMBER, "Empréstimo pessoal": CORAL, "Financiamento do carro": INK}
    blocos = []
    for i, (rot, fim, juros, cor, total) in enumerate(linhas):
        marcos = "".join(f"<i style='position:absolute;left:{m * um - 12:.1f}px;top:-7px;width:24px;height:24px;border-radius:50%;"
                         f"background:{cor_div[n]};box-shadow:0 0 0 4px #fff;display:block'></i>"
                         for n, m in sorted(fim.items(), key=lambda x: x[1]))
        primeira = min(fim.values())
        borda = f"border-top:2px solid {FIO};" if i else ""
        blocos.append(f"""<div style='padding:22px 0 20px;{borda}'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span style='font-size:30px;font-weight:700;color:{INK}'>{rot}</span>
    <span class='tab' style='font-size:30px;font-weight:700;color:{cor}'>{r0(juros)} <span style='font-size:23px;font-weight:600;color:{MUTED}'>de juros</span></span></div>
  <div style='position:relative;height:10px;margin-top:24px;width:{W}px'>
    <div style='position:absolute;left:0;top:0;height:10px;width:{total * um:.1f}px;border-radius:5px;background:{FIO}'></div>{marcos}</div>
  <div style='display:flex;justify-content:space-between;font-size:23px;font-weight:600;color:{MUTED};margin-top:18px'>
    <span>1ª dívida quitada no {primeira}º mês</span><span>tudo quitado em {total} meses</span></div></div>""")
    leg = "".join(f"<span style='display:flex;align-items:center;gap:9px'><i style='width:20px;height:20px;border-radius:50%;background:{c};display:block'></i>{n}</span>"
                  for n, c in [("Crediário", AMBER), ("Empréstimo", CORAL), ("Carro", INK)])
    return f"""<div class='visual' style='margin-top:30px'><div class='card' style='padding:6px 40px 24px'>{''.join(blocos)}
  <div style='display:flex;gap:28px;font-size:23px;font-weight:600;color:{MUTED};padding-top:6px;border-top:2px solid {FIO};padding-top:18px'>
    <span style='color:{INK};font-weight:700'>Quitada:</span>{leg}</div></div>
<div class='nota'>Conta do exemplo: juros compostos ao mês e parcelas fixas; quando uma dívida acaba, a parcela dela vai para a próxima. Sem IOF e tarifas. Valores arredondados.</div></div>"""


def v_regras():
    def cartao(ip, rot, txt, fonte):
        return f"""<div class='card' style='padding:30px 38px 28px;display:flex;gap:26px;align-items:flex-start'>{azulejo(ip, 84, 42)}
  <div><div style='font-size:36px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{rot}</div>
    <div style='font-size:28px;line-height:1.4;color:{INK};margin-top:10px'>{txt}</div>
    <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:12px'>{fonte}</div></div></div>"""
    return f"""<div class='visual' style='margin-top:36px;display:flex;flex-direction:column;gap:22px'>
  {cartao(I_DESCE, "Antecipar tem desconto", "Pagou parcelas antes, no todo ou em parte? Os juros e os acréscimos caem na proporção.", "Código de Defesa do Consumidor · Lei 8.078/1990, art. 52, § 2º")}
  {cartao(I_CARTAO, "O cartão tem teto", "No rotativo e no parcelamento da fatura, juros e encargos, somados, não passam do valor original da dívida.", "Lei 14.690/2023, art. 28, § 1º · Res. CMN 5.112/2023")}
</div>"""


def post_dividas():
    T = 7
    s = [capa_dividas(T)]
    s.append(slide("light", EXTRA_F + topo(
        "Primeiro passo", "Liste todas.",
        "Saldo, parcela e juros ao mês de cada uma. Os juros de um mês mostram quanto cada dívida custa.",
        cls="h2", estilo_p="font-size:34px;margin-top:22px") + v_lista(), 2, T))
    s.append(slide("light", EXTRA_F + topo(
        "Dois jeitos de escolher", "Pague a parcela de todas. O extra vai para uma só.",
        cls="h3", estilo_t="font-size:58px") + v_metodos() + v_estudo(), 3, T))
    s.append(slide("light", EXTRA_F + topo(
        "No exemplo · além das parcelas", f"Com {r0(EXTRA_MES)} a mais por mês.",
        f"A mais cara primeiro paga {r0(DIF_JUROS)} a menos de juros. A menor primeiro quita a primeira dívida {FIM_CARA[ORDEM_CARA[0]] - FIM_MENOR[ORDEM_MENOR[0]]} meses antes.",
        cls="h3", estilo_p="font-size:33px;margin-top:20px") + v_exemplo(), 4, T))
    s.append(slide("light", EXTRA_F + topo("O que a lei garante", "Duas regras a seu favor.", cls="h3") + v_regras(), 5, T))

    arq = tela(P24, "celular-pendentes-dividas-conta-separada-24-02.png")
    cp, cv = CX["2402_pendentes"]["painel:A pagar"], CX["2402_pendentes"]["painel:A vencer"]
    y_fim_resumo = CX["2402_pendentes"]["3 transações"][1] + CX["2402_pendentes"]["3 transações"][3] + 8
    esq = f"""<div style='flex:1;padding-top:4px'>
  <div class='eyebrow'>No timtimcash</div>
  <div class='h3' style='font-size:50px'>Cada parcela no dia dela.</div>
  <div class='p' style='font-size:28px;margin-top:20px'>Lance cada dívida como Parcelada, em Dívidas e empréstimos. Pendentes mostra o que vence.</div>
  <div style='margin-top:26px;padding:20px 22px;border-radius:22px;background:{SOFT};font-size:25px;line-height:1.38;color:{BRAND_DEEP}'>
    As 3 parcelas do exemplo somam <b>{reais(sum(PARC.values()))}</b> por mês.</div>
</div>"""
    dir_ = (f"<div style='flex:none;width:520px'><div class='dupla'>"
            f"{recorte(arq, px(cp[1] - 4), px(y_fim_resumo), largura=520, x0=px(cp[0] - 4), x1=px(cp[0] + cp[2] + 4))}"
            f"{recorte(arq, px(cv[1] - 4), px(cv[1] + cv[3] + 6), largura=520, x0=px(cv[0] - 4), x1=px(cv[0] + cv[2] + 4))}</div>"
            f"<div class='nota' style='text-align:center;font-size:21px'>Tela real do timtimcash, com dados de exemplo.<br>Conta de exemplo só com as 3 dívidas.</div></div>")
    s.append(slide("light", EXTRA_F + f"<div style='display:flex;gap:36px;align-items:center'>{esq}{dir_}</div>", 6, T))

    s.append(fechamento_verde("Liste. Escolha a ordem. Comece pela primeira.",
                              "Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_fb(h) for h in s]


# ============================================================================ 26/02 · Fevereiro fechou: 5 perguntas
def capa_cinco(T):
    vis = f"""<div class='visual' style='margin-top:20px;display:flex;justify-content:center'>
  <div style='position:relative;width:620px;height:600px'>
    <div style='position:absolute;left:30px;top:-40px;font-size:640px;line-height:1;font-weight:700;letter-spacing:-.06em;color:{BRAND_DEEP};font-variant-numeric:tabular-nums'>5</div>
    <div style='position:absolute;right:10px;bottom:20px;width:236px;height:236px;border-radius:50%;background:{BRAND};box-shadow:0 0 0 18px {SOFT};
      display:flex;align-items:center;justify-content:center'>{svg_icone(I_CHECK, 150, '#fff', 2.6)}</div>
  </div></div>"""
    corpo = f"""<div class='eyebrow'>Fim do mês</div>
<div class='h1' style='font-size:108px'>Fevereiro fechou. 5 perguntas.</div>{vis}"""
    return capa("suave", EXTRA_F + corpo, 1, T)


def pergunta(n, onde, titulo, resposta, visual, idx, T, estilo_p="font-size:34px;margin-top:20px"):
    selo = (f"<span style='display:inline-flex;align-items:center;justify-content:center;width:88px;height:88px;border-radius:26px;background:{BRAND};"
            f"color:#fff;font-size:52px;font-weight:700;letter-spacing:-.04em;flex:none'>{n}</span>")
    cab = f"""<div class='eyebrow'>Pergunta {n} de 5 · {onde}</div>
<div style='display:flex;align-items:center;gap:28px'>{selo}<div class='h3' style='font-size:64px'>{titulo}</div></div>
<div class='p' style='{estilo_p}'>{resposta}</div>"""
    return slide("light", EXTRA_F + cab + f"<div class='visual' style='margin-top:30px'>{visual}{NOTA_TELA}</div>", idx, T)


def post_fim_do_mes():
    T = 7
    s = [capa_cinco(T)]
    arq = tela(P26, "celular-visao-geral-ambos-26-02.png")
    s.append(pergunta(1, "Visão geral, em Ambos", "Quanto sobrou?",
                      f"{reais(RES26_REAL)} até hoje. Com a parcela de amanhã, o mês fecha em <b style='color:{BRAND_DARK}'>{reais(RES26_PREV)}</b>.",
                      recorte(arq, px(778), px(1066), largura=700, x0=px(14), x1=px(376)), 2, T))

    arq = tela(P26, "celular-pendentes-26-02.png")
    c = CX["2602_pendentes"]
    y0, y1 = c["painel:A pagar"][1] - 4, c["painel:A vencer"][1] + c["painel:A vencer"][3] + 6
    s.append(pergunta(2, "Pendentes", "O que ainda vence?",
                      "Só a parcela do notebook, amanhã: R$ 360. Nada vencido.",
                      recorte(arq, px(y0), px(y1), largura=520, x0=px(10), x1=px(380)), 3, T))

    arq = tela(P26, "celular-relatorios-26-02.png")
    c = CX["2602_relatorios"]
    y0 = c["Abaixo do seu padrão"][1] - 24
    y1 = c["sua média 18,3%"][1] + c["sua média 18,3%"][3] + 16
    s.append(pergunta(3, "Relatórios", "Quanto da receita ficou?",
                      "11,4% até hoje, abaixo da sua média de 18,3%. A meta é 20%.",
                      recorte(arq, px(y0), px(y1), largura=700, x0=px(14), x1=px(376)), 4, T))

    y0 = c["painel:Maiores desvios em relação"][1] - 2
    y1 = c["Viagem"][1] - 16
    s.append(pergunta(4, "Relatórios", "O que fugiu do normal?",
                      "Mercado: R$ 453,50 acima da média, +28%. Saúde ficou 52% abaixo.",
                      recorte(arq, px(y0), px(y1), largura=740, x0=px(14), x1=px(376)), 5, T))

    arq = tela(P26, "celular-orcamentos-26-02.png")
    c = CX["2602_orcamentos"]
    y0 = c["faixas"][0][2] - 14
    merc = [it for it in c["itens"] if it[0] == "Mercado"][0]
    y1 = merc[2] + merc[4] + 8
    s.append(pergunta(5, "Orçamentos", "Como ficaram os limites?",
                      "Bares e restaurantes passou R$ 101; Mercado, R$ 99. As outras 3 categorias ficaram dentro do limite.",
                      recorte(arq, px(y0), px(y1), largura=660, x0=px(14), x1=px(376)), 6, T))

    s.append(fechamento_verde("Feche o mês com respostas.",
                              "Visão geral, Pendentes, Relatórios e Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_fb(h) for h in s]


# ============================================================================ 19/02 · Lá fora na declaração (era 17/02)
# Fatos (J/FATOS.md, 5e, e as notas do revisor de 20/10/2026): só a Lei 14.754/2023 (15% sobre os rendimentos, na
# declaração anual, separados; a variação cambial entra no rendimento; conversão pela cotação de fechamento de venda do
# Banco Central na data do fato gerador) e o que saiu em 28/12 (a declaração relaciona os bens e direitos, no Brasil ou no
# exterior, de 31 de dezembro; Perguntas e Respostas IRPF 2026, pergunta 007). Sem o passo a passo das perguntas 479 e 639,
# com o fechamento só de Remessas (sem a frase do controle financeiro) e sem valor em reais do fechamento de 2026 (a PTAX de 31/12/2026 ainda não existe).
# Exceção do art. 2º, § 3º (checagem de fatos de 20/10/2026, conferida no Planalto): a variação cambial de depósitos não
# remunerados em conta-corrente no exterior não é tributada.
no_texto("1902_fechamentos", "Quanto havia no fim de cada ano", "202531/12/2025", "202631/12/2026", "2027hoje, em curso",
         "PTAX de compra")
assert [l[:2] for l in CX["1902_fechamentos"]["linhas"]][-4:] == [["Saldo em US$ no fim de 2025", "12.960,00"], ["Câmbio de 31/12/2025", "5,5018"],
                                                                   ["Saldo em US$ no fim de 2026", "13.380,00"], ["Câmbio de 31/12/2026", ""]]
_cart = ESTADO.gerar("2026-12-31")[0]["exterior"]["carteiras"]["USD"]       # a carteira em dólar informada em 31/12/2026
assert (_cart["valorAtual"], _cart["atualizadoEm"]) == (13380, "2026-12-31") and "2026" not in _cart["fechamentos"]
# desde 29/01/2027 (mudança da conta de base, passo do post de 27/01): o saldo de 31/12/2026 informado, sem câmbio
_cart19 = ESTADO.gerar("2027-02-19")[0]["exterior"]["carteiras"]
assert _cart19["USD"]["fechamentos"]["2026"] == {"valor": 13380, "cambio": 0} and _cart19["EUR"]["fechamentos"]["2026"]["cambio"] == 0
no_texto("1902_remessas_eur", "Remetido | € 2.000,00", "Custo total | R$ 11.525,40", "Câmbio médio efetivo | R$ 5,7627",
         "com IOF · sem IOF R$ 5,7000", "IOF pago | R$ 125,40", "1,10% do valor enviado", "01/12/2026", "Banco na Europa")
assert q2(D("11525.40") - D("2000") * D("5.70")) == D("125.40") and (D("125.40") / D("11400") * 100).quantize(D("0.01")) == D("1.10")


def folha_31(ano, semana, cor_faixa=INK, inclina=0):
    """Folha de calendário de mesa: faixa DEZEMBRO, 31 grande, dia da semana e ano."""
    return f"""<div class='card' style='width:330px;padding:0;overflow:hidden;transform:rotate({inclina}deg);box-shadow:0 2px 4px rgba(15,20,16,.06),0 26px 50px -24px rgba(15,20,16,.35)'>
  <div style='height:72px;background:{cor_faixa};color:#fff;display:flex;align-items:center;justify-content:center;font-size:27px;font-weight:700;letter-spacing:.2em'>DEZEMBRO</div>
  <div style='text-align:center;padding:4px 0 26px'>
    <div style='font-size:200px;line-height:1.02;font-weight:700;letter-spacing:-.06em;color:{INK};font-variant-numeric:tabular-nums'>31</div>
    <div style='font-size:28px;font-weight:600;color:{MUTED}'>{semana}</div>
    <div style='font-size:46px;font-weight:700;letter-spacing:-.03em;color:{cor_faixa if cor_faixa != INK else INK};margin-top:2px'>{ano}</div></div></div>"""


def capa_exterior(T):
    """Duas datas grandes, 31/12/2025 e 31/12/2026, ligadas por uma linha: o ano-calendário da declaração de 2027."""
    def data(txt, cor, fundo):
        return (f"<div style='display:inline-flex;align-items:center;height:168px;padding:0 44px;border-radius:40px;background:{fundo};"
                f"box-shadow:0 2px 4px rgba(15,20,16,.05),0 24px 48px -26px rgba(15,20,16,.35)'>"
                f"<span style='font-size:128px;font-weight:700;letter-spacing:-.05em;color:{cor};font-variant-numeric:tabular-nums;line-height:1'>{txt}</span></div>")
    vis = f"""<div class='visual' style='margin-top:64px;position:relative'>
  <div>{data("31/12/2025", MUTED, "#fff")}</div>
  <div style='position:relative;height:150px;margin-left:96px'>
    <div style='position:absolute;left:0;top:-10px;bottom:-10px;width:8px;border-radius:4px;background:{BRAND}'></div>
    <div style='position:absolute;left:40px;top:50%;transform:translateY(-50%);display:flex;align-items:center;gap:16px'>
      <span style='font-size:34px;font-weight:700;letter-spacing:.14em;color:{BRAND_DEEP}'>O SEU 2026</span></div></div>
  <div style='text-align:right'>{data("31/12/2026", "#fff", BRAND_DEEP)}</div>
</div>"""
    corpo = f"""<div class='eyebrow'>Imposto de renda · exterior</div>
<div class='h1' style='font-size:92px'>O que vai de lá fora para a declaração.</div>{vis}"""
    return capa("papel", EXTRA_F + corpo, 1, T)


def v_lei_exterior():
    def linha(ip, t, s, fonte, primeira=False, excecao=""):
        borda = "" if primeira else f"border-top:2px solid {FIO};"
        exc = (f"<div style='font-size:26px;line-height:1.35;color:{BRAND_DEEP};margin-top:10px;padding:10px 16px;border-radius:14px;"
               f"background:{SOFT}'>{excecao}</div>") if excecao else ""
        return f"""<div style='display:flex;gap:26px;align-items:flex-start;padding:26px 0;{borda}'>{azulejo(ip, 80, 40)}
  <div><div style='font-size:36px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{t}</div>
    <div style='font-size:28px;line-height:1.38;color:{INK};margin-top:8px'>{s}</div>{exc}
    <div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:8px'>{fonte}</div></div></div>"""
    I_PCT = '<path d="M18.5 5.5l-13 13"/><circle cx="7.2" cy="7.2" r="2.4"/><circle cx="16.8" cy="16.8" r="2.4"/>'
    return f"""<div class='visual' style='margin-top:34px'><div class='card' style='padding:0 40px'>
  {linha(I_PCT, "15% sobre os rendimentos", "Na declaração anual, separados dos outros rendimentos e sem deduções.", "Lei 14.754/2023, art. 2º", True)}
  {linha(I_GLOBO, "O câmbio também conta", "A variação da moeda em relação ao real entra no rendimento.", "Lei 14.754/2023, art. 3º, § 1º, II",
         excecao="<b>Exceção:</b> conta-corrente lá fora sem rendimento (art. 2º, § 3º).")}
  {linha(I_SETAS, "Em reais, pela cotação de venda", "De fechamento, do Banco Central, na data do fato gerador.", "Lei 14.754/2023, art. 15")}
</div>
<div class='nota'>Regras para aplicações financeiras no exterior, em vigor desde 1º/01/2024 (art. 47).</div></div>"""


def v_contador():
    itens = [(I_CAL, "O saldo de 31/12 de cada ano", "na moeda de cada conta lá fora"),
             (I_SETAS, "Cada remessa e cada resgate", "com a data e o valor na moeda"),
             (I_RECIBO, "Quanto custou em reais", "com o câmbio efetivo e o IOF de cada envio")]
    linhas = "".join(f"""<div style='display:flex;gap:24px;align-items:center;padding:24px 0;{"border-top:2px solid " + FIO + ";" if i else ""}'>{azulejo(ip, 76, 38)}
  <div><div style='font-size:33px;font-weight:700;letter-spacing:-.025em'>{t}</div><div style='font-size:27px;color:{MUTED};margin-top:4px'>{sub}</div></div></div>"""
                     for i, (ip, t, sub) in enumerate(itens))
    return f"""<div class='visual' style='margin-top:32px'><div class='card' style='padding:6px 40px'>
  <div class='rs' style='padding-top:22px;color:{BRAND_DARK}'>Para levar ao contador</div>{linhas}</div>
  {aviso("O timtimcash organiza os números e não faz a declaração. Confira o seu caso com um contador.", I_ALERT)}</div>"""


def post_exterior():
    T = 6
    s = [capa_exterior(T)]

    arq = tela(P19, "celular-editar-fechamentos-19-02.png")
    s.append(slide("light", EXTRA_F + topo(
        "Bens e direitos · 31 de dezembro", "A declaração olha para 31 de dezembro.",
        "Ela relaciona os bens e direitos, no Brasil ou no exterior, que você tinha nesse dia.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"""<div class='visual' style='margin-top:26px'>
<div class='rs' style='text-align:center;color:{BRAND_DARK};margin-bottom:14px'>No timtimcash · Remessas › Editar fechamentos</div>
{recorte(arq, px(582), px(894), largura=540, x0=px(14), x1=px(376))}{NOTA_TELA}
<div class='nota' style='text-align:center;margin-top:8px'>O câmbio do fechamento mede o rendimento. Para o imposto, vale a regra da lei.</div>
<div class='nota' style='text-align:center;margin-top:8px;font-size:21px'>Fonte: Receita Federal, Perguntas e Respostas IRPF 2026, pergunta 007.</div></div>""", 2, T))

    s.append(slide("light", EXTRA_F + topo(
        "Aplicações financeiras lá fora", "O que diz a Lei 14.754/2023.", cls="h3") + v_lei_exterior(), 3, T))

    arq = tela(P19, "celular-remessas-euro-19-02.png")
    c = CX["1902_remessas_eur"]["painel:Remetido"]
    s.append(slide("light", EXTRA_F + topo(
        "Remessas ao exterior", "Cada envio, com data, reais e IOF.",
        "No exemplo, a remessa de 01/12/2026: € 2.000, que custaram R$ 11.525,40, com R$ 125,40 de IOF.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:32px'>{recorte(arq, px(c[1] - 4), px(c[1] + c[3] + 4), largura=800, x0=px(c[0] - 4), x1=px(c[0] + c[2] + 4))}{NOTA_TELA}</div>", 4, T))

    s.append(slide("light", EXTRA_F + topo(
        "No timtimcash", "Os números do ano, organizados.", cls="h3") + v_contador(), 5, T))

    s.append(fechamento_verde("O seu 2026 lá fora, organizado.",
                              "Remessas ao exterior no timtimcash, no computador ou no celular.", 6, T))
    return [sem_quebra_fb(h) for h in s]


# ============================================================================ 22/02 · Informe de rendimentos
# Prazo: IN RFB 2.060/2021, art. 3º, e, para os bancos, IN SRF 698/2006, art. 2º, I ("regra da Receita"): até o último
# dia útil de fevereiro; em 2027, sexta, 26/02 (J/FATOS.md 5a.1 e 5a.4; endereço da IN SRF 698/2006 com idAto=15640,
# conferido no LexML pelo coordenador). Base do imposto e INSS: Lei 9.250/1995, art. 8º, I e II, "d"; imposto retido a cada
# pagamento: Lei 7.713/1988, art. 7º, I e § 1º; 13º só na fonte e separado: Lei 8.134/1990, art. 16, III (conferidos no
# Planalto em 20/10/2026). Redução anual da declaração de 2027: Lei 15.270/2025 (Lei 9.250/1995, art. 11-A), FATOS 5d.5.
from datetime import date
ULTIMO_UTIL = max(d for d in (date(2027, 2, k) for k in range(1, 29)) if d.weekday() < 5)
assert ULTIMO_UTIL == date(2027, 2, 26)
no_texto("2202_salario", "Ano 2026", "14 transações · 14 pagas · 0 pendentes · somam R$ 125.973,36 · 824 no histórico",
         "13º salário · 2ª parcela", "+R$ 2.433,36", "13º salário · 1ª parcela", "+R$ 4.980,00", "+R$ 9.480,00")
_est22, _ = ESTADO.gerar("2027-02-22")
SAL26 = [t for t in _est22["txs"] if t["data"].startswith("2026") and t["tipo"] == "receita" and t.get("categoria") == "Salário"]
assert len(SAL26) == 14 and sum(D(str(t["valor"])) for t in SAL26) == D("125973.36")
assert sum(D(str(t["valor"])) for t in SAL26 if "13º" in t["descricao"]) == D("7413.36")
FAIXA_ZERO, FAIXA_FIM = D("60000.00"), D("88200.00")          # Lei 15.270/2025, redução anual (FATOS 5d.5)
assert D("8429.73") - D("0.095575") * FAIXA_FIM < D("1") and D("8429.73") - D("0.095575") * FAIXA_ZERO > D("2694")


def capa_informe(T):
    """Um envelope com o selo 26."""
    W, H = 640, 400
    aba = (f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='position:absolute;left:0;top:0'>"
           f"<path d='M10 16 L{W / 2} {H * .58} L{W - 10} 16' fill='none' stroke='{NEUTRO}' stroke-width='6' stroke-linejoin='round'/>"
           f"<path d='M10 {H - 14} L{W * .38} {H * .5}' fill='none' stroke='{FIO}' stroke-width='5' stroke-linecap='round'/>"
           f"<path d='M{W - 10} {H - 14} L{W * .62} {H * .5}' fill='none' stroke='{FIO}' stroke-width='5' stroke-linecap='round'/></svg>")
    folha = (f"<div style='position:absolute;left:46px;top:-128px;width:400px;height:230px;border-radius:18px 18px 0 0;background:#fff;"
             f"border:2px solid {FIO};padding:28px 32px'>"
             f"<div style='font-size:22px;font-weight:700;letter-spacing:.14em;color:{BRAND_DARK};line-height:1.35'>INFORME DE<br>RENDIMENTOS</div>"
             f"<div class='sk' style='width:280px;margin-top:20px'></div><div class='sk' style='width:200px;margin-top:14px'></div></div>")
    selo = (f"<div style='position:absolute;right:-30px;top:-70px;width:250px;height:250px;border-radius:50%;background:{BRAND};"
            f"box-shadow:0 0 0 16px {SOFT},0 18px 40px -16px rgba(6,95,70,.6);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;z-index:3'>"
            f"<div style='font-size:124px;font-weight:700;letter-spacing:-.05em;line-height:.9;font-variant-numeric:tabular-nums'>26</div>"
            f"<div style='font-size:30px;font-weight:700;letter-spacing:.16em;margin-top:8px'>FEV</div></div>")
    env = (f"<div style='position:relative;width:{W}px;height:{H}px;margin:150px auto 0'>{folha}"
           f"<div style='position:absolute;inset:0;border-radius:26px;background:#fff;box-shadow:0 2px 4px rgba(15,20,16,.06),0 30px 60px -28px rgba(15,20,16,.4);z-index:2;overflow:hidden'>{aba}</div>{selo}</div>")
    corpo = f"""<div class='eyebrow'>Imposto de renda</div>
<div class='h1' style='font-size:100px'>Informe de rendimentos: até 26/02.</div>
<div class='visual' style='margin-top:20px'>{env}</div>"""
    return capa("suave", EXTRA_F + corpo, 1, T)


def cal_fev():
    """Fevereiro de 2027 começando no domingo, como nos calendários de novembro e dezembro: 26 em verde."""
    sem = ["D", "S", "T", "Q", "Q", "S", "S"]
    cels = [f"<div style='height:44px;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;color:{MUTED}'>{d}</div>" for d in sem]
    off = (date(2027, 2, 1).weekday() + 1) % 7
    cels += ["<div></div>"] * off
    for d in range(1, 29):
        wd = date(2027, 2, d).weekday()
        if d == 26:
            est = f"background:{BRAND};color:#fff;font-weight:700;box-shadow:0 0 0 7px {SOFT}"
        elif wd >= 5:
            est = f"color:{NEUTRO};font-weight:500"
        else:
            est = f"color:{INK};font-weight:500"
        cels.append(f"<div style='display:flex;align-items:center;justify-content:center;height:78px'><span style='width:64px;height:64px;border-radius:50%;"
                    f"display:flex;align-items:center;justify-content:center;font-size:30px;font-variant-numeric:tabular-nums;{est}'>{d}</span></div>")
    return f"""<div class='card' style='padding:24px 34px 22px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding-bottom:10px'>
    <span style='font-size:32px;font-weight:700;letter-spacing:-.02em'>Fevereiro de 2027</span>
    <span style='font-size:24px;font-weight:700;color:{BRAND_DARK}'>26 · sexta-feira</span></div>
  <div style='display:grid;grid-template-columns:repeat(7,1fr)'>{''.join(cels)}</div></div>"""


def v_conferir():
    itens = [(I_RECIBO, "Rendimentos do ano", "o salário antes dos descontos: entra na base do&nbsp;imposto", "Lei 9.250/1995, art. 8º, I"),
             (I_ESCUDO, "INSS descontado", "a contribuição à Previdência sai da base do imposto", "Lei 9.250/1995, art. 8º, II, d"),
             (I_SETAS, "Imposto retido na fonte", "o IR descontado a cada pagamento de salário", "Lei 7.713/1988, art. 7º, I e § 1º"),
             (I_PRESENTE, "13º salário", "tributado só na fonte, separado do resto", "Lei 8.134/1990, art. 16, III")]
    linhas = "".join(f"""<div style='display:flex;gap:24px;align-items:center;padding:20px 0;{"border-top:2px solid " + FIO + ";" if i else ""}'>{azulejo(ip, 72, 36)}
  <div style='flex:1'><div style='font-size:32px;font-weight:700;letter-spacing:-.025em'>{t}</div>
    <div style='font-size:26px;color:{INK};margin-top:4px;line-height:1.3'>{sub}</div>
    <div style='font-size:21px;font-weight:600;color:{MUTED};margin-top:4px'>{fonte}</div></div>
  <span style='flex:none;width:44px;height:44px;border-radius:12px;box-shadow:inset 0 0 0 3px {BRAND};display:flex;align-items:center;justify-content:center'>{svg_icone(I_CHECK, 30, BRAND, 2.6)}</span></div>"""
                     for i, (ip, t, sub, fonte) in enumerate(itens))
    return f"<div class='visual' style='margin-top:30px'><div class='card' style='padding:4px 40px'>{linhas}</div></div>"


def v_bruto():
    """Ilustração sem valores: o rendimento bruto, os descontos e o líquido que cai na conta."""
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:40px 44px 36px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'><span style='font-size:30px;font-weight:700'>No informe</span>
    <span style='font-size:26px;font-weight:600;color:{MUTED}'>rendimentos, antes dos descontos</span></div>
  <div style='display:flex;gap:4px;margin-top:16px;height:84px'>
    <div style='flex:68;border-radius:18px 6px 6px 18px;background:{BRAND};color:#fff;display:flex;align-items:center;padding-left:26px;font-size:28px;font-weight:700'>líquido</div>
    <div style='flex:12;border-radius:6px;background:{CORAL};color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700'>INSS</div>
    <div style='flex:20;border-radius:6px 18px 18px 6px;background:{CORAL_FORTE};color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700'>IR</div></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;margin-top:40px'><span style='font-size:30px;font-weight:700'>No extrato</span>
    <span style='font-size:26px;font-weight:600;color:{MUTED}'>o que caiu na conta</span></div>
  <div style='display:flex;margin-top:16px;height:84px'>
    <div style='width:68%;border-radius:18px;background:{BRAND};color:#fff;display:flex;align-items:center;padding-left:26px;font-size:28px;font-weight:700'>líquido</div></div>
</div>
<div class='nota'>Ilustração, sem valores. O contracheque mostra os descontos de cada mês; o informe soma o ano.</div></div>"""


def v_reducao():
    def zona(flex, cor, cor_t, t, s, raio):
        return (f"<div style='flex:{flex};display:flex;flex-direction:column;gap:12px'>"
                f"<div style='height:70px;border-radius:{raio};background:{cor}'></div>"
                f"<div style='font-size:28px;font-weight:700;color:{cor_t};line-height:1.15'>{t}</div>"
                f"<div style='font-size:23px;color:{MUTED};line-height:1.3'>{s}</div></div>")
    return f"""<div class='visual' style='margin-top:40px'><div class='card' style='padding:40px 40px 32px'>
  <div class='rs' style='color:{BRAND_DARK}'>Rendimentos tributáveis em 2026</div>
  <div style='display:flex;gap:6px;margin-top:22px'>
    {zona(38, BRAND, BRAND_DARK, "Até R$ 60 mil", "a redução zera o imposto", "18px 6px 6px 18px")}
    {zona(35, f"linear-gradient(90deg,{BRAND},{MENTA_CLARA})", INK, "Até R$ 88,2 mil", "a redução diminui", "6px")}
    {zona(27, FIO, MUTED, "Acima disso", "sem redução", "6px 18px 18px 6px")}
  </div></div>
<div class='nota'>Esquema sem escala. Lei 15.270/2025, que incluiu o art. 11-A na Lei 9.250/1995: redução anual a partir da declaração de 2027.</div></div>"""


def post_informe():
    T = 7
    s = [capa_informe(T)]
    s.append(slide("light", EXTRA_F + topo(
        "O prazo · regra da Receita", "Até o último dia útil de fevereiro.",
        "Empresa, banco e demais fontes pagadoras entregam o informe de 2026 até sexta-feira, 26/02.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px")
        + f"<div class='visual' style='margin-top:32px'>{cal_fev()}<div class='nota'>IN RFB 2.060/2021, art. 3º, e IN SRF 698/2006, art. 2º, I.</div></div>", 2, T))
    s.append(slide("light", EXTRA_F + topo(
        "O que conferir", "Compare com os seus contracheques.", cls="h3") + v_conferir(), 3, T))
    s.append(slide("light", EXTRA_F + topo(
        "Bruto e líquido", "Por que o informe mostra mais que o extrato?",
        "No extrato cai o líquido. O informe mostra os rendimentos e, à parte, o que foi descontado.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px") + v_bruto(), 4, T))
    s.append(slide("light", EXTRA_F + topo(
        "Novidade na declaração de 2027", "Até R$ 60 mil no ano, imposto zero.",
        "Vale para os rendimentos tributáveis de 2026. Por isso, confira o total do informe.",
        cls="h3", estilo_p="font-size:34px;margin-top:20px") + v_reducao(), 5, T))

    arq = tela(P22, "celular-transacoes-salario-2026-22-02.png")
    s.append(slide("light", EXTRA_F + topo(
        "No timtimcash", "O que caiu na conta em 2026.",
        "Em Transações, o Ano 2026 e a busca “salário” somam o que entrou, com o 13º: R$ 125.973,36.",
        cls="h3", estilo_p="font-size:33px;margin-top:20px")
        + f"""<div class='visual' style='margin-top:28px'><div class='dupla'>{recorte(arq, px(60), px(118), largura=700, x0=px(10), x1=px(380), raio=30)}
{recorte(arq, px(312), px(486), largura=700, x0=px(10), x1=px(380))}</div>{NOTA_TELA}
{aviso("O timtimcash organiza os números e não faz a declaração. Confira o seu caso com um contador.")}</div>""", 6, T))

    s.append(fechamento_verde("Informe na mão, números no lugar.",
                              "Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra_fb(h) for h in s]


POSTS = {P17: post_modos, P19: post_exterior, P22: post_informe, P24: post_dividas, P26: post_fim_do_mes}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    renderizar(POSTS, so=so)
