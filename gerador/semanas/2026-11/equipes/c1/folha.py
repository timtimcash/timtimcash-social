# -*- coding: utf-8 -*-
"""Folha de contato: python3 folha.py saida.jpg colunas largura img1 img2 ..."""
import sys
from PIL import Image, ImageDraw, ImageFont
saida, cols, larg = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
imgs = sys.argv[4:]
ims = [Image.open(p).convert("RGB") for p in imgs]
alt = max(int(larg * im.size[1] / im.size[0]) for im in ims)
gap = 16
rows = (len(ims) + cols - 1) // cols
W = cols * larg + (cols + 1) * gap
H = rows * (alt + 30) + (rows + 1) * gap
F = Image.new("RGB", (W, H), (200, 200, 200))
d = ImageDraw.Draw(F)
for i, (im, p) in enumerate(zip(ims, imgs)):
    r, c = divmod(i, cols)
    h = int(larg * im.size[1] / im.size[0])
    x = gap + c * (larg + gap); y = gap + r * (alt + 30 + gap)
    F.paste(im.resize((larg, h), Image.LANCZOS), (x, y + 30))
    d.text((x, y + 8), p.split("/")[-2][-28:] + "/" + p.split("/")[-1], fill=(0, 0, 0))
F.save(saida, quality=90)
print(saida, F.size)
