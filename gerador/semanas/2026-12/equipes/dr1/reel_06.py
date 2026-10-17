# -*- coding: utf-8 -*-
"""Reel de 06/12/2026 · "Seu 2026 em 5 números" (capa verde, sem coral), 1080 × 1920, 30 fps. Equipe dr1.

Retrospectiva no tom de "wrapped": cinco números da conta de exemplo, cada um numa cena cheia, com uma tela real curta.
Telas reais do build 2026-10-16.1 (capturas/captura06.py), conta de base, celular 390 px em escala 3, relógio em
06/12/2026 10:00, período Ano 2026 escolhido pela interface ("Dezembro 2026" › "Ano atual" › "Aplicar"):
1. Transações, busca "delivery": "40 transações · 40 pagas · 0 pendentes · somam R$ 3.142,40";
2. Visão geral, "Top saídas": "Casa R$ 27.539,30 30%";
3. Fluxo, "Resumo mensal": "Jan de 2026 · R$ 9.480,00 · −R$ 9.420,00" (a maior saída do ano; IPVA e IPTU em janeiro);
4. Remessas, "Rendimento ano a ano": "2026 até hoje · +3,0% · +350,00 · −6,2% · −R$ 4.067,86";
5. Fluxo: "Resultado · Ano 2026 até 06/12 · R$ 31.769,90 · Guardou 25,6% do que entrou · Entrou R$ 123.860 · Saiu R$ 92.090,10".

python3 reel_06.py  |  REEL_PREVIA="0 0.5 1.6 3.4 5.3 6.8 8.6 10.1 11.9 13.4 15.2 16.8 18.5 20.3" python3 reel_06.py
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-12-06_reel-seu-2026-em-5-numeros"
TRAB = C.trabalho("06")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas("06")
ARQ = CX["arquivos"]

# ---------------------------------------------------------------- números (conferidos contra a tela)
assert CX["a_resumo"][4] == "40 transações · 40 pagas · 0 pendentes · somam R$ 3.142,40 · 750 no histórico"
assert CX["a_periodo"][4] == "Ano 2026"
assert CX["b_casa"][4] == "Casa R$ 27.539,30 30%" and "Ano 2026" in CX["b_periodo_txt"]
assert CX["c_jan"][4].startswith("Jan de 2026 R$ 9.480,00 −R$ 9.420,00")
assert CX["c_cartao"][4].startswith("Resultado · Ano 2026 até 06/12 R$ 31.769 ,90 Guardou 25,6% do que entrou Entrou R$ 123.860")
assert "Saiu R$ 92.090 ,10" in CX["c_cartao"][4]
assert CX["e_2026"][4] == "2026 até hoje +3,0% +350,00 −6,2% −R$ 4.067,86 hoje 13.310,00"
assert "Dec 06 2026" in CX["relogio"]

# ---------------------------------------------------------------- tempos (s)
H = 2.3                       # fim do gancho
DS = 3.3                      # duração de cada número
T0 = [round(H + DS * i, 2) for i in range(5)]
FIM = round(H + DS * 5, 2)
DUR = round(FIM + 2.7, 2)

# ---------------------------------------------------------------- as cinco cenas
def uniao(cx):
    return C.uniao(*cx)

CENAS = [
    dict(id="n1", fundo="tinta", sobre="Delivery", num=40, casas=0, pre="", suf="", cor=A.MENTA,
         rot="pedidos de delivery", sub="R$ 3.142,40 no ano, na busca de Transações",
         foto=ARQ["a"], R=[18, 320, 354, 148], P=[90, 1060, 900], anel=uniao(CX["a_soma"])),
    dict(id="n2", fundo="papel", sobre="Para onde foi", num=30, casas=0, pre="", suf="%", cor=A.CORAL,
         rot="do que saiu foi para Casa", sub="R$ 27.539,30 em 2026: aluguel e conta de luz",
         foto=ARQ["b"], R=[18, 66, 354, 228], P=[140, 1052, 800], anel=CX["b_casa"][:4]),
    dict(id="n3", fundo="suave", sobre="O mês mais caro", num=9420, casas=0, pre="R$", suf="", cor=A.INK,
         rot="em janeiro, o mês mais caro", sub="IPVA e IPTU chegaram juntos",
         foto=ARQ["c2"], R=[10, 124, 370, 176], P=[110, 1052, 860], anel=[15, 170, 360, 64]),
    dict(id="n4", fundo="tinta", sobre="Lá fora", num=350, casas=0, pre="+US$", suf="", cor=A.MENTA,
         rot="rendeu lá fora em 2026, em dólar", sub="Taxa ao ano: +3,0% em US$ · −6,2% em reais",
         foto=ARQ["e"], R=[18, 540, 354, 150], P=[90, 1062, 900], anel=CX["e_2026"][:4]),
    dict(id="n5", fundo="suave", sobre="Guardado", num=25.6, casas=1, pre="", suf="%", cor=A.BRAND_DARK,
         rot="da receita ficou guardada", sub="Entrou R$ 123.860 · saiu R$ 92.090",
         foto=ARQ["c"], R=[22, 147, 346, 184], P=[110, 1050, 860], anel=CX["c_guardou"][:4]),
]
for c in CENAS:
    assert c["R"][1] + c["R"][3] > c["anel"][1] + c["anel"][3] and c["R"][1] < c["anel"][1], c["id"]
    alt = c["R"][3] * c["P"][2] / c["R"][2]
    assert c["P"][1] + alt < 1590, (c["id"], c["P"][1] + alt)

def segmentos(k, escuro):
    """Barra de 5 segmentos (como nos stories): k = cena atual (0 a 4); -1 no gancho."""
    out = []
    for i in range(5):
        out.append(f'<i class="sg{" esc" if escuro else ""}"><b id="sg{k}_{i}"></b></i>')
    return f'<div class="sgs">{"".join(out)}</div>'

def cena_html(k, c):
    escuro = c["fundo"] == "tinta"
    num = (f'<span class="pre">{c["pre"]}</span>' if c["pre"] else "") + f'<span id="{c["id"]}v">0</span>' + \
          (f'<span class="suf">{c["suf"]}</span>' if c["suf"] else "")
    return f"""<div class="cena {c['fundo']} nc" id="{c['id']}" style="clip-path:circle(0px at 540px 560px)">
  {segmentos(k, escuro)}
  <div class="eyebrow ey" id="{c['id']}e">{k + 1} de 5 · {c['sobre']}</div>
  <div class="big" id="{c['id']}n" style="color:{c['cor']}">{num}</div>
  <div class="rot" id="{c['id']}r">{c['rot']}</div>
  <div class="sub" id="{c['id']}s">{c['sub']}</div>
  <div class="nota" id="{c['id']}t" style="top:{c['P'][1] - 46}px;left:{c['P'][0] + 6}px">{K.NOTA}</div>
  {C.pop_html(c['id'] + 'p', os.path.join(TELAS, c['foto']), C.anel_no_recorte(c['id'] + 'a', c['R'], c['P'], c['anel'], 10))}
</div>"""

CSS = f"""
.sgs{{position:absolute;left:90px;top:286px;width:900px;display:flex;gap:12px}}
.sg{{flex:1;height:10px;border-radius:5px;background:{A.FIO};overflow:hidden}}
.sg.esc{{background:#2E3830}}
.sg b{{display:block;height:100%;width:0;background:{A.INK}}}
.sg.esc b{{background:#fff}}
.verde .sg{{background:{A.BRAND_DARK}}}
.verde .sg b{{background:#fff}}
.ey{{position:absolute;left:90px;top:336px;opacity:0}}
.big{{position:absolute;left:84px;top:400px;width:920px;font-size:300px;line-height:1;font-weight:700;letter-spacing:-.06em;
  font-variant-numeric:tabular-nums;white-space:nowrap;transform-origin:0 70%}}
.big .pre{{font-size:.36em;font-weight:600;letter-spacing:-.01em;margin-right:.16em}}
.big .suf{{font-size:.55em;letter-spacing:-.03em;margin-left:.04em}}
.tinta .big .pre{{color:{K.DARK_TEXTO}}}
.papel .big .pre,.suave .big .pre{{color:{A.MUTED}}}
.rot{{position:absolute;left:90px;top:732px;width:900px;font-size:72px;line-height:1.04;font-weight:700;letter-spacing:-.045em;text-wrap:balance;opacity:0}}
.sub{{position:absolute;left:90px;top:900px;width:900px;font-size:40px;line-height:1.25;font-weight:500;letter-spacing:-.02em;opacity:0}}
.tinta .sub{{color:{K.DARK_TEXTO}}}
.papel .sub,.suave .sub{{color:{A.MUTED}}}
.nc .nota{{opacity:0}}
/* gancho (verde) */
#g .ey{{opacity:1;color:#fff}}
#gSeu{{position:absolute;left:90px;top:500px;font-size:96px;font-weight:700;letter-spacing:-.05em;color:#fff}}
#gAno{{position:absolute;left:70px;top:600px;height:400px;display:flex;overflow:hidden}}
#gAno .dg{{display:block;height:400px;overflow:hidden}}
#gAno .fx{{display:block;font-size:400px;line-height:400px;font-weight:700;letter-spacing:-.06em;color:#fff;font-variant-numeric:tabular-nums}}
#gAno .fx i{{display:block;height:400px;font-style:normal}}
#gEm{{position:absolute;left:90px;top:1020px;font-size:118px;line-height:1;font-weight:700;letter-spacing:-.055em;color:#fff}}
#gSub{{position:absolute;left:90px;top:1190px;width:900px;font-size:42px;font-weight:500;letter-spacing:-.02em;color:#fff;opacity:0}}
"""

# "2026": os quatro algarismos sobem em sequência e assentam com um pequeno exagero (legíveis desde o primeiro quadro)
FITAS = [("2", "2"), ("0", "0"), ("2", "2"), ("6", "6")]
def ano_html():
    out = []
    for i, (alvo, fita) in enumerate(FITAS):
        itens = "".join(f"<i>{ch}</i>" for ch in fita)
        out.append(f'<span class="dg"><span class="fx" id="fx{i}">{itens}</span></span>')
    return "".join(out)

CORPO = f"""
<div class="cena verde" id="g">
  {segmentos(-1, False).replace('class="sg"', 'class="sg"')}
  <div class="eyebrow ey">Retrospectiva · conta de exemplo</div>
  <div id="gSeu">Seu</div>
  <div id="gAno">{ano_html()}</div>
  <div id="gEm">em 5 números.</div>
  <div id="gSub">De 1º de janeiro a 6 de dezembro de 2026.</div>
</div>
{"".join(cena_html(k, c) for k, c in enumerate(CENAS))}
{K.fim("Seu 2026 no timtimcash")}
"""

JS = f"""
const H={H}, DS={DS}, T0={T0}, FIM={FIM};
const CENAS={[dict(id=c['id'], num=c['num'], casas=c['casas'], R=c['R'], P=c['P']) for c in CENAS]};
const FITAS={[len(f) - 1 for _, f in FITAS]};
function revela(id, t, a){{ const r = 2300*prog(t, a, a+.5); $(id).style.clipPath = `circle(${{r.toFixed(1)}}px at 540px 560px)`; }}
function segs(k, t){{ for (let i=0;i<5;i++){{ const e = $('sg'+k+'_'+i); if (!e) continue;
    const w = i < k ? 1 : (i === k ? lin(t, T0[k], T0[k]+DS) : 0); e.style.width = (100*w)+'%'; }} }}
function render(t){{
  // gancho: "Seu 2026 em 5 números", com os algarismos girando desde o primeiro quadro
  FITAS.forEach((n, i) => {{ const p = pback(t, -.32 + .09*i, .3 + .09*i); $('fx'+i).style.transform = `translateY(${{(1-p)*110}}px)`; }});
  for (let i=0;i<5;i++){{ const e = $('sg-1_'+i); e.style.width = (100*pout(t, .15+.12*i, .45+.12*i))+'%'; }}
  aparece('gSub', t, .9, 0, 20, .4);
  // as cinco cenas: a cor nova se abre em círculo; o número conta, o rótulo entra, a tela real salta
  CENAS.forEach((c, k) => {{
    const a = T0[k];
    revela(c.id, t, a);
    $(c.id).style.visibility = t >= a ? 'visible' : 'hidden';
    segs(k, t);
    aparece(c.id+'e', t, a+.1, 0, 16, .3);
    const p = pout(t, a+.12, a+.9); const v = c.num*p;
    $(c.id+'v').textContent = fmt(v, c.casas);
    const n = $(c.id+'n'); n.style.opacity = lin(t, a+.1, a+.25);
    n.style.transform = `scale(${{.86 + .14*pback(t, a+.1, a+.55)}})`;
    aparece(c.id+'r', t, a+.35, 0, 26, .4);
    aparece(c.id+'s', t, a+.55, 0, 20, .4);
    aparece(c.id+'t', t, a+.75, 0, 10, .3);
    recorte(c.id+'p', t, a+.8, 0, c.R, [c.P[0], c.P[1]+80, c.P[2], 1], c.P, .5, false);
    anel(c.id+'a', t, a+1.3, 0);
  }});
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (verde, sem coral)
CAPA_CSS = f"""
#capa .eyebrow{{color:#fff}}
.ct{{position:absolute;left:90px;top:430px;width:900px}}
.ct .h1{{font-size:120px;line-height:.97;color:#fff}}
.ca{{position:absolute;left:62px;top:800px;font-size:420px;line-height:1;font-weight:700;letter-spacing:-.065em;color:#fff;font-variant-numeric:tabular-nums}}
.cs{{position:absolute;left:90px;top:1300px;width:900px;display:flex;gap:16px}}
.cs i{{flex:1;height:16px;border-radius:8px;background:#fff}}
.cs i.v{{background:{A.BRAND_DARK}}}
"""
CAPA_CORPO = f"""
{K.logo("verde")}
<div class="ct"><div class="eyebrow" style="margin-bottom:36px">Retrospectiva</div>
  <div class="h1">Seu ano em 5 números</div></div>
<div class="ca">2026</div>
<div class="cs"><i></i><i></i><i></i><i></i><i></i></div>
"""

HTML = C.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="verde")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
