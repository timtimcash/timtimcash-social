# -*- coding: utf-8 -*-
"""Reel de 09/11/2026 · "Empresa tem DRE. E a sua casa?" (capa tinta), 1080 × 1920, 30 fps, 20 s. Equipe r1b (a partir da r1).

Tela real do build 2026-10-16.1 (capturas/captura09.py): Resultado (DRE) no celular, relógio em 08/11/2026 10:00; o site
abre em novembro e outubro vem pelo botão "Anterior" ao lado do mês. Outubro de 2026: resultado +R$ 2.065,00;
receitas R$ 10.280,00 (salário R$ 9.960,00, outras receitas R$ 320,00); despesas R$ 8.215,00, 79,9% da receita.
No celular o site mostra só o 79,9% das despesas; no computador (mesmo dia, mesma conta) aparece a % da receita de
cada categoria: Casa 24,2%, Mercado 16,8%, Educação 14,1%, Transporte 11,7%, Bares e restaurantes 6,6%,
Lazer e hobbies 2,1%, Presentes e doações 1,8%, Saúde 1,4%, Assinaturas e serviços 1,2%. Resultado: 20,1% da receita
(conta feita aqui; a tela mostra o valor em reais). A frase da cena 4 é a do próprio site: o título da seção
"04 · Resultado (DRE)" da página inicial do build 2026-10-16.1, "Quanto entrou, quanto saiu, quanto sobrou."

python3 reel_09.py  |  REEL_PREVIA="0 0.6 1.4 3.6 5.9 8.2 11.5 13.5 15.8 18.5" python3 reel_09.py
"""
import os, sys, json
from decimal import Decimal as D, ROUND_HALF_UP
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-11-09_reel-a-dre-da-sua-casa"
TRAB = os.path.join(AQUI, "trabalho", "09")
TELA = os.path.join(N, "saida", PASTA, "telas", "celular-dre-outubro.png")
SAIDA = os.path.join(N, "saida", PASTA)
DUR = 20.0

CXT = json.load(open(os.path.join(TRAB, "caixas.json"), encoding="utf-8"))
CX = CXT["out"]

# ---------------------------------------------------------------- números (conferidos contra a tela)
REC = D("10280.00")
DESP = [("Casa", "2492.60"), ("Mercado", "1725.00"), ("Educação", "1450.00"), ("Transporte", "1207.00"),
        ("Bares e restaurantes", "681.40"), ("Lazer e hobbies", "214.90"), ("Presentes e doações", "180.00"),
        ("Saúde", "144.30"), ("Assinaturas e serviços", "119.80")]
TOT_D = sum(D(v) for _, v in DESP)
RES = REC - TOT_D
assert TOT_D == D("8215.00") and RES == D("2065.00")
def p1(v):
    return (v / REC * 100).quantize(D("0.1"), rounding=ROUND_HALF_UP)
def vir(v):
    return str(v).replace(".", ",")
PCT = {c: p1(D(v)) for c, v in DESP}
assert [str(PCT[c]) for c, _ in DESP] == ["24.2", "16.8", "14.1", "11.7", "6.6", "2.1", "1.8", "1.4", "1.2"]
assert str(p1(TOT_D)) == "79.9" and str(p1(RES)) == "20.1"
assert CX["periodoTxt"] == "Outubro 2026"
IT = CX["itens"]
assert IT["RESULTADO"]["txt"] == "RESULTADO Receitas menos despesas +R$ 2.065,00"
assert IT["RECEITAS"]["txt"] == "RECEITAS R$ 10.280,00" and IT["DESPESAS"]["txt"] == "DESPESAS 79,9% R$ 8.215,00"
def brl(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
for c, v in DESP:                                     # cada categoria na tela do celular, com o valor
    assert IT[c]["txt"] == f"{c} R$ {brl(D(v))}", (c, IT[c]["txt"])
DESK = dict(CXT["desk"]["pct"])                       # a % da receita de cada categoria, no computador
assert [k for k in DESK] == ["96,9%", "3,1%", "24,2%", "16,8%", "14,1%", "11,7%", "6,6%", "2,1%", "1,8%", "1,4%", "1,2%"]
OUTRAS = sum(D(v) for c, v in DESP[5:])
SEG = [(c, D(v)) for c, v in DESP[:5]] + [("outras", OUTRAS)]
VAL = dict((t.replace("\xa0", " "), b) for t, b in CX["valores"])

# ---------------------------------------------------------------- tempos (s)
SOBE = 2.85
T1, T2, T3 = 3.05, 5.25, 7.45
POP = 3.45           # a lupa se solta da tela
T4 = 9.75            # resumo desenhado
T5 = 14.45           # a frase do site, na tinta
FIM = 17.35
GOLPES = [-0.08, 0.22, 0.52]      # D, R, E batem na tela

# ---------------------------------------------------------------- a lupa que desce pela tela (px CSS)
RA = [24, 214, 342, 213]          # resultado e o começo das receitas
RB = [24, 300, 342, 213]          # receitas: salário e outras receitas, até o cabeçalho das despesas
RC = [24, 444, 342, 213]          # despesas: 79,9% e as primeiras categorias
DY = 92                           # a câmera acompanha: a região fica sempre no mesmo lugar da janela
PARA = [90, 690, 900]
DE = C.de_janela(RA, (RA[1] - DY, 0, 1.0))
V_RES = C.uniao(VAL["+R$ 2.065,00"])
L_REC = IT["RECEITAS"]["linha"]
CHIP = IT["79,9%"]["folha"]
L_DES = IT["DESPESAS"]["linha"]

# ---------------------------------------------------------------- barra empilhada (100% = receita)
CORES_LEG = ["#B4532F", "#D97757", "#B4532F", "#D97757", "#B4532F", "#D97757"]
BX, BW = 90, 900
def segmentos():
    out, x = [], BX
    for i, (c, v) in enumerate(SEG):
        w = float(v / REC) * BW
        out.append(f'<div class="seg" id="sg{i}" style="left:{x:.1f}px;width:{w - 4:.1f}px;background:{CORES_LEG[i]}"></div>')
        x += w
    w = float(RES / REC) * BW
    out.append(f'<div class="seg" id="sg{len(SEG)}" style="left:{x:.1f}px;width:{w:.1f}px;background:{A.BRAND}"></div>')
    return "".join(out)
LEG = [(c, vir(p1(v)), i) for i, (c, v) in enumerate(SEG)]

CSS = C.CSS + f"""
.tit{{font-size:66px}}
.tit b.cor{{color:#B4532F}}
#gt{{position:absolute;left:90px;top:300px;width:900px;font-size:92px;line-height:1.0;font-weight:700;letter-spacing:-.048em;color:#fff}}
#letras{{position:absolute;left:0;top:520px;width:1080px;height:600px;display:flex;justify-content:center;align-items:center;gap:10px;overflow:hidden}}
.le{{position:relative;font-size:430px;line-height:520px;font-weight:700;letter-spacing:-.04em;color:{A.MENTA};opacity:0;transform-origin:50% 62%}}
.onda2{{position:absolute;left:50%;top:62%;width:300px;height:300px;margin:-150px 0 0 -150px;border-radius:50%;border:8px solid {A.MENTA};opacity:0}}
#casa{{position:absolute;left:90px;top:1150px;width:900px;display:flex;align-items:center;gap:30px;opacity:0}}
#casa .q{{font-size:118px;font-weight:700;letter-spacing:-.05em;line-height:1;color:#fff}}
#resumo{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}}
.lin{{position:absolute;left:90px;width:900px;display:flex;align-items:baseline;justify-content:space-between;border-bottom:3px solid {A.FIO};padding-bottom:26px;opacity:0}}
.lin .r{{font-size:40px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{A.MUTED}}}
.lin .v{{font-size:124px;font-weight:700;letter-spacing:-.05em;line-height:1}}
#l3{{border-bottom:0}}
#chipF{{position:absolute;right:90px;top:880px;display:inline-flex;align-items:center;height:72px;padding:0 30px;border-radius:999px;background:{A.SOFT};
  color:{A.BRAND_DEEP};font-size:36px;font-weight:700;opacity:0}}
.seg{{position:absolute;top:1010px;height:120px;border-radius:14px;transform-origin:0 50%;transform:scaleX(0)}}
#barraT{{position:absolute;left:90px;top:964px;font-size:30px;font-weight:600;color:{A.MUTED};opacity:0}}
#legs{{position:absolute;left:90px;top:1168px;width:900px;display:grid;grid-template-columns:372px 480px;grid-template-rows:repeat(4,auto);grid-auto-flow:column;row-gap:22px;column-gap:48px}}
#rodape{{position:absolute;left:90px;top:1428px;width:860px;font-size:30px;font-weight:500;color:{A.MUTED};letter-spacing:-.012em;opacity:0}}
.lg{{display:flex;align-items:center;gap:14px;font-size:31px;font-weight:500;color:{A.INK};opacity:0;white-space:nowrap}}
.lg i{{width:26px;height:26px;border-radius:7px;flex:none}}
.lg b{{font-weight:700;margin-left:auto;font-variant-numeric:tabular-nums}}
#frase{{position:absolute;left:90px;top:780px;width:900px}}
#frase div{{font-size:122px;line-height:1.02;font-weight:700;letter-spacing:-.05em;color:#fff;opacity:0;white-space:nowrap}}
#frase span.e{{color:{A.MENTA}}}
#frase span.s{{color:#F0A487}}
#frase span.f{{color:{A.MENTA}}}
#casa2{{position:absolute;left:84px;top:580px;opacity:0}}
#fonteF{{position:absolute;left:90px;top:1180px;width:860px;font-size:34px;font-weight:500;color:{K.DARK_TEXTO};letter-spacing:-.015em;opacity:0}}
"""

def icone_casa(tam, cor, traco=2.2, ident=""):
    return (f'<svg {ident} width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" stroke-linecap="round" '
            f'stroke-linejoin="round"><path class="tr" d="M3.5 10.5 L12 3.5 L20.5 10.5"/><path class="tr" d="M5.5 9 V20 H18.5 V9"/><path class="tr" d="M10 20 V14.5 H14 V20"/></svg>')

LEG_HTML = "".join(f'<div class="lg" id="lg{i}"><i style="background:{CORES_LEG[i]}"></i>{c if c != "outras" else "outras categorias"}<b>{pc}%</b></div>'
                   for c, pc, i in LEG)
LEG_HTML += f'<div class="lg" id="lg{len(LEG)}" style="color:{A.BRAND_DARK};font-weight:700"><i style="background:{A.BRAND}"></i>ficou<b>{vir(p1(RES))}%</b></div>'

ANEIS_LUPA = '<div class="anel" id="aRes"></div><div class="anel" id="aRec"></div><div class="anel coral" id="aChip"></div>'

CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="t1">Em outubro, sobraram <b>R$ 2.065</b>.</div>
  <div class="tit" id="t2">Entraram <b>R$ 10.280</b>.</div>
  <div class="tit" id="t3">Saíram <b class="cor">R$ 8.215</b>: 79,9% da receita.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{K.tela("tela", TELA)}<div class="veu" id="veu"></div></div>
  {C.pop_html("lupa", TELA, ANEIS_LUPA)}
  <div id="resumo">
    <div class="lin" id="l1" style="top:300px"><span class="r">Entrou</span><span class="v" style="color:{A.BRAND_DARK}">{C.din("10.280")}</span></div>
    <div class="lin" id="l2" style="top:505px"><span class="r">Saiu</span><span class="v" style="color:#B4532F">{C.din("8.215")}</span></div>
    <div class="lin" id="l3" style="top:710px"><span class="r">Ficou</span><span class="v" style="color:{A.INK}">{C.din("2.065")}</span></div>
    <div id="chipF">20,1% da receita</div>
    <div id="barraT">Para onde foi cada real que entrou</div>
    {segmentos()}
    <div id="legs">{LEG_HTML}</div>
    <div id="rodape">No computador, o Resultado (DRE) mostra a % da receita de cada categoria.</div>
  </div>
</div>

<div class="cena tinta" id="cfrase" style="transform:translateY(1920px)">
  <div id="casa2">{icone_casa(150, A.MENTA, 1.8, 'id="svgCasa2"')}</div>
  <div id="frase"><div>Quanto <span class="e">entrou</span>,</div><div>quanto <span class="s">saiu</span>,</div><div>quanto <span class="f">sobrou</span>.</div></div>
</div>

<div class="cena tinta" id="gancho">
  <div id="gt">Empresa fecha o mês com DRE.</div>
  <div id="letras">
    <div class="le" id="L0"><div class="onda2" id="w0"></div>D</div>
    <div class="le" id="L1"><div class="onda2" id="w1"></div>R</div>
    <div class="le" id="L2"><div class="onda2" id="w2"></div>E</div>
  </div>
  <div id="casa">{icone_casa(130, A.MENTA, 2.0)}<span class="q">E a sua casa?</span></div>
</div>

{K.fim("Resultado (DRE) no timtimcash")}
"""

JS = C.JS + f"""
const SOBE={SOBE}, T1={T1}, T2={T2}, T3={T3}, T4={T4}, T5={T5}, FIM={FIM}, GOLPES={GOLPES}, POP={POP};
const RA={RA}, RB={RB}, RC={RC}, DY={DY}, PARA={PARA}, DE={[round(v, 1) for v in DE]};
const V_RES={V_RES}, L_REC={L_REC}, CHIP={CHIP}, L_DES={L_DES};
function mix(a, b, p){{ return a.map((v, i) => v + (b[i]-v)*p); }}
function cam(c){{ const [topo, esq, z] = c; $('tela').style.transform = `translate(${{-esq*E*z}}px, ${{-topo*E*z}}px) scale(${{z}})`; }}
const tr = [...document.querySelectorAll('#svgCasa2 .tr')]; tr.forEach(p => {{ const L = p.getTotalLength(); p.style.strokeDasharray = L; p.dataset.L = L; }});
function render(t){{
  // 1. gancho: D, R, E batem na tela; "E a sua casa?"
  $('gancho').style.transform = `translateY(${{-1920*prog(t, SOBE, SOBE+.45)}}px)`;
  let tremor = 0;
  GOLPES.forEach((g, i) => {{
    const el = $('L'+i); const p = clamp((t - g)/0.2, 0, 1);
    const s = p < 1 ? 2.2 - 1.2*p*p : 1 + 0.10*Math.exp(-(t-g-0.2)*9)*Math.sin((t-g-0.2)*28);
    el.style.opacity = clamp((t-g)/0.08, 0, 1); el.style.transform = `scale(${{s}})`;
    const w = $('w'+i); const q = clamp((t - g - 0.2)/0.55, 0, 1);
    w.style.opacity = (t > g + .2 && q < 1) ? 0.7*(1-q) : 0; w.style.transform = `scale(${{0.4 + 1.6*easeOut(q)}})`;
    if (t > g + .2) tremor += 14*Math.exp(-(t-g-0.2)*14);
  }});
  $('letras').style.transform = `translate(${{tremor*Math.sin(t*95)}}px, ${{tremor*Math.cos(t*80)}}px)`;
  $('gt').style.transform = `translateY(${{-12*pout(t,0,1.2)}}px)`;
  aparece('casa', t, 0.95, 0, 40, .45);
  // 2. papel: a tela real do Resultado (DRE) de outubro; a lupa desce do resultado às despesas
  titulo('t1', t, T1, T2-.32); titulo('t2', t, T2, T3-.32); titulo('t3', t, T3, T4-.45);
  janela('janela', t, SOBE, T4-.6); janela('nota', t, SOBE, T4-.6);
  let R = RA; R = mix(R, RB, prog(t, T2-.1, T2+.5)); R = mix(R, RC, prog(t, T3-.1, T3+.5));
  cam([R[1]-DY, 0, 1.0]);
  $('veu').style.opacity = .62*Math.min(prog(t, POP, POP+.5), 1 - prog(t, T4-.8, T4-.45));
  recorte('lupa', t, POP, T4-.85, R, DE, PARA, .6, true);
  posAnel('aRes', V_RES, R, PARA[2], 14); anel('aRes', t, POP+.7, T2-.2);
  posAnel('aRec', L_REC, R, PARA[2], 10); anel('aRec', t, T2+.5, T3-.2);
  posAnel('aChip', CHIP, R, PARA[2], 12); anel('aChip', t, T3+.55, T4-.95);
  // 3. resumo desenhado: entrou, saiu, ficou; a barra da receita
  $('resumo').style.opacity = Math.min(prog(t, T4-.25, T4), 1 - prog(t, T5+.2, T5+.5));
  ['l1','l2','l3'].forEach((id, i) => {{ const p = pout(t, T4-.08+i*.38, T4+.37+i*.38); $(id).style.opacity = p; $(id).style.transform = `translateY(${{(1-p)*30}}px)`; }});
  const cf = pback(t, T4+1.2, T4+1.6); $('chipF').style.opacity = lin(t, T4+1.2, T4+1.35); $('chipF').style.transform = `scale(${{.6+.4*cf}})`;
  $('barraT').style.opacity = prog(t, T4+1.45, T4+1.75);
  $('rodape').style.opacity = prog(t, T4+2.5, T4+2.8);
  for (let i = 0; i < 7; i++){{ const a = T4 + 1.65 + i*.16; $('sg'+i).style.transform = `scaleX(${{pout(t, a, a+.35)}})`;
    $('lg'+i).style.opacity = prog(t, a+.15, a+.45); }}
  // 4. a frase do site, na tinta
  $('cfrase').style.transform = `translateY(${{1920*(1-prog(t, T5, T5+.45))}}px)`;
  [...$('frase').children].forEach((e, i) => {{ const p = pout(t, T5+.35+i*.32, T5+.8+i*.32); e.style.opacity = p; e.style.transform = `translateY(${{(1-p)*36}}px)`; }});
  tr.forEach(p => {{ p.style.strokeDashoffset = p.dataset.L*(1 - prog(t, T5+.3, T5+1.3)); }});
  $('casa2').style.opacity = lin(t, T5+.3, T5+.4);
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (tinta), a mesma da r1
CAPA_CSS = f"""
#capa .eyebrow{{color:{A.MENTA}}}
.ct{{position:absolute;left:90px;top:440px;width:900px}}
.ct .h1{{font-size:120px;line-height:.98;color:#fff}}
.dre{{position:absolute;left:0;top:930px;width:1080px;text-align:center;font-size:440px;line-height:1;font-weight:700;letter-spacing:-.03em;
  color:transparent;-webkit-text-stroke:7px {A.MENTA}}}
"""
CAPA_CORPO = f"""
{K.logo("tinta")}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Resultado (DRE)</div>
  <div class="h1">Empresa tem.<br>E a sua casa?</div></div>
<div class="dre">DRE</div>
"""

HTML = K.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="tinta")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
