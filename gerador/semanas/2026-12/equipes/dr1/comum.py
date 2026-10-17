# -*- coding: utf-8 -*-
"""Peças comuns da equipe dr1 (Reels de 03, 06, 09, 11 e 14/12/2026), por cima do kit (N/kit/reelkit.py, sem mudança).

Reúne o que foi aprovado em novembro:
- din(): valor em reais no estilo do build 2026-10-16.1 ("R$" e centavos menores que o número) · equipe r1b;
- recorte(): um pedaço da tela real (a mesma foto) que se solta da janela e cresce, para ler de perto · equipe r1b;
- camera(): panorâmica e zoom sobre a tela real (zoom de no máximo 1,2, para não cortar números na borda) · equipe r2.
Nada aqui altera uma captura: as telas só são recortadas, ampliadas e trocadas por fusão.
"""
import os, sys, json
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, os.path.join(N, "kit"))
import reelkit as K
A = K.A
DR1 = os.path.dirname(os.path.abspath(__file__))
MENOS = "−"            # sinal de menos, como o site
JANELA = (150, 600)    # canto da janela da tela real no Reel (kit)
ZOOM_MAX = 1.2


def saida(pasta):
    return os.path.join(N, "saida", pasta)


def telas(pasta):
    return os.path.join(N, "saida", pasta, "telas")


def trabalho(nome):
    return os.path.join(DR1, "trabalho", nome)


def _limpa(v):
    if isinstance(v, str):
        return v.replace("\u00a0", " ").replace("\u202f", " ")
    if isinstance(v, dict):
        return {k: _limpa(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_limpa(x) for x in v]
    return v


def caixas(nome):
    """Caixas (px CSS) e textos medidos na captura, gravados em trabalho/<nome>/caixas.json
    (espaços não separáveis viram espaços comuns, para conferir os números)."""
    return _limpa(json.load(open(os.path.join(trabalho(nome), "caixas.json"), encoding="utf-8")))


def din(valor, cls="", rs="R$", cor_rs=None, cor_cts=None, centavos=True):
    """'2.819,80' -> R$ pequeno + 2.819 + ,80 pequeno. Sem centavos se o texto não tiver vírgula."""
    if "," in valor and centavos:
        inteiro, cts = valor.split(",")
        cts = "," + cts
    else:
        inteiro, cts = valor, ""
    s_rs = f' style="color:{cor_rs}"' if cor_rs else ""
    s_ct = f' style="color:{cor_cts}"' if cor_cts else ""
    rs_html = f'<span class="rs"{s_rs}>{rs}</span>' if rs else ""
    ct_html = f'<span class="cts"{s_ct}>{cts}</span>' if cts else ""
    return f'<span class="din {cls}">{rs_html}<span class="int">{inteiro}</span>{ct_html}</span>'


def brl(v, casas=2):
    """1438.8 -> '1.438,80'"""
    s = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return (MENOS if v < 0 else "") + s


CSS = f"""
.din{{display:inline-flex;align-items:baseline;font-variant-numeric:tabular-nums;white-space:nowrap}}
.din .rs{{font-size:.44em;font-weight:600;letter-spacing:-.01em;margin-right:.34em}}
.din .cts{{font-size:.58em;font-weight:600;letter-spacing:-.02em}}
.pop{{position:absolute;left:0;top:0;opacity:0;pointer-events:none}}
.pop .pc{{position:absolute;left:0;top:0;width:100%;height:100%;overflow:hidden;border-radius:30px;background:#fff}}
.pop .pc img{{position:absolute;left:0;top:0;display:block;max-width:none}}
.veu{{position:absolute;left:0;top:0;width:100%;height:100%;background:{A.BG};opacity:0;pointer-events:none}}
.camadas img{{transition:none}}
"""

JS = r"""
// recorte da tela real que se solta da janela: R = [x,y,w,h] em px CSS da tela; DE e PARA = [left, top, largura] em px do Reel.
// sobe entre a e a+d; em b volta para o lugar (volta=true) ou some subindo; troca = lista de [instante, índice da foto].
function recorte(id, t, a, b, R, DE, PARA, d, volta, troca){
  d = d || .6; const e = $(id), pc = e.querySelector('.pc');
  const p = pback2(t, a, a+d), q = b ? prog(t, b, b+.38) : 0;
  let L, T, W;
  if (volta && q > 0){ L = PARA[0] + (DE[0]-PARA[0])*q; T = PARA[1] + (DE[1]-PARA[1])*q; W = PARA[2] + (DE[2]-PARA[2])*q; }
  else { L = DE[0] + (PARA[0]-DE[0])*p; T = DE[1] + (PARA[1]-DE[1])*p; W = DE[2] + (PARA[2]-DE[2])*p; }
  const s = W / R[2];
  e.style.left = L+'px'; e.style.top = (T - (volta ? 0 : 40*q))+'px'; e.style.width = W+'px'; e.style.height = (R[3]*s)+'px';
  const imgs = e.querySelectorAll('img');
  let foto = 0; if (troca) troca.forEach(([ti, k]) => { if (t >= ti) foto = k; });
  imgs.forEach((im, k) => { im.style.width = (390*s)+'px'; im.style.left = (-R[0]*s)+'px'; im.style.top = (-R[1]*s)+'px';
    im.style.opacity = (k === foto) ? 1 : 0; });
  const sombra = volta ? Math.min(p, 1-q) : p;
  pc.style.boxShadow = `0 0 0 2px rgba(236,233,224,${sombra}), 0 ${34*sombra}px ${70*sombra}px -24px rgba(15,20,16,${.42*sombra})`;
  const fi = DE.length > 3 ? lin(t, a, a+.25) : 1;      // recorte que não sai da janela: entra devagar
  e.style.opacity = (t < a) ? 0 : fi*(volta ? (q >= 1 ? 0 : 1) : 1 - q);
}
// sobe com um pequeno exagero no fim (mais contido que back)
function pback2(t, a, b){ const x = clamp((t-a)/(b-a), 0, 1); const c1 = 1.1, c3 = c1 + 1; return 1 + c3*Math.pow(x-1,3) + c1*Math.pow(x-1,2); }
// câmera sobre a tela real: KF = [[_, _, fx, fy, s], [a, b, fx, fy, s], ...]; (fx, fy) em px CSS do celular fica no
// centro da janela (larg x alt px do Reel), com zoom s (1 = 2 px do Reel por px CSS, como no kit). Zoom máximo 1,2.
function camera(id, t, KF, larg, alt){ larg = larg || 780; alt = alt || 1000;
  let fx=KF[0][2], fy=KF[0][3], s=KF[0][4];
  for (let i=1;i<KF.length;i++){ const [a,b,x,y,z] = KF[i]; const p = prog(t,a,b); fx += (x-fx)*p; fy += (y-fy)*p; s += (z-s)*p; }
  s = Math.min(s, 1.2);
  $(id).style.transform = `translate(${(larg/2 - s*E*fx).toFixed(2)}px, ${(alt/2 - s*E*fy).toFixed(2)}px) scale(${s.toFixed(4)})`;
  return [fx, fy, s]; }
// fotos empilhadas na mesma camada: a de índice k entra por cima da anterior em TR[k]; sem fusão (f = 0) é um corte seco,
// como a tela do site mudando; com fusão f, a anterior fica inteira por baixo até a nova cobrir
function fotos(ids, t, TR, f){ f = f || 0; ids.forEach((id, k) => { const a = TR[k], b = k+1 < TR.length ? TR[k+1] : 1e9;
    $(id).style.opacity = (t >= b + f) ? 0 : (k === 0 ? 1 : (f ? lin(t, a, a+f) : (t >= a ? 1 : 0))); }); }
// some (opacidade e subida curta) entre a e a+.4; sai entre b e b+.3
function some(id, t, a, b, dy){ dy = dy===undefined ? 26 : dy; const e=$(id); const vin=pout(t,a,a+.4), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=Math.min(vin, 1-vout); e.style.transform=`translateY(${(1-vin)*dy - vout*dy*.7}px)`; }
// palavras que entram uma a uma (cada palavra num span .w)
function palavras(id, t, a, b, passo){ passo = passo || .085; const ws = $(id).querySelectorAll('.w'); for (let i=0;i<ws.length;i++){
    const p = pout(t, a + i*passo, a + i*passo + .42), o = b ? prog(t, b, b+.3) : 0;
    ws[i].style.opacity = Math.min(p, 1-o); ws[i].style.transform = `translateY(${(1-p)*34 - o*24}px)`; } }
// traço que se desenha (SVG com pathLength = 1 e classe .tr)
function desenha(sel, t, a, d){ const p = prog(t, a, a+(d||.8)); document.querySelectorAll(sel).forEach(e => {
    e.style.strokeDasharray = '1 1'; e.style.strokeDashoffset = (1-p).toFixed(4); }); }
"""


def pop_html(pid, srcs, aneis_html=""):
    """Recorte que salta: uma ou mais fotos (mesma geometria) e os anéis por cima (posição final)."""
    imgs = "".join(f'<img src="file://{s}">' for s in (srcs if isinstance(srcs, (list, tuple)) else [srcs]))
    return f'<div class="pop" id="{pid}"><div class="pc">{imgs}</div>{aneis_html}</div>'


def camadas(tid, imgs, extra=""):
    """Várias fotos reais empilhadas na mesma .tela (a primeira visível), para trocar de passo com fusão."""
    ims = "".join(f'<img id="{i}" src="file://{c}" style="opacity:{1 if k == 0 else 0}">' for k, (i, c) in enumerate(imgs))
    return f'<div class="tela camadas" id="{tid}">{ims}{extra}</div>'


def de_janela(R, cam=(0, 0, 1.0)):
    """Onde a região R (px CSS) está no Reel com a câmera (topo, esquerda, zoom) parada: [left, top, largura]."""
    topo, esq, z = cam
    return [JANELA[0] + (R[0] - esq) * 2 * z, JANELA[1] + (R[1] - topo) * 2 * z, R[2] * 2 * z]


def de_camera(R, fx, fy, s):
    """Onde a região R (px CSS) está no Reel com a câmera centrada em (fx, fy) e zoom s: [left, top, largura]."""
    return [JANELA[0] + 390 - s * 2 * fx + R[0] * 2 * s, JANELA[1] + 500 - s * 2 * fy + R[1] * 2 * s, R[2] * 2 * s]


def anel_no_recorte(aid, R, PARA, r, pad=12, cor=""):
    """Anel (classe do kit) dentro do recorte, na escala final: r = caixa em px CSS da tela."""
    s = PARA[2] / R[2]
    x, y, w, h = (r[0] - R[0]) * s - pad, (r[1] - R[1]) * s - pad, r[2] * s + 2 * pad, r[3] * s + 2 * pad
    return f'<div class="anel {cor}" id="{aid}" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px"></div>'


def uniao(*cx):
    x0 = min(c[0] for c in cx); y0 = min(c[1] for c in cx)
    x1 = max(c[0] + c[2] for c in cx); y1 = max(c[1] + c[3] for c in cx)
    return [round(x0, 1), round(y0, 1), round(x1 - x0, 1), round(y1 - y0, 1)]


def palavras_html(ident, texto, destaque=(), cls=""):
    """Cada palavra num <span class="w"> (entram uma a uma). destaque: índices das palavras em destaque (<b>)."""
    ws = texto.split(" ")
    return f'<div class="{cls}" id="{ident}">' + " ".join(
        (f'<span class="w"><b>{w}</b></span>' if i in destaque else f'<span class="w">{w}</span>') for i, w in enumerate(ws)) + "</div>"


def pagina(corpo, css, js):
    return K.pagina(corpo, CSS + css, JS + js)


# ---------------------------------------------------------------- captura (usado pelos roteiros de captura)
# caixa (px CSS, com a rolagem) do menor elemento visível cujo texto bate com `re` (expressão regular, sem barras)
CAIXA_RE = r"""([re, dentro]) => {
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const rx = new RegExp(re);
  let els = [...document.querySelectorAll('body *')].filter(e => vis(e) && !e.closest('.sidebar,aside,nav') && rx.test(e.innerText || ''));
  if (dentro) els = els.filter(e => e.closest(dentro));
  els.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
  const el = els[0]; if (!el) return null;
  const r = el.getBoundingClientRect();
  return [+r.x.toFixed(1), +(r.y + scrollY).toFixed(1), +r.width.toFixed(1), +r.height.toFixed(1), (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 160)];
}"""
