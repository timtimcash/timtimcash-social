# -*- coding: utf-8 -*-
"""Carrosséis da equipe c2 (novembro de 2026): 16/11, 19/11, 23/11, 26/11 e 28/11.

Peças do kit (N/kit/carrossel.py), no formato aprovado em outubro. Telas reais capturadas por captura.py
(conta fictícia de N/base_app, build 2026-10-16.1, o mais recente), guardadas em N/saida/<pasta>/telas/; as caixas (px CSS)
dos recortes estão em caixas.json. Toda conta dos slides é conferida por assert neste arquivo.

python3 posts.py [pasta ...]      grava N/saida/<pasta>/01.jpg ... e confere o layout
"""
import json, math, os, sys
from decimal import Decimal as D, ROUND_HALF_UP

N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, N + "/kit")
from carrossel import *          # noqa: F401,F403 (cores, capa, slide, recorte, NOTA_TELA, fechamento_verde, brl...)

AQUI = os.path.dirname(os.path.abspath(__file__))
CX = json.loads(open(os.path.join(AQUI, "caixas.json"), encoding="utf-8").read().replace("\u00a0", " "))   # sem os espaços fixos do site

P16 = "2026-11-16_iof-da-remessa"
P19 = "2026-11-19_custo-fixo-quanto-ja-tem-dono"
P23 = "2026-11-23_50-30-20-no-seu-extrato"
P26 = "2026-11-26_tres-categorias-levam-dois-tercos"
P28 = "2026-11-28_resgate-quando-o-dinheiro-volta"


def tela(pasta, nome):
    return os.path.join(SAIDA, pasta, "telas", nome)


def px(v):
    """px CSS das capturas (escala 3) para px da imagem."""
    return int(round(v * 3))


def q2(v):
    return D(v).quantize(D("0.01"), rounding=ROUND_HALF_UP)


def pct1(parte, todo):
    """porcentagem com uma casa, como o site (toFixed(1))."""
    return (D(parte) / D(todo) * 100).quantize(D("0.1"), rounding=ROUND_HALF_UP)


def reais(v, casas=2):
    """R$ no formato brasileiro, a partir de Decimal ou número."""
    return brl(float(v), casas > 0)


def numbr(v, casas=2):
    return num(float(v), casas)


MENOS = "−"
CINZA_CLARO = "#E6E3DA"
CINZA_MEDIO = "#D4D2C8"
VERMELHO_SUAVE = "#FBEAEA"
AMBAR_SUAVE = "#FBF1DC"

# ícones de traço extras (24 x 24)
I_LIVRO = '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v14.5H6.5A2.5 2.5 0 0 0 4 20z"/><path d="M4 20a2.5 2.5 0 0 0 2.5 2H20v-4.5"/>'
I_PLAY = '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10.2 9.4v5.2l4.4-2.6z"/>'
I_BANCO = '<path d="M12 3.5 20.5 8h-17z"/><path d="M5 11v6.5M9.7 11v6.5M14.3 11v6.5M19 11v6.5"/><path d="M3.5 20.5h17"/>'
I_CALC = '<rect x="5" y="3" width="14" height="18" rx="2.5"/><path d="M8.5 7h7M8.5 11.5h.01M12 11.5h.01M15.5 11.5h.01M8.5 15h.01M12 15h.01M15.5 15v2.5"/>'
I_ESCADA = '<path d="M4 20h4v-4h4v-4h4V8h4"/><path d="M4 20V4"/>'
I_ATUALIZA = '<path d="M20 11a8 8 0 0 0-14.5-4.5L4 8"/><path d="M4 4v4h4"/><path d="M4 13a8 8 0 0 0 14.5 4.5L20 16"/><path d="M20 20v-4h-4"/>'


def item(ip, titulo, sub, ultimo=False, tam_t=38, tam_s=29):
    """Linha com ícone em azulejo, título e apoio (desenho dos modelos de outubro)."""
    return f"""<div style='display:flex;gap:30px;align-items:center;padding:30px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  {azulejo(ip)}
  <div><div style='font-size:{tam_t}px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{titulo}</div>
  <div style='font-size:{tam_s}px;color:{MUTED};margin-top:8px;line-height:1.32;text-wrap:balance'>{sub}</div></div></div>"""


def nota(txt, centro=False):
    estilo = " style='text-align:center'" if centro else ""
    return f"<div class='nota'{estilo}>{txt}</div>"


def rosca(segs, tam=520, esp=72, fundo=FIO, folga=0.0, centro="", rot=-90):
    """Rosca em SVG: segs = [(fração, cor)], começando às 12 h, no sentido horário. folga: px entre fatias."""
    r = (tam - esp) / 2
    c = 2 * math.pi * r
    cx = tam / 2
    partes = [f"<circle cx='{cx}' cy='{cx}' r='{r:.2f}' fill='none' stroke='{fundo}' stroke-width='{esp}'/>"]
    acc = 0.0
    for f, cor in segs:
        L = f * c
        partes.append(f"<circle cx='{cx}' cy='{cx}' r='{r:.2f}' fill='none' stroke='{cor}' stroke-width='{esp}' "
                      f"stroke-dasharray='{max(L - folga, 0):.2f} {c:.2f}' stroke-dashoffset='{-acc:.2f}' transform='rotate({rot} {cx} {cx})'/>")
        acc += L
    return f"<svg width='{tam}' height='{tam}' viewBox='0 0 {tam} {tam}' style='display:block'>{''.join(partes)}{centro}</svg>"


def ponto_na_rosca(frac, tam, raio):
    """coordenadas (x, y) no SVG da rosca para a fração `frac` do giro, a partir das 12 h."""
    a = -math.pi / 2 + 2 * math.pi * frac
    return tam / 2 + raio * math.cos(a), tam / 2 + raio * math.sin(a)


# ================================================================ 16/11 · IOF da remessa: 1,1% ou 3,5%?
USD = D("4000")
CAMBIO = D("5.05")
EM_REAIS = USD * CAMBIO
IOF_INV = q2(EM_REAIS * D("0.011"))
IOF_DISP = q2(EM_REAIS * D("0.035"))
DIF_IOF = IOF_DISP - IOF_INV
TOTAL_INV = EM_REAIS + IOF_INV
TOTAL_DISP = EM_REAIS + IOF_DISP
assert EM_REAIS == D("20200.00") and IOF_INV == D("222.20") and IOF_DISP == D("707.00") and DIF_IOF == D("484.80")
assert TOTAL_INV == D("20422.20") and TOTAL_DISP == D("20907.00")
assert (TOTAL_INV / USD).quantize(D("0.0001"), rounding=ROUND_HALF_UP) == D("5.1056")
# a tela real (relógio em 16/11/2026) mostra exatamente o exemplo
assert CX["16"]["texto_deriva"] == "Câmbio efetivo R$ 5,1056 por US$ · IOF 1,10% · US$ 4.000 custaram R$ 20.422,20"
assert CX["16"]["campos"]["valor"] == "20.422,20" and CX["16"]["campos"]["enviado"] == "4.000,00" and CX["16"]["campos"]["iof"] == "222,20"
assert CX["16"]["campos"]["data"] == "2026-11-16" and CX["16"]["campos"]["titulo"] == "Nova remessa"


def capa_iof(T):
    """Os dois números enormes, cada um sobre uma coluna de pontos: cada ponto é 0,1 ponto percentual."""
    def coluna(numero, n, cor):
        cols, lado, gap = 7, 42, 13
        linhas = math.ceil(n / cols)
        pontos = []
        for i in range(n):
            lin, col = divmod(i, cols)
            pontos.append(f"<i style='position:absolute;left:{col * (lado + gap)}px;bottom:{lin * (lado + gap)}px;width:{lado}px;height:{lado}px;border-radius:50%;background:{cor};display:block'></i>")
        alt = 5 * (lado + gap) - gap
        larg = cols * (lado + gap) - gap
        return f"""<div style='flex:1;display:flex;flex-direction:column;justify-content:flex-end'>
  <div class='big' style='font-size:178px;line-height:.86;letter-spacing:-.055em;color:{cor};white-space:nowrap'>{numero}</div>
  <div style='position:relative;width:{larg}px;height:{alt}px;margin-top:44px'>{''.join(pontos)}</div></div>"""
    corpo = f"""<div class='eyebrow'>Remessa ao exterior</div>
<div class='h1' style='font-size:112px'>IOF: 1,1% ou 3,5%?</div>
<div style='display:flex;gap:40px;align-items:flex-end;margin-top:78px'>
  {coluna('1,1%', 11, MENTA)}
  {coluna('3,5%', 35, '#FFFFFF')}
</div>"""
    return capa("tinta", corpo, 1, T)


def post_iof():
    T = 6
    s = [capa_iof(T)]

    # 2 · a tabela das alíquotas
    lista = [("Remessa para uma conta sua lá fora", "disponibilidade própria no exterior"),
             ("Compras com cartão no exterior", ""),
             ("Cartão pré-pago e cheques de viagem", ""),
             ("Saques no exterior", ""),
             ("Compra de moeda em espécie", "")]
    def linha(t, sub, ultimo=False):
        return f"""<div style='display:flex;align-items:center;gap:22px;padding:19px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <i style='width:14px;height:14px;border-radius:50%;background:{CORAL};flex:none;display:block'></i>
  <div><div style='font-size:32px;font-weight:600;letter-spacing:-.02em;color:{INK}'>{t}</div>{f"<div style='font-size:25px;color:{MUTED};margin-top:4px'>{sub}</div>" if sub else ''}</div></div>"""
    tabela = f"""<div class='visual' style='margin-top:48px'><div class='card' style='overflow:hidden'>
  <div style='display:flex;align-items:center;justify-content:space-between;gap:24px;padding:34px 44px;background:{SOFT}'>
    <div><div style='font-size:24px;font-weight:700;letter-spacing:.14em;color:{BRAND_DEEP}'>INVESTIMENTO</div>
      <div style='font-size:36px;font-weight:700;letter-spacing:-.025em;margin-top:8px'>Remessa para investir lá fora</div></div>
    <div class='big' style='font-size:86px;color:{BRAND_DARK};flex:none'>1,10%</div></div>
  <div style='padding:26px 44px 12px'>
    <div style='display:flex;align-items:center;justify-content:space-between;gap:24px'>
      <div style='font-size:24px;font-weight:700;letter-spacing:.14em;color:{CORAL_TXT}'>PARA USAR OU TER LÁ FORA</div>
      <div class='big' style='font-size:86px;color:{CORAL_FORTE}'>3,5%</div></div>
    {''.join(linha(t, sub, i == len(lista) - 1) for i, (t, sub) in enumerate(lista))}
  </div></div>
<div class='nota'>Decreto 6.306/2007, art. 15-B, com a redação do Decreto 12.499/2025.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>IOF no câmbio</div>
<div class='h2'>Depende da finalidade.</div>{tabela}""", 2, T))

    # 3 · a mesma remessa, os dois IOFs
    W = 560
    esc = W / float(IOF_DISP)
    w_inv, w_disp = float(IOF_INV) * esc, float(IOF_DISP) * esc
    def barra(rotulo, aliq, valor, total, largura, cor, cor_txt):
        return f"""<div style='margin-top:30px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'>
    <span style='font-size:31px;font-weight:700;color:{INK}'>{rotulo} <span style='color:{cor_txt}'>· {aliq}</span></span>
    <span style='font-size:25px;font-weight:600;color:{MUTED}'>total {total}</span></div>
  <div style='display:flex;align-items:center;gap:20px;margin-top:14px'>
    <div style='width:{largura:.1f}px;height:58px;border-radius:14px;background:{cor}'></div>
    <span class='big' style='font-size:46px;color:{cor_txt}'>{valor}</span></div></div>"""
    conta = f"""<div class='visual' style='margin-top:48px'><div class='card' style='padding:30px 46px 38px'>
  <div style='display:flex;align-items:baseline;justify-content:space-between;gap:16px;padding-bottom:22px;border-bottom:2px solid {FIO}'>
    <span class='rot'>US$ 4.000 a R$ 5,05</span><span class='big' style='font-size:48px'>{reais(EM_REAIS)}</span></div>
  <div class='rot' style='margin-top:24px;font-size:26px'>IOF de cada finalidade</div>
  {barra('Para investir', '1,10%', reais(IOF_INV), reais(TOTAL_INV), w_inv, BRAND, BRAND_DARK)}
  {barra('Para uma conta sua lá fora', '3,5%', reais(IOF_DISP), reais(TOTAL_DISP), w_disp, CORAL, CORAL_FORTE)}
  <div style='display:flex;align-items:center;justify-content:space-between;margin-top:36px;padding:24px 30px;border-radius:20px;background:{AMBAR_SUAVE}'>
    <span style='font-size:31px;font-weight:700;color:{INK}'>Diferença</span>
    <span class='big' style='font-size:58px;color:{INK}'>{reais(DIF_IOF)}</span></div>
</div><div class='nota'>Exemplo: US$ 4.000 a R$ 5,05, sem tarifa.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Mesmos dólares, mesmo câmbio</div>
<div class='h2'>R$ 484,80 de diferença.</div>{conta}""", 3, T))

    # 4 · antes de fechar
    assert pct1(IOF_INV, EM_REAIS) == D("1.1")
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Antes de fechar</div>
<div class='h2'>Confira o enquadramento.</div>
<div class='visual' style='margin-top:52px'><div class='card' style='padding:6px 44px'>
  {item(I_BANCO, 'Quem enquadra é a instituição', 'Ela classifica a operação pela finalidade, e a alíquota vem desse enquadramento.')}
  {item(I_RECIBO, 'O IOF está no comprovante', 'O valor cobrado aparece em reais no comprovante da operação.')}
  {item(I_CALC, 'Faça a conta de uma linha', 'IOF ÷ valor em reais. No exemplo: R$ 222,20 ÷ R$ 20.200 = 1,10%.', True)}
</div></div>""", 4, T))

    # 5 · tela real: Nova remessa preenchida, sem salvar (relógio em 16/11/2026)
    c = CX["16"]
    nr = tela(P16, "celular-nova-remessa-preenchida.png")
    y0, y1 = c["enviado"][1] - 4, c["deriva"][3] + 14
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>A Nova remessa mostra a alíquota na hora.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Você informa o total em reais, o valor enviado e o IOF do comprovante.</div>
<div class='visual' style='margin-top:36px'>{recorte(nr, px(y0), px(y1), largura=700, x0=px(12), x1=px(378))}{NOTA_TELA}</div>""", 5, T))

    s.append(fechamento_verde("Saiba quanto o IOF levou de cada remessa.",
                              "Remessas ao exterior no timtimcash, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 19/11 · Quanto do salário já tem dono?
ALUGUEL, ESCOLA = D("2300.00"), D("1450.00")
VIDEO, MUSICA, NUVEM = D("55.90"), D("21.90"), D("42.00")
ASSIN = VIDEO + MUSICA + NUVEM
FIXO = ALUGUEL + ESCOLA + ASSIN
SALARIO = D("9960.00")
PCT_FIXO = pct1(FIXO, SALARIO)
assert ASSIN == D("119.80") and FIXO == D("3869.80") and PCT_FIXO == D("38.9") and pct1(SALARIO - FIXO, SALARIO) == D("61.1")
assert SALARIO - FIXO == D("6090.20")
assert q2(FIXO / SALARIO * 100) == D("38.85")          # R$ 38,85 de cada R$ 100 (no slide: arredondado a 38,9%)
# a tela real (Visão geral, dezembro de 2026, Previsto, relógio em 19/11/2026)
_t19 = CX["19"]["texto"]
for trecho in ["Dezembro 2026", "PREVISTO", "Deve guardar 61,1% da receita", "61,1%", "38,9%", "Receitas R$ 9.960,00",
               "Despesas R$ 3.869,80", "Resultado previsto", "R$ 6.090,20"]:
    assert trecho in _t19, trecho


def capa_fixo(T):
    tam, esp = 520, 80
    f = float(FIXO / SALARIO)
    r_ext = tam / 2
    centro = f"""<text x='{tam / 2}' y='{tam / 2 + 2}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='53' letter-spacing='-2' fill='#FFFFFF' style='font-feature-settings:"tnum","cv11","ss01"'>R$ 3.869,80</text>
<text x='{tam / 2}' y='{tam / 2 + 44}' text-anchor='middle' font-family='Inter' font-weight='600' font-size='25' fill='{DARK_TEXTO}'>antes de o mês começar</text>"""
    svg = rosca([(f, CORAL)], tam=tam, esp=esp, fundo='#2A332B', centro=centro)
    corpo = f"""<div class='eyebrow'>Custo fixo</div>
<div class='h1' style='font-size:100px'>Quanto do seu salário já tem dono?</div>
<div style='display:flex;align-items:center;gap:34px;margin-top:60px'>
  {svg}
  <div style='white-space:nowrap'>
    <div class='big' style='font-size:150px;line-height:.9;color:{CORAL}'>39%</div>
    <div style='font-size:32px;font-weight:700;color:{CORAL_CLARO};margin-top:12px'>do salário</div></div>
</div>"""
    return capa("tinta", corpo, 1, T)


def post_fixo():
    T = 6
    s = [capa_fixo(T)]

    # 2 · o que é custo fixo
    def linha(ip, nome, sub, valor, ultimo=False):
        return f"""<div style='display:flex;gap:28px;align-items:center;padding:28px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  {azulejo(ip)}
  <div style='flex:1'><div style='font-size:38px;font-weight:700;letter-spacing:-.03em'>{nome}</div>
    <div style='font-size:27px;color:{MUTED};margin-top:6px'>{sub}</div></div>
  <div class='big' style='font-size:46px;flex:none'>{valor}</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Custo fixo</div>
<div class='h2'>Vem todo mês, com ou sem você.</div>
<div class='visual' style='margin-top:52px'><div class='card' style='padding:4px 44px 0'>
  {linha(I_CASA, 'Aluguel', 'todo dia 10', reais(ALUGUEL))}
  {linha(I_LIVRO, 'Escola', 'todo dia 10', reais(ESCOLA))}
  {linha(I_PLAY, 'Assinaturas', 'vídeo, música e nuvem', reais(ASSIN), True)}
  <div style='display:flex;align-items:center;justify-content:space-between;margin:0 -44px;padding:28px 44px;background:{VERMELHO_SUAVE};border-radius:0 0 28px 28px'>
    <span style='font-size:34px;font-weight:700;color:{INK}'>Todo mês</span>
    <span class='big' style='font-size:58px;color:{CORAL_FORTE}'>{reais(FIXO)}</span></div>
</div><div class='nota'>Exemplo: a conta fictícia dos nossos posts.</div></div>""", 2, T))

    # 3 · a conta, em 100 quadradinhos (cada um é 1% do salário)
    cheios = int(FIXO / SALARIO * 100)          # 38 inteiros
    resto = float(FIXO / SALARIO * 100) - cheios  # o 39º, 85% pintado
    assert cheios == 38 and 0.84 < resto < 0.86
    quad = []
    for i in range(100):
        if i < cheios:
            fundo = CORAL
        elif i == cheios:
            fundo = f"linear-gradient(90deg,{CORAL} 0,{CORAL} {resto * 100:.0f}%,{CINZA_CLARO} {resto * 100:.0f}%)"
        else:
            fundo = CINZA_CLARO
        quad.append(f"<i style='display:block;aspect-ratio:1;border-radius:7px;background:{fundo}'></i>")
    grade = f"<div style='display:grid;grid-template-columns:repeat(20,1fr);gap:7px'>{''.join(quad)}</div>"
    conta = f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:38px 44px 40px'>
  <div style='display:flex;align-items:flex-end;justify-content:space-between;gap:10px'>
    <div><div class='rot' style='font-size:25px'>Custo fixo</div><div class='big' style='font-size:44px;margin-top:4px'>{reais(FIXO)}</div></div>
    <div class='big' style='font-size:44px;color:{MUTED}'>÷</div>
    <div><div class='rot' style='font-size:25px'>Salário</div><div class='big' style='font-size:44px;margin-top:4px'>{reais(SALARIO)}</div></div>
    <div class='big' style='font-size:44px;color:{MUTED}'>=</div>
    <div class='big' style='font-size:64px;line-height:1;color:{CORAL_FORTE}'>38,9%</div>
  </div>
  <div class='fio' style='margin:34px 0 32px'></div>
  {grade}
  <div style='display:flex;justify-content:space-between;margin-top:20px;font-size:26px;font-weight:600'>
    <span style='color:{CORAL_TXT}'>já tem dono</span><span style='color:{MUTED}'>cada quadradinho é 1% do salário</span></div>
</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta</div>
<div class='h2'>De cada R$ 100 do salário, quase R$ 39 já têm dono.</div>{conta}""", 3, T))

    # 4 · por que importa
    f = float(FIXO / SALARIO * 100)
    barra = f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:36px 44px 38px'>
  <div style='display:flex;height:72px;border-radius:18px;overflow:hidden;gap:5px'>
    <div style='width:{f:.2f}%;background:{CORAL}'></div><div style='flex:1;background:{BRAND}'></div></div>
  <div style='display:flex;margin-top:20px'>
    <div style='width:{f:.2f}%'><div style='font-size:25px;font-weight:700;color:{CORAL_TXT}'>FIXO</div><div class='big' style='font-size:42px;margin-top:4px'>38,9%</div></div>
    <div style='flex:1;padding-left:14px'><div style='font-size:25px;font-weight:700;color:{BRAND_DARK}'>O RESTO DO MÊS</div><div class='big' style='font-size:42px;margin-top:4px'>61,1%</div>
      <div style='font-size:25px;color:{MUTED};margin-top:4px;line-height:1.3'>mercado, transporte, imprevistos e o que você guarda</div></div></div>
</div></div>
<div class='visual' style='margin-top:30px'><div class='card' style='padding:32px 40px;background:{AMBAR_SUAVE};border-color:#F3E2BC;box-shadow:none;display:flex;gap:28px;align-items:flex-start'>
  <div style='width:80px;height:80px;border-radius:28%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none'>{svg_icone(I_CAL, 42, AMBER_TEXT, 2.2)}</div>
  <div><div style='font-size:36px;font-weight:700;letter-spacing:-.03em;color:{INK}'>Fixo novo é decisão de anos.</div>
    <div style='font-size:29px;line-height:1.36;color:{INK};margin-top:10px'>Escola, financiamento, plano anual: antes de assinar, veja quanto ele leva do salário.</div></div>
</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Por que importa</div>
<div class='h2'>Fixo alto, folga curta.</div>
<div class='p' style='margin-top:26px'>Quanto maior o fixo, menos espaço para imprevistos e para guardar.</div>{barra}""", 4, T))

    # 5 · tela real: Visão geral de dezembro em Previsto (relógio em 19/11/2026)
    c = CX["19"]
    vg = tela(P19, "celular-visao-geral-dezembro-previsto.png")
    topo = recorte(vg, px(8), px(c["seg"][3] + 10), largura=560, x0=px(6), x1=px(384))
    mov = recorte(vg, px(c["mov"][1] - 10), px(c["pat"][3] - 6), largura=560, x0=px(20), x1=px(370))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>Dezembro já mostra o que está contratado.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Lance como “Fixa” uma vez: fica pendente nos próximos meses e aparece em “Previsto”.</div>
<div class='visual' style='margin-top:30px'>{topo}<div style='height:16px'></div>{mov}{NOTA_TELA}</div>""", 5, T))

    s.append(fechamento_verde("Veja o mês que vem antes de ele chegar.",
                              "Visão geral no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 23/11 · 50/30/20 no seu extrato
RECEITA_OUT = D("10280.00")
OUT = {"Casa": D("2492.60"), "Mercado": D("1725.00"), "Educação": D("1450.00"), "Transporte": D("1207.00"),
       "Bares e restaurantes": D("681.40"), "Lazer e hobbies": D("214.90"), "Presentes e doações": D("180.00"),
       "Saúde": D("144.30"), "Assinaturas e serviços": D("119.80")}
DESPESA_OUT = sum(OUT.values())
NECESSIDADES = ["Casa", "Educação", "Mercado", "Transporte", "Saúde"]
DESEJOS = ["Bares e restaurantes", "Lazer e hobbies", "Assinaturas e serviços", "Presentes e doações"]
NEC = sum(OUT[k] for k in NECESSIDADES)
DES = sum(OUT[k] for k in DESEJOS)
FUT = RECEITA_OUT - DESPESA_OUT
assert DESPESA_OUT == D("8215.00") and NEC == D("7018.90") and DES == D("1196.10") and FUT == D("2065.00")
P_NEC, P_DES, P_FUT = [int((v / RECEITA_OUT * 100).quantize(D("1"), rounding=ROUND_HALF_UP)) for v in (NEC, DES, FUT)]
assert (P_NEC, P_DES, P_FUT) == (68, 12, 20) and P_NEC + P_DES + P_FUT == 100
# a tela real (DRE de outubro, relógio em 23/11/2026): a % da receita de cada categoria
_l23 = {l[0]: l[1] for l in CX["23"]["linhas"]}
for k, v in OUT.items():
    assert _l23[k] == numbr(pct1(v, RECEITA_OUT), 1) + "%", (k, _l23[k])
assert "+R$ 2.065,00" in CX["23"]["texto"] and "R$ 10.280,00" in CX["23"]["texto"] and "79,9%" in CX["23"]["texto"]
COR_NEC, COR_DES, COR_FUT = CORAL, CORAL_CLARO, BRAND


def barra_503020(partes, altura=118, tam=62, cores=None, cor_txt=INK, raio=20):
    cores = cores or [COR_NEC, COR_DES, COR_FUT]
    segs = []
    for i, (p, cor) in enumerate(zip(partes, cores)):
        r = f"border-radius:{raio}px 0 0 {raio}px" if i == 0 else (f"border-radius:0 {raio}px {raio}px 0" if i == 2 else "")
        segs.append(f"<div style='flex:{p} 1 0;min-width:0;background:{cor};{r};display:flex;align-items:center;justify-content:center'>"
                    f"<span class='big' style='font-size:{tam}px;color:{cor_txt if i < 2 or cor != BRAND else '#fff'}'>{p}</span></div>")
    return f"<div style='display:flex;height:{altura}px;gap:6px'>{''.join(segs)}</div>"


def capa_503020(T):
    cores = [CORAL, CORAL_CLARO, MENTA]
    def leg(cor, txt):
        return f"<span style='display:flex;align-items:center;gap:12px'><i style='width:22px;height:22px;border-radius:6px;background:{cor};display:block'></i>{txt}</span>"
    corpo = f"""<div class='eyebrow'>Regra de bolso</div>
<div class='h1' style='font-size:118px'>50/30/20 no seu extrato</div>
<div style='margin-top:76px'>
  <div style='font-size:28px;font-weight:700;letter-spacing:.12em;color:{DARK_TEXTO}'>A REGRA</div>
  <div style='margin-top:16px'>{barra_503020([50, 30, 20], cores=cores, tam=66)}</div>
  <div style='font-size:28px;font-weight:700;letter-spacing:.12em;color:{DARK_TEXTO};margin-top:46px'>NO EXEMPLO</div>
  <div style='margin-top:16px'>{barra_503020([P_NEC, P_DES, P_FUT], cores=cores, tam=66)}</div>
  <div style='display:flex;gap:34px;margin-top:34px;font-size:27px;font-weight:600;color:{DARK_TEXTO}'>
    {leg(CORAL, 'necessidades')}{leg(CORAL_CLARO, 'desejos')}{leg(MENTA, 'futuro')}</div>
</div>"""
    return capa("tinta", corpo, 1, T)


def post_503020():
    T = 6
    s = [capa_503020(T)]

    # 2 · a regra
    def col(p, cor, nome, sub, cor_n):
        return f"""<div style='flex:1;padding:34px 30px 36px;border-radius:24px;background:#fff;border:1px solid {FIO};box-shadow:0 1px 2px rgba(15,20,16,.04),0 14px 34px -16px rgba(15,20,16,.14)'>
  <div style='height:14px;width:64px;border-radius:7px;background:{cor}'></div>
  <div class='big' style='font-size:92px;margin-top:22px;color:{cor_n}'>{p}%</div>
  <div style='font-size:33px;font-weight:700;letter-spacing:-.02em;margin-top:8px'>{nome}</div>
  <div style='font-size:26px;line-height:1.34;color:{MUTED};margin-top:12px'>{sub}</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A regra</div>
<div class='h2'>O que entra, dividido em três.</div>
<div class='p' style='margin-top:26px'>Um ponto de partida popularizado por Elizabeth Warren e Amelia Warren Tyagi no livro <i>All Your Worth</i> (2005).</div>
<div class='visual' style='margin-top:46px;display:flex;gap:20px'>
  {col(50, COR_NEC, 'Necessidades', 'O que não dá para deixar de pagar.', CORAL_FORTE)}
  {col(30, COR_DES, 'Desejos', 'O que dá para escolher.', CORAL_TXT)}
  {col(20, COR_FUT, 'Futuro', 'Guardar e quitar dívidas.', BRAND_DARK)}
</div>
<div class='nota'>A base é a renda líquida: o salário depois dos descontos.</div>""", 2, T))

    # 3 · no exemplo
    def parte(cor, nome, cats, valor, p, ultimo=False):
        return f"""<div style='display:flex;align-items:center;gap:24px;padding:24px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <i style='width:26px;height:26px;border-radius:8px;background:{cor};display:block;flex:none'></i>
  <div style='flex:1;min-width:0'><div style='font-size:34px;font-weight:700;letter-spacing:-.02em'>{nome}</div>
    <div style='font-size:25px;color:{MUTED};margin-top:5px;line-height:1.3'>{cats}</div></div>
  <div style='text-align:right;flex:none'><div class='big' style='font-size:44px'>{p}%</div>
    <div style='font-size:25px;font-weight:600;color:{MUTED};font-variant-numeric:tabular-nums'>{valor}</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No exemplo</div>
<div class='h2'>68 · 12 · 20.</div>
<div class='p' style='margin-top:22px'>Outubro de 2026, com R$ 10.280 de receita.</div>
<div class='visual' style='margin-top:40px'><div class='card' style='padding:34px 40px 10px'>
  {barra_503020([P_NEC, P_DES, P_FUT], altura=96, tam=50)}
  <div style='margin-top:10px'>
  {parte(COR_NEC, 'Necessidades', 'casa, educação, mercado, transporte e saúde', reais(NEC), P_NEC)}
  {parte(COR_DES, 'Desejos', 'bares e restaurantes, lazer, assinaturas e presentes', reais(DES), P_DES)}
  {parte(COR_FUT, 'Futuro', 'o que sobrou, com os R$ 1.500 da reserva', reais(FUT), P_FUT, True)}</div>
</div><div class='nota'>A divisão das categorias é deste exemplo. Cada pessoa classifica as suas.</div></div>""", 3, T))

    # 4 · leia assim (halteres: a regra e o exemplo na mesma régua)
    def haltere(nome, regra, ex, cor, leitura, cor_leit, ultimo=False):
        x0, x1 = regra / 80 * 100, ex / 80 * 100
        a, b = min(x0, x1), max(x0, x1)
        return f"""<div style='padding:20px 0 16px;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'><span style='font-size:33px;font-weight:700'>{nome}</span>
    <span style='font-size:27px;font-weight:700;color:{cor_leit}'>{leitura}</span></div>
  <div style='position:relative;height:64px;margin-top:12px'>
    <div style='position:absolute;left:0;right:0;top:30px;height:4px;border-radius:2px;background:{FIO}'></div>
    <div style='position:absolute;left:{a:.2f}%;width:{b - a:.2f}%;top:27px;height:10px;border-radius:5px;background:{cor}'></div>
    <i style='position:absolute;left:{x0:.2f}%;top:32px;width:34px;height:34px;border-radius:50%;background:#fff;border:6px solid {MUTED};transform:translate(-50%,-50%);box-sizing:border-box;display:block'></i>
    <i style='position:absolute;left:{x1:.2f}%;top:32px;width:40px;height:40px;border-radius:50%;background:{cor};border:6px solid #fff;box-shadow:0 0 0 2px {cor};transform:translate(-50%,-50%);box-sizing:border-box;display:block'></i>
  </div>
  <div style='position:relative;height:30px;font-size:24px;font-weight:600;color:{MUTED}'>
    <span style='position:absolute;left:{x0:.2f}%;transform:translateX(-50%);white-space:nowrap'>{'regra ' if regra != ex else ''}{regra}%</span>
    {'' if regra == ex else f"<span style='position:absolute;left:{x1:.2f}%;transform:translateX(-50%);white-space:nowrap;color:{INK};font-weight:700'>{ex}%</span>"}
  </div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Leia assim</div>
<div class='h2'>Necessidade acima de 50% é comum.</div>
<div class='p' style='margin-top:20px;font-size:37px'>Com aluguel e escola, acontece. O que pesa é o futuro chegar aos 20%.</div>
<div class='visual' style='margin-top:30px'><div class='card' style='padding:0 44px 2px'>
  {haltere('Necessidades', 50, P_NEC, COR_NEC, '+18 pontos', CORAL_FORTE)}
  {haltere('Desejos', 30, P_DES, COR_DES, '−18 pontos', CORAL_TXT)}
  {haltere('Futuro', 20, P_FUT, COR_FUT, 'nos 20%', BRAND_DARK, True)}
</div><div class='nota'>Os 18 pontos a mais nas necessidades saíram dos desejos.</div></div>""", 4, T))

    # 5 · tela real: Resultado (DRE) de outubro, janela de 800 px no computador (relógio em 23/11/2026)
    c = CX["23"]
    dre = tela(P23, "computador-dre-outubro.png")
    xa, xb = c["cab_des"][0] + 3, c["cab_des"][2] - 3      # por dentro das linhas: a seta e o valor ficam inteiros
    ya, yb = c["linhas"][2][4] - 6, c["linhas"][-1][6] + 6
    larg = 620
    esc = larg / (xb - xa)
    marcas = []
    for nome, pct_txt, val, l, t_, r, b in c["linhas"]:
        if nome not in OUT:
            continue
        cor = COR_NEC if nome in NECESSIDADES else COR_DES
        yc = ((t_ + b) / 2 - ya) * esc
        marcas.append(f"<i style='position:absolute;left:-46px;top:{yc - 11:.1f}px;width:22px;height:22px;border-radius:7px;background:{cor};display:block'></i>")
    alt_rec = (yb - ya) * esc
    tela_dre = f"""<div style='position:relative;width:{larg}px;margin:0 auto'>{recorte(dre, px(ya), px(yb), largura=larg, x0=px(xa), x1=px(xb))}
  {''.join(marcas)}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No Resultado (DRE)</div>
<div class='h3'>Cada categoria em % da receita.</div>
<div class='visual' style='margin-top:40px'>{tela_dre}
<div style='display:flex;justify-content:center;align-items:center;gap:26px;margin-top:22px;font-size:25px;font-weight:600;color:{INK}'>
  <span style='display:flex;align-items:center;gap:10px'><i style='width:22px;height:22px;border-radius:6px;background:{COR_NEC};display:block'></i>necessidade</span>
  <span style='display:flex;align-items:center;gap:10px'><i style='width:22px;height:22px;border-radius:6px;background:{COR_DES};display:block'></i>desejo</span>
  <span style='color:{MUTED}'>· some cada parte</span></div>
{NOTA_TELA}</div>""", 5, T))

    s.append(fechamento_verde("Descubra a sua proporção.",
                              "Resultado (DRE) no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 26/11 · 3 categorias levam mais de 2/3 do gasto
TOP3 = ["Casa", "Mercado", "Educação"]
SOMA_TOP3 = sum(OUT[k] for k in TOP3)
OUTRAS = DESPESA_OUT - SOMA_TOP3
assert SOMA_TOP3 == D("5667.60") and OUTRAS == D("2547.40")
assert [pct1(OUT[k], DESPESA_OUT) for k in TOP3] == [D("30.3"), D("21.0"), D("17.7")] and pct1(OUTRAS, DESPESA_OUT) == D("31.0")
assert int((SOMA_TOP3 / DESPESA_OUT * 100).quantize(D("1"))) == 69 and SOMA_TOP3 / DESPESA_OUT > D(2) / D(3)
CORTE_MERCADO = OUT["Mercado"] * D("0.10")
assert CORTE_MERCADO == D("172.50") and OUT["Assinaturas e serviços"] == D("119.80") and CORTE_MERCADO > OUT["Assinaturas e serviços"]
# a tela real (Relatórios › Concentração, outubro, relógio em 26/11/2026)
_t26 = CX["26"]["texto"]
for trecho in ["3 categorias respondem por 69% do que você gastou", "Casa\n30,3%", "Mercado\n21,0%", "Educação\n17,7%", "Outras 6 categorias\n31,0%"]:
    assert trecho in _t26, trecho
CORES_TOP3 = [CORAL_FORTE, CORAL, CORAL_CLARO]


def capa_concentracao(T):
    tam, esp = 540, 96
    fr = [float(OUT[k] / DESPESA_OUT) for k in TOP3]
    centro = f"""<text x='{tam / 2}' y='{tam / 2 + 50}' text-anchor='middle' font-family='Inter' font-weight='700' font-size='150' letter-spacing='-7' fill='{INK}' style='font-feature-settings:"tnum","cv11","ss01"'>2/3</text>"""
    svg = rosca(list(zip(fr, CORES_TOP3)), tam=tam, esp=esp, fundo="#FFFFFF", folga=5, centro=centro)
    corpo = f"""<div class='eyebrow'>Concentração</div>
<div class='h1' style='font-size:96px'>3 categorias levam mais de 2/3 do seu gasto.</div>
<div style='display:flex;justify-content:center;margin-top:60px'>{svg}</div>"""
    return capa("suave", corpo, 1, T)


def squarify(vals, x, y, w, h):
    """Treemap (algoritmo squarified): vals já em área, em ordem decrescente."""
    rects, vals = [], list(vals)
    def pior(linha, lado):
        s = sum(linha)
        return max(max(lado * lado * r / (s * s), (s * s) / (lado * lado * r)) for r in linha)
    while vals:
        lado = min(w, h)
        linha = [vals.pop(0)]
        while vals and pior(linha + [vals[0]], lado) <= pior(linha, lado):
            linha.append(vals.pop(0))
        s = sum(linha)
        if w >= h:
            cw, yy = s / h, y
            for r in linha:
                rects.append((x, yy, cw, r / cw)); yy += r / cw
            x += cw; w -= cw
        else:
            ch, xx = s / w, x
            for r in linha:
                rects.append((xx, y, r / ch, ch)); xx += r / ch
            y += ch; h -= ch
    return rects


def post_concentracao():
    T = 6
    s = [capa_concentracao(T)]

    # 2 · treemap das 9 categorias de outubro
    W, H, g = 896, 540, 8
    nomes = sorted(OUT, key=lambda k: -OUT[k])
    areas = [float(OUT[k] / DESPESA_OUT) * W * H for k in nomes]
    rects = squarify(areas, 0, 0, W, H)
    curtos = {"Bares e restaurantes": "Bares e restaurantes", "Lazer e hobbies": "Lazer", "Presentes e doações": "Presentes",
              "Assinaturas e serviços": "Assinaturas"}
    blocos = []
    for i, (k, (x, y, w, h)) in enumerate(zip(nomes, rects)):
        forte = k in TOP3
        cor = CORES_TOP3[TOP3.index(k)] if forte else ["#E6E3DA", "#DDDACF", "#D4D2C8"][i % 3]
        txt = "#fff" if cor in (CORAL_FORTE,) else INK
        p_ = pct1(OUT[k], DESPESA_OUT)
        rot = ""
        if w > 150 and h > 110:
            rot = (f"<div style='font-size:{34 if forte else 27}px;font-weight:700;letter-spacing:-.02em;line-height:1.1'>{k if w > 300 else curtos.get(k, k)}</div>"
                   f"<div class='big' style='font-size:{58 if forte else 34}px;color:{txt};margin-top:6px'>{numbr(p_, 1)}%</div>")
        elif w > 120 and h > 70:
            rot = f"<div style='font-size:23px;font-weight:700'>{numbr(p_, 1)}%</div>"
        blocos.append(f"<div style='position:absolute;left:{x + g / 2:.1f}px;top:{y + g / 2:.1f}px;width:{w - g:.1f}px;height:{h - g:.1f}px;"
                      f"border-radius:16px;background:{cor};color:{txt};padding:{18 if w > 150 else 10}px {20 if w > 150 else 10}px;overflow:hidden'>{rot}</div>")
    mapa = f"<div style='position:relative;width:{W}px;height:{H}px;margin-left:-4px'>{''.join(blocos)}</div>"
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O que é</div>
<div class='h2'>Poucas categorias pesam muito.</div>
<div class='p' style='margin-top:22px'>As 9 categorias de gasto de outubro, cada uma do tamanho do que levou.</div>
<div class='visual' style='margin-top:36px'>{mapa}<div class='nota'>Os menores: lazer 2,6%, presentes 2,2%, saúde 1,8% e assinaturas 1,5%.</div></div>""", 2, T))

    # 3 · as três e o resto, como uma conta
    def linha(cor, nome, p_, valor, forte=False):
        return f"""<div style='display:flex;align-items:center;gap:22px;padding:22px 0;border-bottom:2px solid {FIO}'>
  <i style='width:26px;height:26px;border-radius:8px;background:{cor};display:block;flex:none'></i>
  <span style='flex:1;font-size:36px;font-weight:{700 if forte else 600};letter-spacing:-.02em'>{nome}</span>
  <span style='font-size:30px;font-weight:600;color:{MUTED};font-variant-numeric:tabular-nums'>{p_}</span>
  <span class='big' style='font-size:40px;width:250px;text-align:right'>{valor}</span></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No exemplo</div>
<div class='h2'>As três maiores somam 69%.</div>
<div class='visual' style='margin-top:48px'><div class='card' style='padding:14px 44px 0;overflow:hidden'>
  {''.join(linha(c_, k, numbr(pct1(OUT[k], DESPESA_OUT), 1) + '%', reais(OUT[k])) for k, c_ in zip(TOP3, CORES_TOP3))}
  <div style='display:flex;align-items:center;justify-content:space-between;gap:20px;margin:0 -44px;padding:30px 44px;background:{VERMELHO_SUAVE}'>
    <span style='font-size:36px;font-weight:700'>As 3 juntas</span>
    <span style='display:flex;align-items:baseline;gap:22px'><span class='big' style='font-size:74px;color:{CORAL_FORTE}'>69%</span>
      <span class='big' style='font-size:40px'>{reais(SOMA_TOP3)}</span></span></div>
  <div style='display:flex;align-items:center;gap:22px;padding:26px 0 30px'>
    <i style='width:26px;height:26px;border-radius:8px;background:#fff;border:2px solid {NEUTRO};box-sizing:border-box;display:block;flex:none'></i>
    <span style='flex:1;font-size:33px;font-weight:600;color:{MUTED}'>Outras 6 categorias</span>
    <span style='font-size:30px;font-weight:600;color:{MUTED}'>31,0%</span>
    <span class='big' style='font-size:40px;width:250px;text-align:right;color:{MUTED}'>{reais(OUTRAS)}</span></div>
</div><div class='nota'>Despesas de outubro de 2026: R$ 8.215,00.</div></div>""", 3, T))

    # 4 · onde mexer primeiro
    larg = 600
    def barra(rot, sub, valor, v, cor, cor_txt):
        w = float(v / CORTE_MERCADO) * larg
        return f"""<div style='margin-top:34px'>
  <div style='font-size:33px;font-weight:700;letter-spacing:-.02em'>{rot}</div>
  <div style='font-size:26px;color:{MUTED};margin-top:4px'>{sub}</div>
  <div style='display:flex;align-items:center;gap:22px;margin-top:16px'>
    <div style='width:{w:.1f}px;height:66px;border-radius:16px;background:{cor}'></div>
    <span class='big' style='font-size:52px;color:{cor_txt}'>{valor}</span></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Onde mexer primeiro</div>
<div class='h2'>Comece pelo que pesa.</div>
<div class='p' style='margin-top:24px'>Um corte pequeno numa categoria grande vale mais que um corte inteiro numa pequena.</div>
<div class='visual' style='margin-top:40px'><div class='card' style='padding:14px 46px 44px'>
  {barra('Cortar 10% do Mercado', 'de R$ 1.725,00 para R$ 1.552,50', reais(CORTE_MERCADO), CORTE_MERCADO, BRAND, BRAND_DARK)}
  {barra('Cancelar todas as assinaturas', 'vídeo, música e nuvem', reais(OUT['Assinaturas e serviços']), OUT['Assinaturas e serviços'], CINZA_MEDIO, INK)}
  <div class='fio' style='margin:38px 0 0'></div>
  <div style='font-size:28px;font-weight:600;color:{MUTED};margin-top:22px'>quanto fica no bolso por mês, no exemplo de outubro</div>
</div></div>""", 4, T))

    # 5 · tela real: Relatórios › Concentração em outubro (relógio em 26/11/2026)
    conc = tela(P26, "celular-relatorios-concentracao-outubro.png")
    from PIL import Image
    wc, hc = Image.open(conc).size
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Em Relatórios</div>
<div class='h3'>A Concentração faz essa conta.</div>
<div class='p' style='margin-top:18px;font-size:35px'>No período que você escolher, ela mostra quantas categorias levam a maior parte do gasto.</div>
<div class='visual' style='margin-top:44px'>{recorte(conc, 12, hc - 12, largura=760, x0=12, x1=wc - 12)}{NOTA_TELA}</div>""", 5, T))

    s.append(fechamento_verde("Comece pelas categorias que pesam.",
                              "Relatórios no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]


# ================================================================ 28/11 · O dinheiro voltou. E o câmbio?
REMESSAS = [("12/07/2023", D("4.90")), ("14/03/2024", D("5.00")), ("18/04/2024", D("5.10"))]
MEDIO = sum(D("4000") * c for _, c in REMESSAS) / D("12000")
assert MEDIO == D("5.00")
RESG_USD, RESG_BRL = D("1000"), D("5020.00")
CAMBIO_VOLTA = RESG_BRL / RESG_USD
assert CAMBIO_VOLTA == D("5.02")
CUSTO_1000 = RESG_USD * MEDIO
CENARIOS = [(D("4.50"), RED, RED_TEXT), (CAMBIO_VOLTA, BRAND, BRAND_DARK), (D("5.50"), BRAND, BRAND_DARK)]
for cb, _, _ in CENARIOS:
    assert RESG_USD * cb - CUSTO_1000 in (D("-500.00"), D("20.00"), D("500.00"))
# a tela real (relógio em 28/11/2026)
assert CX["28a"]["texto_deriva"] == "Câmbio efetivo R$ 5,0200 por US$ · US$ 1.000 viraram R$ 5.020,00"
assert CX["28a"]["campos"] == {"valor": "5.020,00", "resgatado": "1.000,00", "data": "2026-11-28", "titulo": "Novo resgate"}
_t28 = CX["28b"]["texto"]
for trecho in ["1 movimentação posterior ao valor informado, fora do ganho", "RESGATE", "−US$ 1.000,00", "R$ 5,0200",
               "28/11/2026", "18/04/2024", "R$ 5,1000", "Atualizar"]:
    assert trecho in _t28, trecho


def capa_volta(T):
    W, H = 896, 560
    seta = BRAND
    svg = f"""<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' style='display:block;overflow:visible'>
  <path d='M 372 128 H 676 A 152 152 0 0 1 676 432 H 400' fill='none' stroke='{seta}' stroke-width='34' stroke-linecap='round' stroke-linejoin='round'/>
  <path d='M 420 382 L 352 432 L 420 482' fill='none' stroke='{seta}' stroke-width='34' stroke-linecap='round' stroke-linejoin='round'/>
</svg>"""
    def pilula(txt, top, fundo, cor, borda):
        return (f"<div style='position:absolute;left:0;top:{top}px;width:330px;height:190px;border-radius:95px;background:{fundo};{borda}"
                f"display:flex;align-items:center;justify-content:center'><span class='big' style='font-size:118px;letter-spacing:-.05em;color:{cor}'>{txt}</span></div>")
    rotulo = (f"<div style='position:absolute;left:{556}px;top:{H / 2 - 40}px;transform:translateX(-50%);height:80px;padding:0 30px;border-radius:40px;background:#fff;"
              f"border:2px solid {FIO};box-shadow:0 1px 2px rgba(15,20,16,.05),0 18px 36px -20px rgba(15,20,16,.35);display:flex;align-items:center;"
              f"font-size:31px;font-weight:700;color:{BRAND_DEEP};white-space:nowrap'>câmbio do dia?</div>")
    visual = f"""<div style='position:relative;width:{W}px;height:{H}px;margin-top:70px'>
  {svg}
  {pilula('US$', 33, '#FFFFFF', INK, f'border:2px solid {FIO};box-shadow:0 1px 2px rgba(15,20,16,.05),0 26px 50px -26px rgba(15,20,16,.40);')}
  {pilula('R$', 337, BRAND, '#FFFFFF', '')}
  {rotulo}
</div>"""
    corpo = f"""<div class='eyebrow'>Investimento no exterior</div>
<div class='h1' style='font-size:108px'>O dinheiro voltou. E o câmbio?</div>{visual}"""
    return capa("suave", corpo, 1, T)


def post_volta():
    T = 6
    s = [capa_volta(T)]

    # 2 · ida em três vezes, volta num dia (linha do tempo com as datas reais da conta de exemplo)
    W = 812
    marcos = [(2023 + (7 - 1 + 12 / 31) / 12, "12/07/23", D("4.90")), (2024 + (3 - 1 + 14 / 31) / 12, "14/03/24", D("5.00")),
              (2024 + (4 - 1 + 18 / 30) / 12, "18/04/24", D("5.10"))]
    volta = 2026 + (11 - 1 + 28 / 30) / 12
    t0, t1 = 2023.3, 2027.05
    xp = lambda t: (t - t0) / (t1 - t0) * W
    Y = 168                                   # altura da linha
    el = []
    # rótulos: 2023 em cima, a de março de 2024 embaixo, a de abril de 2024 em cima (as duas ficam a um mês)
    lados = ["cima", "baixo", "cima"]
    ancora = ["-30%", "-50%", "-35%"]
    for (t_, d_, cb), lado, anc in zip(marcos, lados, ancora):
        x = xp(t_)
        el.append(f"<i style='position:absolute;left:{x:.1f}px;top:{Y}px;width:20px;height:20px;border-radius:50%;background:{INK};border:4px solid #fff;box-shadow:0 0 0 2px {INK};transform:translate(-50%,-50%);display:block;z-index:2'></i>")
        topo = Y - 112 if lado == "cima" else Y + 26
        el.append(f"<div style='position:absolute;left:{x:.1f}px;top:{topo}px;transform:translateX({anc});text-align:center;white-space:nowrap'>"
                  f"<div class='big' style='font-size:34px'>R$ {numbr(cb)}</div><div style='font-size:22px;font-weight:600;color:{MUTED};margin-top:2px'>ida · {d_}</div></div>")
    xv = xp(volta)
    x_ult = xp(marcos[-1][0])
    el.append(f"<div style='position:absolute;left:{x_ult + 18:.1f}px;width:{xv - x_ult - 40:.1f}px;top:{Y - 2}px;height:0;border-top:4px dashed {BRAND}'></div>")
    el.append(f"<div style='position:absolute;left:{(x_ult + xv) / 2 - 40:.1f}px;top:{Y + 16}px;transform:translateX(-50%);font-size:24px;font-weight:700;color:{BRAND_DARK};white-space:nowrap'>lá fora</div>")
    el.append(f"<i style='position:absolute;left:{xv:.1f}px;top:{Y}px;width:40px;height:40px;border-radius:50%;background:{BRAND};border:7px solid #fff;box-shadow:0 0 0 3px {BRAND};transform:translate(-50%,-50%);display:block;z-index:2'></i>")
    el.append(f"<div style='position:absolute;left:{xv:.1f}px;top:{Y - 124}px;transform:translateX(-72%);text-align:center;white-space:nowrap'>"
              f"<div class='big' style='font-size:46px;color:{BRAND_DARK}'>R$ 5,02</div><div style='font-size:22px;font-weight:700;color:{BRAND_DARK};margin-top:2px'>volta · 28/11/26</div></div>")
    anos = ""
    linha_t = f"""<div style='position:relative;height:{Y + 96}px;width:{W}px'>
  <div style='position:absolute;left:0;right:0;top:{Y - 3}px;height:6px;border-radius:3px;background:{FIO}'></div>
  {anos}{''.join(el)}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Ida e volta</div>
<div class='h2'>Todo dólar tem dois câmbios.</div>
<div class='p' style='margin-top:24px'>O da ida, que você já pagou. E o da volta, que só se conhece no dia em que o dinheiro volta.</div>
<div class='visual' style='margin-top:44px'><div class='card' style='padding:30px 42px 20px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding-bottom:22px;border-bottom:2px solid {FIO}'>
    <span style='font-size:28px;font-weight:700;color:{INK}'>3 idas · câmbio médio <span style='font-variant-numeric:tabular-nums'>R$ 5,00</span></span>
    <span style='font-size:28px;font-weight:700;color:{BRAND_DARK}'>1 volta</span></div>
  <div style='margin-top:20px'>{linha_t}</div>
</div><div class='nota'>Exemplo: as remessas da conta fictícia dos nossos posts e um resgate de US$ 1.000.</div></div>""", 2, T))

    # 3 · o mesmo dólar volta valendo outro real (barras a partir do que custou na ida)
    meia = 170                                  # px para R$ 500
    def cen(cb, cor, cor_txt):
        recebe = RESG_USD * cb
        dif = recebe - CUSTO_1000
        sinal = "+" if dif >= 0 else MENOS
        w = float(abs(dif)) / 500 * meia
        lado = f"left:{meia:.0f}px" if dif >= 0 else f"left:{meia - w:.1f}px"
        return f"""<div style='display:flex;align-items:center;gap:26px;padding:24px 0;border-bottom:2px solid {FIO}'>
  <div style='width:190px;flex:none'><div style='font-size:22px;font-weight:700;letter-spacing:.1em;color:{MUTED}'>VOLTA A</div>
    <div class='big' style='font-size:48px;margin-top:2px'>R$ {numbr(cb)}</div></div>
  <div style='position:relative;width:{2 * meia}px;height:64px;flex:none'>
    <div style='position:absolute;{lado};top:8px;width:{max(w, 6):.1f}px;height:48px;border-radius:10px;background:{cor}'></div>
  </div>
  <div style='flex:1;text-align:right'><div class='big' style='font-size:44px'>{reais(recebe, 0)}</div>
    <div style='font-size:27px;font-weight:700;color:{cor_txt};margin-top:2px'>{sinal}{reais(abs(dif), 0)}</div></div></div>"""
    eixo = 44 + 190 + 26 + meia
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Na volta</div>
<div class='h2'>O mesmo dólar volta valendo outro real.</div>
<div class='p' style='margin-top:24px'>US$ 1.000 que foram a R$ 5,00 custaram R$ 5.000. Na volta, valem o câmbio do dia.</div>
<div class='visual' style='margin-top:36px'><div class='card' style='padding:4px 44px 24px;position:relative'>
  <div style='position:absolute;left:{eixo - 1.5:.1f}px;top:22px;height:{3 * 113 - 30}px;border-left:3px solid {INK}'></div>
  {''.join(cen(*c_) for c_ in CENARIOS)}
  <div style='display:flex;align-items:center;gap:14px;margin-top:22px;font-size:25px;font-weight:600;color:{MUTED}'>
    <i style='width:0;height:28px;border-left:3px solid {INK};display:block'></i>a linha é o custo na ida: R$ 5.000</div>
</div><div class='nota'>Exemplo ilustrativo: só o efeito do câmbio, sem o rendimento lá fora, sem IOF e sem tarifa.</div></div>""", 3, T))

    # 4 · tela real: Novo resgate preenchido, sem salvar (relógio em 28/11/2026)
    c = CX["28a"]
    rg = tela(P28, "celular-novo-resgate-preenchido.png")
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>O Resgate registra a volta.</div>
<div class='p' style='margin-top:18px;font-size:35px'>Em Remessas ao exterior: o que saiu lá fora, o que entrou na conta e o câmbio da volta, na hora. Teve IOF? Informe o do comprovante.</div>
<div class='visual' style='margin-top:40px'>{recorte(rg, px(c['resgatado'][1] - 4), px(c['deriva'][3] + 14), largura=720, x0=px(12), x1=px(378))}{NOTA_TELA}</div>""", 4, T))

    # 5 · tela real: o resgate na tabela e o aviso para atualizar a carteira (salvo só na sessão do navegador)
    c2 = CX["28b"]
    rm = tela(P28, "celular-remessas-com-resgate.png")
    cart = [x for x in c2["cartoes"] if x[1] == "rem-row saida"][0]
    cartao = recorte(rm, px(cart[2] - 2), px(cart[3] + 2), largura=640, x0=px(cart[4] - 4), x1=px(cart[5] + 4))
    aviso = recorte(rm, px(c2["aviso"][1] - 44), px(c2["aviso"][3] + 10), largura=640, x0=px(17), x1=px(373))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Depois da volta</div>
<div class='h3'>Atualize a carteira.</div>
<div class='p' style='margin-top:18px;font-size:35px'>O resgate entra na lista com o câmbio dele. Até você atualizar o valor da carteira, ele fica fora do ganho.</div>
<div class='visual' style='margin-top:40px'>{cartao}<div style='height:24px'></div>{aviso}{NOTA_TELA}</div>""", 5, T))

    s.append(fechamento_verde("Registre a ida e a volta.",
                              "Remessas ao exterior no timtimcash, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]


POSTS = {
    P16: post_iof,
    P19: post_fixo,
    P23: post_503020,
    P26: post_concentracao,
    P28: post_volta,
}

if __name__ == "__main__":
    so = sys.argv[1:] or None
    if so:
        so = [p for p in POSTS if any(p.startswith(x) or x in p for x in so)]
    renderizar(POSTS, so=so)
