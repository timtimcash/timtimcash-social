# -*- coding: utf-8 -*-
"""Quinta 14/01/2027 · carrossel "Passo 3: os limites" (série Comece 2027, passo 3 de 4, capa verde com logotipo negativo).
Equipe ja. Artes: saida/2027-01-14_passo-3-os-limites/01.jpg a 06.jpg, geradas por equipes/ja/posts.py (post_limites), com o
selo da série de equipes/ja/selo_comece2027.py.
Telas reais (build 2026-10-19.5), relógio em 14/01/2027 10:00, celular, capturadas por equipes/ja/captura.py:
- numa cópia da conta sem nenhum limite em Orçamentos (equipes/ja/<cópia>/variantes.py: a mesma conta do dia com budgets
  vazio; nenhum lançamento ou número muda): "Sem limites definidos" e "Comece pela sua média dos últimos 12 meses",
  "Arredondada para cima, para a primeira semana não começar estourada.": Casa R$ 2.600, Mercado R$ 1.600, Educação R$ 1.500,
  Transporte R$ 1.200, Bares e restaurantes R$ 700, Lazer e hobbies R$ 370 e mais 7 categorias. Conferido com a conta: médias
  de jan a dez/2026 de Casa R$ 2.504,50, Mercado R$ 1.592,80, Educação R$ 1.450,00, Transporte R$ 1.106,79, Bares e
  restaurantes R$ 617,38 e Lazer e hobbies R$ 363,22, arredondadas para cima em degraus (dezena até R$ 500, centena acima);
- na conta de base (limites de Mercado 2.000, Transporte 1.950, Bares e restaurantes 600, Lazer 400 e Saúde 500): dia 14 de
  31 (45% do período); "R$ 1.673,70 no orçamento de R$ 5.450,00" e "R$ 4.745,90 sem limite"; faixas de "Progresso por
  categoria": Vão estourar no ritmo atual: Bares e restaurantes, R$ 284 de R$ 600, 47%; No limite: Mercado, R$ 840 de
  R$ 2.000, 42%; Tranquilas: Transporte (R$ 486 de R$ 1.950), Saúde (R$ 63 de R$ 500) e Lazer e hobbies (R$ 0 de R$ 400);
  Sem limite definido: Educação (R$ 2.390), Casa (R$ 2.300) e Assinaturas e serviços (R$ 55); nenhuma categoria já passou
  do limite. A faixa de cada categoria é conferida por assert em posts.py com a regra do site (_orcRisco: passou do limite;
  senão, projeção = gasto ÷ fração do mês; acima de 102% do limite, vai estourar; de 90% a 102%, no limite; abaixo de 90%,
  tranquila); "Onde definir limite primeiro": Educação (Usar R$ 1.500), Casa (Usar R$ 2.500) e Assinaturas e serviços
  (Usar R$ 120).
Atenção (para o revisor): o site arredonda as duas sugestões de jeitos diferentes. O quadro "Comece pela sua média" arredonda
para cima (Casa: R$ 2.504,50 vira R$ 2.600) e "Onde definir limite primeiro" arredonda para o mais próximo (R$ 2.500). Por isso,
a pedido do coordenador (20/10/2026), o slide 5 recorta o painel só até a primeira sugestão (o cabeçalho e Educação, Usar
R$ 1.500): as linhas de Casa e de Assinaturas ficam fora. A diferença de arredondamento vai ao dono como observação do site.
Diferença para 11/10 (orçamento pela média) e 21/12 (projeção do mercado em dezembro): aqui o foco é o passo 3 da série e as
cinco faixas de janeiro; o texto não usa o "no ritmo, fecha em" de nenhuma categoria.
Sem fato externo (lei, taxa ou estudo)."""

POST = {
    "pasta": "2027-01-14_passo-3-os-limites",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "Passo 3 da série Comece 2027: um limite por categoria em Orçamentos, começando pela média dos últimos 12 meses que o site sugere; as cinco faixas de Progresso por categoria em janeiro, com a marca de hoje; e as sugestões de onde definir limite primeiro",
    "pilar": "Campanha de janeiro · produto e planejamento",
    "data_longa": "quinta-feira, 14 de janeiro de 2027",
    "data_curta": "quinta-feira, 14/01/2027",
    "data_mockup": "14 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-14T10:00:00",
    "slides": [
        "Capa (fundo verde, logotipo negativo) · COMECE 2027 · PASSO 3 DE 4 · Quanto cabe em cada categoria? · O selo do passo 3 (quadrado na tinta com o 3 em menta) e três barras de categoria com a marca de hoje (rotulada hoje): a primeira, coral, passa da marca; a segunda, âmbar, encosta nela; a terceira, branca, está bem antes.",
        "ORÇAMENTOS · SEM LIMITES AINDA · Comece pela sua média. · O site sugere um limite por categoria: a sua média dos últimos 12 meses, arredondada para cima. · Tela real de Orçamentos no celular (14/01/2027, numa cópia da conta sem limites): Comece pela sua média dos últimos 12 meses; Casa R$ 2.600, Mercado R$ 1.600, Educação R$ 1.500, Transporte R$ 1.200, Bares e restaurantes R$ 700, Lazer e hobbies R$ 370 e mais 7 categorias; Usar estes limites; Definir do zero. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "PROGRESSO POR CATEGORIA · 14/01 · Cada categoria cai numa faixa. · A marca vertical é hoje: a barra à esquerda dela está dentro do ritmo. · Tela real de Progresso por categoria no celular (14/01/2027): a legenda da marca (dia 14 de 31 do período); Vão estourar no ritmo atual: Bares e restaurantes, R$ 284 de R$ 600, 47%; No limite: Mercado, R$ 840 de R$ 2.000, 42%. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "AS FAIXAS · CONTA DE EXEMPLO EM 14/01 · Cinco faixas dizem onde olhar. · Quadro com uma barrinha no desenho do site (a marca preta em 45% do mês) e a regra de cada faixa, com as categorias do exemplo: Já passaram do limite (o gasto já passou do limite): nenhuma em 14/01; Vão estourar no ritmo atual (no ritmo de hoje, o mês fecha acima do limite): Bares e restaurantes; No limite (no ritmo, fecha entre 90% e 102% do limite): Mercado; Tranquilas (no ritmo, fecha abaixo de 90% do limite): Transporte, Saúde, Lazer e hobbies; Sem limite definido (a categoria ainda não tem limite): Educação, Casa, Assinaturas e serviços. · Nota: A marca preta é hoje: dia 14 de 31.",
        "SUGESTÕES DO SITE · Onde definir limite primeiro. · A categoria sem limite que mais pesa no mês vem com um valor pela sua média. · Tela real do painel no celular (14/01/2027), recortada no cabeçalho e na primeira sugestão: Onde definir limite primeiro, SUGESTÕES; R$ 4.745,90 do período está em categorias sem limite. Os valores abaixo vêm da sua própria média e servem de ponto de partida; Educação, R$ 2.390 no período, sugestão pela média de 12 meses, Usar R$ 1.500, outro valor. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Passo 3: os limites. · Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Passo 3 de 4: quanto cabe em cada categoria?\n\n"
        "Em Orçamentos, sem nenhum limite, o timtimcash sugere um valor por categoria: a sua média dos últimos 12 meses, arredondada para cima. Dá para usar todos de uma vez ou definir do zero.\n\n"
        "Depois, Progresso por categoria mostra o mês em cinco faixas: já passaram do limite, vão estourar no ritmo atual, no limite, tranquilas e sem limite definido. A marca vertical é hoje: a barra à esquerda dela está dentro do ritmo.\n\n"
        "Na conta de exemplo, em 14/01, uma categoria vai estourar no ritmo atual, uma está no limite e três seguem tranquilas. Para as que ainda não têm limite, o site aponta onde definir primeiro.\n\n"
        "Próximo passo, segunda (18/01): a rota, e se 2027 apertar?\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#orcamento #organizacaofinanceira #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "No meio de janeiro, com o mês já carregado de contas, dá para ver quais categorias pedem atenção antes que o mês feche. É o passo 3 da série Comece 2027, entre o caminho (10/01) e a rota (18/01)."),
        ("O que desperta interesse", "A pergunta da capa, que todo mundo se faz em janeiro, e um quadro que traduz o mês em cinco faixas, com a marca de hoje no desenho do próprio site."),
        ("Benefício para o público", "Sai com um ponto de partida realista (a própria média, e não um número de cabeça), entende o que cada faixa quer dizer e sabe onde pôr o próximo limite."),
        ("Como contribui para o perfil", "Mantém a série reconhecível na grade (capa verde com o selo 3) e mostra Orçamentos por um ângulo novo: as faixas de risco e as sugestões, depois de 11/10 (orçamento pela média) e de 21/12 (a projeção do mercado)."),
    ],
    "alt": [
        "Comece 2027, passo 3 de 4. Quanto cabe em cada categoria? O selo do passo, um quadrado escuro com o número 3, e três barras horizontais com uma marca vertical chamada hoje: a primeira barra, coral, passa da marca; a segunda, amarela, encosta nela; a terceira, branca, fica bem antes.",
        "Orçamentos, sem limites ainda: comece pela sua média. O site sugere um limite por categoria, a média dos últimos 12 meses, arredondada para cima. Tela real no celular, com dados de exemplo: Casa R$ 2.600, Mercado R$ 1.600, Educação R$ 1.500, Transporte R$ 1.200, Bares e restaurantes R$ 700, Lazer e hobbies R$ 370 e mais 7 categorias, com os botões Usar estes limites e Definir do zero.",
        "Progresso por categoria em 14 de janeiro: cada categoria cai numa faixa. A marca vertical é hoje: a barra à esquerda dela está dentro do ritmo. Tela real no celular, com dados de exemplo: Vão estourar no ritmo atual, Bares e restaurantes, R$ 284 de R$ 600, 47%; No limite, Mercado, R$ 840 de R$ 2.000, 42%.",
        "As cinco faixas na conta de exemplo em 14 de janeiro. Já passaram do limite: nenhuma. Vão estourar no ritmo atual, quando no ritmo de hoje o mês fecha acima do limite: Bares e restaurantes. No limite, entre 90% e 102%: Mercado. Tranquilas, abaixo de 90%: Transporte, Saúde e Lazer e hobbies. Sem limite definido: Educação, Casa e Assinaturas e serviços. A marca preta é hoje, dia 14 de 31.",
        "Sugestões do site: onde definir limite primeiro. A categoria sem limite que mais pesa no mês vem com um valor pela sua média. Tela real no celular, com dados de exemplo: R$ 4.745,90 do período está em categorias sem limite; Educação, R$ 2.390 no período, sugestão pela média de 12 meses: usar R$ 1.500, ou outro valor.",
        "Passo 3: os limites. Orçamentos no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-orcamentos-sem-limites-14-01.png · Orçamentos no celular, relógio em 14/01/2027 10:00, numa cópia da conta sem nenhum limite (390 × 1000 em escala 3, para o botão “+” ficar abaixo do quadro) · slide 2 (o quadro “Comece pela sua média dos últimos 12 meses” inteiro)",
        "telas/celular-orcamentos-14-01.png · Orçamentos de Janeiro 2027 no celular, relógio em 14/01/2027 10:00, conta de base (390 × 2400 em escala 3) · slide 3 (da legenda da marca ao fim da linha do Mercado) e slide 5 (o painel “Onde definir limite primeiro” do topo ao fim da sugestão de Educação, antes do fio da linha da Casa)",
        "telas/celular-orcamentos-sem-limite-aberto-14-01.png · a mesma tela depois do toque em “Mostrar as outras 3 categorias com gasto e sem limite” (faixa “Sem limite definido”), guardada para conferir as categorias do slide 4",
    ],
}
