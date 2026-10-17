# -*- coding: utf-8 -*-
"""Quarta 23/12/2026 · carrossel "Viagem: o IOF é igual. O câmbio, não." (educação, exterior, capa tinta).
Artes: saida/2026-12-23_viagem-para-fora-o-iof/01.jpg a 07.jpg, geradas por equipes/dc2/posts.py (contas por assert).
Fatos: FATOS.md (IOF no câmbio, Decreto 6.306/2007, art. 15-B, com a redação do Decreto 12.499/2025), conferidos de novo pela
equipe dc2 no texto compilado do Planalto em 16/10/2026: VII (aquisição de bens e serviços do exterior com os instrumentos de
arranjos de pagamento de abrangência transfronteiriça, ou seja, o cartão usado lá fora, de crédito ou de débito) 3,5%; IX (saques
no exterior) 3,5%; X (cheques de viagem e carregamento de cartão internacional pré-pago) 3,5%; XX (moeda estrangeira em espécie)
3,5%; XXI (remessa para disponibilidade própria no exterior) 3,5%; XXI-A (remessa com finalidade de investimento) 1,10%.
VET: definição e ranking do Banco Central (página do Ranking do VET e Portal de Dados Abertos, consultados em 16/10/2026):
"O Valor Efetivo Total (VET) representa o custo de uma operação de câmbio em reais por moeda estrangeira, englobando a taxa de
câmbio, as tarifas e tributos incidentes sobre essa operação"; "Os valores deste ranking referem-se a meses anteriores"; "As
instituições não são obrigadas a praticar, no presente, os valores divulgados nesta página". A página não carregou dados na
consulta (só o modelo), então o post não cita nenhum VET nem instituição.
Contas: US$ 1.000 × R$ 5,05 = R$ 5.050,00; IOF de 3,5% = R$ 176,75; total R$ 5.226,75. Câmbios hipotéticos de R$ 5,15 e R$ 5,25:
R$ 5.330,25 e R$ 5.433,75 (+R$ 103,50 e +R$ 207,00; cada R$ 0,10 no câmbio custa R$ 100 + 3,5% = R$ 103,50 em US$ 1.000).
Tela real nova em saida/2026-12-23_viagem-para-fora-o-iof/telas/, capturada por equipes/dc2/captura.py na conta de N/base_app
(build 2026-10-16.1), relógio em 23/12/2026 10:00: Orçamentos › "Definir limites", busca "Viagem" e R$ 5.300,00 digitados,
sem salvar (a conta não muda). R$ 5.300 = os US$ 1.000 do exemplo com IOF (R$ 5.226,75), arredondados para cima."""

POST = {
    "pasta": "2026-12-23_viagem-para-fora-o-iof",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Para gastar numa viagem ao exterior, o IOF é de 3,5% no cartão (crédito ou débito), no saque, no pré-pago, na moeda em espécie e na remessa para conta própria (1,10% só na remessa para investir); a conta do IOF em US$ 1.000; o que muda é o câmbio e as tarifas, e o VET do Banco Central compara o custo total; no timtimcash, um limite para a categoria Viagem em Orçamentos",
    "pilar": "Investimento no exterior · educação com fonte oficial",
    "data_longa": "quarta-feira, 23 de dezembro de 2026",
    "data_curta": "quarta-feira, 23/12/2026",
    "data_mockup": "23 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-23T10:00:00",
    "slides": [
        "Capa (fundo tinta, logotipo de fundo escuro) · VIAGEM AO EXTERIOR · Viagem: o IOF é igual. O câmbio, não. (a última frase em menta) · Quatro blocos escuros, cada um com um ícone de traço em menta e “3,5%” enorme em branco: cartão; dinheiro em espécie; cartão pré-pago; conta sua lá fora.",
        "IOF NO CÂMBIO · Para gastar lá fora, 3,5% em todas. · Cartão no exterior (crédito ou débito) 3,5%; Saque no exterior 3,5%; Cartão pré-pago e cheques de viagem 3,5%; Dinheiro em espécie 3,5%; Remessa para uma conta sua lá fora 3,5%; faixa verde suave: Remessa para investir, não é dinheiro para gastar na viagem, 1,10%. · Nota: Decreto 6.306/2007, art. 15-B (incisos VII, IX, X, XX, XXI e XXI-A), com a redação do Decreto 12.499/2025.",
        "A CONTA DO IOF · US$ 1.000 a R$ 5,05: R$ 176,75 de IOF. · US$ 1.000 × R$ 5,05 = R$ 5.050,00; + IOF de 3,5% R$ 176,75; Total R$ 5.226,75. O MESMO IOF EM QUALQUER FORMA: cartão, espécie, pré-pago e conta lá fora, R$ 176,75 cada. · Nota: Exemplo: câmbio de R$ 5,05, sem tarifas.",
        "O QUE MUDA · O câmbio e as tarifas. · Cada R$ 0,10 a mais no câmbio custa R$ 103,50 a mais em US$ 1.000, já com o IOF. · Câmbio R$ 5,05, total com IOF R$ 5.226,75 (a base); R$ 5,15, R$ 5.330,25, +R$ 103,50; R$ 5,25, R$ 5.433,75, +R$ 207,00 (barras em coral). · Nota: Câmbios hipotéticos, só para comparar; sem tarifas.",
        "ANTES DE COMPRAR · Compare o VET. · Peças: câmbio + tarifas + IOF = VET. Citação: “O Valor Efetivo Total (VET) representa o custo de uma operação de câmbio em reais por moeda estrangeira, englobando a taxa de câmbio, as tarifas e tributos incidentes sobre essa operação.” Banco Central, Ranking do VET. Caixa âmbar: No ranking, o Banco Central mostra o VET médio de cada instituição. Os valores são de meses anteriores: confira o de hoje antes de comprar.",
        "NO TIMTIMCASH · Um teto para a viagem. · Em Orçamentos, Definir limites: busque Viagem. Os US$ 1.000 com IOF, e uma folga, dão R$ 5.300. · Tela real no celular (relógio em 23/12/2026, sem salvar): Definir orçamentos, “Limite mensal de despesa e meta mensal de receita”, Despesas, busca “Viagem”, 21 categorias; Viagem, média R$ 640, R$ 5.300,00, usar R$ 700; 8 categorias sem movimento em 12 meses. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Viaje com um teto. · Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Viagem para fora: o IOF é igual. O câmbio, não.\n\n"
        "Para gastar lá fora, o IOF é de 3,5% no cartão de crédito ou de débito, no saque, no cartão pré-pago, na compra de dinheiro em espécie "
        "e na remessa para uma conta sua no exterior. Só a remessa para investir paga 1,10%, e ela não é dinheiro para a viagem.\n\n"
        "Gastar US$ 1.000 a R$ 5,05 custa R$ 5.050 mais R$ 176,75 de IOF, em qualquer forma. O que muda são o câmbio e as tarifas: "
        "cada R$ 0,10 a mais no câmbio custa R$ 103,50 a mais nesses US$ 1.000.\n\n"
        "Compare o VET: o custo total em reais por moeda estrangeira, com câmbio, tarifas e tributos. O Banco Central publica um ranking do VET médio por instituição, com dados de meses anteriores.\n\n"
        "No timtimcash, ponha um teto na categoria Viagem, em Orçamentos.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Decreto 6.306/2007, art. 15-B, com a redação do Decreto 12.499/2025; Banco Central (Ranking do VET).\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#viagem #iof #cambio #dolar #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Véspera do Natal e começo das férias escolares: quem viaja para fora em janeiro compra moeda ou carrega cartão agora. Exterior e câmbio são o que mais alcança no perfil."),
        ("O que desperta interesse", "A capa desmonta a dúvida comum (“qual forma paga menos IOF?”) com quatro 3,5% iguais e vira a chave no título: o que muda é o câmbio. O slide 4 dá o tamanho disso em reais: R$ 103,50 a cada R$ 0,10."),
        ("Benefício para o público", "Sabe a alíquota de cada forma de pagar pelo decreto vigente, faz a conta do IOF de uma viagem e aprende a comparar o custo total (VET) no ranking do Banco Central, sem recomendação de banco, corretora ou cartão."),
        ("Como contribui para o perfil", "Fecha o assunto IOF do perfil (remessa em 16/11, viagem agora) com fonte oficial citada, e liga o tema a Orçamentos com tela real, sem ligar remessas ou câmbio a gratuidade."),
    ],
    "alt": [
        "Viagem ao exterior. Viagem: o IOF é igual. O câmbio, não. Sobre fundo escuro, quatro blocos com ícones de traço e 3,5% em letras grandes em cada um: cartão; dinheiro em espécie; cartão pré-pago; conta sua lá fora.",
        "IOF no câmbio: para gastar lá fora, 3,5% em todas. Cartão no exterior, de crédito ou débito, 3,5%; saque no exterior, 3,5%; cartão pré-pago e cheques de viagem, 3,5%; dinheiro em espécie, 3,5%; remessa para uma conta sua lá fora, 3,5%. Em destaque verde: remessa para investir, que não é dinheiro para gastar na viagem, 1,10%. Decreto 6.306 de 2007, artigo 15-B, com a redação do Decreto 12.499 de 2025.",
        "A conta do IOF: US$ 1.000 a R$ 5,05 pagam R$ 176,75 de IOF. US$ 1.000 vezes R$ 5,05 dão R$ 5.050,00; mais o IOF de 3,5%, R$ 176,75; total de R$ 5.226,75. O mesmo IOF em qualquer forma: cartão, espécie, pré-pago e conta lá fora, R$ 176,75 cada. Exemplo sem tarifas.",
        "O que muda: o câmbio e as tarifas. Cada R$ 0,10 a mais no câmbio custa R$ 103,50 a mais em US$ 1.000, já com o IOF. Com câmbio de R$ 5,05, o total com IOF é de R$ 5.226,75, a base; com R$ 5,15, R$ 5.330,25, mais R$ 103,50; com R$ 5,25, R$ 5.433,75, mais R$ 207,00. Câmbios hipotéticos, sem tarifas.",
        "Antes de comprar, compare o VET: câmbio mais tarifas mais IOF é igual ao VET. Citação do Banco Central: o Valor Efetivo Total, VET, representa o custo de uma operação de câmbio em reais por moeda estrangeira, englobando a taxa de câmbio, as tarifas e tributos incidentes sobre essa operação. No ranking, o Banco Central mostra o VET médio de cada instituição; os valores são de meses anteriores, então confira o de hoje antes de comprar.",
        "No timtimcash, um teto para a viagem. Em Orçamentos, Definir limites: busque Viagem; os US$ 1.000 com IOF, e uma folga, dão R$ 5.300. Tela real no celular, com dados de exemplo: Definir orçamentos, aba Despesas, busca por Viagem; a categoria Viagem, com média de R$ 640, recebe o limite de R$ 5.300,00.",
        "Viaje com um teto. Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Planalto · Decreto nº 6.306, de 2007, texto compilado (art. 15-B, incisos VII, IX, X, XX, XXI e XXI-A), lido em 16/10/2026", "https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306compilado.htm"),
        ("Planalto · Decreto nº 12.499, de 2025 (alíquotas do IOF câmbio)", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12499.htm"),
        ("Banco Central · Ranking do VET (definição do VET; valores de meses anteriores), consultado em 16/10/2026", "https://www.bcb.gov.br/rex/vet/vet.asp"),
        ("Banco Central · Portal de Dados Abertos, Ranking do VET (descrição do conjunto de dados)", "https://dadosabertos.bcb.gov.br/dataset/ranking-do-vet"),
    ],
    "telas": [
        "telas/celular-definir-orcamentos-viagem.png · Orçamentos › “Definir limites”, busca “Viagem” e R$ 5.300,00 no campo da categoria, sem salvar; relógio em 23/12/2026 10:00 (390 × 1400 em escala 3) · slide 6 (do título da folha à linha “8 categorias sem movimento em 12 meses”)",
    ],
}
