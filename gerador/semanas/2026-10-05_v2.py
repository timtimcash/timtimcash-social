# -*- coding: utf-8 -*-
"""Semana de 5 a 9 de outubro de 2026, versão 2, com telas reais (substitui o piloto 2026-10-05.py).

Segunda 05, quarta 07 e sexta 09 substituem os posts do piloto, se aprovados.
Telas reais de gerador/telas/ (conta fictícia). Números conferidos com gerador/telas/LEIAME.md:
setembro de 2026 com receitas R$ 9.960,00, despesas R$ 7.780,00, sobra R$ 2.180,00 (21,9%);
média de 12 meses da receita guardada 14,4%; orçamentos Mercado 1.710/2.000, Bares 672/600 (112%).
"""
import os as _os
from artes import *

TELAS = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "telas")
def tela(nome):
    return "file://" + _os.path.join(TELAS, nome)

EXTRA = f"""<style>
.nota{{margin-top:18px;font-size:24px;font-weight:500;color:{MUTED}}}
.sombra{{box-shadow:0 1px 2px rgba(15,20,16,.05),0 22px 48px -22px rgba(15,20,16,.30)}}
.rot{{font-size:28px;font-weight:600;color:{MUTED}}}
.big{{font-weight:700;letter-spacing:-.04em;font-variant-numeric:tabular-nums;color:{INK}}}
</style>"""

def recorte(nome, larg_px, y0, y1, largura=760, x0=0, x1=None):
    """Recorte real de uma tela: mostra a faixa [y0, y1) (px da imagem original) na largura dada."""
    from PIL import Image
    w = Image.open(_os.path.join(TELAS, nome)).size[0]
    x1 = x1 or w
    esc = largura / (x1 - x0)
    alt = (y1 - y0) * esc
    return f"""<div class='sombra' style='width:{largura}px;height:{alt:.0f}px;overflow:hidden;border-radius:24px;background:#fff;border:1px solid {FIO};margin:0 auto'>
  <img src="{tela(nome)}" style='display:block;width:{w * esc:.1f}px;height:auto;margin-top:{-y0 * esc:.1f}px;margin-left:{-x0 * esc:.1f}px'></div>"""

NOTA_TELA = "<div class='nota' style='text-align:center'>Tela real do timtimcash, com dados de exemplo.</div>"

# ---------------------------------------------------------------- capas (cada uma com um fundo e um visual próprios)
DARK_BG = INK
DARK_TEXTO = "#C9D1C8"
EXTRA_CAPA = f"""<style>
.dark{{background:{DARK_BG};color:#fff}}
.dark .count,.dark .foot{{color:{DARK_TEXTO}}}
.dark .eyebrow{{color:{MENTA}}}
.soft{{background:{SOFT};color:{INK}}}
.soft .count,.soft .foot{{color:{BRAND_DEEP}}}
.soft .eyebrow{{color:{BRAND_DEEP}}}
</style>"""

def capa_page(tema, corpo, idx, total, logo_var):
    head = f"<div class='head'><div class='brand'>{logo_horizontal(logo_var, 44)}</div><div class='count'>{idx}/{total}</div></div>"
    return page(EXTRA + EXTRA_CAPA + head + f"<div class='body'>{corpo}</div>" + footer(), tema)

def capa_poupanca(T):
    r, sw = 190, 46
    c = 2 * 3.14159265 * r
    arco = c * 0.219
    donut = f"""<svg width="470" height="470" viewBox="0 0 470 470">
  <circle cx="235" cy="235" r="{r}" fill="none" stroke="{FIO}" stroke-width="{sw}"/>
  <circle cx="235" cy="235" r="{r}" fill="none" stroke="{BRAND}" stroke-width="{sw}" stroke-linecap="round"
    stroke-dasharray="{arco:.1f} {c:.1f}" transform="rotate(-90 235 235)"/>
  <text x="235" y="250" text-anchor="middle" font-family="Inter" font-weight="700" font-size="104" letter-spacing="-4" fill="{INK}">21,9%</text>
  <text x="235" y="310" text-anchor="middle" font-family="Inter" font-weight="600" font-size="30" fill="{MUTED}">ficou com você</text>
</svg>"""
    corpo = f"""<div class='eyebrow'>Taxa de poupança</div>
<div class='h2' style='font-size:92px'>Quanto do seu salário fica com você?</div>
<div style='display:flex;justify-content:center;margin-top:56px'>{donut}</div>"""
    return capa_page("light", corpo, 1, T, "color")

def capa_orcamentos(T):
    corpo = f"""<div class='eyebrow'>Orçamentos</div>
<div class='h2' style='font-size:92px'>Qual limite pôr em cada gasto?</div>
<div class='visual' style='margin-top:48px'>{recorte('secoes/celular-orcamentos-progresso.jpg', 1086, 730, 1590, largura=800, x0=20, x1=1066)}
<div class='nota' style='text-align:center'>Tela real do timtimcash, com dados de exemplo.</div></div>"""
    return capa_page("light", corpo, 1, T, "color")

def capa_cambio(T):
    lo, hi = 4.20, 5.80
    pos = lambda v: (v - lo) / (hi - lo) * 100
    regua = f"""<div style='position:relative;height:150px;margin-top:70px'>
  <div style='position:absolute;left:0;right:0;top:60px;height:24px;border-radius:12px;background:linear-gradient(90deg,#7A2E2E 0,#7A2E2E {pos(EQ):.1f}%,{BRAND_DARK} {pos(EQ):.1f}%,{BRAND_DARK} 100%)'></div>
  <i style='position:absolute;left:{pos(EQ):.1f}%;top:40px;width:8px;height:64px;border-radius:4px;background:#F19A9A;transform:translateX(-50%);display:block'></i>
  <i style='position:absolute;left:{pos(HOJE):.1f}%;top:72px;width:46px;height:46px;border-radius:50%;background:#fff;border:10px solid {MENTA};transform:translate(-50%,-50%);display:block;box-sizing:border-box'></i>
  <div style='position:absolute;left:{pos(EQ):.1f}%;top:112px;transform:translateX(-50%);font-size:28px;font-weight:600;color:#F19A9A;white-space:nowrap'>aqui vira prejuízo</div>
  <div style='position:absolute;left:{pos(HOJE):.1f}%;top:112px;transform:translateX(-50%);font-size:28px;font-weight:600;color:{MENTA};white-space:nowrap'>hoje</div>
</div>"""
    corpo = f"""<div class='eyebrow'>Investimento no exterior</div>
<div class='h1' style='font-size:112px'>Com qual dólar você começa a perder?</div>
<div style='margin-top:52px;font-size:190px;font-weight:700;letter-spacing:-.05em;line-height:1;color:{MENTA};font-variant-numeric:tabular-nums'>R$ 4,55<span style='color:#fff'>?</span></div>{regua}"""
    return capa_page("dark", corpo, 1, T, "dark")

def capa_susto(T):
    corpo = f"""<div class='eyebrow'>Simulação futura</div>
<div class='h2' style='font-size:92px'>E se a maior renda parasse por 6 meses?</div>
<div class='visual' style='margin-top:52px'>{recorte('secoes/celular-simulacao-e-se-perde-a-maior-renda.jpg', 1086, 395, 1060, largura=800, x0=30, x1=1060)}
<div class='nota' style='text-align:center'>Tela real do timtimcash, com dados de exemplo.</div></div>"""
    return capa_page("light", corpo, 1, T, "color")

def capa_dados(T):
    I_LOCK2 = '<rect x="5" y="11" width="14" height="9.5" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'
    I_EYEOFF = '<path d="M3 3l18 18"/><path d="M10.6 5.2A9.9 9.9 0 0 1 12 5c5 0 8.5 4.5 9.5 7-.4 1-1.2 2.3-2.4 3.5M6.4 6.5C4.6 7.8 3.2 9.8 2.5 12c1 2.5 4.5 7 9.5 7 1.8 0 3.4-.6 4.8-1.4"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>'
    I_DOWN = '<path d="M12 4v11"/><path d="M7 10.5 12 15.5l5-5"/><path d="M5 20h14"/>'
    def tile(ip, rot):
        return f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:22px'>
  <div style='width:230px;height:230px;border-radius:28%;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 2px rgba(15,20,16,.05),0 22px 44px -24px rgba(6,95,70,.45)'>
    <svg width='112' height='112' viewBox='0 0 24 24' fill='none' stroke='{BRAND_DARK}' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'>{ip}</svg></div>
  <div style='font-size:32px;font-weight:700;color:{BRAND_DEEP}'>{rot}</div></div>"""
    corpo = f"""<div style='display:flex;gap:26px'>{tile(I_LOCK2, 'entrada')}{tile(I_EYEOFF, 'dia a dia')}{tile(I_DOWN, 'saída')}</div>
<div class='eyebrow' style='margin-top:84px'>Seus dados</div>
<div class='h1' style='font-size:118px'>Entram por você. Saem com você.</div>"""
    return capa_page("soft", corpo, 1, T, "color")

# ================================================================ segunda 05/10 · educação
def post_poupanca():
    T = 6
    s = []
    s.append(capa_poupanca(T))

    conta = f"""<div class='visual'><div class='card' style='padding:44px 48px'>
  <div style='display:flex;align-items:flex-end;justify-content:space-between;gap:20px'>
    <div><div class='rot'>Sobrou no mês</div><div class='big' style='font-size:64px;margin-top:6px'>R$ 2.180</div></div>
    <div class='big' style='font-size:64px;color:{MUTED}'>÷</div>
    <div><div class='rot'>Entrou no mês</div><div class='big' style='font-size:64px;margin-top:6px'>R$ 9.960</div></div>
  </div>
  <div style='height:2px;background:{FIO};margin:34px 0 28px'></div>
  <div style='display:flex;align-items:center;justify-content:space-between'>
    <div class='rot'>Taxa de poupança</div><div class='big' style='font-size:84px;color:{BRAND_DARK}'>21,9%</div>
  </div>
</div><div class='nota'>Exemplo: receitas de R$ 9.960 e despesas de R$ 7.780 no mês.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta</div>
<div class='h2'>O que sobrou, dividido pelo que entrou.</div>
<div class='p'>O resultado é o pedaço da renda que ficou com você.</div>{conta}""", 2, T))

    def cartao(renda, pct):
        return f"""<div class='card' style='flex:1;padding:36px 36px 38px'>
  <div class='rot'>Ganha</div><div class='big' style='font-size:52px;margin-top:4px'>R$ {renda}</div>
  <div class='rot' style='margin-top:22px'>Sobra</div><div class='big' style='font-size:52px;margin-top:4px'>R$ 1.000</div>
  <div style='height:2px;background:{FIO};margin:26px 0 20px'></div>
  <div class='big' style='font-size:76px;color:{BRAND_DARK}'>{pct}</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Por que em porcentagem</div>
<div class='h2'>A mesma sobra pode ser muito ou pouco.</div>
<div class='p'>R$ 1.000 guardados pesam diferente para cada renda. A porcentagem deixa comparar.</div>
<div class='visual' style='display:flex;gap:24px'>{cartao('4.000', '25%')}{cartao('20.000', '5%')}</div>""", 3, T))

    def barra(rot, pct, cor, forte=False):
        return f"""<div style='margin-top:34px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'><span style='font-size:32px;font-weight:{700 if forte else 600};color:{INK}'>{rot}</span>
  <span class='big' style='font-size:48px;color:{BRAND_DARK if forte else INK}'>{pct}%</span></div>
  <div style='height:26px;border-radius:13px;background:{FIO};margin-top:14px;overflow:hidden'><div style='height:100%;width:{float(pct.replace(",", ".")) / 30 * 100:.1f}%;background:{cor};border-radius:13px'></div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Compare com você</div>
<div class='h2'>O padrão que importa é o seu.</div>
<div class='p'>Um mês bom não faz tendência. Compare com a sua média dos últimos meses para ver a direção.</div>
<div class='visual'><div class='card' style='padding:14px 48px 46px'>{barra('Sua média de 12 meses', '14,4', NEUTRO)}{barra('Setembro', '21,9', BRAND, True)}</div>
<div class='nota'>Exemplo com a mesma conta dos slides anteriores.</div></div>""", 4, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>O Diagnóstico faz essa conta sozinho.</div>
<div class='p' style='margin-top:20px;font-size:36px'>Mostra quanto você guardou, compara com a sua média e aponta o maior desvio. A meta começa em 20% e você ajusta.</div>
<div class='visual' style='margin-top:40px'>{recorte('secoes/celular-relatorios-diagnostico.jpg', 1086, 585, 1275)}{NOTA_TELA}</div>""", 5, T))

    s.append(slide("green", EXTRA + f"""
<div class='h2'>Descubra quanto da sua renda fica com você.</div>
<div class='lead'>Relatórios no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.</div>{v_cta_pill()}""", 6, T))
    return s

# ================================================================ terça 06/10 · produto
def post_orcamentos():
    T = 5
    s = []
    s.append(capa_orcamentos(T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Onde definir limite primeiro</div>
<div class='h3'>O ponto de partida vem do seu histórico.</div>
<div class='p' style='margin-top:20px;font-size:36px'>O timtimcash mostra onde ainda falta limite e sugere um valor pela sua média de gastos.</div>
<div class='visual' style='margin-top:44px'>{recorte('biblioteca/celular-orcamentos.jpg', 1170, 1770, 2215, largura=860, x0=40, x1=1130)}{NOTA_TELA}</div>""", 2, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Progresso por categoria</div>
<div class='h3'>O que pede atenção aparece primeiro.</div>
<div class='p' style='margin-top:20px;font-size:36px'>Cada categoria entra numa faixa, e cada linha diz onde fecha no ritmo atual.</div>
<div class='visual' style='margin-top:40px'>{recorte('secoes/celular-orcamentos-progresso.jpg', 1086, 588, 1600, largura=600)}{NOTA_TELA}</div>""", 3, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O mês inteiro</div>
<div class='h3'>No topo, quanto já foi e quanto ainda cabe.</div>
<div class='p' style='margin-top:20px;font-size:36px'>O limite usado ao lado do período que já passou, para comparar o ritmo num olhar.</div>
<div class='visual' style='margin-top:40px'>{recorte('biblioteca/celular-orcamentos.jpg', 1170, 790, 1690, largura=700, x0=45, x1=1125)}{NOTA_TELA}</div>""", 4, T))

    s.append(slide("green", EXTRA + f"""
<div class='h2'>Um limite que cabe na sua vida real.</div>
<div class='lead'>Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.</div>{v_cta_pill()}""", 5, T))
    return s

# ================================================================ quarta 07/10 · educação (exterior)
# Exemplo da conta fictícia: R$ 60.000 enviados, carteira de US$ 13.200, câmbio médio R$ 5,00, PTAX R$ 5,50.
ENVIADO, US_HOJE, MEDIO, HOJE = 60000, 13200, 5.00, 5.50
EQ = ENVIADO / US_HOJE
assert abs(EQ - 4.5455) < 0.0001
FOLGA = (HOJE - EQ) / HOJE  # 17,4%
assert 0.173 < FOLGA < 0.175

def v_regua():
    lo, hi = 4.20, 5.80
    pos = lambda v: (v - lo) / (hi - lo) * 100
    def marca(v, rot, sub, cor, cheio=True, acima=False):
        bola = f"background:{cor}" if cheio else f"background:#fff;border:6px solid {cor}"
        txt = f"<div style='position:absolute;left:{pos(v):.1f}%;{'bottom:calc(50% + 30px)' if acima else 'top:calc(50% + 30px)'};transform:translateX(-50%);text-align:center;white-space:nowrap'><div class='big' style='font-size:38px'>{rot}</div><div class='rot' style='font-size:24px'>{sub}</div></div>"
        return f"<i style='position:absolute;left:{pos(v):.1f}%;top:50%;width:40px;height:40px;border-radius:50%;{bola};transform:translate(-50%,-50%);display:block;box-sizing:border-box'></i>{txt}"
    return f"""<div class='visual'><div class='card' style='padding:40px 56px'>
  <div style='position:relative;height:260px'>
    <div style='position:absolute;left:0;right:0;top:50%;height:26px;transform:translateY(-50%);border-radius:13px;background:linear-gradient(90deg,#F6DCDC 0,#F6DCDC {pos(EQ):.1f}%,{SOFT} {pos(EQ):.1f}%,{SOFT} 100%)'></div>
    <i style='position:absolute;left:{pos(EQ):.1f}%;top:50%;width:6px;height:64px;background:{RED};transform:translate(-50%,-50%);display:block;border-radius:3px'></i>
    <div style='position:absolute;left:{pos(EQ):.1f}%;top:calc(50% + 40px);transform:translateX(-50%);text-align:center;white-space:nowrap'><div class='big' style='font-size:38px;color:{RED_TEXT}'>R$ 4,55</div><div class='rot' style='font-size:24px'>equilíbrio</div></div>
    {marca(MEDIO, 'R$ 5,00', 'seu câmbio médio', MUTED, cheio=False, acima=True)}
    {marca(HOJE, 'R$ 5,50', 'hoje', BRAND_DARK, acima=True)}
  </div>
  <div style='display:flex;justify-content:space-between;font-size:26px;font-weight:600;margin-top:6px'><span style='color:{RED_TEXT}'>prejuízo em reais</span><span style='color:{BRAND_DEEP}'>lucro em reais</span></div>
</div></div>"""

def post_cambio():
    T = 7
    s = []
    s.append(capa_cambio(T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O que é</div>
<div class='h2'>O câmbio que zera o seu resultado em reais.</div>
<div class='p'>Acima dele, você ganha em reais. Abaixo, perde, mesmo que a carteira tenha rendido em dólar.</div>
<div class='visual' style='display:flex;gap:24px'>
  <div class='card' style='flex:1;padding:36px 36px;background:#FBEAEA;border-color:#FBEAEA'><div class='rot' style='color:{RED_TEXT}'>Dólar abaixo</div><div class='big' style='font-size:52px;margin-top:8px;color:{RED_TEXT}'>prejuízo</div></div>
  <div class='card' style='flex:1;padding:36px 36px;background:{SOFT};border-color:{SOFT}'><div class='rot' style='color:{BRAND_DEEP}'>Dólar acima</div><div class='big' style='font-size:52px;margin-top:8px;color:{BRAND_DEEP}'>lucro</div></div>
</div>""", 2, T))

    conta = f"""<div class='visual'><div class='card' style='padding:44px 48px'>
  <div style='display:flex;align-items:flex-end;justify-content:space-between;gap:20px'>
    <div><div class='rot'>Você mandou</div><div class='big' style='font-size:62px;margin-top:6px'>R$ 60.000</div></div>
    <div class='big' style='font-size:62px;color:{MUTED}'>÷</div>
    <div><div class='rot'>Tem hoje lá fora</div><div class='big' style='font-size:62px;margin-top:6px'>US$ 13.200</div></div>
  </div>
  <div style='height:2px;background:{FIO};margin:34px 0 28px'></div>
  <div style='display:flex;align-items:center;justify-content:space-between'>
    <div class='rot'>Câmbio de equilíbrio</div><div class='big' style='font-size:84px;color:{BRAND_DARK}'>R$ 4,55</div>
  </div>
</div><div class='nota'>Exemplo: 3 remessas somando R$ 60.000 (US$ 12.000), que renderam até US$ 13.200. Sem IOF e tarifas.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta</div>
<div class='h2'>Reais que você mandou, divididos pelos dólares de hoje.</div>{conta}""", 3, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A sua folga</div>
<div class='h2'>Quanto o dólar pode cair antes de doer.</div>
<div class='p'>No exemplo, o dólar teria de cair cerca de 17%, de R$ 5,50 para R$ 4,55, para o resultado em reais zerar.</div>{v_regua()}""", 4, T))

    def linha(titulo, efeito, cor, ultimo=False):
        return f"""<div style='display:flex;align-items:center;justify-content:space-between;gap:24px;padding:34px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div style='font-size:36px;font-weight:600;line-height:1.25;color:{INK};max-width:560px'>{titulo}</div>
  <div style='flex:none;font-size:32px;font-weight:700;color:{cor}'>{efeito}</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Ele se move</div>
<div class='h2'>O equilíbrio muda com o tempo.</div>
<div class='p'>Não é um número fixo. Vale olhar de novo a cada remessa e a cada atualização da carteira.</div>
<div class='visual'><div class='card' style='padding:6px 48px'>
  {linha('A carteira rendeu em dólar', 'equilíbrio desce', BRAND_DARK)}
  {linha('Nova remessa com o dólar acima do seu equilíbrio', 'equilíbrio sobe', RED_TEXT, True)}
</div></div>""", 5, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Remessas ao exterior</div>
<div class='h3'>O timtimcash acha o seu equilíbrio.</div>
<div class='p' style='margin-top:20px;font-size:36px'>O equilíbrio, o seu câmbio médio e o de hoje, com a PTAX do Banco Central.</div>
<div class='visual' style='margin-top:40px'>{recorte('secoes/celular-remessas-cambio-equilibrio.jpg', 1086, 0, 1089, largura=560)}{NOTA_TELA}</div>""", 6, T))

    s.append(slide("green", EXTRA + f"""
<div class='h2'>Saiba com qual dólar o seu dinheiro lá fora empata.</div>
<div class='lead'>Remessas ao exterior no timtimcash. No computador ou no celular.</div>{v_cta_pill()}""", 7, T))
    return s

# ================================================================ quinta 08/10 · produto (simulação)
def post_susto():
    T = 5
    s = []
    s.append(capa_susto(T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>E se...</div>
<div class='h3'>Um toque aplica o susto sobre o seu cenário, sem alterar nada.</div>
<div class='p' style='margin-top:20px;font-size:36px'>No exemplo, “Perde a maior renda”: a maior receita zera nos 6 primeiros meses.</div>
<div class='visual' style='margin-top:40px'>{recorte('secoes/celular-simulacao-e-se-perde-a-maior-renda.jpg', 1086, 1110, 1905, largura=720)}{NOTA_TELA}</div>""", 2, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O impacto</div>
<div class='h3'>A linha tracejada é o seu saldo com o susto.</div>
<div class='p' style='margin-top:20px;font-size:36px'>Em vez de chegar a R$ 37.720 em set/27, o saldo termina em −R$ 22.040.</div>
<div class='visual' style='margin-top:36px'>{recorte('secoes/celular-simulacao-e-se-perde-a-maior-renda.jpg', 1086, 0, 1070, largura=580)}{NOTA_TELA}</div>""", 3, T))

    I_SHIELD = '<path d="M12 3.5 19 6v5.5c0 4.3-2.9 7.6-7 9-4.1-1.4-7-4.7-7-9V6z"/>'
    I_CUT = '<circle cx="6.5" cy="7" r="2.5"/><circle cx="6.5" cy="17" r="2.5"/><path d="M8.6 8.4 20 17M8.6 15.6 20 7"/>'
    I_LAYERS = '<path d="M12 4 3.5 8.5 12 13l8.5-4.5z"/><path d="M3.5 12.5 12 17l8.5-4.5"/><path d="M3.5 16.5 12 21l8.5-4.5"/>'
    def item(ip, t, sub, ultimo=False):
        icone = f"<div class='azulejo' style='width:84px;height:84px;flex:none'><svg width='42' height='42' viewBox='0 0 24 24' fill='none' stroke='{BRAND_DARK}' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>{ip}</svg></div>"
        return f"""<div style='display:flex;gap:30px;align-items:center;padding:30px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>{icone}
  <div><div style='font-size:38px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{t}</div><div style='font-size:28px;color:{MUTED};margin-top:8px;line-height:1.3'>{sub}</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>E agora?</div>
<div class='h2'>Com o número na mão, o plano fica concreto.</div>
<div class='visual' style='margin-top:48px'><div class='card' style='padding:6px 44px'>
  {item(I_SHIELD, 'Quanto de reserva seria preciso', 'O tamanho do buraco já aparece no gráfico.')}
  {item(I_CUT, 'Que despesa ajustar primeiro', 'Mude o cenário e veja a linha subir.')}
  {item(I_LAYERS, 'Qual plano aguenta melhor', 'Compare até 5 cenários lado a lado.', True)}
</div></div>""", 4, T))

    s.append(slide("green", EXTRA + f"""
<div class='h2'>Descubra quanto tempo o seu plano aguenta.</div>
<div class='lead'>Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.</div>{v_cta_pill()}""", 5, T))
    return s

# ================================================================ sexta 09/10 · posicionamento
def post_dados():
    T = 5
    I_LOCK2 = '<rect x="5" y="11" width="14" height="9.5" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'
    I_EYEOFF = '<path d="M3 3l18 18"/><path d="M10.6 5.2A9.9 9.9 0 0 1 12 5c5 0 8.5 4.5 9.5 7-.4 1-1.2 2.3-2.4 3.5M6.4 6.5C4.6 7.8 3.2 9.8 2.5 12c1 2.5 4.5 7 9.5 7 1.8 0 3.4-.6 4.8-1.4"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>'
    I_DOWN = '<path d="M12 4v11"/><path d="M7 10.5 12 15.5l5-5"/><path d="M5 20h14"/>'
    def chips(itens):
        return "<div class='visual' style='display:flex;gap:18px;flex-wrap:wrap'>" + "".join(f"<span class='chip'>{t}</span>" for t in itens) + "</div>"
    def az(ip):
        return f"<div class='azulejo' style='width:120px;height:120px;margin-bottom:44px'><svg width='60' height='60' viewBox='0 0 24 24' fill='none' stroke='{BRAND_DARK}' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>{ip}</svg></div>"
    s = []
    s.append(capa_dados(T))
    s.append(slide("light", EXTRA + f"""{az(I_LOCK2)}
<div class='eyebrow'>Na entrada</div>
<div class='h2'>Nada de senha do banco.</div>
<div class='p'>O timtimcash não se conecta à sua conta. Você lança à mão ou importa o extrato do banco ou a sua planilha.</div>
{chips(['Lançar à mão', '.ofx', '.xlsx', '.csv'])}""", 2, T))
    mascara = f"""<div class='visual'><div class='card' style='padding:36px 44px;display:flex;align-items:center;justify-content:space-between'>
  <div><div class='rot'>Patrimônio</div><div class='big' style='font-size:64px;margin-top:6px;letter-spacing:.08em'>R$ •••••</div></div>
  <div class='azulejo' style='width:84px;height:84px'><svg width='42' height='42' viewBox='0 0 24 24' fill='none' stroke='{BRAND_DARK}' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>{I_EYEOFF}</svg></div>
</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No dia a dia</div>
<div class='h2'>Sem propaganda na tela.</div>
<div class='p'>Os dados são criptografados no envio e no armazenamento. E “Ocultar valores” esconde os números quando você abre as finanças em público.</div>{mascara}""", 3, T))
    s.append(slide("light", EXTRA + f"""{az(I_DOWN)}
<div class='eyebrow'>Na saída</div>
<div class='h2'>Quer levar tudo? Exporte.</div>
<div class='p'>As transações em Excel, PDF ou CSV. E o backup completo, em Preferências.</div>
{chips(['Excel', 'PDF', 'CSV', 'Backup completo'])}""", 4, T))
    head = f"<div class='head'><div></div><div class='count'>{T}/{T}</div></div>"
    corpo = f"""
<div style='margin-bottom:52px'>{logo_vertical('white', 170)}</div>
<div class='h2'>Seu dinheiro. Suas regras.</div>
<div class='lead'>Gratuito para o controle financeiro. No computador ou no celular.</div>{v_cta_pill()}"""
    s.append(page(EXTRA + head + f"<div class='body'>{corpo}</div>" + footer(last=True), "green"))
    return s

POSTS = {
    "2026-10-05_quanto-fica-com-voce": post_poupanca,
    "2026-10-06_orcamento-pela-sua-media": post_orcamentos,
    "2026-10-07_cambio-de-equilibrio": post_cambio,
    "2026-10-08_e-se-a-maior-renda-parar": post_susto,
    "2026-10-09_seus-dados-entram-e-saem-com-voce": post_dados,
}
