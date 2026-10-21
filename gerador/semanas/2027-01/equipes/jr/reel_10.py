# -*- coding: utf-8 -*-
"""Reel de 10/01/2027 (domingo) · "Comece 2027 · Passo 2 de 4: para onde vai?" · capa verde suave · equipe jr.

Série "Comece 2027" (passo 2, O caminho), com o selo da equipe ja (equipes/ja/selo_comece2027.py, sem mudança).
- Gancho (verde suave): "Para onde foi o seu dinheiro em janeiro?" e as 3 maiores categorias do mês até 10/01, lidas
  na tela, em barras que crescem: Casa R$ 2.300,00, Educação R$ 1.450,00, Mercado R$ 402,30 (de R$ 4.820,00 em
  6 categorias).
- Selo (tinta): COMECE 2027 · PASSO 2 DE 4, o selo 2 e "O caminho".
- Telas reais (captura_10.py, celular, relógio 10/01/2027 10:00, build 2026-10-19.5, conta sem mudança):
  Visão geral (Realizado, Janeiro 2027), a câmera desce até "Por categoria" (rosca "Despesas R$ 4.820,00 ·
  6 categorias") e "Top saídas" (Casa 48%, Educação 30%, Mercado 8%, Transporte 8%, Bares e restaurantes 4%, Saúde 1%);
  toque em "Educação" -> Transações filtrada: "2 transações · 1 paga · 1 pendente · somam R$ 2.390,00": a escola
  (R$ 1.450,00, paga em 10/01) e o material escolar (R$ 940,00, pendente, vence em 12/01).
- A mensagem: categoria certa no lançamento é o que faz o gráfico dizer a verdade.
- Fechamento verde: "Passo 2: o caminho. Visão geral no timtimcash."

python3 reel_10.py  |  REEL_PREVIA="0 0.5 1 3 4.6 6.6 7.5 9.3 11.7 13.9 16.2 18.6" python3 reel_10.py
"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A
S = C.selo_ja()
assert S is not None, "selo da equipe ja não encontrado"

PASTA = "2027-01-10_reel-passo-2-para-onde-vai"
TRAB = C.trabalho("10")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas(PASTA)

# ---------------------------------------------------------------- números (conferidos contra a tela)
VA = CX["a-visao-geral-inteira.jpg"]
TOP = [("Casa", "casa", D("2300.00"), 48), ("Educação", "livro", D("1450.00"), 30), ("Mercado", "sacola", D("402.30"), 8)]
TOP_TELA = [r[4] for r in VA["top"]]
assert TOP_TELA == ["Casa R$ 2.300,00 48%", "Educação R$ 1.450,00 30%", "Mercado R$ 402,30 8%", "Transporte R$ 392,00 8%",
                    "Bares e restaurantes R$ 212,50 4%", "Saúde R$ 63,20 1%"], TOP_TELA
TOTAL = D("2300.00") + D("1450.00") + D("402.30") + D("392.00") + D("212.50") + D("63.20")
assert TOTAL == D("4820.00") and "Despesas\nR$ 4.820,00\n6 categorias" in VA["texto"]
for nome, _, v, pct in TOP:
    assert round(v / TOTAL * 100) == pct
VB = CX["b-transacoes-educacao.jpg"]
assert VB["resumo"][4] == "2 transações · 1 paga · 1 pendente · somam R$ 2.390,00 · 776 no histórico"
assert [i[4] for i in VB["itens"]] == ["Material escolar Educação · Conta corrente −R$ 940,00 pendente",
                                       "Escola FixaEducação · Conta corrente −R$ 1.450,00 paga"]
assert "ter · 12 de janeiro" in VB["texto"] and "dom · 10 de janeiro" in VB["texto"] and "Janeiro 2027" in VB["texto"]
assert D("1450.00") + D("940.00") == D("2390.00")
assert "Jan 10 2027 10:0" in CX["relogio"] and not CX["erros"]

# ---------------------------------------------------------------- caixas (px CSS da foto)
ROSCA_TXT = VA["rosca_txt"][:4]
ROSCA = [ROSCA_TXT[0] - 32, ROSCA_TXT[1] - 46, ROSCA_TXT[2] + 64, ROSCA_TXT[3] + 54]   # "Despesas / R$ 4.820,00 / 6 categorias"
TOP3 = C.uniao(*[r[:4] for r in VA["top"][:3]])
EDU = VA["top"][1][:4]
RESUMO = VB["resumo"][:4]
ITENS = C.uniao(*[i[:4] for i in VB["itens"]])
Y_ROSCA = round(VA["canvas"][1][1] + VA["canvas"][1][3] / 2 - 40, 1)     # centro da câmera na rosca
Y_TOP = round(TOP3[1] + 130, 1)                                            # centro da câmera em Top saídas

# ---------------------------------------------------------------- tempos (s)
H_SAI, S_SAI = 3.55, 5.4
T1, T2, T3, T4, T5 = (5.45, 7.85), (7.9, 10.2), (10.25, 12.6), (12.65, 14.9), (14.95, 16.95)
TQ_EDU = 11.05
FIM = 17.0
DUR = round(FIM + 2.75, 2)
CAM = [[0, 0, 195, 250, 1], [5.95, 6.95, 195, Y_ROSCA, 1], [8.05, 8.5, 195, Y_TOP, 1],
       [TQ_EDU + .15, TQ_EDU + .16, 195, 560, 1], [12.7, 13.1, 195, 700, 1]]
FOTOS = [("fa", "a-visao-geral-inteira.jpg"), ("fb", "b-transacoes-educacao.jpg")]
EXTRA = K.aneis("aRosca", "aTop", "aResumo", "aItens") + K.toques("tEdu")

# ---------------------------------------------------------------- gancho: as 3 maiores categorias em barras
ICONES = {
    "casa": '<path d="M4 11.2L12 4.5l8 6.7"/><path d="M6.2 9.6V19.5h11.6V9.6"/><path d="M10.2 19.5v-5.2h3.6v5.2"/>',
    "livro": '<path d="M4.5 5.5c2.6-.9 5.1-.6 7.5 1v13c-2.4-1.6-4.9-1.9-7.5-1z"/><path d="M19.5 5.5c-2.6-.9-5.1-.6-7.5 1v13c2.4-1.6 4.9-1.9 7.5-1z"/>',
    "sacola": '<path d="M5.5 8.5h13l-1 11h-11z"/><path d="M9 8.5V7a3 3 0 0 1 6 0v1.5"/>',
}
def icone(k, tam=40, cor=A.BRAND_DEEP):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="2.1" stroke-linecap="round" '
            f'stroke-linejoin="round">{ICONES[k]}</svg>')
MAXV = max(v for _, _, v, _ in TOP)
LARG = [round(900 * float(v / MAXV), 1) for _, _, v, _ in TOP]
YB = [640, 890, 1140]
def barras():
    out = []
    for i, (nome, ic, v, pct) in enumerate(TOP):
        out.append(f'<div class="cb" id="cb{i}" style="top:{YB[i]}px"><div class="cl"><i>{icone(ic, 44)}</i><span class="cn">{nome}</span>'
                   f'<span class="cv">{C.din(C.brl(float(v)))}</span></div><div class="br"><b id="br{i}"></b></div></div>')
    return "".join(out)

CSS = f"""
.tit{{font-size:64px}}
#h{{background:{A.SOFT}}}
#q{{position:absolute;left:90px;top:292px;width:900px;font-size:92px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK};text-wrap:balance}}
#q b{{color:{A.BRAND_DEEP};font-weight:700}}
.cb{{position:absolute;left:90px;width:900px;opacity:0}}
.cl{{display:flex;align-items:center;gap:22px;height:78px}}
.cl i{{flex:none;width:74px;height:74px;border-radius:22px;background:#fff;display:flex;align-items:center;justify-content:center}}
.cn{{font-size:50px;font-weight:600;letter-spacing:-.03em;color:{A.INK}}}
.cv{{margin-left:auto;font-size:60px;font-weight:700;letter-spacing:-.035em;color:{A.INK}}}
.cv .rs,.cv .cts{{color:{A.MUTED}}}
.br{{margin-top:20px;height:64px;border-radius:32px;background:#fff;overflow:hidden}}
.br b{{display:block;height:100%;width:0;border-radius:32px;background:{A.CORAL}}}
#ctx{{position:absolute;left:92px;top:1400px;font-size:36px;font-weight:500;letter-spacing:-.015em;color:{A.MUTED};opacity:0}}
#ctx b{{color:{A.INK};font-weight:700}}
#s{{background:{A.INK}}}
#sSelo{{position:absolute;left:90px;top:640px;transform-origin:0 50%}}
#sEye{{position:absolute;left:92px;top:556px}}
#sNome{{position:absolute;left:90px;top:1010px;font-size:150px;line-height:1;font-weight:700;letter-spacing:-.055em;color:#fff}}
#sPerg{{position:absolute;left:94px;top:1190px;font-size:52px;font-weight:600;letter-spacing:-.03em;color:{K.DARK_TEXTO}}}
#sPerg b{{color:{A.MENTA};font-weight:700}}
#msg{{position:absolute;left:90px;top:300px;width:900px;font-size:84px;line-height:1.02;font-weight:700;letter-spacing:-.048em;color:{A.INK};text-wrap:balance;opacity:0}}
#msg b{{color:{A.BRAND_DARK};font-weight:700}}
#cat{{position:absolute;left:90px;top:760px;width:900px;opacity:0}}
.lan{{display:flex;align-items:center;height:132px;padding:0 40px;border-radius:36px;background:#fff;border:2px solid {A.FIO};
  box-shadow:0 1px 2px rgba(15,20,16,.04),0 14px 34px -16px rgba(15,20,16,.16)}}
.lan span{{font-size:48px;font-weight:600;letter-spacing:-.03em;color:{A.INK}}}
.lan em{{margin-left:auto;font-style:normal;font-size:52px;font-weight:700;letter-spacing:-.035em;color:{K.CORAL_TXT}}}
.seta{{display:flex;justify-content:center;height:150px;align-items:center}}
.tag{{display:flex;justify-content:center}}
.tag span{{display:inline-flex;align-items:center;gap:20px;height:116px;padding:0 50px;border-radius:999px;background:{A.SOFT};color:{A.BRAND_DEEP};
  font-size:54px;font-weight:700;letter-spacing:-.03em}}
#cap{{position:absolute;left:90px;top:1300px;width:900px;text-align:center;font-size:40px;font-weight:500;letter-spacing:-.02em;color:{A.MUTED};opacity:0;text-wrap:balance}}
"""

def check(cor, tam=46, traco=3.2):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" stroke-linecap="round" '
            f'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')
SETA = (f'<svg width="80" height="120" viewBox="0 0 80 120" fill="none" stroke="{A.BRAND_DARK}" stroke-width="8" stroke-linecap="round" '
        f'stroke-linejoin="round"><path class="sx" d="M40 8v96" pathLength="1"/><path class="sx" d="M14 80l26 26 26-26" pathLength="1"/></svg>')

CORPO = f"""
<div class="cena papel" id="telas">
  <div class="tit" id="t1">Na <b>Visão geral</b>, desça até <b>Por categoria</b>.</div>
  <div class="tit" id="t2"><b>Top saídas</b>: as maiores despesas do mês.</div>
  <div class="tit" id="t3">Toque numa categoria: aparecem os <b>lançamentos</b> dela.</div>
  <div class="tit" id="t4">A escola já saiu. O <b>material escolar</b> vence dia 12.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", [(i, os.path.join(TELAS, f)) for i, f in FOTOS], EXTRA)}</div>
  <div id="msg">Categoria certa no lançamento: o gráfico <b>diz a verdade</b>.</div>
  <div id="cat">
    <div class="lan"><span>Material escolar</span><em>{C.MENOS}R$ 940,00</em></div>
    <div class="seta">{SETA}</div>
    <div class="tag"><span>{check(A.BRAND_DARK, 48)}Educação</span></div>
  </div>
  <div id="cap">Cada lançamento na sua categoria. É assim que Por categoria e Top saídas acertam.</div>
</div>

<div class="cena tinta" id="s">
  <div id="sEye">{S.eyebrow(2, "tinta", 32)}</div>
  <div id="sSelo">{S.selo(2, 330, "tinta")}</div>
  <div id="sNome">{S.NOMES[2]}.</div>
  <div id="sPerg">Para onde vai o <b>seu dinheiro</b>?</div>
</div>

<div class="cena suave" id="h">
  <div id="q">Para onde foi o seu dinheiro <b>em janeiro?</b></div>
  {barras()}
  <div id="ctx">Até 10/01, no exemplo: <b>R$ 4.820,00</b> em 6 categorias.</div>
</div>

{K.fim("Passo 2: o caminho. Visão geral no timtimcash.")}
"""

JS = f"""
const H_SAI={H_SAI}, S_SAI={S_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, FIM={FIM};
const CAM={CAM}, LARG={LARG}, VAL={[float(v) for _, _, v, _ in TOP]};
poeAnel('aRosca', {ROSCA}, 8); poeAnel('aTop', {TOP3}, 8); poeAnel('aResumo', {RESUMO}, 10); poeAnel('aItens', {ITENS}, 8);
poeToque('tEdu', ...{C.centro(EDU)});
function render(t){{
  // 1. gancho: as 3 maiores categorias crescem, com o valor contando
  [0,1,2].forEach(i => {{ const a = .05 + .38*i; $('cb'+i).style.opacity = lin(t, a, a+.18);
    $('cb'+i).style.transform = `translateY(${{(1-pout(t, a, a+.4))*30}}px)`;
    $('br'+i).style.width = (LARG[i]*pout(t, a+.05, a+1.05))+'px';
    const v = VAL[i]*pout(t, a+.05, a+1.05), s = fmt(v, 2).split(',');
    const e = $('cb'+i).querySelector('.cv'); e.querySelector('.int').textContent = s[0]; e.querySelector('.cts').textContent = ',' + s[1]; }});
  aparece('ctx', t, 1.75, 0, 16, .4);
  $('q').style.transform = `translateY(${{-10*pout(t, 0, 1.2)}}px)`;
  saiCima('h', t, H_SAI);
  // 2. selo da série
  salta('sSelo', t, H_SAI+.2, .5); aparece('sEye', t, H_SAI+.3, 0, 20); aparece('sNome', t, H_SAI+.42, 0, 30); aparece('sPerg', t, H_SAI+.6, 0, 24);
  saiCima('s', t, S_SAI);
  // 3. telas reais
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]);
  janela('janela', t, S_SAI+.05, T4[1]); janela('nota', t, S_SAI+.05, T4[1]);
  so(['fa','fb'], t >= {TQ_EDU} + .15 ? 1 : 0);
  camera('tela', t, CAM);
  anel('aRosca', t, 7.0, T1[1]); anel('aTop', t, 8.55, T2[1]);
  toque('tEdu', t, {TQ_EDU});
  anel('aResumo', t, {TQ_EDU}+.45, T3[1]); anel('aItens', t, 13.15, T4[1]);
  // 4. a mensagem
  aparece('msg', t, T5[0]+.05, FIM-.05, 30, .45); aparece('cat', t, T5[0]+.35, FIM-.05, 30, .45);
  desenha('#cat .sx', t, T5[0]+.7, .5); aparece('cap', t, T5[0]+.9, FIM-.05, 20, .4);
  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo("suave")}
  <div style="position:absolute;left:90px;top:430px">{S.eyebrow(2, "suave", 32)}</div>
  <div class="h1" style="position:absolute;left:90px;top:500px;width:900px;font-size:136px;line-height:.96;color:{A.INK}">Para onde vai?</div>
  <div style="position:absolute;left:0;top:860px;width:1080px;display:flex;justify-content:center">{S.selo_com_nome(2, 470, "suave", 70)}</div>"""
    return K.pagina_capa(corpo, "", fundo="suave")


HTML = C.pagina(CORPO, CSS, JS)
CAPA = capa()

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
