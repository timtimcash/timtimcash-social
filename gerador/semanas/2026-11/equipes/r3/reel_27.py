# -*- coding: utf-8 -*-
"""Reel de 27/11/2026 · "Black Friday: respira" (1080 × 1920, 30 fps, 19,4 s). Capa da grade: verde (sem coral).

Só tipografia animada e ícones de traço, sem tela do site. Roteiro:
- 0 a 1,55 s: tensão. Fundo tinta, "Oferta acaba em" e um cronômetro de oferta que corre rápido e acelera
  (00:09:59 para baixo, de 6 a 34 segundos por segundo), com selos de pressão ("−60%", "Só hoje",
  "Últimas unidades"), uma barra coral que esvazia e um tremor que cresce. Tudo congela de uma vez.
- 1,55 a 3,95 s: alívio. O cronômetro congela e a calma se abre do centro, num círculo (expirar): "Respira."
- três perguntas, uma por vez, dentro de um círculo verde suave que "respira" (4 s por ciclo):
  1. "Eu compraria sem o desconto?" (o selo de % cai da etiqueta);
  2. "Era esse o preço há 60 dias?" (Procon-SP, 06/11/2025: desconto sobre o menor preço dos últimos 60 dias);
  3. "A parcela cabe em janeiro?" (IPVA, IPTU e material escolar caem no calendário de janeiro);
- "Comprou pela internet? 7 dias para desistir." (CDC, art. 49: a contar do recebimento; o que foi pago volta);
- fechamento verde: "Orçamentos no timtimcash".
python3 reel_27.py  |  REEL_PREVIA="0 0.5 1 2.5 5 8 11.5 14.5 17.5" python3 reel_27.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r3kit import K, A, saida, trabalho

PASTA = "2026-11-27_reel-black-friday-respira"
SAIDA = saida(PASTA)
TRAB = trabalho("27")
DUR = 19.4
MENOS = "−"

# ---------------------------------------------------------------- tempos (s)
CONG = 1.55                       # o cronômetro congela
Q = [(4.3, 7.0), (7.05, 10.65), (10.7, 13.65), (13.7, 16.6)]   # pergunta 1, 2, 3 e o CDC
FIM = 16.65

def palavras(ident, texto, destaque=(), cls="q"):
    """Cada palavra num <span> (entram uma a uma). destaque: palavras em verde escuro (índices)."""
    ws = texto.split(" ")
    return f'<div class="{cls}" id="{ident}">' + " ".join(
        f'<span class="w{" d" if i in destaque else ""}">{w}</span>' for i, w in enumerate(ws)) + "</div>"

def pontos(n):
    return "".join(f'<i class="pt{" on" if i == n else ""}"></i>' for i in range(3))

# ---------------------------------------------------------------- ícones de traço (viewBox 240 × 240, verde escuro)
TR = f'fill="none" stroke="{A.BRAND_DARK}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" pathLength="1"'
ICO_ETIQUETA = f"""<svg viewBox="0 0 240 240" class="ico" id="ic1">
  <path class="tr" {TR} d="M58 68 H150 L196 120 L150 172 H58 Q46 172 46 160 V80 Q46 68 58 68 Z"/>
  <circle class="tr" {TR} cx="152" cy="120" r="10"/>
  <text x="96" y="137" text-anchor="middle" font-family="Inter" font-weight="700" font-size="46" fill="{A.BRAND_DARK}" class="tx">R$</text>
  <g id="selo"><circle cx="178" cy="62" r="36" fill="{A.CORAL}"/>
    <text x="178" y="78" text-anchor="middle" font-family="Inter" font-weight="700" font-size="44" fill="#fff">%</text></g>
</svg>"""
ICO_60 = f"""<svg viewBox="0 0 240 240" class="ico" id="ic2">
  <rect class="tr" {TR} x="42" y="58" width="156" height="142" rx="24"/>
  <path class="tr" {TR} d="M42 98 H198"/><path class="tr" {TR} d="M86 40 V72"/><path class="tr" {TR} d="M154 40 V72"/>
  <text id="c60" x="120" y="166" text-anchor="middle" font-family="Inter" font-weight="700" font-size="62" letter-spacing="-2"
    fill="{A.BRAND_DARK}" style="font-variant-numeric:tabular-nums" class="tx">60</text>
  <text x="120" y="190" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" letter-spacing="2" fill="{A.BRAND_DARK}" class="tx">DIAS</text>
</svg>"""
ICO_JAN = f"""<svg viewBox="0 0 240 240" class="ico" id="ic3">
  <rect class="tr" {TR} x="42" y="58" width="156" height="142" rx="24"/>
  <path class="tr" {TR} d="M86 40 V72"/><path class="tr" {TR} d="M154 40 V72"/>
  <text x="120" y="92" text-anchor="middle" font-family="Inter" font-weight="700" font-size="22" letter-spacing="3" fill="{A.BRAND_DARK}" class="tx">JAN</text>
  <g id="b1"><rect x="64" y="104" width="112" height="22" rx="8" fill="{A.BRAND_DEEP}"/></g>
  <g id="b2"><rect x="64" y="134" width="112" height="22" rx="8" fill="{A.BRAND_DARK}"/></g>
  <g id="b3"><rect x="64" y="164" width="112" height="22" rx="8" fill="{A.BRAND}"/></g>
</svg>"""
PONTOS7 = "".join(
    f'<circle id="d{i}" cx="{120 + 92 * __import__("math").sin(i * 2 * 3.14159265 / 7):.2f}" '
    f'cy="{120 - 92 * __import__("math").cos(i * 2 * 3.14159265 / 7):.2f}" r="11" fill="#fff" stroke="{A.BRAND_DARK}" stroke-width="5"/>'
    for i in range(7))
ICO_7 = f"""<svg viewBox="0 0 240 240" class="ico" id="ic4">
  {PONTOS7}
  <text x="120" y="146" text-anchor="middle" font-family="Inter" font-weight="700" font-size="92" letter-spacing="-3" fill="{A.BRAND_DARK}" class="tx">7</text>
  <text x="120" y="174" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" letter-spacing="2" fill="{A.BRAND_DARK}" class="tx">DIAS</text>
</svg>"""

CSS = f"""
#tensao{{background:{A.INK}}}
#tensaoIn{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
#oferta{{position:absolute;left:0;top:560px;width:1080px;display:flex;justify-content:center}}
.pilula{{display:inline-flex;align-items:center;gap:22px;height:96px;padding:0 46px;border-radius:999px;border:3px solid #3A2A24;
  background:#1D1714;font-size:44px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#fff}}
.pisca{{width:24px;height:24px;border-radius:50%;background:{A.CORAL}}}
#relogio{{position:absolute;left:40px;top:704px;width:1000px;text-align:center;font-size:208px;font-weight:700;letter-spacing:-.03em;
  line-height:1;color:#fff;font-variant-numeric:tabular-nums;font-feature-settings:'tnum','cv11','ss01'}}
#trilho{{position:absolute;left:110px;top:950px;width:860px;height:16px;border-radius:99px;background:#2A2422}}
#barra{{position:absolute;left:0;top:0;height:16px;border-radius:99px;background:{A.CORAL};width:860px}}
.selo{{position:absolute;display:inline-flex;align-items:center;height:104px;padding:0 42px;border-radius:999px;font-size:44px;font-weight:700;
  letter-spacing:-.01em;white-space:nowrap;opacity:0}}
#s1{{left:640px;top:410px;background:{A.CORAL};color:#fff}}
#s2{{left:110px;top:1060px;border:4px solid #fff;color:#fff}}
#s3{{left:380px;top:1200px;background:{A.AMBER};color:{A.INK}}}
#calma{{position:absolute;left:0;top:0;width:1080px;height:1920px;background:{A.BG};clip-path:circle(0px at 540px 820px)}}
#respiro{{position:absolute;left:0;top:0;width:560px;height:560px;margin:-280px 0 0 -280px;border-radius:50%;background:{A.SOFT}}}
#respira{{position:absolute;left:90px;top:740px;width:900px;text-align:center;font-size:200px;font-weight:700;letter-spacing:-.055em;
  line-height:1;color:{A.INK};opacity:0}}
#respira2{{position:absolute;left:140px;top:1330px;width:800px;text-align:center;font-size:46px;font-weight:600;letter-spacing:-.02em;
  color:{A.MUTED};opacity:0}}
.olho{{position:absolute;left:0;top:300px;width:1080px;display:flex;flex-direction:column;align-items:center;gap:22px;opacity:0}}
.olho .eyebrow{{font-size:30px}}
.pts{{display:flex;gap:14px}}
.pt{{display:block;width:16px;height:16px;border-radius:50%;background:{A.FIO}}}
.pt.on{{background:{A.BRAND}}}
.ico{{position:absolute;left:340px;top:480px;width:400px;height:400px;opacity:0;overflow:visible}}
.q{{position:absolute;left:90px;top:1000px;width:900px;text-align:center;font-size:112px;line-height:1.0;font-weight:700;
  letter-spacing:-.05em;color:{A.INK};text-wrap:balance}}
.q .w{{display:inline-block;opacity:0}}
.q .w.d{{color:{A.BRAND_DARK}}}
.nt{{position:absolute;left:120px;width:840px;opacity:0;text-align:center;font-size:38px;line-height:1.3;font-weight:500;color:{A.MUTED};letter-spacing:-.015em;
  text-wrap:balance}}
.chips{{position:absolute;left:0;top:1345px;width:1080px;display:flex;justify-content:center;gap:22px}}
.chips .chip{{opacity:0;height:100px;font-size:44px;padding:0 44px}}
"""

CORPO = f"""
<div class="cena" id="tensao">
  <div id="tensaoIn">
    <div id="oferta"><span class="pilula"><i class="pisca" id="pisca"></i>Oferta acaba em</span></div>
    <div id="relogio">00:09:59</div>
    <div id="trilho"><div id="barra"></div></div>
    <span class="selo" id="s1">{MENOS}60%</span>
    <span class="selo" id="s2">Só hoje</span>
    <span class="selo" id="s3">Últimas unidades</span>
  </div>
</div>

<div class="cena" id="calma">
  <div id="respiro"></div>
  <div id="respira">Respira.</div>
  <div id="respira2">Antes de comprar, três perguntas.</div>

  <div class="olho" id="o1"><span class="eyebrow">Pergunta 1 de 3</span><span class="pts">{pontos(0)}</span></div>
  <div class="olho" id="o2"><span class="eyebrow">Pergunta 2 de 3</span><span class="pts">{pontos(1)}</span></div>
  <div class="olho" id="o3"><span class="eyebrow">Pergunta 3 de 3</span><span class="pts">{pontos(2)}</span></div>
  <div class="olho" id="o4"><span class="eyebrow">Comprou pela internet?</span></div>
  {ICO_ETIQUETA}{ICO_60}{ICO_JAN}{ICO_7}
  {palavras("q1", "Eu compraria sem o desconto?", (4,))}
  {palavras("q2", "Era esse o preço há 60 dias?", (4, 5))}
  {palavras("q3", "A parcela cabe em janeiro?", (4,))}
  {palavras("q4", "7 dias para desistir.", (0, 1))}
  <div class="nt" id="n2" style="top:1255px">Em 2025, o Procon-SP recomendou: desconto sobre o menor preço dos últimos 60 dias.</div>
  <div class="nt" id="n3" style="top:1255px">O começo do ano já chega com:</div>
  <div class="chips" id="ch3"><span class="chip">IPVA</span><span class="chip">IPTU</span><span class="chip">material escolar</span></div>
  <div class="nt" id="n4" style="top:1255px">Conta a partir do recebimento, e o que você pagou volta. CDC, art. 49.</div>
</div>

{K.fim("Orçamentos no timtimcash")}
"""

JS = f"""
const CONG={CONG}, Q={[list(q) for q in Q]}, FIM={FIM};
function hms(s){{ s = Math.max(0, Math.floor(s)); const h = Math.floor(s/3600), m = Math.floor(s/60)%60, x = s%60;
  return [h,m,x].map(v => String(v).padStart(2,'0')).join(':'); }}
function palavras(id, t, a, b){{ const ws = $(id).children; for (let i=0;i<ws.length;i++){{
    const p = pout(t, a + i*.085, a + i*.085 + .42), o = b ? prog(t, b, b+.3) : 0;
    ws[i].style.opacity = Math.min(p, 1-o); ws[i].style.transform = `translateY(${{(1-p)*34 - o*24}}px)`; }} }}
function some(id, t, a, b){{ const e=$(id); const vin=pout(t,a,a+.4), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=Math.min(vin, 1-vout); e.style.transform=`translateY(${{(1-vin)*26 - vout*18}}px)`; }}
// traço que se desenha (pathLength = 1)
function desenha(id, t, a, d){{ const p = prog(t, a, a+(d||.8)); $(id).querySelectorAll('.tr').forEach(e => {{
    e.style.strokeDasharray = '1 1'; e.style.strokeDashoffset = (1-p).toFixed(3); }});
  $(id).querySelectorAll('.tx').forEach(e => e.style.opacity = prog(t, a+.35, a+.7)); }}
function icone(id, t, a, b){{ const e=$(id); const vin=pout(t,a,a+.45), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity = Math.min(vin, 1-vout); e.style.transform = `scale(${{.86 + .14*vin - .06*vout}})`; desenha(id, t, a, .8); }}
function render(t){{
  // 1. tensão: o cronômetro de oferta corre rápido, os selos pulam, tudo treme um pouco
  const tc = Math.min(t, CONG), corrido = 6*tc + 9*tc*tc;           // acelera: de 6 a 34 segundos por segundo
  $('relogio').textContent = hms(599 - corrido);
  $('barra').style.width = (860*(1 - corrido/50)) + 'px';
  $('pisca').style.opacity = (Math.floor(t*(6 + 8*tc)) % 2 === 0 || t > CONG) ? 1 : .25;
  const tr = t < CONG ? 1.4 + 4.2*Math.pow(tc/CONG, 2) : 0;       // o tremor cresce até o congelamento
  $('tensaoIn').style.transform = `translate(${{tr*Math.sin(t*47)}}px, ${{tr*.75*Math.cos(t*53)}}px)`;
  $('relogio').style.transform = `scale(${{1 + (t < CONG ? .018*Math.abs(Math.sin(corrido*Math.PI)) : 0)}})`;
  [['s1',-.4,-7],['s2',.3,5],['s3',.62,-3]].forEach(([id,a,rot]) => {{
    const p = pback(t, a, a+.32), cai = prog(t, CONG+.0, CONG+.42);
    const e = $(id); e.style.opacity = Math.min(lin(t, a, a+.08), 1-cai);
    e.style.transform = `translateY(${{cai*220}}px) rotate(${{rot + Math.sin(t*9+a*10)*2*tr + cai*18}}deg) scale(${{.5 + .5*p}})`; }});
  // 2. expira: a calma se abre do centro, num círculo que cresce (íris) e cobre a tensão
  const ab = prog(t, CONG+.08, CONG+.7);
  $('calma').style.clipPath = `circle(${{(ab*1260).toFixed(1)}}px at 540px 820px)`;
  $('tensao').style.visibility = t < CONG + .72 ? 'visible' : 'hidden';
  // o círculo verde suave respira (4 s por ciclo); no "Respira." fica grande e no centro, depois sobe
  const fase = .5 - .5*Math.cos(2*Math.PI*Math.max(0, t - (CONG+.3))/4);
  const sobeR = prog(t, Q[0][0]-.25, Q[0][0]+.35);
  const cy = 840 + (680-840)*sobeR, d0 = 1.62 + (1.0-1.62)*sobeR;
  const R = $('respiro'); R.style.left = '540px'; R.style.top = cy + 'px';
  const amp = .12 + (.05-.12)*sobeR;              // no "Respira." o círculo respira fundo; nas perguntas, de leve
  R.style.transform = `scale(${{d0*(1 - amp + amp*fase)*(.55 + .45*pout(t, CONG+.1, CONG+.9))}})`;
  // "Respira."
  const rin = pout(t, CONG+.3, CONG+.8), rout = prog(t, Q[0][0]-.35, Q[0][0]-.05);
  $('respira').style.opacity = Math.min(rin, 1-rout);
  $('respira').style.transform = `scale(${{.9 + .1*rin + .02*fase}}) translateY(${{-rout*30}}px)`;
  some('respira2', t, CONG+.55, Q[0][0]-.35);
  // 3. as perguntas
  ['o1','o2','o3','o4'].forEach((id,i) => some(id, t, Q[i][0], Q[i][1]-.3));
  ['ic1','ic2','ic3','ic4'].forEach((id,i) => icone(id, t, Q[i][0]+.05, Q[i][1]-.3));
  ['q1','q2','q3','q4'].forEach((id,i) => palavras(id, t, Q[i][0]+.25, Q[i][1]-.3));
  // 1: o selo de % se solta da etiqueta e cai
  const solta = prog(t, Q[0][0]+1.55, Q[0][0]+2.2);
  $('selo').style.transformBox = 'fill-box'; $('selo').style.transformOrigin = 'center';
  $('selo').style.transform = `translate(${{solta*40}}px, ${{solta*solta*260}}px) rotate(${{solta*55}}deg)`;
  $('selo').style.opacity = (1 - prog(t, Q[0][0]+1.9, Q[0][0]+2.25)) * prog(t, Q[0][0]+.4, Q[0][0]+.7);
  // 2: o calendário conta até 60
  const c = Math.round(60*pout(t, Q[1][0]+.5, Q[1][0]+1.5)); $('c60').textContent = c;
  some('n2', t, Q[1][0]+1.0, Q[1][1]-.3);
  // 3: as contas de janeiro caem no calendário, uma a uma
  ['b1','b2','b3'].forEach((id,i) => {{ const a = Q[2][0]+.9+i*.32; const p = pback(t, a, a+.4);
    const e = $(id); e.style.opacity = lin(t, a, a+.1); e.style.transform = `translateY(${{(1-p)*-70}}px)`; }});
  some('n3', t, Q[2][0]+.8, Q[2][1]-.3);
  [...$('ch3').children].forEach((e,i) => {{ const a = Q[2][0]+.95+i*.32, p = pback(t, a, a+.4), o = prog(t, Q[2][1]-.3, Q[2][1]);
    e.style.opacity = Math.min(lin(t, a, a+.1), 1-o); e.style.transform = `translateY(${{(1-p)*30}}px) scale(${{.8+.2*p}})`; }});
  // 4: os 7 dias se acendem
  for (let i=0;i<7;i++){{ const a = Q[3][0]+.6+i*.14; const on = t >= a; const e = $('d'+i);
    e.setAttribute('fill', on ? '{A.BRAND}' : '#fff'); e.setAttribute('stroke', on ? '{A.BRAND}' : '{A.BRAND_DARK}');
    e.setAttribute('r', on ? (11 + 3*(1-lin(t, a, a+.25))).toFixed(2) : 11); }}
  some('n4', t, Q[3][0]+1.0, Q[3][1]-.05);
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

def capa():
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Black Friday · 27/11</div>
    <div class="h1" style="font-size:132px;line-height:.96;margin-top:34px">Black Friday: respira.</div>
  </div>
  <div style="position:absolute;left:90px;top:960px;width:900px;height:450px;border:6px solid #fff;border-radius:56px;
    display:flex;flex-direction:column;align-items:center;justify-content:center;gap:28px">
    <div style="font-size:38px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#fff">Oferta acaba em</div>
    <div style="font-size:186px;font-weight:700;letter-spacing:-.03em;line-height:1;color:#fff;font-variant-numeric:tabular-nums">00:09:59</div>
  </div>"""
    return K.pagina_capa(corpo, "", fundo="verde")

if __name__ == "__main__":
    K.executar(K.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
