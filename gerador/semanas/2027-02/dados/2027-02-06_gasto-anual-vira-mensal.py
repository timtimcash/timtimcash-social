# -*- coding: utf-8 -*-
"""Sábado 06/02/2027 · carrossel "O gasto do ano, dividido por 12" (planejamento, capa papel). Equipe fa.
Artes: saida/2027-02-06_gasto-anual-vira-mensal/01.jpg a 06.jpg, geradas por equipes/fa/posts.py (post_anual).
Telas reais em saida/2027-02-06_gasto-anual-vira-mensal/telas/, capturadas por equipes/fa/captura.py na cópia da conta
(igual à base, sem mudança), build 2026-10-19.5, relógio em 06/02/2027 10:00. A regra da Simulação e a "Nova transação"
foram feitas pela interface e não foram salvas nos arquivos da conta.

Números (asserts em posts.py, contra a conta e as telas): IPVA 2027 R$ 1.236 (20/01/2027); IPTU 2027 em 10 parcelas
de R$ 215 (fevereiro a novembro) = R$ 2.150; material escolar R$ 940 (12/01) e uniforme R$ 286 (18/01) = R$ 1.226;
presentes de Natal de 2026 = R$ 852,40 (tela: Transações, Ano 2026, busca "presentes de natal", "3 transações ·
somam R$ 852,40": 389,90 + 264,50 + 198,00). Total R$ 5.464,40; ÷ 12 = R$ 455,37 (arredondado; 12 × 455,37 =
5.464,44).
O fundo do slide 3 (conta minha, com os valores de 2027 repetidos até janeiro de 2028): R$ 455,37 por mês a partir de
fevereiro de 2027; sai o IPTU (R$ 215) de fevereiro a novembro, o Natal (R$ 852,40) em dezembro e IPVA, material e
uniforme (R$ 2.462) em janeiro de 2028. Saldo: R$ 240,37 em fevereiro, R$ 2.403,70 em novembro, R$ 2.006,67 em
dezembro e R$ 0,04 depois de janeiro (nunca fica negativo).
Telas: a regra "+ Um mês do ano" (Simulação futura › Cenário base › horizonte "2 anos" › Impostos e Taxas › "Ajustar
por mês"): "Todo mês de janeiro", R$ 1.236, "Resultado nos 24 meses · 22 meses em R$ 0 · 2 em R$ 1.236", de fev/27 a
jan/29; "Nova transação": Despesa R$ 1.236,00, 20/01/2028, "Marcar como pago" desligado, Impostos e Taxas, "IPVA",
Recorrência Fixa, Anual, "Lançamentos automáticos · anual".
Diferença dos posts de dezembro: 07/12 ("Janeiro caro") mostrou o que chega junto em janeiro; aqui, a conta do ano
inteiro dividida por 12, o fundo mês a mês e duas formas de pôr o gasto anual no timtimcash."""

POST = {
    "pasta": "2027-02-06_gasto-anual-vira-mensal",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "O gasto do ano dividido por 12: IPVA, IPTU, material e uniforme e presentes de Natal da conta de exemplo (R$ 5.464,40, ou R$ 455,37 por mês), o fundo que começa em fevereiro e paga tudo até janeiro, a regra “+ Um mês do ano” da Simulação futura e a recorrência Fixa anual",
    "pilar": "Educação · planejamento, com produto",
    "data_longa": "sábado, 6 de fevereiro de 2027",
    "data_curta": "sábado, 06/02/2027",
    "data_mockup": "6 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-06T10:00:00",
    "slides": [
        "Capa (fundo papel) · PLANEJAMENTO · O gasto do ano, dividido por 12. · Quatro barras horizontais, cada uma partida em 12 fatias, com o comprimento do valor: IPVA (coral), IPTU (âmbar, a mais longa), Material (tinta) e Presentes (coral claro); embaixo, o selo “÷ 12” e uma fila de 12 blocos verdes iguais, de J a D.",
        "NA CONTA DE EXEMPLO · Os gastos que voltam todo ano. · Não são surpresa: só não vêm todo mês. · Lista com ícones: IPVA 2027, à vista em janeiro, R$ 1.236,00; IPTU 2027, 10 × R$ 215, de fevereiro a novembro, R$ 2.150,00; Material e uniforme, janeiro, R$ 1.226,00; Presentes de Natal, dezembro de 2026, R$ 852,40. No ano: R$ 5.464,40. ÷ 12 meses: R$ 455,37. · Nota: Conta de exemplo. Presentes de Natal de 2026: busca em Transações, no Ano 2026.",
        "A REGRA · Guarde 1/12 por mês. · Começando em fevereiro, o dinheiro de janeiro fica pronto antes de janeiro chegar. · Gráfico “O fundo do ano, mês a mês · + R$ 455,37 todo mês”: 12 barras verdes, de fev a jan, que crescem até R$ 2.403,70 em novembro, descem em dezembro e chegam a quase zero em janeiro. Legenda: fev a nov: paga o IPTU e cresce; dez: paga o Natal; jan: paga IPVA, material e uniforme. · Nota: Conta de exemplo, com os valores de 2027 repetidos até janeiro de 2028, quando o fundo paga a última conta do ciclo.",
        "NO TIMTIMCASH · SIMULAÇÃO FUTURA · Um gasto em todo janeiro. · Em “Ajustar por mês”, a regra “+ Um mês do ano” põe o IPVA em cada janeiro do cenário. · Tela real no celular, relógio em 06/02/2027: Regras, 1 regra, “Todo mês de janeiro”, R$ 1.236; os botões “+ A partir de um mês”, “+ Um mês do ano” e “+ Um mês específico”; “Resultado nos 24 meses · 22 meses em R$ 0 · 2 em R$ 1.236”, com a faixa de fev/27 a jan/29 e os dois janeiros em verde. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "NO TIMTIMCASH · NOVA TRANSAÇÃO · Ou lance o IPVA como Fixa anual. · O de 2028 já fica em Pendentes, com a data. E todo janeiro aparece de novo. · Tela real da “Nova transação” no celular, relógio em 06/02/2027: Despesa, R$ 1.236,00; Data 20/01/2028; “Marcar como pago” desligado; Categoria Impostos e Taxas; Pago via Conta corrente; IPVA; Recorrência Fixa; Anual; “Lançamentos automáticos · anual”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Janeiro sem susto. · Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "O gasto que vem uma vez por ano cabe no mês, se você dividir por 12.\n\n"
        "Na conta de exemplo: IPVA de R$ 1.236, IPTU de R$ 2.150 (10 × R$ 215), material e uniforme de R$ 1.226 e R$ 852,40 de presentes de Natal. São R$ 5.464,40 no ano, ou R$ 455,37 por mês.\n\n"
        "A regra: guarde 1/12 por mês. Começando em fevereiro, o fundo paga o IPTU de fevereiro a novembro, o Natal em dezembro e o IPVA, o material e o uniforme em janeiro de 2028.\n\n"
        "No timtimcash, a Simulação futura tem a regra “+ Um mês do ano”: o IPVA entra em todo janeiro do cenário. E na Nova transação, a recorrência Fixa anual deixa o IPVA de 2028 em Pendentes, com a data.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#planejamentofinanceiro #ipva #iptu #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Janeiro acabou de cobrar IPVA, material e uniforme, e o carnê do IPTU começa em fevereiro. É um bom momento para começar o fundo do próximo ciclo: guardando desde fevereiro, ele fecha a conta em janeiro de 2028."),
        ("O que desperta interesse", "A capa mostra os gastos do ano se partindo em 12 fatias, e a conta é simples e concreta: R$ 5.464,40 no ano viram R$ 455,37 por mês, com o fundo desenhado mês a mês."),
        ("Benefício para o público", "Aprende a transformar gastos anuais em uma parcela mensal, vê que o fundo começado em fevereiro paga tudo até o janeiro seguinte e conhece duas formas de deixar isso no timtimcash: a regra da Simulação futura e a Fixa anual."),
        ("Como contribui para o perfil", "Mostra duas funções que ainda não apareceram no perfil (a regra “+ Um mês do ano” e a recorrência Fixa anual), com telas reais e números da mesma conta de exemplo dos posts de janeiro."),
    ],
    "alt": [
        "Planejamento. O gasto do ano, dividido por 12. Quatro barras horizontais, cada uma partida em 12 fatias: IPVA, IPTU, a mais longa, material e presentes. Abaixo, o sinal de dividido por 12 e uma fila de 12 blocos verdes iguais, um para cada mês, de janeiro a dezembro.",
        "Na conta de exemplo, os gastos que voltam todo ano: não são surpresa, só não vêm todo mês. IPVA 2027, à vista em janeiro, R$ 1.236; IPTU 2027, 10 parcelas de R$ 215 de fevereiro a novembro, R$ 2.150; material e uniforme em janeiro, R$ 1.226; presentes de Natal em dezembro de 2026, R$ 852,40. No ano, R$ 5.464,40; dividido por 12 meses, R$ 455,37.",
        "A regra: guarde 1/12 por mês. Começando em fevereiro, o dinheiro de janeiro fica pronto antes de janeiro chegar. Gráfico do fundo do ano, com R$ 455,37 guardados todo mês: as barras crescem de fevereiro a novembro, quando chegam a R$ 2.403,70, mesmo pagando o IPTU; em dezembro o fundo paga o Natal; em janeiro paga IPVA, material e uniforme e fica perto de zero.",
        "No timtimcash, na Simulação futura: um gasto em todo janeiro. Em Ajustar por mês, a regra Um mês do ano põe o IPVA em cada janeiro do cenário. Tela real do celular, com dados de exemplo: regra Todo mês de janeiro, R$ 1.236; resultado nos 24 meses, 22 meses em zero e 2 em R$ 1.236, com os dois janeiros destacados na faixa de fevereiro de 2027 a janeiro de 2029.",
        "No timtimcash, na Nova transação: ou lance o IPVA como Fixa anual. O de 2028 já fica em Pendentes, com a data, e todo janeiro aparece de novo. Tela real do celular, com dados de exemplo: despesa de R$ 1.236, data 20 de janeiro de 2028, ainda não paga, categoria Impostos e Taxas, descrição IPVA, recorrência Fixa, anual.",
        "Janeiro sem susto. Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-busca-presentes-de-natal-2026-06-02.png · Transações no celular (390 × 1100 em escala 3), relógio em 06/02/2027 10:00, build 2026-10-19.5, cópia da conta igual à base: período “Ano atual” e a seta para Ano 2026, busca “presentes de natal”: “3 transações · 3 pagas · 0 pendentes · somam R$ 852,40”; 21/12/2026 −R$ 198,00, 17/12/2026 −R$ 264,50 e 12/12/2026 −R$ 389,90 · número do slide 2 (a tela não aparece no carrossel)",
        "telas/celular-simulacao-regra-ipva-06-02.png · Simulação futura no celular (390 × 1300 em escala 3), mesmo relógio: “Cenário base”, horizonte “2 anos”, ⋯ de Impostos e Taxas › “Ajustar por mês” › “+ Um mês do ano”, mês janeiro e valor 1.236 digitados (só na sessão do navegador): “Todo mês de janeiro”, “Resultado nos 24 meses · 22 meses em R$ 0 · 2 em R$ 1.236”, fev/27 a jan/29 · slide 4 (recorte de “Regras” ao resultado)",
        "telas/celular-nova-despesa-fixa-anual-06-02.png · “Nova transação” no celular (390 × 1100 em escala 3), mesmo relógio, preenchida e fechada sem salvar: Despesa R$ 1.236,00, Data 20/01/2028 (11 toques na seta do calendário), interruptor “Já foi pago” desligado (“Marcar como pago · Fica como pendente até você confirmar”), Categoria Impostos e Taxas, Pago via Conta corrente, descrição IPVA, Recorrência Fixa, Anual (“Lançamentos automáticos · anual”) · slide 5 (recorte do valor à recorrência)",
    ],
}
