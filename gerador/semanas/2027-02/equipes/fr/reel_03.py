# -*- coding: utf-8 -*-
"""Reel de 03/02/2027 (quarta) · "O ano escolar numa conta" · capa tinta · equipe fr.

Telas reais: captura_03.py, build 2026-10-19.5, conta de base (J/base_app, sem mudança), celular 390 px CSS em escala 3,
relógio da página em 03/02/2027 10:00. Tudo pela interface: Visão geral (Realizado, Fevereiro 2027) -> "Previsto" -> toque no
mês -> "Ano atual" -> "Aplicar" (Ano 2027) -> rola até "Top saídas" (Educação R$ 18.626,00 · 32%) -> toque em "Educação"
-> Transações com a categoria e o Ano 2027: "14 transações · 3 pagas · 11 pendentes · somam R$ 18.626,00 · 804 no histórico".
De onde vem o número: escola R$ 1.450 todo dia 10, lançada como Fixa desde outubro de 2026 (12 em 2027: a de janeiro paga,
as de fevereiro a dezembro pendentes), material escolar R$ 940 (pago em 12/01) e uniforme R$ 286 (pago em 18/01).
12 × 1.450 + 940 + 286 = 18.626; ÷ 12 = 1.552,17 por mês; (940 + 286) ÷ 12 = 102,17 a mais que a mensalidade.

python3 reel_03.py  |  REEL_PREVIA="0 0.5 1 2 3.6 5.2 6.4 8.4 10.6 12.8 15.6 18" python3 reel_03.py
"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro, brl

PASTA = "2027-02-03_reel-o-ano-escolar-numa-conta"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("03")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- números (conferidos contra a tela)
ESCOLA, MATERIAL, UNIFORME = D("1450.00"), D("940.00"), D("286.00")
EXTRA = MATERIAL + UNIFORME
TOTAL = 12 * ESCOLA + EXTRA
assert TOTAL == D("18626.00")
POR_MES = TOTAL / 12
assert POR_MES.quantize(D("0.01")) == D("1552.17")
EXTRA_MES = EXTRA / 12
assert EXTRA_MES.quantize(D("0.01")) == D("102.17")
CATS = {c[0].rsplit(" R$", 1)[0]: c for c in C["cats"]}
assert CATS["Educação"][0] == "Educação R$ 18.626,00 32%"
TR = C["trechos"]
assert TR["texto"] == "14 transações · 3 pagas · 11 pendentes · somam R$ 18.626,00 · 804 no histórico", TR["texto"]
LIN = C["linhas"]
assert len(LIN) == 14
assert sum(1 for l in LIN if l[0].startswith("Editar Excluir Escola Fixa") and l[0].endswith("−R$ 1.450,00 pendente")) == 11
assert any(l[0].startswith("Editar Excluir Material escolar") and l[0].endswith("−R$ 940,00 paga") for l in LIN)
assert any(l[0].startswith("Editar Excluir Uniforme escolar") and l[0].endswith("−R$ 286,00 paga") for l in LIN)
assert "Ano 2027" in C["celular-transacoes-educacao-ano-2027-alta.png"]["texto"]
_a = C["celular-visao-geral-previsto-ano-2027.png"]["texto"]
assert "Ano 2027" in _a and "Movimento de 2027\nPREVISTO" in _a
assert "1 jan 2027 a 31 dez 2027" in C["celular-periodo-ano-atual.png"]["texto"]

# ---------------------------------------------------------------- caixas (px CSS do celular)
V1 = C["celular-visao-geral-realizado-fevereiro.png"]["caixas"]
PREV, MES = V1["previsto"], V1["mes"]
CAL = C["celular-periodo-calendario.png"]["caixas"]
ANO_AT, APLICAR = CAL["ano_atual"], CAL["aplicar"]
PIL_ANO = C["celular-visao-geral-previsto-ano-2027.png"]["caixas"]["ano"]
EDU = CATS["Educação"][1:]
SOMA_KEY = [k for k in TR if k.startswith("somam")][0]
RES = uniao(*TR["14 transações"], *TR["3 pagas"], *TR["11 pendentes"], *TR[SOMA_KEY])
ROW1 = LIN[0][1:]                      # Escola de dezembro, Fixa, pendente

# ---------------------------------------------------------------- tempos (s)
SOBE = 2.75                            # o gancho (tinta) sobe e revela a tela real
T1 = (2.9, 6.55)
TQ_PREV, TQ_MES, TQ_ANO, TQ_APL = 3.5, 4.3, 4.95, 5.55
T2 = (6.75, 9.2)
TQ_EDU = 9.3
T3 = (9.45, 11.45)
T4 = (11.6, 13.5)
J_SAI = 13.5
T5 = 13.8
FIM = 17.4
DUR = 20.25

IMGS = [("f1", tela("celular-visao-geral-realizado-fevereiro.png")), ("f2", tela("celular-visao-geral-previsto-fevereiro.png")),
        ("f3", tela("celular-periodo-calendario.png")), ("f4", tela("celular-periodo-ano-atual.png")),
        ("f5", tela("celular-visao-geral-previsto-ano-2027-alta.png")), ("f6", tela("celular-transacoes-educacao-ano-2027-alta.png"))]
TROCAS = [0, TQ_PREV + .15, TQ_MES + .2, TQ_ANO + .15, TQ_APL + .2, TQ_EDU + .2]
EXTRA_HTML = K.aneis("aPrev", "aPrev2", "aAno", "aEdu", "aRes", "aRow") + K.toques("tqPrev", "tqMes", "tqAno", "tqApl", "tqEdu")

# ---------------------------------------------------------------- colunas do ano (gancho e cena 4)
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
X0, LARG, PASSO = 105, 56, 74


def colunas(prefixo, base, escala, cor_rot):
    out = []
    for i, m in enumerate(MESES):
        x = X0 + i * PASSO
        out.append(f'<div class="col" id="{prefixo}c{i}" style="left:{x}px;top:{base}px;width:{LARG}px">'
                   f'<i class="sx" id="{prefixo}x{i}"></i><i class="se" id="{prefixo}e{i}"></i></div>')
        out.append(f'<div class="mes" id="{prefixo}m{i}" style="left:{x - 10}px;top:{base + 14}px;width:{LARG + 20}px;color:{cor_rot}">{m}</div>')
    return "".join(out)


G_BASE, G_ALT = 1330, 400              # gancho: base das colunas e altura de janeiro (R$ 2.676)
S_BASE, S_ALT = 1180, 520              # cena 4
JAN = float(ESCOLA + EXTRA)
H_ESC_G, H_EXT_G = float(ESCOLA) / JAN * G_ALT, float(EXTRA) / JAN * G_ALT
H_ESC_S, H_EXT_S = float(ESCOLA) / JAN * S_ALT, float(EXTRA) / JAN * S_ALT
H_NIVEL_S = float(POR_MES) / JAN * S_ALT      # R$ 1.552,17

CSS = f"""
.tit{{font-size:64px}}
/* gancho */
#g .eb{{position:absolute;left:90px;top:300px}}
#gQ{{position:absolute;left:90px;top:352px;width:900px;font-size:112px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#gQ span{{color:{A.MENTA}}}
#gNum{{position:absolute;left:84px;top:596px;display:flex;align-items:baseline;color:#fff;font-weight:700;letter-spacing:-.05em;
  font-variant-numeric:tabular-nums;transform-origin:0 75%}}
#gNum .rs{{font-size:76px;font-weight:600;color:{K.DARK_TEXTO};margin-right:24px;letter-spacing:-.01em}}
#gNum b{{font-size:208px;line-height:1;font-weight:700}}
.col{{position:absolute;height:0}}
.col i{{position:absolute;left:0;width:100%;display:block;height:0}}
.se{{background:{A.CORAL};border-radius:4px 4px 3px 3px}}
.sx{{background:{A.AMBER};border-radius:10px 10px 3px 3px}}
.mes{{position:absolute;text-align:center;font-size:27px;font-weight:600;opacity:0}}
#gLeg{{position:absolute;left:90px;top:1418px;width:900px;opacity:0}}
.lg{{display:flex;align-items:center;gap:18px;font-size:36px;font-weight:600;letter-spacing:-.02em;line-height:1.35;color:#fff}}
.lg i{{display:inline-block;width:26px;height:26px;border-radius:7px;flex:none}}
.lg b{{font-weight:700}}
/* cena 4 */
#ap5{{position:absolute;left:90px;top:372px;font-size:42px;font-weight:500;color:{A.MUTED};letter-spacing:-.02em;opacity:0}}
#ap5 b{{color:{A.INK};font-weight:700}}
#nivel{{position:absolute;left:{X0 - 14}px;width:{12 * PASSO - PASSO + LARG + 28}px;border-top:5px solid {A.BRAND_DARK};opacity:0}}
#rotNivel{{position:absolute;left:0;width:1080px;text-align:center;opacity:0}}
#rotNivel span{{display:inline-flex;align-items:baseline;gap:14px;background:{A.BRAND};color:#fff;border-radius:999px;padding:16px 40px;
  font-size:56px;font-weight:700;letter-spacing:-.04em;font-variant-numeric:tabular-nums;box-shadow:0 18px 36px -20px rgba(15,20,16,.45)}}
#rotNivel small{{font-size:36px;font-weight:600;letter-spacing:-.01em}}
#leg5{{position:absolute;left:90px;top:1268px;width:900px;opacity:0}}
#leg5 .lg{{color:{A.INK};font-size:36px}}
#leg5 .lg span{{color:{A.MUTED};font-weight:500}}
#leg5 .lg span b{{color:{A.INK};font-weight:700}}
"""

LEG_G = (f'<div class="lg"><i style="background:{A.CORAL}"></i><span>Escola: <b>12 × R$ 1.450</b></span></div>'
         f'<div class="lg"><i style="background:{A.AMBER}"></i><span>Material e uniforme: <b>R$ 1.226</b></span></div>')
LEG_5 = (f'<div class="lg"><i style="background:{A.CORAL}"></i><span><b>Mensalidade:</b> R$ 1.450</span></div>'
         f'<div class="lg"><i style="background:{A.AMBER}"></i><span><b>Material e uniforme:</b> + R$ 102 por mês</span></div>')

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Na Visão geral, toque em <b>Previsto</b> e escolha <b>2027</b>.</div>
  <div class="tit" id="t2">Educação em 2027: <b>R$&nbsp;18.626</b>.</div>
  <div class="tit" id="t3">São <b>14 lançamentos</b>: 3 pagos e 11 pendentes.</div>
  <div class="tit" id="t4">Previsto inclui o que já está <b>contratado</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA_HTML)}</div>

  <div class="tit" id="t5">Por mês, <b>R$&nbsp;1.552</b>.</div>
  <div id="ap5"><b>R$ 18.626</b> ÷ 12 meses</div>
  <div id="g5">{colunas("s", S_BASE, 1, A.MUTED)}</div>
  <div id="nivel" style="top:{S_BASE - H_NIVEL_S - 2.5:.1f}px"></div>
  <div id="rotNivel" style="top:{S_BASE - H_NIVEL_S - 138:.0f}px"><span>R$ 1.552 <small>por mês</small></span></div>
  <div id="leg5">{LEG_5}</div>
</div>

<div class="cena tinta" id="g">
  <div class="eyebrow eb" id="gEb">Volta às aulas</div>
  <div id="gQ">Quanto custa o <span>ano escolar</span>?</div>
  <div id="gNum"><span class="rs">R$</span><b id="gV">0</b></div>
  <div id="gGraf">{colunas("g", G_BASE, 1, K.DARK_TEXTO)}</div>
  <div id="gLeg">{LEG_G}</div>
</div>

{K.fim("Visão geral no timtimcash")}
"""

JS = f"""
const SOBE={SOBE}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, J_SAI={J_SAI}, T5={T5}, FIM={FIM};
const TQ_PREV={TQ_PREV}, TQ_MES={TQ_MES}, TQ_ANO={TQ_ANO}, TQ_APL={TQ_APL}, TQ_EDU={TQ_EDU};
const TROCAS={TROCAS};
const ESC={float(ESCOLA)}, EXT={float(EXTRA)};
const HEG={H_ESC_G:.2f}, HXG={H_EXT_G:.2f}, HES={H_ESC_S:.2f}, HXS={H_EXT_S:.2f}, HNS={H_NIVEL_S:.2f};
poeAnel('aPrev', {PREV}, 8); poeAnel('aPrev2', {PREV}, 8); poeAnel('aAno', {PIL_ANO}, 8); poeAnel('aEdu', {EDU}, 10);
poeAnel('aRes', {RES}, 20); poeAnel('aRow', {ROW1}, 6);
poeToque('tqPrev', ...{centro(PREV)}); poeToque('tqMes', ...{centro(MES)}); poeToque('tqAno', ...{centro(ANO_AT)});
poeToque('tqApl', ...{centro(APLICAR)}); poeToque('tqEdu', ...{centro(EDU)});
// câmera (px CSS do celular no centro da janela)
const CAM = [[0,0,195,250,1], [TQ_MES+.15, TQ_MES+.5, 195, 490, 1], [TQ_APL+.2, TQ_APL+.55, 195, 250, 1],
             [T2[0]-.1, T2[0]+.85, 195, 2430, 1], [TQ_EDU+.19, TQ_EDU+.2, 195, 540, 1], [T4[0]-.05, T4[0]+.85, 195, 900, 1],
             [T4[0]+.95, J_SAI+.3, 195, 1010, 1]];
// gancho: cada mês acende uma coluna (escola) e janeiro ganha material e uniforme; o contador soma as colunas
const GA = i => -0.45 + 0.045*i;
const GX = [0.38, 0.75];
function render(t){{
  // 1. gancho (tinta)
  saiCima('g', t, SOBE);
  $('gQ').style.transform = `translateY(${{(-16*pout(t, -0.2, 1.4)).toFixed(1)}}px)`;
  let soma = 0;
  for (let i=0;i<12;i++){{ const p = pout(t, GA(i), GA(i)+.3); soma += ESC*p;
    $('ge'+i).style.height = (HEG*p)+'px'; $('ge'+i).style.top = (-HEG*p)+'px';
    $('gm'+i).style.opacity = prog(t, GA(i), GA(i)+.25); }}
  const px = pout(t, GX[0], GX[1]); soma += EXT*px;
  $('gx0').style.height = (HXG*px)+'px'; $('gx0').style.top = (-HEG - HXG*px - (px > 0.01 ? 4 : 0))+'px';
  $('gV').textContent = fmt(soma, 0);
  $('gNum').style.transform = `scale(${{(1 + 0.06*Math.sin(Math.PI*clamp((t-GX[1])/0.32, 0, 1))).toFixed(4)}})`;
  $('gLeg').style.opacity = prog(t, 0.55, 0.95);
  // 2. a tela real: Previsto, Ano 2027, Educação, Transações
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, SOBE+.1, J_SAI);
  const ne = prog(t, SOBE+.1, SOBE+.7);
  $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(['f1','f2','f3','f4','f5','f6'], t, TROCAS, 0);
  anel('aPrev', t, T1[0]+.15, TQ_PREV-.1); toque('tqPrev', t, TQ_PREV); toque('tqMes', t, TQ_MES); toque('tqAno', t, TQ_ANO); toque('tqApl', t, TQ_APL);
  anel('aAno', t, TQ_APL+.6, T1[1]); anel('aPrev2', t, TQ_APL+.6, T1[1]);
  anel('aEdu', t, T2[0]+.95, TQ_EDU-.05); toque('tqEdu', t, TQ_EDU);
  anel('aRes', t, T3[0]+.35, T3[1]); anel('aRow', t, T4[0]+.85, J_SAI-.05);
  // 3. por mês: as colunas do ano se espalham por igual (R$ 1.552,17)
  titulo('t5', t, T5, FIM+.4);
  aparece('ap5', t, T5+.2, FIM+.4, 20);
  const nv = prog(t, T5+.8, T5+1.45);
  for (let i=0;i<12;i++){{ const a0 = T5 + .05 + i*.03; const p = pout(t, a0, a0+.32);
    $('sm'+i).style.opacity = prog(t, a0, a0+.25);
    const he = HES*p, hx = (i === 0 ? HXS*pout(t, T5+.35, T5+.62) : 0);
    const alvoX = HNS - HES;                       // parte de material e uniforme em cada mês, depois de espalhar
    const hxN = hx + (alvoX - hx)*nv;
    $('se'+i).style.height = he+'px'; $('se'+i).style.top = (-he)+'px';
    $('sx'+i).style.height = Math.max(0, hxN)+'px'; $('sx'+i).style.top = (-he - Math.max(0, hxN) - (hxN > 0.5 ? 3 : 0))+'px'; }}
  $('nivel').style.opacity = prog(t, T5+1.35, T5+1.6);
  $('nivel').style.transform = `scaleX(${{prog(t, T5+1.35, T5+1.75).toFixed(3)}})`; $('nivel').style.transformOrigin = '0 0';
  salta('rotNivel', t, T5+1.45, .45);
  $('leg5').style.opacity = prog(t, T5+1.6, T5+1.95);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    base, alt = 1268, 330
    cols = []
    for i, m in enumerate(MESES):
        x = X0 + i * PASSO
        he = float(ESCOLA) / JAN * alt
        hx = float(EXTRA) / JAN * alt if i == 0 else 0
        cols.append(f'<div style="position:absolute;left:{x}px;top:{base - he:.1f}px;width:{LARG}px;height:{he:.1f}px;background:{A.CORAL};border-radius:4px 4px 3px 3px"></div>')
        if hx:
            cols.append(f'<div style="position:absolute;left:{x}px;top:{base - he - hx - 4:.1f}px;width:{LARG}px;height:{hx:.1f}px;background:{A.AMBER};border-radius:10px 10px 3px 3px"></div>')
        cols.append(f'<div style="position:absolute;left:{x - 10}px;top:{base + 14}px;width:{LARG + 20}px;text-align:center;font-size:27px;font-weight:600;color:{K.DARK_TEXTO}">{m}</div>')
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:440px;width:900px">
    <div class="eyebrow">Volta às aulas</div>
    <div class="h1" style="font-size:124px;line-height:.97;margin-top:34px;color:#fff">O ano escolar <span style="color:{A.MENTA}">numa conta.</span></div>
  </div>
  {''.join(cols)}
  <div style="position:absolute;left:84px;top:1360px;display:flex;align-items:baseline;color:{A.MENTA};font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums">
    <span style="font-size:72px;font-weight:600;color:{K.DARK_TEXTO};margin-right:22px;letter-spacing:-.01em">R$</span><span style="font-size:200px;line-height:1">18.626</span></div>"""
    return K.pagina_capa(corpo, "", fundo="tinta")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
