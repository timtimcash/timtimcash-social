# -*- coding: utf-8 -*-
"""Reel de 23/01/2027 (sábado) · "Da receita ao resultado: o seu 2026 numa cascata" · capa tinta · equipe js.

Telas reais: captura_23.py, build 2026-10-19.5, celular 390 × 760 em escala 3, conta fictícia de J/base_app (sem mudança), relógio
da página em 23/01/2027 10:00. Relatórios -> período "Ano 2027" (calendário, "Ano atual", "Aplicar") -> seta "‹" -> "Ano 2026"
-> atalho "Cascata" -> "Cascata do período · Da receita ao resultado · Ano 2026" -> um toque em cada degrau; o balão do gráfico:
Receita +R$ 126.293,36 · Casa −R$ 30.054,00 · Mercado −R$ 19.113,60 · Educação −R$ 17.400,00 · Transporte −R$ 13.281,49 ·
Bares e restaurantes −R$ 7.408,62 · Outras (8) −R$ 14.596,99 · Resultado R$ 24.438,66 (conferidos também nos dados do gráfico).
O Diagnóstico de 2026, na mesma tela, diz "Receita guardada 19,4%" (24.438,66 ÷ 126.293,36 = 19,35%).
Casa + Mercado + Educação = R$ 66.567,60 = 52,7% da receita ("mais da metade"); as outras 10 categorias (Transporte, Bares e
restaurantes e as 8 de "Outras (8)") somam R$ 35.287,10; despesas do ano R$ 101.854,70 em 13 categorias ("Despesas por categoria").
Diferença para 06/12 (5 números do ano): aqui é o desenho da cascata, degrau a degrau, com o ano de 2026 fechado.

python3 reel_23.py  |  REEL_PREVIA="0 0.5 1 1.8 3.6 4.5 6.4 9.3 12.3 15.6 18.2" python3 reel_23.py
"""
import os, sys, json
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A
MENOS = C.MENOS

PASTA = "2027-01-23_reel-cascata-do-seu-2026"
SAIDA = C.saida(PASTA)
TELAS = C.telas(PASTA)
TRAB = C.trabalho("23")
CX = C.caixas(PASTA)
F4, F5, F6 = (CX[f"celular-relatorios-{n}.jpg"] for n in ["4-ano-2027", "5-ano-2026", "6-cascata"])
NOMES = ["receita", "casa", "mercado", "educacao", "transporte", "bares", "outras", "resultado"]
FT = [CX[f"celular-relatorios-7-{i}-{n}.jpg"] for i, n in enumerate(NOMES)]

# ---------------------------------------------------------------- conferência com a tela
G = F6["grafico"]
DEGRAUS = [("Receita", "+R$ 126.293,36"), ("Casa", "−R$ 30.054,00"), ("Mercado", "−R$ 19.113,60"), ("Educação", "−R$ 17.400,00"),
           ("Transporte", "−R$ 13.281,49"), ("Bares e restaurantes", "−R$ 7.408,62"), ("Outras (8)", "−R$ 14.596,99"), ("Resultado", "R$ 24.438,66")]
for f, (nome, val) in zip(FT, DEGRAUS):
    assert f["balao"]["titulo"] == [nome] and f["balao"]["corpo"] == [val], (f["balao"], nome, val)
VAL = [D("126293.36"), D("30054.00"), D("19113.60"), D("17400.00"), D("13281.49"), D("7408.62"), D("14596.99"), D("24438.66")]
assert VAL[0] - sum(VAL[1:7]) == VAL[7] and sum(VAL[1:7]) == D("101854.70")
for i, (a, b) in enumerate(G["dados"]):
    assert abs(D(str(b)) - D(str(a)) - VAL[i]) < D("0.01"), (i, a, b)
assert "Da receita ao resultado · Ano 2026" in F6["texto"] and "Ano 2026" in F5["texto"] and "Ano 2027" in F4["texto"]
assert "Receita guardada" in F5["texto"] and "19,4%" in F5["texto"] and "Despesas do período" in F5["texto"]
assert "Jan 23 2027" in CX["relogio"]
TRES = VAL[1] + VAL[2] + VAL[3]
OUTRAS10 = VAL[4] + VAL[5] + VAL[6]
assert TRES == D("66567.60") and OUTRAS10 == D("35287.10") and TRES / VAL[0] > D("0.5")
assert round(VAL[7] / VAL[0] * 100, 1) == D("19.4")

# ---------------------------------------------------------------- caixas (px CSS da foto)
PER4 = F4["periodo"][:4]; PER5 = F5["periodo"][:4]
SETA = F4["seta_ant"][:4]
CHIP = F5["chip_cascata"][:4]
CHIP_RING = [CHIP[0] - 14, CHIP[1] - 10, CHIP[2] + 28, CHIP[3] + 20]       # a pílula inteira (o texto tem 13 px de altura)
ROL = F6["rolagem"]
TAPS = [[b["x"], round((b["y0"] + b["y1"]) / 2 - ROL, 1)] for b in G["barras"]]

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.6
T1, T2, T3, T4 = (2.9, 5.55), (5.75, 8.55), (8.75, 11.45), (11.65, 14.0)
TQ_SETA, TQ_CHIP = 3.95, 4.95
TQ_BAR = [5.95, 7.0, 7.8, 8.95, 9.75, 10.35, 10.9, 11.85]
J_SAI = 14.0
S5 = (14.2, 17.2)
FIM = 17.25
DUR = 20.0

IMGS = ([("f4", os.path.join(TELAS, "celular-relatorios-4-ano-2027.jpg")), ("f5", os.path.join(TELAS, "celular-relatorios-5-ano-2026.jpg")),
         ("f6", os.path.join(TELAS, "celular-relatorios-6-cascata.jpg"))] +
        [(f"b{i}", os.path.join(TELAS, f"celular-relatorios-7-{i}-{n}.jpg")) for i, n in enumerate(NOMES)])
EXTRA = K.aneis("aPer4", "aPer5", "aChip") + K.toques("tqSeta", "tqChip", *[f"tqB{i}" for i in range(8)])

# ---------------------------------------------------------------- gancho: a cascata desenhada
CX0, CPASSO, CLARG, CBASE, CALT = 100, 115, 80, 1450, 680
def cy(v): return CBASE - CALT * float(v / VAL[0])
NIVEIS = [VAL[0]]
for v in VAL[1:7]:
    NIVEIS.append(NIVEIS[-1] - v)
assert NIVEIS[-1] == VAL[7]

def cascata_html(pre, escala=1.0, x0=CX0, passo=CPASSO, larg=CLARG, base=CBASE, alt=CALT, cor_res=None):
    cor_res = cor_res or A.MENTA
    def yy(v): return base - alt * float(v / VAL[0])
    out = [f'<div class="cb" id="{pre}0" style="left:{x0}px;top:{yy(VAL[0]):.1f}px;width:{larg}px;height:{alt:.1f}px;background:{A.BRAND}"></div>']
    for i in range(1, 7):
        top, bot = yy(NIVEIS[i - 1]), yy(NIVEIS[i])
        out.append(f'<div class="cb" id="{pre}{i}" style="left:{x0 + passo * i}px;top:{top:.1f}px;width:{larg}px;height:{bot - top:.1f}px;background:{A.CORAL}"></div>')
        out.append(f'<div class="cl" id="{pre}l{i}" style="left:{x0 + passo * i - passo + larg}px;top:{top:.1f}px;width:{passo - larg}px"></div>')
    out.append(f'<div class="cb" id="{pre}7" style="left:{x0 + passo * 7}px;top:{yy(VAL[7]):.1f}px;width:{larg}px;height:{base - yy(VAL[7]):.1f}px;background:{cor_res};transform-origin:50% 100%"></div>')
    out.append(f'<div class="cl" id="{pre}l7" style="left:{x0 + passo * 6 + larg}px;top:{yy(VAL[7]):.1f}px;width:{passo - larg}px"></div>')
    return "".join(out)

CSS = f"""
#g{{background:{A.INK}}}
#gTop{{position:absolute;left:90px;top:300px;width:900px}}
#gTop .h1{{font-size:92px;line-height:1;margin-top:30px;color:#fff;text-wrap:balance}}
#gTop .h1 b{{color:{A.MENTA};font-weight:700}}
.cb{{position:absolute;border-radius:10px}}
.cl{{position:absolute;height:0;border-top:4px dashed #4A564C}}
.gv{{position:absolute;white-space:nowrap;font-size:52px;font-weight:700;letter-spacing:-.045em;font-variant-numeric:tabular-nums}}
.gr{{position:absolute;top:1470px;font-size:30px;font-weight:600;color:{K.DARK_TEXTO};white-space:nowrap}}
#base0{{position:absolute;left:90px;top:{CBASE + 2}px;width:900px;border-top:4px solid #2F3A31}}
/* cena 5: a receita dividida */
#s5t{{position:absolute;left:90px;top:280px;width:900px;font-size:66px;line-height:1.06;font-weight:700;letter-spacing:-.045em;opacity:0}}
#s5t b{{color:{K.CORAL_FORTE}}}
#pilha{{position:absolute;left:90px;top:690px;width:900px;height:120px;display:flex;gap:6px}}
#pilha i{{display:block;height:120px;border-radius:12px;width:0}}
#chave{{position:absolute;left:90px;top:610px;height:56px;border:4px solid {K.CORAL_FORTE};border-bottom:0;border-radius:14px 14px 0 0;opacity:0}}
#chave span{{position:absolute;left:0;right:0;top:-48px;text-align:center;font-size:34px;font-weight:700;color:{K.CORAL_FORTE};letter-spacing:-.02em;white-space:nowrap}}
.lg{{position:absolute;left:90px;width:900px;display:flex;align-items:center;gap:22px;height:84px;border-bottom:3px solid {A.FIO};opacity:0}}
.lg u{{flex:none;width:34px;height:34px;border-radius:9px}}
.lg span{{font-size:40px;font-weight:600;letter-spacing:-.02em;color:{A.INK}}}
.lg b{{margin-left:auto;font-size:44px;font-weight:700;letter-spacing:-.03em;color:{A.INK};font-variant-numeric:tabular-nums}}
#s5n{{position:absolute;left:90px;top:1400px;width:900px;font-size:40px;line-height:1.25;font-weight:600;letter-spacing:-.02em;color:{A.INK};opacity:0;text-wrap:balance}}
"""

PILHA = [(VAL[1], A.CORAL, "Casa"), (VAL[2], A.CORAL, "Mercado"), (VAL[3], A.CORAL, "Educação"),
         (OUTRAS10, A.NEUTRO, "Outras 10 categorias"), (VAL[7], A.BRAND, "Resultado")]
W_PILHA = 900 - 6 * 4
LARG_P = [round(W_PILHA * float(v / VAL[0]), 1) for v, _, _ in PILHA]
W_CHAVE = round(sum(LARG_P[:3]) + 12, 1)

def legenda():
    ys = [870, 954, 1038, 1122, 1206]
    return "".join(f'<div class="lg" id="lg{i}" style="top:{y}px"><u style="background:{cor}"></u><span>{nome}</span><b>R$ {C.brl(float(v))}</b></div>'
                   for i, ((v, cor, nome), y) in enumerate(zip(PILHA, ys)))

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em Relatórios, escolha o <b>Ano 2026</b> e toque em <b>Cascata</b>.</div>
  <div class="tit" id="t2">A receita do ano no alto. Cada <b>degrau</b> é uma categoria que saiu dela.</div>
  <div class="tit" id="t3">Casa, Mercado e Educação: os <b>três maiores degraus</b>.</div>
  <div class="tit" id="t4">No pé da cascata, o resultado: <b>R$&nbsp;24.438,66</b>, 19,4% da receita.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", IMGS)}{EXTRA}</div>
  <div id="s5t">Casa, Mercado e Educação levaram <b>mais da metade</b> da receita.</div>
  <div id="chave" style="width:{W_CHAVE}px"><span>R$ {C.brl(float(TRES))}</span></div>
  <div id="pilha">{"".join(f'<i id="p{i}" style="background:{cor}"></i>' for i, (_, cor, _) in enumerate(PILHA))}</div>
  {legenda()}
  <div id="s5n">Os degraus mais altos mostram <b style="color:{A.BRAND_DARK}">para onde o dinheiro escorre</b>.</div>
</div>

<div class="cena tinta" id="g">
  <div id="gTop">
    <div class="eyebrow">Relatórios</div>
    <div class="h1">Da receita ao resultado: o seu <b>2026</b> numa cascata.</div>
  </div>
  <div id="base0"></div>
  {cascata_html("c")}
  <div class="gv" id="gvR" style="left:{CX0 - 10}px;top:{cy(VAL[0]) - 78:.0f}px;color:#fff">R$ 126.293</div>
  <div class="gv" id="gvS" style="left:{CX0 + 7 * CPASSO + CLARG - 400}px;width:400px;text-align:right;top:{CBASE + 18}px;color:{A.MENTA}">R$ 24.439</div>
  <div class="gr" style="left:{CX0 - 10}px">Receita</div>
  <div class="gr" id="grS" style="left:{CX0 + 7 * CPASSO + CLARG - 300}px;width:300px;text-align:right;top:{CBASE + 84}px">Resultado</div>
</div>

{K.fim("Relatórios no timtimcash")}
"""

JS = f"""
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, S5={list(S5)}, FIM={FIM}, J_SAI={J_SAI};
const TQ_SETA={TQ_SETA}, TQ_CHIP={TQ_CHIP}, TQ_BAR={TQ_BAR};
const PER4={PER4}, PER5={PER5}, SETA={SETA}, CHIP={CHIP}, CHIP_RING={CHIP_RING}, TAPS={json.dumps(TAPS)};
const LARG_P={LARG_P};
const FOTOS=[[0,'f4'],[TQ_SETA+.15,'f5'],[TQ_CHIP+.15,'f6']].concat(TQ_BAR.map((a, i) => [a+.15, 'b'+i]));
function cx(r){{ return [r[0] + r[2]/2, r[1] + r[3]/2]; }}
function somePagina(id, t, t0){{ if (t >= t0 + .2){{ $('t_'+id).style.opacity = 0; $('o_'+id).style.opacity = 0; }} }}
// câmera: o topo de Relatórios; a cascata de perto
const CAM = [[0,0,195,250,1], [TQ_CHIP+.15,TQ_CHIP+.16,195,318,1.2]];
function render(t){{
  // 1. gancho (tinta): a receita do ano desce em degraus até o resultado
  $('c0').style.transform = `scaleY(${{(.9 + .1*pout(t, -.3, .2)).toFixed(3)}})`; $('c0').style.transformOrigin = '50% 100%';
  for (let i = 1; i <= 6; i++){{ const a = .3 + .2*(i-1); const p = pback(t, a, a+.4);
    $('c'+i).style.opacity = lin(t, a, a+.12); $('c'+i).style.transform = `translateY(${{(-60*(1-p)).toFixed(1)}}px)`;
    $('cl'+i).style.opacity = lin(t, a, a+.2); }}
  const pr = pout(t, 1.55, 2.0);
  $('c7').style.transform = `scaleY(${{Math.max(.001, pr).toFixed(3)}})`; $('cl7').style.opacity = lin(t, 1.5, 1.65);
  $('gvR').style.opacity = lin(t, -.2, .1); $('gvS').style.opacity = lin(t, 1.7, 1.9); $('grS').style.opacity = lin(t, 1.7, 1.9);
  saiCima('g', t, G_SAI);

  // 2. a tela real
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, G_SAI+.15, J_SAI); nota('nota', t, G_SAI+.15, J_SAI);
  const cam = camera('tela', t, CAM);
  fotos(FOTOS, t);
  anelCam('aPer4', PER4, cam, 8); anel('aPer4', t, 3.25, TQ_SETA+.1);
  toqueCam('tqSeta', ...cx(SETA), cam); toque('tqSeta', t, TQ_SETA);
  anelCam('aPer5', PER5, cam, 8); anel('aPer5', t, TQ_SETA+.3, TQ_CHIP-.3);
  anelCam('aChip', CHIP_RING, cam, 6); anel('aChip', t, TQ_SETA+.55, TQ_CHIP-.25);
  toqueCam('tqChip', ...cx(CHIP), cam); toque('tqChip', t, TQ_CHIP); somePagina('tqChip', t, TQ_CHIP);
  TQ_BAR.forEach((a, i) => {{ toqueCam('tqB'+i, TAPS[i][0], TAPS[i][1], cam); toque('tqB'+i, t, a); }});

  // 3. a receita dividida: os três maiores degraus e o resto
  some('s5t', t, S5[0], FIM+.3, 30);
  LARG_P.forEach((w, i) => barra('p'+i, t, S5[0]+.35+.12*i, S5[0]+.95+.12*i, w));
  $('chave').style.opacity = prog(t, S5[0]+.9, S5[0]+1.2);
  for (let i = 0; i < 5; i++) some('lg'+i, t, S5[0]+.7+.12*i, FIM+.3, 18);
  some('s5n', t, S5[0]+1.5, FIM+.3, 14);

  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Relatórios</div>
    <div class="h1" style="font-size:124px;line-height:.97;margin-top:36px;color:#fff;text-wrap:balance">O seu <span style="color:{A.MENTA}">2026</span> numa cascata.</div>
  </div>
  <div style="position:absolute;left:90px;top:1482px;width:900px;border-top:5px solid #2F3A31"></div>
  {cascata_html("k", x0=100, passo=115, larg=84, base=1480, alt=520)}
  <div class="cvl" style="left:90px;top:{1480 - 520 - 80}px;color:#fff">R$ 126.293</div>
  <div class="cvl" style="left:{100 + 7 * 115 + 84 - 400}px;width:400px;text-align:right;top:1500px;color:{A.MENTA}">R$ 24.439</div>"""
    css = """.cb{position:absolute;border-radius:12px}.cl{position:absolute;height:0;border-top:4px dashed #4A564C}
.cvl{position:absolute;white-space:nowrap;font-size:56px;font-weight:700;letter-spacing:-.045em;font-variant-numeric:tabular-nums}"""
    return K.pagina_capa(corpo, css, fundo="tinta")


if __name__ == "__main__":
    K.executar(C.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
