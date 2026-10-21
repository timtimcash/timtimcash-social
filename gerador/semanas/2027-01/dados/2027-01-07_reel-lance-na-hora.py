# -*- coding: utf-8 -*-
"""Quinta 07/01/2027 · Reel "Lance na hora" (produto: Nova transação, o gesto de lançar; capa verde suave). Equipe jr.
Vídeo, capa e prévia gerados por equipes/jr/reel_07.py (assert nos números lidos da tela); telas capturadas por
equipes/jr/captura_07.py no site build 2026-10-19.5, na cópia da conta da equipe (igual à da base), no celular
(390 × 760 em escala 3), relógio da página em 07/01/2027 10:00, tudo pela interface: Transações (Janeiro 2027) › toque no “+” ›
“Nova transação” (já em “Despesa”) › valor tecla a tecla, 1-8-5-0 (a máscara enche pelos centavos: R$ 0,01, 0,18, 1,85, 18,50) ›
descrição “Hortifruti” letra a letra (até “Hortifrut”, a categoria segue “Alimentação”; com a palavra inteira, o site troca para
“Mercado”, selo “sugerida”; o autocompletar mostra “Hortifruti do Bairro · Mercado · 14x”) › “Já foi pago” ligado, como nasce
(“Afeta o saldo real da conta agora”) › “Lançar despesa” › aviso “Transação adicionada” › a lista rolada até quinta, 7 de janeiro:
“Hortifruti · Mercado · Conta corrente · −R$ 18,50 · paga”. O resumo passa de “13 transações · 5 pagas · 8 pendentes · 774 no
histórico” para “14 transações · 6 pagas · 8 pendentes · 775 no histórico”.
MUDANÇA NA CONTA (só nesta captura): o lançamento de R$ 18,50 em 07/01 foi feito pela interface, na sessão do navegador; a conta de base
(estado.py da base) não muda e os outros posts não o têm (no Reel de 10/01, Mercado aparece com R$ 402,30, sem ele).
Por que “Hortifruti” e não “padaria” (exemplo da pauta): pela lista de sugestões do site, “padaria” sugere “Alimentação”, a mesma
categoria com que o formulário já abre, e o selo “sugerida” não aparece; “hortifruti” sugere “Mercado” e mostra o selo.
Computador (1440 × 900, mesmo relógio): a tecla N abre a “Nova transação”; o botão final tem o título “Lançar (Cmd+Enter)” e os atalhos
“Meta+Enter Control+Enter” (lido na captura). FUNCIONALIDADES.md: “Cmd+Enter (ou Ctrl+Enter) lança ou salva a transação”.
Diferença do que já saiu: 04/11 mostrou a busca e a soma em Transações; 14/12 lançou uma despesa com Recorrência “Fixa” para o ano todo.
Aqui é o hábito de lançar na hora: o tempo do gesto (o cronômetro), “Já foi pago” ligado, a linha que aparece na lista e o atalho do
computador."""

POST = {
    "pasta": "2027-01-07_reel-lance-na-hora",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "Lance na hora: o gasto que não é anotado some. Em Nova transação, o valor, a descrição (a categoria vem sugerida) e Lançar despesa levam poucos segundos, e a linha aparece em Transações; no computador, Cmd+Enter (ou Ctrl+Enter) lança",
    "pilar": "Produto (Nova transação) · hábito de começo de ano",
    "data_longa": "quinta-feira, 7 de janeiro de 2027",
    "data_curta": "quinta-feira, 07/01/2027",
    "data_mockup": "7 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-07T10:00:00",
    "video": "saida/2027-01-07_reel-lance-na-hora/reel.mp4",
    "capa": "saida/2027-01-07_reel-lance-na-hora/capa.jpg",
    "previa": "saida/2027-01-07_reel-lance-na-hora/previa.mp4",
    "slides": [
        "Capa da grade (verde suave) · TRANSAÇÕES · Lance em 5 segundos. (“5 segundos.” em verde escuro) · Um botão “+” grande desenhado, verde com o sinal branco, e dois anéis em volta, como um toque.",
        "0 a 3,3 s · Gancho (tinta) · O gasto que você não anota some. (“some” em menta) · Desde o primeiro quadro, um cronômetro dá a volta de 0 a 5 s enquanto o valor é digitado pelos centavos, como no site: R$ 0,01, 0,18, 1,85, 18,50 (em coral); embaixo, “Hortifruti · Mercado” e a pílula “Lançado”.",
        "3,4 a 5,3 s · Toque no +. · Tela real de Transações no celular (07/01/2027) e o toque no botão “+”; abre a “Nova transação”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "5,3 a 7,9 s · Despesa: digite o valor. · Anel em “Despesa” (já marcada); toque em “toque para digitar o valor” e o valor tecla a tecla, de R$ 0,01 a R$ 18,50; anel no valor.",
        "7,9 a 10,8 s · Escreva o que foi: a categoria vem sugerida. · “Hortifruti” letra a letra; a categoria troca sozinha de “Alimentação” para “Mercado”, com o selo “sugerida” (anel).",
        "10,8 a 13,2 s · Já foi pago fica ligado. Toque em Lançar despesa. · Anel em “Já foi pago · Afeta o saldo real da conta agora”; toque em “Lançar despesa” e o aviso “Transação adicionada”.",
        "13,3 a 15,4 s · Pronto: já está em Transações. · A lista no dia 7 de janeiro, com anel na linha nova: Hortifruti, Mercado, Conta corrente, −R$ 18,50, paga.",
        "15,5 a 17,6 s · No computador, Cmd+Enter lança. · Duas teclas desenhadas, “⌘ Cmd” e “↵ Enter”, que se apertam; “Ou Ctrl+Enter.” e “Lança ou salva a transação”.",
        "17,6 a 20,4 s · Fechamento (verde) · Lance na hora. Transações no timtimcash. · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "O gasto que você não anota some.\n\n"
        "Lançar na hora funciona porque você ainda lembra o que foi, quanto foi e em que categoria entra. No fim do mês, os pequenos gastos já sumiram da memória.\n\n"
        "No timtimcash: toque no +, digite o valor e escreva o que foi. Enquanto você digita, o site sugere a categoria. Já foi pago fica ligado, e Lançar despesa põe a linha em Transações. No exemplo do vídeo, R$ 18,50 no hortifruti, em Mercado.\n\n"
        "No computador, Cmd+Enter (ou Ctrl+Enter) lança sem tirar a mão do teclado.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#controlefinanceiro #organizacaofinanceira #financaspessoais #controledegastos #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Primeira semana do ano, quando a vontade de se organizar está no auge: o hábito que sustenta a série Comece 2027 é lançar cada gasto na hora."),
        ("O que desperta interesse", "Uma frase que todo mundo reconhece (o gasto que some) e um cronômetro que fecha a volta enquanto o valor é digitado, já no primeiro segundo."),
        ("Benefício para o público", "Vê, passo a passo e em tela real, que lançar leva segundos: o valor, a descrição com a categoria sugerida, Já foi pago e o atalho do computador."),
        ("Como contribui para o perfil", "Mostra a interface real com toques visíveis e reforça o timtimcash como algo do dia a dia, sem conexão com o banco: a pessoa decide o que entra."),
    ],
    "alt": [
        "Reel de 20 segundos. Num fundo escuro, a frase O gasto que você não anota some, e um cronômetro que dá a volta de 0 a 5 segundos enquanto o valor R$ 18,50 é digitado, "
        "com Hortifruti, Mercado e a pílula Lançado. Depois, telas reais do timtimcash no celular, com dados de exemplo: o toque no botão de mais em Transações, a Nova transação em Despesa, "
        "o valor digitado até R$ 18,50, a descrição Hortifruti digitada e a categoria que muda sozinha de Alimentação para Mercado, com o selo sugerida. Já foi pago fica ligado, o toque em Lançar despesa "
        "e o aviso Transação adicionada; na lista, a linha nova de 7 de janeiro: Hortifruti, menos R$ 18,50, paga. Duas teclas desenhadas, Cmd e Enter, mostram que no computador Cmd+Enter, ou Ctrl+Enter, lança. "
        "Lance na hora. Transações no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/a-transacoes.jpg · Transações no celular, Janeiro 2027, site build 2026-10-19.5, cópia da conta, relógio em 07/01/2027 10:00: “13 transações · 5 pagas · 8 pendentes · 774 no histórico” e o botão “+” · 3,3 a 4,6 s",
        "telas/b-nova-0.jpg · a folha “Nova transação”, em “Despesa”, com R$ 0,00, “Hoje 07/01”, “Já foi pago” ligado e “Alimentação” · 4,6 a 6,8 s",
        "telas/c-valor-1.jpg a c-valor-4.jpg · o valor tecla a tecla: R$ 0,01, 0,18, 1,85, 18,50 · 6,8 a 8,3 s",
        "telas/d-desc-01.jpg a d-desc-10.jpg · “Hortifruti” letra a letra (até “Hortifrut”, Alimentação; com a palavra inteira, “Mercado sugerida”) · 8,3 a 9,4 s",
        "telas/e-sugerida.jpg · “Categoria · Mercado sugerida”, o autocompletar “Hortifruti do Bairro · Mercado · 14x” e “Lançar despesa” · 9,4 a 12,6 s",
        "telas/f-lancado.jpg · de volta a Transações, com o aviso “Transação adicionada” e “14 transações · 6 pagas · 8 pendentes · 775 no histórico” · 12,6 a 13,7 s",
        "telas/g-transacoes-depois.jpg · a lista rolada até quinta, 7 de janeiro: “Hortifruti · Mercado · Conta corrente · −R$ 18,50 · paga” · 13,7 a 15,4 s",
        "telas/h-transacoes-topo-depois.jpg e i-computador-nova.jpg · Transações no topo depois do lançamento e a “Nova transação” no computador (tecla N), que confirma o título “Lançar (Cmd+Enter)” · conferência, não aparecem no vídeo",
        "telas/caixas.json · posições medidas na captura e o texto de cada tela, usados nos anéis, nos toques e nos assert do roteiro",
    ],
}
