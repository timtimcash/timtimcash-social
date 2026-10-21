# -*- coding: utf-8 -*-
"""Sábado 20/02/2027 · Reel "Faxina de sábado" (produto: recategorizar em lote; capa tinta). Equipe fs.
Vídeo, capa e prévia gerados por equipes/fs/reel_20.py (com assert nos textos lidos da tela e na conta); telas capturadas por
equipes/fs/captura_20.py no site build 2026-10-19.5, no celular (390 × 1000 em escala 3), relógio da página em 20/02/2027 10:00,
numa CÓPIA da conta (pasta da equipe fs; estado.py igual ao da base) no cenário "faxina" de cenarios.py: os 9 lançamentos
"Mercado da Vila" de janeiro e fevereiro de 2027 (04/01 R$ 402,30, 11/01 R$ 437,80, 18/01 R$ 389,60, 25/01 R$ 354,90, 30/01
R$ 318,20, 01/02 R$ 396,40, 05/02 R$ 412,70, 12/02 R$ 421,30 e 19/02 R$ 379,20; soma R$ 3.512,40) estão "Sem categoria", o marcador
que o site põe no que chega de um extrato .ofx sem categoria reconhecida pelo nome (o nome "Mercado da Vila" não está na lista de
sugestões do site), e o plano de despesas ganha "Sem categoria", como a importação faz. Nenhum valor muda. Depois da faxina feita na
tela, a conta fica exatamente como a de base, e os números do "depois" são os da conta de base em 20/02/2027.
Passo a passo real (período Ano 2027, pelo calendário do topo, "Ano atual"): Visão geral, "Por categoria" (antes: despesas de
R$ 19.005,50 em 11 categorias; "Sem categoria R$ 3.512,40 18%") -> Transações -> busca "mercado da vila", letra a letra ("9 transações
· 9 pagas · 0 pendentes · somam R$ 3.512,40 · 823 no histórico") -> faixa "Agir sobre as 9 filtradas" -> "Recategorizar todas" ->
"merc" no seletor -> "Mercado" -> aviso "9 transações atualizadas para "Mercado"" com "Desfazer" -> "Por categoria" (depois: as
mesmas despesas de R$ 19.005,50 em 10 categorias; "Mercado R$ 3.897,50 21%" = R$ 3.512,40 + Hortifruti do Bairro R$ 196,70 e
R$ 188,40). O número da pauta era 12 ("conferir o número na tela"): na tela, são 9.
Diferença do que já saiu: 04/11 e 10/02 usaram a busca e a soma; aqui é a ação em lote (Recategorizar todas) e o antes e depois do
Por categoria."""

POST = {
    "pasta": "2027-02-20_reel-faxina-de-sabado",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "Faxina de sábado: 9 lançamentos sem categoria arrumados de uma vez, com a busca e “Recategorizar todas”; no Por categoria, a fatia “Sem categoria” vira Mercado",
    "pilar": "Organização · produto (Transações, ações em lote)",
    "data_longa": "sábado, 20 de fevereiro de 2027",
    "data_curta": "sábado, 20/02/2027",
    "data_mockup": "20 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-20T10:00:00",
    "video": "saida/2027-02-20_reel-faxina-de-sabado/reel.mp4",
    "capa": "saida/2027-02-20_reel-faxina-de-sabado/capa.jpg",
    "previa": "saida/2027-02-20_reel-faxina-de-sabado/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · FAXINA DE SÁBADO · 9 lançamentos de uma vez. · Quatro cartões “Mercado da Vila” com a etiqueta verde “Mercado”.",
        "0 a 2,8 s · Gancho (tinta) · FAXINA DE SÁBADO · 9 lançamentos sem categoria? · Desde o primeiro quadro, 9 cartões “Mercado da Vila” (as datas e os valores da conta de exemplo) bagunçados se alinham e trocam a etiqueta cinza “Sem categoria” pela verde “Mercado” · Arrumados em 10 segundos.",
        "3,0 a 5,35 s · Em Transações, busque o nome: 9 sem categoria. · Tela real de Transações no celular (Ano 2027): a busca “mercado da vila” digitada letra a letra; anel em “9 transações · 9 pagas · 0 pendentes · somam R$ 3.512,40”.",
        "5,5 a 7,75 s · Recategorizar todas e escolha Mercado. · Anel na faixa “Agir sobre as 9 filtradas”; toque em “Recategorizar todas”; no seletor de categoria, “merc” e um toque em “Mercado”.",
        "7,9 a 10,0 s · Pronto: os 9 de uma vez. · O aviso “9 transações atualizadas para “Mercado”” com Desfazer (anel); a lista mostra “Mercado da Vila · Mercado”.",
        "10,15 a 14,25 s · E o gráfico volta a dizer para onde foi o dinheiro. · “Por categoria” do ano na Visão geral: ANTES, anel em “Sem categoria R$ 3.512,40 18%”; DEPOIS, anel em “Mercado R$ 3.897,50 21%”, com o mesmo total de R$ 19.005,50.",
        "14,45 a 16,85 s · Faxina em 3 passos. (tinta) · Busque o nome (em Transações, no período que quiser) · Recategorizar todas (age sobre todas as filtradas) · Escolha a categoria (e, se errar, tem Desfazer).",
        "16,85 a 19,6 s · Fechamento (verde) · Transações no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Faxina de sábado: 9 lançamentos sem categoria, arrumados de uma vez.\n\n"
        "No exemplo, as compras do Mercado da Vila de janeiro e fevereiro ficaram “Sem categoria”, como chega do extrato do banco o que "
        "o timtimcash não reconhece pelo nome. Somam R$ 3.512,40, ou 18% das despesas do ano, sem dizer para onde foram.\n\n"
        "A faxina: em Transações, busque “mercado da vila”. A faixa “Agir sobre as 9 filtradas” traz “Recategorizar todas”. Escolha "
        "Mercado e pronto: os 9 mudam juntos, e o aviso tem Desfazer.\n\n"
        "No Por categoria, a fatia cinza vira Mercado: R$ 3.897,50, 21% do ano.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#organizacaofinanceira #controlefinanceiro #financaspessoais #educacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de semana depois do Carnaval, o momento de pôr a casa em ordem antes de fevereiro fechar; quem importa o extrato do banco acumula lançamentos sem categoria."),
        ("O que desperta interesse", "A pergunta com número no primeiro segundo (“9 lançamentos sem categoria?”) e a bagunça que se arruma sozinha na tela, com o antes e depois do gráfico."),
        ("Benefício para o público", "Corrigir de uma vez o que está fora do lugar, em vez de abrir lançamento por lançamento, e ver o Por categoria contar a verdade."),
        ("Como contribui para o perfil", "Primeira vez que o perfil mostra a ação em lote (“Agir sobre as N filtradas” e “Recategorizar todas”), com telas reais e o Desfazer, que dá segurança."),
    ],
    "alt": [
        "Reel de 20 segundos. Fundo escuro: 9 lançamentos sem categoria? Nove cartões Mercado da Vila, de 4 de janeiro a 19 de fevereiro, "
        "aparecem bagunçados, se alinham e trocam a etiqueta cinza Sem categoria pela verde Mercado; arrumados em 10 segundos. Telas reais "
        "do timtimcash no celular, com dados de exemplo. Em Transações, no ano de 2027, a busca mercado da vila mostra 9 transações que "
        "somam R$ 3.512,40, todas sem categoria. A faixa Agir sobre as 9 filtradas tem o botão Recategorizar todas; no seletor, merc e "
        "Mercado. O aviso diz 9 transações atualizadas para Mercado, com Desfazer, e a lista passa a mostrar Mercado. No gráfico Por "
        "categoria do ano, antes: Sem categoria, R$ 3.512,40, 18%; depois: Mercado, R$ 3.897,50, 21%, com o mesmo total de despesas. "
        "Faxina em 3 passos: busque o nome, Recategorizar todas, escolha a categoria; se errar, tem Desfazer. Transações no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-faxina-1-por-categoria-antes.jpg · Visão geral, Ano 2027, rolada até “Por categoria”: Sem categoria R$ 3.512,40 18% (celular 390 × 1000 em escala 3, build 2026-10-19.5, cópia da conta no cenário faxina, relógio da página em 20/02/2027 10:00) · 10,15 a 12,25 s",
        "telas/celular-faxina-2-transacoes.jpg · Transações, Ano 2027, antes da busca (mesmo relógio) · 3,0 a 3,75 s",
        "telas/celular-faxina-3-busca-01.jpg a celular-faxina-3-busca-15.jpg · a busca “mercado da vila” digitada letra a letra, até “9 transações · 9 pagas · 0 pendentes · somam R$ 3.512,40” e a faixa “Agir sobre as 9 filtradas” · 3,75 a 6,35 s",
        "telas/celular-faxina-4-seletor.jpg e celular-faxina-5-seletor-merc.jpg · o seletor de categoria aberto por “Recategorizar todas” e a busca “merc” com “Mercado” · 6,35 a 7,5 s",
        "telas/celular-faxina-6-pronto.jpg · o aviso “9 transações atualizadas para “Mercado”” com Desfazer · 7,5 a 9,0 s",
        "telas/celular-faxina-7-lista.jpg · a lista depois do aviso, com “Mercado da Vila · Mercado · Conta corrente” · 9,0 a 10,15 s",
        "telas/celular-faxina-8-por-categoria-depois.jpg · “Por categoria” depois da faxina: Mercado R$ 3.897,50 21% (os números da conta de base) · 12,25 a 14,6 s",
        "telas/caixas.json · posições medidas na captura, o texto de cada tela, o aviso e os 9 lançamentos do cenário",
    ],
}
