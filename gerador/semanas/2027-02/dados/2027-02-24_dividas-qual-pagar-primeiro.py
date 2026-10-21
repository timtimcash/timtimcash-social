# -*- coding: utf-8 -*-
"""Quarta 24/02/2027 · carrossel "Qual dívida pagar primeiro?" (educação, dívidas, capa papel). Equipe fb.
Artes: saida/2027-02-24_dividas-qual-pagar-primeiro/01.jpg a 07.jpg, geradas por equipes/fb/posts.py (post_dividas).

Dívidas e taxas de exemplo (redondas e ditas como exemplo; nenhuma taxa média do Banco Central, que estaria velha em
fevereiro de 2027): Crediário da loja, saldo R$ 800, 3% ao mês, 10 parcelas de R$ 93,78; Empréstimo pessoal, R$ 3.000, 7% ao
mês, 12 × R$ 377,71; Financiamento do carro, R$ 6.000, 2% ao mês, 24 × R$ 317,23 (parcelas pela tabela Price). Juros de um
mês (saldo × taxa): R$ 24, R$ 210 e R$ 120.
Simulação do slide 4 (função quitar() em posts.py, conferida por assert e por uma segunda conta independente em ponto
flutuante): todo mês, juros sobre o saldo, a parcela de cada dívida aberta e R$ 300 a mais na dívida da vez; quando uma
acaba, a parcela dela segue para a próxima; sem IOF, tarifas, seguros nem atraso.
  A mais cara primeiro (7% → 3% → 2%): R$ 1.764,35 de juros; o empréstimo acaba no 6º mês; tudo em 11 meses.
  A menor primeiro (R$ 800 → R$ 3.000 → R$ 6.000): R$ 1.893,32 de juros; o crediário acaba no 3º mês; tudo em 11 meses.
  Diferença: R$ 128,97 (R$ 129 no slide, valores arredondados). Só as parcelas, sem o extra: 24 meses e R$ 3.283,84 de
  juros (R$ 13.083,84 em parcelas − R$ 9.800 de saldo).
Fatos: Gal e McShane (2012), FATOS_2.md 1.1 a 1.7 (associação em dados de uma empresa de renegociação de dívidas, não
experimento; "cerca de 6 mil" pela Kellogg; o slide 3, a legenda e o alt seguem a conclusão do artigo, 1.3: quem fechava
mais dívidas inteiras, qualquer que fosse o valor, tinha mais chance de quitar tudo, como pediu a checagem de fatos de
20/10/2026, e não a frase da divulgação da Kellogg sobre começar pelos menores saldos); teto do rotativo e do parcelamento da fatura, FATOS_2.md 4.1 e 4.3 (Lei
14.690/2023, art. 28, § 1º; Res. CMN 5.112/2023). Fato novo, procurado em fonte oficial em 20/10/2026 (não estava nos
FATOS): Código de Defesa do Consumidor, Lei 8.078/1990, art. 52, § 2º: "É assegurado ao consumidor a liquidação
antecipada do débito, total ou parcialmente, mediante redução proporcional dos juros e demais acréscimos." (Planalto).
Não usamos a medida provisória do Desenrola Brasil 3.0 (pode caducar) nem as médias de juros de agosto de 2026.

Tela real numa conta separada da conta principal de exemplo (equipes/fb/<cópia>, variantes.py, so_dividas), pedida
na revisão de 20/10/2026: só a "Conta corrente", de onde saem os pagamentos, e as 3 dívidas de exemplo, lançadas em
24/02/2027 como despesas "Parceladas" em "Dívidas e empréstimos", pendentes (1ª parcela em 25/02, 26/02 e 28/02), com a
mesma estrutura que o site grava pela "Nova transação" (conferida em explora_parcelada.py). Nenhum lançamento da conta
principal (nem o notebook, que o post de 26/02 cita como a única conta a vencer em fevereiro). "A pagar R$ 788,72 ·
3 transações" = R$ 93,78 + R$ 377,71 + R$ 317,23, a soma das 3 parcelas de um mês. Nenhum outro slide mostra tela."""

POST = {
    "pasta": "2027-02-24_dividas-qual-pagar-primeiro",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Qual dívida pagar primeiro: listar todas (saldo, parcela e juros ao mês), os dois jeitos de escolher onde pôr o dinheiro extra (a mais cara primeiro e a menor primeiro, com o estudo de Gal e McShane), um exemplo com 3 dívidas e R$ 300 a mais por mês, duas regras a favor (antecipar com desconto dos juros e o teto do rotativo e do parcelamento da fatura) e as parcelas em Pendentes",
    "pilar": "Educação · dívidas, com fonte oficial e produto",
    "data_longa": "quarta-feira, 24 de fevereiro de 2027",
    "data_curta": "quarta-feira, 24/02/2027",
    "data_mockup": "24 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-24T10:00:00",
    "slides": [
        "Capa (fundo papel) · DÍVIDAS · Qual dívida pagar primeiro? · Três colunas de dívida na altura do saldo, cada uma com a etiqueta dos juros em cima: Crediário da loja, R$ 800, “3% ao mês” (preta, baixa); Empréstimo pessoal, R$ 3.000, “7% ao mês” (coral, a mais cara, com a etiqueta coral); Financiamento do carro, R$ 6.000, “2% ao mês” (preta, a mais alta).",
        "PRIMEIRO PASSO · Liste todas. · Saldo, parcela e juros ao mês de cada uma. Os juros de um mês mostram quanto cada dívida custa. · Tabela: Crediário da loja, R$ 800, 10 × R$ 93,78, 3%, R$ 24 em 1 mês; Empréstimo pessoal (linha em destaque coral), R$ 3.000, 12 × R$ 377,71, 7%, R$ 210; Financiamento do carro, R$ 6.000, 24 × R$ 317,23, 2%, R$ 120. · Destaque: O tamanho engana: a dívida de R$ 3.000 custa mais por mês que a de R$ 6.000. · Nota: Dívidas e taxas de exemplo, com juros ao mês. Em 1 mês: saldo × taxa.",
        "DOIS JEITOS DE ESCOLHER · Pague a parcela de todas. O extra vai para uma só. · Duas colunas. A mais cara primeiro (o método avalanche; pela taxa, da maior à menor): 1 Empréstimo pessoal 7% ao mês, 2 Crediário da loja 3%, 3 Financiamento do carro 2%; “Paga menos juros.” A menor primeiro (a bola de neve; pelo saldo, do menor ao maior): 1 Crediário da loja R$ 800, 2 Empréstimo pessoal R$ 3.000, 3 Financiamento do carro R$ 6.000; “Uma dívida some antes.” · Cartão do estudo: Num estudo com cerca de 6 mil clientes de uma empresa de renegociação de dívidas, quem fechava mais dívidas inteiras, qualquer que fosse o valor, tinha mais chance de quitar tudo. Gal e McShane, 2012 · uma associação, não uma garantia.",
        "NO EXEMPLO · ALÉM DAS PARCELAS · Com R$ 300 a mais por mês. · A mais cara primeiro paga R$ 129 a menos de juros. A menor primeiro quita a primeira dívida 3 meses antes. · Três linhas do tempo na mesma escala, com um ponto colorido no mês em que cada dívida acaba: Só as parcelas, R$ 3.284 de juros, 1ª dívida quitada no 10º mês, tudo em 24 meses; A mais cara primeiro, R$ 1.764 de juros, 1ª no 6º mês, tudo em 11 meses; A menor primeiro, R$ 1.893 de juros, 1ª no 3º mês, tudo em 11 meses. Legenda: Crediário, Empréstimo, Carro. · Nota: Conta do exemplo: juros compostos ao mês e parcelas fixas; quando uma dívida acaba, a parcela dela vai para a próxima. Sem IOF e tarifas. Valores arredondados.",
        "O QUE A LEI GARANTE · Duas regras a seu favor. · Antecipar tem desconto: pagou parcelas antes, no todo ou em parte? Os juros e os acréscimos caem na proporção (Código de Defesa do Consumidor · Lei 8.078/1990, art. 52, § 2º). O cartão tem teto: no rotativo e no parcelamento da fatura, juros e encargos, somados, não passam do valor original da dívida (Lei 14.690/2023, art. 28, § 1º · Res. CMN 5.112/2023).",
        "NO TIMTIMCASH · Cada parcela no dia dela. · Lance cada dívida como Parcelada, em Dívidas e empréstimos. Pendentes mostra o que vence. · Destaque: As 3 parcelas do exemplo somam R$ 788,72 por mês. · Dois recortes da tela real de Pendentes no celular (relógio em 24/02/2027), numa conta de exemplo separada, só com a Conta corrente e as 3 dívidas: “A pagar R$ 788,72 · 3 transações”; e o cartão “A vencer · 3 transações ainda no prazo”: Amanhã, 25/02/2027, Crediário da loja (1/10), −R$ 93,78; Em 2 dias, 26/02, Empréstimo pessoal (1/12), −R$ 377,71; Em 4 dias, 28/02, Financiamento do carro (1/24), −R$ 317,23; todas pendentes. · Notas: Tela real do timtimcash, com dados de exemplo. Conta de exemplo só com as 3 dívidas.",
        "Fechamento (fundo verde) · Liste. Escolha a ordem. Comece pela primeira. · Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Várias dívidas ao mesmo tempo? A ordem de pagar faz diferença.\n\n"
        "Liste todas: saldo, parcela e juros ao mês. Pague a parcela de cada uma e ponha o dinheiro extra numa só. Qual? A mais cara primeiro paga menos juros. A menor primeiro fecha uma dívida antes: num estudo com cerca de 6 mil pessoas, quem fechava mais dívidas inteiras, qualquer que fosse o valor, tinha mais chance de quitar tudo.\n\n"
        "No exemplo, com 3 dívidas e R$ 300 a mais por mês, as duas ordens quitam tudo em 11 meses, contra 24 só com as parcelas. A mais cara primeiro paga R$ 129 a menos de juros; a menor primeiro quita a primeira dívida 3 meses antes.\n\n"
        "Antecipar parcelas reduz os juros na proporção: é direito do consumidor. E, no cartão, juros e encargos do rotativo e do parcelamento da fatura não passam do valor original da dívida.\n\n"
        "No timtimcash, lance cada dívida como Parcelada, em Dívidas e empréstimos, e veja as parcelas em Pendentes.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Gal e McShane, 2012; Lei 8.078/1990, art. 52; Lei 14.690/2023, art. 28.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#dividas #educacaofinanceira #financaspessoais #organizacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fevereiro fecha o primeiro bimestre, quando as parcelas do fim do ano e as contas de janeiro pesam. É a hora de pôr as dívidas na mesa e decidir por onde começar."),
        ("O que desperta interesse", "Uma pergunta prática na capa e uma resposta com números: as duas ordens, lado a lado, num exemplo que mostra o custo e o tempo de cada uma."),
        ("Benefício para o público", "Aprende a listar as dívidas, a comparar pelo custo de um mês, a escolher entre a mais cara e a menor primeiro sabendo o que ganha com cada uma, e conhece dois direitos: o desconto ao antecipar e o teto do cartão."),
        ("Como contribui para o perfil", "Continua a série de crédito (11/11 e 10/12) com um ângulo novo, a ordem de pagar, com fonte oficial e um estudo citado com cuidado, e mostra como acompanhar as parcelas em Pendentes."),
    ],
    "alt": [
        "Dívidas. Qual dívida pagar primeiro? Três colunas na altura do saldo de cada dívida: crediário da loja, 800 reais, a 3% ao mês, a mais baixa; empréstimo pessoal, 3.000 reais, a 7% ao mês, em coral, a mais cara; financiamento do carro, 6.000 reais, a 2% ao mês, a mais alta.",
        "Primeiro passo: liste todas, com saldo, parcela e juros ao mês. Tabela de exemplo: crediário da loja, 800 reais, 10 parcelas de 93,78, 3% ao mês, 24 reais de juros em um mês; empréstimo pessoal, 3.000 reais, 12 de 377,71, 7%, 210 reais em um mês; financiamento do carro, 6.000 reais, 24 de 317,23, 2%, 120 reais em um mês. O tamanho engana: a dívida de 3.000 custa mais por mês que a de 6.000.",
        "Dois jeitos de escolher. Pague a parcela de todas e ponha o extra numa só. A mais cara primeiro, o método avalanche, pela taxa: empréstimo pessoal, crediário, financiamento; paga menos juros. A menor primeiro, a bola de neve, pelo saldo: crediário, empréstimo, financiamento; uma dívida some antes. Num estudo com cerca de 6 mil clientes de uma empresa de renegociação de dívidas, quem fechava mais dívidas inteiras, qualquer que fosse o valor, tinha mais chance de quitar tudo; é uma associação, não uma garantia. Gal e McShane, 2012.",
        "No exemplo, com 300 reais a mais por mês além das parcelas. Três linhas do tempo: só as parcelas, 3.284 reais de juros e tudo quitado em 24 meses; a mais cara primeiro, 1.764 reais de juros, a primeira dívida quitada no 6º mês e tudo em 11 meses; a menor primeiro, 1.893 reais de juros, a primeira dívida quitada no 3º mês e tudo em 11 meses. Conta simplificada, sem IOF e tarifas.",
        "Duas regras a seu favor. Antecipar tem desconto: quem paga parcelas antes, no todo ou em parte, tem redução proporcional dos juros e acréscimos, pelo Código de Defesa do Consumidor, artigo 52. O cartão tem teto: no rotativo e no parcelamento da fatura, juros e encargos somados não passam do valor original da dívida, pela Lei 14.690/2023.",
        "No timtimcash: cada parcela no dia dela. Lance cada dívida como Parcelada, em Dívidas e empréstimos, e veja em Pendentes o que vence. As 3 parcelas do exemplo somam 788,72 reais por mês. Recortes da tela real de Pendentes no celular, numa conta de exemplo só com as 3 dívidas: a pagar, 788,72 reais, 3 transações; amanhã, crediário da loja, 93,78 reais; em 2 dias, empréstimo pessoal, 377,71; em 4 dias, financiamento do carro, 317,23; todas pendentes.",
        "Liste. Escolha a ordem. Comece pela primeira. Pendentes no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Gal, D.; McShane, B. B. Can Small Victories Help Win the War? Evidence from Consumer Debt Management. Journal of Marketing Research, v. 49, n. 4, p. 487-501, 2012 (resumo: fechar contas prevê a saída da dívida, qualquer que fosse o saldo das contas fechadas)", "https://journals.sagepub.com/doi/10.1509/jmr.11.0272"),
        ("Kellogg Insight, 8/1/2014: dados de quase 6.000 clientes de uma empresa de renegociação de dívidas; os autores avisam que número de contas fechadas e valor quitado andam juntos", "https://insight.kellogg.northwestern.edu/article/to_beat_debt_consider_starting_small"),
        ("Kellogg News, 2012: divulgação do estudo, com os dados de 6.000 pessoas", "https://www.kellogg.northwestern.edu/news_articles/2012/snowball-approach.aspx"),
        ("Planalto · Código de Defesa do Consumidor, Lei nº 8.078/1990, art. 52, § 2º (liquidação antecipada, total ou parcial, com redução proporcional dos juros e demais acréscimos), conferido em 20/10/2026", "https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm"),
        ("Planalto · Lei nº 14.690/2023, art. 28, § 1º (juros e encargos do rotativo e do parcelamento da fatura limitados ao valor original da dívida)", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14690.htm"),
        ("Banco Central · Resolução CMN nº 5.112/2023 (regulamenta o teto; vale para as operações feitas depois de 90 dias da lei)", "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20CMN&numero=5112"),
    ],
    "telas": [
        "telas/celular-pendentes-dividas-conta-separada-24-02.png · Menu › Pendentes no celular, relógio em 24/02/2027 10:00, build 2026-10-19.5, numa conta separada (equipes/fb, variantes.py, so_dividas: só a Conta corrente e as 3 dívidas de exemplo lançadas como Parceladas em Dívidas e empréstimos, nenhum lançamento da conta principal), 390 × 1000 em escala 3: A pagar R$ 788,72 (3 transações); Nada vencido; A vencer: 25/02 Crediário da loja · 3% ao mês (1/10) −R$ 93,78; 26/02 Empréstimo pessoal · 7% ao mês (1/12) −R$ 377,71; 28/02 Financiamento do carro · 2% ao mês (1/24) −R$ 317,23 (no celular, os nomes aparecem cortados) · slide 6 (recortes do valor A pagar e do cartão A vencer)",
    ],
}
