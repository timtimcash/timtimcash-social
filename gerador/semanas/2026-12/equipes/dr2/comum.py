# -*- coding: utf-8 -*-
"""Peças comuns da equipe dr2 (Reels de 17, 20, 22, 27 e 30/12/2026), por cima do kit (N/kit/reelkit.py, sem mudança).

- captura: abrir o site (N/base_app, sem mudança) e medir caixas em px CSS do celular (CX_JS, caixas());
- camadas(): várias capturas reais empilhadas na mesma .tela, para trocar de passo com fusão (como a r3);
- camera(): câmera sobre a tela real (como a r2), com zoom de no máximo 1,2 para não cortar números;
- din(): valor em reais com "R$" e centavos menores (como a r1b).
Nada aqui altera captura: as telas só são recortadas, redimensionadas e trocadas por fusão.
"""
import os, sys, json
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, os.path.join(N, "kit"))
import reelkit as K
A = K.A
DR2 = os.path.dirname(os.path.abspath(__file__))
MENOS = "−"   # sinal de menos, como o site


def saida(pasta):
    return os.path.join(N, "saida", pasta)


def trabalho(nome):
    return os.path.join(DR2, "trabalho", nome)


def _limpa(v):
    if isinstance(v, str):
        return v.replace("\xa0", " ").replace(" ", " ")
    if isinstance(v, dict):
        return {k: _limpa(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_limpa(x) for x in v]
    return v


def caixas(pasta, nome="caixas.json"):
    """Caixas e textos medidos na captura (espaços fixos viram espaços comuns, para conferir os números)."""
    return _limpa(json.load(open(os.path.join(saida(pasta), "telas", nome), encoding="utf-8")))


# caixa (px CSS da página, com a rolagem) de um seletor ('sel'), do menor elemento que contém um texto ('tem')
# ou do primeiro cujo texto começa com ('txt')
CX_JS = r"""([modo, alvo]) => {
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const proprio = e => [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
  let el = null;
  if (modo === 'sel') el = [...document.querySelectorAll(alvo)].find(vis);
  else if (modo === 'tem') { const c = [...document.querySelectorAll('body *')].filter(e => vis(e) && e.textContent.replace(/\s+/g,' ').includes(alvo));
    c.sort((a,b) => a.textContent.length - b.textContent.length); el = c[0] || null; }
  else el = [...document.querySelectorAll('body *')].find(e => vis(e) && (proprio(e).startsWith(alvo) || (e.children.length === 0 && e.textContent.trim().startsWith(alvo))));
  if (!el) return null;
  const r = el.getBoundingClientRect();
  return [Math.round(r.x*10)/10, Math.round((r.y + scrollY)*10)/10, Math.round(r.width*10)/10, Math.round(r.height*10)/10];
}"""


async def medir(pg, pedidos):
    out = {}
    for nome, modo, alvo in pedidos:
        out[nome] = await pg.evaluate(CX_JS, [modo, alvo])
    return out


def camadas(tid, imgs, extra="", altura_css=None):
    """imgs: lista de (id, caminho). A primeira começa visível; as outras, transparentes."""
    alt = f"height:{altura_css * 2}px;" if altura_css else ""
    ims = "".join(f'<img id="{i}" src="file://{c}" style="opacity:{1 if k == 0 else 0}">' for k, (i, c) in enumerate(imgs))
    return f'<div class="tela" id="{tid}" style="{alt}">{ims}{extra}</div>'


def din(valor, cls="", rs="R$", cor_rs=None, centavos=True):
    """'2.819,80' -> R$ pequeno + 2.819 + ,80 pequeno."""
    if "," in valor and centavos:
        inteiro, cts = valor.split(",")
        cts = "," + cts
    else:
        inteiro, cts = valor, ""
    s_rs = f' style="color:{cor_rs}"' if cor_rs else ""
    rs_html = f'<span class="rs"{s_rs}>{rs}</span>' if rs else ""
    ct_html = f'<span class="cts">{cts}</span>' if cts else ""
    return f'<span class="din {cls}">{rs_html}<span class="int">{inteiro}</span>{ct_html}</span>'


def uniao(*cx):
    x0 = min(c[0] for c in cx); y0 = min(c[1] for c in cx)
    x1 = max(c[0] + c[2] for c in cx); y1 = max(c[1] + c[3] for c in cx)
    return [round(x0, 1), round(y0, 1), round(x1 - x0, 1), round(y1 - y0, 1)]


def centro(b):
    return [round(b[0] + b[2] / 2, 1), round(b[1] + b[3] / 2, 1)]


CSS = f"""
.din{{display:inline-flex;align-items:baseline;font-variant-numeric:tabular-nums;white-space:nowrap}}
.din .rs{{font-size:.44em;font-weight:600;letter-spacing:-.01em;margin-right:.3em}}
.din .cts{{font-size:.58em;font-weight:600;letter-spacing:-.02em}}
.tela img{{transition:none}}
"""

JS = r"""
// entra e sai (opacidade e deslocamento) para qualquer elemento
function entra(id, t, a, b, dy){ dy = dy===undefined ? 70 : dy; const e=$(id); const ent=prog(t,a,a+.55), sai=b ? prog(t,b,b+.4) : 0;
  e.style.opacity=Math.min(ent, 1-sai); e.style.transform=`translateY(${(1-ent)*dy - sai*40}px)`; }
// cena inteira que sai para cima, entre a e a+.45
function saiCima(id, t, a){ const f = prog(t, a, a+.45); $(id).style.transform = `translateY(${-1920*f}px)`; }
// opacidade de uma camada (captura) dentro da .tela
function op(id, v){ $(id).style.opacity = clamp(v, 0, 1); }
// câmera sobre a tela real: KF = [[_, _, fx, fy, s], [a, b, fx, fy, s], ...]; o ponto (fx, fy) em px CSS do celular fica
// no centro da janela (larg x alt px do Reel), com zoom s (1 = 2 px do Reel por px CSS)
function camera(id, t, KF, larg, alt){ larg = larg || 780; alt = alt || 1000;
  let fx=KF[0][2], fy=KF[0][3], s=KF[0][4];
  for (let i=1;i<KF.length;i++){ const [a,b,x,y,z] = KF[i]; const p = prog(t,a,b); fx += (x-fx)*p; fy += (y-fy)*p; s += (z-s)*p; }
  $(id).style.transform = `translate(${(larg/2 - s*E*fx).toFixed(2)}px, ${(alt/2 - s*E*fy).toFixed(2)}px) scale(${s.toFixed(4)})`;
  return [fx, fy, s]; }
// anel cuja caixa vem de uma câmera: r em px CSS da tela, cam = [fx, fy, s]
function anelCam(id, r, cam, pad, larg, alt){ pad = pad===undefined ? 10 : pad; larg = larg || 780; alt = alt || 1000;
  const [fx, fy, s] = cam, e = $(id), k = s*E;
  e.style.left = (larg/2 + (r[0]-fx)*k - pad)+'px'; e.style.top = (alt/2 + (r[1]-fy)*k - pad)+'px';
  e.style.width = (r[2]*k + 2*pad)+'px'; e.style.height = (r[3]*k + 2*pad)+'px'; }
// toque cuja posição vem de uma câmera
function toqueCam(id, x, y, cam, larg, alt){ larg = larg || 780; alt = alt || 1000; const [fx, fy, s] = cam, k = s*E;
  ['t_','o_'].forEach(p=>{ const e=$(p+id); e.style.left=(larg/2 + (x-fx)*k)+'px'; e.style.top=(alt/2 + (y-fy)*k)+'px'; }); }
"""


def pagina(corpo, css, js):
    return K.pagina(corpo, CSS + css, JS + js)
