# -*- coding: utf-8 -*-
"""Reel de 28/01/2027 (quinta) · "Janeiro de 2027 contra janeiro de 2026" · capa tinta · equipe js.

Telas reais: captura_28.py, build 2026-10-19.5, celular 390 × 1000 em escala 3, conta fictícia de J/base_app (sem mudança), relógio
da página em 28/01/2027 10:00. Comparar (abre com "Período anterior", dez/26) -> toque em "Mesmo período em 2026" -> "Comparar com
jan/26"; "Janeiro de 2027 está em curso, então janeiro de 2026 entra só até o dia 28, para a conta ser justa." (o corte no mesmo
dia); jan/27 R$ 10.821,70 · Diferença +R$ 1.401,70 +15% · jan/26 R$ 9.420; "Quase toda a alta veio de Educação, +R$ 1.226. O resto
subiu R$ 175." -> "Totais lado a lado" -> "Analítico": Educação R$ 2.676,00 +R$ 1.226,00 · Impostos e Taxas R$ 1.236,00 −R$ 154,00
-> Transações (Janeiro 2027), busca "escolar": "2 transações · 2 pagas · 0 pendentes · somam R$ 1.226,00" (Uniforme escolar
−R$ 286,00 em 18/01 e Material escolar −R$ 940,00 em 12/01).
Conferência (fotos em telas/, fora do vídeo): Transações de 01/01/2026 a 28/02/2027, busca "ipva": IPVA 2027 −R$ 1.236,00 (20/01/2027)
e IPVA · parcela única −R$ 1.180,00 (20/01/2026); busca "iptu": IPTU 2027 · 1ª parcela −R$ 215,00 pendente (10/02/2027) e IPTU ·
1ª parcela −R$ 210,00 (12/01/2026). Impostos e Taxas: 1.180 + 210 = 1.390 em jan/26 e 1.236 em jan/27: −R$ 154 = +R$ 56 do IPVA
− R$ 210 do IPTU, que em 2027 vence em fevereiro.
Em janeiro, "Este mês" e "No ano" são o mesmo período (jan/27) e o site marca "No ano"; o vídeo fala da janela "jan/27".
Diferença para 18/11 (comparou com o mês anterior): aqui é o mesmo mês do ano passado.

python3 reel_28.py  |  REEL_PREVIA="0 0.5 1 1.8 3.8 6.4 9.2 11.8 14.4 17.0 19.4" python3 reel_28.py
"""
import os, sys, json
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A
MENOS = C.MENOS

PASTA = "2027-01-28_reel-janeiro-contra-janeiro"
SAIDA = C.saida(PASTA)
TELAS = C.telas(PASTA)
TRAB = C.trabalho("28")
CX = C.caixas(PASTA)
P1, P2, P3, P4 = (CX[f"celular-comparar-{n}.jpg"] for n in ["1-periodo-anterior", "2-mesmo-periodo", "3-totais", "4-analitico"])
P5 = CX["celular-transacoes-1-escolar.jpg"]
CI, CU = CX["celular-conferencia-transacoes-ipva.jpg"]["texto"], CX["celular-conferencia-transacoes-iptu.jpg"]["texto"]

# ---------------------------------------------------------------- conferência com a tela
t2 = P2["texto"].replace("\n", " | ")
assert "Comparar com | jan/26 | Período anterior | Mesmo período em 2026" in t2
assert "Janeiro de 2027 está em curso, então janeiro de 2026 entra só até o dia 28, para a conta ser justa." in t2
assert P2["cartoes"]["foco_t"] == "jan/27 R$10.821,70" and P2["cartoes"]["dif_t"] == "Diferença +R$1.401,70 +15%" and P2["cartoes"]["base_t"] == "jan/26 R$9.420"
assert "Quase toda a alta veio de Educação, +R$ 1.226. O resto subiu R$ 175." in t2
assert "Comparar com | dez/26" in P1["texto"].replace("\n", " | ")
LIN = {l[0].split(" R$")[0].split(" −R$")[0]: l for l in P4["tabela"]["linhas"]}
assert LIN["Educação"][0] == "Educação R$ 2.676,00 +R$ 1.226,00" and LIN["Impostos e Taxas"][0] == "Impostos e Taxas R$ 1.236,00 −R$ 154,00"
assert LIN["Total de despesas"][0] == "Total de despesas R$ 10.821,70 +R$ 1.401,70"
assert P5["resumo"][4] == "2 transações · 2 pagas · 0 pendentes · somam R$ 1.226,00 · 801 no histórico" and P5["busca"][4] == "escolar"
assert "Uniforme escolar | Educação · Conta corrente | −R$ 286,00" in P5["texto"].replace("\n", " | ")
assert "Material escolar | Educação · Conta corrente | −R$ 940,00" in P5["texto"].replace("\n", " | ")
ci, cu = CI.replace("\n", " | "), CU.replace("\n", " | ")
assert "qua · 20 de janeiro | Editar | Excluir | IPVA 2027 | Impostos e Taxas · Conta corrente | −R$ 1.236,00 | paga" in ci
assert "ter · 20 de janeiro, 2026 | Editar | Excluir | IPVA · parcela única | Impostos e Taxas · Conta corrente | −R$ 1.180,00 | paga" in ci
assert "qua · 10 de fevereiro | Editar | Excluir | IPTU 2027 · 1ª parcela | Impostos e Taxas · Conta corrente | −R$ 215,00 | pendente" in cu
assert "seg · 12 de janeiro, 2026 | Editar | Excluir | IPTU · 1ª parcela | Impostos e Taxas · Conta corrente | −R$ 210,00 | paga" in cu
assert D("940") + D("286") == D("1226") and D("10821.70") - D("9420") == D("1401.70") and round(D("1401.70") / D("9420") * 100) == 15
assert D("1236") - (D("1180") + D("210")) == D("-154") and D("1236") - D("1180") == D("56")
assert "Jan 28 2027" in CX["relogio"]

# ---------------------------------------------------------------- caixas (px CSS da foto)
f = lambda b, F: C.na_foto(b, F["rolagem"])
CHIPS = C.uniao(P1["chip_anterior"][:4], P1["chip_mesmo"][:4])
CHIP_MESMO = P1["chip_mesmo"][:4]
AVISO = [52, P2["aviso_txt"][1] - 3, 306, 42]
DIF = P2["cartoes"]["dif"]; FOCO = P2["cartoes"]["foco"]; BASEC = P2["cartoes"]["base"]
CARTOES = C.uniao(FOCO, DIF, BASEC)
CAUSA = P2["causa"][:4]
SEG = f(P3["seg"], P3)
L_EDU = f(LIN["Educação"][1:5], P4)
L_IMP = f(LIN["Impostos e Taxas"][1:5], P4)
RESUMO = P5["resumo"][:4]
LINHAS5 = [l[1:5] for l in P5["linhas"] if l[0].startswith(("Uniforme", "Material"))]
assert len(LINHAS5) == 2
L_ESC = C.uniao(*LINHAS5)

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.6
T1, T2, T3, T4, T5 = (2.9, 5.25), (5.45, 7.65), (7.85, 10.35), (10.55, 13.05), (13.25, 15.65)
TQ_MESMO, TQ_ANALITICO = 4.6, 11.05
X_TOTAIS, X_ESC = 10.5, 13.2         # cortes: "Totais lado a lado" (como quem rola) e Transações com a busca
J_SAI = 15.7
S6 = (15.9, 18.75)
FIM = 18.8
DUR = 21.55

IMGS = [("c1", os.path.join(TELAS, "celular-comparar-1-periodo-anterior.jpg")), ("c2", os.path.join(TELAS, "celular-comparar-2-mesmo-periodo.jpg")),
        ("c3", os.path.join(TELAS, "celular-comparar-3-totais.jpg")), ("c4", os.path.join(TELAS, "celular-comparar-4-analitico.jpg")),
        ("c5", os.path.join(TELAS, "celular-transacoes-1-escolar.jpg"))]
EXTRA = K.aneis("aChips", "aAviso", "aDif", "aCausa", "aEdu", "aRes", "aEsc") + K.aneis("aImp", cor="ambar") + K.toques("tqMesmo", "tqAna")

CSS = f"""
#g{{background:{A.BG}}}
#gTop{{position:absolute;left:90px;top:300px;width:900px}}
#gTop .h1{{font-size:100px;line-height:1;margin-top:30px;color:{A.INK};text-wrap:balance}}
#gTop .h1 b{{color:{K.CORAL_FORTE};font-weight:700}}
.gb{{position:absolute;width:300px;border-radius:22px 22px 6px 6px;transform-origin:50% 100%}}
.gvl{{position:absolute;width:420px;text-align:center;font-size:76px;font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums;white-space:nowrap}}
.gvl small{{font-size:36px;font-weight:600;margin-right:10px;color:{A.MUTED};letter-spacing:-.01em}}
.gml{{position:absolute;width:300px;text-align:center;font-size:40px;font-weight:700;letter-spacing:-.02em;color:{A.INK}}}
#gPct{{position:absolute;left:390px;top:720px;width:300px;text-align:center;opacity:0}}
#gPct span{{display:inline-flex;align-items:center;height:84px;padding:0 34px;border-radius:999px;background:#F6DCD2;color:{K.CORAL_FORTE};font-size:52px;font-weight:700;letter-spacing:-.03em}}
#gNota{{position:absolute;left:90px;top:1530px;width:900px;text-align:center;font-size:32px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em;opacity:0}}
#gBase{{position:absolute;left:90px;top:1452px;width:900px;border-top:4px solid {A.FIO}}}
/* cena 6: os impostos */
#s6t{{position:absolute;left:90px;top:280px;width:900px;font-size:66px;line-height:1.06;font-weight:700;letter-spacing:-.045em;opacity:0}}
#s6t b{{color:{A.BRAND_DARK}}}
.im{{position:absolute;left:90px;width:900px;background:#fff;border:2px solid {A.FIO};border-radius:36px;padding:34px 40px;opacity:0;
  box-shadow:0 1px 2px rgba(15,20,16,.04),0 14px 34px -16px rgba(15,20,16,.14)}}
.im .k{{font-size:30px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{A.MUTED}}}
.im .v{{display:flex;align-items:baseline;gap:22px;margin-top:16px;font-size:56px;font-weight:700;letter-spacing:-.045em;color:{A.INK};font-variant-numeric:tabular-nums;white-space:nowrap}}
.im .v i{{font-style:normal;color:{A.MUTED};font-weight:600}}
.im .v small{{font-size:30px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em;margin-right:-6px}}
.im .ch{{margin-left:auto;display:inline-flex;align-items:center;height:62px;padding:0 24px;border-radius:999px;font-size:36px;font-weight:700;letter-spacing:-.02em}}
.im .d{{margin-top:12px;font-size:34px;font-weight:500;color:{A.MUTED};letter-spacing:-.015em}}
#s6s{{position:absolute;left:90px;top:1300px;width:900px;font-size:44px;font-weight:700;letter-spacing:-.03em;color:{A.INK};opacity:0}}
#s6s b{{color:{A.BRAND_DARK}}}
"""

H26, H27, BASE_Y = round(560 * 9420 / 10821.70, 1), 560, 1450
CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em Comparar, toque em <b>Mesmo período em 2026</b>.</div>
  <div class="tit" id="t2">Janeiro de 2026 entra só até o dia 28: <b>a conta fica justa</b>.</div>
  <div class="tit" id="t3"><b>+R$&nbsp;1.401,70</b> (+15%). Quase toda a alta veio de Educação.</div>
  <div class="tit" id="t4">No Analítico, cada categoria: Educação <b>+R$&nbsp;1.226,00</b>.</div>
  <div class="tit" id="t5">Material e uniforme somam <b>R$&nbsp;1.226</b>: a alta inteira de Educação.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", IMGS)}{EXTRA}</div>
  <div id="s6t">E os impostos? O IPVA subiu, mas <b>o IPTU ficou para fevereiro</b>.</div>
  <div class="im" id="im0" style="top:560px"><div class="k">IPVA</div>
    <div class="v"><small>R$</small>1.180 <i>→</i> <small>R$</small>1.236<span class="ch" style="background:#F6DCD2;color:{K.CORAL_FORTE}">+R$ 56</span></div>
    <div class="d">20/01/2026 e 20/01/2027</div></div>
  <div class="im" id="im1" style="top:860px"><div class="k">IPTU · 1ª parcela</div>
    <div class="v"><small>R$</small>210 <i>em jan/26</i><span class="ch" style="background:{A.SOFT};color:{A.BRAND_DEEP}">{MENOS}R$ 210</span></div>
    <div class="d">a de 2027 vence em 10/02/2027</div></div>
  <div id="s6s">Impostos e Taxas em janeiro: <b>{MENOS}R$ 154</b></div>
</div>

<div class="cena papel" id="g">
  <div id="gTop">
    <div class="eyebrow">Comparar</div>
    <div class="h1">Janeiro de 2027 contra <b>janeiro de 2026</b>.</div>
  </div>
  <div id="gBase"></div>
  <div class="gb" id="gb26" style="left:150px;top:{BASE_Y - H26}px;height:{H26}px;background:{A.NEUTRO}"></div>
  <div class="gb" id="gb27" style="left:630px;top:{BASE_Y - H27}px;height:{H27}px;background:{A.CORAL}"></div>
  <div class="gvl" id="gv26" style="left:90px;top:{BASE_Y - H26 - 100}px;color:{A.INK}"><small>R$</small><span id="n26">9.420</span></div>
  <div class="gvl" id="gv27" style="left:570px;top:{BASE_Y - H27 - 100}px;color:{K.CORAL_FORTE}"><small>R$</small><span id="n27">10.821,70</span></div>
  <div class="gml" style="left:150px;top:{BASE_Y + 22}px">jan/26</div>
  <div class="gml" style="left:630px;top:{BASE_Y + 22}px">jan/27</div>
  <div id="gPct"><span>+15%</span></div>
  <div id="gNota">despesas até o dia 28, na conta de exemplo</div>
</div>

{K.fim("Comparar no timtimcash")}
"""

JS = f"""
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, S6={list(S6)}, FIM={FIM}, J_SAI={J_SAI};
const TQ_MESMO={TQ_MESMO}, TQ_ANALITICO={TQ_ANALITICO}, X_TOTAIS={X_TOTAIS}, X_ESC={X_ESC};
const CHIPS={CHIPS}, CHIP_MESMO={CHIP_MESMO}, AVISO={AVISO}, DIF={DIF}, CAUSA={CAUSA}, SEG={SEG}, L_EDU={L_EDU}, L_IMP={L_IMP};
const RESUMO={RESUMO}, L_ESC={L_ESC};
const FOTOS=[[0,'c1'],[TQ_MESMO+.15,'c2'],[X_TOTAIS,'c3'],[TQ_ANALITICO+.15,'c4'],[X_ESC,'c5']];
function cx(r){{ return [r[0] + r[2]/2, r[1] + r[3]/2]; }}
function somePagina(id, t, t0){{ if (t >= t0 + .2){{ $('t_'+id).style.opacity = 0; $('o_'+id).style.opacity = 0; }} }}
// câmera: os botões do "Comparar com"; os três cartões e a causa; o topo de "Totais"; a tabela; a busca e as duas linhas
const CAM = [[0,0,195,470,1], [7.75,8.3,195,712,1], [X_TOTAIS,X_TOTAIS+.01,195,250,1], [TQ_ANALITICO+.15,TQ_ANALITICO+.6,195,450,1.1],
             [X_ESC,X_ESC+.01,195,560,1], [14.35,14.9,195,705,1]];
function render(t){{
  // 1. gancho (papel): os dois janeiros lado a lado
  const pb = pout(t, -.7, .4);
  $('gb26').style.transform = `scaleY(${{(.55 + .45*pb).toFixed(3)}})`; $('gb27').style.transform = `scaleY(${{(.55 + .45*pout(t, -.6, .5)).toFixed(3)}})`;
  $('n26').textContent = fmt(9420*(.55 + .45*pb), 0);
  const p27 = .55 + .45*pout(t, -.6, .5); $('n27').textContent = fmt(10821.70*p27, 2);
  $('gv26').style.transform = `translateY(${{(560*(9420/10821.70)*(1 - (.55 + .45*pb))).toFixed(1)}}px)`;
  $('gv27').style.transform = `translateY(${{(560*(1 - p27)).toFixed(1)}}px)`;
  const pp = pback(t, .8, 1.2); $('gPct').style.opacity = lin(t, .8, .95); $('gPct').style.transform = `scale(${{(.6 + .4*pp).toFixed(3)}})`;
  $('gNota').style.opacity = lin(t, 1.0, 1.3);
  const gs = prog(t, G_SAI, G_SAI+.3);
  $('g').style.opacity = 1 - gs; $('g').style.transform = `translateY(${{-80*gs}}px)`;

  // 2. a tela real
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, G_SAI+.15, J_SAI); nota('nota', t, G_SAI+.15, J_SAI);
  const cam = camera('tela', t, CAM);
  fotos(FOTOS, t);
  anelCam('aChips', CHIPS, cam, 8); anel('aChips', t, 3.3, TQ_MESMO+.6);
  toqueCam('tqMesmo', ...cx(CHIP_MESMO), cam); toque('tqMesmo', t, TQ_MESMO);
  anelCam('aAviso', AVISO, cam, 10); anel('aAviso', t, 5.85, T2[1]);
  anelCam('aDif', DIF, cam, 8); anel('aDif', t, 8.35, X_TOTAIS-.35);
  anelCam('aCausa', CAUSA, cam, 10); anel('aCausa', t, 8.75, X_TOTAIS-.35);
  toqueCam('tqAna', ...cx(SEG), cam); toque('tqAna', t, TQ_ANALITICO); somePagina('tqAna', t, TQ_ANALITICO);
  anelCam('aEdu', L_EDU, cam, 6); anel('aEdu', t, 11.75, X_ESC-.35);
  anelCam('aImp', L_IMP, cam, 6); anel('aImp', t, 12.15, X_ESC-.35);
  anelCam('aRes', RESUMO, cam, 8); anel('aRes', t, 13.6, 14.4);
  anelCam('aEsc', L_ESC, cam, 8); anel('aEsc', t, 14.75, T5[1]);

  // 3. os impostos: IPVA subiu, IPTU ficou para fevereiro
  some('s6t', t, S6[0], FIM+.3, 30);
  some('im0', t, S6[0]+.35, FIM+.3, 34); some('im1', t, S6[0]+.75, FIM+.3, 34);
  some('s6s', t, S6[0]+1.25, FIM+.3, 20);

  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    h26, h27, base = round(600 * 9420 / 10821.70, 1), 600, 1500
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Comparar</div>
    <div class="h1" style="font-size:132px;line-height:.96;margin-top:36px;color:#fff">Janeiro contra <span style="color:{A.MENTA}">janeiro</span>.</div>
  </div>
  <div style="position:absolute;left:150px;top:{base - h26}px;width:300px;height:{h26}px;border-radius:24px 24px 6px 6px;background:#3A443B"></div>
  <div style="position:absolute;left:630px;top:{base - h27}px;width:300px;height:{h27}px;border-radius:24px 24px 6px 6px;background:{A.CORAL}"></div>
  <div class="cl" style="left:150px;top:{base - h26 + 30}px">2026</div>
  <div class="cl" style="left:630px;top:{base - h27 + 30}px;color:{A.INK}">2027</div>
  <div style="position:absolute;left:600px;top:{base - h27 - 120}px;width:360px;text-align:center">
    <span style="display:inline-flex;align-items:center;height:96px;padding:0 38px;border-radius:999px;background:{A.CORAL};color:{A.INK};font-size:60px;font-weight:700;letter-spacing:-.03em">+15%</span></div>"""
    css = """.cl{position:absolute;width:300px;text-align:center;font-size:64px;font-weight:700;letter-spacing:-.04em;color:#fff}"""
    return K.pagina_capa(corpo, css, fundo="tinta")


if __name__ == "__main__":
    K.executar(C.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
