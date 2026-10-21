# -*- coding: utf-8 -*-
"""Sábado 13/02/2027 · carrossel "Guardar não é gastar" (organização, capa papel). Equipe fa.
Artes: saida/2027-02-13_transferencia-nao-e-gasto/01.jpg a 06.jpg, geradas por equipes/fa/posts.py (post_guardar).
Telas reais em saida/2027-02-13_transferencia-nao-e-gasto/telas/, capturadas por equipes/fa/captura.py na cópia da
conta (igual à base, sem mudança), build 2026-10-19.5, relógio em 13/02/2027 10:00. A "Nova transação" foi preenchida
e fechada sem salvar.

Números das telas (asserts em posts.py): Visão geral de fevereiro (Realizado, parcial): "Guardou 33,6% da receita",
Receitas R$ 9.960,00, Despesas R$ 6.610,10, Resultado do período R$ 3.349,90. Visão geral do Ano 2026: "Guardou 19,4%
da receita", Receitas R$ 126.293,36, Despesas R$ 101.854,70, Resultado R$ 24.438,66. Transações, Ano 2026, filtro de
transferências e busca "reserva": "12 transações · somam R$ 18.000,00" (Aplicação na reserva, R$ 1.500 por mês, Conta
corrente → Reserva). "Nova transação" do slide 5 (não salva): Transferência de R$ 1.000,00 (valor redondo de
exemplo), hoje (13/02), "Já foi feita", De Reserva, Para Conta corrente.
Contas (minhas, com a mesma regra do site, resultado ÷ receitas): se a reserva de fevereiro (R$ 1.500) fosse despesa,
Despesas R$ 8.110,10, Resultado R$ 1.849,90 e 18,6% da receita; se as 12 de 2026 (R$ 18.000) fossem despesa, Resultado
R$ 6.438,66 e 5,1%; se a volta de R$ 1.000 da Reserva entrasse como receita, Receitas R$ 10.960,00, Resultado
R$ 4.349,90 e 39,7% (em vez de 33,6%): o mês pareceria ter guardado mais do que guardou.
Diferença do Reel de 05/02 (o envelope do Carnaval) e de 10/02 (quanto custou o Carnaval): o post não usa o exemplo do
Carnaval (revisão de 20/10/2026); o foco é a reserva de todo mês, na ida e na volta, e o efeito de lançá-la errado no
resultado e na receita guardada."""

POST = {
    "pasta": "2027-02-13_transferencia-nao-e-gasto",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "Guardar não é gastar: a reserva de R$ 1.500 por mês é transferência, não despesa; o efeito de lançá-la como despesa no resultado e na receita guardada (fevereiro e 2026), a Transferência na Nova transação e a carteira do Carnaval como segundo exemplo",
    "pilar": "Educação · organização, com produto",
    "data_longa": "sábado, 13 de fevereiro de 2027",
    "data_curta": "sábado, 13/02/2027",
    "data_mockup": "13 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-13T10:00:00",
    "slides": [
        "Capa (fundo papel) · ORGANIZAÇÃO · Guardar não é gastar. · Dois quadrados verde suave com ícones de traço: Conta corrente (banco) e Reserva (cofre), ligados por uma seta verde com “R$ 1.500” em cima e “TRANSFERÊNCIA” embaixo; abaixo, um selo com X e a palavra “despesa” riscada.",
        "O ERRO COMUM · Como despesa, a reserva encolhe o mês. · Selo verde “Como transferência, como está na tela” sobre a tela real da Visão geral (celular, 13/02/2027): Movimento de fevereiro 2027 (parcial), Guardou 33,6% da receita, Receitas R$ 9.960,00, Despesas R$ 6.610,10, Resultado do período R$ 3.349,90. Selo coral “Se os R$ 1.500 fossem despesa”: 18,6% guardado da receita; Despesas R$ 8.110,10; Resultado R$ 1.849,90. · Nota: Fevereiro até o dia 13, na conta de exemplo. Tela real do timtimcash, com dados de exemplo.",
        "NO TIMTIMCASH · Guardar é Transferência. · De uma conta para a outra, sem categoria. O patrimônio fica igual. · Tela real da “Nova transação” no celular, relógio em 13/02/2027: Transferência, R$ 1.500,00; Data 05/03/2027; “Marcar como feita · Fica como pendente até você confirmar”; De Conta corrente; Para Reserva. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "TODO MÊS, R$ 1.500 · Em 2026, R$ 18.000 guardados. · Doze transferências para a Reserva. Nenhum real como despesa. · Tela real de Transações no celular, relógio em 13/02/2027, Ano 2026, busca “reserva”: “12 transações · 12 pagas · 0 pendentes · somam R$ 18.000,00”. · Nota: Tela real do timtimcash, com dados de exemplo. · Cartão: Guardado da receita em 2026, na Visão geral, com a reserva como transferência: 19,4%; como despesa, seria 5,1%.",
        "NA VOLTA TAMBÉM · Tirou da reserva? Não é receita. · A volta para a Conta corrente também é Transferência. · Selo coral: Se fosse receita. Cartão: 39,7% guardado da receita, em vez de 33,6%; Receitas R$ 10.960,00; Resultado R$ 4.349,90. · Nota: Fevereiro até o dia 13, na conta de exemplo: o mês pareceria ter guardado mais do que guardou. · Tela real da “Nova transação” no celular, relógio em 13/02/2027: Transferência, R$ 1.000,00; Data Hoje 13/02; Já foi feita; De Reserva; Para Conta corrente. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Guardou? É transferência. · Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Guardar não é gastar. O dinheiro que vai para a reserva é transferência, não despesa.\n\n"
        "O erro comum é lançar os R$ 1.500 da reserva como despesa. Na conta de exemplo, fevereiro até o dia 13 tem R$ 3.349,90 de resultado e 33,6% da receita guardada. Com a reserva como despesa, seriam R$ 1.849,90 e 18,6%.\n\n"
        "No timtimcash, escolha Transferência na Nova transação, com De e Para e sem categoria. O dinheiro só muda de conta: o patrimônio fica igual e o resultado mostra só receitas e despesas.\n\n"
        "Em 2026, foram 12 transferências para a reserva, R$ 18.000, e o ano mostrou 19,4% da receita guardada. Como despesa, seriam 5,1%. Na volta vale o mesmo: tirar da reserva também é transferência; como receita, o mês pareceria ter guardado mais do que guardou.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#reservadeemergencia #organizacaofinanceira #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Meio de fevereiro: a reserva do mês já saiu (05/02). É quando quem começou a anotar em janeiro mais confunde guardar com gastar, e tirar da reserva com ganhar."),
        ("O que desperta interesse", "Um erro que parece inofensivo muda o retrato do mês nos dois sentidos: 33,6% da receita guardada viram 18,6% com a reserva como despesa, ou 39,7% com uma retirada contada como receita. No ano de 2026, 19,4% cairiam para 5,1%."),
        ("Benefício para o público", "Aprende a lançar como transferência o dinheiro que vai para a reserva e o que volta dela, e entende por que o resultado e o patrimônio ficam certos assim."),
        ("Como contribui para o perfil", "Explica um conceito de organização com telas reais e números da conta de exemplo, sem repetir o exemplo do Carnaval dos posts de 05/02 e 10/02."),
    ],
    "alt": [
        "Organização. Guardar não é gastar. Dois ícones em quadrados verdes, a conta corrente e a reserva, ligados por uma seta com R$ 1.500 e a palavra transferência; embaixo, a palavra despesa riscada.",
        "O erro comum: como despesa, a reserva encolhe o mês. Tela real da Visão geral no celular, com dados de exemplo, como transferência: fevereiro até o dia 13 com 33,6% da receita guardada, receitas de R$ 9.960, despesas de R$ 6.610,10 e resultado de R$ 3.349,90. Se os R$ 1.500 fossem despesa: 18,6% guardado, despesas de R$ 8.110,10 e resultado de R$ 1.849,90.",
        "No timtimcash, guardar é transferência: de uma conta para a outra, sem categoria, e o patrimônio fica igual. Tela real da Nova transação no celular, com dados de exemplo: transferência de R$ 1.500 em 5 de março de 2027, ainda não feita, da conta corrente para a reserva.",
        "Todo mês, R$ 1.500: em 2026, R$ 18.000 guardados, em doze transferências para a reserva, nenhum real como despesa. Tela real de Transações no celular, com dados de exemplo, no ano de 2026, com a busca reserva: 12 transações que somam R$ 18.000. O ano mostrou 19,4% da receita guardada; como despesa, seriam 5,1%.",
        "Na volta também: tirou da reserva? Não é receita. A volta para a conta corrente também é transferência. Se fosse receita, fevereiro até o dia 13 apareceria com 39,7% da receita guardada em vez de 33,6%, com receitas de R$ 10.960 e resultado de R$ 4.349,90: o mês pareceria ter guardado mais do que guardou. Tela real da Nova transação no celular, com dados de exemplo: transferência de R$ 1.000, hoje, 13 de fevereiro, já feita, da reserva para a conta corrente.",
        "Guardou? É transferência. Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-visao-geral-fevereiro-13-02.png · Visão geral no celular (390 × 1100 em escala 3), relógio em 13/02/2027 10:00, build 2026-10-19.5, cópia da conta igual à base: Fevereiro 2027, Realizado; “Movimento de fevereiro 2027 · Parcial · Guardou 33,6% da receita”; Receitas R$ 9.960,00; Despesas R$ 6.610,10; Resultado do período R$ 3.349,90 · slide 2 (recorte do cartão do movimento)",
        "telas/celular-nova-transferencia-13-02.png · “Nova transação” no celular (390 × 1000 em escala 3), mesmo relógio, preenchida e fechada sem salvar: Transferência, R$ 1.500,00, Data 05/03/2027 (seta do calendário para março), interruptor “Já foi feita” desligado (“Marcar como feita”), De Conta corrente, Para Reserva, descrição “Aplicação na reserva” · slide 3 (recorte do título ao campo Para)",
        "telas/celular-transferencias-reserva-2026-13-02.png · Transações, período “Ano atual” e a seta para Ano 2026, filtro de transferências (“Transf.”) e busca “reserva”: “12 transações · 12 pagas · 0 pendentes · somam R$ 18.000,00” · slide 4 (recorte do resumo à busca)",
        "telas/celular-visao-geral-2026-13-02.png · Visão geral, Ano 2026: “Guardou 19,4% da receita”, Receitas R$ 126.293,36, Despesas R$ 101.854,70, Resultado R$ 24.438,66 · número do slide 4 (a tela não aparece no carrossel)",
        "telas/celular-nova-transferencia-volta-13-02.png · “Nova transação” no celular (390 × 1000 em escala 3), mesmo relógio, preenchida e fechada sem salvar: Transferência, R$ 1.000,00 (valor redondo de exemplo), Data “Hoje 13/02”, “Já foi feita” (como vem), De Reserva, Para Conta corrente, descrição “Retirada da reserva” · slide 5 (recorte do título ao campo Para)",
        "telas/celular-transferencias-fevereiro-13-02.png · Transações de fevereiro, filtro de transferências: “2 transações · somam R$ 2.000,00”; 05/02 Aplicação na reserva R$ 1.500,00; 04/02 Dinheiro para a folia R$ 500,00 · referência (não usada no carrossel desde a revisão de 20/10)",
    ],
}
