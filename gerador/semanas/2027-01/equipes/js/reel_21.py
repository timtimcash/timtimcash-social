# -*- coding: utf-8 -*-
"""Reel de 21/01/2027 (quinta) · "Há quanto tempo o seu dinheiro está lá fora?" · investimento no exterior · capa verde · equipe js.

Telas reais: captura_21.py, build 2026-10-19.5, celular 390 px CSS em escala 3 (janela de 1000 px de altura), conta fictícia de
J/base_app (sem mudança), relógio da página em 21/01/2027 10:00. Remessas (abre no dólar) -> a tabela "Remessas" ("Por remessa"):
cada cartão termina com a data, o câmbio efetivo e o tempo investido (no computador, a coluna "Investido há"):
18/04/2024 · R$ 5,1000 · 33,1 meses; 14/03/2024 · R$ 5,0000 · 34,3 meses; 12/07/2023 · R$ 4,9000 · 42,3 meses ->
um toque em "EUR" (o vídeo mostra só a faixa dos botões de moeda) -> a tabela do euro: 01/12/2026 · R$ 5,7627 · 1,7 meses.
42,3 meses = 3 anos e 6 meses (12/07/2023 a 21/01/2027: 3 anos, 6 meses e 9 dias), o contador do gancho.
O vídeo não mostra o topo de Remessas, "Rendimento ano a ano" nem "Ritmo do retorno": ali há valores em reais de 2026 ao câmbio
salvo de exemplo, e o fechamento de 2026 não existe (a PTAX de 31/12/2026 ainda não saiu). A TIR do "Ritmo do retorno" só é citada,
sem número (não repete 22/10). Post de exterior: sem a frase do controle financeiro.
Os cartões da tabela mostram "Hoje" em reais ao câmbio salvo na conta (o de exemplo, R$ 5,0515 no dólar e R$ 5,6592 no euro, PTAX de
compra de 15/10/2026): o vídeo não destaca esses valores; a legenda diz que o câmbio é de exemplo.

python3 reel_21.py  |  REEL_PREVIA="0 0.5 1 1.6 3.8 6.4 8.8 10.6 12.3 14.6 17.5" python3 reel_21.py
"""
import os, sys, json
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A
MENOS = C.MENOS

PASTA = "2027-01-21_reel-ha-quanto-tempo-esta-la-fora"
SAIDA = C.saida(PASTA)
TELAS = C.telas(PASTA)
TRAB = C.trabalho("21")
CX = C.caixas(PASTA)
FU, F2, F3, FE = (CX[f"celular-remessas-{n}.jpg"] for n in ["1-tabela-dolar", "2-topo-dolar", "3-topo-euro", "4-tabela-euro"])

# ---------------------------------------------------------------- conferência com a tela
LU = FU["tabela"]["linhas"]; LE = FE["tabela"]["linhas"]
assert [(l["data_t"], l["cambio_t"], l["val_t"], l["ha_t"]) for l in LU] == [
    ("18/04/2024", "R$ 5,1000", "US$ 4.000,00", "33,1 meses"), ("14/03/2024", "R$ 5,0000", "US$ 4.000,00", "34,3 meses"),
    ("12/07/2023", "R$ 4,9000", "US$ 4.000,00", "42,3 meses")], [(l["data_t"], l["cambio_t"], l["val_t"], l["ha_t"]) for l in LU]
assert [(l["data_t"], l["cambio_t"], l["val_t"], l["ha_t"]) for l in LE] == [("01/12/2026", "R$ 5,7627", "€ 2.000,00", "1,7 meses")]
assert "Total 3 remessas US$ 12.000,00" in FU["tabela"]["total_t"] and "Total 1 remessa € 2.000,00" in FE["tabela"]["total_t"]
assert [c[0][-3:] for c in F2["chips"]] == ["USD", "EUR"] and F2["chips"][0][5] and not F2["chips"][1][5]
assert F3["chips"][1][5] and not F3["chips"][0][5]
assert "Jan 21 2027" in CX["relogio"]
HOJE = date(2027, 1, 21)
ENVIOS = [(date(2023, 7, 12), "US$ 4.000", "R$ 4,90", "42,3"), (date(2024, 3, 14), "US$ 4.000", "R$ 5,00", "34,3"),
          (date(2024, 4, 18), "US$ 4.000", "R$ 5,10", "33,1"), (date(2026, 12, 1), "€ 2.000", "R$ 5,76", "1,7")]
for d, _, _, m in ENVIOS:          # o tempo do site é (hoje − data) em dias ÷ 30,44 (mês médio), com uma casa
    assert f"{(HOJE - d).days / 30.4375:.1f}".replace(".", ",") == m, (d, m)
assert (HOJE - date(2023, 7, 12)).days // 30.4375 == 42 and 42 // 12 == 3 and 42 % 12 == 6

# ---------------------------------------------------------------- caixas (px CSS da foto)
# texto do tempo e do câmbio dentro de cada cartão: x e largura medidos com Range no site (explora/ver_ha.py)
X_HA, W_HA, X_DATA = 289.2, 59.8, 41
def foto_y(l, F, k="ha"): return round(l[k][1] - F["rolagem"], 1)
HA = [[X_HA - 4, foto_y(l, FU) - 2, W_HA + 8, 20.5] for l in LU]          # "33,1 meses" ...
LINHA = [[X_DATA - 6, foto_y(l, FU) - 5, 320, 26.5] for l in LU]          # data · câmbio · meses
LINHA_E = [X_DATA - 6, foto_y(LE[0], FE) - 5, 320, 26.5]
CHIP_EUR = F2["chips"][1][1:5]
CHIPS = C.uniao(F2["chips"][0][1:5], F2["chips"][1][1:5])

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.6
T1, T2, T3, T4 = (2.9, 5.1), (5.3, 7.55), (7.75, 9.95), (10.15, 13.3)
J1_SAI, J2_IN, TQ_EUR, J2_SAI, J1_VOLTA = 10.05, 10.2, 10.9, 11.45, 11.6
S5 = (13.5, 17.0)
FIM = 17.05
DUR = 19.8

IMGS = [("u1", os.path.join(TELAS, "celular-remessas-1-tabela-dolar.jpg")), ("e4", os.path.join(TELAS, "celular-remessas-4-tabela-euro.jpg"))]
IMGS2 = [("ft2", os.path.join(TELAS, "celular-remessas-2-topo-dolar.jpg")), ("ft3", os.path.join(TELAS, "celular-remessas-3-topo-euro.jpg"))]
EXTRA = K.aneis("aH0", "aH1", "aH2", "aL2", "aL0", "aL1", "aLE")
EXTRA2 = K.aneis("aChips") + K.toques("tqEur")

# ---------------------------------------------------------------- linha do tempo desenhada (cena 5)
X0, X1 = 150, 930
INICIO = date(2023, 7, 1)
def xd(d): return X0 + (X1 - X0) * (d - INICIO).days / (HOJE - INICIO).days
YS = [610, 790, 970, 1150]

def gantt():
    out = []
    for ano in (2024, 2025, 2026):
        x = xd(date(ano, 1, 1))
        out.append(f'<div class="gl" style="left:{x:.1f}px"></div><div class="ga" style="left:{x - 60:.1f}px">{ano}</div>')
    for i, ((d, val, camb, meses), y) in enumerate(zip(ENVIOS, YS)):
        x = xd(d); w = X1 - x
        eu = val.startswith("€")
        rot = f'<b>{d.strftime("%d/%m/%Y")}</b> · {val} a {camb}'
        if eu:
            out.append(f'<div class="gr" id="gr{i}" style="top:{y - 62}px;left:{X1 - 620}px;width:600px;text-align:right">{rot}</div>')
            out.append(f'<div class="gb eu" id="gb{i}" style="top:{y}px;left:{x:.1f}px;width:0"></div>')
            out.append(f'<div class="gm" id="gm{i}" style="top:{y}px;left:{x - 260:.1f}px;width:240px;text-align:right;color:{A.INK}">{meses} meses</div>')
        else:
            out.append(f'<div class="gr" id="gr{i}" style="top:{y - 62}px;left:{x:.1f}px">{rot}</div>')
            out.append(f'<div class="gb" id="gb{i}" style="top:{y}px;left:{x:.1f}px;width:0"><span class="gm2" id="gm{i}">{meses} meses</span></div>')
    out.append(f'<div class="gh" style="left:{X1}px"></div><div class="ghl" style="left:{X1 - 200}px">hoje</div>')
    return "".join(out), [round(X1 - xd(d), 1) for d, _, _, _ in ENVIOS]

GANTT, LARG = gantt()

CSS = f"""
#g{{background:{A.BG}}}
#gTop{{position:absolute;left:90px;top:300px;width:900px}}
#gTop .h1{{font-size:100px;line-height:1;margin-top:30px;color:{A.INK}}}
#gTop .h1 b{{color:{A.BRAND_DARK};font-weight:700}}
#cont{{position:absolute;left:90px;top:790px;display:flex;align-items:baseline;gap:22px;color:{A.INK};font-variant-numeric:tabular-nums}}
#cont .n{{font-size:250px;line-height:1;font-weight:700;letter-spacing:-.06em;color:{A.BRAND_DARK};display:inline-block;min-width:150px;text-align:right}}
#cont .u{{font-size:64px;font-weight:700;letter-spacing:-.04em}}
#cont .e{{font-size:64px;font-weight:600;color:{A.MUTED};margin:0 6px}}
#trilho{{position:absolute;left:90px;top:1150px;width:900px;height:26px;border-radius:13px;background:{A.FIO}}}
#trilho i{{position:absolute;left:0;top:0;height:26px;border-radius:13px;background:{A.BRAND};width:0}}
#trilho b{{position:absolute;top:-17px;width:60px;height:60px;margin-left:-30px;border-radius:50%;background:{A.BRAND};border:8px solid {A.BG};box-shadow:0 0 0 3px {A.BRAND}}}
.tr0{{position:absolute;top:1206px;font-size:32px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em;white-space:nowrap}}
.tr0 b{{color:{A.INK};font-weight:700}}
#jan2{{height:300px;opacity:0}}
/* cena 5: a linha do tempo */
#s5t{{position:absolute;left:90px;top:280px;width:900px;font-size:66px;line-height:1.06;font-weight:700;letter-spacing:-.045em;opacity:0}}
#s5t b{{color:{A.BRAND_DARK}}}
#gw{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}}
.gl{{position:absolute;top:500px;height:800px;border-left:3px dashed {A.NEUTRO}}}
.ga{{position:absolute;top:1316px;width:120px;text-align:center;font-size:30px;font-weight:600;color:{A.MUTED}}}
.gh{{position:absolute;top:470px;height:830px;border-left:5px solid {A.INK}}}
.ghl{{position:absolute;top:1316px;width:186px;text-align:right;font-size:30px;font-weight:700;color:{A.INK}}}
.gr{{position:absolute;font-size:34px;font-weight:500;color:{A.MUTED};letter-spacing:-.015em;white-space:nowrap;opacity:0}}
.gr b{{color:{A.INK};font-weight:700}}
.gb{{position:absolute;height:64px;border-radius:14px 0 0 14px;background:{A.BRAND};overflow:hidden}}
.gb.eu{{background:{A.INK}}}
.gm2{{position:absolute;left:22px;top:0;line-height:64px;font-size:36px;font-weight:700;color:#fff;letter-spacing:-.02em;white-space:nowrap;opacity:0}}
.gm{{position:absolute;line-height:64px;font-size:36px;font-weight:700;letter-spacing:-.02em;white-space:nowrap;opacity:0}}
#s5n{{position:absolute;left:90px;top:1420px;width:900px;font-size:38px;line-height:1.25;font-weight:600;letter-spacing:-.02em;color:{A.INK};opacity:0;text-wrap:balance}}
#s5n b{{color:{A.BRAND_DARK}}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em Remessas, cada envio mostra <b>há quanto tempo</b> está lá fora.</div>
  <div class="tit" id="t2">A primeira, de julho de 2023: <b>42,3 meses</b>.</div>
  <div class="tit" id="t3">As duas de 2024: <b>34,3</b> e <b>33,1 meses</b>.</div>
  <div class="tit" id="t4">No euro, um toque em EUR: a remessa de dezembro tem <b>1,7 meses</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", IMGS)}{EXTRA}</div>
  <div class="janela" id="jan2">{C.camadas("tela2", IMGS2)}{EXTRA2}</div>
  <div id="s5t">Cada envio tem a sua data, <b>o seu câmbio e o seu tempo</b>.</div>
  <div id="gw">{GANTT}</div>
  <div id="s5n">No <b>Ritmo do retorno</b>, a TIR é calculada com a data real de cada envio.</div>
</div>

<div class="cena papel" id="g">
  <div id="gTop">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1">Há quanto tempo o seu dinheiro está <b>lá fora</b>?</div>
  </div>
  <div id="cont"><span class="n" id="cA">0</span><span class="u" id="uA">anos</span><span class="e">e</span><span class="n" id="cM">0</span><span class="u" id="uM">meses</span></div>
  <div id="trilho"><i id="tf"></i><b id="tb"></b></div>
  <div class="tr0" style="left:90px"><b>12/07/2023</b> · a primeira remessa</div>
  <div class="tr0" style="left:790px;width:200px;text-align:right"><b>hoje</b></div>
</div>

{K.fim("Remessas ao exterior no timtimcash")}
"""

JS = f"""
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, S5={list(S5)}, FIM={FIM};
const J1_SAI={J1_SAI}, J2_IN={J2_IN}, TQ_EUR={TQ_EUR}, J2_SAI={J2_SAI}, J1_VOLTA={J1_VOLTA};
const HA={json.dumps(HA)}, LINHA={json.dumps(LINHA)}, LINHA_E={LINHA_E}, CHIP_EUR={CHIP_EUR}, CHIPS={CHIPS};
const LARG={LARG};
function cx(r){{ return [r[0] + r[2]/2, r[1] + r[3]/2]; }}
// a janela da tela real sai e volta (troca da tabela do dólar pela do euro)
function janela2x(id, t, a1, b1, a2, b2){{ const e=$(id); const e1=prog(t,a1,a1+.6), s1=prog(t,b1,b1+.35), e2=prog(t,a2,a2+.55), s2=prog(t,b2,b2+.4);
  const v = t < a2 ? Math.min(e1, 1-s1) : Math.min(e2, 1-s2); e.style.opacity = v;
  e.style.transform = t < a2 ? `translateY(${{(1-e1)*80 - s1*60}}px)` : `translateY(${{(1-e2)*80 - s2*40}}px)`; }}
// câmera: os três cartões; o de 2023 de perto; os dois de 2024; o do euro
const CAM = [[0,0,195,530,1], [5.2,5.75,195,700,1.2], [7.65,8.15,195,445,1.2], [J1_VOLTA-.05,J1_VOLTA,195,694,1.15]];
const CAM2 = [[0,0,195,170,1.2]];
function render(t){{
  // 1. gancho (papel): o contador de anos e meses desde a primeira remessa
  const m = 42*pout(t, -0.45, 1.35), mi = Math.min(42, Math.floor(m + 1e-6));
  $('cA').textContent = Math.floor(mi/12); $('cM').textContent = mi % 12;
  $('uA').textContent = Math.floor(mi/12) === 1 ? 'ano' : 'anos'; $('uM').textContent = (mi % 12) === 1 ? 'mês' : 'meses';
  $('tf').style.width = (900*m/42).toFixed(1) + 'px'; $('tb').style.left = (900*m/42).toFixed(1) + 'px';
  const pulso = 1 + .06*Math.sin(Math.PI*clamp((t-1.35)/.35, 0, 1));
  $('cont').style.transform = `scale(${{pulso.toFixed(3)}})`; $('cont').style.transformOrigin = '0 70%';
  const gs = prog(t, G_SAI, G_SAI+.3);
  $('g').style.opacity = 1 - gs; $('g').style.transform = `translateY(${{-80*gs}}px)`;

  // 2. a tela real: a tabela do dólar, a faixa das moedas, a tabela do euro
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela2x('janela', t, G_SAI+.15, J1_SAI, J1_VOLTA, T4[1]);
  janela('jan2', t, J2_IN, J2_SAI);
  nota('nota', t, G_SAI+.15, T4[1]);
  const cam = camera('tela', t, CAM);
  op('e4', t >= J1_VOLTA ? 1 : 0);
  for (let i = 0; i < 3; i++){{ anelCam('aH'+i, HA[i], cam, 8); anel('aH'+i, t, 3.45 + .22*i, T1[1]); }}
  anelCam('aL2', LINHA[2], cam, 8); anel('aL2', t, 5.85, T2[1]);
  anelCam('aL0', LINHA[0], cam, 8); anel('aL0', t, 8.2, T3[1]);
  anelCam('aL1', LINHA[1], cam, 8); anel('aL1', t, 8.45, T3[1]);
  anelCam('aLE', LINHA_E, cam, 8); anel('aLE', t, J1_VOLTA+.5, T4[1]);
  const cam2 = camera('tela2', t, CAM2, 780, 300);
  op('ft3', t >= TQ_EUR+.15 ? 1 : 0);
  anelCam('aChips', CHIPS, cam2, 8, 780, 300); anel('aChips', t, J2_IN+.3, TQ_EUR-.05);
  toqueCam('tqEur', ...cx(CHIP_EUR), cam2, 780, 300); toque('tqEur', t, TQ_EUR);

  // 3. a linha do tempo desenhada
  some('s5t', t, S5[0], FIM+.3, 30);
  $('gw').style.opacity = prog(t, S5[0]+.1, S5[0]+.45);
  for (let i = 0; i < 4; i++){{ const a = S5[0] + .35 + .28*i;
    some('gr'+i, t, a, FIM+.3, 16); barra('gb'+i, t, a+.1, a+.8, LARG[i]);
    $('gm'+i).style.opacity = prog(t, a+.55, a+.85); }}
  some('s5n', t, S5[0]+1.9, FIM+.3, 16);

  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    # quatro barras do tempo de cada envio, alinhadas em "hoje" (à direita), com o comprimento do tempo investido
    meses = [42.3, 34.3, 33.1, 1.7]
    rot = ["42,3 meses", "34,3 meses", "33,1 meses", "1,7 meses"]
    barras = "".join(f'<div style="position:absolute;left:{990 - 820 * m / 42.3:.1f}px;top:{1030 + 120 * i}px;width:{820 * m / 42.3:.1f}px;height:84px;'
                     f'border-radius:18px 0 0 18px;background:{"#fff" if i < 3 else A.INK}">'
                     + (f'<span style="position:absolute;left:28px;top:0;line-height:84px;font-size:42px;font-weight:700;letter-spacing:-.03em;color:{A.BRAND_DARK};white-space:nowrap">{r}</span>'
                        if i < 3 else f'<span style="position:absolute;right:52px;top:0;line-height:84px;font-size:42px;font-weight:700;letter-spacing:-.03em;color:#fff;white-space:nowrap">{r}</span>')
                     + '</div>' for i, (m, r) in enumerate(zip(meses, rot)))
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1" style="font-size:118px;line-height:.98;margin-top:36px;text-wrap:balance">Há quanto tempo está lá fora?</div>
  </div>
  {barras}
  <div style="position:absolute;left:988px;top:990px;height:520px;border-left:6px solid #fff"></div>
  <div style="position:absolute;left:740px;top:1530px;width:250px;text-align:right;font-size:40px;font-weight:700;color:#fff">hoje</div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


if __name__ == "__main__":
    K.executar(C.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
