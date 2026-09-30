# -*- coding: utf-8 -*-
"""Folha de contato de quadros: python3 folha.py <pasta_ou_arquivos...> <saida.jpg> [colunas] [largura]"""
import sys, glob, os
from PIL import Image, ImageDraw, ImageFont
args = sys.argv[1:]
saida = [a for a in args if a.endswith(".jpg")][0]
cols, W = 4, 360
nums = [a for a in args if a.isdigit()]
if nums: cols = int(nums[0]); W = int(nums[1]) if len(nums) > 1 else W
fontes = [a for a in args if not a.isdigit() and a != saida]
fs = []
for f in fontes:
    fs += sorted(glob.glob(os.path.join(f, "*.png"))) if os.path.isdir(f) else [f]
H = int(W * 1920 / 1080)
rows = (len(fs) + cols - 1) // cols
sheet = Image.new("RGB", (cols * W + (cols + 1) * 12, rows * (H + 34) + 12), "#6b6b6b")
d = ImageDraw.Draw(sheet)
try: fn = ImageFont.truetype("/tmp/inter/extras/ttf/Inter-SemiBold.ttf", 20)
except Exception: fn = None
for i, f in enumerate(fs):
    im = Image.open(f).convert("RGB").resize((W, H), Image.LANCZOS)
    x = 12 + (i % cols) * (W + 12); y = 12 + (i // cols) * (H + 34)
    sheet.paste(im, (x, y + 26)); d.text((x, y + 2), os.path.basename(f), fill="white", font=fn)
sheet.save(saida, quality=88); print(saida, sheet.size)
