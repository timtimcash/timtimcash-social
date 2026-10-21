# -*- coding: utf-8 -*-
"""Reel de 15/02/2027 (segunda) · "Entrou, saiu, guardou" (Fluxo: o ano numa tela) · capa tinta · equipe fr.

Telas reais: captura_15.py, build 2026-10-19.5, conta de base (J/base_app, sem mudança), celular 390 px CSS em escala 3,
relógio da página em 15/02/2027 10:00. Fluxo, com o período digitado no calendário (De 01/03/2026, Até 28/02/2027): os mesmos
12 meses do gráfico "Fluxo detalhado" (Mar/26 a Fev/27, o padrão do gráfico). Números da tela (conferidos abaixo com assert):
"Resultado · 1 mar 2026 - 28 fev 2027 até 15/02" R$ 25.012,76; "Guardou 19,7% do que entrou"; "Entrou" R$ 127.253,36
(15 recebidas); "Saiu" R$ 102.240,60 (307 pagas); barra "20%" e "80% saiu"; "Top saídas": Casa R$ 29.836,80 (29%), Mercado
R$ 19.522,42 (19%), Educação R$ 18.626,00 (18%); "Resumo mensal" com 12 meses e o "Total do período". Só entram lançamentos
pagos ou recebidos (fevereiro vai até o dia 15). Conta: 127.253,36 − 102.240,60 = 25.012,76; 25.012,76 ÷ 127.253,36 = 19,66%.

python3 reel_15.py  |  REEL_PREVIA="0 0.5 1 2 3.4 4.6 6.4 8.8 11.2 13.4 14.4 16.4 19" python3 reel_15.py
"""
import os, sys, json
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro, brl

PASTA = "2027-02-15_reel-fluxo-o-ano-numa-tela"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("15")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- números (conferidos contra a tela)
ENTROU, SAIU = D("127253.36"), D("102240.60")
GUARDOU = ENTROU - SAIU
assert GUARDOU == D("25012.76")
PCT = (GUARDOU / ENTROU * 100).quantize(D("0.1"))
assert PCT == D("19.7")
TX = C["celular-fluxo-12-meses-alta.png"]["texto"]
for k in ["Resultado · 1 mar 2026 - 28 fev 2027", "até 15/02", "R$\n25.012\n,76", "Guardou 19,7% do que entrou", "Entrou\nR$\n127.253\n,36\n15 recebidas",
          "Saiu\nR$\n102.240\n,60\n307 pagas", "80% saiu", "Fluxo detalhado", "Mar/26 a Fev/27 · 12 meses", "Top entradas", "Top saídas",
          "Casa\nR$ 29.836,80 29%", "Mercado\nR$ 19.522,42 19%", "Educação\nR$ 18.626,00 18%", "Resumo mensal"]:
    assert k in TX, k
TAB = {l[0].split(" R$")[0]: l for l in C["linhas_tabela"]}
assert TAB["TOTAL DO PERÍODO"][0] == "TOTAL DO PERÍODO R$ 127.253,36 −R$ 102.240,60 R$ 25.012,76 R$ 115.627,76"
assert len([k for k in TAB if " de 20" in k]) == 12
# os 12 meses (para o desenho do fecho): entradas e saídas do Resumo mensal
MESES = [(k, D(v[0].split("R$ ")[1].split(" ")[0].replace(".", "").replace(",", ".")),
          D(v[0].split("−R$ ")[1].split(" ")[0].replace(".", "").replace(",", "."))) for k, v in TAB.items() if " de 20" in k]
assert sum(e for _, e, _ in MESES) == ENTROU and sum(s for _, _, s in MESES) == SAIU

# ---------------------------------------------------------------- caixas (px CSS do celular)
CA = C["celular-periodo-12-meses.png"]["caixas"]
DE_ATE = uniao(CA["de"], CA["ate"])
APLICAR = CA["aplicar"]
PER = C["trechos_periodo"]["1 mar 2026 - 28 fev 2027"][0]
GUARD = uniao(*C["trechos_cartao"]["Guardou [\\d,]+% do que entrou"])
RESULT = uniao(*C["trechos_resultado"]["R\\$ ?25\\.012 ?,76"])
CX = C["celular-fluxo-12-meses-alta.png"]["caixas"]
BARRA = [33, CX["barra"][1] - 3, 324, CX["barra"][3] + 6]
ENT_SAI = [31, CX["entrou"][1] - 4, 328, 64]
GRAF = uniao(CX["canvas"], CX["legenda_rec"])
TOPS = {l[0].split(" R$")[0]: l[1:] for l in C["linhas_top"]}
TOP3 = uniao(TOPS["Casa"], TOPS["Mercado"], TOPS["Educação"])
TOTAL = [15, TAB["TOTAL DO PERÍODO"][2], 360, TAB["TOTAL DO PERÍODO"][4]]
CAB = TAB["MÊS ENTRADAS SAÍDAS RESULTADO SALDO"] if "MÊS ENTRADAS SAÍDAS RESULTADO SALDO" in TAB else None

# ---------------------------------------------------------------- tempos (s)
SOBE = 2.75
T1, T2, T3, T4, T5 = (2.9, 5.3), (5.45, 7.75), (7.9, 10.2), (10.35, 12.65), (12.8, 15.4)
TQ_APL = 3.95
ARRASTO = 13.75                                       # o dedo arrasta a tabela para o lado
J_SAI = 15.4
T6 = 15.6
FIM = 18.05
DUR = 20.9

IMGS = [("c1", tela("celular-periodo-12-meses.png")), ("c2", tela("celular-fluxo-12-meses-alta.png")),
        ("c3", tela("celular-fluxo-12-meses-alta-tabela-arrastada.png"))]
TROCAS = [0, TQ_APL + .2, ARRASTO + .45]
EXTRA = K.aneis("aDeAte", "aPer", "aGuard", "aBarra", "aGraf", "aTop", "aTotal") + K.toques("tqApl", "tqArr")

# ---------------------------------------------------------------- gancho: entrou, saiu, guardou e a barra
PCT_PILL = '<span class="pp" id="gPct">19,7% do que entrou</span>'
LINHAS = [("Entrou", ENTROU, A.BRAND_DARK, "gE"), ("Saiu", SAIU, K.CORAL_TXT, "gS"), ("Guardou", GUARDOU, A.INK, "gG")]
CENTS = {"gE": ",36", "gS": ",60", "gG": ",76"}
LIN_HTML = "".join(f'<div class="gl" id="{i}l" style="top:{620 + k * 196}px"><span>{n}{PCT_PILL if i == "gG" else ""}</span><b style="color:{cor}"><small>R$</small><i id="{i}">0</i>'
                   f'<em id="{i}c">{CENTS[i]}</em></b></div>' for k, (n, v, cor, i) in enumerate(LINHAS))
# fecho: 12 meses passados (do Resumo mensal) e 6 meses futuros em traço
MAXV = float(max(max(e, s) for _, e, s in MESES))

CSS = f"""
.tit{{font-size:64px}}
.janela{{background:#F7F6F1}}
#gEb{{position:absolute;left:90px;top:300px}}
#gQ{{position:absolute;left:90px;top:350px;width:900px;font-size:120px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#gQ span{{color:{A.BRAND_DARK}}}
.gl{{position:absolute;left:90px;width:900px;display:flex;flex-direction:column;opacity:0}}
.gl span{{font-size:40px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em;line-height:1.1}}
.gl b{{font-size:136px;line-height:1;font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums;display:flex;align-items:baseline}}
.gl small{{font-size:56px;font-weight:600;margin-right:20px;letter-spacing:-.01em;color:{A.MUTED}}}
.gl i{{font-style:normal}}
.gl em{{font-style:normal;font-size:72px;font-weight:700;letter-spacing:-.03em;opacity:0}}
.pp{{display:inline-flex;align-items:center;height:56px;padding:0 24px;margin-left:20px;border-radius:999px;vertical-align:middle;
  background:{A.SOFT};color:{A.BRAND_DEEP};font-size:32px;font-weight:700;letter-spacing:-.02em;opacity:0}}
#gBar{{position:absolute;left:90px;top:1262px;width:900px;height:96px;border-radius:24px;overflow:hidden;background:{A.FIO}}}
#gBarV{{position:absolute;left:0;top:0;height:100%;background:{A.BRAND}}}
#gBarC{{position:absolute;right:0;top:0;height:100%;background:{A.CORAL}}}
#gBarL{{position:absolute;left:90px;top:1376px;width:900px;display:flex;justify-content:space-between;font-size:36px;font-weight:600;letter-spacing:-.02em;opacity:0}}
/* fecho: o que já aconteceu e o que vem */
#lt{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}}
.pb{{position:absolute;width:22px;border-radius:5px 5px 2px 2px}}
.fb{{position:absolute;width:22px;border-radius:5px 5px 2px 2px;border:4px dashed #A9A699;background:transparent}}
#hoje{{position:absolute;top:640px;height:640px;border-left:6px solid {A.INK}}}
#hojeL{{position:absolute;top:592px;font-size:34px;font-weight:700;color:{A.INK};letter-spacing:-.01em}}
.ltl{{position:absolute;top:1300px;font-size:40px;line-height:1.2;font-weight:700;letter-spacing:-.02em;color:{A.INK}}}
.ltl small{{display:block;font-size:34px;font-weight:500;color:{A.MUTED}}}
"""

# barras do fecho
BX0, BW, BG, BASE6, ALT6 = 96, 20, 2, 1240, 520
PASSO6 = 52
pb = []
for i, (m, e, s) in enumerate(MESES):
    x = BX0 + i * PASSO6
    he, hs = float(e) / MAXV * ALT6, float(s) / MAXV * ALT6
    pb.append(f'<i class="pb" id="pe{i}" style="left:{x}px;top:{BASE6 - he:.0f}px;height:{he:.0f}px;background:{A.BRAND}"></i>')
    pb.append(f'<i class="pb" id="ps{i}" style="left:{x + BW + BG}px;top:{BASE6 - hs:.0f}px;height:{hs:.0f}px;background:{A.CORAL}"></i>')
X_HOJE = BX0 + 12 * PASSO6 - 4
fb = "".join(f'<i class="fb" id="fb{j}" style="left:{X_HOJE + 16 + j * PASSO6}px;top:{BASE6 - 0.5 * ALT6:.0f}px;height:{0.5 * ALT6:.0f}px;width:{2 * BW + BG}px"></i>'
             for j in range(4))

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em <b>Fluxo</b>, os últimos 12 meses.</div>
  <div class="tit" id="t2"><b>Guardou 19,7%</b> do que entrou.</div>
  <div class="tit" id="t3">Mês a mês: <b>receitas, despesas</b> e o resultado.</div>
  <div class="tit" id="t4">Para onde foi: <b>Top saídas</b>.</div>
  <div class="tit" id="t5">E o <b>Resumo mensal</b>, mês a mês.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>

  <div class="tit" id="t6">O Fluxo mostra o que <b>já aconteceu</b>. O futuro fica na <b>Simulação futura</b>.</div>
  <div id="lt">
    {"".join(pb)}{fb}
    <div id="hoje" style="left:{X_HOJE + 8}px"></div><div id="hojeL" style="left:{X_HOJE - 30}px">Hoje</div>
    <div class="ltl" style="left:96px">Fluxo<small>o que já entrou e saiu</small></div>
    <div class="ltl" style="left:{X_HOJE + 16 + 4 * PASSO6 - 4 - 380}px;width:380px;text-align:right">Simulação futura<small>o que vem</small></div>
  </div>
</div>

<div class="cena papel" id="g">
  <div class="eyebrow" id="gEb">Fluxo · últimos 12 meses</div>
  <div id="gQ">Entrou, saiu, <span>guardou.</span></div>
  {LIN_HTML}
  <div id="gBar"><div id="gBarV"></div><div id="gBarC"></div></div>
  <div id="gBarL"><span style="color:{A.BRAND_DARK}">20% guardou</span><span style="color:{K.CORAL_TXT}">80% saiu</span></div>
</div>

{K.fim("Fluxo no timtimcash")}
"""

JS = f"""
const SOBE={SOBE}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, J_SAI={J_SAI}, T6={T6}, FIM={FIM};
const TQ_APL={TQ_APL}, ARRASTO={ARRASTO}, TROCAS={TROCAS};
const VAL = {json.dumps([float(ENTROU), float(SAIU), float(GUARDOU)])};
const PCT_SAIU = {float(SAIU / ENTROU):.4f};
poeAnel('aDeAte', {DE_ATE}, 8); poeAnel('aPer', {PER}, 14); poeAnel('aGuard', {GUARD}, 14); poeAnel('aBarra', {BARRA}, 8);
poeAnel('aGraf', {GRAF}, 8); poeAnel('aTop', {TOP3}, 8); poeAnel('aTotal', {TOTAL}, 4);
poeToque('tqApl', ...{centro(APLICAR)});
// câmera: o calendário; o cartão do período; o gráfico; Top saídas; o Resumo mensal
const CAM = [[0,0,195,505,1], [TQ_APL+.19, TQ_APL+.2, 195, 250, 1], [T3[0]-.1, T3[0]+.7, 195, 720, 1],
             [T4[0]-.1, T4[0]+.7, 195, 1430, 1], [T5[0]-.1, T5[0]+.7, 195, 1930, 1], [ARRASTO+.6, ARRASTO+1.2, 195, 2400, 1]];
function render(t){{
  // 1. gancho: os três números chegam e a barra se divide
  saiCima('g', t, SOBE);
  $('gQ').style.transform = `translateY(${{(-14*pout(t, -0.2, 1.3)).toFixed(1)}}px)`;
  const ids = ['gE','gS','gG'], a0 = [-0.35, -0.05, 0.25];
  for (let k=0;k<3;k++){{ const a = a0[k]; aparece(ids[k]+'l', t, a, 0, 30, .3);
    $(ids[k]).textContent = fmt(Math.floor(VAL[k]*pout(t, a, a+.75)), 0); $(ids[k]+'c').style.opacity = prog(t, a+.7, a+.85); }}
  $('gPct').style.opacity = prog(t, 0.95, 1.2);
  const bv = pout(t, -0.3, 0.35), bc = prog(t, 0.2, 0.95);
  $('gBarV').style.width = (900*bv)+'px'; $('gBarC').style.width = (900*PCT_SAIU*bc)+'px';
  $('gBarL').style.opacity = prog(t, 0.85, 1.15);
  // 2. a tela real
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, SOBE+.1, J_SAI);
  const ne = prog(t, SOBE+.1, SOBE+.7);
  $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(['c1','c2','c3'], t, TROCAS, 0);
  anel('aDeAte', t, T1[0]+.35, TQ_APL-.1); toque('tqApl', t, TQ_APL); anel('aPer', t, TQ_APL+.55, T1[1]);
  anel('aGuard', t, T2[0]+.3, T2[0]+1.35); anel('aBarra', t, T2[0]+1.35, T2[1]);
  anel('aGraf', t, T3[0]+.85, T3[1]); anel('aTop', t, T4[0]+.85, T4[1]); anel('aTotal', t, ARRASTO+1.15, J_SAI);
  // o dedo arrasta a tabela para o lado (revela Resultado e Saldo)
  {{ const tq = $('t_tqArr'), on = $('o_tqArr'); const p = prog(t, ARRASTO, ARRASTO+.45); const y = 2000;
    const x = 320 - 220*p; tq.style.left = (x*E)+'px'; tq.style.top = (y*E)+'px'; on.style.opacity = 0;
    tq.style.opacity = (t >= ARRASTO-.15 && t < ARRASTO+.7) ? Math.min(lin(t, ARRASTO-.15, ARRASTO), 1 - lin(t, ARRASTO+.5, ARRASTO+.7)) : 0;
    tq.style.transform = `scale(${{t >= ARRASTO && t < ARRASTO+.5 ? .86 : 1}})`; }}
  // 3. fecho: o que já aconteceu (Fluxo) e o que vem (Simulação futura)
  titulo('t6', t, T6, FIM+.4);
  const lo = prog(t, T6+.1, T6+.45); $('lt').style.opacity = lo;
  for (let i=0;i<12;i++){{ const a = T6 + .15 + i*.045; const p = pout(t, a, a+.35);
    ['pe','ps'].forEach(k => {{ const e = $(k+i); e.style.transform = `scaleY(${{p.toFixed(3)}})`; e.style.transformOrigin = '50% 100%'; }}); }}
  for (let j=0;j<4;j++){{ $('fb'+j).style.opacity = prog(t, T6+.9+j*.08, T6+1.2+j*.08); }}
  $('hoje').style.transform = `scaleY(${{prog(t, T6+.7, T6+1.0).toFixed(3)}})`; $('hoje').style.transformOrigin = '50% 100%';
  $('hojeL').style.opacity = prog(t, T6+.85, T6+1.1);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    w = 900
    pv = float(GUARDOU / ENTROU)
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:440px;width:900px">
    <div class="eyebrow">Fluxo · 12 meses</div>
    <div class="h1" style="font-size:132px;line-height:.96;margin-top:34px;color:#fff">Entrou, saiu, <span style="color:{A.MENTA}">guardou.</span></div>
  </div>
  <div style="position:absolute;left:84px;top:930px;display:flex;align-items:baseline;color:{A.MENTA};font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums">
    <span style="font-size:250px;line-height:1">19,7</span><span style="font-size:120px">%</span>
    <span style="font-size:44px;font-weight:600;letter-spacing:-.02em;color:{K.DARK_TEXTO};margin-left:24px">guardado</span></div>
  <div style="position:absolute;left:90px;top:1240px;width:{w}px;height:120px;border-radius:28px;overflow:hidden;background:{A.CORAL}">
    <div style="position:absolute;left:0;top:0;height:100%;width:{w * pv:.0f}px;background:{A.MENTA}"></div></div>
  <div style="position:absolute;left:90px;top:1386px;width:{w}px;display:flex;justify-content:space-between;font-size:40px;font-weight:600;letter-spacing:-.02em">
    <span style="color:{A.MENTA}">guardou</span><span style="color:{A.CORAL}">saiu</span></div>"""
    return K.pagina_capa(corpo, "", fundo="tinta")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
