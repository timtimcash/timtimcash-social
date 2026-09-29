# -*- coding: utf-8 -*-
"""Post institucional: o timtimcash como um todo (carrossel de 10)."""
from artes import *

AMBER = "#e3a324"
CORAL = "#d97757"
LINE = "#efeee8"

def icon(path, size=40, color=BRAND_DARK, sw=2.2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

I_CARD = '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19"/><path d="M6.5 15h4"/>'
I_CUP = '<path d="M4 8h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M17 9.5h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 2.5v2.5M12 2.5v2.5"/>'
I_HOME = '<path d="M3.5 10.5 12 4l8.5 6.5"/><path d="M5.5 9v10.5h13V9"/><path d="M10 19.5v-5h4v5"/>'
I_COIN = '<circle cx="12" cy="12" r="8.5"/><path d="M14.8 9.2c-.5-.9-1.6-1.4-2.8-1.4-1.6 0-2.8.8-2.8 2.1 0 2.9 5.8 1.4 5.8 4.3 0 1.3-1.3 2.1-3 2.1-1.3 0-2.4-.5-2.9-1.5M12 6.2v1.6M12 16.3v1.6"/>'
I_GLOBE = '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17"/><path d="M12 3.5c2.4 2.6 3.5 5.4 3.5 8.5s-1.1 5.9-3.5 8.5c-2.4-2.6-3.5-5.4-3.5-8.5s1.1-5.9 3.5-8.5z"/>'
I_CART = '<path d="M3 4h2.5l2.2 10.5h10.3l2-7.5H6.4"/><circle cx="9.5" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>'
I_UP = '<path d="M7 17 17 7"/><path d="M8 7h9v9"/>'
I_DOWN = '<path d="M17 7 7 17"/><path d="M16 17H7V8"/>'
I_EYEOFF = '<path d="M3 3l18 18"/><path d="M10.6 5.2A9.9 9.9 0 0 1 12 5c5 0 8.5 4.5 9.5 7-.4 1-1.2 2.3-2.4 3.5M6.4 6.5C4.6 7.8 3.2 9.8 2.5 12c1 2.5 4.5 7 9.5 7 1.8 0 3.4-.6 4.8-1.4"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>'
I_FILE = '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>'

def badge(path, bg="#fff", color=BRAND_DARK, size=104, isz=48):
    return f"<div style='width:{size}px;height:{size}px;border-radius:50%;background:{bg};display:flex;align-items:center;justify-content:center;box-shadow:0 14px 30px -14px rgba(0,0,0,.35)'>{icon(path, isz, color)}</div>"

# ---------------------------------------------------------------- visuais
def v_pistas():
    # trilha de pistas do dia a dia que termina na marca
    pts = [(60, 235), (250, 140), (440, 205), (630, 100)]
    icons = [I_CARD, I_CUP, I_HOME, I_GLOBE]
    path = "M 60 235 C 140 235, 170 140, 250 140 S 360 205, 440 205 S 550 100, 630 100 S 740 150, 810 150"
    badges = "".join(f"<div style='position:absolute;left:{x-52}px;top:{y-52}px'>{badge(p)}</div>" for (x, y), p in zip(pts, icons))
    final = f"<div style='position:absolute;left:{810-80}px;top:{150-80}px;width:160px;height:160px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 40px -16px rgba(0,0,0,.4)'>{logo('color', 64)}</div>"
    return f"""<div class='visual' style='position:relative;height:320px;margin-top:64px'>
  <svg width="896" height="320" viewBox="0 0 896 320" fill="none" style="position:absolute;left:0;top:0">
    <path d="{path}" stroke="rgba(255,255,255,.6)" stroke-width="5" stroke-dasharray="2 16" stroke-linecap="round"/>
  </svg>
  {badges}{final}
</div>"""

def v_lista():
    rows = [
        (I_UP, BRAND, "Salário", 190, 150, ""),
        (I_CART, "#0e9f6e", "Mercado", 150, 130, ""),
        (I_CARD, "#2f6fd6", "Fatura do cartão", 170, 160, ""),
        (I_HOME, AMBER, "Aluguel", 130, 140, "pendente"),
    ]
    html = ""
    for i, (ic, cor, nome, w1, w2, selo) in enumerate(rows):
        borda = "none" if i == len(rows) - 1 else f"1px solid {LINE}"
        pill = f"<span style='margin-left:14px;font-size:22px;font-weight:700;color:#9a6a06;background:#fdf2dc;padding:6px 14px;border-radius:999px'>{selo}</span>" if selo else ""
        html += f"""<div style='display:flex;align-items:center;gap:24px;padding:20px 0;border-bottom:{borda}'>
  <div style='width:62px;height:62px;border-radius:18px;background:{cor}1f;display:flex;align-items:center;justify-content:center'>{icon(ic, 30, cor, 2.4)}</div>
  <div style='flex:1'><div style='font-size:31px;font-weight:600;display:flex;align-items:center'>{nome}{pill}</div><div class='sk' style='width:{w1}px;margin-top:12px'></div></div>
  <div class='sk' style='width:{w2}px;height:24px'></div></div>"""
    return f"<div class='visual' style='margin-top:56px'><div class='card' style='padding:8px 40px'>{html}</div></div>"

def v_orcamentos():
    itens = [("Mercado", 58, BRAND), ("Restaurantes", 86, AMBER), ("Lazer", 100, CORAL)]
    html = ""
    for i, (nome, pct, cor) in enumerate(itens):
        html += f"""<div style='padding:22px 0;{'' if i == 2 else f'border-bottom:1px solid {LINE}'}'>
  <div style='display:flex;justify-content:space-between;align-items:center'><span style='font-size:31px;font-weight:600'>{nome}</span><span style='width:18px;height:18px;border-radius:50%;background:{cor}'></span></div>
  <div style='height:22px;border-radius:11px;background:#eeede6;margin-top:16px;overflow:hidden'><div style='width:{pct}%;height:100%;border-radius:11px;background:{cor}'></div></div>
</div>"""
    return f"<div class='visual' style='margin-top:56px'><div class='card' style='padding:14px 44px'>{html}</div></div>"

def spark(d, cor):
    return f'<svg width="120" height="44" viewBox="0 0 120 44" fill="none"><path d="{d}" stroke="{cor}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def v_visao():
    tiles = [("Saldo", "M4 34 L28 28 L52 30 L76 18 L100 20 L116 10", BRAND),
             ("Receitas", "M4 30 L28 26 L52 28 L76 22 L100 16 L116 14", BRAND),
             ("Despesas", "M4 16 L28 22 L52 18 L76 26 L100 24 L116 30", CORAL),
             ("Patrimônio", "M4 38 L28 32 L52 28 L76 22 L100 14 L116 6", BRAND)]
    t = "".join(f"""<div class='card' style='padding:26px 30px'>
  <div style='display:flex;justify-content:space-between;align-items:flex-start'><span style='font-size:27px;font-weight:600;color:{MUTED}'>{n}</span>{spark(d, c)}</div>
  <div class='sk' style='width:190px;height:30px;margin-top:10px'></div></div>""" for n, d, c in tiles)
    hs = [48, 60, 44, 70, 58, 76, 64, 82, 70, 90, 78, 96]
    bars = "".join(f"<div style='flex:1;height:{h}%;border-radius:8px 8px 3px 3px;background:{BRAND if i == 11 else '#a7e3c9'}'></div>" for i, h in enumerate(hs))
    return f"""<div class='visual' style='margin-top:52px'>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:20px'>{t}</div>
  <div class='card' style='padding:26px 30px;margin-top:20px'><div style='display:flex;gap:12px;align-items:flex-end;height:120px'>{bars}</div></div>
</div>"""

def v_simulacao():
    passado = "M20 170 C 90 160, 140 120, 210 130 S 330 100, 400 110"
    futuro = "M400 110 C 470 118, 540 80, 610 88 S 740 60, 820 50"
    banda = "M400 110 C 470 88, 540 40, 610 42 S 740 10, 820 0 L 820 100 C 740 110, 680 130, 610 134 S 470 140, 400 110 Z"
    return f"""<div class='visual' style='margin-top:56px'><div class='card' style='padding:40px 40px 30px'>
  <svg width="100%" viewBox="0 0 840 220" fill="none">
    <path d="{banda}" fill="{BRAND}" opacity=".10"/>
    <line x1="400" y1="0" x2="400" y2="200" stroke="{INK}" stroke-opacity=".25" stroke-width="2" stroke-dasharray="6 8"/>
    <path d="{passado}" stroke="{INK}" stroke-opacity=".8" stroke-width="6" stroke-linecap="round"/>
    <path d="{futuro}" stroke="{BRAND}" stroke-width="6" stroke-linecap="round" stroke-dasharray="14 12"/>
    <circle cx="400" cy="110" r="12" fill="{BRAND}" stroke="#fff" stroke-width="5"/>
  </svg>
  <div style='display:flex;justify-content:space-between;margin-top:18px;font-size:27px;font-weight:600;color:{MUTED}'>
    <span>até hoje</span><span style='color:{BRAND_DARK}'>próximos meses</span></div>
</div></div>"""

def v_relatorios():
    donut = f'''<svg width="150" height="150" viewBox="0 0 42 42"><circle cx="21" cy="21" r="15.9" fill="none" stroke="#e8f5ef" stroke-width="6"/>
<circle cx="21" cy="21" r="15.9" fill="none" stroke="{BRAND}" stroke-width="6" stroke-dasharray="40 60" stroke-dashoffset="25"/>
<circle cx="21" cy="21" r="15.9" fill="none" stroke="#6ee7b7" stroke-width="6" stroke-dasharray="25 75" stroke-dashoffset="85"/>
<circle cx="21" cy="21" r="15.9" fill="none" stroke="{CORAL}" stroke-width="6" stroke-dasharray="15 85" stroke-dashoffset="60"/></svg>'''
    pares = "".join(f"<div style='display:flex;gap:6px;align-items:flex-end;height:100%'><div style='width:22px;height:{a}%;background:#c8ccd2;border-radius:6px 6px 2px 2px'></div><div style='width:22px;height:{b}%;background:{BRAND};border-radius:6px 6px 2px 2px'></div></div>" for a, b in [(70, 55), (50, 80), (85, 60)])
    saz = "".join(f"<div style='flex:1;height:{h}%;background:{BRAND if h > 80 else '#a7e3c9'};border-radius:4px 4px 2px 2px'></div>" for h in [60, 52, 70, 64, 58, 50, 55, 62, 68, 74, 84, 96])
    def cartao(titulo, corpo):
        return f"<div class='card' style='padding:26px 22px 22px;display:flex;flex-direction:column;align-items:center;gap:20px'><div style='height:150px;width:100%;display:flex;align-items:flex-end;justify-content:center'>{corpo}</div><div style='font-size:25px;font-weight:700'>{titulo}</div></div>"
    return f"""<div class='visual' style='margin-top:56px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px'>
  {cartao('Diagnóstico', donut)}
  {cartao('Comparar', f"<div style='display:flex;gap:26px;height:130px;align-items:flex-end'>{pares}</div>")}
  {cartao('Sazonalidade', f"<div style='display:flex;gap:5px;width:100%;height:130px;align-items:flex-end'>{saz}</div>")}
</div>"""

def v_cascata():
    # você enviou -> rendimento -> efeito do câmbio -> hoje (sem valores)
    cols = [("você enviou", 0, 130, "#c8ccd2"), ("rendimento", 130, 80, BRAND), ("efeito do câmbio", 170, 40, CORAL), ("hoje", 0, 170, BRAND_DARK)]
    base = 230
    barras = ""
    for i, (rot, y0, h, cor) in enumerate(cols):
        x = 40 + i * 205
        barras += f"<rect x='{x}' y='{base - y0 - h}' width='140' height='{h}' rx='12' fill='{cor}'/>"
        if i < 3:
            ny = base - (y0 + h) if i != 2 else base - 170
            barras += f"<line x1='{x+140}' y1='{ny}' x2='{x+205}' y2='{ny}' stroke='{INK}' stroke-opacity='.3' stroke-width='2' stroke-dasharray='5 6'/>"
    rot = "".join(f"<span style='width:205px;text-align:center'>{r}</span>" for r, *_ in cols)
    return f"""<div class='visual' style='margin-top:52px'><div class='card' style='padding:34px 30px 28px'>
  <svg width="100%" viewBox="0 0 860 240" fill="none"><line x1="20" y1="231" x2="840" y2="231" stroke="#e5e7e1" stroke-width="2"/>{barras}</svg>
  <div style='display:flex;padding-left:8px;margin-top:10px;font-size:24px;font-weight:600;color:{MUTED}'>{rot}</div>
  <div style='display:flex;gap:14px;margin-top:26px'>
    <span style='background:{SOFT};color:{BRAND_DARK};font-size:26px;font-weight:700;padding:12px 24px;border-radius:999px'>US$</span>
    <span style='background:{SOFT};color:{BRAND_DARK};font-size:26px;font-weight:700;padding:12px 24px;border-radius:999px'>R$</span>
    <span style='background:{SOFT};color:{BRAND_DARK};font-size:26px;font-weight:700;padding:12px 24px;border-radius:999px'>PTAX · Banco Central</span>
  </div>
</div></div>"""

def v_planilha():
    def arq(ext):
        return f"""<div class='card' style='width:200px;padding:30px 0 26px;display:flex;flex-direction:column;align-items:center;gap:14px'>
  {icon(I_FILE, 64, BRAND_DARK, 1.8)}<span style='font-size:32px;font-weight:800;letter-spacing:.04em;color:{BRAND_DARK}'>{ext}</span></div>"""
    linhas = "".join(f"<div style='display:flex;align-items:center;gap:18px;padding:16px 0;border-bottom:{'none' if i == 3 else f'1px solid {LINE}'}'><div style='width:44px;height:44px;border-radius:13px;background:{SOFT}'></div><div class='sk' style='flex:1;max-width:{w}px'></div><div class='sk' style='width:90px;margin-left:auto'></div></div>" for i, w in enumerate([200, 150, 180, 130]))
    seta = ARROW.replace('width="30" height="30"', 'width="56" height="56"')
    return f"""<div class='visual' style='margin-top:56px;display:flex;align-items:center;gap:26px'>
  <div style='display:flex;flex-direction:column;gap:20px'>{arq('XLS')}{arq('CSV')}</div>
  <div style='color:{BRAND}'>{seta}</div>
  <div class='card' style='flex:1;padding:10px 34px'>{linhas}</div>
</div>"""

def v_privacidade():
    chips = "".join(f"<span class='chip' style='height:68px;font-size:29px'><span style='width:14px;height:14px;border-radius:50%;background:{BRAND};margin-right:14px'></span>{t}</span>" for t in ["Sem propaganda", "Sem conexão bancária", "Tema escuro"])
    return f"""<div class='visual' style='margin-top:52px'>
  <div class='card' style='padding:34px 40px;display:flex;align-items:center;justify-content:space-between'>
    <div><div style='font-size:28px;font-weight:600;color:{MUTED}'>Patrimônio</div>
      <div style='font-size:72px;font-weight:800;letter-spacing:.02em;margin-top:4px'>R$ <span style='letter-spacing:.14em'>••••••</span></div></div>
    <div style='width:96px;height:96px;border-radius:28px;background:{SOFT};display:flex;align-items:center;justify-content:center'>{icon(I_EYEOFF, 50, BRAND_DARK, 2.2)}</div>
  </div>
  <div style='display:flex;flex-wrap:wrap;gap:14px;margin-top:26px'>{chips}</div>
</div>"""

def v_cta():
    return f"""<div class='visual' style='margin-top:56px;display:flex;align-items:center;gap:30px'>
  <span class='pill'>Link na bio {ARROW}</span>
</div>"""

# ---------------------------------------------------------------- post
def slide_final(body, idx, total):
    head = f"<div class='head'><div></div><div class='count'>{idx}/{total}</div></div>"
    return page(head + f"<div class='body'>{body}</div>" + footer(last=True), "green")

def institucional():
    T = 10
    s = []
    s.append(slide("green", f"""
<div class='eyebrow'>Conheça o timtimcash</div>
<div class='h1' style='font-size:100px'>Seu dinheiro deixa pistas todos os dias.</div>
<div class='lead' style='color:rgba(255,255,255,.92)'>O timtimcash junta todas elas e conta a história inteira.</div>{v_pistas()}""", 1, T))
    s.append(slide("light", f"""
<div class='eyebrow'>1 · O dia a dia</div>
<div class='h3'>Tudo o que entra e sai, no lugar certo.</div>
<div class='p' style='margin-top:26px'>Receitas e despesas por categoria, fatura do cartão, várias contas e o que ainda está pendente.</div>{v_lista()}""", 2, T))
    s.append(slide("light", f"""
<div class='eyebrow'>2 · Orçamentos</div>
<div class='h2'>Um limite para cada categoria.</div>
<div class='p'>As faixas de alerta mudam de cor quando o gasto chega perto do limite. Você percebe antes, não depois.</div>{v_orcamentos()}""", 3, T))
    s.append(slide("light", f"""
<div class='eyebrow'>3 · Visão geral</div>
<div class='h2'>O mês inteiro numa tela só.</div>
<div class='p' style='margin-top:26px'>Saldo, receitas, despesas e patrimônio, com o fluxo dos últimos 12 meses logo abaixo.</div>{v_visao()}""", 4, T))
    s.append(slide("light", f"""
<div class='eyebrow'>4 · Simulação</div>
<div class='h2'>Veja o mês que vem antes de ele chegar.</div>
<div class='p'>A simulação de fluxo futuro projeta os próximos meses. Dá tempo de ajustar o rumo.</div>{v_simulacao()}""", 5, T))
    s.append(slide("light", f"""
<div class='eyebrow'>5 · Relatórios</div>
<div class='h2'>Não só quanto você gastou. Por quê.</div>
<div class='p'>Diagnóstico do mês, comparação entre períodos e sazonalidade para enxergar o padrão.</div>{v_relatorios()}""", 6, T))
    s.append(slide("light", f"""
<div class='eyebrow'>6 · Investimentos lá fora</div>
<div class='h3'>Investe fora do Brasil? Veja quanto rendeu de verdade.</div>
<div class='p' style='margin-top:26px;font-size:36px'>Cada remessa na sua data, em dólar e em real, com a cotação PTAX do Banco Central. O que foi rendimento fica separado do que foi câmbio.</div>{v_cascata()}""", 7, T))
    s.append(slide("light", f"""
<div class='eyebrow'>7 · Sua planilha</div>
<div class='h3'>Já controla tudo em planilha? Ela vem junto.</div>
<div class='p' style='margin-top:26px'>Importe arquivos XLS e CSV e comece com o seu histórico, sem digitar tudo de novo.</div>{v_planilha()}""", 8, T))
    s.append(slide("light", f"""
<div class='eyebrow'>8 · Privacidade</div>
<div class='h2'>Seus dados continuam seus.</div>
<div class='p' style='margin-top:26px'>O modo privacidade esconde os valores da tela, e o tema escuro deixa tudo confortável à noite.</div>{v_privacidade()}""", 9, T))
    s.append(slide_final(f"""
<div style='margin-bottom:48px'>{logo('white', 120)}</div>
<div class='h1' style='font-size:96px'>Seu dinheiro, com a clareza que ele merece.</div>
<div class='lead' style='color:rgba(255,255,255,.92)'>Gratuito para o controle financeiro. No computador ou no celular.</div>{v_cta()}""", 10, T))
    return s

POSTS = {"2026-09-29_conheca-o-timtimcash": institucional}
