# -*- coding: utf-8 -*-
"""Domingo 22/11/2026 · Reel "Seu ano tem meses quentes" (produto: Relatórios; capa verde). Equipe r2.
Vídeo, capa e prévia gerados por equipes/r2/reel_22.py; telas reais capturadas por equipes/r2/captura_22.py no site build 2026-10-16.1,
na conta de base (N/base_app, sem mudança), com o relógio em 22/11/2026 10:00, tudo pela interface: toque (ou clique) no mês do topo,
“De” 01/12/2025 e “Até” 30/11/2026 digitados e “Aplicar” (o período Personalizado mostra 12 meses no Mapa de calor; com um mês só,
o padrão, ele mostra 6). No computador, um clique na célula “Outras · jan”; no celular, toques na parte “Pontual” das barras.
Números da tela (conferidos no texto da captura, com assert no gerador): Mapa de calor, dez/25 a nov/26: Outras dez/25 1,1 mil,
jan 1,5 mil, jul 760; Mercado dez/25 1,8 mil; detalhe “Outras · janeiro · 16% das despesas do mês · R$ 1.509,80”.
Recorrentes vs pontuais: “Pontual · Dez/25 R$ 980,00” (Presentes de Natal, 19/12, Presentes e doações); “Pontual · Jan/26
R$ 1.390,00” (IPVA · parcela única R$ 1.180,00 e IPTU · 1ª parcela R$ 210,00, Impostos e Taxas); “Pontual · Jul/26 R$ 640,00”
(Hospedagem nas férias, 14/07, Viagem).
O gancho desenha um termômetro de quadradinhos por mês (desenho, não é tela): a altura segue o gasto total de cada mês na conta
(jan 9.420, jul 8.620 e dez 9.860 ficam acima da média de R$ 8,3 mil dos 13 meses de out/25 a out/26, o dado da Sazonalidade).
Observação: a grade do Mapa de calor do site usa um traço curto para célula sem gasto (Lazer e hobbies em set/26); ele só aparece
pequeno, no cartão inteiro, e fica fora dos trechos com zoom."""

POST = {
    "pasta": "2026-11-22_reel-o-mapa-de-calor",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "Seu ano tem meses quentes: o Mapa de calor de Relatórios mostra 12 meses de gasto por categoria, e Recorrentes vs pontuais mostra o que pesou em cada mês quente (presentes em dezembro, impostos em janeiro, férias em julho, na conta de exemplo)",
    "pilar": "Produto (Relatórios)",
    "data_longa": "domingo, 22 de novembro de 2026",
    "data_curta": "domingo, 22/11/2026",
    "data_mockup": "22 de novembro",
    "hora": "10h00",
    "iso": "2026-11-22T10:00:00",
    "video": "saida/2026-11-22_reel-o-mapa-de-calor/reel.mp4",
    "capa": "saida/2026-11-22_reel-o-mapa-de-calor/capa.jpg",
    "previa": "saida/2026-11-22_reel-o-mapa-de-calor/previa.mp4",
    "slides": [
        "Capa da grade (verde, logotipo negativo) · RELATÓRIOS · Seu ano tem meses quentes · Grade de 6 x 4 quadrados em tons de verde escuro, menta e branco, com o quadrado branco do canto destacado por um contorno; sem coral.",
        "0 a 2,5 s · Gancho (tinta) · RELATÓRIOS · Seu ano tem meses quentes. · Desde o primeiro quadro, um termômetro de quadradinhos por mês, de janeiro a dezembro, acende de baixo para cima, do creme ao coral; janeiro, julho e dezembro chegam ao coral (a altura segue o gasto total de cada mês na conta de exemplo).",
        "2,5 a 5,1 s · No Mapa de calor, cada quadrado é uma categoria num mês. · Tela real do Mapa de calor no computador, período de 1 dez 2025 a 30 nov 2026: primeiro o cartão inteiro, com os 12 meses; depois o zoom de dezembro a abril. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "5,2 a 7,9 s · Dezembro, janeiro e julho: mais quentes. · Anéis na coluna dez/25 e na célula Outras · jan (1,5 mil, a célula escolhida); panorâmica até julho, com anel em Outras · jul (760).",
        "8,2 a 10,5 s · Dezembro: presentes. · Tela real de “Recorrentes vs pontuais” no celular, no mesmo período: toque na parte Pontual da barra de Dez/25; a lista mostra “Pontual · Dez/25 R$ 980,00” e “Presentes de Natal”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "10,6 a 12,5 s · Janeiro: impostos. · Toque em Jan/26: “Pontual · Jan/26 R$ 1.390,00”, com “IPVA · parcela única” R$ 1.180,00 e “IPTU · 1ª parcela” R$ 210,00, em Impostos e Taxas.",
        "12,6 a 14,5 s · Julho: férias. · Toque em Jul/26: “Pontual · Jul/26 R$ 640,00”, com “Hospedagem nas férias”, em Viagem.",
        "14,5 a 17,6 s · Os meses caros se repetem. Dá para ver antes. · Uma folha em tinta sobe com o calendário de 2027: jan (impostos), jul (férias) e dez (presentes) acendem em coral.",
        "17,6 a 20,4 s · Fechamento (verde) · Relatórios no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Seu ano tem meses quentes. Dá para saber quais.\n\n"
        "No exemplo do vídeo, o Mapa de calor de Relatórios mostra 12 meses de gasto por categoria, de dezembro de 2025 a novembro de 2026. "
        "Dezembro, janeiro e julho esquentam.\n\n"
        "Em Recorrentes vs pontuais, um toque na barra do mês mostra o que fugiu da rotina: em dezembro, R$ 980 de presentes de Natal; "
        "em janeiro, R$ 1.390 de IPVA e IPTU; em julho, R$ 640 de hospedagem nas férias.\n\n"
        "Presentes, impostos do começo do ano, férias: esses gastos voltam todo ano. Anote os seus antes de 2027 começar.\n\n"
        "Para ver 12 meses no Mapa de calor, escolha em Relatórios um período personalizado de um ano.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#planejamentofinanceiro #controlefinanceiro #financaspessoais #organizacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Domingo, 22 de novembro, a cinco semanas de 2027: dá tempo de olhar o ano que passou e separar dinheiro para os meses que pesam, como Natal, impostos de janeiro e férias."),
        ("O que desperta interesse", "O gancho em tinta acende um termômetro de quadradinhos por mês, do creme ao coral, e três meses ficam quentes antes de qualquer explicação. Depois, cada toque na tela revela o motivo."),
        ("Benefício para o público", "A pessoa encontra os seus meses caros no próprio histórico e passa a planejá-los com antecedência, em vez de ser surpreendida todo ano."),
        ("Como contribui para o perfil", "Apresenta dois painéis de Relatórios com tela real (o Mapa de calor com 12 meses e Recorrentes vs pontuais) e fecha com uma ideia útil para a virada do ano."),
    ],
    "alt": [
        "Reel de 20 segundos. Seu ano tem meses quentes. Em fundo escuro, um termômetro de quadradinhos para cada mês, de janeiro a dezembro, acende do creme ao coral; janeiro, julho e dezembro chegam ao coral. "
        "Depois, a tela real do Mapa de calor do timtimcash no computador, com dados de exemplo, de dezembro de 2025 a novembro de 2026: cada quadrado é uma categoria num mês. A câmera se aproxima e destaca a coluna de dezembro, "
        "a célula Outras de janeiro e a de julho. Em seguida, a tela real de Recorrentes vs pontuais no celular, com toques nas barras dos meses: dezembro, presentes de Natal, R$ 980; janeiro, IPVA e IPTU, R$ 1.390; "
        "julho, hospedagem nas férias, R$ 640. Os meses caros se repetem. Dá para ver antes: um calendário de 2027 com janeiro, julho e dezembro em destaque. Relatórios no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/computador-mapa-de-calor-12-meses.jpg · Relatórios › Mapa de calor no computador (1440 × 900, escala 3), site build 2026-10-16.1, conta de base, relógio em 22/11/2026 10:00, período Personalizado de 01/12/2025 a 30/11/2026, depois de um clique em Outras · jan · 2,5 a 7,9 s",
        "telas/celular-recorrentes-pontuais-0.jpg · Relatórios › Recorrentes vs pontuais no celular (390 px CSS, escala 3), mesmo relógio e período, antes dos toques · 7,9 a 9,6 s",
        "telas/celular-recorrentes-pontuais-dez.jpg, celular-recorrentes-pontuais-jan.jpg e celular-recorrentes-pontuais-jul.jpg · o mesmo painel depois dos toques na parte Pontual de Dez/25, Jan/26 e Jul/26 · 9,6 a 14,5 s",
        "telas/caixas.json · caixas dos anéis e dos toques (px CSS) e os textos da tela usados na conferência dos números",
    ],
}
