# -*- coding: utf-8 -*-
"""Reel de 20/02/2027 (sábado) · "Faxina de sábado" · capa tinta · equipe fs.

Telas reais: captura_20.py, build 2026-10-19.5, celular 390 × 1000 em escala 3, relógio da página em 20/02/2027 10:00, numa
cópia da conta (cenarios.py da cópia da equipe fs, cenário "faxina"): os 9 lançamentos "Mercado da Vila" de janeiro e fevereiro
de 2027 (R$ 3.512,40) estão "Sem categoria", como chegam de um extrato .ofx quando o nome não é reconhecido. Depois da faxina
na tela, a conta fica exatamente como a de base (os números do "depois" são os da conta de base em 20/02).
Passo a passo (Ano 2027): Visão geral "Por categoria" (antes: "Sem categoria R$ 3.512,40 18%", 11 categorias, despesas de
R$ 19.005,50) -> Transações -> busca "mercado da vila" ("9 transações · 9 pagas · 0 pendentes · somam R$ 3.512,40") ->
"Agir sobre as 9 filtradas" -> "Recategorizar todas" -> "merc" no seletor -> "Mercado" -> aviso "9 transações atualizadas
para "Mercado"" -> "Por categoria" (depois: "Mercado R$ 3.897,50 21%", 10 categorias, as mesmas despesas de R$ 19.005,50).
Conta: Mercado = R$ 3.512,40 (Mercado da Vila) + R$ 385,10 (Hortifruti do Bairro, 21/01 R$ 196,70 e 17/02 R$ 188,40).

python3 reel_20.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_20.py
"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro, folga, brl, MENOS

PASTA = "2027-02-20_reel-faxina-de-sabado"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("20")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- conferência com a tela e com o cenário
MDV = [(d, D(str(v))) for d, v in C["cenario"]["sem_categoria"]]
assert len(MDV) == 9 and sum(v for _, v in MDV) == D("3512.40")
antes, depois = C["celular-faxina-1-por-categoria-antes.jpg"], C["celular-faxina-8-por-categoria-depois.jpg"]
assert "R$ 19.005,50\n11 categorias" in antes["texto"] and "R$ 19.005,50\n10 categorias" in depois["texto"]
assert antes["porcat"]["linhas"]["Sem categoria"][1] == "Sem categoria R$ 3.512,40 18%"
assert depois["porcat"]["linhas"]["Mercado"][1] == "Mercado R$ 3.897,50 21%"
assert D("3512.40") + D("196.70") + D("188.40") == D("3897.50")
b15 = C["celular-faxina-3-busca-15.jpg"]
assert "9 transações · 9 pagas · 0 pendentes · somam R$ 3.512,40 · 823 no histórico" in b15["texto"].replace("\n", " ")
assert "Agir sobre as 9 filtradas" in b15["texto"].replace("\n", " ")
assert all("Mercado da Vila Sem categoria · Conta corrente" in r[1] for r in b15["lista"][:3]), b15["lista"][:3]
assert C["aviso"] == 'Mercado"\nDesfazer'.join(['9 transações atualizadas para "', '']) or C["aviso"].startswith('9 transações atualizadas para "Mercado"')
assert all("Mercado da Vila Mercado · Conta corrente" in r[1] for r in C["celular-faxina-7-lista.jpg"]["lista"][:2])
assert "Ano 2027" in C["celular-faxina-2-transacoes.jpg"]["texto"] and "Feb 20 2027" in C["relogio"]

# ---------------------------------------------------------------- caixas (px CSS do celular)
R0 = antes["rolagem"]
def pagina_para_tela(b, rol): return [b[0], round(b[1] - rol, 1), b[2], b[3]]
SEMCAT = pagina_para_tela(antes["porcat"]["linhas"]["Sem categoria"][0], R0)
MERC = pagina_para_tela(depois["porcat"]["linhas"]["Mercado"][0], depois["rolagem"])
ROSCA = pagina_para_tela(antes["porcat"]["canvas"], R0)
BUSCA = b15["busca"]
RESUMO = b15["resumo"]
P6 = C["celular-faxina-6-pronto.jpg"]
FAIXA = uniao(P6["faixa"], P6["recat"], P6["limpar"])
RECAT = P6["recat"]
AVISO = P6["aviso"]
PRIMEIRA = C["celular-faxina-7-lista.jpg"]["lista"][0][0]
ITEM_MERC = C["celular-faxina-5-seletor-merc.jpg"]["item"][:4]
BUSCA_SEL = C["celular-faxina-5-seletor-merc.jpg"]["busca"]

# ---------------------------------------------------------------- tempos (s)
H_SAI = 2.8
T1, T2, T3, T4 = (3.0, 5.35), (5.5, 7.75), (7.9, 10.0), (10.15, 14.25)
TQ_BUSCA = 3.55
LETRAS = [round(3.75 + .085 * k, 3) for k in range(15)]       # uma foto real por letra
TQ_RECAT, TQ_MERC = 6.2, 7.35
J_SAI = 14.25
S5 = 14.45
FIM = 16.85
DUR = 19.6

IMGS = [("i2", tela("celular-faxina-2-transacoes.jpg"))] + \
       [(f"b{k:02d}", tela(f"celular-faxina-3-busca-{k:02d}.jpg")) for k in range(1, 16)] + \
       [("i4", tela("celular-faxina-4-seletor.jpg")), ("i5", tela("celular-faxina-5-seletor-merc.jpg")),
        ("i6", tela("celular-faxina-6-pronto.jpg")), ("i7", tela("celular-faxina-7-lista.jpg")),
        ("i1", tela("celular-faxina-1-por-categoria-antes.jpg")), ("i8", tela("celular-faxina-8-por-categoria-depois.jpg"))]
TR = [0] + LETRAS + [TQ_RECAT + .15, 6.95, TQ_MERC + .15, 9.0, 10.15, 12.25]
IDS = [i for i, _ in IMGS]
EXTRA = K.aneis("aResumo", "aFaixa", "aAviso", "aLinha", "aSem", "aMerc") + K.toques("tqBusca", "tqRecat", "tqMerc")

# ---------------------------------------------------------------- gancho: os 9 cartões, bagunçados, que se arrumam
VALS = [brl(float(v)) for _, v in MDV]
MESES = {"01": "jan", "02": "fev"}
DATAS = [f"{int(d[8:])} {MESES[d[5:7]]}" for d, _ in MDV]
BAG = [(-70, -8, 40), (35, 7, -30), (-40, -5, 10), (30, 9, 25), (-80, 4, -15), (25, -9, 35), (-20, 6, -40), (35, -6, 15), (-60, 8, -20)]
CW, CH0, CG, CY = 860, 82, 12, 650
cards = "".join(f"""<div class="cc" id="cc{k}" style="top:{CY + k * (CH0 + CG)}px">
  <span class="tg" id="tg{k}"><i class="sem">Sem categoria</i><i class="ok">Mercado</i></span>
  <span class="nm">Mercado da Vila <small>{DATAS[k]}</small></span><span class="vl">{MENOS}R$ {VALS[k]}</span></div>""" for k in range(9))
CHECK = ('<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')
LUPA = ('<svg viewBox="0 0 24 24" width="64" height="64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" '
        'stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 L20 20"/></svg>')
ETIQ = ('<svg viewBox="0 0 24 24" width="64" height="64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" '
        'stroke-linejoin="round"><path d="M3 12V4h8l9 9-8 8z"/><circle cx="7.5" cy="8" r="1.4"/></svg>')

CSS = f"""
.tit{{font-size:64px}}
/* gancho */
#g .eyebrow{{position:absolute;left:90px;top:300px}}
#gT{{position:absolute;left:90px;top:350px;width:900px;font-size:104px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#gT b{{color:{A.MENTA}}}
#gS{{position:absolute;left:90px;top:1520px;width:900px;font-size:52px;font-weight:700;letter-spacing:-.03em;color:{A.MENTA};opacity:0}}
.cc{{position:absolute;left:90px;width:{CW}px;height:{CH0}px;border-radius:22px;background:#192019;border:2px solid #2A332B;display:flex;align-items:center;
  gap:22px;padding:0 26px;will-change:transform}}
.cc .nm{{font-size:34px;font-weight:600;color:#fff;letter-spacing:-.02em;white-space:nowrap}}
.cc .nm small{{font-size:27px;font-weight:500;color:{K.DARK_TEXTO};margin-left:12px}}
.cc .vl{{margin-left:auto;font-size:34px;font-weight:700;color:#F0A58C;font-variant-numeric:tabular-nums;white-space:nowrap}}
.tg{{position:relative;width:236px;height:50px;flex:none}}
.tg i{{position:absolute;inset:0;border-radius:999px;font-style:normal;font-size:26px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px}}
.tg .sem{{background:#3A443B;color:{K.DARK_TEXTO}}}
.tg .ok{{background:{A.BRAND};color:#fff;opacity:0}}
/* cena 5 */
#s5 .h2{{position:absolute;left:90px;top:300px;width:900px;font-size:92px;line-height:1.0;color:#fff}}
#s5 .h2 b{{color:{A.MENTA}}}
.pa{{position:absolute;left:90px;width:900px;height:170px;display:flex;align-items:center;gap:34px;opacity:0}}
.pa .ic{{flex:none;width:128px;height:128px;border-radius:32px;background:{A.SOFT};color:{A.BRAND_DEEP};display:flex;align-items:center;justify-content:center;
  font-size:56px;font-weight:700}}
.pa b{{display:block;font-size:52px;font-weight:700;letter-spacing:-.035em;color:#fff;line-height:1.1}}
.pa span{{display:block;font-size:36px;font-weight:500;color:{K.DARK_TEXTO};letter-spacing:-.015em;margin-top:6px}}
#s5n{{position:absolute;left:90px;top:1400px;width:900px;font-size:44px;font-weight:700;color:{A.MENTA};letter-spacing:-.02em;opacity:0}}
/* rótulos antes e depois sobre a janela */
.ad{{position:absolute;left:150px;top:540px;height:52px;padding:0 24px;border-radius:999px;font-size:28px;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;display:flex;align-items:center;opacity:0}}
#adA{{background:#E9E6DC;color:{A.MUTED}}}
#adD{{background:{A.SOFT};color:{A.BRAND_DEEP}}}
"""

CORPO = f"""
<div class="cena papel" id="cenaTela">
  <div class="tit" id="t1">Em Transações, busque o nome: <b>9 sem categoria.</b></div>
  <div class="tit" id="t2"><b>Recategorizar todas</b> e escolha Mercado.</div>
  <div class="tit" id="t3">Pronto: <b>os 9 de uma vez.</b></div>
  <div class="tit" id="t4">E o gráfico volta a dizer <b>para onde foi o dinheiro.</b></div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="ad" id="adA">Antes</div><div class="ad" id="adD">Depois</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA, 390, 1000)}</div>
</div>

<div class="cena tinta" id="s5" style="transform:translateY(1920px)">
  <div class="h2">Faxina em <b>3 passos.</b></div>
  <div class="pa" id="pa0" style="top:640px"><div class="ic">{LUPA}</div><div><b>Busque o nome</b><span>em Transações, no período que quiser</span></div></div>
  <div class="pa" id="pa1" style="top:860px"><div class="ic">{ETIQ}</div><div><b>Recategorizar todas</b><span>age sobre todas as filtradas</span></div></div>
  <div class="pa" id="pa2" style="top:1080px"><div class="ic">{CHECK.replace('width="30" height="30"', 'width="64" height="64"')}</div><div><b>Escolha a categoria</b><span>e, se errar, tem Desfazer</span></div></div>
</div>

<div class="cena tinta" id="g">
  <div class="eyebrow">Faxina de sábado</div>
  <div id="gT"><b>9 lançamentos</b> sem categoria?</div>
  {cards}
  <div id="gS">Arrumados em 10 segundos.</div>
</div>

{K.fim("Transações no timtimcash")}
"""

JS = f"""
const H_SAI={H_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, J_SAI={J_SAI}, S5={S5}, FIM={FIM};
const TQ_BUSCA={TQ_BUSCA}, TQ_RECAT={TQ_RECAT}, TQ_MERC={TQ_MERC}, TR={TR}, IDS={IDS}, BAG={[list(b) for b in BAG]};
poeAnel('aResumo', {folga(RESUMO, 4)}, 6); poeAnel('aFaixa', {folga(FAIXA, 4)}, 6); poeAnel('aAviso', {folga(AVISO, 2)}, 6);
poeAnel('aLinha', {folga(PRIMEIRA, 1)}, 6); poeAnel('aSem', {folga(SEMCAT, 3)}, 6); poeAnel('aMerc', {folga(MERC, 3)}, 6);
poeToque('tqBusca', {BUSCA[0] + 60}, {BUSCA[1] + BUSCA[3] / 2}); poeToque('tqRecat', ...{centro(RECAT)}); poeToque('tqMerc', ...{centro(ITEM_MERC)});
// câmera: [_, _, fx, fy, zoom] em px CSS do celular
const CAM = [[0,0,195,410,1], [3.2,3.21,195,410,1], [4.75,5.15,195,470,.88], [5.6,5.95,195,560,1], [6.3,6.6,195,260,1], [6.95,7.2,195,750,1],
             [7.45,7.8,195,700,1], [9.0,9.3,195,620,1], [10.15,10.16,195,{round(ROSCA[1] + 270, 1)},1]];
function render(t){{
  // 1. gancho: os 9 lançamentos bagunçados se arrumam e ganham a categoria
  saiCima('g', t, H_SAI);
  for (let k=0;k<9;k++){{
    const [dx, rot, dy] = BAG[k], a = .55 + .045*k, p = pout(t, a, a+.5), e = $('cc'+k);
    const ent = pout(t, -.35 + .05*k, .15 + .05*k);
    e.style.opacity = ent; e.style.transform = `translate(${{(dx*(1-p)).toFixed(1)}}px, ${{(dy*(1-p) + 50*(1-ent)).toFixed(1)}}px) rotate(${{(rot*(1-p)).toFixed(2)}}deg)`;
    const f = prog(t, 1.25 + .07*k, 1.45 + .07*k), tg = $('tg'+k);
    tg.children[0].style.opacity = 1 - f; tg.children[1].style.opacity = f; tg.style.transform = `scale(${{1 + .12*Math.sin(Math.PI*f)}})`;
  }}
  $('gS').style.opacity = prog(t, 1.9, 2.2); $('gS').style.transform = `translateY(${{18*(1-pout(t,1.9,2.3))}}px)`;
  // 2. a tela real: a busca, Recategorizar todas, Mercado, o aviso e o Por categoria antes e depois
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, H_SAI+.1, J_SAI);
  const ne = prog(t, H_SAI+.1, H_SAI+.7); $('nota').style.opacity = ne*(1 - prog(t, T4[0]-.25, T4[0])); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(IDS, t, TR);
  toque('tqBusca', t, TQ_BUSCA); anel('aResumo', t, 4.85, 5.4);
  anel('aFaixa', t, 5.6, TQ_RECAT-.05); toque('tqRecat', t, TQ_RECAT); toque('tqMerc', t, TQ_MERC);
  anel('aAviso', t, 7.95, 8.95); anel('aLinha', t, 9.15, 9.95);
  anel('aSem', t, 10.6, 12.1); anel('aMerc', t, 12.55, 14.15);
  some('adA', t, 10.3, 12.15, 14); some('adD', t, 12.3, 14.2, 14);
  // 3. a faxina em 3 toques (tinta)
  sobe('s5', t, S5);
  for (let k=0;k<3;k++) some('pa'+k, t, S5+.5+.3*k, 0, 30);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    linhas = [("Mercado", "−R$ 379,20", "19 fev"), ("Mercado", "−R$ 421,30", "12 fev"), ("Mercado", "−R$ 412,70", "5 fev"), ("Mercado", "−R$ 396,40", "1 fev")]
    cartoes = "".join(f"""<div style="position:absolute;left:90px;top:{940 + k * 112}px;width:900px;height:96px;border-radius:24px;background:#192019;border:2px solid #2A332B;
      display:flex;align-items:center;gap:22px;padding:0 26px">
      <span style="width:220px;height:56px;border-radius:999px;background:{A.BRAND};color:#fff;font-size:28px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px">{CHECK}{n}</span>
      <span style="font-size:36px;font-weight:600;color:#fff;letter-spacing:-.02em">Mercado da Vila <small style="font-size:28px;color:{K.DARK_TEXTO};font-weight:500;margin-left:10px">{d}</small></span>
      <span style="margin-left:auto;font-size:36px;font-weight:700;color:#F0A58C">{v}</span></div>""" for k, (n, v, d) in enumerate(linhas))
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Faxina de sábado</div>
    <div class="h1" style="font-size:128px;line-height:.95;margin-top:34px;color:#fff"><span style="color:{A.MENTA}">9 lançamentos</span> de uma vez.</div>
  </div>
  {cartoes}"""
    return K.pagina_capa(corpo, "", fundo="tinta")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
