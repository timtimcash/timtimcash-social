# -*- coding: utf-8 -*-
"""Peças comuns da equipe r1b (Reels de 04, 06, 09 e 12/11), por cima do kit (N/kit/reelkit.py, sem mudança).

- din(): valor em reais no estilo do build 2026-10-16.1 ("R$" e centavos menores que o número).
- recorte: um pedaço da tela real (a mesma foto da janela) que se solta da janela e cresce, para ler de perto.
  É a captura recortada e ampliada, sem mudança nenhuma; a janela por trás fica coberta por um véu de papel.
"""
import os, sys
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, os.path.join(N, "kit"))
import reelkit as K
A = K.A

JANELA = (150, 600)      # canto da janela da tela real no Reel (kit)


def din(valor, cls="", rs="R$", cor_rs=None, cor_cts=None, centavos=True):
    """'2.819,80' -> R$ pequeno + 2.819 + ,80 pequeno. Sem centavos se o texto não tiver vírgula.
    centavos=False: as casas decimais ficam no tamanho do número (câmbio, como R$ 5,0515)."""
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


CSS = f"""
.din{{display:inline-flex;align-items:baseline;font-variant-numeric:tabular-nums;white-space:nowrap}}
.din .rs{{font-size:.44em;font-weight:600;letter-spacing:-.01em;margin-right:.34em}}
.din .cts{{font-size:.58em;font-weight:600;letter-spacing:-.02em}}
.pop{{position:absolute;left:0;top:0;opacity:0;pointer-events:none}}
.pop .pc{{position:absolute;left:0;top:0;width:100%;height:100%;overflow:hidden;border-radius:30px;background:#fff}}
.pop .pc img{{position:absolute;left:0;top:0;display:block;max-width:none}}
.veu{{position:absolute;left:0;top:0;width:100%;height:100%;background:{A.BG};opacity:0;pointer-events:none}}
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
// anel dentro de um recorte cuja região R muda com o tempo (a lupa que desce pela tela): r = caixa em px CSS da tela
function posAnel(id, r, R, W, pad){ pad = pad===undefined ? 12 : pad; const s = W / R[2], e = $(id);
  e.style.left = ((r[0]-R[0])*s - pad)+'px'; e.style.top = ((r[1]-R[1])*s - pad)+'px';
  e.style.width = (r[2]*s + 2*pad)+'px'; e.style.height = (r[3]*s + 2*pad)+'px'; }
// sobe com um pequeno exagero no fim (mais contido que back)
function pback2(t, a, b){ const x = clamp((t-a)/(b-a), 0, 1); const c1 = 1.1, c3 = c1 + 1; return 1 + c3*Math.pow(x-1,3) + c1*Math.pow(x-1,2); }
"""


def pop_html(pid, srcs, aneis_html=""):
    """Recorte que salta: uma ou mais fotos (mesma geometria) e os anéis por cima (posição final)."""
    imgs = "".join(f'<img src="file://{s}">' for s in (srcs if isinstance(srcs, (list, tuple)) else [srcs]))
    return f'<div class="pop" id="{pid}"><div class="pc">{imgs}</div>{aneis_html}</div>'


def de_janela(R, cam=(0, 0, 1.0)):
    """Onde a região R (px CSS) está no Reel com a câmera (topo, esquerda, zoom) parada: [left, top, largura]."""
    topo, esq, z = cam
    return [JANELA[0] + (R[0] - esq) * 2 * z, JANELA[1] + (R[1] - topo) * 2 * z, R[2] * 2 * z]


def anel_no_recorte(aid, R, PARA, r, pad=12, cor=""):
    """Anel (classe do kit) dentro do recorte, na escala final: r = caixa em px CSS da tela."""
    s = PARA[2] / R[2]
    x, y, w, h = (r[0] - R[0]) * s - pad, (r[1] - R[1]) * s - pad, r[2] * s + 2 * pad, r[3] * s + 2 * pad
    return f'<div class="anel {cor}" id="{aid}" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px"></div>'


def uniao(*caixas):
    x0 = min(c[0] for c in caixas); y0 = min(c[1] for c in caixas)
    x1 = max(c[0] + c[2] for c in caixas); y1 = max(c[1] + c[3] for c in caixas)
    return [round(x0, 1), round(y0, 1), round(x1 - x0, 1), round(y1 - y0, 1)]
