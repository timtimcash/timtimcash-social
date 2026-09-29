# -*- coding: utf-8 -*-
"""Semana de 28/09/2026: posts avulsos de quarta 30/09, sexta 02/10 e sábado 03/10.

Todos os valores são de exemplo e coerentes entre os posts (mesmo salário, mesmo aluguel, mesma parcela).
"""
from artes import *

# ---------------------------------------------------------------- estilos extras desta semana
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
.selo.red{{background:#F8E1E1;color:{RED_TEXT}}}
.trilho{{height:20px;border-radius:10px;background:{FIO};overflow:hidden}}
.trilho > i{{display:block;height:100%;border-radius:10px}}
</style>"""

def brl(v, sinal=False, centavos=True):
    s = f"{abs(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    inteiro, cent = s.split(",")
    pre = ""
    if sinal:
        pre = "+" if v > 0 else ("−" if v < 0 else "")
    ct = f"<span class='ct'>,{cent}</span>" if centavos else ""
    return f"<span class='val'>{pre}<span class='rs'>R$</span>{inteiro}{ct}</span>"

def usd(v, centavos=True):
    s = f"{abs(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    inteiro, cent = s.split(",")
    ct = f"<span class='ct'>,{cent}</span>" if centavos else ""
    return f"<span class='val'><span class='rs'>US$</span>{inteiro}{ct}</span>"

def ic(path, size=34, cor=BRAND_DARK, sw=2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

I_CHECK = '<path d="M20 6 9 17l-5-5"/>'
I_HOME = '<path d="M3.5 10.5 12 4l8.5 6.5"/><path d="M5.5 9v10.5h13V9"/><path d="M10 19.5v-5h4v5"/>'
I_CART = '<path d="M3 4h2.5l2.2 10.5h10.3l2-7.5H6.4"/><circle cx="9.5" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>'
I_CAR = '<path d="M5 16.5h14M6.5 16.5v2M17.5 16.5v2"/><path d="M4.5 16.5V12l1.8-4.2A2 2 0 0 1 8.1 6.5h7.8a2 2 0 0 1 1.8 1.3L19.5 12v4.5z"/><path d="M4.5 12h15"/>'
I_BOLT = '<path d="M13 3 5 13h6l-1 8 8-10h-6z"/>'
I_HEART = '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>'
I_CARD = '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19"/><path d="M6.5 15h4"/>'
I_UP = '<path d="M7 17 17 7"/><path d="M8 7h9v9"/>'
I_BOOK = '<path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5z"/><path d="M20 5.5A1.5 1.5 0 0 0 18.5 4H13v16h5.5a1.5 1.5 0 0 0 1.5-1.5z"/>'
I_PLAY = '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m10 9.5 4.5 2.5-4.5 2.5z"/>'
I_GLOBE = '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17"/><path d="M12 3.5c2.4 2.6 3.5 5.4 3.5 8.5s-1.1 5.9-3.5 8.5c-2.4-2.6-3.5-5.4-3.5-8.5s1.1-5.9 3.5-8.5z"/>'

def azul(path, size=64, isz=32):
    return f"<div class='azulejo' style='width:{size}px;height:{size}px;flex:none'>{ic(path, isz)}</div>"

# ================================================================= POST 1 · quarta 30/09 · fechamento do mês
def v_calendario():
    # setembro de 2026 começa numa terça (domingo na primeira coluna)
    cab = "".join(f"<div style='text-align:center;font-size:24px;font-weight:700;color:{MUTED}'>{d}</div>" for d in "DSTQQSS")
    cel = ["<div></div>"] * 2
    for d in range(1, 31):
        if d == 30:
            cel.append(f"<div style='display:flex;align-items:center;justify-content:center'><div style='width:74px;height:74px;border-radius:50%;background:{BRAND};color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700'>30</div></div>")
        else:
            cel.append(f"<div style='text-align:center;font-size:30px;font-weight:500;color:{INK};line-height:74px' class='num'>{d}</div>")
    return f"""<div class='visual'><div class='card' style='padding:34px 40px 26px'>
  <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:18px'>
    <span style='font-size:34px;font-weight:700;letter-spacing:-.02em'>Setembro 2026</span>
    <span class='selo ok'>{ic(I_CHECK, 24, BRAND_DEEP, 2.6)} último dia</span></div>
  <div style='display:grid;grid-template-columns:repeat(7,1fr);row-gap:2px'>{cab}{''.join(cel)}</div>
</div></div>"""

def v_saldo_mes():
    return f"""<div class='visual'><div class='card' style='padding:36px 40px'>
  <div style='display:flex;justify-content:space-between;align-items:center'><span class='rot'>Setembro 2026</span><span class='tag'>Exemplo</span></div>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:22px'>
    <div><div class='rot'>Receitas</div><div style='font-size:52px;margin-top:4px'>{brl(9960)}</div><div class='trilho' style='margin-top:14px'><i style='width:100%;background:{BRAND_DARK}'></i></div></div>
    <div><div class='rot'>Despesas</div><div style='font-size:52px;margin-top:4px'>{brl(7780)}</div><div class='trilho' style='margin-top:14px'><i style='width:78%;background:{CORAL}'></i></div></div>
  </div>
  <div style='margin-top:28px;padding-top:24px;border-top:1px solid {FIO};display:flex;justify-content:space-between;align-items:baseline'>
    <span style='font-size:30px;font-weight:600'>Saldo do mês</span><span style='font-size:60px;color:{BRAND_DARK}'>{brl(2180, sinal=True).replace("class='val'", "class='val' style='color:"+BRAND_DARK+"'")}</span></div>
</div></div>"""

def v_categorias():
    itens = [(I_HOME, "Moradia", 2300, 30), (I_CART, "Mercado", 1710, 22), (I_CAR, "Transporte", 1245, 16)]
    linhas = "".join(f"""<div class='linha'>{azul(p, 60, 30)}
  <div style='flex:1'><div style='display:flex;justify-content:space-between;align-items:baseline'><span style='font-size:32px;font-weight:600'>{n}</span><span style='font-size:36px'>{brl(v, centavos=False)}</span></div>
  <div style='display:flex;align-items:center;gap:16px;margin-top:12px'><div class='trilho' style='flex:1'><i style='width:{pc}%;background:{CORAL}'></i></div><span class='num' style='font-size:26px;font-weight:600;color:{MUTED};width:64px;text-align:right'>{pc}%</span></div></div></div>""" for p, n, v, pc in itens)
    return f"""<div class='visual'><div class='card' style='padding:24px 40px 14px'>
  <div style='display:flex;justify-content:space-between;align-items:center;padding-bottom:6px'><span class='rot'>Maiores despesas de setembro</span><span class='tag'>Exemplo</span></div>{linhas}</div></div>"""

def v_orcamentos():
    itens = [("Transporte", 1245, 1950, 64, BRAND, "ok", "tranquilo"), ("Mercado", 1710, 2000, 86, AMBER_BAR, "amb", "no limite"),
             ("Restaurantes", 672, 600, 112, RED, "red", "estourou")]
    linhas = "".join(f"""<div class='linha' style='display:block'>
  <div style='display:flex;justify-content:space-between;align-items:center'><span style='font-size:32px;font-weight:600'>{n}</span><span class='selo {cl}'>{pc}% · {rot}</span></div>
  <div class='trilho' style='margin-top:14px'><i style='width:{min(pc,100)}%;background:{cor}'></i></div>
  <div style='margin-top:10px;font-size:26px;color:{MUTED}'>{brl(g, centavos=False)} de {brl(l, centavos=False)}</div></div>""" for n, g, l, pc, cor, cl, rot in itens)
    return f"""<div class='visual'><div class='card' style='padding:24px 40px 10px'>
  <div style='display:flex;justify-content:space-between;align-items:center;padding-bottom:4px'><span class='rot'>Orçamentos de setembro</span><span class='tag'>Exemplo</span></div>{linhas}</div></div>"""

def v_pendentes():
    itens = [(I_BOLT, "Conta de luz", "vence hoje", -186.40), (I_HEART, "Reembolso do plano de saúde", "a receber", 320.00),
             (I_CARD, "Parcela 3 de 10", "fatura do cartão", -249.90)]
    linhas = "".join(f"""<div class='linha'>{azul(p, 60, 30)}
  <div style='flex:1'><div style='font-size:31px;font-weight:600'>{n}</div><div style='margin-top:8px'><span class='selo amb'>{s}</span></div></div>
  <div style='font-size:36px'>{brl(v, sinal=True)}</div></div>""" for p, n, s, v in itens)
    return f"""<div class='visual'><div class='card' style='padding:24px 40px 14px'>
  <div style='display:flex;justify-content:space-between;align-items:center;padding-bottom:6px'><span class='rot'>Pendentes</span><span class='tag'>Exemplo</span></div>{linhas}</div></div>"""

def v_comparar():
    return f"""<div class='visual'><div class='card' style='padding:36px 40px'>
  <div style='display:flex;justify-content:space-between;align-items:center'><span class='rot'>Despesas</span><span class='tag'>Exemplo</span></div>
  <div style='display:flex;gap:40px;align-items:flex-end;height:250px;margin-top:26px;padding:0 20px'>
    <div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:14px;height:100%;justify-content:flex-end'>
      <div style='font-size:36px'>{brl(8285, centavos=False)}</div><div style='width:100%;height:170px;border-radius:14px 14px 6px 6px;background:{NEUTRO}'></div><div class='rot'>Ago/26</div></div>
    <div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:14px;height:100%;justify-content:flex-end'>
      <div style='font-size:36px'>{brl(7780, centavos=False)}</div><div style='width:100%;height:160px;border-radius:14px 14px 6px 6px;background:{CORAL}'></div><div class='rot'>Set/26</div></div>
  </div>
  <div style='margin-top:26px;text-align:center'><span class='selo ok' style='height:48px;font-size:27px;padding:0 22px'>↓ 6,1% vs Ago/26</span></div>
</div></div>"""

def post1():
    T = 7
    s = []
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Fechamento do mês</div>
<div class='h1'>Hoje o mês fecha.</div>
<div class='lead'>E o seu dinheiro, <span class='accent'>já fechou também?</span></div>{v_calendario()}""", 1, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Pergunta 1 de 5</div>
<div class='h2'>Quanto entrou e quanto saiu?</div>
<div class='p' style='margin-top:24px'>Saldo positivo, você guardou. Negativo, alguém cobriu a diferença: a reserva, o cartão ou o cheque especial.</div>{v_saldo_mes()}""", 2, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Pergunta 2 de 5</div>
<div class='h2'>Para onde foi a maior parte?</div>
<div class='p' style='margin-top:24px'>Olhe as três categorias que mais pesaram. É nelas que qualquer ajuste faz diferença de verdade.</div>{v_categorias()}""", 3, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Pergunta 3 de 5</div>
<div class='h2'>Algum orçamento estourou?</div>
<div class='p' style='margin-top:24px'>Se estoura todo mês, não é acidente: ou o limite está irreal, ou o hábito precisa mudar.</div>{v_orcamentos()}""", 4, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Pergunta 4 de 5</div>
<div class='h2'>O que ainda está pendente?</div>
<div class='p' style='margin-top:24px'>Conta a pagar, reembolso a receber, parcela na fatura. O mês só fecha quando nada fica para trás.</div>{v_pendentes()}""", 5, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Pergunta 5 de 5</div>
<div class='h2'>Foi melhor que agosto?</div>
<div class='p' style='margin-top:24px'>Comparar com o mês anterior mostra a direção. Um mês ruim acontece. Três seguidos já é tendência.</div>{v_comparar()}""", 6, T))
    s.append(slide("green", f"""
<div class='h2'>No timtimcash, as cinco respostas estão numa tela só.</div>
<div class='lead'>Visão geral, orçamentos, pendentes e comparação entre períodos. Gratuito para o controle financeiro.</div>{v_cta_pill()}""", 7, T))
    return s

# ================================================================= POST 2 · sexta 02/10 · rendimento x câmbio
def v_dois_numeros():
    return f"""<div class='visual' style='display:grid;grid-template-columns:1fr 1fr;gap:22px'>
  <div class='card' style='padding:40px 36px'><div class='rot'>Em dólar</div><div style='font-size:104px;font-weight:700;letter-spacing:-.045em;color:{BRAND_DARK};margin-top:6px' class='num'>+10%</div></div>
  <div class='card' style='padding:40px 36px;background:{SOFT};border-color:{SOFT}'><div class='rot' style='color:{BRAND_DEEP}'>Em reais</div><div style='font-size:104px;font-weight:700;letter-spacing:-.045em;color:{BRAND_DEEP};margin-top:6px'>?</div></div>
</div>"""

def v_conversao():
    seta = ARROW.replace('width="30" height="30"', 'width="54" height="54"')
    return f"""<div class='visual'><div class='card' style='padding:40px'>
  <div style='display:flex;justify-content:space-between;align-items:center'><span class='rot'>Remessa</span><span class='tag'>Exemplo</span></div>
  <div style='display:flex;align-items:center;justify-content:space-between;margin-top:26px'>
    <div><div class='rot'>Você mandou</div><div style='font-size:62px;margin-top:6px'>{brl(50000, centavos=False)}</div></div>
    <div style='color:{BRAND}'>{seta}</div>
    <div style='text-align:right'><div class='rot'>Chegou lá fora</div><div style='font-size:62px;margin-top:6px'>{usd(10000, centavos=False)}</div></div>
  </div>
  <div style='margin-top:30px;padding-top:24px;border-top:1px solid {FIO};display:flex;justify-content:space-between'><span class='rot'>Câmbio da remessa</span><span style='font-size:36px'>{brl(5)}</span></div>
</div><div class='nota'>Exemplo simplificado, sem IOF e tarifas.</div></div>"""

def v_um_ano():
    return f"""<div class='visual' style='display:grid;grid-template-columns:1fr 1fr;gap:22px'>
  <div class='card' style='padding:36px'><div class='rot'>Carteira lá fora</div><div style='font-size:58px;margin-top:8px'>{usd(11000, centavos=False)}</div><div style='margin-top:16px'><span class='selo ok'>↑ 10% em dólar</span></div></div>
  <div class='card' style='padding:36px'><div class='rot'>Dólar hoje</div><div style='font-size:58px;margin-top:8px'>{brl(4.60)}</div><div style='margin-top:16px'><span class='selo red'>↓ 8% desde a remessa</span></div></div>
</div><div class='nota'>Exemplo simplificado, sem IOF e tarifas.</div>"""

def v_conta_reais():
    return f"""<div class='visual'><div class='card' style='padding:40px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding-bottom:20px;border-bottom:1px solid {FIO}'><span style='font-size:34px;font-weight:600'>{usd(11000, centavos=False)} × {brl(4.60)}</span><span style='font-size:48px'>{brl(50600, centavos=False)}</span></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding:20px 0;border-bottom:1px solid {FIO}'><span style='font-size:34px;font-weight:500;color:{MUTED}'>Você mandou</span><span style='font-size:48px'>{brl(-50000, sinal=True, centavos=False)}</span></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;padding-top:22px'><span style='font-size:36px;font-weight:700'>Ganho em reais</span><span style='font-size:60px;color:{BRAND_DARK}'>{brl(600, sinal=True, centavos=False).replace("class='val'", "class='val' style='color:"+BRAND_DARK+"'")}</span></div>
</div><div class='nota'>Exemplo simplificado, sem IOF e tarifas.</div></div>"""

def v_cascata_valores():
    base, vmin, vmax = 250, 44000, 55000
    def y(v):
        return base - (v - vmin) * 240 / (vmax - vmin)
    cols = [("Você enviou", base, y(50000), NEUTRO, brl(50000, centavos=False), True),
            ("Rendimento", y(50000), y(54600), BRAND_DARK, brl(4600, sinal=True, centavos=False), False),
            ("Efeito do câmbio", y(50600), y(54600), CORAL, brl(-4000, sinal=True, centavos=False), False),
            ("Hoje", base, y(50600), BRAND, brl(50600, centavos=False), True)]
    barras, rotulos = "", ""
    niveis = [y(50000), y(54600), y(50600)]
    for i, (nome, fundo, topo, cor, txt, quebra) in enumerate(cols):
        x = 20 + i * 215
        barras += f"<rect x='{x}' y='{topo:.1f}' width='150' height='{fundo - topo:.1f}' rx='12' fill='{cor}'/>"
        if quebra:  # eixo não começa no zero: marca de quebra na barra
            barras += f"<path d='M {x-4} {base-38} L {x+154} {base-58} M {x-4} {base-26} L {x+154} {base-46}' stroke='#fff' stroke-width='7'/>"
        if i < 3:
            barras += f"<line x1='{x+150}' y1='{niveis[i]:.1f}' x2='{x+215}' y2='{niveis[i]:.1f}' stroke='{MUTED}' stroke-width='2' stroke-dasharray='5 6'/>"
        rotulos += f"<div style='width:215px;text-align:center'><div style='font-size:32px'>{txt}</div><div class='rot' style='font-size:23px;margin-top:6px'>{nome}</div></div>"
    return f"""<div class='visual'><div class='card' style='padding:34px 26px 28px'>
  <div style='display:flex;justify-content:space-between;align-items:center;padding:0 14px 10px'><span class='rot'>Resultado em reais</span><span class='tag'>Exemplo</span></div>
  <svg width="100%" viewBox="0 0 860 260" fill="none"><line x1="10" y1="251" x2="850" y2="251" stroke="{FIO}" stroke-width="2"/>{barras}</svg>
  <div style='display:flex;margin-top:14px'>{rotulos}</div>
</div><div class='nota'>Rendimento: US$&nbsp;1.000 × R$&nbsp;4,60. Câmbio: US$&nbsp;10.000 × (R$&nbsp;4,60&nbsp;−&nbsp;R$&nbsp;5,00). Eixo a partir de R$&nbsp;44 mil.</div></div>"""

def v_remessas_produto():
    return f"""<div class='visual'><div class='card' style='padding:36px 40px'>
  <div style='display:flex;align-items:center;gap:18px'>{azul(I_GLOBE, 60, 30)}<span style='font-size:34px;font-weight:700;letter-spacing:-.02em'>Remessas · USD</span><span class='tag' style='margin-left:auto'>Exemplo</span></div>
  <div class='rot' style='margin-top:26px'>Na carteira hoje</div>
  <div style='font-size:72px;margin-top:4px'>{usd(11000)}</div>
  <div style='display:flex;gap:12px;margin-top:16px'><span class='selo ok'>+10,0% em US$</span><span class='selo ok'>+1,2% em R$</span></div>
  <div style='margin-top:26px;padding-top:22px;border-top:1px solid {FIO};display:grid;grid-template-columns:1fr 1fr;row-gap:14px;font-size:28px'>
    <span style='color:{MUTED}'>Rendimento</span><span style='text-align:right'>{brl(4600, sinal=True, centavos=False)}</span>
    <span style='color:{MUTED}'>Efeito do câmbio</span><span style='text-align:right'>{brl(-4000, sinal=True, centavos=False)}</span>
    <span style='color:{MUTED}'>Cotação</span><span style='text-align:right;font-weight:600'>PTAX · Banco Central</span>
  </div>
</div></div>"""

def post2():
    T = 7
    s = []
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Investimento no exterior</div>
<div class='h1'>Rendeu 10% em dólar.</div>
<div class='lead'>Quanto você ganhou <span class='accent'>em reais?</span></div>{v_dois_numeros()}""", 1, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O exemplo</div>
<div class='h3'>Você mandou R$&nbsp;50.000 com o dólar a R$&nbsp;5,00.</div>
<div class='p' style='margin-top:24px'>A remessa virou US$&nbsp;10.000 na sua conta lá fora.</div>{v_conversao()}""", 2, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Um ano depois</div>
<div class='h3'>A carteira subiu 10%. O dólar caiu 8%.</div>
<div class='p' style='margin-top:24px'>Seus US$&nbsp;10.000 viraram US$&nbsp;11.000. Mas cada dólar agora vale R$&nbsp;4,60.</div>{v_um_ano()}""", 3, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta em reais</div>
<div class='h2'>Em reais, o ganho foi de 1,2%.</div>
<div class='p' style='margin-top:24px'>Você mandou R$&nbsp;50.000 e hoje tem R$&nbsp;50.600.</div>{v_conta_reais()}""", 4, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Para onde foi o resto</div>
<div class='h3'>O investimento rendeu. O câmbio levou quase tudo de volta.</div>{v_cascata_valores()}""", 5, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>Essa conta é automática, remessa por remessa.</div>
<div class='p' style='margin-top:24px;font-size:36px'>Cada remessa na sua data, com a cotação PTAX do Banco Central. Rendimento e câmbio separados, em dólar e em real.</div>{v_remessas_produto()}""", 6, T))
    s.append(slide("green", f"""
<div class='h2'>Seu dinheiro lá fora, em dólar e em real.</div>
<div class='lead'>Acesse pelo navegador, no computador ou no celular.</div>{v_cta_pill()}""", 7, T))
    return s

# ================================================================= POST 3 · sábado 03/10 · simulação
MESES = ["Out/26", "Nov/26", "Dez/26", "Jan/27", "Fev/27", "Mar/27"]
BASE = [14180, 16360, 18540, 15920, 18100, 20280]
CARRO = [14180, 14760, 15340, 11120, 11700, 12280]

def _curva(vals, x0=60, x1=800, y0=230, y1=30, vmin=10000, vmax=21000):
    pts = []
    for i, v in enumerate(vals):
        x = x0 + (x1 - x0) * i / (len(vals) - 1)
        y = y0 - (v - vmin) / (vmax - vmin) * (y0 - y1)
        pts.append((x, y))
    return pts

def v_projecao(marcar_jan=True, capa=False):
    pts = _curva(BASE)
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    area = d + f" L {pts[-1][0]:.1f} 250 L {pts[0][0]:.1f} 250 Z"
    pontos = "".join(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='9' fill='{AMBER if (i == 3 and marcar_jan) else BRAND}' stroke='#fff' stroke-width='4'/>" for i, (x, y) in enumerate(pts))
    meses = "".join(f"<span style='width:148px;text-align:center'>{m}</span>" for m in MESES)
    jx, jy = pts[3]
    aviso = f"<g><rect x='{jx-150:.0f}' y='{jy+26:.0f}' width='300' height='48' rx='24' fill='#FBF1DC'/><text x='{jx:.0f}' y='{jy+58:.0f}' text-anchor='middle' font-family='Inter' font-size='23' font-weight='700' fill='{AMBER_TEXT}'>IPVA e IPTU apertam</text></g>" if marcar_jan else ""
    return f"""<div class='visual'><div class='card' style='padding:34px 30px 26px'>
  <div style='display:flex;justify-content:space-between;align-items:center;padding:0 10px 8px'><span class='rot'>Saldo projetado</span><span class='tag'>Exemplo</span></div>
  <svg width="100%" viewBox="0 0 860 300" fill="none">
    <path d="{d}" stroke="{BRAND}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{'0' if not capa else '16 12'}"/>
    {pontos}{aviso}
  </svg>
  <div style='display:flex;justify-content:space-between;padding:0 4px;font-size:24px;font-weight:600;color:{MUTED}'>{meses}</div>
</div></div>"""

def v_recorrentes():
    itens = [(I_UP, "Salário", 9960), (I_HOME, "Aluguel", -2300), (I_BOOK, "Escola", -1450), (I_CARD, "Parcela do cartão", -249.90), (I_PLAY, "Assinaturas", -119.80)]
    linhas = "".join(f"""<div class='linha'>{azul(p, 56, 28)}<div style='flex:1;font-size:31px;font-weight:600'>{n}</div><span class='selo ok' style='height:36px;font-size:21px'>todo mês</span><div style='font-size:34px;width:250px;text-align:right'>{brl(v, sinal=True)}</div></div>""" for p, n, v in itens)
    return f"""<div class='visual'><div class='card' style='padding:22px 40px 12px'>
  <div style='display:flex;justify-content:space-between;align-items:center;padding-bottom:4px'><span class='rot'>O que já está escrito</span><span class='tag'>Exemplo</span></div>{linhas}</div></div>"""

def v_cenarios():
    pb, pc = _curva(BASE), _curva(CARRO)
    db = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pb)
    dc = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pc)
    meses = "".join(f"<span style='width:148px;text-align:center'>{m}</span>" for m in MESES)
    return f"""<div class='visual'><div class='card' style='padding:34px 30px 26px'>
  <div style='display:flex;justify-content:space-between;align-items:center;padding:0 10px 8px'><span class='rot'>Dois cenários lado a lado</span><span class='tag'>Exemplo</span></div>
  <svg width="100%" viewBox="0 0 860 260" fill="none">
    <path d="{db}" stroke="{BRAND}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="{dc}" stroke="{CORAL}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="14 12"/>
  </svg>
  <div style='display:flex;justify-content:space-between;padding:0 4px;font-size:24px;font-weight:600;color:{MUTED}'>{meses}</div>
  <div style='margin-top:24px;padding:22px 10px 0;border-top:1px solid {FIO};display:grid;grid-template-columns:1fr auto;row-gap:14px;font-size:30px;align-items:center'>
    <span style='display:flex;align-items:center;gap:14px;font-weight:600'><i style='width:34px;height:6px;border-radius:3px;background:{BRAND}'></i>Cenário base</span><span>{brl(20280, centavos=False)} em Mar/27</span>
    <span style='display:flex;align-items:center;gap:14px;font-weight:600'><i style='width:34px;height:6px;border-radius:3px;background:{CORAL}'></i>Trocar de carro</span><span>{brl(12280, centavos=False)} em Mar/27</span>
  </div>
</div></div>"""

def post3():
    T = 5
    s = []
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Outubro começou</div>
<div class='h1'>Você já sabe como ele termina?</div>
<div class='lead'>E novembro, dezembro, janeiro...</div>{v_projecao(marcar_jan=False, capa=True)}""", 1, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O que você já sabe</div>
<div class='h2'>A maior parte do mês é previsível.</div>
<div class='p' style='margin-top:24px'>Salário, aluguel, escola, parcelas, assinaturas. Isso já dá para escrever hoje.</div>{v_recorrentes()}""", 2, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Simulação de fluxo futuro</div>
<div class='h3'>Monte um cenário. Veja o saldo mês a mês, antes de acontecer.</div>
<div class='p' style='margin-top:24px;font-size:36px'>O timtimcash projeta até cinco anos à frente, e o mês que vai apertar aparece com antecedência.</div>{v_projecao()}""", 3, T))
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>E se...?</div>
<div class='h3'>Teste a decisão antes de tomar.</div>
<div class='p' style='margin-top:24px;font-size:36px'>Crie outro cenário, com a parcela do carro novo ou o aluguel maior, e compare lado a lado.</div>{v_cenarios()}""", 4, T))
    s.append(slide("green", f"""
<div class='h2'>Veja o fim do ano antes de ele chegar.</div>
<div class='lead'>Simulação de fluxo futuro no timtimcash. Acesse pelo navegador, no computador ou no celular.</div>{v_cta_pill()}""", 5, T))
    return s

POSTS = {
    "2026-09-30_hoje-o-mes-fecha": post1,
    "2026-10-02_rendeu-em-dolar-e-em-reais": post2,
    "2026-10-03_outubro-comecou": post3,
}
