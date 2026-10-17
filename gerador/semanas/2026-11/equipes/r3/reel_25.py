# -*- coding: utf-8 -*-
"""Reel de 25/11/2026 · "Atualize a carteira em 30 segundos" (1080 × 1920, 30 fps, 21,2 s). Capa da grade: papel.

Telas reais: capturas/captura_25.py, build 2026-10-16.1 do site, celular 390 × 760 em escala 3, conta fictícia (N/base_app), relógio da página em
15/10/2026 15:00 e a resposta da PTAX real de 15/10/2026 (PTAX_15_10 do kit de captura: compra R$ 5,0515, carimbo 13:00).
Passo a passo: Remessas (US$ 13.200 a R$ 5,50, "Atualizar · há 15 dias") -> toque em Atualizar -> digita 1324000
(máscara em centavos: 0,01 ... 13.240,00) -> "usar a cotação de hoje · R$ 5,0515" -> Salvar -> Remessas com
US$ 13.240 e R$ 66.881,86 ao câmbio de hoje (R$ 5,0515). Conta: 13.240 × 5,0515 = 66.881,86.

python3 reel_25.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_25.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r3kit import K, A, camadas, cronometro, JS_R3, saida, trabalho

PASTA = "2026-11-25_reel-atualizar-carteira"
SAIDA = saida(PASTA)
TELAS = os.path.join(SAIDA, "telas")
TRAB = trabalho("25")
CX = json.load(open(os.path.join(TELAS, "caixas.json"), encoding="utf-8"))
for _k in [k for k in CX if k.startswith("texto") or k == "toast"]:
    CX[_k] = CX[_k].replace("\xa0", " ")         # o site separa "R$" do número com espaço fixo
def tela(n): return os.path.join(TELAS, n)

DUR = 21.2
# conferências dos números que aparecem nos títulos (tirados da tela capturada)
assert "13.200 na carteira hoje" in CX["texto_antes"] and "R$ 72.600,00 ao câmbio de hoje (R$ 5,50)" in CX["texto_antes"]
assert "PTAX de compra do Banco Central, de 15/10/2026 às 13:00." in CX["texto_modal"]
assert "Equivale hoje a\nR$ 66.881,86" in CX["texto_cotacao"] and "PTAX de hoje ✓" in CX["texto_cotacao"]
assert "13.240 na carteira hoje" in CX["texto_depois"] and "R$ 66.881,86 ao câmbio de hoje (R$ 5,0515)" in CX["texto_depois"]
assert round(13240 * 5.0515, 2) == 66881.86

# ---------------------------------------------------------------- posições (px CSS do celular)
c1 = CX["celular-remessas-1-antes.jpg"]
c3 = CX["celular-remessas-3-digitado.jpg"]
c4 = CX["celular-remessas-4-cotacao-de-hoje.jpg"]
ATUALIZAR = c1["atualizar"]                                   # "Atualizar · há 15 dias"
LINHA = c3["linha"]                                           # linha da Corretora com o valor
BOTAO_DICA = [c3["botao_cot"][0], c3["botao_cot"][1], c3["dica"][2], round(c3["dica"][1] + c3["dica"][3] - c3["botao_cot"][1], 1)]
EQUIVALE = c4["equivale"]                                     # "Equivale hoje a R$ 66.881,86"
SALVAR = c4["salvar"]
CARTAO_NUM = [22, 193, 346, 153]                              # US$ 13.240 + as duas pílulas + a linha em reais (build 2026-10-16.1)
def centro(b): return [round(b[0] + b[2] / 2, 1), round(b[1] + b[3] / 2, 1)]

# ---------------------------------------------------------------- tempos (s)
T0C = -0.4          # o cronômetro já corre no quadro 0
TSALVA = 12.85      # toque em Salvar: o cronômetro para (0:17)
SUM = 15.75         # cena do resumo
FIM = 18.4          # fechamento verde
TIP = [5.65, 5.85, 6.05, 6.25, 6.45, 6.65, 6.85]   # uma tecla por vez

# ---------------------------------------------------------------- corpo
IMGS = [("iA0", tela("celular-remessas-1-antes.jpg")), ("iB", tela("celular-remessas-2-atualizar-carteira.jpg"))] + \
       [(f"iC{i}", tela(f"celular-remessas-3-digitando-{i}.jpg")) for i in range(1, 8)] + \
       [("iD", tela("celular-remessas-3-digitado.jpg")), ("iE", tela("celular-remessas-4-cotacao-de-hoje.jpg")),
        ("iF", tela("celular-remessas-5-salvo.jpg")), ("iG", tela("celular-remessas-6-depois.jpg"))]
EXTRA = K.aneis("aAtu", cor="ambar") + K.aneis("aLinha", "aDica", "aEquiv", "aCartao") + K.toques("tqAtu", "tqCot", "tqSalvar")

CSS = f"""
.tit{{width:700px}}
#gancho{{position:absolute;left:90px;top:330px;width:900px}}
#gancho .h1{{font-size:104px;line-height:.98;margin-top:34px;text-wrap:balance}}
#crono{{position:absolute;left:826px;top:286px;width:168px;height:184.8px;transform-origin:84px 100.8px;will-change:transform}}
#pulso{{position:absolute;left:0;top:0;width:560px;height:560px;margin:-280px 0 0 -280px;border-radius:50%;border:5px solid {A.BRAND};opacity:0}}
#resumo{{position:absolute;left:90px;top:600px;width:900px}}
.eq{{background:#fff;border:2px solid {A.FIO};border-radius:40px;padding:22px 52px;
  box-shadow:0 1px 2px rgba(15,20,16,.04),0 18px 40px -20px rgba(15,20,16,.18)}}
.eq-l{{display:flex;align-items:baseline;gap:26px;padding:30px 0;border-bottom:3px solid {A.FIO}}}
.eq-l:last-child{{border-bottom:0}}
.eq-op{{width:58px;flex:none;font-size:76px;font-weight:700;color:{A.MUTED};letter-spacing:-.04em;text-align:center}}
.eq-v{{font-size:92px;font-weight:700;letter-spacing:-.05em;line-height:1;font-variant-numeric:tabular-nums;white-space:nowrap}}
.eq-r{{font-size:32px;font-weight:600;color:{A.MUTED};letter-spacing:-.015em;line-height:1.25;margin-top:12px}}
.eq-c{{display:flex;flex-direction:column}}
#rNota{{font-size:30px;font-weight:500;color:{A.MUTED};margin-top:30px;letter-spacing:-.01em}}
"""

CORPO = f"""
<div class="cena papel" id="papel">
  <div id="gancho">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1">Quanto vale <span style="color:{A.BRAND_DARK}">hoje</span> o que você tem lá fora?</div>
  </div>
  <div class="tit" id="t1">Em Remessas, toque em <b>Atualizar</b>.</div>
  <div class="tit" id="t2">Digite quanto você tem lá fora: <b>US$&nbsp;13.240</b>.</div>
  <div class="tit" id="t3">O site sugere a <b>PTAX de compra</b> do Banco Central.</div>
  <div class="tit" id="t4">Com a PTAX, a carteira vale <b>R$&nbsp;66.881,86</b>.</div>
  <div class="tit" id="t5">Pronto: carteira <b>atualizada</b>, em dólar e em reais.</div>
  <div class="tit" id="t6">Em dólar e em reais, com a <b>PTAX</b> do Banco Central.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>
  <div id="resumo" style="opacity:0">
    <div class="eq">
      <div class="eq-l" id="e1"><span class="eq-op"></span><div class="eq-c"><span class="eq-v">US$ 13.240,00</span><span class="eq-r">na carteira lá fora</span></div></div>
      <div class="eq-l" id="e2"><span class="eq-op">×</span><div class="eq-c"><span class="eq-v" style="color:{A.BRAND_DARK}">R$ 5,0515</span><span class="eq-r">PTAX de compra do Banco Central, 15/10/2026</span></div></div>
      <div class="eq-l" id="e3"><span class="eq-op">=</span><div class="eq-c"><span class="eq-v num" id="eqRS" style="color:{A.BRAND_DARK}">R$ 66.881,86</span><span class="eq-r">em reais</span></div></div>
    </div>
    <div id="rNota">Mesma conta de exemplo da tela real.</div>
  </div>
  <div id="pulso"></div>
  <div id="crono">{cronometro("cr")}</div>
</div>

{K.fim("Remessas ao exterior no timtimcash")}
"""

JS = JS_R3 + f"""
const T0C={T0C}, TSALVA={TSALVA}, SUM={SUM}, FIM={FIM}, TIP={TIP};
poeAnel('aAtu', {ATUALIZAR}, 12); poeToque('tqAtu', ...{centro(ATUALIZAR)});
poeAnel('aLinha', {LINHA}, 8);
poeAnel('aDica', {BOTAO_DICA}, 12); poeToque('tqCot', ...{centro(c3["botao_cot"])});
poeAnel('aEquiv', {EQUIVALE}, 12); poeToque('tqSalvar', ...{centro(SALVAR)});
poeAnel('aCartao', {CARTAO_NUM}, 6);
// cronômetro: grande no gancho (centro em 540, 1150), depois no canto de cima (centro em 910, 386,8)
const GX = 540-910, GY = 1150-386.8, GS = 560/168;
function render(t){{
  // 1. gancho: a pergunta e o cronômetro que já corre
  const sai = prog(t, 2.25, 2.6);
  $('gancho').style.opacity = 1 - sai;
  $('gancho').style.transform = `translateY(${{-6*lin(t,0,2.25) - 60*sai}}px)`;
  const vai = prog(t, 2.25, 2.85);
  const resp = 1 + .018*Math.sin(t*Math.PI*2)*(1-vai);           // o cronômetro "respira" a cada segundo
  $('crono').style.transform = `translate(${{GX*(1-vai)}}px, ${{GY*(1-vai)}}px) scale(${{(GS + (1-GS)*vai)*resp}})`;
  $('crRot').style.opacity = 1 - prog(t, 2.3, 2.6);
  // pulso: um anel sai do mostrador a cada segundo, só no gancho
  const fr = ((t - T0C) % 1 + 1) % 1, pz = $('pulso');
  pz.style.left = '540px'; pz.style.top = '1150px';
  pz.style.opacity = t < 2.2 ? (1-fr)*.55 : 0; pz.style.transform = `scale(${{.86 + .3*fr}})`;
  cronometro('cr', t, T0C, 30, TSALVA);
  const ok = pback(t, TSALVA+.12, TSALVA+.5);
  $('crOk').style.opacity = lin(t, TSALVA+.12, TSALVA+.25); $('crOk').style.transformBox = 'fill-box';
  $('crOk').style.transformOrigin = 'center'; $('crOk').style.transform = `scale(${{.4 + .6*ok}})`;

  // 2. títulos
  // cada título só entra depois que o anterior saiu (saída de 0,3 s)
  titulo('t1', t, 2.55, 4.95); titulo('t2', t, 5.25, 7.95); titulo('t3', t, 8.25, 10.75);
  titulo('t4', t, 11.05, 13.25); titulo('t5', t, 13.55, SUM-.05); titulo('t6', t, SUM+.22, FIM+.5);

  // 3. janela: entra, encolhe para o campo enquanto a pessoa digita (o teclado do celular cobriria o resto) e volta
  const ent = prog(t, 2.45, 3.0), saiJ = prog(t, SUM-.1, SUM+.3);
  // enc: 0 = janela normal (780 × 1000, 1 px CSS = 2 px); 1 = recorte do campo (860 × 650, com zoom de 1,15)
  const enc = prog(t, 5.15, 5.6) * (1 - prog(t, 7.3, 7.85));
  const J = $('janela');
  J.style.opacity = Math.min(ent, 1-saiJ); $('nota').style.opacity = Math.min(ent, 1-saiJ);
  J.style.height = (1000 - 350*enc) + 'px'; J.style.width = (780 + 80*enc) + 'px'; J.style.left = (150 - 40*enc) + 'px';
  J.style.transform = `translateY(${{(1-ent)*80 + 175*enc - saiJ*40}}px)`;
  $('nota').style.transform = `translateY(${{(1-ent)*80 - saiJ*40}}px)`;
  // camadas (troca seca, como na tela de verdade; fusão curta onde o site anima)
  op('iA0', 1);
  op('iB', prog(t, 4.75, 4.95));
  TIP.forEach((a,i) => op('iC'+(i+1), t >= a ? 1 : 0));
  op('iD', t >= 7.15 ? 1 : 0);
  op('iE', prog(t, 10.32, 10.5));
  op('iF', prog(t, 13.02, 13.22));
  op('iG', prog(t, 14.05, 14.35));
  // panorâmica (topo da janela, em px CSS)
  let topo = 0;
  topo += 62*prog(t, 5.15, 5.6);                  // recorte do campo (do título do modal ao "Adicionar banco")
  topo += (250-62)*prog(t, 7.35, 7.9);            // câmbio, sugestão e dica
  topo += (180-250)*prog(t, 12.95, 13.35);        // de volta a Remessas, com o aviso
  topo += (118-180)*prog(t, 14.0, 14.5);          // o cartão inteiro
  const z = 1 + .15*enc, esq = 8*enc;
  $('tela').style.transform = `translate(${{-esq*E*z}}px, ${{-topo*E*z}}px) scale(${{z}})`;
  // anéis e toques
  anel('aAtu', t, 3.3, 4.45); toque('tqAtu', t, 4.55);
  anel('aLinha', t, 5.45, 7.25);
  anel('aDica', t, 8.35, 9.95); toque('tqCot', t, 10.15);
  anel('aEquiv', t, 10.85, 12.55); toque('tqSalvar', t, 12.85);
  anel('aCartao', t, 14.45, SUM-.15);

  // 4. resumo: a conta em dólar e em reais
  const r0 = prog(t, SUM+.05, SUM+.45);
  $('resumo').style.opacity = r0; $('resumo').style.transform = `translateY(${{(1-r0)*40}}px)`;
  ['e1','e2','e3'].forEach((id,i) => {{ const p = prog(t, SUM+.2+i*.32, SUM+.6+i*.32);
    $(id).style.opacity = p; $(id).style.transform = `translateX(${{(1-p)*-40}}px)`; }});
  contar('eqRS', t, SUM+1.0, SUM+1.7, 0, 66881.86, 2, 'R$ ');
  $('rNota').style.opacity = prog(t, SUM+1.5, SUM+1.9);

  // 5. fechamento verde
  sobe('fim', t, FIM);
}}
"""

def capa():
    corpo = f"""{K.logo('papel')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">Remessas ao exterior</div>
    <div class="h1" style="font-size:116px;line-height:.97;margin-top:34px;text-wrap:balance">Atualize a carteira em <span style="color:{A.BRAND_DARK}">30 segundos</span></div>
  </div>
  <div style="position:absolute;left:250px;top:880px;width:580px;height:638px">{cronometro("cc")}</div>"""
    css = """#ccRot{font-size:17px}"""
    return K.pagina_capa(corpo, css, fundo="papel")

if __name__ == "__main__":
    K.executar(K.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
