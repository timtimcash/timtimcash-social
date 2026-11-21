# -*- coding: utf-8 -*-
"""Vídeo 1 · o timtimcash, de maneira geral (24 s) · capa papel.

Telas reais: captura.py, build 2026-11-20.8 (o que está no ar), a conta de exemplo no Grátis (3 limites), tema claro, celular
390 px em escala 3, relógio em 21/11/2026 10:00, numa sessão só:
1. Nova transação: despesa de R$ 24,50, "Padaria", digitada tecla a tecla; a categoria "Padaria e lanches" vem sugerida; toque
   em "Lançar despesa" e o aviso "Transação adicionada".
2. Visão geral (Novembro 2026, parcial): "Guardou 26,4% da receita", Receitas R$ 9.960,00, Despesas R$ 7.331,20, Resultado do
   período R$ 2.628,80, e o Fluxo mensal.
3. Pendentes: "A vencer · EM 6 DIAS · 27/11/2026 · 13º salário · 1ª parcela +R$ 4.980,00".
4. Fluxo: Resultado de novembro até o dia 21 e o Fluxo detalhado, 12 meses.
5. Orçamentos: Progresso por categoria (Bares e restaurantes, Mercado e Transporte).
Gancho: "R$ 7.331,20" são as despesas de novembro até o dia 21 na conta de exemplo, 73,6% da receita (a barra da Visão geral).
Frases de plano e de preço iguais às do site: "E, quando quiser ir mais fundo.", "R$ 14,90 por mês, ou R$ 149 por ano",
"Sem prazo e sem cartão".

python3 video1.py  |  REEL_PREVIA="0.5 1.6 3 5 6.6 7.6 9.4 12 14 16 18.6 21.5" python3 video1.py
"""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI); sys.path.insert(0, os.path.dirname(AQUI))
import kitv as KV
import tempos as T
K, A, C = KV.K, KV.A, KV.C
TELAS = os.path.join(AQUI, "telas"); SAIDA = os.path.join(AQUI, "saida"); TRAB = os.path.join(AQUI, "trabalho")
CX = json.load(open(os.path.join(TELAS, "caixas.json"), encoding="utf-8"))

# ---------------------------------------------------------------- conferência com as telas
d = CX["dashboard"]; tx = d["texto"].replace("\u00a0", " ")
for _k in CX: CX[_k]["texto"] = CX[_k].get("texto", "").replace("\u00a0", " ")
assert d["guardou"][4] == "Guardou 26,4% da receita" and d["despesas"][4] == "Despesas R$ 7.331,20"
assert "Receitas R$ 9.960,00" in tx.replace(" | ", " ") and "R$ 2.628,80" in tx and "73,6%" in tx
assert "Categoria | Padaria e lanches" in CX["folha_fim"]["texto"] and CX["folha_fim"]["desc"][4] == "Padaria"
assert CX["pendentes"]["em"][4] == "EM 6 DIAS" and "+R$ 4.980,00" in CX["pendentes"]["avencer"][4]
assert "12 meses" in CX["fluxo"]["detalhado"][4] and "R$ 2.628 ,80" in CX["fluxo"]["resumo"][4]
assert "3 categorias" in CX["orcamentos"]["progresso"][4]

# ---------------------------------------------------------------- caixas (px CSS da foto)
VAL = [34, 228, 322, 78]
CAT = [8, CX["folha_fim"]["cat"][1] + 1, 374, CX["folha_fim"]["cat"][3] - 2]
CTA = CX["folha_fim"]["cta"][:4]
MOV = [22, d["guardou"][1] - 12, 346, d["resultado"][1] + d["resultado"][3] + 16 - (d["guardou"][1] - 12)]
p = CX["pendentes"]; VENCE = [22, p["em"][1] - 10, 346, p["avencer"][1] + p["avencer"][3] - p["em"][1] + 2]

t = lambda n: os.path.join(TELAS, n + ".png")
IMGS = ([("f0", t("f0"))] + [(f"v{i}", t(f"v{i}")) for i in range(1, 5)] + [(f"d{i}", t(f"d{i}")) for i in range(1, 9)] +
        [("s1", t("s1")), ("dash", t("dashboard")), ("pend", t("pendentes")), ("flux", t("fluxo")), ("orc", t("orcamentos"))])
FOTOS = ([[0, "f0"]] + [[a, f"v{i+1}"] for i, a in enumerate(T.TECLAS_VALOR)] + [[a, f"d{i+1}"] for i, a in enumerate(T.TECLAS_DESC)] +
         [[T.SUGERIDA, "d8"], [T.LANCADA, "s1"], [T.VEJA, "dash", .3], [T.ANTECIPE, "pend"], [T.ACOMPANHE, "flux"], [T.PLANEJE, "orc"]])

VERBOS = [("Lance", "cada gasto, em segundos."), ("Veja", "o mês inteiro, numa tela."), ("Antecipe", "o que vence e o que entra."),
          ("Acompanhe", "mês a mês, em 12 meses."), ("Planeje", "com limites por categoria.")]
PREMIUM = ["Relatórios", "Comparar", "Resultado (DRE)", "Simulação futura", "Remessas ao exterior"]

CSS = f"""
/* gancho */
#g{{background:{A.INK};color:#fff}}
#gEy{{position:absolute;left:90px;top:330px;width:900px;font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{A.MENTA};opacity:0}}
#gRot{{position:absolute;left:90px;top:520px;font-size:52px;font-weight:600;letter-spacing:-.025em;color:{K.DARK_TEXTO};opacity:0}}
#gNum{{position:absolute;left:84px;top:590px;width:960px;font-size:172px;line-height:1.05;font-weight:700;letter-spacing:-.055em;color:#F08A68;font-variant-numeric:tabular-nums;white-space:nowrap}}
#gNum small{{font-size:.5em;font-weight:600;letter-spacing:-.03em;margin-right:.12em}}
#gBar{{position:absolute;left:90px;top:830px;width:900px;height:44px;border-radius:22px;background:#1C241D;overflow:hidden;opacity:0}}
#gBarG{{position:absolute;left:0;top:0;height:44px;background:{A.MENTA}}}
#gBarC{{position:absolute;top:0;height:44px;background:#F08A68}}
#gLeg{{position:absolute;left:90px;top:896px;width:900px;font-size:34px;font-weight:600;color:{K.DARK_TEXTO};letter-spacing:-.015em;opacity:0}}
#gLeg b{{color:#F08A68}}
#gH{{position:absolute;left:90px;top:1060px;width:900px;font-size:168px;line-height:.98;font-weight:700;letter-spacing:-.055em;color:#fff}}
/* marca */
#mLogo{{position:absolute;left:0;top:380px;width:1080px;display:flex;justify-content:center;opacity:0}}
#mH{{position:absolute;left:90px;top:880px;width:900px;text-align:center;font-size:112px;line-height:1.0;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#mH b{{color:{A.BRAND_DARK};font-weight:700}}
#mS{{position:absolute;left:140px;top:1140px;width:800px;text-align:center;font-size:44px;line-height:1.28;font-weight:500;letter-spacing:-.02em;color:{A.MUTED};opacity:0;text-wrap:balance}}
/* painel do Premium */
#pm{{background:{KV.FUNDO_PREMIUM};color:#fff}}
#pmAnel{{position:absolute;right:-320px;bottom:-360px;width:1200px;height:1200px;border-radius:50%;border:100px solid rgba(255,255,255,.05)}}
#pmEy{{position:absolute;left:90px;top:330px;width:900px;display:flex;align-items:center;gap:16px;font-size:32px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{KV.OURO_CLARO};opacity:0}}
#pmEy svg{{width:44px;height:44px}}
#pmH{{position:absolute;left:90px;top:420px;width:900px;font-size:100px;line-height:1.0;font-weight:700;letter-spacing:-.05em}}
.chip2{{position:absolute;left:90px;width:900px;height:104px;border-radius:32px;background:rgba(255,255,255,.1);box-shadow:inset 0 0 0 2px rgba(255,255,255,.14);
  display:flex;align-items:center;gap:26px;padding:0 36px;font-size:48px;font-weight:600;letter-spacing:-.03em;opacity:0}}
.chip2 svg{{width:44px;height:44px;flex:none}}
#pmP{{position:absolute;left:90px;top:1372px;width:900px;font-size:44px;font-weight:600;letter-spacing:-.02em;color:#D9F3E7;opacity:0}}
#pmP b{{color:#fff}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  <div id="mLogo">{A.logo_vertical("color", 330)}</div>
  <div id="mH">{KV.mk("mH1", "O timtimcash")}{KV.mk("mH2", "<b>mostra.</b>")}</div>
  <div id="mS">Suas finanças pessoais, no navegador do computador ou do celular.</div>
  {"".join(KV.verbo(i + 1, w, a) for i, (w, a) in enumerate(VERBOS))}
  <div class="nota2" id="nota">{KV.NOTA}</div>
  {KV.aparelho("fone", "tela", IMGS, K.aneis("aVal", "aCat", "aMov", "aVence") + K.toques("tq"))}
</div>

<div class="cena" id="pm" style="transform:translateY(1920px)">
  <div id="pmAnel"></div>
  <div id="pmEy">{KV.coroa("", KV.OURO_CLARO)}timtimcash Premium</div>
  <div id="pmH">{KV.mk("pmH1", "E, quando quiser")}{KV.mk("pmH2", "ir mais fundo.")}</div>
  {"".join(f'<div class="chip2" id="ch{i}" style="top:{700 + 124 * i}px">{KV.coroa("", KV.OURO_CLARO)}{n}</div>' for i, n in enumerate(PREMIUM))}
  <div id="pmP"><b>R$ 14,90</b> por mês, ou <b>R$ 149</b> por ano.</div>
</div>

<div class="cena" id="g">
  <div id="gEy">Novembro, até o dia 21 · exemplo</div>
  <div id="gRot">Despesas do mês</div>
  <div id="gNum"><small>R$</small><span id="gN">0,00</span></div>
  <div id="gBar"><div id="gBarG"></div><div id="gBarC"></div></div>
  <div id="gLeg"><b>73,6%</b> da receita</div>
  <div id="gH">{KV.mk("gH1", "Para onde")}{KV.mk("gH2", "foi?")}</div>
</div>

{K.fim("Comece grátis.", "Sem prazo e sem cartão. No navegador, no computador ou no celular.")}
"""

JS = f"""
const G_SAI={T.GANCHO_SAI}, M_SAI={T.MARCA_SAI}, FONE={T.FONE}, S=[{T.LANCE},{T.VEJA},{T.ANTECIPE},{T.ACOMPANHE},{T.PLANEJE}], PM={T.PREMIUM}, CHIPS={T.CHIPS}, FIM={T.FIM};
const SUG={T.SUGERIDA}, TOQUE={T.TOQUE}, LANCADA={T.LANCADA};
const VAL={VAL}, CAT={CAT}, CTA={CTA}, MOV={MOV}, VENCE={VENCE};
const FOTOS={json.dumps(FOTOS)};
// câmera (px CSS da foto no centro da janela de 780 x 780 no alto do aparelho)
const CAM=[[0,0,195,282,1], [6.78,7.18,195,470,1], [S[1]+.05,S[1]+.95,195,530,1.03], [9.9,10.75,195,1010,1],
  [S[2],S[2]+.01,195,400,1], [S[2]+.3,S[3],195,430,1.04], [S[3],S[3]+.01,195,400,1], [S[3]+.25,S[4]-.2,195,640,1],
  [S[4],S[4]+.01,195,1130,1], [S[4]+.3,PM,195,1215,1.03]];
function render(t){{
  // 1. gancho: as despesas do mês somam, e a pergunta
  $('gEy').style.opacity = lin(t, 0, .2);
  $('gRot').style.opacity = lin(t, .05, .25);
  const v = 7331.20*pout(t, -.25, 1.0); $('gN').textContent = fmt(v, 2);
  $('gNum').style.transform = `scale(${{(1 + .05*Math.sin(Math.PI*clamp((t-1.0)/.3, 0, 1))).toFixed(4)}})`; $('gNum').style.transformOrigin = '0 60%';
  $('gBar').style.opacity = lin(t, .1, .3); const f = pout(t, .15, 1.05);
  $('gBarG').style.width = (900*.264*f)+'px'; $('gBarC').style.left = (900*.264*f)+'px'; $('gBarC').style.width = (900*.736*f)+'px';
  $('gLeg').style.opacity = lin(t, .9, 1.15);
  sobeTxt('gH1', t, 1.0, 0, .5); sobeTxt('gH2', t, 1.14, 0, .5);
  saiCima('g', t, G_SAI);

  // 2. a marca
  const lg = $('mLogo'); const pl = pback(t, G_SAI+.1, G_SAI+.65), ql = prog(t, M_SAI-.1, M_SAI+.2);
  lg.style.opacity = Math.min(lin(t, G_SAI+.1, G_SAI+.3), 1-ql); lg.style.transform = `translateY(${{(-ql*60).toFixed(1)}}px) scale(${{(.8+.2*pl).toFixed(4)}})`;
  sobeTxt('mH1', t, G_SAI+.3, M_SAI-.05, .5); sobeTxt('mH2', t, G_SAI+.45, M_SAI, .5);
  some('mS', t, G_SAI+.8, M_SAI-.1, 20);

  // 3. as telas reais, dentro do aparelho
  fone('fone', t, FONE, PM-.1); nota2('nota', t, FONE, PM-.15);
  for (let i=0;i<5;i++) verbo(i+1, t, S[i] + (i ? 0 : -.05), (i<4 ? S[i+1] : PM) - .28);
  desliza('tela_d', t, [S[2], S[3], S[4]]);
  const cam = camera('tela', t, CAM, 780, 780);
  fotos(FOTOS, t);
  anelCam('aVal', VAL, cam, 6, 780, 780); anelP('aVal', t, {T.TECLAS_VALOR[0]} - .1, 5.75);
  anelCam('aCat', CAT, cam, 2, 780, 780); anelP('aCat', t, SUG + .05, TOQUE - .05);
  toqueCam('tq', ...cxm(CTA), cam, 780, 780); toque('tq', t, TOQUE);
  if (t >= LANCADA){{ $('t_tq').style.opacity = 0; $('o_tq').style.opacity = 0; }}
  anelCam('aMov', MOV, cam, 6, 780, 780); anelP('aMov', t, S[1]+.95, 9.8);
  anelCam('aVence', VENCE, cam, 6, 780, 780); anelP('aVence', t, S[2]+.55, S[3]-.25);

  // 4. o Premium, em uma cena
  sobe('pm', t, PM);
  $('pmAnel').style.transform = `rotate(${{(10*(t-PM)).toFixed(2)}}deg)`;
  some('pmEy', t, PM+.3, 0, 18); sobeTxt('pmH1', t, PM+.35, 0, .5); sobeTxt('pmH2', t, PM+.48, 0, .5);
  CHIPS.forEach((a, i) => {{ const e = $('ch'+i); const p = pback(t, a, a+.42); e.style.opacity = lin(t, a, a+.12);
    e.style.transform = `translateX(${{((1-p)*-70).toFixed(1)}}px)`; }});
  some('pmP', t, CHIPS[4]+.35, 0, 18);

  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('papel')}
  <div style="position:absolute;left:90px;top:440px;width:900px;font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{A.BRAND_DARK}">Conheça em 24 segundos</div>
  <div style="position:absolute;left:90px;top:500px;width:900px;font-size:148px;line-height:.98;font-weight:700;letter-spacing:-.055em;color:{A.INK}">Para onde foi o seu <span style="color:{A.BRAND_DARK}">dinheiro?</span></div>
  <div style="position:absolute;left:92px;top:958px;font-size:26px;font-weight:500;color:{A.MUTED}">{KV.NOTA}</div>
  <div class="fone" style="opacity:1;top:1030px;transform:rotate(-4deg) translateX(20px)"><div class="visor"><img src="file://{t('dashboard')}" style="position:absolute;left:0;top:-250px;width:780px"></div></div>"""
    return K.pagina_capa(corpo, KV.CSS, fundo="papel")


if __name__ == "__main__":
    K.executar(KV.pagina(CORPO, CSS, JS), T.DUR, SAIDA, TRAB, capa_html=capa())
