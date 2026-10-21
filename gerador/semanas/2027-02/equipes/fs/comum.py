# -*- coding: utf-8 -*-
"""Peças comuns da equipe fs (Reels de 18, 20, 23, 25 e 27/02/2027), por cima do kit (J/kit/reelkit.py, sem mudança).

Reúne o que foi aprovado em novembro e dezembro:
- captura: o site pela cópia da equipe (estado.py e o site iguais aos da base, os cenários em cenarios.py) e as caixas medidas em px CSS da página (medir), como a dr2;
- camadas(): várias fotos reais empilhadas na mesma .tela, para trocar de passo como o site troca (dr2);
- camera(): panorâmica e zoom sobre a tela real (dr2), com a largura da tela como parâmetro (390 no celular, 1440 no
  computador);
- recorte(): um pedaço da mesma foto que se solta da janela e cresce, para ler de perto (r1b e dr1), também com a
  largura da tela como parâmetro;
- din(): valor em reais com "R$" e centavos menores, como o site (r1b).
Nada aqui altera uma captura: as telas só são recortadas, ampliadas e trocadas.
"""
import os, sys, json
J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
sys.path.insert(0, os.path.join(J, "kit"))
import reelkit as K
A = K.A
FS = os.path.dirname(os.path.abspath(__file__))
# a cópia da conta da equipe: a pasta (com o nome que o BRIEFING pede) que guarda estado.py e o site
COPIA = os.path.join(FS, next(d for d in sorted(os.listdir(FS)) if os.path.isfile(os.path.join(FS, d, "estado.py"))))
MENOS = "−"            # sinal de menos, como o site
JANELA = (150, 600)    # canto da janela da tela real no Reel (kit)


def saida(pasta):
    return os.path.join(J, "saida", pasta)


def telas(pasta):
    return os.path.join(J, "saida", pasta, "telas")


def trabalho(nome):
    return os.path.join(FS, "trabalho", nome)


def _limpa(v):
    if isinstance(v, str):
        return v.replace(" ", " ").replace(" ", " ")
    if isinstance(v, dict):
        return {k: _limpa(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_limpa(x) for x in v]
    return v


def caixas(pasta, nome="caixas.json"):
    """Caixas (px CSS) e textos medidos na captura (espaços fixos viram espaços comuns, para conferir os números)."""
    return _limpa(json.load(open(os.path.join(telas(pasta), nome), encoding="utf-8")))


def brl(v, casas=2):
    """1438.8 -> '1.438,80'"""
    s = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return (MENOS if v < 0 else "") + s


# ---------------------------------------------------------------- captura
# caixa (px CSS da página, com a rolagem) de um seletor ('sel'), do menor elemento visível que contém um texto ('tem')
# ou do primeiro cujo texto próprio começa com ('txt')
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


async def foto(pg, pasta_telas, nome, info, pedidos=(), texto_js="document.body.innerText", qualidade=95):
    """Fotografa a página inteira da janela (JPEG) e guarda as caixas e o texto da tela em info[nome]."""
    await pg.screenshot(path=os.path.join(pasta_telas, nome), type="jpeg", quality=qualidade)
    cx = await medir(pg, pedidos) if pedidos else {}
    cx["texto"] = (await pg.evaluate(texto_js))[:3000]
    cx["rolagem"] = await pg.evaluate("scrollY")
    info[nome] = cx
    print("foto", nome, {k: v for k, v in cx.items() if k not in ("texto",)})


def folha(saida_jpg, imgs, cols=4, larg=270, rotulos=None):
    """Folha de contato (para olhar as prévias): imagens lado a lado com o nome embaixo."""
    from PIL import Image, ImageDraw
    ims = [Image.open(p).convert("RGB") for p in imgs]
    alt = max(int(larg * im.size[1] / im.size[0]) for im in ims)
    gap, rot = 14, 26
    rows = (len(ims) + cols - 1) // cols
    F = Image.new("RGB", (cols * larg + (cols + 1) * gap, rows * (alt + rot) + (rows + 1) * gap), (205, 205, 200))
    d = ImageDraw.Draw(F)
    for i, (im, p) in enumerate(zip(ims, imgs)):
        r, c = divmod(i, cols)
        h = int(larg * im.size[1] / im.size[0])
        x, y = gap + c * (larg + gap), gap + r * (alt + rot + gap)
        F.paste(im.resize((larg, h), Image.LANCZOS), (x, y + rot))
        d.text((x + 2, y + 6), (rotulos[i] if rotulos else os.path.basename(p))[:44], fill=(0, 0, 0))
    F.save(saida_jpg, quality=88)
    return saida_jpg


# ---------------------------------------------------------------- peças do Reel
def camadas(tid, imgs, extra="", largura_css=390, altura_css=None):
    """imgs: lista de (id, caminho). A primeira começa visível; as outras, transparentes. 1 px CSS = 2 px do Reel."""
    alt = f"height:{altura_css * 2}px;" if altura_css else ""
    ims = "".join(f'<img id="{i}" src="file://{c}" style="width:{largura_css * 2}px;opacity:{1 if k == 0 else 0}">'
                  for k, (i, c) in enumerate(imgs))
    return f'<div class="tela camadas" id="{tid}" style="width:{largura_css * 2}px;{alt}">{ims}{extra}</div>'


def pop_html(pid, srcs, aneis_html=""):
    """Recorte que salta: uma ou mais fotos (mesma geometria) e os anéis por cima (posição final)."""
    imgs = "".join(f'<img src="file://{s}">' for s in (srcs if isinstance(srcs, (list, tuple)) else [srcs]))
    return f'<div class="pop" id="{pid}"><div class="pc">{imgs}</div>{aneis_html}</div>'


def anel_no_recorte(aid, R, PARA, r, pad=12, cor=""):
    """Anel (classe do kit) dentro do recorte, na escala final: r = caixa em px CSS da tela."""
    s = PARA[2] / R[2]
    x, y, w, h = (r[0] - R[0]) * s - pad, (r[1] - R[1]) * s - pad, r[2] * s + 2 * pad, r[3] * s + 2 * pad
    return f'<div class="anel {cor}" id="{aid}" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px"></div>'


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


def folga(b, dx, dy=None):
    dy = dx if dy is None else dy
    return [round(b[0] - dx, 1), round(b[1] - dy, 1), round(b[2] + 2 * dx, 1), round(b[3] + 2 * dy, 1)]


def tecla(txt, cls="", ident=""):
    """Tecla desenhada (CSS .kc): letra, símbolo ou palavra."""
    i = f' id="{ident}"' if ident else ""
    return f'<span class="kc {cls}"{i}><span class="kt">{txt}</span></span>'


CMD = ('<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="2.1" '
       'stroke-linecap="round" stroke-linejoin="round" style="display:block"><path d="M9 6v12M15 6v12M6 9h12M6 15h12"/>'
       '<path d="M9 9H7.5A1.5 1.5 0 1 1 9 7.5V9zM15 9h1.5A1.5 1.5 0 1 0 15 7.5V9zM9 15H7.5A1.5 1.5 0 1 0 9 16.5V15zM15 15h1.5A1.5 1.5 0 1 1 15 16.5V15z"/></svg>')


CSS = f"""
.din{{display:inline-flex;align-items:baseline;font-variant-numeric:tabular-nums;white-space:nowrap}}
.din .rs{{font-size:.44em;font-weight:600;letter-spacing:-.01em;margin-right:.34em}}
.din .cts{{font-size:.58em;font-weight:600;letter-spacing:-.02em}}
.tela img{{position:absolute;left:0;top:0;display:block;height:auto;transition:none}}
.pop{{position:absolute;left:0;top:0;opacity:0;pointer-events:none}}
.pop .pc{{position:absolute;left:0;top:0;width:100%;height:100%;overflow:hidden;border-radius:30px;background:#fff}}
.pop .pc img{{position:absolute;left:0;top:0;display:block;max-width:none}}
.veu{{position:absolute;left:0;top:0;width:100%;height:100%;background:{A.BG};opacity:0;pointer-events:none}}
/* tecla desenhada */
.kc{{display:inline-flex;align-items:center;justify-content:center;min-width:1.9em;height:1.9em;padding:0 .5em;border-radius:.34em;
  background:#fff;color:{A.INK};font-weight:700;letter-spacing:-.02em;line-height:1;
  box-shadow:0 .09em 0 #D4D2C8,0 .14em .3em rgba(15,20,16,.18),inset 0 0 0 .035em {A.FIO};will-change:transform;white-space:nowrap}}
.kc .kt{{display:inline-flex;align-items:center;gap:.18em}}
.kc.on{{background:{A.SOFT};color:{A.BRAND_DEEP};box-shadow:0 .02em 0 #9FD9BF,0 .05em .12em rgba(15,20,16,.18),inset 0 0 0 .05em {A.BRAND}}}
.mais{{display:inline-block;font-weight:600;margin:0 .22em;color:{A.MUTED}}}
"""

JS = r"""
// entra e sai (opacidade e deslocamento) para qualquer elemento
function entra(id, t, a, b, dy){ dy = dy===undefined ? 70 : dy; const e=$(id); const ent=prog(t,a,a+.55), sai=b ? prog(t,b,b+.4) : 0;
  e.style.opacity=Math.min(ent, 1-sai); e.style.transform=`translateY(${(1-ent)*dy - sai*40}px)`; }
// cena inteira que sai para cima, entre a e a+.45
function saiCima(id, t, a){ const f = prog(t, a, a+.45); $(id).style.transform = `translateY(${-1920*f}px)`; }
// opacidade de uma camada (captura) dentro da .tela
function op(id, v){ $(id).style.opacity = clamp(v, 0, 1); }
// fotos empilhadas: a de índice k vale a partir de TR[k] (corte seco, como a tela do site mudando)
function fotos(ids, t, TR){ let k = 0; TR.forEach((a, i) => { if (t >= a) k = i; }); ids.forEach((id, i) => { $(id).style.opacity = i === k ? 1 : 0; }); return k; }
// câmera sobre a tela real: KF = [[_, _, fx, fy, s], [a, b, fx, fy, s], ...]; o ponto (fx, fy) em px CSS fica no centro da
// janela (larg x alt px do Reel), com zoom s (1 = 2 px do Reel por px CSS)
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
// sobe com um pequeno exagero no fim (mais contido que back)
function pback2(t, a, b){ const x = clamp((t-a)/(b-a), 0, 1); const c1 = 1.1, c3 = c1 + 1; return 1 + c3*Math.pow(x-1,3) + c1*Math.pow(x-1,2); }
// recorte da tela real que se solta da janela: R = [x,y,w,h] em px CSS da tela (de largura LW px CSS); DE e PARA =
// [left, top, largura] em px do Reel; sobe entre a e a+d; some em b; troca = lista de [instante, índice da foto]
function recorte(id, t, a, b, R, DE, PARA, d, troca, LW){
  d = d || .6; LW = LW || 390; const e = $(id), pc = e.querySelector('.pc');
  const p = pback2(t, a, a+d), q = b ? prog(t, b, b+.38) : 0;
  const L = DE[0] + (PARA[0]-DE[0])*p, T = DE[1] + (PARA[1]-DE[1])*p, W = DE[2] + (PARA[2]-DE[2])*p;
  const s = W / R[2];
  e.style.left = L+'px'; e.style.top = (T - 40*q)+'px'; e.style.width = W+'px'; e.style.height = (R[3]*s)+'px';
  const imgs = e.querySelectorAll('img');
  let foto = 0; if (troca) troca.forEach(([ti, k]) => { if (t >= ti) foto = k; });
  imgs.forEach((im, k) => { im.style.width = (LW*s)+'px'; im.style.left = (-R[0]*s)+'px'; im.style.top = (-R[1]*s)+'px';
    im.style.opacity = (k === foto) ? 1 : 0; });
  pc.style.boxShadow = `0 0 0 2px rgba(236,233,224,${p}), 0 ${34*p}px ${70*p}px -24px rgba(15,20,16,${.42*p})`;
  const fi = DE.length > 3 ? lin(t, a, a+.25) : 1;
  e.style.opacity = (t < a) ? 0 : fi*(1 - q);
}
// some (opacidade e subida curta) entre a e a+.4; sai entre b e b+.3
function some(id, t, a, b, dy){ dy = dy===undefined ? 26 : dy; const e=$(id); const vin=pout(t,a,a+.4), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=Math.min(vin, 1-vout); e.style.transform=`translateY(${(1-vin)*dy - vout*dy*.7}px)`; }
// tecla que aperta em t0 (desce e fica verde por um instante) e volta
function aperta(id, t, t0, dur){ dur = dur || .32; const e=$(id); const d = (t>=t0 && t<t0+dur) ? Math.sin(Math.PI*clamp((t-t0)/dur,0,1)) : 0;
  e.style.transform = `translateY(${(d*.085).toFixed(3)}em) scale(${(1 - .03*d).toFixed(3)})`; e.classList.toggle('on', d > .15); }
"""


def pagina(corpo, css, js):
    return K.pagina(corpo, CSS + css, JS + js)
