# -*- coding: utf-8 -*-
"""Reel de 18/11/2026 (quarta) · "Até o mesmo dia" · capa verde suave · equipe r2.

Tela real: Comparar no celular (390 px CSS, escala 3), conta fictícia com o relógio em 18/11/2026 10:00
(captura_18.py). Números da tela: nov/26 R$ 6.571,50; out/26 (até o dia 18) R$ 6.349,15; Diferença +R$ 222,35, +4%;
"Novembro está em curso, então outubro entra só até o dia 18, para a conta ser justa."; "Quase toda a alta veio de
Bares e restaurantes, +R$ 186. O resto subiu R$ 36."; Ponte de variação: Bares e restaurantes +R$ 186,00,
Lazer e hobbies +R$ 124,00, Mercado +R$ 79,85, Presentes e doações −R$ 180,00, Demais 5 +R$ 12,50.
Outubro inteiro: R$ 8.215,00 (despesas do mês na conta fictícia; −20% seria a comparação injusta).
As barras do gancho seguem o gasto acumulado dia a dia da conta (estado.py), um segmento por dia.

python3 reel_18.py  |  REEL_PREVIA="0 1 2 ..." python3 reel_18.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, R2, MENOS, caixas, pagina

PASTA = "2026-11-18_reel-ate-o-mesmo-dia"
SAIDA = os.path.join(N, "saida", PASTA)
TRAB = os.path.join(R2, "trabalho", "18")
TELA = os.path.join(SAIDA, "telas", "celular-comparar-18-11.jpg")
C = caixas(PASTA)
ALT = C["altura_css"]

# gasto acumulado de cada dia (despesas pagas da conta fictícia, estado.py com hoje = 18/11/2026)
OUT = [0.0, 72.9, 471.6, 471.6, 843.6, 843.6, 1011.6, 1074.0, 1138.5, 5309.65, 5489.65, 5545.55, 5676.95, 5764.95, 5786.85,
       5876.75, 6349.15, 6349.15, 6754.15, 6796.15, 6984.35, 7066.25, 7124.95, 7243.85, 7243.85, 7585.85, 7681.85, 8022.4,
       8215.0, 8215.0, 8215.0]
NOV = [76.8, 489.6, 489.6, 877.6, 877.6, 1059.6, 1059.6, 1128.5, 1651.5, 5401.5, 5493.9, 5641.8, 5770.4, 5934.4, 6176.3,
       6571.5, 6571.5, 6571.5]
# conferência com a tela e com a pauta
assert C["textos"]["nota"].startswith("Novembro está em curso, então outubro entra só até o dia 18, para a conta ser justa.")
assert C["textos"]["dif"].replace(" ", "") == "Diferença\n+R$222,35\n+4%"
assert C["textos"]["quase"] == "Quase toda a alta veio de Bares e restaurantes, +R$ 186. O resto subiu R$ 36."
assert "R$6.571,50" in C["textos"]["topo"].replace(" ", "") and "R$6.349,15" in C["textos"]["topo"].replace(" ", "")
assert "+R$ 186,00" in C["textos"]["ponte"] and "−R$ 180,00" in C["textos"]["ponte"]
assert OUT[17] == 6349.15 and OUT[30] == 8215.0 and NOV[17] == 6571.5
assert round((6571.50 / 8215.00 - 1) * 100) == -20 and round(6571.50 - 6349.15, 2) == 222.35 and round(222.35 / 6349.15 * 100) == 4

DUR = 20.1
G_TIT_SAI = 2.45                     # o título do gancho sai
T1, T2 = (2.85, 4.95), (5.15, 7.05)
B_SAI = 7.05                         # a cena das barras sobe
T3, T4, T5 = (7.30, 9.50), (9.65, 11.85), (12.00, 14.30)
T6 = (14.45, 17.20)
FIM = 17.30
TOPO_NUM = round(C["nota_linha"][1] - 75)        # da nota do corte até a frase da causa
TOPO_PONTE = round(C["ponte"][1] + 7.5)          # o cartão "Ponte de variação"
assert C["quase"][1] + C["quase"][3] < TOPO_NUM + 500

# ---------------------------------------------------------------- barras: um segmento por dia
PD = 900 / 31                        # passo de um dia (px)
SW = PD - 5                          # largura do segmento
BX = 90
RN_Y, RO_Y, BH = 800, 1030, 108      # topo das barras de novembro e outubro, altura
XD18 = BX + 18 * PD - 2.5            # o vão depois do dia 18
SELO_X, SELO_Y = 400, 1330            # centro do selo
def segs(pref, n, y):
    return "".join(f'<div class="dseg" style="left:{BX + i * PD:.2f}px;top:{y}px"><i id="{pref}{i}"></i></div>' for i in range(n))

CSS = f"""
.tit{{font-size:70px}}
.tit b.neg{{color:{K.CORAL_TXT}}}
#bar{{background:{A.SOFT}}}
#bar .eyebrow{{position:absolute;left:90px;top:330px;color:{A.BRAND_DEEP}}}
#gTit{{position:absolute;left:90px;top:392px;width:900px;font-size:116px;line-height:.98;transform-origin:0 0}}
.dseg{{position:absolute;width:{SW:.2f}px;height:{BH}px;border-radius:8px;background:#fff;overflow:hidden}}
.dseg i{{position:absolute;left:0;top:0;bottom:0;width:0}}
.nov i{{background:{A.CORAL}}}
.out i{{background:#3F4A43}}
.rot{{position:absolute;left:90px;font-size:38px;font-weight:700;letter-spacing:-.02em;color:{A.INK}}}
.rot span{{font-weight:500;color:{A.MUTED}}}
.val{{position:absolute;right:90px;font-size:50px;font-weight:700;letter-spacing:-.04em;color:{A.INK};font-variant-numeric:tabular-nums}}
#corte{{position:absolute;left:{XD18 - 3:.1f}px;top:{RN_Y - 22}px;width:6px;height:{RO_Y + BH - RN_Y + 44}px;
  background:repeating-linear-gradient(to bottom,{A.INK} 0 14px,transparent 14px 24px);transform-origin:50% 0;transform:scaleY(0)}}
#corteTag{{position:absolute;left:{XD18:.1f}px;top:{RN_Y - 80}px;transform:translateX(-50%);background:{A.INK};color:#fff;font-size:28px;font-weight:700;
  padding:8px 18px;border-radius:999px;opacity:0;white-space:nowrap}}
#chave13{{position:absolute;left:{XD18 + 3:.1f}px;width:{BX + 31 * PD - 5 - XD18 - 3:.1f}px;top:{RO_Y + BH + 18}px;height:26px;border:5px solid {A.RED};border-top:0;
  border-radius:0 0 14px 14px;opacity:0}}
#txt13{{position:absolute;left:{XD18 + 3:.1f}px;width:{BX + 31 * PD - 5 - XD18 - 3:.1f}px;top:{RO_Y + BH + 56}px;text-align:center;font-size:44px;font-weight:700;
  letter-spacing:-.025em;color:{A.RED_TEXT};opacity:0}}
#selo{{position:absolute;left:{SELO_X - 150}px;top:{SELO_Y - 150}px;width:300px;height:300px}}
#seloIn{{position:absolute;inset:0;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;
  font-size:86px;font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums;background:{A.BRAND};
  box-shadow:0 18px 40px -18px rgba(15,20,16,.35)}}
#risco{{position:absolute;left:{SELO_X - 165}px;top:{SELO_Y - 7}px;width:330px;height:14px;border-radius:7px;background:{A.RED};
  transform-origin:50% 50%;transform:rotate(-24deg) scaleX(0)}}
#carimbo{{position:absolute;left:{SELO_X}px;top:{SELO_Y + 150}px;transform:translate(-50%,-50%) rotate(-7deg);white-space:nowrap;background:#fff;
  color:{A.RED_TEXT};border:6px solid {A.RED};border-radius:18px;padding:14px 30px;font-size:50px;font-weight:700;letter-spacing:-.02em;opacity:0}}
"""

CORPO = f"""
<div class="cena papel" id="tela">
  <div class="tit" id="t3">O Comparar faz esse corte <b>sozinho</b>.</div>
  <div class="tit" id="t4">Diferença: <b class="neg">+R$&nbsp;222,35</b>, ou&nbsp;+4%.</div>
  <div class="tit" id="t5">E aponta a causa: <b>Bares e restaurantes</b>.</div>
  <div class="tit" id="t6" style="font-size:88px">Não só o quanto.<br><b>O porquê.</b></div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{K.tela("tl", TELA, ALT, K.aneis("aNota", "aQuase", "aPonte") + K.aneis("aDif", cor="coral"))}</div>
</div>

<div class="cena" id="bar">
  <div class="eyebrow" id="gEye">Comparar</div>
  <div class="h1" id="gTit">Novembro saiu mais barato?</div>
  <div class="tit" id="t1" style="color:{A.INK}">Outubro inteiro tem <b style="color:{A.RED_TEXT}">13 dias a mais</b>.</div>
  <div class="tit" id="t2" style="color:{A.INK}">Até o mesmo dia, o gasto <b class="neg">subiu 4%</b>.</div>
  <div class="rot" style="top:{RN_Y - 62}px">novembro <span id="rotN">até hoje</span></div>
  <div class="val" id="vN" style="top:{RN_Y - 70}px">R$ 0</div>
  <div class="nov">{segs("n", 30, RN_Y)}</div>
  <div class="rot" style="top:{RO_Y - 62}px">outubro <span id="rotO">inteiro</span></div>
  <div class="val" id="vO" style="top:{RO_Y - 70}px">R$ 0</div>
  <div class="out">{segs("o", 31, RO_Y)}</div>
  <div id="corte"></div><div id="corteTag">dia 18</div>
  <div id="chave13"></div><div id="txt13">13 dias a mais</div>
  <div id="selo"><div id="seloIn">{MENOS}20%!</div></div>
  <div id="risco"></div>
  <div id="carimbo">Comparação injusta</div>
</div>

{K.fim("Comparar no timtimcash")}
"""

JS = f"""
const OUT={OUT}, NOV={NOV}, PD={PD:.4f};
const G_TIT_SAI={G_TIT_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, T6={list(T6)};
const B_SAI={B_SAI}, FIM={FIM};
const CX = {{ nota:{C['nota_linha']}, dif:{C['dif']}, quase:{C['quase']} }};
const PL = {C['ponte_linhas']};
const bares = PL.find(l => l[0].startsWith('Bares')), baresV = PL.find(l => l[0] === '+R$ 186,00');
poeAnel('aNota', [CX.nota[0], CX.nota[1]-2, CX.nota[2], 50], 10);
poeAnel('aDif', CX.dif, 9); poeAnel('aQuase', [CX.quase[0]-2, CX.quase[1]-4, CX.quase[2]+4, CX.quase[3]+8], 10);
poeAnel('aPonte', [bares[1]-2, bares[2]-4, (baresV[1]+baresV[3]) - bares[1] + 6, bares[4]+8], 8);
const CAM = [[0,0,195,250,1], [T3[0]+.3, T3[0]+.95, 195, {TOPO_NUM}+250, 1], [T6[0]-.1, T6[0]+.6, 195, {TOPO_PONTE}+250, 1]];
function acum(arr, d){{ if (d <= 0) return 0; const i = Math.min(arr.length, Math.floor(d)); return arr[i-1]; }}
function render(t){{
  // 1. gancho: os dias enchem (novembro até o dia 18, outubro inteiro), com o gasto acumulado de verdade
  const dN = 2 + 16*pout(t, 0, .95), dO = 2 + 29*pout(t, 0, .95);
  for (let i=0;i<30;i++) $('n'+i).style.width = (clamp(dN - i, 0, 1)*100) + '%';
  // depois do corte, os 13 dias de outubro se esvaziam
  const corte = prog(t, 4.45, 5.0);
  for (let i=0;i<31;i++){{ const f = clamp(dO - i, 0, 1) * (i >= 18 ? 1 - corte : 1); $('o'+i).style.width = (f*100) + '%';
    const m = i >= 18 ? prog(t, 3.35 + (i-18)*.025, 3.6 + (i-18)*.025) * (1 - prog(t, 5.0, 5.4)) : 0;
    $('o'+i).parentElement.style.boxShadow = m > 0 ? `inset 0 0 0 ${{(5*m).toFixed(2)}}px {A.RED}` : 'none'; }}
  const cents = t >= 4.45;
  const vN = acum(NOV, dN), vO = cents ? 8215 + (6349.15 - 8215)*corte : acum(OUT, dO);
  $('vN').textContent = 'R$ ' + (cents ? fmt(6571.5, 2) : fmt(Math.floor(vN), 0));
  $('vO').textContent = 'R$ ' + (cents ? fmt(vO, 2) : fmt(Math.floor(vO), 0));
  $('rotO').textContent = t >= 4.75 ? 'até o dia 18' : 'inteiro';
  $('rotN').textContent = t >= 4.75 ? 'até o dia 18' : 'até hoje';
  // selo −20%, risco e carimbo; depois o selo vira +4%
  const vira = t < 5.12 ? 1 - prog(t, 4.95, 5.12) : pback(t, 5.12, 5.45);
  const sp = pback(t, .85, 1.25);
  $('selo').style.opacity = lin(t, .85, 1.0);
  $('selo').style.transform = `scale(${{(.5+.5*sp).toFixed(3)}}) scaleX(${{vira.toFixed(3)}}) rotate(${{t < 5.12 ? -6 : 0}}deg)`;
  const s4 = t >= 5.12;
  $('seloIn').textContent = s4 ? '+4%' : '{MENOS}20%!';
  $('seloIn').style.background = s4 ? '{K.CORAL_TXT}' : '{A.BRAND}';
  const rk = prog(t, 1.45, 1.7) * (1 - prog(t, 4.75, 4.95));
  $('risco').style.transform = `rotate(-24deg) scaleX(${{rk.toFixed(3)}})`; $('risco').style.opacity = rk > 0 ? 1 : 0;
  const cb = pback(t, 1.6, 1.9);
  $('carimbo').style.opacity = lin(t, 1.6, 1.7) * (1 - prog(t, 4.75, 4.95));
  $('carimbo').style.transform = `translate(-50%,-50%) rotate(-7deg) scale(${{(1.5 - .5*cb).toFixed(3)}})`;
  // títulos
  const gs = 1 - prog(t, G_TIT_SAI, G_TIT_SAI + .3);
  $('gTit').style.opacity = gs; $('gEye').style.opacity = gs;
  $('gTit').style.transform = `scale(${{1 + .018*lin(t, 0, G_TIT_SAI)}}) translateY(${{-30*(1-gs)}}px)`;
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]);
  // o corte no dia 18 e os 13 dias a mais
  $('corte').style.transform = `scaleY(${{pout(t, 2.9, 3.35).toFixed(3)}})`;
  const ct = pback(t, 3.1, 3.45); $('corteTag').style.opacity = lin(t, 3.1, 3.2);
  $('corteTag').style.transform = `translateX(-50%) scale(${{(.6+.4*ct).toFixed(3)}})`;
  const k13 = prog(t, 3.55, 3.9) * (1 - prog(t, 4.95, 5.3));
  $('chave13').style.opacity = k13; $('txt13').style.opacity = k13;
  saiCima('bar', t, B_SAI);

  // 2. tela real do Comparar
  titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]); titulo('t6', t, T6[0], T6[1]);
  entra('janela', t, B_SAI+.05, 0); entra('nota', t, B_SAI+.05, 0);
  camera('tl', t, CAM);
  anel('aNota', t, T3[0]+1.0, T3[1]-.1); anel('aDif', t, T4[0]+.3, T4[1]-.1); anel('aQuase', t, T5[0]+.3, T5[1]-.1);
  anel('aPonte', t, T6[0]+.75, T6[1]+.2);

  // 3. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (verde suave)
CN_Y, CO_Y, CBH = 1050, 1292, 118
def csegs(cls, y):
    return "".join(f'<div class="cs {cls}" style="left:{BX + i * PD:.2f}px;top:{y}px"></div>' for i in range(18))
CSS_CAPA = f"""
.cs{{position:absolute;width:{SW:.2f}px;height:{CBH}px;border-radius:8px}}
.cs.n{{background:{A.CORAL}}}
.cs.o{{background:#3F4A43}}
.crot{{position:absolute;left:90px;font-size:40px;font-weight:700;letter-spacing:-.02em;color:{A.INK}}}
.crot span{{font-weight:500;color:{A.MUTED}}}
#cCorte{{position:absolute;left:{XD18 - 3:.1f}px;top:{CN_Y - 96}px;width:6px;height:{CO_Y + CBH - CN_Y + 120}px;
  background:repeating-linear-gradient(to bottom,{A.INK} 0 14px,transparent 14px 24px)}}
#cTag{{position:absolute;left:{XD18:.1f}px;top:{CN_Y - 160}px;transform:translateX(-50%);background:{A.INK};color:#fff;font-size:32px;font-weight:700;
  padding:10px 24px;border-radius:999px;white-space:nowrap}}
#cSelo{{position:absolute;left:{812 - 156}px;top:{(CN_Y + CO_Y + CBH) // 2 - 156}px;width:312px;height:312px;border-radius:50%;background:{K.CORAL_TXT};
  color:#fff;display:flex;align-items:center;justify-content:center;font-size:118px;font-weight:700;letter-spacing:-.05em;
  box-shadow:0 22px 44px -20px rgba(15,20,16,.4);transform:rotate(-6deg)}}
"""
CORPO_CAPA = f"""
{K.logo("suave")}
<div style="position:absolute;left:90px;top:478px;width:900px">
  <div class="eyebrow" style="margin-bottom:34px">Comparar</div>
  <div class="h1" style="font-size:122px;line-height:.98">Até o mesmo dia</div>
</div>
<div class="crot" style="top:{CN_Y - 62}px">novembro</div>
{csegs("n", CN_Y)}
<div class="crot" style="top:{CO_Y - 62}px">outubro</div>
{csegs("o", CO_Y)}
<div id="cCorte"></div><div id="cTag">dia 18</div>
<div id="cSelo">+4%</div>
"""
CAPA = K.pagina_capa(CORPO_CAPA, CSS_CAPA, fundo="suave")
HTML = pagina(CORPO, CSS, JS)

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
