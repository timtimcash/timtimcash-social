# -*- coding: utf-8 -*-
"""Quinta 18/02/2027 · Reel "Atalhos no computador" (produto: atalhos de teclado; capa verde). Equipe fs.
Vídeo, capa e prévia gerados por equipes/fs/reel_18.py (com assert nos textos lidos da tela e no código do site); telas capturadas
por equipes/fs/captura_18.py no site build 2026-10-19.5, na cópia da conta da equipe (pasta equipes/fs, estado.py igual ao da base, sem
mudança), no computador (1440 × 900 em escala 2), relógio da página em 18/02/2027 10:00.
Os cinco atalhos foram conferidos no código do site (index.html do build 2026-10-19.5): N chama openTxSheet() (Nova transação,
com o foco no valor); Cmd ou Ctrl + Enter chama _txCtaClick() (lança ou salva); Cmd ou Ctrl + K chama openGlobalSearch() (busca
global); F chama toggleFocusMode() (aviso "Modo foco ativado · pressione F para sair"); "?" chama showShortcutsHelp() (janela
"Atalhos de teclado", com Busca global Cmd+K, Nova transação N, Lançar ou salvar a transação Cmd+Enter, Buscar na lista /,
Modo foco F, Período anterior / seguinte, Ir para o período atual H, Desfazer a última ação Cmd+Z, Fechar modal Esc, Esta ajuda ?).
Interação real, tecla a tecla (Playwright aperta as teclas; Meta é o Cmd do Mac): N -> "3200" (R$ 32,00) -> clique em "Adicionar
descrição" -> "Cinema" -> a categoria muda sozinha para "Lazer e hobbies" com o selo "sugerida" (a lista de palavras do site:
CINEMA -> Lazer e hobbies) -> Cmd+Enter ("Transação adicionada"). O lançamento de exemplo existe só na captura (o site falso
descarta as gravações). Numa segunda sessão, sem o lançamento: Cmd+K -> "conta" (Contas e carteiras, AÇÃO; Pendentes, TELA;
Preferências, AÇÃO; Conta corrente, CONTA; Conta de luz, TRANSAÇÃO) -> Esc -> F (o menu lateral sai; o selo "MODO FOCO · F PARA
SAIR" no canto) -> F -> "?".
"3 segundos": numa terceira sessão, sem fotos, a mesma sequência (N, 4 teclas do valor, clique, 6 letras, Cmd+Enter) digitada a
0,12 s por tecla levou 2,0 s do N ao aviso "Transação adicionada" (caixas.json, tempo_lancamento_s).
Diferença do que já saiu: 07/01 mostrou o gesto de lançar no celular (com o "+"); aqui é o computador e os outros quatro atalhos."""

POST = {
    "pasta": "2027-02-18_reel-atalhos-no-computador",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "Atalhos no computador: N abre a Nova transação, Cmd + Enter lança, Cmd + K busca, F liga o Modo foco e ? mostra a lista; um gasto lançado em segundos sem sair do teclado, só com um clique na descrição",
    "pilar": "Produto (atalhos de teclado) · organização",
    "data_longa": "quinta-feira, 18 de fevereiro de 2027",
    "data_curta": "quinta-feira, 18/02/2027",
    "data_mockup": "18 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-18T10:00:00",
    "video": "saida/2027-02-18_reel-atalhos-no-computador/reel.mp4",
    "capa": "saida/2027-02-18_reel-atalhos-no-computador/capa.jpg",
    "previa": "saida/2027-02-18_reel-atalhos-no-computador/previa.mp4",
    "slides": [
        "Capa da grade (verde) · ATALHOS DE TECLADO · Lance em 3 segundos. · Teclas desenhadas: N (abre) e ⌘ + Enter (lança).",
        "0 a 2,8 s · Gancho (papel) · ATALHOS DE TECLADO · Lançar um gasto em 3 segundos? · Desde o primeiro quadro, a tecla N se aperta, o campo recebe “R$ 32,00 · Cinema”, as teclas ⌘ e Enter se apertam e aparece “Transação adicionada”.",
        "2,95 a 5,3 s · [N] abre a Nova transação. · Tela real da Visão geral no computador (fevereiro de 2027); a tecla N se aperta e a “Nova transação” abre, com o cursor no valor; a janela se aproxima da folha.",
        "5,45 a 8,05 s · Valor e descrição: a categoria vem sugerida. · R$ 32,00 digitado tecla a tecla, o clique em “Adicionar descrição”, “Cinema” letra a letra e a categoria que muda de Alimentação para “Lazer e hobbies” com o selo “sugerida” (anel).",
        "8,2 a 10,35 s · [⌘] + [Enter] lança. No Windows: Ctrl + Enter. · A folha fecha e o aviso “Transação adicionada” aparece de perto.",
        "10,5 a 12,85 s · [⌘] + [K] busca telas, ações, contas e lançamentos. · A busca global, vazia e depois com “conta”: Contas e carteiras (ação), Pendentes (tela), Preferências (ação), Conta corrente (conta) e Conta de luz (transações).",
        "13,0 a 15,1 s · [F] liga o Modo foco. O menu lateral sai e o conteúdo ganha a tela. F de novo, ele volta. · A tela inteira antes e depois; o aviso “Modo foco ativado · pressione F para sair” de perto.",
        "15,25 a 17,4 s · [?] mostra todos os atalhos. · A janela “Atalhos de teclado” de perto, com a lista do site.",
        "17,55 a 20,35 s · Fechamento (verde) · Atalhos no timtimcash · No navegador do computador. No Windows, Ctrl no lugar do Cmd. · Link na bio.",
    ],
    "legenda": (
        "Lance um gasto em 3 segundos no computador.\n\n"
        "No timtimcash, a tecla N abre a Nova transação com o cursor no valor. Digite o valor, clique na descrição e escreva: "
        "a categoria vem sugerida (no exemplo, “Cinema” vai para Lazer e hobbies). Cmd + Enter lança.\n\n"
        "Mais três atalhos: Cmd + K abre a busca de telas, ações, contas, categorias e lançamentos; F liga o Modo foco, que tira o "
        "menu lateral da frente; e ? mostra a lista completa.\n\n"
        "No Windows, use Ctrl no lugar do Cmd.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#atalhosdeteclado #produtividade #controlefinanceiro #organizacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fevereiro é o mês de pôr em dia o que ficou para trás depois do Carnaval, e quem usa o computador no trabalho lança mais rápido pelo teclado. É uma função que ainda não apareceu no perfil."),
        ("O que desperta interesse", "A pergunta com número no primeiro segundo (“em 3 segundos?”) e as teclas desenhadas se apertando, uma promessa que o vídeo cumpre na tela real."),
        ("Benefício para o público", "Lançar na hora, sem procurar botões, e achar qualquer coisa com Cmd + K: menos atrito para manter o hábito de anotar tudo."),
        ("Como contribui para o perfil", "Mostra o timtimcash no computador, com telas reais, e cinco atalhos conferidos no código do site; complementa o Reel de 07/01, que mostrou o gesto de lançar no celular."),
    ],
    "alt": [
        "Reel de 20 segundos. Lançar um gasto em 3 segundos? Teclas desenhadas se apertam: N, depois o campo recebe R$ 32,00 · Cinema, "
        "depois Cmd e Enter, e aparece Transação adicionada. Telas reais do timtimcash no computador, com dados de exemplo. A tecla N abre a "
        "Nova transação com o cursor no valor; o valor R$ 32,00 é digitado, um clique na descrição, Cinema, e a categoria muda sozinha para "
        "Lazer e hobbies, com o selo sugerida. Cmd mais Enter lança, e o aviso Transação adicionada aparece; no Windows, Ctrl mais Enter. "
        "Cmd mais K abre a busca global; com conta, aparecem ações, telas, a conta corrente e as contas de luz. F liga o Modo foco: o menu lateral "
        "sai e o conteúdo ganha a tela. O ponto de interrogação mostra a lista de atalhos de teclado. Atalhos no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/computador-0-visao-geral.jpg · Visão geral de fevereiro de 2027 no computador (1440 × 900 em escala 2, build 2026-10-19.5, relógio da página em 18/02/2027 10:00) · 2,95 a 3,6 s e 10,5 a 11,0 s e 13,0 a 13,7 s",
        "telas/computador-1-tecla-n.jpg · a Nova transação aberta pela tecla N, com o foco no valor (mesmo relógio) · 3,6 a 5,6 s",
        "telas/computador-2-valor-1.jpg a computador-2-valor-4.jpg · o valor digitado tecla a tecla até R$ 32,00 · 5,55 a 6,5 s",
        "telas/computador-3-descricao.jpg e computador-4-desc-1.jpg a computador-4-desc-6.jpg · o clique na descrição e “Cinema” letra a letra (com a lista de descrições já usadas) · 6,5 a 7,35 s",
        "telas/computador-5-sugerida.jpg · Categoria “Lazer e hobbies” com o selo “sugerida” · 7,35 a 8,85 s",
        "telas/computador-6-lancou.jpg · a folha fechada pelo Cmd+Enter e o aviso “Transação adicionada” · 8,85 a 10,5 s",
        "telas/computador-7-busca-vazia.jpg e computador-8-busca-1.jpg a computador-8-busca-5.jpg · a busca global (Cmd+K), vazia e com “conta” letra a letra (segunda sessão, sem o lançamento de exemplo) · 11,1 a 13,0 s",
        "telas/computador-9-modo-foco.jpg · o Modo foco ligado pela tecla F e o aviso “Modo foco ativado · pressione F para sair” · 13,75 a 15,8 s",
        "telas/computador-10-atalhos.jpg · a janela “Atalhos de teclado” aberta pela tecla “?” · 15,8 a 17,55 s",
        "telas/caixas.json · posições medidas na captura, o texto de cada tela, a categoria sugerida, os avisos e o tempo medido do N ao aviso (2,0 s)",
    ],
}
