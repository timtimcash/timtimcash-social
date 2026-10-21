# -*- coding: utf-8 -*-
"""Folha de contato dos quadros de prévia de um Reel, com as linhas da zona segura (270 e 1600 px; na capa, 285 e 1635 px).
python3 folha.py <pasta com q_*.png [capa.png]> <saida.jpg> [colunas] [largura]"""
import sys, os, glob
from PIL import Image, ImageDraw, ImageFont
pasta, saida = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6
W = int(sys.argv[4]) if len(sys.argv) > 4 else 300
arqs = sorted(glob.glob(os.path.join(pasta, "q_*.png")))
if os.path.exists(os.path.join(pasta, "capa.png")):
    arqs.append(os.path.join(pasta, "capa.png"))
H = int(W * 1920 / 1080)
rows = (len(arqs) + cols - 1) // cols
folha = Image.new("RGB", (cols * (W + 8) + 8, rows * (H + 34) + 8), "#8a8a8a")
fonte = ImageFont.truetype("/tmp/inter/extras/ttf/Inter-Bold.ttf", 20)
d = ImageDraw.Draw(folha)
for k, a in enumerate(arqs):
    im = Image.open(a).convert("RGB").resize((W, H), Image.LANCZOS)
    x = 8 + (k % cols) * (W + 8); y = 8 + (k // cols) * (H + 34)
    folha.paste(im, (x, y + 26))
    capa = os.path.basename(a) == "capa.png"
    for gy in ((285, 1635) if capa else (270, 1600)):
        yy = y + 26 + int(gy * H / 1920)
        d.line([(x, yy), (x + W, yy)], fill="#00a0ff" if capa else "#ff00ff", width=1)
    if not capa:
        xx = x + int(1000 * W / 1080)
        d.line([(xx, y + 26 + H // 2), (xx, y + 26 + H)], fill="#ff00ff", width=1)
    nome = os.path.basename(a).replace("q_", "").replace(".png", "")
    d.text((x + 4, y + 3), nome + ("" if nome == "capa" else " s"), fill="#000", font=fonte)
folha.save(saida, quality=88)
print(saida, folha.size)
