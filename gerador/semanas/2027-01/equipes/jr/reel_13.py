# -*- coding: utf-8 -*-
"""Reel de 13/01/2027 (quarta) · "IPVA: 3% de desconto vale quanto ao mês?" · capa verde suave · equipe jr.

A REGRA E A SELIC FICAM NUM LUGAR SÓ (REGRA e SELIC, logo abaixo). Quando sair o decreto do IPVA 2027 ou um dado mais novo da
Selic, troque só ali (e refaça a conta, que tem assert), e o vídeo, a capa e as notas mudam juntos.
Fatos (FATOS.md, conferidos em 20/10/2026):
- Decreto estadual 70.087, de 12/11/2025 (IPVA 2026 de São Paulo): veículo usado pago à vista em janeiro com 3% de desconto
  (art. 1º); ou em 5 parcelas mensais, de janeiro a maio, sem desconto, para débito de 10 UFESPs ou mais (art. 3º). O decreto do
  IPVA 2027 ainda não tinha saído em 20/10/2026 (os de 2024, 2025 e 2026 saíram entre novembro e dezembro, todos com 3%).
- Meta da Selic: 13,75% ao ano, decisão do Copom de 16/09/2026 (Relatório de Política Monetária de setembro de 2026). Ao mês, a
  comparação é aproximada: a Selic acumulada em setembro de 2026 foi de 1,08% (série 4390 do Banco Central). Nota do revisor no fim
  de FATOS.md: dizer a data da decisão e chamar o número ao mês de aproximado; o Copom se reúne de novo em 03-04/11 e 08-09/12/2026.
A conta (assert abaixo): IPVA 2027 do exemplo, à vista, R$ 1.236,00 (a conta de exemplo: “IPVA 2027” em 20/01, Impostos e Taxas);
valor cheio = 1.236 ÷ 0,97 = R$ 1.274,23; 3% de 1.274,23 = R$ 38,23 (o desconto); 5 parcelas = 1.274,23 ÷ 5 = R$ 254,846 (R$ 254,85).
Taxa implícita (a 1ª parcela no mesmo dia do pagamento à vista, as outras de mês em mês): 1.236 = Σ (1.274,23 ÷ 5) ÷ (1 + i)^k,
k = 0 a 4 -> i = 1,547% ao mês (com as parcelas arredondadas de R$ 254,85, 1,548%) -> (1 + i)^12 − 1 = 20,22% ao ano. Na tela,
1,55% ao mês e 20,2% ao ano.
Tela real (captura_13.py, celular, relógio 13/01/2027 10:00, build 2026-10-19.5, cópia da conta sem mudança): Pendentes de janeiro,
“EM 7 DIAS · 20/01/2027”, “IPVA 2027 · Impostos e Taxas · Conta corrente · −R$ 1.236,00 · pendente”.

python3 reel_13.py  |  REEL_PREVIA="0 0.5 1 2.9 5 8 11 12.6 15 17.4 20" python3 reel_13.py
"""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comum as C
K, A = C.K, C.A

PASTA = "2027-01-13_reel-ipva-desconto-a-vista"
TRAB = C.trabalho("13")
TELAS = C.telas(PASTA)
SAIDA = C.saida(PASTA)
CX = C.caixas(PASTA)

# ---------------------------------------------------------------- A REGRA E A SELIC (trocar aqui)
REGRA = {"ano": 2026, "estado": "São Paulo", "sigla": "SP", "decreto": "Decreto 70.087/2025", "desconto": D("0.03"),
         "parcelas": 5, "meses": "de janeiro a maio", "fonte": "Decreto estadual 70.087/2025 (SP)"}
# Nota do revisor (FATOS.md, 20/10/2026): a Selic com a data da decisão do Copom; a comparação ao mês é aproximada (Selic acumulada no mês).
SELIC = {"meta": "13,75% ao ano", "copom": "16/09/2026", "mes": "setembro de 2026", "valor": D("1.08"),
         "fonte": "Banco Central: decisão do Copom de 16/09/2026 e Selic acumulada no mês (série 4390)"}

# ---------------------------------------------------------------- a conta
def q2(x):
    return x.quantize(D("0.01"), ROUND_HALF_UP)
AVISTA = D("1236.00")                                      # o IPVA 2027 da conta de exemplo, à vista
CHEIO = q2(AVISTA / (1 - REGRA["desconto"]))
assert CHEIO == D("1274.23") and q2(CHEIO * (1 - REGRA["desconto"])) == AVISTA
DESCONTO = q2(CHEIO * REGRA["desconto"])
assert DESCONTO == D("38.23") and CHEIO - AVISTA == DESCONTO
PARC = q2(CHEIO / REGRA["parcelas"])
assert PARC == D("254.85")

def taxa(parcela):
    lo, hi = 0.0, 0.2
    for _ in range(200):
        m = (lo + hi) / 2
        if sum(float(parcela) / (1 + m) ** k for k in range(REGRA["parcelas"])) - float(AVISTA) > 0:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2
I_EXATA, I_ARRED = taxa(CHEIO / REGRA["parcelas"]), taxa(PARC)
I_ANO = (1 + I_EXATA) ** 12 - 1
assert round(I_EXATA * 100, 3) == 1.547 and round(I_ANO * 100, 2) == 20.22        # os números do pedido
assert round(I_ARRED * 100, 2) == 1.55 == round(I_EXATA * 100, 2)                 # na tela: 1,55% ao mês
TAXA_TXT, ANO_TXT = "1,55", "20,2"
assert f"{I_EXATA * 100:.2f}".replace(".", ",") == TAXA_TXT and f"{I_ANO * 100:.1f}".replace(".", ",") == ANO_TXT
SELIC_TXT = C.brl(float(SELIC["valor"]))
assert SELIC["valor"] < D(str(round(I_EXATA * 100, 2)))                           # o desconto rende mais que a Selic do mês

# ---------------------------------------------------------------- tela real
P = CX["a-pendentes-janeiro.jpg"]
assert P["linha_ipva"][4] == "IPVA 2027 Impostos e Taxas·Conta corrente −R$ 1.236,00 pendente"
assert P["em7"][4] == "EM 7 DIAS" and P["data7"][4] == "· 20/01/2027" and "Janeiro 2027" in P["texto"]
assert "Jan 13 2027 10:0" in CX["relogio"] and not CX["erros"]
DATA7 = C.uniao(P["em7"][:4], P["data7"][:4])
LINHA = P["linha_ipva"][:4]

# ---------------------------------------------------------------- tempos (s)
H_SAI = 3.2
T1, T2, T3, T5, T6 = (3.25, 6.4), (6.45, 9.7), (9.75, 13.3), (13.35, 16.3), (16.35, 18.4)
FIM = 18.45
DUR = round(FIM + 2.75, 2)
CONCLUI = 11.35
EXTRA = K.aneis("aData", "aLinha")

# ---------------------------------------------------------------- desenhos
MESES = ["jan", "fev", "mar", "abr", "mai"]
COLW, GAP, X0 = 160, 20, 100
def grade():
    out = []
    for k, m in enumerate(MESES):
        x = X0 + k * (COLW + GAP)
        out.append(f'<div class="mes" style="left:{x}px">{m}</div>')
        if k == 0:
            out.append(f'<div class="blo av" id="av" style="left:{x}px">{C.brl(float(AVISTA), 0)}</div>')
        else:
            out.append(f'<div class="blo vz" style="left:{x}px"></div>')
        out.append(f'<div class="blo pc" id="pc{k}" style="left:{x}px">{C.brl(float(PARC))}</div>')
    return "".join(out)

def check(cor, tam=46, traco=3.2):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" stroke-linecap="round" '
            f'stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>')
ICO_DOC = (f'<svg width="92" height="92" viewBox="0 0 24 24" fill="none" stroke="{A.BRAND_DEEP}" stroke-width="1.8" stroke-linecap="round" '
           f'stroke-linejoin="round"><path d="M6.5 3.5h7.5l4 4v13h-11.5z"/><path d="M13.5 3.5v4.5h4.5"/><path d="M9 12h6M9 15.5h6M9 19h3.5"/></svg>')

CSS = f"""
.tit{{font-size:64px}}
#t2 b{{color:{K.CORAL_TXT}}}
#h{{background:{A.BG}}}
#hEye{{position:absolute;left:92px;top:292px}}
#q{{position:absolute;left:90px;top:346px;width:900px;font-size:96px;line-height:.98;font-weight:700;letter-spacing:-.05em;color:{A.INK};text-wrap:balance}}
#num{{position:absolute;left:76px;top:660px;font-size:290px;line-height:1;font-weight:700;letter-spacing:-.06em;color:{A.BRAND_DARK};font-variant-numeric:tabular-nums;white-space:nowrap}}
#numSub{{position:absolute;left:92px;top:960px;font-size:84px;line-height:1;font-weight:700;letter-spacing:-.04em;color:{A.INK}}}
#hSub{{position:absolute;left:92px;top:1110px;width:900px;font-size:42px;line-height:1.28;font-weight:500;letter-spacing:-.02em;color:{A.MUTED};opacity:0;text-wrap:balance}}
#hSub b{{color:{A.INK};font-weight:700}}
#hAno{{position:absolute;left:92px;top:1250px;opacity:0}}
.pil{{display:inline-flex;align-items:center;height:84px;padding:0 38px;border-radius:999px;background:{A.SOFT};color:{A.BRAND_DEEP};font-size:40px;font-weight:700;letter-spacing:-.02em}}
.pil.cor{{background:#F8E3DA;color:{K.CORAL_FORTE}}}
.cd{{position:absolute;left:90px;width:900px;padding:40px 48px;border-radius:36px;background:#fff;border:2px solid {A.FIO};opacity:0;
  box-shadow:0 1px 2px rgba(15,20,16,.04),0 14px 34px -16px rgba(15,20,16,.16)}}
.cd .rt{{font-size:32px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{A.MUTED}}}
.cd .vl{{margin-top:18px;font-size:124px;font-weight:700;letter-spacing:-.05em;line-height:1;color:{A.INK}}}
.cd .vl .rs,.cd .vl .cts{{color:{A.MUTED}}}
.cd .sb{{margin-top:14px;font-size:42px;font-weight:500;letter-spacing:-.02em;color:{A.MUTED}}}
.cd.verde .vl{{color:{A.BRAND_DARK}}}
#cdA{{top:620px}}
#cdB{{top:1010px}}
#rodape{{position:absolute;left:92px;top:1450px;width:900px;font-size:34px;line-height:1.3;font-weight:500;letter-spacing:-.01em;color:{A.MUTED};opacity:0}}
#gr{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}}
.rot{{position:absolute;left:{X0}px;font-size:30px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{A.MUTED}}}
.mes{{position:absolute;top:640px;width:{COLW}px;text-align:center;font-size:38px;font-weight:600;color:{A.MUTED}}}
.blo{{position:absolute;width:{COLW}px;height:190px;border-radius:30px;display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:700;
  letter-spacing:-.03em;font-variant-numeric:tabular-nums}}
.blo.av{{top:780px;background:{A.BRAND};color:#fff;font-size:44px}}
.blo.vz{{top:780px;border:4px dashed {A.NEUTRO}}}
.blo.pc{{top:1080px;background:{A.CORAL};color:#fff}}
#grTxt{{position:absolute;left:92px;top:1320px;width:900px;font-size:44px;line-height:1.28;font-weight:500;letter-spacing:-.02em;color:{A.MUTED};opacity:0;text-wrap:balance}}
#grTxt b{{color:{A.INK};font-weight:700}}
#grAno{{position:absolute;left:92px;top:1470px;opacity:0}}
.bx{{position:absolute;left:90px;width:900px;opacity:0}}
.bx .lb{{display:flex;align-items:baseline;justify-content:space-between;font-size:46px;font-weight:600;letter-spacing:-.025em;color:{A.INK}}}
.bx .lb b{{font-size:84px;font-weight:700;letter-spacing:-.04em}}
.bx .tr{{margin-top:18px;height:90px;border-radius:45px;background:{A.FIO};overflow:hidden}}
.bx .tr i{{display:block;height:100%;width:0;border-radius:45px}}
#bxS{{top:640px}}
#bxS .lb b{{color:{A.BRAND_DARK}}}
#bxS .tr i{{background:{A.BRAND}}}
#bxI{{top:920px}}
#bxI .lb b{{color:{K.CORAL_TXT}}}
#bxI .tr i{{background:{A.CORAL}}}
#fonteS{{position:absolute;left:92px;top:1170px;width:900px;font-size:32px;line-height:1.3;font-weight:500;color:{A.MUTED};opacity:0}}
#conc{{position:absolute;left:90px;top:1310px;width:900px;display:flex;align-items:center;gap:28px;font-size:64px;line-height:1.06;font-weight:700;
  letter-spacing:-.04em;color:{A.BRAND_DARK};opacity:0;text-wrap:balance}}
#conc i{{flex:none;width:96px;height:96px;border-radius:50%;background:{A.BRAND};display:flex;align-items:center;justify-content:center}}
#regra{{position:absolute;left:90px;top:660px;width:900px;opacity:0}}
#regra .ic{{width:160px;height:160px;border-radius:44px;background:{A.SOFT};display:flex;align-items:center;justify-content:center}}
#regra .tx{{margin-top:50px;font-size:56px;line-height:1.28;font-weight:500;letter-spacing:-.02em;color:{A.MUTED};text-wrap:balance}}
#regra .tx b{{color:{A.INK};font-weight:700}}
"""

CORPO = f"""
<div class="cena papel" id="telas">
  <div class="tit" id="t1">O IPVA do exemplo, de <b>dois jeitos</b>:</div>
  <div class="cd verde" id="cdA"><div class="rt">À vista, em janeiro</div><div class="vl">{C.din(C.brl(float(AVISTA)))}</div>
    <div class="sb">com {int(REGRA["desconto"] * 100)}% de desconto</div></div>
  <div class="cd" id="cdB"><div class="rt">Em {REGRA["parcelas"]} parcelas, {REGRA["meses"]}</div><div class="vl">{REGRA["parcelas"]} × {C.din(C.brl(float(PARC)))}</div>
    <div class="sb">valor cheio: R$ {C.brl(float(CHEIO))}</div></div>
  <div id="rodape">Regra de {REGRA["estado"]} para o IPVA {REGRA["ano"]} ({REGRA["decreto"]}).</div>

  <div class="tit" id="t2">Parcelar custa <b>{TAXA_TXT}% ao mês</b>.</div>
  <div id="gr">
    <div class="rot" style="top:730px">À vista</div>
    <div class="rot" style="top:1030px">{REGRA["parcelas"]} parcelas</div>
    {grade()}
  </div>
  <div id="grTxt">Quem parcela abre mão de <b>R$ {C.brl(float(DESCONTO))}</b> de desconto e paga aos poucos.</div>
  <div id="grAno"><span class="pil cor">≈ {ANO_TXT}% ao ano</span></div>

  <div class="tit" id="t3">E o dinheiro guardado, rende quanto?</div>
  <div class="bx" id="bxS"><div class="lb"><span>Selic, {SELIC["meta"]}</span><b>≈ {SELIC_TXT}%</b></div><div class="tr"><i id="brS"></i></div></div>
  <div class="bx" id="bxI"><div class="lb"><span>Parcelar o IPVA</span><b>{TAXA_TXT}%</b></div><div class="tr"><i id="brI"></i></div></div>
  <div id="fonteS">Ao mês. Selic de {SELIC["meta"]}, decisão do Copom de {SELIC["copom"]}; ao mês, cerca de {SELIC_TXT}% (Selic acumulada em {SELIC["mes"]}, série 4390 do Banco Central).</div>
  <div id="conc"><i>{check("#fff", 50)}</i>Com o dinheiro na mão, o desconto rende mais.</div>

  <div class="tit" id="t5">No exemplo, o IPVA à vista já está em <b>Pendentes</b>.</div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{C.camadas("tela", [("fa", os.path.join(TELAS, "a-pendentes-janeiro.jpg"))], EXTRA)}</div>

  <div class="tit" id="t6">Regra de {REGRA["sigla"]} em {REGRA["ano"]}: confira a sua.</div>
  <div id="regra"><div class="ic">{ICO_DOC}</div>
    <div class="tx"><b>{REGRA["decreto"]}</b>: {int(REGRA["desconto"] * 100)}% à vista em janeiro ou até {REGRA["parcelas"]} parcelas, {REGRA["meses"]}.
    Confira a regra de {REGRA["ano"] + 1} e a do seu estado.</div></div>
</div>

<div class="cena papel" id="h">
  <div class="eyebrow" id="hEye">IPVA · {REGRA["estado"]}</div>
  <div id="q">{int(REGRA["desconto"] * 100)}% de desconto vale quanto ao mês?</div>
  <div id="num"><span id="numV">0,00</span>%</div>
  <div id="numSub">ao mês</div>
  <div id="hSub">No IPVA do exemplo: à vista com {int(REGRA["desconto"] * 100)}% ou em <b>{REGRA["parcelas"]} parcelas</b>.</div>
  <div id="hAno"><span class="pil">≈ {ANO_TXT}% ao ano</span></div>
</div>

{K.fim("Pendentes no timtimcash")}
"""

JS = f"""
const H_SAI={H_SAI}, T1={list(T1)}, T2={list(T2)}, T3={list(T3)}, T5={list(T5)}, T6={list(T6)}, FIM={FIM}, CONCLUI={CONCLUI};
const TAXA={round(I_EXATA * 100, 2)}, LS={round(900 * float(SELIC["valor"]) / (I_EXATA * 100), 1)};
poeAnel('aData', {DATA7}, 8); poeAnel('aLinha', {LINHA}, 6);
function render(t){{
  // 1. gancho: a pergunta e o número
  const v = TAXA*pout(t, .04, .7); $('numV').textContent = fmt(v, 2);
  $('num').style.transform = `scale(${{1 + .05*Math.sin(Math.PI*clamp((t-.7)/.35, 0, 1))}})`;
  $('num').style.transformOrigin = '0 70%';
  aparece('hSub', t, 1.0, 0, 18, .4); aparece('hAno', t, 1.5, 0, 18, .4);
  $('q').style.transform = `translateY(${{-10*pout(t, 0, 1.2)}}px)`;
  saiCima('h', t, H_SAI);
  // 2. os dois jeitos de pagar
  titulo('t1', t, T1[0], T1[1]);
  some('cdA', t, T1[0]+.2, T1[1]); some('cdB', t, T1[0]+.5, T1[1]); some('rodape', t, T1[0]+.9, T1[1], 12);
  // 3. parcelar custa 1,55% ao mês: os meses de janeiro a maio
  titulo('t2', t, T2[0], T2[1]);
  $('gr').style.opacity = Math.min(prog(t, T2[0]+.05, T2[0]+.35), 1 - prog(t, T2[1], T2[1]+.3));
  const av = $('av'); av.style.transform = `scale(${{.6 + .4*pback(t, T2[0]+.25, T2[0]+.65)}})`; av.style.opacity = lin(t, T2[0]+.25, T2[0]+.4);
  [0,1,2,3,4].forEach(k => {{ const e = $('pc'+k), a = T2[0]+.55+.16*k; e.style.opacity = lin(t, a, a+.12); e.style.transform = `scale(${{.6 + .4*pback(t, a, a+.4)}})`; }});
  some('grTxt', t, T2[0]+1.45, T2[1], 16); some('grAno', t, T2[0]+1.8, T2[1], 16);
  // 4. a Selic do mês contra o custo de parcelar
  titulo('t3', t, T3[0], T3[1]);
  some('bxS', t, T3[0]+.2, T3[1]); some('bxI', t, T3[0]+.4, T3[1]);
  $('brS').style.width = (LS*pout(t, T3[0]+.35, T3[0]+1.15))+'px'; $('brI').style.width = (900*pout(t, T3[0]+.55, T3[0]+1.35))+'px';
  some('fonteS', t, T3[0]+.9, T3[1], 12);
  const cc = $('conc'); cc.style.opacity = Math.min(lin(t, CONCLUI, CONCLUI+.2), 1 - prog(t, T3[1], T3[1]+.3));
  cc.style.transform = `translateY(${{(1-pout(t, CONCLUI, CONCLUI+.45))*30}}px)`;
  // 5. tela real: Pendentes
  titulo('t5', t, T5[0], T5[1]);
  janela('janela', t, T5[0], T5[1]); janela('nota', t, T5[0], T5[1]);
  pan('tela', 350);
  anel('aData', t, T5[0]+.7, T5[0]+1.6); anel('aLinha', t, T5[0]+1.55, T5[1]);
  // 6. a regra
  titulo('t6', t, T6[0], T6[1]); some('regra', t, T6[0]+.15, FIM-.05, 24);
  // 7. fechamento verde
  sobe('fim', t, FIM);
}}
"""


def capa():
    corpo = f"""{K.logo("suave")}
  <div class="eyebrow" style="position:absolute;left:90px;top:430px">IPVA</div>
  <div class="h1" style="position:absolute;left:90px;top:494px;width:900px;font-size:140px;line-height:.96;color:{A.INK}">{int(REGRA["desconto"] * 100)}% vale quanto?</div>
  <div style="position:absolute;left:78px;top:900px;font-size:290px;line-height:1;font-weight:700;letter-spacing:-.06em;color:{A.BRAND_DEEP};font-variant-numeric:tabular-nums">{TAXA_TXT}%</div>
  <div style="position:absolute;left:92px;top:1210px;font-size:96px;line-height:1;font-weight:700;letter-spacing:-.04em;color:{A.INK}">ao mês</div>"""
    return K.pagina_capa(corpo, "", fundo="suave")


HTML = C.pagina(CORPO, CSS, JS)
CAPA = capa()

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, TRAB, capa_html=CAPA)
