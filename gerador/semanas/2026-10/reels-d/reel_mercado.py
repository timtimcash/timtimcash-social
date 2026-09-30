# -*- coding: utf-8 -*-
"""Reel de 16/10/2026 · Dia Mundial da Alimentação: quanto do seu mês vai para o mercado? (1080 × 1920, 30 fps).

python3 reel_mercado.py <saida.mp4> [capa.jpg]
Telas reais (conta fictícia, setembro de 2026): "Despesas por categoria" de Relatórios e
"Progresso por categoria" de Orçamentos, no celular (cartões de 362 px CSS, escala 3). Capa verde.
Mercado: R$ 1.710,00, 22% das despesas de R$ 7.780,00; orçamento de R$ 2.000 (86%).
"""
import os, sys
O = "/tmp/claude-0/-home-claude-timtimcash-social/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/outubro"
sys.path.insert(0, os.path.join(O, "reels-b"))
import reelkit as K
A = K.A

DESP = os.path.join(O, "saida/2026-10-06_reel-o-timtimcash-em-20-segundos/telas/celular-relatorios-despesas-por-categoria.jpg")
ORC = "/home/claude/timtimcash-social/gerador/telas/secoes/celular-orcamentos-progresso.jpg"
SAIDA = sys.argv[1]
CAPA = sys.argv[2] if len(sys.argv) > 2 else None
DUR = 21.0
# os cartões têm 362 px CSS; na janela de 780 px, 1 px CSS = 2,155 px. O kit usa E = 2, então converto.
F = (780 / 362) / 2
def cx(r): return [round(v * F, 2) for v in r]

C = {
    "mercado": cx((15, 436, 332, 55)), "valor": cx((228, 440, 96, 46)), "centro": cx((118, 192, 124, 68)),
    "orc_mercado": cx((12, 430, 338, 98)),
}

r, sw = 170, 44
circ = 2 * 3.14159265 * r
arco = circ * 0.22
anel_capa = f"""<svg width="440" height="440" viewBox="0 0 440 440">
  <circle cx="220" cy="220" r="{r}" fill="none" stroke="{A.BRAND_DARK}" stroke-width="{sw}"/>
  <circle id="arcoCapa" cx="220" cy="220" r="{r}" fill="none" stroke="#fff" stroke-width="{sw}" stroke-linecap="round"
    stroke-dasharray="{arco:.1f} {circ:.1f}" transform="rotate(-90 220 220)"/>
  <text x="220" y="238" text-anchor="middle" font-family="Inter" font-weight="700" font-size="112" letter-spacing="-5" fill="#fff">22%</text>
  <text x="220" y="296" text-anchor="middle" font-family="Inter" font-weight="600" font-size="30" fill="{A.MENTA_CLARA}">no mercado</text>
</svg>"""

corpo = f"""
<div class="cena" id="papel">
  <div class="tit" id="tA">No exemplo, o mercado levou <b>R$ 1.710</b> em setembro.</div>
  <div class="tit" id="tB">É <b>22%</b> de tudo o que saiu no mês: R$ 7.780.</div>
  <div class="tit" id="tC">Com limite de <b>R$ 2.000</b>, o mercado fechou em 86%.</div>
  <div class="nota" id="nota" style="opacity:0">Tela real do timtimcash, com dados de exemplo</div>
  <div id="janela" style="opacity:0">
    {K.camada_html("D", DESP, aneis=[("aMerc", None), ("aValor", None), ("aCentro", None)])}
    {K.camada_html("R", ORC, aneis=[("aOrc", None)])}
  </div>
</div>

<div class="cena" id="licao" style="opacity:0">
  <div style="position:absolute;left:90px;top:560px;width:900px">
    <div class="h1" style="font-size:112px">Olhe o mercado em porcentagem do mês.</div>
    <div class="apoio" style="margin-top:44px;font-size:44px;text-wrap:balance">Com um limite em Orçamentos, você vê no meio do mês onde o gasto vai fechar no ritmo atual.</div>
    <div id="chips" style="display:flex;flex-wrap:wrap;gap:22px;margin-top:70px">
      <span class="chip">Despesas por categoria</span><span class="chip">Progresso por categoria</span>
    </div>
  </div>
</div>

<div class="cena verde" id="capa">
  <div style="position:absolute;left:90px;top:290px">{A.logo_horizontal("white", 60)}</div>
  <div style="position:absolute;left:90px;top:470px;width:900px">
    <div class="eyebrow" style="margin-bottom:40px">16/10 · Dia Mundial da Alimentação</div>
    <div class="h1" id="gancho" style="font-size:116px">Quanto do seu mês vai para o mercado?</div>
  </div>
  <div id="capaAnel" style="position:absolute;left:320px;top:1040px">{anel_capa}</div>
  <div style="position:absolute;left:0;top:1500px;width:1080px;text-align:center;font-size:28px;font-weight:600;color:{A.MENTA_CLARA}">na conta de exemplo, em setembro</div>
</div>

{K.fechamento("Relatórios e Orçamentos no timtimcash")}
"""

js = f"""
const C = {{ {", ".join(f'{k}:{v}' for k, v in C.items())} }};
poeAnel('aMerc', C.mercado, 9); poeAnel('aValor', C.valor, 8); poeAnel('aCentro', C.centro, 10);
poeAnel('aOrc', C.orc_mercado, 9);
const ARCO = {arco:.1f}, CIRC = {circ:.1f};
function render(t){{
  // 1. capa verde (0 a 2,6 s): o arco de 22% se desenha; sobe e revela o papel
  const sobe = prog(t, 2.6, 3.05);
  $('capa').style.transform = `translateY(${{-1920*sobe}}px)`;
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,2.6)}})`; $('gancho').style.transformOrigin='0 50%';
  const d = 0.35 + 0.65*prog(t, 0.1, 1.4);
  $('arcoCapa').setAttribute('stroke-dasharray', `${{(ARCO*d).toFixed(1)}} ${{CIRC}}`);
  // 2. títulos
  titulo('tA', t, 2.6, 6.55); titulo('tB', t, 6.85, 10.35); titulo('tC', t, 10.65, 14.6);
  const ent = prog(t, 2.6, 3.15), fora = prog(t, 14.6, 14.95);
  $('janela').style.opacity = Math.min(ent, 1-fora); $('nota').style.opacity = Math.min(ent, 1-fora);
  $('janela').style.transform = `translateY(${{(1-ent)*70 - fora*40}}px)`;
  $('nota').style.transform = `translateY(${{(1-ent)*70 - fora*40}}px)`;
  // Despesas por categoria: do gráfico à linha do Mercado
  const troca = prog(t, 10.4, 10.8);
  const topoD = (30 + 26*prog(t, 3.2, 4.2)) * {F:.4f};
  camada('D', 1-troca, topoD);
  anel('aMerc', t, 3.6, 6.4); anel('aCentro', t, 7.1, 8.6); anel('aValor', t, 8.8, 10.3);
  // Orçamentos: a linha do Mercado
  const topoR = (228 + 30*prog(t, 10.6, 11.4)) * {F:.4f};
  camada('R', troca, topoR);
  anel('aOrc', t, 11.5, 14.45);
  // 3. lição
  const li = prog(t, 14.9, 15.35);
  $('licao').style.opacity = li; $('licao').style.transform = `translateY(${{(1-li)*40}}px)`;
  [...$('chips').children].forEach((c,i)=>{{ const p=prog(t, 15.7+i*.18, 16.05+i*.18); c.style.opacity=p; c.style.transform=`translateY(${{(1-p)*24}}px)`; }});
  // 4. fechamento verde
  const f = prog(t, 17.9, 18.35);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

if __name__ == "__main__":
    K.rodar(K.html(corpo, js), SAIDA, DUR, CAPA, t_capa=1.8)
