# -*- coding: utf-8 -*-
"""Peças comuns da equipe fr (Reels de 03, 05, 10, 12 e 15/02/2027), por cima do kit (J/kit/reelkit.py, sem mudança).

Reúne o que foi aprovado em novembro e dezembro:
- din() e brl(): valor em reais no estilo do site ("R$" e centavos menores) · equipes r1b e dr1;
- camera(): panorâmica e zoom sobre a tela real do celular · equipes r2 e dr2;
- cameraD(): a mesma câmera para a tela do computador (1440 px de largura), em que s = px do Reel por px CSS;
- fotos(): troca de captura (corte seco, como o site mudando, ou fusão curta);
- anelCam(), toqueCam(), cursorCam(): anel, toque de dedo e ponteiro do mouse que seguem a câmera.
Nada aqui altera uma captura: as telas só são recortadas, ampliadas e trocadas.
Texto sem travessão nem meia-risca (regra do BRIEFING).
"""
import os, sys, json, glob
J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
sys.path.insert(0, os.path.join(J, "kit"))
import reelkit as K
A = K.A
FR = os.path.dirname(os.path.abspath(__file__))
MENOS = "−"       # sinal de menos, como o site
BASE_APP = os.path.join(J, "base_app")


def saida(pasta):
    return os.path.join(J, "saida", pasta)


def telas(pasta):
    return os.path.join(J, "saida", pasta, "telas")


def trabalho(nome):
    return os.path.join(FR, "trabalho", nome)


def _limpa(v):
    if isinstance(v, str):
        return v.replace(" ", " ").replace(" ", " ")
    if isinstance(v, dict):
        return {k: _limpa(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_limpa(x) for x in v]
    return v


def caixas(pasta):
    """Caixas (px CSS) e textos medidos na captura, gravados em telas/caixas.json (espaços fixos viram comuns)."""
    return _limpa(json.load(open(os.path.join(telas(pasta), "caixas.json"), encoding="utf-8")))


def brl(v, casas=2):
    """1438.8 -> '1.438,80' (negativo com o sinal de menos)."""
    s = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return (MENOS if v < 0 else "") + s


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


def uniao(*cx):
    x0 = min(c[0] for c in cx); y0 = min(c[1] for c in cx)
    x1 = max(c[0] + c[2] for c in cx); y1 = max(c[1] + c[3] for c in cx)
    return [round(x0, 1), round(y0, 1), round(x1 - x0, 1), round(y1 - y0, 1)]


def centro(b):
    return [round(b[0] + b[2] / 2, 1), round(b[1] + b[3] / 2, 1)]


def camadas(tid, imgs, extra="", largura=780):
    """Várias capturas reais empilhadas na mesma camada (a primeira visível). imgs: lista de (id, caminho)."""
    ims = "".join(f'<img id="{i}" src="file://{c}" style="width:{largura}px;opacity:{1 if k == 0 else 0}">' for k, (i, c) in enumerate(imgs))
    return f'<div class="tela camadas" id="{tid}" style="width:{largura}px">{ims}{extra}</div>'


CSS = f"""
.din{{display:inline-flex;align-items:baseline;font-variant-numeric:tabular-nums;white-space:nowrap}}
.din .rs{{font-size:.44em;font-weight:600;letter-spacing:-.01em;margin-right:.3em}}
.din .cts{{font-size:.58em;font-weight:600;letter-spacing:-.02em}}
.camadas img{{transition:none}}
.cursor{{position:absolute;width:52px;height:52px;margin:-6px 0 0 -10px;opacity:0;pointer-events:none;z-index:5}}
.clique{{position:absolute;width:90px;height:90px;margin:-45px 0 0 -45px;border-radius:50%;border:6px solid {A.BRAND};opacity:0;pointer-events:none;z-index:4}}
.w{{display:inline-block}}
"""

JS = r"""
// câmera sobre a tela real do celular: KF = [[_, _, fx, fy, s], [a, b, fx, fy, s], ...]; o ponto (fx, fy) em px CSS do celular
// fica no centro da janela (larg x alt px do Reel), com zoom s (1 = 2 px do Reel por px CSS, como no kit)
function camera(id, t, KF, larg, alt, zmax){ larg = larg || 780; alt = alt || 1000; zmax = zmax || 1.25;
  let fx=KF[0][2], fy=KF[0][3], s=KF[0][4];
  for (let i=1;i<KF.length;i++){ const [a,b,x,y,z] = KF[i]; const p = prog(t,a,b); fx += (x-fx)*p; fy += (y-fy)*p; s += (z-s)*p; }
  s = Math.min(s, zmax);
  $(id).style.transform = `translate(${(larg/2 - s*E*fx).toFixed(2)}px, ${(alt/2 - s*E*fy).toFixed(2)}px) scale(${s.toFixed(4)})`;
  return [fx, fy, s]; }
// câmera sobre a tela do computador (camada de 1440 px CSS = 1440 px do Reel em s = 1): s = px do Reel por px CSS
function cameraD(id, t, KF, larg, alt){
  let fx=KF[0][2], fy=KF[0][3], s=KF[0][4];
  for (let i=1;i<KF.length;i++){ const [a,b,x,y,z] = KF[i]; const p = prog(t,a,b); fx += (x-fx)*p; fy += (y-fy)*p; s += (z-s)*p; }
  $(id).style.transform = `translate(${(larg/2 - s*fx).toFixed(2)}px, ${(alt/2 - s*fy).toFixed(2)}px) scale(${s.toFixed(4)})`;
  return [fx, fy, s]; }
// fotos empilhadas: a de índice k entra em TR[k] (corte seco se f = 0; fusão de f s se f > 0)
function fotos(ids, t, TR, f){ f = f || 0; ids.forEach((id, k) => { const a = TR[k], b = k+1 < TR.length ? TR[k+1] : 1e9;
    $(id).style.opacity = (t >= b + f) ? 0 : (k === 0 ? 1 : (f ? lin(t, a, a+f) : (t >= a ? 1 : 0))); }); }
function op(id, v){ $(id).style.opacity = clamp(v, 0, 1); }
// anel cuja caixa vem de uma câmera: r em px CSS da tela; k = px do Reel por px CSS (E*s no celular, s no computador)
function anelCam(id, r, cam, pad, larg, alt, k){ pad = pad===undefined ? 10 : pad; larg = larg || 780; alt = alt || 1000;
  const [fx, fy, s] = cam, e = $(id); k = k || s*E;
  e.style.left = (larg/2 + (r[0]-fx)*k - pad)+'px'; e.style.top = (alt/2 + (r[1]-fy)*k - pad)+'px';
  e.style.width = (r[2]*k + 2*pad)+'px'; e.style.height = (r[3]*k + 2*pad)+'px'; }
// toque de dedo cuja posição vem de uma câmera
function toqueCam(id, x, y, cam, larg, alt, k){ larg = larg || 780; alt = alt || 1000; const [fx, fy, s] = cam; k = k || s*E;
  ['t_','o_'].forEach(p=>{ const e=$(p+id); e.style.left=(larg/2 + (x-fx)*k)+'px'; e.style.top=(alt/2 + (y-fy)*k)+'px'; }); }
// ponteiro do mouse: vai de P0 a P1 (px CSS da tela) entre a e b; clica em c (a onda abre de c a c+.6)
function cursorCam(id, t, P0, P1, a, b, c, cam, larg, alt, k, sai){ const [fx, fy, s] = cam; k = k || s;
  const p = prog(t, a, b), x = P0[0] + (P1[0]-P0[0])*p, y = P0[1] + (P1[1]-P0[1])*p;
  const e = $(id), o = $('k_'+id); const L = larg/2 + (x-fx)*k, T = alt/2 + (y-fy)*k;
  e.style.left = L+'px'; e.style.top = T+'px'; o.style.left = L+'px'; o.style.top = T+'px';
  const vis = lin(t, a-.2, a) * (sai ? 1 - lin(t, sai, sai+.25) : 1);
  e.style.opacity = vis; e.style.transform = `scale(${(t >= c && t < c+.18) ? .86 : 1})`;
  o.style.opacity = (t >= c && t <= c+.6) ? 1 - lin(t, c, c+.6) : 0; o.style.transform = `scale(${.4 + 1.2*lin(t, c, c+.6)})`; }
// entra e sai (opacidade e deslocamento) para qualquer elemento
function entra(id, t, a, b, dy){ dy = dy===undefined ? 60 : dy; const e=$(id); const ent=pout(t,a,a+.5), sai=b ? prog(t,b,b+.35) : 0;
  e.style.opacity=Math.min(ent, 1-sai); e.style.transform=`translateY(${(1-ent)*dy - sai*36}px)`; }
// cena inteira que sai para cima, entre a e a+.45
function saiCima(id, t, a){ const f = prog(t, a, a+.45); $(id).style.transform = `translateY(${-1920*f}px)`; }
// palavras que entram uma a uma (cada palavra num span .w)
function palavras(id, t, a, b, passo){ passo = passo || .07; const ws = $(id).querySelectorAll('.w'); for (let i=0;i<ws.length;i++){
    const p = pout(t, a + i*passo, a + i*passo + .4), o = b ? prog(t, b, b+.3) : 0;
    ws[i].style.opacity = Math.min(p, 1-o); ws[i].style.transform = `translateY(${(1-p)*30 - o*22}px)`; } }
// traço que se desenha (SVG com pathLength = 1)
function desenha(sel, t, a, d){ const p = prog(t, a, a+(d||.8)); document.querySelectorAll(sel).forEach(e => {
    e.style.strokeDasharray = '1 1'; e.style.strokeDashoffset = (1-p).toFixed(4); }); }
"""

# ponteiro do mouse (seta de traço, branca com contorno de tinta) e a onda do clique
CURSOR_SVG = ('<svg viewBox="0 0 24 24" width="52" height="52"><path d="M5 3 L5 19.5 L9.4 15.4 L12.3 21.6 L15 20.4 L12.2 14.3 L18.2 14.1 Z" '
              f'fill="#fff" stroke="{A.INK}" stroke-width="1.6" stroke-linejoin="round"/></svg>')


def cursores(*ids):
    return "".join(f'<div class="cursor" id="{i}">{CURSOR_SVG}</div><div class="clique" id="k_{i}"></div>' for i in ids)


def palavras_html(ident, texto, destaque=(), cls="", estilo=""):
    """Cada palavra num <span class="w"> (entram uma a uma). destaque: índices das palavras em destaque (<b>)."""
    ws = texto.split(" ")
    est = f' style="{estilo}"' if estilo else ""
    return f'<div class="{cls}" id="{ident}"{est}>' + " ".join(
        (f'<span class="w"><b>{w}</b></span>' if i in destaque else f'<span class="w">{w}</span>') for i, w in enumerate(ws)) + "</div>"


def pagina(corpo, css, js):
    return K.pagina(corpo, CSS + css, JS + js)


# ---------------------------------------------------------------- envelope desenhado (dupla 05/02 e 10/02)
def envelope(larg, cor, traco=12, aba_id="", fundo="none", ident=""):
    """Envelope de traço, cantos redondos, com a aba (id aba_id) que abre girando no eixo de cima.
    Desenho próprio (ícone), não é imagem de dinheiro. Altura = 0,66 da largura."""
    w, h = larg, larg * 0.66
    t = traco
    idt = f' id="{ident}"' if ident else ""
    aba = f' id="{aba_id}"' if aba_id else ""
    return f"""<svg{idt} width="{w}" height="{h + 2 * t:.0f}" viewBox="{-t} {-t} {w + 2 * t} {h + 2 * t:.0f}" style="overflow:visible;display:block">
  <rect x="0" y="0" width="{w}" height="{h:.0f}" rx="{w * .07:.0f}" fill="{fundo}" stroke="{cor}" stroke-width="{t}" stroke-linejoin="round"/>
  <path d="M{w * .06:.0f} {h * .78:.0f} L{w * .38:.0f} {h * .5:.0f} M{w * .94:.0f} {h * .78:.0f} L{w * .62:.0f} {h * .5:.0f}" fill="none" stroke="{cor}" stroke-width="{t * .8:.1f}" stroke-linecap="round"/>
  <g{aba} style="transform-origin:{w / 2:.0f}px 0px;transform-box:view-box">
    <path d="M{w * .04:.0f} {t * .2:.1f} L{w / 2:.0f} {h * .56:.0f} L{w * .96:.0f} {t * .2:.1f}" fill="{fundo}" stroke="{cor}" stroke-width="{t}" stroke-linejoin="round" stroke-linecap="round"/>
  </g>
</svg>"""


# ---------------------------------------------------------------- captura (usado pelos roteiros de captura)
def site_local():
    """Carrega o módulo que abre a cópia local do site (o arquivo .py de J/base_app que não é estado.py) e devolve
    (abrir, ir, erros_reais). Assim os roteiros de captura não repetem o nome do arquivo."""
    import importlib.util
    sys.path.insert(0, BASE_APP)
    arq = [a for a in glob.glob(os.path.join(BASE_APP, "*.py")) if os.path.basename(a) != "estado.py"][0]
    spec = importlib.util.spec_from_file_location("site_local", arq)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.abrir, m.ir, m.erros_reais



CX_JS = r"""([modo, alvo, dentro]) => {
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const proprio = e => [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
  let els = [];
  if (modo === 'sel') els = [...document.querySelectorAll(alvo)].filter(vis);
  else if (modo === 'tem') { els = [...document.querySelectorAll('body *')].filter(e => vis(e) && (e.innerText || '').replace(/\s+/g,' ').includes(alvo));
    els.sort((a,b) => (a.innerText || '').length - (b.innerText || '').length); }
  else if (modo === 're') { const rx = new RegExp(alvo); els = [...document.querySelectorAll('body *')].filter(e => vis(e) && rx.test((e.innerText || '').replace(/\s+/g,' ')));
    els.sort((a,b) => (a.innerText || '').length - (b.innerText || '').length); }
  else els = [...document.querySelectorAll('body *')].filter(e => vis(e) && (proprio(e).startsWith(alvo) || (e.children.length === 0 && e.textContent.trim().startsWith(alvo))));
  if (dentro) els = els.filter(e => e.closest(dentro));
  const el = els[0]; if (!el) return null;
  const r = el.getBoundingClientRect();
  return [Math.round(r.x*10)/10, Math.round((r.y + scrollY)*10)/10, Math.round(r.width*10)/10, Math.round(r.height*10)/10];
}"""


# caixas (px CSS, com a rolagem) de trechos de texto dentro do menor elemento visível cujo texto bate com `re_el`:
# cada alvo é uma expressão regular (espaços fixos viram espaços comuns antes da busca); devolve as linhas do trecho
TRECHOS_JS = r"""([re_el, alvos]) => {
  const N = s => s.replace(/[  ]/g, ' ');
  const rx = new RegExp(re_el);
  const els = [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().height > 0 && rx.test(N(e.textContent)))
    .sort((a,b) => a.textContent.length - b.textContent.length);
  const res = els[0]; const out = {texto: res ? N(res.textContent).replace(/\s+/g, ' ').trim() : null};
  if (!res) return out;
  const nodes = []; let acc = ''; const w = document.createTreeWalker(res, NodeFilter.SHOW_TEXT); let n;
  while ((n = w.nextNode())) { nodes.push([n, acc.length]); acc += n.textContent; }
  const plano = N(acc);
  const acha = pos => { for (let k = nodes.length - 1; k >= 0; k--) if (nodes[k][1] <= pos) return [nodes[k][0], Math.min(pos - nodes[k][1], nodes[k][0].textContent.length)]; };
  for (const alvo of alvos) {
    const m = plano.match(new RegExp(alvo)); if (!m) { out[alvo] = null; continue; }
    const i = m.index, j = i + m[0].length; const r = document.createRange(); const a = acha(i), b = acha(j);
    r.setStart(a[0], a[1]); r.setEnd(b[0], b[1]);
    out[alvo] = [...r.getClientRects()].filter(q => q.width > 1).map(q => [+q.x.toFixed(1), +(q.y + scrollY).toFixed(1), +q.width.toFixed(1), +q.height.toFixed(1)]);
  }
  return out;
}"""


async def trechos(pg, re_el, alvos):
    return _limpa(await pg.evaluate(TRECHOS_JS, [re_el, list(alvos)]))


async def medir(pg, pedidos):
    """pedidos: lista de (nome, modo, alvo[, dentro]); modo: 'sel', 'tem' (menor elemento que contém), 're' ou 'txt' (começa com)."""
    out = {}
    for p in pedidos:
        nome, modo, alvo = p[:3]
        dentro = p[3] if len(p) > 3 else None
        out[nome] = await pg.evaluate(CX_JS, [modo, alvo, dentro])
    return out


async def texto(pg, sel=None):
    if sel:
        return _limpa(await pg.evaluate("(s) => { const e = document.querySelector(s); return e ? e.innerText : null; }", sel))
    return _limpa(await pg.evaluate("() => document.body.innerText"))


# ---------------------------------------------------------------- folha de contato
def folha_video(mp4, tempos, capa_jpg, pasta, saida_jpg, cols=6, W=250):
    """Folha de contato do vídeo final: um quadro do reel.mp4 em cada instante de `tempos` (ffmpeg) e a capa da grade."""
    import subprocess, shutil
    if os.path.isdir(pasta):
        shutil.rmtree(pasta)
    os.makedirs(pasta)
    for t in tempos:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", mp4, "-frames:v", "1",
                        os.path.join(pasta, f"q_{t:05.2f}.png")], check=True)
    shutil.copy(capa_jpg, os.path.join(pasta, "capa.png"))
    return folha(pasta, saida_jpg, cols, W)


def folha(pasta_previa, saida_jpg, cols=5, W=250):
    """Folha de contato dos quadros q_*.png (e capa.png) de uma prévia. Linhas magenta: zona segura do vídeo (270 e 1600 px);
    azuis na capa: faixa de 285 a 1635 px."""
    from PIL import Image, ImageDraw, ImageFont
    arqs = sorted(glob.glob(os.path.join(pasta_previa, "q_*.png")), key=lambda a: float(os.path.basename(a)[2:-4]))
    if os.path.exists(os.path.join(pasta_previa, "capa.png")):
        arqs.append(os.path.join(pasta_previa, "capa.png"))
    H = int(W * 1920 / 1080)
    rows = (len(arqs) + cols - 1) // cols
    fl = Image.new("RGB", (cols * (W + 8) + 8, rows * (H + 34) + 8), "#8a8a8a")
    fonte = ImageFont.truetype("/tmp/inter/extras/ttf/Inter-Bold.ttf", 20)
    d = ImageDraw.Draw(fl)
    for k, a in enumerate(arqs):
        im = Image.open(a).convert("RGB").resize((W, H), Image.LANCZOS)
        x = 8 + (k % cols) * (W + 8); y = 8 + (k // cols) * (H + 34)
        fl.paste(im, (x, y + 26))
        capa = os.path.basename(a) == "capa.png"
        for gy in ((285, 1635) if capa else (270, 1600)):
            yy = y + 26 + int(gy * H / 1920)
            d.line([(x, yy), (x + W, yy)], fill="#00a0ff" if capa else "#ff00ff", width=1)
        nome = os.path.basename(a).replace("q_", "").replace(".png", "")
        d.text((x + 4, y + 3), nome + ("" if capa else " s"), fill="#000", font=fonte)
    fl.save(saida_jpg, quality=86)
    return saida_jpg
