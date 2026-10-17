import glob, importlib.util, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
R = os.path.join(N, "revisao")
fonte = ImageFont.truetype("/tmp/inter/extras/ttf/Inter-SemiBold.ttf", 22)
so = sys.argv[1:]
for arq in sorted(glob.glob(os.path.join(N, "dados", "*.py"))):
    s = importlib.util.spec_from_file_location("m", arq); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    p = m.POST; pasta = p["pasta"]
    if so and not any(x in pasta for x in so): continue
    if p["tipo"] == "carrossel":
        fs = sorted(glob.glob(os.path.join(N, "saida", pasta, "[0-9][0-9].jpg")))
        W, H = 432, 540
        folha = Image.new("RGB", (len(fs) * (W + 10) + 10, H + 20), "#888")
        for i, f in enumerate(fs):
            folha.paste(Image.open(f).convert("RGB").resize((W, H), Image.LANCZOS), (10 + i * (W + 10), 10))
    else:
        v = os.path.join(N, p["video"]); tmp = os.path.join(R, "_q"); os.makedirs(tmp, exist_ok=True)
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v], capture_output=True, text=True).stdout)
        tempos = [0, 0.4, 1.0, 2.0] + [round(x, 1) for x in [3 + i * (dur - 4) / 9 for i in range(10)]]
        ims = [Image.open(os.path.join(N, p["capa"])).convert("RGB")]
        for t in tempos:
            q = os.path.join(tmp, f"q_{t:05.2f}.jpg")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", v, "-frames:v", "1", "-q:v", "3", q], check=True)
            ims.append(Image.open(q).convert("RGB"))
        W, H = 270, 480
        cols = 8
        rows = (len(ims) + cols - 1) // cols
        folha = Image.new("RGB", (cols * (W + 8) + 8, rows * (H + 40) + 8), "#888")
        d = ImageDraw.Draw(folha)
        rot = ["capa"] + [f"{t:.1f} s" for t in tempos]
        for i, im in enumerate(ims):
            x, y = 8 + (i % cols) * (W + 8), 8 + (i // cols) * (H + 40)
            im = im.resize((W, H), Image.LANCZOS)
            dd = ImageDraw.Draw(im); dd.line([0, 270 * H / 1920, W, 270 * H / 1920], fill=(255, 0, 0), width=1); dd.line([0, 1600 * H / 1920, W, 1600 * H / 1920], fill=(255, 0, 0), width=1)
            folha.paste(im, (x, y)); d.text((x + 4, y + H + 6), rot[i], fill="white", font=fonte)
    saida = os.path.join(R, pasta + ".jpg"); folha.save(saida, quality=86); print(saida, folha.size)
