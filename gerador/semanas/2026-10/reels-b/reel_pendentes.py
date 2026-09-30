# -*- coding: utf-8 -*-
"""Reel de 20/10/2026 · "O que vence esta semana?" (1080 × 1920, 30 fps).

python3 reel_pendentes.py <saida.mp4> [capa.jpg]
Tela Pendentes no celular (390 × 1000 px CSS, escala 3), capturada por app/captura_pendentes.py na
conta fictícia com o relógio da página em 05/10/2026 (segunda-feira), 9h, horário de Brasília:
a conta de luz de R$ 186,40 (vence 30/09) já passou da data e o reembolso de R$ 320,00 (06/10)
chega amanhã. Antes e depois de um toque em "pendente" na conta de luz. Capa em tinta.
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import reelkit as K
A = K.A

O = os.path.dirname(AQUI)
PASTA = "2026-10-20_reel-o-que-vence-esta-semana"
T = os.path.join(O, "saida", PASTA, "telas")
def tela(n): return os.path.join(T, n)

SAIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "pendentes", "reel.mp4")
CAPA = sys.argv[2] if len(sys.argv) > 2 else None
DUR = 22.8
DARK_TEXTO = "#C9D1C8"

# caixas em px CSS do celular (app/pendentes/caixas.json)
C = {
    "kpis": (15, 139, 360, 201),
    "luz": (15, 475.5, 360, 100), "pill_luz": (320.5, 546.6),
    "nada": (18, 359, 354, 40),
    "reembolso": (15, 485.5, 360, 100),
}

corpo = f"""
<div class="cena" id="papel">
  <div class="tit" id="tA">Em Pendentes, tudo o que falta <b>pagar e receber</b>.</div>
  <div class="tit" id="tB">O que já venceu aparece <b>primeiro</b>.</div>
  <div class="tit" id="tC">Pagou? Um toque em <b>“pendente”</b>.</div>
  <div class="tit" id="tD">Pronto: <b>nada vencido</b>.</div>
  <div class="tit" id="tE">E ainda há <b>R$ 320,00</b> a receber amanhã.</div>
  <div class="nota" id="nota" style="opacity:0">Tela real do timtimcash, com dados de exemplo</div>
  <div id="janela" style="opacity:0">
    {K.camada_html("P1", tela("celular-pendentes-antes.jpg"), aneis=[("aKpi", None), ("aLuz", A.RED)], toques=[("tqLuz", A.AMBER_BAR)])}
    {K.camada_html("P2", tela("celular-pendentes-depois.jpg"), aneis=[("aNada", None), ("aReemb", None)])}
  </div>
</div>

<div class="cena" id="licao" style="opacity:0">
  <div style="position:absolute;left:90px;top:560px;width:900px">
    <div class="h1" style="font-size:112px">O mês só fecha quando nada fica para trás.</div>
    <div class="apoio" style="margin-top:44px;font-size:44px;text-wrap:balance">Contas a pagar e a receber num lugar só, com o que venceu primeiro.</div>
    <div id="chips" style="display:flex;flex-wrap:wrap;gap:22px;margin-top:70px">
      <span class="chip">Vencidas</span><span class="chip">A pagar</span><span class="chip">A receber</span><span class="chip">Total pendente</span>
    </div>
  </div>
</div>

<div class="cena" id="capa" style="background:{A.INK};color:#fff">
  <div style="position:absolute;left:90px;top:290px">{A.logo_horizontal("dark", 60)}</div>
  <div style="position:absolute;left:90px;top:500px;width:900px">
    <div class="eyebrow" style="color:{A.MENTA};margin-bottom:40px">Pendentes</div>
    <div class="h1" id="gancho">O que vence esta semana?</div>
  </div>
  <div style="position:absolute;left:0;top:930px;width:1080px;display:flex;flex-direction:column;align-items:center">
    <div id="capaRecorte" style="width:820px;border-radius:34px;overflow:hidden;box-shadow:0 30px 70px -30px rgba(0,0,0,.6)">
      <img src="file://{tela('celular-pendentes-indicadores.jpg')}" style="display:block;width:100%;height:auto"></div>
    <div style="margin-top:30px;font-size:26px;font-weight:500;color:{DARK_TEXTO}">Tela real do timtimcash, com dados de exemplo</div>
  </div>
</div>

{K.fechamento("Pendentes no timtimcash")}
"""

js = f"""
const C = {{ {", ".join(f'{k}:{list(v)}' for k, v in C.items())} }};
poeAnel('aKpi', C.kpis, 8); poeAnel('aLuz', C.luz, 9); poeToque('tqLuz', ...C.pill_luz);
poeAnel('aNada', C.nada, 8); poeAnel('aReemb', C.reembolso, 9);

function render(t){{
  // 1. capa em tinta (0 a 2,6 s), legível desde o quadro 0; sobe e revela o papel
  const sobe = prog(t, 2.6, 3.05);
  $('capa').style.transform = `translateY(${{-1920*sobe}}px)`;
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,2.6)}})`; $('gancho').style.transformOrigin='0 50%';
  $('capaRecorte').style.transform = `scale(${{1+0.025*lin(t,0,2.6)}})`;

  // 2. títulos
  titulo('tA', t, 2.6, 5.75); titulo('tB', t, 6.05, 8.55); titulo('tC', t, 8.85, 10.75);
  titulo('tD', t, 11.05, 13.2); titulo('tE', t, 13.5, 16.15);

  const ent = prog(t, 2.6, 3.15), fora = prog(t, 16.15, 16.5);
  $('janela').style.opacity = Math.min(ent, 1-fora); $('nota').style.opacity = Math.min(ent, 1-fora);
  $('janela').style.transform = `translateY(${{(1-ent)*70 - fora*40}}px)`;
  $('nota').style.transform = `translateY(${{(1-ent)*70 - fora*40}}px)`;

  // antes: indicadores, depois a conta de luz vencida; toque em "pendente"
  const topo1 = 6 + (300-6)*prog(t, 6.1, 6.7);
  const troca = prog(t, 9.45, 9.7);
  camada('P1', 1-troca, topo1);
  anel('aKpi', t, 3.55, 5.7); anel('aLuz', t, 6.85, 8.75); toque('tqLuz', t, 9.2);
  // depois: nada vencido e o reembolso de amanhã
  const topo2 = 300 - 180*prog(t, 9.95, 10.55);
  camada('P2', troca, topo2);
  anel('aNada', t, 11.3, 13.25); anel('aReemb', t, 13.85, 16.05);

  // 3. lição
  const li = prog(t, 16.45, 16.9);
  $('licao').style.opacity = li; $('licao').style.transform = `translateY(${{(1-li)*40}}px)`;
  [...$('chips').children].forEach((c,i)=>{{ const p=prog(t, 17.2+i*.15, 17.55+i*.15); c.style.opacity=p; c.style.transform=`translateY(${{(1-p)*24}}px)`; }});
  // 4. fechamento verde sobe
  const f = prog(t, 19.55, 20.0);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

if __name__ == "__main__":
    K.rodar(K.html(corpo, js), SAIDA, DUR, CAPA, t_capa=2.2)
