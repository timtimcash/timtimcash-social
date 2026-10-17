# -*- coding: utf-8 -*-
"""Reel de 11/12/2026 · "13º: 4 perguntas antes de gastar" (capa tinta, o "4" em menta), 1080 × 1920, 30 fps. Equipe dr1.

Tipografia animada com tensão e alívio, num desenho próprio (uma lista de 4 perguntas que vão sendo marcadas):
- gancho na tinta: a 2ª parcela do exemplo (R$ 2.433,36) escorre até R$ 0 enquanto os gastos de dezembro saem dela;
  depois volta inteira: "Antes de gastar, 4 perguntas.";
- 1. Tenho dívida cara? Taxas médias de agosto de 2026, Banco Central (FATOS.md): rotativo 444,89% ao ano, cheque
  especial 136,41% ao ano;
- 2. Minha reserva cobre quantos meses? Tela real de Relatórios, Diagnóstico de dezembro (relógio em 11/12/2026):
  "Reserva · 13,8 meses · meta 6m";
- 3. O que vence no começo do ano? Na conta (Pendentes de janeiro e fevereiro de 2027, capturados): material escolar
  R$ 940 (12/01), IPVA 2027 R$ 1.236 (20/01), IPTU 2027 1ª parcela R$ 215 (10/02) = R$ 2.391, quase a 2ª parcela;
- 4. Qual é o plano para o resto? Tela real de Pendentes (11/12/2026): "EM 7 DIAS · 18/12/2026 · 13º salário ·
  2ª parcela · +R$ 2.433,36 · pendente".
Telas do build 2026-10-16.1 (capturas/captura11.py), conta de base, celular 390 px em escala 3.

python3 reel_11.py  |  REEL_PREVIA="0 0.8 1.6 2.6 3.4 5.0 6.6 8.4 10.2 12.0 13.8 15.6 17.4 19.6" python3 reel_11.py
"""
import os, sys
from decimal import Decimal as D
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import comum as C
K, A, N = C.K, C.A, C.N

PASTA = "2026-12-11_reel-quatro-perguntas-antes-de-gastar"
TRAB = C.trabalho("11")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas("11")
ARQ = CX["arquivos"]
MENTA, CORAL = A.MENTA, A.CORAL

# ---------------------------------------------------------------- números (conferidos contra a tela e o FATOS.md)
PARC = D("2433.36")
CONTAS = [("Material escolar", "12/01", D("940")), ("IPVA 2027", "20/01", D("1236")), ("IPTU 2027, 1ª parcela", "10/02", D("215"))]
SOMA = sum(v for _, _, v in CONTAS)
assert SOMA == D("2391") and PARC - SOMA == D("42.36")
assert CX["d_reserva"][4] == "Reserva quanto tempo o patrimônio cobre seus gastos 13,8 meses meta 6m"
assert CX["p_13"][4] == "13º salário · 2ª parcela Salário·Conta corrente +R$ 2.433,36 pendente" and CX["p_13dia"][4] == "EM 7 DIAS · 18/12/2026"
assert "A receber R$ 2.433 ,36" in CX["p_cab"][4]
assert CX["c_mat"][4] == "Material escolar Educação·Conta corrente −R$ 940,00 pendente" and "Janeiro 2027" in CX["c_texto"]
assert CX["c_ipva"][4] == "IPVA 2027 Impostos e Taxas·Conta corrente −R$ 1.236,00 pendente"
assert CX["d_iptu"][4] == "IPTU 2027 · 1ª parcela Impostos e Taxas·Conta corrente −R$ 215,00 pendente" and CX["d_per"][4] == "Fevereiro 2027"
assert "Dec 11 2026" in CX["relogio"]
ROT, CHE = D("444.89"), D("136.41")          # FATOS.md: Banco Central, agosto de 2026, % ao ano

# ---------------------------------------------------------------- tempos (s)
H1, H2 = 2.15, 4.0              # o gancho troca de frase em H1; a 1ª pergunta entra em H2
Q = 3.6
T = [round(H2 + Q * i, 2) for i in range(4)]
FIM = round(H2 + 4 * Q, 2)
DUR = round(FIM + 2.7, 2)

R_RES = [18, CX["d_reserva"][1] - 12, 354, CX["d_reserva"][3] + 24]
R_PEN = [10, CX["p_13dia"][1] - 4, 370, CX["p_13"][1] + CX["p_13"][3] - CX["p_13dia"][1] + 10]
P_REC = [90, 800, 900]

def check_svg(cor="#fff"):
    return (f'<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="{cor}" stroke-width="3.2" stroke-linecap="round" '
            f'stroke-linejoin="round"><path class="ck" d="M5 12.5l4.5 4.5L19 7.5" pathLength="1"/></svg>')

def lista(pre):
    """As 4 perguntas como uma lista de marcar: círculo com o número (atual em âmbar) que vira um visto verde."""
    itens = "".join(f'<div class="ci" id="{pre}c{i}"><span class="cn">{i + 1}</span><span class="cv">{check_svg()}</span></div>' for i in range(4))
    return f'<div class="lst" id="{pre}">{itens}</div>'

GASTOS = [("festas", -320, 190), ("presentes", 320, 210), ("viagem", -290, 390), ("promoções", 300, 410)]

CSS = f"""
.tit{{font-size:66px}}
#s0 .tit{{font-size:80px}}
#s0 .tit b{{color:{MENTA}}}
#rot0{{position:absolute;left:90px;top:640px;font-size:38px;font-weight:600;letter-spacing:-.015em;color:{K.DARK_TEXTO}}}
#v0{{position:absolute;left:84px;top:690px;font-size:240px;font-weight:700;letter-spacing:-.055em;line-height:1;color:#fff;font-variant-numeric:tabular-nums;white-space:nowrap}}
#v0 .rs{{font-size:.36em;font-weight:600;margin-right:.18em;color:{K.DARK_TEXTO}}}
#v0 .ct{{font-size:.5em;font-weight:600}}
.gs{{position:absolute;left:540px;top:830px;height:84px;padding:0 34px;border-radius:999px;background:{CORAL};color:#fff;font-size:40px;font-weight:700;
  display:flex;align-items:center;white-space:nowrap;opacity:0;transform-origin:center}}
.lst{{position:absolute;left:90px;top:300px;display:flex;gap:22px}}
.ci{{position:relative;width:84px;height:84px;border-radius:50%;border:5px solid {A.FIO};display:flex;align-items:center;justify-content:center}}
.ci .cn{{font-size:40px;font-weight:700;color:{A.MUTED};letter-spacing:-.02em}}
.ci .cv{{position:absolute;left:0;top:0;width:100%;height:100%;border-radius:50%;background:{A.BRAND};display:flex;align-items:center;justify-content:center;opacity:0}}
.ci.at{{border-color:{A.AMBER_BAR}}}
.ci.at .cn{{color:#8A6416}}
#s0 .lst{{top:1180px}}
#s0 .ci{{border-color:#3A443B;width:120px;height:120px}}
#s0 .ci .cn{{color:{MENTA};font-size:56px}}
.qq{{position:absolute;left:90px;top:430px;width:900px;font-size:100px;line-height:1;font-weight:700;letter-spacing:-.052em;color:{A.INK};text-wrap:balance}}
.qq .w{{display:inline-block;opacity:0}}
.qq b{{color:{A.BRAND_DARK};font-weight:700}}
.al{{position:absolute;left:90px;width:900px;opacity:0}}
.tx{{font-size:40px;font-weight:600;letter-spacing:-.02em;color:{A.INK}}}
.pc{{font-size:120px;font-weight:700;letter-spacing:-.05em;color:{CORAL};line-height:1;font-variant-numeric:tabular-nums}}
.pc small{{font-size:40px;font-weight:600;letter-spacing:-.01em;color:{A.MUTED};margin-left:14px}}
.br{{height:22px;border-radius:11px;background:{CORAL};width:0;margin-top:14px}}
.fo{{font-size:30px;font-weight:500;color:{A.MUTED};letter-spacing:-.01em;line-height:1.3}}
.ok{{display:flex;align-items:center;gap:22px;font-size:58px;font-weight:700;letter-spacing:-.04em;color:{A.BRAND_DARK};line-height:1.05}}
.ok i{{flex:none;width:76px;height:76px;border-radius:50%;background:{A.BRAND};display:flex;align-items:center;justify-content:center}}
.big2{{font-size:64px;font-weight:700;letter-spacing:-.045em;color:{A.INK};line-height:1.06;text-wrap:balance}}
.big2 b{{color:{A.BRAND_DARK}}}
.big2 em{{font-style:normal;color:{CORAL}}}
#trk{{position:absolute;left:90px;top:830px;width:900px;height:120px;border-radius:30px;background:{A.SOFT};border:5px solid {A.BRAND};overflow:hidden;opacity:0}}
#trk i{{position:absolute;top:0;height:100%;background:{CORAL};border-right:5px solid {A.SOFT};width:0}}
.lg{{display:flex;align-items:center;gap:20px;height:64px;font-size:40px;font-weight:600;letter-spacing:-.02em;color:{A.INK};opacity:0}}
.lg u{{flex:none;width:30px;height:30px;border-radius:9px;background:{CORAL}}}
.lg span{{color:{A.MUTED};font-weight:500}}
.lg b{{margin-left:auto;font-variant-numeric:tabular-nums}}
.nt{{position:absolute;left:96px;top:752px;font-size:26px;font-weight:500;color:{A.MUTED};opacity:0}}
"""

def gastos_html():
    return "".join(f'<div class="gs" id="gs{i}">{n}</div>' for i, (n, _, _) in enumerate(GASTOS))

def legenda():
    return "".join(f'<div class="lg" id="lg{i}"><u></u>{n} <span>· {d}</span><b>R$ {C.brl(float(v), 0)}</b></div>' for i, (n, d, v) in enumerate(CONTAS))

CORPO = f"""
<div class="cena papel" id="sq">
  {lista("lstQ")}
  <div class="lbl" id="lbl" style="position:absolute;left:520px;top:326px;font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{A.BRAND_DARK}"></div>

  {C.palavras_html("q1", "Tenho dívida cara?", (2,), "qq")}
  <div class="al" id="a1a" style="top:770px"><div class="tx">Rotativo do cartão</div><div class="pc">444,89%<small>ao ano</small></div><div class="br" id="b1a"></div></div>
  <div class="al" id="a1b" style="top:1035px"><div class="tx">Cheque especial</div><div class="pc">136,41%<small>ao ano</small></div><div class="br" id="b1b"></div></div>
  <div class="al fo" id="a1c" style="top:1290px">Taxas médias para pessoa física em agosto de 2026. Fonte: Banco Central.</div>
  <div class="al ok" id="a1d" style="top:1400px"><i>{check_svg()}</i>Se tiver, ela vem primeiro.</div>

  {C.palavras_html("q2", "Minha reserva cobre quantos meses?", (3, 4), "qq")}
  <div class="nt" id="n2">{K.NOTA}</div>
  {C.pop_html("p2", os.path.join(TELAS, ARQ["a"]))}
  <div class="al big2" id="a2a" style="top:1130px">No exemplo, <b>13,8 meses</b>.</div>
  <div class="al fo" id="a2b" style="top:1225px;font-size:38px">A meta padrão do Diagnóstico é de 6 meses.</div>

  {C.palavras_html("q3", "O que vence no começo do ano?", (4, 5, 6), "qq")}
  <div class="al tx" id="a3a" style="top:768px">2ª parcela do 13º, no exemplo: <b style="color:{A.BRAND_DARK}">R$ 2.433,36</b></div>
  <div id="trk"><i id="k0"></i><i id="k1"></i><i id="k2"></i></div>
  <div class="al" id="a3l" style="top:990px;opacity:1">{legenda()}</div>
  <div class="al big2" id="a3s" style="top:1220px"><em>R$ 2.391</em>: quase a 2ª parcela inteira.</div>
  <div class="al fo" id="a3f" style="top:1390px;font-size:36px">Em São Paulo, o IPTU vence a partir de fevereiro.</div>

  {C.palavras_html("q4", "Qual é o plano para o resto?", (3,), "qq")}
  <div class="nt" id="n4">{K.NOTA}</div>
  {C.pop_html("p4", os.path.join(TELAS, ARQ["b"]), C.anel_no_recorte("a4r", R_PEN, P_REC, [172, 748, 182, 32], 10))}
  <div class="al big2" id="a4a" style="top:1130px">Ela já está em Pendentes, <b>a receber em 18/12</b>.</div>
  <div class="al ok" id="a4b" style="top:1330px"><i>{check_svg()}</i>Dê um destino antes de cair.</div>
</div>

<div class="cena tinta" id="s0">
  <div class="tit" id="h1">Dezembro: o 13º some rápido.</div>
  <div class="tit" id="h2">Antes de gastar, <b>4 perguntas</b>.</div>
  <div id="rot0">2ª parcela do 13º, no exemplo</div>
  <div id="v0"><span class="rs">R$</span><span id="v0n">2.433</span><span class="ct" id="v0c">,36</span></div>
  {gastos_html()}
  {lista("lstH")}
</div>

{K.fim("Pendentes no timtimcash")}
"""

JS = f"""
const H1={H1}, H2={H2}, Q={Q}, T={T}, FIM={FIM};
const GASTOS={[[x, y] for _, x, y in GASTOS]};
const R_RES={R_RES}, R_PEN={R_PEN}, P_REC={P_REC};
const W3={[round(900 * float(v / PARC), 1) for _, _, v in CONTAS]};
function valorTxt(v){{ const s = fmt(v, 2).split(','); $('v0n').textContent = s[0]; $('v0c').textContent = ',' + s[1]; }}
function marca(pre, i, t, a){{ const c = $(pre+'c'+i); const p = pout(t, a, a+.35);
  c.querySelector('.cv').style.opacity = p; c.querySelector('.cv').style.transform = `scale(${{.6 + .4*pback(t, a, a+.4)}})`;
  const ck = c.querySelector('.ck'); ck.style.strokeDasharray = '1 1'; ck.style.strokeDashoffset = (1 - prog(t, a+.1, a+.45)).toFixed(3); }}
function render(t){{
  // gancho (tinta): o 13º escorre até zero enquanto os gastos saem; depois volta inteiro
  $('s0').style.transform = `translateY(${{-1920*prog(t, H2-.05, H2+.4)}}px)`;
  titulo('h1', t, -1, H1-.35); titulo('h2', t, H1, H2-.1);
  const esc = Math.pow(prog(t, .2, 1.55), 1.4), volta = pout(t, H1+.05, H1+.75);
  const v = 2433.36*(1 - esc) + 2433.36*volta*(t > H1 ? 1 : 0);
  valorTxt(Math.max(0, Math.min(2433.36, v)));
  $('v0').style.color = t < H1 ? (esc > .98 ? '{CORAL}' : '#fff') : '{MENTA}';
  const tr = t < 1.6 ? 3*esc*Math.sin(t*61) : 0; $('v0').style.transform = `translateX(${{tr}}px)`;
  GASTOS.forEach(([dx, dy], i) => {{ const a = .3 + .28*i, p = pout(t, a, a+.8);
    const e = $('gs'+i); e.style.opacity = Math.min(lin(t, a, a+.1), 1 - prog(t, a+.55, a+.8));
    e.style.transform = `translate(calc(-50% + ${{dx*p}}px), ${{dy*p}}px) scale(${{.7 + .3*p}})`; }});
  for (let i=0;i<4;i++){{ const e = $('lstHc'+i); e.style.opacity = pout(t, H1+.25+.12*i, H1+.6+.12*i);
    e.style.transform = `scale(${{.7 + .3*pback(t, H1+.25+.12*i, H1+.65+.12*i)}})`; }}
  // as perguntas (papel): a lista no topo marca cada resposta
  for (let i=0;i<4;i++){{ const c = $('lstQc'+i); c.className = 'ci' + (t >= T[i] && t < T[i]+Q-.45 ? ' at' : '');
    c.querySelector('.cn').style.opacity = 1; marca('lstQ', i, t, T[i]+Q-.55); }}
  const k = T.filter(a => t >= a).length; $('lbl').textContent = k ? `Pergunta ${{k}} de 4` : '';
  ['q1','q2','q3','q4'].forEach((id, i) => palavras(id, t, T[i]+.1, T[i]+Q-.3));
  // 1. dívida cara: as taxas médias do Banco Central, em coral (tensão), e o alívio
  some('a1a', t, T[0]+.55, T[1]-.3); some('a1b', t, T[0]+.75, T[1]-.3);
  $('b1a').style.width = (900*pout(t, T[0]+.7, T[0]+1.4))+'px'; $('b1b').style.width = (900*{float(CHE / ROT):.4f}*pout(t, T[0]+.9, T[0]+1.5))+'px';
  some('a1c', t, T[0]+1.0, T[1]-.3); some('a1d', t, T[0]+1.6, T[1]-.3);
  // 2. a reserva: a tela real do Diagnóstico
  some('n2', t, T[1]+.5, T[2]-.3, 10);
  recorte('p2', t, T[1]+.55, T[2]-.3, R_RES, [P_REC[0], P_REC[1]+80, P_REC[2], 1], P_REC, .5, false);
  some('a2a', t, T[1]+1.1, T[2]-.3); some('a2b', t, T[1]+1.35, T[2]-.3);
  // 3. o começo do ano: as contas enchem a 2ª parcela
  some('a3a', t, T[2]+.5, T[3]-.3, 16); some('trk', t, T[2]+.55, T[3]-.3, 16);
  let x = 0; W3.forEach((w, i) => {{ const e = $('k'+i); const p = pout(t, T[2]+.85+.3*i, T[2]+1.2+.3*i); e.style.left = x+'px'; e.style.width = (w*p)+'px'; x += w;
    some('lg'+i, t, T[2]+.85+.3*i, T[3]-.3, 14); }});
  some('a3s', t, T[2]+1.85, T[3]-.3); some('a3f', t, T[2]+2.1, T[3]-.3);
  // 4. o plano: a 2ª parcela já está em Pendentes
  some('n4', t, T[3]+.5, FIM-.1, 10);
  recorte('p4', t, T[3]+.55, FIM-.1, R_PEN, [P_REC[0], P_REC[1]+80, P_REC[2], 1], P_REC, .5, false);
  anel('a4r', t, T[3]+1.05, FIM-.1);
  some('a4a', t, T[3]+1.0, FIM-.1); some('a4b', t, T[3]+1.6, FIM-.1);
  sobe('fim', t, FIM);
}}
"""

# ---------------------------------------------------------------- capa da grade (tinta): o "4" enorme em menta
CAPA_CSS = f"""
.ce{{position:absolute;left:90px;top:440px}}
.c4{{position:absolute;left:52px;top:500px;height:800px;font-size:820px;line-height:800px;font-weight:700;letter-spacing:-.06em;color:{MENTA};
  font-variant-numeric:tabular-nums}}
.ct{{position:absolute;left:600px;top:760px;width:400px}}
.ct .h1{{font-size:92px;line-height:.98;color:#fff}}
.ct .h1 span{{color:{MENTA}}}
.cq{{position:absolute;left:90px;top:1300px;display:flex;gap:22px}}
.cq i{{width:84px;height:84px;border-radius:50%;border:6px solid #3A443B;display:flex;align-items:center;justify-content:center;
  font-style:normal;font-size:40px;font-weight:700;color:{MENTA}}}
"""
CAPA_CORPO = f"""
{K.logo("tinta")}
<div class="eyebrow ce">13º salário · dezembro</div>
<div class="c4">4</div>
<div class="ct"><div class="h1">perguntas antes de gastar o <span>13º</span></div></div>
<div class="cq"><i>1</i><i>2</i><i>3</i><i>4</i></div>
"""

HTML = C.pagina(CORPO, CSS, JS)
CAPA = K.pagina_capa(CAPA_CORPO, CAPA_CSS, fundo="tinta")

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
