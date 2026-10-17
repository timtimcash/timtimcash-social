# -*- coding: utf-8 -*-
"""Reel de 12/11/2026 · "Qual é o seu dólar?" (capa verde suave), 1080 × 1920, 30 fps, 20 s. Equipe r1b (a partir da r1).

Três remessas de US$ 4.000 (conta de exemplo): 12/07/2023 a R$ 4,90 (R$ 19.600), 14/03/2024 a R$ 5,00 (R$ 20.000)
e 18/04/2024 a R$ 5,10 (R$ 20.400). Câmbio médio: R$ 60.000 ÷ US$ 12.000 = R$ 5,00 (conta feita aqui, com assert).
Tela real do build 2026-10-16.1 (capturas/captura12.py): Remessas no celular, relógio em 12/11/2026 10:00, cartão
"Câmbio: onde você está": hoje R$ 5,0515 (o câmbio informado na carteira em 30/10, a PTAX de compra de 15/10/2026),
equilíbrio R$ 4,5249; no equilíbrio R$ 0, hoje +R$ 6.982,89, no seu médio (R$ 5,00) +R$ 6.300,00; carteira de
US$ 13.260 (+US$ 1.260,00, +10,5% em US$; +R$ 6.982,89, +11,6% em R$).

python3 reel_12.py  |  REEL_PREVIA="0 0.6 1.5 3.5 6 7.6 9.2 11 13 15.6 18.5" python3 reel_12.py
"""
import os, sys, json
from decimal import Decimal as D
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-11-12_reel-o-seu-cambio-medio"
TRAB = os.path.join(AQUI, "trabalho", "12")
TELA = os.path.join(N, "saida", PASTA, "telas", "celular-remessas-ate-o-cambio.png")
SAIDA = os.path.join(N, "saida", PASTA)
DUR = 20.0

CX = json.load(open(os.path.join(TRAB, "caixas.json"), encoding="utf-8"))

# ---------------------------------------------------------------- números
REM = [("jul/23", "4.90"), ("mar/24", "5.00"), ("abr/24", "5.10")]
US = D("4000")
REAIS = [US * D(c) for _, c in REM]
assert [str(r) for r in REAIS] == ["19600.00", "20000.00", "20400.00"]
TOT_R, TOT_US = sum(REAIS), US * 3
MEDIO = TOT_R / TOT_US
assert TOT_R == D("60000") and TOT_US == D("12000") and MEDIO == D("5")
NO = dict((t.replace("\xa0", " "), b) for t, b in CX["noCard"])
for t in ["R$ 5,0515", "hoje", "R$ 4,5249", "R$ 5,00", "No equilíbrio (R$ 4,5249)", "R$ 0", "Hoje (R$ 5,0515)", "+R$ 6.982,89",
          "No seu médio (R$ 5,00)", "+R$ 6.300,00"]:
    assert t in NO, t
TXT = CX["texto"].replace("\xa0", " ")
assert "+US$ 1.260,00" in TXT and "US$13.260 na carteira hoje" in TXT.replace("US$ 13.260", "US$13.260") and "+10,5% em US$" in TXT and "+11,6% em R$" in TXT
assert D("1260") * MEDIO == D("6300")      # no médio, o resultado em reais = o retorno de US$ 1.260 × R$ 5,00 (+R$ 6.300,00 na tela)
LIN = CX["linhas"]
MARCAS = {m[0].split(".")[1].split(" ")[0] if "." in m[0] else m[0]: m[1] for m in CX["marcas"]}

def brl(v, casas=0):
    return f"{v:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ---------------------------------------------------------------- tempos (s)
G_FIM = 2.35
T1, T2 = 2.45, 4.55
SOBE = 7.00                        # a cena suave sobe e revela o papel com a tela real
T3, T4, T5 = 7.20, 10.00, 12.10
POP = 8.30                         # o cartão "Câmbio: onde você está" se solta da tela
T6 = 14.20
FIM = 17.30
QUEDAS = [-0.14, 0.24, 0.62]

# ---------------------------------------------------------------- tela real (px CSS)
CARD = CX["card"]                                    # [14, 837.6, 362, 361.5]
R_POP = [CARD[0] + 2, round(CARD[1] + 2, 1), CARD[2] - 4, round(CARD[3] - 4, 1)]
CAM0 = (120, 0, 1.0)
CAM1 = (round(CARD[1] - 60, 1), 0, 1.0)
PARA = [90, 600, 900]
DE = C.de_janela(R_POP, CAM1)
R_HOJE = C.uniao(NO["R$ 5,0515"], NO["hoje"], NO["R$ 5,00"], MARCAS["remx-pin"], MARCAS["remx-doto"])
R_LINHAS = C.uniao(LIN["Hoje (R$ 5,0515)"], LIN["No seu médio (R$ 5,00)"])
R_EQUIL = LIN["No equilíbrio (R$ 4,5249)"]
R_TRACO = C.uniao(MARCAS["remx-tick"], NO["R$ 4,5249"], MARCAS["remx-zneg"])
ANEIS = (C.anel_no_recorte("aHoje", R_POP, PARA, R_HOJE, 14) + C.anel_no_recorte("aLin", R_POP, PARA, R_LINHAS, 10)
         + C.anel_no_recorte("aEq", R_POP, PARA, R_EQUIL, 10, "coral") + C.anel_no_recorte("aTr", R_POP, PARA, R_TRACO, 12, "coral"))

# ---------------------------------------------------------------- fichas
FY = [1230, 1080, 930]               # de baixo para cima
def ficha(i, data, cambio):
    return f"""<div class="ficha" id="fi{i}"><span class="fc">{C.din(cambio.replace('.', ','), centavos=False)}</span><span class="fd">{data}</span></div>"""
FICHAS = "".join(ficha(i, d, c) for i, (d, c) in enumerate(REM))
LINHAS_CONTA = "".join(
    f'<div class="lc" id="lc{i}" style="top:{620 + i * 140}px"><span class="a">{C.din(c.replace(".", ","), centavos=False)}</span><span class="b">× US$ 4.000</span>'
    f'<span class="c" id="lv{i}">{C.din(brl(REAIS[i]))}</span></div>' for i, (d, c) in enumerate(REM))

# ---------------------------------------------------------------- régua desenhada (R$ 4,30 a R$ 5,30)
GX0, GX1, GY, GH = 90, 990, 880, 100
def gx(c):
    return GX0 + (GX1 - GX0) * (c - 4.30) / 1.00
X_EQ, X_MED, X_HOJE = gx(4.5249), gx(5.00), gx(5.0515)

CSS = C.CSS + f"""
.tit{{font-size:66px}}
.tit b.ver{{color:{A.RED_TEXT}}}
#cada{{position:absolute;left:90px;top:1408px;width:900px;text-align:center;font-size:42px;font-weight:600;color:{A.BRAND_DEEP};letter-spacing:-.02em;opacity:0}}
#gq{{position:absolute;left:90px;top:300px;width:900px;font-size:112px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK};z-index:5}}
.ficha{{position:absolute;left:200px;width:680px;height:150px;border-radius:34px;background:#fff;border:3px solid {A.MENTA_CLARA};display:flex;align-items:center;
  justify-content:space-between;padding:0 48px;box-shadow:0 2px 4px rgba(6,95,70,.06),0 22px 40px -22px rgba(6,95,70,.35);transform-origin:50% 100%}}
.fc{{font-size:96px;font-weight:700;letter-spacing:-.045em;color:{A.INK}}}
.fc .rs{{color:{A.MUTED}}}
.fd{{font-size:42px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em;white-space:nowrap}}
.lc{{position:absolute;left:90px;width:900px;height:118px;border-radius:28px;background:#fff;display:flex;align-items:center;padding:0 40px;gap:26px;opacity:0;
  border:3px solid {A.MENTA_CLARA}}}
.lc .a{{font-size:60px;font-weight:700;letter-spacing:-.04em;color:{A.INK};width:250px}}
.lc .a .rs{{color:{A.MUTED}}}
.lc .b{{font-size:38px;font-weight:600;color:{A.MUTED}}}
.lc .c{{margin-left:auto;font-size:58px;font-weight:700;letter-spacing:-.035em;color:{A.BRAND_DEEP};opacity:0}}
#tot{{position:absolute;left:90px;top:1060px;width:900px;display:flex;align-items:baseline;justify-content:space-between;padding:26px 40px 0;border-top:4px solid {A.BRAND_DEEP};opacity:0}}
#tot span{{font-size:48px;font-weight:700;color:{A.BRAND_DEEP};letter-spacing:-.03em}}
#tot b{{font-size:72px;font-weight:700;color:{A.INK};letter-spacing:-.04em}}
#frac{{position:absolute;left:90px;top:620px;width:900px;opacity:0}}
#frac .nu,#frac .de{{text-align:center;font-size:110px;font-weight:700;letter-spacing:-.05em;color:{A.INK};line-height:1.1}}
#frac .ln{{height:8px;border-radius:4px;background:{A.INK};margin:22px 120px;transform-origin:50% 50%}}
#res{{position:absolute;left:90px;top:1030px;width:900px;text-align:center;opacity:0}}
#res .ig{{font-size:72px;font-weight:700;color:{A.MUTED};line-height:1}}
#res .v{{font-size:230px;font-weight:700;letter-spacing:-.055em;color:{A.BRAND_DARK};line-height:1.05;display:inline-flex;align-items:baseline;font-variant-numeric:tabular-nums}}
#res .v .rs{{font-size:96px;font-weight:600;letter-spacing:-.01em;margin-right:22px;color:{A.BRAND_DEEP}}}
#res .r{{font-size:46px;font-weight:600;color:{A.BRAND_DEEP};letter-spacing:-.02em}}
#regua{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}}
#gbar{{position:absolute;left:{GX0}px;top:{GY}px;width:{GX1 - GX0}px;height:{GH}px;border-radius:{GH // 2}px;overflow:hidden;display:flex}}
#gbar i{{display:flex;align-items:center;justify-content:center;height:100%;font-style:normal;font-size:36px;font-weight:700;letter-spacing:-.02em}}
.gm{{position:absolute;top:{GY - 30}px;width:8px;height:{GH + 60}px;margin-left:-4px;border-radius:4px}}
.gl{{position:absolute;white-space:nowrap;line-height:1.05;font-weight:700;letter-spacing:-.035em}}
.gl small{{display:block;font-size:34px;font-weight:600;letter-spacing:-.01em;margin-top:4px}}
#gHoje{{position:absolute;top:{GY + GH / 2}px;width:56px;height:56px;margin:-28px 0 0 -28px;border-radius:50%;background:{A.BRAND_DARK};border:8px solid #fff;box-shadow:0 2px 10px rgba(15,20,16,.3)}}
#frase2{{position:absolute;left:90px;top:1200px;width:900px;font-size:66px;line-height:1.08;font-weight:700;letter-spacing:-.045em;color:{A.INK};opacity:0}}
#frase2 b{{color:{A.RED_TEXT}}}
"""

CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="t3">Seu médio: <b>R$ 5,00</b>. Hoje: R$ 5,0515.</div>
  <div class="tit" id="t4">Hoje, <b>+R$ 6.982,89</b> em reais. No seu médio, +R$ 6.300.</div>
  <div class="tit" id="t5">Equilíbrio: <b class="ver">R$ 4,5249</b>. Abaixo dele, prejuízo.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{K.tela("tela", TELA)}<div class="veu" id="veu"></div></div>
  {C.pop_html("pop", TELA, ANEIS)}
  <div class="tit" id="t6">Acima do seu médio, o câmbio <b>soma</b>.</div>
  <div id="regua">
    <div id="gbar"><i style="width:{X_EQ - GX0:.1f}px;background:#F6DCDC;color:{A.RED_TEXT}">prejuízo</i><i style="width:{X_MED - X_EQ:.1f}px;background:#EEF3EC"></i><i style="flex:1;background:{A.SOFT};color:{A.BRAND_DEEP}">soma</i></div>
    <div class="gm" style="left:{X_EQ:.1f}px;background:{A.RED}"></div>
    <div class="gm" style="left:{X_MED:.1f}px;background:{A.INK}"></div>
    <div class="gl" style="left:{X_EQ - 100:.1f}px;top:{GY - 170}px;font-size:60px;color:{A.RED_TEXT}">R$ 4,5249<small>equilíbrio</small></div>
    <div class="gl" style="left:{X_MED - 160:.1f}px;top:{GY - 170}px;font-size:60px;color:{A.INK}">R$ 5,00<small>seu médio</small></div>
    <div id="gHoje" style="left:{X_HOJE:.1f}px"></div>
    <div class="gl" id="glHoje" style="left:{X_HOJE - 70:.1f}px;top:{GY + GH + 34}px;font-size:48px;color:{A.BRAND_DARK}">R$ 5,0515<small>hoje</small></div>
    <div id="frase2">Abaixo do equilíbrio, vira <b>prejuízo em reais</b>.</div>
  </div>
</div>

<div class="cena suave" id="gancho">
  <div id="gq">Comprou dólar<br>em vezes<br>diferentes?</div>
  {FICHAS}
  <div id="cada">US$ 4.000 em cada remessa</div>
  <div class="tit" id="t1">Some os reais. Divida pelos dólares.</div>
  {LINHAS_CONTA}
  <div id="tot"><span>US$ 12.000</span><b>{C.din("60.000")}</b></div>
  <div class="tit" id="t2"><b>R$ 5,00</b> é o seu câmbio médio.</div>
  <div id="frac"><div class="nu">{C.din("60.000")}</div><div class="ln" id="fln"></div><div class="de">{C.din("12.000", rs="US$")}</div></div>
  <div id="res"><div class="ig">=</div><div class="v"><span class="rs">R$</span><span id="rv">0,00</span></div><div class="r">o seu câmbio médio</div></div>
</div>

{K.fim("Remessas ao exterior no timtimcash")}
"""

JS = C.JS + f"""
const G_FIM={G_FIM}, T1={T1}, T2={T2}, SOBE={SOBE}, T3={T3}, T4={T4}, T5={T5}, T6={T6}, FIM={FIM}, POP={POP};
const QUEDAS={QUEDAS}, FY={FY}, CAM0={list(CAM0)}, CAM1={list(CAM1)};
const R_POP={R_POP}, DE={[round(v, 1) for v in DE]}, PARA={PARA};
function mix(a, b, p){{ return a.map((v, i) => v + (b[i]-v)*p); }}
function cam(c){{ const [topo, esq, z] = c; $('tela').style.transform = `translate(${{-esq*E*z}}px, ${{-topo*E*z}}px) scale(${{z}})`; }}
function render(t){{
  // 1. gancho na cor suave: três fichas caem e se empilham
  $('gancho').style.transform = `translateY(${{-1920*prog(t, SOBE, SOBE+.45)}}px)`;
  const saiQ = prog(t, G_FIM-.15, G_FIM+.15);
  $('gq').style.opacity = 1 - saiQ;
  $('cada').style.opacity = Math.min(prog(t, 1.25, 1.55), 1 - saiQ); $('gq').style.transform = `translateY(${{-12*pout(t,0,1.2) - 20*saiQ}}px)`;
  QUEDAS.forEach((q, i) => {{
    const el = $('fi'+i); const Y0 = 650, G = 6400;
    const tq = Math.sqrt(2*(FY[i] - Y0)/G), u0 = t - q, p = clamp(u0/tq, 0, 1);
    let y = Math.min(FY[i], Y0 + 0.5*G*Math.max(0, u0)*Math.max(0, u0));
    let sx = .94 + .06*clamp(u0/.08, 0, 1), sy = sx, rot = [-4, 3, -2][i]*(1-p);
    if (p >= 1){{ const u = u0 - tq; const k = Math.exp(-u*10)*Math.sin(u*30); sy = 1 - 0.10*k; sx = 1 + 0.06*k; rot = [-1.2, 0.9, -0.6][i]*Math.exp(-u*3); }}
    const vai = prog(t, G_FIM-.1 + i*.05, G_FIM+.3 + i*.05);
    el.style.top = (y - 120*vai)+'px'; el.style.opacity = clamp(u0/.06, 0, 1)*(1 - vai);
    el.style.transform = `rotate(${{rot}}deg) scale(${{sx}}, ${{sy}})`;
  }});
  // 2. a conta: cada remessa em reais, os totais e a divisão
  titulo('t1', t, T1, T2-.32);
  [0,1,2].forEach(i => {{ const a = T1 + .1 + i*.18; aparece('lc'+i, t, a, T2-.32, 30, .4);
    const v = $('lv'+i); const pv = pback(t, a+.55, a+.9); v.style.opacity = lin(t, a+.55, a+.7); v.style.transform = `scale(${{.7+.3*pv}})`; }});
  aparece('tot', t, T1+1.25, T2-.32, 24, .4);
  titulo('t2', t, T2, SOBE+.2);
  const fI = pout(t, T2+.1, T2+.5);
  $('frac').style.opacity = fI; $('frac').style.transform = `translateY(${{(1-fI)*40}}px)`;
  $('fln').style.transform = `scaleX(${{pout(t, T2+.2, T2+.7)}})`;
  $('res').style.opacity = prog(t, T2+.3, T2+.55);
  contar('rv', t, T2+.35, T2+1.1, 0, 5, 2, '');
  const sr = t > T2+1.1 ? 1 + 0.08*Math.sin(Math.PI*clamp((t-T2-1.1)/.35, 0, 1)) : 1;
  $('res').querySelector('.v').style.transform = `scale(${{sr}})`;
  // 3. a tela real: do topo de Remessas até o cartão "Câmbio: onde você está", que se solta da tela
  titulo('t3', t, T3, T4-.32); titulo('t4', t, T4, T5-.32); titulo('t5', t, T5, T6-.45);
  janela('janela', t, SOBE, T6-.45); janela('nota', t, SOBE, T6-.45);
  cam(mix(CAM0, CAM1, prog(t, T3+.45, POP-.05)));
  $('veu').style.opacity = .62*Math.min(prog(t, POP, POP+.5), 1 - prog(t, T6-.75, T6-.4));
  recorte('pop', t, POP, T6-.75, R_POP, DE, PARA, .6, true);
  anel('aHoje', t, POP+.7, T4-.2); anel('aLin', t, T4+.35, T5-.2);
  anel('aEq', t, T5+.35, T6-.9); anel('aTr', t, T5+.55, T6-.9);
  // 4. a lição, numa régua desenhada
  titulo('t6', t, T6-.15, FIM+.3);
  $('regua').style.opacity = prog(t, T6-.3, T6);
  $('gbar').style.clipPath = `inset(0 ${{100 - 100*pout(t, T6, T6+.7)}}% 0 0 round 50px)`;
  const ph = pback(t, T6+.6, T6+1.0); $('gHoje').style.transform = `scale(${{ph}})`;
  $('glHoje').style.opacity = prog(t, T6+.75, T6+1.05);
  aparece('frase2', t, T6+1.0, 0, 30, .45);
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (verde suave), a mesma da r1
CAPA_CSS = f"""
.ct{{position:absolute;left:90px;top:440px;width:900px}}
.ct .h1{{font-size:132px;line-height:.96}}
.ct .eyebrow{{color:{A.BRAND_DEEP}}}
.mini{{position:absolute;left:90px;width:330px;height:104px;border-radius:26px;background:#fff;border:3px solid {A.MENTA_CLARA};display:flex;align-items:center;
  justify-content:center;font-size:58px;font-weight:700;letter-spacing:-.04em;color:{A.INK};box-shadow:0 18px 34px -22px rgba(6,95,70,.4)}}
.mini .rs{{color:{A.MUTED}}}
.grande{{position:absolute;left:540px;top:960px;width:450px;height:280px;border-radius:40px;background:#fff;border:6px solid {A.BRAND};display:flex;flex-direction:column;
  align-items:center;justify-content:center;box-shadow:0 26px 50px -26px rgba(6,95,70,.5)}}
.grande b{{font-size:124px;font-weight:700;letter-spacing:-.05em;color:{A.BRAND_DARK};line-height:1}}
.grande b .rs{{color:{A.BRAND_DEEP}}}
.grande span.m{{font-size:40px;font-weight:700;color:{A.BRAND_DEEP};margin-top:14px;letter-spacing:-.01em}}
"""
CAPA_CORPO = f"""
{K.logo("suave")}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Câmbio médio</div>
  <div class="h1">Qual é o seu dólar?</div></div>
<div class="mini" style="top:900px">{C.din("4,90", centavos=False)}</div>
<div class="mini" style="top:1048px">{C.din("5,00", centavos=False)}</div>
<div class="mini" style="top:1196px">{C.din("5,10", centavos=False)}</div>
<svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920" fill="none">
  <defs><marker id="sc" viewBox="0 0 12 12" refX="8" refY="6" markerWidth="5" markerHeight="5" orient="auto"><path d="M2 2 L10 6 L2 10" fill="none" stroke="{A.BRAND_DARK}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
  <path d="M434 952 C 486 952, 480 1072, 522 1084" stroke="{A.BRAND_DARK}" stroke-width="6" stroke-linecap="round" marker-end="url(#sc)"/>
  <path d="M434 1100 L 522 1100" stroke="{A.BRAND_DARK}" stroke-width="6" stroke-linecap="round" marker-end="url(#sc)"/>
  <path d="M434 1248 C 486 1248, 480 1128, 522 1116" stroke="{A.BRAND_DARK}" stroke-width="6" stroke-linecap="round" marker-end="url(#sc)"/>
</svg>
<div class="grande"><b>{C.din("5,00", centavos=False)}</b><span class="m">médio</span></div>
"""

HTML = K.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, C.CSS + CAPA_CSS, fundo="suave")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
