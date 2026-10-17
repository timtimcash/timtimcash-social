# -*- coding: utf-8 -*-
"""Folha de contato das prévias: python3 folha.py <pasta_previa> <saida.jpg> [colunas] [largura]"""
import sys, os, glob
from PIL import Image, ImageDraw, ImageFont

pasta, saida = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 6
W = int(sys.argv[4]) if len(sys.argv) > 4 else 300
H = int(W * 1920 / 1080)
fs = sorted(glob.glob(os.path.join(pasta, "q_*.png")))
capa = os.path.join(pasta, "capa.png")
if os.path.isfile(capa):
    fs.append(capa)
rows = (len(fs) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (W + 12) + 12, rows * (H + 40) + 12), (200, 200, 196))
d = ImageDraw.Draw(sheet)
try:
    fonte = ImageFont.truetype("/tmp/inter/extras/ttf/Inter-Bold.ttf", 22)
except Exception:
    fonte = None
for i, f in enumerate(fs):
    im = Image.open(f).convert("RGB").resize((W, H), Image.LANCZOS)
    x, y = 12 + (i % cols) * (W + 12), 12 + (i // cols) * (H + 40)
    sheet.paste(im, (x, y + 28))
    # zona segura: 270 e 1600 px
    for yy in (270, 1600):
        yz = y + 28 + int(yy * H / 1920)
        d.line([(x, yz), (x + W, yz)], fill=(255, 0, 120), width=1)
    rot = os.path.basename(f).replace("q_", "").replace(".png", "")
    d.text((x + 2, y + 2), rot + (" s" if rot != "capa" else ""), fill=(20, 20, 20), font=fonte)
sheet.save(saida, quality=88)
print(saida, sheet.size)
