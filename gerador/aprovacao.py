# -*- coding: utf-8 -*-
"""Monta o arquivo HTML de aprovação dos posts (um arquivo só, com imagens e fonte embutidas).

    python3 gerador/aprovacao.py <dados.py> <pasta_das_imagens> <saida.html>

- dados.py define CONFIG, POSTS e FUSO. Modelo: gerador/avulsos/2026-09-30_comece-por-aqui_dados.py
  (CONFIG: titulo_pagina, eyebrow, h1, sub, chave, resumo_titulo, notas, fontes; cada post: n, pasta,
  plataforma, formato, formato_curto, tema, pilar, data_longa, data_curta, data_mockup, hora, slides,
  legenda, justificativa e, opcionais, grade, grade_titulo, grade_legenda e grade_nota para a prévia
  da grade do perfil: grade é uma lista de (rótulo, caminho da capa), com caminho None para este post
  e rótulo "fixado" para o post fixado no topo; caminhos relativos partem da raiz do repositório).
- pasta_das_imagens: onde o render gravou as artes (TT_SAIDA), com <pasta>/01.jpg, 02.jpg...
- O arquivo funciona aberto no navegador, sem internet. A avaliação fica salva no navegador
  (chave CONFIG["chave"], que deve mudar a cada proposta) e o botão "Copiar todas as avaliações"
  gera o resumo para colar na conversa.
"""
import base64, glob, io, json, os, re, sys, importlib.util
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import artes
from render import garante_fonte

if len(sys.argv) != 4:
    sys.exit(__doc__)
_spec = importlib.util.spec_from_file_location("dados_aprovacao", sys.argv[1])
_mod = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_mod)
POSTS, FUSO, CONFIG = _mod.POSTS, _mod.FUSO, _mod.CONFIG
IMAGENS = os.path.abspath(sys.argv[2])
SAIDA = os.path.abspath(sys.argv[3])
garante_fonte()

def img_b64(caminho, qualidade=84):
    im = Image.open(caminho).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=qualidade, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

imagens = {}
for p in POSTS:
    fs = sorted(glob.glob(os.path.join(IMAGENS, p["pasta"], "*.jpg")))
    assert len(fs) == len(p["slides"]), (p["pasta"], len(fs), len(p["slides"]))
    imagens[str(p["n"])] = [img_b64(f) for f in fs]

def img_b64_menor(caminho, largura=360, qualidade=82):
    im = Image.open(caminho).convert("RGB")
    im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=qualidade, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def _caminho(c):
    return c if os.path.isabs(c) else os.path.join(REPO, c)

# grade do perfil (opcional, por post): lista de (rótulo, caminho da capa). Caminho None = este post
# (capa tirada da pasta das imagens). Rótulo "fixado" = post fixado no topo, com o alfinete.
grades = {}
for p in POSTS:
    if p.get("grade"):
        capa = sorted(glob.glob(os.path.join(IMAGENS, p["pasta"], "*.jpg")))[0]
        grades[str(p["n"])] = {
            "titulo": p.get("grade_titulo", "Prévia no perfil"),
            "legenda": p.get("grade_legenda", "Como o perfil fica depois deste post"),
            "nota": p.get("grade_nota", ""),
            "itens": [{"rot": r, "src": img_b64_menor(capa if c is None else _caminho(c)),
                       "este": c is None, "fixado": r.strip().lower() == "fixado"} for r, c in p["grade"]],
        }

logo_h = artes.logo_horizontal("color", 30)
simbolo_neg = artes.logo("white", 20)

def fontes():
    out = []
    for w, f in [(400, "Regular"), (500, "Medium"), (600, "SemiBold"), (700, "Bold")]:
        b = base64.b64encode(open(f"/tmp/inter/web/Inter-{f}.woff2", "rb").read()).decode()
        out.append(f"@font-face{{font-family:'Inter';font-style:normal;font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{b}) format('woff2')}}")
    return "\n".join(out)

dados_js = [{
    "n": p["n"], "plataforma": p["plataforma"], "formato": p["formato"], "formato_curto": p["formato_curto"],
    "tema": p["tema"], "pilar": p["pilar"], "data_longa": p["data_longa"], "data_curta": p["data_curta"],
    "data_mockup": p["data_mockup"], "hora": p["hora"], "slides": p["slides"], "legenda": p["legenda"],
    "justificativa": p["justificativa"],
} for p in POSTS]
import html as _html
notas_html = "".join(f'<div class="note"><strong>{_html.escape(t)}</strong>{_html.escape(x)}</div>' for t, x in CONFIG["notas"])
fontes_html = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{_html.escape(t)}</a></li>' for t, u in CONFIG["fontes"])
pulos_html = "".join(f'<a href="#post-{p["n"]}">Post {p["n"]}</a>' for p in POSTS)

HTML = r"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>__TITULO__</title>
<style>
__FONTES__
:root{
  --brand:#059669;--brand-dark:#047857;--brand-deep:#065F46;--soft:#D1FAE5;
  --paper:#FBFAF6;--card:#FFFFFF;--ink:#0F1410;--muted:#4D524A;--line:#ECE9E0;--neutral:#D4D2C8;
  --amber:#8A6320;--amber-bg:#FBF1DC;--red:#B83C3C;--red-bg:#F8E1E1;--pend:#5F6A64;--pend-bg:#F0EEE7;
  --r-sm:12px;--r-md:20px;--shadow:0 1px 2px rgba(15,20,16,.04),0 12px 32px -14px rgba(15,20,16,.14);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",sans-serif;font-feature-settings:"cv11","ss01";line-height:1.5;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}
header.top{padding-top:28px;padding-bottom:8px}
.brandline{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.eyebrow{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--brand-dark)}
h1{font-size:clamp(28px,4.6vw,44px);line-height:1.04;letter-spacing:-.045em;font-weight:700;margin:14px 0 10px}
.sub{color:var(--muted);font-size:16px;max-width:760px;margin:0}
.bar{position:sticky;top:0;z-index:20;background:rgba(251,250,246,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line);margin-top:18px}
.bar .wrap{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-top:10px;padding-bottom:10px}
.count{display:inline-flex;align-items:center;gap:8px;height:32px;padding:0 12px;border-radius:999px;font-size:13px;font-weight:600;background:var(--card);border:1px solid var(--line)}
.count b{font-variant-numeric:tabular-nums}
.dot{width:8px;height:8px;border-radius:50%}
.bar .jump{margin-left:auto;display:flex;gap:6px}
.bar .jump a{font-size:13px;font-weight:600;color:var(--brand-dark);text-decoration:none;padding:6px 10px;border-radius:999px;border:1px solid var(--line);background:var(--card)}
.notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin:22px 0 6px}
.note{background:var(--card);border:1px solid var(--line);border-radius:var(--r-md);padding:16px 18px;font-size:14px;color:var(--muted)}
.note strong{display:block;color:var(--ink);font-size:14px;margin-bottom:4px}
section.post{background:var(--card);border:1px solid var(--line);border-radius:24px;box-shadow:var(--shadow);margin:26px 0;padding:26px;scroll-margin-top:70px}
.post-head{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:18px;margin-bottom:22px}
.post-head h2{font-size:clamp(22px,3vw,30px);line-height:1.1;letter-spacing:-.04em;font-weight:700;margin:6px 0 8px}
.meta{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;align-items:center;gap:6px;min-height:30px;padding:4px 12px;border-radius:999px;background:var(--paper);border:1px solid var(--line);font-size:13px;font-weight:600;color:var(--ink)}
.chip.g{background:var(--soft);border-color:var(--soft);color:var(--brand-deep)}
.status{display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 16px;border-radius:999px;font-size:14px;font-weight:700;white-space:nowrap}
.status .dot{width:10px;height:10px}
.st-pendente{background:var(--pend-bg);color:var(--pend)} .st-pendente .dot{background:var(--pend)}
.st-aprovado{background:var(--soft);color:var(--brand-deep)} .st-aprovado .dot{background:var(--brand)}
.st-reprovado{background:var(--red-bg);color:var(--red)} .st-reprovado .dot{background:#C94C4C}
.st-alteracao{background:var(--amber-bg);color:var(--amber)} .st-alteracao .dot{background:#D4A14A}
.grid{display:grid;grid-template-columns:minmax(300px,420px) 1fr;gap:30px;align-items:start}
/* mockup */
.phone{position:sticky;top:78px;background:#fff;border:1px solid var(--line);border-radius:28px;overflow:hidden;box-shadow:var(--shadow)}
.ig-top{display:flex;align-items:center;gap:10px;padding:12px 14px}
.avatar{width:34px;height:34px;border-radius:50%;background:var(--brand);display:flex;align-items:center;justify-content:center;flex:none}
.avatar svg{width:22px;height:auto}
.ig-user{font-size:14px;font-weight:600;line-height:1.2}
.ig-user small{display:block;font-weight:400;color:var(--muted);font-size:12px}
.ig-more{margin-left:auto;color:var(--ink);font-weight:700;letter-spacing:1px}
.car{position:relative;background:#F2F1EC}
.track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.track::-webkit-scrollbar{display:none}
.track img{flex:0 0 100%;width:100%;aspect-ratio:4/5;object-fit:cover;scroll-snap-align:center;display:block;cursor:zoom-in;background:#F2F1EC}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:34px;height:34px;border-radius:50%;border:none;background:rgba(255,255,255,.92);box-shadow:0 2px 8px rgba(0,0,0,.18);display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--ink)}
.nav[disabled]{display:none}
.nav.prev{left:10px}.nav.next{right:10px}
.idx{position:absolute;top:12px;right:12px;background:rgba(15,20,16,.72);color:#fff;font-size:12px;font-weight:600;padding:4px 9px;border-radius:999px;font-variant-numeric:tabular-nums}
.ig-actions{display:flex;align-items:center;gap:14px;padding:10px 14px 4px}
.ig-actions svg{width:24px;height:24px}
.dots{display:flex;gap:4px;justify-content:center;flex:1}
.dots i{width:6px;height:6px;border-radius:50%;background:#C9C7BE}
.dots i.on{background:var(--brand)}
.ig-cap{padding:6px 14px 14px;font-size:14px;line-height:1.45;white-space:pre-line}
.ig-cap b{font-weight:600}
.ig-cap .mais{color:var(--muted);cursor:pointer;background:none;border:none;padding:0;font:inherit}
.ig-date{padding:0 14px 16px;font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
/* detalhes */
.block{margin-bottom:22px}
.block h3{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--brand-dark);margin:0 0 10px}
.facts{display:grid;grid-template-columns:auto 1fr;gap:6px 16px;font-size:15px;margin:0}
.facts dt{color:var(--muted);font-weight:500}
.facts dd{margin:0;font-weight:600}
.thumbs{display:grid;grid-template-columns:repeat(auto-fill,minmax(88px,1fr));gap:8px;margin-bottom:12px}
.thumbs button{padding:0;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#F2F1EC;cursor:zoom-in;position:relative}
.thumbs img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}
.thumbs span{position:absolute;left:6px;bottom:6px;background:rgba(15,20,16,.72);color:#fff;font-size:11px;font-weight:600;padding:2px 7px;border-radius:999px}
ol.slides{margin:0;padding-left:22px;font-size:14px;color:var(--ink)}
ol.slides li{margin:0 0 8px}
ol.slides li::marker{color:var(--brand-dark);font-weight:700}
.caption{white-space:pre-line;background:var(--paper);border:1px solid var(--line);border-radius:var(--r-sm);padding:14px 16px;font-size:14px;line-height:1.55}
.just{display:grid;gap:10px}
.just div{background:var(--paper);border:1px solid var(--line);border-radius:var(--r-sm);padding:12px 14px;font-size:14px}
.just b{display:block;font-size:13px;color:var(--brand-deep);margin-bottom:2px}
/* grade do perfil */
.perfil{max-width:380px;background:#fff;border:1px solid var(--line);border-radius:22px;overflow:hidden;box-shadow:var(--shadow)}
.perfil-top{display:flex;align-items:center;gap:10px;padding:14px 14px 10px}
.perfil-top .avatar{width:44px;height:44px}
.perfil-top .avatar svg{width:28px}
.perfil-tabs{display:flex;border-top:1px solid var(--line)}
.perfil-tabs span{flex:1;display:flex;justify-content:center;padding:9px 0;color:var(--muted)}
.perfil-tabs span.on{color:var(--ink);box-shadow:inset 0 -2px 0 var(--ink)}
.perfil-tabs svg{width:20px;height:20px}
.grade{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#fff}
.grade figure{margin:0;position:relative;aspect-ratio:3/4;overflow:hidden;background:#F2F1EC}
.grade img{width:100%;height:100%;object-fit:cover;display:block}
.grade .pin{position:absolute;top:6px;right:6px;width:18px;height:18px;filter:drop-shadow(0 1px 2px rgba(0,0,0,.45))}
.grade figcaption{position:absolute;left:5px;bottom:5px;background:rgba(15,20,16,.72);color:#fff;font-size:10px;font-weight:600;padding:1px 6px;border-radius:999px}
.grade figure.fix{outline:2px solid var(--brand);outline-offset:-2px}
.fontes{margin-top:22px;padding-top:16px;border-top:1px solid var(--line)}
.fontes ul{margin:8px 0 0;padding-left:18px;font-size:13px;color:var(--muted)}
.fontes li{margin:0 0 6px}
.fontes a{color:var(--brand-dark);text-underline-offset:3px}
/* avaliação */
.eval{border:2px solid var(--line);border-radius:var(--r-md);padding:18px;background:#fff;transition:border-color .2s}
.eval.s-aprovado{border-color:var(--brand)} .eval.s-reprovado{border-color:#C94C4C} .eval.s-alteracao{border-color:#D4A14A}
.eval-head{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.eval-head strong{font-size:15px}
.opts{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.opt{position:relative}
.opt input{position:absolute;opacity:0;pointer-events:none}
.opt label{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:8px 10px;border-radius:999px;border:1.5px solid var(--neutral);font-size:14px;font-weight:600;cursor:pointer;text-align:center;background:#fff;color:var(--ink);user-select:none}
.opt input:focus-visible + label{outline:3px solid var(--brand);outline-offset:2px}
.opt input:checked + label.a{background:var(--brand);border-color:var(--brand);color:#fff}
.opt input:checked + label.r{background:#C94C4C;border-color:#C94C4C;color:#fff}
.opt input:checked + label.c{background:#D4A14A;border-color:#D4A14A;color:#1f1604}
.opt label svg{width:18px;height:18px;flex:none}
.cm{margin-top:14px}
.cm label{display:block;font-size:13px;font-weight:600;color:var(--muted);margin-bottom:6px}
textarea{width:100%;min-height:96px;resize:vertical;border:1.5px solid var(--neutral);border-radius:var(--r-sm);padding:12px 14px;font:inherit;font-size:15px;color:var(--ink);background:var(--paper)}
textarea:focus{outline:none;border-color:var(--brand);background:#fff}
.eval.s-alteracao textarea{border-color:#D4A14A;background:#fff}
.eval-foot{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:10px;font-size:12px;color:var(--muted)}
.linkbtn{background:none;border:none;padding:0;font:inherit;font-size:13px;font-weight:600;color:var(--brand-dark);cursor:pointer;text-decoration:underline;text-underline-offset:3px}
.linkbtn[hidden]{display:none}
.warn{display:none;margin-top:8px;font-size:13px;color:var(--amber);font-weight:600}
.eval.s-alteracao.vazio .warn{display:block}
/* final */
.final{background:var(--card);border:1px solid var(--line);border-radius:24px;box-shadow:var(--shadow);padding:26px;margin:30px 0 60px}
.final h2{font-size:26px;letter-spacing:-.04em;margin:6px 0 8px;line-height:1.1}
.primary{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:0 26px;border-radius:999px;border:none;background:var(--brand);color:#fff;font:inherit;font-size:16px;font-weight:600;cursor:pointer}
.primary:hover{background:var(--brand-dark)}
.primary svg{width:20px;height:20px}
.copied{margin-left:12px;font-size:14px;font-weight:600;color:var(--brand-deep)}
#resumo{margin-top:16px;width:100%;min-height:240px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;background:var(--paper)}
.muted{color:var(--muted);font-size:14px}
/* lightbox */
.lb{position:fixed;inset:0;background:rgba(15,20,16,.92);display:none;align-items:center;justify-content:center;z-index:50;padding:20px}
.lb.on{display:flex}
.lb img{max-width:min(92vw,720px);max-height:88vh;border-radius:12px;box-shadow:0 20px 60px rgba(0,0,0,.4)}
.lb button{position:absolute;border:none;background:rgba(255,255,255,.95);width:44px;height:44px;border-radius:50%;cursor:pointer;font-size:20px;display:flex;align-items:center;justify-content:center;color:var(--ink)}
.lb .x{top:16px;right:16px}.lb .p{left:16px;top:50%;transform:translateY(-50%)}.lb .n{right:16px;top:50%;transform:translateY(-50%)}
.lb .c{position:absolute;bottom:18px;left:50%;transform:translateX(-50%);color:#fff;font-size:14px;font-weight:600}
@media (max-width:900px){
  .grid{grid-template-columns:1fr}
  .phone{position:relative;top:0;max-width:440px;margin:0 auto}
  .notes{grid-template-columns:1fr}
}
@media (max-width:520px){
  .wrap{padding:0 16px}
  section.post{padding:18px 16px;border-radius:20px}
  .opts{grid-template-columns:1fr}
  .bar .wrap{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .bar .wrap::-webkit-scrollbar{display:none}
  .count,.bar .jump,.bar .jump a{flex:none}
  .bar .jump{margin-left:4px}
  .final{padding:20px 16px}
  .primary{width:100%}
  .copied{display:block;margin:10px 0 0}
  .facts{grid-template-columns:1fr;gap:0 0}
  .facts dt{margin-top:8px}
}
</style>
</head>
<body>
<header class="top wrap">
  <div class="brandline">__LOGO__<span class="eyebrow">__EYEBROW__</span></div>
  <h1>__H1__</h1>
  <p class="sub">__SUB__</p>
</header>
<div class="bar"><div class="wrap">
  <span class="count"><span class="dot" style="background:var(--pend)"></span>Pendentes <b id="c-pendente">__NPOSTS__</b></span>
  <span class="count"><span class="dot" style="background:var(--brand)"></span>Aprovados <b id="c-aprovado">0</b></span>
  <span class="count"><span class="dot" style="background:#D4A14A"></span>Alteração <b id="c-alteracao">0</b></span>
  <span class="count"><span class="dot" style="background:#C94C4C"></span>Reprovados <b id="c-reprovado">0</b></span>
  <nav class="jump" aria-label="Ir para">__PULOS__<a href="#final">Copiar</a></nav>
</div></div>
<main class="wrap">
  <div class="notes">__NOTAS__</div>
  <div id="posts"></div>
  <section class="final" id="final">
    <span class="eyebrow">Resumo</span>
    <h2>Copiar todas as avaliações</h2>
    <p class="muted">O resumo traz identificação, data, horário, decisão e comentários, mesmo se o post ainda estiver pendente.</p>
    <button class="primary" id="copiar" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="11" height="11" rx="2.5"/><path d="M5 15V6.5A1.5 1.5 0 0 1 6.5 5H15"/></svg>Copiar todas as avaliações</button><span class="copied" id="copiado" role="status" aria-live="polite"></span>
    <label class="muted" for="resumo" style="display:block;margin-top:18px">Prévia do texto copiado (se a cópia automática falhar, selecione e copie daqui):</label>
    <textarea id="resumo" readonly></textarea>
    <div class="fontes"><span class="eyebrow">Fontes</span><ul>__FONTES_LISTA__</ul></div>
  </section>
</main>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Imagem em tamanho maior">
  <button class="x" type="button" aria-label="Fechar">✕</button><button class="p" type="button" aria-label="Anterior">‹</button>
  <img alt=""><button class="n" type="button" aria-label="Próxima">›</button><div class="c"></div>
</div>
<script>
const POSTS = __DADOS__;
const IMGS = __IMGS__;
const SIMBOLO = __SIMBOLO__;
const FUSO = __FUSO__;
const GRADE = __GRADE__;
const RESUMO_TITULO = __RESUMO_TITULO__;
function blocoGrade(k){
  const pin = '<svg class="pin" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M15.5 2.5 21.5 8.5 19.4 9.2 15.9 12.7 16.5 17.6 14.9 19.2 11 15.3 5.3 21 3 21 3 18.7 8.7 13 4.8 9.1 6.4 7.5 11.3 8.1 14.8 4.6z"/></svg>';
  const G = GRADE[k];
  const alt = t => t.este ? ("Este post" + (t.fixado ? ", fixado no topo" : "")) : (t.fixado ? "Post fixado no topo" : "Post de " + esc(t.rot));
  const tiles = G.itens.map(t=>`<figure class="${t.este?'fix':''}"><img src="${t.src}" alt="${alt(t)}">${t.fixado?pin:''}<figcaption>${t.fixado?'fixado':esc(t.rot)}</figcaption></figure>`).join("");
  return `<div class="block"><h3>${esc(G.titulo)}</h3>
    <div class="perfil" aria-label="Prévia da grade do perfil">
      <div class="perfil-top"><span class="avatar">${SIMBOLO}</span><span class="ig-user">timtimcashcom<small>${esc(G.legenda)}</small></span></div>
      <div class="perfil-tabs"><span class="on"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3.5" y="3.5" width="17" height="17" rx="2"/><path d="M9.2 3.5v17M14.8 3.5v17M3.5 9.2h17M3.5 14.8h17"/></svg></span><span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4"/><path d="M3.5 8.5h17M8 3.5l3 5M13.5 3.5l3 5"/><path d="m10.5 12 4 2.2-4 2.2z"/></svg></span><span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="3"/><circle cx="12" cy="10.5" r="2.6"/><path d="M7.2 18.2c1-2.2 2.7-3.3 4.8-3.3s3.8 1.1 4.8 3.3"/></svg></span></div>
      <div class="grade">${tiles}</div>
    </div>
    <p class="muted" style="margin:10px 0 0">A grade do perfil mostra as capas em 3:4, com um corte leve nas laterais.${G.nota ? " " + esc(G.nota) : ""}</p>
  </div>`;
}
const CHAVE = __CHAVE__;
const ROTULO = {pendente:"Pendente de avaliação", aprovado:"Aprovado", reprovado:"Reprovado", alteracao:"Solicitar alteração"};
const ICON = {
  a:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
  r:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
  c:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/></svg>'
};
const IG = {
  heart:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
  com:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M20 12a8 8 0 1 1-3.3-6.5A8 8 0 0 1 20 12z"/><path d="M20 12a8 8 0 0 1-1.2 4.2L20 20l-3.8-1.2"/></svg>',
  send:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M21 3 3 10.5l7 2.5 2.5 7z"/><path d="M10 13 21 3"/></svg>',
  save:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M6 3.5h12v17l-6-4.5-6 4.5z"/></svg>'
};
function esc(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}

let estado = {};
function carregar(){
  try{ const t = localStorage.getItem(CHAVE); if(t){ estado = JSON.parse(t) || {}; } }catch(e){ estado = {}; }
  POSTS.forEach(p=>{ const k=String(p.n); if(!estado[k]) estado[k]={status:"pendente", comentario:""}; if(!ROTULO[estado[k].status]) estado[k].status="pendente"; });
}
function salvar(){ try{ localStorage.setItem(CHAVE, JSON.stringify(estado)); }catch(e){} }

function montar(){
  const alvo = document.getElementById("posts");
  alvo.innerHTML = POSTS.map(p=>{
    const k=String(p.n), imgs=IMGS[k];
    const capCurta = p.legenda.split("\n")[0];
    return `
<section class="post" id="post-${k}" aria-labelledby="t-${k}">
  <div class="post-head">
    <div>
      <span class="eyebrow">Post ${k} · ${esc(p.plataforma)} · ${esc(p.formato_curto)}</span>
      <h2 id="t-${k}">${esc(p.tema)}</h2>
      <div class="meta"><span class="chip g">${esc(p.data_longa)}</span><span class="chip g">${esc(p.hora)}</span><span class="chip">${esc(p.pilar)}</span></div>
    </div>
    <span class="status st-pendente" id="st-${k}" aria-live="polite"><span class="dot"></span><span class="txt">Pendente de avaliação</span></span>
  </div>
  <div class="grid">
    <div>
      <div class="phone" aria-label="Prévia no Instagram">
        <div class="ig-top"><span class="avatar">${SIMBOLO}</span><span class="ig-user">timtimcashcom<small>Prévia do feed</small></span><span class="ig-more">···</span></div>
        <div class="car">
          <div class="track" id="tr-${k}" tabindex="0" aria-label="Slides do carrossel">
            ${imgs.map((src,i)=>`<img src="${src}" alt="Post ${k}, slide ${i+1} de ${imgs.length}" data-k="${k}" data-i="${i}" ${i>1?'loading="lazy"':''}>`).join("")}
          </div>
          <button class="nav prev" type="button" data-k="${k}" data-d="-1" aria-label="Slide anterior"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m15 6-6 6 6 6"/></svg></button>
          <button class="nav next" type="button" data-k="${k}" data-d="1" aria-label="Próximo slide"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m9 6 6 6-6 6"/></svg></button>
          <span class="idx" id="ix-${k}">1/${imgs.length}</span>
        </div>
        <div class="ig-actions">${IG.heart}${IG.com}${IG.send}<div class="dots" id="dt-${k}">${imgs.map((_,i)=>`<i class="${i===0?'on':''}"></i>`).join("")}</div>${IG.save}</div>
        <div class="ig-cap" id="cap-${k}"><b>timtimcashcom</b> <span class="t">${esc(capCurta)}</span> <button class="mais" type="button" data-k="${k}">… mais</button></div>
        <div class="ig-date">${esc(p.data_mockup)}</div>
      </div>
    </div>
    <div>
      <div class="block"><h3>Identificação, data e horário</h3>
        <dl class="facts">
          <dt>Post</dt><dd>Post ${k}</dd>
          <dt>Plataforma</dt><dd>${esc(p.plataforma)} · @timtimcashcom</dd>
          <dt>Formato</dt><dd>${esc(p.formato)}</dd>
          <dt>Data</dt><dd>${esc(p.data_longa)}</dd>
          <dt>Horário</dt><dd>${esc(p.hora)} · ${esc(FUSO)}</dd>
        </dl>
      </div>
      ${GRADE[k] ? blocoGrade(k) : ""}
      <div class="block"><h3>Arte · todos os slides</h3>
        <div class="thumbs">${imgs.map((src,i)=>`<button type="button" data-k="${k}" data-i="${i}" aria-label="Ampliar slide ${i+1}"><img src="${src}" alt=""><span>${i+1}</span></button>`).join("")}</div>
        <ol class="slides">${p.slides.map(s=>`<li>${esc(s)}</li>`).join("")}</ol>
      </div>
      <div class="block"><h3>Legenda completa</h3><div class="caption">${esc(p.legenda)}</div></div>
      <div class="block"><h3>Justificativa</h3><div class="just">${p.justificativa.map(([t,x])=>`<div><b>${esc(t)}</b>${esc(x)}</div>`).join("")}</div></div>
      <div class="eval" id="ev-${k}">
        <div class="eval-head"><strong>Sua avaliação do Post ${k}</strong><span class="status st-pendente" id="st2-${k}"><span class="dot"></span><span class="txt">Pendente de avaliação</span></span></div>
        <div class="opts" role="radiogroup" aria-label="Decisão do Post ${k}">
          <div class="opt"><input type="radio" name="d-${k}" id="d-${k}-a" value="aprovado"><label class="a" for="d-${k}-a">${ICON.a}Aprovado</label></div>
          <div class="opt"><input type="radio" name="d-${k}" id="d-${k}-r" value="reprovado"><label class="r" for="d-${k}-r">${ICON.r}Reprovado</label></div>
          <div class="opt"><input type="radio" name="d-${k}" id="d-${k}-c" value="alteracao"><label class="c" for="d-${k}-c">${ICON.c}Solicitar alteração</label></div>
        </div>
        <div class="cm"><label for="cm-${k}" id="cml-${k}">Comentários (opcional)</label>
          <textarea id="cm-${k}" data-k="${k}" placeholder="Escreva aqui o que quiser comentar sobre este post."></textarea>
          <div class="warn">Descreva a alteração que você quer, para eu saber o que ajustar.</div>
        </div>
        <div class="eval-foot"><span>Salvo automaticamente neste navegador.</span><button class="linkbtn" type="button" id="lp-${k}" data-k="${k}" hidden>Voltar para pendente</button></div>
      </div>
    </div>
  </div>
</section>`;}).join("");
}

function pintar(k){
  const s = estado[k].status, c = estado[k].comentario || "";
  ["st-","st2-"].forEach(pre=>{ const el=document.getElementById(pre+k); el.className="status st-"+s; el.querySelector(".txt").textContent=ROTULO[s]; });
  const ev = document.getElementById("ev-"+k);
  ev.className = "eval" + (s!=="pendente" ? " s-"+s : "") + (s==="alteracao" && !c.trim() ? " vazio" : "");
  document.querySelectorAll(`input[name="d-${k}"]`).forEach(r=>{ r.checked = (r.value===s); });
  const ta = document.getElementById("cm-"+k);
  if(ta.value !== c) ta.value = c;
  document.getElementById("cml-"+k).textContent = s==="alteracao" ? "Sugestões de alteração" : "Comentários (opcional)";
  ta.placeholder = s==="alteracao" ? "Diga o que mudar: texto, arte, data, horário..." : "Escreva aqui o que quiser comentar sobre este post.";
  document.getElementById("lp-"+k).hidden = (s==="pendente");
}
function contar(){
  const n={pendente:0,aprovado:0,reprovado:0,alteracao:0};
  POSTS.forEach(p=>n[estado[String(p.n)].status]++);
  Object.keys(n).forEach(s=>document.getElementById("c-"+s).textContent=n[s]);
  document.getElementById("resumo").value = resumo();
}
function resumo(){
  const n={pendente:0,aprovado:0,reprovado:0,alteracao:0};
  const partes = POSTS.map(p=>{
    const k=String(p.n), e=estado[k]; n[e.status]++;
    const com = (e.comentario||"").trim();
    return [
      `Post ${k} · ${p.plataforma} · ${p.formato_curto}`,
      `Tema: ${p.tema}`,
      `Data: ${p.data_curta}`,
      `Horário: ${p.hora} (horário de Brasília)`,
      `Decisão: ${ROTULO[e.status]}`,
      `Comentários: ${com ? com.replace(/\n+/g," / ") : "sem comentários"}`
    ].join("\n");
  });
  const total = `Total: ${n.aprovado} aprovado(s) · ${n.alteracao} com alteração · ${n.reprovado} reprovado(s) · ${n.pendente} pendente(s)`;
  return [RESUMO_TITULO, "", partes.join("\n\n"), "", total].join("\n");
}
function atualizar(k){ salvar(); pintar(k); contar(); }

function ligar(){
  document.addEventListener("change", ev=>{
    const t=ev.target; if(t.type==="radio" && t.name.startsWith("d-")){ const k=t.name.slice(2); estado[k].status=t.value; atualizar(k); }
  });
  document.addEventListener("input", ev=>{
    const t=ev.target; if(t.tagName==="TEXTAREA" && t.dataset.k){ estado[t.dataset.k].comentario=t.value; salvar(); pintarLeve(t.dataset.k); contar(); }
  });
  document.addEventListener("click", ev=>{
    const b=ev.target.closest("button") || ev.target.closest("img");
    if(!b) return;
    if(b.classList.contains("linkbtn") && b.dataset.k){ estado[b.dataset.k].status="pendente"; atualizar(b.dataset.k); return; }
    if(b.classList.contains("nav") && b.dataset.k){ mover(b.dataset.k, +b.dataset.d); return; }
    if(b.classList.contains("mais")){ const p=POSTS.find(x=>String(x.n)===b.dataset.k); const cap=document.getElementById("cap-"+b.dataset.k); cap.querySelector(".t").textContent=p.legenda; b.remove(); return; }
    if(b.dataset && b.dataset.k && b.dataset.i!==undefined && !b.classList.contains("nav")){ abrirLB(b.dataset.k, +b.dataset.i); return; }
  });
  POSTS.forEach(p=>{
    const k=String(p.n), tr=document.getElementById("tr-"+k);
    let t=null; tr.addEventListener("scroll", ()=>{ clearTimeout(t); t=setTimeout(()=>marcar(k),60); }, {passive:true});
    tr.addEventListener("keydown", e=>{ if(e.key==="ArrowRight"){mover(k,1);e.preventDefault();} if(e.key==="ArrowLeft"){mover(k,-1);e.preventDefault();} });
    marcar(k);
  });
  document.getElementById("copiar").addEventListener("click", copiar);
  const lb=document.getElementById("lb");
  lb.addEventListener("click", e=>{ if(e.target===lb || e.target.classList.contains("x")) fecharLB(); if(e.target.classList.contains("p")) passoLB(-1); if(e.target.classList.contains("n")) passoLB(1); });
  document.addEventListener("keydown", e=>{ if(!lb.classList.contains("on")) return; if(e.key==="Escape") fecharLB(); if(e.key==="ArrowRight") passoLB(1); if(e.key==="ArrowLeft") passoLB(-1); });
}
function pintarLeve(k){ const s=estado[k].status, c=estado[k].comentario||""; const ev=document.getElementById("ev-"+k); ev.classList.toggle("vazio", s==="alteracao" && !c.trim()); }
function atual(k){ const tr=document.getElementById("tr-"+k); return Math.round(tr.scrollLeft / Math.max(1,tr.clientWidth)); }
function mover(k,d){ const tr=document.getElementById("tr-"+k); const n=IMGS[k].length; const i=Math.min(n-1,Math.max(0,atual(k)+d)); tr.scrollTo({left:i*tr.clientWidth, behavior:"smooth"}); setTimeout(()=>marcar(k),350); }
function marcar(k){
  const n=IMGS[k].length, i=Math.min(n-1,Math.max(0,atual(k)));
  document.getElementById("ix-"+k).textContent=(i+1)+"/"+n;
  document.querySelectorAll(`#dt-${k} i`).forEach((d,j)=>d.classList.toggle("on", j===i));
  const sec=document.getElementById("post-"+k);
  sec.querySelector(".nav.prev").disabled = i===0; sec.querySelector(".nav.next").disabled = i===n-1;
}
let lbK=null, lbI=0;
function abrirLB(k,i){ lbK=k; lbI=i; mostrarLB(); document.getElementById("lb").classList.add("on"); }
function mostrarLB(){ const lb=document.getElementById("lb"); lb.querySelector("img").src=IMGS[lbK][lbI]; lb.querySelector("img").alt=`Post ${lbK}, slide ${lbI+1}`; lb.querySelector(".c").textContent=`Post ${lbK} · slide ${lbI+1} de ${IMGS[lbK].length}`; }
function passoLB(d){ const n=IMGS[lbK].length; lbI=(lbI+d+n)%n; mostrarLB(); }
function fecharLB(){ document.getElementById("lb").classList.remove("on"); }

async function copiar(){
  const txt = resumo(); const msg=document.getElementById("copiado");
  document.getElementById("resumo").value = txt;
  let ok=false;
  try{ if(navigator.clipboard && window.isSecureContext){ await navigator.clipboard.writeText(txt); ok=true; } }catch(e){ ok=false; }
  if(!ok){
    const ta=document.getElementById("resumo"); ta.removeAttribute("readonly"); ta.focus(); ta.select(); ta.setSelectionRange(0, txt.length);
    try{ ok=document.execCommand("copy"); }catch(e){ ok=false; }
    ta.setAttribute("readonly",""); window.getSelection && window.getSelection().removeAllRanges();
  }
  msg.textContent = ok ? "Copiado. Agora é só colar na conversa." : "Não consegui copiar sozinho. Selecione o texto abaixo e copie.";
  setTimeout(()=>{ if(ok) msg.textContent=""; }, 6000);
}

carregar(); montar(); POSTS.forEach(p=>pintar(String(p.n))); contar(); ligar();
</script>
</body>
</html>
"""

html = (HTML.replace("__FONTES__", fontes()).replace("__LOGO__", logo_h)
            .replace("__TITULO__", _html.escape(CONFIG["titulo_pagina"])).replace("__EYEBROW__", _html.escape(CONFIG["eyebrow"]))
            .replace("__H1__", _html.escape(CONFIG["h1"])).replace("__SUB__", _html.escape(CONFIG["sub"]))
            .replace("__NPOSTS__", str(len(POSTS))).replace("__PULOS__", pulos_html).replace("__NOTAS__", notas_html)
            .replace("__FONTES_LISTA__", fontes_html).replace("__GRADE__", json.dumps(grades))
            .replace("__RESUMO_TITULO__", json.dumps(CONFIG["resumo_titulo"], ensure_ascii=False))
            .replace("__CHAVE__", json.dumps(CONFIG["chave"]))
            .replace("__DADOS__", json.dumps(dados_js, ensure_ascii=False))
            .replace("__IMGS__", json.dumps(imagens))
            .replace("__SIMBOLO__", json.dumps(simbolo_neg))
            .replace("__FUSO__", json.dumps(FUSO, ensure_ascii=False)))
open(SAIDA, "w", encoding="utf-8").write(html)
print(SAIDA, round(os.path.getsize(SAIDA) / 1024 / 1024, 2), "MB")
proib = [c for c in ("—", "–") if c in re.sub(r"data:(image/jpeg|font/woff2);base64,[A-Za-z0-9+/=]+", "", html)]
print("travessoes:", proib)
