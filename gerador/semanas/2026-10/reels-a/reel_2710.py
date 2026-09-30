# -*- coding: utf-8 -*-
"""Reel de 27/10/2026 · "Vai abrir suas finanças em público?" (capa tinta), 1080 × 1920, 30 fps, 18 s.

Visão geral no celular com e sem "Ocultar valores" (telas movel.png e movel-ocultar.png; o olho fica em
x 311, y 38 px CSS): um toque e os valores somem, outro toque e voltam. Conclusão com a tela real do
"Fluxo mensal": com o olho fechado, o eixo do gráfico também vira "•••" (captura nova, conta fictícia).
python3 reel_2710.py  |  REEL_PREVIA="0 2.2 6" python3 reel_2710.py
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import reelkit as K
A = K.A

PASTA = "2026-10-27_reel-ocultar-valores"
O = os.path.dirname(AQUI)
SAIDA = os.path.join(O, "saida", PASTA)
TELAS = os.path.join(SAIDA, "telas")
def t_(nome): return os.path.join(TELAS, nome)
DUR = 18.0
DARK_TEXTO = "#C9D1C8"

# px CSS nas telas (medidos no site da conta fictícia)
OLHO = (311, 38)
PATRIMONIO = [29, 228, 136, 38]      # "R$ 104.180" (e os pontos, com o olho fechado)
BLOCO = [26, 497, 338, 84]           # "Receitas ... Despesas ..." e "Sobrou no período ..."
EIXO = [24, 268, 56, 200]            # rótulos do eixo do gráfico "Fluxo mensal" (R$ 10 mil, R$ 5 mil, R$ 0)
TOPO_GRAF = 8                        # a captura rolada começa em y 8, como no modelo (esconde o texto que passa atrás do topo)

# tempos (s)
SLIDE = 2.40
A_, B_, C_, D_ = 2.60, 5.20, 8.60, 11.20
TQ1, TQ2, TQ3 = 5.75, 9.55, 12.20    # toques no olho
FIM = 14.60

I_OLHO = '<path d="M2.5 12c1-2.5 4.5-7 9.5-7s8.5 4.5 9.5 7c-1 2.5-4.5 7-9.5 7s-8.5-4.5-9.5-7z"/><circle cx="12" cy="12" r="3"/>'
I_OLHO_OFF = ('<path d="M10.6 5.2A9.9 9.9 0 0 1 12 5c5 0 8.5 4.5 9.5 7-.4 1-1.2 2.3-2.4 3.5M6.4 6.5C4.6 7.8 3.2 9.8 2.5 12c1 2.5 4.5 7 9.5 7 1.8 0 3.4-.6 4.8-1.4"/>'
              '<path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>')

def tela_dupla(tid, a, b, alt, extra=""):
    return K.tela(tid, [(tid + "A", t_(a), 0, 0, 1170, ""), (tid + "B", t_(b), 0, 0, 1170, "opacity:0")], alt, extra)

toques = '<div class="onda" id="onda"></div><div class="toque" id="toque"></div>'
aneis1 = '<div class="anel" id="aPat"></div><div class="anel" id="aBloco"></div><div class="anel" id="aPat2"></div>'
aneis2 = '<div class="anel" id="aEixo"></div><div class="onda" id="onda2"></div><div class="toque" id="toque2"></div>'

CSS = f"""
.tit{{font-size:72px}}
#capa .eyebrow{{color:{A.MENTA}}}
#capa .h1{{font-size:116px;line-height:.96}}
#olhoCapa{{position:absolute;left:370px;top:910px;width:340px;height:340px}}
#olhoCapa svg{{position:absolute;left:0;top:0;overflow:visible}}
#valCapa{{position:absolute;left:90px;top:1310px;width:900px;text-align:center}}
#valCapa .rot{{font-size:34px;font-weight:600;color:{DARK_TEXTO}}}
#valCapa .v{{position:relative;height:160px;margin-top:14px}}
#valCapa .v div{{position:absolute;left:0;right:0;top:0;font-size:136px;font-weight:700;letter-spacing:-.04em;line-height:160px;color:#fff;font-variant-numeric:tabular-nums}}
#valCapa .v .pts{{letter-spacing:.06em}}
.janela .tela{{overflow:hidden}}
"""

CORPO = f"""
<div class="cena" id="papel">
  <div class="tit" id="tA">Na fila, no ônibus, no trabalho?</div>
  <div class="tit" id="tB">Um toque e os valores somem.</div>
  <div class="tit" id="tC">Toque de novo, e eles voltam.</div>
  <div class="tit" id="tD">Os gráficos também escondem.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">
    {tela_dupla("t1", "movel.png", "movel-ocultar.png", 741, aneis1 + toques)}
    {tela_dupla("t2", "celular-dashboard-fluxo-mensal.png", "celular-dashboard-fluxo-mensal-ocultar.png", 1000, aneis2)}
  </div>
</div>

<div class="cena tinta" id="capa">
  <div style="position:absolute;left:90px;top:290px">{A.logo_horizontal("dark", 60)}</div>
  <div style="position:absolute;left:90px;top:420px;width:900px">
    <div class="eyebrow" style="margin-bottom:36px">Privacidade</div>
    <div class="h1" id="gancho" style="text-wrap:wrap">Vai abrir<br>suas finanças<br>em público?</div>
  </div>
  <div id="olhoCapa">
    <svg id="svgAberto" width="340" height="340" viewBox="0 0 24 24" fill="none" stroke="{A.MENTA}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{I_OLHO}</svg>
    <svg id="svgFechado" width="340" height="340" viewBox="0 0 24 24" fill="none" stroke="{A.MENTA}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="opacity:0">{I_OLHO_OFF}
      <path id="corte" d="M3 3l18 18" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>
  </div>
  <div id="valCapa"><div class="rot">Patrimônio</div>
    <div class="v"><div id="vNum">R$ 104.180</div><div id="vPts" class="pts" style="opacity:0">R$ ••••••</div></div></div>
</div>

{K.fim("“Ocultar valores” no timtimcash")}
"""

JS = f"""
const OLHO={list(OLHO)}, SLIDE={SLIDE}, A_={A_}, B_={B_}, C_={C_}, D_={D_}, FIM={FIM};
const TQ1={TQ1}, TQ2={TQ2}, TQ3={TQ3}, TOPO_GRAF={TOPO_GRAF};
caixa($('aPat'), {PATRIMONIO}, 20); caixa($('aPat2'), {PATRIMONIO}, 20); caixa($('aBloco'), {BLOCO}, 18);
caixa($('aEixo'), {EIXO}, 16);
['toque','onda','toque2','onda2'].forEach(i => ponto($(i), OLHO[0], OLHO[1]));
function render(t){{
  // 1. capa (tinta): o olho pisca e fecha, o patrimônio vira pontos; em 2,4 s a capa sobe
  const sobe = prog(t, SLIDE, SLIDE+.45);
  $('capa').style.transform = `translateY(${{-1920*sobe}}px)`;
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,SLIDE)}})`; $('gancho').style.transformOrigin='0 50%';
  const fecha = prog(t, .85, 1.02), abre = prog(t, 1.02, 1.2);
  $('svgAberto').style.opacity = t < 1.02 ? 1 : 0;
  $('svgAberto').style.transform = `scaleY(${{1-.92*fecha}})`;
  $('svgFechado').style.opacity = t < 1.02 ? 0 : 1;
  $('svgFechado').style.transform = `scaleY(${{.08+.92*abre}})`;
  $('corte').setAttribute('stroke-dashoffset', 1-prog(t, 1.1, 1.45));
  const m = prog(t, .95, 1.2);
  $('vNum').style.opacity = 1-m; $('vPts').style.opacity = m;
  $('vNum').style.filter = `blur(${{10*m}}px)`;
  // 2. títulos
  titulo('tA', t, 2.65, B_-.06); titulo('tB', t, B_+.18, C_-.06); titulo('tC', t, C_+.18, D_-.06); titulo('tD', t, D_+.18, 0);
  // 3. janela: entra por baixo como no modelo (fica até o verde cobrir)
  const ent = prog(t, 2.7, 3.3);
  ['janela','nota'].forEach(id => {{ $(id).style.opacity = ent; $(id).style.transform = `translateY(${{(1-ent)*70}}px)`; }});
  // 4. Visão geral: toque, valores somem, rola um pouco, volta ao topo, toque, valores voltam
  toque('toque', 'onda', t, t < (TQ1+TQ2)/2 ? TQ1 : TQ2);
  const oculto1 = prog(t, TQ1+.2, TQ1+.6), volta1 = prog(t, TQ2+.2, TQ2+.6);
  $('t1B').style.opacity = oculto1*(1-volta1);
  const topo1 = 170*prog(t, B_+1.35, B_+2.15) - 170*prog(t, C_+.1, C_+.7);
  // 5. para o gráfico: a tela do Fluxo mensal entra por dissolução (o topo com o olho fica no lugar)
  const rola = prog(t, D_+.05, D_+.55);
  pan('t1', topo1 + TOPO_GRAF*rola);
  $('t1').style.opacity = 1-rola;
  $('t2').style.opacity = rola;
  pan('t2', TOPO_GRAF);
  $('t2').style.visibility = t < D_ ? 'hidden' : 'visible';
  toque('toque2', 'onda2', t, TQ3);
  $('t2B').style.opacity = prog(t, TQ3+.2, TQ3+.6);
  // 6. anéis
  anel('aPat', t, 3.5, B_-.1);
  anel('aBloco', t, B_+2.05, C_-.1);
  anel('aPat2', t, TQ2+.75, D_-.1);
  anel('aEixo', t, TQ3+.8, FIM-.05);
  // 7. fechamento verde
  const f = prog(t, FIM, FIM+.45);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

HTML = K.pagina(CORPO, CSS, JS)

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, capa_t=2.2, trabalho=os.path.join(AQUI, "trabalho", "2710"))
