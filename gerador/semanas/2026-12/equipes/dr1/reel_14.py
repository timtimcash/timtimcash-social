# -*- coding: utf-8 -*-
"""Reel de 14/12/2026 · "Fixas de 2027: lance uma vez" (capa tinta, destaque coral), 1080 × 1920, 30 fps. Equipe dr1.

Telas reais do build 2026-10-16.1 (capturas/captura14.py), conta de base, celular 390 px em escala 3, relógio em
14/12/2026 10:00, tudo pela interface: Visão geral › "+" › R$ 119,90 › "Academia" (o site sugere "Cuidados pessoais",
selo "sugerida") › Data 05/01/2027 › "Marcar como pago" desligado › Recorrência "Fixa", "Mensal" ("Lançamentos
automáticos · mensal") › "Lançar despesa" ("Recorrência criada (mensal)") › Pendentes › "›" de Janeiro a Dezembro de
2027: a linha "Academia · FIXA · −R$ 119,90 · pendente" em todos os meses › Transações, Ano 2027, busca "Academia":
"12 transações · 0 pagas · 12 pendentes · somam R$ 1.438,80".

python3 reel_14.py  |  REEL_PREVIA="0 0.8 2.4 4.0 5.6 7.2 8.7 10.0 11.6 13.0 14.6 16.4 18.6" python3 reel_14.py
"""
import os, sys
from decimal import Decimal as D
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-12-14_reel-fixas-de-2027"
TRAB = C.trabalho("14")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas("14")
ARQ = CX["arquivos"]
CORAL = A.CORAL
CORAL_T = K.CORAL_TXT        # coral escuro para texto sobre o papel
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
NOMES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# ---------------------------------------------------------------- números (conferidos contra a tela)
assert CX["valorFinal"] == "119,90"
assert "05/01/2027" in CX["modalTxt"] and "Marcar como pago" in CX["modalTxt"] and "Cuidados pessoais sugerida" in CX["modalTxt"]
assert "Lançamentos automáticos · mensal" in CX["modalTxt"]
assert CX["toast"][4] == "Recorrência criada (mensal)"
for m, li in enumerate(CX["meses"]):
    assert li["periodo"] == f"{NOMES[m]} 2027", li["periodo"]
    assert li["texto"].startswith("Academia FIXA·Cuidados pessoais·Conta corrente −R$ 119,90 pendente"), li["texto"]
    assert li["linha"] == CX["meses"][0]["linha"]
assert "12 transações · 0 pagas · 12 pendentes · somam R$ 1.438,80" in CX["tx_texto"] and "Ano 2027" in CX["tx_texto"]
assert D("119.90") * 12 == D("1438.80")
assert "Dec 14 2026" in CX["relogio"]

# ---------------------------------------------------------------- tempos (s)
S2 = 3.0
TQ = {"fab": 3.55, "val": 3.95, "desc": 5.0, "data": 6.4, "prox": 6.9, "d5": 7.4, "jp": 7.9, "fixa": 8.45, "lanc": 9.5}
VAL = [4.15, 4.3, 4.45, 4.6, 4.75]
LET = [round(5.2 + .1 * i, 2) for i in range(8)]
T_E1, T_D9, T_C1, T_C2, T_C3, T_P1, T_R1, T_R2, T_T1 = 3.75, 6.1, 6.6, 7.1, 7.6, 8.1, 8.65, 9.0, 9.7
S3 = 11.3
FLIP0, PASSO = 11.75, .25
S4 = 15.75
FIM = 17.95
DUR = 20.65

ORDEM = (["e0", "e1"] + [f"v{i}" for i in range(1, 6)] + [f"d{i}" for i in range(1, 10)] +
         ["c1", "c2", "c3", "p1", "r1", "r2", "t1"])
TR = [0, T_E1] + VAL + LET + [T_D9, T_C1, T_C2, T_C3, T_P1, T_R1, T_R2, T_T1]
assert len(ORDEM) == len(TR)
IMGS = [(f"f_{k}", os.path.join(TELAS, ARQ[k])) for k in ORDEM]
fab, zv, de, dr, dp, d5, jp, fx, ln = CX["fab"], CX["zonaValor"], CX["desc"], CX["dataRow"], CX["dpProx"], CX["dia5"], CX["jp"], CX["fixa"], CX["lancar"]
cen = lambda b: (b[0] + b[2] / 2, b[1] + b[3] / 2)
PT = {"fab": cen(fab), "val": (zv[0] + zv[2] / 2, zv[1] + 62), "desc": (de[0] + 70, de[1] + de[3] / 2), "data": (dr[0] + 300, dr[1] + dr[3] / 2),
      "prox": cen(dp), "d5": cen(d5), "jp": (347, jp[1] + jp[3] / 2), "fixa": cen(fx), "lanc": cen(ln)}
CAM = [[0, 0, 195, 500, 1.0], [3.7, 3.95, 195, 300, 1.0], [4.8, 5.0, 195, 420, 1.0], [6.2, 6.45, 195, 360, 1.0],
       [8.1, 8.35, 195, 480, 1.0]]

# cena 3: a pílula do período e a linha "Academia", de janeiro a dezembro de 2027 (mesma posição nas 12 fotos)
FOTOS_M = [os.path.join(TELAS, ARQ[f"m{m}"]) for m in range(1, 13)]
LIN = CX["meses"][0]["linha"]
R_ROW = [10, LIN[1] - 8, 370, LIN[3] + 16]
R_PIL = [12, 64, 206, 56]
P_PIL = [90, 610, 520]
P_ROW = [90, 800, 900]
TROCA = [[FLIP0 + PASSO * m, m] for m in range(12)]
R_TX = [18, 326, 354, 138]
P_TX = [90, 640, 900]
RES_TX = CX["tx_resumo"][:4]

# ---------------------------------------------------------------- grade dos 12 meses
def grade(pre, x0, y0, w, h, gap, tema):
    out = []
    for i, m in enumerate(MESES):
        x = x0 + (i % 4) * (w + gap); y = y0 + (i // 4) * (h + gap)
        out.append(f'<div class="mc {tema}" id="{pre}{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
                   f'<span>{m}</span><i class="st" id="{pre}s{i}"><b>5</b></i></div>')
    return "".join(out)

CSS = f"""
.tit{{font-size:66px}}
.tit b{{color:{A.BRAND_DARK}}}
#s1 .q{{position:absolute;left:90px;top:300px;width:900px;font-size:104px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#s1 .q span{{color:{CORAL}}}
.mc{{position:absolute;border-radius:30px}}
.mc span{{position:absolute;left:26px;top:20px;font-size:34px;font-weight:700;letter-spacing:-.01em}}
.mc.esc{{background:#192019;border:2px solid #262E27}}
.mc.esc span{{color:{K.DARK_TEXTO}}}
.mc.cla{{background:#fff;border:2px solid {A.FIO}}}
.mc.cla span{{color:{A.MUTED}}}
.st{{position:absolute;left:50%;top:56%;width:92px;height:92px;margin:-46px 0 0 -46px;border-radius:50%;background:{CORAL};
  display:flex;align-items:center;justify-content:center;opacity:0}}
.st b{{font-size:46px;font-weight:700;color:#fff;letter-spacing:-.03em;font-style:normal}}
.mc.cla .st{{left:70%;top:50%;width:76px;height:76px;margin:-38px 0 0 -38px}}
.mc.cla .st b{{font-size:38px}}
#leg1{{position:absolute;left:90px;top:1440px;width:900px;font-size:42px;font-weight:600;letter-spacing:-.02em;color:{K.DARK_TEXTO};opacity:0}}
#leg1 b{{color:#fff}}
#veu{{z-index:3}}
#nota3{{position:absolute;left:96px;top:556px;font-size:26px;font-weight:500;color:{A.MUTED};opacity:0}}
#ano{{position:absolute;left:90px;top:1072px;font-size:30px;font-weight:700;letter-spacing:.16em;color:{A.BRAND_DARK};opacity:0}}
#s4 .tit{{opacity:0}}
#s4 .nota{{top:590px}}
#conta{{position:absolute;left:90px;top:1110px;width:900px;opacity:0}}
#conta small{{display:block;font-size:54px;font-weight:600;letter-spacing:-.03em;color:{A.MUTED}}}
#conta .din{{font-size:190px;font-weight:700;letter-spacing:-.055em;color:{A.INK};line-height:1;margin-top:14px}}
#conta .din .rs,#conta .din .cts{{color:{A.MUTED}}}
#conta i{{display:block;margin-top:24px;width:0;height:10px;border-radius:5px;background:{CORAL}}}
"""

CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="t2a">Nova transação: <b>R$&nbsp;119,90</b>, Academia.</div>
  <div class="tit" id="t2b">Data <b>05/01/2027</b> e Recorrência <b>Fixa</b>.</div>
  <div class="tit" id="t2c"><b>Lançar despesa</b>: recorrência criada.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">
    {C.camadas("tela", IMGS, K.toques(*PT.keys()))}
  </div>

  <div class="tit" id="t3">Lance uma vez. <b>Ela aparece em cada mês.</b></div>
  <div id="nota3">{K.NOTA}</div>
  {C.pop_html("popP", FOTOS_M)}
  {C.pop_html("popR", FOTOS_M, C.anel_no_recorte("aR", R_ROW, P_ROW, LIN, 4))}
  <div id="ano">2027</div>
  {grade("g", 90, 1120, 210, 128, 20, "cla")}
</div>

<div class="cena papel" id="s4" style="transform:translateY(1920px)">
  <div class="tit" id="t4">No ano: 12 lançamentos, <b>R$&nbsp;1.438,80</b>.</div>
  <div class="nota" id="nota4">{K.NOTA}</div>
  {C.pop_html("popX", os.path.join(TELAS, ARQ["x1"]), C.anel_no_recorte("aX", R_TX, P_TX, RES_TX, 12))}
  <div id="conta"><small>12 × R$ 119,90 =</small>{C.din("1.438,80")}<i id="contaL"></i></div>
</div>

<div class="cena tinta" id="s1">
  <div class="q" id="q">Fixas de 2027:<br>lance <span>uma vez</span>.</div>
  {grade("h", 90, 640, 210, 230, 20, "esc")}
  <div id="leg1">Academia · <b>R$ 119,90</b> todo dia 5, o ano inteiro</div>
</div>

{K.fim("Recorrência Fixa no timtimcash")}
"""

JS = f"""
const S2={S2}, S3={S3}, S4={S4}, FIM={FIM}, FLIP0={FLIP0}, PASSO={PASSO};
const TR={TR}, IDS={[i for i, _ in IMGS]}, CAM={CAM}, TROCA={TROCA};
const R_PIL={R_PIL}, P_PIL={P_PIL}, R_ROW={R_ROW}, P_ROW={P_ROW}, R_TX={R_TX}, P_TX={P_TX};
{"".join(f"poeToque('{k}', {x:.1f}, {y:.1f});" for k, (x, y) in PT.items())}
const TQ={{{", ".join(f"{k}: {v}" for k, v in TQ.items())}}};
function carimbo(id, t, a){{ const e = $(id); const p = clamp((t-a)/.28, 0, 1);
  e.style.opacity = lin(t, a, a+.06); e.style.transform = `scale(${{(1.7 - .7*easeOut(p)) * (1 + .08*Math.sin(Math.PI*clamp((t-a-.28)/.2,0,1)))}})`; }}
function render(t){{
  // 1. gancho na tinta: o mesmo carimbo cai em cada mês de 2027
  $('s1').style.transform = `translateY(${{-1920*prog(t, S2-.05, S2+.4)}}px)`;
  $('q').style.transform = `translateY(${{-10*pout(t,0,1.2)}}px)`;
  for (let i=0;i<12;i++) carimbo('hs'+i, t, .02 + .11*i);
  aparece('leg1', t, 1.45, 0, 24, .4);
  // 2. a tela real: Nova transação, valor, descrição, data, pago, Fixa e Lançar despesa
  titulo('t2a', t, S2+.1, 5.85); titulo('t2b', t, 6.2, 8.85); titulo('t2c', t, 9.15, S3-.35);
  janela('janela', t, S2, S3-.1); janela('nota', t, S2, S3-.1);
  fotos(IDS, t, TR);
  camera('tela', t, CAM);
  Object.keys(TQ).forEach(k => toque(k, t, TQ[k]));
  // 3. a mesma linha em todos os meses de 2027
  titulo('t3', t, S3, S4-.1);
  aparece('nota3', t, S3+.2, S4-.1, 10, .3);
  recorte('popP', t, S3+.2, S4-.1, R_PIL, [P_PIL[0], P_PIL[1]+90, P_PIL[2], 1], P_PIL, .5, false, TROCA);
  recorte('popR', t, S3+.3, S4-.1, R_ROW, [P_ROW[0], P_ROW[1]+90, P_ROW[2], 1], P_ROW, .5, false, TROCA);
  anel('aR', t, S3+.75, S4-.1);
  aparece('ano', t, S3+.35, S4-.1, 16, .3);
  for (let i=0;i<12;i++){{ const a = FLIP0 + PASSO*i; aparece('g'+i, t, S3+.35+.03*i, S4-.1, 20, .3); carimbo('gs'+i, t, a+.05); }}
  // 4. no ano: a soma das 12 em Transações (Ano 2027, busca "Academia")
  sobe('s4', t, S4);
  titulo('t4', t, S4+.35, 0); aparece('nota4', t, S4+.4, 0, 10, .3);
  recorte('popX', t, S4+.45, 0, R_TX, [P_TX[0], P_TX[1]+90, P_TX[2], 1], P_TX, .5, false);
  anel('aX', t, S4+.95, 0);
  aparece('conta', t, S4+.8, 0, 30, .45); $('contaL').style.width = (520*pout(t, S4+1.1, S4+1.7))+'px';
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (tinta, coral): 2027 com a mesma marca em todos os meses
CAPA_CSS = f"""
#capa .eyebrow{{color:{CORAL}}}
.ct{{position:absolute;left:90px;top:430px;width:900px}}
.ct .h1{{font-size:120px;line-height:.97;color:#fff;text-wrap:balance}}
.ct .h1 span{{color:{CORAL}}}
.cy{{position:absolute;left:90px;top:870px;font-size:34px;font-weight:700;letter-spacing:.16em;color:{K.DARK_TEXTO}}}
.cg .mc{{position:absolute;border-radius:24px;background:#192019;border:2px solid #262E27}}
.cg .mc span{{position:absolute;left:20px;top:14px;font-size:28px;font-weight:700;color:{K.DARK_TEXTO}}}
.cg .st{{position:absolute;left:50%;top:58%;width:74px;height:74px;margin:-37px 0 0 -37px;border-radius:50%;background:{CORAL};
  display:flex;align-items:center;justify-content:center}}
.cg .st b{{font-size:36px;font-weight:700;color:#fff;letter-spacing:-.03em;font-style:normal}}
"""
def capa_grade():
    out = []
    w, h, gap, x0, y0 = 210, 150, 20, 90, 930
    for i, m in enumerate(MESES):
        x = x0 + (i % 4) * (w + gap); y = y0 + (i // 4) * (h + gap)
        out.append(f'<div class="mc" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><span>{m}</span><i class="st"><b>5</b></i></div>')
    return '<div class="cg">' + "".join(out) + "</div>"

CAPA_CORPO = f"""
{K.logo("tinta")}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Recorrência Fixa</div>
  <div class="h1">Fixas de 2027: lance <span>uma vez</span></div></div>
<div class="cy">2027</div>
{capa_grade()}
"""

HTML = C.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="tinta")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
