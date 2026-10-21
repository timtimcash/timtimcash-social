# -*- coding: utf-8 -*-
"""Reel de 05/02/2027 (sexta) · "O envelope do Carnaval" · capa verde · equipe fr. Primeiro da dupla com o de 10/02
("Quanto custou o seu Carnaval?"): o mesmo envelope desenhado, antes (R$ 500 entram) e depois (sobram R$ 45,20).

Telas reais: captura_05.py, build 2026-10-19.5, conta de base (J/base_app, sem mudança: a conta "Carteira do Carnaval" e a
transferência de 04/02 já estão nela), celular 390 px CSS em escala 3, relógio da página em 05/02/2027 10:00:
- "Contas e carteiras" (pelo menu): "Carteira do Carnaval", Dinheiro / Carteira, No total, R$ 410,10;
- "Editar transação" da transferência "Dinheiro para a folia" (04/02): Transferência, R$ 500,00, "Já foi feita · Afeta o saldo
  das duas contas agora", De Conta corrente, Para Carteira do Carnaval (aberta só para mostrar, sem salvar);
- "Editar transação" da "Fantasia de Carnaval" (04/02): Despesa, R$ 89,90, Lazer e hobbies, "Pago via" Carteira do Carnaval;
- Transações filtradas pela conta: a fantasia (−R$ 89,90, paga) e a transferência (R$ 500,00); "Saldo acumulado" R$ 410,10.
Conta: 500,00 − 89,90 = 410,10.

python3 reel_05.py  |  REEL_PREVIA="0 0.4 1 2 3.8 6.2 8.6 11 13.4 16 19" python3 reel_05.py
"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro
import envelope as EV

PASTA = "2027-02-05_reel-o-envelope-do-carnaval"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("05")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- números (conferidos contra a tela)
ENVELOPE, FANTASIA = D("500.00"), D("89.90")
SOBRA = ENVELOPE - FANTASIA
assert SOBRA == D("410.10")
assert any(l[0] == "Carteira do Carnaval Dinheiro / Carteira · No total R$ 410,10" for l in C["linhas_contas"]), C["linhas_contas"]
LIN = C["linhas_carteira"]
assert LIN[0][0] == "Editar Excluir Fantasia de Carnaval Lazer e hobbies · Carteira do Carnaval −R$ 89,90 paga"
assert LIN[1][0] == "Editar Excluir Dinheiro para a folia Transf.Conta corrente → Carteira do Carnaval R$ 500,00"
_tx = C["celular-transacoes-so-carteira.png"]["texto"]
assert "Saldo acumulado\nR$\n410\n,10" in _tx and "2 transações · 2 pagas · 0 pendentes" in _tx
_tr = C["celular-editar-transferencia.png"]["texto"]
for k in ["Editar transação", "Transferência", "500,00", "Já foi feita", "Afeta o saldo das duas contas agora", "De\n", "Conta corrente",
          "Para\n", "Carteira do Carnaval"]:
    assert k in _tr, k
_fa = C["celular-editar-fantasia.png"]["texto"]
for k in ["Editar transação", "89,90", "Lazer e hobbies", "Pago via", "Carteira do Carnaval", "Já foi pago"]:
    assert k in _fa, k

# ---------------------------------------------------------------- caixas (px CSS do celular)
CART = [l for l in C["linhas_contas"] if l[0].startswith("Carteira do Carnaval")][0][1:]
F2 = C["celular-editar-transferencia.png"]["caixas"]
TAB_TRANSF = F2["transferencia"]
DE_PARA = uniao(F2["de_linha"], F2["para_linha"])
DE_PARA = [DE_PARA[0] + 8, DE_PARA[1] + 3, DE_PARA[2] - 16, DE_PARA[3] - 6]
FEITA = F2["feita_linha"]
FEITA = [FEITA[0] + 8, FEITA[1] + 3, FEITA[2] - 16, FEITA[3] - 6]
F3 = C["celular-editar-fantasia.png"]["caixas"]
PAGO_VIA = F3["pago_via_linha"]
PAGO_VIA = [PAGO_VIA[0] + 8, PAGO_VIA[1] + 3, PAGO_VIA[2] - 16, PAGO_VIA[3] - 6]
F4 = C["celular-transacoes-so-carteira.png"]["caixas"]
ROW_FANT, ROW_FOLIA = LIN[0][1:], LIN[1][1:]
SALDO = uniao(F4["saldo"], F4["saldo_int"], F4["saldo_cts"], F4["saldo_em"])

# ---------------------------------------------------------------- tempos (s)
SOBE = 2.75
T1, T2, T3, T4, T5 = (2.9, 5.2), (5.35, 7.55), (7.7, 9.9), (10.05, 12.25), (12.4, 14.8)
J_SAI = 14.8
T6 = 15.0
FIM = 17.75
DUR = 20.6

IMGS = [("p1", tela("celular-contas-e-carteiras.png")), ("p2", tela("celular-editar-transferencia.png")),
        ("p3", tela("celular-editar-fantasia.png")), ("p4", tela("celular-transacoes-so-carteira.png"))]
TROCAS = [0, T2[0] - .05, T4[0] - .05, T5[0] - .05]
EXTRA = K.aneis("aCart", "aTab", "aDePara", "aFeita", "aPago", "aRowF", "aRowT", "aSaldo")

# ---------------------------------------------------------------- envelope (gancho e fecho)
EW, ET = 520, 14                      # largura e traço do envelope
EH = round(EW * 0.66)
EX, EY = (1080 - EW) // 2, 1010       # canto de cima do corpo (gancho)
PILULA = (f'<div id="pil" style="position:absolute;left:0;width:1080px;top:0;text-align:center">'
          f'<span style="display:inline-flex;align-items:baseline;gap:18px;background:{A.BRAND};color:#fff;border-radius:999px;'
          f'padding:22px 56px;font-size:112px;font-weight:700;letter-spacing:-.045em;font-variant-numeric:tabular-nums;'
          f'box-shadow:0 26px 50px -26px rgba(15,20,16,.5)"><small style="font-size:56px;font-weight:600;letter-spacing:-.01em">R$</small>500</span></div>')
ROT_G = (f'<div style="display:inline-flex;align-items:baseline;gap:14px;color:{A.BRAND_DARK};font-weight:700;letter-spacing:-.045em;'
         f'font-variant-numeric:tabular-nums"><small style="font-size:46px;font-weight:600;letter-spacing:-.01em">R$</small>'
         f'<span id="rotV" style="font-size:104px;line-height:1">500</span></div>')
ENV_G = EV.html("e", EW, A.BRAND, ET, A.BG, EX, EY, PILULA, ROT_G)
EX2, EY2 = EX, 860                    # o mesmo envelope no fecho
CHIP = (f'<div id="chip" style="position:absolute;left:0;top:0;opacity:0"><span style="display:inline-flex;align-items:baseline;gap:12px;'
        f'background:#fff;border:3px solid {A.FIO};color:{K.CORAL_TXT};border-radius:999px;padding:16px 34px;font-size:52px;font-weight:700;'
        f'letter-spacing:-.03em;font-variant-numeric:tabular-nums;box-shadow:0 18px 36px -20px rgba(15,20,16,.35)">−R$ 89,90'
        f'<small style="font-size:34px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em">fantasia</small></span></div>')
ROT_F = (f'<div style="display:inline-flex;align-items:baseline;gap:12px;color:{A.BRAND_DARK};font-weight:700;letter-spacing:-.045em;'
         f'font-variant-numeric:tabular-nums"><small style="font-size:44px;font-weight:600;letter-spacing:-.01em">R$</small>'
         f'<span id="rotF" style="font-size:96px;line-height:1">500,00</span></div>')
ENV_F = EV.html("f", EW, A.BRAND, ET, A.BG, EX2, EY2, CHIP, ROT_F)

CSS = f"""
.tit{{font-size:64px}}
#gEb{{position:absolute;left:90px;top:300px}}
#gQ{{position:absolute;left:90px;top:350px;width:900px;font-size:100px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK};text-wrap:balance}}
#gQ span{{color:{A.BRAND_DARK}}}
.legEnv{{position:absolute;left:90px;width:900px;text-align:center;font-size:40px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em}}
#fConta{{position:absolute;left:90px;width:900px;text-align:center;font-size:40px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em;opacity:0}}
#fConta b{{color:{A.INK};font-weight:700}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Em Contas e carteiras, uma conta <b>só para a folia</b>.</div>
  <div class="tit" id="t2">Passe <b>R$&nbsp;500</b> para ela, com uma transferência.</div>
  <div class="tit" id="t3">Transferência não é gasto: o dinheiro <b>só muda de lugar</b>.</div>
  <div class="tit" id="t4">Cada gasto da folia sai <b>da carteira</b>.</div>
  <div class="tit" id="t5">Na carteira, sobram <b>R$&nbsp;410,10</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>

  <div class="tit" id="t6">Quando acabar, <b>acabou</b>.</div>
  <div id="fecho" style="opacity:0">{ENV_F}</div>
  <div id="fConta" style="top:{EY2 + EH + 70}px">R$ 500 − R$ 89,90 = <b>R$ 410,10</b></div>
</div>

<div class="cena papel" id="g">
  <div class="eyebrow" id="gEb">Antes do Carnaval</div>
  <div id="gQ">Carnaval com envelope: <span>quando acabar, acabou.</span></div>
  {ENV_G}
  <div class="legEnv" id="gLeg" style="top:{EY + EH + 60}px;opacity:0">Carteira do Carnaval</div>
</div>

{K.fim("Contas e carteiras no timtimcash")}
"""

JS = EV.JS + f"""
const SOBE={SOBE}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, J_SAI={J_SAI}, T6={T6}, FIM={FIM};
const TROCAS={TROCAS};
const EY={EY}, EH={EH}, EY2={EY2};
poeAnel('aCart', {CART}, 6); poeAnel('aTab', {TAB_TRANSF}, 8); poeAnel('aDePara', {DE_PARA}, 8); poeAnel('aFeita', {FEITA}, 8);
poeAnel('aPago', {PAGO_VIA}, 8); poeAnel('aRowF', {ROW_FANT}, 4); poeAnel('aRowT', {ROW_FOLIA}, 4); poeAnel('aSaldo', {SALDO}, 18);
// câmera: Contas e carteiras; as folhas de edição; a lista da carteira e o saldo
const CAM = [[0,0,195,430,1], [T2[0]-.06, T2[0]-.05, 195, 560, 1], [T5[0]-.06, T5[0]-.05, 195, 740, 1], [T5[0]+1.15, T5[0]+1.6, 195, 400, 1]];
function render(t){{
  // 1. gancho: R$ 500 entram no envelope, a aba fecha e o valor fica escrito nele
  saiCima('g', t, SOBE);
  $('gQ').style.transform = `translateY(${{(-14*pout(t, -0.2, 1.3)).toFixed(1)}}px)`;
  // a pílula chega por cima, para um instante sobre o envelope e desce para dentro dele
  $('pil').style.top = (EY - 420 + 150*pout(t, -0.3, 0.3) + 360*prog(t, 0.34, 0.68)) + 'px';
  aba('e', -1 + 2*prog(t, 0.66, 0.96));
  const r = pback(t, 0.68, 1.02); $('eRot').style.opacity = lin(t, .68, .8); $('eRot').style.transform = `scale(${{(.6+.4*r).toFixed(3)}})`;
  $('gLeg').style.opacity = prog(t, 1.05, 1.4);
  // 2. a tela real
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, SOBE+.1, J_SAI);
  const ne = prog(t, SOBE+.1, SOBE+.7);
  $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(['p1','p2','p3','p4'], t, TROCAS, .14);
  anel('aCart', t, T1[0]+.6, T1[1]);
  anel('aTab', t, T2[0]+.35, T2[0]+1.05); anel('aDePara', t, T2[0]+1.1, T2[1]);
  anel('aFeita', t, T3[0]+.35, T3[1]);
  anel('aPago', t, T4[0]+.35, T4[1]);
  anel('aRowF', t, T5[0]+.3, T5[0]+1.05); anel('aRowT', t, T5[0]+.3, T5[0]+1.05); anel('aSaldo', t, T5[0]+1.6, T5[1]);
  // 3. fecho: o mesmo envelope; a fantasia sai e o valor vai de R$ 500,00 a R$ 410,10
  titulo('t6', t, T6, FIM+.4);
  const fo = prog(t, T6, T6+.35); $('fecho').style.opacity = fo; $('fecho').style.transform = `translateY(${{(1-fo)*60}}px)`;
  aba('f', 1);
  const sai = prog(t, T6+.55, T6+1.35);
  $('chip').style.opacity = lin(t, T6+.5, T6+.65) * (1 - prog(t, T6+2.2, T6+2.5));
  $('chip').style.left = (330 + 170*sai) + 'px'; $('chip').style.top = (EY2 + 120 - 350*sai) + 'px';
  contar('rotF', t, T6+.6, T6+1.4, 500, 410.10, 2, '', '');
  $('fConta').style.opacity = prog(t, T6+1.3, T6+1.65);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    w, tr = 600, 16
    h = round(w * 0.66)
    x, y = (1080 - w) // 2, 1080
    corpo_svg, aba_svg, _, _ = EV.partes(w, "#fff", tr, A.BRAND)
    pil = (f'<span style="display:inline-flex;align-items:baseline;gap:20px;background:#fff;color:{A.BRAND_DARK};border-radius:999px;'
           f'padding:22px 58px;font-size:118px;font-weight:700;letter-spacing:-.045em;font-variant-numeric:tabular-nums;'
           f'box-shadow:0 26px 50px -26px rgba(15,20,16,.45)"><small style="font-size:58px;font-weight:600;letter-spacing:-.01em">R$</small>500</span>')
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:440px;width:900px">
    <div class="eyebrow">Carnaval</div>
    <div class="h1" style="font-size:124px;line-height:.96;margin-top:34px;color:#fff">O envelope da folia.</div>
  </div>
  <div style="position:absolute;left:{x - tr}px;top:{y - tr}px;transform-origin:{tr + w / 2}px {tr}px;transform:scaleY(-1)">{aba_svg}</div>
  <div style="position:absolute;left:0;top:{y - 150}px;width:1080px;text-align:center">{pil}</div>
  <div style="position:absolute;left:{x - tr}px;top:{y - tr}px">{corpo_svg}</div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
