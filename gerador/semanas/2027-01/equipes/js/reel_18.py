# -*- coding: utf-8 -*-
"""Reel de 18/01/2027 (segunda) · "E se 2027 apertar?" · Comece 2027 · passo 4 de 4 (a rota) · capa tinta · equipe js.

Telas reais: captura_18.py, build 2026-10-19.5, celular 390 px CSS em escala 3, conta fictícia de J/base_app (sem mudança),
relógio da página em 18/01/2027 10:00. Simulação futura -> "Cenário base" -> o resultado ("Saldo em set/27 R$ 29.000",
"+R$ 1.646 por mês · 9 meses") -> "E se…": "Receita −10%" ("O saldo final cai R$ 8.964 (31%), de R$ 29.000 para R$ 20.036.")
-> "Inflação 5% a.a." ("O saldo final cai R$ 1.152 (4%), de R$ 29.000 para R$ 27.847.") -> "Remover susto" (volta o
"Testa um susto sobre o cenário, sem alterar nada."). O saldo do topo fica em R$ 29.000 nas cinco fotos: o teste não muda o cenário.
O gancho desenha o saldo projetado com os números da linha do tempo do site (partida R$ 14.180; jan/27 R$ 11.560, com o ajuste
de R$ 4.800 em impostos do cenário; +R$ 2.180 por mês de fev/27 a set/27; set/27 R$ 29.000) e a linha do susto "Receita −10%"
calculada como o site calcula (receita de R$ 9.960 × 0,9 = R$ 8.964 por mês: jan/27 R$ 10.564, +R$ 1.184 por mês, set/27
R$ 20.036, a mesma queda de R$ 8.964 que o site mostra). Diferença para o carrossel de 21/10 ("Perde a maior renda"): aqui são
outros testes, em vídeo; não repete o "Definir uma meta" de 30/12.
Título do quadro de 13,5 a 15,6 s (revisão de 20/10/2026): "O susto é só um teste: o plano não muda.", com o anel na frase do site que
o confirma ("Testa um susto sobre o cenário, sem alterar nada.").
O site arredonda os saldos: R$ 29.000 − R$ 27.847 dá R$ 1.153, e o site diz "cai R$ 1.152"; o vídeo mostra só os saldos finais e
os percentuais (−31% e −4%), sem a diferença em reais da inflação.

python3 reel_18.py  |  REEL_PREVIA="0 0.5 1 1.6 3.6 6 9.2 12 14.5 17 19.5" python3 reel_18.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A, SELO = C.K, C.A, C.SELO
MENOS = C.MENOS

PASTA = "2027-01-18_reel-passo-4-e-se-2027-apertar"
SAIDA = C.saida(PASTA)
TELAS = C.telas(PASTA)
TRAB = C.trabalho("18")
CX = C.caixas(PASTA)
F1, F2, F3, F4, F5 = (CX[f"celular-simulacao-{n}.jpg"] for n in ["1-cenarios", "2-resultado", "3-receita", "4-inflacao", "5-sem-susto"])

# ---------------------------------------------------------------- conferência com a tela
for f in (F2, F3, F4, F5):
    assert "hero: Saldo em set/27 | R$29.000 | +R$ 1.646 por mês · 9 meses" in f["texto"], f["texto"][:120]
assert "Testa um susto sobre o cenário, sem alterar nada." in F2["texto"] and "Testa um susto sobre o cenário, sem alterar nada." in F5["texto"]
assert "O saldo final cai R$ 8.964 (31%), de R$ 29.000 para R$ 20.036." in F3["texto"] and CX["pressionado_3"] == ["Receita −10%"]
assert "Toda receita cai 10% pelo horizonte inteiro." in F3["texto"]
assert "O saldo final cai R$ 1.152 (4%), de R$ 29.000 para R$ 27.847." in F4["texto"] and CX["pressionado_4"] == ["Inflação 5% a.a."]
assert "As despesas sobem 5% ao ano, compostos mês a mês." in F4["texto"]
assert CX["pressionado_5"] == [] and "Remover susto" not in F5["texto"]
assert "Cenário base" in F1["texto"] and "R$ 29 mil" in F1["texto"] and "9 meses · até set/27 · +R$ 1.646 por mês" in F1["texto"]
LT = CX["linha_do_tempo"].replace("\n", " | ")
assert "Saldo de partida | R$ 14.180" in LT and "saldo em jan/27: R$ 11.560" in LT and "+R$ 2.180/mês" in LT
assert "saldo em ago/27: R$ 26.820" in LT and "set/27 | R$ 29.000" in LT
assert "Jan 18 2027" in CX["relogio"]
BASE = [14180, 11560] + [11560 + 2180 * k for k in range(1, 9)]
assert BASE[-1] == 29000 and BASE[-2] == 26820 and len(BASE) == 10
SUSTO = [14180, 14180 + 8964 - 12580] + [14180 + 8964 - 12580 + (8964 - 7780) * k for k in range(1, 9)]
assert SUSTO[1] == 10564 and SUSTO[-1] == 20036 and BASE[-1] - SUSTO[-1] == 8964
FINAIS = [("Cenário base", 29000, None), ("Receita " + MENOS + "10%", 20036, 31), ("Inflação 5% a.a.", 27847, 4)]
assert round(8964 / 29000 * 100) == 31 and round(1152 / 29000 * 100) == 4

# ---------------------------------------------------------------- caixas (px CSS da foto)
f2 = lambda b, F: C.na_foto(b, F["rolagem"])
BASE_CARD = F1["base"][:4]
HERO = C.uniao(f2(F2["hero_lbl"], F2), f2(F2["hero_val"], F2), f2(F2["hero_sub"], F2))
CHIP_REC = f2(F2["chip_rec"], F2)
CHIP_INF = f2(F3["chip_inf"], F3)
CAIXA3 = f2(F3["caixa_susto"], F3)
CAIXA4 = f2(F4["caixa_susto"], F4)
REMOVER = f2(F4["remover"], F4)
ES_SUB5 = f2(F5["es_sub"], F5)
GRAF = f2(F2["grafico"], F2)
assert CAIXA3 == CAIXA4 and HERO[1] > 95

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.55
T1, T2, T3, T4, T5 = (2.85, 4.95), (5.15, 7.4), (7.6, 10.35), (10.55, 13.25), (13.45, 15.6)
TQ_BASE, TQ_REC, TQ_INF, TQ_REM = 4.45, 8.1, 10.95, 13.85
J_SAI = 15.65
S6 = (15.85, 18.6)
FIM = 18.65
DUR = 21.4

IMGS = [("f1", os.path.join(TELAS, "celular-simulacao-1-cenarios.jpg")), ("f2", os.path.join(TELAS, "celular-simulacao-2-resultado.jpg")),
        ("f3", os.path.join(TELAS, "celular-simulacao-3-receita.jpg")), ("f4", os.path.join(TELAS, "celular-simulacao-4-inflacao.jpg")),
        ("f5", os.path.join(TELAS, "celular-simulacao-5-sem-susto.jpg"))]
EXTRA = K.aneis("aBase", "aHero", "aSub") + K.aneis("aCx3", "aCx4", cor="ambar") + K.toques("tqBase", "tqRec", "tqInf", "tqRem")

# ---------------------------------------------------------------- gancho: o saldo projetado e o susto
GX0, GX1, GY0, GY1, V0, V1 = 150, 700, 1420, 830, 8000, 32000
def gx(i): return GX0 + (GX1 - GX0) * i / 9
def gy(v): return GY1 + (GY0 - GY1) * (V1 - v) / (V1 - V0)
P_BASE = [[round(gx(i), 1), round(gy(v), 1)] for i, v in enumerate(BASE)]
P_SUSTO = [[round(gx(i), 1), round(gy(v), 1)] for i, v in enumerate(SUSTO)]
caminho = "M" + " L".join(f"{x} {y}" for x, y in P_BASE)
grade = "".join(f'<line x1="{GX0}" x2="{GX1 + 290}" y1="{gy(v):.1f}" y2="{gy(v):.1f}" stroke="#2A332B" stroke-width="3" stroke-dasharray="10 12"/>'
                f'<text x="{GX0 - 16}" y="{gy(v) + 10:.1f}" text-anchor="end" font-family="Inter" font-weight="600" font-size="27" fill="{K.DARK_TEXTO}">{v // 1000} mil</text>'
                for v in (10000, 20000, 30000))
rotx = (f'<text x="{GX0}" y="{GY0 + 62}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="28" fill="{K.DARK_TEXTO}">hoje</text>'
        f'<text x="{GX1}" y="{GY0 + 62}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="28" fill="{K.DARK_TEXTO}">set/27</text>')

CSS = f"""
#g{{background:{A.INK}}}
#gTop{{position:absolute;left:90px;top:300px;width:720px}}
#gTop .h1{{font-size:124px;margin-top:34px;color:#fff;line-height:.98}}
#gTop .h1 b{{color:{A.MENTA};font-weight:700}}
#gSelo{{position:absolute;left:840px;top:300px}}
#graf{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
.gv{{position:absolute;left:0;top:0;white-space:nowrap;font-weight:700;letter-spacing:-.045em;font-variant-numeric:tabular-nums}}
#gvBase{{font-size:54px;color:{A.MENTA}}}
#gvSusto{{font-size:54px;color:{A.AMBER}}}
#gTag{{position:absolute;left:0;top:0;height:64px;padding:0 26px;border-radius:999px;background:{A.AMBER};color:{A.INK};font-size:32px;font-weight:700;
  display:flex;align-items:center;white-space:nowrap;letter-spacing:-.01em;opacity:0}}
/* resumo */
#s6t{{position:absolute;left:90px;top:280px;width:900px;font-size:66px;line-height:1.06;font-weight:700;letter-spacing:-.045em;opacity:0}}
#s6t b{{color:{A.BRAND_DARK}}}
#s6s{{position:absolute;left:90px;top:440px;width:900px;font-size:36px;font-weight:600;letter-spacing:-.02em;color:{A.MUTED};opacity:0}}
.fn{{position:absolute;left:90px;width:860px;opacity:0}}
.fn .lb{{display:flex;align-items:baseline;justify-content:space-between;gap:20px}}
.fn .nm{{font-size:40px;font-weight:600;letter-spacing:-.02em;color:{A.INK}}}
.fn .vl{{font-size:76px;font-weight:700;letter-spacing:-.045em;color:{A.INK};font-variant-numeric:tabular-nums;white-space:nowrap}}
.fn .vl small{{font-size:34px;font-weight:600;margin-right:10px;color:{A.MUTED}}}
.fn .pc{{display:inline-flex;align-items:center;height:56px;padding:0 20px;border-radius:999px;font-size:30px;font-weight:700;margin-left:16px;vertical-align:middle;letter-spacing:-.01em}}
.fn .br{{height:30px;border-radius:15px;margin-top:16px;width:0}}
#s6n{{position:absolute;left:90px;top:1440px;width:900px;font-size:30px;font-weight:500;color:{A.MUTED};letter-spacing:-.01em;opacity:0}}
"""

def finais():
    cores = [A.BRAND, A.CORAL, A.AMBER]
    tons = [None, (K.CORAL_FORTE, "#F6DCD2"), (A.AMBER_TEXT, "#F5E7C8")]
    ys = [620, 860, 1100]
    out = []
    for i, ((nome, v, pct), cor, tom, y) in enumerate(zip(FINAIS, cores, tons, ys)):
        chip = f'<span class="pc" style="color:{tom[0]};background:{tom[1]}">{MENOS}{pct}%</span>' if pct else ""
        out.append(f'<div class="fn" id="fn{i}" style="top:{y}px"><div class="lb"><span class="nm">{nome}</span>'
                   f'<span class="vl"><small>R$</small>{C.brl(v, 0)}{chip}</span></div><div class="br" id="fb{i}" style="background:{cor}"></div></div>')
    return "".join(out)

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">Passo 4: na Simulação futura, abra o seu <b>cenário</b>.</div>
  <div class="tit" id="t2">No plano, setembro de 2027 chega com <b>R$&nbsp;29.000</b>.</div>
  <div class="tit" id="t3">E se a receita cair 10%? O saldo final cai para <b style="color:{A.AMBER_TEXT}">R$&nbsp;20.036</b>.</div>
  <div class="tit" id="t4">E se a inflação for de 5% ao ano? O saldo final cai para <b style="color:{A.AMBER_TEXT}">R$&nbsp;27.847</b>.</div>
  <div class="tit" id="t5">O susto é só um teste: <b>o plano não muda</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", IMGS)}{EXTRA}</div>
  <div id="s6t">O mesmo plano, <b>três finais</b>.</div>
  <div id="s6s">Saldo em set/27, no exemplo</div>
  {finais()}
  <div id="s6n">Simulação futura, Cenário base e os testes do “E se…”, com dados de exemplo.</div>
</div>

<div class="cena tinta" id="g">
  <div id="gTop">
    <div class="eyebrow">{SELO.sobretitulo(4)}</div>
    <div class="h1">E se 2027 <b>apertar</b>?</div>
  </div>
  <div id="gSelo">{SELO.selo(4, 150, "tinta")}</div>
  <svg id="graf" viewBox="0 0 1080 1920">
    {grade}{rotx}
    <path id="gBase" d="{caminho}" fill="none" stroke="{A.MENTA}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="gSusto" d="{caminho}" fill="none" stroke="{A.AMBER}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="26 20" opacity="0"/>
    <circle id="gPB" r="16" fill="{A.MENTA}" stroke="{A.INK}" stroke-width="6"/>
    <circle id="gPS" r="15" fill="{A.AMBER}" stroke="{A.INK}" stroke-width="6" opacity="0"/>
  </svg>
  <div class="gv" id="gvBase">R$ 29.000</div>
  <div class="gv" id="gvSusto" style="opacity:0">R$ 29.000</div>
  <div id="gTag">Receita {MENOS}10%</div>
</div>

{K.fim("Passo 4: a rota.", "Simulação futura no timtimcash. Acesse pelo navegador, no computador ou no celular.")}
"""

JS = f"""
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, S6={list(S6)};
const TQ_BASE={TQ_BASE}, TQ_REC={TQ_REC}, TQ_INF={TQ_INF}, TQ_REM={TQ_REM}, J_SAI={J_SAI}, FIM={FIM};
const PB={json.dumps(P_BASE)}, PS={json.dumps(P_SUSTO)};
const BASE_CARD={BASE_CARD}, HERO={HERO}, CAIXA3={CAIXA3}, CAIXA4={CAIXA4}, ES_SUB5={ES_SUB5};
const CHIP_REC={CHIP_REC}, CHIP_INF={CHIP_INF}, REMOVER={REMOVER};
const FOTOS=[[0,'f1'],[TQ_BASE+.15,'f2'],[TQ_REC+.15,'f3'],[TQ_INF+.15,'f4'],[TQ_REM+.15,'f5']];
const L = $('gBase').getTotalLength();
const LARG_FN = {[860, round(860 * 20036 / 29000, 1), round(860 * 27847 / 29000, 1)]};
function caminho(P){{ return 'M' + P.map(p => p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' L'); }}
function cx(r){{ return [r[0] + r[2]/2, r[1] + r[3]/2]; }}
// o toque que troca de página some quando a página nova aparece
function somePagina(id, t, t0){{ if (t >= t0 + .2){{ $('t_'+id).style.opacity = 0; $('o_'+id).style.opacity = 0; }} }}
// câmera: a lista de cenários; o saldo e o gráfico; o "E se…" com o gráfico e a caixa do susto
const CAM = [[0,0,195,250,1], [TQ_BASE+.15,TQ_BASE+.16,195,292,1.1], [7.35,7.9,195,487,1.0]];
function render(t){{
  // 1. gancho (tinta): a linha do saldo até set/27 e o susto que derruba o fim
  const pd = prog(t, -0.6, 0.4);
  const gb = $('gBase'); gb.style.strokeDasharray = L + ' ' + L; gb.style.strokeDashoffset = (L*(1-pd)).toFixed(1);
  const qb = gb.getPointAtLength(Math.max(.01, L*pd));
  $('gPB').setAttribute('cx', qb.x.toFixed(1)); $('gPB').setAttribute('cy', qb.y.toFixed(1));
  const ps = pout(t, .85, 1.95);
  const P = PB.map((p, i) => [p[0], p[1] + (PS[i][1] - p[1])*ps]);
  $('gSusto').setAttribute('d', caminho(P)); $('gSusto').setAttribute('opacity', lin(t, .7, .85).toFixed(3));
  const fimS = P[P.length-1];
  $('gPS').setAttribute('cx', fimS[0]); $('gPS').setAttribute('cy', fimS[1].toFixed(1)); $('gPS').setAttribute('opacity', lin(t, .7, .85).toFixed(3));
  const vb = $('gvBase'); vb.style.transform = `translate(${{(PB[9][0] + 34).toFixed(1)}}px, ${{(PB[9][1] - 34).toFixed(1)}}px)`;
  vb.style.opacity = lin(t, -.1, .15);
  const vs = $('gvSusto'); vs.textContent = 'R$ ' + fmt(29000 - 8964*ps, 0);
  vs.style.opacity = lin(t, .8, .95); vs.style.transform = `translate(${{(fimS[0] + 34).toFixed(1)}}px, ${{(fimS[1] - 34).toFixed(1)}}px)`;
  const tg = $('gTag'); tg.style.opacity = lin(t, .75, .95);
  tg.style.transform = `translate(${{(PS[4][0] - 40).toFixed(1)}}px, ${{(PB[4][1] + (PS[4][1]-PB[4][1])*ps + 44).toFixed(1)}}px) scale(${{(.7 + .3*pback(t, .75, 1.15)).toFixed(3)}})`;
  $('gSelo').style.transform = `scale(${{(.6 + .4*pback(t, -.2, .35)).toFixed(3)}})`;
  saiCima('g', t, G_SAI);

  // 2. a tela real
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, G_SAI+.15, J_SAI); nota('nota', t, G_SAI+.15, J_SAI);
  const cam = camera('tela', t, CAM);
  fotos(FOTOS, t);
  anelCam('aBase', BASE_CARD, cam, 6); anel('aBase', t, 3.3, TQ_BASE-.25);
  toqueCam('tqBase', ...cx(BASE_CARD), cam); toque('tqBase', t, TQ_BASE); somePagina('tqBase', t, TQ_BASE);
  anelCam('aHero', HERO, cam, 10); anel('aHero', t, 5.55, 7.25);
  toqueCam('tqRec', ...cx(CHIP_REC), cam); toque('tqRec', t, TQ_REC);
  anelCam('aCx3', CAIXA3, cam, 8); anel('aCx3', t, TQ_REC+.55, TQ_INF-.15);
  toqueCam('tqInf', ...cx(CHIP_INF), cam); toque('tqInf', t, TQ_INF);
  anelCam('aCx4', CAIXA4, cam, 8); anel('aCx4', t, TQ_INF+.5, TQ_REM-.3);
  toqueCam('tqRem', ...cx(REMOVER), cam); toque('tqRem', t, TQ_REM); somePagina('tqRem', t, TQ_REM);
  anelCam('aSub', ES_SUB5, cam, 10); anel('aSub', t, TQ_REM+.45, T5[1]);

  // 3. resumo: os três finais em set/27
  some('s6t', t, S6[0], FIM+.3, 30); some('s6s', t, S6[0]+.15, FIM+.3, 20);
  [0,1,2].forEach(i => {{ some('fn'+i, t, S6[0]+.35+.3*i, FIM+.3, 30); barra('fb'+i, t, S6[0]+.5+.3*i, S6[0]+1.2+.3*i, LARG_FN[i]); }});
  some('s6n', t, S6[0]+1.4, FIM+.3, 10);

  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    # mini gráfico: a linha do plano (menta) e a do susto (âmbar, tracejada), com os dois finais
    X0, X1, Y0, Y1 = 120, 690, 1480, 1000
    def px(i): return X0 + (X1 - X0) * i / 9
    def py(v): return Y1 + (Y0 - Y1) * (32000 - v) / (32000 - 8000)
    pb = "M" + " L".join(f"{px(i):.1f} {py(v):.1f}" for i, v in enumerate(BASE))
    pss = "M" + " L".join(f"{px(i):.1f} {py(v):.1f}" for i, v in enumerate(SUSTO))
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:440px;width:640px">
    <div class="eyebrow">{SELO.sobretitulo(4)}</div>
    <div class="h1" style="font-size:132px;line-height:.96;margin-top:40px;color:#fff">E se 2027 <span style="color:{A.MENTA}">apertar</span>?</div>
  </div>
  <div style="position:absolute;left:760px;top:470px">{SELO.selo(4, 230, "tinta")}</div>
  <svg style="position:absolute;left:0;top:0;overflow:visible" width="1080" height="1920" viewBox="0 0 1080 1920">
    <line x1="{X0}" x2="{X1 + 300}" y1="{py(20000):.1f}" y2="{py(20000):.1f}" stroke="#2A332B" stroke-width="4" stroke-dasharray="12 14"/>
    <line x1="{X0}" x2="{X1 + 300}" y1="{py(30000):.1f}" y2="{py(30000):.1f}" stroke="#2A332B" stroke-width="4" stroke-dasharray="12 14"/>
    <path d="{pb}" fill="none" stroke="{A.MENTA}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="{pss}" fill="none" stroke="{A.AMBER}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="30 22"/>
    <circle cx="{px(9):.1f}" cy="{py(29000):.1f}" r="22" fill="{A.MENTA}" stroke="{A.INK}" stroke-width="8"/>
    <circle cx="{px(9):.1f}" cy="{py(20036):.1f}" r="20" fill="{A.AMBER}" stroke="{A.INK}" stroke-width="8"/>
  </svg>
  <div class="cv" style="left:{px(9) + 40:.0f}px;top:{py(29000) - 36:.0f}px;color:{A.MENTA}">R$ 29.000</div>
  <div class="cv" style="left:{px(9) + 40:.0f}px;top:{py(20036) - 36:.0f}px;color:{A.AMBER}">R$ 20.036</div>"""
    css = """.cv{position:absolute;white-space:nowrap;font-size:58px;font-weight:700;letter-spacing:-.045em;font-variant-numeric:tabular-nums}"""
    return K.pagina_capa(corpo, css, fundo="tinta")


if __name__ == "__main__":
    K.executar(C.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
