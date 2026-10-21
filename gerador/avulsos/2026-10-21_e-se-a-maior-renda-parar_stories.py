# -*- coding: utf-8 -*-
"""Stories animado de 21/10/2026 (aprovado pelo dono e publicado pelo Metricool no mesmo dia) · "E se a maior renda parasse por 6 meses?" · leva ao carrossel do dia (publicado às 10h).

1080 x 1920, 30 fps, 14 s, sem som (faixa AAC muda, como nos Reels). Zona segura dos Stories: nada importante acima de
280 px (nome do perfil e barra de progresso) nem abaixo de 1600 px (campo de resposta).
Números: os mesmos do carrossel publicado (gerador/telas/LEIAME.md): no cenário base, o saldo de set/27 é R$ 37.720; com o
teste "Perde a maior renda" (a maior receita zera nos 6 primeiros meses), cai R$ 59.760 e termina em −R$ 22.040.
A curva da cena 1 é ilustração (sem eixos nem moldura do site), com a mesma conta: 13 meses, receita de R$ 9.960, despesa de
R$ 7.780, IPVA e IPTU de R$ 4.800 em janeiro; no susto, sem receita nos 6 primeiros meses.
A cena 2 é a tela real (gerador/telas/secoes/celular-simulacao-e-se-perde-a-maior-renda.jpg, build 2026-09-30.1).

python3 gerador/avulsos/2026-10-21_e-se-a-maior-renda-parar_stories.py   vídeo em $TT_SAIDA/<PASTA>/story.mp4 (padrão /tmp/tt_stories)
REEL_PREVIA="0.4 1 2.4 3.6 5.2 7 8.4 11 13.5" (o mesmo comando)   quadros soltos em $TT_SAIDA/trabalho/previa/
"""
import os, sys, shutil
from decimal import Decimal as D
sys.path.insert(0, "/home/claude/timtimcash-social/gerador/semanas/2026-11/kit")
import reelkit as K
A = K.A

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = "2026-10-21_e-se-a-maior-renda-parar_stories"
BASE = os.environ.get("TT_SAIDA", "/tmp/tt_stories")          # fora do repositório; o aprovado vai para posts/<PASTA>/
SAIDA = os.path.join(BASE, PASTA)
TRAB = os.path.join(BASE, "trabalho")
TELA = "/home/claude/timtimcash-social/gerador/telas/secoes/celular-simulacao-e-se-perde-a-maior-renda.jpg"
DUR = 14.0

# ---------------------------------------------------------------- a conta da ilustração (fecha com a tela real)
INICIO, REC, DESP, JAN = D("14180"), D("9960"), D("7780"), D("4800")
base, susto = [INICIO], [INICIO]
for k in range(1, 14):                         # 13 meses, de hoje (30/09/2026) a set/27; janeiro é k = 4
    extra = JAN if k == 4 else D(0)
    base.append(base[-1] + REC - DESP - extra)
    susto.append(susto[-1] + (REC if k > 6 else D(0)) - DESP - extra)
assert base[-1] == D("37720") and susto[-1] == D("-22040") and base[-1] - susto[-1] == D("59760")

# ilustração: 900 x 470 px; de −40 mil a +40 mil
W, H, X0, X1 = 900, 470, 20, 640
def px(k, v):
    return X0 + k * (X1 - X0) / 13, H / 2 - float(v) / 40000 * (H / 2 - 18)
pb = " ".join(f"{'M' if k == 0 else 'L'}{px(k, v)[0]:.1f},{px(k, v)[1]:.1f}" for k, v in enumerate(base))
ps = " ".join(f"{'M' if k == 0 else 'L'}{px(k, v)[0]:.1f},{px(k, v)[1]:.1f}" for k, v in enumerate(susto))
fb, fs = px(13, base[-1]), px(13, susto[-1])

# ---------------------------------------------------------------- tela real: caixas medidas na imagem (1086 px de largura)
ESC = 780 / 1086
CHIP = (45, 1488, 533, 1589)       # "Perde a maior renda", fundo âmbar
MSG = (45, 1747, 1040, 1892)       # "O saldo final cai R$ 59.760 (158%), de R$ 37.720 para −R$ 22.040."
PAN = 480                          # px da janela: os dois ficam à vista e o fim do gráfico continua no alto
def caixa(r, pad=12):
    x0, y0, x1, y1 = (v * ESC for v in r)
    return [round(x0 - pad), round(y0 - PAN - pad), round(x1 - x0 + 2 * pad), round(y1 - y0 + 2 * pad)]

CSS = f"""
#c1,#c2{{position:absolute;left:0;top:0;width:1080px;height:1920px;background:{A.BG}}}
#eye{{position:absolute;left:90px;top:300px;opacity:0}}
#q{{position:absolute;left:90px;top:352px;width:900px;font-size:112px;line-height:.98;font-weight:700;letter-spacing:-.05em;text-wrap:balance;opacity:0}}
#rot{{position:absolute;left:90px;top:722px;font-size:36px;font-weight:600;color:{A.MUTED};letter-spacing:-.01em;opacity:0}}
#saldo{{position:absolute;left:86px;top:770px;font-size:118px;font-weight:700;letter-spacing:-.05em;color:{A.BRAND_DARK};opacity:0}}
#graf{{position:absolute;left:90px;top:942px;width:{W}px;height:{H}px;opacity:0}}
#leg{{position:absolute;left:90px;top:1428px;display:flex;gap:44px;font-size:32px;font-weight:600;color:{A.MUTED};opacity:0}}
#leg span{{display:inline-flex;align-items:center;gap:16px}}
#cai{{position:absolute;left:90px;top:1494px;opacity:0;transform-origin:0 50%}}
#cai .pill{{background:{A.RED};color:#fff;font-size:46px;padding:24px 44px}}
.lbl{{position:absolute;font-size:44px;font-weight:700;letter-spacing:-.03em;white-space:nowrap;opacity:0}}
#t1,#t2{{width:900px}}
"""

CORPO = f"""
<div class="cena papel" id="c1">
  <div class="eyebrow" id="eye">Simulação futura</div>
  <div id="q">E se a maior renda parasse por 6 meses?</div>
  <div id="rot">Saldo em set/27, no exemplo</div>
  <div class="num" id="saldo">R$ 37.720</div>
  <div id="graf">
    <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0;overflow:visible">
      <defs>
        <clipPath id="cb"><rect id="rb" x="0" y="-40" width="0" height="{H + 80}"/></clipPath>
        <clipPath id="cs"><rect id="rs" x="0" y="-40" width="0" height="{H + 80}"/></clipPath>
      </defs>
      <line x1="0" y1="{H / 2}" x2="{X1 + 12}" y2="{H / 2}" stroke="#DDD9CE" stroke-width="4"/>
      <text x="{X1 + 30}" y="{H / 2 + 11}" font-family="Inter" font-weight="600" font-size="32" fill="{A.MUTED}">R$ 0</text>
      <g clip-path="url(#cs)">
        <path d="{ps}" fill="none" stroke="{A.RED}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="26 20"/>
        <circle cx="{fs[0]:.1f}" cy="{fs[1]:.1f}" r="15" fill="{A.RED}"/>
      </g>
      <g clip-path="url(#cb)">
        <path d="{pb}" fill="none" stroke="{A.BRAND}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="{fb[0]:.1f}" cy="{fb[1]:.1f}" r="16" fill="{A.BRAND}"/>
      </g>
    </svg>
    <div class="lbl" id="lb" style="left:{fb[0] + 32:.0f}px;top:{fb[1] - 28:.0f}px;color:{A.BRAND_DARK}">R$ 37.720</div>
  </div>
  <div id="leg">
    <span><svg width="64" height="12"><line x1="4" y1="6" x2="60" y2="6" stroke="{A.BRAND}" stroke-width="10" stroke-linecap="round"/></svg>cenário atual</span>
    <span><svg width="64" height="12"><line x1="5" y1="6" x2="60" y2="6" stroke="{A.RED}" stroke-width="9" stroke-linecap="round" stroke-dasharray="18 14"/></svg>com o susto</span>
  </div>
  <div id="cai"><span class="pill">O saldo cai R$ 59.760</span></div>
</div>

<div class="cena papel" id="c2" style="opacity:0">
  <div class="tit" id="t1">Um toque aplica o susto. <b>Sem alterar nada.</b></div>
  <div class="tit" id="t2">No exemplo, o saldo final cai <b>R$ 59.760.</b></div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="jan">
    <div class="tela" id="tl"><img src="file://{TELA}"></div>
    <div class="anel" id="a1"></div>
    <div class="anel coral" id="a2"></div>
  </div>
</div>

<div class="cena verde" id="fim" style="transform:translateY(1920px)">
  <div style="position:absolute;left:0;top:420px;width:1080px;display:flex;flex-direction:column;align-items:center;text-align:center">
    {A.logo_vertical("white", 300)}
    <div style="font-size:70px;font-weight:700;letter-spacing:-.045em;line-height:1.05;margin-top:90px;width:880px;text-wrap:balance">Descubra quanto tempo o seu plano aguenta.</div>
    <div style="font-size:40px;font-weight:500;letter-spacing:-.02em;line-height:1.3;margin-top:30px;width:840px;text-wrap:balance">Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.</div>
    <div style="margin-top:64px"><span class="pill">Post novo no perfil</span></div>
    <div style="margin-top:34px;font-size:38px;font-weight:600;letter-spacing:-.01em">@timtimcashcom</div>
  </div>
</div>
"""

A1, A2 = caixa(CHIP), caixa(MSG)
JS_RENDER = f"""
const A1 = {A1}, A2 = {A2};
function poe(id, r){{ const e=$(id); e.style.left=r[0]+'px'; e.style.top=r[1]+'px'; e.style.width=r[2]+'px'; e.style.height=r[3]+'px'; }}
poe('a1', A1); poe('a2', A2);
function render(t){{
  // cena 1: a pergunta e o número já no primeiro segundo
  const s1 = 1 - prog(t, 4.6, 5.0);
  $('c1').style.opacity = s1; $('c1').style.transform = `translateY(${{-60 * prog(t, 4.6, 5.0)}}px)`;
  aparece('eye', t, 0, 0, 20, .3); aparece('q', t, 0.05, 0, 34, .4);
  aparece('rot', t, 0.35, 0, 20, .35); aparece('saldo', t, 0.35, 0, 24, .35);
  aparece('graf', t, 0.3, 0, 30, .35);
  $('rb').setAttribute('width', {W + 40} * prog(t, 0.45, 1.65));
  aparece('lb', t, 1.5, 0, 12, .3);
  $('rs').setAttribute('width', {W + 40} * prog(t, 2.0, 3.4));
  aparece('leg', t, 1.0, 0, 16, .35);
  // o saldo cai junto com a linha do susto: de R$ 37.720 a −R$ 22.040
  const v = 37720 + (-22040 - 37720) * prog(t, 2.0, 3.4);
  $('saldo').textContent = (v < 0 ? '−' : '') + 'R$ ' + fmt(Math.abs(v), 0);
  $('saldo').style.color = v < 0 ? '{K.CORAL_FORTE}' : '{A.BRAND_DARK}';
  salta('cai', t, 3.45, .45);
  // cena 2: a tela real
  $('c2').style.opacity = prog(t, 4.6, 4.9);
  titulo('t1', t, 4.75, 7.35); titulo('t2', t, 7.55, 0);
  aparece('nota', t, 4.9, 0, 0, .3);
  janela('jan', t, 4.7, 0);
  $('tl').style.transform = `translateY(${{-{PAN} * prog(t, 5.7, 6.7)}}px)`;
  anel('a1', t, 6.75, 7.75); anel('a2', t, 7.85, 0);
  // fechamento
  sobe('fim', t, 9.75);
}}
"""

HTML = K.pagina(CORPO, CSS, JS_RENDER)

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB)
    if not os.environ.get("REEL_PREVIA"):
        shutil.move(os.path.join(SAIDA, "reel.mp4"), os.path.join(SAIDA, "story.mp4"))
        print("story:", os.path.join(SAIDA, "story.mp4"))
