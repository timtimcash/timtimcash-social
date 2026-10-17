# -*- coding: utf-8 -*-
"""Gerador de Reels do timtimcash para novembro e dezembro de 2026 (1080 × 1920, 30 fps).

Junta os kits de outubro (reels-a e reels-b): cada quadro é desenhado no Chromium por render(t) e vai direto
para o ffmpeg com os mesmos parâmetros dos Reels aprovados. Novidades:
- o vídeo começa já em movimento (o gancho no primeiro segundo); a capa da grade é uma página própria
  (capa_html), desenhada no fundo do calendário, e não um quadro do vídeo;
- contadores de valor (contar), texto digitado (digitar), barras que crescem (barra) e fundos (verde, tinta, suave, papel).

Uso num roteiro (reel_<data>.py):
    import sys; sys.path.insert(0, "<novdez>/kit"); import reelkit as K; A = K.A
    HTML = K.pagina(CORPO, CSS_EXTRA, JS_RENDER)          # JS_RENDER define function render(t){...}
    CAPA = K.pagina_capa(CORPO_CAPA, CSS_EXTRA_CAPA, fundo="tinta")
    K.executar(HTML, DUR, pasta_saida, trabalho, capa_html=CAPA)
Variáveis de ambiente:
    REEL_PREVIA="0.5 4 9"   grava só quadros soltos em PNG em <trabalho>/previa/ (e a capa), sem vídeo.

Zona segura (regra do Samuel, gerador/MARCA.md): nada importante nos 270 px de cima (nome do perfil e áudio);
títulos das cenas a partir de 280 px, logo da capa a partir de 290 px; nada importante abaixo de 1600 px
(legenda) nem encostado na borda direita da metade de baixo (botões). Na capa da grade, o essencial fica na
faixa central de 1080 × 1350 (de 285 a 1635 px), que sobrevive ao recorte 4:5 do feed e 3:4 da grade.
"""
import os, sys, subprocess, asyncio
sys.path.insert(0, "/home/claude/timtimcash-social/gerador")
import artes as A
from playwright.async_api import async_playwright

FPS = 30
FUNDO_TELA = "#F7F6F1"   # fundo da página do site no celular (medido nas telas reais)
ACESSE = "Acesse pelo navegador, no computador ou no celular."
NOTA = "Tela real do timtimcash, com dados de exemplo"
DARK_TEXTO = "#C9D1C8"   # texto de apoio sobre a tinta
CORAL_TXT = "#B4532F"    # coral escuro para texto pequeno sobre o papel (4,8:1)
CORAL_FORTE = "#9A3F22"

FUNDOS = {"papel": (A.BG, A.INK), "tinta": (A.INK, "#fff"), "suave": (A.SOFT, A.INK), "verde": (A.BRAND, "#fff")}
LOGO_VAR = {"papel": "color", "tinta": "dark", "suave": "color", "verde": "white"}


# ---------------------------------------------------------------- CSS
def css(extra=""):
    return f"""{A.font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:{A.BG}}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;font-feature-settings:'cv11','ss01';color:{A.INK}}}
.cena{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden}}
.papel{{background:{A.BG};color:{A.INK}}}
.verde{{background:{A.BRAND};color:#fff}}
.tinta{{background:{A.INK};color:#fff}}
.suave{{background:{A.SOFT};color:{A.INK}}}
.eyebrow{{font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{A.BRAND_DARK}}}
.tinta .eyebrow{{color:{A.MENTA}}}
.verde .eyebrow{{color:#fff}}
.suave .eyebrow{{color:{A.BRAND_DEEP}}}
.h1{{font-size:124px;line-height:.98;font-weight:700;letter-spacing:-.05em;text-wrap:balance}}
.h2{{font-size:96px;line-height:1.0;font-weight:700;letter-spacing:-.048em;text-wrap:balance}}
.tit{{position:absolute;left:90px;top:280px;width:900px;font-size:64px;line-height:1.06;font-weight:700;letter-spacing:-.045em;text-wrap:balance;opacity:0}}
.tit b{{color:{A.BRAND_DARK};font-weight:700}}
.tinta .tit b{{color:{A.MENTA}}}
.verde .tit b{{color:#fff;text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:10px}}
.sobre{{display:block;font-size:30px;line-height:1;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{A.BRAND_DARK};margin-bottom:26px}}
.tinta .sobre{{color:{A.MENTA}}}
.nota{{position:absolute;left:150px;top:548px;font-size:26px;font-weight:500;color:{A.MUTED};letter-spacing:-.005em;opacity:0}}
.tinta .nota{{color:{DARK_TEXTO}}}
.janela{{position:absolute;left:150px;top:600px;width:780px;height:1000px;border-radius:44px;overflow:hidden;background:#fff;
  border:2px solid {A.FIO};box-shadow:0 2px 4px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.28);opacity:0}}
.tela{{position:absolute;left:0;top:0;width:780px;transform-origin:0 0;background:{FUNDO_TELA};will-change:transform}}
.tela img{{position:absolute;left:0;top:0;display:block;width:780px;height:auto}}
.anel{{position:absolute;border-radius:28px;border:9px solid {A.BRAND};opacity:0;pointer-events:none}}
.anel.coral{{border-color:{A.RED}}}
.anel.ambar{{border-color:{A.AMBER_BAR}}}
.toque{{position:absolute;width:110px;height:110px;margin:-55px 0 0 -55px;border-radius:50%;background:rgba(15,20,16,.16);border:6px solid #fff;
  box-shadow:0 6px 18px rgba(15,20,16,.25);opacity:0}}
.onda{{position:absolute;width:110px;height:110px;margin:-55px 0 0 -55px;border-radius:50%;border:6px solid {A.BRAND};opacity:0}}
.apoio{{font-size:40px;line-height:1.3;font-weight:500;color:{A.MUTED};letter-spacing:-.02em;text-wrap:balance}}
.tinta .apoio{{color:{DARK_TEXTO}}}
.verde .apoio{{color:#fff}}
.chip{{display:inline-flex;align-items:center;height:92px;padding:0 40px;border-radius:999px;background:#fff;border:3px solid {A.FIO};
  font-size:38px;font-weight:600;color:{A.INK};letter-spacing:-.01em}}
.pill{{display:inline-flex;align-items:center;gap:16px;background:#fff;color:{A.BRAND_DARK};font-weight:600;font-size:44px;padding:28px 48px;border-radius:999px}}
.num{{font-variant-numeric:tabular-nums}}
.card{{background:#fff;border-radius:36px;border:2px solid {A.FIO};box-shadow:0 1px 2px rgba(15,20,16,.04),0 14px 34px -16px rgba(15,20,16,.14)}}
.tinta .card{{background:#192019;border-color:#262E27;box-shadow:none}}
{extra}"""


# ---------------------------------------------------------------- JavaScript comum
JS = r"""
const $ = id => document.getElementById(id);
const clamp = (x,a,b) => Math.min(b, Math.max(a, x));
const ease = x => x<.5 ? 4*x*x*x : 1-Math.pow(-2*x+2,3)/2;
const easeOut = x => 1-Math.pow(1-x,3);
const back = x => { const c1=1.70158, c3=c1+1; return 1 + c3*Math.pow(x-1,3) + c1*Math.pow(x-1,2); };   // passa um pouco e volta
const prog = (t,a,b) => ease(clamp((t-a)/(b-a),0,1));
const pout = (t,a,b) => easeOut(clamp((t-a)/(b-a),0,1));
const pback = (t,a,b) => back(clamp((t-a)/(b-a),0,1));
const lin = (t,a,b) => clamp((t-a)/(b-a),0,1);
const E = 2;          // tela do celular (390 px CSS) na janela de 780 px: 1 px CSS = 2 px do Reel
// número no formato brasileiro: fmt(2819.8, 2) -> "2.819,80"
function fmt(v, casas){ casas = casas===undefined ? 2 : casas; const s = Math.abs(v).toFixed(casas).split('.');
  s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.'); return (v<0 ? '−' : '') + s[0] + (casas ? ',' + s[1] : ''); }
// contador: escreve em `id` o valor indo de v0 a v1 entre a e b (com prefixo e sufixo)
function contar(id, t, a, b, v0, v1, casas, pre, suf){ const p = pout(t,a,b); const v = v0 + (v1-v0)*p;
  $(id).textContent = (pre||'') + fmt(v, casas) + (suf||''); }
// texto digitado: mostra os primeiros caracteres de `txt` a `cps` caracteres por segundo, a partir de a (cursor opcional)
function digitar(id, t, a, txt, cps, cursor){ const n = clamp(Math.floor((t-a)*(cps||12)), 0, txt.length);
  const pisca = cursor && (Math.floor(t*2.2) % 2 === 0) ? '|' : (cursor ? ' ' : '');
  $(id).textContent = txt.slice(0, n) + (n < txt.length || cursor ? pisca : ''); }
// título: entra em a, sai em b (0,35 s e 0,3 s), com deslocamento vertical
function titulo(id, t, a, b, dy){ dy = dy===undefined ? 28 : dy; const e=$(id); const vin=prog(t,a,a+.35), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=Math.min(vin, 1-vout); e.style.transform=`translateY(${(1-vin)*dy - vout*dy}px)`; }
// aparece (opacidade e subida) entre a e a+d; some entre b e b+.3
function aparece(id, t, a, b, dy, d){ dy = dy===undefined ? 40 : dy; d = d || .4; const e=$(id); const vin=pout(t,a,a+d), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=Math.min(vin, 1-vout); e.style.transform=`translateY(${(1-vin)*dy - vout*dy*.5}px)`; }
// salta: entra crescendo com um pequeno exagero (para números e selos)
function salta(id, t, a, d){ d = d || .45; const e=$(id); const p = pback(t,a,a+d);
  e.style.opacity = lin(t,a,a+.15); e.style.transform = `scale(${.6 + .4*p})`; }
// barra que cresce: largura (ou altura, se vertical) de 0 até `alvo` px entre a e b
function barra(id, t, a, b, alvo, vertical){ const v = alvo*pout(t,a,b); $(id).style[vertical ? 'height' : 'width'] = v + 'px'; }
// anel de destaque numa caixa [x,y,w,h] em px CSS da tela do celular (E = 2), com folga `pad` px do Reel
function poeAnel(id, r, pad){ pad = pad===undefined ? 10 : pad; const e=$(id); e.style.left=(r[0]*E-pad)+'px'; e.style.top=(r[1]*E-pad)+'px';
  e.style.width=(r[2]*E+2*pad)+'px'; e.style.height=(r[3]*E+2*pad)+'px'; }
function anel(id, t, a, b){ const e=$(id); const vi=prog(t,a,a+.35), vo=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=vi*(1-vo); e.style.transform=`scale(${1.06-.06*vi})`; }
// toque de dedo num ponto (x, y) em px CSS da tela: chega em t0-.1, aperta em t0+.15, a onda abre de t0+.2 a t0+.8
function poeToque(id, x, y){ ['t_','o_'].forEach(p=>{ const e=$(p+id); e.style.left=(x*E)+'px'; e.style.top=(y*E)+'px'; }); }
function toque(id, t, t0){ const tq=$('t_'+id), on=$('o_'+id);
  tq.style.opacity = (t>=t0-.1 && t<t0+.9) ? (t<t0 ? lin(t,t0-.1,t0) : 1-lin(t,t0+.5,t0+.8)) : 0;
  tq.style.transform = `scale(${t<t0+.15 ? 1 : .86})`;
  on.style.opacity = (t>=t0+.2 && t<=t0+.8) ? (1-lin(t,t0+.2,t0+.8)) : 0;
  on.style.transform = `scale(${1+1.6*lin(t,t0+.2,t0+.8)})`; }
// panorâmica de uma tela (camada .tela): `topo` = px CSS do celular no alto da janela
function pan(id, topo){ $(id).style.transform = `translateY(${-topo*E}px)`; }
// janela da tela real: entra por baixo entre a e a+.6, sai entre b e b+.4
function janela(id, t, a, b){ const e=$(id); const ent=prog(t,a,a+.6), sai=b ? prog(t,b,b+.4) : 0;
  e.style.opacity=Math.min(ent, 1-sai); e.style.transform=`translateY(${(1-ent)*80 - sai*40}px)`; }
// cena inteira que sobe (como o fechamento): de baixo para cima entre a e a+.45
function sobe(id, t, a){ const f = prog(t, a, a+.45); $(id).style.transform = `translateY(${1920*(1-f)}px)`; }
"""


# ---------------------------------------------------------------- peças comuns
def tela(tid, src, altura_css=None, extra=""):
    """Camada de tela real do celular (imagem em escala 3, 1170 px de largura) dentro da janela de 780 px."""
    alt = f"height:{altura_css * 2}px;" if altura_css else ""
    return f'<div class="tela" id="{tid}" style="{alt}"><img src="file://{src}">{extra}</div>'


def aneis(*ids, cor=""):
    return "".join(f'<div class="anel {cor}" id="{i}"></div>' for i in ids)


def toques(*ids):
    return "".join(f'<div class="toque" id="t_{i}"></div><div class="onda" id="o_{i}"></div>' for i in ids)


def fim(nome, linha=ACESSE):
    """Fechamento verde (igual ao dos Reels aprovados): logotipo vertical negativo, nome, linha de apoio e Link na bio.
    Entra com sobe('fim', t, FIM)."""
    return f"""<div class="cena verde" id="fim" style="transform:translateY(1920px)">
  <div style="position:absolute;left:0;top:470px;width:1080px;display:flex;flex-direction:column;align-items:center;text-align:center">
    {A.logo_vertical("white", 300)}
    <div style="font-size:66px;font-weight:700;letter-spacing:-.045em;line-height:1.06;margin-top:90px;width:860px;text-wrap:balance">{nome}</div>
    <div style="font-size:40px;font-weight:500;letter-spacing:-.02em;line-height:1.3;margin-top:30px;width:820px;text-wrap:balance">{linha}</div>
    <div style="margin-top:70px"><span class="pill">Link na bio {A.ARROW}</span></div>
  </div>
</div>"""


def logo(fundo, altura=60, top=290, left=90):
    """Logotipo horizontal na versão certa para o fundo, a partir de 290 px (zona segura)."""
    return f'<div style="position:absolute;left:{left}px;top:{top}px">{A.logo_horizontal(LOGO_VAR[fundo], altura)}</div>'


def pagina(corpo, css_extra, js_render):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
{css(css_extra)}
</style></head><body>
{corpo}
<script>{JS}
{js_render}
render(0);
</script></body></html>"""


def pagina_capa(corpo, css_extra="", fundo="papel"):
    """Capa da grade (1080 × 1920): página estática no fundo do calendário. O essencial fica entre 285 e 1635 px."""
    bg, cor = FUNDOS[fundo]
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
{css(css_extra)}
html,body{{background:{bg};color:{cor}}}
</style></head><body><div class="cena {fundo}" id="capa">{corpo}</div></body></html>"""


# ---------------------------------------------------------------- saída
async def _abrir(p, html_path):
    b = await p.chromium.launch(args=["--font-render-hinting=none"])
    pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    await pg.goto("file://" + html_path)
    await pg.evaluate("document.fonts.ready")
    await pg.wait_for_timeout(800)
    return b, pg


async def _previa(html_path, tempos, destino, capa_path=None):
    os.makedirs(destino, exist_ok=True)
    async with async_playwright() as p:
        b, pg = await _abrir(p, html_path)
        for t in tempos:
            await pg.evaluate(f"render({t})")
            await pg.screenshot(path=os.path.join(destino, f"q_{t:05.2f}.png"))
        if capa_path:
            await pg.goto("file://" + capa_path)
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=os.path.join(destino, "capa.png"))
        await b.close()


async def _video(html_path, dur, saida, capa_jpg, capa_path, capa_t):
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000", "-shortest",
        "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-g", str(FPS), "-keyint_min", str(FPS), "-sc_threshold", "0",
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-movflags", "+faststart", "-use_editlist", "0", saida], stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b, pg = await _abrir(p, html_path)
        n = int(round(dur * FPS))
        for i in range(n):
            await pg.evaluate(f"render({i / FPS:.5f})")
            ff.stdin.write(await pg.screenshot(type="jpeg", quality=96))
        if capa_path:
            await pg.goto("file://" + capa_path)
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(600)
            await pg.screenshot(path=capa_jpg, type="jpeg", quality=94)
        elif capa_t is not None:
            await pg.evaluate(f"render({capa_t})")
            await pg.screenshot(path=capa_jpg, type="jpeg", quality=94)
        await b.close()
    ff.stdin.close(); ff.wait()
    return n


def executar(html, dur, pasta, trabalho, capa_html=None, capa_t=None):
    """pasta: <novdez>/saida/<pasta do post> (reel.mp4, capa.jpg, previa.mp4); trabalho: HTML e prévias do Reel."""
    os.makedirs(pasta, exist_ok=True); os.makedirs(trabalho, exist_ok=True)
    html_path = os.path.join(trabalho, "reel.html")
    open(html_path, "w", encoding="utf-8").write(html)
    capa_path = None
    if capa_html:
        capa_path = os.path.join(trabalho, "capa.html")
        open(capa_path, "w", encoding="utf-8").write(capa_html)
    if os.environ.get("REEL_PREVIA"):
        tempos = [float(x) for x in os.environ["REEL_PREVIA"].split()]
        asyncio.run(_previa(html_path, tempos, os.path.join(trabalho, "previa"), capa_path))
        print("prévias em", os.path.join(trabalho, "previa"))
        return
    saida = os.path.join(pasta, "reel.mp4")
    n = asyncio.run(_video(html_path, dur, saida, os.path.join(pasta, "capa.jpg"), capa_path, capa_t))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", saida, "-vf", "scale=720:1280", "-c:v", "libx264", "-crf", "28",
                    "-preset", "veryfast", "-an", "-movflags", "+faststart", os.path.join(pasta, "previa.mp4")], check=True)
    print("ok", saida, n, "quadros")
