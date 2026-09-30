# -*- coding: utf-8 -*-
"""Quinta 15/10/2026 · carrossel "Reserva de emergência: quantos meses você aguentaria?" (educação, capa verde suave).
Artes: saida/2026-10-15_reserva-em-meses/01.jpg a 07.jpg, geradas por carrosseis-a/posts.py (contas conferidas por assert).
Tela real: gerador/telas/secoes/celular-relatorios-diagnostico.jpg (do repositório, sem captura nova).
A conta da "Reserva" do Diagnóstico, conferida no código do site (calcDiagnostico, cópia em carrosseis-a/app/site):
reserva = totalGeral() ÷ despesa média mensal. totalGeral() soma o saldo das contas marcadas em "Incluir no patrimônio
total"; a média usa os 12 meses antes do mês atual (janela padrão, ajustável em 3, 6, 12 ou 24), sem os meses sem
lançamento ("Ignorar meses vazios", ligado por padrão). Meta padrão de 6 meses (ajustável de 1 a 36).
Conta fictícia: R$ 104.180 ÷ R$ 8.342,27 (média de out/25 a ago/26, 11 meses com lançamentos) = 12,49 = "12,5 meses".
Saldos conferidos na página: Conta corrente R$ 14.180; Reserva R$ 30.000; Corretora no exterior R$ 60.000.
Só o que está à mão (conta corrente e reserva): R$ 44.180 ÷ R$ 8.342,27 = 5,30 = 5,3 meses."""

POST = {
    "pasta": "2026-10-15_reserva-em-meses",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Reserva de emergência medida em meses de gasto: por que em meses e não em reais, a conta do Diagnóstico (patrimônio dividido pela despesa média do mês), por que nem todo patrimônio é reserva e o teste “Perde a maior renda” da Simulação futura",
    "pilar": "Educação prática",
    "data_longa": "quinta-feira, 15 de outubro de 2026",
    "data_curta": "quinta-feira, 15/10/2026",
    "data_mockup": "15 de outubro",
    "hora": "10h00",
    "iso": "2026-10-15T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · RESERVA DE EMERGÊNCIA · Quantos meses você aguentaria? · 12,5 meses em número grande, sobre uma fileira de 13 blocos de mês (12 cheios e o último pela metade), com as marcas 1, 6 e 12.",
        "POR QUE EM MESES · O mesmo dinheiro pode durar 10 meses ou 3. · Depende de quanto você gasta. Por isso a reserva se mede em meses de gasto, não em reais. · Cartão com duas fileiras de 12 blocos: gasta R$ 3.000 por mês, 10 meses; gasta R$ 10.000 por mês, 3 meses. · Nota: Exemplo: R$ 30.000 guardados nos dois casos. Cada bloco é um mês.",
        "A CONTA · Patrimônio dividido pela despesa média. · É a conta que o Diagnóstico do timtimcash faz. · Cartão: patrimônio R$ 104.180 ÷ despesa média por mês R$ 8.342,27 = reserva 12,5 meses. · Nota: Exemplo com a conta dos outros posts. Patrimônio: as contas incluídas no total. Média: os 12 meses anteriores, sem os meses vazios.",
        "LIQUIDEZ · Nem todo patrimônio é reserva. · Na emergência, vale o que está à mão. Dinheiro lá fora ou num imóvel pode demorar a virar dinheiro. · Barra do patrimônio: à mão R$ 44.180 (conta corrente e reserva); demora a virar dinheiro R$ 60.000 (corretora no exterior). Com tudo, 12,5 meses; só o que está à mão, 5,3 meses, abaixo da meta de 6 meses. · Nota: Exemplo: R$ 44.180 ÷ R$ 8.342,27 = 5,3 meses.",
        "NO TIMTIMCASH · O Diagnóstico mostra a sua reserva em meses. · Em Relatórios, ao lado da meta. Ela começa em 6 meses e você ajusta em “Como o diagnóstico é calculado”. · Tela real do Diagnóstico no celular: Despesas do período R$ 7.780,00 (−6,7%), sua média mensal (12m) R$ 8.342,27; Reserva, “quanto tempo o patrimônio cobre seus gastos”, 12,5 meses, meta 6m. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "E SE A RENDA PARAR? · Depois, ponha a reserva à prova. · Meses de reserva são uma média. O “E se...” da Simulação futura mostra o caminho, mês a mês. · “Perde a maior renda”: a maior receita zera nos 6 primeiros meses · Mês a mês, não pela média: os meses mais caros do cenário entram na conta · Sem alterar nada: o teste é só uma leitura sobre o seu cenário.",
        "Fechamento (fundo verde) · Saiba quantos meses você aguentaria. · Relatórios e Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Se a sua renda parasse hoje, quantos meses você aguentaria?\n\n"
        "A reserva de emergência se mede em meses, não em reais: o patrimônio dividido pela despesa média do mês. É a conta do Diagnóstico do timtimcash. "
        "No exemplo do carrossel, R$ 104.180 divididos por R$ 8.342,27 dão 12,5 meses; a meta começa em 6 meses e você ajusta.\n\n"
        "Mas nem todo patrimônio é reserva. Dinheiro investido lá fora ou num imóvel pode demorar a virar dinheiro. No mesmo exemplo, só com o que está à mão, a reserva cai para 5,3 meses.\n\n"
        "Depois, ponha a reserva à prova: na Simulação futura, o teste “Perde a maior renda” mostra, mês a mês, se o saldo aguenta.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#reservadeemergencia #educacaofinanceira #financaspessoais #controlefinanceiro #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Meio do mês, longe do fechamento: um bom momento para olhar a reserva com calma. O tema estava guardado no histórico do perfil (Diagnóstico, reserva de emergência em meses) e continua a taxa de poupança de 05/10: lá, quanto da renda sobra; aqui, quanto tempo o que você juntou aguenta. Termina no teste “Perde a maior renda” só pelo nome, sem repetir o gráfico do Reel de 30/09 nem as telas do carrossel de 21/10."),
        ("O que desperta interesse", "A pergunta da capa é pessoal e dá um frio na barriga, e o número grande com os blocos de mês se entende de longe na grade. O slide 4 traz a virada: com o mesmo patrimônio, só o que está à mão cobre 5,3 meses, abaixo da meta de 6."),
        ("Benefício para o público", "Sai do post sabendo fazer a conta da própria reserva, entendendo por que medir em meses e não em reais e separando o que é reserva do patrimônio que demora a virar dinheiro. Sem recomendação de investimento e sem regra de mercado: a meta de 6 meses é o ponto de partida do site, que a pessoa ajusta."),
        ("Como contribui para o perfil", "Conteúdo de salvar, que liga educação financeira a duas funções reais (Diagnóstico e Simulação futura), com tela real e números que batem com a conta de exemplo dos outros posts. Reforça o olhar de economista do perfil: liquidez, média e teste de estresse em linguagem simples."),
    ],
    "alt": [
        "Reserva de emergência. Quantos meses você aguentaria? Em destaque, 12,5 meses, sobre uma fileira de 13 blocos de mês: 12 cheios de verde e o último pela metade, com as marcas 1, 6 e 12.",
        "Por que em meses. O mesmo dinheiro pode durar 10 meses ou 3. Depende de quanto você gasta; por isso a reserva se mede em meses de gasto, não em reais. Quem gasta R$ 3.000 por mês tem 10 meses; quem gasta R$ 10.000 por mês tem 3 meses, com R$ 30.000 guardados nos dois casos.",
        "A conta. Patrimônio dividido pela despesa média. É a conta que o Diagnóstico do timtimcash faz. Exemplo: patrimônio de R$ 104.180 dividido por uma despesa média de R$ 8.342,27 por mês dá uma reserva de 12,5 meses. O patrimônio soma as contas incluídas no total; a média usa os 12 meses anteriores, sem os meses vazios.",
        "Liquidez. Nem todo patrimônio é reserva. Na emergência, vale o que está à mão; dinheiro lá fora ou num imóvel pode demorar a virar dinheiro. Barra do patrimônio de exemplo: R$ 44.180 à mão, na conta corrente e na reserva, e R$ 60.000 na corretora no exterior. Com tudo, 12,5 meses; só com o que está à mão, 5,3 meses, abaixo da meta de 6 meses.",
        "No timtimcash, o Diagnóstico mostra a sua reserva em meses, em Relatórios, ao lado da meta, que começa em 6 meses e se ajusta em Como o diagnóstico é calculado. Tela real no celular, com dados de exemplo: despesas do período de R$ 7.780,00, 6,7% abaixo da média mensal de 12 meses, de R$ 8.342,27; reserva, quanto tempo o patrimônio cobre seus gastos, 12,5 meses, com meta de 6 meses.",
        "E se a renda parar? Depois, ponha a reserva à prova. Meses de reserva são uma média; o E se da Simulação futura mostra o caminho, mês a mês. Perde a maior renda: a maior receita zera nos 6 primeiros meses. Mês a mês, não pela média: os meses mais caros do cenário entram na conta. Sem alterar nada: o teste é só uma leitura sobre o seu cenário.",
        "Saiba quantos meses você aguentaria. Relatórios e Simulação futura no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "gerador/telas/secoes/celular-relatorios-diagnostico.jpg · Diagnóstico de setembro 2026 no celular, recorte das linhas “Despesas do período” (R$ 7.780,00, sua média mensal (12m) R$ 8.342,27) e “Reserva” (12,5 meses, meta 6m) · slide 5",
    ],
}
