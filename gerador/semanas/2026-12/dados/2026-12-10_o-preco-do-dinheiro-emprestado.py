# -*- coding: utf-8 -*-
"""Quinta 10/12/2026 · carrossel "O preço do dinheiro emprestado" (educação, crédito, capa verde suave). Equipe dc1.
Artes: saida/2026-12-10_o-preco-do-dinheiro-emprestado/01.jpg a 07.jpg, geradas por equipes/dc1/posts.py (post_juros).
Taxas: Banco Central, estatísticas monetárias e de crédito, agosto de 2026 (o mês mais recente publicado em 16/10/2026; nota
à imprensa de 29/9/2026), taxas médias de juros das novas operações para pessoa física. Valores lidos nas séries SGS
(api.bcb.gov.br) em 16/10/2026, cada um conferido em duas leituras e entre a série ao mês e a série ao ano; nomes das séries
conferidos em dadosabertos.bcb.gov.br:
  rotativo do cartão 15,18% a.m. (SGS 25477) e 444,89% a.a. (22022) · parcelado do cartão 9,34% (25478) e 192,08% (22023) ·
  cheque especial 7,43% (25463) e 136,41% (20741) · crédito pessoal não consignado 6,39% (25464) e 110,22% (20742) ·
  consignado setor privado 3,79% (25466) e 56,34% (20744) · aquisição de veículos 1,97% (25471) e 26,42% (20749) ·
  consignado setor público 1,82% (25467) e 24,14% (20745) · consignado INSS 1,82% (25468) e 24,12% (20746) ·
  imobiliário com taxas de mercado, crédito direcionado, 1,12% (25497) e 14,24% (20772).
ATENÇÃO: os dados de setembro saem no fim de outubro e os de outubro no fim de novembro; antes de agendar, conferir se o
revisor quer atualizar para o mês mais novo (as contas do post dependem destas taxas).
Contas (assert em posts.py): 444,89 ÷ 14,24 = 31,2 ("31 vezes"); R$ 1.000 por 12 meses sem pagamentos: R$ 1.142,40 no
imobiliário e R$ 5.448,90 no rotativo pela taxa, limitado a R$ 2.000 pelo teto (diferença de R$ 857,60 mesmo com o teto);
12 × 6,39% = 76,68%, 12 × 7,43% = 89,16%, 12 × 15,18% = 182,16%; crédito pessoal: R$ 1.000 em 12 parcelas iguais a 6,39% a.m.
(tabela Price, sem IOF e tarifas) = 12 × R$ 121,84 = R$ 1.462,08.
Tela real em saida/2026-12-10_o-preco-do-dinheiro-emprestado/telas/, capturada por equipes/dc1/captura.py na conta de base
(N/base_app, sem mudança), build 2026-10-16.1, relógio em 10/12/2026 10:00: "Nova transação" preenchida e fechada sem salvar."""

POST = {
    "pasta": "2026-12-10_o-preco-do-dinheiro-emprestado",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "O preço do dinheiro emprestado: as taxas médias de juros para pessoa física em agosto de 2026 (Banco Central), do rotativo do cartão ao imobiliário, a diferença em reais, os tetos do rotativo e do cheque especial e como lançar um empréstimo parcelado",
    "pilar": "Educação · crédito, com fonte oficial e produto",
    "data_longa": "quinta-feira, 10 de dezembro de 2026",
    "data_curta": "quinta-feira, 10/12/2026",
    "data_mockup": "10 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-10T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · JUROS DO CRÉDITO · O preço do dinheiro emprestado. · Nove barras horizontais com o comprimento das taxas médias ao ano de agosto de 2026, da maior para a menor: a primeira, em coral, ocupa a largura toda, “444,89% ao ano”; as sete do meio, em verde escuro, cada vez menores; a última, verde e mínima, “14,24%”.",
        "TAXA MÉDIA AO ANO · AGOSTO DE 2026 · A mais cara é 31 vezes a mais barata. · Ranking em barras, pessoa física, com a taxa ao mês embaixo de cada nome: Rotativo do cartão 444,89% (15,18% ao mês); Parcelado do cartão 192,08% (9,34%); Cheque especial 136,41% (7,43%); Crédito pessoal 110,22% (6,39%); Consignado privado 56,34% (3,79%); Veículos 26,42% (1,97%); Consignado público 24,14% (1,82%); Consignado INSS 24,12% (1,82%); Imobiliário 14,24% (1,12%). · Nota: Pessoa física, agosto de 2026. Banco Central, nota de 29/9/2026. Imobiliário: taxas de mercado.",
        "AO MÊS E AO ANO · Ao mês parece pouco. No ano, não. · Os juros de um mês entram na dívida do mês seguinte. · Três linhas: Crédito pessoal, 6,39% ao mês → 110,22% ao ano, e não 12 × 6,39% = 76,68%; Cheque especial, 7,43% ao mês → 136,41% ao ano, e não 12 × 7,43% = 89,16%; Rotativo do cartão, 15,18% ao mês → 444,89% ao ano, e não 12 × 15,18% = 182,16%. · Nota: Taxas médias de agosto de 2026, pessoa física (Banco Central).",
        "R$ 1.000 POR 12 MESES · O mais barato e o mais caro, em reais. · Sem pagar nada no meio, só com os juros de cada taxa média. · Imobiliário, 14,24% ao ano: R$ 1.142,40 (a dívida de R$ 1.000 em preto e os juros em verde). Rotativo, 444,89% ao ano: pela taxa, R$ 5.448,90 (riscado); a barra para no teto de R$ 2.000 (a dívida em preto, os juros até o teto em coral e, listrado, o que o teto corta). Mesmo com o teto, o rotativo custa a mais R$ 857,60. · Nota: Conta simples: só juros, sem IOF e tarifas. No contrato, compare o CET, que soma tudo (Res. CMN 4.881/2020).",
        "OS TETOS · Dois limites que já estão na lei. · Rotativo e parcelamento da fatura: R$ 1.000 de dívida viram, no máximo, R$ 2.000 (juros e encargos, somados, até o valor da dívida · desde 3/1/2024 · Lei 14.690/2023, art. 28). Cheque especial: 8% ao mês, no máximo; régua com a média de agosto de 2026, 7,43%, perto do teto de 8% (desde 6/1/2020 · Res. CMN 4.765/2019, art. 3º).",
        "NO TIMTIMCASH · Lance o total. As parcelas aparecem mês a mês. · Em “Dívidas e empréstimos”, com Recorrência “Parcelada”, cada parcela fica em Pendentes no mês dela. · Exemplo: R$ 1.000 no crédito pessoal, à taxa média (6,39% ao mês), em 12 parcelas: 12 × R$ 121,84 = R$ 1.462,08. · Tela real de “Nova transação” no celular, relógio em 10/12/2026: Despesa; Valor R$ 1.462,08; Data 10/01/2027; “Marcar como pago” desligado; Categoria Dívidas e empréstimos; Pago via Conta corrente; “Empréstimo pessoal”; Recorrência Parcelada; Nº parcelas 12; A cada Meses; “12× de R$ 121,84 · mensal”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Antes de assinar, faça a conta inteira. · Dívidas e empréstimos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "O mesmo R$ 1.000 emprestado pode custar pouco ou muito. Depende da linha de crédito.\n\n"
        "Em agosto de 2026, segundo o Banco Central, a taxa média para pessoa física foi de 444,89% ao ano no rotativo do cartão e de 14,24% ao ano no imobiliário: 31 vezes de diferença. No meio, o parcelado do cartão (192,08%), o cheque especial (136,41%), o crédito pessoal (110,22%), os veículos (26,42%) e o consignado (de 24,12% a 56,34%).\n\n"
        "Ao mês parece pouco: 6,39% ao mês no crédito pessoal são 110,22% ao ano. R$ 1.000 por 12 meses, sem pagar nada, viram R$ 1.142,40 no imobiliário. No rotativo, a lei põe um teto: no máximo R$ 2.000. O cheque especial tem teto de 8% ao mês.\n\n"
        "No timtimcash, lance o total do empréstimo em Dívidas e empréstimos, com a Recorrência Parcelada: cada parcela aparece em Pendentes no mês dela.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Banco Central (agosto de 2026); Lei 14.690/2023; Res. CMN 4.765/2019.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#juros #credito #educacaofinanceira #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Dezembro concentra gastos de fim de ano e a tentação do crédito fácil (cheque especial, rotativo, parcelamentos). Mostrar o preço de cada linha antes das compras ajuda a escolher, ou a evitar, a dívida mais cara."),
        ("O que desperta interesse", "Um ranking visual com números oficiais, em que a barra do rotativo é 31 vezes a do imobiliário, e a conta simples que traduz porcentagens em reais."),
        ("Benefício para o público", "Entende a diferença entre taxa ao mês e ao ano, sabe quais linhas costumam ser mais caras e mais baratas, conhece os tetos do rotativo e do cheque especial e aprende a comparar pelo CET."),
        ("Como contribui para o perfil", "Reforça o pilar de educação com fonte oficial (Banco Central, com as séries SGS) e mostra, em tela real, como acompanhar um empréstimo parcelado no timtimcash, sem recomendar banco nem produto."),
    ],
    "alt": [
        "Juros do crédito. O preço do dinheiro emprestado. Nove barras horizontais, da maior para a menor, com as taxas médias ao ano de agosto de 2026: a primeira, em coral, ocupa a largura toda, 444,89% ao ano; as do meio, em verde escuro, vão diminuindo; a última é mínima, 14,24%.",
        "Taxa média ao ano de agosto de 2026, pessoa física: a mais cara é 31 vezes a mais barata. Ranking: rotativo do cartão, 444,89% ao ano, 15,18% ao mês; parcelado do cartão, 192,08%; cheque especial, 136,41%; crédito pessoal, 110,22%; consignado privado, 56,34%; veículos, 26,42%; consignado público, 24,14%; consignado do INSS, 24,12%; imobiliário, 14,24% ao ano, 1,12% ao mês. Fonte: Banco Central.",
        "Ao mês parece pouco. No ano, não: os juros de um mês entram na dívida do mês seguinte. Crédito pessoal: 6,39% ao mês são 110,22% ao ano, e não 76,68%. Cheque especial: 7,43% ao mês são 136,41% ao ano, e não 89,16%. Rotativo do cartão: 15,18% ao mês são 444,89% ao ano, e não 182,16%.",
        "R$ 1.000 por 12 meses: o mais barato e o mais caro, em reais, sem pagar nada no meio e só com os juros. No imobiliário, a 14,24% ao ano, viram R$ 1.142,40. No rotativo, a 444,89% ao ano, a taxa levaria a R$ 5.448,90, mas o teto da lei para a conta em R$ 2.000. Mesmo com o teto, o rotativo custa R$ 857,60 a mais. Conta simples, sem IOF e tarifas; no contrato, compare o CET.",
        "Os tetos: dois limites que já estão na lei. Rotativo e parcelamento da fatura: R$ 1.000 de dívida viram, no máximo, R$ 2.000, porque juros e encargos, somados, não passam do valor da dívida, desde janeiro de 2024. Cheque especial: no máximo 8% ao mês, desde janeiro de 2020; a média de agosto de 2026 foi de 7,43%, perto do teto.",
        "No timtimcash: lance o total, e as parcelas aparecem mês a mês. Em Dívidas e empréstimos, com recorrência Parcelada, cada parcela fica em Pendentes no mês dela. Exemplo: R$ 1.000 no crédito pessoal, à taxa média de 6,39% ao mês, em 12 parcelas de R$ 121,84, R$ 1.462,08 no total. Tela real do formulário Nova transação no celular, com dados de exemplo: despesa de R$ 1.462,08, data 10 de janeiro de 2027, categoria Dívidas e empréstimos, descrição Empréstimo pessoal, parcelada em 12 meses, 12 vezes de R$ 121,84.",
        "Antes de assinar, faça a conta inteira. Dívidas e empréstimos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Banco Central · Estatísticas monetárias e de crédito, nota à imprensa de 29/9/2026 (agosto de 2026)", "https://www.bcb.gov.br/content/estatisticas/hist_estatisticasmonetariascredito/202609_Texto_de_estatisticas_monetarias_e_de_credito.pdf"),
        ("Banco Central · SGS 22022 (% a.a.) e 25477 (% a.m.), rotativo do cartão, pessoa física: 444,89% e 15,18% em agosto de 2026 (lido em 16/10/2026)", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.22022/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 22023 e 25478, parcelado do cartão: 192,08% e 9,34%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.22023/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 20741 e 25463, cheque especial: 136,41% e 7,43%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20741/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 20742 e 25464, crédito pessoal não consignado: 110,22% e 6,39%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20742/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 20744 e 25466, consignado para trabalhadores do setor privado: 56,34% e 3,79%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20744/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 20749 e 25471, aquisição de veículos: 26,42% e 1,97%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20749/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 20745 e 25467, consignado para trabalhadores do setor público: 24,14% e 1,82%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20745/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 20746 e 25468, consignado para aposentados e pensionistas do INSS: 24,12% e 1,82%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20746/dados/ultimos/1?formato=json"),
        ("Banco Central · SGS 20772 e 25497, financiamento imobiliário com taxas de mercado (crédito direcionado): 14,24% e 1,12%", "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20772/dados/ultimos/1?formato=json"),
        ("Banco Central · Dados abertos, descrição das séries (exemplo: SGS 25464, crédito pessoal não consignado, % ao mês)", "https://dadosabertos.bcb.gov.br/dataset/25464-taxa-media-mensal-de-juros-das-operacoes-de-credito-com-recursos-livres---pessoas-fisicas---c"),
        ("Planalto · Lei nº 14.690/2023, art. 28, § 1º (juros e encargos do rotativo e do parcelamento da fatura limitados ao valor original da dívida)", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14690.htm"),
        ("Banco Central · Resolução CMN nº 4.549/2017, arts. 1º, 2º e 2º-A a 2º-D (rotativo até a fatura seguinte; parcelamento; teto pela Res. CMN 5.112/2023)", "https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50330/Res_4549_v2_L.pdf"),
        ("Banco Central · Resolução CMN nº 4.765/2019, art. 3º (teto de 8% ao mês no cheque especial)", "https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50875/Res_4765_v2_P.pdf"),
        ("Banco Central · Resolução CMN nº 4.881/2020, arts. 3º, 4º e 7º (CET: juros, tarifas, tributos, seguros e outras despesas, em taxa anual, informado antes da contratação)", "https://www.bcb.gov.br/content/estabilidadefinanceira/especialnor/Resolu%C3%A7%C3%A3o4881.pdf"),
    ],
    "telas": [
        "telas/celular-nova-despesa-parcelada-10-12.png · “Nova transação” (botão + da Visão geral) no celular, relógio em 10/12/2026 10:00, build 2026-10-16.1, conta de base sem mudança (390 × 1000 em escala 3), preenchida pela interface e fechada sem salvar: Despesa; Valor R$ 1.462,08; Data 10/01/2027 (seta do calendário para janeiro); o interruptor “Já foi pago” tocado e desligado (“Marcar como pago · Fica como pendente até você confirmar”); Categoria “Dívidas e empréstimos”; Pago via Conta corrente; descrição “Empréstimo pessoal”; Recorrência “Parcelada”; Nº parcelas 12; A cada Meses; resumo “12× de R$ 121,84 · mensal” · slide 6 (recorte do valor ao resumo das parcelas)",
    ],
}
