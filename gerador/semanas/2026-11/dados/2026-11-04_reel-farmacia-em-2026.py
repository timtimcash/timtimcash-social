# -*- coding: utf-8 -*-
"""Quarta 04/11/2026 · Reel "Quanto foi na farmácia?" (produto: Transações, busca e soma do filtrado; capa tinta). Equipe r1b (a partir da r1).
Versão de 17/10/2026. Na avaliação de novembro (16/10), o dono pediu "outro exemplo que não seja o delivery"; na da versão com
combustível (17/10), sugeriu assinaturas de streaming e outras assinaturas online. Como o carrossel de 07/11 (aprovado e agendado)
já é sobre assinaturas, com a mesma tela e os mesmos números, ele escolheu manter o 07/11 e usar outro gasto do dia a dia: a farmácia.
As versões anteriores ficam em equipes/r1b/reel_04_delivery.py e reel_04_combustivel.py (capturas: captura04_delivery.py e
captura04_combustivel.py).
Vídeo, capa e prévia gerados por equipes/r1b/reel_04.py; telas reais capturadas por equipes/r1b/capturas/captura04.py no site build
2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular (390 px CSS, escala 3), com o relógio em 04/11/2026 19:30, tudo
pela interface: toque em "Novembro 2026", "Ano atual", "Aplicar"; toque na busca e "farmácia" digitado letra a letra (uma foto
depois de cada letra). Números da tela (assert no gerador): "20 transações · 20 pagas · 0 pendentes · somam R$ 3.085,34 · 711 no
histórico" (período Ano 2026). Conta feita no gerador (assert): R$ 3.085,34 ÷ 20 = R$ 154,27 por compra; média de jan a out =
R$ 3.085,34 ÷ 10 = R$ 308,53 (R$ 309 no vídeo). Duas compras por mês na conta de exemplo, nenhuma em novembro até o dia 4; em
setembro e outubro, as compras foram menores (R$ 133,20 e R$ 144,30 no mês).
Buscas na mesma tela (Ano 2026), com assert: padaria 10 transações, R$ 1.047,14; cinema 9, R$ 1.994,55; luz 10, R$ 2.037,50.
O recorte ampliado das cenas 3 e 5 é a própria captura, recortada e ampliada (cartão "Transações": título, resumo do filtrado e busca)."""

POST = {
    "pasta": "2026-11-04_reel-farmacia-em-2026",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 19 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 19 s",
    "tema": "Quanto foi na farmácia este ano? Em Transações, o período Ano e a busca “farmácia” somam R$ 3.085,34 em 20 compras na conta de exemplo; a soma do que está filtrado aparece no topo, na hora, para qualquer busca",
    "pilar": "Produto (Transações: busca e soma do filtrado)",
    "data_longa": "quarta-feira, 4 de novembro de 2026",
    "data_curta": "quarta-feira, 04/11/2026",
    "data_mockup": "4 de novembro",
    "hora": "10h00",
    "iso": "2026-11-04T10:00:00",
    "video": "saida/2026-11-04_reel-farmacia-em-2026/reel.mp4",
    "capa": "saida/2026-11-04_reel-farmacia-em-2026/capa.jpg",
    "previa": "saida/2026-11-04_reel-farmacia-em-2026/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · TRANSAÇÕES · Quanto foi na farmácia este ano? · Campo de busca branco com a lupa e “farmácia”; embaixo, um “R$ ?” enorme, com o “R$” menor, como no site.",
        "0 a 4,4 s · Gancho (tinta) · Quanto foi na farmácia este ano? · “farmácia” é digitado letra a letra num campo de busca grande, já no primeiro quadro; um contador gira e para em R$ 3.085,34, com o “R$” e os centavos menores, como no site, e 20 quadradinhos, um por compra, acendem no ritmo do contador. · 20 compras em 2026, até 4/11.",
        "4,4 a 7,3 s · Em Transações: período Ano e a busca “farmácia”. · Tela real de Transações no celular: anel na pílula “Ano 2026”, toque no campo de busca e “farmácia” digitado; a cada letra, a foto real seguinte, e a soma do filtrado muda na hora (com “f”, 33 transações e R$ 7.017,54; a partir de “fa”, 20 e R$ 3.085,34). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "7,6 a 10,1 s · A soma do que está filtrado aparece no topo. · O cartão “Transações” se solta da tela e cresce (a mesma foto, recortada e ampliada), com anel em “somam R$ 3.085,34”; atrás, a lista das compras desce (“Farmácia” em 22 de outubro, R$ 81,90; 8 de outubro, R$ 62,40; 17 de setembro, R$ 74,30).",
        "10,4 a 13,1 s · Em média, R$ 309 por mês. · de janeiro a outubro de 2026 · Barras mês a mês, de jan a out, com a linha tracejada da média de R$ 309 (em setembro e outubro, as compras da conta de exemplo foram menores). · 20 compras · R$ 154,27 cada, em média.",
        "13,3 a 16,7 s · Busque qualquer coisa. A soma aparece na hora. · O mesmo cartão real, ampliado, com cada busca e anel na soma: padaria, cinema e luz; embaixo, as três somas em letras grandes: padaria, 10 transações, R$ 1.047,14; cinema, 9 transações, R$ 1.994,55; luz, 10 transações, R$ 2.037,50. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "16,7 a 19,4 s · Fechamento (verde) · Transações no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Quanto foi na farmácia este ano? A resposta está a uma busca.\n\n"
        "No exemplo do vídeo, foram 20 compras de 1º de janeiro a 4 de novembro: R$ 3.085,34. Dá R$ 154,27 por compra e uns R$ 309 por mês, de janeiro a outubro.\n\n"
        "Para ver o seu: em Transações, escolha o período Ano e digite “farmácia” na busca. A soma do que está filtrado aparece no topo, na hora. "
        "A busca olha a descrição, a categoria e o valor, então serve para qualquer gasto: padaria, cinema, conta de luz.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#controlefinanceiro #financaspessoais #organizacaofinanceira #educacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Quarta-feira, começo de novembro: antes da Black Friday e dos gastos de fim de ano, vale olhar quanto um gasto miúdo somou no ano inteiro. Compra a compra, a farmácia parece pouco; somada no ano, surpreende."),
        ("O que desperta interesse", "Quase todo mundo compra na farmácia, e pouca gente sabe quanto foi no ano. A resposta vem no primeiro segundo: “farmácia” sendo digitado e um contador que gira até R$ 3.085,34, com um quadradinho aceso para cada compra."),
        ("Benefício para o público", "Aprende um gesto de poucos segundos que vale para qualquer gasto: em Transações, período Ano, uma palavra na busca e a soma aparece no topo, sem planilha e sem fórmula."),
        ("Como contribui para o perfil", "Mostra, com a tela real do site mais recente e a digitação de verdade, uma função do dia a dia do timtimcash (a busca com a soma do filtrado), no formato de Reel que abre em movimento. O exemplo é um gasto comum, sem julgamento de hábito, e não repete o tema do carrossel de assinaturas de 07/11."),
    ],
    "alt": [
        "Reel de 19 segundos. Quanto foi na farmácia este ano? Num fundo escuro, a palavra farmácia é digitada num campo de busca e um contador gira até R$ 3.085,34, enquanto 20 quadradinhos acendem, um por compra: 20 compras em 2026, até 4 de novembro. "
        "Depois, a tela real de Transações do timtimcash no celular, com dados de exemplo: o período Ano 2026 em destaque, o toque na busca e farmácia digitado letra a letra, com a soma do filtrado mudando a cada letra. "
        "O cartão Transações se solta da tela e cresce, com destaque em 20 transações pagas que somam R$ 3.085,34, enquanto a lista das compras desce atrás. "
        "Um gráfico de barras mostra o gasto mês a mês, de janeiro a outubro, com a média de R$ 309 por mês e R$ 154,27 por compra. "
        "Busque qualquer coisa, a soma aparece na hora: o mesmo cartão real com as buscas padaria, R$ 1.047,14; cinema, R$ 1.994,55; luz, R$ 2.037,50, no ano de 2026 da mesma conta. Transações no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-transacoes-novembro.png · Transações no celular ao abrir, Novembro 2026, site build 2026-10-16.1, conta de base, relógio em 04/11/2026 19:30 · ponto de partida, não aparece no vídeo",
        "telas/celular-transacoes-periodo-ano-atual.png · a folha de período depois do toque em “Ano atual” (01/01/2026 a 31/12/2026), antes de “Aplicar” · não aparece no vídeo",
        "telas/celular-transacoes-ano-2026.png e celular-transacoes-ano-2026-busca-tocada.png · Ano 2026, “288 transações · 275 pagas · 13 pendentes · 711 no histórico”, antes e depois do toque na busca · 4,4 a 6,3 s",
        "telas/celular-transacoes-ano-digitando-01.png a celular-transacoes-ano-digitando-08.png · uma foto real depois de cada letra de “farmácia” (com “f”: 33 transações, R$ 7.017,54; a partir de “fa”: 20, R$ 3.085,34) · 6,3 a 10,1 s; a última também no recorte ampliado de 7,8 a 10,1 s",
        "telas/celular-transacoes-ano-busca-farmacia-alta.png · a mesma tela com a busca “farmácia”, em foto alta (390 × 1800 px CSS, escala 3) · referência da lista",
        "telas/celular-transacoes-ano-busca-padaria.png, celular-transacoes-ano-busca-cinema.png e celular-transacoes-ano-busca-luz.png · as somas de padaria (10, R$ 1.047,14), cinema (9, R$ 1.994,55) e luz (10, R$ 2.037,50) no período Ano 2026 · recorte ampliado de 13,3 a 16,7 s",
    ],
}
