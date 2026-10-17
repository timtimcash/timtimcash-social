# -*- coding: utf-8 -*-
"""Quarta 09/12/2026 · Reel "A jornada: sua história lá fora" (investimento no exterior; capa tinta, destaque menta). Equipe dr1.
Vídeo, capa e prévia gerados por equipes/dr1/reel_09.py; telas reais capturadas por equipes/dr1/capturas/captura09.py no site build
2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular (390 px CSS, escala 3), com o relógio em 09/12/2026 10:00:
Remessas ao exterior, aba USD (a que abre), numa foto alta (390 × 2000 px CSS) para a panorâmica, e "Ritmo do retorno" com toque em "ao ano".
Números da tela (assert no gerador): "US$13.310 na carteira hoje · +US$ 1.310,00 +10,9% em US$ · +R$ 7.235,46 +12,1% em R$";
"A jornada, desde jul/23" (degrau, trajetória tracejada e o ponto "US$ 13.310 · enviados: US$ 12.000"); marcos "Primeira remessa
12/07/2023 · 3 anos atrás", "Envios 3 · a cada 14 meses, em média", "Maior envio 4.000,00 · 12/07/2023", "Média por envio 4.000,00";
"Ritmo do retorno", ao ano: "3,6% na moeda" e "4,0% em reais".
O gráfico animado da abertura é desenhado com os mesmos dados e a mesma lógica do cartão do site: degraus nas datas reais das 3 remessas
(12/07/2023, 14/03/2024 e 18/04/2024, US$ 4.000 cada) e a trajetória na taxa constante que leva as remessas ao valor informado em
30/11/2026 (US$ 13.310); a taxa calculada no gerador (assert) bate com os 3,6% ao ano da tela."""

POST = {
    "pasta": "2026-12-09_reel-a-jornada-la-fora",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 18 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 18 s",
    "tema": "A jornada: sua história lá fora. A linha do tempo das remessas da conta de exemplo, de jul/23 a dez/26: os degraus do que foi enviado (US$ 12.000), a trajetória na taxa medida (3,6% ao ano em dólar) e o valor de hoje (US$ 13.310), com o cartão “A jornada” de Remessas",
    "pilar": "Investimento no exterior (Remessas: “A jornada”)",
    "data_longa": "quarta-feira, 9 de dezembro de 2026",
    "data_curta": "quarta-feira, 09/12/2026",
    "data_mockup": "9 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-09T10:00:00",
    "video": "saida/2026-12-09_reel-a-jornada-la-fora/reel.mp4",
    "capa": "saida/2026-12-09_reel-a-jornada-la-fora/capa.jpg",
    "previa": "saida/2026-12-09_reel-a-jornada-la-fora/previa.mp4",
    "slides": [
        "Capa da grade (tinta, logotipo de fundo escuro) · REMESSAS · A JORNADA · Sua história lá fora (“lá fora” em menta) · Uma linha do tempo em menta, grossa, com três degraus subindo da esquerda para a direita e um ponto em cada degrau.",
        "0 a 2,8 s · Gancho (tinta) · Sua história lá fora começou em jul/23. · Desde o primeiro quadro, o gráfico se desenha (eixos de 2023 a 2026, em mil US$) e o primeiro degrau sobe: US$ 4.000, 12/07/2023.",
        "2,8 a 5,6 s · Mais dois envios em 2024: US$ 12.000 ao todo. · Os degraus de março e abril de 2024 sobem e a linha segue até dez/26: “US$ 12.000 enviados · mar/24 e abr/24”.",
        "5,6 a 8,6 s · A linha tracejada é o ritmo: 3,6% ao ano, em dólar. · A trajetória tracejada (a taxa medida, como no site) se desenha por cima dos degraus até o ponto verde “US$ 13.310 · informado em 30/11/2026”; uma chave em menta marca a diferença: +US$ 1.310.",
        "8,6 a 11,6 s · Em Remessas, hoje: US$ 13.310, +10,9% em dólar. · Tela real de Remessas no celular (aba USD): “US$13.310 na carteira hoje”, com anel em “+US$ 1.310,00 +10,9% em US$”; logo abaixo, “+R$ 7.235,46 +12,1% em R$”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "11,6 a 15,4 s · “A jornada” guarda os marcos: a primeira, o maior envio, o ritmo. · A tela desce até o cartão “A jornada, desde jul/23” (o degrau, o tracejado e o ponto verde do site); os marcos saltam da tela, ampliados, com anel em “Primeira remessa 12/07/2023, 3 anos atrás” e depois em “Envios 3, a cada 14 meses, em média”; ao lado, “Maior envio 4.000,00” e “Média por envio 4.000,00”.",
        "15,4 a 18,1 s · Fechamento (verde) · Remessas no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Sua história lá fora cabe num gráfico.\n\n"
        "No exemplo do vídeo, a primeira remessa foi em 12/07/2023: US$ 4.000. Vieram mais duas em 2024, e o total enviado chegou a US$ 12.000. Hoje a carteira tem US$ 13.310: +US$ 1.310, ou +10,9% em dólar.\n\n"
        "Em Remessas, o cartão “A jornada” desenha essa história. O degrau soma o que você enviou, nas datas reais. A linha tracejada é a trajetória na taxa medida: 3,6% ao ano em dólar, no exemplo. A distância entre os dois é o rendimento. E os marcos ficam anotados: a primeira remessa, o maior envio e o ritmo dos envios.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #remessainternacional #dolar #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de ano é hora de olhar o caminho, e o exterior é o tema que mais alcança no perfil (o Reel de 14/10 teve o maior alcance de outubro)."),
        ("O que desperta interesse", "Uma linha do tempo que se desenha na frente da pessoa, desde o primeiro quadro: três degraus, a linha do rendimento e o valor de hoje, com a mesma lógica do gráfico do site."),
        ("Benefício para o público", "Entende como ler a própria história de investimentos lá fora: o que foi enviado, quanto rendeu em dólar e quais foram os marcos, sem planilha."),
        ("Como contribui para o perfil", "Apresenta o cartão “A jornada” de Remessas, uma função própria do timtimcash, com tela real e números coerentes com os outros posts de exterior (US$ 13.310 a R$ 5,0515)."),
    ],
    "alt": [
        "Reel de 18 segundos. Num fundo escuro, um gráfico se desenha: sua história lá fora começou em julho de 2023, com a primeira remessa de 4 mil dólares em 12/07/2023. "
        "Mais dois envios em 2024, em março e abril, levam o total enviado a 12 mil dólares, em degraus verde-menta. "
        "Uma linha tracejada sobe por cima dos degraus, o ritmo de 3,6% ao ano em dólar, até um ponto verde: 13.310 dólares, informado em 30/11/2026, mais 1.310 dólares. "
        "Depois, a tela real de Remessas do timtimcash no celular, com dados de exemplo: 13.310 dólares na carteira hoje, mais 10,9% em dólar e mais 12,1% em reais. "
        "A tela desce até o cartão A jornada, desde jul/23, e os marcos saltam ampliados: primeira remessa em 12/07/2023, três envios a cada 14 meses em média, maior envio de 4 mil dólares. Remessas no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/a-remessas-usd-alta.png · Remessas ao exterior no celular, aba USD, foto alta (390 × 2000 px CSS), site build 2026-10-16.1, conta de base, relógio em 09/12/2026 10:00: o cabeçalho (US$ 13.310, +US$ 1.310,00 +10,9% em US$) e o cartão “A jornada, desde jul/23” com os marcos · janela de 8,6 a 15,4 s (panorâmica do cabeçalho até o cartão) e recorte dos marcos de 13,0 a 15,4 s",
        "telas/b-ritmo-do-retorno-ao-ano.png · a mesma página, “Ritmo do retorno” depois do toque em “ao ano”: 3,6% na moeda, 4,0% em reais · conferência da taxa do tracejado, não aparece no vídeo",
    ],
}
