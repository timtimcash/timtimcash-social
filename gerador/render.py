# -*- coding: utf-8 -*-
"""Renderiza uma semana de artes em JPEG dentro de posts/.

python3 gerador/render.py gerador/semanas/AAAA-MM-DD.py
Baixa a fonte Inter (GitHub rsms/inter) se ainda não existir em /tmp/inter.
"""
import os, sys, io, zipfile, importlib.util, urllib.request
from PIL import Image
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
INTER_ZIP = "https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip"

def garante_fonte():
    alvo = os.environ.get("INTER_TTF_DIR", "/tmp/inter/extras/ttf")
    if os.path.exists(os.path.join(alvo, "Inter-ExtraBold.ttf")):
        return
    dados = urllib.request.urlopen(INTER_ZIP).read()
    zipfile.ZipFile(io.BytesIO(dados)).extractall("/tmp/inter")

def main(spec_path):
    garante_fonte()
    spec = importlib.util.spec_from_file_location("semana", spec_path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    html_dir = "/tmp/tt_html"; os.makedirs(html_dir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        w, h = getattr(mod, "TAMANHO", (1080, 1350))
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        for nome, fn in mod.POSTS.items():
            destino = os.path.join(REPO, "posts", nome); os.makedirs(destino, exist_ok=True)
            for i, html in enumerate(fn(), 1):
                hp = os.path.join(html_dir, f"{nome}_{i:02d}.html")
                open(hp, "w", encoding="utf-8").write(html)
                pg.goto("file://" + hp); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(150)
                sobra = pg.evaluate("() => { const b=document.querySelector('.body'); return b.scrollHeight - b.clientHeight }")
                if sobra > 0:
                    print(f"ATENCAO: texto estourou a area em {nome} slide {i} ({sobra}px)")
                png = pg.screenshot()
                Image.open(io.BytesIO(png)).convert("RGB").save(
                    os.path.join(destino, f"{i:02d}.jpg"), "JPEG", quality=92, optimize=True, subsampling=0)
                print("ok", nome, i)
        b.close()

if __name__ == "__main__":
    main(sys.argv[1])
