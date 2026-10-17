# -*- coding: utf-8 -*-
"""Reel de 06/11/2026 · "10% à vista ou 10x sem juros?" (capa papel), 1080 × 1920, 30 fps, 20 s. Equipe r1b (a partir da r1:
as mesmas contas e o mesmo roteiro, com os gráficos maiores, ocupando a faixa de 600 a 1500 px, e textos de apoio maiores).

Conta rápida, sem tela real: preço R$ 1.000; à vista R$ 900 (10% de desconto); 10 parcelas de R$ 100, a 1ª em 30 dias.
As contas são feitas aqui e conferidas com assert:
- juro embutido no "sem juros": a taxa i que faz R$ 900 hoje = 10 × R$ 100 (1ª em 30 dias) -> 1,96% ao mês (26,3% ao ano);
- com a 1ª parcela no ato, a taxa sobe para 2,42% ao mês;
- com rendimento de 1% ao mês, as 10 parcelas valem hoje R$ 947,13: o desconto que empata é 5,3%.

python3 reel_06.py  |  REEL_PREVIA="0 1 2 4 7 9 12 15.5 18.5" python3 reel_06.py
"""
import os, sys, json
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, os.path.join(N, "kit"))
import reelkit as K
A = K.A

PASTA = "2026-11-06_reel-a-vista-ou-parcelado"
AQUI = os.path.dirname(os.path.abspath(__file__))
TRAB = os.path.join(AQUI, "trabalho", "06")
SAIDA = os.path.join(N, "saida", PASTA)
DUR = 20.0

# ---------------------------------------------------------------- as contas
PRECO, AVISTA, N_PARC, PARC = 1000.0, 900.0, 10, 100.0
assert AVISTA == PRECO * 0.9 and N_PARC * PARC == PRECO

def vp(i, n=N_PARC, pmt=PARC, no_ato=False):
    """Valor hoje de n parcelas iguais (1ª em 30 dias, ou no ato)."""
    if no_ato:
        return pmt + pmt * (1 - (1 + i) ** -(n - 1)) / i
    return pmt * (1 - (1 + i) ** -n) / i

def taxa(alvo, no_ato=False):
    lo, hi = 1e-9, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if vp(m, no_ato=no_ato) > alvo:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2

I_MES = taxa(AVISTA)
I_ANO = (1 + I_MES) ** 12 - 1
I_ATO = taxa(AVISTA, no_ato=True)
VP_1 = vp(0.01)
EMPATE = 1 - VP_1 / PRECO
assert abs(vp(I_MES) - AVISTA) < 1e-6
assert f"{I_MES * 100:.2f}" == "1.96", I_MES
assert f"{I_ANO * 100:.1f}" == "26.3", I_ANO
assert f"{I_ATO * 100:.2f}" == "2.42", I_ATO
assert f"{VP_1:.2f}" == "947.13", VP_1
assert f"{EMPATE * 100:.1f}" == "5.3", EMPATE
assert 0.01 < I_MES            # rendimento de 1% fica abaixo do juro embutido: à vista ganha
assert 0.10 > EMPATE           # o desconto de 10% passa do empate
def pct(v, casas):
    return f"{v * 100:.{casas}f}".replace(".", ",")
TX_MES, TX_ANO, TX_ATO, TX_EMP = pct(I_MES, 2), pct(I_ANO, 1), pct(I_ATO, 2), pct(EMPATE, 1)

# ---------------------------------------------------------------- tempos (s)
G_FIM = 2.35                      # fim do gancho
T1, T2, T3, T4 = 2.45, 6.25, 10.25, 14.25
FIM = 17.30

# ---------------------------------------------------------------- etiquetas (SVG + texto)
TAG_W, TAG_H = 380, 470
def etiqueta(ident, fundo, borda, linhas):
    caminho = ("M48,96 L150,24 Q190,0 230,24 L332,96 Q380,124 380,170 L380,426 Q380,470 336,470 "
               "L44,470 Q0,470 0,426 L0,170 Q0,124 48,96 Z")
    txt = "".join(linhas)
    return f"""<div class="tag" id="{ident}">
  <div class="fio"></div>
  <svg class="tagsvg" width="{TAG_W}" height="{TAG_H}" viewBox="-4 -4 {TAG_W + 8} {TAG_H + 8}">
    <path d="{caminho}" fill="{fundo}" stroke="{borda}" stroke-width="5" stroke-linejoin="round"/>
    <circle cx="190" cy="74" r="17" fill="{A.BG}" stroke="{borda}" stroke-width="5"/>
  </svg>
  <div class="tagtxt">{txt}</div>
</div>"""

AMBAR_SUAVE = "#FBF1DC"
TAG_A = etiqueta("tagA", A.SOFT, A.BRAND, ['<div class="tg1" style="color:#065F46">R$ 900</div>', '<div class="tg2" style="color:#065F46">à vista</div>'])
TAG_B = etiqueta("tagB", AMBAR_SUAVE, A.AMBER, ['<div class="tg3" style="color:#8A6320">10x de</div>',
                                                '<div class="tg1" style="color:#5E4416">R$ 100</div>',
                                                '<div class="tg2" style="color:#8A6320">sem juros</div>'])

# ---------------------------------------------------------------- blocos: linha do tempo -> torres
ESC = 0.62                         # px por real
SLOT = 900 / 11
BASE1, BASE2 = 1390, 1440
BL = 66                            # largura dos blocos da linha do tempo
def geo_linha(k):                  # k = -1: à vista; 0..9: parcelas
    cx = 90 + SLOT * (k + 1.5)
    if k < 0:
        return [cx - BL / 2, BASE1 - AVISTA * ESC, BL, AVISTA * ESC]
    return [cx - BL / 2, BASE1 - PARC * ESC, BL, PARC * ESC - 6]
def geo_torre(k):
    if k < 0:
        return [215, BASE2 - AVISTA * ESC, 210, AVISTA * ESC]
    return [575, BASE2 - (k + 1) * PARC * ESC, 210, PARC * ESC - 6]
GL = [geo_linha(k) for k in range(-1, 10)]
GT = [geo_torre(k) for k in range(-1, 10)]
BLOCOS = "".join(f'<div class="bloco {"bv" if k < 0 else "ba"}" id="bk{k + 1}"></div>' for k in range(-1, 10))
ROT_LINHA = "".join(f'<div class="rotp" id="rp{k}" style="left:{90 + SLOT * (k + 1.5) - 40:.1f}px;top:{BASE1 - PARC * ESC - 54:.1f}px">100</div>' for k in range(10))
EIXO = "".join(f'<div class="eixo" style="left:{90 + SLOT * (k + 0.5) - 40:.1f}px">{"hoje" if k == 0 else k}</div>' for k in range(11))

# ---------------------------------------------------------------- régua (0% a 2,5% ao mês)
RX0, RX1, RY = 120, 940, 1060
def rx(p):                          # p em % ao mês
    return RX0 + (RX1 - RX0) * p / 2.5
TICKS = "".join(f'<div class="tick" style="left:{rx(v):.1f}px"></div><div class="tickl" style="left:{rx(v) - 40:.1f}px">{str(v).replace(".", ",").replace(",0", "")}%</div>'
                for v in [0, 0.5, 1.0, 1.5, 2.0, 2.5])
X_JURO = rx(I_MES * 100)
X_REND = rx(1.0)

# ---------------------------------------------------------------- desconto (0% a 10%)
DX0, DX1 = 90, 990
DY = 880                            # topo da barra do desconto
def dx(p):
    return DX0 + (DX1 - DX0) * p / 10
X_EMP = dx(EMPATE * 100)

CSS = f"""
.tit{{font-size:64px}}
.tit b.amb{{color:#8A6320}}
#gq{{position:absolute;left:90px;top:300px;width:900px;font-size:124px;line-height:.96;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#cheio{{position:absolute;left:90px;top:1262px;width:900px;text-align:center;font-size:48px;font-weight:500;color:{A.MUTED};letter-spacing:-.02em;opacity:0}}
#cheio b{{color:{A.INK};font-weight:700}}
#trilho{{position:absolute;left:60px;top:640px;width:960px;height:6px;border-radius:3px;background:{A.NEUTRO}}}
.tag{{position:absolute;top:646px;width:{TAG_W}px;height:{TAG_H + 60}px;transform-origin:{TAG_W / 2}px 0}}
.tag .fio{{position:absolute;left:{TAG_W / 2 - 2}px;top:0;width:4px;height:84px;background:{A.INK};border-radius:2px}}
.tag .tagsvg{{position:absolute;left:-4px;top:56px}}
.tag .tagtxt{{position:absolute;left:0;top:{56 + 140}px;width:{TAG_W}px;text-align:center}}
.tg1{{font-size:96px;font-weight:700;letter-spacing:-.05em;line-height:1.02;font-variant-numeric:tabular-nums}}
.tg2{{font-size:46px;font-weight:600;letter-spacing:-.02em;margin-top:14px}}
.tg3{{font-size:46px;font-weight:600;letter-spacing:-.02em;margin-bottom:6px}}
.bloco{{position:absolute;border-radius:14px;opacity:0}}
.bv{{background:{A.BRAND}}}
.ba{{background:{A.AMBER}}}
.rotp{{position:absolute;width:80px;text-align:center;font-size:34px;font-weight:700;color:#8A6320;font-variant-numeric:tabular-nums;opacity:0}}
#rotV{{position:absolute;width:260px;text-align:center;font-size:54px;font-weight:700;color:{A.BRAND_DARK};letter-spacing:-.035em;opacity:0}}
#eixo{{position:absolute;left:0;top:{BASE1 + 22}px;width:1080px;opacity:0}}
.eixo{{position:absolute;top:0;width:80px;text-align:center;font-size:32px;font-weight:600;color:{A.MUTED}}}
#eixoT{{position:absolute;left:90px;top:{BASE1 + 76}px;width:900px;text-align:center;font-size:34px;font-weight:500;color:{A.MUTED};opacity:0}}
#linhaBase{{position:absolute;left:90px;top:{BASE1}px;height:5px;width:900px;background:{A.INK};border-radius:3px;opacity:0;transform-origin:0 0}}
#legenda{{position:absolute;left:90px;top:540px;display:flex;gap:20px;opacity:0}}
.leg{{display:inline-flex;align-items:center;gap:16px;height:78px;padding:0 32px;border-radius:999px;background:#fff;border:3px solid {A.FIO};font-size:36px;font-weight:600;color:{A.INK}}}
.leg i{{width:28px;height:28px;border-radius:7px;display:inline-block}}
#torreA,#torreB{{position:absolute;top:{BASE2 + 24}px;width:320px;text-align:center;font-size:44px;font-weight:700;color:{A.INK};line-height:1.12;letter-spacing:-.03em;opacity:0}}
#torreA small,#torreB small{{display:block;font-size:34px;font-weight:500;color:{A.MUTED};letter-spacing:-.015em}}
#torreA{{left:{215 + 105 - 160}px}}
#torreB{{left:{575 + 105 - 160}px}}
#chave{{position:absolute;left:{575 + 210 + 12}px;top:{BASE2 - 1000 * ESC}px;width:200px;height:{(1000 - 900) * ESC}px;opacity:0}}
#chave .br{{position:absolute;left:0;top:0;width:28px;height:100%;border:6px solid #8A6320;border-left:0;border-radius:0 14px 14px 0}}
#chave span{{position:absolute;left:44px;top:50%;transform:translateY(-50%);font-size:44px;font-weight:700;color:#8A6320;white-space:nowrap;letter-spacing:-.03em}}
#linha900{{position:absolute;left:215px;top:{BASE2 - 900 * ESC - 2}px;width:570px;border-top:5px dashed {A.BRAND_DARK};opacity:0}}
#conta{{position:absolute;left:90px;top:520px;width:900px;opacity:0}}
#conta .n{{font-size:176px;font-weight:700;letter-spacing:-.05em;line-height:1;color:#8A6320;font-variant-numeric:tabular-nums}}
#conta .n small{{font-size:66px;letter-spacing:-.03em;margin-left:18px;color:#8A6320}}
#conta .s{{font-size:38px;font-weight:500;color:{A.MUTED};margin-top:18px;letter-spacing:-.015em}}
#conta .s b{{color:{A.INK};font-weight:700}}
#regua{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}}
#rlinha{{position:absolute;left:{RX0}px;top:{RY - 12}px;width:{RX1 - RX0}px;height:24px;border-radius:12px;background:{A.FIO};overflow:hidden}}
#rgap{{position:absolute;top:0;height:24px;background:{A.AMBER};left:{X_REND - RX0:.1f}px;width:0}}
.tick{{position:absolute;top:{RY + 30}px;width:5px;height:26px;margin-left:-2.5px;background:{A.NEUTRO};border-radius:3px}}
.tickl{{position:absolute;top:{RY + 66}px;width:100px;text-align:center;font-size:34px;font-weight:600;color:{A.MUTED}}}
.pino{{position:absolute;width:0;height:0}}
.pino .h{{position:absolute;left:-4px;width:8px;border-radius:4px}}
.pino .d{{position:absolute;left:-24px;width:48px;height:48px;border-radius:50%;border:8px solid #fff;box-shadow:0 2px 10px rgba(15,20,16,.25)}}
.pino .l{{position:absolute;white-space:nowrap;font-weight:700;letter-spacing:-.04em;line-height:1.02}}
.pino .l small{{display:block;font-size:36px;font-weight:600;letter-spacing:-.015em;margin-top:8px}}
#pJuro .h{{top:-330px;height:330px;background:{A.AMBER}}}
#pJuro .d{{top:-24px;background:{A.AMBER}}}
#pJuro .l{{right:-40px;top:-490px;text-align:right;font-size:104px;color:#8A6320}}
#pJuro .l small{{color:#8A6320}}
#pRend .h{{top:-160px;height:160px;background:{A.BRAND}}}
#pRend .d{{top:-24px;background:{A.BRAND}}}
#pRend .l{{left:-40px;top:-320px;font-size:104px;color:{A.BRAND_DARK}}}
#pRend .l small{{color:{A.BRAND_DARK}}}
#veredito{{position:absolute;left:90px;top:1230px;width:900px;opacity:0}}
.selo{{display:inline-flex;align-items:center;gap:22px;height:128px;padding:0 56px;border-radius:999px;background:{A.BRAND};color:#fff;font-size:62px;font-weight:700;letter-spacing:-.035em}}
#veredito .s{{font-size:40px;font-weight:500;color:{A.MUTED};margin-top:26px;letter-spacing:-.018em;line-height:1.3}}
#desc{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}}
#dbar{{position:absolute;left:{DX0}px;top:{DY}px;width:{DX1 - DX0}px;height:190px;border-radius:36px;overflow:hidden;display:flex}}
#dbar .z1{{height:100%;background:{AMBAR_SUAVE};width:{X_EMP - DX0:.1f}px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:40px;line-height:1.15;font-weight:700;color:#8A6320;letter-spacing:-.02em}}
#dbar .z2{{height:100%;background:{A.SOFT};flex:1;display:flex;align-items:center;justify-content:center;text-align:center;font-size:40px;line-height:1.15;font-weight:700;color:#065F46;letter-spacing:-.02em}}
#dmarca{{position:absolute;left:{X_EMP - 4:.1f}px;top:{DY - 40}px;width:8px;height:270px;background:{A.INK};border-radius:4px;transform-origin:50% 100%}}
#drot{{position:absolute;left:{X_EMP - 420:.1f}px;top:{DY - 196}px;width:400px;text-align:right;font-size:150px;font-weight:700;letter-spacing:-.05em;color:{A.INK};line-height:1}}
#dticks{{position:absolute;left:0;top:{DY + 214}px;width:1080px}}
.dtl{{position:absolute;top:0;width:100px;text-align:center;font-size:34px;font-weight:600;color:{A.MUTED}}}
#dex{{position:absolute;left:{dx(10) - 4:.1f}px;top:{DY - 40}px;width:8px;height:270px;background:{A.BRAND_DARK};border-radius:4px;transform-origin:50% 100%;opacity:0}}
#dexl{{position:absolute;left:{dx(10) - 330:.1f}px;top:{DY - 98}px;width:330px;text-align:right;font-size:40px;font-weight:700;color:{A.BRAND_DARK};letter-spacing:-.025em;opacity:0}}
#dnota{{position:absolute;left:90px;top:{DY + 300}px;width:860px;font-size:40px;font-weight:500;color:{A.MUTED};letter-spacing:-.018em;line-height:1.35}}
#dnota b{{color:{A.INK};font-weight:700}}
"""

DTICKS = "".join(f'<div class="dtl" style="left:{min(max(dx(v) - 50, DX0), DX1 - 100):.1f}px;text-align:{"left" if v == 0 else ("right" if v == 10 else "center")}">{v}%</div>' for v in [0, 2, 4, 6, 8, 10])

CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="t1">À vista, <b>R$ 900</b> hoje. Parcelado, <b class="amb">R$ 100</b> por mês, por 10 meses.</div>
  <div id="legenda"><span class="leg"><i style="background:{A.BRAND}"></i>à vista</span><span class="leg"><i style="background:{A.AMBER}"></i>10x sem juros</span></div>
  <div id="linhaBase"></div>
  {BLOCOS}
  <div id="rotV">R$ 900</div>
  {ROT_LINHA}
  <div id="eixo">{EIXO}</div>
  <div id="eixoT">meses</div>
  <div class="tit" id="t2">Parcelar é ficar com R$ 900 hoje e devolver <b class="amb">R$ 1.000</b> em 10 meses.</div>
  <div id="conta"><div class="n num" id="nTaxa">0,00%<small>ao mês</small></div>
    <div class="s">o juro embutido no “sem juros” · <b>{TX_ANO}% ao ano</b></div></div>
  <div id="linha900"></div>
  <div id="chave"><div class="br"></div><span>+R$ 100</span></div>
  <div id="torreA">R$ 900<small>à vista, hoje</small></div>
  <div id="torreB">R$ 1.000<small>em 10 parcelas</small></div>
  <div class="tit" id="t3">Seu dinheiro rende <b>1% ao mês</b>?</div>
  <div id="regua">
    <div id="rlinha"><div id="rgap"></div></div>
    {TICKS}
    <div class="pino" id="pJuro" style="left:{X_JURO:.1f}px;top:{RY + 5}px"><div class="h"></div><div class="d"></div><div class="l">{TX_MES}%<small>juro do parcelado</small></div></div>
    <div class="pino" id="pRend" style="left:{X_REND:.1f}px;top:{RY + 5}px"><div class="h"></div><div class="d"></div><div class="l">1%<small>seu rendimento</small></div></div>
    <div id="veredito"><span class="selo"><svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>À vista ganha</span>
      <div class="s">Rendendo menos que o juro embutido, o desconto de 10% vale mais que parcelar.</div></div>
  </div>
  <div class="tit" id="t4">Desconto acima de <b>{TX_EMP}%</b> vence um rendimento de 1% ao mês.</div>
  <div id="desc">
    <div id="drot">{TX_EMP}%</div>
    <div id="dbar"><div class="z1" id="dz1">parcelar pode valer</div><div class="z2" id="dz2">à vista ganha</div></div>
    <div id="dmarca"></div>
    <div id="dex"></div><div id="dexl">o exemplo: 10%</div>
    <div id="dticks">{DTICKS}</div>
    <div id="dnota">No exemplo, o desconto é de <b>10%</b>: à vista ganha. Exemplo ilustrativo, com a 1ª parcela em 30 dias.</div>
  </div>
</div>

<div class="cena papel" id="gancho">
  <div id="gq">Qual sai<br>mais barato?</div>
  <div id="trilho"></div>
  {TAG_A}
  {TAG_B}
  <div id="cheio">Preço cheio: <b>R$ 1.000</b></div>
</div>

{K.fim("Faça a conta antes de parcelar.", "Lance a compra parcelada e veja cada parcela no seu mês.")}
"""

JS = f"""
const G_FIM={G_FIM}, T1={T1}, T2={T2}, T3={T3}, T4={T4}, FIM={FIM};
const BL={BL}, GL={json.dumps([[round(v, 1) for v in g] for g in GL])}, GT={json.dumps([[round(v, 1) for v in g] for g in GT])};
const I_MES={I_MES * 100:.6f}, X_JURO={X_JURO:.1f}, X_REND={X_REND:.1f}, RX0={RX0};
// pêndulo das etiquetas: o ponto de apoio desliza pelo trilho e a etiqueta balança (simulado uma vez, de -1 s a 25 s)
const PASSO = 1/600, T0 = -1.0;
function trilhoX(t, x0, x1, a, d){{ return x1 + (x0 - x1)*(1 - easeOut(clamp((t-a)/d, 0, 1))); }}
function simula(x0, x1, a, d){{
  const L = 330, g = 9800, b = 3.2; let th = 0, w = 0; const out = [];
  for (let t = T0; t <= 25; t += PASSO){{
    const ac = (trilhoX(t+PASSO, x0, x1, a, d) - 2*trilhoX(t, x0, x1, a, d) + trilhoX(t-PASSO, x0, x1, a, d)) / (PASSO*PASSO);
    const al = -(g/L)*Math.sin(th) - 0.36*(ac/L)*Math.cos(th) - b*w;
    w += al*PASSO; th += w*PASSO; out.push(th);
  }}
  return out;
}}
const TAGA = [-460, 90, -0.35, 0.95], TAGB = [1140, 610, -0.25, 0.95];
const SA = simula(...TAGA), SB = simula(...TAGB);
function ang(S, t){{ const i = clamp((t - T0)/PASSO, 0, S.length-1); const k = Math.floor(i); const f = i - k;
  return (S[k]*(1-f) + S[Math.min(k+1, S.length-1)]*f) * 180/Math.PI; }}
function geo(el, g){{ el.style.left = g[0]+'px'; el.style.top = g[1]+'px'; el.style.width = g[2]+'px'; el.style.height = g[3]+'px'; }}
function render(t){{
  // 1. gancho: as duas etiquetas chegam de lados opostos e balançam
  const sai = prog(t, G_FIM-.2, G_FIM+.12);
  $('gancho').style.opacity = 1 - sai;
  $('gq').style.transform = `translateY(${{-10*pout(t,0,1.2) - 70*sai}}px)`; $('cheio').style.marginTop = (-50*sai)+'px';
  aparece('cheio', t, .55, 0, 22, .45);
  const xa = trilhoX(t, ...TAGA) - 900*easeOut(clamp((t-G_FIM+.05)/.4,0,1));
  const xb = trilhoX(t, ...TAGB) + 900*easeOut(clamp((t-G_FIM+.05)/.4,0,1));
  const ida = 1.2*Math.sin(2*Math.PI*(t-1.4)/2.6);         // balanço leve depois de parar
  $('tagA').style.left = xa+'px'; $('tagA').style.transform = `rotate(${{-ang(SA, t) + ida*prog(t,1.2,2)}}deg)`;
  $('tagB').style.left = xb+'px'; $('tagB').style.transform = `rotate(${{-ang(SB, t) - ida*prog(t,1.2,2)}}deg)`;
  // 2. linha do tempo: R$ 900 hoje contra 10 blocos de R$ 100, um por mês
  titulo('t1', t, T1, T2-.32);
  aparece('legenda', t, T1+.15, T2-.32, 20);
  const eix = Math.min(prog(t, T1+.1, T1+.5), 1 - prog(t, T2-.3, T2+.05));
  $('linhaBase').style.opacity = eix; $('linhaBase').style.transform = `scaleX(${{pout(t, T1, T1+.6)}})`;
  $('eixo').style.opacity = eix; $('eixoT').style.opacity = Math.min(prog(t, T1+2.0, T1+2.3), 1 - prog(t, T2-.3, T2+.05));
  // blocos: crescem/caem na linha do tempo; depois voam para as torres (T2) e somem em T3
  const vai = (k) => prog(t, T2 + .05 + k*.045, T2 + .6 + k*.045);
  const some = 1 - prog(t, T3-.3, T3+.05);
  for (let k = 0; k < 11; k++){{
    const el = $('bk'+k); let g = GL[k].slice();
    if (k === 0){{ const p = pout(t, T1+.25, T1+.85); g[1] = GL[0][1] + GL[0][3]*(1-p); g[3] = GL[0][3]*p; el.style.opacity = Math.min(lin(t, T1+.25, T1+.3), some); }}
    else {{ const a = T1 + .75 + (k-1)*.17; const p = clamp((t-a)/.42, 0, 1);
      const queda = p < 1 ? (1 - easeOut(p))*-260 : 0; const pulo = p >= 1 ? 0 : 0;
      g[1] = GL[k][1] + queda; el.style.opacity = Math.min(lin(t, a, a+.12), some); }}
    const v = vai(k); g = g.map((x, i) => x + (GT[k][i] - x)*v);
    geo(el, g);
  }}
  $('rotV').style.left = (GL[0][0]+BL/2-130)+'px'; $('rotV').style.top = (GL[0][1]-70)+'px';
  $('rotV').style.opacity = Math.min(prog(t, T1+.7, T1+1.0), 1 - prog(t, T2-.3, T2));
  for (let k = 0; k < 10; k++){{ const a = T1 + .75 + k*.17 + .3; $('rp'+k).style.opacity = Math.min(prog(t, a, a+.25), 1 - prog(t, T2-.3, T2)); }}
  // 3. a conta: R$ 900 hoje, R$ 1.000 em 10 meses; o juro embutido
  titulo('t2', t, T2, T3-.32);
  const cI = prog(t, T2+.9, T2+1.25);
  $('conta').style.opacity = Math.min(cI, some); $('conta').style.transform = `translateY(${{(1-cI)*24}}px)`;
  contar('nTaxa', t, T2+1.0, T2+2.2, 0, I_MES, 2, '', '%');
  $('nTaxa').innerHTML = $('nTaxa').textContent + '<small>ao mês</small>';
  ['torreA','torreB'].forEach((id, i) => {{ $(id).style.opacity = Math.min(prog(t, T2+.7+i*.12, T2+1.0+i*.12), some); }});
  $('linha900').style.opacity = Math.min(prog(t, T2+.9, T2+1.2), some);
  $('chave').style.opacity = Math.min(prog(t, T2+1.15, T2+1.45), some);
  // 4. régua: 1% ao mês fica abaixo de 1,96%
  titulo('t3', t, T3, T4-.32);
  const rI = Math.min(prog(t, T3-.2, T3+.15), 1 - prog(t, T4-.35, T4-.1));
  $('regua').style.opacity = rI;
  const pj = pback(t, T3+.05, T3+.5); $('pJuro').style.transform = `scale(${{.4+.6*pj}})`; $('pJuro').style.opacity = lin(t, T3+.05, T3+.2);
  const rm = pout(t, T3+.7, T3+1.5);
  $('pRend').style.left = (RX0 + (X_REND - RX0)*rm)+'px'; $('pRend').style.opacity = lin(t, T3+.85, T3+1.0);
  $('rgap').style.width = ((X_JURO - X_REND)*pout(t, T3+1.5, T3+1.9))+'px';
  const vI = pback(t, T3+1.85, T3+2.3);
  $('veredito').style.opacity = lin(t, T3+1.85, T3+2.05); $('veredito').style.transform = `scale(${{.85+.15*vI}})`; $('veredito').style.transformOrigin = '0 50%';
  // 5. a regra de bolso: desconto acima de 5,3%
  titulo('t4', t, T4, FIM+.3);
  $('desc').style.opacity = prog(t, T4-.15, T4+.15);
  const dI = pout(t, T4+.05, T4+.75);
  $('dbar').style.clipPath = `inset(0 ${{100 - 100*dI}}% 0 0 round 28px)`;
  const mI = pback(t, T4+.7, T4+1.1);
  $('dmarca').style.transform = `scaleY(${{mI}})`; $('drot').style.opacity = lin(t, T4+.75, T4+.9); $('drot').style.transform = `translateY(${{(1-mI)*30}}px)`;
  $('dnota').style.opacity = prog(t, T4+1.6, T4+1.9);
  const xI = pback(t, T4+1.25, T4+1.6); $('dex').style.opacity = lin(t, T4+1.25, T4+1.35); $('dex').style.transform = `scaleY(${{xI}})`;
  $('dexl').style.opacity = prog(t, T4+1.35, T4+1.6);
  // 6. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (papel)
CAPA_CSS = f"""
.ct{{position:absolute;left:90px;top:440px;width:900px}}
.ct .h1{{font-size:118px;line-height:.98}}
.ct .h1 b{{color:{A.MENTA};font-weight:700}}
#ctrilho{{position:absolute;left:60px;top:880px;width:960px;height:6px;border-radius:3px;background:#3A443B}}
.cap .tag{{position:absolute;top:886px;width:{TAG_W}px;height:{TAG_H + 60}px;transform-origin:{TAG_W / 2}px 0}}
.cap .tag .fio{{position:absolute;left:{TAG_W / 2 - 2}px;top:0;width:4px;height:84px;background:#6B786D;border-radius:2px}}
.cap .tag .tagsvg{{position:absolute;left:-4px;top:56px}}
.cap .tag .tagtxt{{position:absolute;left:0;top:{56 + 140}px;width:{TAG_W}px;text-align:center}}
.tg1{{font-size:96px;font-weight:700;letter-spacing:-.05em;line-height:1.02;font-variant-numeric:tabular-nums}}
.tg2{{font-size:46px;font-weight:600;letter-spacing:-.02em;margin-top:14px}}
.tg3{{font-size:46px;font-weight:600;letter-spacing:-.02em;margin-bottom:6px}}
#cq{{position:absolute;left:0;top:1090px;width:1080px;text-align:center;font-size:260px;font-weight:700;color:{A.MENTA};letter-spacing:-.05em;line-height:1}}
"""
CAPA_CORPO = f"""
{K.logo("tinta")}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Conta rápida</div>
  <div class="h1">10% à vista ou 10x sem juros?</div></div>
<div class="cap">
  <div id="ctrilho"></div>
  {TAG_A.replace('id="tagA"', 'id="cA" style="left:60px;transform:scale(.94) rotate(-5deg)"')}
  {TAG_B.replace('id="tagB"', 'id="cB" style="left:640px;transform:scale(.94) rotate(4deg)"')}
  <div id="cq">?</div>
</div>
"""

HTML = K.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="tinta")

if __name__ == "__main__":
    print(f"juro embutido {TX_MES}% ao mês ({TX_ANO}% ao ano) · no ato {TX_ATO}% · VP a 1% R$ {VP_1:.2f} · empate {TX_EMP}%")
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
