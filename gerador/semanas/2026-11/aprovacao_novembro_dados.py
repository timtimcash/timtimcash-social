# -*- coding: utf-8 -*-
"""Novembro de 2026 inteiro para aprovação: os 20 posts novos de N/dados (10 carrosséis e 10 Reels).

python3 /home/claude/timtimcash-social/gerador/aprovacao.py aprovacao_novembro_dados.py saida aprovacao/novembro.html
"""
import glob, importlib.util, os

N = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/claude/timtimcash-social"
POSTS_REPO = os.path.join(REPO, "posts")
FUSO = "horário de Brasília (America/Sao_Paulo, UTC−3)"


def _mod(caminho):
    s = importlib.util.spec_from_file_location("m" + str(abs(hash(caminho))), caminho)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


CURTOS = {
    "2026-11-01_novembro-do-seu-dinheiro": "Novembro do seu dinheiro",
    "2026-11-04_reel-combustivel-em-2026": "Quanto foi de combustível?",
    "2026-11-05_ptax-o-dolar-do-banco-central": "PTAX: o dólar do Banco Central",
    "2026-11-06_reel-a-vista-ou-parcelado": "10% à vista ou 10x sem juros?",
    "2026-11-07_assinaturas-o-preco-por-ano": "Assinaturas: o preço por ano",
    "2026-11-09_reel-a-dre-da-sua-casa": "Empresa tem DRE. E a sua casa?",
    "2026-11-11_pagou-o-minimo-da-fatura": "Pagou o mínimo. E o resto?",
    "2026-11-12_reel-o-seu-cambio-medio": "Qual é o seu dólar?",
    "2026-11-13_black-friday-o-desconto-e-de-verdade": "Black Friday: o desconto é de verdade?",
    "2026-11-14_reel-metade-do-mes": "Metade do mês: quanto dá por dia?",
    "2026-11-16_iof-da-remessa": "IOF da remessa: 1,1% ou 3,5%?",
    "2026-11-18_reel-ate-o-mesmo-dia": "Até o mesmo dia",
    "2026-11-19_custo-fixo-quanto-ja-tem-dono": "Quanto do salário já tem dono?",
    "2026-11-22_reel-o-mapa-de-calor": "Seu ano tem meses quentes",
    "2026-11-23_50-30-20-no-seu-extrato": "50/30/20 no seu extrato",
    "2026-11-25_reel-atualizar-carteira": "Atualize a carteira em 30 segundos",
    "2026-11-26_tres-categorias-levam-dois-tercos": "3 categorias levam 2/3 do gasto",
    "2026-11-27_reel-black-friday-respira": "Black Friday: respira",
    "2026-11-28_resgate-quando-o-dinheiro-volta": "O dinheiro voltou. E o câmbio?",
    "2026-11-30_reel-ultimo-dia-da-primeira-parcela": "Hoje: último dia da 1ª parcela",
}

POSTS = []
for arq in sorted(glob.glob(os.path.join(N, "dados", "2026-11-*.py"))):
    p = dict(_mod(arq).POST)
    p.update(status_tipo="novo", status_atual="Novo")
    if p["tipo"] == "reel":
        for c in ("video", "capa", "previa"):
            p[c] = os.path.join(N, p[c])
    else:
        p["imagens_dir"] = os.path.join(N, "saida")
    POSTS.append(p)
POSTS.sort(key=lambda p: p["iso"])
for i, p in enumerate(POSTS, 1):
    p["n"] = i
    p["titulo_curto"] = CURTOS[p["pasta"]]
assert len(POSTS) == 20, len(POSTS)
assert sum(p["tipo"] == "reel" for p in POSTS) == 10


def _capa(p):
    return p["capa"] if p["tipo"] == "reel" else os.path.join(p["imagens_dir"], p["pasta"], "01.jpg")


# grade do perfil em 30/11: o fixado, novembro do mais novo para o mais antigo e o fim de outubro (já publicado)
OUTUBRO = [("30/10", "2026-10-30_reel-13-salario/capa.jpg", "reel"), ("29/10", "2026-10-29_cambio-efetivo/01.jpg", "carrossel"),
           ("27/10", "2026-10-27_reel-ocultar-valores/capa.jpg", "reel"), ("25/10", "2026-10-26_parcela-que-cabe-hoje/01.jpg", "carrossel"),
           ("23/10", "2026-10-23_sua-planilha-vem-junto/01.jpg", "carrossel"), ("22/10", "2026-10-22_reel-ritmo-do-retorno/capa.jpg", "reel")]
itens = [("fixado", os.path.join(POSTS_REPO, "2026-09-30_comece-por-aqui/01.jpg"), "fixado")]
itens += [(p["data_curta"].split(", ")[1][:5], _capa(p), p["tipo"]) for p in reversed(POSTS)]
itens += [(d, os.path.join(POSTS_REPO, c), t) for d, c, t in OUTUBRO]

fontes, vistos = [], set()
for p in POSTS:
    for t, u in p.get("fontes", []):
        if u not in vistos:
            vistos.add(u); fontes.append((t, u))

CONFIG = {
    "titulo_pagina": "Novembro no Instagram · timtimcash",
    "eyebrow": "Proposta para aprovação · enviada em 16/10/2026",
    "h1": "Novembro inteiro: 20 posts, 10 Reels",
    "sub": "Dez carrosséis e dez Reels, na ordem do mês, com o calendário e a prévia da grade do perfil. Nada é agendado antes da sua resposta.",
    "chave": "timtimcash-aprovacao-novembro-2026-v1",
    "resumo_titulo": "Avaliação dos posts de novembro de 2026 do timtimcash (proposta de 16/10/2026)",
    "largura_imagens": 720,
    "aprovar_todos": True,
    "notas": [
        ("Como avaliar", "Marque Aprovado, Reprovado ou Solicitar alteração em cada post e escreva o que quiser mudar. O botão “Aprovar todos os pendentes”, na barra do topo, marca de uma vez os que você ainda não avaliou. No fim, copie a avaliação e cole na conversa."),
        ("20 posts, todos às 10h", "Carrossel e Reel se alternam, sem dois Reels seguidos. Todo fim de semana tem post: domingos 01 e 22, sábados 07, 14 e 28. Sem post nos feriados de 02, 15 e 20/11. O limite do Metricool gratuito é de 20 posts por mês."),
        ("Reels novos", "Em outubro, o tempo médio assistido dos Reels foi de 3 segundos, e a capa parada no começo segurava pouco. Agora cada Reel abre em movimento, com a pergunta e um número no primeiro segundo, dura de 19 a 22 segundos e tem uma capa própria para a grade. Aqui os vídeos estão em qualidade reduzida e sem som, para o arquivo ficar leve; o que vai ao ar é 1080 × 1920. Vão sem música: se quiser trilha, me mande um arquivo livre de direitos."),
        ("Telas do site de hoje", "Todas as telas reais foram capturadas no build 2026-10-16.1, o que você mandou hoje, numa conta fictícia que segue a dos posts de outubro (setembro com R$ 9.960 de receita, as mesmas remessas em dólar). Os números de outubro e novembro da conta foram montados para as histórias dos posts e conferidos tela a tela."),
        ("Fontes", "Lei, taxa e dado do consumidor vêm de fonte oficial: Planalto, Banco Central e Procon-SP, com a data de cada número. Os de agosto de 2026 (rotativo e cheque especial) são os mais recentes do Banco Central hoje; se sair um dado mais novo antes da publicação, eu atualizo."),
        ("Capas e grade", "Os fundos alternam entre papel, tinta, verde suave e verde, com no máximo uma capa verde por semana (07, 13, 22 e 27/11). Além de nunca ficarem duas iguais lado a lado, agora também nunca ficam uma em cima da outra: como a grade tem 3 colunas, dois posts a 3 posições de distância ficam empilhados. Na primeira versão do mês, uma coluna inteira tinha capa em papel; troquei o fundo de quatro capas para quebrar isso. A exceção é o post fixado, verde e sempre no primeiro quadrado: por alguns dias, uma capa verde fica embaixo dele."),
    ],
    "fontes": fontes,
    "grade_mes": {"titulo": "Prévia da grade do perfil", "legenda": "Como o perfil fica em 30/11",
                  "nota": "A grade mostra as capas em 3:4. O post fixado (“Comece por aqui”) fica no topo; o ícone de play marca os Reels. Depois de novembro aparecem os últimos posts de outubro, já publicados.",
                  "itens": itens},
}
