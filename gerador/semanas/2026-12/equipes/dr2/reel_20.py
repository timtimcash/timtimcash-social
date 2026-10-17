# -*- coding: utf-8 -*-
"""Reel de 20/12/2026 (domingo) · "Seu ano num arquivo" · capa verde · equipe dr2.

Telas reais: captura_20.py, build 2026-10-16.1, celular 390 × 844 em escala 3, conta fictícia de N/base_app (sem mudança), relógio
da página em 20/12/2026 10:00. Passo a passo: Menu -> Exportar -> "Ano atual · 2026" (o contador passa de 24 para 328 lançamentos)
-> rola até "Formato" -> PDF -> Exportar (aviso "Relatório de 328 transações gerado") -> Preferências › Backup ("Exportar backup completo").
O gancho desenha os 328 lançamentos de 2026 da conta de exemplo (um traço por lançamento, mês a mês, na cor do tipo: receita, despesa,
transferência), contados no estado do dia (estado_2026-12-20.js); são os mesmos 328 que o site conta em "Ano atual".
Revisão de 16/10: a aba do relatório em PDF entra no vídeo (revisao/captura_20_relatorio.py). A página pede ao Google Fonts a DM Serif
Display e a Inter; a captura entrega essas mesmas fontes, locais, e a aba sai como a pessoa vê no celular: a página de 980 px reduzida
à largura da tela, com o botão "Imprimir / Salvar PDF" no canto. O aviso "Relatório de 328 transações gerado" fica na aba de origem.

python3 reel_20.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_20.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, N, saida, trabalho, caixas, camadas, pagina, uniao, centro

PASTA = "2026-12-20_reel-seu-ano-num-arquivo"
SAIDA = saida(PASTA)
TELAS = os.path.join(SAIDA, "telas")
TRAB = trabalho("20")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- conferência com a tela e com a conta
assert "24 lançamentos" in C["celular-exportar-3-janela.jpg"]["texto"]
assert "Ano atual\n2026" in C["celular-exportar-4-ano.jpg"]["texto"] and "328 lançamentos" in C["celular-exportar-4-ano.jpg"]["texto"]
for k in ["Excel\n.xlsx · editável", "PDF\nRelatório pronto", "CSV\nTexto universal", "Todas as contas"]:
    assert k in C["celular-exportar-5-formatos.jpg"]["texto"], k
assert C["aviso"] == "Relatório de 328 transações gerado"
assert "Período: 01/01/2026 até 31/12/2026" in C["relatorio_texto"] and "328 transações" in C["relatorio_texto"]
assert "Exportar backup completo\nArquivo JSON com contas, transações, categorias e orçamentos." in C["celular-preferencias-backup.jpg"]["texto"]
assert C["cpf_visivel"] is False
_e = open(os.path.join(N, "base_app", "estado_2026-12-20.js"), encoding="utf-8").read()
_d = json.loads(_e[_e.index("=") + 1:_e.index(";\n")])
TX26 = sorted([t for t in _d["txs"] if t["data"].startswith("2026")], key=lambda t: (t["data"], t["id"]))
assert len(TX26) == 328
POR_MES = [[t["tipo"] for t in TX26 if t["data"][5:7] == f"{m:02d}"] for m in range(1, 13)]
assert [len(x) for x in POR_MES] == [28, 27, 25, 27, 27, 27, 28, 27, 26, 30, 32, 24]

# ---------------------------------------------------------------- caixas (px CSS do celular)
c1, c2 = C["celular-exportar-1-visao-geral.jpg"], C["celular-exportar-2-menu.jpg"]
c4, c5 = C["celular-exportar-4-ano.jpg"], C["celular-exportar-5-formatos.jpg"]
c7, c8 = C["celular-exportar-7-relatorio-gerado.jpg"], C["celular-preferencias-backup.jpg"]
MENU, EXPORTAR_M = c1["menu"], c2["exportar"]
ANO, CONT = c4["r_ano"], c4["contador"]
TODAS = c5["todas"]
FORMATOS = uniao(c5["f_xlsx"], c5["f_pdf"], c5["f_csv"])
PDF, BOTAO = c5["f_pdf"], c5["exportar"]
AVISO = c7["aviso"]
PRINT = [310.7, 819.7, 71.0, 16.0]   # botão "Imprimir / Salvar PDF" na aba do relatório (px CSS do celular)
BACKUP = [25, c8["backup"][1] - 14, 340, c8["baixar"][1] + c8["baixar"][3] + 14 - (c8["backup"][1] - 14)]

# ---------------------------------------------------------------- tempos (s)
G_SAI = 2.6
T1, T2, T3, T4, T5 = (2.9, 4.85), (5.1, 7.6), (7.85, 10.2), (10.45, 13.75), (14.0, 16.35)
TQ_MENU, TQ_EXP, TQ_ANO, TQ_PDF, TQ_BOT = 3.45, 4.85, 5.85, 10.25, 11.85
J_SAI = 16.4
S4 = 16.6
FIM = 19.25
DUR = 22.0

IMGS = [("i1", tela("celular-exportar-1-visao-geral.jpg")), ("i2", tela("celular-exportar-2-menu.jpg")),
        ("i3", tela("celular-exportar-3-janela.jpg")), ("i4", tela("celular-exportar-4-ano.jpg")),
        ("i5", tela("celular-exportar-5-formatos.jpg")), ("i6", tela("celular-exportar-6-pdf.jpg")),
        ("i7", tela("celular-exportar-7b-relatorio-aba.jpg")), ("i8", tela("celular-preferencias-backup.jpg"))]
EXTRA = K.aneis("aMenu", "aExp", "aAno", "aCont", "aTodas", "aFmt", "aPdf", "aPrint", "aBackup") + \
        K.toques("tqMenu", "tqExp", "tqAno", "tqPdf", "tqBot")

# ---------------------------------------------------------------- gancho: os 328 lançamentos de 2026, mês a mês
COR = {"receita": A.BRAND, "despesa": A.CORAL, "transferencia": A.NEUTRO}
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
BX0, BW, BG_, BH, BP, BASE = 99, 58, 16, 11, 16, 1270     # x do 1º mês, largura, vão, altura do traço, passo vertical, base
traços, dados_js = [], []
for m, tipos in enumerate(POR_MES):
    for k, tp in enumerate(tipos):
        x, y = BX0 + m * (BW + BG_), BASE - (k + 1) * BP
        traços.append(f'<i class="tr" id="b{len(dados_js)}" style="left:{x}px;top:{y}px;background:{COR[tp]}"></i>')
        dados_js.append([m, k, x + BW / 2, y + BH / 2])
rotulos = "".join(f'<span class="ml" style="left:{BX0 + m * (BW + BG_) - 6}px">{n}</span>' for m, n in enumerate(MESES))
FX, FY = 540, 1010          # centro do arquivo desenhado


def arquivo(w, cor, traco=10, ano="2026", tam=None, fundo="none", ident=""):
    """Arquivo desenhado em traço (cantos redondos, dobra no canto de cima), com o ano dentro."""
    h = w * 1.25
    d = w * 0.3
    tam = tam or w * 0.27
    idt = f' id="{ident}"' if ident else ""
    return f"""<svg{idt} width="{w}" height="{h:.0f}" viewBox="-{traco} -{traco} {w + 2 * traco} {h + 2 * traco:.0f}" style="overflow:visible;display:block">
  <path d="M{traco / 2} {traco / 2 + 18} q0 -18 18 -18 H{w - d} L{w - traco / 2} {d} V{h - traco / 2 - 18} q0 18 -18 18 H{traco / 2 + 18} q-18 0 -18 -18 Z"
    fill="{fundo}" stroke="{cor}" stroke-width="{traco}" stroke-linejoin="round"/>
  <path d="M{w - d} {traco / 2} V{d - 14} q0 14 14 14 H{w - traco / 2}" fill="none" stroke="{cor}" stroke-width="{traco}" stroke-linejoin="round" stroke-linecap="round"/>
  <text x="{w / 2 - 4}" y="{h * 0.62:.0f}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="{tam:.0f}" letter-spacing="-2"
    fill="{cor}" style="font-feature-settings:'tnum','cv11','ss01'">{ano}</text>
</svg>"""


FORMATOS_DES = [("Excel", ".xlsx"), ("PDF", ".pdf"), ("CSV", ".csv"), ("Backup", ".json")]
arquivos_s4 = "".join(f'<div class="fx" id="fx{i}">{arquivo(176, A.MENTA, 10, ext, 40)}<span>{nome}</span></div>' for i, (nome, ext) in enumerate(FORMATOS_DES))

CSS = f"""
#g{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
#gTop{{position:absolute;left:90px;top:330px;width:900px}}
#gTop .h1{{font-size:110px;margin-top:30px}}
.tr{{position:absolute;width:{BW}px;height:{BH}px;border-radius:6px;opacity:0;will-change:transform}}
.ml{{position:absolute;top:{BASE + 18}px;width:{BW + 12}px;text-align:center;font-size:27px;font-weight:600;color:{A.MUTED}}}
#gCont{{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;top:{BASE + 92}px;text-align:center;font-size:56px;font-weight:700;letter-spacing:-.04em;color:{A.INK}}}
#gCont b{{color:{A.BRAND_DARK};font-variant-numeric:tabular-nums}}
#gArq{{position:absolute;left:{FX - 170}px;top:{FY - 212}px;width:340px;opacity:0;transform-origin:170px 212px}}
.tit{{font-size:66px}}
/* seus dados saem com você */
#s4{{transform:translateY(1920px)}}
#s4 .h2{{position:absolute;left:90px;top:320px;width:900px;font-size:104px;line-height:1.0;color:#fff}}
#s4 .h2 b{{color:{A.MENTA}}}
#fxs{{position:absolute;left:80px;top:860px;width:920px;width:900px;display:flex;justify-content:space-between}}
.fx{{display:flex;flex-direction:column;align-items:center;gap:26px;opacity:0}}
.fx span{{font-size:44px;font-weight:700;color:#fff;letter-spacing:-.02em}}
#s4n{{position:absolute;left:90px;top:1300px;width:900px;font-size:40px;line-height:1.3;font-weight:500;color:{K.DARK_TEXTO};letter-spacing:-.02em;opacity:0;text-wrap:balance}}
"""

CORPO = f"""
<div class="cena papel" id="tl">
  <div class="tit" id="t1">No menu, toque em <b>Exportar</b>.</div>
  <div class="tit" id="t2">Escolha o <b>ano</b>: são 328 lançamentos de 2026.</div>
  <div class="tit" id="t3">Todas as contas, em <b>Excel, PDF ou CSV</b>.</div>
  <div class="tit" id="t4"><b>PDF</b>: o relatório abre pronto para imprimir ou salvar.</div>
  <div class="tit" id="t5">E o <b>backup completo</b> fica em Preferências.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>
</div>

<div class="cena tinta" id="s4">
  <div class="h2">Seus dados <b>saem com você.</b></div>
  <div id="fxs">{arquivos_s4}</div>
  <div id="s4n">Quando quiser, no computador ou no celular.</div>
</div>

<div class="cena papel" id="g">
  <div id="gTop">
    <div class="eyebrow">Exportar</div>
    <div class="h1">2026 inteiro, <span style="color:{A.BRAND_DARK}">num arquivo só.</span></div>
  </div>
  {"".join(traços)}
  {rotulos}
  <div id="gArq">{arquivo(340, A.INK, 12, "2026", 86, "#fff")}</div>
  <div id="gCont"><b id="gN">0</b> lançamentos</div>
</div>

{K.fim("Exportar no timtimcash")}
"""

JS = f"""
const DADOS = {json.dumps(dados_js)}, FX = {FX}, FY = {FY};
const G_SAI={G_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, J_SAI={J_SAI}, S4={S4}, FIM={FIM};
const TQ_MENU={TQ_MENU}, TQ_EXP={TQ_EXP}, TQ_ANO={TQ_ANO}, TQ_PDF={TQ_PDF}, TQ_BOT={TQ_BOT};
poeAnel('aMenu', {MENU}, 8); poeAnel('aExp', {EXPORTAR_M}, 8); poeAnel('aAno', {ANO}, 6); poeAnel('aCont', {CONT}, 10);
poeAnel('aTodas', {TODAS}, 8); poeAnel('aFmt', {FORMATOS}, 8); poeAnel('aPdf', {PDF}, 6); poeAnel('aPrint', {PRINT}, 8); poeAnel('aBackup', {BACKUP}, 4);
poeToque('tqMenu', ...{centro(MENU)}); poeToque('tqExp', ...{centro(EXPORTAR_M)}); poeToque('tqAno', ...{centro(ANO)});
poeToque('tqPdf', ...{centro(PDF)}); poeToque('tqBot', ...{centro(BOTAO)});
// câmera (px CSS do celular no centro da janela)
const CAM = [[0,0,195,250,1], [3.7,4.2,195,594,1], [4.95,5.35,195,330,1], [6.05,6.5,195,540,1], [7.7,7.95,195,540,1], [11.3,11.75,195,594,1], [11.99,12.0,195,250,1], [12.15,12.7,103,125,2.0], [12.95,13.5,346,815,3.2], [13.84,13.85,195,300,1]];
function render(t){{
  // 1. gancho: cada lançamento de 2026 entra no seu mês; depois todos entram no arquivo
  const voa0 = 1.45;
  let n = 0;
  for (let i=0;i<DADOS.length;i++){{
    const [m, k, cx, cy] = DADOS[i];
    const a = -0.35 + m*0.085 + k*0.012;
    const p = pout(t, a, a+.22);
    if (t >= a) n++;
    const v0 = voa0 + m*0.03 + (k%7)*0.012, v = prog(t, v0, v0+.5);
    const dx = (FX - cx)*v, dy = (FY + 40 - cy)*v;
    const e = $('b'+i);
    e.style.opacity = p*(1 - lin(t, v0+.32, v0+.5));
    e.style.transform = `translate(${{dx.toFixed(1)}}px, ${{(dy + (1-p)*-26).toFixed(1)}}px) scale(${{(1 - .7*v).toFixed(3)}})`;
  }}
  $('gN').textContent = Math.min(328, n);
  document.querySelectorAll('.ml').forEach(e => e.style.opacity = 1 - prog(t, voa0, voa0+.35));
  const pa = pback(t, voa0+.35, voa0+.85);
  $('gArq').style.opacity = lin(t, voa0+.35, voa0+.5);
  $('gArq').style.transform = `scale(${{(.55 + .45*pa).toFixed(3)}})`;
  const gs = prog(t, G_SAI, G_SAI+.28);
  $('g').style.opacity = 1 - gs; $('g').style.transform = `translateY(${{-70*gs}}px)`;

  // 2. a tela real: Menu, Exportar, Ano, Formato, PDF, aviso e backup
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]);
  titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, G_SAI+.2, J_SAI);
  const ne = prog(t, G_SAI+.2, G_SAI+.8);
  $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  op('i2', prog(t, TQ_MENU+.15, TQ_MENU+.32)); op('i3', prog(t, TQ_EXP+.15, TQ_EXP+.32));
  op('i4', t >= TQ_ANO+.15 ? 1 : 0); op('i5', prog(t, 7.7, 7.95)); op('i6', t >= TQ_PDF+.15 ? 1 : 0);
  op('i7', t >= 12.0 ? 1 : 0); op('i8', prog(t, 13.85, 14.07));
  anel('aMenu', t, 2.95, 3.35); toque('tqMenu', t, TQ_MENU);
  anel('aExp', t, 4.2, 4.75); toque('tqExp', t, TQ_EXP);
  anel('aAno', t, 5.25, 6.2); toque('tqAno', t, TQ_ANO); anel('aCont', t, 6.55, 7.45);
  anel('aTodas', t, 8.1, 8.95); anel('aFmt', t, 9.05, 10.1); toque('tqPdf', t, TQ_PDF);
  anel('aPdf', t, 10.6, 11.25); toque('tqBot', t, TQ_BOT); anel('aPrint', t, 13.4, 13.85);
  anel('aBackup', t, 14.35, 16.25);

  // 3. seus dados saem com você
  sobe('s4', t, S4);
  for (let i=0;i<4;i++){{ const a0 = S4+.55+i*.16; const p = pback(t, a0, a0+.45);
    $('fx'+i).style.opacity = lin(t, a0, a0+.12); $('fx'+i).style.transform = `translateY(${{((1-p)*60 + 8*Math.sin((t-a0)*2.4 + i)).toFixed(1)}}px)`; }}
  $('s4n').style.opacity = prog(t, S4+1.3, S4+1.7);

  // 4. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Exportar</div>
    <div class="h1" style="font-size:124px;line-height:.97;margin-top:34px">Seu ano num arquivo</div>
  </div>
  <div style="position:absolute;left:{540 - 205}px;top:880px">{arquivo(410, "#fff", 14, "2026", 108)}</div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
