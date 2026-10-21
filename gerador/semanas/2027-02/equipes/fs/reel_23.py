# -*- coding: utf-8 -*-
"""Reel de 23/02/2027 (terça) · "Meta de receita" · capa verde · equipe fs.
(Trocou de dia com "Nova remessa, câmbio na hora", a pedido da revisão: este era o de 25/02.)

Telas reais: captura_23.py, build 2026-10-19.5, celular 390 × 1000 em escala 3, relógio da página em 23/02/2027 10:00, numa
CONTA DE EXEMPLO SEPARADA (cenarios.py da cópia da equipe fs, cenário "renda", pedido da revisão): só uma "Conta corrente", sem
orçamentos e sem lançamentos da conta principal, com duas receitas de exemplo "Trabalho extra" em "Outras receitas", 12/02 R$ 450,00
e 22/02 R$ 300,00 (R$ 750 no mês). Sem meta de receita antes da captura. A nota da tela diz "Conta de exemplo só com a renda extra."
Passo a passo: Orçamentos ("Sem limites definidos") -> "Definir limites" -> aba "Receitas" -> "Outras receitas" R$ 1.000,00 ("META TOTAL POR MÊS ·
1 categoria · R$ 1.000,00") -> "Salvar" ("Orçamentos salvos") -> painel "Metas de receita · Fevereiro 2027": "Outras receitas
R$ 750 de R$ 1.000 · 75% · Faltam R$ 250 para a meta" -> "+" -> "Receita" -> R$ 250,00 -> "Trab" -> a descrição já usada
"Trabalho extra" (traz "Outras receitas") -> "Lançar receita" ("Transação adicionada") -> "R$ 1.000 de R$ 1.000 · 100% ·
Meta cumprida". A receita de R$ 250 fica só na captura (o site falso descarta as gravações).

python3 reel_23.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_23.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import K, A, saida, telas, trabalho, caixas, camadas, pagina, uniao, centro, folga

PASTA = "2027-02-23_reel-meta-de-receita"
SAIDA = saida(PASTA)
TELAS = telas(PASTA)
TRAB = trabalho("23")
C = caixas(PASTA)
def tela(n): return os.path.join(TELAS, n)

# ---------------------------------------------------------------- conferência com a tela e com o cenário
assert C["cenario"]["hoje"] == "2027-02-23" and C["cenario"]["renda"] == [["2027-02-12", "450.00"], ["2027-02-22", "300.00"]] and C["cenario"]["separada"]
assert "Sem limites definidos" in C["celular-meta-1-orcamentos.jpg"]["texto"] and "Sem limites de despesa" in C["celular-meta-6-faltam-limpo.jpg"]["texto"]
assert 450 + 300 == 750 and 750 + 250 == 1000
assert [C[t[2]]["valor"] for t in C["teclas"]] == ["R$ 0,01", "R$ 0,10", "R$ 1,00", "R$ 10,00", "R$ 100,00", "R$ 1.000,00"]
assert "META TOTAL POR MÊS\n1 categoria\nR$ 1.000,00" in C["celular-meta-4-digita-6.jpg"]["texto"]
assert C["aviso_salvar"].startswith("Orçamentos salvos") and C["aviso_lancar"].startswith("Transação adicionada")
M6, M11 = C["celular-meta-6-faltam-limpo.jpg"]["metas"], C["celular-meta-11-cumprida-limpo.jpg"]["metas"]
assert M6["texto"] == "Metas de receita Fevereiro 2027 Editar metas Outras receitas R$ 750 de R$ 1.000 75% Faltam R$ 250 para a meta"
assert M11["texto"] == "Metas de receita Fevereiro 2027 Editar metas Outras receitas R$ 1.000 de R$ 1.000 100% Meta cumprida"
assert C["sugestao"][4] == "Trabalho extra Outras receitas · 2x"
assert "Hoje 23/02" in C["celular-meta-7-receita.jpg"]["texto"] and "Categoria\nOutras receitas" in C["celular-meta-9-preenchida.jpg"]["texto"]
assert C["valor_receita"] == "250,00" and C["receita_preenchida"] == {"valor": "250,00", "desc": "Trabalho extra"}
assert "Feb 23 2027" in C["relogio"]

# ---------------------------------------------------------------- caixas (px CSS do celular, na tela)
def v(b, rol): return [b[0], round(b[1] - rol, 1), b[2], b[3]]
c1, c2, c3 = C["celular-meta-1-orcamentos.jpg"], C["celular-meta-2-despesas.jpg"], C["celular-meta-3-receitas.jpg"]
c46, c7 = C["celular-meta-4-digita-6.jpg"], C["celular-meta-7-receita.jpg"]
R1 = c1["rolagem"]
DEFINIR = v(c1["definir"], R1)
ABA_REC = v(C["aba_receitas"], R1)
CAMPO = v(c3["campo"], R1)
LINHA_OR = v(uniao(c46["campo"], c46["linha"]), R1)
SALVAR = v(c46["salvar"], R1)
RM = C["celular-meta-6-faltam-limpo.jpg"]["rolagem"]
ITEM = v(M6["item"], RM)
PAINEL = v(M6["painel"], RM)
VALOR_F = v(c7["valor"], RM)
SUG = v(C["sugestao"][:4], RM)
LANCAR = v(c7["lancar"], RM)
BOT_REC = v(C["botao_receita"], RM)

# ---------------------------------------------------------------- tempos (s)
H_SAI = 2.8
T1, T2, T3, T4, T5 = (3.0, 5.45), (5.6, 8.1), (8.25, 10.55), (10.7, 13.45), (13.6, 16.1)
TQ_DEF, TQ_ABA = 3.75, 4.95
TECLAS = [5.95, 6.12, 6.29, 6.46, 6.63, 6.8]
TQ_SALVAR = 7.6
TQ_MAIS, TQ_VALOR, TQ_SUG, TQ_LANCAR = 10.85, 11.35, 12.15, 12.95
J_SAI = 16.1
FIM = 16.35
DUR = 19.15

IMGS = [("i1", tela("celular-meta-1-orcamentos.jpg")), ("i2", tela("celular-meta-2-despesas.jpg")), ("i3", tela("celular-meta-3-receitas.jpg"))] + \
       [(f"d{k}", tela(f"celular-meta-4-digita-{k}.jpg")) for k in range(1, 7)] + \
       [("i5", tela("celular-meta-5-faltam.jpg")), ("i6", tela("celular-meta-6-faltam-limpo.jpg")), ("i7", tela("celular-meta-7-receita.jpg")),
        ("i8", tela("celular-meta-8-sugestao.jpg")), ("i9", tela("celular-meta-9-preenchida.jpg")), ("i10", tela("celular-meta-10-cumprida.jpg")),
        ("i11", tela("celular-meta-11-cumprida-limpo.jpg"))]
TR = [0, TQ_DEF + .15, TQ_ABA + .15] + TECLAS + [TQ_SALVAR + .15, 8.3, TQ_MAIS + .15, TQ_VALOR + .55, TQ_SUG + .15, TQ_LANCAR + .15, 13.85]
IDS = [i for i, _ in IMGS]
EXTRA = K.aneis("aDef", "aAba", "aCampo", "aItem", "aSug", "aItem2") + K.toques("tqDef", "tqAba", "tqCampo", "tqSalvar", "tqMais", "tqValor", "tqSug", "tqLancar")

# ---------------------------------------------------------------- gancho: a barra da renda extra enche até a meta
PASSOS = [("12/02", 450), ("22/02", 300), ("23/02", 250)]
BX, BY, BW, BH = 90, 860, 900, 120
chips = "".join(f'<div class="rc" id="rc{k}"><i>Trabalho extra · {d}</i><b>+R$ {v}</b></div>' for k, (d, v) in enumerate(PASSOS))
CHECK = ('<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')

CSS = f"""
.tit{{font-size:64px}}
#nota{{top:516px;line-height:1.3}}
/* gancho */
#g .eyebrow{{position:absolute;left:90px;top:300px}}
#gT{{position:absolute;left:90px;top:350px;width:900px;font-size:112px;line-height:.97;font-weight:700;letter-spacing:-.05em;color:{A.INK}}}
#gT b{{color:{A.BRAND_DEEP}}}
#gMeta{{position:absolute;left:{BX + BW - 300}px;top:{BY - 74}px;width:300px;text-align:right;font-size:36px;font-weight:700;color:{A.INK};letter-spacing:-.02em}}
#gMeta span{{color:{A.BRAND_DEEP}}}
#gBar{{position:absolute;left:{BX}px;top:{BY}px;width:{BW}px;height:{BH}px;border-radius:36px;background:#fff;border:3px solid #A7DCC2;overflow:hidden}}
#gFill{{position:absolute;left:0;top:0;height:100%;width:0;background:{A.BRAND};border-radius:0 30px 30px 0}}
#gLinha{{position:absolute;left:{BX + BW - 3}px;top:{BY - 18}px;width:6px;height:{BH + 36}px;border-radius:3px;background:{A.INK}}}
#gNum{{position:absolute;left:84px;top:{BY + BH + 40}px;font-size:150px;font-weight:700;letter-spacing:-.055em;line-height:1;color:{A.INK};font-variant-numeric:tabular-nums;white-space:nowrap}}
#gNum small{{font-size:.3em;font-weight:600;letter-spacing:-.01em;color:{A.MUTED};margin-left:18px}}
#gNum .rs{{font-size:.36em;color:{A.MUTED};margin-right:.18em}}
.rc{{position:absolute;left:{BX}px;top:640px;height:80px;padding:0 28px;border-radius:999px;background:{A.INK};color:#fff;display:flex;align-items:center;gap:18px;
  white-space:nowrap;opacity:0}}
.rc i{{font-style:normal;font-size:30px;font-weight:600;color:{K.DARK_TEXTO}}}
.rc b{{font-size:34px;font-weight:700;color:{A.MENTA};font-variant-numeric:tabular-nums}}
#gOk{{position:absolute;left:{BX}px;top:{BY + BH + 230}px;height:96px;padding:0 36px 0 26px;border-radius:999px;background:{A.BRAND};color:#fff;display:flex;align-items:center;gap:14px;
  font-size:44px;font-weight:700;letter-spacing:-.02em;opacity:0}}
/* cena da meta mês a mês */
"""

CORPO = f"""
<div class="cena papel" id="cenaTela">
  <div class="tit" id="t1">Em Orçamentos, <b>Definir limites</b> e a aba <b>Receitas</b>.</div>
  <div class="tit" id="t2">Uma meta por mês: <b>R$ 1.000</b> em Outras receitas.</div>
  <div class="tit" id="t3">Fevereiro até aqui: <b>faltam R$ 250.</b></div>
  <div class="tit" id="t4">Entrou mais um trabalho? <b>Lance a receita.</b></div>
  <div class="tit" id="t5"><b>Meta cumprida.</b> No mês seguinte, a barra recomeça.</div>
  <div class="nota" id="nota">{K.NOTA}<br>Conta de exemplo só com a renda extra.</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA, 390, 1000)}</div>
</div>

<div class="cena suave" id="g">
  <div class="eyebrow">Renda extra</div>
  <div id="gT">Tem renda extra? <b>Ponha uma meta.</b></div>
  <div id="gMeta">meta <span>R$ 1.000</span></div>
  <div id="gBar"><div id="gFill"></div></div>
  <div id="gLinha"></div>
  <div id="gNum"><span class="rs">R$</span><span id="gV">0</span><small>de R$ 1.000 no mês</small></div>
  {chips}
  <div id="gOk">{CHECK}Meta cumprida</div>
</div>

{K.fim("Orçamentos no timtimcash")}
"""

JS = f"""
const H_SAI={H_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T4={list(T4)}, T5={list(T5)}, J_SAI={J_SAI}, FIM={FIM};
const TQ_DEF={TQ_DEF}, TQ_ABA={TQ_ABA}, TECLAS={TECLAS}, TQ_SALVAR={TQ_SALVAR}, TQ_MAIS={TQ_MAIS}, TQ_VALOR={TQ_VALOR}, TQ_SUG={TQ_SUG}, TQ_LANCAR={TQ_LANCAR};
const TR={TR}, IDS={IDS}, BW={BW};
poeAnel('aDef', {folga(DEFINIR, 3)}, 6); poeAnel('aAba', {folga(ABA_REC, 6, 4)}, 6); poeAnel('aCampo', {folga(LINHA_OR, 6)}, 6);
poeAnel('aItem', {folga(ITEM, 6)}, 6); poeAnel('aSug', {folga(SUG, 3)}, 6); poeAnel('aItem2', {folga(ITEM, 6)}, 6);
poeToque('tqDef', ...{centro(DEFINIR)}); poeToque('tqAba', ...{centro(ABA_REC)}); poeToque('tqCampo', ...{centro(CAMPO)});
poeToque('tqSalvar', ...{centro(SALVAR)}); poeToque('tqMais', 352, 958); poeToque('tqValor', 195, {round(VALOR_F[1] + VALOR_F[3] + 18, 1)});
poeToque('tqSug', ...{centro(SUG)}); poeToque('tqLancar', ...{centro(LANCAR)});
// câmera: [_, _, fx, fy, zoom] em px CSS do celular
const FY_PAINEL = {round(ITEM[1] + ITEM[3] / 2 - 40, 1)};
const CAM = [[0,0,195,300,1], [4.1,4.5,195,{round(ABA_REC[1] + 160, 1)},1], [5.1,5.45,195,{round(CAMPO[1] + 40, 1)},1], [7.0,7.35,195,{min(750, round(SALVAR[1] - 120, 1))},1],
             [7.85,8.3,195,FY_PAINEL,1.12], [10.85,10.86,195,FY_PAINEL,1], [11.05,11.45,195,{round(VALOR_F[1] + 170, 1)},1], [12.5,12.8,195,{min(750, round(LANCAR[1] - 180, 1))},1],
             [13.15,13.5,195,FY_PAINEL,1.12]];
function render(t){{
  // 1. gancho: as receitas extras enchem a barra até a meta de R$ 1.000
  saiCima('g', t, H_SAI);
  const passos = [[-.1, .45, 450], [.55, 1.0, 300], [1.15, 1.6, 250]];
  let total = 0;
  passos.forEach(([a, b, v], k) => {{ total += v*pout(t, a, b); const e = $('rc'+k);
    const q = prog(t, a+.05, b); e.style.opacity = Math.min(lin(t, a-.25, a-.05), 1 - prog(t, b-.12, b+.05));
    e.style.transform = `translate(${{(BW*(total/1000) - 40)*q*0}}px, ${{(255*q).toFixed(1)}}px) scale(${{1 - .25*q}})`; }});
  $('gFill').style.width = (BW*total/1000) + 'px';
  $('gV').textContent = fmt(total, 0);
  const ok = pback(t, 1.65, 2.1); $('gOk').style.opacity = lin(t, 1.65, 1.8); $('gOk').style.transform = `scale(${{.7 + .3*ok}})`;
  $('gLinha').style.background = t >= 1.6 ? '{A.BRAND}' : '{A.INK}';
  // 2. a tela real: Definir limites, a meta, o painel, a receita e a meta cumprida
  titulo('t1', t, T1[0], T1[1]); titulo('t2', t, T2[0], T2[1]); titulo('t3', t, T3[0], T3[1]); titulo('t4', t, T4[0], T4[1]); titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, H_SAI+.1, J_SAI);
  const ne = prog(t, H_SAI+.1, H_SAI+.7); $('nota').style.opacity = ne*(1 - prog(t, J_SAI, J_SAI+.4)); $('nota').style.transform = `translateY(${{(1-ne)*80}}px)`;
  camera('tela', t, CAM);
  fotos(IDS, t, TR);
  anel('aDef', t, 3.2, TQ_DEF-.05); toque('tqDef', t, TQ_DEF);
  anel('aAba', t, 4.45, TQ_ABA-.05); toque('tqAba', t, TQ_ABA);
  toque('tqCampo', t, 5.75); anel('aCampo', t, 6.9, 7.45); toque('tqSalvar', t, TQ_SALVAR);
  anel('aItem', t, 8.6, 10.5);
  toque('tqMais', t, TQ_MAIS); toque('tqValor', t, TQ_VALOR); anel('aSug', t, 11.75, TQ_SUG-.05); toque('tqSug', t, TQ_SUG); toque('tqLancar', t, TQ_LANCAR);
  anel('aItem2', t, 14.0, 16.0);
  // 3. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo('verde')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Renda extra</div>
    <div class="h1" style="font-size:132px;line-height:.95;margin-top:34px">Ponha uma meta.</div>
  </div>
  <div style="position:absolute;left:90px;top:880px;width:900px;font-size:42px;font-weight:700;letter-spacing:-.02em;display:flex;justify-content:space-between">
    <span>Outras receitas</span><span>100%</span></div>
  <div style="position:absolute;left:90px;top:950px;width:900px;height:120px;border-radius:40px;background:{A.BRAND_DARK};overflow:hidden">
    <div style="position:absolute;left:0;top:0;width:100%;height:100%;background:#fff;border-radius:40px"></div></div>
  <div style="position:absolute;left:90px;top:1110px;font-size:64px;font-weight:700;letter-spacing:-.04em;white-space:nowrap">R$ 1.000 de R$ 1.000</div>
  <div style="position:absolute;left:90px;top:1230px;height:96px;padding:0 36px 0 26px;border-radius:999px;background:#fff;color:{A.BRAND_DARK};display:flex;align-items:center;gap:14px;
    font-size:44px;font-weight:700;letter-spacing:-.02em">{CHECK}Meta cumprida</div>"""
    return K.pagina_capa(corpo, "", fundo="verde")


if __name__ == "__main__":
    K.executar(pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
