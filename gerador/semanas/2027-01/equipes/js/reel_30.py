# -*- coding: utf-8 -*-
"""Reel de 30/01/2027 (sábado) · "5 minutos no sábado. 3 telas." · fecha a série Comece 2027 · capa verde · equipe js.

Telas reais: captura_30.py, build 2026-10-19.5, celular 390 × 1000 em escala 3, conta fictícia de J/base_app (sem mudança), relógio
da página em 30/01/2027 10:00 (sábado). A revisão da semana, em três telas:
1. Visão geral (Janeiro 2027, "Realizado"): "Movimento de janeiro 2027 · PARCIAL · A receita cobriu 89,4% das despesas · Receitas
   R$ 9.960,00 · Despesas R$ 11.139,90 · Resultado negativo do período R$ 1.179,90" (janeiro tem IPVA e material escolar).
2. Pendentes: Janeiro 2027 "Tudo em dia"; um toque na seta "›" (Fevereiro 2027): "EM 6 DIAS · 05/02/2027 · Salário +R$ 9.960,00";
   "10/02/2027": Aluguel −R$ 2.300,00, Escola −R$ 1.450,00 e IPTU 2027 · 1ª parcela −R$ 215,00 (todos pendentes).
3. Orçamentos (de volta a Janeiro 2027): "30 de 31 dias · 97% do período", "77% do limite"; em "Progresso por categoria", Mercado
   "Já passou do limite" (R$ 2.099 de R$ 2.000, 105%, "Excedeu em R$ 99"); Bares e restaurantes no limite (97%) e três tranquilas.
Fecha a série: os 4 selos da equipe ja (equipes/ja/selo_comece2027.py) e "Os 4 passos de janeiro viram 5 minutos por semana."
O relógio do gancho é um desenho (0:00 a 5:00): os 5 minutos são a proposta do hábito, não uma medida do site.

python3 reel_30.py  |  REEL_PREVIA="0 0.5 1 1.8 3.8 5.8 7.6 8.4 10 12 14.2 16.6 19.6" python3 reel_30.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A, SELO = C.K, C.A, C.SELO
MENOS = C.MENOS

PASTA = "2027-01-30_reel-revisao-de-sabado"
SAIDA = C.saida(PASTA)
TELAS = C.telas(PASTA)
TRAB = C.trabalho("30")
CX = C.caixas(PASTA)
V1, V2, V3, V4, V5 = (CX[f"celular-{n}.jpg"] for n in ["1-visao-geral", "2-pendentes-janeiro", "3-pendentes-fevereiro", "4-orcamentos",
                                                         "5-orcamentos-progresso"])

# ---------------------------------------------------------------- conferência com a tela
t1 = V1["texto"].replace("\n", " | ")
assert "Movimento de janeiro 2027 | PARCIAL | A receita cobriu 89,4% das despesas" in t1
assert "Receitas R$ 9.960,00 | Despesas R$ 11.139,90 | Resultado negativo do período | R$ 1.179,90" in t1
assert V1["periodo"][4] == "Janeiro 2027" and V1["modo"][4] == "Realizado"
assert V2["tudo"][4].startswith("Tudo em dia") and V2["periodo"][4] == "Janeiro 2027"
assert V3["periodo"][4] == "Fevereiro 2027" and V3["em6"][4] == "EM 6 DIAS" and "05/02/2027" in V3["texto"]
assert V3["l_salario"][4] == "Salário FIXA·Salário·Conta corrente +R$ 9.960,00 pendente"
assert V3["l_aluguel"][4] == "Aluguel FIXA·Casa·Conta corrente −R$ 2.300,00 pendente" and V3["dia10"][4] == "10/02/2027"
assert V3["l_escola"][4] == "Escola FIXA·Educação·Conta corrente −R$ 1.450,00 pendente"
assert V3["l_iptu"][4] == "IPTU 2027 · 1ª parcela Impostos e Taxas·Conta corrente −R$ 215,00 pendente"
assert "Nada vencido." in V3["texto"] and CX["periodo_depois_da_volta"] == "Janeiro 2027"
assert "30 de 31 dias · 97% do período | 77% do limite | 97% do período" in V4["texto"].replace("\n", " | ")
assert V5["l_mercado"][4] == "Mercado R$ 2.099 de R$ 2.000 105% Excedeu em R$ 99 e, no ritmo, fecha em R$ 2.169 8% ACIMA"
assert V5["l_bares"][4].startswith("Bares e restaurantes R$ 583 de R$ 600 97%") and "TRANQUILAS | 3 categorias" in V5["texto"].replace("\n", " | ")
assert "Sat Jan 30 2027" in CX["relogio"]

# ---------------------------------------------------------------- caixas (px CSS da foto)
f = lambda k, F: C.na_foto(F[k][:4], F["rolagem"])
MOV = [25, V1["movimento"][1] - 6, 340, V1["resultado"][1] + V1["resultado"][3] - V1["movimento"][1] + 14]
COB = C.uniao(V1["cobriu"][:4], V1["barra"][:4])
COB = [25, COB[1] - 6, 340, COB[3] + 12]
TUDO = V2["tudo"][:4]
PROX = V2["setas"][1][1:5]
SAL = C.uniao(V3["em6"][:4], V3["l_salario"][:4])
DIA10 = C.uniao(V3["dia10"][:4], V3["l_aluguel"][:4], V3["l_escola"][:4], V3["l_iptu"][:4])
RITMO = [27, V4["ritmo"][1] - 8, 336, V4["pct_lim"][1] + V4["pct_lim"][3] + 26 - V4["ritmo"][1]]
MERC = f("l_mercado", V5)

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.6
T1A, T1B = (2.9, 4.8), (4.95, 6.75)
T2A, T2B = (6.95, 8.85), (9.0, 10.95)
T3A, T3B = (11.15, 13.05), (13.2, 15.2)
X_V2, TQ_PROX, X_V4, X_V5 = 6.85, 7.95, 11.05, 13.1
J_SAI = 15.25
S4 = 15.4
FIM = 18.65
DUR = 21.4

IMGS = [("v1", os.path.join(TELAS, "celular-1-visao-geral.jpg")), ("v2", os.path.join(TELAS, "celular-2-pendentes-janeiro.jpg")),
        ("v3", os.path.join(TELAS, "celular-3-pendentes-fevereiro.jpg")), ("v4", os.path.join(TELAS, "celular-4-orcamentos.jpg")),
        ("v5", os.path.join(TELAS, "celular-5-orcamentos-progresso.jpg"))]
EXTRA = K.aneis("aMov", "aCob", "aTudo", "aSal", "aDia10", "aRitmo") + K.aneis("aMerc", cor="coral") + K.toques("tqProx")

R_REL = 215
CIRC = round(2 * 3.14159265 * R_REL, 1)

CSS = f"""
#g{{background:{A.INK}}}
#gTop{{position:absolute;left:90px;top:300px;width:900px}}
#gTop .h1{{font-size:112px;line-height:.98;margin-top:34px;color:#fff}}
#gTop .h1 b{{color:{A.MENTA};font-weight:700}}
#rel{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
#relT{{position:absolute;left:240px;top:{1065 - 82}px;width:600px;text-align:center;font-size:164px;line-height:164px;font-weight:700;letter-spacing:-.05em;
  color:#fff;font-variant-numeric:tabular-nums}}
#relS{{position:absolute;left:340px;top:{1065 + 92}px;width:400px;text-align:center;font-size:34px;font-weight:600;color:{K.DARK_TEXTO};letter-spacing:.02em}}
#chips{{position:absolute;left:90px;top:1400px;width:900px;display:flex;justify-content:center;gap:14px}}
.ch{{display:inline-flex;align-items:center;gap:12px;height:80px;padding:0 24px 0 12px;border-radius:999px;background:#1C241D;box-shadow:inset 0 0 0 3px #34413A;
  font-size:31px;font-weight:600;color:#fff;letter-spacing:-.01em;white-space:nowrap;opacity:0}}
.ch i{{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:50%;background:{A.MENTA};color:{A.INK};font-weight:700}}
.tit .nn{{color:{A.BRAND_DARK}}}
/* fecho da série (tinta) */
#s4 .h2{{position:absolute;left:90px;top:330px;width:900px;font-size:84px;line-height:1.02;color:#fff;letter-spacing:-.045em;font-weight:700;text-wrap:balance}}
#s4 .h2 b{{color:{A.MENTA}}}
#selos{{position:absolute;left:0;top:690px;width:1080px;display:flex;justify-content:center;gap:40px}}
.sl{{position:relative;opacity:0}}
.ok{{position:absolute;right:-14px;top:-14px;width:64px;height:64px;border-radius:50%;background:{A.MENTA};border:6px solid {A.INK};display:flex;align-items:center;justify-content:center;opacity:0}}
#s4n{{position:absolute;left:90px;top:1150px;width:900px;text-align:center;font-size:44px;line-height:1.3;font-weight:600;color:{K.DARK_TEXTO};letter-spacing:-.02em;opacity:0;text-wrap:balance}}
#s4n b{{color:#fff}}
"""

CHECK = (f'<svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="{A.INK}" stroke-width="3.4" stroke-linecap="round" '
         f'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1a"><span class="nn">1 ·</span> Visão geral: <b>como vai o mês?</b></div>
  <div class="tit" id="t1b">A receita cobriu <b>89,4%</b> das despesas de janeiro, mês de IPVA e material.</div>
  <div class="tit" id="t2a"><span class="nn">2 ·</span> Pendentes: <b>o que vem por aí?</b></div>
  <div class="tit" id="t2b">Em 6 dias, o salário. No dia 10, <b>aluguel, escola e IPTU</b>.</div>
  <div class="tit" id="t3a"><span class="nn">3 ·</span> Orçamentos: <b>o ritmo do mês</b>.</div>
  <div class="tit" id="t3b">Mercado passou do limite (<span style="color:{A.RED_TEXT}">105%</span>). As outras quatro, <b>dentro</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", IMGS)}{EXTRA}</div>
</div>

<div class="cena tinta" id="s4" style="transform:translateY(1920px)">
  <div class="h2">Os 4 passos de janeiro viram <b>5 minutos por semana</b>.</div>
  <div id="selos">{"".join(f'<div class="sl" id="sl{n}">{SELO.selo_com_nome(n, 188, "tinta")}<div class="ok" id="ok{n}">{CHECK}</div></div>' for n in range(1, 5))}</div>
  <div id="s4n">Todo sábado: <b>Visão geral</b>, <b>Pendentes</b> e <b>Orçamentos</b>.</div>
</div>

<div class="cena tinta" id="g">
  <div id="gTop">
    <div class="eyebrow">{SELO.sobretitulo()} · revisão da semana</div>
    <div class="h1">5 minutos no sábado. <b>3 telas.</b></div>
  </div>
  <svg id="rel" viewBox="0 0 1080 1920">
    <circle cx="540" cy="1065" r="{R_REL}" fill="none" stroke="#24302A" stroke-width="30"/>
    <circle id="relP" cx="540" cy="1065" r="{R_REL}" fill="none" stroke="{A.MENTA}" stroke-width="30" stroke-linecap="round"
      stroke-dasharray="{CIRC} {CIRC}" stroke-dashoffset="{CIRC}" transform="rotate(-90 540 1065)"/>
  </svg>
  <div id="relT">0:00</div>
  <div id="relS">minutos</div>
  <div id="chips"><span class="ch" id="ch1"><i>1</i>Visão geral</span><span class="ch" id="ch2"><i>2</i>Pendentes</span><span class="ch" id="ch3"><i>3</i>Orçamentos</span></div>
</div>

{K.fim("Comece 2027 organizado.", "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro, no computador ou no celular.")}
"""

JS = f"""
const G_SAI={G_SAI}, T1A={list(T1A)}, T1B={list(T1B)}, T2A={list(T2A)}, T2B={list(T2B)}, T3A={list(T3A)}, T3B={list(T3B)};
const X_V2={X_V2}, TQ_PROX={TQ_PROX}, X_V4={X_V4}, X_V5={X_V5}, J_SAI={J_SAI}, S4={S4}, FIM={FIM}, CIRC={CIRC};
const MOV={MOV}, COB={COB}, TUDO={TUDO}, PROX={PROX}, SAL={SAL}, DIA10={DIA10}, RITMO={RITMO}, MERC={MERC};
const FOTOS=[[0,'v1'],[X_V2,'v2'],[TQ_PROX+.15,'v3'],[X_V4,'v4'],[X_V5,'v5']];
function cx(r){{ return [r[0] + r[2]/2, r[1] + r[3]/2]; }}
// troca de tela (outra página do site): a janela sai pela esquerda e volta pela direita com a tela nova, trocada no meio
function deslize(t, trocas){{ let x = 0; trocas.forEach(s => {{ if (t >= s - .24 && t < s) x = -940*prog(t, s - .24, s);
  else if (t >= s && t < s + .3) x = 940*(1 - pout(t, s, s + .3)); }}); return x; }}
// câmera: o movimento do mês; Pendentes de janeiro; fevereiro (desce até o dia 10); o topo de Orçamentos; o progresso por categoria
const CAM = [[0,0,195,470,1], [X_V2,X_V2+.01,195,300,1], [8.45,9.0,195,640,1], [X_V4,X_V4+.01,195,330,1], [X_V5,X_V5+.01,195,420,1]];
function render(t){{
  // 1. gancho (tinta): o relógio anda até 5:00
  const seg = 300*pout(t, -.55, 1.45);
  const mm = Math.floor(seg/60), ss = Math.floor(seg % 60);
  $('relT').textContent = mm + ':' + String(ss).padStart(2, '0');
  $('relP').setAttribute('stroke-dashoffset', (CIRC*(1 - seg/300)).toFixed(1));
  const pulso = 1 + .07*Math.sin(Math.PI*clamp((t-1.45)/.35, 0, 1));
  $('relT').style.transform = `scale(${{pulso.toFixed(3)}})`;
  [1,2,3].forEach(i => {{ const a = .75 + .18*i; $('ch'+i).style.opacity = lin(t, a, a+.15);
    $('ch'+i).style.transform = `translateY(${{(30*(1 - pout(t, a, a+.4))).toFixed(1)}}px)`; }});
  saiCima('g', t, G_SAI);

  // 2. a tela real: as três telas da revisão
  titulo('t1a', t, T1A[0], T1A[1]); titulo('t1b', t, T1B[0], T1B[1]); titulo('t2a', t, T2A[0], T2A[1]);
  titulo('t2b', t, T2B[0], T2B[1]); titulo('t3a', t, T3A[0], T3A[1]); titulo('t3b', t, T3B[0], T3B[1]);
  janela('janela', t, G_SAI+.15, J_SAI); nota('nota', t, G_SAI+.15, J_SAI);
  $('janela').style.transform += ` translateX(${{deslize(t, [X_V2, X_V4]).toFixed(1)}}px)`;
  const cam = camera('tela', t, CAM);
  fotos(FOTOS, t);
  anelCam('aMov', MOV, cam, 6); anel('aMov', t, 3.3, T1A[1]);
  anelCam('aCob', COB, cam, 6); anel('aCob', t, 5.3, X_V2-.35);
  anelCam('aTudo', TUDO, cam, 4); anel('aTudo', t, 7.2, TQ_PROX-.05);
  toqueCam('tqProx', ...cx(PROX), cam); toque('tqProx', t, TQ_PROX);
  if (t >= TQ_PROX + .2){{ $('t_tqProx').style.opacity = 0; $('o_tqProx').style.opacity = 0; }}
  anelCam('aSal', SAL, cam, 6); anel('aSal', t, 9.15, X_V4-.35);
  anelCam('aDia10', DIA10, cam, 6); anel('aDia10', t, 9.55, X_V4-.35);
  anelCam('aRitmo', RITMO, cam, 6); anel('aRitmo', t, 11.55, X_V5-.35);
  anelCam('aMerc', MERC, cam, 6); anel('aMerc', t, 13.55, T3B[1]);

  // 3. fecho da série: os 4 passos e os 5 minutos por semana
  sobe('s4', t, S4);
  [1,2,3,4].forEach(n => {{ const a = S4 + .45 + .17*(n-1);
    salta('sl'+n, t, a, .45); const k = a + .45; $('ok'+n).style.opacity = lin(t, k, k+.12);
    $('ok'+n).style.transform = `scale(${{(.5 + .5*pback(t, k, k+.35)).toFixed(3)}})`; }});
  some('s4n', t, S4 + 1.5, 0, 20);

  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    r, circ = 190, round(2 * 3.14159265 * 190, 1)
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">{SELO.sobretitulo()} · revisão da semana</div>
    <div class="h1" style="font-size:128px;line-height:.96;margin-top:36px;text-wrap:balance">5 minutos no sábado.</div>
  </div>
  <svg style="position:absolute;left:0;top:0;overflow:visible" width="1080" height="1920" viewBox="0 0 1080 1920">
    <circle cx="540" cy="1050" r="{r}" fill="none" stroke="{A.BRAND_DARK}" stroke-width="28"/>
    <circle cx="540" cy="1050" r="{r}" fill="none" stroke="#fff" stroke-width="28" stroke-linecap="round"
      stroke-dasharray="{circ} {circ}" stroke-dashoffset="0" transform="rotate(-90 540 1050)"/>
  </svg>
  <div style="position:absolute;left:0;top:{1050 - 74}px;width:1080px;text-align:center;font-size:150px;line-height:150px;font-weight:700;letter-spacing:-.05em;color:#fff;font-variant-numeric:tabular-nums">5:00</div>
  <div style="position:absolute;left:0;top:1330px;width:1080px;display:flex;justify-content:center;gap:34px">{"".join(SELO.selo(n, 124, "verde") for n in range(1, 5))}</div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


if __name__ == "__main__":
    K.executar(C.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
