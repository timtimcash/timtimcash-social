# -*- coding: utf-8 -*-
"""Domingo 27/12/2026 · Reel "O que mudou no seu dezembro" (produto: Relatórios; capa verde suave). Equipe dr2.
A pasta mantém o nome da pauta (o-que-mudou-no-seu-ano), mas o título virou "O que mudou no seu dezembro": a pauta deixava escolher
o período que contasse uma boa história ("dezembro contra a média, ou o ano"), e dezembro contra a média de 12 meses conta uma história clara
e honesta (no ano, os desvios são pequenos: Lazer e hobbies −10%, Saúde −10%, Compras +55%, Roupas novo; e "Maiores variações"
do ano compara com jan/25 a dez/25, quando a conta de exemplo só começa em out/25).
Vídeo, capa e prévia gerados por equipes/dr2/reel_27.py (com assert nos números lidos da tela); telas capturadas por
equipes/dr2/captura_27.py no site build 2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular (390 px em escala 3,
janela de 1300 px de altura), relógio da página em 27/12/2026 10:00, período Dezembro 2026 (o que a tela abre).
Interação real: Relatórios (topo) -> toque em "O que mudou" no índice do relatório (a página rola até o painel; no vídeo, a câmera
desce pela foto do topo e troca para a foto depois da rolagem, com o mesmo painel no mesmo lugar) -> "Variações" no índice
("Maiores variações").
Números da tela, "O que mudou · Maiores desvios em relação à sua média de 12 meses": Presentes e doações, média R$ 96,67, agora
R$ 972,40, +R$ 875,73, +906% (10,1x); Mercado, média R$ 1.550,07, agora R$ 1.992,00, +R$ 441,93, +29%; Lazer e hobbies, média
R$ 403,60, agora R$ 92,00, −R$ 311,60, −77%; Compras, +R$ 305,08, +556% (6,6x). Os três maiores desvios em R$ são os das setas.
"Maiores variações · Despesas por categoria · Dezembro 2026 vs 1 nov - 27 nov": Presentes e doações novo, Roupas novo, Mercado +35%,
Transporte −1%, Compras −45%, Bares e restaurantes −52%, Lazer e hobbies −70%.
As setas do gancho e do resumo são desenhadas a partir da linha da média, com o comprimento proporcional ao desvio em R$."""

POST = {
    "pasta": "2026-12-27_reel-o-que-mudou-no-seu-ano",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 22 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 22 s",
    "tema": "O que mudou no seu dezembro: em Relatórios, O que mudou mostra os maiores desvios da média de 12 meses (presentes, mercado e lazer) e Maiores variações compara com novembro até o mesmo dia",
    "pilar": "Produto (Relatórios) · fim de ano",
    "data_longa": "domingo, 27 de dezembro de 2026",
    "data_curta": "domingo, 27/12/2026",
    "data_mockup": "27 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-27T10:00:00",
    "video": "saida/2026-12-27_reel-o-que-mudou-no-seu-ano/reel.mp4",
    "capa": "saida/2026-12-27_reel-o-que-mudou-no-seu-ano/capa.jpg",
    "previa": "saida/2026-12-27_reel-o-que-mudou-no-seu-ano/previa.mp4",
    "slides": [
        "Capa da grade (verde suave) · RELATÓRIOS · O que mudou no seu dezembro · Três setas a partir de uma linha tracejada: duas para cima em coral e uma para baixo em verde.",
        "0 a 2,6 s · Gancho (papel) · RELATÓRIOS · O que fugiu do normal no seu dezembro? · Desde o primeiro quadro, três setas crescem a partir da linha “sua média”: Presentes +R$ 875,73 e Mercado +R$ 441,93 (coral, para cima), Lazer −R$ 311,60 (verde, para baixo).",
        "2,9 a 5,1 s · Em Relatórios, toque em O que mudou. · Tela real do topo de Relatórios (Diagnóstico de dezembro 2026); anel e toque em “O que mudou” no índice; a página rola até o painel.",
        "5,4 a 7,6 s · Presentes: 10,1 vezes a média dos últimos 12 meses. · Painel “O que mudou”; anel em “Presentes e doações · média R$ 96,67 · agora R$ 972,40 · +R$ 875,73 · +906% (10,1x)”.",
        "7,8 a 10,0 s · Mercado: +R$ 441,93 acima da média. · Anel em “Mercado · média R$ 1.550,07 · agora R$ 1.992,00 · +R$ 441,93 · +29%”.",
        "10,2 a 12,1 s · Lazer: −77%, bem abaixo da média. · Anel verde em “Lazer e hobbies · média R$ 403,60 · agora R$ 92,00 · −R$ 311,60 · −77%”.",
        "12,5 a 15,0 s · Contra novembro, até o dia 27: presentes e roupas são novos. · Painel “Maiores variações” (Dezembro 2026 vs 1 a 27 de novembro), com anel em Presentes e doações e Roupas, “novo”.",
        "15,2 a 18,7 s · Cena em tinta · Antes de virar o ano, veja o que mudou. · As três setas de novo, com os valores.",
        "18,7 a 21,5 s · Fechamento (verde) · Relatórios no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "O que fugiu do normal no seu dezembro?\n\n"
        "Em Relatórios, o painel O que mudou compara o mês com a sua média dos últimos 12 meses e mostra os maiores desvios. "
        "No exemplo do vídeo, com dezembro ainda em curso:\n\n"
        "Presentes e doações: R$ 972,40, contra uma média de R$ 96,67. São +R$ 875,73, 10,1 vezes a média.\n"
        "Mercado: R$ 441,93 acima da média (+29%).\n"
        "Lazer e hobbies: R$ 311,60 abaixo da média (−77%).\n\n"
        "Em Maiores variações, contra novembro até o mesmo dia, presentes e roupas aparecem como novos.\n\n"
        "Antes de virar o ano, veja o que mudou e o que vale levar para 2027.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#financaspessoais #controlefinanceiro #organizacaofinanceira #fimdeano #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Domingo, 27/12, entre o Natal e o Ano-Novo: dezembro é o mês que mais foge da rotina (presentes, ceia, festas), e esta é a hora de olhar o que mudou antes de virar o ano."),
        ("O que desperta interesse", "A pergunta e as três setas com os valores já no primeiro segundo; o salto dos presentes, 10,1 vezes a média, é fácil de reconhecer na própria vida."),
        ("Benefício para o público", "A pessoa aprende a achar em segundos o que fugiu do normal, com O que mudou (contra a média de 12 meses) e Maiores variações (contra o mês anterior até o mesmo dia)."),
        ("Como contribui para o perfil", "Mostra com tela real dois painéis de Relatórios ainda inéditos no perfil e fecha a linha sazonal de dezembro com um olhar de retrospectiva, sem julgar os gastos."),
    ],
    "alt": [
        "Reel de 22 segundos. O que fugiu do normal no seu dezembro? Três setas saem da linha da média: Presentes, mais R$ 875,73, e "
        "Mercado, mais R$ 441,93, para cima em coral; Lazer, menos R$ 311,60, para baixo em verde. Telas reais do timtimcash no celular, "
        "com dados de exemplo. Em Relatórios, um toque em O que mudou leva ao painel dos maiores desvios em relação à média de 12 meses: "
        "Presentes e doações, R$ 972,40 contra a média de R$ 96,67, 10,1 vezes a média; Mercado, mais R$ 441,93, mais 29%; Lazer e hobbies, "
        "menos R$ 311,60, menos 77%. No painel Maiores variações, contra novembro até o dia 27, presentes e roupas aparecem como novos. "
        "Antes de virar o ano, veja o que mudou. Relatórios no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-relatorios-1-topo.jpg · Relatórios, topo da página: índice do relatório, “Diagnóstico de dezembro 2026” e “O que mudou” mais abaixo (celular 390 px em escala 3, janela de 1300 px de altura, build 2026-10-16.1, relógio da página em 27/12/2026 10:00, período Dezembro 2026) · 2,8 a 5,3 s",
        "telas/celular-relatorios-2-o-que-mudou.jpg · depois do toque em “O que mudou” no índice: a página rolada até o painel, com o índice preso no alto e “O que mudou” marcado (mesmo relógio) · 5,3 a 12,6 s",
        "telas/celular-relatorios-3-maiores-variacoes.jpg · depois do toque em “Variações” no índice: “Maiores variações · Despesas por categoria · Dezembro 2026 vs 1 nov - 27 nov” (mesmo relógio) · 12,4 a 15,4 s",
        "telas/caixas.json · posições medidas na captura (índice, painéis e linhas, com a rolagem de cada foto) e o texto dos painéis, usados nos anéis e nos assert do roteiro",
    ],
}
