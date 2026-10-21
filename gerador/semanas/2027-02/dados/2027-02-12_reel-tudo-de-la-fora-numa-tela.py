# -*- coding: utf-8 -*-
"""Sexta 12/02/2027 · Reel "Tudo de lá fora, numa tela só" (investimento no exterior e produto: Remessas ao exterior no computador;
capa verde). Equipe fr. Versão de 20/10/2026, depois da revisão interna (três ajustes):
1. conta de base com o saldo de 31/12/2026 informado em 29/01/2027 em "Editar fechamentos" (US$ 13.380 e € 2.014, câmbio vazio, como
   ensina o post de 27/01): o "Rendimento ano a ano" mostra 2026 com +3,2% e +420,00 em US$ e "falta o câmbio de 31/12" em reais, e
   2027 "até hoje" com "falta o câmbio do ano anterior";
2. legibilidade: nos quadros "Cada ano" e "E cada remessa", a câmera chega a 2,75 e 2,5 px do Reel por px CSS e cada número em foco
   tem pelo menos 30 px de altura (porcentagens do ano a ano 13 px · 2,75 = 35,8 px; valores 11 px · 2,75 = 30,3 px; datas 12 px e
   câmbios 13 px · 2,5 = 30 e 32,5 px; tamanhos da letra medidos na captura e conferidos por assert no roteiro);
3. o indicador "IOF pago R$ 0,00" (painel de Remetido, Custo total, Câmbio médio efetivo e IOF pago) não aparece em nenhum quadro: a
   descida do gancho para antes dele, as passagens para a tabela das remessas e de volta ao topo são cortes secos, e a coluna IOF da
   tabela fica fora do recorte (conferido por assert com as caixas medidas).
Vídeo, capa e prévia gerados por equipes/fr/reel_12.py; telas capturadas por equipes/fr/captura_12.py no site build 2026-10-19.5, na
conta de base (J/base_app/estado.py; o estado de 12/02 foi gerado a partir dele em equipes/fr/trabalho/12/estado_2027-02-12.js, sem
usar o arquivo pronto antigo da base), no computador (1440 × 900 em escala 3), relógio da página em 12/02/2027 10:00: Remessas ao
exterior pelo menu lateral, no dólar, na tela do computador e na página inteira (janela alta de 1440 × 2700, a mesma página sem rolar);
depois, um clique no botão "EUR" (a tela do euro, 1440 × 900).
Números da tela: "US$ 13.450 na carteira hoje", +US$ 1.450,00 (+12,1% em US$), +R$ 7.942,68 (+13,2% em R$), "R$ 67.942,68 ao câmbio
de hoje (R$ 5,0515)"; "De onde veio o resultado em reais": R$ 60.000 enviados, +R$ 7.325 de rendimento, +R$ 618 de efeito do câmbio,
R$ 67.943 hoje; "Câmbio: onde você está": equilíbrio R$ 4,461 (R$ 0); "Rendimento ano a ano": 2023 +6,5% e +120,00 em US$, +3,8% e
+R$ 343,68 em R$; 2024 +3,6% e +360,00, +34,4% e +R$ 16.928,73; 2025 +3,9% e +480,00, −7,7% e −R$ 5.969,09; 2026 +3,2% e +420,00 em
US$, "falta o câmbio de 31/12"; 3 remessas de US$ 4.000 (18/04/2024 a R$ 5,1000, 14/03/2024 a R$ 5,0000 e 12/07/2023 a R$ 4,9000).
Euro: "€ 2.018 na carteira hoje", +€ 18,00 (+0,9% em €), −R$ 105,13 (−0,9% em R$).
O câmbio "de hoje" da conta de exemplo é o salvo na carteira: a PTAX de compra real de 15/10/2026 (dólar R$ 5,0515; euro R$ 5,6592),
como nos posts de dezembro; os fechamentos de 2023 a 2025 usam a PTAX de compra real do último dia útil de cada ano (R$ 4,8407,
R$ 6,1917 e R$ 5,5018). Fatos de novdez/FATOS.md (PTAX), repetidos no BRIEFING; não estão no FATOS.md de janeiro e fevereiro.
Painel que depende da internet: sem ela, "Contra o CDI" não aparece e "Câmbio: onde você está" vem sem a linha do CDI; nada vazio
entra no vídeo. Como é exterior, a legenda não traz a frase do controle financeiro nem o convite de cadastro.
Diferença do que já saiu: os posts de Remessas de outubro a janeiro mostraram um painel por vez, no celular (câmbio de equilíbrio,
rendimento ano a ano, ritmo do retorno, câmbio médio, atualizar carteira, a jornada, dólar e euro, investido há); aqui é a página
inteira no computador, numa passada só, com o clique que troca de moeda."""

POST = {
    "pasta": "2027-02-12_reel-tudo-de-la-fora-numa-tela",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Tudo de lá fora, numa tela só: no computador, a página de Remessas ao exterior mostra a carteira e o resultado na moeda e em reais, de onde veio o resultado, o câmbio de equilíbrio, cada ano e cada remessa; um clique troca para o euro",
    "pilar": "Investimento no exterior · produto (Remessas ao exterior, no computador)",
    "data_longa": "sexta-feira, 12 de fevereiro de 2027",
    "data_curta": "sexta-feira, 12/02/2027",
    "data_mockup": "12 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-12T10:00:00",
    "video": "saida/2027-02-12_reel-tudo-de-la-fora-numa-tela/reel.mp4",
    "capa": "saida/2027-02-12_reel-tudo-de-la-fora-numa-tela/capa.jpg",
    "previa": "saida/2027-02-12_reel-tudo-de-la-fora-numa-tela/previa.mp4",
    "slides": [
        "Capa da grade (verde, logotipo negativo) · REMESSAS AO EXTERIOR · Tudo de lá fora, numa tela só. · Um computador desenhado em traço branco, com quatro ícones de traço na tela: barras, uma trajetória, uma escada e uma tabela.",
        "0 a 2,6 s · Gancho (tinta) · REMESSAS AO EXTERIOR · Tudo de lá fora, numa tela só. · As pílulas “US$ 13.450” e “€ 2.018” saltam no primeiro quadro; embaixo, a tela real do computador (12/02/2027) com a página de Remessas, e a câmera desce do topo até o “Rendimento ano a ano” (para antes do painel do IOF). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "2,8 a 4,8 s · Quanto tem e quanto rendeu: na moeda e em reais. · A câmera chega perto do topo: anel em “US$ 13.450 na carteira hoje” e depois nas pílulas “+US$ 1.450,00 +12,1% em US$” e “+R$ 7.942,68 +13,2% em R$”.",
        "4,9 a 6,9 s · De onde veio: rendimento e câmbio. · Painel “De onde veio o resultado em reais” (R$ 60.000 enviados, +R$ 7.325 de rendimento, +R$ 618 de câmbio, R$ 67.943 hoje); anel na frase do site.",
        "7,1 a 9,1 s · O câmbio que zera o resultado: R$ 4,461. · Painel “Câmbio: onde você está”, de perto; anel em “No equilíbrio (R$ 4,461) R$ 0”.",
        "9,2 a 12,8 s · Cada ano, em dólar e em reais. · “Rendimento ano a ano” de perto: primeiro a coluna ANO e as barras (2023 a 2026), depois um deslize lento até EM US$ e EM R$; o anel acompanha as linhas de 2023 a 2025: +6,5% e +120,00 / +3,8% e +R$ 343,68; +3,6% e +360,00 / +34,4% e +R$ 16.928,73; +3,9% e +480,00 / −7,7% e −R$ 5.969,09. Embaixo, 2026: +3,2% e +420,00 em US$ e “falta o câmbio de 31/12”.",
        "13,0 a 15,4 s · E cada remessa, com o câmbio que pagou. · Corte seco para a tabela “Remessas”, de perto: DATA, ORIGEM e DESTINO; deslize até ENVIADO e CÂMBIO EFETIVO (US$ 4.000,00 a R$ 5,1000, R$ 5,0000 e R$ 4,9000); anel nas 3 remessas. A coluna IOF fica fora do recorte.",
        "15,6 a 17,8 s · O euro também, num clique. · Corte para o topo; o ponteiro clica em “EUR” e a página troca: anel em “€ 2.018 na carteira hoje”.",
        "17,8 a 20,6 s · Fechamento (verde) · Remessas ao exterior no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Tudo de lá fora, numa tela só.\n\n"
        "No computador, a página de Remessas ao exterior mostra de uma vez: quanto você tem na carteira (US$ 13.450 no exemplo), quanto "
        "rendeu na moeda (+12,1%) e em reais (+13,2%), de onde veio o resultado (R$ 7.325 de rendimento e R$ 618 de câmbio), o câmbio que "
        "zeraria o resultado em reais (R$ 4,461), cada ano em dólar e em reais e cada remessa, com o câmbio que custou.\n\n"
        "Com dólar e euro, cada moeda tem o seu botão: um clique troca a página.\n\n"
        "Tela real do timtimcash, com dados de exemplo. O câmbio de hoje do exemplo é o salvo na carteira: a PTAX de compra de 15/10/2026 "
        "(dólar R$ 5,0515; euro R$ 5,6592).\n\n"
        "Fonte: Banco Central do Brasil, PTAX de 15/10/2026.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #remessas #dolar #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fevereiro é quando quem investe lá fora começa a olhar os números de 2026 para a declaração; a página inteira, numa olhada, mostra onde cada número está."),
        ("O que desperta interesse", "A promessa de ver tudo numa tela só, com os dois valores (US$ 13.450 e € 2.018) no primeiro quadro e a câmera descendo pela página real do computador."),
        ("Benefício para o público", "Entende o que cada parte da página responde: quanto tem, quanto rendeu, por quê, a partir de que câmbio perde em reais, ano a ano e remessa a remessa."),
        ("Como contribui para o perfil", "Primeira vez que o perfil mostra Remessas no computador, inteira e numa passada, com um terceiro exterior do mês sem repetir os ângulos de outubro a janeiro."),
    ],
    "alt": [
        "Reel de 21 segundos. Em fundo escuro, a frase Tudo de lá fora, numa tela só, com as pílulas US$ 13.450 e € 2.018, e a tela real do timtimcash no "
        "computador, com dados de exemplo: a página de Remessas ao exterior. Depois, a câmera chega perto de cada parte: "
        "US$ 13.450 na carteira hoje, mais 12,1% em dólar e mais 13,2% em reais; de onde veio o resultado em reais, com rendimento e efeito do câmbio; o câmbio "
        "de equilíbrio, R$ 4,461, que zera o resultado; o rendimento ano a ano em dólar e em reais: 2023, mais 6,5% "
        "em dólar e mais 3,8% em reais; 2024, mais 3,6% e mais 34,4%; 2025, mais 3,9% e menos 7,7%; e 2026, mais 3,2% em dólar, com o câmbio de 31/12 ainda por informar. "
        "Na tabela das remessas, as 3 remessas de US$ 4.000, com o câmbio efetivo de cada uma: R$ 5,10, R$ 5,00 e R$ 4,90. No fim, o ponteiro clica em EUR "
        "e a página troca para o euro: € 2.018 na carteira hoje. Remessas ao exterior no timtimcash. Link na bio."
    ],
    "fontes": [
        ("Banco Central do Brasil · PTAX, cotações de fechamento de 15/10/2026 (dólar: compra R$ 5,0515; euro: compra R$ 5,6592), o câmbio salvo na conta de exemplo",
         "https://ptax.bcb.gov.br/ptax_internet/consultarTodasAsMoedas.do?method=consultaTodasMoedas"),
        ("Receita Federal · taxas de câmbio para fins fiscais (PTAX de compra do fim de 2023, 2024 e 2025, usadas nos fechamentos da conta de exemplo)",
         "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/ecf/taxas-de-cambio-incluindo-valor-do-dolar-para-fins-fiscais-irpj-AC-anteriores"),
    ],
    "telas": [
        "telas/computador-remessas-dolar-pagina.png · Remessas ao exterior no computador, no dólar, página inteira (janela de 1440 × 2700 em escala 3; site build 2026-10-19.5, conta de base com o saldo de 31/12/2026 informado, relógio em 12/02/2027 10:00) · 0 a 16,5 s",
        "telas/computador-remessas-euro-tela.png · a mesma página depois do clique em EUR (1440 × 900): € 2.018 na carteira hoje, +€ 18,00 (+0,9% em €), −R$ 105,13 (−0,9% em R$) · 16,5 a 17,8 s",
        "telas/computador-remessas-dolar-tela.png e computador-remessas-euro-pagina.png · a tela do dólar em 1440 × 900 e a página inteira do euro (no euro, 2026 com +8,9% em € e “falta o câmbio de 31/12”) · conferência, não aparecem no vídeo",
        "telas/caixas.json · posições medidas na captura (painéis, linhas e colunas das tabelas, botões), o tamanho da letra de cada número usado e o texto de cada tela, usados nos anéis, no ponteiro, na câmera e nos assert do roteiro",
    ],
}
