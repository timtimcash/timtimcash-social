# -*- coding: utf-8 -*-
"""Domingo 10/01/2027 · Reel "Comece 2027 · Passo 2 de 4: para onde vai?" (série Comece 2027, passo 2, O caminho; capa verde suave).
Equipe jr. Vídeo, capa e prévia gerados por equipes/jr/reel_10.py (assert nos números lidos da tela); telas capturadas por
equipes/jr/captura_10.py no site build 2026-10-19.5, na cópia da conta da equipe (igual à da base, sem mudança),
no celular (390 px em escala 3), relógio da página em 10/01/2027 10:00, tudo pela interface:
A) Visão geral (Realizado, Janeiro 2027) numa foto alta (390 × 3000, a página inteira), para a câmera descer como quem rola a tela;
B) toque em “Educação” em “Top saídas” (o site leva a Transações com a categoria filtrada), foto de 390 × 1000 para a lista caber.
Números da tela (assert no gerador): rosca “Despesas R$ 4.820,00 · 6 categorias”; Top saídas: Casa R$ 2.300,00 48%, Educação
R$ 1.450,00 30%, Mercado R$ 402,30 8%, Transporte R$ 392,00 8%, Bares e restaurantes R$ 212,50 4%, Saúde R$ 63,20 1%
(soma 4.820,00). Transações filtrada: “2 transações · 1 paga · 1 pendente · somam R$ 2.390,00 · 776 no histórico”: Material escolar
−R$ 940,00 pendente (ter, 12 de janeiro) e Escola −R$ 1.450,00 paga (dom, 10 de janeiro).
De onde vêm (estado.py): até 10/01, padaria 38,50 (02/01), mercado 402,30 e combustível 392,00 (04/01), farmácia 63,20 (08/01),
restaurante 174,00 (09/01), aluguel 2.300 e escola 1.450 (10/01, fixas pagas no dia); o material escolar (940, lançado em dezembro)
vence em 12/01. O gancho usa as 3 maiores da tela, sem o ano de 2026 (pauta).
Selo e sobretítulo da série: equipes/ja/selo_comece2027.py, sem mudança.
Diferença do que já saiu: 26/11 (três categorias levam dois terços) e 06/12 (o ano em 5 números) olharam 2026; aqui é o mês em curso,
o passo 2 da série, com o toque na categoria que abre os lançamentos dela (ainda não mostrado) e a mensagem de categorizar certo."""

POST = {
    "pasta": "2027-01-10_reel-passo-2-para-onde-vai",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "Comece 2027, passo 2 de 4, o caminho: para onde foi o dinheiro em janeiro. Na Visão geral, Por categoria e Top saídas mostram as maiores despesas do mês (Casa, Educação e Mercado até 10/01 no exemplo), e um toque na categoria abre os lançamentos dela; a categoria certa no lançamento faz o gráfico dizer a verdade",
    "pilar": "Produto (Visão geral: Por categoria e Top saídas) · série Comece 2027, passo 2",
    "data_longa": "domingo, 10 de janeiro de 2027",
    "data_curta": "domingo, 10/01/2027",
    "data_mockup": "10 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-10T10:00:00",
    "video": "saida/2027-01-10_reel-passo-2-para-onde-vai/reel.mp4",
    "capa": "saida/2027-01-10_reel-passo-2-para-onde-vai/capa.jpg",
    "previa": "saida/2027-01-10_reel-passo-2-para-onde-vai/previa.mp4",
    "slides": [
        "Capa da grade (verde suave) · COMECE 2027 · PASSO 2 DE 4 · Para onde vai? · O selo do passo 2 grande (quadrado tinta com o 2 em menta e os 4 tracinhos, os dois primeiros acesos) e “O caminho” embaixo.",
        "0 a 3,6 s · Gancho (verde suave) · Para onde foi o seu dinheiro em janeiro? · Desde o primeiro quadro, três barras coral crescem com o valor contando: Casa R$ 2.300,00; Educação R$ 1.450,00; Mercado R$ 402,30. · Até 10/01, no exemplo: R$ 4.820,00 em 6 categorias.",
        "3,6 a 5,4 s · Selo da série (tinta) · COMECE 2027 · PASSO 2 DE 4 · O selo 2 · O caminho. · Para onde vai o seu dinheiro?",
        "5,5 a 7,9 s · Na Visão geral, desça até Por categoria. · Tela real no celular (10/01/2027): a câmera desce da Visão geral até a rosca, com anel em “Despesas R$ 4.820,00 · 6 categorias”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "7,9 a 10,2 s · Top saídas: as maiores despesas do mês. · Anel em Casa R$ 2.300,00 48%, Educação R$ 1.450,00 30% e Mercado R$ 402,30 8% (embaixo, Transporte, Bares e restaurantes e Saúde).",
        "10,3 a 12,6 s · Toque numa categoria: aparecem os lançamentos dela. · Toque em Educação: Transações filtrada, com anel em “2 transações · 1 paga · 1 pendente · somam R$ 2.390,00”.",
        "12,7 a 14,9 s · A escola já saiu. O material escolar vence dia 12. · Anel nas duas linhas: Material escolar −R$ 940,00 pendente (12 de janeiro) e Escola −R$ 1.450,00 paga (10 de janeiro).",
        "15,0 a 17,0 s · Categoria certa no lançamento: o gráfico diz a verdade. · Desenho: o lançamento “Material escolar −R$ 940,00”, uma seta e a etiqueta “Educação” com um visto. · Cada lançamento na sua categoria. É assim que Por categoria e Top saídas acertam.",
        "17,0 a 19,8 s · Fechamento (verde) · Passo 2: o caminho. Visão geral no timtimcash. · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Para onde foi o seu dinheiro em janeiro?\n\n"
        "É o passo 2 da série Comece 2027: o caminho. Lance cada gasto com a categoria certa. Na Visão geral, Por categoria e Top saídas mostram para onde o dinheiro foi no mês.\n\n"
        "No exemplo do vídeo, até 10/01 saíram R$ 4.820,00 em 6 categorias. As maiores: Casa, R$ 2.300,00 (48%); Educação, R$ 1.450,00 (30%); Mercado, R$ 402,30 (8%).\n\n"
        "Um toque numa categoria abre os lançamentos dela. Em Educação, a escola já foi paga e o material escolar, de R$ 940,00, vence dia 12.\n\n"
        "Quinta, 14/01, vem o passo 3: quanto cabe em cada categoria. Salve para fazer junto.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#organizacaofinanceira #controledegastos #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Primeiro domingo depois do salário e das contas fixas do dia 10: o mês já tem movimento para mostrar o caminho do dinheiro, e a série Comece 2027 chega ao passo 2."),
        ("O que desperta interesse", "A pergunta que todo mundo se faz em janeiro e três barras que crescem com os valores do mês já no primeiro segundo."),
        ("Benefício para o público", "Aprende a ler Por categoria e Top saídas, a abrir os lançamentos de uma categoria com um toque e por que categorizar certo muda o retrato do mês."),
        ("Como contribui para o perfil", "Continua a série com o mesmo selo e mostra em tela real o toque na categoria que leva às transações, uma função ainda inédita no perfil."),
    ],
    "alt": [
        "Reel de 20 segundos. Num fundo verde-claro, a pergunta Para onde foi o seu dinheiro em janeiro? e três barras que crescem com os valores do mês até 10/01: Casa, R$ 2.300,00; Educação, R$ 1.450,00; Mercado, R$ 402,30; "
        "no exemplo, R$ 4.820,00 em 6 categorias. Num fundo escuro, o selo da série: Comece 2027, passo 2 de 4, O caminho. Depois, telas reais do timtimcash no celular, com dados de exemplo: a Visão geral rola até Por categoria, "
        "com a rosca de despesas de R$ 4.820,00, e Top saídas, com Casa 48%, Educação 30% e Mercado 8%. Um toque em Educação abre Transações filtrada: 2 transações que somam R$ 2.390,00, a escola paga em 10 de janeiro "
        "e o material escolar de R$ 940,00, pendente para 12 de janeiro. Um desenho liga o lançamento Material escolar à etiqueta Educação: categoria certa no lançamento, o gráfico diz a verdade. "
        "Passo 2: o caminho. Visão geral no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/a-visao-geral-inteira.jpg · Visão geral no celular, Janeiro 2027, Realizado, site build 2026-10-19.5, cópia da conta sem mudança, relógio em 10/01/2027 10:00, a página inteira (390 × 3000): rosca “Despesas R$ 4.820,00 · 6 categorias” e “Top saídas” · 5,5 a 11,2 s (a câmera desce do topo até Top saídas)",
        "telas/b-transacoes-educacao.jpg · depois do toque em “Educação”: Transações filtrada (390 × 1000), “2 transações · 1 paga · 1 pendente · somam R$ 2.390,00 · 776 no histórico”, Material escolar −R$ 940,00 pendente e Escola −R$ 1.450,00 paga · 11,2 a 14,9 s",
        "telas/caixas.json · posições medidas na captura e o texto de cada tela, usados nos anéis, no toque e nos assert do roteiro",
    ],
}
