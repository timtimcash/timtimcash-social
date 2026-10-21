# -*- coding: utf-8 -*-
"""Janeiro de 2027 inteiro para aprovação: os 20 posts de J/dados (10 carrosséis e 10 Reels).

python3 /home/claude/timtimcash-social/gerador/aprovacao.py aprovacao_janeiro_dados.py saida aprovacao/janeiro.html
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
    "2027-01-02_comece-2027-organizado": "2027 começa organizado",
    "2027-01-04_reel-passo-1-quanto-voce-tem": "Passo 1: quanto você tem?",
    "2027-01-06_material-escolar-o-que-a-escola-nao-pode-pedir": "Material escolar: o que não pode",
    "2027-01-07_reel-lance-na-hora": "Lance em 5 segundos",
    "2027-01-08_habito-leva-66-dias": "Hábito: 66 dias, em média",
    "2027-01-10_reel-passo-2-para-onde-vai": "Passo 2: para onde vai?",
    "2027-01-27_categorias-que-funcionam": "Categorias que funcionam",
    "2027-01-13_reel-ipva-desconto-a-vista": "IPVA: 3% vale quanto?",
    "2027-01-14_passo-3-os-limites": "Passo 3: os limites",
    "2027-01-15_reel-insights-o-que-o-mes-diz": "Os recados do seu mês",
    "2027-01-11_remessas-quanto-foi-para-fora": "Quanto foi para fora, ano a ano",
    "2027-01-18_reel-passo-4-e-se-2027-apertar": "Passo 4: e se 2027 apertar?",
    "2027-01-20_traga-3-meses-de-historico": "Traga 3 meses do passado",
    "2027-01-21_reel-ha-quanto-tempo-esta-la-fora": "Há quanto tempo está lá fora?",
    "2027-01-22_seus-dados-guardados": "Seus dados, guardados todo dia",
    "2027-01-23_reel-cascata-do-seu-2026": "A cascata do seu 2026",
    "2027-01-29_fechamento-de-2026-la-fora": "2026 fechou: informe o saldo",
    "2027-01-28_reel-janeiro-contra-janeiro": "Janeiro contra janeiro",
    "2027-01-16_o-que-se-repete-todo-mes": "O que se repete todo mês",
    "2027-01-30_reel-revisao-de-sabado": "Revisão de sábado: 5 minutos",
}

POSTS = []
for arq in sorted(glob.glob(os.path.join(N, "dados", "2027-01-*.py"))):
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


# grade do perfil em 30/01: o fixado, janeiro do mais novo para o mais antigo e o fim de dezembro (aprovado e agendado)
DEZEMBRO = [("30/12", "2026-12-30_reel-2027-comeca-com-um-plano/capa.jpg", "reel"),
            ("28/12", "2026-12-28_anote-quanto-ha-la-fora/01.jpg", "carrossel"),
            ("27/12", "2026-12-27_reel-o-que-mudou-no-seu-ano/capa.jpg", "reel"),
            ("23/12", "2026-12-23_viagem-para-fora-o-iof/01.jpg", "carrossel"),
            ("22/12", "2026-12-22_reel-boas-festas/capa.jpg", "reel"),
            ("21/12", "2026-12-21_metas-de-2027-que-da-para-medir/01.jpg", "carrossel")]
itens = [("fixado", os.path.join(POSTS_REPO, "2026-09-30_comece-por-aqui/01.jpg"), "fixado")]
itens += [(p["data_curta"].split(", ")[1][:5], _capa(p), p["tipo"]) for p in reversed(POSTS)]
itens += [(d, os.path.join(POSTS_REPO, c), t) for d, c, t in DEZEMBRO]
for _, c, _ in itens:
    assert os.path.isfile(c), c

fontes, vistos = [], set()
for p in POSTS:
    for t, u in p.get("fontes", []):
        if u not in vistos:
            vistos.add(u); fontes.append((t, u))

# notas da página, escritas na revisão em aprovacao_notas.py
_notas = os.path.join(N, "aprovacao_notas.py")
NOTAS = getattr(_mod(_notas), "NOTAS_JANEIRO", []) if os.path.isfile(_notas) else []

CONFIG = {
    "titulo_pagina": "Janeiro no Instagram · timtimcash",
    "eyebrow": "Proposta para aprovação · enviada em 20/10/2026",
    "h1": "Janeiro: comece 2027 organizado",
    "sub": "Vinte posts, dez Reels, na ordem do mês, com o calendário e a prévia da grade do perfil. Nada é agendado antes da sua resposta.",
    "chave": "timtimcash-aprovacao-janeiro-2027-v1",
    "resumo_titulo": "Avaliação dos posts de janeiro de 2027 do timtimcash (proposta de 20/10/2026)",
    "largura_imagens": 720,
    "aprovar_todos": True,
    "notas": NOTAS,
    "fontes": fontes,
    "grade_mes": {"titulo": "Prévia da grade do perfil", "legenda": "Como o perfil fica em 30/01",
                  "nota": "A grade mostra as capas em 3:4. O post fixado (“Comece por aqui”) fica no topo; o ícone de play marca os Reels. Depois de janeiro aparecem os últimos posts de dezembro, já aprovados.",
                  "itens": itens},
}
