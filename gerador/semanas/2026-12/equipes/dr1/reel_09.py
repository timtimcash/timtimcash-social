# -*- coding: utf-8 -*-
"""Reel de 09/12/2026 · "A jornada: sua história lá fora" (capa tinta, destaque menta), 1080 × 1920, 30 fps. Equipe dr1.

A linha do tempo desenhada de jul/23 a dez/26 com os dados da conta de exemplo, como no cartão "A jornada" do site:
- degraus = enviado acumulado nas datas reais das remessas (12/07/2023, 14/03/2024 e 18/04/2024, US$ 4.000 cada);
- linha tracejada = a trajetória na taxa medida (a TIR de "Ritmo do retorno", 3,6% ao ano na moeda), como o site desenha;
- ponto = o valor informado, US$ 13.310 em 30/11/2026.
Telas reais do build 2026-10-16.1 (capturas/captura09.py), conta de base, celular 390 px em escala 3, relógio em
09/12/2026 10:00: Remessas (aba USD), "US$ 13.310 na carteira hoje · +US$ 1.310,00 +10,9% em US$ · +R$ 7.235,46
+12,1% em R$" e o cartão "A jornada, desde jul/23" (Primeira remessa 12/07/2023 · Envios 3, a cada 14 meses, em média ·
Maior envio 4.000,00 · Média por envio 4.000,00); "Ritmo do retorno", ao ano: 3,6% na moeda.

python3 reel_09.py  |  REEL_PREVIA="0 0.7 2.4 4.2 6.2 7.9 9.6 11.2 12.6 13.8 14.9 16.8" python3 reel_09.py
"""
import os, sys
from datetime import date
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-12-09_reel-a-jornada-la-fora"
TRAB = C.trabalho("09")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas("09")
ARQ = CX["arquivos"]
MENTA = A.MENTA

# ---------------------------------------------------------------- números (conferidos contra a tela)
REM = [(date(2023, 7, 12), 4000), (date(2024, 3, 14), 4000), (date(2024, 4, 18), 4000)]
INFORMADO = (date(2026, 11, 30), 13310)
assert CX["carteira"][4] == "US$13.310 na carteira hoje"
assert CX["res_usd"][4] == "+US$ 1.310,00 +10,9% em US$" and CX["res_brl"][4] == "+R$ 7.235,46 +12,1% em R$"
assert CX["m_primeira"][4] == "Primeira remessa 12/07/2023 3 anos atrás"
assert CX["m_envios"][4] == "Envios 3 a cada 14 meses, em média" and CX["m_maior"][4] == "Maior envio 4.000,00 12/07/2023"
assert "ao ano ao mês 3,6% na moeda" in CX["ritmo_ano"][4] and "4,0% em reais" in CX["ritmo_ano"][4]   # depois do toque em "ao ano"
assert "Remessas" in CX["texto"] and "US$ 13.310 | enviados: US$ 12.000" in CX["texto"]
assert "Dec 09 2026" in CX["relogio"]

def valor(d, r):
    return sum(v * (1 + r) ** ((d - di).days / 365.25) for di, v in REM if d >= di)

lo, hi = 0.0, 0.2                      # a taxa constante que leva as remessas ao valor informado (a TIR)
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if valor(INFORMADO[0], mid) < INFORMADO[1] else (lo, mid)
TIR = (lo + hi) / 2
assert abs(TIR - 0.036) < 0.0015, TIR  # o site mostra 3,6% ao ano na moeda

# ---------------------------------------------------------------- gráfico (px do Reel)
X0, X1 = 130, 990
D0, D1 = date(2023, 7, 1), date(2026, 12, 31)
Y0, YM = 1460, 14000                     # base (US$ 0) e topo da escala
ALTURA = 760
def gx(d):
    return X0 + (d - D0).days / (D1 - D0).days * (X1 - X0)
def gy(v):
    return Y0 - v / YM * ALTURA

# degraus (enviado acumulado) até 31/12/2026
pts = [(gx(D0), gy(0))]
acum = 0
for d, v in REM:
    pts.append((gx(d), gy(acum)))
    acum += v
    pts.append((gx(d), gy(acum)))
pts.append((gx(D1), gy(acum)))
DEGRAU = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
SEGS = [abs(x1 - x0) + abs(y1 - y0) for (x0, y0), (x1, y1) in zip(pts, pts[1:])]
F1 = sum(SEGS[:3]) / sum(SEGS)            # até o pé do 2º degrau (o 1º envio e o trecho plano até mar/24)
# trajetória na taxa medida, de 12/07/2023 a 30/11/2026
traj = []
d = REM[0][0]
from datetime import timedelta
while d <= INFORMADO[0]:
    traj.append((gx(d), gy(valor(d, TIR))))
    d += timedelta(days=7)
traj.append((gx(INFORMADO[0]), gy(INFORMADO[1])))
TRAJ = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in traj)
PX, PY = gx(INFORMADO[0]), gy(INFORMADO[1])
Y12 = gy(12000)
ANOS = [date(2024, 1, 1), date(2025, 1, 1), date(2026, 1, 1)]
ROT_ANOS = [(D0, date(2024, 1, 1), "2023"), (date(2024, 1, 1), date(2025, 1, 1), "2024"), (date(2025, 1, 1), date(2026, 1, 1), "2025"),
            (date(2026, 1, 1), D1, "2026")]

def grafico():
    grades = "".join(f'<line x1="{X0}" x2="{X1}" y1="{gy(v):.1f}" y2="{gy(v):.1f}" class="gl"/>'
                     f'<text x="{X0 - 16}" y="{gy(v) + 10:.1f}" text-anchor="end" class="gt">{v // 1000}</text>' for v in (4000, 8000, 12000))
    anos = "".join(f'<line x1="{gx(d):.1f}" x2="{gx(d):.1f}" y1="{Y0}" y2="{Y0 + 18}" class="ax"/>' for d in ANOS)
    anos += "".join(f'<text x="{(gx(a) + gx(b)) / 2:.1f}" y="{Y0 + 56}" text-anchor="middle" class="at">{t}</text>' for a, b, t in ROT_ANOS)
    return f"""<svg id="graf" width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0;overflow:visible">
  <g id="eixos">{grades}
    <line x1="{X0}" x2="{X1}" y1="{Y0}" y2="{Y0}" class="ax"/>{anos}
    <text x="{X0 - 16}" y="{gy(14000) + 8:.1f}" text-anchor="end" class="gt">mil US$</text></g>
  <path id="traj" d="{TRAJ}" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-dasharray="14 14" pathLength="1000"/>
  <path id="deg" d="{DEGRAU}" fill="none" stroke="{MENTA}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" pathLength="1"/>
  {''.join(f'<circle id="pd{i}" cx="{gx(d):.1f}" cy="{gy(4000 * (i + 1)):.1f}" r="13" fill="{MENTA}" stroke="{A.INK}" stroke-width="6" style="opacity:0"/>' for i, (d, _) in enumerate(REM))}
  <g id="brk" style="opacity:0"><path d="M{PX + 26:.1f} {Y12:.1f} h14 V{PY:.1f} h-14" fill="none" stroke="{MENTA}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
  <circle id="ponto" cx="{PX:.1f}" cy="{PY:.1f}" r="18" fill="{A.BRAND}" stroke="#fff" stroke-width="6" style="opacity:0"/>
</svg>"""

# ---------------------------------------------------------------- tempos (s)
C2, C3, S2, T5, FIM = 2.8, 5.6, 8.6, 11.6, 15.4
DUR = 18.1
POP = 13.0
CAM = [[0, 0, 195, 300, 1.0], [T5 - .1, T5 + .55, 195, 1500, 1.0]]
RU = CX["res_usd"][:4]
R_M = [18, CX["m_primeira"][1] - 10, 354, CX["m_media"][1] + CX["m_media"][3] - CX["m_primeira"][1] + 20]
DE_M = C.de_camera(R_M, 195, 1500, 1.0)
P_M = [90, 1040, 900]
AN_P = C.anel_no_recorte("aP", R_M, P_M, CX["m_primeira"][:4], 8)
AN_E = C.anel_no_recorte("aE", R_M, P_M, CX["m_envios"][:4], 8)

CSS = f"""
.gl{{stroke:#262E27;stroke-width:2}}
.ax{{stroke:#3A443B;stroke-width:3}}
.gt,.at{{font-family:Inter;font-weight:600;font-size:28px;fill:{K.DARK_TEXTO};font-variant-numeric:tabular-nums}}
#hk{{position:absolute;left:90px;top:300px;width:900px;font-size:96px;line-height:1;font-weight:700;letter-spacing:-.05em;color:#fff}}
#hk span{{color:{MENTA}}}
#s1 .tit{{color:#fff}}
.rot{{position:absolute;font-size:34px;font-weight:700;letter-spacing:-.02em;color:#fff;white-space:nowrap;opacity:0;font-variant-numeric:tabular-nums}}
.rot small{{display:block;font-size:26px;font-weight:600;color:{K.DARK_TEXTO};letter-spacing:-.005em}}
#rP{{text-align:right}}
#rP b{{color:{MENTA}}}
#rB{{color:{MENTA}}}
#veu{{z-index:3}}
"""

CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="t4">Em Remessas, hoje: <b>US$&nbsp;13.310</b>, +10,9% em dólar.</div>
  <div class="tit" id="t5"><b>“A jornada”</b> guarda os marcos: a primeira, o maior envio, o ritmo.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">
    <div class="tela" id="tela"><img src="file://{os.path.join(TELAS, ARQ['a'])}">{K.aneis("aU")}</div>
    <div class="veu" id="veu"></div>
  </div>
  {C.pop_html("popM", os.path.join(TELAS, ARQ["a"]), AN_P + AN_E)}
</div>

<div class="cena tinta" id="s1">
  <div id="hk">Sua história lá fora começou em <span>jul/23</span>.</div>
  <div class="tit" id="c2">Mais dois envios em 2024: <b>US$&nbsp;12.000</b> ao todo.</div>
  <div class="tit" id="c3">A linha tracejada é o ritmo: <b>3,6% ao ano</b>, em dólar.</div>
  {grafico()}
  <div class="rot" id="r1" style="left:{gx(REM[0][0]) + 22:.0f}px;top:{gy(4000) - 96:.0f}px">US$ 4.000<small>12/07/2023</small></div>
  <div class="rot" id="r3" style="left:{gx(REM[2][0]) + 24:.0f}px;top:{gy(12000) + 18:.0f}px">US$ 12.000 enviados<small>mar/24 e abr/24</small></div>
  <div class="rot" id="rP" style="left:{PX - 420:.0f}px;width:380px;top:{PY - 112:.0f}px"><b>US$ 13.310</b><small>informado em 30/11/2026</small></div>
  <div class="rot" id="rB" style="left:{PX - 200:.0f}px;width:180px;text-align:right;top:{Y12 - 46:.0f}px;font-size:30px">+US$ 1.310</div>
</div>

{K.fim("Remessas no timtimcash")}
"""

JS = f"""
const C2={C2}, C3={C3}, S2={S2}, T5={T5}, FIM={FIM}, POP={POP}, CAM={CAM}, F1={F1:.4f};
const R_M={R_M}, DE_M={[round(v, 1) for v in DE_M]}, P_M={P_M};
poeAnel('aU', {RU}, 10);
function render(t){{
  // 1. a linha do tempo, na tinta: o primeiro degrau desde o primeiro quadro
  $('s1').style.transform = `translateY(${{-1920*prog(t, S2, S2+.45)}}px)`;
  titulo('hk', t, -1, C2-.35, 24);
  titulo('c2', t, C2, C3-.35); titulo('c3', t, C3, S2-.05);
  $('eixos').style.opacity = lin(t, -.2, .25);
  // o degrau: 0 a 0,28 (até o 1º envio e a subida), depois os outros dois e o resto até dez/26
  const dg = t < C2 ? F1*pout(t, .05, 1.4) : F1 + (1-F1)*pout(t, C2+.15, C2+1.7);
  $('deg').style.strokeDasharray = `${{dg.toFixed(4)}} 1`;
  $('pd0').style.opacity = lin(t, .9, 1.1); $('pd1').style.opacity = lin(t, C2+.55, C2+.75); $('pd2').style.opacity = lin(t, C2+.7, C2+.9);
  aparece('r1', t, .95, C2+.2, 16, .35); aparece('r3', t, C2+.95, 0, 16, .35);
  // a trajetória tracejada (taxa medida) e o ponto informado
  const tr = 1000*pout(t, C3+.1, C3+1.5);
  $('traj').style.strokeDasharray = '14 14'; $('traj').style.clipPath = `inset(0 ${{(100 - tr/10).toFixed(2)}}% 0 0)`;
  $('ponto').style.opacity = lin(t, C3+1.35, C3+1.55);
  $('ponto').style.transformBox = 'fill-box'; $('ponto').style.transformOrigin = 'center';
  $('ponto').style.transform = `scale(${{1 + .5*Math.exp(-6*Math.max(0, t-(C3+1.4)))*(t > C3+1.4 ? 1 : 0)}})`;
  aparece('rP', t, C3+1.45, 0, 14, .35);
  $('brk').style.opacity = prog(t, C3+1.7, C3+2.0); aparece('rB', t, C3+1.8, 0, 10, .3);
  // 2. a tela real: o cabeçalho de Remessas e o cartão "A jornada"
  titulo('t4', t, S2+.1, T5-.35); titulo('t5', t, T5, FIM-.1);
  janela('janela', t, S2, FIM-.1); janela('nota', t, S2, FIM-.1);
  camera('tela', t, CAM);
  anel('aU', t, S2+.9, T5-.2);
  $('veu').style.opacity = .62*prog(t, POP, POP+.45);
  recorte('popM', t, POP, 0, R_M, DE_M, P_M, .6, false);
  anel('aP', t, POP+.55, POP+1.35); anel('aE', t, POP+1.4, 0);
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (tinta, menta): três degraus
def degraus_capa():
    x = [90, 300, 560, 820, 990]
    y = [1470, 1270, 1070, 870]
    d = f"M{x[0]} {y[0]} H{x[1]} V{y[1]} H{x[2]} V{y[2]} H{x[3]} V{y[3]} H{x[4]}"
    pontos = "".join(f'<circle cx="{x[i + 1]}" cy="{y[i + 1]}" r="20" fill="{MENTA}" stroke="{A.INK}" stroke-width="8"/>' for i in range(3))
    return f"""<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">
  <line x1="90" x2="990" y1="1470" y2="1470" stroke="#3A443B" stroke-width="4"/>
  <path d="{d}" fill="none" stroke="{MENTA}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>{pontos}
</svg>"""

CAPA_CSS = f"""
.ct{{position:absolute;left:90px;top:430px;width:900px}}
.ct .h1{{font-size:130px;line-height:.96;color:#fff}}
.ct .h1 span{{color:{MENTA}}}
"""
CAPA_CORPO = f"""
{K.logo("tinta")}
{degraus_capa()}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Remessas · A jornada</div>
  <div class="h1">Sua história <span>lá fora</span></div></div>
"""

HTML = C.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="tinta")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
