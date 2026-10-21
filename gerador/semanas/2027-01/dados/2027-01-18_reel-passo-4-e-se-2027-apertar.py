# -*- coding: utf-8 -*-
"""Segunda 18/01/2027 · Reel "E se 2027 apertar?" · série Comece 2027, passo 4 de 4 (a rota) · capa tinta · equipe js.
Vídeo, capa e prévia gerados por equipes/js/reel_18.py (com assert nos números lidos da tela); telas capturadas por
equipes/js/captura_18.py no site build 2026-10-19.5, na conta de base (J/base_app, sem mudança), no celular (390 px em escala 3;
as fotos do resultado com a janela de 1000 px de altura, na mesma rolagem), relógio da página em 18/01/2027 10:00.
Interação real, toque a toque: Simulação futura ("2 cenários · partindo de R$ 14.180,00") -> "Cenário base" -> o resultado
("Saldo em set/27 R$ 29.000 · +R$ 1.646 por mês · 9 meses") -> "E se…" -> "Receita −10%" ("O saldo final cai R$ 8.964 (31%), de
R$ 29.000 para R$ 20.036.") -> "Inflação 5% a.a." ("O saldo final cai R$ 1.152 (4%), de R$ 29.000 para R$ 27.847.") -> "Remover susto"
(volta "Testa um susto sobre o cenário, sem alterar nada."). O saldo do topo fica em R$ 29.000 nas cinco fotos.
O gancho desenha o saldo do cenário com a linha do tempo do site (partida R$ 14.180; jan/27 R$ 11.560, com o ajuste de R$ 4.800 em
impostos que o cenário já tem; +R$ 2.180 por mês; ago/27 R$ 26.820; set/27 R$ 29.000) e a linha do susto "Receita −10%", calculada como
o site (receita de R$ 8.964 por mês: jan/27 R$ 10.564, +R$ 1.184 por mês, set/27 R$ 20.036; a mesma queda de R$ 8.964 do site).
O site arredonda os saldos (R$ 29.000 − R$ 27.847 = R$ 1.153, e ele diz "cai R$ 1.152"); o vídeo e a legenda usam só os saldos finais e os
percentuais (31% e 4%), como o site os mostra.
Selo e sobretítulo da série: equipes/ja/selo_comece2027.py (selo(4) e sobretitulo(4)), importados do arquivo da equipe ja.
A simulação não calcula juros nem rendimento sobre o saldo (FUNCIONALIDADES.md): a legenda avisa."""

POST = {
    "pasta": "2027-01-18_reel-passo-4-e-se-2027-apertar",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Comece 2027, passo 4 de 4 (a rota): na Simulação futura, o \"E se…\" testa um susto sobre o cenário sem alterar nada; com a receita 10% menor ou a inflação de 5% ao ano, quanto sobra em set/27",
    "pilar": "Série Comece 2027 · produto (Simulação futura) · planejamento",
    "data_longa": "segunda-feira, 18 de janeiro de 2027",
    "data_curta": "segunda-feira, 18/01/2027",
    "data_mockup": "18 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-18T10:00:00",
    "video": "saida/2027-01-18_reel-passo-4-e-se-2027-apertar/reel.mp4",
    "capa": "saida/2027-01-18_reel-passo-4-e-se-2027-apertar/capa.jpg",
    "previa": "saida/2027-01-18_reel-passo-4-e-se-2027-apertar/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · COMECE 2027 · PASSO 4 DE 4 · E se 2027 apertar? · O selo 4 da série (quadrado com o 4 em menta) e um gráfico: a linha do plano em menta até R$ 29.000 e a do susto, tracejada em âmbar, até R$ 20.036.",
        "0 a 2,6 s · Gancho (tinta) · COMECE 2027 · PASSO 4 DE 4, com o selo 4 · E se 2027 apertar? · Desde o primeiro quadro, a linha do saldo projetado sobe até R$ 29.000 em set/27; a linha tracejada do susto “Receita −10%” se descola e derruba o fim, com o valor caindo até R$ 20.036.",
        "2,9 a 5,0 s · Passo 4: na Simulação futura, abra o seu cenário. · Tela real com os dois cenários; anel e toque em Cenário base.",
        "5,2 a 7,4 s · No plano, setembro de 2027 chega com R$ 29.000. · O resultado do cenário em anel: “Saldo em set/27 R$ 29.000 · +R$ 1.646 por mês · 9 meses”, com o gráfico desde Hoje.",
        "7,6 a 10,4 s · E se a receita cair 10%? O saldo final cai para R$ 20.036. · Toque em “Receita −10%”: a linha tracejada “com o susto” aparece no gráfico e a caixa “O saldo final cai R$ 8.964 (31%), de R$ 29.000 para R$ 20.036.” fica em anel âmbar.",
        "10,6 a 13,3 s · E se a inflação for de 5% ao ano? O saldo final cai para R$ 27.847. · Toque em “Inflação 5% a.a.”: “O saldo final cai R$ 1.152 (4%), de R$ 29.000 para R$ 27.847.”",
        "13,5 a 15,6 s · O susto é só um teste: o plano não muda. · Toque em “Remover susto”: o gráfico volta ao cenário de antes, com a frase do site em anel (“Testa um susto sobre o cenário, sem alterar nada.”).",
        "15,9 a 18,6 s · O mesmo plano, três finais. · Saldo em set/27, no exemplo, em barras: Cenário base R$ 29.000; Receita −10% R$ 20.036 (−31%); Inflação 5% a.a. R$ 27.847 (−4%).",
        "18,7 a 21,4 s · Fechamento (verde) · Passo 4: a rota. · Simulação futura no timtimcash. Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "E se 2027 apertar? O passo 4 de 4 da série Comece 2027: a rota.\n\n"
        "Na Simulação futura, o seu cenário projeta o saldo mês a mês. No exemplo do vídeo, o Cenário base chega a setembro de 2027 "
        "com R$ 29.000.\n\n"
        "Em “E se…”, um toque testa um susto. Com a receita 10% menor, o saldo final cai para R$ 20.036 (31% a menos). Com inflação "
        "de 5% ao ano nas despesas, cai para R$ 27.847 (4% a menos). O susto é só um teste: o plano não muda, e um toque em “Remover susto” "
        "traz tudo de volta.\n\n"
        "O passo da semana: abra a sua simulação e teste um susto antes que ele chegue. Saber o tamanho do aperto ajuda a decidir hoje "
        "quanto guardar. A simulação usa as receitas e as despesas que você estima; ela não calcula juros nem rendimento.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#planejamentofinanceiro #organizacaofinanceira #financaspessoais #controlefinanceiro #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Segunda, 18/01: o último passo da série Comece 2027, aberta em 02/01. Depois do retrato (04/01), do caminho (10/01) e dos limites (14/01), a rota. Na conta de exemplo, o IPVA vence nesta semana (20/01), e o começo do ano mostra que o orçamento pode apertar; o sábado 30/01 fecha a série com a revisão semanal."),
        ("O que desperta interesse", "A pergunta “E se 2027 apertar?” com a linha do saldo projetado caindo na tela já no primeiro segundo, de R$ 29.000 para R$ 20.036."),
        ("Benefício para o público", "A pessoa mede o tamanho de um aperto (renda menor, inflação maior) antes que ele aconteça, num toque e sem mexer no plano, e sai com um número para decidir quanto guardar."),
        ("Como contribui para o perfil", "Fecha os 4 passos com uma função forte e pouco mostrada (o “E se…” da Simulação futura), com testes diferentes do “Perde a maior renda” de 21/10 e sem repetir a meta de 30/12, e mantém o selo da série na grade."),
    ],
    "alt": [
        "Reel de 21 segundos. Comece 2027, passo 4 de 4. E se 2027 apertar? Uma linha verde mostra o saldo projetado subindo até "
        "R$ 29.000 em setembro de 2027; uma linha tracejada âmbar, com a receita 10% menor, termina em R$ 20.036. Telas reais do "
        "timtimcash no celular, com dados de exemplo. Na Simulação futura, um toque abre o Cenário base: saldo em set/27 de R$ 29.000, "
        "mais R$ 1.646 por mês em 9 meses. Em E se, um toque em Receita menos 10% mostra que o saldo final cai R$ 8.964, 31%, para "
        "R$ 20.036; um toque em Inflação 5% ao ano mostra a queda para R$ 27.847, 4%. O susto é só um teste: o plano não muda; um toque em "
        "Remover susto volta ao cenário de antes. Um quadro resume os três finais em setembro de 2027. Passo 4: a rota. Simulação futura no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-simulacao-1-cenarios.jpg · Simulação futura: “2 cenários · partindo de R$ 14.180,00”, Cenário base (R$ 29 mil, +105%, até set/27) e Trocar de carro (celular 390 × 760 em escala 3, build 2026-10-19.5, relógio da página em 18/01/2027 10:00) · 2,7 a 4,6 s",
        "telas/celular-simulacao-2-resultado.jpg · o Cenário base rolado até o resultado (janela de 1000 px): “Saldo em set/27 R$ 29.000 · +R$ 1.646 por mês · 9 meses”, o gráfico desde Hoje e “E se…” (mesmo relógio) · 4,6 a 8,3 s",
        "telas/celular-simulacao-3-receita.jpg · depois do toque em “Receita −10%”: a linha “com o susto” e “O saldo final cai R$ 8.964 (31%), de R$ 29.000 para R$ 20.036.” · 8,3 a 11,1 s",
        "telas/celular-simulacao-4-inflacao.jpg · depois do toque em “Inflação 5% a.a.”: “O saldo final cai R$ 1.152 (4%), de R$ 29.000 para R$ 27.847.” · 11,1 a 14,0 s",
        "telas/celular-simulacao-5-sem-susto.jpg · depois do toque em “Remover susto”: o cenário de antes, com “Testa um susto sobre o cenário, sem alterar nada.” · 14,0 a 15,7 s",
        "telas/caixas.json · posições medidas na captura (com a rolagem de cada foto), o texto do resultado e do “E se…” em cada foto e a linha do tempo do cenário, usados nos anéis e nos assert do roteiro",
    ],
}
