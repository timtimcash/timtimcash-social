# -*- coding: utf-8 -*-
"""Dados do post fixado "Comece por aqui" para o HTML de aprovação e para o agendamento."""

FUSO = "horário de Brasília (America/Sao_Paulo, UTC−3)"

CONFIG = {
    "saida": "timtimcash-post-fixado-telas-reais.html",
    "titulo_pagina": "Post fixado · timtimcash",
    "eyebrow": "Proposta para aprovação · enviada em 30/09/2026",
    "h1": "O post de apresentação, para fixar no perfil",
    "sub": "Um carrossel “Comece por aqui” para quem chega ao @timtimcashcom entender o que é o timtimcash e o que ele tem de diferente, agora com telas reais do sistema. Nada é agendado antes da sua resposta.",
    "chave": "timtimcash-aprovacao-fixado-2026-10-01-v2",
    "resumo_titulo": "Avaliação do post fixado do timtimcash (proposta de 30/09/2026, versão com telas reais)",
    "notas": [
        ("Telas reais", "Os slides 2, 4, 5 e 6 mostram telas do próprio timtimcash, abertas numa conta fictícia com os mesmos números de exemplo dos posts. Nenhum dado seu aparece, e o post avisa que os dados são de exemplo."),
        ("Como avaliar", "Escolha uma opção e, se quiser, escreva comentários. Tudo fica salvo neste navegador, mesmo se você recarregar a página. No fim, copie a avaliação e cole na conversa."),
        ("Fixar no perfil", "O Metricool agenda e publica, mas não fixa. Depois que o post sair, fixar é um toque no app do Instagram: nos três pontinhos do post, “Fixar no seu perfil”. Cabem até 3 posts fixados."),
        ("Data proposta", "Quinta 01/10, às 10h: é o único dia sem post nesta semana e a melhor hora de quinta no Metricool. Se preferir no ar ainda hoje, o melhor horário da tarde é 18h. Com ele, outubro fica com 6 posts agendados."),
    ],
    "fontes": [
        ("Instagram · Fixar um post no topo do perfil", "https://help.instagram.com/318456537074409/"),
        ("Metricool · Como fixar uma publicação no Instagram", "https://metricool.com/pin-post-instagram/"),
        ("The Verge · Grade do perfil em retângulos (17/01/2025)", "https://www.theverge.com/2025/1/17/24346304/instagram-profile-grids-rectangles-squares"),
        ("Kapwing · Nova grade 3:4 e o corte das imagens 4:5", "https://www.kapwing.com/resources/instagrams-new-grid-layout-size-and-dimensions-2025/"),
    ],
}

POSTS = [{
    "n": 1,
    "pasta": "2026-09-30_comece-por-aqui",
    "plataforma": "Instagram",
    "formato": "Carrossel de 8 imagens no feed (1080 × 1350, 4:5), para fixar no topo do perfil",
    "formato_curto": "Carrossel de 8 imagens · post fixado",
    "tema": "Comece por aqui: o que é o timtimcash, o que ele tem de diferente e como começar",
    "pilar": "Apresentação · post fixado",
    "data_longa": "quinta-feira, 1º de outubro de 2026",
    "data_curta": "quinta-feira, 01/10/2026",
    "data_mockup": "1 de outubro",
    "hora": "10h00",
    "iso": "2026-10-01T10:00:00",
    "slides": [
        "Capa (fundo verde) · BOAS-VINDAS · Comece por aqui. · O que é o timtimcash, o que ele tem de diferente e como começar. · Sumário: 2 O que é, 3 O que ele responde, 4 Seu dinheiro lá fora, 5 Sua planilha vem junto, 6 Sem senha do banco, 7 Como começar.",
        "O QUE É · Um site que organiza o seu dinheiro. · Você lança ou importa o que entra e sai. Ele organiza, calcula e mostra. · Telas reais da Visão geral no navegador do computador e no celular (endereço timtimcash.com), com dados de exemplo: patrimônio R$ 104.180, receitas R$ 9.960,00, despesas R$ 7.780,00, sobrou R$ 2.180,00. · Nota: Telas reais do timtimcash, com dados de exemplo.",
        "O QUE ELE RESPONDE · Quatro perguntas, num lugar só. · Para onde o dinheiro está indo? (categorias, orçamentos e relatórios) · Quanto sobra no fim do mês? (visão geral, pendentes e comparação) · Como vão ser os próximos meses? (simulação de fluxo futuro, até 5 anos à frente) · Quanto rendeu lá fora, em reais? (remessas e investimentos no exterior, em destaque).",
        "INVESTIMENTOS LÁ FORA · Quanto rendeu de verdade, em dólar e em real. · Cada remessa na sua data, com a PTAX do Banco Central. Rendimento e câmbio separados. · Tela real de Remessas ao exterior, “De onde veio o resultado em reais”: você enviou R$ 60.000, rendimento +R$ 6.600, efeito do câmbio +R$ 6.000, hoje R$ 72.600; os investimentos renderam +US$ 1.200,00 (+10,0%) e sobrou +R$ 12.600,00 (+21,0%). · Nota: Tela real do timtimcash, com dados de exemplo, sem IOF e tarifas.",
        "SEU HISTÓRICO VEM JUNTO · Já usa planilha? Ela vem junto. · Importe a planilha (.xlsx, .csv) ou o extrato do banco (.ofx), com as categorias já sugeridas. · Tela real “Revisar importação” de um extrato .ofx: 3 de 3 linhas com categoria sugerida pelo nome do estabelecimento (Supermercado da Vila em Mercado, Posto Avenida em Transporte, Farmácia São José em Saúde). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "PRIVACIDADE · Sem senha do banco. Sem propaganda. · O timtimcash não se conecta à sua conta bancária. E um toque no olho esconde os valores da tela. · Duas telas reais da Visão geral no celular: “Valores à mostra” (patrimônio R$ 104.180) e “Um toque e eles somem” (valores escondidos, com o olho em destaque).",
        "COMO COMEÇAR · Três passos e o seu mês aparece. · 1 Acesse timtimcash.com, pelo navegador, no computador ou no celular. · 2 Crie sua conta, com nome, e-mail e senha. · 3 Adicione seu banco ou carteira; depois importe o extrato ou lance à mão.",
        "Fechamento (fundo verde) · Logotipo vertical · Seu dinheiro, com a clareza que ele merece. · Gratuito para o controle financeiro. No computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Novo por aqui? Este é o post para começar.\n\n"
        "O timtimcash é um site de finanças pessoais. Você lança ou importa o que entra e sai, e ele mostra para onde o dinheiro está indo, "
        "quanto sobra no fim do mês, como vão ser os próximos meses e quanto seus investimentos lá fora renderam de verdade.\n\n"
        "O que ele tem de diferente:\n"
        "· Investimentos no exterior em dólar e em real, remessa por remessa, com a cotação PTAX do Banco Central\n"
        "· A sua planilha (.xlsx ou .csv) e o extrato do banco (.ofx) vêm junto\n"
        "· Nenhuma conexão com a sua conta bancária e nenhuma propaganda\n\n"
        "Gratuito para o controle financeiro. Funciona no navegador, no computador ou no celular.\n\n"
        "Toda semana tem post novo por aqui: finanças pessoais na prática, o timtimcash em ação e investimento no exterior explicado em reais. "
        "Siga o perfil para acompanhar.\n\n"
        "Comece pelo link na bio: timtimcash.com\n\n"
        "#financaspessoais #controlefinanceiro #organizacaofinanceira #investimentonoexterior #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "O perfil passou a publicar quase todo dia e já recebe visitas de quem vê os posts. Quem chega ao perfil decide em poucos segundos se segue, e o post fixado fica no topo da grade, o primeiro lugar que essa pessoa olha. Quinta 01/10 é o único dia sem post nesta semana, e 10h tem a melhor pontuação de quinta na análise de melhor horário do Metricool."),
        ("O que desperta interesse", "A capa diz exatamente o que o post entrega (“Comece por aqui”) e traz um sumário, que convida a deslizar. Por dentro, as telas são reais: a pessoa vê o sistema como ele é, no computador e no celular, o que passa mais confiança do que qualquer ilustração. Na grade do perfil, o título continua legível mesmo na miniatura."),
        ("Benefício para o público", "Em 8 telas, a pessoa entende o que é o site, as quatro perguntas que ele responde, os três diferenciais (investimentos lá fora medidos em reais, planilha e extrato que vêm junto, nenhuma senha de banco) e os três passos para começar, sem precisar abrir o site para descobrir."),
        ("Como contribui para o perfil", "Converte visita em seguidor e em cadastro, e fica como porta de entrada permanente. Segue o plano de tração: o exterior é o corte, quem já vive de planilha é o segundo público, e não pedir a senha do banco vira razão para experimentar. Também responde de uma vez as dúvidas que se repetiriam nos comentários."),
    ],
    "alt": [
        "Boas-vindas. Comece por aqui. O que é o timtimcash, o que ele tem de diferente e como começar. Sumário: 2, O que é; 3, O que ele responde; 4, Seu dinheiro lá fora; 5, Sua planilha vem junto; 6, Sem senha do banco; 7, Como começar.",
        "O que é. Um site que organiza o seu dinheiro. Você lança ou importa o que entra e sai. Ele organiza, calcula e mostra. Telas reais da Visão geral do timtimcash no navegador do computador e no celular, com dados de exemplo: patrimônio de R$ 104.180, receitas de R$ 9.960,00, despesas de R$ 7.780,00 e R$ 2.180,00 de sobra no mês.",
        "O que ele responde. Quatro perguntas, num lugar só. Para onde o dinheiro está indo? Categorias, orçamentos e relatórios. Quanto sobra no fim do mês? Visão geral, pendentes e comparação. Como vão ser os próximos meses? Simulação de fluxo futuro, até 5 anos à frente. Quanto rendeu lá fora, em reais? Remessas e investimentos no exterior.",
        "Investimentos lá fora. Quanto rendeu de verdade, em dólar e em real. Cada remessa na sua data, com a PTAX do Banco Central. Rendimento e câmbio separados. Tela real da seção Remessas ao exterior, com dados de exemplo: de onde veio o resultado em reais. Você enviou R$ 60.000, o rendimento somou R$ 6.600, o efeito do câmbio somou R$ 6.000 e hoje são R$ 72.600. Os investimentos renderam 10% em dólar e o resultado em reais foi de 21%. Sem IOF e tarifas.",
        "Seu histórico vem junto. Já usa planilha? Ela vem junto. Importe a planilha (.xlsx, .csv) ou o extrato do banco (.ofx), com as categorias já sugeridas. Tela real da revisão da importação de um extrato, com dados de exemplo: as 3 linhas vieram com categoria sugerida pelo nome do estabelecimento, Supermercado da Vila em Mercado, Posto Avenida em Transporte e Farmácia São José em Saúde.",
        "Privacidade. Sem senha do banco. Sem propaganda. O timtimcash não se conecta à sua conta bancária. E um toque no olho esconde os valores da tela. Duas telas reais da Visão geral no celular, com dados de exemplo: à esquerda os valores à mostra, com patrimônio de R$ 104.180; à direita, depois de tocar no olho, os valores aparecem escondidos.",
        "Como começar. Três passos e o seu mês aparece. Passo 1: acesse timtimcash.com, pelo navegador, no computador ou no celular. Passo 2: crie sua conta, com nome, e-mail e senha. Passo 3: adicione seu banco ou carteira e depois importe o extrato ou lance à mão.",
        "Logotipo do timtimcash. Seu dinheiro, com a clareza que ele merece. Gratuito para o controle financeiro. No computador ou no celular. Link na bio.",
    ],
    # grade do perfil como fica no sábado 03/10, com este post fixado no topo
    "grade_titulo": "Prévia no perfil · fixado no topo",
    "grade_legenda": "Como o perfil fica no sábado, 03/10",
    "grade_nota": "O título da capa continua legível na miniatura.",
    "grade": [
        ("fixado", None),
        ("03/10", "posts/2026-10-03_outubro-comecou/01.jpg"),
        ("02/10", "posts/2026-10-02_rendeu-em-dolar-e-em-reais/01.jpg"),
        ("30/09", "posts/2026-09-30_hoje-o-mes-fecha/01.jpg"),
        ("29/09", "posts/2026-09-29_conheca-o-timtimcash/01.jpg"),
    ],
}]
