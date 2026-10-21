# -*- coding: utf-8 -*-
"""Revisão de jan/fev de 2027: dados, capas (fundo certo), hashtags, palavras proibidas e folhas de contato.

python3 conferir.py            -> resumo dos 40 posts
python3 conferir.py folhas     -> também as folhas de contato em revisao/folhas/
"""
import glob, importlib.util, os, re, sys, subprocess
from PIL import Image
J = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(J, "plano"))
from grade_final import FUNDOS
COR = {"papel": (251, 250, 246), "tinta": (15, 20, 16), "suave": (209, 250, 229), "verde": (5, 150, 105)}

def mod(p):
    s = importlib.util.spec_from_file_location("m" + str(abs(hash(p))), p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def fundo(img):
    im = Image.open(img).convert("RGB")
    w, h = im.size
    pts = [im.getpixel((x, y)) for x, y in [(8, h // 2), (w - 8, h // 2), (w // 2, 8), (8, 8), (w - 8, h - 8)]]
    def dist(a, b): return sum((x - y) ** 2 for x, y in zip(a, b)) ** .5
    votos = {}
    for p in pts:
        k = min(COR, key=lambda c: dist(p, COR[c]))
        votos[k] = votos.get(k, 0) + 1
    return max(votos, key=votos.get)

problemas = []
dados = sorted(glob.glob(os.path.join(J, "dados", "2027-0[12]-*.py")))
vistos = set()
for arq in dados:
    P = mod(arq).POST
    d = P["iso"][:10]
    vistos.add(d)
    pasta = os.path.join(J, "saida", P["pasta"])
    capa = os.path.join(pasta, "capa.jpg" if P["tipo"] == "reel" else "01.jpg")
    linha = f"{d} {P['tipo'][:4]:4s} {P['pasta'][11:][:44]:44s}"
    if not os.path.isfile(capa):
        problemas.append(f"{d}: sem capa ({capa})"); print(linha, "SEM CAPA"); continue
    f = fundo(capa)
    esperado = FUNDOS.get(d)
    ok = "ok" if f == esperado else f"FUNDO {f} (pauta: {esperado})"
    if f != esperado: problemas.append(f"{d}: fundo {f}, pauta {esperado}")
    tags = re.findall(r"#\w+", P["legenda"])
    if len(tags) > 5: problemas.append(f"{d}: {len(tags)} hashtags")
    txt = " ".join([P["legenda"]] + list(P.get("alt", [])) + list(P.get("slides", [])))
    if re.search(r"[–—]", txt): problemas.append(f"{d}: travessão ou meia-risca")
    if re.search(r"\bapp\b|\baplicativo\b", txt, re.I) and "Aplicativo de transporte" not in txt: problemas.append(f"{d}: 'app'")
    if re.search(r"intelig[eê]ncia artificial|\bIA\b", txt): problemas.append(f"{d}: IA")
    for m in re.finditer(r"[Gg]ratuit[oa]", txt):
        trecho = txt[max(0, m.start() - 5): m.end() + 30]
        if "para o controle financeiro" not in trecho: problemas.append(f"{d}: 'gratuito' fora da frase: {trecho!r}")
    if P["tipo"] == "reel":
        for c in ("reel.mp4", "previa.mp4"):
            if not os.path.isfile(os.path.join(pasta, c)): problemas.append(f"{d}: falta {c}")
        dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(pasta, "reel.mp4")],
                             capture_output=True, text=True).stdout.strip() if os.path.isfile(os.path.join(pasta, "reel.mp4")) else "?"
        extra = f"{float(dur):.1f}s" if dur not in ("", "?") else "?"
    else:
        n = len(glob.glob(os.path.join(pasta, "[0-9][0-9].jpg")))
        extra = f"{n} slides"
        if n != len(P["slides"]): problemas.append(f"{d}: {n} imagens e {len(P['slides'])} slides nos dados")
        if len(P.get("alt", [])) != n: problemas.append(f"{d}: {len(P.get('alt', []))} textos alternativos para {n} imagens")
    print(linha, f"{f:6s}", ok, extra, f"{len(tags)} tags")
faltam = sorted(set(FUNDOS) - vistos)
print(f"\n{len(dados)} de 40 posts com dados; faltam: {', '.join(x[5:] for x in faltam) or 'nenhum'}")
print("PROBLEMAS:" if problemas else "Sem problemas.", *problemas, sep="\n  ")

if "folhas" in sys.argv:
    only = [a for a in sys.argv[sys.argv.index("folhas") + 1:]]
    os.makedirs(os.path.join(J, "revisao", "folhas"), exist_ok=True)
    for arq in dados:
        P = mod(arq).POST
        pasta = os.path.join(J, "saida", P["pasta"])
        if P["tipo"] == "reel" and not all(os.path.isfile(os.path.join(pasta, c)) for c in ("reel.mp4", "capa.jpg")):
            print("sem vídeo ou capa ainda:", P["pasta"]); continue
        if only and not any(o in P["pasta"] for o in only):
            continue
        if P["tipo"] == "reel":
            q = os.path.join(J, "revisao", "folhas", P["pasta"] + "_q")
            os.makedirs(q, exist_ok=True)
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(pasta, "reel.mp4")], capture_output=True, text=True).stdout.strip())
            ts = [0.2, 0.9] + [round(dur * k / 9, 1) for k in range(2, 9)] + [dur - 0.5]
            ims = [Image.open(os.path.join(pasta, "capa.jpg")).convert("RGB")]
            for t in ts:
                o = os.path.join(q, f"{t:05.1f}.png")
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", os.path.join(pasta, "reel.mp4"), "-frames:v", "1", o])
                ims.append(Image.open(o).convert("RGB"))
            W, H = 216, 384
        else:
            ims = [Image.open(f).convert("RGB") for f in sorted(glob.glob(os.path.join(pasta, "[0-9][0-9].jpg")))]
            W, H = 300, 375
        cols = 6 if P["tipo"] == "reel" else 4
        rows = (len(ims) + cols - 1) // cols
        folha = Image.new("RGB", (cols * (W + 6), rows * (H + 6)), "white")
        for i, im in enumerate(ims):
            folha.paste(im.resize((W, H)), ((i % cols) * (W + 6), (i // cols) * (H + 6)))
        folha.save(os.path.join(J, "revisao", "folhas", P["pasta"] + ".jpg"), quality=85)
    print("folhas em", os.path.join(J, "revisao", "folhas"))
