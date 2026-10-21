# -*- coding: utf-8 -*-
"""Confere a saída dos 5 Reels da equipe fs: arquivos, duração, resolução, áudio mudo e uma folha de contato tirada do próprio
reel.mp4 (quadros extraídos com o ffmpeg) junto da capa.jpg. Uso: python3 confere_saida.py [pastas...]"""
import os, sys, json, subprocess, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import J, folha

PASTAS = sys.argv[1:] or ["2027-02-18_reel-atalhos-no-computador", "2027-02-20_reel-faxina-de-sabado", "2027-02-23_reel-meta-de-receita",
                          "2027-02-25_reel-nova-remessa-cambio-na-hora", "2027-02-27_reel-o-dia-10-de-marco"]
for p in PASTAS:
    s = os.path.join(J, "saida", p)
    v = os.path.join(s, "reel.mp4")
    if not os.path.isfile(v):
        print(p, "sem reel.mp4 ainda"); continue
    info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", v], capture_output=True, text=True).stdout)
    vs = [x for x in info["streams"] if x["codec_type"] == "video"][0]
    au = [x for x in info["streams"] if x["codec_type"] == "audio"]
    dur = float(info["format"]["duration"])
    vol = subprocess.run(["ffmpeg", "-i", v, "-af", "volumedetect", "-vn", "-f", "null", "-"], capture_output=True, text=True).stderr
    maxv = [l for l in vol.splitlines() if "max_volume" in l]
    tel = len(glob.glob(os.path.join(s, "telas", "*.jpg")))
    print(f"{p}: {vs['width']}x{vs['height']} {vs.get('r_frame_rate')} {dur:.2f} s · áudio {len(au)} faixa(s) {maxv[0].split(':')[-1].strip() if maxv else '?'} · "
          f"capa {os.path.isfile(os.path.join(s, 'capa.jpg'))} · prévia {os.path.isfile(os.path.join(s, 'previa.mp4'))} · telas {tel} · {os.path.getsize(v) // 1024} KB")
    out = os.path.join(J, "equipes", "fs", "trabalho", "video_" + p[:10])
    os.makedirs(out, exist_ok=True)
    tempos = [0.0, 0.6, 2.0, round(dur * .2, 1), round(dur * .35, 1), round(dur * .5, 1), round(dur * .65, 1), round(dur * .8, 1), round(dur - .5, 1)]
    fs = []
    for t in tempos:
        f = os.path.join(out, f"v_{t:05.2f}.png")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", v, "-frames:v", "1", f], check=True)
        fs.append(f)
    fs.append(os.path.join(s, "capa.jpg"))
    print("  folha:", folha(os.path.join(out, "folha_video.jpg"), fs, cols=10, larg=200))
