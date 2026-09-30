# -*- coding: utf-8 -*-
"""Pequeno gerador de Reels do timtimcash (1080 × 1920, 30 fps), a partir do Reel aprovado de 30/09
(base_app/modelo_reel/reel.py): cada quadro é desenhado no Chromium por render(t) e vai direto
para o ffmpeg, com exatamente os mesmos parâmetros do modelo.

Cada Reel (reel_*.py) monta o HTML das cenas e a função JavaScript render(t) e chama:
    reelkit.executar(html, dur, pasta_saida, capa_t)
Variáveis de ambiente:
    REEL_PREVIA="0.5 4 9"   grava só quadros soltos em PNG (pasta_saida/../previa_<pasta>/), sem vídeo.
Zona segura do Instagram: nada importante nos 270 px de cima (14% da altura), onde o app põe o nome do perfil
e o áudio. Por isso o título das cenas começa em 280 px e a logo da capa em 290 px.
"""
import os, sys, subprocess, asyncio, shutil
sys.path.insert(0, "/home/claude/timtimcash-social/gerador")
import artes as A
from playwright.async_api import async_playwright

FPS = 30
FUNDO_TELA = "#F7F6F1"  # fundo da página do site no celular (medido nas telas reais)
ACESSE = "Acesse pelo navegador, no computador ou no celular."
NOTA = "Tela real do timtimcash, com dados de exemplo"

# ---------------------------------------------------------------- CSS (o do modelo, mais as peças comuns)
def css(extra=""):
    return f"""{A.font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:{A.BG}}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;font-feature-settings:'cv11','ss01';color:{A.INK}}}
.cena{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
.verde{{background:{A.BRAND};color:#fff}}
.tinta{{background:{A.INK};color:#fff}}
.eyebrow{{font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
.h1{{font-size:124px;line-height:.98;font-weight:700;letter-spacing:-.05em;text-wrap:balance}}
.tit{{position:absolute;left:90px;top:280px;width:900px;font-size:64px;line-height:1.06;font-weight:700;letter-spacing:-.045em;text-wrap:balance}}
.tit b{{color:{A.BRAND_DARK};font-weight:700}}
.sobre{{display:block;font-size:30px;line-height:1;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{A.BRAND_DARK};margin-bottom:26px}}
.nota{{position:absolute;left:150px;top:548px;font-size:26px;font-weight:500;color:{A.MUTED};letter-spacing:-.005em}}
.janela{{position:absolute;left:150px;top:600px;width:780px;height:1000px;border-radius:44px;overflow:hidden;background:#fff;
  border:2px solid {A.FIO};box-shadow:0 2px 4px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.28)}}
.tela{{position:absolute;left:0;top:0;width:1170px;transform-origin:0 0;background:{FUNDO_TELA}}}
.tela img{{position:absolute;display:block}}
.anel{{position:absolute;border-radius:28px;border:9px solid {A.BRAND};opacity:0}}
.anel.coral{{border-color:{A.RED}}}
.anel.ambar{{border-color:{A.AMBER_BAR}}}
.toque{{position:absolute;width:132px;height:132px;margin:-66px 0 0 -66px;border-radius:50%;background:rgba(15,20,16,.16);border:6px solid #fff;
  box-shadow:0 6px 18px rgba(15,20,16,.25);opacity:0}}
.onda{{position:absolute;width:132px;height:132px;margin:-66px 0 0 -66px;border-radius:50%;border:6px solid {A.AMBER_BAR};opacity:0}}
.apoio{{font-size:40px;line-height:1.3;font-weight:500;color:{A.MUTED};letter-spacing:-.02em}}
.chip{{display:inline-flex;align-items:center;height:92px;padding:0 40px;border-radius:999px;background:#fff;border:3px solid {A.FIO};
  font-size:38px;font-weight:600;color:{A.INK};letter-spacing:-.01em}}
.pill{{display:inline-flex;align-items:center;gap:16px;background:#fff;color:{A.BRAND_DARK};font-weight:600;font-size:44px;padding:28px 48px;border-radius:999px}}
.num{{font-variant-numeric:tabular-nums}}
{extra}"""

# ---------------------------------------------------------------- JavaScript comum
JS = """
const $ = id => document.getElementById(id);
const clamp = (x,a,b) => Math.min(b, Math.max(a, x));
const ease = x => x<.5 ? 4*x*x*x : 1-Math.pow(-2*x+2,3)/2;
const easeOut = x => 1-Math.pow(1-x,3);
const prog = (t,a,b) => ease(clamp((t-a)/(b-a),0,1));
const pout = (t,a,b) => easeOut(clamp((t-a)/(b-a),0,1));
const lin = (t,a,b) => clamp((t-a)/(b-a),0,1);
const Z = 780/1170;                       // tela em escala 3 dentro da janela de 780 px: 2 px por px CSS
// caixa em px CSS da tela (a imagem tem escala 3) + folga em px da imagem
function caixa(el, r, pad){ const s=3; el.style.left=(r[0]*s-pad)+'px'; el.style.top=(r[1]*s-pad)+'px';
  el.style.width=(r[2]*s+2*pad)+'px'; el.style.height=(r[3]*s+2*pad)+'px'; }
function ponto(el, x, y){ el.style.left=(x*3)+'px'; el.style.top=(y*3)+'px'; }
// título: entra em a, sai em b (0,35 s e 0,3 s), com deslocamento vertical
function titulo(id, t, a, b, dy){ dy = dy===undefined ? 28 : dy; const e=$(id); const vin=prog(t,a,a+.35), vout=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=Math.min(vin, 1-vout); e.style.transform=`translateY(${(1-vin)*dy - vout*dy}px)`; }
// anel de destaque: aparece em a (encolhendo de 106% para 100%), some em b
function anel(id, t, a, b){ const e=$(id); const vi=prog(t,a,a+.35), vo=b ? prog(t,b,b+.3) : 0;
  e.style.opacity=vi*(1-vo); e.style.transform=`scale(${1.06-.06*vi})`; }
// toque (mesmo ritmo do modelo): o dedo chega em a-0,1, aperta em a+0,15, a onda abre de a+0,1 a a+0,7
function toque(tid, oid, t, a){ const T=$(tid), O=$(oid);
  T.style.opacity=(t>=a-.1 && t<a+.8) ? (t<a ? lin(t,a-.1,a) : 1-lin(t,a+.5,a+.8)) : 0;
  T.style.transform=`scale(${t<a+.15 ? 1 : .86})`;
  O.style.opacity=(t>=a+.1 && t<=a+.7) ? (1-lin(t,a+.1,a+.7)) : 0;
  O.style.transform=`scale(${1+1.6*lin(t,a+.1,a+.7)})`; }
// panorâmica: topo visível da tela em px CSS
function pan(id, topo){ $(id).style.transform=`translate(0px, ${-topo*3*Z}px) scale(${Z})`; }
"""

# ---------------------------------------------------------------- peças comuns
def tela(tid, imgs, altura_css, extra=""):
    """Camada de tela (1170 px = 390 px CSS em escala 3). imgs: lista de (id, src, x_css, y_css, largura_px, estilo)."""
    partes = []
    for iid, src, x, y, larg, est in imgs:
        partes.append(f'<img id="{iid}" src="file://{src}" style="left:{x*3}px;top:{y*3}px;width:{larg}px;{est}">')
    return f'<div class="tela" id="{tid}" style="height:{altura_css*3}px">{"".join(partes)}{extra}</div>'

def fim(nome):
    """Fechamento em verde (igual ao modelo): logotipo vertical, nome, 'Acesse...' e a pílula 'Link na bio'."""
    return f"""<div class="cena verde" id="fim" style="transform:translateY(1920px)">
  <div style="position:absolute;left:0;top:470px;width:1080px;display:flex;flex-direction:column;align-items:center;text-align:center">
    {A.logo_vertical("white", 300)}
    <div style="font-size:66px;font-weight:700;letter-spacing:-.045em;line-height:1.06;margin-top:90px;width:860px;text-wrap:balance">{nome}</div>
    <div style="font-size:40px;font-weight:500;letter-spacing:-.02em;line-height:1.3;margin-top:30px;width:820px;text-wrap:balance">{ACESSE}</div>
    <div style="margin-top:70px"><span class="pill">Link na bio {A.ARROW}</span></div>
  </div>
</div>"""

def pagina(corpo, css_extra, js_render):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
{css(css_extra)}
</style></head><body>
{corpo}
<script>{JS}
{js_render}
render(0);
</script></body></html>"""

# ---------------------------------------------------------------- saída
async def _abrir(p, html_path):
    b = await p.chromium.launch()
    pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    await pg.goto("file://" + html_path)
    await pg.evaluate("document.fonts.ready")
    await pg.wait_for_timeout(800)
    return b, pg

async def _previa(html_path, tempos, destino):
    os.makedirs(destino, exist_ok=True)
    async with async_playwright() as p:
        b, pg = await _abrir(p, html_path)
        for t in tempos:
            await pg.evaluate(f"render({t})")
            await pg.screenshot(path=os.path.join(destino, f"q_{t:05.2f}.png"))
        await b.close()

async def _video(html_path, dur, saida, capa, capa_t):
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
        if capa:
            await pg.evaluate(f"render({capa_t})")
            await pg.screenshot(path=capa, type="jpeg", quality=94)
        await b.close()
    ff.stdin.close(); ff.wait()
    return n

def executar(html, dur, pasta, capa_t, trabalho):
    """pasta: $O/saida/<pasta>; trabalho: pasta de trabalho do Reel (HTML e prévias)."""
    os.makedirs(pasta, exist_ok=True); os.makedirs(trabalho, exist_ok=True)
    html_path = os.path.join(trabalho, "reel.html")
    open(html_path, "w", encoding="utf-8").write(html)
    if os.environ.get("REEL_PREVIA"):
        tempos = [float(x) for x in os.environ["REEL_PREVIA"].split()]
        asyncio.run(_previa(html_path, tempos, os.path.join(trabalho, "previa")))
        print("prévias em", os.path.join(trabalho, "previa"))
        return
    saida = os.path.join(pasta, "reel.mp4")
    n = asyncio.run(_video(html_path, dur, saida, os.path.join(pasta, "capa.jpg"), capa_t))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", saida, "-vf", "scale=720:1280", "-c:v", "libx264", "-crf", "28",
                    "-preset", "veryfast", "-an", "-movflags", "+faststart", os.path.join(pasta, "previa.mp4")], check=True)
    print("ok", saida, n, "quadros")
