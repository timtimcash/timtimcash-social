# -*- coding: utf-8 -*-
"""Folha de contato dos slides de uma pasta: python3 folha.py <pasta> [colunas] [largura]"""
import sys, glob, os
from PIL import Image, ImageDraw
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
pasta = sys.argv[1]
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 4
w = int(sys.argv[3]) if len(sys.argv) > 3 else 420
imgs = sorted(glob.glob(os.path.join(N, "saida", pasta, "[0-9][0-9].jpg")))
so = sys.argv[4:]
if so:
    imgs = [i for i in imgs if os.path.basename(i)[:2] in so]
h = int(1350 * w / 1080)
rows = (len(imgs) + cols - 1) // cols
gap = 14
folha = Image.new("RGB", (cols * w + (cols + 1) * gap, rows * (h + gap) + gap), (60, 60, 60))
for i, p in enumerate(imgs):
    r, c = divmod(i, cols)
    folha.paste(Image.open(p).resize((w, h), Image.LANCZOS), (gap + c * (w + gap), gap + r * (h + gap)))
out = os.path.join(N, "equipes", "dc2", "prev", pasta[:10] + ("_" + "_".join(so) if so else "") + ".jpg")
folha.save(out, quality=88)
print(out, folha.size)
