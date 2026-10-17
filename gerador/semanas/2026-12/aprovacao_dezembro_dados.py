# -*- coding: utf-8 -*-
"""Dezembro de 2026 inteiro para aprovação: os 20 posts novos de N/dados (10 carrosséis e 10 Reels).

python3 /home/claude/timtimcash-social/gerador/aprovacao.py aprovacao_dezembro_dados.py saida aprovacao/dezembro.html
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
    "2026-12-02_dezembro-do-seu-dinheiro": "Dezembro do seu dinheiro",
    "2026-12-03_reel-presentes-o-teto-antes-da-loja": "Presentes: o teto antes da loja",
    "2026-12-04_por-que-a-segunda-parcela-vem-menor": "Por que a 2ª parcela vem menor",
    "2026-12-06_reel-seu-2026-em-5-numeros": "Seu 2026 em 5 números",
    "2026-12-07_janeiro-caro-o-que-chega-junto": "Janeiro caro: o que chega junto",
    "2026-12-09_reel-a-jornada-la-fora": "Sua história lá fora",
    "2026-12-10_o-preco-do-dinheiro-emprestado": "O preço do dinheiro emprestado",
    "2026-12-11_reel-quatro-perguntas-antes-de-gastar": "4 perguntas antes de gastar o 13º",
    "2026-12-12_oito-siglas-do-seu-dinheiro": "8 siglas do seu dinheiro",
    "2026-12-14_reel-fixas-de-2027": "Fixas de 2027: lance uma vez",
    "2026-12-16_sua-inflacao-nao-e-a-do-ipca": "Sua inflação não é a do IPCA",
    "2026-12-17_reel-dolar-e-euro": "Dólar e euro, cada um na sua moeda",
    "2026-12-18_patrimonio-quanto-voce-tem": "Quanto você tem de verdade?",
    "2026-12-20_reel-seu-ano-num-arquivo": "Seu ano num arquivo",
    "2026-12-21_metas-de-2027-que-da-para-medir": "Metas de 2027 que dá para medir",
    "2026-12-22_reel-boas-festas": "Boas festas",
    "2026-12-23_viagem-para-fora-o-iof": "Viagem: o IOF é igual. O câmbio, não.",
    "2026-12-27_reel-o-que-mudou-no-seu-ano": "O que mudou no seu dezembro",
    "2026-12-28_anote-quanto-ha-la-fora": "31/12: anote quanto há lá fora",
    "2026-12-30_reel-2027-comeca-com-um-plano": "2027 começa com um plano",
}

POSTS = []
for arq in sorted(glob.glob(os.path.join(N, "dados", "2026-12-*.py"))):
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


# grade do perfil em 30/12: o fixado, dezembro do mais novo para o mais antigo e o fim de novembro (proposta enviada antes)
NOVEMBRO = [("30/11", "2026-11-30_reel-ultimo-dia-da-primeira-parcela/capa.jpg", "reel"),
            ("28/11", "2026-11-28_resgate-quando-o-dinheiro-volta/01.jpg", "carrossel"),
            ("27/11", "2026-11-27_reel-black-friday-respira/capa.jpg", "reel"),
            ("26/11", "2026-11-26_tres-categorias-levam-dois-tercos/01.jpg", "carrossel"),
            ("25/11", "2026-11-25_reel-atualizar-carteira/capa.jpg", "reel"),
            ("23/11", "2026-11-23_50-30-20-no-seu-extrato/01.jpg", "carrossel")]
itens = [("fixado", os.path.join(POSTS_REPO, "2026-09-30_comece-por-aqui/01.jpg"), "fixado")]
itens += [(p["data_curta"].split(", ")[1][:5], _capa(p), p["tipo"]) for p in reversed(POSTS)]
itens += [(d, os.path.join(SAIDA, c), t) for d, c, t in NOVEMBRO]
for _, c, _ in itens:
    assert os.path.isfile(c), c

fontes, vistos = [], set()
for p in POSTS:
    for t, u in p.get("fontes", []):
        if u not in vistos:
            vistos.add(u); fontes.append((t, u))

CONFIG = {
    "titulo_pagina": "Dezembro no Instagram · timtimcash",
    "eyebrow": "Proposta para aprovação · enviada em 16/10/2026",
    "h1": "Dezembro inteiro: 20 posts, 10 Reels",
    "sub": "Dez carrosséis e dez Reels, na ordem do mês, com o calendário e a prévia da grade do perfil. Nada é agendado antes da sua resposta.",
    "chave": "timtimcash-aprovacao-dezembro-2026-v1",
    "resumo_titulo": "Avaliação dos posts de dezembro de 2026 do timtimcash (proposta de 16/10/2026)",
    "largura_imagens": 720,
    "aprovar_todos": True,
    "notas": [
        ("Como avaliar", "Marque Aprovado, Reprovado ou Solicitar alteração em cada post e escreva o que quiser mudar. O botão “Aprovar todos os pendentes”, na barra do topo, marca de uma vez os que você ainda não avaliou. No fim, copie a avaliação e cole na conversa."),
        ("20 posts, todos às 10h", "Carrossel e Reel se alternam, sem dois Reels seguidos. Todo fim de semana tem post: domingos 06, 20 e 27 e sábado 12. Sem post em 24, 25 e 31/12. O mês segue o calendário do dinheiro: a 2ª parcela do 13º (até 20/12, que cai num domingo), o Natal, o fechamento do ano lá fora em 31/12 e as contas de janeiro."),
        ("Reels", "Como em novembro: cada Reel abre em movimento, com a pergunta e um número no primeiro segundo, dura de 18 a 22 segundos e tem capa própria para a grade. A exceção é o de Boas festas (22/12), de 12 segundos e sem número. Aqui os vídeos estão em qualidade reduzida e sem som; o que vai ao ar é 1080 × 1920."),
        ("Telas reais e conta fictícia", "Todas as telas foram capturadas no build 2026-10-16.1, na mesma conta fictícia de novembro: a 2ª parcela do 13º em 18/12, as compras de Natal, uma remessa de € 2.000 em 1º/12 e a carteira em dólar de outubro. Os câmbios do exemplo são as PTAX reais de 15/10/2026. Para IPVA e IPTU, os posts usam as regras de São Paulo como exemplo e pedem para conferir o calendário do seu estado e da sua cidade."),
        ("Fontes", "Lei, taxa, índice e definição vêm de fonte oficial, com a data de cada número: Planalto, Banco Central, IBGE, Receita Federal, B3, Assembleia Legislativa e Prefeitura de São Paulo. As citações entre aspas (IBGE Explica, Ranking do VET) foram conferidas no texto original."),
        ("Números que podem mudar até a publicação", "Quatro posts usam o dado mais recente de hoje e podem ganhar um número mais novo antes de ir ao ar: os juros médios de agosto de 2026 (10 e 11/12; o Banco Central publica os de outubro no fim de novembro), o IPCA de setembro (16/12; o de novembro sai por volta de 10/12) e as regras do IPVA de 2026 (07/12; o calendário de 2027 de São Paulo costuma sair em novembro). Se quiser, eu atualizo antes de agendar."),
        ("Capas e grade", "Os fundos alternam entre papel, tinta, verde suave e verde, com no máximo uma capa verde por semana (06, 12, 20, 22 e 30/12). Nenhuma capa fica ao lado nem em cima de outra do mesmo fundo, também na virada de novembro para dezembro. O post fixado, verde, fica no primeiro quadrado."),
        ("Para o site, fora dos posts", "No relatório em PDF (Exportar), os percentuais de Despesas por categoria saem com ponto (“30.1%”), e não com vírgula. No 20/12 o vídeo aproxima o cabeçalho e o botão “Imprimir / Salvar PDF”, sem mostrar esses percentuais."),
    ],
    "fontes": fontes,
    "grade_mes": {"titulo": "Prévia da grade do perfil", "legenda": "Como o perfil fica em 30/12",
                  "nota": "A grade mostra as capas em 3:4. O post fixado (“Comece por aqui”) fica no topo; o ícone de play marca os Reels. Depois de dezembro aparecem os últimos posts de novembro, da proposta anterior.",
                  "itens": itens},
}
