# -*- coding: utf-8 -*-
"""Reel de 27/12/2026 (domingo) · "O que mudou no seu dezembro" · capa verde suave · equipe dr2.

Telas reais: captura_27.py, build 2026-10-16.1, celular 390 px CSS em escala 3 (janela de 1300 px de altura), conta fictícia de
N/base_app (sem mudança), relógio da página em 27/12/2026 10:00, período Dezembro 2026. Relatórios (topo, com o Diagnóstico) ->
toque em "O que mudou" no índice (a página rola até o painel) -> "Maiores variações" (pelo índice, em "Variações").
Números da tela (conferidos abaixo com assert), "O que mudou · Maiores desvios em relação à sua média de 12 meses":
Presentes e doações +R$ 875,73 (+906%, 10,1x; média R$ 96,67, agora R$ 972,40); Mercado +R$ 441,93 (+29%); Lazer e hobbies
−R$ 311,60 (−77%); Compras +R$ 305,08 (+556%, 6,6x). Os três maiores desvios (em R$) são os do gancho e do resumo.
"Maiores variações · Despesas por categoria · Dezembro 2026 vs 1 nov - 27 nov": Presentes e doações novo, Roupas novo, Mercado +35%,
Transporte −1%, Compras −45%, Bares e restaurantes −52%, Lazer e hobbies −70%.
O gancho e o resumo desenham os três desvios como setas a partir da linha da média, com o comprimento proporcional ao valor em R$.

python3 reel_27.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_27.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, saida, trabalho, caixas, camadas, pagina, uniao, centro, MENOS

PASTA = "2026-12-27_reel-o-que-mudou-no-seu-ano"
SAIDA = saida(PASTA)
TELAS = os.path.join(SAIDA, "telas")
TRAB = trabalho("27")
C = caixas(PASTA)
CA, CB, CC = C["celular-relatorios-1-topo.jpg"], C["celular-relatorios-2-o-que-mudou.jpg"], C["celular-relatorios-3-maiores-variacoes.jpg"]

# ---------------------------------------------------------------- conferência com a tela
L = {l[0]: l for l in CA["oqm_linhas"]}
assert L["Presentes e doações"][5] == "Presentes e doações | média R$ 96,67 · agora R$ 972,40 | +R$ 875,73 | +906% (10,1x)"
assert L["Mercado"][5] == "Mercado | média R$ 1.550,07 · agora R$ 1.992,00 | +R$ 441,93 | +29%"
assert L["Lazer e hobbies"][5] == "Lazer e hobbies | média R$ 403,60 · agora R$ 92,00 | −R$ 311,60 | −77%"
assert L["Compras"][5] == "Compras | média R$ 54,92 · agora R$ 360,00 | +R$ 305,08 | +556% (6,6x)"
assert "Maiores desvios em relação à sua média de 12 meses" in CA["oqm_texto"]
V = {l[0]: l for l in CC["var_linhas"]}
assert V["Presentes e doações"][5].endswith("novo") and V["Roupas"][5].endswith("novo") and V["Lazer e hobbies"][5].endswith("−70%")
assert "Dezembro 2026 vs 1 nov - 27 nov" in CC["var_texto"]
assert [c[0] for c in CB["chips"] if c[1]] == ["O que mudou"] and [c[0] for c in CC["chips"] if c[1]] == ["Variações"]
DESV = [("Presentes", 875.73, "+R$ 875,73"), ("Mercado", 441.93, "+R$ 441,93"), ("Lazer", -311.60, f"{MENOS}R$ 311,60")]
assert round(972.40 - 96.67, 2) == 875.73 and round(1992.00 - 1550.07, 2) == 441.93 and round(92.00 - 403.60, 2) == -311.60

# ---------------------------------------------------------------- caixas (px CSS) e alinhamento das duas fotos
OFF_B = CA["oqm"][1] - CB["oqm"][1]                 # a foto depois do toque, posta onde o painel já estava na foto do topo
CHIP = [c for c in CA["chips"] if c[0] == "O que mudou"][0][2:]
R1, R2, R3 = L["Presentes e doações"][1:5], L["Mercado"][1:5], L["Lazer e hobbies"][1:5]
NOVOS = uniao(V["Presentes e doações"][1:5], V["Roupas"][1:5])
FY_PAINEL = CA["oqm"][1] + CA["oqm"][3] / 2 - 12

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.6
T1, T2, T3, T4 = (2.9, 5.1), (5.4, 7.6), (7.8, 10.0), (10.2, 12.1)
TQ = 4.45
ROLA = (4.6, 5.3)
J1_SAI = 12.2
J2 = 12.35
T5 = (12.45, 15.0)
J2_SAI = 15.05
S6 = 15.2
FIM = 18.7
DUR = 21.45

IMGS1 = [("fA", os.path.join(TELAS, "celular-relatorios-1-topo.jpg"))]
EXTRA1 = (f'<img id="fB" src="file://{os.path.join(TELAS, "celular-relatorios-2-o-que-mudou.jpg")}" style="top:{OFF_B * 2}px;opacity:0">'
          + K.aneis("aChip") + K.aneis("aR1", "aR2", cor="coral") + K.aneis("aR3") + K.toques("tqChip"))
IMGS2 = [("fC", os.path.join(TELAS, "celular-relatorios-3-maiores-variacoes.jpg"))]
EXTRA2 = K.aneis("aNovos", cor="coral")


# ---------------------------------------------------------------- setas dos desvios (gancho e resumo)
def setas(pre, cor_sobe, cor_desce, cor_nome, cor_val_sobe, cor_val_desce, cor_linha, base=1260, escala=430):
    xs = [320, 575, 830]
    partes = [f'<div class="linha" style="top:{base}px;border-color:{cor_linha}"></div>',
              f'<div class="media" style="top:{base - 44}px;color:{cor_nome}">sua média</div>']
    for i, ((nome, v, txt), x) in enumerate(zip(DESV, xs)):
        L_ = escala * abs(v) / DESV[0][1]
        sobe = v > 0
        cor = cor_sobe if sobe else cor_desce
        topo = base - L_ if sobe else base
        ponta = "M-30 34 L0 0 L30 34" if sobe else f"M-30 {L_ - 34:.1f} L0 {L_:.1f} L30 {L_ - 34:.1f}"
        haste = f"M0 {L_:.1f} L0 4" if sobe else f"M0 0 L0 {L_ - 4:.1f}"
        partes.append(f"""<svg class="seta" id="{pre}s{i}" style="left:{x - 40}px;top:{topo:.1f}px;width:80px;height:{L_ + 6:.1f}px;transform-origin:40px {L_ if sobe else 0:.1f}px"
   viewBox="-40 -3 80 {L_ + 6:.1f}"><path d="{haste}" stroke="{cor}" stroke-width="24" stroke-linecap="round" fill="none"/>
   <path d="{ponta}" stroke="{cor}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>""")
        yv = (topo - 64) if sobe else (base + L_ + 14)
        partes.append(f'<div class="val" id="{pre}v{i}" style="left:{x - 150}px;top:{yv:.1f}px;color:{cor_val_sobe if sobe else cor_val_desce}">{txt}</div>')
        yn = (base + 22) if sobe else (base - 70)
        partes.append(f'<div class="nome" id="{pre}n{i}" style="left:{x - 150}px;top:{yn}px;color:{cor_nome}">{nome}</div>')
    return "".join(partes)


CSS = f"""
#g{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
#gTop{{position:absolute;left:90px;top:330px;width:900px}}
#gTop .h1{{font-size:100px;margin-top:30px}}
.linha{{position:absolute;left:90px;width:900px;height:0;border-top:4px dashed}}
.media{{position:absolute;left:90px;font-size:29px;font-weight:600;letter-spacing:-.01em}}
.seta{{position:absolute;overflow:visible}}
.val{{position:absolute;width:300px;text-align:center;font-size:50px;font-weight:700;letter-spacing:-.04em;font-variant-numeric:tabular-nums;opacity:0}}
.nome{{position:absolute;width:300px;text-align:center;font-size:40px;font-weight:600;letter-spacing:-.02em;opacity:0}}
.tit{{font-size:66px}}
#janela2{{opacity:0}}
#nota2{{opacity:0}}
#s6 .h2{{position:absolute;left:90px;top:320px;width:900px;font-size:96px;line-height:1.02;color:#fff}}
#s6 .h2 b{{color:{A.MENTA}}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em Relatórios, toque em <b>O que mudou</b>.</div>
  <div class="tit" id="t2">Presentes: <b>10,1 vezes</b> a média dos últimos 12 meses.</div>
  <div class="tit" id="t3">Mercado: <b>+R$&nbsp;441,93</b> acima da média.</div>
  <div class="tit" id="t4">Lazer: <b>{MENOS}77%</b>, bem abaixo da média.</div>
  <div class="tit" id="t5">Contra novembro, até o dia 27: <b>presentes e roupas</b> são novos.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS1, EXTRA1)}</div>
  <div class="nota" id="nota2">{K.NOTA}</div>
  <div class="janela" id="janela2">{camadas("tela2", IMGS2, EXTRA2)}</div>
</div>

<div class="cena tinta" id="s6" style="transform:translateY(1920px)">
  <div class="h2">Antes de virar o ano, veja <b>o que mudou.</b></div>
  {setas("r", A.CORAL, A.MENTA, "#fff", A.CORAL, A.MENTA, "#3A433B")}
</div>

<div class="cena papel" id="g">
  <div id="gTop">
    <div class="eyebrow">Relatórios</div>
    <div class="h1">O que fugiu do normal no seu <span style="color:{A.BRAND_DARK}">dezembro</span>?</div>
  </div>
  {setas("g", A.CORAL, A.BRAND, A.INK, K.CORAL_TXT, A.BRAND_DARK, A.NEUTRO)}
</div>

{K.fim("Relatórios no timtimcash")}
"""

JS = f"""
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)};
const TQ={TQ}, ROLA={list(ROLA)}, J1_SAI={J1_SAI}, J2={J2}, J2_SAI={J2_SAI}, S6={S6}, FIM={FIM};
poeAnel('aChip', {CHIP}, 8); poeToque('tqChip', ...{centro(CHIP)});
poeAnel('aR1', {R1}, 14); poeAnel('aR2', {R2}, 14); poeAnel('aR3', {R3}, 14);
poeAnel('aNovos', {NOVOS}, 14);
// câmera: o topo; a rolagem que o toque faz; o painel inteiro
const CAM1 = [[0,0,195,250,1], [ROLA[0],ROLA[1],195,{FY_PAINEL:.1f},1]];
const CAM2 = [[0,0,195,300,1]];
function anima(pre, t, a){{
  for (let i=0;i<3;i++){{ const a0 = a + i*.22; const p = pback(t, a0, a0+.6);
    $(pre+'s'+i).style.transform = `scaleY(${{Math.max(0.001, p).toFixed(3)}})`;
    $(pre+'v'+i).style.opacity = lin(t, a0+.3, a0+.5); $(pre+'n'+i).style.opacity = lin(t, a0+.1, a0+.3); }}
}}
function render(t){{
  // 1. gancho: três desvios da média, como setas
  anima('g', t, -0.35);
  const gs = prog(t, G_SAI, G_SAI+.28);
  $('g').style.opacity = 1 - gs; $('g').style.transform = `translateY(${{-70*gs}}px)`;

  // 2. a tela real: o índice, a rolagem até "O que mudou" e as três linhas
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, G_SAI+.2, J1_SAI);
  const n1 = prog(t, G_SAI+.2, G_SAI+.8);
  $('nota').style.opacity = n1*(1 - prog(t, J1_SAI, J1_SAI+.4)); $('nota').style.transform = `translateY(${{(1-n1)*80}}px)`;
  camera('tela', t, CAM1);
  op('fB', t >= ROLA[1] ? 1 : 0);
  anel('aChip', t, 3.3, 4.3); toque('tqChip', t, TQ);
  anel('aR1', t, 5.75, 7.45); anel('aR2', t, 8.15, 9.85); anel('aR3', t, 10.5, 11.95);

  // 3. Maiores variações
  titulo('t5', t, T5[0], T5[1]);
  janela('janela2', t, J2, J2_SAI);
  const n2 = prog(t, J2, J2+.6);
  $('nota2').style.opacity = n2*(1 - prog(t, J2_SAI, J2_SAI+.4)); $('nota2').style.transform = `translateY(${{(1-n2)*80}}px)`;
  camera('tela2', t, CAM2);
  anel('aNovos', t, 13.0, 14.9);

  // 4. resumo em tinta
  sobe('s6', t, S6);
  anima('r', t, S6+.55);

  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    xs, L_ = [330, 540, 750], [360, 250, 210]
    cores = [A.CORAL, A.CORAL, A.BRAND]
    base = 1250
    svgs = []
    for x, l, cor, sobe in zip(xs, L_, cores, [True, True, False]):
        topo = base - l if sobe else base - 40
        ponta = "M-34 40 L0 0 L34 40" if sobe else f"M-34 {l - 40} L0 {l} L34 {l - 40}"
        haste = f"M0 {l} L0 6" if sobe else f"M0 0 L0 {l - 6}"
        svgs.append(f"""<svg style="position:absolute;left:{x - 45}px;top:{topo}px;overflow:visible" width="90" height="{l}" viewBox="-45 0 90 {l}">
          <path d="{haste}" stroke="{cor}" stroke-width="30" stroke-linecap="round" fill="none"/>
          <path d="{ponta}" stroke="{cor}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>""")
    corpo = f"""{K.logo('suave')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Relatórios</div>
    <div class="h1" style="font-size:120px;line-height:.97;margin-top:34px;text-wrap:balance">O que mudou no seu <span style="color:{A.BRAND_DEEP}">dezembro</span></div>
  </div>
  <div style="position:absolute;left:200px;top:{base - 20}px;width:680px;border-top:5px dashed {A.BRAND_DEEP};opacity:1"></div>
  {"".join(svgs)}"""
    return K.pagina_capa(corpo, "", fundo="suave")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
