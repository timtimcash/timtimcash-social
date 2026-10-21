# -*- coding: utf-8 -*-
"""Terça 23/02/2027 · Reel "Meta de receita" (produto: Orçamentos, metas de receita; capa verde). Equipe fs.
Trocou de dia com "Nova remessa, câmbio na hora" a pedido da revisão (este era o de 25/02); capturado de novo com o relógio em 23/02.
Vídeo, capa e prévia gerados por equipes/fs/reel_23.py (com assert nos textos lidos da tela e no cenário); telas capturadas por
equipes/fs/captura_23.py no site build 2026-10-19.5, no celular (390 × 1000 em escala 3), relógio da página em 23/02/2027 10:00, numa
CONTA DE EXEMPLO SEPARADA (cenário "renda" de cenarios.py, na cópia da equipe fs, pedido da revisão, como o 24/02): só uma "Conta corrente",
sem orçamentos e sem nenhum lançamento da conta principal, com duas receitas de exemplo "Trabalho extra" em "Outras receitas",
12/02/2027 R$ 450,00 e 22/02/2027 R$ 300,00 (R$ 750 em fevereiro), e nenhuma meta de receita. Assim, as receitas extras não aparecem
na conta principal, que nos outros posts de fevereiro tem "Receitas R$ 9.960". A nota da tela, no vídeo, ganha a linha "Conta de
exemplo só com a renda extra.", e a tela de Orçamentos mostra só a meta de receita ("Sem limites definidos" antes; "Sem limites de
despesa" e o painel "Metas de receita" depois).
Passo a passo real: Orçamentos ("Sem limites definidos") -> "Definir limites" -> janela "Definir orçamentos" ("Limite mensal de despesa e meta mensal de
receita"), aba "Receitas" -> no campo de "Outras receitas", R$ 1.000,00 tecla a tecla ("META TOTAL POR MÊS · 1 categoria · R$ 1.000,00")
-> "Salvar" (aviso "Orçamentos salvos") -> painel "Metas de receita · Fevereiro 2027": "Outras receitas R$ 750 de R$ 1.000 · 75% ·
Faltam R$ 250 para a meta" -> "+" -> "Receita" -> R$ 250,00 -> "Trab" -> a descrição já usada "Trabalho extra · Outras receitas · 2x"
(traz a categoria) -> "Lançar receita" (aviso "Transação adicionada") -> "R$ 1.000 de R$ 1.000 · 100% · Meta cumprida".
Conta: 450 + 300 = 750; 1.000 − 750 = 250; 750 + 250 = 1.000. A receita de R$ 250 fica só na captura (o site falso descarta as
gravações). A meta é mensal ("meta mensal de receita"): no mês seguinte, o painel conta as receitas do novo mês.
Diferença do que já saiu: 11/10 e 14/01 mostraram limites de despesa; aqui é a meta de receita, inédita no perfil."""

POST = {
    "pasta": "2027-02-23_reel-meta-de-receita",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 19 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 19 s",
    "tema": "Renda extra com meta: em Orçamentos, a meta mensal de receita para “Outras receitas”; o painel “Metas de receita” mostra quanto falta e avisa quando a meta é cumprida",
    "pilar": "Planejamento · produto (Orçamentos, metas de receita)",
    "data_longa": "terça-feira, 23 de fevereiro de 2027",
    "data_curta": "terça-feira, 23/02/2027",
    "data_mockup": "23 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-23T10:00:00",
    "video": "saida/2027-02-23_reel-meta-de-receita/reel.mp4",
    "capa": "saida/2027-02-23_reel-meta-de-receita/capa.jpg",
    "previa": "saida/2027-02-23_reel-meta-de-receita/previa.mp4",
    "slides": [
        "Capa da grade (verde) · RENDA EXTRA · Ponha uma meta. · Uma barra cheia, “Outras receitas · 100%”, “R$ 1.000 de R$ 1.000” e o selo “Meta cumprida”.",
        "0 a 2,8 s · Gancho (verde suave) · RENDA EXTRA · Tem renda extra? Ponha uma meta. · Desde o primeiro quadro, três receitas de exemplo de “Trabalho extra” (12/02 +R$ 450, 22/02 +R$ 300 e 23/02 +R$ 250) caem numa barra que enche até a “meta R$ 1.000”; o contador vai a R$ 1.000 “de R$ 1.000 no mês” e aparece “Meta cumprida”.",
        "3,0 a 5,45 s · Em Orçamentos, Definir limites e a aba Receitas. · Tela real de Orçamentos no celular (fevereiro de 2027), numa conta de exemplo só com a renda extra (a nota diz “Conta de exemplo só com a renda extra.”): “Sem limites definidos”, anel e toque em “Definir limites”; a janela “Definir orçamentos”; anel e toque na aba “Receitas”.",
        "5,6 a 8,1 s · Uma meta por mês: R$ 1.000 em Outras receitas. · R$ 1.000,00 digitado tecla a tecla no campo de “Outras receitas” (anel) e o toque em “Salvar”.",
        "8,25 a 10,55 s · Fevereiro até aqui: faltam R$ 250. · Painel “Metas de receita”: “Outras receitas R$ 750 de R$ 1.000 · 75% · Faltam R$ 250 para a meta” (anel).",
        "10,7 a 13,45 s · Entrou mais um trabalho? Lance a receita. · O “+”, “Receita”, R$ 250,00, “Trab” e a descrição já usada “Trabalho extra” (anel), que traz “Outras receitas”; toque em “Lançar receita”.",
        "13,6 a 16,1 s · Meta cumprida. No mês seguinte, a barra recomeça. · O painel: “Outras receitas R$ 1.000 de R$ 1.000 · 100% · Meta cumprida” (anel).",
        "16,35 a 19,15 s · Fechamento (verde) · Orçamentos no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Tem renda extra? Ponha uma meta para ela.\n\n"
        "No timtimcash, a meta de receita fica em Orçamentos: Definir limites, aba Receitas. No vídeo, numa conta de exemplo só com a "
        "renda extra, a meta é de R$ 1.000 por mês em Outras receitas, onde entra o trabalho extra.\n\n"
        "Com dois trabalhos em fevereiro (R$ 450 e R$ 300), o painel Metas de receita mostra R$ 750 de R$ 1.000 e avisa: faltam R$ 250. "
        "Lançou o terceiro, de R$ 250? Meta cumprida.\n\n"
        "A meta é mensal: no mês seguinte, a barra começa do zero.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#rendaextra #metasfinanceiras #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de fevereiro, quando dá para ver se o mês fechou a conta; renda extra (um trabalho por fora, uma venda) é comum no começo do ano para cobrir os gastos de janeiro e fevereiro."),
        ("O que desperta interesse", "A pergunta direta (“Tem renda extra?”) com a barra que enche até a meta já no primeiro segundo e o selo “Meta cumprida” no fim."),
        ("Benefício para o público", "Transformar a renda extra num objetivo mensal claro, com quanto falta à vista, em vez de deixar o dinheiro entrar sem rumo."),
        ("Como contribui para o perfil", "Mostra uma função inédita no perfil (metas de receita) com telas reais, e equilibra a série de orçamentos, que até aqui só tratou de limites de gasto."),
    ],
    "alt": [
        "Reel de 19 segundos. Fundo verde-claro: tem renda extra? Ponha uma meta. Três receitas de exemplo de trabalho extra, de R$ 450, "
        "R$ 300 e R$ 250, caem numa barra que enche até a meta de R$ 1.000, e aparece Meta cumprida. Telas reais do timtimcash no celular, "
        "com dados de exemplo, numa conta de exemplo só com a renda extra. Em Orçamentos, sem limites definidos, Definir limites abre a janela Definir orçamentos; na aba Receitas, R$ 1.000 é digitado em "
        "Outras receitas, e Salvar. O painel Metas de receita mostra R$ 750 de R$ 1.000, 75%, faltam R$ 250 para a meta. Uma nova receita "
        "de R$ 250, Trabalho extra, é lançada pelo botão mais. O painel passa a mostrar R$ 1.000 de R$ 1.000, 100%, Meta cumprida; no mês "
        "seguinte, a barra recomeça. Orçamentos no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-meta-1-orcamentos.jpg · Orçamentos de fevereiro de 2027, “Sem limites definidos” e o botão “Definir limites” (celular 390 × 1000 em escala 3, build 2026-10-19.5, conta de exemplo separada, só com a renda extra, relógio da página em 23/02/2027 10:00) · 3,0 a 3,9 s",
        "telas/celular-meta-2-despesas.jpg e celular-meta-3-receitas.jpg · a janela “Definir orçamentos”, na aba Despesas e na aba Receitas · 3,9 a 5,95 s",
        "telas/celular-meta-4-digita-1.jpg a celular-meta-4-digita-6.jpg · a meta de Outras receitas digitada tecla a tecla até R$ 1.000,00 (“META TOTAL POR MÊS · R$ 1.000,00”) · 5,95 a 7,75 s",
        "telas/celular-meta-5-faltam.jpg e celular-meta-6-faltam-limpo.jpg · o painel “Metas de receita” com o aviso “Orçamentos salvos” e depois dele: R$ 750 de R$ 1.000, 75%, Faltam R$ 250 para a meta · 7,75 a 11,0 s",
        "telas/celular-meta-7-receita.jpg, celular-meta-8-sugestao.jpg e celular-meta-9-preenchida.jpg · a Nova transação em Receita, R$ 250,00, “Trab” com a descrição já usada “Trabalho extra” e o formulário preenchido com Outras receitas · 11,0 a 13,1 s",
        "telas/celular-meta-10-cumprida.jpg e celular-meta-11-cumprida-limpo.jpg · o painel com o aviso “Transação adicionada” e depois dele: R$ 1.000 de R$ 1.000, 100%, Meta cumprida · 13,1 a 16,35 s",
        "telas/caixas.json · posições medidas na captura, o texto de cada tela, os avisos, o valor digitado e o cenário (a conta separada com as duas receitas de exemplo)",
    ],
}
