# -*- coding: utf-8 -*-
"""Quarta 17/02/2027 · carrossel "3 jeitos de ver o mesmo mês" (Visão geral: Realizado, Previsto e Ambos; capa verde suave).
Equipe fb. Artes: saida/2027-02-17_realizado-previsto-e-ambos/01.jpg a 06.jpg, geradas por equipes/fb/posts.py (post_modos).
Na revisão de 20/10/2026, este post trocou de dia com "Lá fora na declaração" (era 19/02, com capa papel); o fundo da
capa segue a data (17/02, verde suave) e as telas foram refeitas com o relógio em 17/02.

Nomes e frases do site (FUNCIONALIDADES.md, build 2026-10-19.5): "Realizado" (só o que já entrou e saiu; é o padrão sempre
que o site abre), "Previsto" (inclui o que está pendente), "Ambos" (o que já aconteceu e quanto falta para o mês fechar).
Números da conta de base em 17/02/2027 (refeitos de estado.py e conferidos por assert em posts.py contra o texto das telas):
- fevereiro até 17/02: receitas R$ 9.960,00; despesas pagas R$ 6.904,40; resultado R$ 3.055,60; "Guardou 30,7% da receita".
- pendentes de fevereiro: Armazenamento na nuvem R$ 42,00 (20/02) e Notebook (4/10) R$ 360,00 (27/02) = R$ 402,00.
- Previsto: despesas R$ 7.306,40; "Resultado previsto R$ 2.653,60"; "Deve guardar 26,6% da receita".
- Ambos: "Concluído · 100% já aconteceu" (receitas); "Faltam R$ 402,00 · 94% já aconteceu" (despesas; 94,5% truncado
  pelo site); "Deve fechar em R$ 2.653,60"; "Com os pendentes, R$ 115.037,36 · −R$ 402,00 pendentes" (patrimônio).
- conferência do slide 5 ("em março, aluguel e escola já aparecem"): Previsto de março de 2027 visto em 17/02, Casa
  R$ 2.300,00 e Educação R$ 1.450,00 já pendentes (despesas de março R$ 4.444,80); foto de exploração, não publicada.
O gasto do dia a dia depois de 17/02 ainda não existe na conta (só o contratado fica pendente), por isso o Previsto de
17/02 (R$ 2.653,60) não é o resultado final do mês: o slide 3 avisa que o Previsto soma o que está lançado.
Telas da conta de base (J/base_app, com o saldo de 31/12/2026 informado desde 29/01, que não aparece nestas telas),
capturadas por equipes/fb/captura.py (visao_1702)."""

POST = {
    "pasta": "2027-02-17_realizado-previsto-e-ambos",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "Os três modos de cálculo da Visão geral: Realizado (só o que já entrou e saiu, o padrão), Previsto (inclui o que ainda vai vencer) e Ambos (o que já aconteceu e quanto falta para o mês fechar), com fevereiro de 2027 da conta de exemplo nos três modos e quando usar cada um",
    "pilar": "Produto (Visão geral) com educação financeira",
    "data_longa": "quarta-feira, 17 de fevereiro de 2027",
    "data_curta": "quarta-feira, 17/02/2027",
    "data_mockup": "17 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-17T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · VISÃO GERAL · 3 jeitos de ver o mesmo mês. · Três chips como os do site (“Realizado”, “Previsto” e “Ambos”), cada um sobre uma régua de fevereiro de 2027 com 28 quadradinhos: no Realizado, verdes até o dia 17 e claros depois; no Previsto, verdes até o 17 e âmbar nos dias 20 e 27 (os pendentes); no Ambos, igual ao Previsto e o resto do mês com contorno âmbar. Uma linha preta marca “hoje · 17/02”; nas pontas, 1º/02 e 28/02.",
        "REALIZADO · O PADRÃO · Só o que já entrou e saiu. · É assim que o site abre. Em 17/02, o resultado de fevereiro era R$ 3.055,60. · Recortes da tela real da Visão geral no celular (relógio em 17/02/2027): o seletor com “Realizado” marcado e o cartão “Movimento de fevereiro 2027 · PARCIAL”: Guardou 30,7% da receita; Receitas R$ 9.960,00; Despesas R$ 6.904,40; Resultado do período R$ 3.055,60. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "PREVISTO · Inclui o que ainda vai vencer. · Entram as contas que já têm data no mês: a nuvem, no dia 20, e a parcela do notebook, no dia 27. · Recortes da tela real com “Previsto” marcado: “Movimento de fevereiro 2027 · PREVISTO · PARCIAL”: Deve guardar 26,6% da receita; Receitas R$ 9.960,00; Despesas R$ 7.306,40; Resultado previsto R$ 2.653,60. · Nota: Tela real do timtimcash, com dados de exemplo. · Aviso em âmbar: O Previsto soma o que está lançado. O gasto do dia a dia entra quando você lança.",
        "AMBOS · O que já foi e o que falta. · Cada número mostra quanto já aconteceu, e o resultado diz onde o mês deve fechar. · Recortes da tela real com “Ambos” marcado: Receitas R$ 9.960, Concluído, 100% já aconteceu; Despesas R$ 6.904,40, Faltam R$ 402,00, 94% já aconteceu; Resultado R$ 3.055,60, Deve fechar em R$ 2.653,60. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "QUANDO USAR CADA UM · Um modo para cada pergunta. · Quanto já sobrou? (Realizado): para conferir com o extrato do banco, é o dinheiro que já se mexeu. Quanto vai sobrar? (Previsto): para planejar; vale para o mês que vem: em março, aluguel e escola já aparecem. Quanto ainda falta? (Ambos): no meio do mês, para saber o que já foi e o que ainda vai sair.",
        "Fechamento (fundo verde) · Realizado, Previsto ou Ambos: um toque. · Visão geral no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "O mesmo mês, três números. E todos estão certos.\n\n"
        "Na Visão geral do timtimcash, o cálculo tem três modos. Realizado mostra só o que já entrou e saiu da conta: é o padrão sempre que o site abre. Previsto inclui o que ainda vai vencer. Ambos mostra o que já aconteceu e quanto falta para o mês fechar.\n\n"
        "No exemplo, em 17/02: Realizado, R$ 3.055,60 de resultado em fevereiro. Previsto, R$ 2.653,60, porque a nuvem (dia 20) e a parcela do notebook (dia 27) somam R$ 402. Ambos mostra os dois: faltam R$ 402,00, e o mês deve fechar em R$ 2.653,60.\n\n"
        "O Previsto soma o que está lançado. O gasto do dia a dia entra quando você lança.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#controlefinanceiro #organizacaofinanceira #financaspessoais #orcamento #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Passado o Carnaval, na metade de fevereiro, a pergunta muda de quanto já gastei para quanto vai sobrar. É o momento em que os três modos fazem mais diferença."),
        ("O que desperta interesse", "Três números diferentes para o mesmo mês, e todos certos: a capa mostra as três réguas e o carrossel resolve o mistério com telas reais."),
        ("Benefício para o público", "Aprende a ler o resultado do mês sem confundir o que já aconteceu com o que vai acontecer, e sabe qual modo usar para conferir o extrato, planejar ou ajustar no meio do mês."),
        ("Como contribui para o perfil", "Apresenta uma função que ainda não tinha aparecido por inteiro no perfil (o seletor Realizado, Previsto e Ambos), com números que batem com a conta de exemplo dos outros posts."),
    ],
    "alt": [
        "Visão geral. 3 jeitos de ver o mesmo mês. Três chips, Realizado, Previsto e Ambos, cada um sobre uma régua de fevereiro com 28 quadradinhos. No Realizado, verdes até o dia 17 e claros depois. No Previsto, verdes até o dia 17 e âmbar nos dias 20 e 27, as contas pendentes. No Ambos, o mesmo e o resto do mês contornado em âmbar. Uma linha marca hoje, 17 de fevereiro.",
        "Realizado, o padrão: só o que já entrou e saiu. É assim que o site abre. Em 17 de fevereiro, o resultado do mês era 3.055,60 reais. Recortes da tela real da Visão geral no celular, com dados de exemplo: Realizado marcado; movimento de fevereiro de 2027, parcial; guardou 30,7% da receita; receitas de 9.960 reais; despesas de 6.904,40 reais; resultado do período de 3.055,60 reais.",
        "Previsto: inclui o que ainda vai vencer. Entram as contas que já têm data no mês: a nuvem, no dia 20, e a parcela do notebook, no dia 27. Recortes da tela real com Previsto marcado: deve guardar 26,6% da receita; receitas de 9.960 reais; despesas de 7.306,40 reais; resultado previsto de 2.653,60 reais. Aviso: o Previsto soma o que está lançado; o gasto do dia a dia entra quando você lança.",
        "Ambos: o que já foi e o que falta. Recortes da tela real com Ambos marcado: receitas de 9.960 reais, concluído, 100% já aconteceu; despesas de 6.904,40 reais, faltam 402 reais, 94% já aconteceu; resultado de 3.055,60 reais, deve fechar em 2.653,60 reais.",
        "Um modo para cada pergunta. Quanto já sobrou? Realizado, para conferir com o extrato do banco. Quanto vai sobrar? Previsto, para planejar, inclusive o mês que vem: em março, aluguel e escola já aparecem. Quanto ainda falta? Ambos, no meio do mês, para saber o que já foi e o que ainda vai sair.",
        "Realizado, Previsto ou Ambos: um toque. Visão geral no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-visao-geral-realizado-17-02.png · Visão geral no celular, Fevereiro 2027, “Realizado” (o padrão ao abrir), relógio em 17/02/2027 10:00, build 2026-10-19.5, conta de base (390 × 1700 em escala 3) · slide 2 (recortes do seletor e do cartão “Movimento de fevereiro 2027”)",
        "telas/celular-visao-geral-previsto-17-02.png · a mesma tela depois do toque em “Previsto” · slide 3 (recortes do seletor e do cartão do movimento)",
        "telas/celular-visao-geral-ambos-17-02.png · a mesma tela depois do toque em “Ambos” · slide 4 (recortes do seletor e do cartão com Receitas, Despesas e Resultado)",
    ],
}
