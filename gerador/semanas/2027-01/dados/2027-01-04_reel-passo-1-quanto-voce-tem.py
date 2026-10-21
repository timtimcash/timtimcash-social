# -*- coding: utf-8 -*-
"""Segunda 04/01/2027 · Reel "Comece 2027 · Passo 1 de 4: quanto você tem?" (série Comece 2027, passo 1, O retrato; capa verde).
Equipe jr. Vídeo, capa e prévia gerados por equipes/jr/reel_04.py (assert nos números lidos da tela); telas capturadas por
equipes/jr/captura_04.py no site build 2026-10-19.5, na cópia da conta da equipe (igual à da base, sem mudança),
no celular (390 × 760 em escala 3), relógio da página em 04/01/2027 10:00, tudo pela interface: Visão geral › "Menu" (rolado até
"Configurar") › "Contas e carteiras" › "Nova conta" › nome "Carteira" letra a letra › "Tipo" › "Dinheiro / Carteira" › "Saldo atual"
digitado pelos centavos (R$ 0,01, 0,15, 1,50, 15,00, 150,00) › "Incluir no patrimônio total" ligado (como nasce).
A conta de exemplo "Carteira" NÃO é salva ("Adicionar conta" não é tocado): nada muda na conta, e o patrimônio segue R$ 112.730,86.
Números da tela (assert no gerador): "4 contas · todas no total do patrimônio", "PATRIMÔNIO CONSOLIDADO R$ 112.730,86"; Banco na Europa
R$ 11.525,40; Conta corrente R$ 18.230,86; Corretora no exterior R$ 60.000,00; Reserva R$ 22.974,60 (soma: 112.730,86).
De onde vêm (estado.py): a Corretora no exterior recebeu as 3 remessas em dólar, em reais (19.600 + 20.000 + 20.400 = 60.000); o Banco
na Europa recebeu a remessa de € 2.000 de 01/12/2026 com o IOF (11.400,00 + 125,40 = 11.525,40). Por isso o vídeo e a legenda dizem que
as contas lá fora entram pelo que custaram em reais e que o valor de hoje fica em Remessas (FUNCIONALIDADES.md e o carrossel de 18/12).
Selo e sobretítulo da série: equipes/ja/selo_comece2027.py (o mesmo dos outros posts da série), sem mudança.
Diferença do que já saiu: o carrossel de 18/12 ("Patrimônio: quanto você tem") explicou patrimônio, liquidez e o custo do exterior com
Contas e carteiras em 18/12; aqui é o passo 1 da série, em vídeo, com a soma que se monta e a folha "Nova conta" preenchida (como
cadastrar uma conta com o saldo de hoje), que ainda não tinha aparecido."""

POST = {
    "pasta": "2027-01-04_reel-passo-1-quanto-voce-tem",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Comece 2027, passo 1 de 4, o retrato: quanto você tem, somando tudo. Em Contas e carteiras, cada conta com o saldo de hoje e o Patrimônio consolidado já somado (R$ 112.730,86 em 4 contas no exemplo); a folha Nova conta mostra como incluir a conta que faltou",
    "pilar": "Produto (Contas e carteiras, Nova conta) · série Comece 2027, passo 1",
    "data_longa": "segunda-feira, 4 de janeiro de 2027",
    "data_curta": "segunda-feira, 04/01/2027",
    "data_mockup": "4 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-04T10:00:00",
    "video": "saida/2027-01-04_reel-passo-1-quanto-voce-tem/reel.mp4",
    "capa": "saida/2027-01-04_reel-passo-1-quanto-voce-tem/capa.jpg",
    "previa": "saida/2027-01-04_reel-passo-1-quanto-voce-tem/previa.mp4",
    "slides": [
        "Capa da grade (verde, logotipo negativo) · COMECE 2027 · PASSO 1 DE 4 · Quanto você tem? · O selo do passo 1 grande (quadrado tinta com o 1 em menta e os 4 tracinhos, o primeiro aceso) e “O retrato” embaixo.",
        "0 a 3,8 s · Gancho (papel) · Quanto você tem, somando tudo? · Desde o primeiro quadro, as 4 contas do exemplo entram uma a uma e a soma sobe: Conta corrente R$ 18.230,86; Reserva R$ 22.974,60; Corretora no exterior R$ 60.000,00; Banco na Europa R$ 11.525,40; PATRIMÔNIO · 4 CONTAS SOMADAS R$ 112.730,86 (em verde no fim). · Nota: Contas lá fora: entra o que custou em reais.",
        "3,8 a 5,6 s · Selo da série (tinta) · COMECE 2027 · PASSO 1 DE 4 · O selo 1 · O retrato. · Quanto você tem, somando tudo?",
        "5,6 a 9,5 s · Em Contas e carteiras, cada conta com o saldo de hoje. · Tela real no celular (04/01/2027): toque em “Menu”, o menu rolado até “Configurar”, toque em “Contas e carteiras”; anel em “Patrimônio consolidado R$ 112.730,86” e depois nas 4 contas (Banco na Europa, Conta corrente, Corretora no exterior, Reserva). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "9,6 a 11,5 s · Faltou alguma? Toque em Nova conta. · Anel e toque no botão “Nova conta”: abre a folha “Nova conta”.",
        "11,5 a 14,3 s · Dê um nome e escolha o tipo. · O nome “Carteira” digitado letra a letra; toque em “Tipo”, a folha “Tipo de conta” e o toque em “Dinheiro / Carteira”; anel na linha do tipo.",
        "14,4 a 16,2 s · Saldo atual: quanto tem na conta hoje. · O saldo digitado pelos centavos, até R$ 150,00, e anel na linha “Saldo atual · quanto tem na conta hoje”.",
        "16,3 a 18,1 s · Incluir no patrimônio total: o saldo entra na soma. · Anel no interruptor ligado (“o saldo soma ao total geral de contas”). A conta de exemplo não é salva.",
        "18,2 a 20,9 s · Fechamento (verde) · Passo 1: o retrato. Contas e carteiras no timtimcash. · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Quanto você tem, somando tudo?\n\n"
        "É o passo 1 da série Comece 2027: o retrato. Liste todas as suas contas, cada uma com o saldo de hoje: banco, carteira, investimento, lá fora. Em Contas e carteiras, o timtimcash mostra o Patrimônio consolidado, já somado.\n\n"
        "No exemplo do vídeo, 4 contas somam R$ 112.730,86. Faltou alguma? Toque em Nova conta, escolha o tipo, informe o Saldo atual e deixe ligado Incluir no patrimônio total.\n\n"
        "As contas lá fora entram pelo que custaram em reais. O valor de hoje, ao câmbio do dia, fica em Remessas ao exterior.\n\n"
        "Domingo, 10/01, vem o passo 2: para onde vai o seu dinheiro. Salve para fazer junto.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#organizacaofinanceira #controlefinanceiro #financaspessoais #patrimonio #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Primeira segunda-feira do ano: abre a série Comece 2027 (apresentada no carrossel de 02/01) com o passo mais simples e o que dá base aos outros três, saber quanto se tem."),
        ("O que desperta interesse", "A pergunta que pouca gente responde de cabeça e uma soma que se monta já no primeiro segundo, conta a conta, até R$ 112.730,86."),
        ("Benefício para o público", "Aprende a fazer o retrato do patrimônio: cadastrar cada conta com o saldo de hoje, deixar no total e entender que o exterior entra pelo custo em reais."),
        ("Como contribui para o perfil", "Dá cara à série com o selo do passo e mostra em tela real a folha Nova conta, ainda inédita no perfil, com o tipo, o Saldo atual e o Incluir no patrimônio total."),
    ],
    "alt": [
        "Reel de 21 segundos. Num fundo claro, a pergunta Quanto você tem, somando tudo? e quatro contas que entram uma a uma, enquanto o total sobe: conta corrente, R$ 18.230,86; "
        "reserva, R$ 22.974,60; corretora no exterior, R$ 60.000,00; banco na Europa, R$ 11.525,40. O total, 4 contas somadas, para em R$ 112.730,86; uma nota diz que as contas lá fora entram pelo que custaram em reais. "
        "Num fundo escuro, o selo da série: Comece 2027, passo 1 de 4, O retrato. Depois, telas reais do timtimcash no celular, com dados de exemplo: o menu, Contas e carteiras com o Patrimônio consolidado de R$ 112.730,86 e as quatro contas; "
        "o toque em Nova conta, o nome Carteira digitado, o tipo Dinheiro / Carteira, o Saldo atual de R$ 150,00, quanto tem na conta hoje, e o interruptor Incluir no patrimônio total ligado. "
        "Passo 1: o retrato. Contas e carteiras no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/a-visao-geral.jpg · Visão geral no celular, Janeiro 2027, site build 2026-10-19.5, cópia da conta sem mudança, relógio em 04/01/2027 10:00 (o botão “Menu” no alto) · 5,6 a 6,6 s",
        "telas/b0-menu-aberto.jpg e b-menu.jpg · o menu recém-aberto e rolado até “Configurar · Contas e carteiras” · 6,6 a 7,4 s",
        "telas/c-contas-e-carteiras.jpg · “Contas e carteiras”: “4 contas · todas no total do patrimônio”, PATRIMÔNIO CONSOLIDADO R$ 112.730,86, Banco na Europa R$ 11.525,40, Conta corrente R$ 18.230,86, Corretora no exterior R$ 60.000,00, Reserva R$ 22.974,60, botão “Nova conta” · 7,4 a 10,9 s",
        "telas/d-nova-conta-0.jpg e d-nova-conta-nome-1.jpg a d-nova-conta-nome-8.jpg · a folha “Nova conta” e o nome “Carteira” letra a letra · 10,9 a 13,1 s",
        "telas/e-tipo.jpg e f-tipo-escolhido.jpg · a folha “Tipo de conta” e o tipo “Dinheiro / Carteira” escolhido · 13,1 a 14,7 s",
        "telas/g-saldo-1.jpg a g-saldo-5.jpg · “Saldo atual” digitado pelos centavos até R$ 150,00, com “Incluir no patrimônio total” ligado · 14,7 a 18,1 s",
        "telas/h-pronto.jpg · o formulário pronto (as caixas da medida final; mesma tela de g-saldo-5) · não aparece sozinho no vídeo",
        "telas/caixas.json · posições medidas na captura e o texto de cada tela, usados nos anéis, nos toques e nos assert do roteiro",
    ],
}
