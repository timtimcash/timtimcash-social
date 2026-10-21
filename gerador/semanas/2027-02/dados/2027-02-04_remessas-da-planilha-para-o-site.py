# -*- coding: utf-8 -*-
"""Quinta 04/02/2027 · carrossel "Anos de remessas numa planilha? Traga todas." (exterior, produto, capa verde suave).
Equipe fa. O fechamento não traz a frase do controle financeiro: o post é só de remessas e investimentos lá fora.
Artes: saida/2027-02-04_remessas-da-planilha-para-o-site/01.jpg a 06.jpg, geradas por equipes/fa/posts.py
(post_remessas). Telas reais em saida/2027-02-04_remessas-da-planilha-para-o-site/telas/, capturadas por
equipes/fa/captura.py, build 2026-10-19.5, relógio em 04/02/2027 10:00, com a conta de base atualizada em 20/10/2026
(fechamento de 2026 informado em 29/01/2027, sem câmbio).

Mudança na conta (só na cópia da equipe fa, só neste post): a variante "sem-remessas-usd" (variantes.py, na pasta da
cópia) tira os 3 registros de remessa em dólar; as 3 transferências da Conta corrente para a Corretora no exterior
ficam, sem o vínculo. A pessoa importa explora/minhas-remessas.csv (planilha_0402.py: o cabeçalho do modelo que o
próprio site baixa, "modelo-remessas.xlsx", com as 3 remessas da conta de exemplo, só com o TOTAL; "Valor em R$" e
"IOF" em branco). Na revisão, o site diz "3 linhas ficam vinculadas às transferências que já existem no timtimcash, sem
mudar o saldo"; depois de "Importar 3 remessas", a tela de Remessas fica igual à da base, número por número (conferido
por assert em captura.py; só muda a ordem dos botões de moeda, EUR antes de USD). Nenhum número de outro post muda.

Números (asserts em posts.py): remessas de 12/07/2023, 14/03/2024 e 18/04/2024, US$ 4.000 cada, R$ 19.600, R$ 20.000
e R$ 20.400 debitados: câmbio efetivo R$ 4,90, R$ 5,00 e R$ 5,10; total US$ 12.000 e R$ 60.000; "Câmbio médio efetivo
R$ 5,0000". Rendimento ano a ano (tela): 2023 "aportes 4.000,00 · a R$ 4,90 · fim 4.120,00" (+6,5% e +120,00 em US$;
+3,8% e +R$ 343,68 em reais); 2024 "aportes 8.000,00 · a R$ 5,05 · fim 12.480,00" (+3,6%, +360,00; +34,4%,
+R$ 16.928,73). O recorte mostra só 2023 e 2024 (os anos com remessa em dólar); 2026 aparece na tela com "falta o
câmbio de 31/12" em reais, fora do recorte. Nenhum valor do fechamento de 2026 em reais aparece no post, e nenhuma tela
em foco mostra o "IOF pago" das remessas em dólar (o IOF delas está dentro do total, e o indicador lê zero).
Colunas do modelo (conferidas no arquivo que o site gera): Data, Conta de origem, Conta de destino, Valor em moeda,
Valor em R$, IOF, TOTAL, Moeda; as cinco obrigatórias e o resto do texto vêm do modal "Importar planilha"."""

POST = {
    "pasta": "2027-02-04_remessas-da-planilha-para-o-site",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "Remessas da planilha para o site: o menu “Mais ações” (“Baixar planilha modelo” e “Importar planilha”), as 5 colunas obrigatórias, a revisão linha por linha com o câmbio efetivo e o rendimento ano a ano com todas as remessas",
    "pilar": "Exterior · produto (Remessas ao exterior), com tela real",
    "data_longa": "quinta-feira, 4 de fevereiro de 2027",
    "data_curta": "quinta-feira, 04/02/2027",
    "data_mockup": "4 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-04T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · INVESTIMENTO NO EXTERIOR · Anos de remessas numa planilha? Traga todas. · À esquerda, uma planilha desenhada (colunas A, B e C; cabeçalho verde Data, US$ e Total R$; linhas 12/07/2023 4.000 19.600, 14/03/2024 4.000 20.000 e 18/04/2024 4.000 20.400); de cada linha sai uma seta verde para um cartão: US$ 4.000, câmbio R$ 4,90; US$ 4.000, câmbio R$ 5,00; US$ 4.000, câmbio R$ 5,10.",
        "EM REMESSAS · Comece pelo menu “Mais ações”. · Tela real de Remessas no computador, relógio em 04/02/2027: os botões Resgate, Nova remessa e ⋮, com o menu aberto: Importar planilha e Baixar planilha modelo. · Nota: Tela real do timtimcash, com dados de exemplo. · Cartão: “Baixar planilha modelo”: um Excel com as colunas certas e uma aba que explica cada uma. “Importar planilha”: aceita .xlsx, .xls e .csv, inclusive a planilha que você já usa.",
        "UMA LINHA POR REMESSA · 5 colunas obrigatórias. · Faltando as contas, dá para escolher na revisão. · Tabela no estilo do modelo, com a 1ª remessa da conta de exemplo: Data 12/07/2023, Conta de origem Conta corrente, Conta de destino Corretora no exterior, Valor em moeda 4.000,00 e TOTAL 19.600,00 (obrigatórias, em verde); Valor em R$ e IOF em branco, Moeda USD (opcionais). · Nota: No lugar do TOTAL, dá para pôr o Valor em R$ e o IOF: o timtimcash soma. Moeda em branco entra como dólar. Exemplo: a 1ª remessa da conta de exemplo.",
        "ANTES DE IMPORTAR · Você revisa linha por linha. · O câmbio efetivo de cada remessa aparece na hora. · Tela real de “Revisar importação” no celular, relógio em 04/02/2027, a 1ª linha: Corretora no exterior; Data 12/07/2023; Moeda USD; Enviado 4.000,00; Total em R$ 19.600,00; IOF em branco; Câmbio efetivo R$ 4,9000. · Nota: Tela real do timtimcash, com dados de exemplo. · Três cartões: 12/07/2023 R$ 4,90; 14/03/2024 R$ 5,00; 18/04/2024 R$ 5,10.",
        "DEPOIS · Cada ano com o seu câmbio. · No rendimento ano a ano, os aportes de cada ano e o câmbio médio deles. · Tela real de Remessas › Rendimento ano a ano no celular, relógio em 04/02/2027, depois da importação: 2023 +6,5%, +120,00, +3,8%, +R$ 343,68, “aportes 4.000,00 · a R$ 4,90 · fim 4.120,00”; 2024 +3,6%, +360,00, +34,4%, +R$ 16.928,73, “aportes 8.000,00 · a R$ 5,05 · fim 12.480,00”. · Nota: Tela real do timtimcash, com dados de exemplo. · Selo: Câmbio médio efetivo das 3: R$ 5,0000.",
        "Fechamento (fundo verde) · Seu histórico lá fora, num lugar só. · Remessas ao exterior no timtimcash, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Anos de remessas numa planilha? Dá para trazer todas de uma vez.\n\n"
        "Em Remessas, o menu “Mais ações” tem “Baixar planilha modelo” e “Importar planilha”. A planilha precisa de uma linha por remessa e de 5 colunas: data, conta de origem, conta de destino, valor na moeda e o total em reais. IOF e moeda são opcionais, e moeda em branco entra como dólar. Vale .xlsx, .xls e .csv, inclusive a planilha que você já usa.\n\n"
        "Antes de importar, você revisa linha por linha, com o câmbio efetivo calculado na hora. No exemplo, 3 remessas de US$ 4.000: R$ 4,90, R$ 5,00 e R$ 5,10 por dólar.\n\n"
        "Depois, o rendimento ano a ano passa a contar com todas elas: os aportes de 2023 a R$ 4,90, os de 2024 a R$ 5,05, e um câmbio médio efetivo de R$ 5,0000.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #remessas #dolar #planilha #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Começo do ano é quando quem investe lá fora junta o histórico para a declaração e para planejar as remessas de 2027. Quem começou a usar o timtimcash em janeiro ainda tem os anos anteriores numa planilha."),
        ("O que desperta interesse", "A capa mostra a planilha virando remessas com o câmbio de cada uma, e o post responde a uma dúvida prática: dá para trazer o histórico sem digitar tudo de novo."),
        ("Benefício para o público", "Sabe onde fica a importação, quais colunas a planilha precisa, que pode revisar e corrigir antes de importar e que o câmbio médio e o rendimento de cada ano passam a contar com todas as remessas."),
        ("Como contribui para o perfil", "Mostra pela primeira vez a importação de remessas (os posts de 08/10 e 23/10 falaram do extrato e da planilha de transações), com telas reais e números iguais aos dos outros posts de exterior."),
    ],
    "alt": [
        "Investimento no exterior. Anos de remessas numa planilha? Traga todas. Ilustração: uma planilha com as colunas Data, US$ e Total R$ e três linhas, de 12 de julho de 2023, 14 de março de 2024 e 18 de abril de 2024, cada uma com 4.000 dólares e o total em reais; de cada linha sai uma seta para um cartão de remessa de 4.000 dólares, com o câmbio de R$ 4,90, R$ 5,00 e R$ 5,10.",
        "Em Remessas, comece pelo menu Mais ações. Tela real do timtimcash no computador, com dados de exemplo: ao lado dos botões Resgate e Nova remessa, o botão de três pontos abre o menu com Importar planilha e Baixar planilha modelo. Baixar planilha modelo traz um Excel com as colunas certas e uma aba que explica cada uma; Importar planilha aceita xlsx, xls e csv, inclusive a planilha que você já usa.",
        "Uma linha por remessa: 5 colunas obrigatórias. Faltando as contas, dá para escolher na revisão. Tabela com a primeira remessa da conta de exemplo: data 12/07/2023, conta de origem Conta corrente, conta de destino Corretora no exterior, valor em moeda 4.000 e total de R$ 19.600, as obrigatórias; valor em reais e IOF em branco e moeda USD, as opcionais. No lugar do total, dá para pôr o valor em reais e o IOF, que o timtimcash soma; moeda em branco entra como dólar.",
        "Antes de importar, você revisa linha por linha: o câmbio efetivo de cada remessa aparece na hora. Tela real da revisão da importação no celular, com dados de exemplo: Corretora no exterior, 12/07/2023, USD, 4.000 enviados, R$ 19.600 no total, câmbio efetivo de R$ 4,90. Abaixo, os três câmbios: R$ 4,90 em 12/07/2023, R$ 5,00 em 14/03/2024 e R$ 5,10 em 18/04/2024.",
        "Depois, cada ano com o seu câmbio. Tela real do rendimento ano a ano das remessas, com dados de exemplo: em 2023, aportes de 4.000 dólares a R$ 4,90, e o ano fechou com 4.120 dólares, alta de 6,5% em dólar; em 2024, aportes de 8.000 dólares a R$ 5,05, e o ano fechou com 12.480 dólares, alta de 3,6% em dólar. Câmbio médio efetivo das 3 remessas: R$ 5,0000.",
        "Seu histórico lá fora, num lugar só. Remessas ao exterior no timtimcash, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/computador-remessas-menu-04-02.png · Remessas no computador (1440 × 1000 em escala 2), relógio em 04/02/2027 10:00, build 2026-10-19.5, cópia da conta na variante sem as remessas em dólar (só a remessa em euro de 01/12/2026): toque no botão ⋮ (“Mais ações”), menu aberto com “Importar planilha” e “Baixar planilha modelo” · slide 2 (recorte dos botões e do menu, sem valores)",
        "telas/celular-remessas-menu-04-02.png e telas/celular-importar-planilha-04-02.png · o mesmo menu no celular e o modal “Importar planilha” (“A planilha precisa de uma linha por remessa, com estas colunas: Data, Conta de origem, Conta de destino, Valor em moeda, TOTAL em R$, Valor em R$, IOF, Moeda”; “As cinco primeiras são obrigatórias...”) · referência do texto do slide 3",
        "telas/celular-revisar-importacao-04-02.png · “Revisar importação” no celular (390 × 1500 em escala 3), mesma variante, depois de escolher explora/minhas-remessas.csv: “3 linhas lidas de minhas-remessas.csv · confira antes de confirmar”; “3 linhas ficam vinculadas às transferências que já existem no timtimcash, sem mudar o saldo.”; 1ª linha Corretora no exterior, 12/07/2023, USD, 4.000,00, 19.600,00, IOF em branco, câmbio efetivo R$ 4,9000; “Importar 3 remessas” · slide 4 (recorte da 1ª linha)",
        "telas/computador-revisar-importacao-04-02.png · a mesma revisão no computador, em tabela (referência; não usada no carrossel, o texto ficaria pequeno demais)",
        "telas/celular-remessas-depois-04-02.png · Remessas em USD no celular, página inteira, depois de “Importar 3 remessas”; igual à tela da base no mesmo dia (conferido): Rendimento ano a ano com 2023 e 2024 (aportes a R$ 4,90 e R$ 5,05), 2025, 2026 (“falta o câmbio de 31/12”) e 2027; Remetido US$ 12.000,00 · 3 remessas · desde jul/23; Câmbio médio efetivo R$ 5,0000 · slide 5 (recorte das linhas de 2023 e 2024)",
    ],
}
