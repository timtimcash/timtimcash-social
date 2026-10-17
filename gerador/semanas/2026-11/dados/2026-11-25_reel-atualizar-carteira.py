# -*- coding: utf-8 -*-
"""Quarta 25/11/2026 · Reel "Atualize a carteira em 30 segundos" (investimento no exterior e produto; capa papel). Equipe r3.
Vídeo, capa e prévia gerados por equipes/r3/reel_25.py (com assert nos números lidos da tela); telas capturadas por
equipes/r3/capturas/captura_25.py no site build 2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular
(390 × 760 em escala 3), com o relógio da página em 15/10/2026 15:00 e a resposta simulada da PTAX real de 15/10/2026
(PTAX_15_10: compra R$ 5,0515). O post sai em 25/11, mas a captura é de 15/10 porque só essa PTAX é real; a legenda diz isso.
Números da tela: antes, "US$ 13.200 na carteira hoje", "R$ 72.600,00 ao câmbio de hoje (R$ 5,50)" e "Atualizar · há 15 dias";
no modal, "PTAX de compra do Banco Central, de 15/10/2026 às 13:00." (a hora é a do carimbo da resposta simulada, 13:00, o
fechamento informado pelo Banco Central); depois do valor US$ 13.240 e da cotação, "Equivale hoje a R$ 66.881,86";
depois de salvar, "US$ 13.240 na carteira hoje", +US$ 1.240,00 (+10,3% em US$), +R$ 6.881,86 (+11,5% em R$) e
"R$ 66.881,86 ao câmbio de hoje (R$ 5,0515)". Conta: 13.240 × 5,0515 = 66.881,86.
Enquanto a pessoa digita (máscara em centavos: 0,01 ... 13.240,00), o site mostra embaixo um aviso de valor muito menor
que o salvo; a janela fica recortada no campo, como a pessoa vê com o teclado aberto, e esse aviso passageiro não aparece."""

POST = {
    "pasta": "2026-11-25_reel-atualizar-carteira",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Atualize a carteira em 30 segundos: em Remessas, o passo a passo real de Atualizar carteira, com a PTAX de compra do Banco Central sugerida pelo site, e a carteira em dólar e em reais",
    "pilar": "Investimento no exterior · produto (Remessas ao exterior)",
    "data_longa": "quarta-feira, 25 de novembro de 2026",
    "data_curta": "quarta-feira, 25/11/2026",
    "data_mockup": "25 de novembro",
    "hora": "10h00",
    "iso": "2026-11-25T10:00:00",
    "video": "saida/2026-11-25_reel-atualizar-carteira/reel.mp4",
    "capa": "saida/2026-11-25_reel-atualizar-carteira/capa.jpg",
    "previa": "saida/2026-11-25_reel-atualizar-carteira/previa.mp4",
    "slides": [
        "Capa da grade (papel) · REMESSAS AO EXTERIOR · Atualize a carteira em 30 segundos · Cronômetro grande de traço, com o arco verde cheio, “0:30” e “US$ → R$” no mostrador.",
        "0 a 2,5 s · Gancho (papel) · REMESSAS AO EXTERIOR · Quanto vale hoje o que você tem lá fora? · Desde o primeiro quadro, o cronômetro corre de 0:30 para baixo, com um pulso a cada segundo; depois ele voa para o canto de cima e segue correndo.",
        "2,5 a 5,1 s · Em Remessas, toque em Atualizar. · Tela real de Remessas: US$ 13.200 na carteira hoje, R$ 72.600,00 ao câmbio de hoje (R$ 5,50); anel âmbar em “Atualizar · há 15 dias” e toque.",
        "5,1 a 8,1 s · Digite quanto você tem lá fora: US$ 13.240. · Tela real de “Atualizar carteira”, recortada no campo: o valor entra tecla a tecla, de 0,01 a 13.240,00, com anel na linha da corretora.",
        "8,1 a 10,9 s · O site sugere a PTAX de compra do Banco Central. · Anel em “usar a cotação de hoje · R$ 5,0515” e na linha “PTAX de compra do Banco Central, de 15/10/2026 às 13:00.”; toque no botão.",
        "10,9 a 13,4 s · Com a PTAX, a carteira vale R$ 66.881,86. · Anel em “Equivale hoje a R$ 66.881,86” (câmbio 5,0515, “PTAX de hoje ✓”); toque em Salvar; o cronômetro para em 0:17 e ganha um sinal de feito.",
        "13,4 a 15,8 s · Pronto: carteira atualizada, em dólar e em reais. · Aviso “Carteira atualizada · +US$ 40,00 desde 30/09/2026” e o topo de Remessas com US$ 13.240, +US$ 1.240,00 (+10,3% em US$), +R$ 6.881,86 (+11,5% em R$) e R$ 66.881,86 ao câmbio de hoje (R$ 5,0515), em anel.",
        "15,8 a 18,4 s · Em dólar e em reais, com a PTAX do Banco Central. · Cartão com a conta: US$ 13.240,00 (na carteira lá fora) × R$ 5,0515 (PTAX de compra do Banco Central, 15/10/2026) = R$ 66.881,86 (em reais), com contador. · Mesma conta de exemplo da tela real.",
        "18,4 a 21,2 s · Fechamento (verde) · Remessas ao exterior no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Quanto vale hoje o que você tem lá fora? Atualizar a carteira leva menos de 30 segundos.\n\n"
        "Em Remessas, toque em Atualizar e digite o valor que aparece na corretora. O site busca sozinho a PTAX de compra do Banco Central "
        "e mostra a data e a hora do boletim. Um toque usa a cotação, outro salva.\n\n"
        "No exemplo do vídeo, US$ 13.240 com a PTAX de compra de 15/10/2026, de R$ 5,0515, dão R$ 66.881,86. O topo de Remessas passa a "
        "mostrar a carteira em dólar e em reais, com o resultado nas duas moedas.\n\n"
        "A cotação é só uma sugestão: vale o que você confirmar no campo.\n\n"
        "Tela real do timtimcash, com dados de exemplo. A cotação é a PTAX real de 15/10/2026.\n\n"
        "Fonte: Banco Central do Brasil, PTAX de 15/10/2026.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #dolar #cambio #ptax #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de novembro, a cinco semanas do fechamento do ano, quando quem investe lá fora começa a conferir quanto tem em dólar e em reais. Continua a série de exterior do mês (PTAX, câmbio médio e IOF) com a rotina que mantém tudo em dia: atualizar a carteira."),
        ("O que desperta interesse", "O cronômetro correndo desde o primeiro quadro e a pergunta direta, “Quanto vale hoje o que você tem lá fora?”; o passo a passo real termina com a conta em reais pronta e o cronômetro parado em 0:17."),
        ("Benefício para o público", "A pessoa vê que manter a carteira do exterior em dia leva poucos toques, com a PTAX de compra do Banco Central sugerida com a data e a hora do boletim, e entende que a cotação é só uma sugestão até ela salvar."),
        ("Como contribui para o perfil", "Mostra com tela real uma função de Remessas que ainda não tinha aparecido no perfil (Atualizar carteira com a PTAX sugerida), sem ligar remessas a gratuidade."),
    ],
    "alt": [
        "Reel de 21 segundos. Quanto vale hoje o que você tem lá fora? Um cronômetro de 30 segundos começa a correr. Telas reais do timtimcash "
        "no celular, com dados de exemplo. Em Remessas, a carteira está em US$ 13.200 e o botão Atualizar diz há 15 dias; um toque abre "
        "Atualizar carteira. A pessoa digita US$ 13.240. O site sugere a PTAX de compra do Banco Central, de 15/10/2026 às 13:00: R$ 5,0515. "
        "Um toque usa a cotação, e a carteira equivale a R$ 66.881,86. Outro toque salva, e o cronômetro para em 0:17. O topo de Remessas "
        "passa a mostrar US$ 13.240 e R$ 66.881,86 ao câmbio de hoje. Resumo: US$ 13.240,00 vezes R$ 5,0515 é igual a R$ 66.881,86. "
        "Remessas ao exterior no timtimcash. Link na bio."
    ],
    "fontes": [
        ("Banco Central do Brasil · PTAX, cotações de fechamento de 15/10/2026 (dólar: compra R$ 5,0515, venda R$ 5,0521)",
         "https://ptax.bcb.gov.br/ptax_internet/consultarTodasAsMoedas.do?method=consultaTodasMoedas"),
    ],
    "telas": [
        "telas/celular-remessas-1-antes.jpg · Remessas: US$ 13.200 na carteira hoje, R$ 72.600,00 ao câmbio de hoje (R$ 5,50), “Atualizar · há 15 dias” (celular 390 × 760 em escala 3, build 2026-10-16.1, relógio da página em 15/10/2026 15:00, PTAX real de 15/10)",
        "telas/celular-remessas-2-atualizar-carteira.jpg · “Atualizar carteira” aberto pelo toque em Atualizar: 13.200,00 selecionado, “usar a cotação de hoje · R$ 5,0515” e “PTAX de compra do Banco Central, de 15/10/2026 às 13:00.” (mesmo relógio)",
        "telas/celular-remessas-3-digitando-1.jpg a -7.jpg e celular-remessas-3-digitado.jpg · o valor digitado tecla a tecla (0,01; 0,13; 1,32; 13,24; 132,40; 1.324,00; 13.240,00) e “+US$ 40,00 (+0,3%) desde 30/09/2026” (mesmo relógio)",
        "telas/celular-remessas-4-cotacao-de-hoje.jpg · depois do toque na sugestão: câmbio 5,0515, “PTAX de hoje ✓”, “Equivale hoje a R$ 66.881,86” (mesmo relógio)",
        "telas/celular-remessas-5-salvo.jpg · depois do Salvar, com o aviso “Carteira atualizada · +US$ 40,00 desde 30/09/2026” (mesmo relógio)",
        "telas/celular-remessas-6-depois.jpg · Remessas: US$ 13.240 na carteira hoje, +US$ 1.240,00 (+10,3% em US$), +R$ 6.881,86 (+11,5% em R$), R$ 66.881,86 ao câmbio de hoje (R$ 5,0515), “Atualizar · hoje” (mesmo relógio)",
    ],
}
