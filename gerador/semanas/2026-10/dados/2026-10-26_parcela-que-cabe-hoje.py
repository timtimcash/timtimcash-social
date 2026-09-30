# -*- coding: utf-8 -*-
"""Segunda 26/10/2026 · carrossel "A parcela cabe hoje. E daqui a três meses?" (educação com produto, capa papel).
Artes: saida/2026-10-26_parcela-que-cabe-hoje/01.jpg a 06.jpg, geradas por carrosseis-a/posts.py (contas conferidas por assert).
Tela real nova em saida/2026-10-26_parcela-que-cabe-hoje/telas/, capturada por carrosseis-a/app/captura_a.py: "Nova transação"
com "Parcelada" preenchida, sem salvar, com o relógio da página parado em 26/10/2026 às 10h (a data do post) e o mesmo
"Cartão principal" do post de 19/10 (fecha no dia 3, vence no dia 10), acrescentado só à cópia do estado.py.
Exemplo (marcado como exemplo nas artes), parcelas somadas por mês:
geladeira R$ 2.499 em 10× de R$ 249,90 (out a jul); presentes de Natal 6× de R$ 200 (dez a mai); material escolar 3× de R$ 600 (jan a mar).
out 249,90 · nov 249,90 · dez 449,90 · jan, fev e mar 1.049,90 · abr e mai 449,90 · jun e jul 249,90.
Sobra de um mês comum: R$ 2.180 (setembro: R$ 9.960 − R$ 7.780); 1.049,90 ÷ 2.180 = 48,2%.
No site (código conferido): "Parcelada" aceita de 2 a 120 parcelas, o valor digitado é o total (splitParcelas), cada parcela
vai para o seu mês e as seguintes à primeira nascem pendentes. A Simulação futura não lê lançamentos pendentes: por isso o
texto diz para pôr as parcelas num cenário."""

POST = {
    "pasta": "2026-10-26_parcela-que-cabe-hoje",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "Compras parceladas: cada parcela é pequena, mas as parcelas somam e ocupam os meses seguintes até terminar; exemplo de três compras que somam R$ 1.049,90 em janeiro, a comparação com a sobra de um mês comum e a “Parcelada” da Nova transação",
    "pilar": "Educação com produto",
    "data_longa": "segunda-feira, 26 de outubro de 2026",
    "data_curta": "segunda-feira, 26/10/2026",
    "data_mockup": "26 de outubro",
    "hora": "10h00",
    "iso": "2026-10-26T10:00:00",
    "slides": [
        "Capa (fundo papel) · COMPRAS PARCELADAS · A parcela cabe hoje. E daqui a três meses? · Duas barras: hoje, R$ 249,90; em 3 meses, R$ 1.049,90, com três parcelas empilhadas em tons de coral.",
        "UMA COMPRA, DEZ MESES · A parcela é pequena. O prazo, não. · Uma compra de R$ 2.499 em 10× vira R$ 249,90 em cada um dos próximos 10 meses. · Cartão: R$ 2.499 e 10× de R$ 249,90, com dez blocos de out a jul. · Nota: Exemplo: uma geladeira comprada em outubro, em 10 parcelas mensais.",
        "ELAS SE SOMAM · Cada parcela cabe. Juntas, pesam. · Gráfico das parcelas somadas em cada mês, em R$: out 249,90; dez 449,90; jan a mar 1.049,90; abr 449,90; jul 249,90. Legenda: Geladeira, 10× R$ 249,90, out a jul; Presentes de Natal, 6× R$ 200,00, dez a mai; Material escolar, 3× R$ 600,00, jan a mar. · Nota: Exemplo: três compras parceladas, a partir de outubro.",
        "ANTES DE PARCELAR · Olhe o mês mais cheio, não a parcela. · Some o que já está comprometido e compare com o que sobra num mês comum. · Cartão: sobra de um mês comum R$ 2.180; parcelas em janeiro R$ 1.049,90, 48%, quase metade da sobra. · Nota: Exemplo: sobra de R$ 2.180, como em setembro (receitas de R$ 9.960 e despesas de R$ 7.780).",
        "NO TIMTIMCASH · Lance uma vez. Cada parcela cai no seu mês. · Em “Recorrência”, escolha “Parcelada” e o “Nº parcelas”, de 2 a 120. Você digita o total, e as próximas parcelas ficam pendentes. · Tela real de “Nova transação” no celular: Geladeira nova, “Será incluído na fatura que vence 10/nov”, Recorrência Parcelada, Nº parcelas 10, A cada Meses, “10× de R$ 249,90 · mensal”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Veja o mês que aperta antes de parcelar. · Transações e Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Uma parcela de R$ 249,90 cabe no mês. O que pesa é a soma das parcelas nos meses seguintes.\n\n"
        "Cada compra parcelada ocupa um pedaço dos próximos meses até a última parcela. No exemplo do carrossel, a geladeira de R$ 2.499 em 10× começa em outubro; "
        "em dezembro entram os presentes, em 6× de R$ 200, e em janeiro o material escolar, em 3× de R$ 600. Em janeiro, as parcelas já somam R$ 1.049,90: quase metade de uma sobra de R$ 2.180.\n\n"
        "Antes de parcelar, olhe o mês mais cheio, não a parcela. Para ver o mês que aperta, ponha as parcelas num cenário da Simulação futura.\n\n"
        "No timtimcash, a opção “Parcelada” da Nova transação divide o total em 2 a 120 parcelas e lança cada uma no seu mês.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#compraparcelada #cartaodecredito #educacaofinanceira #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Última semana de outubro, às vésperas das compras de fim de ano, quando muita gente parcela. Fecha o mês ligado ao carrossel de 19/10 (o mesmo cartão de exemplo, que fecha no dia 3 e vence no dia 10) e usa a parcela de R$ 249,90 do post de 30/09, para os números conversarem."),
        ("O que desperta interesse", "A capa responde com uma imagem à pergunta do título: a barra de hoje, pequena, ao lado da barra de daqui a três meses, quatro vezes mais alta. O gráfico do slide 3 mostra o degrau subindo e descendo à medida que as parcelas começam e terminam."),
        ("Benefício para o público", "Troca a pergunta “a parcela cabe?” por “quanto já está comprometido no mês mais cheio?”, com uma conta simples, comparada com a própria sobra. Sem juros, sem recomendação de crédito e sem promessa."),
        ("Como contribui para o perfil", "Educação com produto: termina na tela real da Nova transação com “Parcelada” preenchida e aponta a Simulação futura para ver o mês que aperta, do jeito que ela funciona (um cenário com as parcelas), sem prometer o que o site não faz."),
    ],
    "alt": [
        "Compras parceladas. A parcela cabe hoje. E daqui a três meses? Duas barras: hoje, R$ 249,90; em 3 meses, R$ 1.049,90, uma barra quatro vezes mais alta, feita de três parcelas empilhadas.",
        "Uma compra, dez meses. A parcela é pequena. O prazo, não. Uma compra de R$ 2.499 em 10 vezes vira R$ 249,90 em cada um dos próximos 10 meses. Dez blocos, de outubro a julho. Exemplo de uma geladeira comprada em outubro.",
        "Elas se somam. Cada parcela cabe. Juntas, pesam. Gráfico das parcelas somadas em cada mês, em reais: 249,90 em outubro e novembro; 449,90 em dezembro; 1.049,90 em janeiro, fevereiro e março; 449,90 em abril e maio; 249,90 em junho e julho. Três compras de exemplo: geladeira, 10 vezes de R$ 249,90, de outubro a julho; presentes de Natal, 6 vezes de R$ 200, de dezembro a maio; material escolar, 3 vezes de R$ 600, de janeiro a março.",
        "Antes de parcelar. Olhe o mês mais cheio, não a parcela. Some o que já está comprometido e compare com o que sobra num mês comum. Sobra de um mês comum, R$ 2.180; parcelas em janeiro, R$ 1.049,90, ou 48%, quase metade da sobra. Exemplo com a sobra de setembro: receitas de R$ 9.960 e despesas de R$ 7.780.",
        "No timtimcash, lance uma vez e cada parcela cai no seu mês. Em Recorrência, escolha Parcelada e o número de parcelas, de 2 a 120; você digita o total, e as próximas parcelas ficam pendentes. Tela real de Nova transação no celular, com dados de exemplo: Geladeira nova, será incluído na fatura que vence 10 de novembro, recorrência Parcelada, 10 parcelas, a cada mês, 10 vezes de R$ 249,90, mensal.",
        "Veja o mês que aperta antes de parcelar. Transações e Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-nova-transacao-parcelada.jpg · “Nova transação” no celular: despesa de R$ 2.499,00, Casa, “Cartão principal”, Geladeira nova, “Será incluído na fatura que vence 10/nov”, Recorrência “Parcelada”, Nº parcelas 10, A cada Meses, “10× de R$ 249,90 · mensal”; sem salvar; relógio da página em 26/10/2026 às 10h (a data aparece como “Hoje 26/10”, fora do recorte) (celular, 390 × 844 em escala 3) · slide 5",
    ],
}
