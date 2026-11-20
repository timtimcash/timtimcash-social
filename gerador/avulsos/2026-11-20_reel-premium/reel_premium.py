# -*- coding: utf-8 -*-
"""Reel do lançamento do timtimcash Premium (20/11/2026) · capa verde suave.

Telas reais: captura.py, build 2026-11-20.1 (enviado pelo dono em 20/11/2026), celular 390 de largura em escala 3, conta de
exemplo (base_app/estado.py, a mesma dos posts), relógio em 20/11/2026 10:00. Conta Premium (assinatura mensal de exemplo do
cliente falso) e, para a tela Planos com os preços, a mesma conta no Grátis. Caixas dos destaques: medir.py (telas/destaques.json).
1. Menu aberto: o selo PREMIUM embaixo do logotipo e a coroa nas cinco telas do Premium.
2. Relatórios de outubro de 2026: "Acima do seu padrão · +4,9 pontos percentuais".
3. Comparar, outubro de 2026 contra outubro de 2025: out/26 R$ 8.215, out/25 R$ 7.940, diferença +R$ 275 (+3%).
4. Resultado (DRE) de outubro de 2026: receitas R$ 10.280,00, despesas R$ 8.215,00, resultado +R$ 2.065,00.
5. Simulação futura: Cenário base R$ 33,4 mil; Trocar de carro R$ 15,8 mil, "−R$ 17,6 mil que a base".
6. Remessas ao exterior (novembro de 2026): US$ 13.260 na carteira; +US$ 1.260,00 (+10,5% em US$); +R$ 6.982,89 (+11,6% em R$).
7. Planos, na conta no Grátis: Mensal R$ 14,90 por mês; Anual R$ 149 por ano, "2 meses grátis", "Sai a R$ 12,42 por mês".
Textos do Premium iguais aos do site (lista _PLN_LISTA_PREMIUM, chamada "Veja o seu dinheiro por inteiro.", preços e
"Desista em até 7 dias e receba tudo de volta."). A coroa é a do site (_PLN_COROA), nas cores do site (#F3DFA2 no verde,
#B8860B no claro); o fundo do gancho é o do cartão do Premium do site.

python3 reel_premium.py  |  REEL_PREVIA="0.2 0.8 1.6 2.6 3.6 4.9 6.6 8.6 10.6 12.6 14.6 16.6 18.6 20.4" python3 reel_premium.py
"""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev/equipes/js")
import comum as C
import tempos as T
K, A = C.K, C.A

TELAS = os.path.join(AQUI, "telas")
SAIDA = os.path.join(AQUI, "saida")
TRAB = os.path.join(AQUI, "trabalho")
D = json.load(open(os.path.join(TELAS, "destaques.json"), encoding="utf-8"))

# ---------------------------------------------------------------- conferência com as telas (os números do vídeo)
assert D["relatorios_out"]["resumo"][5].startswith("20% Acima do seu padrão · +4,9 pontos percentuais")
assert D["comparar_out_2025"]["diferenca"][5] == "Diferença +R$275 +3%"
assert D["dre_out"]["resultado"][5] == "RESULTADO Receitas menos despesas +R$ 2.065,00"
assert D["dre_out"]["receitas"][5] == "RECEITAS R$ 10.280,00" and D["dre_out"]["despesas"][5] == "DESPESAS 79,9% R$ 8.215,00"
assert D["simulacao"]["carro"][5] == "−R$ 17,6 mil que a base"
assert D["remessas"]["pilula_usd"][5] == "+US$ 1.260,00 +10,5% em US$" and D["remessas"]["pilula_brl"][5] == "+R$ 6.982,89 +11,6% em R$"
assert D["menu"]["selo"][5] == "PREMIUM"

# ---------------------------------------------------------------- caixas (px CSS da foto)
SELO = D["menu"]["selo"][:4]
ITENS = C.uniao(D["menu"]["relatorios"][:4], D["menu"]["remessas"][:4])
ITEM1 = D["menu"]["relatorios"][:4]
RESUMO = D["relatorios_out"]["resumo"][:4]
DIF = D["comparar_out_2025"]["diferenca"][:4]
RESULT = D["dre_out"]["resultado"][:4]
CARRO = D["simulacao"]["cartao_carro"][:4]   # o cartão inteiro do cenário "Trocar de carro" (com o "−R$ 17,6 mil que a base")
PILULAS = C.uniao(D["remessas"]["pilula_usd"][:4], D["remessas"]["pilula_brl"][:4])
OPS = C.uniao(D["planos_gratis"]["ops"], [212, 788.5, 89.3, 19.75])   # opções Mensal e Anual, com o selo "2 meses grátis" (medido em captura.py)

X1, X2, X3, X4, X5 = T.TROCAS
IMGS = [("f_menu", os.path.join(TELAS, "menu.png")), ("f_rel", os.path.join(TELAS, "relatorios_out.png")),
        ("f_comp", os.path.join(TELAS, "comparar_out_2025.png")), ("f_dre", os.path.join(TELAS, "dre_out.png")),
        ("f_sim", os.path.join(TELAS, "simulacao.png")), ("f_rem", os.path.join(TELAS, "remessas.png"))]

# ---------------------------------------------------------------- peças
OURO, OURO_CLARO, OURO_TINTA = "#B8860B", "#F3DFA2", "#8A6320"     # cores da coroa e do sobretítulo no site
FUNDO_PREMIUM = ("radial-gradient(120% 140% at 100% 0%,rgba(255,255,255,.13) 0%,rgba(255,255,255,0) 55%),"
                 "linear-gradient(135deg,#053F31 0%,#04694F 55%,#047857 100%)")
COROA_D = ('<path d="M3.3 8.3a1 1 0 0 1 1.6-1l3.5 2.8 2.75-4.55a1 1 0 0 1 1.7 0L15.6 10.1l3.5-2.8a1 1 0 0 1 1.6 1l-1.45 7.9a1 1 0 0 1-1 .8H5.75a1 1 0 0 1-1-.8z"/>'
           '<rect x="5" y="18.7" width="14" height="1.9" rx=".95"/>')


def coroa(cls="cw", cor=OURO):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="{cor}" aria-hidden="true">{COROA_D}</svg>'


CHECK = (f'<svg viewBox="0 0 16 16" width="44" height="44" fill="none" stroke="{A.BRAND_DARK}" stroke-width="2.2" stroke-linecap="round" '
         f'stroke-linejoin="round"><path d="M3.2 8.4l3 3 6.6-6.8"/></svg>')
BRILHO = '<path d="M12 0C12.9 7.6 16.4 11.1 24 12C16.4 12.9 12.9 16.4 12 24C11.1 16.4 7.6 12.9 0 12C7.6 11.1 11.1 7.6 12 0Z"/>'

# coroa grande do gancho: dourado em degradê, com um brilho que atravessa (recortado no desenho da coroa)
COROA_GRANDE = f"""<svg id="gCoroaSvg" viewBox="0 0 24 24" width="280" height="280" aria-hidden="true">
  <defs>
    <linearGradient id="ouro" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBEFC6"/><stop offset=".45" stop-color="#F3DFA2"/><stop offset="1" stop-color="#D9A848"/></linearGradient>
    <linearGradient id="faixa" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <clipPath id="recorte">{COROA_D}</clipPath>
  </defs>
  <g fill="url(#ouro)">{COROA_D}</g>
  <g clip-path="url(#recorte)"><rect id="gFaixa" x="-14" y="-4" width="7" height="32" fill="url(#faixa)" transform="rotate(18 12 12)"/></g>
</svg>"""

TIT = {  # títulos das cenas das telas (a coroa dourada antes do nome de cada tela do Premium)
    "t_menu": f'As telas com <span style="white-space:nowrap">a coroa {coroa()}</span> são do <b>Premium</b>.',
    "t_rel": f'{coroa()} <b>Relatórios</b>: o mês contra o seu padrão.',
    "t_comp": f'{coroa()} <b>Comparar</b>: dois períodos lado a lado.',
    "t_dre": f'{coroa()} <b>Resultado (DRE)</b>: quanto entrou, saiu e sobrou.',
    "t_sim": f'{coroa()} <b>Simulação futura</b>: e se você trocar de carro?',
    "t_rem": f'{coroa()} <b>Remessas ao exterior</b>: quanto rendeu, em dólar e em reais.',
    "t_mais": 'E mais, no <b>Premium</b>:',
    "t_preco": '<b>R$ 14,90</b> por mês ou <b>R$ 149</b> por ano.',
}
MAIS = ["Orçamentos e metas sem limite", "Aviso por <span style=\"white-space:nowrap\">e-mail</span> dos vencimentos", "Importar planilhas sem limite"]

CSS = f"""
.cw{{width:.8em;height:.8em;vertical-align:-.06em;fill:{OURO}}}
.cwf{{width:.9em;height:.9em;fill:{OURO_CLARO}}}
/* gancho: o fundo do cartão do Premium do site */
#g{{background:{FUNDO_PREMIUM};color:#fff}}
#gAnel{{position:absolute;right:-300px;bottom:-330px;width:1150px;height:1150px;border-radius:50%;border:96px solid rgba(255,255,255,.055)}}
#gLogo{{position:absolute;left:0;top:300px;width:1080px;display:flex;justify-content:center;opacity:0}}
#gCoroa{{position:absolute;left:400px;top:420px;width:280px;height:280px;opacity:0}}
.bri{{position:absolute;width:46px;height:46px;fill:{OURO_CLARO};opacity:0}}
#gH1{{position:absolute;left:90px;top:752px;width:900px;text-align:center;font-size:136px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#gH1 .w{{display:inline-block;opacity:0}}
#gPreco{{position:absolute;left:0;top:1052px;width:1080px;display:flex;justify-content:center;opacity:0}}
#gPreco span{{display:inline-flex;align-items:baseline;gap:16px;background:#fff;color:{A.BRAND_DARK};font-weight:700;font-size:64px;letter-spacing:-.03em;
  padding:26px 54px 28px;border-radius:999px;box-shadow:0 18px 40px -18px rgba(0,0,0,.45)}}
#gPreco small{{font-size:40px;font-weight:600;letter-spacing:-.01em}}
#gOu{{position:absolute;left:0;top:1206px;width:1080px;text-align:center;font-size:38px;font-weight:600;color:#CDEBDD;letter-spacing:-.01em;opacity:0}}
#gPerg{{position:absolute;left:120px;top:1324px;width:840px;text-align:center;font-size:58px;line-height:1.12;font-weight:700;letter-spacing:-.035em;color:#fff;opacity:0;text-wrap:balance}}
/* cena das telas */
#subPreco{{position:absolute;left:90px;top:432px;width:900px;font-size:36px;font-weight:600;color:{A.MUTED};letter-spacing:-.015em;opacity:0}}
.mais{{position:absolute;left:90px;width:900px;height:150px;display:flex;align-items:center;gap:28px;padding:0 36px;opacity:0}}
.mais i{{flex:none;display:flex;align-items:center;justify-content:center;width:80px;height:80px;border-radius:50%;background:{A.SOFT}}}
.mais span{{font-size:45px;font-weight:600;letter-spacing:-.03em;line-height:1.1;white-space:nowrap}}
#janela2{{opacity:0}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  {"".join(f'<div class="tit" id="{k}">{v}</div>' for k, v in TIT.items())}
  <div id="subPreco">Desista em até 7 dias e receba tudo de volta.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", IMGS)}{K.aneis("aSelo", "aItens", "aResumo", "aDif", "aResult", "aPil")}{K.aneis("aCarro", cor="coral")}</div>
  {"".join(f'<div class="mais card" id="m{i}" style="top:{660 + 200 * i}px"><i>{CHECK}</i><span>{t}</span></div>' for i, t in enumerate(MAIS))}
  <div class="nota" id="nota2">{K.NOTA}</div>
  <div class="janela" id="janela2">{C.camadas("tela2", [("f_plan", os.path.join(TELAS, "planos_gratis.png"))])}{K.aneis("aOps")}</div>
</div>

<div class="cena" id="g">
  <div id="gAnel"></div>
  <div id="gCoroa">{COROA_GRANDE}</div>
  {"".join(f'<svg class="bri" id="b{i}" viewBox="0 0 24 24" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px">{BRILHO}</svg>' for i, (x, y, s) in enumerate([(330, 452, 54), (716, 420, 40), (736, 630, 58), (318, 652, 34)]))}
  <div id="gLogo">{A.logo_horizontal("white", 66)}</div>
  <div id="gH1"><span class="w">Chegou</span> <span class="w">o</span> <span class="w">Premium.</span></div>
  <div id="gPreco"><span>R$ 14,90 <small>por mês</small></span></div>
  <div id="gOu">ou R$ 149 por ano, com 2 meses grátis</div>
  <div id="gPerg">Quer ver o seu dinheiro por inteiro?</div>
</div>

{K.fim(f'<span style="display:inline-flex;align-items:center;gap:20px">{coroa("cwf", OURO_CLARO)}timtimcash Premium</span>', "Assine em Planos, no menu do site.")}
"""

JS = f"""
const G_SAI={T.G_SAI}, J_ENTRA={T.JANELA_ENTRA}, SELO_T={T.SELO}, VARRE={list(T.VARRE)}, X=[{X1},{X2},{X3},{X4},{X5}], AT={T.ANEL_ATRASO};
const J_SAI={T.JANELA_SAI}, MAIS={list(T.MAIS)}, PRECO={T.PRECO}, PRECO_ANEL={T.PRECO_ANEL}, FIM={T.FIM};
const SELO={SELO}, ITENS={ITENS}, ITEM1={ITEM1}, RESUMO={RESUMO}, DIF={DIF}, RESULT={RESULT}, CARRO={CARRO}, PILULAS={PILULAS}, OPS={OPS};
const FOTOS=[[0,'f_menu'],[X[0],'f_rel'],[X[1],'f_comp'],[X[2],'f_dre'],[X[3],'f_sim'],[X[4],'f_rem']];
// câmera: o menu (o selo no alto, depois as telas com a coroa); cada tela com uma aproximação lenta
const CAM=[[0,0,195,262,1], [3.95,4.35,195,468,1],
  [X[0],X[0]+.01,195,330,1], [X[0]+.3,X[1]-.3,195,372,1.06],
  [X[1],X[1]+.01,195,470,1], [X[1]+.3,X[2]-.3,195,536,1.06],
  [X[2],X[2]+.01,195,372,1], [X[2]+.3,X[3]-.3,195,392,1.06],
  [X[3],X[3]+.01,195,300,1], [X[3]+.3,X[4]-.3,195,330,1.06],
  [X[4],X[4]+.01,195,330,1], [X[4]+.3,J_SAI,195,318,1.06]];
const CAM2=[[0,0,195,850,1], [PRECO+.3,FIM,195,858,1.05]];
// troca de tela (outra página do site): a janela sai pela esquerda e volta pela direita com a tela nova, trocada no meio
function deslize(t, trocas){{ let x = 0; trocas.forEach(s => {{ if (t >= s - .24 && t < s) x = -940*prog(t, s - .24, s);
  else if (t >= s && t < s + .3) x = 940*(1 - pout(t, s, s + .3)); }}); return x; }}
function render(t){{
  // 1. gancho: a coroa com brilho, "Chegou o Premium.", o preço e a pergunta
  const c = $('gCoroa'); const pc = pback(t, 0, .5); c.style.opacity = lin(t, 0, .12);
  c.style.transform = `translateY(${{(1-pc)*-40}}px) scale(${{(.55 + .45*pc).toFixed(3)}}) rotate(${{((1-pc)*-10).toFixed(2)}}deg)`;
  $('gFaixa').setAttribute('x', (-14 + 40*lin(t, .35, 1.15)).toFixed(2));
  [[.32,.95],[.42,1.05],[.5,1.2],[.6,1.3]].forEach(([a,b],i) => {{ const e = $('b'+i); const v = Math.sin(Math.PI*lin(t, a, b));
    e.style.opacity = v.toFixed(3); e.style.transform = `scale(${{(.3 + .9*v).toFixed(3)}}) rotate(${{(45*lin(t, a, b)).toFixed(1)}}deg)`; }});
  some('gLogo', t, .05, 0, 16);
  palavras('gH1', t, .2, 0, .1);
  salta('gPreco', t, .75, .45);
  some('gOu', t, 1.1, 0, 18);
  some('gPerg', t, 1.45, 0, 24);
  $('gAnel').style.transform = `rotate(${{(12*t).toFixed(2)}}deg)`;
  saiCima('g', t, G_SAI);

  // 2. as telas reais do Premium, na mesma janela
  titulo('t_menu', t, J_ENTRA+.05, X[0]-.3); titulo('t_rel', t, X[0], X[1]-.3); titulo('t_comp', t, X[1], X[2]-.3);
  titulo('t_dre', t, X[2], X[3]-.3); titulo('t_sim', t, X[3], X[4]-.3); titulo('t_rem', t, X[4], J_SAI);
  janela('janela', t, J_ENTRA, J_SAI); nota('nota', t, J_ENTRA, J_SAI);
  $('janela').style.transform += ` translateX(${{deslize(t, X).toFixed(1)}}px)`;
  const cam = camera('tela', t, CAM);
  fotos(FOTOS, t);
  anelCam('aSelo', SELO, cam, 14); anel('aSelo', t, SELO_T, 3.95);
  // o anel desce do primeiro item com coroa até o último (Relatórios a Remessas ao exterior)
  const v = pout(t, VARRE[0], VARRE[1]);
  const R = [ITENS[0], ITENS[1], ITENS[2], ITEM1[3] + (ITENS[3] - ITEM1[3])*v];
  anelCam('aItens', R, cam, 8); anel('aItens', t, VARRE[0]-.1, X[0]-.25);
  anelCam('aResumo', RESUMO, cam, 8); anel('aResumo', t, X[0]+AT, X[1]-.3);
  anelCam('aDif', DIF, cam, 8); anel('aDif', t, X[1]+AT, X[2]-.3);
  anelCam('aResult', RESULT, cam, 8); anel('aResult', t, X[2]+AT, X[3]-.3);
  anelCam('aCarro', CARRO, cam, 8); anel('aCarro', t, X[3]+AT, X[4]-.3);
  anelCam('aPil', PILULAS, cam, 10); anel('aPil', t, X[4]+AT, J_SAI);

  // 3. e mais, no Premium
  titulo('t_mais', t, J_SAI+.2, PRECO-.35);
  MAIS.forEach((a, i) => aparece('m'+i, t, a, PRECO-.35, 50, .38));

  // 4. o preço, na tela Planos (conta no Grátis)
  titulo('t_preco', t, PRECO, FIM); some('subPreco', t, PRECO+.25, FIM, 20);
  janela('janela2', t, PRECO, FIM); nota('nota2', t, PRECO, FIM);
  const cam2 = camera('tela2', t, CAM2);
  anelCam('aOps', OPS, cam2, 12); anel('aOps', t, PRECO_ANEL, FIM);

  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('suave')}
  <div style="position:absolute;left:390px;top:480px;width:300px;height:300px">{coroa("cg", OURO)}</div>
  <div style="position:absolute;left:90px;top:850px;width:900px;text-align:center;font-size:150px;line-height:.96;font-weight:700;letter-spacing:-.05em;color:{A.INK}">Chegou o Premium.</div>
  <div style="position:absolute;left:0;top:1212px;width:1080px;display:flex;justify-content:center">
    <span style="display:inline-flex;align-items:baseline;gap:16px;background:{A.BRAND_DARK};color:#fff;font-weight:700;font-size:66px;letter-spacing:-.03em;padding:28px 58px 30px;border-radius:999px">R$ 14,90 <small style="font-size:42px;font-weight:600;letter-spacing:-.01em">por mês</small></span></div>
  <div style="position:absolute;left:0;top:1386px;width:1080px;text-align:center;font-size:40px;font-weight:600;color:{A.BRAND_DEEP};letter-spacing:-.01em">ou R$ 149 por ano</div>"""
    return K.pagina_capa(corpo, ".cg{width:300px;height:300px}", fundo="suave")


if __name__ == "__main__":
    K.executar(C.pagina(CORPO, CSS, JS), T.DUR, SAIDA, TRAB, capa_html=capa())
