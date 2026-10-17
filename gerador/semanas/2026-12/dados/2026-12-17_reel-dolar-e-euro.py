# -*- coding: utf-8 -*-
"""Quinta 17/12/2026 · Reel "Dólar e euro: cada um na sua moeda" (investimento no exterior e produto; capa verde suave). Equipe dr2.
Vídeo, capa e prévia gerados por equipes/dr2/reel_17.py (com assert nos números lidos da tela); telas capturadas por
equipes/dr2/captura_17.py no site build 2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular (390 px em escala 3,
janela de 1100 px de altura para pegar o topo e o painel "De onde veio o resultado em reais"), relógio da página em 16/12/2026 10:00.
Interação real: Remessas abre na primeira moeda (USD); um toque no botão "EUR" redesenha a tela no euro (troca seca, como no site).
Números da tela: dólar, "US$ 13.310 na carteira hoje", +US$ 1.310,00 (+10,9% em US$), +R$ 7.235,46 (+12,1% em R$),
"R$ 67.235,47 ao câmbio de hoje (R$ 5,0515)"; euro, "€ 2.012 na carteira hoje", +€ 12,00 (+0,6% em €), −R$ 139,09 (−1,2% em R$),
"R$ 11.386,31 ao câmbio de hoje (R$ 5,6592)" e "O câmbio caiu 1,8% desde o câmbio médio do que ainda está lá fora
(R$ 5,7627 → R$ 5,6592) e devolveu R$ 207. Falta −R$ 139,09 (−1,2%)." Conta: 2.012 × 5,6592 = 11.386,31; 11.386,31 − 11.525,40 = −139,09.
R$ 5,7627 é o câmbio efetivo da remessa de € 2.000 (R$ 11.525,40 com IOF de 1,10%). Os câmbios das carteiras da conta fictícia
(dólar R$ 5,0515 desde 30/11 e euro R$ 5,6592 desde 15/12) são as PTAX de compra reais de 15/10/2026 (FATOS.md); a legenda diz isso.
18 moedas e 41 destinos: listas _REM_MOEDAS e _REM_PAISES do código do site (build 2026-10-16.1), contadas; o quadro de moedas do
vídeo é desenhado com os 18 códigos dessa lista. O site não soma moedas diferentes num total (FUNCIONALIDADES.md): o vídeo diz isso."""

POST = {
    "pasta": "2026-12-17_reel-dolar-e-euro",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Dólar e euro, cada um na sua moeda: em Remessas, um toque troca a tela de moeda; o dólar rendeu em dólar e em reais, o euro rendeu em euro e perdeu em reais, e por isso, em Remessas, o site não soma moedas diferentes num total",
    "pilar": "Investimento no exterior · produto (Remessas ao exterior)",
    "data_longa": "quinta-feira, 17 de dezembro de 2026",
    "data_curta": "quinta-feira, 17/12/2026",
    "data_mockup": "17 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-17T10:00:00",
    "video": "saida/2026-12-17_reel-dolar-e-euro/reel.mp4",
    "capa": "saida/2026-12-17_reel-dolar-e-euro/capa.jpg",
    "previa": "saida/2026-12-17_reel-dolar-e-euro/previa.mp4",
    "slides": [
        "Capa da grade (verde suave) · REMESSAS AO EXTERIOR · Dólar e euro, cada um na sua moeda · Duas pílulas grandes lado a lado: “US$” em verde e “€” em tinta.",
        "0 a 2,5 s · Gancho (papel) · REMESSAS AO EXTERIOR · Quanto você tem lá fora? · Desde o primeiro quadro, as pílulas “US$ 13.310” e “€ 2.012” entram pelos lados, com um “+” e um “= ?” que balança.",
        "2,8 a 4,8 s · Em Remessas, cada moeda tem o seu botão. · Tela real de Remessas no dólar, com o topo da tela e anel nos botões USD e EUR.",
        "5,0 a 6,8 s · Dólar: +10,9% em US$. Em reais, +12,1%. · Zoom no cartão do topo: US$ 13.310 na carteira hoje; anel em “+US$ 1.310,00 +10,9% em US$” e “+R$ 7.235,46 +12,1% em R$”.",
        "6,9 a 7,3 s · Toque no botão EUR: a tela troca para o euro.",
        "7,4 a 9,7 s · Euro: +0,6% em euro. Em reais, −1,2%. · € 2.012 na carteira hoje; anel verde em “+€ 12,00 +0,6% em €” e anel vermelho em “−R$ 139,09 −1,2% em R$”.",
        "9,9 a 12,4 s · Pagou R$ 5,7627 por euro, com IOF. Hoje: R$ 5,6592. · Painel “De onde veio o resultado em reais” do euro (11,5 mil enviados, +68 de rendimento, −207 de efeito do câmbio, 11,4 mil hoje), com anel no texto do site.",
        "12,8 a 16,5 s · Somar as duas esconderia isso. Cada uma na sua moeda. · Quadro desenhado: US$ (13.310 na carteira) +10,9% na moeda e +12,1% em reais; € (2.012 na carteira) +0,6% na moeda e −1,2% em reais. · Em Remessas, o timtimcash não soma moedas diferentes num total: cada uma é medida na própria moeda e em reais.",
        "16,7 a 18,7 s · 18 moedas e 41 destinos. · As 18 moedas do site aparecem uma a uma (USD e EUR em verde). · Cada moeda em uso ganha o seu botão em Remessas.",
        "18,7 a 21,4 s · Fechamento (verde) · Remessas ao exterior no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Tem dólar e euro lá fora? Cada um na sua moeda.\n\n"
        "Em Remessas, cada moeda em uso ganha um botão, e um toque troca a tela inteira. No exemplo do vídeo, a carteira em dólar "
        "tem US$ 13.310: +10,9% em dólar e +12,1% em reais.\n\n"
        "O euro conta outra história. Os € 2.000 enviados em 1º de dezembro viraram € 2.012: +0,6% em euro. Em reais, −1,2%: "
        "o envio custou R$ 5,7627 por euro, já com o IOF, e hoje o euro vale R$ 5,6592.\n\n"
        "Por isso, em Remessas, o timtimcash não soma moedas diferentes num total: cada uma é medida na própria moeda e em reais. São 18 moedas e 41 destinos.\n\n"
        "Tela real do timtimcash, com dados de exemplo. Os câmbios do exemplo são as PTAX de compra reais de 15/10/2026 "
        "(dólar R$ 5,0515; euro R$ 5,6592).\n\n"
        "Fonte: Banco Central do Brasil, PTAX de 15/10/2026.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #dolar #euro #cambio #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de ano, quando quem investe lá fora olha a carteira antes de fechar o ano. A conta do exemplo fez a primeira remessa em euro em 1º de dezembro, e o exterior é o tema que mais alcançou em outubro. Continua a série de Remessas de novembro (câmbio médio e atualizar a carteira)."),
        ("O que desperta interesse", "A conta que não fecha logo no primeiro segundo (US$ 13.310 + € 2.012 = ?) e a virada da história: o euro rendeu em euro e, no mesmo período, perdeu em reais."),
        ("Benefício para o público", "Entender que cada moeda tem o próprio câmbio e o próprio resultado, e que um total único em reais esconderia o que aconteceu com cada uma. A pessoa vê como trocar de moeda no site com um toque."),
        ("Como contribui para o perfil", "Mostra com tela real uma função ainda inédita no perfil (o botão de cada moeda em Remessas) e reforça a honestidade das contas: o site não mistura moedas num total."),
    ],
    "alt": [
        "Reel de 21 segundos. Quanto você tem lá fora? As pílulas US$ 13.310 e € 2.012 entram com um sinal de mais e um igual com ponto "
        "de interrogação. Telas reais do timtimcash no celular, com dados de exemplo. Em Remessas, cada moeda tem o seu botão, USD e EUR. "
        "No dólar, US$ 13.310 na carteira: mais 10,9% em dólar e mais 12,1% em reais. Um toque em EUR troca a tela: € 2.012 na carteira, "
        "mais 0,6% em euro e menos 1,2% em reais. O título diz que o envio custou R$ 5,7627 por euro, com IOF, e que hoje o euro vale "
        "R$ 5,6592; o painel De onde veio o resultado em reais mostra que o câmbio devolveu R$ 207. Um quadro resume as duas moedas, cada uma na própria moeda e em reais, e lembra que, em Remessas, o site não soma "
        "moedas diferentes num total. Depois aparecem as 18 moedas: são 18 moedas e 41 destinos. Remessas ao exterior no timtimcash. Link na bio."
    ],
    "fontes": [
        ("Banco Central do Brasil · PTAX, cotações de fechamento de 15/10/2026 (dólar: compra R$ 5,0515; euro: compra R$ 5,6592)",
         "https://ptax.bcb.gov.br/ptax_internet/consultarTodasAsMoedas.do?method=consultaTodasMoedas"),
    ],
    "telas": [
        "telas/celular-remessas-dolar.jpg · Remessas no dólar: botões USD e EUR, US$ 13.310 na carteira hoje, +US$ 1.310,00 (+10,9% em US$), +R$ 7.235,46 (+12,1% em R$), R$ 67.235,47 ao câmbio de hoje (R$ 5,0515), “Atualizar · há 16 dias” (celular 390 px em escala 3, build 2026-10-16.1, relógio da página em 16/12/2026 10:00)",
        "telas/celular-remessas-euro.jpg · a mesma tela depois do toque em EUR: € 2.012 na carteira hoje, +€ 12,00 (+0,6% em €), −R$ 139,09 (−1,2% em R$), R$ 11.386,31 ao câmbio de hoje (R$ 5,6592) e o painel “De onde veio o resultado em reais” (mesmo relógio)",
        "telas/caixas.json · posições medidas na captura (botões, pílulas, painel) e o texto de cada tela, usados nos anéis e nos assert do roteiro",
    ],
}
