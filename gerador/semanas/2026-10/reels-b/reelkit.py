# -*- coding: utf-8 -*-
"""Base comum dos dois Reels (08/10 e 20/10), tirada do Reel aprovado (base_app/modelo_reel/reel.py).

O mesmo desenho (fontes, título das cenas, nota, janela da tela real, anéis, toque, fechamento verde)
e o mesmo motor: cada quadro é desenhado no Chromium por render(t) e vai direto para o ffmpeg,
com exatamente os parâmetros do ffmpeg do modelo.
REEL_PREVIA="0.5 4 9" grava quadros soltos em PNG ao lado da saída, sem gerar o vídeo.
Zona segura do Instagram: nada importante nos 270 px de cima (14% da altura), onde o app põe o nome do perfil
e o áudio. Por isso o título das cenas começa em 280 px e a logo da capa em 290 px.
"""
import os, sys, subprocess, asyncio
sys.path.insert(0, "/home/claude/timtimcash-social/gerador")
import artes as A
from playwright.async_api import async_playwright

FPS = 30

CSS = f"""
{A.font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:{A.BG}}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;font-feature-settings:'cv11','ss01';color:{A.INK}}}
.cena{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
.verde{{background:{A.BRAND};color:#fff}}
.eyebrow{{font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
.h1{{font-size:124px;line-height:.98;font-weight:700;letter-spacing:-.05em;text-wrap:balance}}
.tit{{position:absolute;left:90px;top:280px;width:900px;font-size:64px;line-height:1.06;font-weight:700;letter-spacing:-.045em;text-wrap:balance;opacity:0}}
.tit b{{color:{A.BRAND_DARK};font-weight:700}}
.nota{{position:absolute;left:150px;top:548px;font-size:26px;font-weight:500;color:{A.MUTED};letter-spacing:-.005em}}
#janela{{position:absolute;left:150px;top:600px;width:780px;height:1000px;border-radius:44px;overflow:hidden;background:#fff;
  border:2px solid {A.FIO};box-shadow:0 2px 4px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.28)}}
.lay{{position:absolute;left:0;top:0;width:780px;opacity:0;will-change:transform,opacity}}
.lay img{{display:block;width:780px;height:auto}}
.anel{{position:absolute;border-radius:28px;border:9px solid {A.BRAND};opacity:0}}
.toque{{position:absolute;width:132px;height:132px;margin:-66px 0 0 -66px;border-radius:50%;background:rgba(15,20,16,.16);border:6px solid #fff;
  box-shadow:0 6px 18px rgba(15,20,16,.25);opacity:0}}
.onda{{position:absolute;width:132px;height:132px;margin:-66px 0 0 -66px;border-radius:50%;border:6px solid {A.BRAND};opacity:0}}
.apoio{{font-size:40px;line-height:1.3;font-weight:500;color:{A.MUTED};letter-spacing:-.02em}}
.chip{{display:inline-flex;align-items:center;height:92px;padding:0 40px;border-radius:999px;background:#fff;border:3px solid {A.FIO};
  font-size:38px;font-weight:600;color:{A.INK};letter-spacing:-.01em}}
.pill{{display:inline-flex;align-items:center;gap:16px;background:#fff;color:{A.BRAND_DARK};font-weight:600;font-size:44px;padding:28px 48px;border-radius:999px}}
.num{{font-variant-numeric:tabular-nums}}
.recorte{{border-radius:30px;overflow:hidden;background:#fff;border:2px solid {A.FIO};
  box-shadow:0 2px 4px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.30)}}
.recorte img{{display:block;width:100%;height:auto}}
"""

JS_BASE = """
const $ = id => document.getElementById(id);
const clamp = (x,a,b) => Math.min(b, Math.max(a, x));
const ease = x => x<.5 ? 4*x*x*x : 1-Math.pow(-2*x+2,3)/2;
const prog = (t,a,b) => ease(clamp((t-a)/(b-a),0,1));
const lin = (t,a,b) => clamp((t-a)/(b-a),0,1);
const E = 2;   // 1 px CSS do celular = 2 px do Reel (390 px CSS na janela de 780)
function titulo(id, t, a, b){ // entra em a, sai em b (0,35 s cada), como no modelo
  const e = $(id); const vin = prog(t,a,a+.35), vout = b ? prog(t,b,b+.35) : 0;
  e.style.opacity = Math.min(vin, 1-vout); e.style.transform = `translateY(${(1-vin)*28 - vout*28}px)`; }
// uma tela real (camada): opacidade e topo visível (px CSS do celular)
function camada(id, op, topo, dy){ const e=$(id); e.style.opacity=op; e.style.transform=`translateY(${-topo*E + (dy||0)}px)`; }
// anel em volta de uma caixa [x,y,w,h] (px CSS) dentro da camada
function poeAnel(id, r, pad){ const e=$(id); e.style.left=(r[0]*E-pad)+'px'; e.style.top=(r[1]*E-pad)+'px';
  e.style.width=(r[2]*E+2*pad)+'px'; e.style.height=(r[3]*E+2*pad)+'px'; }
function anel(id, t, a, b){ const v = prog(t,a,a+.4)*(1-prog(t,b,b+.3)); const e=$(id);
  e.style.opacity=v; e.style.transform=`scale(${1.06-.06*prog(t,a,a+.4)})`; }
// toque: aparece em t0-.1, aperta em t0+.15, some em t0+.8; a onda abre de t0+.2 a t0+.8
function poeToque(id, x, y){ ['t_','o_'].forEach(p=>{ const e=$(p+id); e.style.left=(x*E)+'px'; e.style.top=(y*E)+'px'; }); }
function toque(id, t, t0){
  const tq=$('t_'+id), on=$('o_'+id);
  tq.style.opacity = (t>=t0-.1 && t<t0+.9) ? (t<t0 ? lin(t,t0-.1,t0) : 1-lin(t,t0+.5,t0+.8)) : 0;
  tq.style.transform = `scale(${t<t0+.15 ? 1 : .86})`;
  on.style.opacity = (t>=t0+.2 && t<=t0+.8) ? (1-lin(t,t0+.2,t0+.8)) : 0;
  on.style.transform = `scale(${1+1.6*lin(t,t0+.2,t0+.8)})`;
}
"""

def html(corpo, js):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
{corpo}
<script>{JS_BASE}
{js}
render(0);
</script></body></html>"""

def fechamento(nome):
    """Cena final verde, igual à do modelo: logotipo vertical negativo, nome da funcionalidade, chamada e Link na bio."""
    return f"""<div class="cena verde" id="fim" style="transform:translateY(1920px)">
  <div style="position:absolute;left:0;top:470px;width:1080px;display:flex;flex-direction:column;align-items:center;text-align:center">
    {A.logo_vertical("white", 300)}
    <div style="font-size:66px;font-weight:700;letter-spacing:-.045em;line-height:1.06;margin-top:90px;width:860px;text-wrap:balance">{nome}</div>
    <div style="font-size:40px;font-weight:500;letter-spacing:-.02em;line-height:1.3;margin-top:30px;width:820px;text-wrap:balance">Acesse pelo navegador, no computador ou no celular.</div>
    <div style="margin-top:70px"><span class="pill">Link na bio {A.ARROW}</span></div>
  </div>
</div>"""

def _cor(c):
    return ' style="border-color:%s"' % c if c else ""

def camada_html(id_, img, aneis=(), toques=(), extra=""):
    """Uma tela real dentro da janela, com os seus anéis e toques (ids) e cores opcionais."""
    a = "".join('<div class="anel" id="%s"%s></div>' % (i, _cor(c)) for i, c in aneis)
    t = "".join('<div class="onda" id="o_%s"%s></div><div class="toque" id="t_%s"></div>' % (i, _cor(c), i) for i, c in toques)
    return '<div class="lay" id="%s"><img src="file://%s">%s%s%s</div>' % (id_, img, a, t, extra)

async def _abrir(p, pagina):
    b = await p.chromium.launch()
    pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    await pg.goto("file://" + pagina); await pg.evaluate("document.fonts.ready")
    await pg.evaluate("Promise.all([...document.images].map(i => i.decode ? i.decode().catch(()=>0) : 0))")
    await pg.wait_for_timeout(800)
    return b, pg

async def _previa(pagina, pasta, tempos):
    async with async_playwright() as p:
        b, pg = await _abrir(p, pagina)
        for t in tempos:
            await pg.evaluate(f"render({t})")
            await pg.screenshot(path=os.path.join(pasta, f"previa_{t:05.2f}.png"))
        await b.close()

async def _video(pagina, saida, dur, capa, t_capa):
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000", "-shortest",
        "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-g", str(FPS), "-keyint_min", str(FPS), "-sc_threshold", "0",
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-movflags", "+faststart", "-use_editlist", "0", saida], stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b, pg = await _abrir(p, pagina)
        n = int(round(dur * FPS))
        for i in range(n):
            await pg.evaluate(f"render({i / FPS:.5f})")
            ff.stdin.write(await pg.screenshot(type="jpeg", quality=96))
        if capa:
            await pg.evaluate(f"render({t_capa})")
            await pg.screenshot(path=capa, type="jpeg", quality=94)
        await b.close()
    ff.stdin.close(); ff.wait()
    print("ok", saida, n, "quadros")

def rodar(pagina_html, saida, dur, capa=None, t_capa=2.2):
    """Grava a página ao lado da saída e gera o vídeo (ou só as prévias, com REEL_PREVIA)."""
    pasta = os.path.dirname(os.path.abspath(saida))
    os.makedirs(pasta, exist_ok=True)
    pagina = os.path.join(pasta, "reel.html")
    open(pagina, "w", encoding="utf-8").write(pagina_html)
    if os.environ.get("REEL_PREVIA"):
        return asyncio.run(_previa(pagina, pasta, [float(x) for x in os.environ["REEL_PREVIA"].split()]))
    asyncio.run(_video(pagina, os.path.abspath(saida), dur, capa and os.path.abspath(capa), t_capa))
