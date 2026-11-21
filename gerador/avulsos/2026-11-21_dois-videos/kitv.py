# -*- coding: utf-8 -*-
"""Kit dos dois vídeos de 20/11/2026 (o timtimcash e o Premium), por cima do kit dos Reels (kit/reelkit.py) e das peças da
equipe js (equipes/js/comum.py: câmera, anéis e troca de fotos).

O que este kit acrescenta:
- o aparelho: a tela real dentro de um celular que entra de baixo, inclinado, e assenta; ele passa da borda de baixo do vídeo,
  e o que importa fica acima de 1600 px (zona segura). As telas trocam deslizando dentro do aparelho;
- títulos que sobem de dentro de uma máscara (palavra grande e linha de apoio);
- a resposta: um cartão grande, por cima do aparelho, com o número que a tela mostra;
- a coroa e o fundo do Premium, iguais aos do site.
Nada aqui altera uma captura: as telas só são recortadas, ampliadas e trocadas.
"""
import os, sys
RAIZ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev/equipes/js")
import comum as C
K, A = C.K, C.A

OURO, OURO_CLARO, OURO_TINTA = "#B8860B", "#F3DFA2", "#8A6320"       # a coroa e o sobretítulo do Premium no site
FUNDO_PREMIUM = ("radial-gradient(120% 140% at 100% 0%,rgba(255,255,255,.13) 0%,rgba(255,255,255,0) 55%),"
                 "linear-gradient(135deg,#053F31 0%,#04694F 55%,#047857 100%)")           # o cartão do Premium do site
FUNDO_NOITE = "radial-gradient(90% 60% at 50% 38%,#12382C 0%,#0B1F18 55%,#08130F 100%)"   # fundo das telas no tema escuro
COROA_D = ('<path d="M3.3 8.3a1 1 0 0 1 1.6-1l3.5 2.8 2.75-4.55a1 1 0 0 1 1.7 0L15.6 10.1l3.5-2.8a1 1 0 0 1 1.6 1l-1.45 7.9a1 1 0 0 1-1 .8H5.75a1 1 0 0 1-1-.8z"/>'
           '<rect x="5" y="18.7" width="14" height="1.9" rx=".95"/>')                      # _PLN_COROA, do site
NOTA = K.NOTA


def coroa(cls="cw", cor=OURO, extra=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="{cor}" aria-hidden="true" {extra}>{COROA_D}</svg>'


CSS = f"""
.cw{{width:.8em;height:.8em;vertical-align:-.06em}}
/* o aparelho */
.fone{{position:absolute;left:130px;top:566px;width:820px;height:1500px;border-radius:86px;background:#0F1410;opacity:0;transform-origin:50% 28%;
  box-shadow:inset 0 0 0 2px #2B352E,0 60px 90px -40px rgba(15,20,16,.5),0 10px 24px rgba(15,20,16,.14)}}
.visor{{position:absolute;left:20px;top:20px;width:780px;height:1460px;border-radius:66px;overflow:hidden;background:{K.FUNDO_TELA}}}
.fone.esc{{background:#17211C;box-shadow:inset 0 0 0 2px rgba(243,223,162,.34),0 70px 140px -40px rgba(0,0,0,.85),0 0 160px -30px rgba(16,185,129,.35)}}
.fone.esc .visor{{background:#0C110F}}
.desl{{position:absolute;left:0;top:0;width:780px;height:1460px;will-change:transform}}
.visor .tela{{background:transparent}}
.visor .anel{{border-width:8px;border-radius:26px}}
.fone.esc .anel{{border-color:{OURO_CLARO};box-shadow:0 0 0 6px rgba(243,223,162,.16),0 0 40px rgba(243,223,162,.25)}}
.nota2{{position:absolute;left:0;top:510px;width:1080px;text-align:center;font-size:25px;font-weight:500;color:{A.MUTED};letter-spacing:-.005em;opacity:0}}
.noite .nota2{{color:#A9B8AE}}
/* títulos que sobem de dentro de uma máscara */
.mk{{display:block;overflow:hidden;padding-bottom:.14em;margin-bottom:-.14em}}
.mk>span{{display:inline-block;will-change:transform}}
.vb{{position:absolute;left:90px;top:272px;width:900px}}
.vbw{{font-size:136px;line-height:1.02;font-weight:700;letter-spacing:-.055em;color:{A.BRAND_DARK}}}
.vbd{{font-size:46px;line-height:1.15;font-weight:500;letter-spacing:-.025em;color:{A.INK};margin-top:14px;opacity:0}}
/* a resposta: o número que a tela mostra, grande, por cima do aparelho */
.resp{{position:absolute;left:90px;top:1366px;width:900px;min-height:196px;border-radius:44px;padding:34px 46px 36px;opacity:0;transform-origin:50% 100%;
  background:linear-gradient(135deg,#FBEFC6 0%,#F3DFA2 55%,#E4C272 100%);color:#1B1607;box-shadow:0 40px 80px -30px rgba(0,0,0,.75),inset 0 0 0 2px rgba(255,255,255,.45)}}
.resp b{{display:block;font-size:92px;line-height:1;font-weight:700;letter-spacing:-.05em;font-variant-numeric:tabular-nums;white-space:nowrap}}
.resp span{{display:block;font-size:38px;line-height:1.15;font-weight:600;letter-spacing:-.02em;margin-top:14px;color:#4A3B12}}
"""

JS = r"""
// aparelho: entra de baixo, inclinado, e assenta; sai para baixo
function fone(id, t, a, b){ const e = $(id); const en = pout(t, a, a+.75), sa = b ? prog(t, b, b+.45) : 0;
  e.style.opacity = Math.min(lin(t, a, a+.12), 1 - (b ? lin(t, b+.3, b+.45) : 0));
  e.style.transform = `perspective(2600px) translateY(${((1-en)*640 + sa*900).toFixed(1)}px) rotateX(${((1-en)*16).toFixed(2)}deg) scale(${(.93+.07*en).toFixed(4)})`; }
// troca de tela dentro do aparelho (outra página do site): a que sai vai para a esquerda, a nova chega pela direita
function desliza(id, t, trocas){ let x = 0; trocas.forEach(s => { if (t >= s-.2 && t < s) x = -800*prog(t, s-.2, s);
  else if (t >= s && t < s+.34) x = 800*(1 - pout(t, s, s+.34)); }); $(id).style.transform = `translateX(${x.toFixed(1)}px)`; }
// texto que sobe de dentro da máscara (.mk > span): entra em a, sai em b
function sobeTxt(id, t, a, b, d){ d = d || .5; const s = $(id).firstElementChild; const p = pout(t, a, a+d), q = b ? prog(t, b, b+.26) : 0;
  s.style.transform = `translateY(${((1-p)*112 - q*112).toFixed(2)}%)`; }
// palavra grande e linha de apoio
function verbo(n, t, a, b){ sobeTxt('vw'+n, t, a, b, .55); const e = $('vd'+n); const p = pout(t, a+.16, a+.6), q = b ? prog(t, b-.04, b+.2) : 0;
  e.style.opacity = Math.min(p, 1-q); e.style.transform = `translateY(${((1-p)*22 - q*14).toFixed(1)}px)`; }
// cartão da resposta: salta em a, sai em b
function resposta(id, t, a, b){ const e = $(id); const p = pback(t, a, a+.5), q = b ? prog(t, b, b+.24) : 0;
  e.style.opacity = Math.min(lin(t, a, a+.12), 1-q); e.style.transform = `translateY(${((1-p)*70 + q*40).toFixed(1)}px) scale(${(.9+.1*p).toFixed(4)})`; }
// anel com um pulso leve depois de entrar
function anelP(id, t, a, b){ const e = $(id); const vi = prog(t, a, a+.32), vo = b ? prog(t, b, b+.22) : 0;
  const pu = 1 + .018*Math.sin(Math.PI*clamp((t-a-.32)/.5, 0, 1));
  e.style.opacity = vi*(1-vo); e.style.transform = `scale(${((1.07-.07*vi)*pu).toFixed(4)})`; }
// nota "Tela real..." junto com o aparelho
function nota2(id, t, a, b){ $(id).style.opacity = Math.min(lin(t, a+.25, a+.6), 1 - (b ? lin(t, b, b+.25) : 0)); }
const cxm = r => [r[0] + r[2]/2, r[1] + r[3]/2];
"""


def aparelho(fid, tid, imgs, extra="", escuro=False):
    """O celular com as fotos reais empilhadas (a primeira visível) e os anéis e toques por cima."""
    ims = "".join(f'<img id="{i}" src="file://{c}" style="opacity:{1 if k == 0 else 0}">' for k, (i, c) in enumerate(imgs))
    return (f'<div class="fone{" esc" if escuro else ""}" id="{fid}"><div class="visor"><div class="desl" id="{tid}_d">'
            f'<div class="tela" id="{tid}">{ims}</div></div>{extra}</div></div>')


def mk(ident, html, cls=""):
    return f'<span class="mk {cls}" id="{ident}"><span>{html}</span></span>'


def verbo(n, palavra, apoio):
    return f'<div class="vb">{mk(f"vw{n}", palavra, "vbw")}<div class="vbd" id="vd{n}">{apoio}</div></div>'


def pagina(corpo, css, js):
    return K.pagina(corpo, C.CSS + CSS + css, C.JS + JS + js)
