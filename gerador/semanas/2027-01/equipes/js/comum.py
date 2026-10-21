# -*- coding: utf-8 -*-
"""Peças comuns da equipe js (Reels de 18, 21, 23, 28 e 30/01/2027), por cima do kit (J/kit/reelkit.py, sem mudança).

Reúne o que foi aprovado em novembro e dezembro (equipes r1b, r2, dr1 e dr2):
- din() e brl(): valor em reais no estilo do site ("R$" e centavos menores que o número);
- camadas() e op(): várias fotos reais empilhadas na mesma janela, trocadas como a tela do site muda;
- camera(), anelCam() e toqueCam(): câmera sobre a tela real (zoom de no máximo 1,2, para não cortar números), com
  anéis e toques que acompanham a câmera;
- recorte(): um pedaço da tela real que se solta da janela e cresce, para ler de perto;
- selo(): o selo da série "Comece 2027", da equipe ja (equipes/ja/selo_comece2027.py), carregado do arquivo dela.
Nada aqui altera uma captura: as telas só são recortadas, ampliadas e trocadas.
Capturas: a conta de base (J/base_app, sem mudança); o que muda numa captura (um toque, um filtro) só vive no navegador.
"""
import os, sys, json, importlib.util
J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
sys.path.insert(0, os.path.join(J, "kit"))
import reelkit as K
A = K.A
JS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_APP = os.path.join(J, "base_app")
MENOS = "−"            # sinal de menos, como o site
JANELA = (150, 600)    # canto da janela da tela real no Reel (kit)


def site():
    """O módulo do kit que abre a cópia local do site (J/base_app, sem mudança): abrir, ir, erros_reais.
    (O nome do módulo é o do kit, não o do produto: o timtimcash é um site.)"""
    if BASE_APP not in sys.path:
        sys.path.insert(0, BASE_APP)
    import app as kit_site
    return kit_site


def saida(pasta):
    return os.path.join(J, "saida", pasta)


def telas(pasta):
    return os.path.join(J, "saida", pasta, "telas")


def trabalho(nome):
    return os.path.join(JS_DIR, "trabalho", nome)


def _limpa(v):
    if isinstance(v, str):
        return v.replace(" ", " ").replace(" ", " ")
    if isinstance(v, dict):
        return {k: _limpa(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_limpa(x) for x in v]
    return v


def caixas(pasta):
    """Caixas (px CSS da foto) e textos medidos na captura: saida/<pasta>/telas/caixas.json
    (espaços não separáveis viram espaços comuns, para conferir os números)."""
    return _limpa(json.load(open(os.path.join(telas(pasta), "caixas.json"), encoding="utf-8")))


def brl(v, casas=2):
    """1438.8 -> '1.438,80'"""
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


def na_foto(b, rolagem):
    """Caixa medida na página (com a rolagem) -> caixa na foto (px CSS a partir do topo da foto)."""
    return [b[0], round(b[1] - rolagem, 1), b[2], b[3]]


# ---------------------------------------------------------------- selo da série "Comece 2027" (equipe ja)
SELO_JA = os.path.join(J, "equipes", "ja", "selo_comece2027.py")


def _selo_mod():
    spec = importlib.util.spec_from_file_location("selo_comece2027", SELO_JA)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


SELO = _selo_mod()          # selo(n, tam, fundo), selo_com_nome(n, tam, fundo), sobretitulo(n), NOMES


CSS = f"""
.din{{display:inline-flex;align-items:baseline;font-variant-numeric:tabular-nums;white-space:nowrap}}
.din .rs{{font-size:.44em;font-weight:600;letter-spacing:-.01em;margin-right:.3em}}
.din .cts{{font-size:.58em;font-weight:600;letter-spacing:-.02em}}
.pop{{position:absolute;left:0;top:0;opacity:0;pointer-events:none}}
.pop .pc{{position:absolute;left:0;top:0;width:100%;height:100%;overflow:hidden;border-radius:30px;background:#fff}}
.pop .pc img{{position:absolute;left:0;top:0;display:block;max-width:none}}
.tela img{{transition:none}}
.tit{{font-size:66px}}
"""

JS = r"""
// sobe com um pequeno exagero no fim (mais contido que back)
function pback2(t, a, b){ const x = clamp((t-a)/(b-a), 0, 1); const c1 = 1.1, c3 = c1 + 1; return 1 + c3*Math.pow(x-1,3) + c1*Math.pow(x-1,2); }
// recorte da tela real que se solta da janela: R = [x,y,w,h] em px CSS da foto; DE e PARA = [left, top, largura] em px do Reel.
// sobe entre a e a+d; em b some subindo (ou volta, com volta=true); troca = lista de [instante, índice da foto].
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
  const fi = DE.length > 3 ? lin(t, a, a+.25) : 1;
  e.style.opacity = (t < a) ? 0 : fi*(volta ? (q >= 1 ? 0 : 1) : 1 - q);
}
// câmera sobre a tela real: KF = [[_, _, fx, fy, s], [a, b, fx, fy, s], ...]; (fx, fy) em px CSS da foto fica no centro
// da janela (larg x alt px do Reel), com zoom s (1 = 2 px do Reel por px CSS, como no kit). Zoom máximo 1,2.
function camera(id, t, KF, larg, alt){ larg = larg || 780; alt = alt || 1000;
  let fx=KF[0][2], fy=KF[0][3], s=KF[0][4];
  for (let i=1;i<KF.length;i++){ const [a,b,x,y,z] = KF[i]; const p = prog(t,a,b); fx += (x-fx)*p; fy += (y-fy)*p; s += (z-s)*p; }
  s = Math.min(s, 1.2);
  $(id).style.transform = `translate(${(larg/2 - s*E*fx).toFixed(2)}px, ${(alt/2 - s*E*fy).toFixed(2)}px) scale(${s.toFixed(4)})`;
  return [fx, fy, s]; }
// anel cuja caixa vem de uma câmera: r em px CSS da foto, cam = [fx, fy, s] (o anel fica na janela, fora da .tela)
function anelCam(id, r, cam, pad, larg, alt){ pad = pad===undefined ? 10 : pad; larg = larg || 780; alt = alt || 1000;
  const [fx, fy, s] = cam, e = $(id), k = s*E;
  e.style.left = (larg/2 + (r[0]-fx)*k - pad)+'px'; e.style.top = (alt/2 + (r[1]-fy)*k - pad)+'px';
  e.style.width = (r[2]*k + 2*pad)+'px'; e.style.height = (r[3]*k + 2*pad)+'px'; }
// toque cuja posição vem de uma câmera (o toque fica na janela, fora da .tela)
function toqueCam(id, x, y, cam, larg, alt){ larg = larg || 780; alt = alt || 1000; const [fx, fy, s] = cam, k = s*E;
  ['t_','o_'].forEach(p=>{ const e=$(p+id); e.style.left=(larg/2 + (x-fx)*k)+'px'; e.style.top=(alt/2 + (y-fy)*k)+'px'; }); }
// opacidade de uma camada (captura) dentro da .tela
function op(id, v){ $(id).style.opacity = clamp(v, 0, 1); }
// mostra só a foto da vez: TR = [[instante, id, fusão?], ...] em ordem; troca seca (fusão 0, como a tela do site mudando)
// ou com fusão curta (em s, para a troca de uma tela por outra); f = fusão padrão das entradas sem a sua
function fotos(TR, t, f){ f = f || 0; let k = 0; TR.forEach(([a, id], i) => { if (t >= a) k = i; });
  const fk = TR[k].length > 2 ? TR[k][2] : f;
  TR.forEach(([a, id], i) => { let v = 0;
    if (i === k) v = (fk && i > 0) ? lin(t, a, a+fk) : 1;
    else if (i === k-1 && fk && t < TR[k][0] + fk) v = 1;     // a anterior fica inteira por baixo até a nova cobrir
    $(id).style.opacity = v; $(id).style.zIndex = i === k ? 2 : 1; }); }
// some (opacidade e subida curta) entre a e a+.4; sai entre b e b+.3
function some(id, t, a, b, dy){ dy = dy===undefined ? 26 : dy; const e=$(id); const vin=pout(t,a,a+.4), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=Math.min(vin, 1-vout); e.style.transform=`translateY(${(1-vin)*dy - vout*dy*.7}px)`; }
// entra e sai (opacidade e deslocamento) para qualquer elemento
function entra(id, t, a, b, dy){ dy = dy===undefined ? 70 : dy; const e=$(id); const ent=prog(t,a,a+.55), sai=b ? prog(t,b,b+.4) : 0;
  e.style.opacity=Math.min(ent, 1-sai); e.style.transform=`translateY(${(1-ent)*dy - sai*40}px)`; }
// cena inteira que sai para cima, entre a e a+.45
function saiCima(id, t, a){ const f = prog(t, a, a+.45); $(id).style.transform = `translateY(${-1920*f}px)`; }
// palavras que entram uma a uma (cada palavra num span .w)
function palavras(id, t, a, b, passo){ passo = passo || .085; const ws = $(id).querySelectorAll('.w'); for (let i=0;i<ws.length;i++){
    const p = pout(t, a + i*passo, a + i*passo + .42), o = b ? prog(t, b, b+.3) : 0;
    ws[i].style.opacity = Math.min(p, 1-o); ws[i].style.transform = `translateY(${(1-p)*34 - o*24}px)`; } }
// traço que se desenha (SVG com pathLength = 1)
function desenha(sel, t, a, d){ const p = prog(t, a, a+(d||.8)); document.querySelectorAll(sel).forEach(e => {
    e.style.strokeDasharray = '1 1'; e.style.strokeDashoffset = (1-p).toFixed(4); }); }
// nota "Tela real..." que entra e sai com a janela
function nota(id, t, a, b){ const n = prog(t, a, a+.6); $(id).style.opacity = n*(b ? 1 - prog(t, b, b+.4) : 1);
  $(id).style.transform = `translateY(${(1-n)*80}px)`; }
"""


def pop_html(pid, srcs, aneis_html=""):
    """Recorte que salta: uma ou mais fotos (mesma geometria) e os anéis por cima (posição final)."""
    imgs = "".join(f'<img src="file://{s}">' for s in (srcs if isinstance(srcs, (list, tuple)) else [srcs]))
    return f'<div class="pop" id="{pid}"><div class="pc">{imgs}</div>{aneis_html}</div>'


def camadas(tid, imgs, extra="", altura_css=None):
    """Várias fotos reais empilhadas na mesma .tela (a primeira visível). imgs: lista de (id, caminho)."""
    alt = f"height:{altura_css * 2}px;" if altura_css else ""
    ims = "".join(f'<img id="{i}" src="file://{c}" style="opacity:{1 if k == 0 else 0}">' for k, (i, c) in enumerate(imgs))
    return f'<div class="tela" id="{tid}" style="{alt}">{ims}{extra}</div>'


def anel_no_recorte(aid, R, PARA, r, pad=12, cor=""):
    """Anel (classe do kit) dentro do recorte, na escala final: r = caixa em px CSS da foto."""
    s = PARA[2] / R[2]
    x, y, w, h = (r[0] - R[0]) * s - pad, (r[1] - R[1]) * s - pad, r[2] * s + 2 * pad, r[3] * s + 2 * pad
    return f'<div class="anel {cor}" id="{aid}" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px"></div>'


def palavras_html(ident, texto, destaque=(), cls=""):
    """Cada palavra num <span class="w"> (entram uma a uma). destaque: índices das palavras em destaque (<b>)."""
    ws = texto.split(" ")
    return f'<div class="{cls}" id="{ident}">' + " ".join(
        (f'<span class="w"><b>{w}</b></span>' if i in destaque else f'<span class="w">{w}</span>') for i, w in enumerate(ws)) + "</div>"


def pagina(corpo, css, js):
    return K.pagina(corpo, CSS + css, JS + js)


# ---------------------------------------------------------------- captura (usado pelos roteiros de captura)
# caixa (px CSS da página, com a rolagem) de um seletor ('sel'), do menor elemento que contém um texto ('tem')
# ou do primeiro cujo texto próprio começa com ('txt'); 'dentro' limita a busca a um seletor
CX_JS = r"""([modo, alvo, dentro]) => {
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const proprio = e => [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
  let todos = [...document.querySelectorAll(dentro ? dentro + ' *' : 'body *')].filter(e => !e.closest('.sidebar,aside,nav'));
  let el = null;
  if (modo === 'sel') el = [...document.querySelectorAll(alvo)].find(vis);
  else if (modo === 'tem') { const c = todos.filter(e => vis(e) && e.textContent.replace(/\s+/g,' ').includes(alvo));
    c.sort((a,b) => a.textContent.length - b.textContent.length); el = c[0] || null; }
  else el = todos.find(e => vis(e) && (proprio(e).startsWith(alvo) || (e.children.length === 0 && e.textContent.trim().startsWith(alvo))));
  if (!el) return null;
  const r = el.getBoundingClientRect();
  return [Math.round(r.x*10)/10, Math.round((r.y + scrollY)*10)/10, Math.round(r.width*10)/10, Math.round(r.height*10)/10,
          (el.innerText || el.value || '').replace(/\s+/g, ' ').trim().slice(0, 240)];
}"""

# caixa do cartão (painel com canto arredondado e fundo ou borda) que contém o elemento achado como em CX_JS
CARTAO_JS = r"""([modo, alvo, larg_min]) => {
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const proprio = e => [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
  const todos = [...document.querySelectorAll('body *')].filter(e => !e.closest('.sidebar,aside,nav'));
  let h = null;
  if (modo === 'sel') h = [...document.querySelectorAll(alvo)].find(vis);
  else h = todos.find(e => vis(e) && (proprio(e).startsWith(alvo) || (e.children.length === 0 && e.textContent.trim().startsWith(alvo))));
  if (!h) return null;
  let c = h.parentElement;
  while (c && c !== document.body) { const s = getComputedStyle(c), r = c.getBoundingClientRect();
    const fundo = s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== 'transparent';
    if (parseFloat(s.borderTopLeftRadius) >= 10 && (fundo || s.borderTopWidth !== '0px' || s.boxShadow !== 'none') && r.width >= (larg_min || 280)) break;
    c = c.parentElement; }
  if (!c || c === document.body) return null;
  const r = c.getBoundingClientRect();
  return [Math.round(r.x*10)/10, Math.round((r.y + scrollY)*10)/10, Math.round(r.width*10)/10, Math.round(r.height*10)/10,
          (c.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 300)];
}"""


async def medir(pg, pedidos):
    """pedidos: (nome, modo, alvo[, dentro]); modo 'sel', 'tem', 'txt' ou 'cartao' (alvo = texto do começo)."""
    out = {}
    for p in pedidos:
        nome, modo, alvo = p[:3]
        if modo == "cartao":
            out[nome] = await pg.evaluate(CARTAO_JS, [p[3] if len(p) > 3 else "txt", alvo, p[4] if len(p) > 4 else 280])
        else:
            dentro = p[3] if len(p) > 3 else None
            out[nome] = await pg.evaluate(CX_JS, [modo, alvo, dentro])
    return out


async def foto(pg, pasta_telas, nome, info, pedidos=(), texto_js="document.body.innerText"):
    """Fotografa a página (JPEG 95), mede as caixas pedidas e guarda o texto da tela e a rolagem em info[nome]."""
    caminho = os.path.join(pasta_telas, nome)
    await pg.screenshot(path=caminho, type="jpeg", quality=95)
    cx = await medir(pg, pedidos) if pedidos else {}
    cx["rolagem"] = await pg.evaluate("scrollY")
    cx["viewport"] = await pg.evaluate("[innerWidth, innerHeight]")
    cx["texto"] = (await pg.evaluate(texto_js))[:4000]
    info[nome] = cx
    print("foto", nome, {k: (v[:4] if isinstance(v, list) else v) for k, v in cx.items() if k != "texto"})
    return cx
