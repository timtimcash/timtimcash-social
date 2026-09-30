# -*- coding: utf-8 -*-
"""Reel de 14/10/2026 · "Rendeu em dólar todos os anos. E em reais?" (capa tinta), 1080 × 1920, 30 fps, 23 s.

Tela real "Rendimento ano a ano" (Remessas ao exterior, celular, conta fictícia), revelada ano a ano
com anéis: 2023 +6,5% em US$ e +3,8% em R$; 2024 +3,6% e +34,4%; 2025 +3,9% e −7,7%;
2026 até hoje +2,5% e +2,4% (gerador/telas/LEIAME.md).
python3 reel_1410.py  |  REEL_PREVIA="0 2.4 4" python3 reel_1410.py
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import reelkit as K
A = K.A

PASTA = "2026-10-14_reel-rendimento-ano-a-ano"
O = os.path.dirname(AQUI)
SAIDA = os.path.join(O, "saida", PASTA)
TELA = os.path.join(SAIDA, "telas", "celular-remessas-rendimento-ano-a-ano.jpg")
DUR = 23.0

DARK_TEXTO = "#C9D1C8"   # texto de apoio sobre a tinta (o mesmo das capas de 05/10)
MENOS = "−"

# ano, sobretítulo, US$, R$, negativo?, panorâmica, caixa do R$ no cartão (px CSS)
ANOS = [
    ("2023", "2023", "+6,5%", "+3,8%", False, 0, [284.5, 190.5, 62.5, 38]),
    ("2024", "2024", "+3,6%", "+34,4%", False, 60, [269, 318, 78, 38]),
    ("2025", "2025", "+3,9%", MENOS + "7,7%", True, 185, [274.8, 445.5, 72.2, 38]),
    ("2026", "2026 até hoje", "+2,5%", "+2,4%", False, 300, [275.8, 573.5, 71.2, 38]),
]
M = 14                       # margem do cartão na tela do celular
ALT = 937 + 2 * M            # altura da tela em px CSS
NOTA_CARTAO = [15, 855.5, 332, 66]   # "Em US$ é o rendimento do investimento. Em R$ ..."

# tempos (s)
SLIDE = 2.60
Y = [2.80, 5.30, 7.80, 10.30]   # cada ano
EXPL = 12.80                     # como é calculado
CONC = 16.00                     # conclusão
FIM = 19.60                      # fechamento

def m(r):  # caixa do cartão -> caixa na tela
    return [r[0] + M, r[1] + M, r[2], r[3]]

def m_rs(r):  # anel do R$: quase sem folga em cima (o valor em US$ está 3 px CSS acima), folga dos lados e embaixo
    return [round(r[0] + M - 7, 1), round(r[1] + M - 1.5, 1), round(r[2] + 14, 1), round(r[3] + 8, 1)]

aneis = "".join(f'<div class="anel{" coral" if neg else ""}" id="a{a}"></div>' for a, _, _, _, neg, _, _ in ANOS) + '<div class="anel" id="aNota"></div>'
titulos = "".join(
    f'<div class="tit" id="t{a}"><span class="sobre">{sob}</span>Em dólar, rendeu {us}.<br>Em reais, <b class="{"neg" if neg else ""}">{rs}</b>.</div>'
    for a, sob, us, rs, neg, _, _ in ANOS)

def capa_tabela():
    linhas = "".join(
        f'<div class="c-lin"><div class="c-ano">{a}{"<small>até hoje</small>" if a == "2026" else ""}</div>'
        f'<div class="c-us">{u}</div><div class="c-rs"><span id="q{i}">?</span></div></div>'
        for i, (a, _, u, *_) in enumerate(ANOS))
    return f"""<div id="tabela">
  <div class="c-cab"><span></span><span>em US$</span><span>em R$</span></div>
  {linhas}
</div>"""

def resumo():
    cab = "".join(f'<div class="r-ano">{a}{"<small>até hoje</small>" if a == "2026" else ""}</div>' for a, *_ in ANOS)
    us = "".join(f'<div class="r-v" id="ru{i}">{u}</div>' for i, (_, _, u, *_) in enumerate(ANOS))
    rs = "".join(f'<div class="r-v {"neg" if neg else "pos"}" id="rr{i}">{r}</div>' for i, (_, _, _, r, neg, *_) in enumerate(ANOS))
    return f"""<div id="resumo">
  <div class="r-lin r-cab"><div class="r-rot"></div>{cab}</div>
  <div class="r-lin"><div class="r-rot">em US$</div>{us}</div>
  <div class="r-lin"><div class="r-rot">em R$</div>{rs}</div>
</div>"""

CSS = f"""
.tit{{font-size:72px}}
.tit b.neg{{color:{A.RED_TEXT}}}
#capa .eyebrow{{color:{A.MENTA}}}
#capa .h1{{font-size:116px;line-height:.96}}
#tabela{{position:absolute;left:90px;top:910px;width:900px}}
.c-cab,.c-lin{{display:grid;grid-template-columns:250px 1fr 1fr;align-items:center}}
.c-cab{{height:64px;font-size:32px;font-weight:600;color:{DARK_TEXTO}}}
.c-cab span{{text-align:center}}
.c-lin{{height:146px;border-top:2px solid #262E27}}
.c-ano{{font-size:44px;font-weight:700;letter-spacing:-.02em;color:#fff;font-variant-numeric:tabular-nums;line-height:1}}
.c-ano small{{display:block;font-size:24px;font-weight:600;letter-spacing:0;color:{DARK_TEXTO};margin-top:8px}}
.c-us{{text-align:center;font-size:76px;font-weight:700;letter-spacing:-.04em;color:{A.MENTA};font-variant-numeric:tabular-nums}}
.c-rs{{display:flex;justify-content:center}}
.c-rs span{{display:flex;align-items:center;justify-content:center;width:150px;height:100px;border-radius:26px;border:3px dashed #6B786D;
  font-size:70px;font-weight:700;color:#fff}}
.apoio2{{font-size:33px;line-height:1.28;font-weight:500;color:{A.MUTED};letter-spacing:-.018em;margin-top:16px;text-wrap:balance}}
#resumo{{margin-top:70px;background:#fff;border:2px solid {A.FIO};border-radius:36px;padding:34px 36px 30px;
  box-shadow:0 1px 2px rgba(15,20,16,.04),0 14px 34px -16px rgba(15,20,16,.14)}}
.r-lin{{display:flex;align-items:center;height:104px}}
.r-lin+.r-lin{{border-top:2px solid {A.FIO}}}
.r-cab{{height:78px;align-items:flex-start}}
.r-rot{{width:124px;flex:none;font-size:30px;font-weight:600;color:{A.MUTED}}}
.r-ano{{flex:1;text-align:center;font-size:30px;font-weight:700;color:{A.MUTED};font-variant-numeric:tabular-nums;line-height:1}}
.r-ano small{{display:block;font-size:20px;font-weight:600;margin-top:6px}}
.r-v{{flex:1;text-align:center;font-size:44px;font-weight:700;letter-spacing:-.035em;font-variant-numeric:tabular-nums;color:{A.INK}}}
.r-v.pos{{color:{A.BRAND_DARK}}}
.r-v.neg{{color:{A.RED_TEXT}}}
"""

CORPO = f"""
<div class="cena" id="papel">
  {titulos}
  <div class="tit" id="tE" style="font-size:60px">Em reais, entra também a variação do câmbio no ano.
    <div class="apoio2">Para fechar cada ano, ele usa o saldo de 31/12 e a PTAX de compra do último dia útil.</div></div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{K.tela("tela", [("img", TELA, M, M, 1086, "")], ALT, aneis)}</div>
</div>

<div class="cena" id="conc" style="opacity:0">
  <div style="position:absolute;left:90px;top:360px;width:900px">
    <div class="h1" style="font-size:104px;line-height:.98;text-wrap:wrap">O investimento<br>é o mesmo.<br><span style="color:{A.BRAND_DARK}">O câmbio muda<br>o ano.</span></div>
    {resumo()}
    <div class="apoio" id="rNota" style="font-size:28px;margin-top:22px">Mesma conta de exemplo da tela real.</div>
  </div>
</div>

<div class="cena tinta" id="capa">
  <div style="position:absolute;left:90px;top:290px">{A.logo_horizontal("dark", 60)}</div>
  <div style="position:absolute;left:90px;top:420px;width:900px">
    <div class="eyebrow" style="margin-bottom:36px">Investimento no exterior</div>
    <div class="h1" id="gancho">Rendeu em dólar<br>todos os anos.<br>E em reais?</div>
  </div>
  {capa_tabela()}
</div>

{K.fim("Remessas ao exterior no timtimcash")}
"""

JS = f"""
const Y={Y}, EXPL={EXPL}, CONC={CONC}, FIM={FIM}, SLIDE={SLIDE};
const PAN={[p for *_, p, _ in ANOS]};
const ANOS={[a for a, *_ in ANOS]};
const CX={[m_rs(r) for *_, r in ANOS]};
const US={[float(u.replace("+", "").replace("%", "").replace(",", ".")) for _, _, u, *_ in ANOS]};
ANOS.forEach((a,i) => caixa($('a'+a), CX[i], 0));
caixa($('aNota'), {m(NOTA_CARTAO)}, 22);
const TOPO_EXPL = {ALT - 500};
function render(t){{
  // 1. capa (tinta): barras do dólar crescem, as interrogações pulsam; em 2,6 s a capa sobe
  const sobe = prog(t, SLIDE, SLIDE+.45);
  $('capa').style.transform = `translateY(${{-1920*sobe}}px)`;
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,SLIDE)}})`; $('gancho').style.transformOrigin='0 50%';
  for (let i=0;i<4;i++){{ const f = (t*1.6 - i*.22); const s = 1 + .045*Math.max(0, Math.sin(Math.PI*2*f))*(t<SLIDE?1:0); $('q'+i).style.transform=`scale(${{s}})`; }}
  // 2. títulos ano a ano
  ANOS.forEach((a,i) => {{
    const ini = i==0 ? 2.85 : Y[i]+.18, sai = i<3 ? Y[i+1]-.06 : EXPL-.06;
    titulo('t'+a, t, ini, sai);
  }});
  titulo('tE', t, EXPL+.18, CONC-.06);
  // 3. janela: entra por baixo como no modelo; sai na conclusão
  const ent = prog(t, 2.9, 3.5), saiJ = prog(t, CONC, CONC+.4);
  ['janela','nota'].forEach(id => {{ $(id).style.opacity = Math.min(ent, 1-saiJ);
    $(id).style.transform = `translateY(${{(1-ent)*70 - saiJ*40}}px)`; }});
  // panorâmica: um ano de cada vez e, no fim, a nota do cartão
  let topo = 0;
  for (let i=1;i<4;i++) topo += (PAN[i]-PAN[i-1])*prog(t, Y[i]+.05, Y[i]+.7);
  topo += (TOPO_EXPL-PAN[3])*prog(t, EXPL+.05, EXPL+.9);
  pan('tela', topo);
  // 4. anéis no resultado em reais de cada ano
  ANOS.forEach((a,i) => {{ const ini = i==0 ? 3.65 : Y[i]+.8, sai = i<3 ? Y[i+1]-.12 : EXPL-.12; anel('a'+a, t, ini, sai); }});
  anel('aNota', t, EXPL+1.0, CONC-.1);
  // 5. conclusão
  const ci = prog(t, CONC+.15, CONC+.55);
  $('conc').style.opacity = ci; $('conc').style.transform = `translateY(${{(1-ci)*40}}px)`;
  const r0 = prog(t, CONC+.45, CONC+.8);
  $('resumo').style.opacity = r0; $('resumo').style.transform = `translateY(${{(1-r0)*30}}px)`;
  $('rNota').style.opacity = prog(t, CONC+.9, CONC+1.2);
  for (let i=0;i<4;i++){{ const p = prog(t, CONC+.8+i*.14, CONC+1.1+i*.14); const e = $('rr'+i);
    e.style.opacity = p; e.style.transform = `scale(${{1.18-.18*p}})`; }}
  // 6. fechamento verde
  const f = prog(t, FIM, FIM+.45);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

HTML = K.pagina(CORPO, CSS, JS)

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, capa_t=2.3, trabalho=os.path.join(AQUI, "trabalho", "1410"))
