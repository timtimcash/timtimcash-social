# -*- coding: utf-8 -*-
"""Post de apresentação para fixar no topo do perfil: "Comece por aqui" (carrossel de 8).

Aprovado e publicado em 30/09/2026. Slides 2, 4, 5 e 6 com telas reais do timtimcash (conta fictícia).

Atemporal: nada de datas, "hoje" só dentro das maquetes. Todos os valores são de exemplo e coerentes
com os posts da semana de 28/09/2026 (receitas R$ 9.960, despesas R$ 7.780, saldo do mês +R$ 2.180).
"""
from artes import *

# ---------------------------------------------------------------- estilos extras
EXTRA = f"""<style>
.tag{{display:inline-flex;align-items:center;height:40px;padding:0 18px;border-radius:999px;background:{SOFT};color:{BRAND_DEEP};font-size:22px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}}
.nota{{margin-top:22px;font-size:24px;font-weight:500;color:{MUTED}}}
.rot{{font-size:26px;font-weight:600;color:{MUTED}}}
.val{{font-weight:600;font-variant-numeric:tabular-nums;letter-spacing:-.02em;color:{INK}}}
.val .rs{{font-size:.55em;font-weight:500;margin-right:6px;color:{MUTED}}}
.val .ct{{font-size:.55em;font-weight:500;color:{MUTED}}}
.linha{{display:flex;align-items:center;gap:22px;padding:18px 0;border-bottom:1px solid {FIO}}}
.linha:last-child{{border-bottom:none}}
.selo{{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 16px;border-radius:999px;font-size:23px;font-weight:700}}
.selo.ok{{background:{SOFT};color:{BRAND_DEEP}}}
.selo.amb{{background:#FBF1DC;color:{AMBER_TEXT}}}
.trilho{{height:20px;border-radius:10px;background:{FIO};overflow:hidden}}
.trilho > i{{display:block;height:100%;border-radius:10px}}
.sombra{{box-shadow:0 1px 2px rgba(15,20,16,.05),0 22px 48px -22px rgba(15,20,16,.30)}}
</style>"""

def _fmt(v, casas=2):
    s = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s

def brl(v, sinal=False, centavos=True):
    s = _fmt(v)
    inteiro, cent = s.split(",")
    pre = ""
    if sinal:
        pre = "+" if v > 0 else ("−" if v < 0 else "")
    ct = f"<span class='ct'>,{cent}</span>" if centavos else ""
    return f"<span class='val'>{pre}<span class='rs'>R$</span>{inteiro}{ct}</span>"

def usd(v, centavos=True):
    s = _fmt(v)
    inteiro, cent = s.split(",")
    ct = f"<span class='ct'>,{cent}</span>" if centavos else ""
    return f"<span class='val'><span class='rs'>US$</span>{inteiro}{ct}</span>"

def verde(html):
    """Valor em verde escuro (texto verde do manual)."""
    return html.replace("class='val'", f"class='val' style='color:{BRAND_DARK}'", 1)

def ic(path, size=34, cor=BRAND_DARK, sw=2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

def azul(path, size=64, isz=32, fundo=None):
    estilo = f"width:{size}px;height:{size}px;flex:none" + (f";background:{fundo}" if fundo else "")
    return f"<div class='azulejo' style='{estilo}'>{ic(path, isz)}</div>"

# ícones de traço, grade de 24
I_CHECK = '<path d="M20 6 9 17l-5-5"/>'
I_PIE = '<path d="M20.5 13.5A8.5 8.5 0 1 1 10.5 3.5V13.5z"/><path d="M14 3.2a8.5 8.5 0 0 1 6.8 6.8H14z"/>'
I_WALLET = '<path d="M18 8V6.5A1.5 1.5 0 0 0 16.5 5h-10A2.5 2.5 0 0 0 4 7.5"/><rect x="4" y="8" width="16.5" height="11.5" rx="2.5"/><path d="M16 14h1.5"/>'
I_TREND = '<path d="M3.5 17.5 9 12l4 4 7.5-8"/><path d="M15 8h5.5v5.5"/>'
I_GLOBE = '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17"/><path d="M12 3.5c2.4 2.6 3.5 5.4 3.5 8.5s-1.1 5.9-3.5 8.5c-2.4-2.6-3.5-5.4-3.5-8.5s1.1-5.9 3.5-8.5z"/>'
I_LOCK = '<rect x="5" y="11" width="14" height="9.5" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'
I_FILE = '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>'
I_UP = '<path d="M7 17 17 7"/><path d="M8 7h9v9"/>'
I_HOME = '<path d="M3.5 10.5 12 4l8.5 6.5"/><path d="M5.5 9v10.5h13V9"/><path d="M10 19.5v-5h4v5"/>'
I_CART = '<path d="M3 4h2.5l2.2 10.5h10.3l2-7.5H6.4"/><circle cx="9.5" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>'
I_PLUS = '<path d="M12 5v14M5 12h14"/>'
I_BOOK = '<path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5z"/><path d="M20 5.5A1.5 1.5 0 0 0 18.5 4H13v16h5.5a1.5 1.5 0 0 0 1.5-1.5z"/>'
I_BOLT = '<path d="M13 3 5 13h6l-1 8 8-10h-6z"/>'
I_EYEOFF = '<path d="M3 3l18 18"/><path d="M10.6 5.2A9.9 9.9 0 0 1 12 5c5 0 8.5 4.5 9.5 7-.4 1-1.2 2.3-2.4 3.5M6.4 6.5C4.6 7.8 3.2 9.8 2.5 12c1 2.5 4.5 7 9.5 7 1.8 0 3.4-.6 4.8-1.4"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>'

SETA = ARROW  # seta oficial do gerador (30 px)

# Telas reais do timtimcash, capturadas numa conta fictícia (dados de exemplo)
import os as _os
# banco de telas reais do repositório: gerador/telas (conta fictícia, sem dado real)
TELAS = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "telas")
def tela(nome):
    return "file://" + _os.path.join(TELAS, nome)

I_SINAL = '<path d="M3 17h2v3H3zM8 14h2v6H8zM13 11h2v9h-2zM18 8h2v12h-2z" fill="currentColor" stroke="none"/>'
I_WIFI = '<path d="M2.5 9.5a14 14 0 0 1 19 0M5.8 13a9.2 9.2 0 0 1 12.4 0M9.1 16.5a4.5 4.5 0 0 1 5.8 0"/><circle cx="12" cy="19.6" r="1.3" fill="currentColor" stroke="none"/>'
I_BATERIA = '<rect x="2" y="7" width="18" height="10" rx="2.6"/><rect x="4" y="9" width="12.5" height="6" rx="1.2" fill="currentColor" stroke="none"/><path d="M22 10.5v3"/>'


# ================================================================= 1 · capa
INDICE = [(2, "O que é"), (3, "O que ele responde"), (4, "Seu dinheiro lá fora"),
          (5, "Sua planilha vem junto"), (6, "Sem senha do banco"), (7, "Como começar")]

def v_indice():
    linhas = "".join(f"""<div style='display:flex;align-items:center;gap:26px;padding:14px 0;{'' if i == len(INDICE) - 1 else f'border-bottom:1px solid {FIO};'}'>
  <span class='num' style='width:44px;font-size:32px;font-weight:700;color:{BRAND_DARK}'>{n}</span>
  <span style='flex:1;font-size:34px;font-weight:600;letter-spacing:-.02em;color:{INK}'>{t}</span>
  <span style='color:{BRAND}'>{SETA}</span></div>""" for i, (n, t) in enumerate(INDICE))
    return f"<div class='visual' style='margin-top:48px'><div class='card' style='padding:10px 40px'>{linhas}</div></div>"

def capa():
    return slide("green", EXTRA + f"""
<div class='eyebrow'>Boas-vindas</div>
<div class='h1' style='font-size:140px;line-height:.95;letter-spacing:-.05em'>Comece<br>por aqui.</div>
<div class='lead' style='max-width:840px'>O que é o timtimcash, o que ele tem de diferente e como começar.</div>{v_indice()}""", 1, 8)

# ================================================================= 2 · o que é
def v_telas():
    pontos = "".join(f"<i style='width:12px;height:12px;border-radius:50%;background:{NEUTRO};display:block'></i>" for _ in range(3))
    navegador = f"""<div class='sombra' style='position:absolute;left:0;top:68px;width:600px;border-radius:20px;background:#fff;border:1px solid {FIO};overflow:hidden'>
  <div style='height:42px;display:flex;align-items:center;gap:8px;padding:0 16px;background:{BG};border-bottom:1px solid {FIO}'>{pontos}
    <div style='margin-left:12px;width:280px;height:28px;border-radius:999px;background:#fff;border:1px solid {FIO};display:flex;align-items:center;gap:8px;padding:0 13px;font-size:16px;font-weight:600;color:{INK}'>{ic(I_LOCK, 14, MUTED, 2.2)}timtimcash.com</div>
  </div>
  <img src="{tela('desktop.png')}" style='display:block;width:600px;height:auto'>
</div>"""
    barra_status = f"""<div style='height:30px;display:flex;align-items:center;justify-content:space-between;padding:0 20px 0 24px;font-size:14px;font-weight:600;color:{INK};background:{BG}'>
  <span class='num'>10:00</span><span style='display:flex;gap:5px;align-items:center'>{ic(I_SINAL, 15, INK, 0)}{ic(I_WIFI, 15, INK, 2.2)}{ic(I_BATERIA, 20, INK, 1.6)}</span></div>"""
    barra_url = f"""<div style='height:46px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;background:{BG};border-top:1px solid {FIO}'>
  <span style='display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 14px;border-radius:999px;background:#fff;border:1px solid {FIO};font-size:13px;font-weight:600;color:{INK}'>{ic(I_LOCK, 11, MUTED, 2.4)}timtimcash.com</span>
  <i style='width:92px;height:4px;border-radius:2px;background:{INK};display:block'></i></div>"""
    celular = f"""<div class='sombra' style='position:absolute;right:0;top:0;width:262px;border-radius:42px;background:{INK};padding:11px'>
  <div style='border-radius:36px;overflow:hidden;background:{BG}'>{barra_status}<img src="{tela('movel.png')}" style='display:block;width:240px;height:auto'>{barra_url}</div>
</div>"""
    return f"""<div class='visual' style='position:relative;height:556px;margin-top:38px'>{navegador}{celular}</div>
<div class='nota' style='margin-top:18px'>Telas reais do timtimcash, com dados de exemplo.</div>"""

def o_que_e():
    return slide("light", EXTRA + f"""
<div class='eyebrow'>O que é</div>
<div class='h2'>Um site que organiza o seu dinheiro.</div>
<div class='p' style='margin-top:24px'>Você lança ou importa o que entra e sai. Ele organiza, calcula e mostra.</div>{v_telas()}""", 2, 8)

# ================================================================= 3 · o que ele responde
def v_perguntas():
    itens = [(I_PIE, "Para onde o dinheiro está indo?", "Categorias, orçamentos e relatórios", False),
             (I_WALLET, "Quanto sobra no fim do mês?", "Visão geral, pendentes e comparação", False),
             (I_TREND, "Como vão ser os próximos meses?", "Simulação de fluxo futuro, até 5 anos à frente", False),
             (I_GLOBE, "Quanto rendeu lá fora, em reais?", "Remessas e investimentos no exterior", True)]
    cards = ""
    for p, q, f, dest in itens:
        fundo = f"background:{SOFT};border-color:{SOFT};" if dest else ""
        cor_f = BRAND_DEEP if dest else MUTED
        cards += f"""<div class='card' style='{fundo}padding:30px 30px 32px;display:flex;flex-direction:column'>
  {azul(p, 72, 40, '#fff' if dest else None)}
  <div style='margin-top:24px;font-size:39px;font-weight:700;line-height:1.1;letter-spacing:-.035em;color:{INK}'>{q}</div>
  <div style='margin-top:16px;font-size:27px;font-weight:500;line-height:1.3;color:{cor_f}'>{f}</div>
</div>"""
    return f"<div class='visual' style='display:grid;grid-template-columns:1fr 1fr;gap:22px'>{cards}</div>"

def responde():
    return slide("light", EXTRA + f"""
<div class='eyebrow'>O que ele responde</div>
<div class='h2'>Quatro perguntas, num lugar só.</div>{v_perguntas()}""", 3, 8)

# ================================================================= 4 · lá fora
# Exemplo: 3 remessas de US$ 4.000 (R$ 19.600 a 4,90; R$ 20.000 a 5,00; R$ 20.400 a 5,10)
# = R$ 60.000 por US$ 12.000, câmbio médio R$ 5,00. Carteira hoje US$ 13.200 (+10%),
# PTAX R$ 5,50 → R$ 72.600. Ganho R$ 12.600 (+21%) = rendimento US$ 1.200 × 5,50 (R$ 6.600)
# + câmbio US$ 12.000 × (5,50 − 5,00) (R$ 6.000).
ENVIADO, US_INI, US_HOJE, PTAX_HOJE = 60000, 12000, 13200, 5.50
REAIS_HOJE = US_HOJE * PTAX_HOJE
REND = (US_HOJE - US_INI) * PTAX_HOJE
CAMB = US_INI * (PTAX_HOJE - ENVIADO / US_INI)
assert abs(REAIS_HOJE - 72600) < .01 and abs(REND - 6600) < .01 and abs(CAMB - 6000) < .01
assert abs((REND + CAMB) - (REAIS_HOJE - ENVIADO)) < .01

def v_exterior():
    return f"""<div class='visual' style='margin-top:32px'>
  <div class='sombra' style='border-radius:26px;overflow:hidden;background:#fff'><img src="{tela('remessas-resultado.png')}" style='display:block;width:100%;height:auto'></div>
  <div class='nota' style='margin-top:16px'>Tela real do timtimcash, com dados de exemplo, sem IOF e tarifas.</div>
</div>"""

def exterior():
    return slide("light", EXTRA + f"""
<div class='eyebrow'>Investimentos lá fora</div>
<div class='h3'>Quanto rendeu de verdade, em dólar e em real.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Cada remessa na sua data, com a PTAX do Banco Central. Rendimento e câmbio separados.</div>{v_exterior()}""", 4, 8)

# ================================================================= 5 · planilha e extrato
def v_importacao():
    return f"""<div class='visual' style='margin-top:44px'>
  <div class='sombra' style='position:relative;border-radius:26px;overflow:hidden;background:#fff'><img src="{tela('importacao-recorte.png')}" style='display:block;width:100%;height:auto'>
    <i style='position:absolute;top:0;right:0;bottom:0;width:44px;background:linear-gradient(90deg,rgba(255,255,255,0),#fff);display:block'></i></div>
  <div class='nota'>Tela real do timtimcash, com dados de exemplo.</div>
</div>"""

def planilha():
    return slide("light", EXTRA + f"""
<div class='eyebrow'>Seu histórico vem junto</div>
<div class='h2'>Já usa planilha? Ela vem junto.</div>
<div class='p' style='margin-top:22px;font-size:36px'>Importe a planilha (.xlsx, .csv) ou o extrato do banco (.ofx), com as categorias já sugeridas.</div>{v_importacao()}""", 5, 8)

# ================================================================= 6 · privacidade
def v_privacidade():
    larg, alt = 430, 556            # recorte do topo da tela do celular (390 px de largura na tela)
    esc = larg / 390
    def quadro(img, legenda, destaque=False):
        anel = ""
        if destaque:  # o olho fica no topo, à direita (311, 38 em px de tela)
            cx, cy = 311 * esc, 38 * esc
            anel = f"<i style='position:absolute;left:{cx - 31:.0f}px;top:{cy - 31:.0f}px;width:62px;height:62px;border-radius:50%;border:4px solid {BRAND};display:block'></i>"
        return f"""<div>
  <div class='sombra' style='position:relative;width:{larg}px;height:{alt}px;border-radius:28px;overflow:hidden;background:{BG};border:1px solid {FIO}'>
    <img src="{tela(img)}" style='display:block;width:{larg}px;height:auto'>{anel}</div>
  <div style='margin-top:18px;font-size:27px;font-weight:600;color:{INK};display:flex;align-items:center;gap:12px'>{legenda}</div>
</div>"""
    return f"""<div class='visual' style='margin-top:44px;display:flex;justify-content:space-between'>
  {quadro('movel.png', 'Valores à mostra')}
  {quadro('movel-ocultar.png', ic(I_EYEOFF, 28, BRAND_DARK, 2.2) + 'Um toque e eles somem', destaque=True)}
</div>"""

def privacidade():
    return slide("light", EXTRA + f"""
<div class='eyebrow'>Privacidade</div>
<div class='h2'>Sem senha do banco. Sem propaganda.</div>
<div class='p' style='margin-top:22px;font-size:36px'>O timtimcash não se conecta à sua conta bancária. E um toque no olho esconde os valores da tela.</div>{v_privacidade()}""", 6, 8)

# ================================================================= 7 · como começar
def v_passos():
    url = f"<span style='display:inline-flex;align-items:center;gap:12px;height:58px;padding:0 24px;border-radius:999px;background:#fff;border:1.5px solid {FIO};font-size:27px;font-weight:600;color:{INK}'>{ic(I_LOCK, 24, MUTED, 2.2)}timtimcash.com</span>"
    criar = f"<span style='display:inline-flex;align-items:center;height:58px;padding:0 30px;border-radius:999px;background:{BRAND};color:#fff;font-size:27px;font-weight:600'>Criar conta</span>"
    banco = f"<span style='display:inline-flex;align-items:center;gap:10px;height:58px;padding:0 26px;border-radius:999px;background:#fff;border:1.5px solid {NEUTRO};font-size:27px;font-weight:600;color:{INK}'>{ic(I_PLUS, 24, BRAND_DARK, 2.6)}Adicionar banco ou carteira</span>"
    passos = [("Acesse timtimcash.com", "Pelo navegador, no computador ou no celular.", url),
              ("Crie sua conta", "Com nome, e-mail e senha.", criar),
              ("Adicione seu banco ou carteira", "Depois importe o extrato ou lance à mão.", banco)]
    html = ""
    for i, (t, s, ui) in enumerate(passos, 1):
        fio = "" if i == len(passos) else f"<i style='position:absolute;left:35px;top:84px;bottom:-30px;width:4px;border-radius:2px;background:{FIO};display:block'></i>"
        html += f"""<div style='position:relative;display:grid;grid-template-columns:74px 1fr;column-gap:30px;padding-bottom:{0 if i == len(passos) else 30}px'>
  {fio}<div style='width:74px;height:74px;border-radius:50%;background:{BRAND};color:#fff;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:700'>{i}</div>
  <div><div style='font-size:40px;font-weight:700;letter-spacing:-.035em;line-height:1.1;margin-top:12px'>{t}</div>
    <div style='font-size:28px;color:{MUTED};line-height:1.35;margin-top:10px'>{s}</div>
    <div style='margin-top:18px'>{ui}</div></div>
</div>"""
    return f"<div class='visual' style='margin-top:58px'>{html}</div>"

def comecar():
    return slide("light", EXTRA + f"""
<div class='eyebrow'>Como começar</div>
<div class='h2'>Três passos e o seu mês aparece.</div>{v_passos()}""", 7, 8)

# ================================================================= 8 · fechamento
def fechamento():
    head = "<div class='head'><div></div><div class='count'>8/8</div></div>"
    corpo = f"""
<div style='margin-bottom:52px'>{logo_vertical('white', 190)}</div>
<div class='h2'>Seu dinheiro, com a clareza que ele merece.</div>
<div class='lead'>Gratuito para o controle financeiro. No computador ou no celular.</div>{v_cta_pill()}"""
    return page(head + f"<div class='body'>{corpo}</div>" + footer(last=True), "green")

def post():
    return [capa(), o_que_e(), responde(), exterior(), planilha(), privacidade(), comecar(), fechamento()]

POSTS = {"2026-09-30_comece-por-aqui": post}
