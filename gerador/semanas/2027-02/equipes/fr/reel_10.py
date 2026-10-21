# -*- coding: utf-8 -*-
"""Reel de 10/02/2027 (quarta) · "Quanto custou o seu Carnaval?" · capa tinta · equipe fr. Segundo da dupla com o de 05/02
("Carnaval com envelope"): o mesmo envelope desenhado, agora depois da folia (de R$ 500 sobram R$ 45,20).

Telas reais: captura_10.py, build 2026-10-19.5, conta de base (J/base_app, sem mudança), celular 390 px CSS em escala 3,
relógio da página em 10/02/2027 10:00:
- Transações (Fevereiro 2027): toque na busca e "carnaval" digitado letra a letra (uma foto real depois de cada letra). O resumo
  muda a cada letra: 21 transações (antes) -> "c" 17 -> "ca" 11 -> "car" 5; com "carnaval": "5 transações · 5 pagas ·
  0 pendentes · somam R$ 454,80 · 815 no histórico". As 5 linhas saem da "Carteira do Carnaval";
- "Contas e carteiras" (pelo menu): "Carteira do Carnaval", R$ 45,20.
Os 5 gastos (descrições com "Carnaval", de 04 a 09/02): fantasia 89,90 (04/02), ingresso da festa 180,00 (06/02), comida 64,50
(07/02), transporte 72,40 (08/02), lanche no bloco 48,00 (09/02) = 454,80. Envelope: 500,00 − 454,80 = 45,20.
Diferença do Reel de 04/11 (busca e soma da farmácia): aqui a história é o envelope; a digitação aparece em teclas (no gancho) e
numa tecla que salta sobre cada letra da busca real, com a lista encolhendo de 21 para 5 lançamentos.

python3 reel_10.py  |  REEL_PREVIA="0 0.4 1 2 3.6 4.3 5.8 8 10.6 13 14.4 16.5" python3 reel_10.py
"""
import os, sys, json
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro, brl
import envelope as EV

PASTA = "2027-02-10_reel-quanto-custou-o-carnaval"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("10")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- números (conferidos contra a tela)
GASTOS = [("04/02", "Fantasia", "89.90"), ("06/02", "Ingresso da festa", "180.00"), ("07/02", "Comida", "64.50"),
          ("08/02", "Transporte", "72.40"), ("09/02", "Lanche no bloco", "48.00")]
TOTAL = sum(D(v) for _, _, v in GASTOS)
assert TOTAL == D("454.80")
ENVELOPE = D("500.00")
SOBRA = ENVELOPE - TOTAL
assert SOBRA == D("45.20")
ARQ = C["arquivos"]
assert len(ARQ) == 8 and C[ARQ[-1]]["valor"] == "carnaval"
RES = [C[a]["trechos"]["texto"] for a in ARQ]
assert RES[0].startswith("17 transações") and RES[1].startswith("11 transações") and RES[2].startswith("5 transações")
assert all(r == "5 transações · 5 pagas · 0 pendentes · somam R$ 454,80 · 815 no histórico" for r in RES[2:]), RES
assert C["trechos_alta"]["texto"] == RES[-1]
assert "21 transações · 17 pagas · 4 pendentes · 815 no histórico" in C["celular-transacoes-busca-tocada.png"]["texto"]
LIN = C["linhas"]
NOMES = ["Lanche no bloco de Carnaval", "Transporte no Carnaval", "Comida no Carnaval", "Ingresso de festa de Carnaval", "Fantasia de Carnaval"]
VALS = ["48,00", "72,40", "64,50", "180,00", "89,90"]
for l, n, v in zip(LIN, NOMES, VALS):
    assert l[0].startswith("Editar Excluir " + n) and "· Carteira do Carnaval" in l[0] and l[0].endswith(f"−R$ {v} paga"), l
assert any(l[0] == "Carteira do Carnaval Dinheiro / Carteira · No total R$ 45,20" for l in C["linhas_contas"])

# ---------------------------------------------------------------- caixas (px CSS do celular)
BUSCA0 = C["celular-transacoes-busca-tocada.png"]["caixas"]["busca"]
TOQUE = centro(BUSCA0)
CURSOR = [C[a]["cursor"]["x_ultima"] for a in ARQ]          # centro da última letra digitada
CAMPO_Y = C[ARQ[0]]["cursor"]["campo"][1]                     # topo do campo depois da 1ª letra
T8 = C["trechos_alta"]                                      # o resumo com "carnaval" (mesmo lugar na foto alta e na 8ª letra)
RES_BOX = uniao(*T8["5 transações"], *[b for k, v in T8.items() if k.startswith("somam") for b in v])
CONTAS_LIN = [c[1:] for c in C["contas_nas_linhas"] if c[1] > 0]
assert len(CONTAS_LIN) == 5
CART = [l for l in C["linhas_contas"] if l[0].startswith("Carteira do Carnaval")][0][1:]
LETRAS = "carnaval"

# ---------------------------------------------------------------- tempos (s)
SOBE = 2.75
T1, T2, T3, T4 = (2.9, 4.95), (5.1, 7.1), (7.25, 9.45), (9.6, 11.8)
TQ = 3.35
LT = [round(3.75 + 0.13 * k, 2) for k in range(8)]          # uma letra (e uma foto real) a cada 0,13 s
ALTA = 7.2                                                    # a mesma tela, alta, para descer até as 5 linhas
J_SAI = 11.8
T5 = 12.0
FIM = 15.05
DUR = 17.9

IMGS = ([("s0", tela("celular-transacoes-fevereiro.png")), ("s0f", tela("celular-transacoes-busca-tocada.png"))]
        + [(f"s{k + 1}", tela(a)) for k, a in enumerate(ARQ)]
        + [("sAlta", tela("celular-transacoes-busca-carnaval-alta.png")), ("sContas", tela("celular-contas-e-carteiras.png"))])
IDS = [i for i, _ in IMGS]
TROCAS = [0, TQ + .12] + [a + .02 for a in LT] + [ALTA, T4[0] - .05]

TECLA_POP = "".join(f'<div class="kp" id="kp{k}"><span>{ch}</span></div>' for k, ch in enumerate(LETRAS))
EXTRA = K.aneis("aRes", "aCart", *[f"aC{k}" for k in range(5)]) + K.toques("tqBusca") + TECLA_POP

# ---------------------------------------------------------------- gancho: teclas, o total e o recibo da folia
TECLAS = "".join(f'<div class="tk" id="tk{k}"><span>{ch}</span></div>' for k, ch in enumerate(LETRAS))
RECIBO = "".join(f'<div class="rl" id="rl{k}"><i>{d}</i><span>{n}</span><b>{brl(D(v))}</b></div>' for k, (d, n, v) in enumerate(GASTOS))
VALORES = [float(v) for _, _, v in GASTOS]

# ---------------------------------------------------------------- fecho: o envelope (o mesmo de 05/02)
EW, ET = 520, 14
EH = round(EW * 0.66)
EX, EY = (1080 - EW) // 2, 900
CHIPS = "".join(f'<div class="ch" id="ch{k}"><span>−R$ {brl(D(v))}</span></div>' for k, (_, _, v) in enumerate(GASTOS))
ROT = (f'<div style="display:inline-flex;align-items:baseline;gap:12px;color:{A.BRAND_DARK};font-weight:700;letter-spacing:-.045em;'
       f'font-variant-numeric:tabular-nums"><small style="font-size:44px;font-weight:600;letter-spacing:-.01em">R$</small>'
       f'<span id="rotF" style="font-size:96px;line-height:1">500,00</span></div>')
ENV = EV.html("f", EW, A.BRAND, ET, A.BG, EX, EY, CHIPS, ROT)
# destino de cada pedacinho que sai do envelope (canto de cima, px do Reel)
DESTINO = [(100, 700), (236, 572), (420, 512), (592, 572), (742, 700)]

CSS = f"""
.tit{{font-size:64px}}
.janela{{background:#F7F6F1}}
/* gancho */
#g .eb{{position:absolute;left:90px;top:300px;color:{A.BRAND_DEEP}}}
#gQ{{position:absolute;left:90px;top:350px;width:900px;font-size:104px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#gQ span{{color:{A.BRAND_DEEP}}}
#tks{{position:absolute;left:0;top:598px;width:1080px;display:flex;justify-content:center;gap:14px}}
.tk{{width:92px;height:108px;border-radius:20px;background:#fff;border:3px solid #A7E9CB;border-bottom-width:10px;display:flex;align-items:center;
  justify-content:center;font-size:64px;font-weight:600;color:{A.INK};letter-spacing:-.02em;opacity:0;box-shadow:0 12px 24px -16px rgba(6,95,70,.45)}}
#gTot{{position:absolute;left:0;top:756px;width:1080px;text-align:center;color:{A.INK};font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums}}
#gTot small{{font-size:70px;font-weight:600;color:{A.MUTED};margin-right:22px;letter-spacing:-.01em}}
#gTot b{{font-size:184px;line-height:1;font-weight:700}}
#gSub{{position:absolute;left:90px;top:960px;width:900px;text-align:center;font-size:40px;font-weight:600;color:{A.BRAND_DEEP};letter-spacing:-.02em;opacity:0}}
#rec{{position:absolute;left:150px;top:1040px;width:780px;background:#fff;border-radius:32px;padding:18px 40px;box-shadow:0 22px 44px -26px rgba(6,95,70,.4)}}
.rl{{display:grid;grid-template-columns:110px 1fr auto;align-items:baseline;height:74px;line-height:74px;border-bottom:3px dashed {A.FIO};opacity:0;
  font-variant-numeric:tabular-nums}}
.rl:last-child{{border-bottom:0}}
.rl i{{font-style:normal;font-size:32px;font-weight:600;color:{A.MUTED}}}
.rl span{{font-size:40px;font-weight:600;color:{A.INK};letter-spacing:-.02em}}
.rl b{{font-size:42px;font-weight:700;color:{K.CORAL_TXT};letter-spacing:-.02em}}
/* tecla que salta sobre cada letra da busca real (px do Reel dentro da tela; a camada escala com a câmera) */
.kp{{position:absolute;width:64px;height:80px;margin-left:-32px;border-radius:14px;background:#fff;border:2px solid {A.NEUTRO};border-bottom-width:5px;
  display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:600;color:{A.INK};opacity:0;
  box-shadow:0 10px 18px -8px rgba(15,20,16,.35);transform-origin:50% 100%}}
/* fecho */
.ch{{position:absolute;left:0;top:0;opacity:0}}
.ch span{{display:inline-flex;align-items:baseline;background:#fff;border:3px solid {A.FIO};color:{K.CORAL_TXT};border-radius:999px;padding:12px 28px;
  font-size:46px;font-weight:700;letter-spacing:-.03em;font-variant-numeric:tabular-nums;box-shadow:0 16px 30px -18px rgba(15,20,16,.35)}}
#fConta{{position:absolute;left:90px;width:900px;text-align:center;font-size:40px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em;opacity:0}}
#fConta b{{color:{A.INK};font-weight:700}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em Transações, busque <b>“carnaval”</b>.</div>
  <div class="tit" id="t2"><b>5 gastos</b>, que somam <b>R$&nbsp;454,80</b>.</div>
  <div class="tit" id="t3">Todos pagos com a <b>Carteira do Carnaval</b>.</div>
  <div class="tit" id="t4">Na carteira, sobraram <b>R$&nbsp;45,20</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>

  <div class="tit" id="t5">O envelope <b>segurou</b> o Carnaval.</div>
  <div id="fecho" style="opacity:0">{ENV}</div>
  <div id="fConta" style="top:{EY + EH + 70}px">R$ 500 − R$ 454,80 = <b>R$ 45,20</b></div>
</div>

<div class="cena suave" id="g">
  <div class="eyebrow eb">Depois do Carnaval</div>
  <div id="gQ">Quanto custou o seu <span>Carnaval</span>?</div>
  <div id="tks">{TECLAS}</div>
  <div id="gTot"><small>R$</small><b id="gV">0,00</b></div>
  <div id="gSub">5 gastos com “carnaval”</div>
  <div id="rec">{RECIBO}</div>
</div>

{K.fim("Transações no timtimcash")}
"""

JS = EV.JS + f"""
const SOBE={SOBE}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, J_SAI={J_SAI}, T5={T5}, FIM={FIM};
const TQ={TQ}, LT={LT}, ALTA={ALTA}, IDS={json.dumps(IDS)}, TROCAS={TROCAS};
const CURSOR={CURSOR}, CAMPO_Y={CAMPO_Y}, VALORES={VALORES}, DESTINO={json.dumps(DESTINO)}, EX={EX}, EY={EY};
poeAnel('aRes', {RES_BOX}, 18); poeAnel('aCart', {CART}, 6);
{"".join(f"poeAnel('aC{k}', {b}, 10);" for k, b in enumerate(CONTAS_LIN))}
poeToque('tqBusca', {TOQUE[0]}, {TOQUE[1]});
for (let k=0;k<8;k++){{ const e = $('kp'+k); e.style.left = (CURSOR[k]*E)+'px'; e.style.top = ((CAMPO_Y - 47)*E)+'px'; }}
// câmera: o campo de busca e o resumo (zoom 1,1); as 5 linhas (zoom 0,88); Contas e carteiras
const CAM = [[0,0,195,515,1.15], [ALTA, ALTA+.85, 195, 1022, .88], [T4[0]-.06, T4[0]-.05, 195, 430, 1]];
function render(t){{
  // 1. gancho: as teclas de "carnaval", o recibo da folia e o total
  saiCima('g', t, SOBE);
  $('gQ').style.transform = `translateY(${{(-14*pout(t, -0.2, 1.3)).toFixed(1)}}px)`;
  for (let k=0;k<8;k++){{ const a = -0.35 + 0.07*k; const p = pback(t, a, a+.25); const e = $('tk'+k);
    e.style.opacity = lin(t, a, a+.08); const aperta = (t >= a+.04 && t < a+.16) ? 7 : 0;
    e.style.transform = `translateY(${{aperta}}px) scale(${{(.6+.4*p).toFixed(3)}})`; e.style.borderBottomWidth = (10 - aperta)+'px'; }}
  let soma = 0;
  for (let r=0;r<5;r++){{ const b = -0.3 + 0.13*r; const p = pout(t, b, b+.22); soma += VALORES[r]*p;
    $('rl'+r).style.opacity = p; $('rl'+r).style.transform = `translateX(${{((1-p)*-40).toFixed(1)}}px)`; }}
  $('gV').textContent = fmt(soma, 2);
  $('gTot').style.transform = `scale(${{(1 + 0.05*Math.sin(Math.PI*clamp((t-0.44)/0.3, 0, 1))).toFixed(4)}})`;
  $('gSub').style.opacity = prog(t, 0.45, 0.75);
  // 2. a tela real: toque na busca, uma letra por foto, a tecla que salta sobre a letra
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, SOBE+.1, J_SAI);
  const ne = prog(t, SOBE+.1, SOBE+.7);
  $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(IDS, t, TROCAS, 0);
  toque('tqBusca', t, TQ);
  for (let k=0;k<8;k++){{ const a = LT[k]; const e = $('kp'+k); const v = (t >= a-.02 && t < a+.24) ? 1 : 0;
    e.style.opacity = v * (1 - lin(t, a+.16, a+.24)); e.style.transform = `translateY(${{(-8*pout(t, a-.02, a+.08)).toFixed(1)}}px) scale(${{(.7 + .3*pback(t, a-.02, a+.1)).toFixed(3)}})`; }}
  anel('aRes', t, T2[0]+.25, T2[1]);
  for (let k=0;k<5;k++) anel('aC'+k, t, T3[0]+.75+k*.16, T3[1]);
  anel('aCart', t, T4[0]+.45, T4[1]);
  // 3. fecho: o mesmo envelope de 05/02; os 5 gastos saem dele e sobram R$ 45,20
  titulo('t5', t, T5, FIM+.4);
  const fo = prog(t, T5, T5+.35); $('fecho').style.opacity = fo; $('fecho').style.transform = `translateY(${{(1-fo)*60}}px)`;
  aba('f', 1);
  let resto = 500;
  for (let k=0;k<5;k++){{ const a = T5 + .45 + k*.22; const p = prog(t, a, a+.6); resto -= VALORES[k]*prog(t, a, a+.35);
    const e = $('ch'+k), [dx, dy] = DESTINO[k];
    e.style.opacity = lin(t, a, a+.12); e.style.left = (EX + 130 + (dx - EX - 130)*p) + 'px'; e.style.top = (EY + 120 + (dy - EY - 120)*p) + 'px'; }}
  $('rotF').textContent = fmt(Math.max(resto, 45.2), 2);
  $('fConta').style.opacity = prog(t, T5+1.75, T5+2.1);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    w, tr = 600, 16
    h = round(w * 0.66)
    x, y = (1080 - w) // 2, 1010
    corpo_svg, aba_svg, _, _ = EV.partes(w, A.MENTA, tr, A.INK)
    lab = (f'<div style="position:absolute;left:{x}px;top:{y + h * .56:.0f}px;width:{w}px;text-align:center;color:{A.MENTA};font-weight:700;'
           f'letter-spacing:-.045em;font-variant-numeric:tabular-nums"><small style="font-size:48px;font-weight:600;letter-spacing:-.01em;margin-right:14px;color:{K.DARK_TEXTO}">sobraram R$</small>'
           f'<span style="font-size:118px;line-height:1">45,20</span></div>')
    chips = "".join(f'<span style="position:absolute;left:{cx}px;top:{cy}px;display:inline-flex;background:#192019;border:3px solid #2E3830;color:{A.CORAL};'
                    f'border-radius:999px;padding:12px 28px;font-size:44px;font-weight:700;letter-spacing:-.03em;font-variant-numeric:tabular-nums">−{v}</span>'
                    for (cx, cy), v in zip([(118, 868), (640, 836), (372, 790)], ["89,90", "180,00", "64,50"]))
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:440px;width:900px">
    <div class="eyebrow">Carnaval</div>
    <div class="h1" style="font-size:124px;line-height:.96;margin-top:34px;color:#fff">Quanto custou <span style="color:{A.MENTA}">a folia?</span></div>
  </div>
  {chips}
  <div style="position:absolute;left:{x - tr}px;top:{y - tr}px">{corpo_svg}</div>
  <div style="position:absolute;left:{x - tr}px;top:{y - tr}px">{aba_svg}</div>
  {lab}"""
    return K.pagina_capa(corpo, "", fundo="tinta")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
