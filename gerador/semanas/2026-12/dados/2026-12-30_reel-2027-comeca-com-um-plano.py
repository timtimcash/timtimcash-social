# -*- coding: utf-8 -*-
"""Quarta 30/12/2026 · Reel "2027 começa com um plano" (produto: Simulação futura; capa verde). Equipe dr2.
Vídeo, capa e prévia gerados por equipes/dr2/reel_30.py (com assert nos números lidos da tela); telas capturadas por
equipes/dr2/captura_30.py no site build 2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular (390 × 844 em escala 3;
as fotos do resultado com a janela esticada para 1500 px, na mesma rolagem, para o saldo, o gráfico e "Plano contra realidade"
caberem numa foto), relógio da página em 30/12/2026 10:00.
Interação real, toque a toque: Simulação futura -> "Cenário base" -> mês final ("Setembro de 2027") -> "Dez" no calendário de 2027
-> "Saldo em dez/27 R$ 37.720 · +R$ 1.810 por mês · 13 meses" e o gráfico desde "Hoje" -> "Plano contra realidade" ("O plano prevê
+R$ 2.180 por mês × Aconteceu +R$ 2.464, média de 6 meses"; "Sobra R$ 284 por mês a mais que o plano previa (13% acima).") ->
"Definir uma meta" -> digita 35000 (o campo mostra 3, 35, 350, 3.500 e 35.000) -> OK -> "Meta R$ 35 mil · atinge em nov/27".
A curva do gancho usa os números da linha do tempo do site: partida R$ 14.180 (valor manual do cenário base); dez/26 R$ 16.360;
jan/27 R$ 13.740 (o cenário tem um ajuste de R$ 4.800 em Impostos e Taxas em jan/27); +R$ 2.180 por mês de fev/27 a nov/27
(R$ 35.540); dez/27 R$ 37.720. O valor na ponta da curva só mostra esses números, mês a mês (sem interpolar).
"Ajustar o plano pelo real" não foi tocado: a conta do site troca a base de cada linha pela média dos meses COM movimento nos
últimos 12 meses (a janela de confirmação diz isso), e Impostos e Taxas, que só teve movimento em jan/26 (IPVA e IPTU, R$ 1.390),
viraria R$ 1.390 por mês em 2027; o plano cairia para +R$ 1.169 por mês e R$ 25.976 em dez/27, um retrato pior que o real.
Depois da meta, o painel "Plano contra realidade" passa a dizer "Nesse ritmo real a meta de R$ 35 mil antecipa 3 meses: ago/27 no
lugar de nov/27." (fica na foto, sem destaque no vídeo): a conta usa a média real de 6 meses sem o ajuste de janeiro, então é otimista.
A simulação não calcula juros nem rendimento sobre o saldo (FUNCIONALIDADES.md): o vídeo não diz que calcula e a legenda avisa."""

POST = {
    "pasta": "2026-12-30_reel-2027-comeca-com-um-plano",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "2027 começa com um plano: na Simulação futura, o cenário levado até dezembro de 2027, o saldo projetado desde hoje, o Plano contra realidade e uma meta com o mês em que ela chega",
    "pilar": "Produto (Simulação futura) · planejamento",
    "data_longa": "quarta-feira, 30 de dezembro de 2026",
    "data_curta": "quarta-feira, 30/12/2026",
    "data_mockup": "30 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-30T10:00:00",
    "video": "saida/2026-12-30_reel-2027-comeca-com-um-plano/reel.mp4",
    "capa": "saida/2026-12-30_reel-2027-comeca-com-um-plano/capa.jpg",
    "previa": "saida/2026-12-30_reel-2027-comeca-com-um-plano/previa.mp4",
    "slides": [
        "Capa da grade (verde) · SIMULAÇÃO FUTURA · 2027 começa com um plano · “2027” grande em contorno branco, com uma curva branca subindo até um ponto acima de uma linha tracejada.",
        "0 a 2,7 s · Gancho (tinta) · SIMULAÇÃO FUTURA · Como termina o seu 2027? · Desde o primeiro quadro, a curva do saldo projetado é desenhada em menta, mês a mês, com o valor do mês na ponta: R$ 14.180 hoje, a queda de janeiro (R$ 13.740) e R$ 37.720 em dez/27.",
        "2,9 a 4,9 s · Na Simulação futura, abra o seu cenário. · Tela real com os dois cenários; anel e toque em Cenário base.",
        "5,1 a 8,5 s · Leve o plano até dezembro de 2027. · Anel e toque no mês final (“Setembro de 2027”); o calendário de 2027 abre; anel e toque em Dez; o botão passa a “Dezembro de 2027”.",
        "8,7 a 11,2 s · No plano, 2027 termina com R$ 37.720. · “Saldo em dez/27 R$ 37.720 · +R$ 1.810 por mês · 13 meses” e o gráfico desde Hoje, em anel.",
        "11,5 a 14,3 s · E a realidade? Sobrou R$ 284 por mês a mais que o plano. · “Plano contra realidade”: o plano prevê +R$ 2.180 por mês, aconteceu +R$ 2.464 (média de 6 meses); anel em “Sobra R$ 284 por mês a mais que o plano previa (13% acima).”",
        "14,6 a 18,2 s · Uma meta de R$ 35 mil: no plano, chega em nov/27. · Toque em “Definir uma meta”; na janela “Meta do cenário”, o valor entra tecla a tecla até 35.000; toque em OK; “Meta R$ 35 mil · atinge em nov/27” em anel, com a linha da meta no gráfico.",
        "18,5 a 21,3 s · Fechamento (verde) · Simulação futura no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Como termina o seu 2027?\n\n"
        "Na Simulação futura, o seu cenário projeta o saldo mês a mês, a partir de hoje. No exemplo do vídeo, o cenário base vai até "
        "dezembro de 2027 e termina com R$ 37.720, já com um ajuste de impostos em janeiro.\n\n"
        "E a realidade? Em Plano contra realidade, o site compara o que o plano previa (+R$ 2.180 por mês) com a média real dos últimos "
        "6 meses (+R$ 2.464): sobrou R$ 284 por mês a mais.\n\n"
        "Com uma meta de R$ 35 mil, o site mostra o mês em que ela chega: nov/27, no plano.\n\n"
        "A simulação projeta o saldo com as receitas e as despesas que você estima. Ela não calcula juros nem rendimento.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#planejamentofinanceiro #metasfinanceiras #financaspessoais #organizacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Quarta, 30/12, véspera do Ano-Novo (31/12 não tem post): é o último post do ano e o momento natural de planejar 2027."),
        ("O que desperta interesse", "A pergunta “Como termina o seu 2027?” com a curva do saldo sendo desenhada e o valor de cada mês na ponta, já no primeiro segundo."),
        ("Benefício para o público", "A pessoa vê como levar o plano até o fim de 2027, comparar o plano com o que de fato sobrou nos últimos meses e definir uma meta com o mês em que ela chega."),
        ("Como contribui para o perfil", "Mostra com tela real a Simulação futura, ainda inédita no perfil, e fecha dezembro com um convite a planejar, sem prometer rendimento: a simulação não calcula juros."),
    ],
    "alt": [
        "Reel de 21 segundos. Como termina o seu 2027? Uma curva verde desenha o saldo projetado mês a mês, de R$ 14.180 hoje, com uma "
        "queda em janeiro, até R$ 37.720 em dezembro de 2027. Telas reais do timtimcash no celular, com dados de exemplo. Na Simulação "
        "futura, um toque abre o Cenário base; outro toque no mês final abre o calendário de 2027, e um toque em Dez leva o plano até "
        "dezembro de 2027. O saldo em dez/27 é R$ 37.720, com o gráfico desde hoje. No painel Plano contra realidade, o plano previa mais "
        "R$ 2.180 por mês e a média real de 6 meses foi de mais R$ 2.464: sobra R$ 284 por mês a mais. Um toque em Definir uma meta, o "
        "valor de 35 mil é digitado e, depois do OK, aparece Meta R$ 35 mil, atinge em nov/27. Simulação futura no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-simulacao-1-cenarios.jpg · Simulação futura: “2 cenários · partindo de R$ 14.180,00”, Cenário base e Trocar de carro (celular 390 × 844 em escala 3, build 2026-10-16.1, relógio da página em 30/12/2026 10:00) · 2,8 a 4,6 s",
        "telas/celular-simulacao-2-cenario.jpg · Cenário base aberto, com o mês final “Setembro de 2027” (mesmo relógio) · 4,6 a 6,1 s",
        "telas/celular-simulacao-3-meses.jpg · o calendário de 2027 aberto pelo toque no mês final, com Set marcado · 6,1 a 7,4 s",
        "telas/celular-simulacao-4-dezembro.jpg · depois do toque em Dez: “Dezembro de 2027” · 7,4 a 8,6 s",
        "telas/celular-simulacao-5-resultado.jpg · a mesma página rolada até o resultado (janela de 1500 px): “Saldo em dez/27 R$ 37.720”, o gráfico desde Hoje, “E se…”, “Plano contra realidade” e a linha do tempo · 8,5 a 15,1 s",
        "telas/celular-simulacao-6-meta-0.jpg a celular-simulacao-6-meta-5.jpg · a janela “Meta do cenário” vazia e depois de cada tecla (3, 35, 350, 3.500, 35.000) · 15,1 a 16,6 s",
        "telas/celular-simulacao-6-meta.jpg · a mesma janela com 35.000, antes do OK (conferência das caixas) · não aparece no vídeo",
        "telas/celular-simulacao-7-meta-ok.jpg · depois do OK: “Meta R$ 35 mil · atinge em nov/27” e a linha “meta R$ 35 mil” no gráfico (janela de 1500 px, mesma rolagem) · 16,6 a 18,6 s",
        "telas/caixas.json · posições medidas na captura (com a rolagem de cada foto), o texto de cada tela e o valor do campo a cada tecla",
    ],
}
