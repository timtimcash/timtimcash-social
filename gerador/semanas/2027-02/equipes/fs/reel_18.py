# -*- coding: utf-8 -*-
"""Reel de 18/02/2027 (quinta) · "Atalhos no computador" · capa verde · equipe fs.

Telas reais: captura_18.py, build 2026-10-19.5, computador 1440 × 900 em escala 2, cópia da conta (estado.py igual ao da base),
relógio da página em 18/02/2027 10:00. Tudo pelo teclado: N abre a "Nova transação" (foco no valor) -> "3200" (R$ 32,00) ->
clique em "Adicionar descrição" -> "Cinema" -> categoria "Lazer e hobbies" com o selo "sugerida" -> Cmd+Enter ("Transação
adicionada"); Cmd+K (busca global) -> "conta" (ações, telas, contas e lançamentos); F ("Modo foco ativado · pressione F para
sair"); "?" ("Atalhos de teclado"). Os cinco atalhos estão no ouvinte de teclado do index.html do build 2026-10-19.5 (N, F, "?",
Cmd/Ctrl+K e Cmd/Ctrl+Enter) e na lista "Atalhos de teclado" do próprio site (conferido abaixo com assert no texto da tela).
"3 segundos": na captura, do N ao aviso, digitando a 0,12 s por tecla, a sequência levou 2,0 s (caixas.json, tempo_lancamento_s).
O lançamento de exemplo (Cinema, R$ 32,00) fica só na captura; depois dele, o vídeo mostra só o aviso, sem os totais do mês.

python3 reel_18.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_18.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, COPIA, saida, telas, trabalho, caixas, camadas, pagina, pop_html, uniao, centro, folga, tecla, CMD, CSS as CSS_COMUM

PASTA = "2027-02-18_reel-atalhos-no-computador"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("18")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- conferência com a tela (e com o código do site)
SITE = open(os.path.join(COPIA, "site", "index.html"), encoding="utf-8").read()
for trecho in ['if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==="k"){', 'if(e.key==="n"&&!e.ctrlKey&&!e.metaKey&&!e.altKey&&!inInput&&!_overlayAberto()){',
               'if(e.key==="?"&&!inInput&&!_overlayAberto()){', 'if(e.key==="f"&&!e.ctrlKey&&!e.metaKey&&!e.altKey&&!inInput&&!_overlayAberto()){',
               'if(e.key!=="Enter"||!(e.metaKey||e.ctrlKey)||e.altKey||e.shiftKey||e.repeat||!currentUser)return;']:
    assert trecho in SITE, trecho
assert C["atalhos_caixa"][4] == ("Atalhos de teclado Busca global Cmd+K Nova transação N Lançar ou salvar a transação Cmd+Enter Buscar na lista / "
                                 "Modo foco F Período anterior / seguinte ← → Ir para o período atual H Desfazer a última ação Cmd+Z Fechar modal Esc Esta ajuda ? Fechar")
assert C["foco_depois_do_n"] == "f-valor" and C["computador-2-valor-4.jpg"]["valor"] == "32,00"
assert C["categoria_sugerida"].replace("\n", " ") == "Categoria Lazer e hobbies sugerida"
assert C["aviso"] == "Transação adicionada" and C["janela_fechou"] is True and C["lancado"] == [["Cinema", "Lazer e hobbies", 32, "despesa"]]
t8 = C["computador-8-busca-5.jpg"]["texto"]
for k in ["Contas e carteiras\nGerenciar contas\nAÇÃO", "Pendentes\nTransações não pagas\nTELA", "Conta corrente\nBanco / Digital", "CONTA", "Conta de luz", "TRANSAÇÃO"]:
    assert k in t8, k
assert C["aviso_foco"] == "Modo foco ativado · pressione F para sair" and C["corpo_foco"] is True and C["saiu_do_foco"] is True
assert C["tempo_lancamento_s"] <= 3.0 and "Feb 18 2027" in C["relogio"]

# ---------------------------------------------------------------- caixas (px CSS do computador)
c1 = C["computador-1-tecla-n.jpg"]
MODAL = c1["folha"]
CAT = C["computador-5-sugerida.jpg"]["cat"]
DESC = C["clique_desc"]
TOAST = C["computador-6-lancou.jpg"]["aviso"]
TOAST_F = C["computador-9-modo-foco.jpg"]["aviso"]
BUSCA = C["busca_caixa_fim"]
AJUDA = C["atalhos_caixa"][:4]

# janela do computador: deitada (a tela inteira, 900 × 562,5) ou em pé (zoom, 900 × 1000)
JX, JW = 90, 900
DEITADA, EM_PE = (690, 562.5), (600, 1000)
S_TODA = JW / 2 / 1440                    # 0,3125: a tela inteira na largura da janela
S_MODAL = JW / 2 / MODAL[2]               # a Nova transação na largura da janela
S_BUSCA = JW / 2 / BUSCA[2]
S_AJUDA = 1.0
def no_reel(r):
    """Onde a caixa r (px CSS) fica no Reel com a janela deitada e a tela inteira: [left, top, largura]."""
    k = 2 * S_TODA
    return [round(JX + r[0] * k, 1), round(DEITADA[0] + r[1] * k, 1), round(r[2] * k, 1)]
R_TOAST = [TOAST[0] - 4, TOAST[1] - 3, TOAST[2] + 8, TOAST[3] + 6]
R_TOAST_F = [TOAST_F[0] - 4, TOAST_F[1] - 3, TOAST_F[2] + 8, TOAST_F[3] + 6]

# ---------------------------------------------------------------- tempos (s)
H_SAI = 2.8
T = {1: (2.95, 5.3), 2: (5.45, 8.05), 3: (8.2, 10.35), 4: (10.5, 12.85), 5: (13.0, 15.1), 6: (15.25, 17.4)}
P_N, P_ENTER, P_K, P_F, P_AJ = 3.55, 8.75, 11.0, 13.65, 15.7
TV = [5.55, 5.7, 5.85, 6.0]
CLIQUE = 6.5
TD = [round(6.7 + .1 * k, 2) for k in range(6)]
T_SUG = 7.35
TB = [round(11.75 + .14 * k, 2) for k in range(5)]
FIM = 17.55
DUR = 20.35

IMGS = [("f0", tela("computador-0-visao-geral.jpg")), ("f1", tela("computador-1-tecla-n.jpg"))] + \
       [(f"v{k}", tela(f"computador-2-valor-{k}.jpg")) for k in range(1, 5)] + [("f3", tela("computador-3-descricao.jpg"))] + \
       [(f"d{k}", tela(f"computador-4-desc-{k}.jpg")) for k in range(1, 7)] + [("f5", tela("computador-5-sugerida.jpg")), ("f6", tela("computador-6-lancou.jpg")),
        ("g0", tela("computador-0-visao-geral.jpg")), ("f7", tela("computador-7-busca-vazia.jpg"))] + \
       [(f"b{k}", tela(f"computador-8-busca-{k}.jpg")) for k in range(1, 6)] + [("g1", tela("computador-0-visao-geral.jpg")),
        ("f9", tela("computador-9-modo-foco.jpg")), ("f10", tela("computador-10-atalhos.jpg"))]
TR = [0, P_N + .07] + TV + [CLIQUE + .05] + TD + [T_SUG, P_ENTER + .1, 10.5, P_K + .1] + TB + [13.0, P_F + .1, P_AJ + .1]
IDS = [i for i, _ in IMGS]
EXTRA = K.aneis("aCat")

SETA = ('<svg id="cursor" width="54" height="54" viewBox="0 0 24 24" style="position:absolute;left:0;top:0;opacity:0;z-index:5;overflow:visible">'
        '<path d="M5 3l14 8.2-6.2 1.3 3.6 6.6-2.4 1.3-3.6-6.6L5 18.2z" fill="#0F1410" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/></svg>'
        '<div id="clique" style="position:absolute;width:70px;height:70px;margin:-35px 0 0 -35px;border-radius:50%;border:6px solid ' + A.BRAND + ';opacity:0;z-index:4"></div>')
CHECK = ('<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')
def k(txt, ident, cls=""):
    return tecla(txt, cls, ident)
MAIS = '<span class="mais">+</span>'

CSS = f"""
.tit{{font-size:62px}}
.tit .kc{{font-size:50px;vertical-align:-.28em;margin-right:14px}}
.tit .mais{{font-size:50px;margin:0 6px 0 -4px;vertical-align:-.05em}}
.tit small{{display:block;font-size:34px;font-weight:600;letter-spacing:-.015em;color:{A.MUTED};margin-top:16px}}
#mon{{position:absolute;left:{JX}px;width:{JW}px;border-radius:30px;overflow:hidden;background:{K.FUNDO_TELA};border:2px solid {A.FIO};
  box-shadow:0 2px 4px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.28);opacity:0}}
#tela{{position:absolute;left:0;top:0;transform-origin:0 0}}
#notaM{{position:absolute;left:{JX + 6}px;font-size:26px;font-weight:500;color:{A.MUTED};opacity:0}}
/* gancho */
#g .eyebrow{{position:absolute;left:90px;top:300px}}
#gT{{position:absolute;left:90px;top:350px;width:900px;font-size:108px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#gT b{{color:{A.BRAND_DARK}}}
.lin{{position:absolute;left:90px;width:900px;display:flex;align-items:center;gap:22px}}
.lin .kc{{font-size:96px}}
.lin .mais{{font-size:76px;margin:0 6px}}
#gCampo{{flex:1;height:170px;border-radius:34px;background:#fff;border:3px solid {A.FIO};display:flex;align-items:center;padding:0 36px;gap:16px;
  font-size:56px;font-weight:600;color:{A.INK};letter-spacing:-.02em;white-space:nowrap;overflow:hidden}}
#gCampo .cur{{display:inline-block;width:5px;height:58px;border-radius:3px;background:{A.BRAND}}}
.lin .rot{{font-size:52px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em}}
#gOk{{position:absolute;left:90px;top:1300px;height:110px;padding:0 40px 0 30px;border-radius:999px;background:{A.INK};color:#fff;display:flex;align-items:center;gap:16px;
  font-size:44px;font-weight:600;letter-spacing:-.015em;opacity:0}}
#gOk svg{{color:{A.MENTA}}}
"""

CORPO = f"""
<div class="cena papel" id="cenaTela">
  <div class="tit" id="t1">{k("N", "kN")}abre a <b>Nova transação</b>.</div>
  <div class="tit" id="t2">Valor e descrição: <b>a categoria vem sugerida.</b></div>
  <div class="tit" id="t3">{k(CMD, "kC1")}{MAIS}{k("Enter", "kE")}lança.<small>No Windows: Ctrl + Enter.</small></div>
  <div class="tit" id="t4">{k(CMD, "kC2")}{MAIS}{k("K", "kK")}busca <b>telas, ações, contas e lançamentos.</b></div>
  <div class="tit" id="t5">{k("F", "kF")}liga o <b>Modo foco</b>.<small>O menu lateral sai e o conteúdo ganha a tela. F de novo, ele volta.</small></div>
  <div class="tit" id="t6">{k("?", "kQ")}mostra <b>todos os atalhos</b>.</div>
  <div id="notaM">{K.NOTA}</div>
  <div id="mon">{camadas("tela", IMGS, "", 1440)}{EXTRA}{SETA}</div>
  {pop_html("popT", tela("computador-6-lancou.jpg"))}
  {pop_html("popF", tela("computador-9-modo-foco.jpg"))}
</div>

<div class="cena papel" id="g">
  <div class="eyebrow">Atalhos de teclado</div>
  <div id="gT">Lançar um gasto em <b>3 segundos?</b></div>
  <div class="lin" style="top:740px">{k("N", "hN")}<div id="gCampo"><span id="gTxt"></span><span class="cur" id="gCur"></span></div></div>
  <div class="lin" style="top:1010px">{k(CMD, "hC")}{MAIS}{k("Enter", "hE")}<span class="rot">e pronto</span></div>
  <div id="gOk">{CHECK}Transação adicionada</div>
</div>

{K.fim("Atalhos no timtimcash", "No navegador do computador. No Windows, Ctrl no lugar do Cmd.")}
"""

JS = f"""
const H_SAI={H_SAI}, TT={ {i: list(v) for i, v in T.items()} }, FIM={FIM};
const P_N={P_N}, P_ENTER={P_ENTER}, P_K={P_K}, P_F={P_F}, P_AJ={P_AJ}, CLIQUE={CLIQUE}, TR={TR}, IDS={IDS};
const JX={JX}, JW={JW}, DEIT={list(DEITADA)}, PE={list(EM_PE)};
const R_TOAST={R_TOAST}, R_TOAST_F={R_TOAST_F}, DE_T={no_reel(R_TOAST)}, DE_F={no_reel(R_TOAST_F)};
const DESC={DESC}, CAT={folga(CAT, 2)};
// câmera (px CSS do computador): [_, _, fx, fy, zoom]; a janela vai de deitada (tela inteira) a em pé (zoom)
const FULL = [720, 450, {S_TODA}];
const CAM = [[0,0,...FULL], [3.75,4.25,720,450,{S_MODAL:.4f}], [8.85,8.86,...FULL], [11.1,11.55,720,{round(BUSCA[1] + BUSCA[3] / 2, 1)},{S_BUSCA:.4f}],
             [12.95,13.35,...FULL], [15.85,16.3,720,{round(AJUDA[1] + AJUDA[3] / 2, 1)},{S_AJUDA}]];
const FORMA = [[0,0], [3.75,4.2,1], [8.85,8.86,0], [11.1,11.55,1], [12.95,13.35,0], [15.85,16.3,1]];
function forma(t){{ let f = 0; for (let i=1;i<FORMA.length;i++){{ const [a,b,v] = FORMA[i]; const p = prog(t,a,b); f += (v-f)*p; }} return f; }}
function render(t){{
  // 1. gancho: N, o valor e a descrição, Cmd+Enter
  saiCima('g', t, H_SAI);
  aperta('hN', t, .05, .4);
  const txt = 'R$ 32,00 · Cinema', n = clamp(Math.floor((t-.3)*22), 0, txt.length);
  $('gTxt').textContent = txt.slice(0, n); $('gCur').style.opacity = (Math.floor(t*3) % 2 === 0 || t < 1.2) ? 1 : 0;
  aperta('hC', t, 1.3, .4); aperta('hE', t, 1.36, .4);
  $('gOk').style.opacity = lin(t, 1.55, 1.7); $('gOk').style.transform = `scale(${{.8 + .2*pback(t, 1.55, 1.95)}})`;
  // 2. as telas reais no computador
  [1,2,3,4,5,6].forEach(i => titulo('t'+i, t, TT[i][0], TT[i][1]));
  aperta('kN', t, P_N); aperta('kC1', t, P_ENTER); aperta('kE', t, P_ENTER+.05); aperta('kC2', t, P_K); aperta('kK', t, P_K+.05);
  aperta('kF', t, P_F); aperta('kQ', t, P_AJ);
  const f = forma(t), top = DEIT[0] + (PE[0]-DEIT[0])*f, alt = DEIT[1] + (PE[1]-DEIT[1])*f;
  const mon = $('mon'); mon.style.top = top+'px'; mon.style.height = alt+'px';
  const ent = prog(t, H_SAI+.05, H_SAI+.6), sai = prog(t, FIM-.2, FIM);
  mon.style.opacity = ent*(1-sai); mon.style.transform = `translateY(${{(1-ent)*80}}px)`;
  const nm = $('notaM'); nm.style.top = (top - 52)+'px'; nm.style.opacity = ent*(1-sai);
  const cam = camera('tela', t, CAM, JW, alt);
  fotos(IDS, t, TR);
  // o clique em "Adicionar descrição"
  const k2 = cam[2]*E, cx = JW/2 + (DESC[0] + 60 - cam[0])*k2, cy = alt/2 + (DESC[1] + DESC[3]/2 - cam[1])*k2;
  const vc = Math.min(lin(t, CLIQUE-.45, CLIQUE-.3), 1 - lin(t, CLIQUE+.5, CLIQUE+.65));
  const ch = pout(t, CLIQUE-.45, CLIQUE-.05);
  const cur = $('cursor'); cur.style.opacity = vc; cur.style.left = (cx + 120*(1-ch))+'px'; cur.style.top = (cy + 90*(1-ch))+'px';
  const cl = $('clique'); cl.style.left = cx+'px'; cl.style.top = cy+'px';
  cl.style.opacity = (t >= CLIQUE && t < CLIQUE+.5) ? 1 - lin(t, CLIQUE, CLIQUE+.5) : 0; cl.style.transform = `scale(${{1 + 1.2*lin(t, CLIQUE, CLIQUE+.5)}})`;
  anelCam('aCat', CAT, cam, 10, JW, alt); anel('aCat', t, 7.4, 8.05);
  // os avisos de perto
  recorte('popT', t, 9.4, 10.3, R_TOAST, DE_T, [150, 1330, 780], .55, null, 1440);
  recorte('popF', t, 14.0, 15.05, R_TOAST_F, DE_F, [150, 1330, 780], .55, null, 1440);
  // 3. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    css = f""".lin{{position:absolute;left:90px;width:900px;display:flex;align-items:center;gap:26px}}
.lin .kc{{font-size:96px;box-shadow:0 .09em 0 {A.BRAND_DARK},0 .14em .3em rgba(15,20,16,.25)}}
.lin .mais{{font-size:80px;color:#fff;font-weight:700;margin:0 6px}}
.lin .rot{{font-size:48px;font-weight:600;color:#fff;letter-spacing:-.02em}}"""
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Atalhos de teclado</div>
    <div class="h1" style="font-size:136px;line-height:.95;margin-top:34px">Lance em 3 segundos.</div>
  </div>
  <div class="lin" style="top:930px">{tecla("N")}<span class="rot">abre</span></div>
  <div class="lin" style="top:1190px">{tecla(CMD)}<span class="mais">+</span>{tecla("Enter")}<span class="rot">lança</span></div>"""
    return K.pagina_capa(corpo, CSS_COMUM + css, fundo="verde")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
