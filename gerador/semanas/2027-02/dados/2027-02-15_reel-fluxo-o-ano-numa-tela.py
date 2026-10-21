# -*- coding: utf-8 -*-
"""Segunda 15/02/2027 · Reel "Entrou, saiu, guardou" (produto: Fluxo, o ano numa tela; capa tinta). Equipe fr.
Vídeo, capa e prévia gerados por equipes/fr/reel_15.py (assert nos números lidos da tela); telas capturadas por
equipes/fr/captura_15.py no site build 2026-10-19.5, na conta de base (J/base_app, sem mudança), no celular (390 px em escala 3),
relógio da página em 15/02/2027 10:00, tudo pela interface: Fluxo › toque no período › "Ou digite o período": De 01/03/2026,
Até 28/02/2027 › "Aplicar". São os mesmos 12 meses do gráfico "Fluxo detalhado" (Mar/26 a Fev/27, o padrão do gráfico); fevereiro
vai até o dia 15 ("até 15/02"), e só entram lançamentos pagos ou recebidos.
Números da tela: "Resultado · 1 mar 2026 - 28 fev 2027 até 15/02" R$ 25.012,76; "Guardou 19,7% do que entrou"; "Entrou" R$ 127.253,36
(15 recebidas); "Saiu" R$ 102.240,60 (307 pagas); barra "20%" e "80% saiu"; "Fluxo detalhado": Receitas R$ 127.253, Despesas
R$ 102.240, Resultado R$ 25.012, "+R$ 25.012 em 12 meses · média de R$ 2.084 por mês"; "Top saídas": Casa R$ 29.836,80 (29%),
Mercado R$ 19.522,42 (19%), Educação R$ 18.626,00 (18%), Transporte R$ 12.889,29 (13%), Bares e restaurantes R$ 7.274,90 (7%);
"Resumo mensal" de Mar de 2026 a Fev de 2027 e "Total do período" R$ 127.253,36, −R$ 102.240,60, R$ 25.012,76 e saldo R$ 115.627,76
(no celular, a tabela rola para o lado: o vídeo mostra o arraste que revela "Resultado" e "Saldo").
Conta: 127.253,36 − 102.240,60 = 25.012,76; 25.012,76 ÷ 127.253,36 = 19,66%. O desenho do fecho usa as entradas e saídas de cada mês
do "Resumo mensal" (12 meses) e 4 meses futuros em traço, sem valor.
Diferença do que já saiu: o Fluxo ainda não apareceu no perfil (a pauta o lista entre as funções novas de fevereiro). 26/11 e 06/12
falaram do ano por outros caminhos (taxa de poupança e 5 números de 2026); aqui são os 12 meses até hoje numa tela, no Fluxo."""

POST = {
    "pasta": "2027-02-15_reel-fluxo-o-ano-numa-tela",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Entrou, saiu, guardou: no Fluxo, os últimos 12 meses numa tela (entraram R$ 127.253,36, saíram R$ 102.240,60, ficaram R$ 25.012,76, 19,7% do que entrou), com o gráfico mês a mês, as maiores saídas e o Resumo mensal; o futuro fica na Simulação futura",
    "pilar": "Produto (Fluxo) · organização",
    "data_longa": "segunda-feira, 15 de fevereiro de 2027",
    "data_curta": "segunda-feira, 15/02/2027",
    "data_mockup": "15 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-15T10:00:00",
    "video": "saida/2027-02-15_reel-fluxo-o-ano-numa-tela/reel.mp4",
    "capa": "saida/2027-02-15_reel-fluxo-o-ano-numa-tela/capa.jpg",
    "previa": "saida/2027-02-15_reel-fluxo-o-ano-numa-tela/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · FLUXO · 12 MESES · Entrou, saiu, guardou. (“guardou.” em menta) · “19,7%” enorme em menta, com “guardado”, e uma barra dividida: menta (guardou) e coral (saiu).",
        "0 a 2,8 s · Gancho (papel) · FLUXO · ÚLTIMOS 12 MESES · Entrou, saiu, guardou. · Desde o primeiro quadro, três contadores: Entrou R$ 127.253,36 (verde), Saiu R$ 102.240,60 (coral) e Guardou R$ 25.012,76, com a pílula “19,7% do que entrou”; a barra se divide em 20% guardou e 80% saiu.",
        "2,9 a 5,3 s · Em Fluxo, os últimos 12 meses. · Tela real do calendário do Fluxo no celular (15/02/2027): anel em De 01/03/2026 e Até 28/02/2027, toque em Aplicar; anel no período “1 mar 2026 - 28 fev 2027”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "5,5 a 7,8 s · Guardou 19,7% do que entrou. · O cartão do período: anel em “Guardou 19,7% do que entrou” e depois na barra “20%” e “80% saiu”.",
        "7,9 a 10,2 s · Mês a mês: receitas, despesas e o resultado. · A câmera desce até o “Fluxo detalhado” (barras de receitas e despesas, linha do resultado, área do saldo); anel no gráfico.",
        "10,4 a 12,7 s · Para onde foi: Top saídas. · Anel em Casa (R$ 29.836,80), Mercado (R$ 19.522,42) e Educação (R$ 18.626,00).",
        "12,8 a 15,4 s · E o Resumo mensal, mês a mês. · A tabela de março de 2026 a fevereiro de 2027; um dedo arrasta a tabela para o lado e aparecem Resultado e Saldo; anel no “Total do período” (R$ 25.012,76 e R$ 115.627,76).",
        "15,6 a 18,1 s · O Fluxo mostra o que já aconteceu. O futuro fica na Simulação futura. · Desenho: os 12 meses (entradas em verde e saídas em coral, do Resumo mensal), a linha “Hoje” e quatro meses em traço; “Fluxo, o que já entrou e saiu” e “Simulação futura, o que vem”.",
        "18,1 a 20,9 s · Fechamento (verde) · Fluxo no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Entrou, saiu, guardou: o seu ano numa tela.\n\n"
        "No exemplo do vídeo, de março de 2026 até 15 de fevereiro de 2027, entraram R$ 127.253,36 e saíram R$ 102.240,60. Ficaram "
        "R$ 25.012,76: 19,7% do que entrou.\n\n"
        "No Fluxo, isso aparece num cartão, no gráfico Fluxo detalhado (receitas e despesas em barras, o resultado em linha e o saldo "
        "acumulado), nas maiores entradas e saídas e no Resumo mensal, mês a mês. Para ver 12 meses, escolha o período no calendário: "
        "aqui, de 01/03/2026 a 28/02/2027.\n\n"
        "O Fluxo mostra o que já aconteceu: só entram lançamentos pagos ou recebidos. O futuro fica na Simulação futura.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#fluxodecaixa #controlefinanceiro #organizacaofinanceira #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Metade de fevereiro, depois das contas pesadas de janeiro: bom momento para olhar os últimos 12 meses inteiros e ver o que sobrou."),
        ("O que desperta interesse", "Três palavras que resumem o dinheiro de qualquer pessoa e três números que chegam já no primeiro segundo, com a barra que mostra quanto ficou."),
        ("Benefício para o público", "Aprende a ler o próprio ano numa tela: quanto entrou, quanto saiu, quanto ficou (a taxa de poupança), em que meses e para onde foi."),
        ("Como contribui para o perfil", "Apresenta o Fluxo, função que ainda não tinha aparecido no perfil, com tela real e o gesto de arrastar a tabela, e separa bem o passado (Fluxo) do futuro (Simulação futura)."),
    ],
    "alt": [
        "Reel de 21 segundos. Em fundo claro, a frase Entrou, saiu, guardou, com três números que sobem: entrou R$ 127.253,36, saiu R$ 102.240,60 e guardou "
        "R$ 25.012,76, 19,7% do que entrou, e uma barra que se divide em 20% guardou e 80% saiu. Depois, telas reais do timtimcash no celular, com dados de exemplo: "
        "no Fluxo, o período de 01/03/2026 a 28/02/2027 digitado no calendário e aplicado; o cartão com Guardou 19,7% do que entrou; o gráfico Fluxo detalhado, mês a mês; "
        "as maiores saídas, Casa, Mercado e Educação; e o Resumo mensal, arrastado para o lado até o total do período. No fim, um desenho com os 12 meses que já "
        "aconteceram, a linha Hoje e os meses que vêm em traço: o Fluxo mostra o que já aconteceu, e o futuro fica na Simulação futura. Fluxo no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-periodo-12-meses.png · o calendário do Fluxo no celular com De 01/03/2026 e Até 28/02/2027 digitados (site build 2026-10-19.5, conta de base, relógio em 15/02/2027 10:00) · 2,9 a 4,2 s",
        "telas/celular-fluxo-12-meses-alta.png · o Fluxo com 1 mar 2026 - 28 fev 2027 (até 15/02), numa janela alta: cartão do período, Fluxo detalhado, Top entradas, Top saídas e Resumo mensal · 4,2 a 14,2 s",
        "telas/celular-fluxo-12-meses-alta-tabela-arrastada.png · a mesma tela com o Resumo mensal arrastado para o lado (Resultado e Saldo) · 14,2 a 15,4 s",
        "telas/celular-fluxo-fevereiro.png e celular-fluxo-12-meses.png · o Fluxo no mês (Fevereiro 2027, até o dia 15) e o topo da tela de 12 meses · conferência, não aparecem no vídeo",
        "telas/caixas.json · posições medidas na captura e o texto de cada tela, usados nos anéis, no toque, no arraste e nos assert do roteiro",
    ],
}
