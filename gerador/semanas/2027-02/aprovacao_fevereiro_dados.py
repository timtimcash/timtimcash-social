# -*- coding: utf-8 -*-
"""Fevereiro de 2027 inteiro para aprovação: os 20 posts de J/dados (10 carrosséis e 10 Reels).

python3 /home/claude/timtimcash-social/gerador/aprovacao.py aprovacao_fevereiro_dados.py saida aprovacao/fevereiro.html
"""
import glob, importlib.util, os

N = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/claude/timtimcash-social"
POSTS_REPO = os.path.join(REPO, "posts")
SAIDA = os.path.join(N, "saida")
FUSO = "horário de Brasília (America/Sao_Paulo, UTC−3)"


def _mod(caminho):
    s = importlib.util.spec_from_file_location("m" + str(abs(hash(caminho))), caminho)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


CURTOS = {
    "2027-02-01_fevereiro-do-seu-dinheiro": "Fevereiro do seu dinheiro",
    "2027-02-03_reel-o-ano-escolar-numa-conta": "O ano escolar numa conta",
    "2027-02-04_remessas-da-planilha-para-o-site": "Remessas: da planilha para o site",
    "2027-02-05_reel-o-envelope-do-carnaval": "O envelope do Carnaval",
    "2027-02-06_gasto-anual-vira-mensal": "O gasto do ano, dividido por 12",
    "2027-02-10_reel-quanto-custou-o-carnaval": "Quanto custou o Carnaval?",
    "2027-02-11_ir-saude-e-educacao-o-que-deduz": "IR: saúde e educação",
    "2027-02-12_reel-tudo-de-la-fora-numa-tela": "Tudo de lá fora numa tela",
    "2027-02-13_transferencia-nao-e-gasto": "Guardar não é gastar",
    "2027-02-15_reel-fluxo-o-ano-numa-tela": "Fluxo: entrou, saiu, guardou",
    "2027-02-17_realizado-previsto-e-ambos": "3 jeitos de ver o mês",
    "2027-02-18_reel-atalhos-no-computador": "Atalhos no computador",
    "2027-02-19_la-fora-na-declaracao": "Lá fora na declaração",
    "2027-02-20_reel-faxina-de-sabado": "Faxina de sábado",
    "2027-02-22_informe-de-rendimentos-o-que-conferir": "Informe de rendimentos",
    "2027-02-23_reel-meta-de-receita": "Meta de receita",
    "2027-02-24_dividas-qual-pagar-primeiro": "Qual dívida pagar primeiro?",
    "2027-02-25_reel-nova-remessa-cambio-na-hora": "Câmbio efetivo na hora",
    "2027-02-26_fevereiro-fechou-5-perguntas": "Fevereiro fechou: 5 perguntas",
    "2027-02-27_reel-o-dia-10-de-marco": "O dia 10 de março",
}

POSTS = []
for arq in sorted(glob.glob(os.path.join(N, "dados", "2027-02-*.py"))):
    p = dict(_mod(arq).POST)
    p.update(status_tipo="novo", status_atual="Novo")
    if p["tipo"] == "reel":
        for c in ("video", "capa", "previa"):
            p[c] = os.path.join(N, p[c])
    else:
        p["imagens_dir"] = SAIDA
    POSTS.append(p)
POSTS.sort(key=lambda p: p["iso"])
for i, p in enumerate(POSTS, 1):
    p["n"] = i
    p["titulo_curto"] = CURTOS[p["pasta"]]
assert len(POSTS) == 20, len(POSTS)
assert sum(p["tipo"] == "reel" for p in POSTS) == 10


def _capa(p):
    return p["capa"] if p["tipo"] == "reel" else os.path.join(p["imagens_dir"], p["pasta"], "01.jpg")


# grade do perfil em 27/02: o fixado, fevereiro do mais novo para o mais antigo e o fim de janeiro (proposta anterior)
JANEIRO = [("30/01", "2027-01-30_reel-revisao-de-sabado/capa.jpg", "reel"),
           ("29/01", "2027-01-29_fechamento-de-2026-la-fora/01.jpg", "carrossel"),
           ("28/01", "2027-01-28_reel-janeiro-contra-janeiro/capa.jpg", "reel"),
           ("27/01", "2027-01-27_categorias-que-funcionam/01.jpg", "carrossel"),
           ("23/01", "2027-01-23_reel-cascata-do-seu-2026/capa.jpg", "reel"),
           ("22/01", "2027-01-22_seus-dados-guardados/01.jpg", "carrossel")]
itens = [("fixado", os.path.join(POSTS_REPO, "2026-09-30_comece-por-aqui/01.jpg"), "fixado")]
itens += [(p["data_curta"].split(", ")[1][:5], _capa(p), p["tipo"]) for p in reversed(POSTS)]
itens += [(d, os.path.join(SAIDA, c), t) for d, c, t in JANEIRO]
for _, c, _ in itens:
    assert os.path.isfile(c), c

fontes, vistos = [], set()
for p in POSTS:
    for t, u in p.get("fontes", []):
        if u not in vistos:
            vistos.add(u); fontes.append((t, u))

# notas da página, escritas na revisão em aprovacao_notas.py
_notas = os.path.join(N, "aprovacao_notas.py")
NOTAS = getattr(_mod(_notas), "NOTAS_FEVEREIRO", []) if os.path.isfile(_notas) else []

CONFIG = {
    "titulo_pagina": "Fevereiro no Instagram · timtimcash",
    "eyebrow": "Proposta para aprovação · enviada em 20/10/2026",
    "h1": "Fevereiro: o mês curto",
    "sub": "Vinte posts, dez Reels, na ordem do mês, com o calendário e a prévia da grade do perfil. Nada é agendado antes da sua resposta.",
    "chave": "timtimcash-aprovacao-fevereiro-2027-v1",
    "resumo_titulo": "Avaliação dos posts de fevereiro de 2027 do timtimcash (proposta de 20/10/2026)",
    "largura_imagens": 720,
    "aprovar_todos": True,
    "notas": NOTAS,
    "fontes": fontes,
    "grade_mes": {"titulo": "Prévia da grade do perfil", "legenda": "Como o perfil fica em 27/02",
                  "nota": "A grade mostra as capas em 3:4. O post fixado (“Comece por aqui”) fica no topo; o ícone de play marca os Reels. Depois de fevereiro aparecem os últimos posts de janeiro, da proposta ao lado.",
                  "itens": itens},
}
