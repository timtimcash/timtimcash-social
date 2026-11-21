# -*- coding: utf-8 -*-
"""Vídeo 2 · timtimcash Premium: cinco perguntas que o Premium responde (22,6 s) · capa verde suave.

Telas reais: captura.py, build 2026-11-20.8 (o que está no ar), a conta de exemplo com o Premium, no tema escuro do site, celular
390 px em escala 3, relógio em 21/11/2026 10:00. Para os preços, a tela Planos da mesma conta no Grátis.
1. Relatórios de outubro de 2026: "Acima do seu padrão · +4,9 pontos percentuais"; Receita guardada 20,1%; "Sua média de 12 meses é 15,2%".
2. Comparar (Despesas), out/26 contra out/25: R$ 8.215 e R$ 7.940; "Diferença +R$ 275 +3%".
3. Resultado (DRE) de outubro de 2026: "RESULTADO · Receitas menos despesas · +R$ 2.065,00".
4. Simulação futura: "Trocar de carro · −R$ 17,6 mil que a base", até set/27; em Comparar cenários, R$ 33.360,00 e R$ 15.760,00.
5. Remessas ao exterior: "+US$ 1.260,00 +10,5% em US$" e "+R$ 6.982,89 +11,6% em R$".
6. Planos: Mensal R$ 14,90 por mês; Anual R$ 149 por ano, "2 meses grátis"; "Desista em até 7 dias e receba tudo de volta."
Cada resposta em destaque repete um número que está na tela. A coroa e o fundo verde são os do Premium no site.

python3 video2.py  |  REEL_PREVIA="0.4 1.6 2.6 4.4 7.2 9.9 11.9 13.3 15.4 18 20.6 22" python3 video2.py
"""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI); sys.path.insert(0, os.path.dirname(AQUI))
import kitv as KV
import tempos as T
K, A, C = KV.K, KV.A, KV.C
TELAS = os.path.join(AQUI, "telas"); SAIDA = os.path.join(AQUI, "saida"); TRAB = os.path.join(AQUI, "trabalho")
CX = json.load(open(os.path.join(TELAS, "caixas.json"), encoding="utf-8"))
for _k in CX:
    for _c in CX[_k]:
        if isinstance(CX[_k][_c], list) and CX[_k][_c] and isinstance(CX[_k][_c][-1], str): CX[_k][_c][-1] = CX[_k][_c][-1].replace(" ", " ")

# ---------------------------------------------------------------- conferência com as telas (os números das respostas)
assert CX["relatorios"]["resumo"][4].startswith("20% Acima do seu padrão · +4,9 pontos percentuais Sua média de 12 meses é 15,2% da receita.")
assert CX["relatorios"]["pct"][4] == "20,1%"
assert CX["comparar"]["dif"][4] == "Diferença +R$275 +3%" and "out/25" in CX["comparar"]["com"][4] and "out/26 contra out/25" in CX["comparar"]["totais"][4]
assert CX["dre"]["resultado"][4] == "RESULTADO Receitas menos despesas +R$ 2.065,00"
assert CX["simulacao"]["menos"][4] == "−R$ 17,6 mil que a base" and "até set/27" in CX["simulacao"]["carro"][4]
assert CX["sim_comparar"]["vs"][4] == "Trocar de carro R$ 15.760,00 −R$ 17.600,00 vs Cenário base"
assert CX["remessas"]["usd"][4] == "+US$ 1.260,00 +10,5% em US$" and CX["remessas"]["brl"][4] == "+R$ 6.982,89 +11,6% em R$"
assert CX["planos"]["mensal"][4] == "Mensal R$ 14,90 por mês Cobrado todo mês" and CX["planos"]["anual"][4] == "Anual 2 meses grátis R$ 149 por ano Sai a R$ 12,42 por mês"
assert CX["planos"]["seguro"][4] == "Desista em até 7 dias e receba tudo de volta."

# ---------------------------------------------------------------- caixas (px CSS da foto)
c4 = lambda k, n: CX[k][n][:4]
RESUMO, DIF, RESULT = c4("relatorios", "resumo"), c4("comparar", "dif"), c4("dre", "resultado")
CARRO, VS = c4("simulacao", "carro"), c4("sim_comparar", "vs")
PILULAS = C.uniao(c4("remessas", "usd"), c4("remessas", "brl"))
OPS = C.uniao(CX["planos"]["ops"][:4], c4("planos", "selo"))
SEG = [56, CX["planos"]["seguro"][1] - 24, 278, 46]     # "Pagamento seguro pela Stripe" e "Desista em até 7 dias e receba tudo de volta."

t = lambda n: os.path.join(TELAS, n + ".png")
IMGS = [(n, t(n)) for n in ["relatorios", "comparar", "dre", "simulacao", "sim_comparar", "remessas", "planos"]]
Q = T.Q
FOTOS = [[0, "relatorios"], [Q[1], "comparar"], [Q[2], "dre"], [Q[3], "simulacao"], [Q[3] + T.GRAFICO, "sim_comparar", .22], [Q[4], "remessas"], [T.PRECO, "planos"]]

PERG = [("Guardei mais que", "o meu normal?"), ("O que mudou", "em um ano?"), ("Quanto sobrou,", "de verdade?"),
        ("E se eu trocar", "de carro?"), ("Quanto rendeu lá", "fora, em reais?")]
ONDE = ["Relatórios", "Comparar", "Resultado (DRE)", "Simulação futura", "Remessas ao exterior"]
RESP = [("20,1% guardados", "A sua média de 12 meses: 15,2%."), ("Despesas: +R$ 275", "Outubro de 2026 contra outubro de 2025."),
        ("+R$ 2.065,00", "O resultado de outubro de 2026."), ("−R$ 17,6 mil", "No saldo de set/27, contra o cenário base."),
        ("+11,6% em reais", "E +10,5% em dólar, na carteira de hoje.")]

BRILHO = '<path d="M12 0C12.9 7.6 16.4 11.1 24 12C16.4 12.9 12.9 16.4 12 24C11.1 16.4 7.6 12.9 0 12C7.6 11.1 11.1 7.6 12 0Z"/>'
COROA_GRANDE = f"""<svg viewBox="0 0 24 24" width="150" height="150" aria-hidden="true">
  <defs><linearGradient id="ouro" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBEFC6"/><stop offset=".45" stop-color="#F3DFA2"/><stop offset="1" stop-color="#D9A848"/></linearGradient>
    <linearGradient id="faixa" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <clipPath id="rec">{KV.COROA_D}</clipPath></defs>
  <g fill="url(#ouro)">{KV.COROA_D}</g><g clip-path="url(#rec)"><rect id="gFaixa" x="-14" y="-4" width="7" height="32" fill="url(#faixa)" transform="rotate(18 12 12)"/></g></svg>"""

CSS = f"""
#tl{{background:{KV.FUNDO_NOITE};color:#fff}}
/* gancho */
#g{{background:{KV.FUNDO_PREMIUM};color:#fff}}
.anelzao{{position:absolute;right:-320px;bottom:-360px;width:1200px;height:1200px;border-radius:50%;border:100px solid rgba(255,255,255,.05)}}
#gLogo{{position:absolute;left:0;top:300px;width:1080px;display:flex;justify-content:center;opacity:0}}
#gCoroa{{position:absolute;left:465px;top:372px;width:150px;height:150px;opacity:0}}
.bri{{position:absolute;fill:{KV.OURO_CLARO};opacity:0}}
#gN5{{position:absolute;left:0;top:486px;width:1080px;text-align:center;font-size:380px;line-height:.9;font-weight:700;letter-spacing:-.06em;color:{KV.OURO_CLARO};opacity:0}}
#gH{{position:absolute;left:60px;top:826px;width:960px;text-align:center;font-size:146px;line-height:1.0;font-weight:700;letter-spacing:-.06em;white-space:nowrap}}
#gS{{position:absolute;left:90px;top:994px;width:900px;text-align:center;font-size:76px;line-height:1.05;font-weight:700;letter-spacing:-.045em}}
#gS b{{color:{KV.OURO_CLARO};font-weight:700}}
#gNums{{position:absolute;left:0;top:1132px;width:1080px;display:flex;justify-content:center;gap:26px}}
.gn{{width:110px;height:110px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:54px;font-weight:700;color:{KV.OURO_CLARO};
  box-shadow:inset 0 0 0 4px rgba(243,223,162,.7);opacity:0}}
#gP{{position:absolute;left:0;top:1296px;width:1080px;text-align:center;font-size:42px;font-weight:600;letter-spacing:-.02em;color:#D9F3E7;opacity:0}}
/* perguntas */
.pe{{position:absolute;left:90px;top:282px;width:900px}}
.pey{{display:flex;align-items:center;gap:14px;font-size:28px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{KV.OURO_CLARO};opacity:0}}
.pey svg{{width:34px;height:34px}}
.pey i{{font-style:normal;color:#A9B8AE;letter-spacing:.12em}}
.peq{{font-size:76px;line-height:1.04;font-weight:700;letter-spacing:-.05em;color:#fff;margin-top:16px}}
.peq b{{color:{KV.OURO_CLARO};font-weight:700}}
.peq small{{font-size:40px;font-weight:600;letter-spacing:-.02em;color:#D9F3E7}}
#segs{{position:absolute;left:650px;top:295px;display:flex;gap:10px;opacity:0}}
#segs i{{display:block;width:60px;height:8px;border-radius:4px;background:rgba(255,255,255,.16);overflow:hidden}}
#segs i b{{display:block;height:8px;width:0;background:{KV.OURO_CLARO};border-radius:4px}}
/* fechamento */
#fim{{background:{KV.FUNDO_PREMIUM};color:#fff}}
#fCol{{position:absolute;left:0;top:430px;width:1080px;display:flex;flex-direction:column;align-items:center;text-align:center}}
#fNome{{display:flex;align-items:center;gap:20px;font-size:68px;font-weight:700;letter-spacing:-.045em;margin-top:84px}}
#fNome svg{{width:62px;height:62px}}
#fL1{{font-size:46px;font-weight:600;letter-spacing:-.025em;margin-top:26px;color:{KV.OURO_CLARO}}}
#fL2{{font-size:38px;font-weight:500;letter-spacing:-.02em;margin-top:22px;color:#D9F3E7}}
"""

perguntas = "".join(
    f'<div class="pe"><div class="pey" id="py{i}">{KV.coroa("", KV.OURO_CLARO)}{ONDE[i]}</div>'
    f'<div class="peq">{KV.mk(f"pa{i}", a)}{KV.mk(f"pb{i}", b)}</div></div>' for i, (a, b) in enumerate(PERG))
respostas = "".join(f'<div class="resp" id="r{i}"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(RESP))

CORPO = f"""
<div class="cena noite" id="tl">
  {perguntas}
  <div class="pe"><div class="pey" id="py5">{KV.coroa("", KV.OURO_CLARO)}Planos</div>
    <div class="peq">{KV.mk("pa5", "<b>R$ 14,90</b> por mês")}{KV.mk("pb5", "ou <b>R$ 149</b> por ano.")}</div></div>
  <div id="segs">{"<i><b></b></i>" * 5}</div>
  <div class="nota2" id="nota">{KV.NOTA}</div>
  {KV.aparelho("fone", "tela", IMGS, K.aneis("a0", "a1", "a2", "a3", "a3b", "a4", "a5", "a5b"), escuro=True)}
  {respostas}
</div>

<div class="cena" id="g">
  <div class="anelzao" id="gAnel"></div>
  <div id="gLogo">{A.logo_horizontal("white", 62)}</div>
  <div id="gCoroa">{COROA_GRANDE}</div>
  {"".join(f'<svg class="bri" id="b{i}" viewBox="0 0 24 24" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px">{BRILHO}</svg>' for i, (x, y, s) in enumerate([(390, 380, 44), (650, 366, 34), (664, 486, 46), (380, 500, 28)]))}
  <div id="gN5">5</div>
  <div id="gH">{KV.mk("gH1", "perguntas.")}</div>
  <div id="gS">{KV.mk("gS1", "O <b>Premium</b> responde.")}</div>
  <div id="gNums">{"".join(f'<div class="gn" id="gn{i}">{i + 1}</div>' for i in range(5))}</div>
  <div id="gP">A partir de R$ 12,42 por mês, no plano anual.</div>
</div>

<div class="cena" id="fim" style="transform:translateY(1920px)">
  <div class="anelzao" id="fAnel"></div>
  <div id="fCol">{A.logo_vertical("white", 290)}
    <div id="fNome">{KV.coroa("", KV.OURO_CLARO)}timtimcash Premium</div>
    <div id="fL1">Veja o seu dinheiro por inteiro.</div>
    <div id="fL2">Assine em Planos, no menu do site.</div>
    <div style="margin-top:64px"><span class="pill">Link na bio {A.ARROW}</span></div>
  </div>
</div>
"""

JS = f"""
const BAR={T.BAR}, Q={json.dumps(Q)}, AN={T.ANEL}, RS={T.RESP}, GRAF={T.GRAFICO}, PRECO={T.PRECO}, FIM={T.FIM};
const RESUMO={RESUMO}, DIF={DIF}, RESULT={RESULT}, CARRO={CARRO}, VS={VS}, PILULAS={PILULAS}, OPS={OPS}, SEG={SEG};
const FOTOS={json.dumps(FOTOS)};
const INI=[...Q, PRECO], FIMS=[...Q.slice(1), PRECO, FIM];
// câmera: cada tela começa parada no destaque e chega um pouco mais perto
const P=[[195,395],[195,612],[195,372],[195,345],[195,300]];
const CAM=[[0,0,195,395,1]];
P.forEach(([x,y],i) => {{ CAM.push([Q[i], Q[i]+.01, x, y, 1]);
  if (i === 3){{ CAM.push([Q[i]+.3, Q[i]+GRAF-.05, x, y+8, 1.03]); CAM.push([Q[i]+GRAF, Q[i]+GRAF+.01, 195, 410, 1]); CAM.push([Q[i]+GRAF+.2, Q[i+1]-.2, 195, 418, 1.04]); }}
  else CAM.push([Q[i]+.3, FIMS[i]-.2, x, y+8, 1.05]); }});
CAM.push([PRECO, PRECO+.01, 195, 955, 1]); CAM.push([PRECO+.3, FIM, 195, 962, 1.03]);
function render(t){{
  // 1. gancho: a coroa, "5 perguntas." e os cinco números
  const c = $('gCoroa'); const pc = pback(t, 0, .5); c.style.opacity = lin(t, 0, .12);
  c.style.transform = `translateY(${{((1-pc)*-40).toFixed(1)}}px) scale(${{(.55+.45*pc).toFixed(3)}}) rotate(${{((1-pc)*-10).toFixed(2)}}deg)`;
  $('gFaixa').setAttribute('x', (-14 + 40*lin(t, .35, 1.15)).toFixed(2));
  [[.3,.95],[.4,1.05],[.5,1.2],[.6,1.3]].forEach(([a,b],i) => {{ const e = $('b'+i); const v = Math.sin(Math.PI*lin(t, a, b));
    e.style.opacity = v.toFixed(3); e.style.transform = `scale(${{(.3+.9*v).toFixed(3)}}) rotate(${{(45*lin(t, a, b)).toFixed(1)}}deg)`; }});
  some('gLogo', t, .05, 0, 16);
  const n5 = $('gN5'); const p5 = pback(t, .1, .6); n5.style.opacity = lin(t, .1, .22); n5.style.transform = `scale(${{(.6+.4*p5).toFixed(4)}})`;
  sobeTxt('gH1', t, .32, 0, .5); sobeTxt('gS1', t, .8, 0, .5);
  for (let i=0;i<5;i++){{ const a = 1.25 + .12*i, e = $('gn'+i); const p = pback(t, a, a+.4); e.style.opacity = lin(t, a, a+.1); e.style.transform = `scale(${{(.5+.5*p).toFixed(3)}})`; }}
  some('gP', t, 1.9, 0, 16);
  $('gAnel').style.transform = `rotate(${{(12*t).toFixed(2)}}deg)`;
  saiCima('g', t, Q[0]-.12);

  // 2. as cinco perguntas e o preço: o título em cima, a tela real no aparelho e a resposta em destaque
  fone('fone', t, Q[0]-.2, FIM-.12); nota2('nota', t, Q[0]-.1, FIM-.2);
  $('segs').style.opacity = Math.min(lin(t, Q[0], Q[0]+.3), 1-lin(t, PRECO-.25, PRECO));
  document.querySelectorAll('#segs i b').forEach((e, i) => {{ e.style.width = (60*clamp((t-Q[i])/(BAR-.1), 0, 1)).toFixed(1)+'px'; }});
  for (let i=0;i<6;i++){{ const a = INI[i], b = FIMS[i]-.26;
    const e = $('py'+i); e.style.opacity = Math.min(lin(t, a, a+.25), 1-lin(t, b, b+.2));
    sobeTxt('pa'+i, t, a+.02, b, .5); sobeTxt('pb'+i, t, a+.13, b+.03, .5);
    if (i<5) resposta('r'+i, t, a+RS, b); }}
  desliza('tela_d', t, [...Q.slice(1), PRECO]);
  const cam = camera('tela', t, CAM, 780, 780);
  fotos(FOTOS, t);
  [['a0',RESUMO,0],['a1',DIF,1],['a2',RESULT,2],['a4',PILULAS,4],['a5',OPS,5]].forEach(([id,r,i]) => {{
    anelCam(id, r, cam, 8, 780, 780); anelP(id, t, INI[i]+AN, FIMS[i]-.28); }});
  anelCam('a3', CARRO, cam, 6, 780, 780); anelP('a3', t, Q[3]+.55, Q[3]+GRAF-.12);
  anelCam('a5b', SEG, cam, 4, 780, 780); anelP('a5b', t, PRECO+1.45, FIM-.28);
  anelCam('a3b', VS, cam, 6, 780, 780); anelP('a3b', t, Q[3]+GRAF+.35, Q[4]-.28);

  // 3. fechamento
  sobe('fim', t, FIM);
  $('fAnel').style.transform = `rotate(${{(12*(t-FIM)).toFixed(2)}}deg)`;
}}
"""


def capa():
    corpo = f"""{K.logo('suave')}
  <div style="position:absolute;left:90px;top:430px;width:900px;display:flex;align-items:center;gap:16px;font-size:32px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{KV.OURO_TINTA}">{KV.coroa("", KV.OURO, 'style="width:44px;height:44px"')}timtimcash Premium</div>
  <div style="position:absolute;left:78px;top:470px;font-size:560px;line-height:1;font-weight:700;letter-spacing:-.06em;color:{A.BRAND_DARK}">5</div>
  <div style="position:absolute;left:430px;top:600px;width:580px;font-size:118px;line-height:.98;font-weight:700;letter-spacing:-.055em;color:{A.INK}">perguntas que o Premium responde.</div>
  <div style="position:absolute;left:90px;top:1130px;width:900px;display:flex;flex-direction:column;gap:20px">
    {"".join(f'<div style="height:104px;border-radius:32px;background:#fff;display:flex;align-items:center;padding:0 38px;font-size:46px;font-weight:600;letter-spacing:-.03em;color:{A.INK}">{a} {b}</div>' for a, b in PERG[:4])}
  </div>"""
    return K.pagina_capa(corpo, KV.CSS, fundo="suave")


if __name__ == "__main__":
    K.executar(KV.pagina(CORPO, CSS, JS), T.DUR, SAIDA, TRAB, capa_html=capa())
