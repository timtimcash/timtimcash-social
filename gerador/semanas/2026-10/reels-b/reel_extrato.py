# -*- coding: utf-8 -*-
"""Reel de 08/10/2026 · "Seu extrato do banco, já com as categorias." (1080 × 1920, 30 fps).

python3 reel_extrato.py <saida.mp4> [capa.jpg]
Telas reais do celular (390 px CSS de largura, escala 3), capturadas por app/captura_importar.py
na conta fictícia com o relógio da página em 30/09/2026, lidas de $O/saida/<pasta>/telas/.
Capa em papel. Cada quadro é desenhado no Chromium (render(t)) e vai direto para o ffmpeg.
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import reelkit as K
A = K.A

O = os.path.dirname(AQUI)
PASTA = "2026-10-08_reel-extrato-com-categoria-sugerida"
T = os.path.join(O, "saida", PASTA, "telas")
def tela(n): return os.path.join(T, n)

SAIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "extrato", "reel.mp4")
CAPA = sys.argv[2] if len(sys.argv) > 2 else None
DUR = 24.9

# ---------------------------------------------------------------- caixas (px CSS do celular, da captura)
C = {
    "aba_ofx": (195, 1300, 167, 34), "escolher": (247.5, 1647),
    "conta_corrente": (195, 802.5),
    "faixa_ofx": (29, 567, 332, 102),
    "chip1": (157.5, 975, 162.9, 24), "chip2": (157.5, 1182, 174.5, 24), "chip3": (158.5, 1389, 150.2, 24), "toque_chip3": (233.6, 1401),
    "cuidados": (150, 748.5),
    "cartao": (36, 1221, 318, 212), "aplicar": (125.2, 1417.5),
    "importar3": (247.5, 1647),
    "aviso_dup": (40, 483, 298, 34), "auto3": (158.5, 1389, 190, 24),
}

corpo = f"""
<div class="cena" id="papel">
  <div class="tit" id="tA">Sem senha do banco: baixe o extrato <b>.ofx</b> e importe.</div>
  <div class="tit" id="tB">As categorias já chegam <b>sugeridas</b>.</div>
  <div class="tit" id="tC">Mudou uma categoria? O timtimcash pergunta se deve <b>lembrar</b>.</div>
  <div class="tit" id="tD">Confira e <b>importe</b>.</div>
  <div class="tit" id="tE">Importou o mesmo extrato de novo? O que já entrou vem <b>desmarcado</b>.</div>
  <div class="tit" id="tF">E a farmácia já chega na categoria que você <b>escolheu</b>.</div>
  <div class="nota" id="nota" style="opacity:0">Tela real do timtimcash, com dados de exemplo</div>
  <div id="janela" style="opacity:0">
    {K.camada_html("LA", tela("celular-importar-1-extrato-ofx.jpg"), aneis=[("aAba", None)], toques=[("tqA", None)])}
    {K.camada_html("LB", tela("celular-importar-2-conta-de-destino.jpg"), toques=[("tqB", None)])}
    {K.camada_html("LC", tela("celular-importar-3-revisar-importacao.jpg"), aneis=[("aFaixa", None), ("aC1", None), ("aC2", None), ("aC3", None)], toques=[("tqC", None)])}
    {K.camada_html("LD", tela("celular-importar-4-trocar-categoria.jpg"), toques=[("tqD", None)])}
    {K.camada_html("LE", tela("celular-importar-5-automatizar-esta-categoria.jpg"), aneis=[("aCartao", None)], toques=[("tqE", None)])}
    {K.camada_html("LF", tela("celular-importar-6-regra-salva.jpg"), toques=[("tqF", None)])}
    {K.camada_html("LI", tela("celular-importar-7-mesmo-extrato-de-novo.jpg"), aneis=[("aDup", A.AMBER_BAR), ("aAuto", None)])}
  </div>
</div>

<div class="cena" id="licao" style="opacity:0">
  <div style="position:absolute;left:90px;top:560px;width:900px">
    <div class="h1" style="font-size:112px">Categorize uma vez, o timtimcash aprende.</div>
    <div class="apoio" style="margin-top:44px;font-size:44px;text-wrap:balance">Transações já importadas são detectadas e desmarcadas.</div>
    <div id="chips" style="display:flex;flex-wrap:wrap;gap:22px;margin-top:70px">
      <span class="chip">Sem senha do banco</span><span class="chip">Você revisa antes de importar</span>
    </div>
  </div>
</div>

<div class="cena" id="capa">
  <div id="capaLogo" style="position:absolute;left:90px;top:290px">{A.logo_horizontal("color", 60)}</div>
  <div id="capaTexto" style="position:absolute;left:90px;top:420px;width:900px">
    <div class="eyebrow" style="color:{A.BRAND_DARK};margin-bottom:38px">Importar extrato</div>
    <div class="h1" id="gancho" style="font-size:112px">Seu extrato do banco, já com as categorias.</div>
  </div>
  <div id="capaVisual" style="position:absolute;left:0;top:870px;width:1080px;display:flex;flex-direction:column;align-items:center">
    <div class="recorte" id="capaRecorte" style="width:700px"><img src="file://{tela('computador-importar-categorias-sugeridas.jpg')}"></div>
    <div style="margin-top:26px;font-size:26px;font-weight:500;color:{A.MUTED}">Tela real do timtimcash, com dados de exemplo</div>
  </div>
</div>

{K.fechamento("Importar extrato no timtimcash")}
"""

js = f"""
const C = {{ {", ".join(f'{k}:{list(v)}' for k, v in C.items())} }};
poeAnel('aAba', C.aba_ofx, 16); poeToque('tqA', ...C.escolher);
poeToque('tqB', ...C.conta_corrente);
poeAnel('aFaixa', C.faixa_ofx, 12); poeAnel('aC1', C.chip1, 14); poeAnel('aC2', C.chip2, 14); poeAnel('aC3', C.chip3, 14); poeToque('tqC', ...C.toque_chip3);
poeToque('tqD', ...C.cuidados);
poeAnel('aCartao', C.cartao, 8); poeToque('tqE', ...C.aplicar);
poeToque('tqF', ...C.importar3);
poeAnel('aDup', C.aviso_dup, 12); poeAnel('aAuto', C.auto3, 14);

function render(t){{
  // 1. capa em papel (0 a 2,6 s): tudo legível desde o quadro 0; sai subindo
  const sai = prog(t, 2.55, 2.95);
  ['capaLogo','capaTexto','capaVisual'].forEach((id,i)=>{{ const e=$(id); e.style.opacity = 1-sai; e.style.transform = `translateY(${{-90*sai - i*20*sai}}px)`; }});
  $('capa').style.visibility = t < 3.0 ? 'visible' : 'hidden';
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,2.6)}})`; $('gancho').style.transformOrigin='0 50%';
  $('capaRecorte').style.transform = `scale(${{1+0.025*lin(t,0,2.6)}})`;

  // 2. títulos das cenas
  titulo('tA', t, 2.8, 5.1); titulo('tB', t, 5.4, 8.35); titulo('tC', t, 8.65, 12.85);
  titulo('tD', t, 13.15, 14.45); titulo('tE', t, 14.75, 16.7); titulo('tF', t, 17.0, 18.7);

  // janela e nota entram com a primeira tela e saem antes da lição
  const ent = prog(t, 2.85, 3.4), fora = prog(t, 18.7, 19.05);
  $('janela').style.opacity = Math.min(ent, 1-fora); $('nota').style.opacity = Math.min(ent, 1-fora);
  $('janela').style.transform = `translateY(${{(1-ent)*70 - fora*40}}px)`;
  $('nota').style.transform = `translateY(${{(1-ent)*70 - fora*40}}px)`;

  // A · Importar transações, aba do extrato .ofx; toque em "Escolher arquivo"
  const aOut = prog(t, 4.5, 4.75);
  camada('LA', 1-aOut, 1179);
  anel('aAba', t, 3.35, 3.95); toque('tqA', t, 4.05);
  // B · Conta de destino; toque em "Conta corrente"
  const bIn = prog(t, 4.5, 4.75), bOut = prog(t, 5.45, 5.7);
  camada('LB', Math.min(bIn, 1-bOut), 600);
  toque('tqB', t, 5.0);
  // C · Revisar importação: faixa do extrato, depois as 3 categorias sugeridas; toque na da farmácia
  const cIn = prog(t, 5.45, 5.7), cOut = prog(t, 9.15, 9.4);
  const topoC = 470 + (1003-470)*prog(t, 6.5, 8.3);
  camada('LC', Math.min(cIn, 1-cOut), topoC);
  anel('aFaixa', t, 5.95, 6.55); anel('aC1', t, 7.0, 8.0); anel('aC2', t, 7.4, 8.5); anel('aC3', t, 7.8, 8.75);
  toque('tqC', t, 8.95);
  // D · lista de categorias sobe; toque em "Cuidados pessoais"
  const dIn = prog(t, 9.15, 9.5), dOut = prog(t, 10.45, 10.7);
  camada('LD', Math.min(dIn, 1-dOut), 328, (1-dIn)*420);
  toque('tqD', t, 10.0);
  // E · "Automatizar esta categoria?"; toque em "Aplicar e lembrar"
  const eIn = prog(t, 10.45, 10.7), eOut = prog(t, 12.5, 12.72);
  const topoE = 945 - 29*prog(t, 12.5, 12.72);
  camada('LE', Math.min(eIn, 1-eOut), topoE);
  anel('aCartao', t, 10.9, 12.05); toque('tqE', t, 12.2);
  // F · "Regra salva para as próximas importações"; toque em "Importar 3 linhas"
  const fIn = prog(t, 12.5, 12.72), fOut = prog(t, 14.35, 14.75);
  camada('LF', Math.min(fIn, 1-fOut), topoE + 262);
  $('LF').style.transform += ` translateX(${{-780*fOut}}px)`;
  toque('tqF', t, 13.85);
  // I · o mesmo extrato de novo: desmarcadas e a regra já aplicada
  const iIn = prog(t, 14.35, 14.75);
  camada('LI', iIn, 290 + (1003-290)*prog(t, 16.95, 17.6));
  $('LI').style.transform += ` translateX(${{780*(1-iIn)}}px)`;
  anel('aDup', t, 15.2, 16.75); anel('aAuto', t, 17.7, 18.6);

  // 3. lição
  const li = prog(t, 18.95, 19.4);
  $('licao').style.opacity = li; $('licao').style.transform = `translateY(${{(1-li)*40}}px)`;
  [...$('chips').children].forEach((c,i)=>{{ const p=prog(t, 19.7+i*.18, 20.05+i*.18); c.style.opacity=p; c.style.transform=`translateY(${{(1-p)*24}}px)`; }});
  // 4. fechamento verde sobe
  const f = prog(t, 21.55, 22.0);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

if __name__ == "__main__":
    K.rodar(K.html(corpo, js), SAIDA, DUR, CAPA, t_capa=2.2)
