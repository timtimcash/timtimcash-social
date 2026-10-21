# -*- coding: utf-8 -*-
"""Sábado 02/01/2027 · carrossel "2027 começa organizado" (abertura da série "Comece 2027", capa tinta). Equipe ja.
Artes: saida/2027-01-02_comece-2027-organizado/01.jpg a 07.jpg, geradas por equipes/ja/posts.py (post_comece), com o selo da
série de equipes/ja/selo_comece2027.py (quadrado na tinta, número em menta, quatro tracinhos do caminho).
Datas dos passos (pauta, conferidas por assert em posts.py): passo 1 em 04/01 (segunda), passo 2 em 10/01 (domingo), passo 3 em
14/01 (quinta), passo 4 em 18/01 (segunda) e a revisão de sábado em 30/01. Os posts dos passos não saem um por semana (04, 10, 14
e 18/01), por isso o slide 2 e a legenda dizem "um de cada vez", e não "um por semana", como estava na pauta.
Números das telas (conta de base, build 2026-10-19.5, conferidos por assert em posts.py):
- 04/01: Patrimônio consolidado R$ 112.730,86 = Banco na Europa R$ 11.525,40 + Conta corrente R$ 18.230,86 + Corretora no
  exterior R$ 60.000,00 + Reserva R$ 22.974,60;
- 10/01: Por categoria, Despesas R$ 4.820,00 em 6 categorias (Casa 2.300,00; Educação 1.450,00; Mercado 402,30; Transporte
  392,00; Bares e restaurantes 212,50; Saúde 63,20);
- 14/01 (cópia sem limites, ver equipes/ja/<cópia>/variantes.py): "Comece pela sua média dos últimos 12 meses": Casa R$ 2.600,
  Mercado R$ 1.600, Educação R$ 1.500, Transporte R$ 1.200, Bares e restaurantes R$ 700, Lazer e hobbies R$ 370 e mais 7;
- 18/01: Simulação futura › Cenário base › "E se…" (Receita −10%, Despesa +10%, Perde a maior renda, Inflação 5% a.a., Outro
  valor), sem aplicar nenhum teste (os testes ficam para o Reel de 18/01, equipe js).
Sem fato externo (lei, taxa ou estudo)."""

POST = {
    "pasta": "2027-01-02_comece-2027-organizado",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Abertura da série Comece 2027: os 4 passos de janeiro para organizar o dinheiro no timtimcash (o retrato, o caminho, os limites e a rota), o dia do post de cada um e a revisão de sábado que fecha a série",
    "pilar": "Campanha de janeiro · produto e hábito",
    "data_longa": "sábado, 2 de janeiro de 2027",
    "data_curta": "sábado, 02/01/2027",
    "data_mockup": "2 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-02T10:00:00",
    "slides": [
        "Capa (fundo tinta) · COMECE 2027 · 2027 começa organizado. · Os 4 selos da série numa trilha pontilhada que sobe da esquerda para a direita: quadrados arredondados com os números 1, 2, 3 e 4 em menta e, embaixo, O retrato, O caminho, Os limites e A rota.",
        "A SÉRIE DE JANEIRO · Um passo de cada vez. · Cada passo sai num post: o que fazer e onde fica no site. · Agenda de janeiro de 2027 com o dia do post: 04 seg, Passo 1 · O retrato, Quanto você tem?; 10 dom, Passo 2 · O caminho, Para onde vai?; 14 qui, Passo 3 · Os limites, Quanto cabe?; 18 seg, Passo 4 · A rota, E se 2027 apertar?; 30 sáb, Revisão de sábado, 5 minutos por semana. Cada linha com o selo do passo (a última, com um ícone de revisão).",
        "COMECE 2027 · PASSO 1 DE 4 · selo 1 · O retrato · Quanto você tem? · Em Contas e carteiras, cadastre cada conta com o saldo de hoje. O Patrimônio consolidado soma tudo. · Tela real de Contas e carteiras no celular (04/01/2027): Patrimônio consolidado R$ 112.730,86; Banco na Europa R$ 11.525,40; Conta corrente R$ 18.230,86; Corretora no exterior R$ 60.000,00; Reserva R$ 22.974,60; botão Nova conta. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "COMECE 2027 · PASSO 2 DE 4 · selo 2 · O caminho · Para onde vai? · Lance cada gasto com a categoria. Na Visão geral, o painel Por categoria mostra para onde foi. · Tela real da Visão geral no celular (10/01/2027): Por categoria, Despesas do período, a rosca com R$ 4.820,00 em 6 categorias. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "COMECE 2027 · PASSO 3 DE 4 · selo 3 · Os limites · Quanto cabe? · Em Orçamentos, dê um limite a cada categoria. Comece pela sua média. · Tela real de Orçamentos no celular (14/01/2027, numa cópia da conta sem limites): Comece pela sua média dos últimos 12 meses, arredondada para cima; Casa R$ 2.600, Mercado R$ 1.600, Educação R$ 1.500, Transporte R$ 1.200, Bares e restaurantes R$ 700, Lazer e hobbies R$ 370 e mais 7 categorias; Usar estes limites; Definir do zero. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "COMECE 2027 · PASSO 4 DE 4 · selo 4 · A rota · E se 2027 apertar? · Na Simulação futura, o E se… testa um susto sobre o cenário, sem mudar nada. · Tela real do painel E se… no celular (18/01/2027): Testa um susto sobre o cenário, sem alterar nada; Receita −10%, Despesa +10%, Perde a maior renda, Inflação 5% a.a., Outro valor. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Comece hoje: crie sua conta com nome, e-mail e senha. · Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "2027 começa organizado: 4 passos, um de cada vez.\n\n"
        "Em janeiro, a série Comece 2027 mostra como pôr o seu dinheiro em ordem no timtimcash, um passo por post:\n"
        "1 · O retrato (04/01): quanto você tem, somando todas as contas.\n"
        "2 · O caminho (10/01): para onde vai o dinheiro, por categoria.\n"
        "3 · Os limites (14/01): quanto cabe em cada categoria, a partir da sua média.\n"
        "4 · A rota (18/01): e se 2027 apertar? Um teste na Simulação futura, sem mudar nada.\n"
        "Em 30/01, a revisão de sábado fecha a série.\n\n"
        "Salve este post e siga o perfil para fazer junto. Comece hoje: crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#organizacaofinanceira #controlefinanceiro #financaspessoais #anonovo #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "O primeiro sábado do ano é quando mais gente decide se organizar. Abrir a série no dia 2 dá um roteiro para essa vontade antes da primeira semana útil, com data marcada para cada passo."),
        ("O que desperta interesse", "A promessa de um caminho curto e completo (4 passos, cada um com uma pergunta simples) e uma capa que se lê como uma escada, com o selo que vai voltar em cada post da série."),
        ("Benefício para o público", "Sabe o que fazer em cada passo e onde fica no site, vê as telas reais antes de começar e pode salvar a agenda para seguir no próprio ritmo."),
        ("Como contribui para o perfil", "Lança a campanha de janeiro e cria uma série reconhecível na grade (o sobretítulo COMECE 2027 · PASSO N DE 4 e o selo do passo), que puxa os posts de 04, 10, 14 e 18/01 e a revisão de 30/01."),
    ],
    "alt": [
        "Comece 2027. 2027 começa organizado. Quatro quadrados escuros numa trilha pontilhada que sobe, com os números 1, 2, 3 e 4 em verde-menta e os nomes dos passos: O retrato, O caminho, Os limites e A rota.",
        "A série de janeiro: um passo de cada vez. Cada passo sai num post, com o que fazer e onde fica no site. Agenda de janeiro de 2027: dia 4, segunda, passo 1, O retrato, quanto você tem; dia 10, domingo, passo 2, O caminho, para onde vai; dia 14, quinta, passo 3, Os limites, quanto cabe; dia 18, segunda, passo 4, A rota, e se 2027 apertar; dia 30, sábado, revisão de sábado, 5 minutos por semana.",
        "Passo 1 de 4, O retrato: quanto você tem? Em Contas e carteiras, cadastre cada conta com o saldo de hoje; o Patrimônio consolidado soma tudo. Tela real no celular, com dados de exemplo: patrimônio consolidado de R$ 112.730,86 em quatro contas, Banco na Europa, Conta corrente, Corretora no exterior e Reserva, e o botão Nova conta.",
        "Passo 2 de 4, O caminho: para onde vai? Lance cada gasto com a categoria; na Visão geral, o painel Por categoria mostra para onde foi. Tela real no celular, com dados de exemplo: gráfico de rosca com despesas de R$ 4.820,00 em seis categorias.",
        "Passo 3 de 4, Os limites: quanto cabe? Em Orçamentos, dê um limite a cada categoria, começando pela sua média. Tela real no celular, com dados de exemplo: o quadro Comece pela sua média dos últimos 12 meses, com Casa R$ 2.600, Mercado R$ 1.600, Educação R$ 1.500, Transporte R$ 1.200, Bares e restaurantes R$ 700 e Lazer e hobbies R$ 370, e os botões Usar estes limites e Definir do zero.",
        "Passo 4 de 4, A rota: e se 2027 apertar? Na Simulação futura, o E se testa um susto sobre o cenário, sem mudar nada. Tela real no celular, com dados de exemplo: os botões Receita menos 10%, Despesa mais 10%, Perde a maior renda, Inflação 5% ao ano e Outro valor.",
        "Comece hoje: crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-contas-e-carteiras-04-01.png · Menu › “Contas e carteiras” no celular, relógio em 04/01/2027 10:00, conta de base (390 × 1300 em escala 3): “4 contas · todas no total do patrimônio”, Patrimônio consolidado R$ 112.730,86 e as 4 contas · slide 3 (do patrimônio consolidado ao botão Nova conta)",
        "telas/celular-visao-geral-10-01.png · Visão geral (Realizado, Janeiro 2027) no celular, relógio em 10/01/2027 10:00, conta de base (390 × 3000 em escala 3) · slide 4 (o painel Por categoria, da cabeça ao fim da rosca)",
        "telas/celular-orcamentos-sem-limites-14-01.png · Orçamentos no celular, relógio em 14/01/2027 10:00, numa cópia da conta sem nenhum limite (390 × 1000 em escala 3): “Sem limites definidos” e o quadro “Comece pela sua média dos últimos 12 meses” · slide 5 (o quadro inteiro)",
        "telas/celular-simulacao-cenario-base-18-01.png · Simulação futura › “Cenário base” no celular, relógio em 18/01/2027 10:00, conta de base (390 × 2700 em escala 3), sem aplicar teste · slide 6 (o painel “E se…”)",
    ],
}
