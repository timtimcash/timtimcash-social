# -*- coding: utf-8 -*-
"""Folha de contato: python3 folha.py saida.jpg colunas largura img1 img2 ..."""
import sys
from PIL import Image, ImageDraw, ImageFont
out, cols, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
imgs = sys.argv[4:]
ims = [Image.open(p).convert("RGB") for p in imgs]
h = max(int(im.size[1] * w / im.size[0]) for im in ims)
rows = (len(ims) + cols - 1) // cols
gap = 16
sheet = Image.new("RGB", (cols * w + (cols + 1) * gap, rows * (h + 30) + (rows + 1) * gap), (60, 60, 60))
d = ImageDraw.Draw(sheet)
for i, (im, p) in enumerate(zip(ims, imgs)):
    r, c = divmod(i, cols)
    im2 = im.resize((w, int(im.size[1] * w / im.size[0])), Image.LANCZOS)
    x, y = gap + c * (w + gap), gap + r * (h + 30 + gap)
    sheet.paste(im2, (x, y + 30))
    d.text((x, y + 6), p.split("/")[-2][-28:] + "/" + p.split("/")[-1], fill=(255, 255, 255))
sheet.save(out, quality=88)
print(out, sheet.size)
