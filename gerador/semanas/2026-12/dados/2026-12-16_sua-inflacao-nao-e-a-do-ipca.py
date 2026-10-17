# -*- coding: utf-8 -*-
"""Quarta 16/12/2026 · carrossel "Sua inflação não é a do IPCA" (educação com produto, capa papel).
Artes: saida/2026-12-16_sua-inflacao-nao-e-a-do-ipca/01.jpg a 07.jpg, geradas por equipes/dc2/posts.py (contas por assert).
Tela real nova em saida/2026-12-16_sua-inflacao-nao-e-a-do-ipca/telas/, capturada por equipes/dc2/captura.py na conta de N/base_app
(build 2026-10-16.1), sem mudar nada: Relatórios no celular, relógio em 16/12/2026, seta "Anterior" até Novembro 2026.
Fatos pesquisados pela equipe dc2 em 16/10/2026 (fontes oficiais, IBGE), o último mês divulgado é setembro de 2026:
- peso mensal de cada grupo em setembro de 2026 (SIDRA, quadro do IPCA Brasil): Alimentação e bebidas 21,5090%; Habitação 15,2611%;
  Artigos de residência 3,4843%; Vestuário 4,6171%; Transportes 20,1607%; Saúde e cuidados pessoais 13,8408%; Despesas pessoais 10,4075%;
  Educação 6,2085%; Comunicação 4,5111% (nos slides, com uma casa);
- variação em 12 meses até setembro de 2026 (Indicadores IBGE, IPCA setembro de 2026, p. 15): índice 4,58%; Alimentação 4,66%;
  Habitação 4,22%; Artigos de residência 2,08%; Vestuário 3,34%; Transportes 3,94%; Saúde 5,75%; Despesas pessoais 5,90%;
  Educação 5,95%; Comunicação 2,79% (Cursos regulares 6,75%, não usado);
- IBGE Explica: "o seu índice pessoal de inflação pode ser maior ou menor do que o IPCA".
Pesos do exemplo: despesas de novembro de 2026 (R$ 9.149,40) na tela real; Alimentação = Mercado (R$ 1.844,90) + Bares e restaurantes
(R$ 928,60) = 30,3%; Habitação = Casa (aluguel e luz, R$ 2.501,80) = 27,3%; Educação 15,8%; Transportes 13,2%; Saúde 1,4%;
outros (compras, lazer e assinaturas) 11,9%. Educação: 15,85% ÷ 6,2085% = 2,55, "duas vezes e meia". O post não calcula uma
"inflação pessoal" (o site não calcula).
Atenção do revisor: o IPCA de novembro sai por volta de 10/12/2026, antes da publicação; se quiser, troque os números de setembro
pelos do mês mais recente (os pesos mudam pouco; as variações em 12 meses mudam)."""

POST = {
    "pasta": "2026-12-16_sua-inflacao-nao-e-a-do-ipca",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "O IPCA é a cesta média de quem ganha de 1 a 40 salários mínimos (pesos da POF): o peso e a variação em 12 meses de cada grupo em setembro de 2026, comparados com os pesos do gasto da conta de exemplo em novembro (Educação pesa 2,5 vezes mais), e Relatórios › Despesas por categoria para ver a própria cesta",
    "pilar": "Educação com produto · fonte oficial (IBGE)",
    "data_longa": "quarta-feira, 16 de dezembro de 2026",
    "data_curta": "quarta-feira, 16/12/2026",
    "data_mockup": "16 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-16T10:00:00",
    "slides": [
        "Capa (fundo papel) · INFLAÇÃO · Sua inflação não é a do IPCA · Duas colunas empilhadas, “a cesta do IPCA” e “a sua cesta”, ligadas por faixas de cada grupo: Alimentação 21,5% e 30,3%; Habitação 15,3% e 27,3%; Transportes 20,2% e 13,2%; Saúde 13,8% e 1,4%; outros; Educação em coral, 6,2% e 15,8%.",
        "O QUE É O IPCA · A inflação oficial é uma cesta média. · Cupom “CESTA DO IPCA · peso de cada grupo · set/26”: Alimentação 21,5%; Transportes 20,2%; Habitação 15,3%; Saúde 13,8%; Despesas pessoais 10,4%; Educação 6,2% (barra coral); Vestuário 4,6%; Comunicação 4,5%; Artigos de residência 3,5%; TOTAL 100%. · Nota: Famílias com renda de 1 a 40 salários mínimos; pesos da POF 2017-2018. Fonte: IBGE.",
        "EM 12 MESES · Cada grupo subiu de um jeito. · Régua com a linha “IPCA 4,58%”: acima dela, em coral, Educação 5,95% (destaque), Despesas pessoais 5,90%, Saúde 5,75% e Alimentação 4,66%; abaixo, em cinza, Habitação 4,22%, Transportes 3,94%, Vestuário 3,34%, Comunicação 2,79% e Artigos de residência 2,08%. · Nota: Variação acumulada em 12 meses até setembro de 2026. Fonte: IBGE.",
        "NO EXEMPLO · A sua cesta tem outros pesos. · Barras em par (cinza: IPCA, setembro de 2026; coral: exemplo, novembro de 2026): Alimentação 21,5% e 30,3%; Habitação 15,3% e 27,3%; Educação 6,2% e 15,8% (destaque); Transportes 20,2% e 13,2%; Saúde 13,8% e 1,4%. · Nota: Em % do gasto. No exemplo (novembro de 2026), Alimentação soma mercado e bares e restaurantes; Habitação, aluguel e luz.",
        "LEIA ASSIM · Onde a sua cesta pesa mais, a alta pesa mais. · Cartão: Educação no IPCA 6,2% → no exemplo 15,8% · 2,5× o peso. “Em 12 meses, Educação subiu 5,95%, mais que o índice (4,58%). Nessa casa, a alta da escola pesa duas vezes e meia o que pesa no IPCA.” · Citação em verde suave: “O seu índice pessoal de inflação pode ser maior ou menor do que o IPCA.” IBGE, “Inflação”, na série IBGE Explica.",
        "NO TIMTIMCASH · Veja quanto cada categoria leva do seu gasto. · Em Relatórios, Despesas por categoria, no período que você escolher. · Tela real no celular (relógio em 16/12/2026, novembro de 2026): “Despesas por categoria · 9 categorias · Total R$ 9.149,40”; Casa R$ 2.501,80 27,3%; Mercado R$ 1.844,90 20,2%; Educação R$ 1.450,00 15,8%; Transporte R$ 1.210,00 13,2%; Bares e restaurantes R$ 928,60 10,1%. Ao lado, o “GRUPO DO IPCA” de cada linha: Habitação, Alimentação, Educação (em coral), Transportes, Alimentação. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Conheça a sua cesta. · Relatórios no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "A inflação oficial é uma média. A sua tem outros pesos.\n\n"
        "O IPCA mede os preços para famílias com renda de 1 a 40 salários mínimos, com os pesos da POF 2017-2018. "
        "Em setembro de 2026, Alimentação e bebidas pesava 21,5% da cesta; Transportes, 20,2%; Habitação, 15,3%; Educação, 6,2%. "
        "Em 12 meses, o índice subiu 4,58%, e Educação, 5,95%.\n\n"
        "No nosso exemplo, a escola leva 15,8% das despesas de novembro: duas vezes e meia o peso de Educação no IPCA. "
        "Quando a mensalidade sobe, essa casa sente mais do que o índice. O próprio IBGE lembra: a sua inflação pode ser maior ou menor do que o IPCA.\n\n"
        "No timtimcash, Relatórios mostra em Despesas por categoria quanto cada categoria leva do seu gasto, no período que você escolher.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fonte: IBGE, IPCA de setembro de 2026 (divulgado em 09/10/2026).\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#inflacao #ipca #orcamento #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Segunda quinzena de dezembro, quando a inflação do ano vira assunto e chegam os reajustes de 2027 (mensalidade, aluguel). O IPCA é citado o tempo todo, mas pouca gente sabe que ele é uma média com pesos fixos, e que a própria cesta pode ser bem diferente."),
        ("O que desperta interesse", "A capa põe as duas cestas lado a lado e a faixa de Educação que engrossa de 6,2% para 15,8%: a pergunta “e a minha?” vem sozinha. O cupom do slide 2 e a régua do slide 3 mostram, num olhar, os pesos e quem subiu mais."),
        ("Benefício para o público", "Entende o que o IPCA mede (famílias de 1 a 40 salários mínimos, pesos da POF), vê que cada grupo sobe diferente e aprende a comparar os pesos do próprio gasto com os do índice, sem uma “inflação pessoal” inventada: o post mostra a ideia com os pesos, como o IBGE explica."),
        ("Como contribui para o perfil", "Educação financeira com fonte oficial citada (IBGE, setembro de 2026) e tela real nova de Relatórios, com os números de novembro da conta de exemplo, coerentes com os outros posts (aluguel, escola, mercado)."),
    ],
    "alt": [
        "Inflação. Sua inflação não é a do IPCA. Duas colunas empilhadas, a cesta do IPCA e a sua cesta, ligadas por faixas: Alimentação, 21,5% no IPCA e 30,3% na sua cesta; Habitação, 15,3% e 27,3%; Transportes, 20,2% e 13,2%; Saúde, 13,8% e 1,4%; outros; e Educação, em coral, de 6,2% para 15,8%.",
        "O que é o IPCA: a inflação oficial é uma cesta média. Um cupom com o peso de cada grupo em setembro de 2026: Alimentação, 21,5%; Transportes, 20,2%; Habitação, 15,3%; Saúde, 13,8%; Despesas pessoais, 10,4%; Educação, 6,2%; Vestuário, 4,6%; Comunicação, 4,5%; Artigos de residência, 3,5%; total, 100%. Famílias com renda de 1 a 40 salários mínimos; pesos da POF 2017-2018. Fonte: IBGE.",
        "Em 12 meses, cada grupo subiu de um jeito. Uma régua com a linha do IPCA em 4,58%. Acima dela: Educação, 5,95%, em destaque; Despesas pessoais, 5,90%; Saúde, 5,75%; Alimentação, 4,66%. Abaixo: Habitação, 4,22%; Transportes, 3,94%; Vestuário, 3,34%; Comunicação, 2,79%; Artigos de residência, 2,08%. Variação acumulada em 12 meses até setembro de 2026, segundo o IBGE.",
        "No exemplo, a sua cesta tem outros pesos. Barras em par, o IPCA de setembro de 2026 e o exemplo de novembro de 2026, em porcentagem do gasto: Alimentação, 21,5% e 30,3%; Habitação, 15,3% e 27,3%; Educação, 6,2% e 15,8%; Transportes, 20,2% e 13,2%; Saúde, 13,8% e 1,4%. No exemplo, Alimentação soma mercado e bares e restaurantes; Habitação, aluguel e luz.",
        "Leia assim: onde a sua cesta pesa mais, a alta pesa mais. Educação pesa 6,2% no IPCA e 15,8% no exemplo, 2,5 vezes o peso. Em 12 meses, Educação subiu 5,95%, mais que o índice, de 4,58%; nessa casa, a alta da escola pesa duas vezes e meia o que pesa no IPCA. Citação do IBGE: o seu índice pessoal de inflação pode ser maior ou menor do que o IPCA.",
        "No timtimcash: veja quanto cada categoria leva do seu gasto, em Relatórios, Despesas por categoria. Tela real no celular, novembro de 2026, com dados de exemplo: total de R$ 9.149,40 em 9 categorias; Casa, R$ 2.501,80, 27,3%; Mercado, R$ 1.844,90, 20,2%; Educação, R$ 1.450,00, 15,8%; Transporte, R$ 1.210,00, 13,2%; Bares e restaurantes, R$ 928,60, 10,1%. Ao lado de cada linha, o grupo do IPCA: Habitação, Alimentação, Educação, Transportes e Alimentação.",
        "Conheça a sua cesta. Relatórios no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("IBGE · IPCA fica em 0,82% em setembro (4,58% em 12 meses), release de 09/10/2026", "https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/48246-ipca-fica-em-0-82-em-setembro"),
        ("IBGE SIDRA · IPCA Brasil, setembro de 2026: peso mensal de cada grupo (consultado em 16/10/2026)", "https://sidra.ibge.gov.br/home/ipca/brasil"),
        ("IBGE · Indicadores IBGE, IPCA setembro de 2026: variações acumuladas em 12 meses por grupos e itens (p. 15)", "https://biblioteca.ibge.gov.br/visualizacao/periodicos/236/inpc_ipca_2026_set.pdf"),
        ("IBGE Explica · Inflação (o índice pessoal pode ser maior ou menor do que o IPCA)", "https://www.ibge.gov.br/explica/inflacao.php"),
        ("IBGE · Índice Nacional de Preços ao Consumidor Amplo (famílias de 1 a 40 salários mínimos; pesos da POF 2017-2018)", "https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-indice-nacional-de-precos-ao-consumidor-amplo.html"),
    ],
    "telas": [
        "telas/celular-relatorios-novembro.png · Relatórios no celular com o relógio em 16/12/2026 10:00 e a seta “Anterior” até Novembro 2026 (página inteira, 390 × 760 em escala 3): painel “Despesas por categoria”, 9 categorias, total R$ 9.149,40; recortados o cabeçalho do painel e as linhas de Casa a Bares e restaurantes · slide 6",
    ],
}
