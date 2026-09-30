# -*- coding: utf-8 -*-
"""Carrosséis de 15/10, 19/10 e 26/10 de 2026 (equipe carrosseis-a), no formato do modelo aprovado
gerador/semanas/2026-10-05_v2.py (capas capa_*, recorte e NOTA_TELA).

Números conferidos com gerador/telas/LEIAME.md e com o código do site (cópia do kit em carrosseis-a/app):
- Reserva do Diagnóstico (calcDiagnostico): totalGeral() ÷ despesa média mensal da janela (12 meses antes
  do mês atual, sem os meses sem lançamento): R$ 104.180 ÷ R$ 8.342,27 = 12,5 meses. Meta padrão: 6 meses.
- Saldos: Conta corrente R$ 14.180; Reserva R$ 30.000; Corretora no exterior R$ 60.000 (pelo custo das remessas).
  Só o que está à mão: R$ 44.180 ÷ R$ 8.342,27 = 5,3 meses.
- Cartão (acrescentado só na cópia do kit, sem compras): fecha no dia 3, vence no dia 10. Compra em 02/10 cai
  na fatura de 10/out; em 04/10, na de 10/nov (calcFaturaDaCompra: depois do dia de fechamento, próxima fatura).
- Parcelada: 2 a 120 parcelas, o valor digitado é o total; R$ 2.499 em 10× = R$ 249,90.
"""
import os as _os
import re as _re
from artes import *

TELAS = "/home/claude/timtimcash-social/gerador/telas"
O = "/tmp/claude-0/-home-claude-timtimcash-social/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/outubro"
SAIDA = _os.path.join(O, "saida")

P15 = "2026-10-15_reserva-em-meses"
P19 = "2026-10-19_cartao-fechamento-e-vencimento"
P26 = "2026-10-26_parcela-que-cabe-hoje"

CORAL_TXT = "#B4532F"    # coral escuro: texto pequeno em coral (4,8:1 sobre o papel)
CORAL_FORTE = "#9A3F22"  # números grandes das despesas somadas
CORAL_CLARO = "#EBAA90"

def tela_repo(nome):
    return _os.path.join(TELAS, nome)

def tela_nova(pasta, nome):
    return _os.path.join(SAIDA, pasta, "telas", nome)

def sem_quebra(html):
    """Não separa "R$" do número, nem o número da unidade (meses, dias), no fim de uma linha."""
    html = html.replace("R$ ", "R$\u00a0").replace("\u00e0 m\u00e3o", "\u00e0\u00a0m\u00e3o")
    html = _re.sub(r"(\d) (meses|mês|dias|dia)\b", "\\1\u00a0\\2", html)
    html = _re.sub(r"\b(dia|dias) (\d)", "\\1\u00a0\\2", html)
    return html

EXTRA = f"""<style>
.nota{{margin-top:18px;font-size:24px;font-weight:500;color:{MUTED}}}
.sombra{{box-shadow:0 1px 2px rgba(15,20,16,.05),0 22px 48px -22px rgba(15,20,16,.30)}}
.rot{{font-size:28px;font-weight:600;color:{MUTED}}}
.big{{font-weight:700;letter-spacing:-.04em;font-variant-numeric:tabular-nums;color:{INK}}}
.fio{{height:2px;background:{FIO}}}
</style>"""

def recorte(caminho, y0, y1, largura=760, x0=0, x1=None):
    """Recorte real de uma tela (caminho absoluto): mostra a faixa [y0, y1) da imagem original na largura dada."""
    from PIL import Image
    w = Image.open(caminho).size[0]
    x1 = x1 or w
    esc = largura / (x1 - x0)
    alt = (y1 - y0) * esc
    return f"""<div class='sombra' style='width:{largura}px;height:{alt:.0f}px;overflow:hidden;border-radius:24px;background:#fff;border:1px solid {FIO};margin:0 auto'>
  <img src="file://{caminho}" style='display:block;width:{w * esc:.1f}px;height:auto;margin-top:{-y0 * esc:.1f}px;margin-left:{-x0 * esc:.1f}px'></div>"""

NOTA_TELA = "<div class='nota' style='text-align:center'>Tela real do timtimcash, com dados de exemplo.</div>"

# ---------------------------------------------------------------- capas (mesma estrutura do modelo)
EXTRA_CAPA = f"""<style>
.dark{{background:{INK};color:#fff}}
.dark .count,.dark .foot{{color:#C9D1C8}}
.dark .eyebrow{{color:{MENTA}}}
.soft{{background:{SOFT};color:{INK}}}
.soft .count,.soft .foot{{color:{BRAND_DEEP}}}
.soft .eyebrow{{color:{BRAND_DEEP}}}
</style>"""

def capa_page(tema, corpo, idx, total, logo_var):
    head = f"<div class='head'><div class='brand'>{logo_horizontal(logo_var, 44)}</div><div class='count'>{idx}/{total}</div></div>"
    return page(EXTRA + EXTRA_CAPA + head + f"<div class='body'>{corpo}</div>" + footer(), tema)

def fechamento_verde(titulo, lead, idx, total):
    return slide("green", EXTRA + f"""
<div class='h2'>{titulo}</div>
<div class='lead'>{lead}</div>{v_cta_pill()}""", idx, total)

def svg_icone(caminhos, tam=42, cor=BRAND_DARK, traco=2):
    return f"<svg width='{tam}' height='{tam}' viewBox='0 0 24 24' fill='none' stroke='{cor}' stroke-width='{traco}' stroke-linecap='round' stroke-linejoin='round'>{caminhos}</svg>"

I_CAL = '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'
I_CLOCK = '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>'
I_ALERT = '<path d="M12 4 21 19.5H3z"/><path d="M12 10v4.2M12 17.2v.1"/>'
I_QUEDA = '<path d="M3 7l6 6 4-4 8 8"/><path d="M21 12v5h-5"/>'
I_EYE = '<path d="M2.5 12C4 8.5 7.5 6 12 6s8 2.5 9.5 6c-1.5 3.5-5 6-9.5 6s-8-2.5-9.5-6z"/><circle cx="12" cy="12" r="2.8"/>'

def brl(v, cent=True):
    s = f"{v:,.2f}" if cent else f"{v:,.0f}"
    return "R$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")

def num(v):
    return brl(v).replace("R$ ", "")

# ================================================================ 15/10 · reserva de emergência em meses
PATRIMONIO = 104180.00
MEDIA_DESP = 8342.27               # média de out/25 a ago/26 (11 meses com lançamentos na janela de 12)
CONTA_CORRENTE, RESERVA_CONTA, EXTERIOR = 14180.00, 30000.00, 60000.00
A_MAO = CONTA_CORRENTE + RESERVA_CONTA
assert CONTA_CORRENTE + RESERVA_CONTA + EXTERIOR == PATRIMONIO
assert round(PATRIMONIO / MEDIA_DESP, 1) == 12.5
assert round(A_MAO / MEDIA_DESP, 1) == 5.3

def capa_reserva(T):
    n, cheias = 13, 12
    def pil(i):
        alt = 100 if i <= cheias else 50
        return (f"<div style='flex:1;height:150px;border-radius:18px;background:#fff;position:relative;overflow:hidden;"
                f"box-shadow:0 1px 2px rgba(6,95,70,.10),0 16px 30px -20px rgba(6,95,70,.55)'>"
                f"<i style='position:absolute;left:0;right:0;bottom:0;height:{alt}%;background:{BRAND};display:block'></i></div>")
    rotulos = {1: "1", 6: "6", 12: "12"}
    marcas = "".join(f"<div style='flex:1;text-align:center;font-size:28px;font-weight:700;color:{BRAND_DEEP};font-variant-numeric:tabular-nums'>{rotulos.get(i, '')}</div>" for i in range(1, n + 1))
    corpo = f"""<div class='eyebrow'>Reserva de emergência</div>
<div class='h1' style='font-size:100px'>Quantos meses você aguentaria?</div>
<div style='display:flex;align-items:baseline;gap:22px;margin-top:60px'>
  <span class='big' style='font-size:230px;line-height:.9;letter-spacing:-.055em'>12,5</span>
  <span style='font-size:64px;font-weight:700;letter-spacing:-.03em;color:{BRAND_DEEP}'>meses</span></div>
<div style='display:flex;gap:12px;margin-top:64px'>{''.join(pil(i) for i in range(1, n + 1))}</div>
<div style='display:flex;gap:12px;margin-top:16px'>{marcas}</div>"""
    return capa_page("soft", corpo, 1, T, "color")

def linha_meses(rot, meses, cor):
    blocos = "".join(f"<div style='flex:1;height:58px;border-radius:12px;background:{BRAND if i < meses else FIO}'></div>" for i in range(12))
    return f"""<div style='padding:30px 0 34px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline;gap:20px'>
    <span style='font-size:34px;font-weight:600;color:{INK}'>{rot}</span>
    <span class='big' style='font-size:56px;color:{cor}'>{meses} meses</span></div>
  <div style='display:flex;gap:8px;margin-top:22px'>{blocos}</div></div>"""

def post_reserva():
    T = 7
    s = [capa_reserva(T)]

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Por que em meses</div>
<div class='h2'>O mesmo dinheiro pode durar 10 meses ou 3.</div>
<div class='p'>Depende de quanto você gasta. Por isso a reserva se mede em meses de gasto, não em reais.</div>
<div class='visual'><div class='card' style='padding:6px 48px'>
  {linha_meses('Gasta R$ 3.000 por mês', 10, BRAND_DARK)}
  <div class='fio'></div>
  {linha_meses('Gasta R$ 10.000 por mês', 3, INK)}
</div><div class='nota'>Exemplo: R$ 30.000 guardados nos dois casos. Cada bloco é um mês.</div></div>""", 2, T))

    conta = f"""<div class='visual'><div class='card' style='padding:44px 48px'>
  <div style='display:flex;align-items:flex-end;justify-content:space-between;gap:16px'>
    <div><div class='rot'>Patrimônio</div><div class='big' style='font-size:60px;margin-top:6px'>R$ 104.180</div></div>
    <div class='big' style='font-size:60px;color:{MUTED}'>÷</div>
    <div><div class='rot'>Despesa média por mês</div><div class='big' style='font-size:60px;margin-top:6px'>R$ 8.342,27</div></div>
  </div>
  <div class='fio' style='margin:34px 0 28px'></div>
  <div style='display:flex;align-items:center;justify-content:space-between'>
    <div class='rot'>Reserva</div><div class='big' style='font-size:84px;color:{BRAND_DARK}'>12,5 meses</div>
  </div>
</div><div class='nota'>Exemplo com a conta dos outros posts. Patrimônio: as contas incluídas no total. Média: os 12 meses anteriores, sem os meses vazios.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta</div>
<div class='h2'>Patrimônio dividido pela despesa média.</div>
<div class='p'>É a conta que o Diagnóstico do timtimcash faz.</div>{conta}""", 3, T))

    listra = f"repeating-linear-gradient(135deg,{NEUTRO} 0 12px,#E6E3DA 12px 24px)"
    frac = A_MAO / PATRIMONIO * 100
    def grupo(rot, cor_rot, valor, sub):
        return f"""<div><div style='font-size:26px;font-weight:700;color:{cor_rot}'>{rot}</div>
  <div class='big' style='font-size:44px;margin-top:4px'>{valor}</div>
  <div style='font-size:24px;font-weight:500;color:{MUTED};margin-top:2px'>{sub}</div></div>"""
    barra = f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:38px 44px 36px'>
  <div style='display:flex;height:56px;border-radius:14px;overflow:hidden;gap:5px'>
    <div style='flex:{CONTA_CORRENTE:.0f};background:{BRAND}'></div>
    <div style='flex:{RESERVA_CONTA:.0f};background:{BRAND_DARK}'></div>
    <div style='flex:{EXTERIOR:.0f};background:{listra}'></div></div>
  <div style='display:flex;margin-top:20px'>
    <div style='width:{frac:.1f}%'>{grupo('À mão', BRAND_DARK, 'R$ 44.180', 'conta corrente e reserva')}</div>
    <div style='flex:1;padding-left:12px'>{grupo('Demora a virar dinheiro', MUTED, 'R$ 60.000', 'corretora no exterior')}</div>
  </div>
  <div class='fio' style='margin:30px 0 26px'></div>
  <div style='display:flex;gap:24px'>
    <div style='flex:1'><div class='rot'>Com tudo</div><div class='big' style='font-size:60px;margin-top:4px'>12,5 meses</div></div>
    <div style='flex:1'><div class='rot'>Só o que está à mão</div><div class='big' style='font-size:60px;margin-top:4px;color:{BRAND_DARK}'>5,3 meses</div>
      <div style='font-size:24px;font-weight:700;color:{AMBER_TEXT};margin-top:6px'>abaixo da meta de 6 meses</div></div>
  </div>
</div><div class='nota'>Exemplo: R$ 44.180 ÷ R$ 8.342,27 = 5,3 meses.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Liquidez</div>
<div class='h2'>Nem todo patrimônio é reserva.</div>
<div class='p' style='margin-top:26px'>Na emergência, vale o que está à mão. Dinheiro lá fora ou num imóvel pode demorar a virar dinheiro.</div>{barra}""", 4, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>O Diagnóstico mostra a sua reserva em meses.</div>
<div class='p' style='margin-top:20px;font-size:36px'>Em Relatórios, ao lado da meta. Ela começa em 6 meses e você ajusta em “Como o diagnóstico é calculado”.</div>
<div class='visual' style='margin-top:44px'>{recorte(tela_repo('secoes/celular-relatorios-diagnostico.jpg'), 1270, 1745, largura=860, x0=6, x1=1080)}{NOTA_TELA}</div>""", 5, T))

    def item(ip, t, sub, ultimo=False):
        icone = f"<div class='azulejo' style='width:84px;height:84px;flex:none'>{svg_icone(ip)}</div>"
        return f"""<div style='display:flex;gap:30px;align-items:center;padding:30px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>{icone}
  <div><div style='font-size:38px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{t}</div><div style='font-size:28px;color:{MUTED};margin-top:8px;line-height:1.3'>{sub}</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>E se a renda parar?</div>
<div class='h2'>Depois, ponha a reserva à prova.</div>
<div class='p' style='margin-top:28px'>Meses de reserva são uma média. O “E se...” da Simulação futura mostra o caminho, mês a mês.</div>
<div class='visual' style='margin-top:44px'><div class='card' style='padding:6px 44px'>
  {item(I_QUEDA, '“Perde a maior renda”', 'A maior receita zera nos 6 primeiros meses.')}
  {item(I_CAL, 'Mês a mês, não pela média', 'Os meses mais caros do cenário entram na conta.')}
  {item(I_EYE, 'Sem alterar nada', 'O teste é só uma leitura sobre o seu cenário.', True)}
</div></div>""", 6, T))

    s.append(fechamento_verde("Saiba quantos meses você aguentaria.",
        "Relatórios e Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 7, T))
    return [sem_quebra(h) for h in s]

# ================================================================ 19/10 · cartão: fechamento, vencimento e melhor dia
FECHA, VENCE = 3, 10

def capa_cartao(T):
    cels = []
    for d in range(1, 32):
        if d == FECHA:
            bola = f"background:{INK};color:#fff"
        elif d == FECHA + 1:
            bola = f"background:{BRAND};color:#fff;box-shadow:0 0 0 8px {SOFT}"
        elif d == VENCE:
            bola = f"background:#fff;color:{CORAL_TXT};box-shadow:inset 0 0 0 5px {CORAL}"
        else:
            bola = f"color:{MUTED}"
        forte = d in (FECHA, FECHA + 1, VENCE)
        cels.append(f"<div style='display:flex;align-items:center;justify-content:center;height:92px'>"
                    f"<span style='width:78px;height:78px;border-radius:50%;display:flex;align-items:center;justify-content:center;"
                    f"font-size:34px;font-weight:{700 if forte else 500};font-variant-numeric:tabular-nums;{bola}'>{d}</span></div>")
    def leg(estilo, txt, cor=INK):
        return f"<span style='display:flex;align-items:center;gap:12px;font-size:28px;font-weight:700;color:{cor}'><i style='width:26px;height:26px;border-radius:50%;display:block;{estilo}'></i>{txt}</span>"
    argolas = "".join(f"<i style='position:absolute;top:-16px;left:{x};width:18px;height:44px;border-radius:9px;background:{INK};display:block'></i>" for x in ("22%", "76%"))
    cal = f"""<div class='card' style='position:relative;margin-top:54px;padding:0;overflow:visible'>
  {argolas}
  <div style='height:30px;border-radius:28px 28px 0 0;background:{FIO}'></div>
  <div style='padding:22px 34px 8px;display:grid;grid-template-columns:repeat(7,1fr);row-gap:4px'>{''.join(cels)}</div>
  <div style='display:flex;justify-content:center;gap:34px;padding:10px 30px 34px;border-top:2px solid {FIO};margin:14px 34px 0'>
    {leg(f'background:{INK}', 'fecha')}{leg(f'background:{BRAND}', 'melhor dia', BRAND_DARK)}{leg(f'background:#fff;box-shadow:inset 0 0 0 5px {CORAL}', 'vence')}
  </div>
</div>"""
    corpo = f"""<div class='eyebrow'>Cartão de crédito</div>
<div class='h1' style='font-size:100px'>Qual é o melhor dia de compra?</div>{cal}"""
    return capa_page("light", corpo, 1, T, "color")

def v_timeline():
    """Linha do tempo de 1/10 a 10/11: a compra do dia 2 e a do dia 4, com os fechamentos marcados."""
    W = 808
    x = lambda d: (d - 1) / 40 * W          # d = 1 é 1/10; d = 41 é 10/11
    NOV, FO, FN = x(32), x(3), x(34)
    def marca_fecha(px, y):
        return f"<i style='position:absolute;left:{px:.1f}px;top:{y}px;width:6px;height:40px;border-radius:3px;background:{INK};transform:translate(-50%,-50%);box-shadow:0 0 0 3px #fff;display:block;z-index:3'></i>"
    def linha(y, d0, d1, cor, rot, dias, cor_dias, fim):
        x0, x1 = x(d0), x(d1)
        yb = y + 78
        return f"""
<div style='position:absolute;left:0;top:{y}px;width:{W}px;display:flex;justify-content:space-between;align-items:baseline'>
  <span style='font-size:30px;font-weight:700;color:{INK}'>{rot}</span>
  <span><span class='big' style='font-size:46px;color:{cor_dias}'>{dias}</span><span style='font-size:24px;font-weight:600;color:{MUTED};margin-left:10px'>para pagar</span></span></div>
<div style='position:absolute;left:0;top:{yb - 3}px;width:{W}px;height:6px;border-radius:3px;background:{FIO}'></div>
<div style='position:absolute;left:{x0:.1f}px;top:{yb - 9}px;width:{x1 - x0:.1f}px;height:18px;border-radius:9px;background:{cor}'></div>
{marca_fecha(FO, yb)}{marca_fecha(FN, yb)}
<i style='position:absolute;left:{x0:.1f}px;top:{yb}px;width:32px;height:32px;border-radius:50%;background:#fff;border:7px solid {cor};transform:translate(-50%,-50%);box-sizing:border-box;display:block;z-index:4'></i>
<i style='position:absolute;left:{x1:.1f}px;top:{yb}px;width:32px;height:32px;border-radius:50%;background:{CORAL};border:6px solid #fff;box-shadow:0 0 0 2px {CORAL};transform:translate(-50%,-50%);box-sizing:border-box;display:block;z-index:4'></i>
<div style='position:absolute;left:{x1:.1f}px;top:{yb + 26}px;transform:translateX({'-100%' if x1 > W - 90 else '-50%'});font-size:24px;font-weight:700;color:{CORAL_TXT};white-space:nowrap'>{fim}</div>"""
    return f"""<div class='visual' style='margin-top:46px'><div class='card' style='padding:30px 44px 30px'>
  <div style='position:relative;height:74px'>
    <div style='position:absolute;left:0;top:0;font-size:22px;font-weight:700;letter-spacing:.14em;color:{MUTED}'>OUTUBRO</div>
    <div style='position:absolute;left:{NOV + 6:.1f}px;top:0;font-size:22px;font-weight:700;letter-spacing:.14em;color:{MUTED}'>NOVEMBRO</div>
    <div style='position:absolute;left:0;top:34px;width:{NOV - 3:.1f}px;height:8px;border-radius:4px;background:{FIO}'></div>
    <div style='position:absolute;left:{NOV + 3:.1f}px;top:34px;width:{W - NOV - 3:.1f}px;height:8px;border-radius:4px;background:{FIO}'></div>
  </div>
  <div style='position:relative;height:330px'>
    <div style='position:absolute;left:{FO - 3:.1f}px;top:0;font-size:22px;font-weight:700;color:{INK};white-space:nowrap'>fecha 3/10</div>
    <div style='position:absolute;left:{FN:.1f}px;top:0;transform:translateX(-50%);font-size:22px;font-weight:700;color:{INK};white-space:nowrap'>fecha 3/11</div>
    {linha(46, 2, 10, MUTED, 'Compra no dia 2', '8 dias', INK, 'vence 10/10')}
    {linha(196, 4, 41, BRAND, 'Compra no dia 4', '37 dias', BRAND_DARK, 'vence 10/11')}
  </div>
</div><div class='nota'>Exemplo: cartão que fecha no dia 3 e vence no dia 10.</div></div>"""

def post_cartao():
    T = 6
    s = [capa_cartao(T)]

    def linha(ip, titulo, sub, dia, ultimo=False):
        return f"""<div style='display:flex;gap:30px;align-items:center;padding:34px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div class='azulejo' style='width:92px;height:92px;flex:none'>{svg_icone(ip, 46)}</div>
  <div style='flex:1'><div style='font-size:40px;font-weight:700;letter-spacing:-.03em'>{titulo}</div>
    <div style='font-size:29px;color:{MUTED};margin-top:8px;line-height:1.32'>{sub}</div></div>
  <div style='flex:none;text-align:right'><div class='rot' style='font-size:24px'>dia</div><div class='big' style='font-size:88px;line-height:.95'>{dia}</div></div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>As duas datas</div>
<div class='h2'>Duas datas mandam na sua fatura.</div>
<div class='visual' style='margin-top:52px'><div class='card' style='padding:6px 44px'>
  {linha(I_CAL, 'Fechamento', 'O dia em que a fatura fecha. O que você compra depois dele vai para a próxima.', FECHA)}
  {linha(I_CLOCK, 'Vencimento', 'O dia de pagar a fatura que fechou.', VENCE, True)}
</div><div class='nota'>Exemplo: um cartão que fecha no dia 3 e vence no dia 10.</div></div>""", 2, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Dia 2 ou dia 4?</div>
<div class='h2'>Dois dias na compra, um mês no pagamento.</div>
<div class='p' style='margin-top:28px'>A compra do dia 2 entra na fatura que fecha no dia 3. A do dia 4 já fica para a próxima.</div>{v_timeline()}""", 3, T))

    def dia_faixa(d):
        if d == FECHA:
            estilo, cor = f"background:{INK};color:#fff", "#fff"
        elif d == FECHA + 1:
            estilo, cor = f"background:{BRAND};color:#fff;box-shadow:0 0 0 8px {SOFT}", "#fff"
        else:
            estilo, cor = f"color:{MUTED}", MUTED
        acima = f"<div style='height:34px;font-size:24px;font-weight:700;color:{INK}'>{'fecha' if d == FECHA else ''}</div>"
        abaixo = f"<div style='height:34px;font-size:24px;font-weight:700;color:{BRAND_DARK};white-space:nowrap'>{'melhor dia' if d == FECHA + 1 else ''}</div>"
        return f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:10px'>{acima}
  <span style='width:76px;height:76px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:{700 if d in (FECHA, FECHA + 1) else 500};font-variant-numeric:tabular-nums;{estilo}'>{d}</span>{abaixo}</div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>O melhor dia de compra</div>
<div class='h2'>É o dia seguinte ao fechamento.</div>
<div class='visual' style='margin-top:44px'><div class='card' style='padding:24px 28px 22px;display:flex'>{''.join(dia_faixa(d) for d in range(1, 9))}</div></div>
<div class='p' style='margin-top:40px'>A compra vai para a fatura seguinte: é a que demora mais para ser cobrada. E prazo maior não é desconto: o valor é o mesmo.</div>
<div class='visual' style='margin-top:44px'><div class='card' style='padding:34px 40px;background:#FBF1DC;border-color:#F3E2BC;box-shadow:none;display:flex;gap:28px;align-items:flex-start'>
  <div style='width:80px;height:80px;border-radius:28%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none'>{svg_icone(I_ALERT, 42, AMBER_TEXT, 2.2)}</div>
  <div><div style='font-size:36px;font-weight:700;letter-spacing:-.03em;color:{INK}'>E no próprio dia do fechamento?</div>
    <div style='font-size:30px;line-height:1.38;color:{INK};margin-top:10px'>A regra varia entre os emissores. Confira as datas do seu cartão na fatura.</div></div>
</div></div>""", 4, T))

    compra = tela_nova(P19, "celular-compra-no-cartao-dia-04.jpg")
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>A compra já mostra em qual fatura vai entrar.</div>
<div class='p' style='margin-top:18px;font-size:34px'>Cada cartão tem “Fecha no dia” e “Vence no dia”. No exemplo, a compra do dia 4 vai para a fatura que vence 10/nov.</div>
<div class='visual' style='margin-top:36px'>{recorte(compra, 1244, 2019, largura=760, x0=26, x1=1144)}{NOTA_TELA}</div>""", 5, T))

    s.append(fechamento_verde("Saiba em qual fatura cada compra vai cair.",
        "Cartões de crédito no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]

# ================================================================ 26/10 · a parcela que cabe hoje
MESES = ["out", "nov", "dez", "jan", "fev", "mar", "abr", "mai", "jun", "jul"]
COMPRAS = [  # (nome, parcela, primeiro mês, nº de parcelas, cor)
    ("Geladeira", 249.90, 0, 10, CORAL),
    ("Presentes de Natal", 200.00, 2, 6, CORAL_TXT),
    ("Material escolar", 600.00, 3, 3, CORAL_CLARO),
]
assert abs(249.90 * 10 - 2499) < 0.001
def por_mes(i):
    return round(sum(p for _, p, ini, n, _ in COMPRAS if ini <= i < ini + n), 2)
TOTAIS = [por_mes(i) for i in range(10)]
assert TOTAIS == [249.90, 249.90, 449.90, 1049.90, 1049.90, 1049.90, 449.90, 449.90, 249.90, 249.90]
SOBRA = 2180.00
assert 9960 - 7780 == SOBRA
assert round(TOTAIS[3] / SOBRA * 100) == 48

def barra_empilhada(i, esc, largura):
    segs = []
    for nome, p, ini, n, cor in COMPRAS:
        if ini <= i < ini + n:
            segs.append(f"<div style='height:{p * esc:.1f}px;background:{cor};border-radius:6px'></div>")
    return f"<div style='width:{largura}px;display:flex;flex-direction:column-reverse;gap:4px'>{''.join(segs)}</div>"

def capa_parcela(T):
    esc = 0.36   # px por real
    def coluna(i, rot, valor, cor_valor):
        return f"""<div style='display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:18px'>
  <div class='big' style='font-size:58px;color:{cor_valor}'>{valor}</div>
  {barra_empilhada(i, esc, 250)}
  <div style='font-size:30px;font-weight:700;color:{INK}'>{rot}</div></div>"""
    corpo = f"""<div class='eyebrow'>Compras parceladas</div>
<div class='h1' style='font-size:92px'>A parcela cabe hoje.<br>E daqui a três meses?</div>
<div class='card' style='margin-top:52px;padding:40px 60px 34px;display:flex;justify-content:space-around;align-items:flex-end'>
  {coluna(0, 'hoje', brl(TOTAIS[0]), CORAL_TXT)}
  {coluna(3, 'em 3 meses', brl(TOTAIS[3]), CORAL_FORTE)}
</div>"""
    return capa_page("light", corpo, 1, T, "color")

def v_grafico_parcelas():
    CW, n, gap = 812, 10, 20
    colw = (CW - gap * (n - 1)) / n
    esc = 260 / max(TOTAIS)
    base = 330
    xs = [i * (colw + gap) for i in range(n)]
    el, topos = [], []
    for i in range(n):
        y = base
        for nome, p, ini, k, cor in COMPRAS:
            if ini <= i < ini + k:
                h = p * esc
                el.append(f"<div style='position:absolute;left:{xs[i]:.1f}px;top:{y - h + 4:.1f}px;width:{colw:.1f}px;height:{h - 4:.1f}px;background:{cor};border-radius:6px'></div>")
                y -= h
        topos.append(y)
        forte = 3 <= i <= 5
        el.append(f"<div style='position:absolute;left:{xs[i]:.1f}px;top:{base + 16}px;width:{colw:.1f}px;text-align:center;font-size:24px;font-weight:{800 if forte else 600};color:{INK if forte else MUTED}'>{MESES[i]}</div>")
    for i in (0, 2, 6, 9):
        el.append(f"<div style='position:absolute;left:{xs[i] + colw / 2:.1f}px;top:{topos[i] - 40:.1f}px;transform:translateX(-50%);font-size:22px;font-weight:700;color:{MUTED};font-variant-numeric:tabular-nums;white-space:nowrap'>{num(TOTAIS[i])}</div>")
    xa, xb, yt = xs[3], xs[5] + colw, topos[3] - 20
    el.append(f"<div style='position:absolute;left:{xa:.1f}px;top:{yt:.1f}px;width:{xb - xa:.1f}px;height:12px;border:3px solid {CORAL_FORTE};border-bottom:none;border-radius:8px 8px 0 0;box-sizing:border-box'></div>")
    el.append(f"<div style='position:absolute;left:{(xa + xb) / 2:.1f}px;top:{yt - 48:.1f}px;transform:translateX(-50%);font-size:34px;font-weight:700;letter-spacing:-.02em;color:{CORAL_FORTE};font-variant-numeric:tabular-nums;white-space:nowrap'>{num(TOTAIS[3])}</div>")
    return f"<div style='position:relative;height:{base + 56}px;width:{CW}px'>{''.join(el)}</div>"

def post_parcela():
    T = 6
    s = [capa_parcela(T)]

    tiles = "".join(f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:12px'>
  <div style='width:100%;height:120px;border-radius:14px;background:{CORAL}'></div>
  <div style='font-size:24px;font-weight:700;color:{MUTED}'>{m}</div></div>""" for m in MESES)
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Uma compra, dez meses</div>
<div class='h2'>A parcela é pequena. O prazo, não.</div>
<div class='p'>Uma compra de R$ 2.499 em 10× vira R$ 249,90 em cada um dos próximos 10 meses.</div>
<div class='visual'><div class='card' style='padding:40px 40px 34px'>
  <div style='display:flex;align-items:baseline;justify-content:space-between;gap:20px'>
    <div class='big' style='font-size:62px'>R$ 2.499</div>
    <div class='big' style='font-size:62px;color:{CORAL_TXT}'>10× de R$ 249,90</div></div>
  <div style='display:flex;gap:10px;margin-top:34px'>{tiles}</div>
</div><div class='nota'>Exemplo: uma geladeira comprada em outubro, em 10 parcelas mensais.</div></div>""", 2, T))

    def leg(nome, p, ini, n, cor):
        return f"""<div style='display:flex;align-items:center;gap:16px;padding:8px 0'>
  <i style='width:26px;height:26px;border-radius:7px;background:{cor};display:block;flex:none'></i>
  <span style='flex:1;font-size:28px;font-weight:600;color:{INK}'>{nome}</span>
  <span style='font-size:28px;font-weight:600;color:{MUTED};font-variant-numeric:tabular-nums'>{n}× {brl(p)} · {MESES[ini]} a {MESES[ini + n - 1]}</span></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Elas se somam</div>
<div class='h2'>Cada parcela cabe. Juntas, pesam.</div>
<div class='visual' style='margin-top:44px'><div class='card' style='padding:30px 36px 22px'>
  <div style='font-size:24px;font-weight:600;color:{MUTED};margin-bottom:6px'>Parcelas somadas em cada mês, em R$</div>
  {v_grafico_parcelas()}
  <div class='fio' style='margin:4px 0 10px'></div>
  {''.join(leg(*c) for c in COMPRAS)}
</div><div class='nota'>Exemplo: três compras parceladas, a partir de outubro.</div></div>""", 3, T))

    pct = TOTAIS[3] / SOBRA * 100
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Antes de parcelar</div>
<div class='h2'>Olhe o mês mais cheio, não a parcela.</div>
<div class='p'>Some o que já está comprometido e compare com o que sobra num mês comum.</div>
<div class='visual'><div class='card' style='padding:40px 48px 40px'>
  <div style='display:flex;justify-content:space-between;align-items:baseline'><span style='font-size:30px;font-weight:600;color:{INK}'>Sobra de um mês comum</span><span class='big' style='font-size:48px'>R$ 2.180</span></div>
  <div style='height:30px;border-radius:15px;background:{BRAND};margin-top:16px'></div>
  <div style='display:flex;justify-content:space-between;align-items:baseline;margin-top:40px'><span style='font-size:30px;font-weight:600;color:{INK}'>Parcelas em janeiro</span><span class='big' style='font-size:48px;color:{CORAL_FORTE}'>R$ 1.049,90</span></div>
  <div style='display:flex;align-items:center;gap:18px;margin-top:16px'>
    <div style='flex:1;height:30px;border-radius:15px;background:{FIO};overflow:hidden'><div style='height:100%;width:{pct:.1f}%;background:{CORAL};border-radius:15px'></div></div>
    <span class='big' style='font-size:40px;color:{CORAL_FORTE}'>48%</span></div>
  <div style='font-size:28px;font-weight:700;color:{CORAL_TXT};margin-top:14px'>quase metade da sobra</div>
</div><div class='nota'>Exemplo: sobra de R$ 2.180, como em setembro (receitas de R$ 9.960 e despesas de R$ 7.780).</div></div>""", 4, T))

    tela = tela_nova(P26, "celular-nova-transacao-parcelada.jpg")
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>No timtimcash</div>
<div class='h3'>Lance uma vez. Cada parcela cai no seu mês.</div>
<div class='p' style='margin-top:16px;font-size:34px'>Em “Recorrência”, escolha “Parcelada” e o “Nº parcelas”, de 2 a 120. Você digita o total, e as próximas parcelas ficam pendentes.</div>
<div class='visual' style='margin-top:30px'>{recorte(tela, 1438, 2262, largura=680, x0=70, x1=1100)}{NOTA_TELA}</div>""", 5, T))

    s.append(fechamento_verde("Veja o mês que aperta antes de parcelar.",
        "Transações e Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.", 6, T))
    return [sem_quebra(h) for h in s]

POSTS = {
    P15: post_reserva,
    P19: post_cartao,
    P26: post_parcela,
}
