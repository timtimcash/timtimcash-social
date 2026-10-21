# -*- coding: utf-8 -*-
"""Reel de 15/01/2027 (sexta) · "O seu mês tem 3 recados" (Insights) · capa tinta · equipe jr.

- Gancho (tinta): "O seu mês tem 3 recados." e os 3 cartões reais dos Insights de 15/01/2027 entrando um a um
  (recortes da tela, sem nenhuma mudança): "Educação 65% acima da média" (R$ 2.390,00 este mês vs média de R$ 1.450,00,
  últimos 6 meses), "Excelente! Receita guardada: 35%" (R$ 3.518,50 de R$ 9.960,00 recebidos), "Educação: 37% das
  despesas" (R$ 2.390,00).
- Telas reais (captura_15.py, celular, relógio 15/01/2027 10:00, build 2026-10-19.5, conta sem mudança): a Visão geral
  (Realizado, Janeiro 2027) numa foto alta; a câmera desce até "Insights" ("Análise automática do período") e cada cartão
  ganha um anel com o que ele diz; toque no X do terceiro cartão: ele sai (o X dispensa no mês).
  O que está por trás de cada número (estado.py e a tela): Educação = escola R$ 1.450 + material escolar R$ 940 (pago em
  12/01) = R$ 2.390; 2.390 ÷ 1.450 = 1,648 (65% acima); receita guardada = (9.960 − 6.441,50) ÷ 9.960 = 35,3%, acima da
  meta padrão de 20% (Relatórios, "Ajustar cálculo"); 2.390 ÷ 6.441,50 = 37,1%.
- Mensagem: "São regras fixas: comparam o seu mês com a sua média e com as suas metas." (como manda FUNCIONALIDADES.md),
  e os outros cartões que existem (orçamento acima de 70% ou estourado, conta no negativo, lançamento vencido; FUNCIONALIDADES.md).
- Fechamento verde: "Insights na Visão geral do timtimcash."

python3 reel_15.py  |  REEL_PREVIA="0 0.5 1 2.8 4.4 6.4 9.2 11.9 14.2 15.2 16.9 19.4" python3 reel_15.py
"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A

PASTA = "2027-01-15_reel-insights-o-que-o-mes-diz"
TRAB = C.trabalho("15")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas(PASTA)

# ---------------------------------------------------------------- números (conferidos contra a tela)
FA, FB = "a-visao-geral-inteira.jpg", "b-visao-geral-inteira-depois-do-x.jpg"
CA, CB = CX[FA]["cartoes"], CX[FB]["cartoes"]
assert [(c["titulo"], c["desc"]) for c in CA] == [
    ("Educação 65% acima da média", "R$ 2.390,00 este mês vs média de R$ 1.450,00 (últimos 6 meses)."),
    ("Excelente! Receita guardada: 35%", "Você guardou R$ 3.518,50 de R$ 9.960,00 recebidos. Continue assim!"),
    ("Educação: 37% das despesas", "Concentra R$ 2.390,00 dos seus gastos.")], CA
assert [c["titulo"] for c in CB] == ["Educação 65% acima da média", "Excelente! Receita guardada: 35%"]
assert CX["n_antes"] == 3 and CX["n_depois"] == 2
EDU, MEDIA, MAT = D("2390.00"), D("1450.00"), D("940.00")
REC, DESP = D("9960.00"), D("6441.50")
assert MEDIA + MAT == EDU and round((EDU / MEDIA - 1) * 100) == 65
assert REC - DESP == D("3518.50") and round((REC - DESP) / REC * 100) == 35
assert round(EDU / DESP * 100) == 37
assert "Despesas\nR$ 6.441,50" in CX[FA]["texto"] and "Jan 15 2027 10:0" in CX["relogio"] and not CX["erros"]
PAINEL = CX[FA]["painel"]["painel"]
assert CX[FB]["painel"]["painel"][1] == PAINEL[1]          # o painel fica no lugar; só o terceiro cartão sai

# ---------------------------------------------------------------- caixas (px CSS da foto)
CARD = [c["caixa"] for c in CA]
X3 = CA[2]["x"]
Y_PAINEL = round(PAINEL[1] + PAINEL[3] / 2, 1)
Z = 1.15

# ---------------------------------------------------------------- tempos (s)
H_SAI = 3.4
T1, T2, T3, T4, T5, T6 = (3.5, 5.6), (5.65, 8.25), (8.3, 10.9), (10.95, 13.55), (13.6, 15.8), (15.85, 17.95)
TQ_X = 14.45
FIM = 18.0
DUR = round(FIM + 2.75, 2)
CAM = [[0, 0, 195, 250, 1], [3.95, 5.15, 195, Y_PAINEL, Z]]
EXTRA = K.aneis("aC0", "aC1", "aC2") + K.toques("tX")

# ---------------------------------------------------------------- gancho: os 3 cartões reais
LARG = 900
S_H = LARG / CARD[0][2]
YH = [560]
for c in CARD[:-1]:
    YH.append(round(YH[-1] + c[3] * S_H + 30, 1))
def corte(i, R, larg, top):
    s = larg / R[2]
    return (f'<div class="ct" id="ct{i}" style="top:{top}px;width:{larg}px;height:{R[3] * s:.1f}px;border-radius:{12 * s:.1f}px">'
            f'<img src="file://{os.path.join(TELAS, FA)}" style="width:{390 * s:.1f}px;left:{-R[0] * s:.1f}px;top:{-R[1] * s:.1f}px"></div>'
            f'<div class="nb" id="nb{i}" style="top:{top - 22}px">{i + 1}</div>')
Y_NOTA_H = round(YH[-1] + CARD[-1][3] * S_H + 34, 1)

CSS = f"""
.tit{{font-size:64px}}
#h{{background:{A.INK}}}
#q{{position:absolute;left:90px;top:292px;width:900px;font-size:104px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#q b{{color:{A.MENTA};font-weight:700}}
.ct{{position:absolute;left:90px;overflow:hidden;opacity:0;box-shadow:0 30px 60px -28px rgba(0,0,0,.6)}}
.ct img{{position:absolute;display:block;max-width:none}}
.nb{{position:absolute;left:62px;width:64px;height:64px;border-radius:50%;background:{A.MENTA};color:{A.INK};font-size:36px;font-weight:700;
  display:flex;align-items:center;justify-content:center;opacity:0;font-variant-numeric:tabular-nums;box-shadow:0 0 0 8px {A.INK}}}
#notaH{{position:absolute;left:92px;top:{Y_NOTA_H}px;font-size:26px;font-weight:500;color:{K.DARK_TEXTO};opacity:0}}
#msg{{position:absolute;left:90px;top:300px;width:900px;font-size:84px;line-height:1.02;font-weight:700;letter-spacing:-.048em;color:{A.INK};text-wrap:balance;opacity:0}}
#msg b{{color:{A.BRAND_DARK};font-weight:700}}
#regras{{position:absolute;left:90px;top:780px;width:900px;display:flex;flex-direction:column;gap:26px;opacity:0}}
.rg{{display:flex;align-items:center;gap:28px;height:140px;padding:0 40px;border-radius:36px;background:#fff;border:2px solid {A.FIO};
  box-shadow:0 1px 2px rgba(15,20,16,.04),0 14px 34px -16px rgba(15,20,16,.14);font-size:48px;font-weight:600;letter-spacing:-.03em;color:{A.INK}}}
.rg i{{flex:none;width:84px;height:84px;border-radius:24px;background:{A.SOFT};display:flex;align-items:center;justify-content:center}}
#tambem{{position:absolute;left:90px;top:1150px;width:900px;font-size:40px;line-height:1.3;font-weight:500;letter-spacing:-.02em;color:{A.MUTED};opacity:0;text-wrap:balance}}
#tambem b{{color:{A.INK};font-weight:600}}
"""

ICO_MEDIA = (f'<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="{A.BRAND_DEEP}" stroke-width="2.1" stroke-linecap="round" '
             f'stroke-linejoin="round"><path d="M4 20V11M9.3 20V6M14.6 20v-8M20 20V8"/><path d="M3 9.5h18" stroke-dasharray="2.2 2.6"/></svg>')
ICO_META = (f'<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="{A.BRAND_DEEP}" stroke-width="2.1" stroke-linecap="round" '
            f'stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="1.2"/></svg>')

CORPO = f"""
<div class="cena papel" id="telas">
  <div class="tit" id="t1">Em <b>Insights</b>, no fim da Visão geral.</div>
  <div class="tit" id="t2">1 · O material escolar levou <b>Educação</b> a 65% acima da média.</div>
  <div class="tit" id="t3">2 · <b>Receita guardada</b>: 35% até aqui. A meta padrão é 20%.</div>
  <div class="tit" id="t4">3 · <b>Educação</b> leva 37% do que saiu no mês.</div>
  <div class="tit" id="t5">Já viu? O <b>X</b> dispensa o recado até o fim do mês.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", [("fa", os.path.join(TELAS, FA)), ("fb", os.path.join(TELAS, FB))], EXTRA)}</div>
  <div id="msg">São <b>regras fixas</b>: comparam o seu mês com a sua média e com as suas metas.</div>
  <div id="regras"><div class="rg"><i>{ICO_MEDIA}</i>A sua média dos meses anteriores</div><div class="rg"><i>{ICO_META}</i>As suas metas e os seus limites</div></div>
  <div id="tambem">Também há cartões para orçamento acima de <b>70%</b>, conta <b>no negativo</b> e lançamento <b>vencido</b>.</div>
</div>

<div class="cena tinta" id="h">
  <div id="q">O seu mês tem <b>3&nbsp;recados</b>.</div>
  {"".join(corte(i, CARD[i], LARG, YH[i]) for i in range(3))}
  <div id="notaH">{K.NOTA}</div>
</div>

{K.fim("Insights na Visão geral do timtimcash.")}
"""

JS = f"""
const H_SAI={H_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, T6={list(T6)}, FIM={FIM};
const CAM={CAM};
poeAnel('aC0', {CARD[0]}, 6); poeAnel('aC1', {CARD[1]}, 6); poeAnel('aC2', {CARD[2]}, 6);
poeToque('tX', ...{C.centro(X3)});
function render(t){{
  // 1. gancho: os 3 cartões reais entram um a um, numerados
  [0,1,2].forEach(i => {{ const a = .12 + .42*i, p = pback2(t, a, a+.55);
    $('ct'+i).style.opacity = lin(t, a, a+.18); $('ct'+i).style.transform = `translateY(${{(1-p)*90}}px) scale(${{.94 + .06*p}})`;
    salta('nb'+i, t, a+.3, .4); }});
  aparece('notaH', t, .3, 0, 10, .4);
  $('q').style.transform = `translateY(${{-10*pout(t, 0, 1.2)}}px)`;
  saiCima('h', t, H_SAI);
  // 2. telas reais: a câmera desce até os Insights; um anel em cada cartão; o X
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, H_SAI+.05, T5[1]); janela('nota', t, H_SAI+.05, T5[1]);
  so(['fa','fb'], t >= {TQ_X} + .15 ? 1 : 0);
  camera('tela', t, CAM);
  anel('aC0', t, T2[0]+.15, T2[1]); anel('aC1', t, T3[0]+.15, T3[1]); anel('aC2', t, T4[0]+.15, T5[0]+.5);
  toque('tX', t, {TQ_X});
  if (t >= {TQ_X}+.2){{ $('t_tX').style.opacity = 0; $('o_tX').style.opacity = 0; $('aC2').style.opacity = 0; }}   // o cartão saiu
  // 3. regras fixas
  aparece('msg', t, T6[0]+.05, FIM-.05, 30, .45); aparece('regras', t, T6[0]+.35, FIM-.05, 30, .45); aparece('tambem', t, T6[0]+.75, FIM-.05, 20, .4);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    s = 760 / CARD[0][2]
    pilha = ""
    y = 822
    for i in range(3):
        R = CARD[i]
        pilha += (f'<div style="position:absolute;left:160px;top:{y:.0f}px;width:760px;height:{R[3] * s:.1f}px;border-radius:{12 * s:.1f}px;overflow:hidden;'
                  f'box-shadow:0 30px 60px -28px rgba(0,0,0,.6)"><img src="file://{os.path.join(TELAS, FA)}" style="position:absolute;display:block;max-width:none;'
                  f'width:{390 * s:.1f}px;left:{-R[0] * s:.1f}px;top:{-R[1] * s:.1f}px"></div>')
        y += R[3] * s + 22
    corpo = f"""{K.logo("tinta")}
  <div class="eyebrow" style="position:absolute;left:90px;top:430px">Visão geral · Insights</div>
  <div class="h1" style="position:absolute;left:90px;top:494px;width:900px;font-size:124px;line-height:.96;color:#fff">O seu mês tem <span style="color:{A.MENTA}">3 recados.</span></div>
  {pilha}
  <div style="position:absolute;left:162px;top:{y + 6:.0f}px;font-size:24px;font-weight:500;color:{K.DARK_TEXTO}">{K.NOTA}</div>"""
    return K.pagina_capa(corpo, "", fundo="tinta")


HTML = C.pagina(CORPO, CSS, JS)
CAPA = capa()

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
