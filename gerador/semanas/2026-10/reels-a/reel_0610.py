# -*- coding: utf-8 -*-
"""Reel de 06/10/2026 · "O timtimcash em 20 segundos" (capa verde), 1080 × 1920, 30 fps, 20 s.

Cortes rápidos por cinco telas reais do celular (conta fictícia), cada uma com uma frase:
Visão geral, Orçamentos, Relatórios, Simulação futura e Remessas ao exterior.
A janela da capa é a mesma da primeira cena: o verde sobe e a tela continua.
python3 reel_0610.py            (vídeo, capa.jpg e previa.mp4 em $O/saida/<pasta>/)
REEL_PREVIA="0 2.3 4.6" python3 reel_0610.py   (só quadros soltos)
"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import reelkit as K
A = K.A

PASTA = "2026-10-06_reel-o-timtimcash-em-20-segundos"
O = os.path.dirname(AQUI)
SAIDA = os.path.join(O, "saida", PASTA)
TELAS = os.path.join(SAIDA, "telas")
def t_(nome): return os.path.join(TELAS, nome)
DUR = 20.0

# ---------------------------------------------------------------- tempos (s)
SLIDE = 2.50                          # a capa verde sobe (0,5 s)
S = [2.75, 5.15, 7.55, 9.95, 12.35]   # início de cada cena de tela
CONC = 14.75                          # conclusão
FIM = 16.95                           # fechamento verde sobe (0,45 s)

# ---------------------------------------------------------------- telas (px CSS; cartões com 14 px de margem, como no celular)
M = 14
CENAS = [
    # id, sobretítulo, título, imagem, x, y, largura_px, altura_css, panorâmica até
    ("1", "Visão geral", "Quanto entrou, quanto saiu, quanto sobrou.", "celular-dashboard.jpg", 0, 0, 1170, 741, 178),
    ("2", "Orçamentos", "O que estourou e o que ainda cabe.", "celular-orcamentos-progresso.jpg", M, M, 1086, 929 + 2 * M, 190),
    ("3", "Relatórios", "Para onde o dinheiro foi.", "celular-relatorios-despesas-por-categoria.jpg", M, M, 1086, 849 + 2 * M, 115),
    ("4", "Simulação futura", "Como fecham os próximos meses.", "celular-simulacao-cenario-coluna.jpg", M, M, 1086, 1499 + 2 * M, 100),
    ("5", "Remessas ao exterior", "Quanto rendeu lá fora, em reais.", "celular-remessas.jpg", 0, 0, 1170, 741, 178),
]
# anéis: (id, janela, caixa px CSS da tela, folga px da imagem, classe)
ANEIS = [
    ("aSobrou", "1", [31, 545, 328, 30], 24, ""),                 # Sobrou no período · R$ 2.180,00
    ("aBares", "2", [15 + M, 240 + M, 332, 118], 20, "coral"),     # Bares e restaurantes · 112% · excedeu em R$ 72
    ("aMercado", "2", [15 + M, 428 + M, 332, 90], 20, ""),         # Mercado · 86%
    ("aCasa", "3", [15 + M, 380 + M, 332, 48], 22, ""),            # Casa · R$ 2.300,00 · 29,6%
    ("aSaldo", "4", [15 + M, 12 + M, 172, 78], 22, ""),            # Saldo em set/27 · R$ 37.720
    ("aRend", "5", [29, 280, 191, 24], 20, ""),                    # +R$ 12.600,00 · +21,0% em R$
]

def janela(cid, arq, x, y, larg, alt):
    aneis = "".join(f'<div class="anel {cl}" id="{aid}"></div>' for aid, j, _, _, cl in ANEIS if j == cid)
    return f'<div class="janela" id="j{cid}">' + K.tela(f"tela{cid}", [(f"img{cid}", t_(arq), x, y, larg, "")], alt, aneis) + "</div>"

titulos = "".join(f'<div class="tit" id="t{c}"><span class="sobre">{sob}</span>{tit}</div>' for c, sob, tit, *_ in CENAS)
janelas = "".join(janela(c, arq, x, y, larg, alt) for c, _, _, arq, x, y, larg, alt, _ in CENAS if c != "1")
j1 = janela(*[(c, arq, x, y, larg, alt) for c, _, _, arq, x, y, larg, alt, _ in CENAS if c == "1"][0])

CHIPS = ["Visão geral", "Orçamentos", "Relatórios", "Simulação futura", "Remessas ao exterior"]

CSS = f"""
.tit{{font-size:72px}}
#capa .h1{{font-size:116px;line-height:.96}}
#capa .nota-capa{{position:absolute;left:150px;font-size:28px;font-weight:600;color:#fff;letter-spacing:-.005em}}
#j1{{z-index:5}}
#fim{{z-index:6}}
.chip b{{display:inline-block;width:18px;height:18px;border-radius:50%;background:{A.BRAND};margin-right:18px}}
"""

CORPO = f"""
<div class="cena" id="papel">
  {titulos}
  <div class="nota" id="nota">{K.NOTA}</div>
  {janelas}
</div>

<div class="cena" id="conc" style="opacity:0">
  <div style="position:absolute;left:90px;top:560px;width:900px">
    <div class="h1" id="cTit" style="font-size:118px">Todo dinheiro, um só lugar.</div>
    <div id="chips" style="display:flex;flex-wrap:wrap;gap:22px;margin-top:80px">
      {"".join(f'<span class="chip"><b></b>{c}</span>' for c in CHIPS)}
    </div>
  </div>
</div>

<div class="cena verde" id="capa">
  <div style="position:absolute;left:90px;top:290px">{A.logo_horizontal("white", 60)}</div>
  <div style="position:absolute;left:90px;top:420px;width:900px">
    <div class="eyebrow" style="margin-bottom:36px">Tour pelo site</div>
    <div class="h1" id="gancho">O timtimcash em 20 segundos</div>
  </div>
  <div class="nota-capa" id="notaCapa" style="top:756px">{K.NOTA}</div>
</div>
{j1}

{K.fim("Seu dinheiro, com a clareza que ele merece.")}
"""

JS = f"""
const S={S}, CONC={CONC}, FIM={FIM}, SLIDE={SLIDE};
const PAN={{{",".join(f"'{c}':{p}" for c, *_, p in CENAS)}}};
const ANEIS={{{",".join(f"'{a}':[{r},{pad}]" for a, _, r, pad, _ in ANEIS)}}};
for (const k in ANEIS) caixa($(k), ANEIS[k][0], ANEIS[k][1]);
// geometria da janela 1: na capa (top 810, 830 de altura, abaixo da logo fora da zona do nome do perfil) e na cena (top 600, 1000)
const CAPA_TOP=810, CAPA_H=830;
function render(t){{
  // 1. capa verde: o título cresce de leve; a janela desce a tela devagar; em 2,5 s o verde sobe
  const sobe = prog(t, SLIDE, SLIDE+.5);
  $('capa').style.transform = `translateY(${{-1920*sobe}}px)`;
  $('gancho').style.transform = `scale(${{1+0.02*lin(t,0,SLIDE)}})`; $('gancho').style.transformOrigin='0 50%';
  const j1 = $('j1');
  j1.style.top = (CAPA_TOP + (600-CAPA_TOP)*sobe) + 'px';
  j1.style.height = (CAPA_H + (1000-CAPA_H)*sobe) + 'px';
  // 2. títulos das cenas
  for (let k=0; k<5; k++){{
    const a = k==0 ? 2.80 : S[k]+.22, b = k<4 ? S[k+1]-.06 : CONC-.06;
    titulo('t'+(k+1), t, a, b);
  }}
  // nota da tela real: entra com a primeira cena, sai na conclusão
  const nIn = prog(t, 2.85, 3.2), nOut = prog(t, CONC, CONC+.35);
  $('nota').style.opacity = Math.min(nIn, 1-nOut);
  // 3. janelas: a 1 vem da capa; as outras entram pela direita enquanto a anterior sai pela esquerda
  for (let k=1; k<=5; k++){{
    const e = $('j'+k);
    const ent = k==1 ? 1 : prog(t, S[k-1], S[k-1]+.45);
    const sai = k<5 ? prog(t, S[k], S[k]+.45) : 0;
    let x = 1080*(1-ent) - 1080*sai;
    let y = 0, op = 1;
    if (k==5){{ const f = prog(t, CONC, CONC+.4); y = 40*f; op = 1-f; }}
    e.style.transform = `translate(${{x}}px, ${{y}}px)`;
    e.style.opacity = op;
    e.style.visibility = (k>1 && t < S[k-1]-.01) || (k<5 && t > S[k]+.5) ? 'hidden' : 'visible';
  }}
  // 4. panorâmicas: a tela rola um pouco em cada cena
  pan('tela1', 24*lin(t,0,SLIDE) + (PAN['1']-24)*prog(t, 3.05, 4.15));
  pan('tela2', PAN['2']*prog(t, S[1]+.5, S[1]+1.35));
  pan('tela3', PAN['3']*prog(t, S[2]+.5, S[2]+1.35));
  pan('tela4', PAN['4']*(1-prog(t, S[3]+.5, S[3]+1.3)));
  pan('tela5', PAN['5']*prog(t, S[4]+.5, S[4]+1.6));
  // 5. anéis
  anel('aSobrou', t, 4.05, S[1]-.05);
  anel('aBares', t, S[1]+.85, S[1]+1.55);
  anel('aMercado', t, S[1]+1.55, S[2]-.05);
  anel('aCasa', t, S[2]+1.0, S[3]-.05);
  anel('aSaldo', t, S[3]+1.25, S[4]-.05);
  anel('aRend', t, S[4]+.55, CONC-.05);
  // 6. conclusão
  const ci = prog(t, CONC+.15, CONC+.55);
  $('conc').style.opacity = ci; $('conc').style.transform = `translateY(${{(1-ci)*40}}px)`;
  [...$('chips').children].forEach((c,i)=>{{ const p=prog(t, CONC+.45+i*.12, CONC+.8+i*.12); c.style.opacity=p; c.style.transform=`translateY(${{(1-p)*24}}px)`; }});
  // 7. fechamento verde sobe
  const f = prog(t, FIM, FIM+.45);
  $('fim').style.transform = `translateY(${{1920*(1-f)}}px)`;
}}
"""

HTML = K.pagina(CORPO, CSS, JS)

if __name__ == "__main__":
    K.executar(HTML, DUR, SAIDA, capa_t=2.3, trabalho=os.path.join(AQUI, "trabalho", "0610"))
