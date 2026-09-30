# -*- coding: utf-8 -*-
"""Base comum dos Reels 22/10, 30/10 e 16/10 (1080 × 1920, 30 fps).

Parte do Reel aprovado e publicado em 30/09/2026 (base_app/modelo_reel/reel.py):
mesma grade (título em cima, nota, janela de 780 × 1000 com a tela real), mesmos
anéis, toque e onda, mesmo fechamento verde e EXATAMENTE os mesmos parâmetros do
ffmpeg. Cada quadro é desenhado no Chromium (render(t)) e vai direto para o ffmpeg.
Zona segura do Instagram: nada importante nos 270 px de cima (14% da altura), onde o app põe o nome do perfil
e o áudio. Por isso o título das cenas começa em 280 px e a logo da capa em 290 px.
"""
import os, sys, subprocess, asyncio
sys.path.insert(0, "/home/claude/timtimcash-social/gerador")
import artes as A
from playwright.async_api import async_playwright

FPS = 30
NOTA = "Tela real do timtimcash, com dados de exemplo"

CSS = f"""
{A.font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:{A.BG}}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;font-feature-settings:'cv11','ss01';color:{A.INK}}}
.cena{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
.verde{{background:{A.BRAND};color:#fff}}
.suave{{background:{A.SOFT};color:{A.INK}}}
.eyebrow{{font-size:30px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}}
.h1{{font-size:124px;line-height:.98;font-weight:700;letter-spacing:-.05em;text-wrap:balance}}
.tit{{position:absolute;left:90px;top:280px;width:900px;font-size:64px;line-height:1.06;font-weight:700;letter-spacing:-.045em;text-wrap:balance;opacity:0}}
.tit b{{color:{A.BRAND_DARK};font-weight:700}}
.nota{{position:absolute;left:150px;top:548px;font-size:26px;font-weight:500;color:{A.MUTED};letter-spacing:-.005em}}
#janela{{position:absolute;left:150px;top:600px;width:780px;height:1000px;border-radius:44px;overflow:hidden;background:#fff;
  border:2px solid {A.FIO};box-shadow:0 2px 4px rgba(15,20,16,.05),0 30px 60px -30px rgba(15,20,16,.28)}}
#tela{{position:absolute;left:0;top:0;width:1170px;transform-origin:0 0}}
#tela img{{position:absolute;left:0;top:0;width:1170px}}
.anel{{position:absolute;border-radius:28px;border:9px solid {A.BRAND};opacity:0}}
.marca{{position:absolute;border-radius:10px;background:{A.MENTA_CLARA};mix-blend-mode:multiply;clip-path:inset(0 100% 0 0)}}
.toque{{position:absolute;width:132px;height:132px;margin:-66px 0 0 -66px;border-radius:50%;background:rgba(15,20,16,.16);border:6px solid #fff;
  box-shadow:0 6px 18px rgba(15,20,16,.25);opacity:0}}
.onda{{position:absolute;width:132px;height:132px;margin:-66px 0 0 -66px;border-radius:50%;border:6px solid {A.BRAND};opacity:0}}
.apoio{{font-size:40px;line-height:1.3;font-weight:500;color:{A.MUTED};letter-spacing:-.02em;text-wrap:pretty}}
.chip{{display:inline-flex;align-items:center;height:92px;padding:0 40px;border-radius:999px;background:#fff;border:3px solid {A.FIO};
  font-size:38px;font-weight:600;color:{A.INK};letter-spacing:-.01em}}
.pill{{display:inline-flex;align-items:center;gap:16px;background:#fff;color:{A.BRAND_DARK};font-weight:600;font-size:44px;padding:28px 48px;border-radius:999px}}
.num{{font-variant-numeric:tabular-nums}}
"""

def fechamento(nome):
    """Fechamento verde do modelo: logotipo vertical negativo, nome da funcionalidade, chamada e pílula."""
    return f"""<div class="cena verde" id="fim" style="transform:translateY(1920px)">
  <div style="position:absolute;left:0;top:470px;width:1080px;display:flex;flex-direction:column;align-items:center;text-align:center">
    {A.logo_vertical("white", 300)}
    <div style="font-size:66px;font-weight:700;letter-spacing:-.045em;line-height:1.06;margin-top:90px;width:860px;text-wrap:balance">{nome}</div>
    <div style="font-size:40px;font-weight:500;letter-spacing:-.02em;line-height:1.3;margin-top:30px;width:820px;text-wrap:balance">Acesse pelo navegador, no computador ou no celular.</div>
    <div style="margin-top:70px"><span class="pill">Link na bio {A.ARROW}</span></div>
  </div>
</div>"""

JS_BASE = r"""
const $ = id => document.getElementById(id);
const clamp = (x,a,b) => Math.min(b, Math.max(a, x));
const ease = x => x<.5 ? 4*x*x*x : 1-Math.pow(-2*x+2,3)/2;
const prog = (t,a,b) => ease(clamp((t-a)/(b-a),0,1));
const lin = (t,a,b) => clamp((t-a)/(b-a),0,1);
// Caixa em px CSS da tela (a imagem tem escala 3) -> posição dentro de #tela
// pad: número ou [esquerda, cima, direita, baixo], em px da imagem (3 por px CSS)
function caixa(el, r, pad){ const s=3; const p = Array.isArray(pad) ? pad : [pad,pad,pad,pad];
  el.style.left=(r[0]*s-p[0])+'px'; el.style.top=(r[1]*s-p[1])+'px';
  el.style.width=(r[2]*s+p[0]+p[2])+'px'; el.style.height=(r[3]*s+p[1]+p[3])+'px'; }
// Marca-texto sobre linhas de texto da tela (multiplica: o fundo branco vira menta e o texto continua legível)
function marcas(pref, linhas, cor, cont){ const tela=$(cont||'tela');
  linhas.forEach((l,i)=>{ const d=document.createElement('div'); d.id=pref+i; d.className='marca';
    d.style.left=(l[0]*3-6)+'px'; d.style.top=(l[1]*3-2)+'px'; d.style.width=(l[2]*3+12)+'px'; d.style.height=(l[3]*3+4)+'px';
    if(cor) d.style.background=cor; tela.appendChild(d); }); }
function marca(pref, n, t, a, b){ for(let i=0;i<n;i++){ const d=$(pref+i); const p=prog(t, a+i*.12, a+i*.12+.35);
  d.style.clipPath=`inset(0 ${100-100*p}% 0 0)`; d.style.opacity = 1 - prog(t,b,b+.35); } }
function ponto(el, x, y){ el.style.left=(x*3)+'px'; el.style.top=(y*3)+'px'; }
function titulo(id, t, a, b){ // entra em a, sai em b (0,35 s cada), como no modelo
  const e = $(id); const vin = prog(t,a,a+.35), vout = b ? prog(t,b,b+.35) : 0;
  e.style.opacity = Math.min(vin, 1-vout); e.style.transform = `translateY(${(1-vin)*28 - vout*28}px)`; }
// Câmera da janela: topo e esquerda em px CSS da tela; Z = px do vídeo por px CSS (2 = largura inteira)
function camera(topo, esq, Z){ $('tela').style.transform = `translate(${-esq*Z}px, ${-topo*Z}px) scale(${Z/3})`; }
// Anel que aparece em a (0,4 s) e some em b (0,35 s), com o leve encolher do modelo
function anel(id, t, a, b){ const v = prog(t,a,a+.4) * (1 - prog(t,b,b+.35));
  $(id).style.opacity = v; $(id).style.transform = `scale(${1.06 - .06*prog(t,a,a+.4)})`; }
// Toque em t0 (px CSS da tela): círculo aparece, aperta, e a onda abre
function toque(idT, idO, t, t0){
  $(idT).style.opacity = (t>=t0-.1 && t<t0+.8) ? (t<t0 ? lin(t,t0-.1,t0) : 1-lin(t,t0+.5,t0+.8)) : 0;
  $(idT).style.transform = `scale(${t<t0+.15 ? 1 : .86})`;
  $(idO).style.opacity = (t>=t0+.1 && t<=t0+.7) ? (1-lin(t,t0+.1,t0+.7)) : 0;
  $(idO).style.transform = `scale(${1+1.6*lin(t,t0+.1,t0+.7)})`; }
"""

def pagina(corpo, js):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
{corpo}
<script>{JS_BASE}
{js}
render(0);
</script></body></html>"""

async def _abrir(p, html, pasta):
    arq = os.path.join(pasta, "reel.html")
    open(arq, "w", encoding="utf-8").write(html)
    b = await p.chromium.launch()
    pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    await pg.goto("file://" + arq); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(800)
    return b, pg

async def previa(html, pasta, tempos):
    """Quadros soltos em PNG (previa_SS.ss.png) para conferir, sem gerar o vídeo."""
    async with async_playwright() as p:
        b, pg = await _abrir(p, html, pasta)
        for t in tempos:
            await pg.evaluate(f"render({t})")
            await pg.screenshot(path=os.path.join(pasta, f"previa_{t:05.2f}.png"))
        await b.close()

async def gerar(html, saida, dur, capa=None, t_capa=2.5):
    """Mesmos parâmetros do ffmpeg do Reel modelo (base_app/modelo_reel/reel.py)."""
    pasta = os.path.dirname(os.path.abspath(saida))
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000", "-shortest",
        "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-g", str(FPS), "-keyint_min", str(FPS), "-sc_threshold", "0",
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-movflags", "+faststart", "-use_editlist", "0", saida], stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b, pg = await _abrir(p, html, pasta)
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

def executar(html, saida, dur, capa=None, t_capa=2.5):
    pasta = os.path.dirname(os.path.abspath(saida))
    os.makedirs(pasta, exist_ok=True)
    if os.environ.get("REEL_PREVIA"):
        return asyncio.run(previa(html, os.environ.get("REEL_PREVIA_DIR", pasta), [float(x) for x in os.environ["REEL_PREVIA"].split()]))
    asyncio.run(gerar(html, saida, dur, capa, t_capa))
