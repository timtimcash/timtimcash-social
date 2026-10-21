# Folha de contato (copiada da equipe dr1 de dezembro, sem mudança na lógica).
#   python3 folha.py <pasta com q_*.png [capa.png]> <saida.jpg> [colunas] [largura]
#   python3 folha.py --video <reel.mp4> <saida.jpg> "<t1 t2 ...>" [colunas] [largura] [capa.jpg]
# As linhas magenta marcam a zona segura (270 e 1600 px).
import sys, os, glob, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont

FONTE = "/tmp/inter/extras/ttf/Inter-Bold.ttf"


def montar(arqs, rotulos, saida, cols, W):
    H = int(W * 1920 / 1080)
    rows = (len(arqs) + cols - 1) // cols
    folha = Image.new("RGB", (cols * (W + 8) + 8, rows * (H + 34) + 8), "#8a8a8a")
    try:
        fonte = ImageFont.truetype(FONTE, 20)
    except OSError:
        fonte = ImageFont.load_default()
    d = ImageDraw.Draw(folha)
    for k, (a, rot) in enumerate(zip(arqs, rotulos)):
        im = Image.open(a).convert("RGB").resize((W, H), Image.LANCZOS)
        x = 8 + (k % cols) * (W + 8); y = 8 + (k // cols) * (H + 34)
        folha.paste(im, (x, y + 26))
        for gy in (270, 1600):
            yy = y + 26 + int(gy * H / 1920)
            d.line([(x, yy), (x + W, yy)], fill="#ff00ff", width=1)
        d.text((x + 4, y + 3), rot, fill="#000", font=fonte)
    folha.save(saida, quality=86)
    print(saida, folha.size)


if sys.argv[1] == "--video":
    video, saida, tempos = sys.argv[2], sys.argv[3], [float(x) for x in sys.argv[4].split()]
    cols = int(sys.argv[5]) if len(sys.argv) > 5 else 6
    W = int(sys.argv[6]) if len(sys.argv) > 6 else 240
    capa = sys.argv[7] if len(sys.argv) > 7 else None
    tmp = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(__file__)))
    arqs, rots = [], []
    for t in tempos:
        a = os.path.join(tmp, f"v_{t:06.2f}.png")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", video, "-frames:v", "1", a], check=True)
        arqs.append(a); rots.append(f"{t:g} s")
    if capa:
        arqs.append(capa); rots.append("capa")
    montar(arqs, rots, saida, cols, W)
    for a in arqs:
        if a.startswith(tmp):
            os.remove(a)
    os.rmdir(tmp)
else:
    pasta, saida = sys.argv[1], sys.argv[2]
    cols = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    W = int(sys.argv[4]) if len(sys.argv) > 4 else 250
    arqs = sorted(glob.glob(os.path.join(pasta, "q_*.png")))
    if os.path.exists(os.path.join(pasta, "capa.png")):
        arqs.append(os.path.join(pasta, "capa.png"))
    rots = []
    for a in arqs:
        nome = os.path.basename(a).replace("q_", "").replace(".png", "")
        rots.append(nome if nome == "capa" else f"{float(nome):g} s")
    montar(arqs, rots, saida, cols, W)
