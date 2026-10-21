# -*- coding: utf-8 -*-
"""Reel de 04/01/2027 (segunda) · "Comece 2027 · Passo 1 de 4: quanto você tem?" · capa verde · equipe jr.

Série "Comece 2027" (passo 1, O retrato), com o selo da equipe ja (equipes/ja/selo_comece2027.py, sem mudança).
- Gancho (papel): "Quanto você tem, somando tudo?" e uma soma que se monta: as 4 contas da conta de exemplo entram uma a
  uma e o total sobe até R$ 112.730,86 (Conta corrente R$ 18.230,86; Reserva R$ 22.974,60; Corretora no exterior
  R$ 60.000,00; Banco na Europa R$ 11.525,40), os números da tela "Contas e carteiras" de 04/01/2027.
  As contas lá fora entram pelo que custaram em reais (as remessas: 19.600 + 20.000 + 20.400 = 60.000; € 2.000 com IOF =
  R$ 11.525,40); o valor de hoje fica em Remessas. O vídeo diz isso numa nota curta e a legenda explica.
- Selo (tinta): COMECE 2027 · PASSO 1 DE 4, o selo 1 e "O retrato".
- Telas reais (captura_04.py, celular, relógio 04/01/2027 10:00, build 2026-10-19.5, cópia da conta sem mudança):
  Menu -> "Contas e carteiras" ("Patrimônio consolidado R$ 112.730,86" e as 4 contas) -> "Nova conta" preenchida pela
  interface com uma conta de exemplo ("Carteira", "Dinheiro / Carteira", "Saldo atual" R$ 150,00, "Incluir no
  patrimônio total" ligado), sem salvar: o patrimônio continua R$ 112.730,86.
- Fechamento verde: "Passo 1: o retrato. Contas e carteiras no timtimcash."

python3 reel_04.py  |  REEL_PREVIA="0 0.5 1 2.6 4.6 7 9 10.6 12.9 15.2 17 19.5" python3 reel_04.py
"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A
S = C.selo_ja()
assert S is not None, "selo da equipe ja não encontrado"

PASTA = "2027-01-04_reel-passo-1-quanto-voce-tem"
TRAB = C.trabalho("04")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas(PASTA)

# ---------------------------------------------------------------- números (conferidos contra a tela)
CONTAS = [("Conta corrente", "banco", D("18230.86")), ("Reserva", "reserva", D("22974.60")),
          ("Corretora no exterior", "globo", D("60000.00")), ("Banco na Europa", "globo", D("11525.40"))]
TOTAL = sum(v for _, _, v in CONTAS)
assert TOTAL == D("112730.86")
assert D("19600") + D("20000") + D("20400") == D("60000.00")          # as 3 remessas em dólar, em reais
assert D("11400.00") + D("125.40") == D("11525.40")                   # € 2.000 a R$ 5,70 e o IOF de 1,10%
TC = CX["c-contas-e-carteiras.jpg"]
assert "4 contas · todas no total do patrimônio" in TC["texto"] and "PATRIMÔNIO CONSOLIDADO\nR$ 112.730,86" in TC["texto"], TC["texto"]
for nome, _, v in CONTAS:
    linha = [l for l in TC["linhas"] if l[4].startswith(nome + " ")]
    assert len(linha) == 1 and linha[0][4].endswith("No total R$ " + C.brl(float(v))), (nome, linha)
assert CX["d-nova-conta-nome-8.jpg"]["nome_in"][4] == "Carteira"
assert CX["f-tipo-escolhido.jpg"]["tipo_txt"][4] == "Dinheiro / Carteira"
assert [CX[f"g-saldo-{i}.jpg"]["saldo_in"][4] for i in range(1, 6)] == ["R$ 0,01", "R$ 0,15", "R$ 1,50", "R$ 15,00", "R$ 150,00"]
assert CX["incl_ligado"] is True and CX["valores"] == {"nome": "Carteira", "tipo": "dinheiro", "saldo": "R$ 150,00"}
FORM = CX["h-pronto.jpg"]["texto"]
assert "Saldo atual\nquanto tem na conta hoje" in FORM and "Incluir no patrimônio total\no saldo soma ao total geral de contas" in FORM
assert "Jan 04 2027 10:0" in CX["relogio"] and not CX["erros"]
PARCIAIS = [sum(v for _, _, v in CONTAS[:k + 1]) for k in range(4)]
assert PARCIAIS == [D("18230.86"), D("41205.46"), D("101205.46"), D("112730.86")]

# ---------------------------------------------------------------- tempos (s)
L = [0.12, 0.72, 1.32, 1.92]          # cada conta pousa na soma
H_SAI = 3.75                           # o gancho sobe
S_SAI = 5.55                           # o selo sobe
T2, T3, T4, T5, T6 = (5.6, 9.5), (9.6, 11.45), (11.5, 14.3), (14.35, 16.2), (16.25, 18.1)
FIM = 18.15
DUR = round(FIM + 2.75, 2)
TQ_MENU, TQ_CONTAS, TQ_NOVA, TQ_NOME, TQ_TIPO, TQ_DIN, TQ_SALDO = 6.45, 7.25, 10.75, 11.65, 13.0, 13.75, 14.5
LETRAS = [round(11.85 + 0.1 * k, 2) for k in range(8)]
DIGITOS = [round(14.75 + 0.15 * k, 2) for k in range(5)]

# ---------------------------------------------------------------- caixas (px CSS da foto)
def cx(foto, k):
    return CX[foto][k][:4]
B_CONTAS = cx("b-menu.jpg", "contas")
TOT = cx("c-contas-e-carteiras.jpg", "total")
ROWS = C.uniao(*[l[:4] for l in TC["linhas"]])
NOVA = cx("c-contas-e-carteiras.jpg", "nova")
NOME_IN = cx("d-nova-conta-0.jpg", "nome_in")
TIPO = cx("f-tipo-escolhido.jpg", "tipo")
DIN = cx("e-tipo.jpg", "dinheiro")
SALDO, SALDO_IN = cx("h-pronto.jpg", "saldo"), cx("h-pronto.jpg", "saldo_in")
INCL = cx("h-pronto.jpg", "incl")
MENU = cx("a-visao-geral.jpg", "menu")

FOTOS = [("fa", "a-visao-geral.jpg"), ("fb0", "b0-menu-aberto.jpg"), ("fb", "b-menu.jpg"), ("fc", "c-contas-e-carteiras.jpg"), ("fd0", "d-nova-conta-0.jpg")] + \
        [(f"fd{i}", f"d-nova-conta-nome-{i}.jpg") for i in range(1, 9)] + [("fe", "e-tipo.jpg"), ("ff", "f-tipo-escolhido.jpg")] + \
        [(f"fg{i}", f"g-saldo-{i}.jpg") for i in range(1, 6)]
IDS = [i for i, _ in FOTOS]
# quando cada foto entra (troca seca, como a tela do site muda)
TROCAS = [(0, "fa"), (TQ_MENU + .15, "fb0"), (TQ_MENU + .5, "fb"), (TQ_CONTAS + .15, "fc"), (TQ_NOVA + .15, "fd0")] + \
         [(a, f"fd{i + 1}") for i, a in enumerate(LETRAS)] + [(TQ_TIPO + .15, "fe"), (TQ_DIN + .15, "ff")] + \
         [(a, f"fg{i + 1}") for i, a in enumerate(DIGITOS)]
CAM = [[0, 0, 195, 250, 1], [TQ_CONTAS + .2, TQ_CONTAS + .55, 195, 495, 1], [TQ_NOVA + .2, TQ_NOVA + .5, 195, 250, 1],
       [TQ_TIPO + .2, TQ_TIPO + .5, 195, 510, 1], [TQ_DIN + .2, TQ_DIN + .5, 195, 250, 1]]
EXTRA = K.aneis("aTot", "aRows", "aNova", "aTipo", "aSaldo", "aIncl") + K.toques("tMenu", "tContas", "tNova", "tNome", "tTipo", "tDin", "tSaldo")

# ---------------------------------------------------------------- gancho: a soma das contas
ICONES = {
    "banco": '<path d="M3.5 9.5h17M5.5 9.5v8M9.8 9.5v8M14.2 9.5v8M18.5 9.5v8M3.5 20h17M12 3.5l8.5 4.5h-17z"/>',
    "reserva": '<path d="M12 3.2l7.6 2.9v5.6c0 4.4-3.2 7.7-7.6 9.1-4.4-1.4-7.6-4.7-7.6-9.1V6.1z"/><path d="M8.8 12.2l2.2 2.2 4.3-4.4"/>',
    "globo": '<circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4c2.3 2.4 3.5 5.3 3.5 8.6s-1.2 6.2-3.5 8.6c-2.3-2.4-3.5-5.3-3.5-8.6S9.7 5.8 12 3.4z"/>',
}
def icone(k, tam=40, cor=A.BRAND_DARK):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="2.1" stroke-linecap="round" '
            f'stroke-linejoin="round">{ICONES[k]}</svg>')

Y0, PASSO = 584, 132
def linhas_html():
    out = []
    for i, (nome, ic, v) in enumerate(CONTAS):
        out.append(f'<div class="lc" id="lc{i}" style="top:{Y0 + i * PASSO}px"><i>{icone(ic, 42)}</i><span class="nm">{nome}</span>'
                   f'<span class="vl">{C.din(C.brl(float(v)))}</span></div>')
    return "".join(out)
Y_REGUA = Y0 + 4 * PASSO + 6

CSS = f"""
.tit{{font-size:64px}}
#h{{background:{A.BG}}}
#q{{position:absolute;left:90px;top:292px;width:900px;font-size:100px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#q b{{color:{A.BRAND_DARK};font-weight:700}}
.lc{{position:absolute;left:90px;width:900px;height:112px;border-radius:30px;background:#fff;border:2px solid {A.FIO};display:flex;align-items:center;
  padding:0 34px 0 18px;gap:24px;opacity:0;box-shadow:0 1px 2px rgba(15,20,16,.04),0 12px 28px -16px rgba(15,20,16,.16)}}
.lc i{{flex:none;width:72px;height:72px;border-radius:21px;background:{A.SOFT};display:flex;align-items:center;justify-content:center}}
.lc .nm{{font-size:42px;font-weight:600;letter-spacing:-.025em;color:{A.INK};white-space:nowrap}}
.lc .vl{{margin-left:auto;font-size:50px;font-weight:700;letter-spacing:-.03em;color:{A.INK}}}
.lc .vl .rs,.lc .vl .cts{{color:{A.MUTED}}}
#regua{{position:absolute;left:90px;top:{Y_REGUA}px;height:6px;border-radius:3px;background:{A.INK};width:0}}
#rot{{position:absolute;left:92px;top:{Y_REGUA + 44}px}}
#tot{{position:absolute;left:84px;top:{Y_REGUA + 92}px;font-size:150px;font-weight:700;letter-spacing:-.05em;line-height:1;color:{A.INK};transform-origin:0 70%}}
#tot .rs{{font-size:.36em;color:{A.MUTED};margin-right:.22em}}
#tot .cts{{font-size:.48em}}
#lafora{{position:absolute;left:92px;top:{Y_REGUA + 290}px;font-size:32px;font-weight:500;letter-spacing:-.01em;color:{A.MUTED};opacity:0}}
#s{{background:{A.INK}}}
#sSelo{{position:absolute;left:90px;top:640px;transform-origin:0 50%}}
#sEye{{position:absolute;left:92px;top:556px}}
#sNome{{position:absolute;left:90px;top:1010px;font-size:150px;line-height:1;font-weight:700;letter-spacing:-.055em;color:#fff}}
#sPerg{{position:absolute;left:94px;top:1190px;font-size:52px;font-weight:600;letter-spacing:-.03em;color:{K.DARK_TEXTO}}}
#sPerg b{{color:{A.MENTA};font-weight:700}}
"""

CORPO = f"""
<div class="cena papel" id="telas">
  <div class="tit" id="t2">Em <b>Contas e carteiras</b>, cada conta com o saldo de hoje.</div>
  <div class="tit" id="t3">Faltou alguma? Toque em <b>Nova conta</b>.</div>
  <div class="tit" id="t4">Dê um nome e escolha o <b>tipo</b>.</div>
  <div class="tit" id="t5"><b>Saldo atual</b>: quanto tem na conta hoje.</div>
  <div class="tit" id="t6"><b>Incluir no patrimônio total</b>: o saldo entra na soma.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", [(i, os.path.join(TELAS, f)) for i, f in FOTOS], EXTRA)}</div>
</div>

<div class="cena tinta" id="s">
  <div id="sEye">{S.eyebrow(1, "tinta", 32)}</div>
  <div id="sSelo">{S.selo(1, 330, "tinta")}</div>
  <div id="sNome">{S.NOMES[1]}.</div>
  <div id="sPerg">Quanto você tem, <b>somando tudo</b>?</div>
</div>

<div class="cena papel" id="h">
  <div id="q">Quanto você tem,<br><b>somando tudo?</b></div>
  {linhas_html()}
  <div id="regua"></div>
  <div class="eyebrow" id="rot">Patrimônio · 4 contas somadas</div>
  <div id="tot"><span class="rs">R$</span><span id="totI">0</span><span class="cts" id="totC">,00</span></div>
  <div id="lafora">Contas lá fora: entra o que custou em reais.</div>
</div>

{K.fim("Passo 1: o retrato. Contas e carteiras no timtimcash.")}
"""

JS = f"""
const L={L}, VAL={[float(v) for _, _, v in CONTAS]}, H_SAI={H_SAI}, S_SAI={S_SAI}, FIM={FIM};
const T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, T6={list(T6)};
const TROCAS={[[a, i] for a, i in TROCAS]}, IDS={IDS}, CAM={CAM};
const TQ={{menu:{TQ_MENU}, contas:{TQ_CONTAS}, nova:{TQ_NOVA}, nome:{TQ_NOME}, tipo:{TQ_TIPO}, din:{TQ_DIN}, saldo:{TQ_SALDO}}};
poeAnel('aTot', {TOT}, 10); poeAnel('aRows', {ROWS}, 10); poeAnel('aNova', {NOVA}, 10);
poeAnel('aTipo', {TIPO}, 8); poeAnel('aSaldo', {SALDO}, 8); poeAnel('aIncl', {INCL}, 8);
poeToque('tMenu', ...{C.centro(MENU)}); poeToque('tContas', ...{C.centro(B_CONTAS)}); poeToque('tNova', ...{C.centro(NOVA)});
poeToque('tNome', ...{C.centro(NOME_IN)}); poeToque('tTipo', ...{C.centro(TIPO)}); poeToque('tDin', ...{C.centro(DIN)});
poeToque('tSaldo', ...{C.centro(SALDO_IN)});
function total(v){{ const s = fmt(v, 2).split(','); $('totI').textContent = s[0]; $('totC').textContent = ',' + s[1]; }}
function render(t){{
  // 1. gancho: as contas entram e a soma sobe até o patrimônio
  let v = 0;
  VAL.forEach((x, i) => {{ const e = $('lc'+i), p = pout(t, L[i]-.3, L[i]+.12);
    e.style.opacity = lin(t, L[i]-.3, L[i]-.05); e.style.transform = `translateX(${{(1-p)*160}}px)`;
    v += x*pout(t, L[i], L[i]+.5); }});
  total(t >= L[3]+.5 ? {float(TOTAL)} : v);
  $('regua').style.width = (900*pout(t, -.2, L[3]+.3))+'px';
  const fimSoma = L[3]+.5, pulso = Math.sin(Math.PI*clamp((t-fimSoma)/.38, 0, 1));
  $('tot').style.transform = `scale(${{1 + .06*pulso}})`;
  $('tot').style.color = t >= fimSoma ? '{A.BRAND_DARK}' : '{A.INK}';
  aparece('lafora', t, 1.75, 0, 16, .4);
  $('q').style.transform = `translateY(${{-10*pout(t, 0, 1.2)}}px)`;
  saiCima('h', t, H_SAI);
  // 2. selo da série
  salta('sSelo', t, H_SAI+.2, .5); aparece('sEye', t, H_SAI+.3, 0, 20); aparece('sNome', t, H_SAI+.42, 0, 30); aparece('sPerg', t, H_SAI+.6, 0, 24);
  saiCima('s', t, S_SAI);
  // 3. telas reais
  titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  titulo('t5', t, T5[0], T5[1]); titulo('t6', t, T6[0], T6[1]);
  janela('janela', t, S_SAI+.05, FIM); janela('nota', t, S_SAI+.05, FIM);
  let atual = 'fa'; TROCAS.forEach(([a, id]) => {{ if (t >= a) atual = id; }}); so(IDS, IDS.indexOf(atual));
  camera('tela', t, CAM);
  toque('tMenu', t, TQ.menu); toque('tContas', t, TQ.contas);
  anel('aTot', t, TQ.contas+.75, TQ.contas+1.85); anel('aRows', t, TQ.contas+1.95, T2[1]-.05);
  anel('aNova', t, T3[0]+.2, TQ.nova-.05); toque('tNova', t, TQ.nova);
  toque('tNome', t, TQ.nome); toque('tTipo', t, TQ.tipo); toque('tDin', t, TQ.din);
  anel('aTipo', t, TQ.din+.6, T4[1]); toque('tSaldo', t, TQ.saldo);
  anel('aSaldo', t, {DIGITOS[-1]} + .25, T5[1]); anel('aIncl', t, T6[0]+.2, FIM-.05);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo("verde")}
  <div style="position:absolute;left:90px;top:430px">{S.eyebrow(1, "verde", 32)}</div>
  <div class="h1" style="position:absolute;left:90px;top:500px;width:900px;font-size:136px;line-height:.96;color:#fff">Quanto você tem?</div>
  <div style="position:absolute;left:0;top:860px;width:1080px;display:flex;justify-content:center">{S.selo_com_nome(1, 470, "verde", 70)}</div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


HTML = C.pagina(CORPO, CSS, JS)
CAPA = capa()

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
