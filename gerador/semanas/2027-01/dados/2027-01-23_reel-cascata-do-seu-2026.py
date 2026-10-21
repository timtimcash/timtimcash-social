# -*- coding: utf-8 -*-
"""Sábado 23/01/2027 · Reel "Da receita ao resultado: o seu 2026 numa cascata" (produto: Relatórios; capa tinta). Equipe js.
Vídeo, capa e prévia gerados por equipes/js/reel_23.py (com assert nos números lidos da tela e dos dados do gráfico); telas capturadas
por equipes/js/captura_23.py no site build 2026-10-19.5, na conta de base (J/base_app, sem mudança), no celular (390 × 760 em escala 3),
relógio da página em 23/01/2027 10:00.
Interação real: Relatórios -> calendário do topo -> "Ano atual" -> "Aplicar" (Ano 2027) -> a faixa de atalhos deslizada até "Cascata" ->
seta "‹" (Ano 2026) -> atalho "Cascata" (a página rola até "Cascata do período · Da receita ao resultado · Ano 2026") -> um toque em cada
degrau; o balão do gráfico mostra: Receita +R$ 126.293,36; Casa −R$ 30.054,00; Mercado −R$ 19.113,60; Educação −R$ 17.400,00;
Transporte −R$ 13.281,49; Bares e restaurantes −R$ 7.408,62; Outras (8) −R$ 14.596,99; Resultado R$ 24.438,66 (os mesmos valores dos
dados do gráfico, Chart.getChart('rep-waterfall')). Despesas do ano: R$ 101.854,70 em 13 categorias ("Despesas por categoria").
O Diagnóstico de 2026, no topo da mesma tela, diz "Receita guardada 19,4%" (24.438,66 ÷ 126.293,36 = 19,35%).
Contas do resumo: Casa + Mercado + Educação = R$ 66.567,60 = 52,7% da receita ("mais da metade"); as outras 10 categorias (Transporte, Bares
e restaurantes e as 8 de "Outras (8)") = R$ 35.287,10; 66.567,60 + 35.287,10 + 24.438,66 = 126.293,36.
O gancho e a capa desenham a mesma cascata, na escala dos valores do site (degraus em coral, receita em verde, resultado em menta)."""

POST = {
    "pasta": "2027-01-23_reel-cascata-do-seu-2026",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "O seu 2026 numa cascata: em Relatórios, com o período Ano 2026, a Cascata do período desce da receita ao resultado, um degrau por categoria; os três maiores levaram mais da metade da receita",
    "pilar": "Produto (Relatórios) · balanço do ano",
    "data_longa": "sábado, 23 de janeiro de 2027",
    "data_curta": "sábado, 23/01/2027",
    "data_mockup": "23 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-23T10:00:00",
    "video": "saida/2027-01-23_reel-cascata-do-seu-2026/reel.mp4",
    "capa": "saida/2027-01-23_reel-cascata-do-seu-2026/capa.jpg",
    "previa": "saida/2027-01-23_reel-cascata-do-seu-2026/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · RELATÓRIOS · O seu 2026 numa cascata. · Uma cascata desenhada: a barra verde da receita (R$ 126.293), seis degraus em coral descendo e a barra menta do resultado (R$ 24.439).",
        "0 a 2,6 s · Gancho (tinta) · RELATÓRIOS · Da receita ao resultado: o seu 2026 numa cascata. · Desde o primeiro quadro, a barra da receita aparece cheia (R$ 126.293) e os degraus em coral vão saindo dela até a barra do resultado (R$ 24.439).",
        "2,9 a 5,6 s · Em Relatórios, escolha o Ano 2026 e toque em Cascata. · Tela real: anel no período (Ano 2027), toque na seta “‹” (Ano 2026, em anel), anel e toque no atalho Cascata.",
        "5,8 a 8,6 s · A receita do ano no alto. Cada degrau é uma categoria que saiu dela. · A Cascata do período (Ano 2026) de perto; um toque em cada degrau mostra o balão do site: Receita +R$ 126.293,36, Casa −R$ 30.054,00, Mercado −R$ 19.113,60.",
        "8,8 a 11,5 s · Casa, Mercado e Educação: os três maiores degraus. · Os toques seguem: Educação −R$ 17.400,00, Transporte −R$ 13.281,49, Bares e restaurantes −R$ 7.408,62, Outras (8) −R$ 14.596,99.",
        "11,7 a 14,0 s · No pé da cascata, o resultado: R$ 24.438,66, 19,4% da receita. · Toque no último degrau: Resultado R$ 24.438,66.",
        "14,2 a 17,2 s · Casa, Mercado e Educação levaram mais da metade da receita. · A receita do ano numa barra dividida: Casa R$ 30.054,00, Mercado R$ 19.113,60 e Educação R$ 17.400,00 (juntas, R$ 66.567,60), outras 10 categorias R$ 35.287,10 e o resultado R$ 24.438,66. · Os degraus mais altos mostram para onde o dinheiro escorre.",
        "17,3 a 20,0 s · Fechamento (verde) · Relatórios no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "O seu 2026 numa cascata: da receita ao resultado.\n\n"
        "Em Relatórios, escolha o período Ano 2026 e toque em Cascata. A receita do ano fica no alto, e cada degrau é uma categoria que "
        "saiu dela. No exemplo do vídeo, a receita foi de R$ 126.293,36; Casa levou R$ 30.054,00, Mercado R$ 19.113,60 e Educação "
        "R$ 17.400,00. No pé da cascata, o resultado: R$ 24.438,66, 19,4% da receita.\n\n"
        "Os três maiores degraus levaram mais da metade da receita (R$ 66.567,60). Os degraus mais altos mostram para onde o dinheiro "
        "escorre, e são o primeiro lugar para olhar ao planejar 2027.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#relatoriofinanceiro #financaspessoais #organizacaofinanceira #controlefinanceiro #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de janeiro, com 2026 fechado no site: é a hora de olhar o ano inteiro de uma vez antes de seguir com 2027. Sábado é dia de post mais leve e visual."),
        ("O que desperta interesse", "A cascata se desenhando no primeiro segundo: a receita do ano cheia, os degraus caindo e o resultado no pé, com os dois números na tela."),
        ("Benefício para o público", "A pessoa vê para onde foi a receita do ano, degrau a degrau, e descobre que três categorias levaram mais da metade: um ponto de partida concreto para o planejamento."),
        ("Como contribui para o perfil", "Mostra com tela real e toques um gráfico ainda inédito no perfil (a Cascata do período), com um ângulo diferente dos 5 números de 06/12 e da concentração de 26/11."),
    ],
    "alt": [
        "Reel de 20 segundos. Da receita ao resultado: o seu 2026 numa cascata. Uma barra verde mostra a receita do ano, R$ 126.293, e "
        "degraus em coral descem até a barra do resultado, R$ 24.439. Telas reais do timtimcash no celular, com dados de exemplo. Em "
        "Relatórios, um toque na seta muda o período para Ano 2026 e um toque no atalho Cascata abre a Cascata do período. Um toque em cada "
        "degrau mostra o valor: receita de R$ 126.293,36; Casa, R$ 30.054,00; Mercado, R$ 19.113,60; Educação, R$ 17.400,00; Transporte, "
        "R$ 13.281,49; Bares e restaurantes, R$ 7.408,62; outras 8 categorias, R$ 14.596,99; e o resultado, R$ 24.438,66, 19,4% da receita. "
        "Uma barra dividida mostra que Casa, Mercado e Educação levaram mais da metade da receita, R$ 66.567,60. Os degraus mais altos mostram "
        "para onde o dinheiro escorre. Relatórios no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-relatorios-4-ano-2027.jpg · Relatórios com o período Ano 2027 e a faixa de atalhos deslizada até Cascata (celular 390 × 760 em escala 3, build 2026-10-19.5, relógio da página em 23/01/2027 10:00) · 2,7 a 4,1 s",
        "telas/celular-relatorios-5-ano-2026.jpg · depois do toque na seta “‹”: Ano 2026, com o Diagnóstico de 2026 (Receita guardada 19,4%) · 4,1 a 5,1 s",
        "telas/celular-relatorios-6-cascata.jpg · depois do toque no atalho Cascata: “Cascata do período · Da receita ao resultado · Ano 2026” · 5,1 a 6,1 s",
        "telas/celular-relatorios-7-0-receita.jpg a celular-relatorios-7-7-resultado.jpg · a mesma tela depois de um toque em cada degrau, com o balão do site (Receita, Casa, Mercado, Educação, Transporte, Bares e restaurantes, Outras (8) e Resultado) · 6,1 a 14,4 s",
        "telas/celular-relatorios-1-janeiro.jpg, celular-relatorios-2-calendario.jpg e celular-relatorios-3-calendario-ano.jpg · os passos do período (Janeiro 2027, o calendário, “Ano atual”), guardados como registro · não aparecem no vídeo",
        "telas/caixas.json · posições medidas na captura (com a rolagem de cada foto), os dados do gráfico da cascata e o texto de cada balão, usados nos toques e nos assert do roteiro",
    ],
}
