# -*- coding: utf-8 -*-
"""Domingo 06/12/2026 · Reel "Seu 2026 em 5 números" (produto, retrospectiva; capa verde, sem coral). Equipe dr1.
Vídeo, capa e prévia gerados por equipes/dr1/reel_06.py; telas reais capturadas por equipes/dr1/capturas/captura06.py (e captura06b.py,
que refez a foto da Visão geral abaixo da barra do topo) no site build 2026-10-16.1, na conta de base (N/base_app, sem mudança),
no celular (390 px CSS, escala 3), com o relógio em 06/12/2026 10:00 e o período Ano 2026 escolhido pela interface
("Dezembro 2026" › "Ano atual" › "Aplicar"). Números da tela (assert no gerador):
1. Transações, busca "delivery": "40 transações · 40 pagas · 0 pendentes · somam R$ 3.142,40 · 750 no histórico";
2. Visão geral, "Top saídas": "Casa R$ 27.539,30 30%" (aluguel e conta de luz de janeiro a novembro; o aluguel de dezembro vence em 10/12);
3. Fluxo, "Resumo mensal": "Jan de 2026 · R$ 9.480,00 · −R$ 9.420,00", a maior saída do ano (fev R$ 8.050, nov R$ 9.149,40);
   em janeiro de 2026 a conta tem "IPVA · parcela única" (R$ 1.180) e "IPTU · 1ª parcela" (R$ 210);
4. Remessas, "Rendimento ano a ano": "2026 até hoje · +3,0% · +350,00 · −6,2% · −R$ 4.067,86 · hoje 13.310,00";
5. Fluxo: "Resultado · Ano 2026 até 06/12 · R$ 31.769,90 · Guardou 25,6% do que entrou · Entrou R$ 123.860 · Saiu R$ 92.090,10".
O ano ainda não acabou: o vídeo e a legenda dizem "de 1º de janeiro a 6 de dezembro"."""

POST = {
    "pasta": "2026-12-06_reel-seu-2026-em-5-numeros",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Seu 2026 em 5 números: uma retrospectiva no tom de “wrapped”, com telas reais. Na conta de exemplo, de 1º/1 a 6/12: 40 pedidos de delivery, 30% para Casa, janeiro como o mês mais caro, +US$ 350 lá fora e 25,6% da receita guardada",
    "pilar": "Produto (Transações, Visão geral, Fluxo e Remessas) · retrospectiva de fim de ano",
    "data_longa": "domingo, 6 de dezembro de 2026",
    "data_curta": "domingo, 06/12/2026",
    "data_mockup": "6 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-06T10:00:00",
    "video": "saida/2026-12-06_reel-seu-2026-em-5-numeros/reel.mp4",
    "capa": "saida/2026-12-06_reel-seu-2026-em-5-numeros/capa.jpg",
    "previa": "saida/2026-12-06_reel-seu-2026-em-5-numeros/previa.mp4",
    "slides": [
        "Capa da grade (verde, logotipo negativo) · RETROSPECTIVA · Seu ano em 5 números · “2026” enorme em branco e, embaixo, cinco barrinhas brancas, como os segmentos de um story. Sem coral.",
        "0 a 2,3 s · Gancho (verde) · RETROSPECTIVA · CONTA DE EXEMPLO · Seu 2026 em 5 números. · Os algarismos de “2026” sobem em sequência desde o primeiro quadro; no topo, uma barra de 5 segmentos se acende. · De 1º de janeiro a 6 de dezembro de 2026.",
        "2,3 a 5,6 s · 1 DE 5 · DELIVERY (tinta) · “40” enorme em menta, contando · pedidos de delivery · R$ 3.142,40 no ano, na busca de Transações · Recorte real de Transações (Ano 2026, busca “delivery”): “40 transações · 40 pagas · 0 pendentes · somam R$ 3.142,40”, com anel. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "5,6 a 8,9 s · 2 DE 5 · PARA ONDE FOI (papel) · “30%” enorme em coral · do que saiu foi para Casa · R$ 27.539,30 em 2026: aluguel e conta de luz · Recorte real da Visão geral (Ano 2026), “Top saídas”: Casa R$ 27.539,30 30% (com anel), Mercado R$ 17.260,10 19%, Educação R$ 15.950,00 17%.",
        "8,9 a 12,2 s · 3 DE 5 · O MÊS MAIS CARO (verde suave) · “R$ 9.420” enorme · em janeiro, o mês mais caro · IPVA e IPTU chegaram juntos · Recorte real do Fluxo (Ano 2026), “Resumo mensal”: Jan de 2026, entradas R$ 9.480,00, saídas −R$ 9.420,00 (com anel); Fev de 2026, −R$ 8.050,00.",
        "12,2 a 15,5 s · 4 DE 5 · LÁ FORA (tinta) · “+US$ 350” enorme em menta · rendeu lá fora em 2026, em dólar · Taxa ao ano: +3,0% em US$ · −6,2% em reais · Recorte real de Remessas, “Rendimento ano a ano”: 2026 até hoje, +3,0%, +350,00, −6,2%, −R$ 4.067,86, hoje 13.310,00 (com anel).",
        "15,5 a 18,8 s · 5 DE 5 · GUARDADO (verde suave) · “25,6%” enorme em verde escuro · da receita ficou guardada · Entrou R$ 123.860 · saiu R$ 92.090 · Recorte real do Fluxo (Ano 2026): “Resultado · Ano 2026 até 06/12 · R$ 31.769,90 · Guardou 25,6% do que entrou · Entrou R$ 123.860 · Saiu R$ 92.090,10”, com anel em “Guardou 25,6%”.",
        "18,8 a 21,5 s · Fechamento (verde) · Seu 2026 no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Seu 2026 em 5 números. Quais seriam os seus?\n\n"
        "No exemplo do vídeo, de 1º de janeiro a 6 de dezembro:\n"
        "1. 40 pedidos de delivery, R$ 3.142,40 no ano.\n"
        "2. 30% do que saiu foi para Casa: R$ 27.539,30 de aluguel e conta de luz.\n"
        "3. Janeiro foi o mês mais caro: R$ 9.420, com IPVA e IPTU.\n"
        "4. Lá fora, a carteira rendeu US$ 350 em 2026, numa taxa de 3,0% ao ano em dólar. Em reais, com o dólar mais barato, a taxa do ano está em −6,2%.\n"
        "5. 25,6% da receita ficou guardada: entraram R$ 123.860 e saíram R$ 92.090.\n\n"
        "Para ver os seus, escolha o período Ano no timtimcash: Transações, Visão geral, Fluxo e Remessas mostram cada número.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#retrospectiva2026 #controlefinanceiro #financaspessoais #organizacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Domingo de dezembro, quando todo mundo olha para trás: as retrospectivas do ano estão em toda parte, e a do dinheiro também cabe em cinco números."),
        ("O que desperta interesse", "O formato de retrospectiva, com uma cor por número e o “2026” enorme logo no primeiro segundo; números curiosos (40 pedidos de delivery) ao lado de números que importam (25,6% guardados), cada um com a tela real."),
        ("Benefício para o público", "Descobre onde achar o próprio retrato do ano no timtimcash: o período Ano em Transações, Visão geral, Fluxo e Remessas, incluindo a leitura honesta do exterior (em dólar e em reais)."),
        ("Como contribui para o perfil", "Mostra a amplitude do produto num só Reel, com quatro telas reais e dados coerentes entre si, num formato de fim de ano feito para compartilhar."),
    ],
    "alt": [
        "Reel de 21 segundos. Num fundo verde, o título Seu 2026 em 5 números, com 2026 enorme e uma barra de cinco segmentos, como num story; de 1º de janeiro a 6 de dezembro de 2026, na conta de exemplo. "
        "Cada número abre uma cena de uma cor, com um recorte da tela real do timtimcash: 1, num fundo escuro, 40 pedidos de delivery, R$ 3.142,40 no ano, na busca de Transações. "
        "2, num fundo claro, 30% do que saiu foi para Casa, R$ 27.539,30 de aluguel e conta de luz, na lista Top saídas da Visão geral. "
        "3, num fundo verde-claro, R$ 9.420 em janeiro, o mês mais caro, com IPVA e IPTU, no Resumo mensal do Fluxo. "
        "4, num fundo escuro, mais 350 dólares lá fora em 2026, numa taxa de 3,0% ao ano em dólar e de menos 6,2% em reais por causa do câmbio, no Rendimento ano a ano das Remessas. "
        "5, num fundo verde-claro, 25,6% da receita ficou guardada: entraram R$ 123.860 e saíram R$ 92.090, no Fluxo. Seu 2026 no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/a-transacoes-ano-2026-delivery.png · Transações no celular, período Ano 2026 escolhido pela interface e a busca “delivery” digitada, site build 2026-10-16.1, conta de base, relógio em 06/12/2026 10:00: “40 transações · 40 pagas · 0 pendentes · somam R$ 3.142,40” · recorte de 3,1 a 5,6 s",
        "telas/b-visao-geral-ano-2026-top-saidas.png · Visão geral, Ano 2026, rolada até “Top saídas” (Casa R$ 27.539,30 30%) · recorte de 6,4 a 8,9 s",
        "telas/c-fluxo-ano-2026-resultado.png · Fluxo, Ano 2026: “Resultado · Ano 2026 até 06/12 · R$ 31.769,90 · Guardou 25,6% do que entrou” · recorte de 16,3 a 18,8 s",
        "telas/c-fluxo-ano-2026-resumo-mensal.png · Fluxo, Ano 2026, rolado até “Resumo mensal” (Jan de 2026, −R$ 9.420,00) · recorte de 9,7 a 12,2 s",
        "telas/d-relatorios-sazonalidade.png · Relatórios, Ano 2026, “Sazonalidade” (janeiro é a barra mais alta) · referência, não aparece no vídeo",
        "telas/e-remessas-rendimento-ano-a-ano.png · Remessas (USD), “Rendimento ano a ano”: 2026 até hoje, +3,0%, +350,00, −6,2%, −R$ 4.067,86 · recorte de 13,0 a 15,5 s",
    ],
}
