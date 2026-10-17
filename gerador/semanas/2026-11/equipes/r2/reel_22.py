# -*- coding: utf-8 -*-
"""Reel de 22/11/2026 (domingo) · "Seu ano tem meses quentes" · capa verde · equipe r2.

Telas reais (captura_22.py), conta fictícia com o relógio em 22/11/2026 10:00 e o período Personalizado de 01/12/2025 a 30/11/2026:
- computador: o cartão "Mapa de calor" com 12 meses (dez/25 a nov/26), com a célula "Outras · jan" escolhida (R$ 1.509,80);
- celular: "Recorrentes vs pontuais", com toques na parte "Pontual" das barras: Dez/25 R$ 980,00 (Presentes de Natal),
  Jan/26 R$ 1.390,00 (IPVA · parcela única R$ 1.180,00 e IPTU · 1ª parcela R$ 210,00, Impostos e Taxas),
  Jul/26 R$ 640,00 (Hospedagem nas férias, Viagem).
O gancho desenha cada mês do ano como um termômetro de quadradinhos; a "temperatura" segue o gasto total de cada mês na conta
(o mesmo dado da "Sazonalidade": jan 9.420, jul 8.620 e dez 9.860 ficam acima da média de R$ 8,3 mil).

python3 reel_22.py  |  REEL_PREVIA="0 1 2 ..." python3 reel_22.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, R2, caixas, pagina

PASTA = "2026-11-22_reel-o-mapa-de-calor"
SAIDA = os.path.join(N, "saida", PASTA)
TRAB = os.path.join(R2, "trabalho", "22")
T = os.path.join(SAIDA, "telas")
MAPA = os.path.join(T, "computador-mapa-de-calor-12-meses.jpg")
RP = {k: os.path.join(T, f"celular-recorrentes-pontuais-{k}.jpg") for k in ["0", "dez", "jan", "jul"]}
C = caixas(PASTA)
M = C["mapa"]

# conferência com a tela
assert C["periodo"][0] == "1 dez 2025 - 30 nov 2026" and C["periodo_comp"][0] == "1 dez 2025 - 30 nov 2026"
assert [m[0] for m in M["mes"]][:3] == ["dez/25", "jan", "fev"] and M["mes"][7][0] == "jul"
outras = [c[0] for c in M["cel"][7 * 12:8 * 12]]
assert outras[:2] == ["1,1 mil", "1,5 mil"] and outras[7] == "760"
assert M["detalhe"][0].startswith("Outras · janeiro")
assert "Pontual · Dez/25" in C["rp_dez"]["det_txt"] and "Presentes de Natal" in C["rp_dez"]["det_txt"] and "R$ 980,00" in C["rp_dez"]["det_txt"]
assert "Pontual · Jan/26" in C["rp_jan"]["det_txt"] and "IPVA · parcela única" in C["rp_jan"]["det_txt"] and "IPTU · 1ª parcela" in C["rp_jan"]["det_txt"]
assert "R$ 1.390,00" in C["rp_jan"]["det_txt"] and "Impostos e Taxas" in C["rp_jan"]["det_txt"]
assert "Pontual · Jul/26" in C["rp_jul"]["det_txt"] and "Hospedagem nas férias" in C["rp_jul"]["det_txt"] and "R$ 640,00" in C["rp_jul"]["det_txt"]

DUR = 20.35
G_SAI = 2.50
H1, H2 = (2.75, 5.05), (5.20, 7.90)
ZOOM = (3.90, 4.70)
PAN_JUL = (6.50, 7.10)
HM_SAI = 7.85
P1, P2, P3 = (8.20, 10.45), (10.60, 12.45), (12.60, 14.45)
TQ = [9.50, 10.75, 12.75]                  # toques em Dez/25, Jan/26 e Jul/26
PP_SAI = 14.45
CL = 14.45                                 # a folha em tinta sobe (0,45 s): 2027
FIM = 17.60

# ---------------------------------------------------------------- gancho: um termômetro de quadradinhos por mês
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
TOT = [9420, 8050, 7690, 7830, 7910, 8040, 8620, 8285, 7780, (7940 + 8215) / 2, 8120, 9860]   # média de cada mês do ano (out/25 a out/26)
MEDIA = (7940 + 8120 + 9860 + 9420 + 8050 + 7690 + 7830 + 7910 + 8040 + 8620 + 8285 + 7780 + 8215) / 13
assert round(MEDIA) == 8289
def nivel(v):
    return 5 if v >= 8500 else 4 if v >= 8200 else 3 if v >= 7900 else 2
NIV = [nivel(v) for v in TOT]
QUENTES = [i for i, v in enumerate(TOT) if v > MEDIA]
assert QUENTES == [0, 6, 11] and NIV == [5, 3, 2, 2, 3, 3, 5, 4, 2, 3, 3, 5]
CORES = ["#fbf2e0", "#f5dfae", "#ecc178", "#df9c55", "#cd6b42"]   # as faixas do Mapa de calor do site (claro para quente)
QX0, QP, QS, QG = 90, 76, 64, 12              # x inicial, passo, lado do quadrado, vão vertical
QB = 1330                                    # base dos termômetros
quad = "".join(f'<div class="q" id="q{i}_{k}" style="left:{QX0 + i * QP}px;top:{QB - (k + 1) * QS - k * QG}px"><i id="c{i}_{k}" style="background:{CORES[k]}"></i></div>'
               for i in range(12) for k in range(5))
rots = "".join(f'<div class="qm" id="m{i}" style="left:{QX0 + i * QP - 8}px">{m}</div>' for i, m in enumerate(MESES))

# ---------------------------------------------------------------- mapa de calor (computador): janela larga
JX, JY, JW, JH = 90, 660, 900, 520
PW, PH = C["mapa_painel"]
mes = {m[0]: m for m in M["mes"]}
col = lambda nome: mes[nome][1:5]           # [x, y, w, h] do rótulo do mês
dez, jan, jul = col("dez/25"), col("jan"), col("jul")
cel = {(r, c_): M["cel"][r * 12 + c_][2:6] for r in range(8) for c_ in range(12)}
A_DEZ = [dez[0] - 4, dez[1] - 4, dez[2] + 8, cel[(7, 0)][1] + cel[(7, 0)][3] - dez[1] + 8]
A_JAN = cel[(7, 1)]
A_JUL = cel[(7, 7)]
S_GERAL = 0.97 * JW / (2 * PW)              # o cartão inteiro na janela
S_ZOOM = 0.92                               # 1,84 px do Reel por px CSS
FX_ZOOM = 20 + JW / (4 * S_ZOOM)            # do rótulo "Casa" até abril
FY_ZOOM = (dez[1] - 14 + cel[(7, 0)][1] + cel[(7, 0)][3] + 14) / 2
FX_JUL = 530                                # julho à direita, sem chegar à coluna de setembro (que tem uma célula vazia)
assert FX_JUL + JW / (4 * S_ZOOM) < col('set')[0] and FX_JUL + JW / (4 * S_ZOOM) > jul[0] + jul[2] + 8

# ---------------------------------------------------------------- recorrentes vs pontuais (celular)
CV = C["rp_dez"]["canvas"]                  # o gráfico; a lista de Jan/26 é a mais alta
MEIA = 1000 / (2 * 2 * 1.15)                # meia altura visível (px CSS) com zoom 1,15
FY_RP = CV[1] - 10 + MEIA                   # o topo da janela logo acima do gráfico (sem cortar o cartão de cima)
assert C["rp_jan"]["det"][1] + C["rp_jan"]["det"][3] + 8 < FY_RP + MEIA
def det(k):
    d = C["rp_" + k]["det"]
    return [d[0] + 14, d[1], d[2], d[3]]
TOQ = {k: [C["rp_" + k]["toque"][0] + 14, C["rp_" + k]["toque"][1]] for k in ["dez", "jan", "jul"]}
ALT_RP = max(1057, 720)
camadas = "".join(f'<img id="rp{k}" src="file://{RP[k]}" style="left:28px;top:0;width:724px;opacity:{1 if k == "0" else 0}">' for k in ["0", "dez", "jan", "jul"])

# ---------------------------------------------------------------- fecho: 2027, o ano todo em 2 linhas de 6 meses
FW, FH, FG, FY0 = 140, 168, 12, 900
MOTIVO = {0: "impostos", 6: "férias", 11: "presentes"}
def fpos(i):
    return 90 + (i % 6) * (FW + FG), FY0 + (i // 6) * (FH + FG)
anos = "".join(
    f'<div class="a7" id="s{i}" style="left:{fpos(i)[0]:.1f}px;top:{fpos(i)[1]}px"><i id="si{i}"></i><span class="a7m" id="sm{i}">{m}</span>'
    + (f'<span class="mot" id="mot{i}">{MOTIVO[i]}</span>' if i in MOTIVO else "") + '</div>'
    for i, m in enumerate(MESES))

CSS = f"""
.tit{{font-size:70px}}
.tit.grande{{font-size:104px;line-height:1.0;top:296px}}
/* gancho */
#g .eyebrow{{position:absolute;left:90px;top:330px}}
#gTit{{position:absolute;left:90px;top:392px;width:920px;font-size:120px;line-height:.98;transform-origin:0 0;color:#fff}}
#gTit b{{color:{A.CORAL}}}
.q{{position:absolute;width:{QS}px;height:{QS}px;border-radius:12px;background:#1E271F}}
.q i{{position:absolute;inset:0;border-radius:12px;opacity:0}}
.qm{{position:absolute;top:{QB + 22}px;width:{QS + 16}px;text-align:center;font-size:30px;font-weight:600;color:{K.DARK_TEXTO}}}
/* mapa de calor */
#notaM{{position:absolute;left:{JX}px;top:{JY - 46}px;font-size:26px;font-weight:500;color:{A.MUTED};opacity:0}}
#jm{{position:absolute;left:{JX}px;top:{JY}px;width:{JW}px;height:{JH}px;border-radius:28px;overflow:hidden;background:{K.FUNDO_TELA};
  border:2px solid {A.FIO};box-shadow:0 2px 4px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.28);opacity:0}}
#tm{{position:absolute;left:0;top:0;width:{2 * PW}px;height:{2 * PH}px;transform-origin:0 0}}
#tm img{{position:absolute;left:0;top:0;width:{2 * PW}px;height:{2 * PH}px}}
/* recorrentes vs pontuais */
#tp img{{position:absolute;display:block;height:auto}}
/* fecho */
#cl .h2{{position:absolute;left:90px;top:320px;width:900px;font-size:100px;line-height:1.0;color:#fff}}
#cl .h2 b{{color:{A.MENTA}}}
#ano{{position:absolute;left:90px;top:{FY0 - 74}px;font-size:44px;font-weight:700;letter-spacing:-.02em;color:{A.MENTA}}}
.a7{{position:absolute;width:{FW}px;height:{FH}px;border-radius:22px;background:#1E271F;opacity:0;overflow:hidden}}
.a7 i{{position:absolute;inset:0;background:{K.CORAL_TXT};opacity:0}}
.a7m{{position:absolute;left:16px;top:16px;font-size:36px;font-weight:700;letter-spacing:-.02em;color:{K.DARK_TEXTO}}}
.mot{{position:absolute;left:16px;bottom:18px;font-size:24px;font-weight:700;letter-spacing:-.01em;color:#fff;opacity:0;white-space:nowrap}}
"""

aneis_m = K.aneis("aDez", "aJan", "aJul")

CORPO = f"""
<div class="cena papel" id="hm">
  <div class="tit" id="h1">No Mapa de calor, cada quadrado é uma categoria num mês.</div>
  <div class="tit" id="h2">Dezembro, janeiro e julho: <b>mais quentes</b>.</div>
  <div id="notaM">{K.NOTA}</div>
  <div id="jm"><div id="tm"><img src="file://{MAPA}">{aneis_m}</div></div>
</div>

<div class="cena" id="pp" style="background:transparent">
  <div class="tit grande" id="p1">Dezembro: <b>presentes</b>.</div>
  <div class="tit grande" id="p2">Janeiro: <b>impostos</b>.</div>
  <div class="tit grande" id="p3">Julho: <b>férias</b>.</div>
  <div class="nota" id="notaP">{K.NOTA}</div>
  <div class="janela" id="jp"><div class="tela" id="tp" style="height:{ALT_RP * 2}px">{camadas}{K.aneis("rDez", "rJan", "rJul")}{K.toques("tq0", "tq1", "tq2")}</div></div>
</div>

<div class="cena tinta" id="cl" style="transform:translateY(1920px)">
  <div class="h2" id="clTit">Os meses caros se repetem. <b>Dá para ver antes.</b></div>
  <div id="ano">2027</div>
  {anos}
</div>

<div class="cena tinta" id="g">
  <div class="eyebrow">Relatórios</div>
  <div class="h1" id="gTit">Seu ano tem <b>meses quentes</b>.</div>
  {quad}
  {rots}
</div>

{K.fim("Relatórios no timtimcash")}
"""

JS = f"""
const NIV={NIV}, CORES={CORES}, QUENTES={QUENTES};
const G_SAI={G_SAI}, H1={list(H1)}, H2={list(H2)}, ZOOM={list(ZOOM)}, PAN_JUL={list(PAN_JUL)}, HM_SAI={HM_SAI};
const P1={list(P1)}, P2={list(P2)}, P3={list(P3)}, TQ={TQ}, PP_SAI={PP_SAI}, CL={CL}, FIM={FIM};
poeAnel('aDez', {A_DEZ}, 8); poeAnel('aJan', {A_JAN}, 9); poeAnel('aJul', {A_JUL}, 9);
poeAnel('rDez', {det('dez')}, 8); poeAnel('rJan', {det('jan')}, 8); poeAnel('rJul', {det('jul')}, 8);
poeToque('tq0', {TOQ['dez'][0]}, {TOQ['dez'][1]}); poeToque('tq1', {TOQ['jan'][0]}, {TOQ['jan'][1]}); poeToque('tq2', {TOQ['jul'][0]}, {TOQ['jul'][1]});
const CAM_M = [[0,0,{PW / 2:.1f},{PH / 2:.1f},{S_GERAL:.4f}], [ZOOM[0], ZOOM[1], {FX_ZOOM:.1f}, {FY_ZOOM:.1f}, {S_ZOOM}], [PAN_JUL[0], PAN_JUL[1], {FX_JUL:.1f}, {FY_ZOOM:.1f}, {S_ZOOM}]];
const CAM_P = [[0,0,195,250,1], [8.75, 9.35, 195, {FY_RP:.1f}, 1.15]];
function render(t){{
  // 1. gancho: cada mês acende de baixo para cima, do claro ao coral, como um termômetro
  for (let i=0;i<12;i++){{
    const ti = -0.30 + 0.085*i;
    for (let k=0;k<5;k++){{
      const e = $('c'+i+'_'+k);
      const p = k < NIV[i] ? pout(t, ti + .10*k, ti + .10*k + .22) : 0;
      e.style.opacity = p; e.style.transform = `scale(${{(.55 + .45*p).toFixed(3)}})`;
    }}
  }}
  QUENTES.forEach(i => {{ const m = $('m'+i); const p = prog(t, 1.45, 1.75); m.style.color = p > .5 ? '#fff' : '{K.DARK_TEXTO}'; m.style.fontWeight = p > .5 ? 700 : 600;
    const top = $('q'+i+'_4'); const pul = Math.max(0, Math.sin(Math.PI*clamp((t-1.55)/.45, 0, 1)));
    top.style.transform = `scale(${{(1 + .14*pul).toFixed(3)}})`; }});
  $('gTit').style.transform = `scale(${{1 + .018*lin(t, 0, G_SAI)}})`;
  saiCima('g', t, G_SAI);

  // 2. o Mapa de calor do computador, 12 meses: o cartão inteiro, depois o zoom e a panorâmica até julho
  titulo('h1', t, H1[0], H1[1]); titulo('h2', t, H2[0], H2[1]);
  entra('jm', t, G_SAI+.05, HM_SAI); entra('notaM', t, G_SAI+.05, HM_SAI);
  camera('tm', t, CAM_M, {JW}, {JH});
  anel('aDez', t, H2[0]+.25, PAN_JUL[0]-.2); anel('aJan', t, H2[0]+.55, PAN_JUL[0]-.2); anel('aJul', t, PAN_JUL[1]+.05, HM_SAI-.1);

  // 3. Recorrentes vs pontuais no celular: um toque em cada mês quente
  titulo('p1', t, P1[0], P1[1]); titulo('p2', t, P2[0], P2[1]); titulo('p3', t, P3[0], P3[1]);
  entra('jp', t, HM_SAI+.25, 0); entra('notaP', t, HM_SAI+.25, 0);
  camera('tp', t, CAM_P);
  const est = ['0', 'dez', 'jan', 'jul'];
  const vis = [1 - prog(t, TQ[0]+.12, TQ[0]+.2), prog(t, TQ[0]+.12, TQ[0]+.2) * (1 - prog(t, TQ[1]+.12, TQ[1]+.2)),
               prog(t, TQ[1]+.12, TQ[1]+.2) * (1 - prog(t, TQ[2]+.12, TQ[2]+.2)), prog(t, TQ[2]+.12, TQ[2]+.2)];
  est.forEach((k, i) => $('rp'+k).style.opacity = vis[i]);
  toque('tq0', t, TQ[0]); toque('tq1', t, TQ[1]); toque('tq2', t, TQ[2]);
  anel('rDez', t, TQ[0]+.45, P1[1]-.05); anel('rJan', t, TQ[1]+.45, P2[1]-.05); anel('rJul', t, TQ[2]+.45, P3[1]+.3);

  // 4. fecho em tinta: os meses quentes de 2027 já aparecem
  sobe('cl', t, CL);
  $('ano').style.opacity = prog(t, CL+.35, CL+.6);
  for (let i=0;i<12;i++){{ const p = pback(t, CL+.4 + .03*i, CL+.7 + .03*i); const s = $('s'+i);
    s.style.opacity = lin(t, CL+.4 + .03*i, CL+.5 + .03*i); s.style.transform = `scale(${{(.6+.4*p).toFixed(3)}})`; }}
  QUENTES.forEach((i, n) => {{ const a = CL+.8 + .12*n; const p = prog(t, a, a+.25);
    $('si'+i).style.opacity = p; $('sm'+i).style.color = p > .5 ? '#fff' : '{K.DARK_TEXTO}';
    const pul = Math.max(0, Math.sin(Math.PI*clamp((t - a)/.4, 0, 1)));
    $('s'+i).style.transform = `scale(${{(1 + .08*pul).toFixed(3)}})`;
    const m = $('mot'+i); m.style.opacity = prog(t, a+.15, a+.4); m.style.transform = `translateY(${{(1-prog(t, a+.15, a+.4))*12}}px)`; }});

  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (verde, sem coral)
GRADE = [[2, 1, 2, 1, 3, 5],
         [3, 2, 1, 2, 2, 4],
         [1, 2, 3, 1, 2, 4],
         [2, 1, 2, 2, 1, 3]]
TONS = {1: A.BRAND_DARK, 2: A.VERDE_LUZ, 3: A.MENTA, 4: A.MENTA_CLARA, 5: "#FFFFFF"}
CW, CH, CG, CY = 135, 118, 18, 930
capa_q = "".join(
    f'<div class="cq{" dest" if (r, c_) == (0, 5) else ""}" style="left:{90 + c_ * (CW + CG)}px;top:{CY + r * (CH + CG)}px;background:{TONS[v]}"></div>'
    for r, linha in enumerate(GRADE) for c_, v in enumerate(linha))
CSS_CAPA = f"""
.cq{{position:absolute;width:{CW}px;height:{CH}px;border-radius:18px}}
.cq.dest{{box-shadow:0 0 0 9px {A.BRAND},0 0 0 17px #fff}}
"""
CORPO_CAPA = f"""
{K.logo("verde")}
<div style="position:absolute;left:90px;top:478px;width:900px">
  <div class="eyebrow" style="margin-bottom:34px">Relatórios</div>
  <div class="h1" style="font-size:118px;line-height:.98">Seu ano tem meses quentes</div>
</div>
{capa_q}
"""
CAPA = K.pagina_capa(CORPO_CAPA, CSS_CAPA, fundo="verde")
HTML = pagina(CORPO, CSS, JS)

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
