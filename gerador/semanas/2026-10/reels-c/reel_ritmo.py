# -*- coding: utf-8 -*-
"""Reel 22/10/2026 · "Rendeu 11,8%. Em quanto tempo?" (1080 × 1920, 30 fps).

python3 reel_ritmo.py <saida.mp4> [capa.jpg]
Telas: capturas/ritmo/ (periodo, ano, mes, como), capturadas por app/captura_ritmo.py no celular
(390 × 1000 em escala 3, conta fictícia, relógio da página em 30/09/2026), com um toque real em
"ao ano", em "ao mês" e em "Como o retorno é calculado".
"""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from reelkit import A, NOTA, pagina, fechamento, executar

TELAS = os.path.join(AQUI, "capturas", "ritmo")
CX = json.load(open(os.path.join(TELAS, "caixas.json"), encoding="utf-8"))
SAIDA = os.path.abspath(sys.argv[1]); CAPA = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else None
DUR = 23.8

def r(b):  # caixa em px CSS [x, y, w, h]
    return [round(b["x"], 1), round(b["y"], 1), round(b["w"], 1), round(b["h"], 1)]
PAR = r(CX["periodo"]["par"])                    # 11,8% na moeda · 25,1% em reais (com o ganho no total)
PER = r(CX["periodo"]["trecho_periodo"])         # De 12/07/2023 a 30/09/2026 (3,2 anos)
PER_L = [r(l) for l in CX["periodo"]["trecho_periodo"]["linhas"]]
SEG_ANO = CX["periodo"]["segs"][1]; SEG_MES = CX["ano"]["segs"][2]
SUM = CX["como_summary"]
FRASE = r(CX["como"]["como"]["frase1"])          # Cada remessa entra na conta na data em que ...
FRASE_L = [r(l) for l in CX["como"]["como"]["frase1"]["linhas"]]
centro = lambda b: [round(b["x"] + b["w"] / 2, 1), round(b["y"] + b["h"] / 2, 1)]
T_ANO, T_MES, T_COMO = centro(SEG_ANO), centro(SEG_MES), [round(SUM["x"] + 70, 1), round(SUM["y"] + SUM["h"] / 2, 1)]

# ---------------------------------------------------------------- capa (verde suave)
# Linha do tempo real das remessas da conta fictícia: 12/07/2023, 14/03/2024 e 18/04/2024, avaliada em 30/09/2026.
X0, X1, DIAS = 110, 970, 1176
xd = lambda d: X0 + (X1 - X0) * d / DIAS
DOTS = [xd(0), xd(246), xd(281)]
CAPA_SVG = f"""<svg style="position:absolute;left:0;top:1130px" width="1080" height="500" viewBox="0 0 1080 500">
  <path id="chave" d="M{X0} 222 V 178 H {X1} V 222" fill="none" stroke="{A.BRAND}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <g id="interr"><circle cx="540" cy="178" r="70" fill="#fff"/>
    <text x="540" y="210" text-anchor="middle" font-family="Inter" font-weight="700" font-size="96" fill="{A.BRAND_DARK}">?</text></g>
  <line x1="{X0}" y1="318" x2="{X1}" y2="318" stroke="{A.BRAND_DEEP}" stroke-width="10" stroke-linecap="round"/>
  {''.join(f'<circle class="dot" cx="{x:.1f}" cy="318" r="22" fill="{A.BRAND_DARK}" stroke="{A.SOFT}" stroke-width="7"/>' for x in DOTS)}
  <circle cx="{X1}" cy="318" r="28" fill="#fff" stroke="{A.BRAND_DEEP}" stroke-width="10"/>
  <text x="{X0 - 8}" y="400" font-family="Inter" font-weight="700" font-size="38" fill="{A.BRAND_DEEP}">jul/23</text>
  <text x="{X1 + 8}" y="400" text-anchor="end" font-family="Inter" font-weight="700" font-size="38" fill="{A.BRAND_DEEP}">set/26</text>
  <text x="{X0 - 8}" y="448" font-family="Inter" font-weight="500" font-size="32" fill="{A.BRAND_DEEP}">1ª remessa</text>
  <text x="{X1 + 8}" y="448" text-anchor="end" font-family="Inter" font-weight="500" font-size="32" fill="{A.BRAND_DEEP}">valor da carteira</text>
</svg>"""

CORPO = f"""
<div class="cena" id="papel">
  <div class="tit" id="tA">No período: <b>11,8%</b> em dólar e <b>25,1%</b> em reais.</div>
  <div class="tit" id="tA2">Só que esse período tem <b>3,2 anos</b>.</div>
  <div class="tit" id="tB">Ao ano: <b>3,5%</b> em dólar e <b>7,2%</b> em reais.</div>
  <div class="tit" id="tC">Ao mês: <b>0,29%</b> em dólar e <b>0,58%</b> em reais.</div>
  <div class="tit" id="tD">A TIR usa a data real de cada remessa.</div>
  <div class="nota" id="nota">{NOTA}</div>
  <div id="janela"><div id="tela">
    <img id="iPer" src="file://{TELAS}/periodo.png"><img id="iAno" src="file://{TELAS}/ano.png" style="opacity:0">
    <img id="iMes" src="file://{TELAS}/mes.png" style="opacity:0"><img id="iComo" src="file://{TELAS}/como.png" style="opacity:0">
    <div class="anel" id="aPar"></div><div class="anel" id="aAno"></div><div class="anel" id="aMes"></div>
    <div class="onda" id="o1"></div><div class="toque" id="q1"></div>
    <div class="onda" id="o2"></div><div class="toque" id="q2"></div>
    <div class="onda" id="o3"></div><div class="toque" id="q3"></div>
  </div></div>
</div>

<div class="cena" id="licao" style="opacity:0">
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="h1" style="font-size:104px">Rendimento no período não é rendimento ao ano.</div>
    <div class="apoio" style="margin-top:44px;font-size:44px">É o mesmo número, escrito de três jeitos. Para comparar taxas, use a mesma base.</div>
    <div id="chips" style="display:flex;flex-direction:column;gap:22px;margin-top:64px">
      <div class="linha-t"><span class="lt-v num">11,8%</span><span class="lt-r">no período</span></div>
      <div class="linha-t"><span class="lt-v num">3,5%</span><span class="lt-r">ao ano</span></div>
      <div class="linha-t"><span class="lt-v num">0,29%</span><span class="lt-r">ao mês</span></div>
    </div>
    <div class="apoio" id="lt-nota" style="margin-top:26px;font-size:30px">Em dólar, na conta de exemplo.</div>
  </div>
</div>

<div class="cena suave" id="capa">
  <div style="position:absolute;left:90px;top:290px">{A.logo_horizontal("color", 60)}</div>
  <div style="position:absolute;left:90px;top:560px;width:900px">
    <div class="eyebrow" style="margin-bottom:40px;color:{A.BRAND_DEEP}">Ritmo do retorno</div>
    <div class="h1" id="gancho">Rendeu <span style="color:{A.BRAND_DARK}">11,8%</span>. Em quanto tempo?</div>
  </div>
  {CAPA_SVG}
</div>

{fechamento("Remessas ao exterior no timtimcash")}
<style>
.linha-t{{display:flex;align-items:baseline;gap:24px;padding:22px 34px;border-radius:28px;background:#fff;border:3px solid {A.FIO}}}
.lt-v{{font-size:64px;font-weight:700;letter-spacing:-.04em;color:{A.BRAND_DARK};min-width:220px}}
.lt-r{{font-size:40px;font-weight:600;color:{A.INK};letter-spacing:-.02em}}
</style>
"""

JS = f"""
const PAR={PAR}, PER_L={PER_L}, FRASE_L={FRASE_L};
const T_ANO={T_ANO}, T_MES={T_MES}, T_COMO={T_COMO};
caixa($('aPar'), PAR, [22,22,22,8]); caixa($('aAno'), PAR, [22,22,22,8]); caixa($('aMes'), PAR, [22,22,22,8]);
marcas('mPer', PER_L); marcas('mFr', FRASE_L);
ponto($('q1'), ...T_ANO); ponto($('o1'), ...T_ANO); ponto($('q2'), ...T_MES); ponto($('o2'), ...T_MES);
ponto($('q3'), ...T_COMO); ponto($('o3'), ...T_COMO);
const chave = document.getElementById('chave'); const L = chave.getTotalLength();
chave.style.strokeDasharray = L;
function render(t){{
  // 1. capa verde suave (0 a 2,7 s): a chave do período se desenha e a pergunta aparece; depois sobe
  const sobe = prog(t, 2.7, 3.15);
  $('capa').style.transform = `translateY(${{-1920*sobe}}px)`;
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,2.7)}})`; $('gancho').style.transformOrigin='0 50%';
  chave.style.strokeDashoffset = L*(1-prog(t, 0.25, 1.35));
  const q = prog(t, 1.1, 1.55); $('interr').style.opacity = q;
  $('interr').style.transform = `translate(540px,178px) scale(${{.6+.4*q}}) translate(-540px,-178px)`;
  [...document.querySelectorAll('.dot')].forEach((d,i)=>{{ const p = .55+.45*prog(t, .1+i*.18, .45+i*.18);
    d.style.transformBox='fill-box'; d.style.transformOrigin='center'; d.style.transform=`scale(${{p}})`; }});
  // 2. papel: títulos
  titulo('tA', t, 2.85, 5.3); titulo('tA2', t, 5.45, 7.75); titulo('tB', t, 7.9, 10.55);
  titulo('tC', t, 10.7, 13.25); titulo('tD', t, 13.4, 16.6);
  const ent = prog(t, 2.9, 3.5), sai = prog(t, 16.6, 16.95);
  $('janela').style.opacity = Math.min(ent, 1-sai); $('nota').style.opacity = Math.min(ent, 1-sai);
  $('janela').style.transform = `translateY(${{(1-ent)*70 - sai*40}}px)`;
  $('nota').style.transform = `translateY(${{(1-ent)*70 - sai*40}}px)`;
  // câmera: o cartão inteiro; depois do toque em "Como o retorno é calculado", aproxima da explicação
  const c = prog(t, 14.35, 15.1);
  camera(6 + (318-6)*c, 29*c, 2 + 0.35*c);
  // anéis
  anel('aPar', t, 3.75, 5.15); marca('mPer', PER_L.length, t, 5.95, 7.5);
  anel('aAno', t, 9.0, 10.4); anel('aMes', t, 11.8, 13.1); marca('mFr', FRASE_L.length, t, 15.2, 16.45);
  // toques e troca de estado (cada tela é a captura real depois do toque)
  toque('q1','o1', t, 8.4); toque('q2','o2', t, 11.2); toque('q3','o3', t, 13.9);
  $('iAno').style.opacity = prog(t, 8.55, 8.9); $('iMes').style.opacity = prog(t, 11.35, 11.7);
  $('iComo').style.opacity = prog(t, 14.05, 14.4);
  // 3. lição
  const li = prog(t, 17.0, 17.4);
  $('licao').style.opacity = li; $('licao').style.transform = `translateY(${{(1-li)*40}}px)`;
  [...$('chips').children].forEach((e,i)=>{{ const p=prog(t, 17.6+i*.18, 17.95+i*.18); e.style.opacity=p; e.style.transform=`translateY(${{(1-p)*24}}px)`; }});
  $('lt-nota').style.opacity = prog(t, 18.2, 18.55);
  // 4. fechamento verde sobe
  const f = prog(t, 20.4, 20.85);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

if __name__ == "__main__":
    executar(pagina(CORPO, JS), SAIDA, DUR, CAPA, t_capa=2.5)
