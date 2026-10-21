# -*- coding: utf-8 -*-
"""Quinta 21/01/2027 · Reel "Há quanto tempo o seu dinheiro está lá fora?" (investimento no exterior; capa verde). Equipe js.
Vídeo, capa e prévia gerados por equipes/js/reel_21.py (com assert nos números lidos da tela); telas capturadas por
equipes/js/captura_21.py no site build 2026-10-19.5, na conta de base (J/base_app, sem mudança), no celular (390 px em escala 3, janela de
1000 px de altura), relógio da página em 21/01/2027 10:00.
Interação real: Remessas (abre no dólar) -> a tabela "Remessas" ("Por remessa"), em que cada cartão termina com a data, o câmbio efetivo e o
tempo investido (no computador, a coluna "Investido há"): 18/04/2024 · R$ 5,1000 · 33,1 meses; 14/03/2024 · R$ 5,0000 · 34,3 meses;
12/07/2023 · R$ 4,9000 · 42,3 meses (US$ 4.000,00 cada) -> um toque em "EUR" (o vídeo mostra só a faixa dos botões de moeda) -> a tabela do
euro: 01/12/2026 · R$ 5,7627 · 1,7 meses (€ 2.000,00). O tempo confere com a data: dias até 21/01/2027 ÷ 30,44 (1.289, 1.043, 1.008 e
51 dias). 42,3 meses = 3 anos e 6 meses (o contador do gancho).
Fora do vídeo de propósito: o topo de Remessas, "Rendimento ano a ano" e "Ritmo do retorno", que trazem valores em reais de 2026 ao câmbio
salvo de exemplo; o fechamento de 2026 não existe (a PTAX de 31/12/2026 ainda não saiu) e nada dele aparece. A TIR do "Ritmo do retorno"
só é citada, sem número (não repete 22/10). Post de exterior: sem a frase do controle financeiro.
Nos cartões, "Hoje" em reais usa o câmbio salvo na conta de exemplo (dólar R$ 5,0515 e euro R$ 5,6592, as PTAX de compra reais de
15/10/2026): o vídeo não destaca esses valores e a legenda diz que o câmbio é de exemplo. Os câmbios da linha do tempo desenhada
(R$ 4,90, R$ 5,00, R$ 5,10 e R$ 5,76) são os câmbios efetivos de cada remessa, arredondados a duas casas (o site mostra quatro)."""

POST = {
    "pasta": "2027-01-21_reel-ha-quanto-tempo-esta-la-fora",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "Há quanto tempo o seu dinheiro está lá fora: em Remessas, cada envio mostra o tempo investido; cada data trouxe um câmbio, e o Ritmo do retorno calcula a TIR com a data real de cada envio",
    "pilar": "Investimento no exterior · produto (Remessas ao exterior)",
    "data_longa": "quinta-feira, 21 de janeiro de 2027",
    "data_curta": "quinta-feira, 21/01/2027",
    "data_mockup": "21 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-21T10:00:00",
    "video": "saida/2027-01-21_reel-ha-quanto-tempo-esta-la-fora/reel.mp4",
    "capa": "saida/2027-01-21_reel-ha-quanto-tempo-esta-la-fora/capa.jpg",
    "previa": "saida/2027-01-21_reel-ha-quanto-tempo-esta-la-fora/previa.mp4",
    "slides": [
        "Capa da grade (verde) · REMESSAS AO EXTERIOR · Há quanto tempo está lá fora? · Quatro barras brancas alinhadas em “hoje”, do tamanho do tempo de cada envio: 42,3, 34,3 e 33,1 meses (dólar) e 1,7 meses (euro, em tinta).",
        "0 a 2,6 s · Gancho (papel) · REMESSAS AO EXTERIOR · Há quanto tempo o seu dinheiro está lá fora? · Desde o primeiro quadro, um contador de anos e meses corre até “3 anos e 6 meses”, com uma trilha de 12/07/2023 (a primeira remessa) até hoje.",
        "2,9 a 5,1 s · Em Remessas, cada envio mostra há quanto tempo está lá fora. · Tela real da tabela de remessas do dólar, com anel nos três tempos: 33,1, 34,3 e 42,3 meses.",
        "5,3 a 7,6 s · A primeira, de julho de 2023: 42,3 meses. · Zoom no cartão de 12/07/2023 (US$ 4.000,00, câmbio R$ 4,9000), com anel na linha da data, do câmbio e do tempo.",
        "7,8 a 10,0 s · As duas de 2024: 34,3 e 33,1 meses. · Anéis nos cartões de 14/03/2024 (R$ 5,0000) e 18/04/2024 (R$ 5,1000).",
        "10,2 a 13,3 s · No euro, um toque em EUR: a remessa de dezembro tem 1,7 meses. · A faixa dos botões USD e EUR, com anel e toque em EUR; depois, a tabela do euro: 01/12/2026, câmbio R$ 5,7627, 1,7 meses, em anel.",
        "13,5 a 17,0 s · Cada envio tem a sua data, o seu câmbio e o seu tempo. · Linha do tempo desenhada de jul/2023 a hoje: uma barra por envio até hoje (US$ 4.000 a R$ 4,90, 42,3 meses; a R$ 5,00, 34,3 meses; a R$ 5,10, 33,1 meses; € 2.000 a R$ 5,76, 1,7 meses). · No Ritmo do retorno, a TIR é calculada com a data real de cada envio.",
        "17,1 a 19,8 s · Fechamento (verde) · Remessas ao exterior no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Há quanto tempo o seu dinheiro está lá fora?\n\n"
        "Em Remessas, cada envio mostra há quanto tempo está investido. No exemplo do vídeo, a primeira remessa, de 12/07/2023, está lá "
        "fora há 42,3 meses: 3 anos e 6 meses. As duas de 2024 têm 34,3 e 33,1 meses, e a de euro, de 01/12/2026, 1,7 meses.\n\n"
        "Cada data trouxe um câmbio efetivo: R$ 4,90, R$ 5,00 e R$ 5,10 por dólar, e R$ 5,7627 por euro. Por isso cada remessa tem o "
        "seu resultado, e o Ritmo do retorno calcula a TIR com a data real de cada envio. No computador, o tempo aparece na coluna "
        "“Investido há”.\n\n"
        "Tela real do timtimcash, com dados de exemplo. Os valores de hoje em reais usam o câmbio salvo de exemplo, a PTAX de compra de "
        "15/10/2026 (dólar R$ 5,0515; euro R$ 5,6592).\n\n"
        "Fonte: Banco Central do Brasil, PTAX de 15/10/2026.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #remessas #dolar #cambio #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Janeiro é quando quem investe lá fora olha o ano que passou e planeja os envios de 2027. É o segundo post de exterior do mês (depois de 11/01, quanto foi por ano), com um ângulo novo: o tempo de cada envio."),
        ("O que desperta interesse", "A pergunta “Há quanto tempo o seu dinheiro está lá fora?” com um contador que corre até “3 anos e 6 meses” já no primeiro segundo."),
        ("Benefício para o público", "A pessoa vê que cada remessa tem a sua data, o seu câmbio e o seu tempo investido, e entende por que o resultado de cada uma é diferente e por que a TIR usa as datas reais."),
        ("Como contribui para o perfil", "Mostra com tela real a coluna do tempo investido, ainda inédita no perfil, e o botão de cada moeda, sem repetir os números de rendimento de 22/10 e sem nada do fechamento de 2026."),
    ],
    "alt": [
        "Reel de 20 segundos. Há quanto tempo o seu dinheiro está lá fora? Um contador de anos e meses corre até 3 anos e 6 meses, "
        "numa trilha de 12/07/2023, a primeira remessa, até hoje. Telas reais do timtimcash no celular, com dados de exemplo. Em Remessas, "
        "a tabela de envios em dólar mostra o tempo de cada um: 42,3 meses para a remessa de 12/07/2023, a câmbio de R$ 4,90, e 34,3 e 33,1 "
        "meses para as de março e abril de 2024, a R$ 5,00 e R$ 5,10. Um toque em EUR mostra a remessa em euro de 01/12/2026, a R$ 5,7627, "
        "com 1,7 meses. Uma linha do tempo desenhada põe as quatro remessas lado a lado, cada uma com a sua data, o seu câmbio e o seu tempo, "
        "e lembra que o Ritmo do retorno calcula a TIR com a data real de cada envio. Remessas ao exterior no timtimcash. Link na bio."
    ],
    "fontes": [
        ("Banco Central do Brasil · PTAX, cotações de fechamento de 15/10/2026 (dólar: compra R$ 5,0515; euro: compra R$ 5,6592), o câmbio salvo de exemplo na conta",
         "https://ptax.bcb.gov.br/ptax_internet/consultarTodasAsMoedas.do?method=consultaTodasMoedas"),
    ],
    "telas": [
        "telas/celular-remessas-1-tabela-dolar.jpg · Remessas no dólar, rolada até a tabela “Remessas” (“Por remessa”): três cartões de US$ 4.000,00, com 33,1, 34,3 e 42,3 meses, e o total (celular 390 × 1000 em escala 3, build 2026-10-19.5, relógio da página em 21/01/2027 10:00) · 2,7 a 10,4 s",
        "telas/celular-remessas-2-topo-dolar.jpg · o topo de Remessas no dólar; no vídeo aparece só a faixa dos botões USD e EUR (mesmo relógio) · 10,2 a 11,0 s",
        "telas/celular-remessas-3-topo-euro.jpg · a mesma faixa depois do toque em EUR (o vídeo mostra só os botões) · 11,0 a 11,8 s",
        "telas/celular-remessas-4-tabela-euro.jpg · a tabela do euro: 01/12/2026, Reserva para Banco na Europa, € 2.000,00, câmbio R$ 5,7627, 1,7 meses · 11,6 a 13,7 s",
        "telas/caixas.json · posições medidas na captura (com a rolagem de cada foto), os textos de cada cartão e o estado dos botões de moeda, usados nos anéis e nos assert do roteiro",
    ],
}
