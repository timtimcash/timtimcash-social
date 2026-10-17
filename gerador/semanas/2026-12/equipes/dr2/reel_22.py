# -*- coding: utf-8 -*-
"""Reel de 22/12/2026 (terça) · "Boas festas" · marca · capa verde · equipe dr2. 12 s.

A frase da marca ("Seu dinheiro deixa pistas todos os dias.", da página do site e do manual) vira "Que 2027 deixe boas pistas.".
Os 365 dias de 2026 aparecem como pontos num calendário (1º/1/2026 é quinta-feira; cada mês com os dias no dia da semana certo),
caminham pela tela e se juntam no símbolo do timtimcash. O símbolo e o logotipo vêm só dos arquivos oficiais (artes.logo e
artes.logo_vertical): sobre o papel, a versão em cores para fundo claro; sobre o verde, a negativa. Entrada do símbolo só por escala
uniforme e opacidade; nada de girar, distorcer, recolorir, sombra ou brilho. Os pontos não desenham o símbolo: chegam a uma área em
volta dele e somem quando ele aparece. Tom de agradecimento, sem vender: o fechamento tem só o logotipo e o obrigado.

python3 reel_22.py  |  REEL_PREVIA="0 0.5 1 3 6 10" python3 reel_22.py
"""
import os, sys, json, math, random
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, saida, trabalho, pagina

PASTA = "2026-12-22_reel-boas-festas"
SAIDA = saida(PASTA)
TRAB = trabalho("22")

# ---------------------------------------------------------------- os 365 dias de 2026 num calendário (4 × 3 meses)
assert date(2026, 1, 1).weekday() == 3          # quinta-feira
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
P, D = 30, 19                                    # passo e diâmetro dos pontos
X0, Y0, GX, GY, ROT = 90, 740, 230, 250, 36
pontos, rotulos = [], []
for m in range(12):
    bx, by = X0 + (m % 4) * GX, Y0 + (m // 4) * GY
    rotulos.append(f'<span class="ml" style="left:{bx}px;top:{by}px">{MESES[m]}</span>')
    d = date(2026, m + 1, 1)
    primeiro = (d.weekday() + 1) % 7              # domingo = 0
    while d.month == m + 1:
        i = primeiro + d.day - 1
        pontos.append([m, round(bx + (i % 7) * P + P / 2, 1), round(by + ROT + (i // 7) * P + P / 2, 1)])
        d = date.fromordinal(d.toordinal() + 1)
assert len(pontos) == 365
# destino: uma área em volta do símbolo (elipse), sem desenhar o símbolo
SX, SY, SH = 540, 1075, 300                      # centro e altura do símbolo oficial
SW = SH * 220 / 134
rnd = random.Random(2026)
dados = []
for k, (m, x, y) in enumerate(pontos):
    ang, r = rnd.uniform(0, 2 * math.pi), math.sqrt(rnd.uniform(0.05, 1))
    tx, ty = SX + math.cos(ang) * r * SW * .47, SY + math.sin(ang) * r * SH * .42
    mx, my = (x + tx) / 2, (y + ty) / 2
    dx, dy = tx - x, ty - y
    sinal = 1 if k % 2 else -1
    cx, cy = mx - dy * .42 * sinal, my + dx * .42 * sinal          # curva: os pontos caminham em arco
    dados.append([round(x, 1), round(y, 1), round(cx, 1), round(cy, 1), round(tx, 1), round(ty, 1)])
bolinhas = "".join(f'<i class="pt" id="p{k}"></i>' for k in range(365))
# pistas que flutuam nas margens enquanto o símbolo fica parado (não encostam no símbolo nem no texto)
soltas = []
for k in range(14):
    lado = k % 2
    x = rnd.uniform(80, 220) if lado == 0 else rnd.uniform(860, 1000)
    soltas.append([round(x, 1), round(rnd.uniform(900, 1250), 1), round(rnd.uniform(10, 16), 1), round(rnd.uniform(0, 1.4), 2), round(rnd.uniform(26, 48), 1)])
flutua = "".join(f'<i class="fl" id="fl{k}" style="width:{d}px;height:{d}px;margin:-{d / 2}px 0 0 -{d / 2}px"></i>' for k, (x, y, d, a, v) in enumerate(soltas))

# ---------------------------------------------------------------- tempos (s)
T1 = (0.0, 2.95)        # frase da marca
T2 = (3.15, 5.7)        # Que 2027 deixe boas pistas.
VIAGEM = 3.0            # os pontos começam a caminhar
SIMB = (4.85, 5.5)      # o símbolo entra
T3 = 5.85               # Boas festas
FIM = 8.55
DUR = 12.2

CSS = f"""
#cena{{background:{A.BG}}}
#top{{position:absolute;left:90px;top:330px;width:900px}}
#top .h1{{font-size:100px;margin-top:30px}}
#f2{{position:absolute;left:90px;top:330px;width:900px;opacity:0}}
#f2 .h1{{font-size:112px;margin-top:30px}}
.pt{{position:absolute;left:0;top:0;width:{D}px;height:{D}px;margin:-{D / 2}px 0 0 -{D / 2}px;border-radius:50%;background:{A.BRAND};opacity:0;will-change:transform}}
.fl{{position:absolute;left:0;top:0;border-radius:50%;background:{A.BRAND};opacity:0}}
.ml{{position:absolute;font-size:26px;font-weight:700;letter-spacing:.04em;color:{A.MUTED};opacity:0}}
#sim{{position:absolute;left:{SX - SW / 2:.1f}px;top:{SY - SH / 2:.1f}px;width:{SW:.1f}px;height:{SH}px;opacity:0;transform-origin:50% 50%}}
#bf{{position:absolute;left:0;top:1300px;width:1080px;text-align:center;opacity:0}}
#bf span{{display:inline-block;font-size:150px;line-height:1;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#ob{{background:{A.BRAND};color:#fff}}
#obIn{{position:absolute;left:0;top:520px;width:1080px;display:flex;flex-direction:column;align-items:center;text-align:center}}
#obT{{font-size:72px;line-height:1.08;font-weight:700;letter-spacing:-.045em;width:820px;margin-top:96px;text-wrap:balance}}
"""

CORPO = f"""
<div class="cena" id="cena">
  <div id="top">
    <div class="eyebrow">Fim de ano</div>
    <div class="h1">Seu dinheiro deixa <span style="color:{A.BRAND_DARK}">pistas</span> todos os dias.</div>
  </div>
  <div id="f2">
    <div class="eyebrow">2027</div>
    <div class="h1">Que 2027 deixe <span style="color:{A.BRAND_DARK}">boas pistas.</span></div>
  </div>
  {"".join(rotulos)}
  {bolinhas}
  {flutua}
  <div id="sim">{A.logo("color", SH)}</div>
  <div id="bf"><span id="bfT">Boas festas</span></div>
</div>

<div class="cena" id="ob" style="transform:translateY(1920px)">
  <div id="obIn">
    {A.logo_vertical("white", 300)}
    <div id="obT">Obrigado por estar com a gente em 2026.</div>
  </div>
</div>
"""

JS = f"""
const DADOS = {json.dumps(dados)}, MES = {json.dumps([p[0] for p in pontos])}, SOLTAS = {json.dumps(soltas)};
const T1={list(T1)}, T2={list(T2)}, VIAGEM={VIAGEM}, SIMB={list(SIMB)}, T3={T3}, FIM={FIM};
function render(t){{
  // 1. a frase da marca e os dias de 2026, um ponto por dia
  const s1 = prog(t, T1[1], T1[1]+.3);
  $('top').style.opacity = 1 - s1; $('top').style.transform = `translateY(${{-40*s1}}px)`;
  document.querySelectorAll('.ml').forEach((e,m) => {{ e.style.opacity = lin(t, -0.3 + m*.17, -0.1 + m*.17) * (1 - prog(t, VIAGEM-.1, VIAGEM+.3)); }});
  for (let k=0;k<365;k++){{
    const [x, y, cx, cy, tx, ty] = DADOS[k];
    const a = -0.3 + k*0.0062, p = pback(t, a, a+.3);
    const v0 = VIAGEM + k*0.0037, v = prog(t, v0, v0+.95);
    const u = 1 - v;
    const px = u*u*x + 2*u*v*cx + v*v*tx, py = u*u*y + 2*u*v*cy + v*v*ty;
    const e = $('p'+k);
    e.style.opacity = lin(t, a, a+.1) * (1 - lin(t, v0+.7, v0+.95));
    e.style.transform = `translate(${{px.toFixed(1)}}px, ${{py.toFixed(1)}}px) scale(${{(Math.max(0, p) * (1 - .45*v)).toFixed(3)}})`;
  }}
  // 2. Que 2027 deixe boas pistas.
  const e2 = prog(t, T2[0], T2[0]+.4), s2 = prog(t, T2[1], T2[1]+.3);
  $('f2').style.opacity = Math.min(e2, 1 - s2); $('f2').style.transform = `translateY(${{(1-e2)*30 - s2*40}}px)`;
  // 3. o símbolo oficial: só escala uniforme e opacidade
  const ps = pout(t, SIMB[0], SIMB[1]);
  $('sim').style.opacity = ps; $('sim').style.transform = `scale(${{(.82 + .18*ps).toFixed(4)}})`;
  // 4. Boas festas
  const pb = pback(t, T3, T3+.55);
  $('bf').style.opacity = lin(t, T3, T3+.2); $('bfT').style.transform = `scale(${{(.7 + .3*pb).toFixed(3)}})`;
  // pistas soltas nas margens, subindo devagar
  SOLTAS.forEach(([x, y, d, a, v], k) => {{ const t0 = SIMB[0] + a; const e = $('fl'+k);
    const vida = t - t0; e.style.opacity = t < t0 ? 0 : Math.min(lin(t, t0, t0+.4), 1 - prog(t, FIM-.1, FIM+.3)) * .9;
    e.style.transform = `translate(${{x.toFixed(1)}}px, ${{(y - v*Math.max(0, vida)).toFixed(1)}}px)`; }});
  // 5. obrigado (verde, logotipo negativo)
  sobe('ob', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:{540 - 330 * 220 / 134 / 2:.1f}px;top:610px">{A.logo("white", 330)}</div>
  <div style="position:absolute;left:0;top:1080px;width:1080px;text-align:center">
    <div style="font-size:176px;line-height:1;font-weight:700;letter-spacing:-.05em;color:#fff">Boas festas</div>
  </div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
