# -*- coding: utf-8 -*-
"""Segunda 28/12/2026 · carrossel "31/12: anote quanto há lá fora" (investimento no exterior, capa papel).
Artes: saida/2026-12-28_anote-quanto-ha-la-fora/01.jpg a 07.jpg, geradas por equipes/dc2/posts.py (contas por assert).
Telas reais novas em saida/2026-12-28_anote-quanto-ha-la-fora/telas/, capturadas por equipes/dc2/captura.py na conta de N/base_app
(build 2026-10-16.1), sem mudar nada, relógio em 28/12/2026 10:00 (celular), Remessas em dólar:
- "Rendimento ano a ano": 2023 +6,5% (+120,00) e +3,8% (+R$ 343,68), aportes 4.000,00 a R$ 4,90, fim 4.120,00; 2024 +3,6% (+360,00)
  e +34,4% (+R$ 16.928,73), aportes 8.000,00 a R$ 5,05, fim 12.480,00; 2025 +3,9% (+480,00) e −7,7% (−R$ 5.969,09), fim 12.960,00;
  2026 até hoje +3,0% (+350,00) e −6,2% (−R$ 4.067,86), hoje 13.310,00 (taxas ao ano, como o site mostra);
- "Editar fechamentos" ("Quanto havia no fim de cada ano"): 2023 4.120,00 a R$ 4,8407; 2024 12.480,00 a R$ 6,1917; 2025 12.960,00 a
  R$ 5,5018; 2026 "hoje, em curso", 13.310,00 a R$ 5,0515. O botão PTAX não foi tocado (a cópia do site não tem internet).
Como o site faz (código do build): o botão PTAX busca a PTAX de compra do último boletim do ano no Banco Central e, quando não
é de 31/12, diz a data ("O Banco Central não publica em 31/12"); um ano só vira fechamento editável quando a carteira tem valor
atualizado num ano seguinte, por isso o post diz "em janeiro, atualize a carteira e informe o saldo de 31/12".
PTAX de fechamento: 2023 R$ 4,8407 e 2024 R$ 6,1917 (FATOS.md, Receita Federal, taxas para fins fiscais); 2025 R$ 5,5018 (FATOS.md,
usada na conta fictícia; a equipe dc2 não achou fonte oficial que abrisse para conferir este valor; ver o relatório).
Declaração, pesquisa da equipe dc2 em 16/10/2026: Receita Federal, Perguntas e Respostas IRPF 2026 (versão 1.0), pergunta 007:
"relacionar os bens e direitos que, no Brasil ou no exterior, constituam, em 31 de dezembro de 2024 e de 2025, seu patrimônio";
Lei 14.754/2023, art. 2º: rendimentos do capital aplicado no exterior declarados na DAA, separados, com 15% sobre a parcela anual
(FATOS.md). O post não dá orientação de preenchimento nem de conversão para a declaração: manda conferir com um contador."""

POST = {
    "pasta": "2026-12-28_anote-quanto-ha-la-fora",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Por que anotar o saldo de 31/12 de cada conta no exterior: com ele, o Rendimento ano a ano separa a taxa de cada ano, e em reais o fechamento usa a PTAX de compra do último dia útil (2024 +34,4% e 2025 −7,7% em reais, com rendimento parecido em dólar); como informar em Editar fechamentos; e o que a Receita diz sobre 31/12 e aplicações no exterior, sem consultoria",
    "pilar": "Investimento no exterior · fonte oficial (Receita Federal)",
    "data_longa": "segunda-feira, 28 de dezembro de 2026",
    "data_curta": "segunda-feira, 28/12/2026",
    "data_mockup": "28 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-28T10:00:00",
    "slides": [
        "Capa (fundo papel) · INVESTIMENTO NO EXTERIOR · 31/12: anote quanto há lá fora · Folha de calendário de mesa, levemente inclinada, com a faixa escura “DEZEMBRO”, “31” enorme e “quinta-feira · 2026”; pendurada por um fio, uma etiqueta verde suave “SALDO LÁ FORA · US$ ……” para preencher.",
        "POR QUE 31/12 · O ano fecha num dia. · Com o saldo de 31 de dezembro, cada ano ganha a sua taxa. Sem ele, só dá para medir o período inteiro. · Linha do tempo: 31/12/2023 US$ 4.120 (taxa de 2023 +6,5%); 31/12/2024 US$ 12.480 (taxa de 2024 +3,6%); 31/12/2025 US$ 12.960 (taxa de 2025 +3,9%); 31/12/2026 “US$ ?” em coral tracejado (taxa de 2026 +3,0% até hoje). · Nota: Exemplo: a carteira em dólar da conta fictícia dos nossos posts; taxas ao ano em US$, como o site mostra.",
        "EM REAIS · O câmbio do último dia muda o ano. · Quase o mesmo rendimento em dólar. Em reais, anos opostos. · 2024, dólar no fechamento R$ 6,1917: US$ +3,6%, R$ +34,4% (barras verdes). 2025, dólar no fechamento R$ 5,5018: US$ +3,9% (verde), R$ −7,7% (coral). · Nota: Taxas ao ano do exemplo. O site usa a PTAX de compra do último dia útil de cada ano.",
        "NO TIMTIMCASH · Cada ano, em US$ e em reais. · Tela real no celular (relógio em 28/12/2026): Rendimento ano a ano, “Taxa de cada ano, em US$ e em reais”, botão Editar fechamentos; 2024 +3,6% +360,00, +34,4% +R$ 16.928,73, aportes 8.000,00 · a R$ 5,05 · fim 12.480,00; 2025 +3,9% +480,00, −7,7% −R$ 5.969,09, fim 12.960,00. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "COMO FAZER · Anote em 31/12. Informe depois. · Tela real no celular (relógio em 28/12/2026): “Quanto havia no fim de cada ano”, “Com o saldo de 31 de dezembro, o timtimcash separa o rendimento ano a ano. Sem ele, só dá para medir o período inteiro.”; 2025 (31/12/2025) saldo 12.960,00, câmbio R$ 5,5018, botão PTAX; 2026 hoje, em curso, 13.310,00, R$ 5,0515. Ao lado: 1. Em 31/12: anote o saldo de cada conta lá fora, na moeda. 2. Em janeiro: atualize a carteira e informe o saldo de 31/12 em Editar fechamentos. 3. Toque em PTAX: e o site busca o câmbio de compra do último boletim do ano. 31/12 nem sempre tem boletim. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "E A DECLARAÇÃO? · O IR também olha para 31/12. · BENS E DIREITOS: A declaração relaciona os bens e direitos, no Brasil ou no exterior, que formam o seu patrimônio em 31 de dezembro. Receita Federal, Perguntas e Respostas IRPF 2026, pergunta 007. APLICAÇÕES NO EXTERIOR: Desde 2024, os rendimentos entram na declaração anual, separados dos demais, com 15% sobre a parcela anual. Lei 14.754/2023, art. 2º. Caixa âmbar: O timtimcash organiza os números; não faz a declaração. Para o seu caso, confira com um contador.",
        "Fechamento (fundo verde) · Feche o ano com o saldo anotado. · Remessas ao exterior no timtimcash, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "31/12: anote quanto há lá fora.\n\n"
        "O ano fecha num dia. Com o saldo de 31 de dezembro de cada conta no exterior, dá para separar o rendimento de cada ano. "
        "No nosso exemplo: US$ 4.120 em 2023, US$ 12.480 em 2024 e US$ 12.960 em 2025.\n\n"
        "Em reais, o fechamento usa a PTAX de compra do último dia útil do ano. Por isso, no exemplo, 2025 rendeu 3,9% em dólar e ficou em −7,7% em reais: "
        "a PTAX de compra do fim do ano caiu de R$ 6,1917 (2024) para R$ 5,5018 (2025).\n\n"
        "No timtimcash: anote o saldo em 31/12; em janeiro, atualize a carteira e informe o saldo em Remessas › Rendimento ano a ano › Editar fechamentos. "
        "O botão PTAX busca o câmbio no Banco Central.\n\n"
        "A declaração do IR também relaciona os bens e direitos, no Brasil e no exterior, de 31 de dezembro. Desde 2024, os rendimentos de aplicações no exterior "
        "pagam 15% na declaração anual. Confira o seu caso com um contador.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Receita Federal (Perguntas e Respostas IRPF 2026; taxas de câmbio para fins fiscais); Lei 14.754/2023.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #dolar #ptax #impostoderenda #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Segunda-feira antes da virada: o saldo de 31/12 só se anota nesse dia (ou no extrato de dezembro). Exterior é o tema que mais alcança no perfil, e este é o último post de exterior de 2026."),
        ("O que desperta interesse", "A capa é um lembrete de calendário com uma etiqueta para preencher. O slide 3 mostra o mesmo rendimento em dólar virando +34,4% e −7,7% em reais, só pelo câmbio do último dia do ano."),
        ("Benefício para o público", "Sabe por que e como registrar o saldo de 31/12, entende o papel da PTAX de fechamento e sabe o que a Receita diz sobre 31/12 e sobre as aplicações no exterior, com a indicação de procurar um contador para o próprio caso."),
        ("Como contribui para o perfil", "Apresenta o Rendimento ano a ano e o Editar fechamentos, funções das Remessas, com telas reais novas, e reforça o perfil como referência em exterior contado em reais, com fonte oficial e sem consultoria tributária."),
    ],
    "alt": [
        "Investimento no exterior. 31/12: anote quanto há lá fora. Uma folha de calendário de mesa com dezembro, o número 31 grande e quinta-feira, 2026; pendurada nela, uma etiqueta verde com saldo lá fora, US$, e um espaço pontilhado para preencher.",
        "Por que 31/12: o ano fecha num dia. Com o saldo de 31 de dezembro, cada ano ganha a sua taxa; sem ele, só dá para medir o período inteiro. Linha do tempo do exemplo: 31/12/2023, US$ 4.120, taxa de 2023 de 6,5%; 31/12/2024, US$ 12.480, taxa de 3,6%; 31/12/2025, US$ 12.960, taxa de 3,9%; 31/12/2026, US$ com um ponto de interrogação, e a taxa de 2026 de 3,0% até hoje. Taxas ao ano em dólar.",
        "Em reais, o câmbio do último dia muda o ano. Quase o mesmo rendimento em dólar; em reais, anos opostos. 2024, com o dólar no fechamento a R$ 6,1917: mais 3,6% em dólar e mais 34,4% em reais. 2025, com o dólar no fechamento a R$ 5,5018: mais 3,9% em dólar e menos 7,7% em reais. O site usa a PTAX de compra do último dia útil de cada ano.",
        "No timtimcash, cada ano em dólar e em reais. Tela real no celular, com dados de exemplo, do painel Rendimento ano a ano, com o botão Editar fechamentos. 2024: mais 3,6% e mais 360,00 em dólar; mais 34,4% e mais R$ 16.928,73 em reais; aportes de 8.000,00 a R$ 5,05; fim, 12.480,00. 2025: mais 3,9% e mais 480,00 em dólar; menos 7,7% e menos R$ 5.969,09 em reais; fim, 12.960,00.",
        "Como fazer: anote em 31/12 e informe depois. Tela real no celular, com dados de exemplo, de Quanto havia no fim de cada ano: com o saldo de 31 de dezembro, o timtimcash separa o rendimento ano a ano. 2025, saldo de 12.960,00 e câmbio de R$ 5,5018, com o botão PTAX; 2026, hoje, em curso. Passos: em 31/12, anote o saldo de cada conta lá fora, na moeda; em janeiro, atualize a carteira e informe o saldo de 31/12 em Editar fechamentos; toque em PTAX e o site busca o câmbio de compra do último boletim do ano, já que 31/12 nem sempre tem boletim.",
        "E a declaração? O IR também olha para 31/12. Bens e direitos: a declaração relaciona os bens e direitos, no Brasil ou no exterior, que formam o seu patrimônio em 31 de dezembro, segundo as Perguntas e Respostas do IRPF 2026, da Receita Federal. Aplicações no exterior: desde 2024, os rendimentos entram na declaração anual, separados dos demais, com 15% sobre a parcela anual, pela Lei 14.754 de 2023. O timtimcash organiza os números e não faz a declaração; para o seu caso, confira com um contador.",
        "Feche o ano com o saldo anotado. Remessas ao exterior no timtimcash, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Receita Federal · Perguntas e Respostas IRPF 2026, versão 1.0, pergunta 007 (bens e direitos, no Brasil ou no exterior, em 31 de dezembro), consultado em 16/10/2026", "https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf"),
        ("Planalto · Lei nº 14.754, de 2023, art. 2º (rendimentos de aplicações no exterior na Declaração de Ajuste Anual, 15% sobre a parcela anual)", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm"),
        ("Receita Federal · Taxas de câmbio para fins fiscais, anos anteriores: dólar, compra, R$ 4,8407 em 29/12/2023, R$ 6,1917 em 31/12/2024 e R$ 5,5018 em 31/12/2025 (conferido em 16/10/2026)", "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/ecf/taxas-de-cambio-incluindo-valor-do-dolar-para-fins-fiscais-irpj-AC-anteriores"),
    ],
    "telas": [
        "telas/celular-remessas-dolar.png · Remessas ao exterior, moeda USD, relógio em 28/12/2026 10:00 (página inteira, 390 × 1400 em escala 3): painel “Rendimento ano a ano” · slide 4 (o cabeçalho com Editar fechamentos e as linhas de 2024 e 2025)",
        "telas/celular-fechamentos.png · “Editar fechamentos” aberto, “Quanto havia no fim de cada ano”, sem mudar nada; relógio em 28/12/2026 10:00 · slide 5 (o título e as linhas de 2025 e de 2026)",
    ],
}
