# -*- coding: utf-8 -*-
"""Folha de contato dos slides de uma pasta: python3 folha.py <pasta absoluta ou nome em J/saida> [colunas] [largura] [saida.jpg]"""
import sys, glob, os
from PIL import Image
J = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev"
AQUI = os.path.dirname(os.path.abspath(__file__))
pasta = sys.argv[1]
d = pasta if os.path.isabs(pasta) else os.path.join(J, "saida", pasta)
cols = int(sys.argv[2]) if len(sys.argv) > 2 else 4
w = int(sys.argv[3]) if len(sys.argv) > 3 else 420
imgs = sorted(glob.glob(os.path.join(d, "[0-9][0-9].jpg")))
h = int(1350 * w / 1080)
rows = (len(imgs) + cols - 1) // cols
gap = 14
folha = Image.new("RGB", (cols * w + (cols + 1) * gap, rows * (h + gap) + gap), (60, 60, 60))
for i, p in enumerate(imgs):
    r, c = divmod(i, cols)
    folha.paste(Image.open(p).resize((w, h), Image.LANCZOS), (gap + c * (w + gap), gap + r * (h + gap)))
out = sys.argv[4] if len(sys.argv) > 4 else os.path.join(AQUI, "prev", os.path.basename(d.rstrip("/"))[:10] + ".jpg")
folha.save(out, quality=88)
print(out, folha.size)
