# -*- coding: utf-8 -*-
"""Reel de 27/02/2027 (sábado) · "O dia 10 de março" · capa tinta · equipe fs.

Telas reais: captura_27.py, build 2026-10-19.5, celular 390 × 1000 em escala 3, conta fictícia de base (cópia da equipe,
estado.py sem mudança), relógio da página em 27/02/2027 10:00. Pendentes de fevereiro ("Tudo em dia") -> "Próximo" ->
Março 2027 ("A pagar R$ 4.444,80 · 7 transações"; no grupo 10/03/2027: Aluguel −R$ 2.300,00, Escola −R$ 1.450,00 e
IPTU 2027 · 2ª parcela −R$ 215,00; em 05/03, Salário +R$ 9.960,00) -> calendário -> 10 e 10 -> "Aplicar" ("10 mar 2027":
"A pagar R$ 3.965 · 3 transações"). Conta: 2.300 + 1.450 + 215 = 3.965.
"Até novembro": na mesma captura, Pendentes do "Ano atual" mostram nos dias 10 de março a novembro as mesmas três contas
(IPTU da 2ª à 10ª parcela, R$ 215 cada) e, em 10/12, só aluguel e escola (conferido abaixo com assert, foto de conferência
que não entra no vídeo).

python3 reel_27.py  |  REEL_PREVIA="0 0.5 1 3 4.6 6.5 8.8 11.2 12.8 14.8 16 18" python3 reel_27.py
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro, folga, din, MENOS

PASTA = "2027-02-27_reel-o-dia-10-de-marco"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("27")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- conferência com a tela
c1, c2, c3 = C["celular-pendentes-1-fevereiro.jpg"], C["celular-pendentes-2-marco.jpg"], C["celular-pendentes-3-calendario.jpg"]
c4, c5, c6 = C["celular-pendentes-4-dia-10-inicio.jpg"], C["celular-pendentes-5-dia-10.jpg"], C["celular-pendentes-6-so-o-dia-10.jpg"]
assert "Fevereiro 2027" in c1["texto"] and "Tudo em dia" in c1["texto"]
t2 = c2["texto"]
assert "Março 2027" in t2 and "A pagar\nR$\n4.444\n,80\n7 transações" in t2 and "A receber\nR$\n9.960" in t2
G = c2["linhas"]["grupos"]
dia10 = G["10/03/2027"]["itens"]
assert [i["texto"] for i in dia10] == ["Editar Excluir Aluguel FIXA·Casa·Conta corrente −R$ 2.300,00 pendente",
                                       "Editar Excluir Escola FIXA·Educação·Conta corrente −R$ 1.450,00 pendente",
                                       "Editar Excluir IPTU 2027 · 2ª parcela Impostos e Taxas·Conta corrente −R$ 215,00 pendente"]
sal = G["EM 6 DIAS · 05/03/2027"]["itens"]
assert [i["texto"] for i in sal] == ["Editar Excluir Salário FIXA·Salário·Conta corrente +R$ 9.960,00 pendente"]
assert 2300 + 1450 + 215 == 3965
assert "1 mar 2027 a 31 mar 2027" in c3["texto"] and "10 mar 2027 a 10 mar 2027" in c5["texto"] and "Início: 10 mar 2027" in c4["texto"]
t6 = c6["texto"]
assert t6.startswith("Pendentes\n10 mar 2027") and "A pagar\nR$\n3.965\n3 transações" in t6
assert len(c6["linhas"]["grupos"]) == 1 and len(c6["linhas"]["grupos"]["10/03/2027"]["itens"]) == 3
# o dia 10 de março a novembro (Pendentes do ano 2027, foto de conferência)
GA = C["conferencia-pendentes-ano-2027.jpg"]["linhas"]["grupos"]
for k, mes in enumerate(range(3, 12), 2):
    its = [i["texto"] for i in GA[f"10/{mes:02d}/2027"]["itens"]]
    assert its[0].endswith("Aluguel FIXA·Casa·Conta corrente −R$ 2.300,00 pendente") and its[1].endswith("Escola FIXA·Educação·Conta corrente −R$ 1.450,00 pendente")
    assert its[2].endswith(f"IPTU 2027 · {k}ª parcela Impostos e Taxas·Conta corrente −R$ 215,00 pendente") and len(its) == 3, (mes, its)
assert len(GA["10/12/2027"]["itens"]) == 2
assert "Feb 27 2027" in C["relogio"]

# ---------------------------------------------------------------- caixas (px CSS do celular)
PROX = c1["proximo"]
APAGAR = c2["apagar"]
GRUPO10 = G["10/03/2027"]["caixa"]
SAL = sal[0]["caixa"]
PILULA = c2["pilula"]
DIA10 = C["dia10"][:4]
APLICAR = c5["aplicar"]
APAGAR6 = c6["apagar"]

# ---------------------------------------------------------------- tempos (s)
H_SAI = 2.75
T1, T2, T3, T4 = (2.95, 5.25), (5.4, 7.6), (7.75, 9.75), (9.9, 13.35)
TQ_PROX = 3.75
TQ_PIL, TQ_D1, TQ_D2, TQ_APL = 10.4, 11.05, 11.5, 12.1
J_SAI = 13.35
S5 = 13.55
FIM = 16.75
DUR = 19.5

IMGS = [("i1", tela("celular-pendentes-1-fevereiro.jpg")), ("i2", tela("celular-pendentes-2-marco.jpg")),
        ("i3", tela("celular-pendentes-3-calendario.jpg")), ("i4", tela("celular-pendentes-4-dia-10-inicio.jpg")),
        ("i5", tela("celular-pendentes-5-dia-10.jpg")), ("i6", tela("celular-pendentes-6-so-o-dia-10.jpg"))]
TR = [0, TQ_PROX + .15, TQ_PIL + .15, TQ_D1 + .15, TQ_D2 + .15, TQ_APL + .15]
EXTRA = K.aneis("aPagar", "aGrupo", "aSal", "aDia10") + K.toques("tqProx", "tqPil", "tqD1", "tqD2", "tqApl")

# ---------------------------------------------------------------- gancho: março de 2027 (domingo primeiro, como o calendário do site)
CEL, VAO, CX0, CY0 = 104, 12, 140, 820          # célula, vão, canto da grade
SEM = ["D", "S", "T", "Q", "Q", "S", "S"]
DIAS = [28] + list(range(1, 32)) + [1, 2, 3]     # 28/02, março inteiro, 1 a 3 de abril
def cel_xy(i):
    return CX0 + (i % 7) * (CEL + VAO), CY0 + 64 + (i // 7) * (CEL + VAO)
cab = "".join(f'<span class="cs" style="left:{CX0 + k * (CEL + VAO)}px;top:{CY0}px">{d}</span>' for k, d in enumerate(SEM))
cels = []
for i, d in enumerate(DIAS):
    x, y = cel_xy(i)
    outro = i == 0 or i > 31
    cls = "cd outro" if outro else ("cd dez" if d == 10 and not outro else "cd")
    ident = ' id="c10"' if (d == 10 and not outro) else ""
    cels.append(f'<span class="{cls}"{ident} style="left:{x}px;top:{y}px">{d}</span>')
I10 = DIAS.index(10)
X10, Y10 = cel_xy(I10)
CHIPS = [("Aluguel", "2.300"), ("Escola", "1.450"), ("IPTU", "215")]
CHX = [90, 382, 668]            # x de cada etiqueta na fila, acima do calendário (y 690)
chips = '<div id="chs">' + "".join(f'<div class="ch" id="ch{k}"><b>{n}</b><span>R$ {v}</span></div>' for k, (n, v) in enumerate(CHIPS)) + "</div>"

# ---------------------------------------------------------------- cena 5: o dia 10 de março a novembro
MESES = ["mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov"]
TW, TH, TG = 268, 200, 22
def tile_xy(k):
    return 90 + (k % 3) * (TW + TG), 760 + (k // 3) * (TH + TG)
tiles = "".join(f'<div class="tl" id="tl{k}" style="left:{tile_xy(k)[0]}px;top:{tile_xy(k)[1]}px"><i>{m}</i><b>10</b><span>R$ 3.965</span></div>'
                for k, m in enumerate(MESES))

CSS = f"""
.tit{{font-size:64px}}
/* gancho */
#g .eyebrow{{position:absolute;left:90px;top:300px}}
#gNum{{position:absolute;left:84px;top:345px;font-size:180px;font-weight:700;letter-spacing:-.055em;line-height:1;color:{A.INK};white-space:nowrap}}
#gNum .rs{{font-size:.36em;color:{A.MUTED};margin-right:.2em}}
#gSub{{position:absolute;left:90px;top:548px;font-size:88px;font-weight:700;letter-spacing:-.05em;line-height:1;color:{A.INK}}}
#gSub b{{color:{K.CORAL_TXT}}}
.cs{{position:absolute;width:{CEL}px;text-align:center;font-size:30px;font-weight:700;color:{A.MUTED}}}
.cd{{position:absolute;width:{CEL}px;height:{CEL}px;border-radius:22px;background:#fff;border:3px solid {A.FIO};display:flex;align-items:center;justify-content:center;
  font-size:40px;font-weight:600;color:{A.INK};font-variant-numeric:tabular-nums}}
.cd.outro{{background:transparent;border-color:transparent;color:#B9B6AB;font-weight:500}}
.cd.dez{{z-index:2}}
#chs{{position:absolute;left:90px;top:690px;width:900px;display:flex;gap:14px;z-index:3}}
.ch{{position:relative;display:flex;gap:12px;height:76px;padding:0 24px;border-radius:999px;
  background:{A.INK};color:#fff;white-space:nowrap;opacity:0;align-items:center}}
.ch b{{font-size:31px;font-weight:700;letter-spacing:-.02em}}
.ch span{{font-size:31px;font-weight:600;color:{A.MENTA};font-variant-numeric:tabular-nums}}
#gQ{{position:absolute;left:90px;top:1496px;width:900px;font-size:48px;font-weight:600;letter-spacing:-.025em;color:{A.INK};opacity:0}}
#gQ b{{color:{A.BRAND_DARK}}}
/* cena 5 */
#s5 .h2{{position:absolute;left:90px;top:300px;width:900px;font-size:92px;line-height:1.0;color:#fff}}
#s5 .h2 b{{color:{A.MENTA}}}
.tl{{position:absolute;width:{TW}px;height:{TH}px;border-radius:30px;background:#192019;border:2px solid #262E27;overflow:hidden;opacity:0}}
.tl i{{position:absolute;left:0;top:0;width:100%;height:52px;background:#262E27;font-style:normal;font-size:28px;font-weight:700;letter-spacing:.12em;
  text-transform:uppercase;color:{K.DARK_TEXTO};display:flex;align-items:center;justify-content:center}}
.tl b{{position:absolute;left:0;top:58px;width:100%;text-align:center;font-size:76px;font-weight:700;letter-spacing:-.04em;color:#fff;line-height:1}}
.tl span{{position:absolute;left:0;bottom:20px;width:100%;text-align:center;font-size:34px;font-weight:700;color:{A.MENTA};font-variant-numeric:tabular-nums}}
.tl.on{{border-color:{A.MENTA}}}
#s5n{{position:absolute;left:90px;top:1440px;width:900px;font-size:44px;line-height:1.25;font-weight:600;color:#fff;letter-spacing:-.02em;opacity:0}}
#s5n span{{color:{K.DARK_TEXTO};font-weight:500}}
"""

CORPO = f"""
<div class="cena papel" id="cenaTela">
  <div class="tit" id="t1">Fevereiro está em dia? <b>Olhe março.</b></div>
  <div class="tit" id="t2">No dia 10: <b>aluguel, escola e IPTU.</b></div>
  <div class="tit" id="t3">O salário entra antes, <b>no dia 5.</b></div>
  <div class="tit" id="t4">Só o dia 10: <b>R$ 3.965</b> a pagar.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA, 390, 1000)}</div>
</div>

<div class="cena tinta" id="s5" style="transform:translateY(1920px)">
  <div class="h2">Até novembro, todo dia 10 pede <b>R$ 3.965</b>.</div>
  {tiles}
  <div id="s5n">Veja antes e deixe o saldo pronto. <span>O IPTU do exemplo vai até a 10ª parcela, em 10/11.</span></div>
</div>

<div class="cena papel" id="g">
  <div class="eyebrow">10 de março</div>
  <div id="gNum"><span class="rs">R$</span>3.965</div>
  <div id="gSub">no <b>mesmo dia.</b></div>
  {cab}
  {"".join(cels)}
  {chips}
  <div id="gQ">Seu saldo está <b>pronto?</b></div>
</div>

{K.fim("Pendentes no timtimcash")}
"""

JS = f"""
const H_SAI={H_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, J_SAI={J_SAI}, S5={S5}, FIM={FIM};
const TQ_PROX={TQ_PROX}, TQ_PIL={TQ_PIL}, TQ_D1={TQ_D1}, TQ_D2={TQ_D2}, TQ_APL={TQ_APL}, TR={TR};
const CHX={CHX}, X10={X10}, Y10={Y10}, CEL={CEL};
poeAnel('aPagar', {folga(APAGAR, 2)}, 8); poeAnel('aGrupo', {folga(GRUPO10, 2)}, 6); poeAnel('aSal', {folga(SAL, 2)}, 6); poeAnel('aDia10', {folga(DIA10, 3)}, 6);
poeToque('tqProx', ...{centro(PROX)}); poeToque('tqPil', ...{centro(PILULA)}); poeToque('tqD1', ...{centro(DIA10)});
poeToque('tqD2', ...{centro(DIA10)}); poeToque('tqApl', ...{centro(APLICAR)});
// câmera: [_, _, fx, fy, zoom] em px CSS do celular (a janela mostra 390 × 500 px CSS com zoom 1)
const FY_TOPO = 250, FY_10 = {round(GRUPO10[1] + GRUPO10[3] / 2 - 40, 1)}, FY_CAL = {round(DIA10[1] + 110, 1)}, FY_APL = 750;
const CAM = [[0,0,195,FY_TOPO,1], [5.4,5.95,195,FY_10,1], [9.9,10.3,195,FY_TOPO,1], [10.45,10.9,195,FY_CAL,1], [11.6,11.95,195,FY_APL,1], [12.15,12.42,195,FY_TOPO,1]];
function render(t){{
  // 1. gancho: março, o dia 10 pulsa e as três contas caem nele
  const g = prog(t, H_SAI, H_SAI+.45); $('g').style.transform = `translateY(${{-1920*g}}px)`;
  $('gNum').style.transform = `translateY(${{-16*pout(t,0,1.6)}}px)`;
  const c10 = $('c10'); const pul = Math.sin(Math.PI*clamp((t-.88)/.45,0,1));
  const cheio = t >= .88; c10.style.background = cheio ? '{A.CORAL}' : '#fff'; c10.style.color = cheio ? '#fff' : '{A.INK}';
  c10.style.borderColor = cheio ? '{A.CORAL}' : '{A.FIO}'; c10.style.transform = `scale(${{1 + .22*pul + .06*Math.sin(Math.max(0,t-1.4)*5.5)*(t>1.4?1:0)}})`;
  // as etiquetas entram na fila (já no 1º quadro) e caem, uma a uma, no dia 10
  CHX.forEach((x, k) => {{ const a = -.3 + .12*k, p = pout(t, a, a+.4), v = prog(t, .55+.14*k, .9+.14*k);
    const e = $('ch'+k), w = e.offsetWidth, dx = (X10 + CEL/2 - w/2 - 90 - e.offsetLeft)*v, dy = (Y10 + CEL/2 - 38 - 690)*v;
    e.style.opacity = Math.min(lin(t, a, a+.12), 1 - prog(t, .8+.14*k, .92+.14*k));
    e.style.transform = `translate(${{dx}}px, ${{dy + 30*(1-p)}}px) scale(${{1 - .6*v}})`; }});
  $('gQ').style.opacity = prog(t, .25, .55); $('gQ').style.transform = `translateY(${{16*(1-pout(t,.25,.7))}}px)`;
  // 2. a tela real: Pendentes de fevereiro e março, o dia 10 e o salário, o calendário
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, H_SAI+.15, J_SAI);
  const ne = prog(t, H_SAI+.15, H_SAI+.75); $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(['i1','i2','i3','i4','i5','i6'], t, TR);
  toque('tqProx', t, TQ_PROX); anel('aPagar', t, 4.3, 5.2);
  anel('aGrupo', t, 6.0, 7.55); anel('aSal', t, 7.95, 9.7);
  toque('tqPil', t, TQ_PIL); toque('tqD1', t, TQ_D1); toque('tqD2', t, TQ_D2); toque('tqApl', t, TQ_APL);
  anel('aDia10', t, TQ_D2+.2, TQ_APL-.15); anel('aPagar', t, t < 9 ? 4.3 : 12.65, t < 9 ? 5.2 : 13.3);
  // 3. até novembro (tinta)
  sobe('s5', t, S5);
  for (let k=0;k<9;k++){{ const a = S5+.45+.11*k, e = $('tl'+k); e.style.opacity = lin(t, a, a+.15);
    e.style.transform = `translateY(${{(1-pback(t, a, a+.42))*50}}px)`; e.className = 'tl' + (t >= a+.25 ? ' on' : ''); }}
  $('s5n').style.opacity = prog(t, S5+1.6, S5+2.0);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    cs = 92; vg = 12; x0, y0 = 120, 1000
    grade = "".join(
        f'<span style="position:absolute;left:{x0 + (i % 7) * (cs + vg)}px;top:{y0 + (i // 7) * (cs + vg)}px;width:{cs}px;height:{cs}px;border-radius:20px;'
        f'display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:600;font-variant-numeric:tabular-nums;'
        + (f'background:{A.CORAL};color:#fff;font-weight:700;transform:scale(1.18);box-shadow:0 0 0 8px rgba(217,119,87,.25)' if d == 10 and 0 < i < 32
           else ('color:#5B635A' if (i == 0 or i > 31) else f'background:#192019;color:{K.DARK_TEXTO}'))
        + f'">{d}</span>' for i, d in enumerate(DIAS[:35]))
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">10 de março</div>
    <div class="h1" style="font-size:132px;line-height:.95;margin-top:34px;color:#fff"><span style="color:{A.MENTA}">R$ 3.965</span> no mesmo dia.</div>
  </div>
  {grade}"""
    return K.pagina_capa(corpo, "", fundo="tinta")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
