# -*- coding: utf-8 -*-
"""Quarta 11/11/2026 · carrossel "Pagou o mínimo. E o resto?" (educação, crédito, capa papel). Equipe c1.
Artes: saida/2026-11-11_pagou-o-minimo-da-fatura/01.jpg a 07.jpg, geradas por equipes/c1/posts.py (post_minimo).
Taxas: FATOS.md (Banco Central, nota de 29/9/2026): rotativo de agosto de 2026, 15,18% ao mês e 444,89% ao ano; cheque
especial, 7,43% ao mês e 136,41% ao ano; teto do cheque especial, 8% ao mês (Res. CMN 4.765/2019, desde 6/1/2020);
teto do rotativo e do parcelamento da fatura: juros e encargos não passam do valor original (Lei 14.690/2023, art. 28,
operações desde 3/1/2024). Exemplo do slide 3 (assert em posts.py): R$ 1.000 × 15,18% = R$ 151,80 de juros em um mês.
Nenhum valor de pagamento mínimo aparece (depende do emissor).
Telas reais em saida/2026-11-11_pagou-o-minimo-da-fatura/telas/, capturadas por equipes/c1/captura_cartao.py, relógio em
11/11/2026 10:00, no build 2026-10-16.1 do site (recapturadas em 16/10/2026), na cópia da conta da equipe (estado.py
da pasta da equipe, equipes/c1). Mudanças nessa cópia, e só nela:
- o "Cartão principal" dos posts de outubro (17/10 e 26/10): limite R$ 8.000, fecha no dia 3, vence no dia 10, pago pela
  Conta corrente (id 7001);
- quatro compras de novembro que já existiam na conta passam a ser pagas nesse cartão (o mesmo lançamento, data,
  categoria e valor; muda só o "Pago via"): Combustível 04/11 R$ 388,00, Restaurante 06/11 R$ 182,00, Mercado da Vila
  09/11 R$ 468,10 e Farmácia 09/11 R$ 54,90. Gravadas como o site grava uma compra no cartão feita pela "Nova
  transação" (contaId da conta que paga e cartaoId), conferido criando uma compra pela interface.
Os totais do mês e de cada categoria não mudam (equipes/c1/confere_conta.py). Fatura atual: R$ 1.093,00, de 04/nov a
03/dez, vence 10/dez/26; Limite usado R$ 1.093,00; Disponível R$ 6.907,00 de R$ 8.000,00. Como as compras no cartão
só saem da Conta corrente quando a fatura é paga, o saldo da Conta corrente nessa cópia, em 11/11, fica R$ 1.093,00
maior que na conta de base (nenhuma tela usada mostra esse saldo)."""

POST = {
    "pasta": "2026-11-11_pagou-o-minimo-da-fatura",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Pagou o mínimo da fatura: o resto vira crédito rotativo, com juros; a taxa média do rotativo em agosto de 2026 (15,18% ao mês, 444,89% ao ano); o teto de juros e encargos do rotativo e do parcelamento da fatura (R$ 1.000 viram, no máximo, R$ 2.000); o teto de 8% ao mês do cheque especial; e o cartão no timtimcash, com a fatura atual, o limite usado, o disponível e a fatura não paga em Pendentes",
    "pilar": "Educação · crédito",
    "data_longa": "quarta-feira, 11 de novembro de 2026",
    "data_curta": "quarta-feira, 11/11/2026",
    "data_mockup": "11 de novembro",
    "hora": "10h00",
    "iso": "2026-11-11T10:00:00",
    "slides": [
        "Capa (fundo papel) · CARTÃO DE CRÉDITO · Pagou o mínimo. E o resto? · Cartão de fatura: Total da fatura R$ 1.000,00, com uma barra em que um pedaço pequeno verde é “o que você pagou” e o resto, em coral, “vai para o rotativo”. Sem valor de pagamento mínimo.",
        "O RESTO · O que não é pago vira rotativo. · Pagou menos que o total? O saldo vira um financiamento: o crédito rotativo, com juros. · Ilustração: esta fatura, com a parte paga e o resto; o resto vira rotativo, com juros, e aparece na próxima fatura, com os juros somados. · Nota: Ilustração, sem valores: o pagamento mínimo depende do emissor do cartão.",
        "QUANTO CUSTA · A taxa média do rotativo em agosto de 2026. · 15,18% ao mês, em destaque; no ano, 444,89%. · Na taxa média, R$ 1.000 no rotativo geram R$ 151,80 de juros em um mês. · Nota: Taxa média do rotativo do cartão, pessoa física, agosto de 2026. Fonte: Banco Central, nota de 29/9/2026 (séries 25477 e 22022).",
        "TEM TETO · Os juros não passam do valor da dívida. · Rotativo e parcelamento da fatura somados: R$ 1.000 viram, no máximo, R$ 2.000. · Barra: a dívida, R$ 1.000, mais juros e encargos somados, até R$ 1.000: no máximo R$ 2.000. · Nota: Para o rotativo e o parcelamento da fatura contratados desde 3/1/2024. Lei 14.690/2023, art. 28; Res. CMN 4.549/2017, com a Res. CMN 5.112/2023.",
        "CHEQUE ESPECIAL · Também tem teto: 8% ao mês. · E a média de agosto ficou perto dele. · Média de agosto de 2026: 7,43%; teto: 8%, numa régua de 0% a 8% ao mês; a média, no ano: 136,41%. · Nota: Teto desde 6/1/2020: Res. CMN 4.765/2019, art. 3º. Fonte das médias: Banco Central, nota de 29/9/2026 (séries 25463 e 20741).",
        "NO TIMTIMCASH · A fatura antes de vencer. · Cada cartão mostra a fatura atual, o “Limite usado” e o “Disponível”. A fatura não paga aparece em Pendentes. · Telas reais no celular, relógio em 11/11/2026: “Cartão principal”, fecha 3, vence 10, paga via Conta corrente; Limite usado R$ 1.093,00; Disponível R$ 6.907,00 de R$ 8.000,00; Fatura atual, aberta, 04/nov a 03/dez, vence 10/dez/26, R$ 1.093,00. Em Pendentes de dezembro: Faturas (1), Cartão principal, “Fatura em aberto · vence 10/dez/…” (a data aparece cortada no celular), R$ 1.093,00. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Veja a fatura antes que ela vire rotativo. · Cartões de crédito no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Pagou o mínimo da fatura? O resto não some: vira crédito rotativo, com juros.\n\n"
        "Em agosto de 2026, a taxa média do rotativo do cartão foi de 15,18% ao mês, ou 444,89% ao ano, segundo o Banco Central. Na taxa média, R$ 1.000 no rotativo geram R$ 151,80 de juros em um mês.\n\n"
        "Desde janeiro de 2024 há um teto: juros e encargos do rotativo e do parcelamento da fatura, somados, não passam do valor original da dívida. R$ 1.000 viram, no máximo, R$ 2.000. O cheque especial também tem teto, de 8% ao mês, e a média de agosto foi de 7,43% ao mês.\n\n"
        "No timtimcash, cada cartão mostra a fatura atual, o limite usado e o disponível, e a fatura que não foi paga aparece em Pendentes.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Banco Central (nota de 29/9/2026); Lei 14.690/2023; Res. CMN 4.765/2019.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#cartaodecredito #juros #educacaofinanceira #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Meio de novembro, a duas semanas da Black Friday e antes das compras de fim de ano: é a hora de saber o que acontece com a fatura que não é paga inteira. A taxa de agosto de 2026 é a mais recente publicada pelo Banco Central (nota de 29/9/2026)."),
        ("O que desperta interesse", "A pergunta da capa é a que a própria fatura provoca, e o slide 3 traz um número grande e real: 15,18% ao mês. O teto, que pouca gente conhece, vira uma imagem simples: R$ 1.000 viram, no máximo, R$ 2.000."),
        ("Benefício para o público", "Entende o que acontece com o que não é pago, quanto isso custa em média, que existe teto para o rotativo e para o cheque especial, e onde acompanhar a fatura antes do vencimento. Sem recomendar banco nem produto e sem citar valor de pagamento mínimo."),
        ("Como contribui para o perfil", "Educação de crédito com fonte oficial que termina numa função concreta, com tela real: o mesmo “Cartão principal” dos posts de outubro, agora com compras, limite usado, disponível e a fatura em Pendentes."),
    ],
    "alt": [
        "Cartão de crédito. Pagou o mínimo. E o resto? Cartão de fatura com o total de R$ 1.000,00 e uma barra: um pedaço pequeno em verde, o que você pagou, e o resto em coral, que vai para o rotativo.",
        "O resto. O que não é pago vira rotativo. Pagou menos que o total? O saldo vira um financiamento, o crédito rotativo, com juros. Ilustração: nesta fatura, uma parte paga e o resto; na próxima fatura, o resto aparece de novo, com os juros somados. Sem valores: o pagamento mínimo depende do emissor do cartão.",
        "Quanto custa. A taxa média do rotativo em agosto de 2026: 15,18% ao mês; no ano, 444,89%. Na taxa média, R$ 1.000 no rotativo geram R$ 151,80 de juros em um mês. Taxa média do rotativo do cartão para pessoa física, segundo o Banco Central.",
        "Tem teto. Os juros não passam do valor da dívida. Rotativo e parcelamento da fatura somados: R$ 1.000 viram, no máximo, R$ 2.000. Barra com a dívida de R$ 1.000 e, ao lado, juros e encargos somados de até R$ 1.000. Vale para o que foi contratado desde 3 de janeiro de 2024, pela Lei 14.690 de 2023.",
        "Cheque especial. Também tem teto: 8% ao mês. E a média de agosto de 2026 ficou perto dele: 7,43% ao mês, numa régua de 0% a 8%; no ano, a média foi de 136,41%. Teto desde 6 de janeiro de 2020, pela Resolução CMN 4.765 de 2019.",
        "No timtimcash, a fatura antes de vencer. Cada cartão mostra a fatura atual, o limite usado e o disponível, e a fatura não paga aparece em Pendentes. Telas reais no celular, com dados de exemplo, em 11 de novembro de 2026: Cartão principal, que fecha no dia 3 e vence no dia 10; limite usado de R$ 1.093,00; disponível de R$ 6.907,00, de R$ 8.000,00; fatura atual aberta, de 4 de novembro a 3 de dezembro, vence em 10 de dezembro, R$ 1.093,00. Em Pendentes, a fatura em aberto do Cartão principal, de R$ 1.093,00.",
        "Veja a fatura antes que ela vire rotativo. Cartões de crédito no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Banco Central · Estatísticas monetárias e de crédito, nota de 29/9/2026 (agosto de 2026: rotativo do cartão, séries SGS 25477 e 22022; cheque especial, séries SGS 25463 e 20741)", "https://www.bcb.gov.br/content/estatisticas/hist_estatisticasmonetariascredito/202609_Texto_de_estatisticas_monetarias_e_de_credito.pdf"),
        ("Planalto · Lei nº 14.690/2023, art. 28 (juros e encargos do rotativo e do parcelamento da fatura limitados ao valor original da dívida)", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14690.htm"),
        ("Banco Central · Resolução CMN nº 4.765/2019, art. 3º (teto de 8% ao mês nos juros do cheque especial)", "https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50875/Res_4765_v2_P.pdf"),
    ],
    "telas": [
        "telas/celular-cartao-principal-11-11.png · Menu › “Cartões de crédito” › “Cartão principal” no celular, relógio em 11/11/2026 10:00, build 2026-10-16.1, na cópia da conta da equipe c1 (390 × 844 em escala 3): “Fecha 3 · Vence 10 · paga via Conta corrente”, Limite usado R$ 1.093,00, Disponível R$ 6.907,00 de R$ 8.000,00, Fatura atual ABERTA, 04/nov a 03/dez, vence 10/dez/26, R$ 1.093,00 (Mercado da Vila R$ 468,10, Farmácia R$ 54,90, Restaurante R$ 182,00 e Combustível R$ 388,00) · slide 6 (recorte até o cabeçalho da fatura)",
        "telas/celular-pendentes-dezembro-11-11.png · Pendentes, uma seta adiante (Dezembro 2026), mesmo relógio e mesma cópia: “Faturas (1) · Cartão principal · Fatura em aberto · vence 10/dez/26 · R$ 1.093,00” (no celular, a data aparece cortada: “vence 10/dez/…”), A pagar R$ 4.962,80 (5 transações e 1 fatura) · slide 6 (recorte do bloco Faturas)",
        "telas/celular-cartoes-de-credito-11-11.png e telas/celular-pendentes-novembro-11-11.png · a lista de cartões (“R$ 1.093,00 de R$ 8.000,00 · vence 10/dez · paga via Conta corrente”) e Pendentes de novembro, sem fatura (referência, não usadas nas artes)",
    ],
}
