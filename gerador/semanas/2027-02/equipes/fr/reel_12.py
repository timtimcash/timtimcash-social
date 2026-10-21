# -*- coding: utf-8 -*-
"""Reel de 12/02/2027 (sexta) · "Tudo de lá fora, numa tela só" · capa verde · equipe fr.
Versão de 20/10/2026, depois da revisão (três ajustes): conta de base com o saldo de 31/12/2026 informado; câmera perto o bastante
para cada número em foco ter pelo menos 30 px de altura no vídeo; o indicador "IOF pago" fora de todos os quadros.

Telas reais: captura_12.py, build 2026-10-19.5, conta de base (J/base_app/estado.py; o estado de 12/02 gerado em
trabalho/12/estado_2027-02-12.js), computador 1440 x 900 em escala 3, relógio da página em 12/02/2027 10:00. Remessas ao exterior
(pelo menu lateral), no dólar: a página inteira (janela alta, 1440 x 2700), percorrida por uma câmera; no fim, um clique no botão
"EUR" troca a página para o euro (tela de 1440 x 900).
Números da tela (conferidos abaixo com assert): US$ 13.450 na carteira hoje, +US$ 1.450,00 (+12,1% em US$), +R$ 7.942,68
(+13,2% em R$); "De onde veio": +R$ 7.325 de rendimento e +R$ 618 de efeito do câmbio; equilíbrio R$ 4,461 (R$ 0);
ano a ano: 2023 +6,5% e +120,00 em US$, +3,8% e +R$ 343,68 em R$; 2024 +3,6% e +360,00, +34,4% e +R$ 16.928,73; 2025 +3,9% e
+480,00, −7,7% e −R$ 5.969,09; 2026 +3,2% e +420,00 em US$ e "falta o câmbio de 31/12" em reais (o saldo de 31/12/2026, US$ 13.380,
informado em 29/01/2027 sem câmbio, como ensina o post de 27/01); 3 remessas de US$ 4.000 (18/04/2024 a R$ 5,1000, 14/03/2024 a
R$ 5,0000 e 12/07/2023 a R$ 4,9000). Euro: € 2.018 na carteira hoje, +€ 18,00 (+0,9% em €), −R$ 105,13 (−0,9% em R$).
O câmbio "de hoje" da conta de exemplo é o salvo na carteira: as PTAX de compra de 15/10/2026 (dólar R$ 5,0515; euro R$ 5,6592).
Sem internet, o painel "Contra o CDI" não aparece e "Câmbio: onde você está" vem sem a linha do CDI: nada vazio entra no vídeo.
Legibilidade: nas duas tabelas (cada ano e cada remessa), a câmera fica a 2,75 e 2,5 px do Reel por px CSS e cada número em foco tem
pelo menos 30 px de altura (conferido abaixo com assert, pelo tamanho da letra medido na captura); o topo vai a 2,2 e o câmbio a 2,3; os anéis e o ponteiro ficam por cima da câmera, com traço
fixo. O painel com "IOF pago" (y de 1904 a 2018 px CSS) não aparece em nenhum quadro: a descida do gancho para antes dele, e as
passagens da tabela do ano a ano para a das remessas e de volta ao topo são cortes secos; a coluna IOF da tabela fica fora do recorte.

python3 reel_12.py  |  REEL_PREVIA="0 1.3 2.5 3.6 4.4 6 8 9.6 10.9 12.2 13.3 14.9 16.2 17.2 19" python3 reel_12.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro, cursores

PASTA = "2027-02-12_reel-tudo-de-la-fora-numa-tela"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("12")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)
TRACO = "\u2013"                       # o site mostra um traço onde não há valor

# ---------------------------------------------------------------- conferência com a tela
assert C["fechamentos"]["USD"]["2026"] == {"valor": 13380, "cambio": 0} and C["fechamentos"]["EUR"]["2026"] == {"valor": 2014, "cambio": 0}
TU = C["computador-remessas-dolar-pagina.png"]["texto"]
for k in ["US$13.450 na carteira hoje", "+US$ 1.450,00\n+12,1% em US$\n+R$ 7.942,68\n+13,2% em R$",
          "R$ 67.942,68 ao câmbio de hoje (R$ 5,0515)", "R$ 60.000\nvocê enviou\n+R$ 7.325\nrendimento\n+R$ 618\nefeito do câmbio\nR$ 67.943\nhoje",
          "No equilíbrio (R$ 4,461)\nR$ 0", "Câmbio: onde você está", "Rendimento ano a ano"]:
    assert k in TU, k
assert "CDI" not in TU and "Contra o" not in TU
ANO = {l[0].split(" ")[0]: l for l in C["linhas_ano"]}
assert ANO["2023"][0] == "2023 4.000,00 R$ 4,90 4.120,00 +6,5% +120,00 +3,8% +R$ 343,68"
assert ANO["2024"][0] == "2024 8.000,00 R$ 5,05 12.480,00 +3,6% +360,00 +34,4% +R$ 16.928,73"
assert ANO["2025"][0] == f"2025 {TRACO} {TRACO} 12.960,00 +3,9% +480,00 −7,7% −R$ 5.969,09"
assert ANO["2026"][0] == f"2026 {TRACO} {TRACO} 13.380,00 +3,2% +420,00 falta o câmbio de 31/12", ANO["2026"]
assert ANO["2027"][0].startswith("2027 até hoje") and ANO["2027"][0].endswith("falta o câmbio do ano anterior"), ANO["2027"]
TAB = [l for l in C["linhas_tabela"] if l[0][:2].isdigit()]
assert [l[0][:10] for l in TAB] == ["18/04/2024", "14/03/2024", "12/07/2023"] and all("US$ 4.000,00" in l[0] for l in TAB)
assert [l[0].split("US$ 4.000,00 ")[1][:9] for l in TAB] == ["R$ 5,1000", "R$ 5,0000", "R$ 4,9000"]
TE = C["computador-remessas-euro-tela.png"]["texto"]
assert "€2.018 na carteira hoje" in TE and "+€ 18,00\n+0,9% em €\n−R$ 105,13\n−0,9% em R$" in TE

# ---------------------------------------------------------------- caixas (px CSS da página, 1440 de largura)
CU = C["computador-remessas-dolar-pagina.png"]["caixas"]
PAIN = {p[0]: p[1:] for p in C["computador-remessas-dolar-pagina.png"]["paineis"]}
CUSTOS = PAIN["panel remx-custos"]                                   # o painel com "IOF pago": nunca no quadro
NUM = [337, 200, CU["na_carteira"][0] + CU["na_carteira"][2] - 337 + 4, 40]
PIL = uniao(CU["pilula_moeda"], CU["pilula_reais"])
LA, LT, LTOPO = C["letra_ano"], C["letra_tabela"], C["letra_topo"]
FRASE = CU["frase_de_onde"]                                         # a frase do site sob a cascata
EQUI = [1001, CU["equilibrio"][1] - 9, 376, 33]
ANOS = uniao(ANO["2023"][1:], ANO["2024"][1:], ANO["2025"][1:])
REM = uniao(*[l[1:] for l in TAB])
EUR = CU["eur"]
CE = C["computador-remessas-euro-tela.png"]["caixas"]
NUM_E = [337, 200, CE["na_carteira"][0] + CE["na_carteira"][2] - 337 + 4, 40]

# ---------------------------------------------------------------- tempos (s)
T1, T2, T3 = (2.75, 4.75), (4.9, 6.9), (7.05, 9.05)
T4 = (9.2, 12.8)                       # cada ano: ANO e as barras, deslize, EM US$ e EM R$
T5 = (13.0, 15.4)                      # cada remessa: DATA, deslize, ENVIADO e CÂMBIO EFETIVO
T6 = (15.6, 17.75)
CORTE5, CORTE6 = 12.945, 15.54         # cortes secos entre dois quadros (a 30 fps), para a câmera não passar pelo painel do IOF
CLIQUE = 16.45
FIM = 17.75
DUR = 20.6
JW, JH, JX, JY = 900, 920, 90, 680    # janela do computador no Reel

# câmera: (fx, fy) em px CSS no centro da janela e s em px do Reel por px CSS
HOOK0, HOOK1 = (720, 736, .625), (720, 1150, .625)
TOPO = (534.5, 232, 2.2)
CASC_C = (634, 578, 1.45)                # o painel inteiro, com a frase do site (como na versão aprovada)
CAMB_C = (1189, 592, 2.3)
ANO_A, ANO_B = (494, 1512, 2.75), (1270, 1512, 2.75)
REM_A, REM_B = (519, 2324, 2.5), (738, 2324, 2.5)


def vista(c):
    fx, fy, s = c
    return [fx - JW / 2 / s, fy - JH / 2 / s, JW / s, JH / s]


def dentro(caixa, v, folga=0):
    return caixa[0] >= v[0] - folga and caixa[1] >= v[1] - folga and caixa[0] + caixa[2] <= v[0] + v[2] + folga and caixa[1] + caixa[3] <= v[1] + v[3] + folga


def fora(caixa, v):
    return caixa[0] >= v[0] + v[2] or caixa[0] + caixa[2] <= v[0] or caixa[1] >= v[1] + v[3] or caixa[1] + caixa[3] <= v[1]


# o painel com "IOF pago" fica fora de todas as paradas e das duas pontas da descida do gancho
for c in [HOOK0, HOOK1, TOPO, CASC_C, CAMB_C, ANO_A, ANO_B, REM_A, REM_B]:
    assert fora(CUSTOS, vista(c)), (c, vista(c))
# na tabela das remessas, a coluna IOF (texto a partir de x = 923) fica fora do recorte
assert vista(REM_B)[0] + vista(REM_B)[2] <= 920
assert vista(ANO_A)[1] <= C["letra_ano"]["Rendimento ano a ano"][1] and vista(ANO_A)[1] + vista(ANO_A)[3] <= ANO["2027"][2] + 1
for corte in (CORTE5, CORTE6):
    assert all(not (corte < k / 30 < corte + .01) for k in range(int(DUR * 30) + 1)), corte
# cada número em foco com pelo menos 30 px de altura (tamanho da letra × zoom) e dentro do quadro
FOCO = [("US$13.450", LTOPO, TOPO), ("+US$ 1.450,00", None, TOPO), ("+R$ 7.942,68", None, TOPO),
        ("2023", LA, ANO_A), ("2024", LA, ANO_A), ("2025", LA, ANO_A),
        ("+120,00", LA, ANO_B), ("+R$ 343,68", LA, ANO_B), ("+R$ 16.928,73", LA, ANO_B), ("−R$ 5.969,09", LA, ANO_B),
        ("18/04/2024", LT, REM_A), ("14/03/2024", LT, REM_A), ("12/07/2023", LT, REM_A),
        ("US$ 4.000,00", LT, REM_B), ("R$ 5,1000", LT, REM_B), ("R$ 4,9000", LT, REM_B)]
for alvo, fonte, cam in FOCO:
    if fonte is None:
        continue
    cx = fonte[alvo]
    assert cx[4] * cam[2] >= 30, (alvo, cx[4], cam[2])
    assert dentro(cx[:4], vista(cam), 2) or alvo.startswith(("+", "−")), (alvo, cx, vista(cam))
# as pílulas do topo: letra de 12 px (valor) e 11 px (porcentagem), no zoom 2,2: 26,4 e 24,2 px; as porcentagens do ano a ano
# (13 px) e os valores (11 px) no zoom 2,75: 35,8 e 30,3 px; datas (12 px) e câmbios (13 px) das remessas no zoom 2,5: 30 e 32,5 px
assert 13 * ANO_B[2] >= 30 and 11 * ANO_B[2] >= 30 and 12 * REM_A[2] >= 30 and 13 * REM_B[2] >= 30
# (a cascata fica no zoom da versão aprovada, 1,45: frase de 13 px com 18,9 px; o equilíbrio, 12 px, no zoom 2,3: 27,6 px)
assert round(12 * CAMB_C[2], 2) >= 27.6 and dentro([997, 570, 384, 41], vista(CAMB_C)) and dentro([332, 705, 604, 72], vista(CASC_C))

IMGS = [("dU", tela("computador-remessas-dolar-pagina.png")), ("dE", tela("computador-remessas-euro-tela.png"))]
SOBRE = K.aneis("aNum", "aPil", "aFrase", "aEqui", "aAnos", "aRem", "aNumE") + cursores("cur")

CSS = f"""
.tit{{font-size:64px}}
.nota{{top:{JY - 42}px;left:{JX + 4}px}}
.janela{{left:{JX}px;top:{JY}px;width:{JW}px;height:{JH}px;border-radius:30px;background:#F7F6F1;border:2px solid #2A332C;
  box-shadow:0 0 0 10px #192019,0 40px 80px -30px rgba(0,0,0,.7)}}
.tela{{width:1440px}}
.tela img{{width:1440px}}
#hEb{{position:absolute;left:90px;top:286px}}
#hT{{position:absolute;left:90px;top:330px;width:900px;font-size:100px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#hT span{{color:{A.MENTA}}}
#hP{{position:absolute;left:90px;top:546px;display:flex;gap:22px}}
.pm{{display:inline-flex;align-items:baseline;gap:12px;height:76px;padding:0 30px;border-radius:999px;font-size:48px;font-weight:700;letter-spacing:-.04em;
  font-variant-numeric:tabular-nums;line-height:76px}}
"""

CORPO = f"""
<div class="cena tinta" id="tl">
  <div class="eyebrow" id="hEb">Remessas ao exterior</div>
  <div id="hT">Tudo de lá fora, <span>numa tela só.</span></div>
  <div id="hP"><span class="pm" id="pU" style="background:{A.BRAND};color:#fff">US$ 13.450</span>
    <span class="pm" id="pE" style="background:#fff;color:{A.INK}">€ 2.018</span></div>
  <div class="tit" id="t1">Quanto tem e quanto rendeu: <b>na moeda e em reais</b>.</div>
  <div class="tit" id="t2">De onde veio: <b>rendimento</b> e <b>câmbio</b>.</div>
  <div class="tit" id="t3">O câmbio que zera o resultado: <b>R$&nbsp;4,461</b>.</div>
  <div class="tit" id="t4">Cada ano, em <b>dólar</b> e em <b>reais</b>.</div>
  <div class="tit" id="t5">E cada remessa, com o <b>câmbio que pagou</b>.</div>
  <div class="tit" id="t6">O euro também, <b>num clique</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela" style="opacity:1">{camadas("tela", IMGS, "", largura=1440)}{SOBRE}</div>
</div>

{K.fim("Remessas ao exterior no timtimcash")}
"""

def kf(a, b, c):
    return [a, b, c[0], c[1], c[2]]


CAM = [[0, 0, *HOOK0], kf(0.15, 2.45, HOOK1), kf(T1[0] - .2, T1[0] + .45, TOPO), kf(T2[0] - .1, T2[0] + .5, CASC_C),
       kf(T3[0] - .1, T3[0] + .5, CAMB_C), kf(T4[0] - .1, T4[0] + .55, ANO_A), kf(10.2, 11.6, ANO_B),
       kf(CORTE5, CORTE5 + .01, REM_A), kf(13.55, 14.5, REM_B), kf(CORTE6, CORTE6 + .01, TOPO)]

JS = f"""
const T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, T6={list(T6)}, CLIQUE={CLIQUE}, FIM={FIM};
const JW={JW}, JH={JH};
const CAM = {json.dumps(CAM)};
const NUM={NUM}, PIL={PIL}, FRASE={FRASE}, EQUI={EQUI}, ANOS={ANOS}, REM={REM}, NUM_E={NUM_E};
const P0=[760, 330], P1=[{EUR[0] + EUR[2] / 2:.1f}, {EUR[1] + EUR[3] / 2 + 4:.1f}];
function render(t){{
  // 1. gancho: a frase, os dois valores e a câmera que desce pela página (até antes do painel do IOF)
  const hs = prog(t, 2.45, 2.8);
  ['hEb','hT','hP'].forEach(id => {{ $(id).style.opacity = 1 - hs; $(id).style.transform = `translateY(${{(-30*hs).toFixed(1)}}px)`; }});
  const pu = pback(t, -0.25, 0.3), pe = pback(t, -0.05, 0.5);
  $('pU').style.transform = `scale(${{(.6+.4*pu).toFixed(3)}})`; $('pU').style.opacity = lin(t, -0.25, -0.1);
  $('pE').style.transform = `scale(${{(.6+.4*pe).toFixed(3)}})`; $('pE').style.opacity = lin(t, -0.05, 0.1);
  // 2. as paradas: a câmera chega perto; os anéis e o ponteiro ficam por cima, com traço fixo
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]); titulo('t6', t, T6[0], FIM+.4);
  $('nota').style.opacity = 1;
  const cam = cameraD('tela', t, CAM, JW, JH);
  op('dE', t >= CLIQUE + .1 ? 1 : 0);
  const A = (id, r, a, b, pad) => {{ anelCam(id, r, cam, pad, JW, JH, cam[2]); anel(id, t, a, b); }};
  A('aNum', NUM, T1[0]+.5, T1[0]+1.15, 10); A('aPil', PIL, T1[0]+1.15, T1[1], 10);
  A('aFrase', FRASE, T2[0]+.55, T2[1], 10); A('aEqui', EQUI, T3[0]+.55, T3[1], 8);
  A('aAnos', ANOS, T4[0]+.6, T4[1], 20); A('aRem', REM, T5[0]+.35, T5[1], 16);
  A('aNumE', NUM_E, CLIQUE+.35, FIM, 10);
  cursorCam('cur', t, P0, P1, T6[0]+.25, CLIQUE-.1, CLIQUE, cam, JW, JH, cam[2], CLIQUE+.7);
  // 3. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    tr = 16
    # computador desenhado em traço (tela, base e pé) com quatro ícones de traço: barras, câmbio, trajetória e tabela
    icones = f"""
    <g fill="none" stroke="#fff" stroke-width="13" stroke-linecap="round" stroke-linejoin="round">
      <path d="M112 300 V236 M162 300 V196 M212 300 V252"/>
      <path d="M332 286 C 372 286, 380 210, 420 210 S 470 250, 500 236"/><circle cx="500" cy="236" r="12" fill="#fff"/>
      <path d="M112 452 H 152 V 412 H 192 V 372 H 232"/><path d="M110 452 L 236 362" stroke-dasharray="2 22"/>
      <rect x="320" y="364" width="196" height="96" rx="14"/><path d="M320 396 H 516 M320 428 H 516 M384 364 V 460"/>
    </g>"""
    monitor = f"""<svg width="660" height="620" viewBox="0 0 660 620" style="display:block;overflow:visible">
      <rect x="20" y="20" width="620" height="440" rx="34" fill="none" stroke="#fff" stroke-width="{tr}"/>
      <path d="M262 470 L 246 560 H 414 L 398 470" fill="none" stroke="#fff" stroke-width="{tr}" stroke-linejoin="round"/>
      <path d="M200 566 H 460" stroke="#fff" stroke-width="{tr}" stroke-linecap="round"/>
      <g transform="translate(0,-110)">{icones}</g>
    </svg>"""
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:440px;width:900px">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1" style="font-size:118px;line-height:.96;margin-top:34px;color:#fff">Tudo de lá fora, numa tela só.</div>
  </div>
  <div style="position:absolute;left:{(1080 - 660) // 2}px;top:930px">{monitor}</div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
