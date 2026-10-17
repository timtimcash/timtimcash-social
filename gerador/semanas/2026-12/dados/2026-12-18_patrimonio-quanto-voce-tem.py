# -*- coding: utf-8 -*-
"""Sexta 18/12/2026 · carrossel "Patrimônio: quanto você tem de verdade" (educação com produto, capa papel).
Artes: saida/2026-12-18_patrimonio-quanto-voce-tem/01.jpg a 07.jpg, geradas por equipes/dc2/posts.py (contas por assert).
Telas reais novas em saida/2026-12-18_patrimonio-quanto-voce-tem/telas/, capturadas por equipes/dc2/captura.py na conta de N/base_app
(build 2026-10-16.1), sem mudar nada, relógio em 18/12/2026 10:00 (celular):
- Contas e carteiras (Menu): Patrimônio consolidado R$ 117.051,46; Banco na Europa R$ 11.525,40; Conta corrente R$ 22.551,46;
  Corretora no exterior R$ 60.000,00; Reserva R$ 22.974,60; todas "No total" ("4 contas · todas no total do patrimônio");
- Editar conta da Corretora no exterior (sem salvar): "Incluir no patrimônio total · o saldo soma ao total geral de contas", ligado;
- Remessas: dólar "US$13.310 na carteira hoje", "R$ 67.235,47 ao câmbio de hoje (R$ 5,0515)", +R$ 7.235,46 (+12,1% em R$);
  euro "€2.012 na carteira hoje", "R$ 11.386,31 ao câmbio de hoje (R$ 5,6592)", −R$ 139,09 (−1,2% em R$).
Como o site conta (código do build e telas): cada remessa é uma transferência para a conta de destino (Corretora no exterior,
Banco na Europa), então o exterior entra no patrimônio pelo custo em reais (R$ 60.000,00 + R$ 11.525,40 = R$ 71.525,40);
o valor de hoje fica em Remessas, cada moeda na sua (o site não soma moedas diferentes).
Contas do post: lá fora 61,1%, reserva 19,6%, conta corrente 19,3% de R$ 117.051,46; o que deve: as parcelas 2 a 10 do notebook
da Black Friday (10x de R$ 360,00 desde 27/11; "Notebook (2/10)" pendente em 27/12 na tela de Transações), 9 × R$ 360,00 =
R$ 3.240,00; patrimônio líquido R$ 113.811,46. A conta fictícia não tem cartão de crédito."""

POST = {
    "pasta": "2026-12-18_patrimonio-quanto-voce-tem",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Patrimônio é o que você tem menos o que deve (R$ 117.051,46 − R$ 3.240,00 no exemplo); ter não é o mesmo que poder usar amanhã (liquidez: 61% está lá fora); no timtimcash, o exterior entra no patrimônio pelo custo das remessas e o valor de hoje fica em Remessas, cada moeda na sua; Contas e carteiras e o “Incluir no patrimônio total”",
    "pilar": "Educação com produto",
    "data_longa": "sexta-feira, 18 de dezembro de 2026",
    "data_curta": "sexta-feira, 18/12/2026",
    "data_mockup": "18 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-18T10:00:00",
    "slides": [
        "Capa (fundo papel) · PATRIMÔNIO · Quanto você tem de verdade? · “TOTAL DAS CONTAS R$ 117.051” sobre uma pilha em perspectiva de três lajes com altura proporcional ao valor: conta corrente R$ 22.551 (branca, em cima), reserva R$ 22.975 (verde) e lá fora R$ 71.525 (tinta, a maior, embaixo), com rótulos ao lado.",
        "A CONTA · Patrimônio é o que você tem menos o que deve. · O que você tem (as 4 contas do exemplo) R$ 117.051,46; O que você deve (9 parcelas de R$ 360) −R$ 3.240,00; Patrimônio líquido R$ 113.811,46; barra verde com a dívida em coral na mesma régua. · Nota: Exemplo: a conta fictícia dos nossos posts em 18/12/2026; faltam 9 das 10 parcelas do notebook.",
        "LIQUIDEZ · Ter não é o mesmo que usar amanhã. · Liquidez é o quanto vira dinheiro rápido. No exemplo, 61% está lá fora. · Barra 19,3% (conta corrente, branca), 19,6% (reserva, verde), 61,1% (lá fora, tinta). Conta corrente R$ 22.551,46 · na hora; Reserva R$ 22.974,60 · depende da aplicação; Lá fora R$ 71.525,40 · depende de vender, do câmbio do dia e do prazo da volta.",
        "LÁ FORA · No patrimônio, lá fora entra pelo custo. · O valor de hoje fica em Remessas. · US$ 13.310 (câmbio salvo: R$ 5,0515): NO PATRIMÔNIO R$ 60.000,00, o custo das remessas → HOJE, EM REMESSAS R$ 67.235,47, +R$ 7.235,46 · +12,1%. € 2.012 (câmbio salvo: R$ 5,6592): NO PATRIMÔNIO R$ 11.525,40 → HOJE, EM REMESSAS R$ 11.386,31, −R$ 139,09 · −1,2%.",
        "NO TIMTIMCASH · Contas e carteiras: tudo somado. · Tela real no celular (relógio em 18/12/2026): PATRIMÔNIO CONSOLIDADO R$ 117.051,46; Banco na Europa R$ 11.525,40; Conta corrente R$ 22.551,46; Corretora no exterior R$ 60.000,00; Reserva R$ 22.974,60, todas “No total”. Seta “e em cada conta, você escolhe” e a linha “Incluir no patrimônio total · o saldo soma ao total geral de contas”, ligada (Editar conta da Corretora no exterior, sem salvar). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "EM REMESSAS · O valor de hoje, em cada moeda. · Telas reais no celular (relógio em 18/12/2026): Investido no exterior, Estados Unidos, “no patrimônio · conta de destino”, US$ 13.310 na carteira hoje, +US$ 1.310,00 +10,9% em US$, +R$ 7.235,46 +12,1% em R$, R$ 67.235,47 ao câmbio de hoje (R$ 5,0515); Investido no exterior, Portugal, € 2.012 na carteira hoje, +€ 12,00 +0,6% em €, −R$ 139,09 −1,2% em R$, R$ 11.386,31 ao câmbio de hoje (R$ 5,6592). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Saiba quanto você tem, de verdade. · Contas, carteiras e remessas no timtimcash, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Quanto você tem de verdade? Comece pela conta certa.\n\n"
        "Patrimônio é o que você tem menos o que deve. No nosso exemplo, as 4 contas somam R$ 117.051,46 em 18/12. "
        "Faltam 9 parcelas de R$ 360 do notebook (R$ 3.240): o patrimônio líquido é de R$ 113.811,46.\n\n"
        "E ter não é o mesmo que poder usar amanhã: 61% desse dinheiro está lá fora, e trazer de volta depende de vender, do câmbio do dia e do prazo.\n\n"
        "No timtimcash, cada remessa entra no patrimônio pelo custo em reais (R$ 71.525,40 no exemplo). O valor de hoje fica em Remessas, "
        "cada moeda na sua: US$ 13.310 valem R$ 67.235,47 ao câmbio salvo, e € 2.012, R$ 11.386,31.\n\n"
        "Em Contas e carteiras, você vê o patrimônio consolidado e escolhe, em cada conta, o que entra no total.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#patrimonio #financaspessoais #investimentonoexterior #controlefinanceiro #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de ano é hora de balanço, e a 2ª parcela do 13º cai no dia 18 no exemplo. Muita gente soma o que tem nessa época; o post ensina a somar direito: o que tem, menos o que deve, e o que vira dinheiro rápido."),
        ("O que desperta interesse", "A pergunta da capa (“de verdade?”) e a pilha que mostra a maior parte do exemplo lá fora. O slide 4 surpreende: o mesmo dinheiro vale uma coisa no patrimônio (o custo) e outra em Remessas (hoje), em cada moeda."),
        ("Benefício para o público", "Aprende a calcular o patrimônio líquido, a separar o que tem do que pode usar logo (liquidez) e a ler o exterior pelo custo e pelo valor de hoje, sem somar moedas diferentes."),
        ("Como contribui para o perfil", "Apresenta Contas e carteiras (o patrimônio consolidado e o “Incluir no patrimônio total”) e liga a função às Remessas, com telas reais novas e os números da conta de exemplo usados nos posts de exterior, sem ligar remessas a gratuidade."),
    ],
    "alt": [
        "Patrimônio. Quanto você tem de verdade? Total das contas: R$ 117.051. Uma pilha em perspectiva de três lajes, cada uma da altura do seu valor: conta corrente, R$ 22.551, branca, em cima; reserva, R$ 22.975, verde; e lá fora, R$ 71.525, escura e bem maior, embaixo.",
        "A conta: patrimônio é o que você tem menos o que deve. O que você tem, as 4 contas do exemplo: R$ 117.051,46. O que você deve, 9 parcelas de R$ 360: menos R$ 3.240,00. Patrimônio líquido: R$ 113.811,46. Uma barra verde com a dívida em coral na mesma régua. Exemplo da conta fictícia dos nossos posts em 18/12/2026.",
        "Liquidez: ter não é o mesmo que usar amanhã. Liquidez é o quanto vira dinheiro rápido; no exemplo, 61% está lá fora. Uma barra dividida em 19,3% na conta corrente, 19,6% na reserva e 61,1% lá fora. Conta corrente, R$ 22.551,46, na hora. Reserva, R$ 22.974,60, depende da aplicação. Lá fora, R$ 71.525,40, depende de vender, do câmbio do dia e do prazo da volta.",
        "Lá fora: no patrimônio, o exterior entra pelo custo. O valor de hoje fica em Remessas. US$ 13.310, com câmbio salvo de R$ 5,0515: no patrimônio, R$ 60.000,00, o custo das remessas; hoje, em Remessas, R$ 67.235,47, mais R$ 7.235,46, ou 12,1%. € 2.012, com câmbio salvo de R$ 5,6592: no patrimônio, R$ 11.525,40; hoje, R$ 11.386,31, menos R$ 139,09, ou 1,2%.",
        "No timtimcash, Contas e carteiras: tudo somado. Tela real no celular, com dados de exemplo: patrimônio consolidado de R$ 117.051,46; Banco na Europa, R$ 11.525,40; Conta corrente, R$ 22.551,46; Corretora no exterior, R$ 60.000,00; Reserva, R$ 22.974,60; todas no total. Abaixo, a linha da própria conta: Incluir no patrimônio total, o saldo soma ao total geral de contas, com o interruptor ligado.",
        "Em Remessas, o valor de hoje em cada moeda. Telas reais no celular, com dados de exemplo. Estados Unidos: US$ 13.310 na carteira hoje, mais US$ 1.310,00, ou 10,9% em dólar, e mais R$ 7.235,46, ou 12,1% em reais; R$ 67.235,47 ao câmbio de hoje, de R$ 5,0515. Portugal: € 2.012 na carteira hoje, mais € 12,00, ou 0,6% em euro, e menos R$ 139,09, ou 1,2% em reais; R$ 11.386,31 ao câmbio de hoje, de R$ 5,6592.",
        "Saiba quanto você tem, de verdade. Contas, carteiras e remessas no timtimcash, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-contas-e-carteiras.png · Menu › “Contas e carteiras” no celular, relógio em 18/12/2026 10:00 (390 × 1400 em escala 3): “4 contas · todas no total do patrimônio”, Patrimônio consolidado R$ 117.051,46 e as 4 contas · slide 5 (do patrimônio consolidado à última conta)",
        "telas/celular-editar-conta-corretora.png · a linha “Corretora no exterior” aberta em “Editar conta”, sem salvar; recortada a linha “Incluir no patrimônio total”, ligada; relógio em 18/12/2026 10:00 · slide 5",
        "telas/celular-remessas-dolar.png · Remessas ao exterior, moeda USD, relógio em 18/12/2026 10:00 (390 × 1400 em escala 3): “US$13.310 na carteira hoje”, “R$ 67.235,47 ao câmbio de hoje (R$ 5,0515)” · slide 6",
        "telas/celular-remessas-euro.png · a mesma tela depois do toque em “EUR”: “€2.012 na carteira hoje”, “R$ 11.386,31 ao câmbio de hoje (R$ 5,6592)”; relógio em 18/12/2026 10:00 · slide 6",
    ],
}
