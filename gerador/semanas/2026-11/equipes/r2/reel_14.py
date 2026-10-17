# -*- coding: utf-8 -*-
"""Reel de 14/11/2026 (sábado) · "Metade do mês: quanto dá por dia?" · capa papel · equipe r2.

Tela real: Orçamentos no celular (390 px CSS, escala 3), conta fictícia com o relógio em 14/11/2026 10:00
(captura_14.py). Números da tela: "14 de 30 dias · 47% do período"; limite definido R$ 5.450,00 em 5 categorias;
usado R$ 2.128,50 (39% do limite); sobra do limite R$ 3.321,50, "R$ 207 por dia nos 16 dias que faltam";
Bares e restaurantes R$ 712 de R$ 600 (119%), "Excedeu em R$ 112", no ritmo fecha em R$ 1.527;
Mercado 44%, no limite, no ritmo fecha em R$ 1.887; Transporte 25%, Saúde 11%, Lazer e hobbies 0%.

python3 reel_14.py                                   vídeo final (reel.mp4, capa.jpg e previa.mp4 em N/saida/<pasta>/)
REEL_PREVIA="0 0.5 1.2 ..." python3 reel_14.py       quadros soltos em trabalho/14/previa/
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, R2, caixas, pagina

PASTA = "2026-11-14_reel-metade-do-mes"
SAIDA = os.path.join(N, "saida", PASTA)
TRAB = os.path.join(R2, "trabalho", "14")
TELA = os.path.join(SAIDA, "telas", "celular-orcamentos-14-11.jpg")
C = caixas(PASTA)
ALT = C["altura_css"]

# conferência dos números com o texto capturado da tela
assert "14 de 30 dias · 47% do período" in C["textos"]["cab"]
assert "R$ 5.450,00" in C["textos"]["cab"] and "R$ 2.128,50" in C["textos"]["cab"]
assert "R$ 3.321,50" in C["textos"]["sobra"] and C["textos"]["pordia"] == "R$ 207 por dia nos 16 dias que faltam"
assert "R$ 712 de R$ 600" in C["textos"]["bares"] and "R$ 1.527" in C["textos"]["bares"] and "Excedeu em R$ 112" in C["textos"]["bares"]
assert "R$ 880 de R$ 2.000" in C["textos"]["mercado"] and "R$ 1.887" in C["textos"]["mercado"] and "NO LIMITE" in C["textos"]["mercado"]
# a conta do site: R$ 3.321,50 em 16 dias = R$ 207,59 (mostra R$ 207); o ritmo de Bares: 712,70 / 14 x 30 = 1.527,21
assert int(3321.50 / 16) == 207 and int(712.70 / 14 * 30) == 1527 and int(880.90 / 14 * 30) == 1887

DUR = 21.4
G_SAI = 2.70                                  # o gancho sobe
T1, T2 = (2.95, 5.55), (5.75, 8.30)
PAN1 = (8.30, 9.00)                           # panorâmica até "Progresso por categoria"
T3, T4 = (8.55, 10.65), (10.80, 12.90)
PAN2 = (12.85, 13.45)
T5 = (13.05, 14.90)
J_SAI = 15.30                                 # a janela sai (já coberta pela folha)
P_IN = 14.75                                  # a folha da previsão sobe (0,45 s)
FIM = 18.70
TOPO_CAT = round(C["faixa_passaram"][1] - 13)  # topo da janela (px CSS): de "Já passaram do limite" até Transporte
TOPO_TRANQ = round(C["tranquilas"][1] + C["tranquilas"][3] + 20 - 500)   # de Mercado até Lazer e hobbies
assert TOPO_TRANQ + 500 <= ALT and C["mercado"][1] >= TOPO_TRANQ

# ---------------------------------------------------------------- gancho: a barra do mês
NSEG, HOJE = 30, 14
X0, BW, GAP = 90, 24.2, 6.0                   # 30 segmentos em 900 px
BAR_Y, BAR_H = 1010, 170
def seg_x(d):                                  # x do meio do vão depois do dia d
    return X0 + d * (BW + GAP) - GAP / 2
x15, x30 = X0 + HOJE * (BW + GAP), X0 + NSEG * (BW + GAP) - GAP
segs = "".join(f'<div class="seg" style="left:{X0 + i * (BW + GAP):.1f}px"><i id="f{i}"></i></div>' for i in range(NSEG))

# ---------------------------------------------------------------- previsão: o ritmo de Bares e restaurantes
PX0, PX1 = 150, 950                            # dia 0 e dia 30
PY0, PYK = 1380, 0.3875                        # R$ 0 em y = 1380; 0,3875 px por real
def px(d): return PX0 + (PX1 - PX0) * d / 30
def py(v): return PY0 - v * PYK
HX, HY = px(14), py(712.70)
FX, FY = px(30), py(712.70 / 14 * 30)
LY = py(600)
LEN = ((HX - PX0) ** 2 + (HY - PY0) ** 2) ** .5
X118 = px(600 / 712.70 * 14)                  # onde a linha cruza o limite

svg_prev = f"""<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0">
  <defs><clipPath id="clipT"><rect id="clipR" x="{HX - 12:.1f}" y="600" width="0" height="800"/></clipPath>
    <clipPath id="clipZ"><rect id="clipZr" x="{X118 - 4:.1f}" y="600" width="0" height="800"/></clipPath></defs>
  <line x1="{PX0}" y1="{PY0}" x2="{PX1}" y2="{PY0}" stroke="{A.NEUTRO}" stroke-width="4" stroke-linecap="round"/>
  <g id="gLim" opacity="0">
    <line x1="{PX0}" y1="{LY:.1f}" x2="{PX1}" y2="{LY:.1f}" stroke="{A.MUTED}" stroke-width="4" stroke-dasharray="2 14" stroke-linecap="round"/>
    <text x="{PX0}" y="{LY + 48:.1f}" font-family="Inter" font-weight="600" font-size="30" fill="{A.MUTED}">limite R$ 600</text>
  </g>
  <polygon id="zAcima" points="{X118:.1f},{LY:.1f} {HX:.1f},{HY:.1f} {FX:.1f},{FY:.1f} {FX:.1f},{LY:.1f}" fill="#F7E3D9" opacity="0" clip-path="url(#clipZ)"/>
  <text id="tAcima" x="{FX - 24:.1f}" y="{LY - 26:.1f}" text-anchor="end" font-family="Inter" font-weight="700" font-size="30" fill="{K.CORAL_TXT}" opacity="0">acima do limite</text>
  <line id="lHoje" x1="{HX:.1f}" y1="{PY0}" x2="{HX:.1f}" y2="{HY:.1f}" stroke="{A.INK}" stroke-width="4" stroke-dasharray="3 11" stroke-linecap="round" opacity="0"/>
  <path id="pReal" d="M{PX0},{PY0} L{HX:.1f},{HY:.1f}" fill="none" stroke="{A.CORAL}" stroke-width="16" stroke-linecap="round"
    stroke-dasharray="{LEN:.1f}" stroke-dashoffset="{LEN:.1f}"/>
  <path d="M{HX:.1f},{HY:.1f} L{FX:.1f},{FY:.1f}" fill="none" stroke="{A.CORAL}" stroke-width="11" stroke-dasharray="3 23" stroke-linecap="round" clip-path="url(#clipT)"/>
  <circle id="cHoje" cx="{HX:.1f}" cy="{HY:.1f}" r="18" fill="{A.CORAL}" stroke="{A.BG}" stroke-width="7" opacity="0"/>
  <circle id="cFim" cx="{FX:.1f}" cy="{FY:.1f}" r="20" fill="{K.CORAL_TXT}" stroke="{A.BG}" stroke-width="7" opacity="0"/>
  <text x="{PX0}" y="{PY0 + 52}" font-family="Inter" font-weight="600" font-size="30" fill="{A.MUTED}">dia 1</text>
  <text x="{HX:.1f}" y="{PY0 + 52}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="{A.INK}">hoje, dia 14</text>
  <text x="{PX1}" y="{PY0 + 52}" text-anchor="end" font-family="Inter" font-weight="600" font-size="30" fill="{A.MUTED}">dia 30</text>
</svg>"""

CSS = f"""
.tit{{font-size:70px}}
.tit b.neg{{color:{A.RED_TEXT}}}
.tit b.amb{{color:{A.AMBER_TEXT}}}
/* gancho */
#g .eyebrow{{position:absolute;left:90px;top:340px}}
#g .h1{{position:absolute;left:90px;top:400px;width:920px;font-size:118px;line-height:1.0;transform-origin:0 0}}
#g .h1 b{{color:{A.BRAND_DARK}}}
.seg{{position:absolute;top:{BAR_Y}px;width:{BW}px;height:{BAR_H}px;border-radius:9px;background:{A.FIO};overflow:hidden}}
.seg i{{position:absolute;left:0;top:0;bottom:0;width:0;background:{A.BRAND}}}
#mesRot{{position:absolute;left:90px;top:{BAR_Y - 70}px;font-size:36px;font-weight:700;letter-spacing:-.015em;color:{A.INK}}}
#mesDia{{position:absolute;right:90px;top:{BAR_Y - 84}px;font-size:40px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em}}
#mesDia b{{font-size:56px;font-weight:700;color:{A.INK};font-variant-numeric:tabular-nums;letter-spacing:-.03em}}
#hoje{{position:absolute;top:{BAR_Y - 24}px;width:8px;margin-left:-4px;height:{BAR_H + 48}px;border-radius:4px;background:{A.INK}}}
#hojeTag{{position:absolute;top:{BAR_Y - 96}px;background:{A.INK};color:#fff;font-size:32px;font-weight:700;
  padding:10px 24px;border-radius:999px;white-space:nowrap;opacity:0}}
.dRot{{position:absolute;top:{BAR_Y + BAR_H + 30}px;font-size:30px;font-weight:600;color:{A.MUTED}}}
#chave{{position:absolute;left:{x15:.1f}px;width:{x30 - x15:.1f}px;top:{BAR_Y + BAR_H + 80}px;height:28px;border:5px solid {A.BRAND_DARK};border-top:0;
  border-radius:0 0 14px 14px;opacity:0}}
#chaveTxt{{position:absolute;left:{x15:.1f}px;width:{x30 - x15:.1f}px;top:{BAR_Y + BAR_H + 128}px;text-align:center;font-size:52px;font-weight:700;
  letter-spacing:-.03em;color:{A.BRAND_DARK};opacity:0}}
/* previsão */
#prev .h2{{position:absolute;left:90px;top:290px;width:900px;font-size:84px;line-height:1.02}}
#prev .h2 b{{color:{A.BRAND_DARK}}}
#prevSob{{position:absolute;left:{PX0}px;top:566px;font-size:28px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{K.CORAL_TXT};opacity:0}}
#prevHoje{{position:absolute;right:{1080 - (HX - 36):.0f}px;top:{HY - 150:.0f}px;text-align:right;opacity:0}}
#prevFim{{position:absolute;right:90px;top:{FY - 150:.0f}px;text-align:right;opacity:0;transform-origin:100% 100%}}
.pv-k{{font-size:32px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em}}
.pv-v{{font-size:62px;font-weight:700;letter-spacing:-.04em;color:{A.INK};font-variant-numeric:tabular-nums;line-height:1.05}}
#prevFim .pv-v{{font-size:80px;color:{K.CORAL_TXT}}}
"""

aneis = K.aneis("aSobra", "aDia", "aTranq") + K.aneis("aBares", cor="coral") + K.aneis("aMerc", cor="ambar")

CORPO = f"""
<div class="cena papel" id="tela">
  <div class="tit" id="t1">No exemplo, sobram <b>R$ 3.321,50</b> do limite.</div>
  <div class="tit" id="t2">Dá <b>R$ 207 por dia</b> nos 16 dias que faltam.</div>
  <div class="tit" id="t3">Bares e restaurantes <b class="neg">já passou</b> do limite.</div>
  <div class="tit" id="t4">Mercado: <b class="amb">no limite</b>. No ritmo, fecha em R$ 1.887.</div>
  <div class="tit" id="t5">Transporte, Saúde e Lazer: <b>tranquilas</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{K.tela("tl", TELA, ALT, aneis)}</div>
</div>

<div class="cena papel" id="prev" style="transform:translateY(1920px)">
  <div class="h2" id="prevTit">O ritmo de hoje vira a <b>previsão</b> do fim do mês.</div>
  {svg_prev}
  <div id="prevSob">Bares e restaurantes · exemplo</div>
  <div id="prevHoje"><div class="pv-k">até hoje</div><div class="pv-v">R$ 712</div></div>
  <div id="prevFim"><div class="pv-k">no ritmo, fecha em</div><div class="pv-v">R$ 1.527</div></div>
</div>

<div class="cena papel" id="g">
  <div class="eyebrow">Orçamentos</div>
  <div class="h1" id="gTit">Metade do mês.<br>Quanto ainda dá <b>por dia</b>?</div>
  <div id="mesRot">Novembro</div>
  <div id="mesDia">dia <b id="cont">3</b> de 30</div>
  {segs}
  <div class="dRot" style="left:{X0}px">1</div>
  <div class="dRot" style="right:90px">30</div>
  <div id="hoje"></div><div id="hojeTag">hoje</div>
  <div id="chave"></div><div id="chaveTxt">faltam 16 dias</div>
</div>

{K.fim("Orçamentos no timtimcash")}
"""

JS = f"""
const NSEG={NSEG}, HOJE={HOJE}, X0={X0}, BW={BW}, GAP={GAP};
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, PAN1={list(PAN1)}, PAN2={list(PAN2)};
const J_SAI={J_SAI}, P_IN={P_IN}, FIM={FIM};
const C = {{ sobra:{C['sobra']}, dia:{C['pordia']}, bares:{C['bares']}, merc:{C['mercado']}, tranq:{C['tranquilas']} }};
poeAnel('aSobra', C.sobra, 10); poeAnel('aDia', [C.dia[0]-5, C.dia[1]-3.5, C.dia[2]+10, C.dia[3]+7], 6);
poeAnel('aBares', C.bares, 10); poeAnel('aMerc', C.merc, 10); poeAnel('aTranq', [C.tranq[0], C.tranq[1]-6, C.tranq[2], C.tranq[3]+8], 10);
// câmera: [a, b, fx, fy, zoom]; fy = topo + 250 com zoom 1
const CAM = [[0, 0, 195, 250, 1], [3.35, 4.0, 195, {C['cab'][1] - 10 + 250}, 1], [T2[0]+.05, T2[0]+.75, 195, {C['sobra'][1] + 28:.1f}, 1.2],
             [PAN1[0], PAN1[1], 195, {TOPO_CAT} + 250, 1], [PAN2[0], PAN2[1], 195, {TOPO_TRANQ} + 250, 1]];
const PREV = {{ hx:{HX:.2f}, fx:{FX:.2f}, len:{LEN:.1f}, x118:{X118:.2f} }};
function render(t){{
  // 1. gancho: a barra do mês enche até o dia 14 desde o quadro 0
  const dias = 3 + (HOJE-3)*pout(t, 0, 1.15);
  for (let i=0;i<NSEG;i++) $('f'+i).style.width = (clamp(dias - i, 0, 1)*100) + '%';
  $('cont').textContent = Math.min(HOJE, Math.max(1, Math.floor(dias + 1e-6)));
  const hx = X0 + dias*(BW+GAP) - GAP/2;
  $('hoje').style.left = hx + 'px';
  const tg = pback(t, 1.05, 1.45); const tag = $('hojeTag');
  tag.style.opacity = lin(t, 1.05, 1.2); tag.style.left = hx + 'px';
  tag.style.transform = `translateX(-50%) scale(${{.6+.4*tg}})`;
  for (let i=HOJE;i<NSEG;i++){{ const p = prog(t, 1.25 + (i-HOJE)*.03, 1.45 + (i-HOJE)*.03);
    $('f'+i).parentElement.style.boxShadow = `inset 0 0 0 ${{(5*p).toFixed(2)}}px {A.BRAND}`; }}
  $('chave').style.opacity = prog(t, 1.6, 1.9);
  $('chaveTxt').style.opacity = prog(t, 1.7, 2.0); $('chaveTxt').style.transform = `translateY(${{(1-prog(t,1.7,2.0))*16}}px)`;
  $('gTit').style.transform = `scale(${{1 + .018*lin(t, 0, G_SAI)}})`;
  saiCima('g', t, G_SAI);

  // 2. tela real: a sobra do limite e o valor por dia; depois as faixas das categorias
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]);
  titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  entra('janela', t, G_SAI+.05, J_SAI); entra('nota', t, G_SAI+.05, J_SAI);
  camera('tl', t, CAM);
  anel('aSobra', t, 3.9, T1[1]-.15); anel('aDia', t, T2[0]+.8, T2[1]-.1);
  anel('aBares', t, PAN1[1]+.05, T3[1]-.1); anel('aMerc', t, T4[0]+.3, T4[1]-.15); anel('aTranq', t, PAN2[1]+.05, T5[1]-.1);

  // 3. a previsão: a linha do ritmo até hoje e o pontilhado até o dia 30
  $('prev').style.opacity = 1; sobe('prev', t, P_IN);
  const P0 = P_IN + .25;
  $('gLim').setAttribute('opacity', prog(t, P0+.3, P0+.6));
  $('prevSob').style.opacity = prog(t, P0+.3, P0+.6);
  $('pReal').style.strokeDashoffset = PREV.len*(1-pout(t, P0+.4, P0+.95));
  $('lHoje').setAttribute('opacity', prog(t, P0+.85, P0+1.1));
  const ch = pback(t, P0+.9, P0+1.25); $('cHoje').setAttribute('opacity', lin(t, P0+.9, P0+1.0));
  $('cHoje').setAttribute('r', (18*(.5+.5*ch)).toFixed(2));
  aparece('prevHoje', t, P0+.95, 0, 24);
  $('clipR').setAttribute('width', ((PREV.fx - PREV.hx + 40)*pout(t, P0+1.15, P0+1.75)).toFixed(1));
  $('zAcima').setAttribute('opacity', prog(t, P0+1.1, P0+1.4));
  $('clipZr').setAttribute('width', ((PREV.hx - PREV.x118 + 8) + (PREV.fx - PREV.hx + 40)*pout(t, P0+1.15, P0+1.75)).toFixed(1)); $('tAcima').setAttribute('opacity', prog(t, P0+1.6, P0+1.9));
  const cf = pback(t, P0+1.7, P0+2.05); $('cFim').setAttribute('opacity', lin(t, P0+1.7, P0+1.8));
  $('cFim').setAttribute('r', (20*(.5+.5*cf)).toFixed(2));
  aparece('prevFim', t, P0+1.75, 0, 24);
  $('prevFim').style.transform += ` scale(${{.9+.1*pback(t, P0+1.75, P0+2.2)}})`;

  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (papel)
CY = 1050
capa_segs = "".join(
    f'<div class="cseg{" ok" if i < HOJE else ""}" style="left:{X0 + i * (BW + GAP):.1f}px"></div>' for i in range(NSEG))
CSS_CAPA = f"""
.cseg{{position:absolute;top:{CY}px;width:{BW}px;height:116px;border-radius:9px;background:#FFFFFF;box-shadow:inset 0 0 0 5px {A.BRAND}}}
.cseg.ok{{background:{A.BRAND};box-shadow:none}}
#cHoje{{position:absolute;left:{seg_x(HOJE) - 4:.1f}px;top:{CY - 22}px;width:8px;height:160px;border-radius:4px;background:{A.INK}}}
#cTag{{position:absolute;left:{seg_x(HOJE):.1f}px;top:{CY - 92}px;transform:translateX(-50%);background:{A.INK};color:#fff;font-size:32px;font-weight:700;
  padding:10px 24px;border-radius:999px;white-space:nowrap}}
#cValor{{position:absolute;left:90px;top:{CY + 186}px;display:flex;align-items:baseline;gap:26px}}
#cValor .v{{font-size:196px;font-weight:700;letter-spacing:-.055em;line-height:.86;color:{A.BRAND_DEEP};font-variant-numeric:tabular-nums}}
#cValor .s{{font-size:76px;font-weight:700;letter-spacing:-.045em;color:{A.INK}}}
#cNota{{position:absolute;left:90px;top:{CY + 400}px;font-size:40px;font-weight:600;letter-spacing:-.02em;color:{A.BRAND_DEEP}}}
"""
CORPO_CAPA = f"""
{K.logo("suave")}
<div style="position:absolute;left:90px;top:490px;width:900px">
  <div class="eyebrow" style="margin-bottom:34px">Orçamentos</div>
  <div class="h1" style="font-size:112px;line-height:.98">Metade do mês: quanto ainda dá por dia?</div>
</div>
{capa_segs}
<div id="cHoje"></div><div id="cTag">hoje, dia 14</div>
<div id="cValor"><div class="v">R$ 207</div><div class="s">por dia</div></div>
<div id="cNota">nos 16 dias que faltam, no exemplo</div>
"""
CAPA = K.pagina_capa(CORPO_CAPA, CSS_CAPA, fundo="suave")
HTML = pagina(CORPO, CSS, JS)

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
