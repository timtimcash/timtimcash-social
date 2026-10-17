# -*- coding: utf-8 -*-
"""Remonta, a partir deste repositório, a pasta de trabalho dos posts de novembro e dezembro de 2026 (a "N" dos roteiros).

Uso:  python3 gerador/restaurar_pasta.py <destino>

Serve para refazer um post já aprovado numa máquina nova (por exemplo, os quatro posts de dezembro com números que podem
mudar até a publicação: 07, 10, 11 e 16/12). O repositório precisa estar em /home/claude/timtimcash-social, porque o kit
importa gerador/artes.py desse caminho.

O que vai para <destino>:
- kit/ (de gerador/semanas/2026-11/kit), equipes/ e dados/ dos dois meses, PAUTA.md, FATOS.md e os dados das páginas de
  aprovação;
- saida/<pasta>/telas/ (as telas reais de gerador/semanas/<mês>/telas/<pasta>/) e, em saida/<pasta>/, a arte aprovada
  que está em posts/<pasta>/;
- nos roteiros copiados, o caminho antigo da pasta de trabalho troca pelo <destino>.

A fonte Inter 4.1 (licença OFL) vem do lançamento oficial no GitHub, se ainda não estiver em /tmp/inter
(o caminho padrão de gerador/artes.py; outro caminho vai em INTER_TTF_DIR).

Fica de fora, de propósito: a cópia local do site e o servidor falso das capturas (nunca vão para este repositório
público). Para capturar telas novas, é preciso o index.html mais recente, enviado pelo dono.
"""
import glob, io, os, shutil, sys, urllib.request, zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEMANAS = os.path.join(REPO, "gerador", "semanas")
MESES = ["2026-11", "2026-12"]
N_ANTIGO = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
INTER_ZIP = "https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip"
INTER_DIR = "/tmp/inter"


def copia_arvore(de, para):
    shutil.copytree(de, para, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))


def fonte():
    ttf = os.environ.get("INTER_TTF_DIR", os.path.join(INTER_DIR, "extras", "ttf"))
    if os.path.isfile(os.path.join(ttf, "Inter-Bold.ttf")):
        return f"Inter já estava em {ttf}"
    with urllib.request.urlopen(INTER_ZIP, timeout=120) as r:
        zipfile.ZipFile(io.BytesIO(r.read())).extractall(INTER_DIR)
    assert os.path.isfile(os.path.join(INTER_DIR, "extras", "ttf", "Inter-Bold.ttf")), "a Inter não veio no zip"
    return f"Inter 4.1 baixada em {INTER_DIR}"


def main(destino):
    destino = os.path.abspath(destino)
    os.makedirs(os.path.join(destino, "dados"), exist_ok=True)
    copia_arvore(os.path.join(SEMANAS, "2026-11", "kit"), os.path.join(destino, "kit"))
    pastas = []
    for mes in MESES:
        m = os.path.join(SEMANAS, mes)
        for eq in sorted(os.listdir(os.path.join(m, "equipes"))):
            copia_arvore(os.path.join(m, "equipes", eq), os.path.join(destino, "equipes", eq))
        for arq in glob.glob(os.path.join(m, "dados", "*.py")):
            shutil.copy2(arq, os.path.join(destino, "dados"))
        for pasta in sorted(os.listdir(os.path.join(m, "telas"))):
            copia_arvore(os.path.join(m, "telas", pasta), os.path.join(destino, "saida", pasta, "telas"))
        for arq in glob.glob(os.path.join(m, "aprovacao_*_dados.py")) + [os.path.join(m, x) for x in ("PAUTA.md", "FATOS.md")]:
            if os.path.isfile(arq):
                shutil.copy2(arq, destino)
    for pasta in sorted(os.listdir(os.path.join(REPO, "posts"))):
        if pasta[:7] in MESES:
            pastas.append(pasta)
            os.makedirs(os.path.join(destino, "saida", pasta), exist_ok=True)
            for arq in glob.glob(os.path.join(REPO, "posts", pasta, "*")):
                shutil.copy2(arq, os.path.join(destino, "saida", pasta))
    trocados = 0
    for arq in glob.glob(os.path.join(destino, "**", "*.py"), recursive=True):
        txt = open(arq, encoding="utf-8").read()
        if N_ANTIGO in txt and destino != N_ANTIGO:
            open(arq, "w", encoding="utf-8").write(txt.replace(N_ANTIGO, destino))
            trocados += 1
    print(f"pasta de trabalho em {destino}: {len(pastas)} posts com arte, {len(glob.glob(os.path.join(destino, 'dados', '*.py')))} arquivos de dados, "
          f"caminho trocado em {trocados} roteiros")
    print(fonte())
    print("Para refazer um carrossel: python3 equipes/<equipe>/posts.py <data>, por exemplo dc2/posts.py 2026-12-16."
          " Para um Reel: python3 equipes/<equipe>/reel_<dia>.py. Depois: python3 kit/checar.py tudo.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
