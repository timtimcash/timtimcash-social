# -*- coding: utf-8 -*-
"""Reel de 30/12/2026 (quarta) · "2027 começa com um plano" · capa verde · equipe dr2.

Telas reais: captura_30.py, build 2026-10-16.1, celular 390 × 844 em escala 3 (as fotos do resultado com a janela esticada para
1500 px), conta fictícia de N/base_app (sem mudança), relógio da página em 30/12/2026 10:00. Simulação futura -> "Cenário base" ->
mês final de "Setembro de 2027" para "Dezembro de 2027" -> "Saldo em dez/27 R$ 37.720" e o gráfico desde "Hoje" -> "Plano contra
realidade" (+R$ 2.180 previstos por mês contra +R$ 2.464 de média real em 6 meses: "Sobra R$ 284 por mês a mais que o plano previa
(13% acima).") -> "Definir uma meta" de R$ 35.000 -> "Meta R$ 35 mil · atinge em nov/27".
O gancho desenha a curva do saldo projetado mês a mês com os números da linha do tempo do site (partida R$ 14.180; dez/26 R$ 16.360;
jan/27 R$ 13.740, com o ajuste de R$ 4.800 de impostos do cenário; +R$ 2.180 por mês de fev/27 a dez/27; dez/27 R$ 37.720).
A simulação não calcula juros nem rendimento sobre o saldo: o vídeo não diz que calcula.

python3 reel_30.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_30.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, saida, trabalho, caixas, camadas, pagina, uniao, centro

PASTA = "2026-12-30_reel-2027-comeca-com-um-plano"
SAIDA = saida(PASTA)
TELAS = os.path.join(SAIDA, "telas")
TRAB = trabalho("30")
C = caixas(PASTA)
c1, c2, c3, c4 = (C[f"celular-simulacao-{n}.jpg"] for n in ["1-cenarios", "2-cenario", "3-meses", "4-dezembro"])
c5, c6, c7 = C["celular-simulacao-5-resultado.jpg"], C["celular-simulacao-6-meta.jpg"], C["celular-simulacao-7-meta-ok.jpg"]

# ---------------------------------------------------------------- conferência com a tela
t5, t7 = c5["texto"], c7["texto"]
assert "Setembro de 2027" in c2["texto"] and "Dezembro de 2027" in c4["texto"]
assert "Saldo em dez/27\nR$37.720\n+R$ 1.810 por mês · 13 meses" in t5
assert "O PLANO PREVÊ\n+R$ 2.180\npor mês\n×\nACONTECEU\n+R$ 2.464\nmédia de 6 meses" in t5
assert "Sobra R$ 284 por mês a mais que o plano previa (13% acima)." in t5
assert "Saldo de partida\nR$ 14.180" in t5 and "saldo em dez/26: R$ 16.360" in t5 and "saldo em jan/27: R$ 13.740" in t5
assert "fev/27 a nov/2710 MESES\n+R$ 2.180/mês" in t5 and "saldo em nov/27: R$ 35.540" in t5 and "dez/27\nR$ 37.720" in t5
assert "Meta R$ 35 mil · atinge em nov/27" in t7
SERIE = [14180, 16360, 13740] + [13740 + 2180 * k for k in range(1, 12)]
assert SERIE[-1] == 37720 and SERIE[-2] == 35540 and len(SERIE) == 14
ROT = ["Hoje", "dez/26", "jan/27", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez/27"]

# ---------------------------------------------------------------- caixas (px CSS da foto)
def foto(c, k):
    b = c[k]; r = c.get("rolagem", 0)
    return [b[0], round(b[1] - r, 1), b[2], b[3]]
BASE_CARD = [20, foto(c1, "base")[1] - 22, 350, 100]
CHIP = foto(c2, "chip_data")
CHIP4 = foto(c4, "chip_data")
DEZ = foto(c3, "dez")
SALDO = [24, foto(c5, "saldo_em")[1] - 8, 342, foto(c5, "meta_btn")[1] - foto(c5, "saldo_em")[1] - 2]
GRAF = foto(c5, "grafico")
PAR = foto(c5, "par")
SOBRA = foto(c5, "sobra")
META_BTN = foto(c5, "meta_btn")
CAMPO, OK = foto(c6, "campo"), foto(c6, "ok")
META = foto(c7, "meta_btn")

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.65
T1, T2, T3, T4, T5 = (2.9, 4.85), (5.05, 8.45), (8.7, 11.2), (11.45, 14.3), (14.55, 18.2)
TQ_BASE, TQ_CHIP, TQ_DEZ, TQ_META, TQ_OK = 4.45, 5.95, 7.25, 14.95, 16.45
X5 = 8.5           # troca para a foto do resultado (como quem rola a tela)
J_SAI = 18.25
FIM = 18.45
DUR = 21.2

IMGS = [("s1", os.path.join(TELAS, "celular-simulacao-1-cenarios.jpg")), ("s2", os.path.join(TELAS, "celular-simulacao-2-cenario.jpg")),
        ("s3", os.path.join(TELAS, "celular-simulacao-3-meses.jpg")), ("s4", os.path.join(TELAS, "celular-simulacao-4-dezembro.jpg")),
        ("s5", os.path.join(TELAS, "celular-simulacao-5-resultado.jpg")), ("s6", os.path.join(TELAS, "celular-simulacao-6-meta-0.jpg"))] + \
       [(f"d{i}", os.path.join(TELAS, f"celular-simulacao-6-meta-{i}.jpg")) for i in range(1, 6)] + \
       [("s7", os.path.join(TELAS, "celular-simulacao-7-meta-ok.jpg"))]
assert [C[f"digitado_{i}"] for i in range(1, 6)] == ["3", "35", "350", "3.500", "35.000"]
TECLAS = [15.55, 15.7, 15.85, 16.0, 16.15]
EXTRA = K.aneis("aBase", "aChip", "aDez", "aChip4", "aSaldo", "aGraf", "aPar", "aSobra", "aCampo", "aMeta") + \
        K.toques("tqBase", "tqChip", "tqDez", "tqMeta", "tqOk")

# ---------------------------------------------------------------- gancho: a curva do saldo até dez/27
GX0, GX1, GY0, GY1, V0, V1 = 130, 950, 1410, 830, 12000, 40000
def gx(i): return GX0 + (GX1 - GX0) * i / 13
def gy(v): return GY1 + (GY0 - GY1) * (V1 - v) / (V1 - V0)
pts = [(gx(i), gy(v)) for i, v in enumerate(SERIE)]
caminho = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
grade = "".join(f'<line x1="{GX0}" x2="{GX1}" y1="{gy(v):.1f}" y2="{gy(v):.1f}" stroke="#2A332B" stroke-width="3" stroke-dasharray="10 12"/>'
                f'<text x="{GX0 - 20}" y="{gy(v) + 10:.1f}" text-anchor="end" font-family="Inter" font-weight="600" font-size="27" fill="{K.DARK_TEXTO}">{v // 1000} mil</text>'
                for v in (20000, 30000))
rotx = "".join(f'<text x="{gx(i):.1f}" y="{GY0 + 58}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="27" fill="{K.DARK_TEXTO}">{r}</text>'
               for i, r in enumerate(ROT) if i in (0, 2, 5, 8, 11, 13))

CSS = f"""
#g{{background:{A.INK}}}
#gTop{{position:absolute;left:90px;top:330px;width:900px}}
#gTop .h1{{font-size:112px;margin-top:30px;color:#fff}}
#gTop .h1 b{{color:{A.MENTA};font-weight:700}}
#graf{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
#gVal{{position:absolute;left:0;top:0;white-space:nowrap;font-size:60px;font-weight:700;letter-spacing:-.045em;color:{A.MENTA};font-variant-numeric:tabular-nums}}
#gMes{{position:absolute;left:0;top:0;white-space:nowrap;font-size:28px;font-weight:700;letter-spacing:.06em;color:#fff;text-transform:uppercase}}
.tit{{font-size:66px}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Na Simulação futura, abra o seu <b>cenário</b>.</div>
  <div class="tit" id="t2">Leve o plano até <b>dezembro de 2027</b>.</div>
  <div class="tit" id="t3">No plano, 2027 termina com <b>R$&nbsp;37.720</b>.</div>
  <div class="tit" id="t4">E a realidade? Sobrou <b>R$&nbsp;284 por mês</b> a mais que o plano.</div>
  <div class="tit" id="t5">Uma meta de <b>R$&nbsp;35 mil</b>: no plano, chega em nov/27.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>
</div>

<div class="cena tinta" id="g">
  <div id="gTop">
    <div class="eyebrow">Simulação futura</div>
    <div class="h1">Como termina o seu <b>2027</b>?</div>
  </div>
  <svg id="graf" viewBox="0 0 1080 1920">
    {grade}{rotx}
    <path id="gLinha" d="{caminho}" fill="none" stroke="{A.MENTA}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <circle id="gPonto" r="17" fill="{A.MENTA}" stroke="{A.INK}" stroke-width="6"/>
  </svg>
  <div id="gVal">R$ 14.180</div>
  <div id="gMes">hoje</div>
</div>

{K.fim("Simulação futura no timtimcash")}
"""

JS = f"""
const SERIE = {json.dumps(SERIE)}, ROT = {json.dumps(ROT)}, PTS = {json.dumps([[round(x, 1), round(y, 1)] for x, y in pts])};
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)};
const TQ_BASE={TQ_BASE}, TQ_CHIP={TQ_CHIP}, TQ_DEZ={TQ_DEZ}, TQ_META={TQ_META}, TQ_OK={TQ_OK}, X5={X5}, J_SAI={J_SAI}, FIM={FIM}, TECLAS={TECLAS};
poeAnel('aBase', {BASE_CARD}, 6); poeToque('tqBase', ...{centro(BASE_CARD)});
poeAnel('aChip', {CHIP}, 8); poeToque('tqChip', ...{centro(CHIP)});
poeAnel('aDez', {DEZ}, 8); poeToque('tqDez', ...{centro(DEZ)});
poeAnel('aChip4', {CHIP4}, 8);
poeAnel('aSaldo', {SALDO}, 8); poeAnel('aGraf', {GRAF}, 8); poeAnel('aPar', {PAR}, 10); poeAnel('aSobra', {SOBRA}, 10);
poeToque('tqMeta', ...{centro(META_BTN)}); poeAnel('aCampo', {CAMPO}, 8); poeToque('tqOk', ...{centro(OK)});
poeAnel('aMeta', {META}, 8);
const L = $('gLinha').getTotalLength();
// câmera (px CSS da foto no centro da janela)
const CAM = [[0,0,195,250,1], [6.0,6.35,195,{DEZ[1] - 60:.1f},1], [7.35,7.7,195,250,1], [11.2,11.75,195,{PAR[1] + 80:.1f},1],
             [14.35,14.75,195,250,1], [15.05,15.4,195,{(CAMPO[1] + OK[1]) / 2 + 10:.1f},1], [16.65,17.0,195,250,1]];
function render(t){{
  // 1. gancho: a curva do saldo, mês a mês, até dez/27
  const p = prog(t, -0.25, 2.05), d = L*p;
  const lin_ = $('gLinha'); lin_.style.strokeDasharray = L + ' ' + L; lin_.style.strokeDashoffset = (L - d).toFixed(1);
  const q = lin_.getPointAtLength(Math.max(.01, d));
  $('gPonto').setAttribute('cx', q.x.toFixed(1)); $('gPonto').setAttribute('cy', q.y.toFixed(1));
  // valor na ponta: interpolado entre os meses da linha do tempo do site
  let k = 0; while (k < 13 && PTS[k+1][0] <= q.x) k++;
  const f = k < 13 ? clamp((q.x - PTS[k][0]) / (PTS[k+1][0] - PTS[k][0]), 0, 1) : 0;
  const v = k < 13 ? SERIE[k] + (SERIE[k+1] - SERIE[k]) * f : SERIE[13];
  const fim = p >= 1;
  $('gVal').textContent = 'R$ ' + fmt(SERIE[k], 0);
  $('gMes').textContent = k === 13 ? 'em dez/27' : ROT[k];
  const lx = Math.min(q.x - 20, 1000 - $('gVal').offsetWidth);
  $('gVal').style.transform = `translate(${{lx.toFixed(1)}}px, ${{(q.y - 118).toFixed(1)}}px)`;
  $('gMes').style.transform = `translate(${{lx.toFixed(1)}}px, ${{(q.y - 150).toFixed(1)}}px)`;
  saiCima('g', t, G_SAI);

  // 2. a tela real
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, G_SAI+.15, J_SAI);
  const ne = prog(t, G_SAI+.15, G_SAI+.75);
  $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  op('s2', t >= TQ_BASE+.15 ? 1 : 0); op('s3', prog(t, TQ_CHIP+.15, TQ_CHIP+.3)); op('s4', prog(t, TQ_DEZ+.15, TQ_DEZ+.3));
  op('s5', prog(t, X5, X5+.25)); op('s6', prog(t, TQ_META+.15, TQ_META+.3));
  TECLAS.forEach((a, i) => op('d'+(i+1), t >= a ? 1 : 0)); op('s7', t >= TQ_OK+.15 ? 1 : 0);   // a janela da meta fecha na hora
  anel('aBase', t, 3.25, 4.3); toque('tqBase', t, TQ_BASE);
  anel('aChip', t, 5.25, 5.85); toque('tqChip', t, TQ_CHIP);
  anel('aDez', t, 6.5, 7.15); toque('tqDez', t, TQ_DEZ);
  anel('aChip4', t, 7.75, 8.4);
  anel('aSaldo', t, 8.95, 10.0); anel('aGraf', t, 10.1, 11.1);
  anel('aPar', t, 11.9, 13.0); anel('aSobra', t, 13.1, 14.2);
  toque('tqMeta', t, TQ_META); anel('aCampo', t, 15.45, 16.3); toque('tqOk', t, TQ_OK);
  if (t >= TQ_OK+.2){{ $('t_tqOk').style.opacity = 0; $('o_tqOk').style.opacity = 0; }}   // o toque some quando a janela fecha
  anel('aMeta', t, 17.0, 18.1);

  // 3. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Simulação futura</div>
    <div class="h1" style="font-size:112px;line-height:.98;margin-top:34px;text-wrap:balance">2027 começa com um plano</div>
  </div>
  <div class="ano">2027</div>
  <svg style="position:absolute;left:0;top:0;overflow:visible" width="1080" height="1920" viewBox="0 0 1080 1920">
    <line x1="90" x2="990" y1="1090" y2="1090" stroke="#fff" stroke-width="5" stroke-dasharray="14 16" stroke-linecap="round"/>
    <path d="M90 1520 C 300 1500, 380 1390, 520 1330 S 800 1180, 940 1060" fill="none" stroke="#fff" stroke-width="16" stroke-linecap="round"/>
    <circle cx="940" cy="1060" r="26" fill="#fff"/>
  </svg>"""
    css = """.ano{position:absolute;left:0;top:1120px;width:1080px;text-align:center;font-size:330px;line-height:1;font-weight:700;letter-spacing:-.06em;
      color:transparent;-webkit-text-stroke:5px #fff;font-variant-numeric:tabular-nums}"""
    return K.pagina_capa(corpo, css, fundo="verde")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
