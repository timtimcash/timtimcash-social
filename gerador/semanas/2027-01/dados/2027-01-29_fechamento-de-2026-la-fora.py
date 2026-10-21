# -*- coding: utf-8 -*-
"""Sexta 29/01/2027 · carrossel "2026 fechou. Informe o saldo de 31/12." (investimento no exterior, capa verde suave). Equipe jb.
Continuação do post de 28/12/2026 ("31/12: anote quanto há lá fora").
Artes: saida/2027-01-29_fechamento-de-2026-la-fora/01.jpg a 07.jpg, geradas por equipes/jb/posts.py (post_27, contas por assert).
Telas reais em saida/2027-01-29_fechamento-de-2026-la-fora/telas/, capturadas por equipes/jb/captura.py (c27), celular 390 px em
escala 3, relógio em 27/01/2027 10:00, build 2026-10-19.5, Remessas em dólar.

MUDANÇA NA CONTA (só na cópia jb, estado_jb.py, gerar_27): a atualização da carteira de janeiro, que na conta de base acontece em
29/01 (US$ 13.450 e € 2.018, ao câmbio salvo de exemplo, PTAX de compra de 15/10/2026), acontece em 27/01. Sem ela o site trata 2026
como o ano em curso e o "Editar fechamentos" não mostra 2026 para preencher (o código abre um ano para fechamento só quando a carteira
tem valor de um ano seguinte). Nenhum número da conta mudou; o fechamento de 2026 continua fora da conta.
PTAX de 31/12/2026: NÃO EXISTE AINDA (hoje é 20/10/2026). O post não mostra nem inventa câmbio ou valor em reais de 2026: o campo de
câmbio de 2026 ficou vazio, o botão PTAX não foi tocado (a cópia do site não tem internet) e os recortes mostram só o saldo em dólar,
o botão PTAX e a frase do site "falta o câmbio de 31/12". A linha "hoje, em curso" (2027, com o câmbio salvo de exemplo) e a linha
"Desde 2023" ficaram fora dos recortes.
Telas: "Rendimento ano a ano" antes (2025: +3,9% +480,00 −7,7% −R$ 5.969,09 fim 12.960,00; 2026: "falta o saldo de 31/12"); "Editar
fechamentos" ("Quanto havia no fim de cada ano"), com 13.380,00 digitado no saldo de 2026 e o câmbio vazio; "Salvar" (só na sessão);
o painel depois (2026: +3,2% +420,00 · falta o câmbio de 31/12 · fim 13.380,00).
Contas: saldos de 31/12 na conta de base: 2023 US$ 4.120, 2024 US$ 12.480, 2025 US$ 12.960 (fechamentos salvos) e 2026 US$ 13.380
(a carteira atualizada em 31/12/2026). 13.380 − 12.960 = 420; 420 ÷ 12.960 = 3,24% (3,2%); a taxa ao ano do site, pelas datas,
(13.380 ÷ 12.960)^(365/364) − 1 = 3,25% (3,2%). Sem envio em dólar em 2026 (a remessa de 2026 é a de € 2.000).
Como o site faz (código do build): o botão PTAX busca no Banco Central a PTAX de compra do último boletim do ano e diz a data
("PTAX de compra de 31/12/2026." ou "Último boletim de 2026: dd/mm/aaaa. O Banco Central não publica em 31/12."). Sem fato externo
novo: o post não fala da declaração (o post de 19/02 trata disso).
Revisão de 20/10/2026: o post passou de 27/01 para 29/01, para separar os temas na grade do perfil. As telas foram capturadas com o relógio em 27/01/2027, e nada nelas depende do dia."""

POST = {
    "pasta": "2027-01-29_fechamento-de-2026-la-fora",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "O fechamento de 2026 lá fora, a continuação do post de 28/12: o saldo de 31/12/2026 do exemplo (US$ 13.380), por que 2026 só aparece para fechar depois de atualizar a carteira em janeiro, como informar o saldo em Editar fechamentos, 2026 em dólar (de US$ 12.960 para US$ 13.380, +3,2%) e o botão PTAX para ver o ano em reais, sem mostrar câmbio ou valor em reais de 2026",
    "pilar": "Investimento no exterior · produto (Remessas › Rendimento ano a ano)",
    "data_longa": "sexta-feira, 29 de janeiro de 2027",
    "data_curta": "sexta-feira, 29/01/2027",
    "data_mockup": "29 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-29T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · INVESTIMENTO NO EXTERIOR · 2026 fechou. Informe o saldo de 31/12. · Duas folhas de calendário de mesa: à esquerda, inclinada, a de DEZEMBRO, 31, quinta-feira · 2026 (faixa escura); uma seta curva leva à direita, à de JANEIRO, 1, sexta-feira · 2027 (faixa verde escura). Pendurada por um fio na folha de dezembro, uma etiqueta branca: SALDO EM 31/12 · US$ 13.380.",
        "O SALDO DE 31/12 · No exemplo, US$ 13.380. · Com o saldo de 31/12, cada ano ganha a sua taxa. Sem ele, só dá para medir o período inteiro. · Linha do tempo: 31/12/2023 US$ 4.120; 31/12/2024 US$ 12.480; 31/12/2025 US$ 12.960; 31/12/2026 US$ 13.380 em verde, com o selo “anotado em 31/12”. · Nota: Exemplo: a carteira em dólar da conta fictícia dos nossos posts, no último dia de cada ano.",
        "EM JANEIRO · 2026 espera o seu saldo. · Atualize a carteira em 2027: aí 2026 vira um ano fechado e o Rendimento ano a ano pede o 31/12. · Tela real no celular: Rendimento ano a ano, “Taxa de cada ano, em US$ e em reais”, botão Editar fechamentos; 2025: +3,9% +480,00, −7,7% −R$ 5.969,09, fim 12.960,00; 2026: “falta o saldo de 31/12” nas duas taxas. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "EDITAR FECHAMENTOS · Digite o saldo de 31/12/2026. · Na moeda, como estava na conta lá fora no último dia do ano. · Tela real: “Quanto havia no fim de cada ano · Com o saldo de 31 de dezembro, o timtimcash separa o rendimento ano a ano. Sem ele, só dá para medir o período inteiro.” e a linha 2026 · 31/12/2026 · Saldo 13.380,00 (só o saldo, sem a linha do câmbio). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "EM DÓLAR · 2026 rendeu 3,2% em dólar. · Sem envios em dólar no ano. Sem o câmbio, o site mostra 2026 só em US$. · Tela real depois de Salvar: 2025 +3,9% +480,00 −7,7% −R$ 5.969,09 fim 12.960,00; 2026 +3,2% +420,00, “falta o câmbio de 31/12”, fim 13.380,00. Cartão: 31/12/2025 US$ 12.960 → 31/12/2026 US$ 13.380, +3,2%, +US$ 420. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "EM REAIS · Para o ano em reais, toque em PTAX. · Tela real do botão PTAX (recortado sozinho) e, ao lado: Toque aqui: o site busca a PTAX de compra do último boletim de 2026 e diz a data. Embaixo, a dica real: “O botão ao lado de cada câmbio busca o PTAX de compra do fecho daquele ano no Banco Central. O campo é opcional: sem ele o ano aparece só em US$, porque converter pelo câmbio de hoje daria um rendimento em reais que não aconteceu naquele ano.” · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Feche 2026 lá fora. · Remessas ao exterior no timtimcash, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "2026 fechou. Informe o saldo de 31/12.\n\n"
        "Em dezembro, pedimos para anotar quanto havia lá fora no último dia do ano. No exemplo, US$ 13.380 na carteira em dólar.\n\n"
        "Em janeiro, atualize a carteira em Remessas: aí 2026 vira um ano fechado, e o Rendimento ano a ano pede o fechamento. Em Editar "
        "fechamentos, digite o saldo de 31/12/2026 na moeda.\n\n"
        "Em dólar, o ano já fecha: de US$ 12.960 para US$ 13.380, sem envios em dólar no ano, +3,2%. Para ver o ano em reais, toque em "
        "PTAX: o site busca no Banco Central a PTAX de compra do último boletim de 2026 e diz a data. Sem o câmbio, 2026 aparece só em US$, "
        "porque converter pelo câmbio de hoje daria um rendimento em reais que não aconteceu naquele ano.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #dolar #ptax #rendimento #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "No fim de janeiro, o saldo de 31/12 já está no extrato de dezembro e a PTAX do último boletim de 2026 já saiu: é o momento de fechar 2026. Fecha o ciclo aberto no post de 28/12, no mesmo dia em que a conta de exemplo atualiza a carteira."),
        ("O que desperta interesse", "A capa vira a folha do calendário de 31/12 para 2027, e a etiqueta que estava em branco em 28/12 agora tem o número. Dentro, o passo a passo com telas reais e o ano em dólar já calculado."),
        ("Benefício para o público", "Sabe exatamente o que fazer em janeiro: atualizar a carteira, informar o saldo de 31/12 em Editar fechamentos e tocar em PTAX para ter o ano em reais, e entende por que o site não converte pelo câmbio de hoje."),
        ("Como contribui para o perfil", "Dá continuidade a um post anterior (série de exterior), mostra o Editar fechamentos de um jeito novo e respeita o cuidado com dados: nenhum câmbio ou valor em reais de 2026 aparece."),
    ],
    "alt": [
        "Investimento no exterior. 2026 fechou: informe o saldo de 31/12. Duas folhas de calendário de mesa: a de dezembro, 31, quinta-feira, 2026, inclinada à esquerda, e uma seta curva até a de janeiro, 1, sexta-feira, 2027. Pendurada na folha de dezembro, uma etiqueta: saldo em 31/12, US$ 13.380.",
        "O saldo de 31/12: no exemplo, US$ 13.380. Com o saldo de 31/12, cada ano ganha a sua taxa; sem ele, só dá para medir o período inteiro. Linha do tempo da carteira em dólar: 31/12/2023, US$ 4.120; 31/12/2024, US$ 12.480; 31/12/2025, US$ 12.960; 31/12/2026, US$ 13.380, anotado em 31/12.",
        "Em janeiro, 2026 espera o seu saldo: atualize a carteira em 2027, e 2026 vira um ano fechado. Tela real no celular, com dados de exemplo, do painel Rendimento ano a ano, com o botão Editar fechamentos: 2025, mais 3,9% e 480 dólares, menos 7,7% e menos 5.969 reais e 9 centavos, fim de 12.960 dólares; 2026, falta o saldo de 31/12.",
        "Editar fechamentos: digite o saldo de 31/12/2026, na moeda. Tela real de Quanto havia no fim de cada ano: com o saldo de 31 de dezembro, o timtimcash separa o rendimento ano a ano; sem ele, só dá para medir o período inteiro. Linha de 2026, 31/12/2026, saldo de 13.380,00 dólares.",
        "Em dólar, 2026 rendeu 3,2%, sem envios em dólar no ano; sem o câmbio, o site mostra 2026 só em dólar. Tela real depois de salvar: 2025, mais 3,9% em dólar e menos 7,7% em reais; 2026, mais 3,2% e 420 dólares, falta o câmbio de 31/12, fim de 13.380 dólares. Cartão: de US$ 12.960 em 31/12/2025 para US$ 13.380 em 31/12/2026, mais 3,2%, mais 420 dólares.",
        "Para o ano em reais, toque em PTAX. Tela real do botão PTAX: o site busca a PTAX de compra do último boletim de 2026 e diz a data. Dica real da tela: o botão ao lado de cada câmbio busca o PTAX de compra do fecho daquele ano no Banco Central; o campo é opcional, e sem ele o ano aparece só em dólar, porque converter pelo câmbio de hoje daria um rendimento em reais que não aconteceu naquele ano.",
        "Feche 2026 lá fora. Remessas ao exterior no timtimcash, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-rendimento-ano-a-ano-antes.png · Remessas ao exterior, USD, relógio em 27/01/2027 10:00, celular 390 × 3200 em escala 3, cópia jb (carteira atualizada em 27/01) · slide 3 (cabeçalho do painel e as linhas de 2025 e 2026)",
        "telas/celular-editar-fechamentos-2026.png · Editar fechamentos com 13.380,00 digitado em 2026 e o câmbio vazio, sem tocar no PTAX · slides 4 (título e a linha do saldo de 2026) e 6 (o botão PTAX e a dica)",
        "telas/celular-rendimento-ano-a-ano-depois.png · o painel depois de Salvar (só na sessão do navegador) · slide 5 (as linhas de 2025 e 2026)",
    ],
}
