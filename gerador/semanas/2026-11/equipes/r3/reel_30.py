# -*- coding: utf-8 -*-
"""Reel de 30/11/2026 · "Hoje: último dia da 1ª parcela" (1080 × 1920, 30 fps, 20,7 s). Capa da grade: tinta.

- 0 a 2,5 s (tinta): uma folhinha de calendário vira (26, 27, 28, 29) e para em 30 de novembro, segunda-feira, com
  "Último dia da 1ª parcela do 13º." (Lei 4.749/1965, art. 2º: a 1ª parcela sai entre fevereiro e novembro.)
- 2,5 a 6,8 s (tinta): "Ela vem cheia: metade do salário, sem INSS e sem IR." e "Os descontos ficam para a 2ª parcela."
  Barra do 13º do exemplo (R$ 9.960): 1ª parcela R$ 4.980 cheia; 2ª até 20/12, com INSS e IR do 13º inteiro
  (Lei 8.134/1990, art. 16; Decreto 3.048/1999, art. 214, §6º). A folha vira para cima e revela o papel.
- telas reais (capturas/captura_30.py, build 2026-10-16.1 do site, celular em escala 3, relógio da página em 30/11/2026 10:00):
  Visão geral com Receitas R$ 14.940,00 -> "+" -> "Transferência" -> R$ 2.000,00 -> Para "Reserva" ->
  "Registrar transferência" -> "Transferência adicionada".
- 14,1 a 17,4 s: Minhas contas, antes e depois: Reserva de R$ 33.000,00 para R$ 35.000,00; Conta corrente de
  R$ 18.849,20 para R$ 16.849,20; patrimônio total igual (R$ 111.849,20).
- 17,4 s: fechamento verde "Transferências no timtimcash".
python3 reel_30.py  |  REEL_PREVIA="0 0.5 1 3 6 10 14 18" python3 reel_30.py
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r3kit import K, A, camadas, JS_R3, saida, trabalho

PASTA = "2026-11-30_reel-ultimo-dia-da-primeira-parcela"
SAIDA = saida(PASTA)
TELAS = os.path.join(SAIDA, "telas")
TRAB = trabalho("30")
CX = json.load(open(os.path.join(TELAS, "caixas.json"), encoding="utf-8"))
for _k in [k for k in CX if k.startswith("texto") or k == "toast"]:
    CX[_k] = CX[_k].replace("\xa0", " ")
def tela(n): return os.path.join(TELAS, n)
DUR = 20.7

# conferências (texto lido da tela capturada)
assert "Reserva\nINVESTIMENTO\nR$ 33.000,00\nConta corrente\nR$ 18.849,20" in CX["texto_contas_antes"]
assert "Reserva\nINVESTIMENTO\nR$ 35.000,00\nConta corrente\nR$ 16.849,20" in CX["texto_contas_depois"]
assert "PATRIMÔNIO TOTAL\nR$ 111.849,20" in CX["texto_contas_antes"] and "PATRIMÔNIO TOTAL\nR$ 111.849,20" in CX["texto_contas_depois"]
assert "De\nConta corrente\nPara\nReserva" in CX["texto_form"] and CX["toast"] == "Transferência adicionada"
assert 9960 / 2 == 4980 and 9960 + 4980 == 14940

# ---------------------------------------------------------------- posições (px CSS do celular)
v1 = CX["celular-visao-geral-1-novembro.jpg"]
f1 = CX["celular-transferencia-1-nova-transacao.jpg"]
f2 = CX["celular-transferencia-2-tipo.jpg"]
f5 = CX["celular-transferencia-5-preenchida.jpg"]
pk = {n: [x, y, w, h] for n, x, y, w, h in CX["picker"]}
def centro(b): return [round(b[0] + b[2] / 2, 1), round(b[1] + b[3] / 2, 1)]
RECEITAS = v1["receitas"]                                   # "Receitas R$ 14.940,00"
FAB = v1["fab"]
TIPO = f1["transf"]                                         # aba "Transferência" (no formulário de despesa)
VALOR = f2["valor"]                                         # zona do valor
LF = {l[0].split(" ")[0]: l[1:] for l in CX["linhas_form"]}  # linhas da folha preenchida: Data, Já, De, Para, Remessa
assert CX["linhas_form"][2][0] == "De Conta corrente" and CX["linhas_form"][3][0] == "Para Reserva"
DE_PARA = [9, LF["De"][1], 372, round(LF["Para"][1] + LF["Para"][3] - LF["De"][1], 1)]   # linhas De e Para
PARA = LF["Para"]                                           # linha "Para" (a mesma posição antes de escolher)
RESERVA_PK = pk["Reserva"]
BOTAO = f5["botao"]
LINHA_RESERVA = [30, 336, 334, 64]                          # linha da Reserva em Minhas contas (ícone, nome e saldo)
TOTAL = [24, 168, 196, 56]                                  # PATRIMÔNIO TOTAL R$ 111.849,20

# ---------------------------------------------------------------- tempos (s)
SH = 0.3             # a parte das telas começa 0,3 s depois do plano original (tempos abaixo sem o SH)
VIRA = 6.55 + SH     # a folha tinta vira para cima e revela o papel
TC = [(6.95, 8.95), (9.25, 14.25), (14.55, 17.6)]
FIM = 17.5 + SH
TIP = [10.15, 10.3, 10.45, 10.6, 10.75, 10.9]

# ---------------------------------------------------------------- folhinha do calendário
DIAS = [("26", "quinta-feira"), ("27", "sexta-feira"), ("28", "sábado"), ("29", "domingo"), ("30", "segunda-feira")]
def folha(i, dia, sem):
    return f"""<div class="folha" id="f{i}" style="z-index:{10 - i}">
  <div class="f-cab">Novembro 2026</div>
  <div class="f-dia num">{dia}</div>
  <div class="f-sem">{sem}</div>
</div>"""
FOLHAS = "".join(folha(i, d, s) for i, (d, s) in enumerate(DIAS))

IMGS = [("iA0", tela("celular-visao-geral-1-novembro.jpg")), ("iB", tela("celular-transferencia-1-nova-transacao.jpg")),
        ("iC", tela("celular-transferencia-2-tipo.jpg")), ("iD0", tela("celular-transferencia-3-valor-0.jpg"))] + \
       [(f"iD{i}", tela(f"celular-transferencia-3-valor-{i}.jpg")) for i in range(1, 7)] + \
       [("iE", tela("celular-transferencia-4-para.jpg")), ("iF", tela("celular-transferencia-5-preenchida.jpg")),
        ("iG", tela("celular-transferencia-6-registrada.jpg")), ("iH", tela("celular-visao-geral-2-contas-antes.jpg")),
        ("iI", tela("celular-visao-geral-3-contas-depois.jpg"))]
EXTRA = K.aneis("aRec", "aDePara", "aReserva", "aTotal") + K.toques("tqFab", "tqTipo", "tqValor", "tqPara", "tqRes", "tqReg")

CSS = f"""
#tinta{{transform-origin:50% 0;backface-visibility:hidden}}
#cena3d{{position:absolute;left:0;top:0;width:1080px;height:1920px;perspective:2400px}}
#gancho{{position:absolute;left:90px;top:330px;width:900px}}
#gancho .h1{{font-size:104px;line-height:.98;margin-top:34px;color:#fff;text-wrap:balance}}
#gancho .h1 b{{color:{A.MENTA};font-weight:700}}
#bloco{{position:absolute;left:260px;top:800px;width:560px;height:620px;perspective:1600px}}
.folha{{position:absolute;left:0;top:0;width:560px;height:600px;border-radius:44px;background:#fff;overflow:hidden;
  transform-origin:50% 0;backface-visibility:hidden;box-shadow:0 2px 0 #D9D6CC}}
.f-cab{{height:132px;background:{A.BRAND};color:#fff;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:700;
  letter-spacing:.16em;text-transform:uppercase}}
.f-dia{{text-align:center;font-size:300px;font-weight:700;letter-spacing:-.06em;line-height:1;color:{A.INK};margin-top:22px}}
.f-sem{{text-align:center;font-size:46px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em;margin-top:10px}}
#base1,#base2{{position:absolute;left:14px;width:532px;height:40px;border-radius:0 0 40px 40px;background:#DCD9CF}}
#base1{{top:592px;background:#E9E6DD}} #base2{{top:604px;left:28px;width:504px;background:#C9C6BC}}
#hoje{{position:absolute;left:640px;top:740px;display:inline-flex;align-items:center;height:88px;padding:0 40px;border-radius:999px;
  background:{A.MENTA};color:{A.INK};font-size:42px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;opacity:0}}
.tt{{position:absolute;left:90px;top:300px;width:900px;font-size:76px;line-height:1.04;font-weight:700;letter-spacing:-.045em;color:#fff;
  text-wrap:balance;opacity:0}}
.tt b{{color:{A.MENTA};font-weight:700}}
#treze{{position:absolute;left:90px;top:760px;width:900px;opacity:0}}
.tr-rot{{display:flex;justify-content:space-between;align-items:flex-end;font-size:34px;font-weight:600;color:{K.DARK_TEXTO};margin-bottom:18px}}
.tr-rot b{{color:#fff;font-weight:700}}
.chave{{height:16px;border:4px solid #3A443B;border-bottom:0;border-radius:12px 12px 0 0;margin-bottom:16px}}
.tr-barra{{display:flex;gap:18px;height:330px}}
.p1,.p2{{flex:1;border-radius:34px;padding:30px 28px;display:flex;flex-direction:column;justify-content:space-between}}
.p1{{background:{A.MENTA};color:{A.INK}}}
.p2{{border:4px dashed #6B786D;color:#fff}}
.p-rot{{font-size:36px;font-weight:700;letter-spacing:-.01em;line-height:1.2}}
.p-v{{white-space:nowrap;font-size:82px;font-weight:700;letter-spacing:-.05em;line-height:1;font-variant-numeric:tabular-nums}}
.p-sub{{font-size:40px;font-weight:700;line-height:1.1;letter-spacing:-.03em;color:#fff}}
.marcas{{display:flex;gap:18px;margin-top:30px}}
.mc{{flex:1;display:flex;flex-direction:column;gap:16px;font-size:38px;font-weight:600;color:#fff;letter-spacing:-.015em}}
.mc span{{display:flex;align-items:center;gap:14px;opacity:0}}
.ok{{width:40px;height:40px;border-radius:50%;background:{A.MENTA};display:inline-flex;align-items:center;justify-content:center;flex:none}}
.mc2 span{{color:{K.DARK_TEXTO}}}
.tit .ap{{display:block;font-size:36px;line-height:1.3;font-weight:500;color:{A.MUTED};letter-spacing:-.018em;margin-top:16px}}
"""

OK_SVG = f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{A.INK}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

CORPO = f"""
<div class="cena papel" id="papel">
  <div class="tit" id="c1">Separe antes de <b>gastar</b>.<span class="ap">No exemplo, novembro tem R$ 14.940 de receitas, com a 1ª parcela.</span></div>
  <div class="tit" id="c2">Transferência de <b>R$&nbsp;2.000</b> da Conta corrente para a Reserva.</div>
  <div class="tit" id="c3">A Reserva vai a <b>R$&nbsp;35.000</b>.<span class="ap">O patrimônio continua o mesmo: o dinheiro só mudou de conta.</span></div>
  <div class="nota" id="nota">{K.NOTA}</div>
  <div class="janela" id="janela">{camadas("tela", IMGS, EXTRA)}</div>
</div>

<div id="cena3d"><div class="cena tinta" id="tinta">
  <div id="gancho">
    <div class="eyebrow">13º salário · 30/11</div>
    <div class="h1">Último dia da <b>1ª parcela</b> do 13º.</div>
  </div>
  <div id="bloco"><div id="base2"></div><div id="base1"></div>{FOLHAS}</div>
  <div id="hoje">Hoje</div>

  <div class="tt" id="e1">Ela vem cheia: metade do salário, <b>sem INSS e sem IR</b>.</div>
  <div class="tt" id="e2">Os descontos ficam para a <b>2ª parcela</b>.</div>
  <div id="treze">
    <div class="tr-rot"><span>13º do exemplo</span><b class="num">R$ 9.960</b></div>
    <div class="chave"></div>
    <div class="tr-barra">
      <div class="p1" id="p1"><span class="p-rot">1ª parcela · até 30/11</span><span class="p-v" id="v1">R$ 4.980</span></div>
      <div class="p2" id="p2"><span class="p-rot">2ª parcela · até 20/12</span><span class="p-sub">o resto</span></div>
    </div>
    <div class="marcas">
      <div class="mc" id="m1"><span><i class="ok">{OK_SVG}</i>sem INSS</span><span><i class="ok">{OK_SVG}</i>sem IR</span></div>
      <div class="mc mc2" id="m2"><span>menos INSS e IR do 13º inteiro</span></div>
    </div>
  </div>
</div></div>

{K.fim("Transferências no timtimcash")}
"""

JS = JS_R3 + f"""
const SH={SH}, VIRA={VIRA}, TC={[list(x) for x in TC]}, FIM={FIM}, TIP={TIP};
poeAnel('aRec', {RECEITAS}, 12); poeToque('tqFab', ...{centro(FAB)});
poeToque('tqTipo', ...{centro(TIPO)}); poeToque('tqValor', ...{centro(VALOR)});
poeToque('tqPara', ...{centro(PARA)}); poeToque('tqRes', ...{centro(RESERVA_PK)}); poeToque('tqReg', ...{centro(BOTAO)});
poeAnel('aDePara', {DE_PARA}, 6); poeAnel('aReserva', {LINHA_RESERVA}, 6); poeAnel('aTotal', {TOTAL}, 8);
const FLIP = [0.06, 0.32, 0.58, 0.84];            // cada folha vira em 0,22 s
function render(t){{
  // 1. folhinha: 26, 27, 28 e 29 viram; para no 30
  FLIP.forEach((a,i) => {{ const p = Math.pow(lin(t, a, a+.22), 1.6); const e = $('f'+i);
    e.style.transform = `rotateX(${{-104*p}}deg)`; e.style.opacity = p < .98 ? 1 : 0;
    e.style.filter = `brightness(${{1 - .25*p}})`; }});
  const pousa = pback(t, 1.06, 1.42);
  $('f4').style.transform = `scale(${{1 + .035*Math.sin(Math.PI*lin(t,1.06,1.42))}})`;
  const hj = pback(t, 1.35, 1.75);
  $('hoje').style.opacity = lin(t, 1.35, 1.45) * (1 - prog(t, 2.35, 2.6));
  $('hoje').style.transform = `rotate(${{-6 + 6*hj}}deg) scale(${{.5 + .5*hj}})`;
  // o gancho sai e a folhinha sobe; entram as frases e a barra do 13º
  const s1 = prog(t, 2.35, 2.75);
  $('gancho').style.opacity = 1 - s1; $('gancho').style.transform = `translateY(${{-50*s1}}px)`;
  $('bloco').style.opacity = 1 - s1; $('bloco').style.transform = `translateY(${{-120*s1}}px) scale(${{1 - .1*s1}})`;
  titulo('e1', t, 2.75, 4.6); titulo('e2', t, 4.9, VIRA-.05);
  const tz = prog(t, 2.9, 3.4);
  $('treze').style.opacity = tz; $('treze').style.transform = `translateY(${{(1-tz)*50}}px)`;
  contar('v1', t, 3.2, 4.0, 0, 4980, 0, 'R$ ');
  [...$('m1').children].forEach((e,i) => {{ const p = pback(t, 3.7+i*.3, 4.1+i*.3); e.style.opacity = lin(t, 3.7+i*.3, 3.8+i*.3);
    e.style.transform = `scale(${{.7+.3*p}})`; e.style.transformOrigin = '0 50%'; }});
  const d2 = prog(t, 5.0, 5.4);
  $('p2').style.borderColor = d2 > .5 ? '{A.MENTA}' : '#6B786D';
  $('p2').style.transform = `scale(${{1 + .03*Math.sin(Math.PI*d2)}})`;
  [...$('m2').children].forEach(e => {{ const p = pout(t, 5.2, 5.6); e.style.opacity = p; e.style.transform = `translateY(${{(1-p)*16}}px)`; }});
  // a folha tinta vira para cima (como uma folhinha) e mostra o papel
  const v = prog(t, VIRA, VIRA+.55);
  $('tinta').style.transform = `rotateX(${{-96*v}}deg)`;
  $('cena3d').style.visibility = v < .99 ? 'visible' : 'hidden';

  // 2. telas reais (u: o relógio desta parte, 0,3 s depois do plano original, para a 2ª frase ficar 1,8 s na tela)
  const u = t - SH;
  titulo('c1', u, TC[0][0], TC[0][1]); titulo('c2', u, TC[1][0], TC[1][1]); titulo('c3', u, TC[2][0], FIM-SH+.4);
  const ent = prog(u, 6.75, 7.3);
  const J = $('janela'); J.style.opacity = ent; $('nota').style.opacity = ent;
  J.style.transform = `translateY(${{(1-ent)*80}}px)`; $('nota').style.transform = `translateY(${{(1-ent)*80}}px)`;
  op('iA0', 1);
  op('iB', prog(u, 8.92, 9.1));
  op('iC', u >= 9.55 ? 1 : 0);
  op('iD0', u >= 10.0 ? 1 : 0);
  TIP.forEach((a,i) => op('iD'+(i+1), u >= a ? 1 : 0));
  op('iE', prog(u, 11.62, 11.8));
  op('iF', prog(u, 12.18, 12.34));
  op('iG', prog(u, 13.82, 14.0));
  op('iH', prog(u, 14.62, 14.8));
  op('iI', prog(u, 15.3, 15.6));
  let topo = 250;
  topo += (40-250)*prog(u, 8.92, 9.2);           // o formulário, do topo
  topo += (262-40)*prog(u, 10.98, 11.4);          // De, Para, a lista de contas e o botão
  topo += (118-262)*prog(u, 12.22, 12.6);         // a folha preenchida: valor, De e Para
  topo += (262-118)*prog(u, 13.18, 13.5);         // e o botão
  topo += (82-262)*prog(u, 14.62, 14.8);          // Minhas contas
  pan('tela', topo);
  anel('aRec', u, 7.4, 8.6); toque('tqFab', u, 8.75);
  toque('tqTipo', u, 9.4); toque('tqValor', u, 9.85);
  toque('tqPara', u, 11.5); toque('tqRes', u, 12.04);
  anel('aDePara', u, 12.55, 13.2); toque('tqReg', u, 13.65);
  anel('aReserva', u, 15.45, 17.35); anel('aTotal', u, 16.25, 17.35);

  // 3. fechamento verde
  sobe('fim', t, FIM);
}}
"""

def capa():
    corpo = f"""{K.logo('tinta')}
  <div style="position:absolute;left:90px;top:430px;width:900px">
    <div class="eyebrow">13º salário</div>
    <div class="h1" style="font-size:104px;line-height:.98;margin-top:34px;color:#fff;text-wrap:balance">Hoje: último dia da <span style="color:{A.MENTA}">1ª parcela</span> do 13º</div>
  </div>
  <div style="position:absolute;left:290px;top:930px;width:500px">
    <div style="position:absolute;left:24px;top:532px;width:452px;height:40px;border-radius:0 0 38px 38px;background:#C9C6BC"></div>
    <div style="position:absolute;left:12px;top:520px;width:476px;height:40px;border-radius:0 0 38px 38px;background:#E9E6DD"></div>
    <div style="position:relative;width:500px;height:540px;border-radius:40px;background:#fff;overflow:hidden">
      <div style="height:118px;background:{A.BRAND};color:#fff;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:700;letter-spacing:.16em;text-transform:uppercase">Novembro 2026</div>
      <div style="text-align:center;font-size:270px;font-weight:700;letter-spacing:-.06em;line-height:1;color:{A.INK};margin-top:20px">30</div>
      <div style="text-align:center;font-size:42px;font-weight:600;color:{A.MUTED};letter-spacing:-.02em;margin-top:8px">segunda-feira</div>
    </div>
  </div>"""
    return K.pagina_capa(corpo, "", fundo="tinta")

if __name__ == "__main__":
    K.executar(K.pagina(CORPO, CSS, JS), DUR, SAIDA, TRAB, capa_html=capa())
