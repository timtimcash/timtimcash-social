# -*- coding: utf-8 -*-
"""Sexta 15/01/2027 · Reel "O seu mês tem 3 recados" (produto: Insights da Visão geral; capa tinta). Equipe jr.
Vídeo, capa e prévia gerados por equipes/jr/reel_15.py (assert nos números lidos da tela); telas capturadas por
equipes/jr/captura_15.py no site build 2026-10-19.5, na cópia da conta da equipe (igual à da base, sem mudança),
no celular (390 px em escala 3, a página inteira da Visão geral numa foto alta de 390 × 4781, para a câmera descer como quem rola
e para o painel ficar parado quando um cartão sai), relógio da página em 15/01/2027 10:00, Janeiro 2027, Realizado.
Os 3 cartões do dia (assert no gerador), com a conta por trás (estado.py e a tela):
1) “Educação 65% acima da média · R$ 2.390,00 este mês vs média de R$ 1.450,00 (últimos 6 meses).” Educação = escola 1.450 + material
   escolar 940 (pago em 12/01) = 2.390; 2.390 ÷ 1.450 = 1,648.
2) “Excelente! Receita guardada: 35% · Você guardou R$ 3.518,50 de R$ 9.960,00 recebidos. Continue assim!” Receitas 9.960,00 e despesas
   6.441,50 até 15/01 (Realizado): (9.960 − 6.441,50) ÷ 9.960 = 35,3%, acima da meta padrão de 20% (Relatórios, “Ajustar cálculo”;
   FUNCIONALIDADES.md). O vídeo diz “até aqui”: o mês ainda tem o IPVA (20/01) e fecha com resultado −R$ 1.179,90.
3) “Educação: 37% das despesas · Concentra R$ 2.390,00 dos seus gastos.” 2.390 ÷ 6.441,50 = 37,1%.
Toque no X do terceiro cartão (“Dispensar este insight”): ele sai e ficam dois (o site guarda a dispensa no mês, só nesta sessão).
As regras (código do site, build 2026-10-19.5): categoria 35% ou mais acima da média dos 6 meses anteriores (e R$ 100 a mais),
receita guardada contra a meta, maior categoria do período, orçamentos acima de 70% ou estourados, contas no negativo e lançamentos
vencidos; até 3 cartões. São regras fixas, e é assim que o vídeo e a legenda falam delas (FUNCIONALIDADES.md).
Por que 15/01: é o dia do post e já mostra o material escolar (12/01) num cartão. O IPVA (20/01) e um orçamento acima de 70% (Mercado
passa de 70% em 21/01) só apareceriam depois do dia do post; o vídeo cita esses outros cartões sem mostrar tela de outro dia.
Diferença do que já saiu: os Insights ainda não tinham sido o assunto de um post (27/12 mostrou “O que mudou”, em Relatórios)."""

POST = {
    "pasta": "2027-01-15_reel-insights-o-que-o-mes-diz",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "O seu mês tem 3 recados: os Insights da Visão geral (Análise automática do período) em 15/01, cartão a cartão (Educação 65% acima da média pelo material escolar, receita guardada de 35% contra a meta de 20%, Educação com 37% das despesas), o X que dispensa no mês e a explicação de que são regras fixas",
    "pilar": "Produto (Visão geral: Insights)",
    "data_longa": "sexta-feira, 15 de janeiro de 2027",
    "data_curta": "sexta-feira, 15/01/2027",
    "data_mockup": "15 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-15T10:00:00",
    "video": "saida/2027-01-15_reel-insights-o-que-o-mes-diz/reel.mp4",
    "capa": "saida/2027-01-15_reel-insights-o-que-o-mes-diz/capa.jpg",
    "previa": "saida/2027-01-15_reel-insights-o-que-o-mes-diz/previa.mp4",
    "slides": [
        "Capa da grade (tinta, logotipo de fundo escuro) · VISÃO GERAL · INSIGHTS · O seu mês tem 3 recados. (“3 recados.” em menta) · Os 3 cartões reais dos Insights de 15/01, empilhados (recortes da tela) · Nota: Tela real do timtimcash, com dados de exemplo.",
        "0 a 3,4 s · Gancho (tinta) · O seu mês tem 3 recados. · Desde o primeiro quadro, os 3 cartões reais entram um a um, cada um com um número em menta: “Educação 65% acima da média”, “Excelente! Receita guardada: 35%” e “Educação: 37% das despesas”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "3,5 a 5,6 s · Em Insights, no fim da Visão geral. · Tela real no celular (15/01/2027): a câmera desce da Visão geral até o painel “Insights · Análise automática do período”.",
        "5,7 a 8,3 s · 1 · O material escolar levou Educação a 65% acima da média. · Anel no cartão: R$ 2.390,00 este mês vs média de R$ 1.450,00 (últimos 6 meses).",
        "8,3 a 10,9 s · 2 · Receita guardada: 35% até aqui. A meta padrão é 20%. · Anel no cartão: Você guardou R$ 3.518,50 de R$ 9.960,00 recebidos.",
        "11,0 a 13,6 s · 3 · Educação leva 37% do que saiu no mês. · Anel no cartão: Concentra R$ 2.390,00 dos seus gastos.",
        "13,6 a 15,8 s · Já viu? O X dispensa o recado até o fim do mês. · Toque no X do terceiro cartão: ele sai e ficam dois.",
        "15,9 a 18,0 s · São regras fixas: comparam o seu mês com a sua média e com as suas metas. · Dois cartões desenhados: “A sua média dos meses anteriores” e “As suas metas e os seus limites”. · Também há cartões para orçamento acima de 70%, conta no negativo e lançamento vencido.",
        "18,0 a 20,8 s · Fechamento (verde) · Insights na Visão geral do timtimcash. · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "O seu mês tem 3 recados.\n\n"
        "Na Visão geral, o painel Insights faz a análise do período: até 3 cartões, que mudam conforme o mês.\n\n"
        "Em 15/01, no exemplo do vídeo: Educação 65% acima da média, porque o material escolar de R$ 940,00 entrou; receita guardada de 35% até aqui, acima da meta padrão de 20%; e Educação com 37% das despesas do mês.\n\n"
        "São regras fixas: comparam o seu mês com a sua média e com as suas metas. Também há cartões para orçamento acima de 70%, conta no negativo e lançamento vencido. Já leu? O X dispensa o cartão até o fim do mês.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#controlefinanceiro #organizacaofinanceira #financaspessoais #educacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Metade de janeiro, quando os gastos de começo de ano (material escolar) já pesam e a pessoa precisa saber, sem fazer conta, o que fugiu do normal."),
        ("O que desperta interesse", "Uma promessa curta (3 recados) e os 3 cartões reais entrando um a um logo no primeiro segundo, cada um com um número."),
        ("Benefício para o público", "Aprende a ler cada cartão (acima da média, receita guardada contra a meta, concentração), a dispensar o que já leu e que são regras fixas, sem mistério."),
        ("Como contribui para o perfil", "Apresenta os Insights, ainda inéditos no perfil, com tela real e a explicação honesta de como funcionam."),
    ],
    "alt": [
        "Reel de 21 segundos. Num fundo escuro, o título O seu mês tem 3 recados e três cartões reais do timtimcash que entram um a um, numerados: Educação 65% acima da média; Excelente! Receita guardada: 35%; "
        "Educação: 37% das despesas. Depois, a tela real da Visão geral no celular, com dados de exemplo, rola até o painel Insights, Análise automática do período, e cada cartão ganha um anel: "
        "o material escolar levou Educação a R$ 2.390,00 contra a média de R$ 1.450,00; a receita guardada está em 35% até aqui, com R$ 3.518,50 de R$ 9.960,00, e a meta padrão é 20%; Educação leva 37% do que saiu no mês. "
        "Um toque no X tira o terceiro cartão até o fim do mês. A frase final explica que são regras fixas, que comparam o mês com a sua média e com as suas metas, e que há cartões para orçamento acima de 70%, conta no negativo e lançamento vencido. "
        "Insights na Visão geral do timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/a-visao-geral-inteira.jpg · Visão geral no celular, Janeiro 2027, Realizado, site build 2026-10-19.5, cópia da conta sem mudança, relógio em 15/01/2027 10:00, a página inteira (390 × 4781), com os 3 cartões dos Insights · recortes do gancho (0 a 3,4 s) e da capa; na janela de 3,5 a 14,6 s",
        "telas/b-visao-geral-inteira-depois-do-x.jpg · a mesma página depois do toque no X do terceiro cartão: ficam dois · 14,6 a 15,8 s",
        "telas/caixas.json · posições medidas na captura (cartões, X, painel) e o texto de cada cartão, usados nos anéis, no toque e nos assert do roteiro",
    ],
}
