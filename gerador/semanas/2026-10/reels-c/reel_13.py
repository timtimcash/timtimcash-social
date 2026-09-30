# -*- coding: utf-8 -*-
"""Reel 30/10/2026 · "O 13º vem aí: veja agora o que ele muda no seu saldo" (1080 × 1920, 30 fps).

python3 reel_13.py <saida.mp4> [capa.jpg]
Telas: capturas/13/, feitas por app/captura_13.py no celular (conta fictícia, relógio da página em
30/09/2026), com toques reais: o cartão jan/27 da linha do tempo, o menu da linha Salário,
"Ajustar por mês", "+ Um mês específico" (mês nov/26, valor R$ 14.940) e "Concluir".
No código do site (_simValorMes), a regra de um mês SUBSTITUI o valor daquele mês: por isso
novembro leva R$ 9.960 + R$ 4.980 = R$ 14.940, e não só os R$ 4.980.
"""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from reelkit import A, NOTA, pagina, fechamento, executar

TELAS = os.path.join(AQUI, "capturas", "13")
CX = json.load(open(os.path.join(TELAS, "caixas.json"), encoding="utf-8"))
SAIDA = os.path.abspath(sys.argv[1]); CAPA = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else None
DUR = 24.3

# ---------------------------------------------------------------- posições (px CSS das capturas)
SALDO_A = [29, 110.5, 140, 42]            # "R$ 37.720" (antes)
SALDO_F = [29, 110.5, 140, 42]            # "R$ 42.700" (depois)
JAN = CX["antes_jan"]["toque_jan"]         # toque no cabeçalho do cartão jan/27
IMPOSTOS = [[42, 1480, 319, 31]]           # linha "Impostos e Taxas · ajuste do mês · R$ 4.800" (cartão aberto)
MENU = CX["salario"]["menu"]; AJ = CX["folha"]["ajustar"]; UM = CX["modal"]["um_mes"]
REGRA = CX["regra"]["item"]; RESUMO = CX["regra"]["resumo"]; CONC = CX["regra"]["concluir"]
cen = lambda b: [round(b["x"] + b["w"] / 2, 1), round(b["y"] + b["h"] / 2, 1)]
SELETOR = [300, round(REGRA["y"] + 20, 1)]  # o seletor do mês, na linha da regra
PONTO_NOV = CX["depois"]["grafico"]["datasets"][0]["pts"][3]   # nov/26 no gráfico do depois
assert CX["depois"]["grafico"]["labels"][3] == "nov/26"
assert CX["antes"]["valor"]["txt"] == "R$ 37.720" and CX["depois"]["valor"]["txt"] == "R$ 42.700"

# ---------------------------------------------------------------- capa (verde): os meses e o caminho do 13º
def ladrilho(x, rot, cor_fundo, cor_txt, dentro="", ident=""):
    return f"""<g {ident}><rect x="{x}" y="0" width="192" height="262" rx="36" fill="{cor_fundo}"/>
  <text x="{x + 96}" y="62" text-anchor="middle" font-family="Inter" font-weight="700" font-size="36" letter-spacing="1" fill="{cor_txt}">{rot}</text>
  {dentro}</g>"""
XS = [90, 326, 562, 798]
CAPA_SVG = f"""<svg style="position:absolute;left:0;top:1080px" width="1080" height="520" viewBox="0 0 1080 520">
  <defs><marker id="seta" viewBox="0 0 12 12" refX="7" refY="6" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse">
    <path d="M1.5 1.5 L10 6 L1.5 10.5" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
  <path id="arco" d="M{XS[1] + 96} 218 C {XS[1] + 150} 60, {XS[3] + 40} 60, {XS[3] + 96} 208" fill="none" stroke="#fff" stroke-width="9"
    stroke-linecap="round" stroke-dasharray="3 20" marker-end="url(#seta)"/>
  <g transform="translate(0,240)">
    {ladrilho(XS[0], "out", A.BRAND_DARK, "#fff")}
    {ladrilho(XS[1], "nov", "#fff", A.BRAND_DARK, f'<text id="t13" x="{XS[1] + 96}" y="178" text-anchor="middle" font-family="Inter" font-weight="700" font-size="92" letter-spacing="-3" fill="{A.BRAND_DARK}">13º</text><text x="{XS[1] + 96}" y="226" text-anchor="middle" font-family="Inter" font-weight="600" font-size="28" fill="{A.BRAND_DARK}">1ª parcela</text>', 'id="gNov"')}
    {ladrilho(XS[2], "dez", A.BRAND_DARK, "#fff")}
    {ladrilho(XS[3], "jan", A.MENTA_CLARA, A.BRAND_DEEP, f'<text x="{XS[3] + 96}" y="150" text-anchor="middle" font-family="Inter" font-weight="700" font-size="42" fill="{A.BRAND_DEEP}">IPVA</text><text x="{XS[3] + 96}" y="204" text-anchor="middle" font-family="Inter" font-weight="700" font-size="42" fill="{A.BRAND_DEEP}">IPTU</text>')}
  </g>
</svg>"""

def camada(ident, imgs, extra=""):
    oculta = ' style="opacity:0"'
    ims = "".join(f'<img id="{i}" src="file://{TELAS}/{f}"{oculta if k else ""}>' for k, (i, f) in enumerate(imgs))
    return f'<div class="camada" id="{ident}" style="opacity:0">{ims}{extra}</div>'

CORPO = f"""
<div class="cena" id="papel">
  <div class="tit" id="t1">No cenário base, o saldo chega a <b>R$ 37.720</b> em set/27.</div>
  <div class="tit" id="t2">Em janeiro, IPVA e IPTU somam <b>R$ 4.800</b>.</div>
  <div class="tit" id="t3">A 1ª parcela do 13º é metade do salário: <b>R$ 4.980</b>.</div>
  <div class="tit" id="t4">Só em nov/26: R$ 9.960 + R$ 4.980 = <b>R$ 14.940</b>.</div>
  <div class="tit" id="t5">Guardada, a parcela leva o saldo final a <b>R$ 42.700</b>.</div>
  <div class="nota" id="nota">{NOTA}</div>
  <div id="janela">
    {camada("cA", [("iA", "antes.png"), ("iA2", "antes_jan.png")],
            '<div class="anel" id="aSaldoA"></div><div class="onda" id="oJan"></div><div class="toque" id="qJan"></div>')}
    {camada("cB", [("iB", "salario.png"), ("iC", "folha.png"), ("iD", "modal.png"), ("iD2", "modal_regra_nova.png"), ("iE", "modal_regra.png")],
            '<div class="anel" id="aRegra"></div>'
            '<div class="onda" id="oMenu"></div><div class="toque" id="qMenu"></div><div class="onda" id="oAj"></div><div class="toque" id="qAj"></div>'
            '<div class="onda" id="oUm"></div><div class="toque" id="qUm"></div><div class="onda" id="oSel"></div><div class="toque" id="qSel"></div>'
            '<div class="onda" id="oConc"></div><div class="toque" id="qConc"></div>')}
    {camada("cF", [("iF", "depois.png")], '<div class="anel" id="aSaldoF"></div><div class="anel redondo" id="aNov"></div>')}
  </div>
</div>

<div class="cena" id="licao" style="opacity:0">
  <div style="position:absolute;left:90px;top:330px;width:900px">
    <div class="h1" style="font-size:100px">Guardada, a 1ª parcela cobre o janeiro caro.</div>
    <div id="conta" style="margin-top:56px;background:#fff;border:3px solid {A.FIO};border-radius:36px;padding:14px 44px">
      <div class="lc"><span class="lc-v num" style="color:{A.BRAND_DARK}">+R$ 4.980</span><span class="lc-r">1ª parcela do 13º · nov/26</span></div>
      <div class="lc"><span class="lc-v num" style="color:{A.RED_TEXT}">−R$ 4.800</span><span class="lc-r">IPVA e IPTU · jan/27</span></div>
      <div class="lc" style="border-bottom:0"><span class="lc-v num">+R$ 180</span><span class="lc-r">ainda sobra</span></div>
    </div>
    <div class="apoio" id="lei" style="margin-top:34px;font-size:30px;line-height:1.35">Lei 4.749/1965: a 1ª parcela, metade do salário do mês anterior, sai entre fevereiro e novembro; o 13º inteiro, até 20 de dezembro. Valores da conta de exemplo.</div>
  </div>
</div>

<div class="cena verde" id="capa">
  <div style="position:absolute;left:90px;top:290px">{A.logo_horizontal("white", 60)}</div>
  <div style="position:absolute;left:90px;top:520px;width:900px">
    <div class="eyebrow" style="margin-bottom:40px">13º salário</div>
    <div class="h1" id="gancho" style="font-size:116px;text-wrap:initial">O 13º vem aí.<br>O que ele muda no seu saldo?</div>
  </div>
  {CAPA_SVG}
</div>

{fechamento("Simulação futura no timtimcash")}
<style>
.camada{{position:absolute;left:0;top:0;width:1170px;transform-origin:0 0}}
.camada img{{position:absolute;left:0;top:0;width:1170px}}
.anel.redondo{{border-radius:50%}}
.lc{{display:flex;align-items:baseline;gap:28px;padding:26px 0;border-bottom:3px solid {A.FIO}}}
.lc-v{{font-size:62px;font-weight:700;letter-spacing:-.04em;min-width:300px;color:{A.INK}}}
.lc-r{{font-size:36px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em}}
</style>
"""

JS = f"""
const SALDO_A={SALDO_A}, SALDO_F={SALDO_F}, IMPOSTOS={IMPOSTOS};
const REGRA={[REGRA['x'], REGRA['y'], REGRA['w'], REGRA['h']]}, RESUMO=[[{RESUMO['x']}, {RESUMO['y']}, {RESUMO['w']}, {RESUMO['h']}]];
const P_NOV=[{PONTO_NOV['x']:.1f}, {PONTO_NOV['y']:.1f}];
function cam(id, topo, esq, Z){{ $(id).style.transform = `translate(${{-esq*Z}}px, ${{-topo*Z}}px) scale(${{Z/3}})`; }}
function mover(el, id){{ $(id).appendChild(el); }}
caixa($('aSaldoA'), SALDO_A, 20); caixa($('aSaldoF'), SALDO_F, 20);
caixa($('aRegra'), REGRA, [18, 14, 18, 14]);
{{ const r=22; const a=$('aNov'); a.style.left=(P_NOV[0]*3-r*3)+'px'; a.style.top=(P_NOV[1]*3-r*3)+'px'; a.style.width=(r*6)+'px'; a.style.height=(r*6)+'px'; }}
// marca-texto: cada um na sua camada
marcas('mImp', IMPOSTOS, null, 'cA'); marcas('mRes', RESUMO, null, 'cB');
ponto($('qJan'), {JAN['x']}, {JAN['y']}); ponto($('oJan'), {JAN['x']}, {JAN['y']});
ponto($('qMenu'), ...{cen(MENU)}); ponto($('oMenu'), ...{cen(MENU)});
ponto($('qAj'), ...{cen(AJ)}); ponto($('oAj'), ...{cen(AJ)});
ponto($('qUm'), ...{cen(UM)}); ponto($('oUm'), ...{cen(UM)});
ponto($('qSel'), ...{SELETOR}); ponto($('oSel'), ...{SELETOR});
ponto($('qConc'), ...{cen(CONC)}); ponto($('oConc'), ...{cen(CONC)});
const arco = $('arco'); const LA = arco.getTotalLength();
function render(t){{
  // 1. capa verde (0 a 2,7 s): o 13º de novembro segue até janeiro
  const sobe = prog(t, 2.7, 3.15);
  $('capa').style.transform = `translateY(${{-1920*sobe}}px)`;
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,2.7)}})`; $('gancho').style.transformOrigin='0 50%';
  const d = prog(t, 0.45, 1.6);
   arco.style.opacity = d > 0.01 ? 1 : 0;
  arco.style.clipPath = `inset(0 ${{100 - 100*d}}% 0 0)`;
  const s13 = .7 + .3*prog(t, 0.1, 0.5); $('t13').style.transformBox='fill-box'; $('t13').style.transformOrigin='center';
  $('t13').style.transform = `scale(${{s13}})`;
  // 2. papel: títulos
  titulo('t1', t, 2.85, 5.45); titulo('t2', t, 5.6, 8.15); titulo('t3', t, 8.3, 10.95);
  titulo('t4', t, 11.1, 13.7); titulo('t5', t, 13.85, 16.6);
  const ent = prog(t, 2.9, 3.5), sai = prog(t, 16.6, 16.95);
  $('janela').style.opacity = Math.min(ent, 1-sai); $('nota').style.opacity = Math.min(ent, 1-sai);
  $('janela').style.transform = `translateY(${{(1-ent)*70 - sai*40}}px)`;
  $('nota').style.transform = `translateY(${{(1-ent)*70 - sai*40}}px)`;
  // camadas: A (antes) até 8,3 s; B (menu, folha e modal) de 8,3 a 14,15 s; F (depois) a partir de 14,15 s
  const oB = prog(t, 8.3, 8.6), oF = prog(t, 14.15, 14.45);
  $('cA').style.opacity = 1 - oB; $('cB').style.opacity = Math.min(oB, 1 - oF); $('cF').style.opacity = oF;
  // A: saldo, depois a linha do tempo; toque em jan/27 abre o cartão
  cam('cA', 4 + (1080-4)*prog(t, 5.75, 6.55), 0, 2);
  anel('aSaldoA', t, 3.8, 5.3);
  toque('qJan', 'oJan', t, 6.85); $('iA2').style.opacity = prog(t, 7.0, 7.3);
  marca('mImp', 1, t, 7.4, 8.1);
  // B: menu da linha, folha, modal e regra (a câmera acompanha o que muda na tela)
  const zB = 0 + 500*prog(t, 9.15, 9.55) - 70*prog(t, 9.95, 10.3) + 40*prog(t, 10.75, 11.05);
  cam('cB', zB, 0, 2);
  toque('qMenu', 'oMenu', t, 8.95); $('iC').style.opacity = prog(t, 9.1, 9.35);
  toque('qAj', 'oAj', t, 9.8); $('iD').style.opacity = prog(t, 9.95, 10.2);
  toque('qUm', 'oUm', t, 10.6); $('iD2').style.opacity = prog(t, 10.75, 10.95);
  toque('qSel', 'oSel', t, 11.35); $('iE').style.opacity = prog(t, 11.5, 11.7);
  anel('aRegra', t, 11.95, 13.55); marca('mRes', 1, t, 12.35, 13.55);
  toque('qConc', 'oConc', t, 13.95);
  // F: depois do "Concluir"
  cam('cF', 4, 0, 2);
  anel('aSaldoF', t, 14.7, 16.4); anel('aNov', t, 15.3, 16.4);
  // 3. lição
  const li = prog(t, 17.0, 17.4);
  $('licao').style.opacity = li; $('licao').style.transform = `translateY(${{(1-li)*40}}px)`;
  [...$('conta').children].forEach((e,i)=>{{ const p=prog(t, 17.55+i*.22, 17.9+i*.22); e.style.opacity=p; e.style.transform=`translateY(${{(1-p)*20}}px)`; }});
  $('conta').style.opacity = prog(t, 17.35, 17.6); $('lei').style.opacity = prog(t, 18.4, 18.75);
  // 4. fechamento verde sobe
  const f = prog(t, 20.8, 21.25);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

if __name__ == "__main__":
    executar(pagina(CORPO, JS), SAIDA, DUR, CAPA, t_capa=2.5)
