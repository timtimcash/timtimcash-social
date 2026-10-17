# -*- coding: utf-8 -*-
"""Reel de 17/12/2026 (quinta) · "Dólar e euro: cada um na sua moeda" · capa verde suave · equipe dr2.

Telas reais: captura_17.py, build 2026-10-16.1, celular 390 px CSS em escala 3, conta fictícia de N/base_app (sem mudança),
relógio da página em 16/12/2026 10:00. Remessas abre no dólar; um toque no botão "EUR" troca a tela inteira para o euro.
Números da tela (conferidos abaixo com assert):
- dólar: US$ 13.310 na carteira hoje · +US$ 1.310,00 · +10,9% em US$ · +R$ 7.235,46 · +12,1% em R$;
- euro: € 2.012 na carteira hoje · +€ 12,00 · +0,6% em € · −R$ 139,09 · −1,2% em R$ · R$ 11.386,31 ao câmbio de hoje (R$ 5,6592);
  "O câmbio caiu 1,8% desde o câmbio médio do que ainda está lá fora (R$ 5,7627 → R$ 5,6592) e devolveu R$ 207."
18 moedas e 41 destinos: listas _REM_MOEDAS e _REM_PAISES do código do site (build 2026-10-16.1), contadas.
O site não soma moedas diferentes num total (FUNCIONALIDADES.md): o vídeo não diz que soma.

python3 reel_17.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_17.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, saida, trabalho, caixas, camadas, pagina, uniao, centro, MENOS

PASTA = "2026-12-17_reel-dolar-e-euro"
SAIDA = saida(PASTA)
TELAS = os.path.join(SAIDA, "telas")
TRAB = trabalho("17")
C = caixas(PASTA)
U, EU = C["celular-remessas-dolar.jpg"], C["celular-remessas-euro.jpg"]

# ---------------------------------------------------------------- conferência com a tela
tu, te = U["texto"], EU["texto"]
assert "US$13.310 na carteira hoje" in tu.replace("\n", " ")
assert "+US$ 1.310,00\n+10,9% em US$\n+R$ 7.235,46\n+12,1% em R$" in tu
assert "€2.012 na carteira hoje" in te.replace("\n", " ")
assert "+€ 12,00\n+0,6% em €\n−R$ 139,09\n−1,2% em R$" in te
assert "R$ 11.386,31 ao câmbio de hoje (R$ 5,6592)" in te
assert "O câmbio caiu 1,8% desde o câmbio médio do que ainda está lá fora (R$ 5,7627 → R$ 5,6592) e devolveu R$ 207." in te
assert round(2012 * 5.6592, 2) == 11386.31 and round(11386.31 - 11525.40, 2) == -139.09
MOEDAS = ["USD", "EUR", "GBP", "CHF", "CAD", "AUD", "JPY", "SGD", "HKD", "AED", "NZD", "SEK", "NOK", "DKK", "ILS", "CNY", "MXN", "UYU"]
assert len(MOEDAS) == 18

# ---------------------------------------------------------------- caixas (px CSS do celular)
CHIPS = U["chips"][:2] + [U["chip_eur"][0] + U["chip_eur"][2] - U["chips"][0], U["chips"][3]]
PIL_U = uniao(*[p[1:] for p in U["pilulas"]])                 # as duas pílulas do dólar (uma embaixo da outra)
PIL_E1 = [p[1:] for p in EU["pilulas"] if "€" in p[0] and "R$" not in p[0]][0]
PIL_E2 = [p[1:] for p in EU["pilulas"] if "R$" in p[0]][0]
NUM_U = uniao(U["numero"], U["na_carteira"])
NUM_E = uniao(EU["numero"], EU["na_carteira"])
TXT_E = EU["origem_txt"]
EURX, EURY = centro(U["chip_eur"])

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.5
T1, T2 = (2.85, 4.75), (5.0, 6.75)
TOQ = 6.95                     # toque no EUR
T3, T4 = (7.35, 9.65), (9.9, 12.4)
J_SAI = 12.45
T5 = (12.75, 16.45)
T6 = (16.7, 18.6)
FIM = 18.65
DUR = 21.4

IMGS = [("iU", os.path.join(TELAS, "celular-remessas-dolar.jpg")), ("iE", os.path.join(TELAS, "celular-remessas-euro.jpg"))]
EXTRA = K.aneis("aChips", "aPilU", "aNumU", "aPilE1", "aTxtE") + K.aneis("aPilE2", cor="coral") + K.toques("tqEur")

def pilula(txt, fundo, cor, tam=88, extra=""):
    return f'<span class="pil" style="background:{fundo};color:{cor};font-size:{tam}px{extra}">{txt}</span>'

grade_moedas = "".join(f'<span class="mo{" on" if m in ("USD", "EUR") else ""}" id="m{i}">{m}</span>' for i, m in enumerate(MOEDAS))

CSS = f"""
#g{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
#gTop{{position:absolute;left:90px;top:330px;width:900px}}
#gTop .h1{{font-size:112px;margin-top:30px}}
.pil{{display:inline-flex;align-items:center;justify-content:center;height:1.62em;padding:0 .62em;border-radius:999px;font-weight:700;
  letter-spacing:-.04em;font-variant-numeric:tabular-nums;white-space:nowrap;box-shadow:0 18px 40px -22px rgba(15,20,16,.45)}}
.eqL{{position:absolute;left:0;width:1080px;display:flex;justify-content:center}}
#gMais,#gIgual{{font-weight:700;letter-spacing:-.04em;color:{A.MUTED}}}
#gIgual{{color:{A.BRAND_DARK}}}
#gIgual b{{display:inline-block;color:{A.BRAND_DARK}}}
.tit{{font-size:66px}}
/* resumo */
#res{{position:absolute;left:90px;top:640px;width:900px;opacity:0}}
.tab{{background:#fff;border:2px solid {A.FIO};border-radius:40px;padding:18px 40px 26px;box-shadow:0 1px 2px rgba(15,20,16,.04),0 18px 40px -20px rgba(15,20,16,.18)}}
.tr{{display:grid;grid-template-columns:286px 1fr 1fr;column-gap:22px;align-items:center;padding:30px 0;border-bottom:3px solid {A.FIO}}}
.tr:last-child{{border-bottom:0}}
.tr.cab{{padding:16px 0 18px}}
.cab span{{font-size:28px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{A.MUTED}}}
.moeda{{display:flex;flex-direction:column;gap:10px}}
.moeda .pil{{font-size:46px;height:1.5em;align-self:flex-start;box-shadow:none}}
.moeda i{{font-style:normal;white-space:nowrap;font-size:31px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em;font-variant-numeric:tabular-nums}}
.pct{{display:flex;align-items:center;gap:10px;font-size:70px;font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums}}
.pct svg{{width:40px;height:40px;flex:none}}
.pos{{color:{A.BRAND_DARK}}}
.neg{{color:{A.RED_TEXT}}}
#resNota{{margin-top:34px;font-size:38px;line-height:1.3;font-weight:600;letter-spacing:-.02em;color:{A.INK};opacity:0;text-wrap:balance}}
/* 18 moedas */
#mo{{position:absolute;left:90px;top:720px;width:900px;display:grid;grid-template-columns:repeat(6,1fr);gap:26px 18px}}
.mo{{display:flex;align-items:center;justify-content:center;height:122px;border-radius:999px;background:#fff;border:3px solid {A.FIO};
  font-size:46px;font-weight:700;letter-spacing:.02em;color:{A.INK};opacity:0}}
.mo.on{{background:{A.BRAND};border-color:{A.BRAND};color:#fff}}
#moNota{{position:absolute;left:90px;top:1190px;width:900px;font-size:38px;line-height:1.3;font-weight:600;color:{A.MUTED};letter-spacing:-.02em;opacity:0}}
"""

SETA_C = f'<svg viewBox="0 0 24 24" fill="none" stroke="{A.BRAND_DARK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5"/><path d="M5.5 11.5 12 5l6.5 6.5"/></svg>'
SETA_B = f'<svg viewBox="0 0 24 24" fill="none" stroke="{A.RED_TEXT}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="M5.5 12.5 12 19l6.5-6.5"/></svg>'

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em Remessas, <b>cada moeda</b> tem o seu botão.</div>
  <div class="tit" id="t2">Dólar: <b>+10,9%</b> em US$. Em reais, <b>+12,1%</b>.</div>
  <div class="tit" id="t3">Euro: <b>+0,6%</b> em euro. Em reais, <span style="color:{A.RED_TEXT}">{MENOS}1,2%</span>.</div>
  <div class="tit" id="t4">Pagou <b>R$&nbsp;5,7627</b> por euro, com IOF. Hoje: <b>R$&nbsp;5,6592</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>

  <div class="tit" id="t5">Somar as duas esconderia isso. <b>Cada uma na sua moeda.</b></div>
  <div id="res">
    <div class="tab">
      <div class="tr cab"><span></span><span>na moeda</span><span>em reais</span></div>
      <div class="tr" id="r1"><div class="moeda">{pilula("US$", A.BRAND, "#fff", 46)}<i>13.310 na carteira</i></div>
        <div class="pct pos">+10,9%</div><div class="pct pos">+12,1%</div></div>
      <div class="tr" id="r2"><div class="moeda">{pilula("€", A.INK, "#fff", 46)}<i>2.012 na carteira</i></div>
        <div class="pct pos">+0,6%</div><div class="pct neg">{MENOS}1,2%</div></div>
    </div>
    <div id="resNota">Em Remessas, o timtimcash não soma moedas diferentes num total: cada uma é medida na própria moeda e em reais.</div>
  </div>

  <div class="tit" id="t6"><b>18 moedas</b> e <b>41 destinos</b>.</div>
  <div id="mo">{grade_moedas}</div>
  <div id="moNota">Cada moeda em uso ganha o seu botão em Remessas.</div>
</div>

<div class="cena papel" id="g">
  <div id="gTop">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1">Quanto você tem <span style="color:{A.BRAND_DARK}">lá fora</span>?</div>
  </div>
  <div class="eqL" id="gU" style="top:700px">{pilula("US$ 13.310", A.BRAND, "#fff", 118)}</div>
  <div class="eqL" style="top:930px"><span id="gMais" style="font-size:130px;line-height:1">+</span></div>
  <div class="eqL" id="gE" style="top:1075px">{pilula("€ 2.012", A.INK, "#fff", 118)}</div>
  <div class="eqL" style="top:1318px"><span id="gIgual" style="font-size:170px;line-height:1">= <b id="gQ">?</b></span></div>
</div>

{K.fim("Remessas ao exterior no timtimcash")}
"""

JS = f"""
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, T6={list(T6)};
const TOQ={TOQ}, J_SAI={J_SAI}, FIM={FIM};
poeAnel('aChips', {CHIPS}, 10); poeAnel('aPilU', {PIL_U}, 10); poeAnel('aNumU', {NUM_U}, 10);
poeAnel('aPilE1', {PIL_E1}, 9); poeAnel('aPilE2', {PIL_E2}, 9); poeAnel('aTxtE', {TXT_E}, 12);
poeToque('tqEur', {EURX}, {EURY});
// câmera: o cartão do topo inteiro; zoom nas pílulas; desce até "De onde veio o resultado em reais"
const CAM = [[0,0,195,250,1], [4.95,5.5,195,300,1.12], [6.6,7.05,195,330,1.1], [9.75,10.45,195,640,1.0], [10.75,11.3,195,{TXT_E[1] + TXT_E[3]/2 - 40:.1f},1.15]];
function render(t){{
  // 1. gancho: a pergunta e a conta que não fecha
  const gs = prog(t, G_SAI, G_SAI+.28);
  $('g').style.opacity = 1 - gs; $('g').style.transform = `translateY(${{-70*gs}}px)`;
  const pu = pback(t, -0.18, 0.62), pe = pback(t, 0.12, 0.92);
  const fl = Math.sin(t*2.6), fl2 = Math.sin(t*2.6 + 1.9);
  $('gU').style.transform = `translate(${{(1-pu)*-1000}}px, ${{(fl*7).toFixed(1)}}px)`; $('gE').style.transform = `translate(${{(1-pe)*1000}}px, ${{(fl2*7).toFixed(1)}}px)`;
  const pm = pback(t, .62, 1.02); $('gMais').style.display='inline-block'; $('gMais').style.opacity = lin(t,.62,.77); $('gMais').style.transform = `scale(${{.4+.6*pm}})`;
  const pi = pback(t, .9, 1.3); $('gIgual').style.display='inline-block'; $('gIgual').style.opacity = lin(t,.9,1.05); $('gIgual').style.transform = `scale(${{.4+.6*pi}})`;
  const bat = Math.max(0, Math.sin(Math.PI*2*(t-1.3)/0.9));
  $('gQ').style.transform = `scale(${{1 + .16*bat*(t>1.3?1:0)}}) rotate(${{(t>1.3? 8*Math.sin(Math.PI*2*(t-1.3)/0.9):0).toFixed(2)}}deg)`;

  // 2. a tela real: dólar, toque no EUR, euro
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, G_SAI+.22, J_SAI);
  const nt = prog(t, G_SAI+.22, G_SAI+.82) * (1 - prog(t, J_SAI, J_SAI+.4));
  $('nota').style.opacity = nt; $('nota').style.transform = `translateY(${{(1-prog(t, G_SAI+.22, G_SAI+.82))*80}}px)`;
  camera('tela', t, CAM);
  op('iE', t >= TOQ+.15 ? 1 : 0);              // troca seca, como no site (o botão redesenha a tela)
  anel('aChips', t, 3.25, 4.6); anel('aPilU', t, 5.55, 6.55);
  toque('tqEur', t, TOQ);
  anel('aPilE1', t, 7.6, 9.5); anel('aPilE2', t, 7.85, 9.5); anel('aTxtE', t, 10.55, 12.3);

  // 3. resumo: as duas moedas, cada uma na sua conta
  titulo('t5', t, T5[0], T5[1]);
  const r0 = prog(t, T5[0]+.1, T5[0]+.5), r9 = prog(t, T5[1], T5[1]+.3);
  $('res').style.opacity = Math.min(r0, 1-r9); $('res').style.transform = `translateY(${{(1-r0)*50 - r9*30}}px)`;
  ['r1','r2'].forEach((id,i) => {{ const p = prog(t, T5[0]+.35+i*.35, T5[0]+.8+i*.35); $(id).style.opacity = p; $(id).style.transform = `translateX(${{(1-p)*-50}}px)`; }});
  $('resNota').style.opacity = prog(t, T5[0]+1.3, T5[0]+1.7);

  // 4. 18 moedas e 41 destinos
  titulo('t6', t, T6[0], FIM+.4);
  const m9 = prog(t, FIM+.45, FIM+.5);
  for (let i=0;i<18;i++){{ const a0 = T6[0] + .05 + i*.045; const p = pback(t, a0, a0+.4);
    $('m'+i).style.opacity = lin(t, a0, a0+.12)*(1-m9); $('m'+i).style.transform = `scale(${{(.5+.5*p).toFixed(3)}})`; }}
  $('moNota').style.opacity = prog(t, T6[0]+.6, T6[0]+1.0)*(1-m9);

  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('suave')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1" style="font-size:118px;line-height:.97;margin-top:34px;text-wrap:balance">Dólar e euro, <span style="color:{A.BRAND_DEEP}">cada um na sua moeda</span></div>
  </div>
  <div style="position:absolute;left:90px;top:1105px;width:900px;display:flex;gap:36px;justify-content:center">
    <span class="cp" style="background:{A.BRAND}">US$</span><span class="cp" style="background:{A.INK}">€</span>
  </div>"""
    css = f""".cp{{display:inline-flex;align-items:center;justify-content:center;width:400px;height:260px;border-radius:999px;color:#fff;
      font-size:150px;font-weight:700;letter-spacing:-.05em;box-shadow:0 28px 60px -30px rgba(15,20,16,.5)}}"""
    return K.pagina_capa(corpo, css, fundo="suave")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
