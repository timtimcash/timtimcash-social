# -*- coding: utf-8 -*-
"""Reel de 04/11/2026 · "Quanto foi na farmácia?" (capa tinta), 1080 × 1920, 30 fps, 19,4 s. Equipe r1b (a partir da r1).
Versão de 17/10/2026, a pedido do Samuel: nem delivery (16/10) nem combustível (17/10); assinaturas já estão no carrossel de
07/11, então ficou a farmácia. As versões anteriores ficam em reel_04_delivery.py e reel_04_combustivel.py.

Telas reais do build 2026-10-16.1 (capturas/captura04.py): Transações no celular com o relógio em 04/11/2026 19:30,
tudo pela interface: período "Ano atual" (Ano 2026) e a busca "farmácia" digitada letra a letra (uma foto real depois
de cada letra). A soma do filtrado: "20 transações · 20 pagas · 0 pendentes · somam R$ 3.085,34 · 711 no histórico".
Mês a mês (conta de exemplo, duas compras por mês, nenhuma em novembro até o dia 4): jan 355,12 · fev 355,41 · mar 325,30 ·
abr 339,42 · mai 346,62 · jun 358,01 · jul 351,40 · ago 376,56 · set 133,20 · out 144,30. Média de jan a out: R$ 308,53.
Buscas na mesma tela (Ano 2026): padaria R$ 1.047,14 (10) · cinema R$ 1.994,55 (9) · luz R$ 2.037,50 (10).

python3 reel_04.py  |  REEL_PREVIA="0 1 2.4 5 6.6 8.8 11.8 14.2 15.9 18" python3 reel_04.py
"""
import os, sys, json
from decimal import Decimal as D
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-11-04_reel-farmacia-em-2026"
TRAB = os.path.join(AQUI, "trabalho", "04f")
TELAS = os.path.join(N, "saida", PASTA, "telas")
SAIDA = os.path.join(N, "saida", PASTA)
DUR = 19.4

CX = json.load(open(os.path.join(TRAB, "caixas.json"), encoding="utf-8"))
ARQ = CX["arquivos"]

# ---------------------------------------------------------------- números (conferidos contra a tela)
MESES = [("jan", "355.12"), ("fev", "355.41"), ("mar", "325.30"), ("abr", "339.42"), ("mai", "346.62"), ("jun", "358.01"),
         ("jul", "351.40"), ("ago", "376.56"), ("set", "133.20"), ("out", "144.30")]
TOTAL = sum(D(v) for _, v in MESES)
assert TOTAL == D("3085.34")
PALAVRA = "farmácia"
N_QD = 20                                               # compras na farmácia em 2026, até 4/11
S8 = CX["s8"]
assert S8["valor"] == PALAVRA and S8["periodoTxt"] == "Ano 2026"
assert S8["resumo"] == "20 transações · 20 pagas · 0 pendentes · somam R$ 3.085,34 · 711 no histórico", S8["resumo"]
MEDIA = sum(D(v) for _, v in MESES[:10]) / 10           # jan a out
assert MEDIA == D("308.534")
POR_PEDIDO = (TOTAL / N_QD).quantize(D("0.01"))
assert POR_PEDIDO == D("154.27")
BUSCAS = [("padaria", "1.047,14", 10), ("cinema", "1.994,55", 9), ("luz", "2.037,50", 10)]
for w, v, n in BUSCAS:
    r = CX[w]["resumo"]
    assert CX[w]["valor"] == w and f"{n} transações" in r and f"somam R$ {v}" in r, (w, r)

def brl(v, casas=2):
    return f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ---------------------------------------------------------------- tempos (s)
SOBE = 4.35          # a cena de tinta sobe e revela o papel
T1, T2, T3, T4 = 4.55, 7.60, 10.60, 13.50
FIM = 16.70
TAP = 5.95           # toque no campo de busca
LETRAS = [round(6.35 + 0.15 * k, 2) for k in range(8)]   # uma foto real depois de cada letra
POP = 7.75           # o resumo do filtrado se solta da tela
CAM0 = (56, 0, 1.0)  # câmera da janela: (topo, esquerda, zoom) em px CSS da tela
CAM_LISTA = (700, 0, 1.0)

# ---------------------------------------------------------------- tela real: as fotos da digitação
ESTADOS = ["s0", "s0f"] + [f"s{i}" for i in range(1, 9)]
OCULTA = ' style="opacity:0"'
imgs = "".join(f'<img id="{e}" src="file://{TELAS}/{ARQ[e]}"{"" if i == 0 else OCULTA}>' for i, e in enumerate(ESTADOS))
PERIODO = CX["s0"]["pilula"]                       # pílula "‹ Ano 2026 ›" (px CSS)
BUSCA0 = CX["s0"]["busca"]
TOQUE = [BUSCA0[0] + 60, BUSCA0[1] + BUSCA0[3] / 2]

# recorte do cartão "Transações": título, resumo do filtrado e o campo de busca
R_POP = [18, 320, 354, 148]
assert S8["resumoBox"][1] > R_POP[1] and S8["campo"][1] + S8["campo"][3] < R_POP[1] + R_POP[3]
SOMA = C.uniao(*S8["soma"])                         # "somam R$ 3.085,34"
PARA = [90, 640, 900]
DE = C.de_janela(R_POP, CAM0)
P4 = [90, 500, 900]                                # o recorte das três buscas (cena 4)
SOMAS4 = [C.uniao(*CX[w]["soma"]) for w, _, _ in BUSCAS]

def lupa(tam, cor, traco=2.4):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" '
            f'stroke-linecap="round" stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 L20 20"/></svg>')

# ---------------------------------------------------------------- odômetro do gancho (R$ e centavos menores, como no site)
GRANDE, PEQ = "3.085", "34"
VOLTAS = [1, 2, 2, 3, 3, 4]
def col(k, cls):
    return f'<span class="col {cls}"><span class="fita" id="f{k}"><i>9</i><i>0</i><i>1</i></span></span>'
def odometro():
    partes, k = ['<span class="rs">R$</span>'], 0
    for ch in GRANDE:
        if ch.isdigit():
            partes.append(col(k, "g")); k += 1
        else:
            partes.append(f'<span class="sep g">{ch}</span>')
    partes.append('<span class="sep p">,</span>')
    for ch in PEQ:
        partes.append(col(k, "p")); k += 1
    return "".join(partes)
DIGITOS = [c for c in GRANDE + PEQ if c.isdigit()]
ALVOS_COL = [VOLTAS[k] * 10 + int(c) for k, c in enumerate(DIGITOS)]
ALT_COL = [196] * 4 + [112] * 2
ODO_A, ODO_FIM = -0.18, 1.55                 # o odômetro gira desde antes do 1º quadro
POUSO = ODO_FIM + 5 * 0.13

# 20 quadradinhos, um por compra, acendem no ritmo do contador
def quadros():
    out, tam, gap = [], 58.8, 17.6
    for i in range(N_QD):
        x = 90 + (i % 12) * (tam + gap); y = 1372 + (i // 12) * (tam + gap)
        out.append(f'<i class="qd" id="q{i}" style="left:{x:.1f}px;top:{y:.1f}px"></i>')
    return "".join(out)
QD_T = [round(ODO_A + (POUSO - .1 - ODO_A) * (1 - (1 - (i + 1) / N_QD) ** (1 / 3)), 3) for i in range(N_QD)]

# ---------------------------------------------------------------- barras mês a mês
MAXV = max(D(v) for _, v in MESES)
BAR_H, BASE = 600, 1290
X0, PASSO, LARG = 214, 76, 52
Y_MED = BASE - float(MEDIA / MAXV) * BAR_H
def barras():
    out = []
    for i, (m, v) in enumerate(MESES):
        x = X0 + i * PASSO
        out.append(f'<div class="bar" id="b{i}" style="left:{x:.1f}px;width:{LARG}px;top:{BASE}px;height:0"></div>')
        out.append(f'<div class="mes" id="m{i}" style="left:{x - 12:.1f}px;width:{LARG + 24}px;top:{BASE + 20}px">{m}</div>')
    out.append(f'<div id="linhaMedia" style="top:{Y_MED - 2:.1f}px"></div>')
    out.append(f'<div id="rotMedia" style="top:{Y_MED - 50:.1f}px"><b>{C.din("309")}</b><small>média</small></div>')
    return "".join(out)
H_BARRAS = [float(D(v) / MAXV) * BAR_H for _, v in MESES]

# ---------------------------------------------------------------- cena 4: as somas das três buscas
YS4 = [930, 1080, 1230]
def tally():
    return "".join(f"""<div class="tl" id="tl{i}" style="top:{YS4[i]}px"><div class="tw">{lupa(40, A.MUTED, 2.6)}<span>{w}</span><small>{n} transações</small></div>
  <div class="tv">{C.din(v)}</div></div>""" for i, (w, v, n) in enumerate(BUSCAS))
TROCA4 = [[T4 - .2, 0], [T4 + .85, 1], [T4 + 1.85, 2]]

CSS = C.CSS + f"""
.tit{{font-size:66px}}
#gancho .q{{position:absolute;left:90px;top:310px;width:900px;font-size:118px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#gancho .q span{{color:{A.MENTA}}}
#campo{{position:absolute;left:90px;top:780px;width:900px;height:164px;border-radius:999px;background:#fff;display:flex;align-items:center;gap:30px;padding:0 54px;
  box-shadow:0 0 0 12px rgba(110,231,183,.16)}}
#campo .txt{{font-size:78px;font-weight:600;letter-spacing:-.03em;color:{A.INK}}}
.cursor{{display:inline-block;width:7px;height:84px;border-radius:4px;background:{A.BRAND};margin-left:6px;vertical-align:middle}}
#odoW{{position:absolute;left:84px;top:1036px;width:910px;transform-origin:0 70%}}
#odo{{display:flex;align-items:flex-end;color:{A.MENTA};font-weight:700;letter-spacing:-.04em;font-variant-numeric:tabular-nums}}
#odo .rs{{font-size:80px;line-height:80px;font-weight:600;color:{K.DARK_TEXTO};margin:0 22px 24px 6px;letter-spacing:-.01em}}
#odo .col{{display:block;overflow:hidden;-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 14%,#000 86%,transparent 100%)}}
#odo .col.g{{height:196px;font-size:172px;line-height:196px}}
#odo .col.p{{height:112px;font-size:96px;line-height:112px;margin-bottom:14px;color:{K.DARK_TEXTO};font-weight:600}}
#odo .fita{{display:block;will-change:transform}}
#odo .fita i{{display:block;font-style:normal}}
#odo .col.g .fita i{{height:196px}}
#odo .col.p .fita i{{height:112px}}
#odo .sep.g{{font-size:172px;line-height:196px}}
#odo .sep.p{{font-size:96px;line-height:112px;margin-bottom:14px;color:{K.DARK_TEXTO};font-weight:600}}
#pedidos{{position:absolute;left:92px;top:1262px;font-size:52px;font-weight:600;color:#fff;letter-spacing:-.02em;opacity:0}}
#pedidos span{{color:{K.DARK_TEXTO};font-weight:500}}
.qd{{position:absolute;width:58.8px;height:58.8px;border-radius:16px;border:4px solid #2E3830;display:block}}
.qd.on{{background:{A.BRAND};border-color:{A.BRAND}}}
.qd.novo{{background:{A.MENTA};border-color:{A.MENTA}}}
#veu{{z-index:3}}
#apoio3{{position:absolute;left:90px;top:372px;font-size:38px;font-weight:500;color:{A.MUTED};letter-spacing:-.018em;opacity:0}}
.bar{{position:absolute;background:{A.CORAL};border-radius:12px 12px 3px 3px;transform:translateY(-100%)}}
.bar.parcial{{background:#fff;border:4px solid {A.CORAL};border-bottom:0}}
.mes{{position:absolute;text-align:center;font-size:31px;font-weight:600;color:{A.MUTED};opacity:0}}
.mes.mini{{font-size:25px;font-weight:500;white-space:nowrap}}
#linhaMedia{{position:absolute;left:200px;width:0;border-top:4px dashed {A.INK}}}
#rotMedia{{position:absolute;left:84px;opacity:0;line-height:1;white-space:nowrap}}
#rotMedia b{{display:block;font-size:48px;font-weight:700;letter-spacing:-.03em;color:{A.INK}}}
#rotMedia small{{display:block;font-size:28px;font-weight:600;color:{A.MUTED};margin-top:6px}}
#extra{{position:absolute;left:90px;top:1420px;width:900px;font-size:40px;font-weight:500;color:{A.MUTED};letter-spacing:-.015em;opacity:0}}
#extra b{{color:{A.INK};font-weight:700}}
#nota4{{position:absolute;left:96px;top:452px;font-size:26px;font-weight:500;color:{A.MUTED};letter-spacing:-.005em;opacity:0}}
.tl{{position:absolute;left:90px;width:860px;height:130px;display:flex;align-items:center;justify-content:space-between;border-bottom:3px solid {A.FIO};opacity:0}}
.tw{{display:grid;grid-template-columns:52px auto;grid-template-rows:auto auto;column-gap:16px;align-items:center}}
.tw svg{{grid-row:1 / span 2}}
.tw span{{font-size:50px;font-weight:700;letter-spacing:-.035em;color:{A.INK};line-height:1.05}}
.tw small{{font-size:30px;font-weight:500;color:{A.MUTED};letter-spacing:-.01em}}
.tv{{font-size:84px;font-weight:700;letter-spacing:-.045em;color:{A.INK};line-height:1}}
.tv .rs,.tv .cts{{color:{A.MUTED}}}
"""

CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="t1">Em Transações: período <b>Ano</b> e a busca “farmácia”.</div>
  <div class="tit" id="t2">A soma do que está filtrado aparece <b>no topo</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">
    <div class="tela" id="tela">{imgs}{K.aneis("aPer")}{K.toques("busca")}</div>
    <div class="veu" id="veu"></div>
  </div>
  {C.pop_html("pop", f"{TELAS}/{ARQ['s8']}", C.anel_no_recorte("aSoma", R_POP, PARA, SOMA, 14))}
  <div class="tit" id="t3">Em média, <b>R$ 309</b> por mês.</div>
  <div id="apoio3">de janeiro a outubro de 2026</div>
  <div id="graf">{barras()}</div>
  <div id="extra">{N_QD} compras · <b>R$ {brl(POR_PEDIDO)}</b> cada, em média</div>
  <div class="tit" id="t4">Busque qualquer coisa. <b>A soma aparece na hora.</b></div>
  <div id="nota4">{K.NOTA}</div>
  {C.pop_html("pop4", [f"{TELAS}/{CX['arquivos'][w]}" for w, _, _ in BUSCAS],
              "".join(C.anel_no_recorte(f"aS{i}", R_POP, P4, SOMAS4[i], 14) for i in range(3)))}
  {tally()}
</div>

<div class="cena tinta" id="gancho">
  <div class="q" id="q">Quanto foi<br>na <span>farmácia</span><br>este ano?</div>
  <div id="campo">{lupa(72, A.MUTED, 2.6)}<span class="txt" id="dg"></span></div>
  <div id="odoW"><div id="odo">{odometro()}</div></div>
  <div id="pedidos">{N_QD} compras <span>em 2026, até 4/11</span></div>
  {quadros()}
</div>

{K.fim("Transações no timtimcash")}
"""

JS = C.JS + f"""
const SOBE={SOBE}, T1={T1}, T2={T2}, T3={T3}, T4={T4}, FIM={FIM}, TAP={TAP}, POP={POP};
const LETRAS={LETRAS}, ESTADOS={json.dumps(ESTADOS)}, ALVOS={ALVOS_COL}, ALT={ALT_COL}, HB={[round(h, 1) for h in H_BARRAS]};
const ODO_A={ODO_A}, ODO_FIM={ODO_FIM}, POUSO={POUSO}, QD_T={QD_T}, N_QD={N_QD};
const CAM0={list(CAM0)}, CAM_LISTA={list(CAM_LISTA)};
const R_POP={R_POP}, DE={[round(v, 1) for v in DE]}, PARA={PARA}, P4={P4}, DE4={[P4[0], P4[1] + 140, P4[2], 1]}, TROCA4={TROCA4};
poeAnel('aPer', {PERIODO}, 12);
poeToque('busca', {TOQUE[0]:.1f}, {TOQUE[1]:.1f});
function caret(id, t, ligado){{ $(id).style.opacity = ligado ? ((Math.floor(t*2.4) % 2 === 0) ? 1 : 0) : 0; }}
function mix(a, b, p){{ return a.map((v, i) => v + (b[i]-v)*p); }}
function cam(c){{ const [topo, esq, z] = c; $('tela').style.transform = `translate(${{-esq*E*z}}px, ${{-topo*E*z}}px) scale(${{z}})`; }}
function render(t){{
  // 1. gancho na tinta: a busca digitada, o odômetro que gira e para em R$ 3.085,34, um quadradinho por compra
  $('gancho').style.transform = `translateY(${{-1920*prog(t, SOBE, SOBE+.45)}}px)`;
  $('q').style.transform = `translateY(${{-14*pout(t,0,1.4)}}px)`;
  const txt = 'farmácia'; const n = clamp(Math.floor((t+0.12)*9), 0, txt.length);
  $('dg').innerHTML = txt.slice(0,n) + '<span class="cursor" id="cur"></span>';
  caret('cur', t, true);
  ALVOS.forEach((alvo, i) => {{
    const fimCol = ODO_FIM + i*0.13;
    const p = easeOut(clamp((t-ODO_A)/(fimCol-ODO_A), 0, 1));
    const pos = alvo*p, base = Math.floor(pos + 1e-9), fr = pos - base, f = $('f'+i).children;
    f[0].textContent = (base+9) % 10; f[1].textContent = base % 10; f[2].textContent = (base+1) % 10;
    $('f'+i).style.transform = `translateY(${{-(1+fr)*ALT[i]}}px)`;
  }});
  $('odoW').style.transform = `scale(${{1 + 0.07*Math.sin(Math.PI*clamp((t-POUSO)/0.36,0,1))}})`;
  aparece('pedidos', t, POUSO+0.15, 0, 26, .45);
  QD_T.forEach((a, i) => {{ const e = $('q'+i); const on = t >= a; e.className = on ? (t < a + .22 || (i === N_QD - 1 && t < POUSO + .6) ? 'qd novo' : 'qd on') : 'qd';
    const s = on ? 1 + 0.22*Math.exp(-(t-a)*14)*Math.sin(Math.min(t-a, .5)*22) : 1; e.style.transform = `scale(${{s}})`; }});
  // 2. papel: a tela real (período Ano, toque na busca, uma foto por letra); o resumo se solta da tela
  titulo('t1', t, T1, T2-.32); titulo('t2', t, T2, T3-.5);
  janela('janela', t, SOBE, T3-.45); janela('nota', t, SOBE, T3-.45);
  let atual = 0;
  if (t >= TAP + .12) atual = 1;
  LETRAS.forEach((a, i) => {{ if (t >= a) atual = i + 2; }});
  ESTADOS.forEach((e, i) => {{ $(e).style.opacity = i === atual ? 1 : 0; }});
  anel('aPer', t, T1+.45, TAP-.25);
  toque('busca', t, TAP);
  cam(mix(CAM0, CAM_LISTA, prog(t, POP+.5, T3-.35)));
  $('veu').style.opacity = .62*prog(t, POP, POP+.5);
  recorte('pop', t, POP, T3-.5, R_POP, DE, PARA, .6, false);
  anel('aSoma', t, POP+.7, T3-.5);
  // 3. barras mês a mês
  titulo('t3', t, T3-.25, T4-.4); aparece('apoio3', t, T3-.1, T4-.4, 20);
  const saiG = prog(t, T4-.4, T4-.12);
  $('graf').style.opacity = Math.min(prog(t, T3-.3, T3-.1), 1 - saiG); $('extra').style.opacity = Math.min(prog(t, T3+1.4, T3+1.7), 1 - saiG);
  $('graf').style.transform = `translateY(${{-60*saiG}}px)`; $('extra').style.transform = `translateY(${{-60*saiG}}px)`;
  HB.forEach((h, i) => {{ const p = pout(t, T3-.15+i*.07, T3+.45+i*.07); $('b'+i).style.height = (h*p)+'px'; $('b'+i).style.opacity = p > 0.01 ? 1 : 0;
    $('m'+i).style.opacity = prog(t, T3-.2+i*.07, T3+.1+i*.07); }});
  $('linhaMedia').style.width = (760*pout(t, T3+.95, T3+1.55))+'px';
  $('rotMedia').style.opacity = prog(t, T3+1.2, T3+1.5);
  // 4. busque qualquer coisa: a tela real de cada busca e as somas, uma embaixo da outra
  titulo('t4', t, T4-.2, FIM+.3);
  $('nota4').style.opacity = prog(t, T4-.1, T4+.2);
  recorte('pop4', t, T4-.2, 0, R_POP, DE4, P4, .55, false, TROCA4);
  [0,1,2].forEach(i => {{ const a = TROCA4[i][0]; anel('aS'+i, t, a+.45, i < 2 ? TROCA4[i+1][0]-.05 : 0);
    aparece('tl'+i, t, a+.4, 0, 30, .4); }});
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (tinta), a mesma da r1
CAPA_CSS = f"""
#capa .eyebrow{{color:{A.MENTA}}}
.ct{{position:absolute;left:90px;top:440px;width:900px}}
.ct .h1{{font-size:112px;line-height:.98;color:#fff;text-wrap:balance}}
.ct .h1 span{{color:{A.MENTA}}}
.cc{{position:absolute;left:90px;top:900px;width:900px;height:150px;border-radius:999px;background:#fff;display:flex;align-items:center;gap:28px;padding:0 52px;
  box-shadow:0 0 0 12px rgba(110,231,183,.16)}}
.cc span{{font-size:70px;font-weight:600;letter-spacing:-.03em;color:{A.INK}}}
.cc i{{display:inline-block;width:7px;height:78px;border-radius:4px;background:{A.BRAND};margin-left:-18px}}
.cr{{position:absolute;left:84px;top:1110px;font-size:400px;line-height:1;font-weight:700;letter-spacing:-.06em;color:{A.MENTA};font-variant-numeric:tabular-nums}}
.cr small{{font-size:150px;letter-spacing:-.02em;margin-right:30px;color:{K.DARK_TEXTO};font-weight:600}}
"""
CAPA_CORPO = f"""
{K.logo("tinta")}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Transações</div>
  <div class="h1">Quanto foi na <span>farmácia</span> este ano?</div></div>
<div class="cc">{lupa(66, A.MUTED, 2.6)}<span>farmácia</span><i></i></div>
<div class="cr"><small>R$</small>?</div>
"""

HTML = K.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="tinta")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
