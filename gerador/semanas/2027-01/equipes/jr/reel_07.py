# -*- coding: utf-8 -*-
"""Reel de 07/01/2027 (quinta) · "Lance na hora" · capa verde suave · equipe jr.

- Gancho (tinta): "O gasto que você não anota some." Um cronômetro dá a volta de 0 a 5 s enquanto o valor é digitado
  como no site, pelos centavos (R$ 0,01, 0,18, 1,85, 18,50), e termina com "Lançado".
- Telas reais (captura_07.py, celular, relógio 07/01/2027 10:00, build 2026-10-19.5, cópia da conta da equipe):
  Transações -> toque no "+" -> "Nova transação" já em "Despesa" -> valor tecla a tecla (R$ 18,50) -> descrição
  "Hortifruti" letra a letra: a categoria muda sozinha de "Alimentação" para "Mercado" com o selo "sugerida" ->
  "Já foi pago" ligado (como nasce) -> "Lançar despesa" -> aviso "Transação adicionada" -> a linha nova em Transações
  (quinta, 7 de janeiro: Hortifruti, Mercado, −R$ 18,50, paga). O resumo passa de "13 transações · 5 pagas" para
  "14 transações · 6 pagas". O lançamento só existe nesta captura (a conta de base não muda).
  Por que "Hortifruti" e não "padaria" (exemplo da pauta): "padaria" sugere "Alimentação", a categoria com que o formulário
  já abre, e o selo "sugerida" não aparece.
- Nota (papel): no computador, Cmd+Enter (ou Ctrl+Enter) lança (FUNCIONALIDADES.md; o botão diz "Lançar (Cmd+Enter)").
- Fechamento verde: "Lance na hora. Transações no timtimcash."

python3 reel_07.py  |  REEL_PREVIA="0 1 2.8 4.4 6.5 7.5 9.8 11.5 12.8 14.6 16.6 19" python3 reel_07.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A

PASTA = "2027-01-07_reel-lance-na-hora"
TRAB = C.trabalho("07")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas(PASTA)

# ---------------------------------------------------------------- conferência com a tela
VALORES = ["0,01", "0,18", "1,85", "18,50"]
DESC = "Hortifruti"
assert [CX[f"c-valor-{i}.jpg"]["valor_in"][4] for i in range(1, 5)] == VALORES
assert [CX[f"d-desc-{i:02d}.jpg"]["desc_in"][4] for i in range(1, 11)] == [DESC[:k] for k in range(1, 11)]
assert all(CX[f"d-desc-{i:02d}.jpg"]["cat"][4] == "Categoria Alimentação" for i in range(1, 10))   # até "Hortifrut"
assert CX["d-desc-10.jpg"]["cat"][4] == "Categoria Mercado sugerida"     # a palavra inteira: a sugestão chega (350 ms depois da tecla)
assert CX["form_estado"] == {"cat": "Mercado", "valor": "18,50", "desc": "Hortifruti", "sug": True}
assert "Categoria\nMercado sugerida" in CX["e-sugerida.jpg"]["texto"] and "Já foi pago\nAfeta o saldo real da conta agora" in CX["e-sugerida.jpg"]["texto"]
assert "Despesa" in CX["b-nova-0.jpg"]["despesa"][4] and "Hoje 07/01" in CX["b-nova-0.jpg"]["texto"]
assert CX["a-transacoes.jpg"]["resumo"][4] == "13 transações · 5 pagas · 8 pendentes · 774 no histórico"
assert CX["f-lancado.jpg"]["toast"][4] == "Transação adicionada"
assert CX["f-lancado.jpg"]["resumo"][4] == "14 transações · 6 pagas · 8 pendentes · 775 no histórico"
assert CX["g-transacoes-depois.jpg"]["linha_hortifruti"][4] == "Hortifruti Mercado · Conta corrente −R$ 18,50 paga"
assert CX["computador_title"] == ["Lançar (Cmd+Enter)", "Meta+Enter Control+Enter"]
assert "Jan 07 2027 10:0" in CX["relogio"] and not CX["erros"]

# ---------------------------------------------------------------- caixas (px CSS da foto)
def cx(foto, k):
    return CX[foto][k][:4]
FAB = cx("a-transacoes.jpg", "fab")
DESPESA = cx("b-nova-0.jpg", "despesa")
VALOR_Z, VALOR_IN = cx("b-nova-0.jpg", "valor"), cx("b-nova-0.jpg", "valor_in")
JAFOI = cx("b-nova-0.jpg", "jafoi")
CAT = cx("e-sugerida.jpg", "cat")
DESC_IN = cx("b-nova-0.jpg", "desc_in")
LANCAR = cx("b-nova-0.jpg", "lancar")
G = CX["g-transacoes-depois.jpg"]
LINHA = [G["linha_hortifruti"][0], round(G["linha_hortifruti"][1] - G["rolagem"], 1), G["linha_hortifruti"][2], G["linha_hortifruti"][3]]

# ---------------------------------------------------------------- tempos (s)
H_SAI = 3.25
T1, T2, T3, T4, T5, T6 = (3.35, 5.25), (5.3, 7.85), (7.9, 10.75), (10.8, 13.2), (13.25, 15.35), (15.45, 17.55)
TQ_FAB, TQ_VALOR, TQ_DESC, TQ_LANCAR = 4.45, 5.95, 8.05, 12.45
DIGS = [6.75, 6.92, 7.09, 7.26]          # depois da onda do toque, para ela não cobrir os números
LETRAS = [round(8.25 + 0.08 * k, 2) for k in range(10)]
SUGERE = 9.35
LISTA = 13.7
FIM = 17.6
DUR = round(FIM + 2.75, 2)

FOTOS = [("fa", "a-transacoes.jpg"), ("fb", "b-nova-0.jpg")] + [(f"fc{i}", f"c-valor-{i}.jpg") for i in range(1, 5)] + \
        [(f"fd{i}", f"d-desc-{i:02d}.jpg") for i in range(1, 11)] + [("fe", "e-sugerida.jpg"), ("ff", "f-lancado.jpg"), ("fg", "g-transacoes-depois.jpg")]
IDS = [i for i, _ in FOTOS]
TROCAS = [(0, "fa"), (TQ_FAB + .15, "fb")] + [(a, f"fc{i + 1}") for i, a in enumerate(DIGS)] + \
         [(a, f"fd{i + 1}") for i, a in enumerate(LETRAS)] + [(SUGERE, "fe"), (TQ_LANCAR + .15, "ff"), (LISTA, "fg")]
CAM = [[0, 0, 195, 500, 1], [TQ_FAB + .15, TQ_FAB + .5, 195, 350, 1], [11.75, 12.15, 195, 510, 1], [LISTA, LISTA + .35, 195, 250, 1]]
EXTRA = K.aneis("aDesp", "aValor", "aCat", "aJa", "aLinha") + K.toques("tFab", "tValor", "tDesc", "tLancar")

# ---------------------------------------------------------------- gancho: o cronômetro
R_CR, CX0, CY0 = 250, 540, 1060
CIRC = round(2 * 3.14159265 * R_CR, 1)
def marcas():
    out = []
    import math
    for k in range(60):
        a = math.radians(-90 + k * 6)
        r1 = R_CR + 44 if k % 12 == 0 else R_CR + 52
        r2 = R_CR + 64
        out.append(f'<line x1="{CX0 + r1 * math.cos(a):.1f}" y1="{CY0 + r1 * math.sin(a):.1f}" x2="{CX0 + r2 * math.cos(a):.1f}" y2="{CY0 + r2 * math.sin(a):.1f}" '
                   f'stroke="{"#5B665D" if k % 12 == 0 else "#2E3830"}" stroke-width="{6 if k % 12 == 0 else 4}" stroke-linecap="round"/>')
    return "".join(out)

CSS = f"""
.tit{{font-size:64px}}
#h{{background:{A.INK}}}
#q{{position:absolute;left:90px;top:292px;width:900px;font-size:100px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:#fff}}
#q b{{color:{A.MENTA};font-weight:700}}
#cr{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
#crVal{{position:absolute;left:90px;top:{CY0 - 82}px;width:900px;text-align:center;font-size:132px;font-weight:700;letter-spacing:-.045em;line-height:1;color:{A.CORAL}}}
#crVal .rs{{font-size:.42em;color:{K.DARK_TEXTO};margin-right:.25em;font-weight:600}}
#crVal .cts{{font-size:1em;font-weight:700}}
#crRot{{position:absolute;left:90px;top:{CY0 + 70}px;width:900px;text-align:center;font-size:40px;font-weight:600;letter-spacing:-.01em;color:{K.DARK_TEXTO}}}
#crSeg{{position:absolute;left:90px;top:{CY0 - 196}px;width:900px;text-align:center;font-size:44px;font-weight:700;letter-spacing:-.02em;color:#fff;font-variant-numeric:tabular-nums}}
#ok{{position:absolute;left:90px;top:{CY0 + R_CR + 110}px;width:900px;display:flex;justify-content:center;opacity:0}}
#ok span{{display:inline-flex;align-items:center;gap:18px;height:96px;padding:0 44px;border-radius:999px;background:{A.MENTA};color:{A.INK};font-size:44px;font-weight:700;letter-spacing:-.02em}}
#teclas{{position:absolute;left:90px;top:760px;width:900px;display:flex;align-items:center;justify-content:center;gap:36px;opacity:0}}
.tc{{display:flex;flex-direction:column;justify-content:flex-end;align-items:flex-start;height:200px;padding:0 34px 26px;border-radius:34px;background:#fff;
  border:3px solid {A.NEUTRO};box-shadow:0 12px 0 {A.NEUTRO},0 26px 40px -18px rgba(15,20,16,.35);font-size:60px;font-weight:700;letter-spacing:-.03em;color:{A.INK}}}
.tc small{{font-size:44px;font-weight:600;color:{A.MUTED};margin-bottom:6px;line-height:1}}
#tcCmd{{width:250px}}
#tcEnter{{width:330px}}
.mais{{font-size:80px;font-weight:600;color:{A.MUTED}}}
#ctrl{{position:absolute;left:90px;top:1060px;width:900px;text-align:center;font-size:44px;font-weight:600;letter-spacing:-.02em;color:{A.MUTED};opacity:0}}
#ctrl b{{color:{A.INK};font-weight:700}}
#lancou{{position:absolute;left:90px;top:1200px;width:900px;display:flex;justify-content:center;opacity:0}}
#lancou span{{display:inline-flex;align-items:center;gap:18px;height:96px;padding:0 44px;border-radius:999px;background:{A.SOFT};color:{A.BRAND_DEEP};font-size:44px;font-weight:700;letter-spacing:-.02em}}
"""

def check(cor, tam=46, traco=3.2):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" stroke-linecap="round" '
            f'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')

CORPO = f"""
<div class="cena papel" id="telas">
  <div class="tit" id="t1">Toque no <b>+</b>.</div>
  <div class="tit" id="t2"><b>Despesa</b>: digite o valor.</div>
  <div class="tit" id="t3">Escreva o que foi: a categoria vem <b>sugerida</b>.</div>
  <div class="tit" id="t4"><b>Já foi pago</b> fica ligado. Toque em <b>Lançar despesa</b>.</div>
  <div class="tit" id="t5">Pronto: já está em <b>Transações</b>.</div>
  <div class="tit" id="t6">No computador, <b>Cmd+Enter</b> lança.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", [(i, os.path.join(TELAS, f)) for i, f in FOTOS], EXTRA)}</div>
  <div id="teclas"><div class="tc" id="tcCmd"><small>⌘</small>Cmd</div><span class="mais">+</span><div class="tc" id="tcEnter"><small>↵</small>Enter</div></div>
  <div id="ctrl">Ou <b>Ctrl+Enter</b>.</div>
  <div id="lancou"><span>{check(A.BRAND_DARK, 44)}Lança ou salva a transação</span></div>
</div>

<div class="cena tinta" id="h">
  <div id="q">O gasto que você não anota <b>some</b>.</div>
  <svg id="cr" viewBox="0 0 1080 1920">
    {marcas()}
    <rect x="{CX0 - 46}" y="{CY0 - R_CR - 128}" width="92" height="40" rx="14" fill="#2E3830"/>
    <rect x="{CX0 - 16}" y="{CY0 - R_CR - 92}" width="32" height="34" fill="#2E3830"/>
    <circle cx="{CX0}" cy="{CY0}" r="{R_CR}" fill="none" stroke="#1F2820" stroke-width="30"/>
    <circle id="arco" cx="{CX0}" cy="{CY0}" r="{R_CR}" fill="none" stroke="{A.MENTA}" stroke-width="30" stroke-linecap="round"
      transform="rotate(-90 {CX0} {CY0})" stroke-dasharray="{CIRC} {CIRC}" stroke-dashoffset="{CIRC}"/>
  </svg>
  <div id="crSeg">0 s</div>
  <div id="crVal"><span class="rs">R$</span><span id="crNum">0,00</span></div>
  <div id="crRot">Hortifruti · Mercado</div>
  <div id="ok"><span>{check(A.INK, 46)}Lançado</span></div>
</div>

{K.fim("Lance na hora. Transações no timtimcash.")}
"""

JS = f"""
const H_SAI={H_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, T6={list(T6)}, FIM={FIM};
const TROCAS={[[a, i] for a, i in TROCAS]}, IDS={IDS}, CAM={CAM}, CIRC={CIRC};
const VALS={VALORES}, TV=[0.25, 0.55, 0.85, 1.15];
poeAnel('aDesp', {DESPESA}, 8); poeAnel('aValor', {VALOR_Z}, 6); poeAnel('aCat', {CAT}, 6); poeAnel('aJa', {JAFOI}, 6); poeAnel('aLinha', {LINHA}, 8);
poeToque('tFab', ...{C.centro(FAB)}); poeToque('tValor', {round(VALOR_Z[0] + VALOR_Z[2] / 2, 1)}, {round(VALOR_Z[1] + VALOR_Z[3] - 26, 1)}); poeToque('tDesc', ...{C.centro(DESC_IN)}); poeToque('tLancar', ...{C.centro(LANCAR)});
function tecla(id, t, a){{ const p = Math.sin(Math.PI*clamp((t-a)/.28, 0, 1)); $(id).style.transform = `translateY(${{10*p}}px)`;
  $(id).style.boxShadow = `0 ${{12-10*p}}px 0 {A.NEUTRO}, 0 26px 40px -18px rgba(15,20,16,${{.35-.2*p}})`; }}
function render(t){{
  // 1. gancho: o cronômetro dá a volta (0 a 5 s) enquanto o valor é digitado pelos centavos
  const p = prog(t, 0, 2.45);
  $('arco').setAttribute('stroke-dashoffset', (CIRC*(1-p)).toFixed(1));
  $('crSeg').textContent = Math.min(5, Math.floor(p*5 + 1e-6)) + ' s';
  let k = -1; TV.forEach((a, i) => {{ if (t >= a) k = i; }});
  $('crNum').textContent = k < 0 ? '0,00' : VALS[k];
  $('crVal').style.transform = `scale(${{k >= 0 ? 1 + .05*Math.exp(-(t-TV[k])*12) : 1}})`;
  aparece('crRot', t, 1.45, 0, 16, .35);
  const ok = pback(t, 2.5, 2.9); $('ok').style.opacity = lin(t, 2.5, 2.62); $('ok').style.transform = `scale(${{.7 + .3*ok}})`;
  saiCima('h', t, H_SAI);
  // 2. telas reais
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]); titulo('t6', t, T6[0], T6[1]);
  janela('janela', t, H_SAI+.05, T5[1]); janela('nota', t, H_SAI+.05, T5[1]);
  let atual = 'fa'; TROCAS.forEach(([a, id]) => {{ if (t >= a) atual = id; }}); so(IDS, IDS.indexOf(atual));
  camera('tela', t, CAM);
  toque('tFab', t, {TQ_FAB});
  anel('aDesp', t, T2[0]+.15, {TQ_VALOR}-.05); toque('tValor', t, {TQ_VALOR}); anel('aValor', t, {DIGS[-1]}+.12, T2[1]);
  toque('tDesc', t, {TQ_DESC}); anel('aCat', t, {SUGERE}+.15, T3[1]);
  anel('aJa', t, T4[0]+.15, 11.7); toque('tLancar', t, {TQ_LANCAR});
  if (t >= {TQ_LANCAR}+.2){{ $('t_tLancar').style.opacity = 0; $('o_tLancar').style.opacity = 0; }}   // a folha fechou: o toque some junto
  anel('aLinha', t, {LISTA}+.4, T5[1]-.05);
  // 3. no computador
  aparece('teclas', t, T6[0]+.1, FIM-.05, 40, .45); tecla('tcCmd', t, T6[0]+.7); tecla('tcEnter', t, T6[0]+.8);
  aparece('ctrl', t, T6[0]+.45, FIM-.05, 24); aparece('lancou', t, T6[0]+1.05, FIM-.05, 24);
  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo("suave")}
  <div class="eyebrow" style="position:absolute;left:90px;top:430px">Transações</div>
  <div class="h1" style="position:absolute;left:90px;top:494px;width:900px;font-size:132px;line-height:.96;color:{A.INK}">Lance em <span style="color:{A.BRAND_DARK}">5 segundos.</span></div>
  <svg style="position:absolute;left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">
    <circle cx="540" cy="1215" r="300" fill="none" stroke="{A.MENTA_CLARA}" stroke-width="10"/>
    <circle cx="540" cy="1215" r="250" fill="none" stroke="{A.MENTA}" stroke-width="12"/>
    <circle cx="540" cy="1215" r="196" fill="{A.BRAND}"/>
    <path d="M540 1125v180M450 1215h180" stroke="#fff" stroke-width="30" stroke-linecap="round"/>
  </svg>"""
    return K.pagina_capa(corpo, "", fundo="suave")


HTML = C.pagina(CORPO, CSS, JS)
CAPA = capa()

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
