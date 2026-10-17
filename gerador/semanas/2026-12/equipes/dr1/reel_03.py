# -*- coding: utf-8 -*-
"""Reel de 03/12/2026 · "Presentes: o teto antes da loja" (capa tinta, destaque âmbar), 1080 × 1920, 30 fps. Equipe dr1.

Telas reais do build 2026-10-16.1 (capturas/captura03.py), conta de base, celular 390 px em escala 3, tudo pela interface:
- relógio em 03/12/2026: Orçamentos › "Definir limites" › busca "Presentes" › campo de "Presentes e doações" › 8-0-0-0-0
  (R$ 800,00) › "Salvar" ("Orçamentos salvos") › a linha nova: "Presentes e doações R$ 0 de R$ 800 0%" (Tranquilas);
- relógio em 17/12/2026 (o mesmo limite, definido de novo pela interface): "VÃO ESTOURAR NO RITMO ATUAL ·
  Presentes e doações R$ 774 de R$ 800 97% · no ritmo, fecha em R$ 1.412 77% ACIMA";
- relógio em 21/12/2026: "JÁ PASSARAM DO LIMITE · Presentes e doações R$ 972 de R$ 800 122% · Excedeu em R$ 172 ·
  e, no ritmo, fecha em R$ 1.435 79% ACIMA".
Gancho: Transações em Dezembro 2025 com a busca "Presentes": "1 transação · somam R$ 980,00".
Presentes de dezembro na conta: 08/12 R$ 120 (amigo secreto), 12/12 R$ 389,90, 17/12 R$ 264,50 e 21/12 R$ 198 (Natal).

python3 reel_03.py  |  REEL_PREVIA="0 1 2.6 4.6 5.9 7.3 8.9 9.5 11.0 12.4 14.2 15.6 17.6 19.6" python3 reel_03.py
"""
import os, sys
from decimal import Decimal as D
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-12-03_reel-presentes-o-teto-antes-da-loja"
TRAB = C.trabalho("03")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas("03")
ARQ = CX["arquivos"]
AMBAR = A.AMBER               # âmbar da marca (limite), sobre a tinta
AMBAR_P = A.AMBER_BAR         # âmbar escuro, para traço sobre o papel (3:1)
AMBAR_TXT = A.AMBER

# ---------------------------------------------------------------- números (conferidos contra a tela)
LIM = D("800")
PRESENTES = [("08/12", "amigo secreto", D("120.00")), ("12/12", "Natal", D("389.90")),
             ("17/12", "Natal", D("264.50")), ("21/12", "Natal", D("198.00"))]
ATE17 = sum(v for _, _, v in PRESENTES[:3]); ATE21 = sum(v for _, _, v in PRESENTES)
assert ATE17 == D("774.40") and ATE21 == D("972.40") and ATE21 - LIM == D("172.40")
assert CX["avalor_5"] == "R$ 800,00"
assert "6 categorias | R$ 6.250,00" in CX["amodalTxt"]
assert CX["alinha"]["texto"] == "Presentes e doações R$ 0 de R$ 800 0%", CX["alinha"]["texto"]
assert CX["blinha"]["texto"].startswith("Presentes e doações R$ 774 de R$ 800 97% no ritmo, fecha em R$ 1.412"), CX["blinha"]["texto"]
assert CX["blinha"]["faixaTxt"].startswith("VÃO ESTOURAR NO RITMO ATUAL")
assert CX["clinha"]["texto"].startswith("Presentes e doações R$ 972 de R$ 800 122% Excedeu em R$ 172"), CX["clinha"]["texto"]
assert CX["clinha"]["faixaTxt"].startswith("JÁ PASSARAM DO LIMITE")
assert "somam R$ 980,00" in CX["d_texto"] and "Dezembro 2025" in CX["d_texto"]
assert "Dec 03 2026" in CX["a_relogio"] and "Dec 17 2026" in CX["b_relogio"] and "Dec 21 2026" in CX["c_relogio"]

# ---------------------------------------------------------------- tempos (s)
SOBE1 = 3.25          # o gancho (tinta) sobe e revela o papel
TQ1, TQ2, TQ3, TQ4 = 4.05, 4.75, 6.0, 7.55     # toques: Definir limites, busca, campo, Salvar
LETRAS = [round(4.95 + .09 * i, 2) for i in range(9)]
DIGITOS = [round(6.45 + .16 * i, 2) for i in range(5)]
T_A1, T_A3, T_A5, T_A6 = 4.25, 6.2, 7.75, 8.05
POPA = 8.3
S3 = 9.65             # os presentes chegam
B_T = [10.0, 10.35, 10.7, 13.05]
POPB, POPC = 11.15, 13.35
T3B = 12.8
S4 = 15.95            # a lição (tinta)
FIM = 18.55
DUR = 21.3

# ---------------------------------------------------------------- tela real (camadas)
ORDEM = ["a0", "a1"] + [f"a2_{i}" for i in range(1, 10)] + ["a3"] + [f"a4_{i}" for i in range(1, 6)] + ["a5", "a6"]
TR = [3.0, T_A1] + LETRAS + [T_A3] + DIGITOS + [T_A5, T_A6]
assert len(ORDEM) == len(TR)
IMGS = [(f"f_{k}", os.path.join(TELAS, ARQ[k])) for k in ORDEM]
b0 = CX["abotao"]; bu = CX["abusca"]; ca = CX["acampo"]; sv = CX["asalvar"]
TOQ = {"tq1": (b0[0] + b0[2] / 2, b0[1] + b0[3] / 2), "tq2": (bu[0] + 70, bu[1] + bu[3] / 2),
       "tq3": (ca[0] + ca[2] / 2, ca[1] + ca[3] / 2), "tq4": (sv[0] + sv[2] / 2, sv[1] + sv[3] / 2)}
# câmera: (início, fim, x, y, zoom) com (x, y) em px CSS no centro da janela
CAM = [[0, 0, 195, 300, 1.0], [4.1, 4.4, 195, 290, 1.0], [4.85, 5.25, 195, 420, 1.0], [7.1, 7.42, 195, 505, 1.0],
       [7.95, 8.3, 195, 420, 1.0]]
RL = CX["arolado"]                                   # a linha nova, na foto rolada (px CSS da janela do celular)
R_A = [18, RL[1] - 10, 354, RL[3] + 20]
DE_A = C.de_camera(R_A, 195, 420, 1.0)
PARA_A = [90, 760, 900]

# recortes de 17/12 e 21/12 (fotos altas): a faixa e a linha
bl, cl = CX["blinha"], CX["clinha"]
R_B = [18, bl["faixa"][1] - 10, 354, bl["item"][1] + bl["item"][3] - bl["faixa"][1] + 18]
R_C = [18, cl["faixa"][1] - 10, 354, cl["item"][1] + cl["item"][3] - cl["faixa"][1] + 18]
P_REC = [90, 1105, 900]
DE_B = [90, 1165, 900, 1]
PCT_B = bl["pct"]
EXC_C = [29.5, 1312.5, 99, 15]                      # "Excedeu em R$ 172" (medido pelos pixels da foto)
assert R_C[1] < EXC_C[1] < R_C[1] + R_C[3]

# ---------------------------------------------------------------- o copo dos presentes (cena 3)
G_X, G_W, G_Y0, G_H = 120, 230, 1000, 500          # base do copo em y = 1000, escala de R$ 1.000 em 500 px
def gy(v):
    return G_Y0 - float(v) / 1000 * G_H
TETO_Y = gy(LIM)
blocos, chips = [], []
acum = D("0")
for i, (dia, nome, v) in enumerate(PRESENTES):
    topo, base = gy(acum + v), gy(acum)
    acum += v
    blocos.append((topo, base))
    centro = (topo + base) / 2
    chips.append(min(centro, TETO_Y - 60) if i == 3 else centro)   # o último fica acima da linha do teto

def bloco_html(i, topo, base):
    h = base - topo
    over = ""
    if i == 3:   # a parte acima do teto fica vermelha
        h_over = TETO_Y - topo
        over = f'<i class="over" id="ov" style="height:{h_over:.1f}px"></i>'
    return f'<div class="blk" id="bk{i}" style="top:{topo:.1f}px;height:{h:.1f}px">{over}</div>'

def chip_html(i, centro):
    dia, nome, v = PRESENTES[i]
    return (f'<div class="chp" id="ch{i}" style="top:{centro - 52:.1f}px">{presente_svg(44, A.BRAND_DARK)}'
            f'<div><b>{C.din(C.brl(float(v)))}</b><small>{dia} · {nome}</small></div></div>')

def presente_svg(tam, cor, traco=2.2):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" '
            f'stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="9" width="17" height="11.5" rx="2"/>'
            f'<path d="M2.5 9h19M12 9v11.5"/><path d="M12 9c-2.5 0-5-1-5-3.2C7 4 9.5 3.6 12 9zM12 9c2.5 0 5-1 5-3.2C17 4 14.5 3.6 12 9z"/></svg>')

# ---------------------------------------------------------------- CSS
CSS = f"""
.tit{{font-size:66px}}
/* 1. gancho na tinta: a etiqueta de presente que balança */
#q1{{position:absolute;left:90px;top:300px;width:900px;font-size:84px;line-height:1.02;font-weight:700;letter-spacing:-.05em;color:#fff}}
#bal{{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:540px 470px}}
#fio{{position:absolute;left:538px;top:470px;width:4px;height:128px;background:{AMBAR}}}
#prego{{position:absolute;left:526px;top:456px;width:28px;height:28px;border-radius:50%;background:{AMBAR}}}
#etq{{position:absolute;left:160px;top:590px;width:760px;height:480px;border-radius:60px;border:7px solid {AMBAR};background:#192019;
  display:flex;flex-direction:column;align-items:center;justify-content:center;padding-top:40px}}
#furo{{position:absolute;left:350px;top:24px;width:46px;height:46px;border-radius:50%;border:7px solid {AMBAR};background:{A.INK}}}
#etq .din{{font-size:280px;font-weight:700;letter-spacing:-.055em;color:#fff;line-height:1}}
#etq .din .rs{{color:{K.DARK_TEXTO}}}
#etq small{{display:block;margin-top:18px;font-size:46px;font-weight:600;letter-spacing:-.02em;color:{K.DARK_TEXTO}}}
#q2{{position:absolute;left:90px;top:1200px;width:900px;font-size:150px;line-height:1;font-weight:700;letter-spacing:-.055em;color:{A.MENTA};opacity:0}}
/* 2. a tela real */
#veu{{z-index:3}}
/* 3. o copo dos presentes */
#copo{{position:absolute;left:{G_X - 10}px;top:{G_Y0 - G_H - 14}px;width:{G_W + 20}px;height:{G_H + 24}px;border:7px solid {A.FIO};border-top:0;
  border-radius:0 0 46px 46px;opacity:0}}
.blk{{position:absolute;left:{G_X + 6}px;width:{G_W - 12}px;background:{A.BRAND};border-radius:14px;border:4px solid {A.BG};opacity:0}}
.blk .over{{position:absolute;left:-4px;top:-4px;width:calc(100% + 8px);background:{A.RED};border-radius:14px 14px 0 0;opacity:0}}
#teto{{position:absolute;left:{G_X - 40}px;top:{TETO_Y - 3:.1f}px;width:{990 - G_X + 40}px;height:0;border-top:6px dashed {AMBAR_P};opacity:0}}
#tetoR{{position:absolute;left:760px;top:{TETO_Y - 92:.1f}px;width:230px;text-align:right;font-size:30px;font-weight:700;letter-spacing:.12em;
  text-transform:uppercase;color:#8A6416;opacity:0}}
#tetoR b{{display:block;font-size:46px;letter-spacing:-.03em;text-transform:none;color:{A.INK}}}
.chp{{position:absolute;left:400px;height:104px;display:flex;align-items:center;gap:22px;opacity:0}}
.chp svg{{flex:none;width:76px;height:76px;padding:14px;border-radius:22px;background:{A.SOFT}}}
.chp b{{display:block;font-size:52px;font-weight:700;letter-spacing:-.04em;color:{A.INK};line-height:1.02}}
.chp b .rs,.chp b .cts{{color:{A.MUTED}}}
.chp small{{display:block;font-size:30px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em;margin-top:4px}}
#ch3 b{{color:{A.RED}}}
#nota3{{position:absolute;left:96px;top:1062px;font-size:26px;font-weight:500;color:{A.MUTED};opacity:0}}
/* 4. a lição */
#s4 .l{{position:absolute;left:90px;width:900px;font-weight:700;letter-spacing:-.05em;line-height:1.02;color:#fff}}
#s4 .l .w{{display:inline-block;opacity:0}}
#s4 .l b{{color:{A.MENTA};font-weight:700}}
#l1{{top:600px;font-size:108px}}
#l2{{top:860px;font-size:108px}}
#s4 .tetoM{{position:absolute;left:90px;top:1160px;width:900px;height:0;border-top:6px dashed {AMBAR};opacity:0}}
"""

# ---------------------------------------------------------------- corpo
CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="t2a">Em Orçamentos: <b>Definir limites</b> e a busca “Presentes”.</div>
  <div class="tit" id="t2b">Teto de <b>R$&nbsp;800</b>, antes da primeira compra.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">
    {C.camadas("tela", IMGS, K.toques(*TOQ.keys()))}
    <div class="veu" id="veu"></div>
  </div>
  {C.pop_html("popA", os.path.join(TELAS, ARQ["a6"]), C.anel_no_recorte("aA", R_A, PARA_A, [RL[0], RL[1], RL[2], RL[3]], 6))}

  <div class="tit" id="t3a">Dia 17: <b>R$&nbsp;774 de R$&nbsp;800</b>. No ritmo, vai passar.</div>
  <div class="tit" id="t3b">Dia 21: mais R$&nbsp;198. <b>Passou R$&nbsp;172.</b></div>
  <div id="copo"></div>
  {"".join(bloco_html(i, t_, b_) for i, (t_, b_) in enumerate(blocos))}
  <div id="teto"></div>
  <div id="tetoR">teto<b>R$ 800</b></div>
  {"".join(chip_html(i, c_) for i, c_ in enumerate(chips))}
  <div id="nota3">{K.NOTA}</div>
  {C.pop_html("popB", os.path.join(TELAS, ARQ["balta"]), C.anel_no_recorte("aB", R_B, P_REC, PCT_B, 10, "coral"))}
  {C.pop_html("popC", os.path.join(TELAS, ARQ["calta"]), C.anel_no_recorte("aC", R_C, P_REC, EXC_C, 10, "coral"))}
</div>

<div class="cena tinta" id="s4">
  {C.palavras_html("l1", "O teto não proíbe a compra.", (), "l")}
  {C.palavras_html("l2", "Mostra quanto ainda cabe.", (1, 2, 3), "l")}
  <div class="tetoM" id="tetoM"></div>
</div>

<div class="cena tinta" id="s1">
  <div id="q1">Dezembro passado:</div>
  <div id="bal">
    <div id="fio"></div><div id="prego"></div>
    <div id="etq"><div id="furo"></div>{C.din("980")}<small>em presentes</small></div>
  </div>
  <div id="q2">E este ano?</div>
</div>

{K.fim("Orçamentos no timtimcash")}
"""

JS = f"""
const SOBE1={SOBE1}, S3={S3}, S4={S4}, FIM={FIM}, POPA={POPA}, POPB={POPB}, POPC={POPC};
const TR={TR}, IDS={[i for i, _ in IMGS]}, CAM={CAM}, B_T={B_T};
const R_A={R_A}, DE_A={[round(v, 1) for v in DE_A]}, PARA_A={PARA_A};
const R_B={R_B}, R_C={R_C}, P_REC={P_REC}, DE_B={DE_B};
{"".join(f"poeToque('{k}', {x:.1f}, {y:.1f});" for k, (x, y) in TOQ.items())}
function render(t){{
  // 1. gancho: a etiqueta de presente balança desde o primeiro quadro; "E este ano?" entra em 1,35 s
  $('s1').style.transform = `translateY(${{-1920*prog(t, SOBE1, SOBE1+.45)}}px)`;
  const th = 8.5*Math.exp(-1.05*t)*Math.cos(2*Math.PI*t/1.25) + 2.2*Math.exp(-1.6*Math.max(0,t-1.35))*Math.sin(2*Math.PI*Math.max(0,t-1.35)/1.1)*(t>1.35?1:0);
  $('bal').style.transform = `rotate(${{th.toFixed(3)}}deg)`;
  $('q1').style.transform = `translateY(${{-10*pout(t,0,1.2)}}px)`;
  aparece('q2', t, 1.35, 0, 40, .45);
  // 2. a tela real: Definir limites, a busca, o valor e Salvar
  titulo('t2a', t, SOBE1+.1, 6.0); titulo('t2b', t, 6.35, S3-.35);
  janela('janela', t, SOBE1, S3-.1); janela('nota', t, SOBE1, S3-.1);
  fotos(IDS, t, TR);
  camera('tela', t, CAM);
  toque('tq1', t, {TQ1}); toque('tq2', t, {TQ2}); toque('tq3', t, {TQ3}); toque('tq4', t, {TQ4});
  $('veu').style.opacity = .62*prog(t, POPA, POPA+.45);
  recorte('popA', t, POPA, S3-.1, R_A, DE_A, PARA_A, .6, false);
  anel('aA', t, POPA+.55, S3-.1);
  // 3. os presentes chegam: cada um cai no copo; o teto de R$ 800 é a linha tracejada
  titulo('t3a', t, S3, {T3B}-.35); titulo('t3b', t, {T3B}, S4-.1);
  const saiu3 = prog(t, S4-.15, S4+.2);
  aparece('copo', t, S3+.1, 0, 30); $('copo').style.borderColor = t < B_T[2]+.35 ? '{A.FIO}' : (t < B_T[3]+.3 ? '{AMBAR_P}' : '{A.RED}');
  B_T.forEach((a, i) => {{ const e = $('bk'+i), p = pback(t, a, a+.42);
    e.style.opacity = lin(t, a, a+.08); e.style.transform = `translateY(${{-(1-p)*420}}px)`;
    aparece('ch'+i, t, a+.12, 0, 24, .35); }});
  $('ov').style.opacity = prog(t, B_T[3]+.3, B_T[3]+.55);
  aparece('teto', t, S3+.25, 0, 0, .4); aparece('tetoR', t, S3+.3, 0, 16, .4);
  aparece('nota3', t, POPB-.1, 0, 10, .3);
  recorte('popB', t, POPB, POPC-.25, R_B, DE_B, P_REC, .55, false);
  anel('aB', t, POPB+.5, POPC-.25);
  recorte('popC', t, POPC-.15, 0, R_C, DE_B, P_REC, .5, false);
  anel('aC', t, POPC+.45, 0);
  // 4. a lição, na tinta
  sobe('s4', t, S4);
  palavras('l1', t, S4+.2, 0); palavras('l2', t, S4+.5, 0);
  $('tetoM').style.opacity = prog(t, S4+.9, S4+1.2); $('tetoM').style.width = (900*pout(t, S4+.9, S4+1.5))+'px';
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (tinta, âmbar): o laço e o teto de R$ 800
def laco_svg():
    tr = f'fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"'
    return f"""<svg viewBox="0 0 600 520" width="690" height="598" style="position:absolute;left:195px;top:1000px;overflow:visible">
  <rect x="70" y="210" width="460" height="290" rx="28" {tr}/>
  <rect x="40" y="140" width="520" height="80" rx="22" {tr}/>
  <path d="M300 140 V500" {tr}/>
  <path d="M300 140 C250 140 170 120 170 70 C170 20 240 10 300 140 Z" {tr}/>
  <path d="M300 140 C350 140 430 120 430 70 C430 20 360 10 300 140 Z" {tr}/>
</svg>"""

CAPA_CSS = f"""
#capa .eyebrow{{color:{AMBAR_TXT}}}
.ct{{position:absolute;left:90px;top:430px;width:900px}}
.ct .h1{{font-size:118px;line-height:.98;color:#fff;text-wrap:balance}}
.ct .h1 span{{color:{AMBAR_TXT}}}
.tt{{position:absolute;left:90px;top:930px;width:860px;height:0;border-top:8px dashed {AMBAR}}}
.tp{{position:absolute;left:600px;top:880px;height:100px;padding:0 40px;border-radius:999px;background:{AMBAR};color:{A.INK};
  display:flex;align-items:center;font-size:58px;font-weight:700;letter-spacing:-.035em;font-variant-numeric:tabular-nums}}
.tp small{{font-size:30px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-right:16px}}
"""
CAPA_CORPO = f"""
{K.logo("tinta")}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Orçamentos</div>
  <div class="h1">Presentes: o <span>teto</span> antes da loja</div></div>
<div class="tt"></div>
<div class="tp"><small>teto</small>R$ 800</div>
{laco_svg()}
"""

HTML = C.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="tinta")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
