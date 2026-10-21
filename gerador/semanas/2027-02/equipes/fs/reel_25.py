# -*- coding: utf-8 -*-
"""Reel de 25/02/2027 (quinta) · "Nova remessa: o câmbio na hora" · capa tinta · equipe fs.
(Trocou de dia com "Meta de receita", a pedido da revisão: este era o de 23/02.)

Telas reais: captura_25.py, build 2026-10-19.5, celular 390 × 1000 em escala 3, relógio da página em 25/02/2027 10:00, cópia da
conta (estado.py igual ao da base). A remessa NÃO é salva (no fim, "Cancelar"): nada muda na conta.
"Nova remessa" em dólar (Conta corrente -> Corretora no exterior, Estados Unidos) com valores de EXEMPLO, redondos, digitados tecla
a tecla: Valor (o total debitado) R$ 10.110,00, Enviado US$ 2.000,00 e IOF R$ 110,00 (o do comprovante). A linha do site muda a
cada tecla (com valores de passagem, como "R$ 505500,0000 por US$" com US$ 0,02) e termina em "Câmbio efetivo R$ 5,0550 por US$ ·
IOF 1,10% · US$ 2.000 custaram R$ 10.110,00". Revisão: ninguém deve ver os valores de passagem; depois do toque em Enviado e em IOF,
o vídeo corta direto para o valor final (as fotos tecla a tecla desses dois campos ficam fora do vídeo e da entrega, em
trabalho/fora_da_entrega_25/). O Valor, no topo,
é mostrado tecla a tecla, com a linha do câmbio fora do quadro.
Conta (feita aqui e conferida com assert): 10.110 ÷ 2.000 = 5,0550; 10.110 − 110 = 10.000 = 2.000 × 5,00; 110 ÷ 10.000 = 1,10%.
Post de exterior: nenhuma menção a preço do site. O vídeo diz que os valores são de exemplo.

python3 reel_25.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_25.py
"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, pop_html, anel_no_recorte, uniao, centro, folga, din

PASTA = "2027-02-25_reel-nova-remessa-cambio-na-hora"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("25")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- conferência com a tela e a conta
TOTAL, USD, IOF = D("10110.00"), D("2000.00"), D("110.00")
assert (TOTAL / USD).quantize(D("0.0001")) == D("5.0550")
assert TOTAL - IOF == D("10000.00") == USD * D("5.00")
assert (IOF / (TOTAL - IOF) * 100).quantize(D("0.01")) == D("1.10")
LINHA = "Câmbio efetivo R$ 5,0550 por US$ · IOF 1,10% · US$ 2.000 custaram R$ 10.110,00"
v7 = C["celular-remessa-7-pronta.jpg"]["valores"]
assert v7["valor"] == "10.110,00" and v7["enviado"] == "2.000,00" and v7["iof"] == "110,00" and v7["inst"] == "Corretora no exterior"
assert v7["deriva"].replace("\n", " ") == LINHA
assert "De\nConta corrente\nPara\nCorretora no exterior" in C["celular-remessa-2-dolar.jpg"]["texto"] and "Estados Unidos" in C["celular-remessa-2-dolar.jpg"]["texto"]
assert "Hoje 25/02" in C["celular-remessa-2-dolar.jpg"]["texto"] and "US$" in C["celular-remessa-2-dolar.jpg"]["texto"]
assert C["salvou"] == 4 and "Feb 25 2027" in C["relogio"]          # as 4 remessas da conta; a de exemplo não foi salva
ENV = [C[t[2]]["valores"]["deriva"].replace("\n", " ") for t in C["teclas"] if t[0] == "enviado"]
assert ENV[-1] == "Câmbio efetivo R$ 5,0550 por US$ · US$ 2.000 custaram R$ 10.110,00" and ENV[0].startswith("Câmbio efetivo R$ 505500,0000")
IOFS = [C[t[2]]["valores"]["deriva"].replace("\n", " ") for t in C["teclas"] if t[0] == "iof"]
assert IOFS[-1] == LINHA

# ---------------------------------------------------------------- caixas (px CSS do celular)
c2, c4, c7 = C["celular-remessa-2-dolar.jpg"], C["celular-remessa-4-embaixo.jpg"], C["celular-remessa-7-pronta.jpg"]
VALOR = c2["valor"]
VALOR7 = C["celular-remessa-3-valor-7.jpg"]["valor"]
ENVIADO, IOFC, DERIVA = c4["enviado"], c4["iof"], c7["deriva"]
L = c7["linhas"]
ENV_LINHA, IOF_LINHA = L["Enviado o que chegou lá fora US$"], L["IOF está no comprovante R$"]

# ---------------------------------------------------------------- tempos (s)
H_SAI = 2.8
T1, T2, T3 = (3.0, 5.55), (5.7, 8.55), (8.7, 11.0)
TQ_VALOR = 3.55
TV = [round(3.75 + .12 * k, 2) for k in range(7)]
CAM_DESCE = (5.6, 6.1)
TQ_ENV = 6.35
TE = [round(6.55 + .14 * k, 2) for k in range(6)]
TQ_IOF = 9.0
TI = [round(9.2 + .14 * k, 2) for k in range(5)]
J_SAI = 11.0
S4 = 11.0
T4 = (11.2, 14.55)
S5 = 14.75
FIM = 17.15
DUR = 19.95

IMGS = [("i2", tela("celular-remessa-2-dolar.jpg"))] + [(f"v{k}", tela(f"celular-remessa-3-valor-{k}.jpg")) for k in range(1, 8)] + \
       [("i4", tela("celular-remessa-4-embaixo.jpg")), ("e6", tela("celular-remessa-5-enviado-6.jpg")), ("o5", tela("celular-remessa-6-iof-5.jpg"))]
TR = [0] + TV + [CAM_DESCE[0], TQ_ENV + .25, TQ_IOF + .25]      # Enviado e IOF: direto para o valor final
IDS = [i for i, _ in IMGS]
EXTRA = K.aneis("aValor", "aDer1", "aDer2") + K.toques("tqValor", "tqEnv", "tqIof")

# recorte da linha do câmbio (foto final), grande, na cena de papel
R_POP = [10, DERIVA[1] - 6, 370, DERIVA[3] + 12]
P_POP = [90, 560, 900]

CSS = f"""
.tit{{font-size:64px}}
/* gancho */
#g .eyebrow{{position:absolute;left:90px;top:300px}}
#gT{{position:absolute;left:90px;top:350px;width:900px;font-size:112px;line-height:.97;font-weight:700;letter-spacing:-.05em;color:#fff}}
#gT b{{color:{A.MENTA}}}
.gp{{position:absolute;top:730px;height:104px;padding:0 34px;border-radius:999px;background:#192019;border:2px solid #2E3830;display:flex;align-items:center;
  font-size:50px;font-weight:700;letter-spacing:-.03em;color:#fff;white-space:nowrap;opacity:0;font-variant-numeric:tabular-nums}}
#gDiv{{position:absolute;left:500px;top:744px;font-size:64px;font-weight:700;color:{K.DARK_TEXTO};opacity:0}}
#gIg{{position:absolute;left:90px;top:900px;font-size:64px;font-weight:700;color:{K.DARK_TEXTO};opacity:0}}
#gRes{{position:absolute;left:84px;top:960px;font-size:200px;font-weight:700;letter-spacing:-.055em;line-height:1;color:{A.MENTA};font-variant-numeric:tabular-nums;white-space:nowrap;opacity:0}}
#gRes .rs{{font-size:.36em;color:{K.DARK_TEXTO};margin-right:.18em}}
#gPor{{position:absolute;left:90px;top:1190px;font-size:48px;font-weight:600;color:#fff;letter-spacing:-.02em;opacity:0}}
#gPor span{{color:{K.DARK_TEXTO};font-weight:500}}
#gEx{{position:absolute;left:90px;top:1300px;height:60px;padding:0 24px;border-radius:999px;border:2px solid #3A443B;color:{K.DARK_TEXTO};font-size:30px;font-weight:600;
  display:flex;align-items:center;opacity:0}}
/* cena 4: a linha do câmbio, de perto, e a conta */
#s4 .tit{{opacity:0}}
.cr{{position:absolute;left:90px;width:900px;display:flex;justify-content:space-between;align-items:baseline;padding:22px 0;border-bottom:3px solid {A.FIO};opacity:0}}
.cr span{{font-size:40px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em}}
.cr b{{font-size:52px;font-weight:700;color:{A.INK};letter-spacing:-.035em;font-variant-numeric:tabular-nums;white-space:nowrap}}
.cr.res{{border-bottom:0}}
.cr.res span{{color:{A.INK};font-weight:700}}
.cr.res b{{color:{A.BRAND_DARK};font-size:64px}}
#s4ex{{position:absolute;left:90px;top:1470px;font-size:34px;font-weight:600;color:{A.MUTED};opacity:0}}
#s4nota{{position:absolute;left:96px;top:508px;font-size:26px;font-weight:500;color:{A.MUTED};opacity:0}}
/* cena 5 */
#s5 .h2{{position:absolute;left:90px;top:300px;width:900px;font-size:88px;line-height:1.02;color:#fff}}
#s5 .h2 b{{color:{A.MENTA}}}
#s5n{{position:absolute;left:90px;top:760px;width:900px;font-size:44px;line-height:1.3;font-weight:500;color:{K.DARK_TEXTO};letter-spacing:-.02em;opacity:0}}
#s5n b{{color:#fff;font-weight:700}}
"""

CORPO = f"""
<div class="cena papel" id="cenaTela">
  <div class="tit" id="t1">Na Nova remessa, digite <b>o total que saiu da conta.</b></div>
  <div class="tit" id="t2">Depois, os dólares que chegaram: <b>o câmbio aparece na hora.</b></div>
  <div class="tit" id="t3">E o IOF do comprovante: <b>1,10%.</b></div>
  <div class="nota" id="nota">{K.NOTA} · valores de exemplo</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA, 390, 1000)}</div>
</div>

<div class="cena papel" id="s4" style="transform:translateY(1920px)">
  <div class="tit" id="t4">Cada dólar saiu por <b>R$ 5,0550</b>, já com o IOF.</div>
  <div id="s4nota">{K.NOTA}</div>
  {pop_html("pop", tela("celular-remessa-7-pronta.jpg"))}
  <div class="cr" id="cr0" style="top:780px"><span>US$ 2.000 a R$ 5,00</span><b>R$ 10.000,00</b></div>
  <div class="cr" id="cr1" style="top:900px"><span>IOF do comprovante</span><b>+ R$ 110,00</b></div>
  <div class="cr" id="cr2" style="top:1020px"><span>Saiu da conta</span><b>R$ 10.110,00</b></div>
  <div class="cr res" id="cr3" style="top:1150px"><span>÷ US$ 2.000</span><b>R$ 5,0550</b></div>
  <div id="s4ex">Valores de exemplo.</div>
</div>

<div class="cena tinta" id="s5" style="transform:translateY(1920px)">
  <div class="h2">Cada remessa entra no seu <b>câmbio médio</b>, em Remessas.</div>
  <div id="s5n">Lance com o total, os dólares e o IOF do comprovante. <b>O câmbio de cada envio fica guardado.</b></div>
</div>

<div class="cena tinta" id="g">
  <div class="eyebrow">Remessas ao exterior</div>
  <div id="gT">Quanto custou <b>cada dólar?</b></div>
  <div class="gp" id="gp0" style="left:90px">R$ 10.110</div>
  <div id="gDiv">÷</div>
  <div class="gp" id="gp1" style="left:580px">US$ 2.000</div>
  <div id="gIg">=</div>
  <div id="gRes"><span class="rs">R$</span><span id="gV">5,0550</span></div>
  <div id="gPor">por dólar, <span>já com o IOF</span></div>
  <div id="gEx">valores de exemplo</div>
</div>

{K.fim("Remessas ao exterior no timtimcash")}
"""

JS = f"""
const H_SAI={H_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, J_SAI={J_SAI}, S4={S4}, S5={S5}, FIM={FIM};
const TQ_VALOR={TQ_VALOR}, TQ_ENV={TQ_ENV}, TQ_IOF={TQ_IOF}, TR={TR}, IDS={IDS};
const R_POP={R_POP}, P_POP={P_POP};
poeAnel('aValor', {folga(VALOR7, 8, 4)}, 6); poeAnel('aDer1', {folga(DERIVA, 2)}, 6); poeAnel('aDer2', {folga(DERIVA, 2)}, 6);
poeToque('tqValor', 195, {round(VALOR[1] + VALOR[3] + 16, 1)}); poeToque('tqEnv', {round(ENVIADO[0] + 14, 1)}, {round(ENVIADO[1] + ENVIADO[3] / 2, 1)}); poeToque('tqIof', {round(IOFC[0] + 14, 1)}, {round(IOFC[1] + IOFC[3] / 2, 1)});
const CAM = [[0,0,195,250,1], [{CAM_DESCE[0]},{CAM_DESCE[1]},195,{round(ENV_LINHA[1] + 150, 1)},1]];
function render(t){{
  // 1. gancho: R$ 10.110 ÷ US$ 2.000 = R$ 5,0550 (o resultado salta já no valor final, sem contador)
  saiCima('g', t, H_SAI);
  [0,1].forEach(k => {{ const a = -.2 + .22*k, e = $('gp'+k); e.style.opacity = lin(t, a, a+.15); e.style.transform = `translateY(${{30*(1-pout(t, a, a+.4))}}px)`; }});
  $('gDiv').style.opacity = lin(t, .05, .2); $('gIg').style.opacity = lin(t, .3, .45);
  $('gRes').style.opacity = lin(t, .3, .42);
  $('gRes').style.transform = `scale(${{.7 + .3*pback(t, .3, .8)}})`;
  some('gPor', t, 1.2, 0, 16); some('gEx', t, 1.45, 0, 16);
  // 2. a tela real: o total, os dólares e o IOF
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  janela('janela', t, H_SAI+.1, J_SAI);
  const ne = prog(t, H_SAI+.1, H_SAI+.7); $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(IDS, t, TR);
  toque('tqValor', t, TQ_VALOR); anel('aValor', t, 4.75, 5.5);
  toque('tqEnv', t, TQ_ENV); anel('aDer1', t, 7.0, 8.5);
  toque('tqIof', t, TQ_IOF); anel('aDer2', t, 9.6, 10.95);
  // 3. a linha do câmbio de perto, e a conta
  sobe('s4', t, S4);
  titulo('t4', t, T4[0], T4[1]); some('s4nota', t, S4+.3, T4[1], 10);
  recorte('pop', t, S4+.35, T4[1], R_POP, [P_POP[0], P_POP[1]+60, P_POP[2], 1], P_POP, .55, null, 390);
  for (let k=0;k<4;k++) some('cr'+k, t, S4+1.0+.35*k, T4[1], 22);
  some('s4ex', t, S4+2.4, T4[1], 12);
  // 4. o câmbio médio (tinta)
  sobe('s5', t, S5); some('s5n', t, S5+.6, 0, 20);
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1" style="font-size:128px;line-height:.95;margin-top:34px;color:#fff">Quanto custou <span style="color:{A.MENTA}">cada dólar?</span></div>
  </div>
  <div style="position:absolute;left:84px;top:960px;font-size:200px;font-weight:700;letter-spacing:-.055em;line-height:1;color:{A.MENTA};white-space:nowrap">
    <span style="font-size:.36em;color:{K.DARK_TEXTO};margin-right:.18em">R$</span>5,0550</div>
  <div style="position:absolute;left:90px;top:1190px;font-size:48px;font-weight:600;color:#fff;letter-spacing:-.02em">por dólar, <span style="color:{K.DARK_TEXTO};font-weight:500">já com o IOF</span></div>
  <div style="position:absolute;left:90px;top:1300px;height:60px;padding:0 24px;border-radius:999px;border:2px solid #3A443B;color:{K.DARK_TEXTO};font-size:30px;font-weight:600;
    display:flex;align-items:center">valores de exemplo</div>"""
    return K.pagina_capa(corpo, "", fundo="tinta")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
