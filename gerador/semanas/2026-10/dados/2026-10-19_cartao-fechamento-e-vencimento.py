# -*- coding: utf-8 -*-
"""Segunda 19/10/2026 · carrossel "Cartão de crédito: fechamento, vencimento e o melhor dia de compra" (educação, capa papel).
Artes: saida/2026-10-19_cartao-fechamento-e-vencimento/01.jpg a 06.jpg, geradas por carrosseis-a/posts.py.
Ilustrações de calendário e linha do tempo nos slides de educação; tela real só no slide 5.
Tela real nova em saida/2026-10-19_cartao-fechamento-e-vencimento/telas/, capturada por carrosseis-a/app/captura_a.py.
Para a captura, a cópia do kit (carrosseis-a/app/estado.py) ganhou um cartão "Cartão principal" (fecha no dia 3, vence no
dia 10, pago pela Conta corrente, limite R$ 8.000, sem nenhuma compra); nenhum número existente mudou. Formulário
preenchido e fotografado sem salvar.
Regra do site (calcFaturaDaCompra): compra DEPOIS do dia de fechamento vai para a fatura seguinte; vencimento no mesmo mês
do fechamento quando o dia de vencimento é maior que o de fechamento. Conferido na página: compra em 02/10/2026,
"Será incluído na fatura que vence 10/out"; compra em 04/10/2026, "Será incluído na fatura que vence 10/nov".
Prazos do exemplo: 2/10 a 10/10 = 8 dias; 4/10 a 10/11 = 37 dias (outubro tem 31 dias)."""

POST = {
    "pasta": "2026-10-19_cartao-fechamento-e-vencimento",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "Cartão de crédito: as datas de fechamento e de vencimento, por que a compra do dia 2 e a do dia 4 caem em faturas diferentes, o melhor dia de compra (com a ressalva de que a regra do dia do fechamento varia entre emissores) e o cartão no timtimcash, com “Fecha no dia”, “Vence no dia” e o aviso da fatura na compra",
    "pilar": "Educação prática",
    "data_longa": "segunda-feira, 19 de outubro de 2026",
    "data_curta": "segunda-feira, 19/10/2026",
    "data_mockup": "19 de outubro",
    "hora": "10h00",
    "iso": "2026-10-19T10:00:00",
    "slides": [
        "Capa (fundo papel) · CARTÃO DE CRÉDITO · Qual é o melhor dia de compra? · Calendário ilustrado de um mês (dias 1 a 31): dia 3 em preto (fecha), dia 4 em verde (melhor dia) e dia 10 com anel coral (vence), com legenda.",
        "AS DUAS DATAS · Duas datas mandam na sua fatura. · Fechamento, dia 3: o dia em que a fatura fecha; o que você compra depois dele vai para a próxima. · Vencimento, dia 10: o dia de pagar a fatura que fechou. · Nota: Exemplo: um cartão que fecha no dia 3 e vence no dia 10.",
        "DIA 2 OU DIA 4? · Dois dias na compra, um mês no pagamento. · A compra do dia 2 entra na fatura que fecha no dia 3. A do dia 4 já fica para a próxima. · Linha do tempo de outubro a novembro, com os fechamentos em 3/10 e 3/11: compra no dia 2, vence 10/10, 8 dias para pagar; compra no dia 4, vence 10/11, 37 dias para pagar. · Nota: Exemplo: cartão que fecha no dia 3 e vence no dia 10.",
        "O MELHOR DIA DE COMPRA · É o dia seguinte ao fechamento. · Faixa com os dias de 1 a 8: dia 3, fecha; dia 4, melhor dia. · A compra vai para a fatura seguinte: é a que demora mais para ser cobrada. E prazo maior não é desconto: o valor é o mesmo. · Aviso: E no próprio dia do fechamento? A regra varia entre os emissores. Confira as datas do seu cartão na fatura.",
        "NO TIMTIMCASH · A compra já mostra em qual fatura vai entrar. · Cada cartão tem “Fecha no dia” e “Vence no dia”. No exemplo, a compra do dia 4 vai para a fatura que vence 10/nov. · Tela real de “Nova transação” no celular: Data 04/10/2026, Categoria Mercado, Pago via Cartão principal (cartão de crédito), Mercado da Vila, “Será incluído na fatura que vence 10/nov”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Saiba em qual fatura cada compra vai cair. · Cartões de crédito no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Comprar no dia 2 ou no dia 4 pode mudar em um mês a data de pagar. Quem decide é o fechamento da fatura.\n\n"
        "Num cartão que fecha no dia 3 e vence no dia 10, a compra do dia 2 entra na fatura que vence no dia 10 do mesmo mês: 8 dias para pagar. "
        "A do dia 4 fica para a fatura seguinte e só vence no dia 10 do mês que vem: 37 dias, no exemplo de outubro.\n\n"
        "Por isso o melhor dia de compra é o dia seguinte ao fechamento. Mas prazo maior não é desconto, e a regra do próprio dia do fechamento varia entre os emissores: confira as datas do seu cartão na fatura.\n\n"
        "No timtimcash, cada cartão tem “Fecha no dia” e “Vence no dia”, e a compra no cartão já avisa em qual fatura vai entrar.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#cartaodecredito #educacaofinanceira #financaspessoais #controlefinanceiro #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Segunda quinzena de outubro, antes das compras de fim de ano: é quando entender o ciclo da fatura mais ajuda a planejar. O tema estava guardado no histórico do perfil (dia de fechamento, dia de vencimento e a compra que cai na fatura seguinte) e não repete nenhum post de outubro."),
        ("O que desperta interesse", "A capa é um calendário que todo mundo reconhece, com três dias marcados, e a pergunta tem resposta prática. O slide 3 mostra o contraste que surpreende: dois dias de diferença na compra viram 8 ou 37 dias para pagar."),
        ("Benefício para o público", "Entende as duas datas da fatura, descobre o próprio melhor dia de compra e sabe onde conferir as datas do seu cartão. Sem juros do rotativo, sem números de mercado e sem promessa: prazo maior não é desconto."),
        ("Como contribui para o perfil", "Educação com ilustração que termina numa função concreta, com tela real: o cartão com fechamento e vencimento e o aviso da fatura na compra. Prepara o carrossel de 26/10, sobre parcelas, que usa o mesmo cartão de exemplo."),
    ],
    "alt": [
        "Cartão de crédito. Qual é o melhor dia de compra? Calendário de um mês com o dia 3 marcado em preto, fecha; o dia 4 em verde, melhor dia; e o dia 10 com um anel coral, vence.",
        "As duas datas. Duas datas mandam na sua fatura. Fechamento, dia 3: o dia em que a fatura fecha; o que você compra depois dele vai para a próxima. Vencimento, dia 10: o dia de pagar a fatura que fechou. Exemplo de um cartão que fecha no dia 3 e vence no dia 10.",
        "Dia 2 ou dia 4? Dois dias na compra, um mês no pagamento. A compra do dia 2 entra na fatura que fecha no dia 3; a do dia 4 já fica para a próxima. Linha do tempo de outubro a novembro, com os fechamentos em 3 de outubro e 3 de novembro: a compra do dia 2 vence em 10 de outubro, 8 dias para pagar; a compra do dia 4 vence em 10 de novembro, 37 dias para pagar.",
        "O melhor dia de compra é o dia seguinte ao fechamento. Faixa com os dias de 1 a 8: o dia 3 fecha e o dia 4 é o melhor dia. A compra vai para a fatura seguinte: é a que demora mais para ser cobrada. E prazo maior não é desconto: o valor é o mesmo. Aviso: e no próprio dia do fechamento? A regra varia entre os emissores; confira as datas do seu cartão na fatura.",
        "No timtimcash, a compra já mostra em qual fatura vai entrar. Cada cartão tem Fecha no dia e Vence no dia. Tela real de Nova transação no celular, com dados de exemplo: data 4 de outubro de 2026, categoria Mercado, pago via Cartão principal, cartão de crédito, descrição Mercado da Vila e o aviso: será incluído na fatura que vence 10 de novembro.",
        "Saiba em qual fatura cada compra vai cair. Cartões de crédito no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-compra-no-cartao-dia-04.jpg · “Nova transação” no celular: despesa de R$ 412,35 (Mercado, Mercado da Vila) no “Cartão principal”, data 04/10/2026, com o aviso “Será incluído na fatura que vence 10/nov”; sem salvar; o cartão (fecha no dia 3, vence no dia 10, sem compras) existe só na cópia do estado.py de carrosseis-a (celular, 390 × 844 em escala 3) · slide 5",
    ],
}
