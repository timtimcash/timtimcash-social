# -*- coding: utf-8 -*-
"""Quarta 10/02/2027 · Reel "Quanto custou o seu Carnaval?" (Carnaval e produto: busca de Transações e Contas e carteiras; capa tinta).
Equipe fr. Segundo da dupla com o Reel de 05/02 ("O envelope do Carnaval"): o mesmo envelope desenhado, agora depois da folia.
Vídeo, capa e prévia gerados por equipes/fr/reel_10.py (assert nos números lidos da tela); telas capturadas por
equipes/fr/captura_10.py no site build 2026-10-19.5, na conta de base (J/base_app, sem mudança), no celular (390 px em escala 3),
relógio da página em 10/02/2027 10:00, tudo pela interface:
- Transações (Fevereiro 2027): toque na busca e "carnaval" digitado letra a letra, uma foto real depois de cada letra. O resumo muda a
  cada letra: antes, "21 transações · 17 pagas · 4 pendentes · 815 no histórico"; "c", 17 transações (R$ 7.668,00); "ca", 11
  (R$ 6.535,80); "car" em diante, "5 transações · 5 pagas · 0 pendentes · somam R$ 454,80 · 815 no histórico". As 5 linhas trazem
  "· Carteira do Carnaval": lanche no bloco R$ 48,00 (09/02), transporte R$ 72,40 (08/02), comida R$ 64,50 (07/02), ingresso de festa
  R$ 180,00 (06/02) e fantasia R$ 89,90 (04/02);
- Menu › "Contas e carteiras": "Carteira do Carnaval · Dinheiro / Carteira · No total · R$ 45,20".
Conta: 89,90 + 180,00 + 64,50 + 72,40 + 48,00 = 454,80; 500,00 − 454,80 = 45,20.
O recibo desenhado do gancho usa os mesmos 5 gastos, com nomes curtos (as descrições inteiras estão na tela real).
Diferença do Reel de 04/11 (busca e soma da farmácia, gancho em tinta com o campo branco, o odômetro e os quadradinhos): aqui a história
é o envelope que segurou o Carnaval. A digitação aparece de outro jeito: no gancho, em teclas que se apertam uma a uma, com um recibo
que se imprime; na tela real, uma tecla desenhada salta sobre cada letra digitada e a lista encolhe de 21 para 5 lançamentos."""

POST = {
    "pasta": "2027-02-10_reel-quanto-custou-o-carnaval",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 18 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 18 s",
    "tema": "Quanto custou o seu Carnaval: a busca por “carnaval” em Transações junta os 5 gastos da folia (R$ 454,80), todos pagos com a Carteira do Carnaval; dos R$ 500 do envelope, sobraram R$ 45,20",
    "pilar": "Carnaval · produto (busca em Transações, Contas e carteiras)",
    "data_longa": "quarta-feira, 10 de fevereiro de 2027",
    "data_curta": "quarta-feira, 10/02/2027",
    "data_mockup": "10 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-10T10:00:00",
    "video": "saida/2027-02-10_reel-quanto-custou-o-carnaval/reel.mp4",
    "capa": "saida/2027-02-10_reel-quanto-custou-o-carnaval/capa.jpg",
    "previa": "saida/2027-02-10_reel-quanto-custou-o-carnaval/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · CARNAVAL · Quanto custou a folia? (“a folia?” em menta) · O mesmo envelope do Reel de 05/02, em traço menta e fechado, com “sobraram R$ 45,20” escrito nele; acima, três pílulas de gasto saindo (−89,90, −180,00, −64,50).",
        "0 a 2,8 s · Gancho (verde suave) · DEPOIS DO CARNAVAL · Quanto custou o seu Carnaval? · Desde o primeiro quadro, as teclas c, a, r, n, a, v, a, l se apertam uma a uma, um recibo imprime os 5 gastos (04/02 Fantasia 89,90; 06/02 Ingresso da festa 180,00; 07/02 Comida 64,50; 08/02 Transporte 72,40; 09/02 Lanche no bloco 48,00) e o total sobe até R$ 454,80 (em 0,5 s); “5 gastos com “carnaval””.",
        "2,9 a 5,0 s · Em Transações, busque “carnaval”. · Tela real de Transações no celular (10/02/2027): toque na busca e “carnaval” digitado letra a letra (uma foto real por letra), com uma tecla desenhada que salta sobre cada letra; o resumo encolhe de 21 para 17, 11 e 5 transações. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "5,1 a 7,1 s · 5 gastos, que somam R$ 454,80. · Anel em “5 transações · 5 pagas · 0 pendentes · somam R$ 454,80”.",
        "7,3 a 9,5 s · Todos pagos com a Carteira do Carnaval. · A lista desce pelas 5 linhas; um anel em cada “· Carteira do Carnaval”.",
        "9,6 a 11,8 s · Na carteira, sobraram R$ 45,20. · Tela real de Contas e carteiras; anel em “Carteira do Carnaval · Dinheiro / Carteira · R$ 45,20”.",
        "12,0 a 15,1 s · O envelope segurou o Carnaval. · O mesmo envelope do Reel de 05/02: os 5 gastos saem dele em pílulas (−R$ 89,90, −R$ 180,00, −R$ 64,50, −R$ 72,40, −R$ 48,00) e o valor vai de R$ 500,00 a R$ 45,20; embaixo, “R$ 500 − R$ 454,80 = R$ 45,20”.",
        "15,1 a 17,9 s · Fechamento (verde) · Transações no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Quanto custou o seu Carnaval?\n\n"
        "No exemplo do vídeo, a busca por “carnaval” em Transações encontra 5 gastos: fantasia, ingresso da festa, comida, transporte e "
        "lanche no bloco. Somam R$ 454,80, e a soma aparece no topo da lista. A cada letra digitada, a lista já encolhe.\n\n"
        "Os 5 saíram da Carteira do Carnaval, a conta que recebeu R$ 500 antes da folia. Sobraram R$ 45,20: o envelope segurou.\n\n"
        "O que sobrou pode voltar para a conta corrente ou para a reserva, com outra transferência.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#carnaval #controledegastos #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Quarta-feira depois do Carnaval: é quando bate a curiosidade (e o medo) de saber quanto a folia custou."),
        ("O que desperta interesse", "A pergunta que todo mundo faz nesse dia, com a palavra sendo digitada e o total de R$ 454,80 já no primeiro segundo, num recibo que se imprime."),
        ("Benefício para o público", "Vê como juntar os gastos de um evento com uma busca e como um teto separado numa conta segura o gasto: dos R$ 500, sobraram R$ 45,20."),
        ("Como contribui para o perfil", "Fecha a dupla com o Reel de 05/02 com o mesmo envelope desenhado e mostra com tela real a busca de Transações, com outra animação da digitação."),
    ],
    "alt": [
        "Reel de 18 segundos. Em fundo verde-claro, a pergunta Quanto custou o seu Carnaval?, com teclas que se apertam formando a palavra carnaval, "
        "um recibo com os 5 gastos da folia e o total, R$ 454,80. Depois, telas reais do timtimcash no celular, com dados de exemplo: em Transações, a "
        "palavra carnaval é digitada na busca, letra a letra, e a lista encolhe até 5 transações, que somam R$ 454,80. As 5 linhas mostram que os gastos "
        "saíram da Carteira do Carnaval, e em Contas e carteiras a carteira tem R$ 45,20. No fim, um envelope desenhado de onde saem os 5 gastos: de R$ 500, "
        "sobraram R$ 45,20. O envelope segurou o Carnaval. Transações no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-transacoes-fevereiro.png e celular-transacoes-busca-tocada.png · Transações no celular, Fevereiro 2027 (site build 2026-10-19.5, conta de base, relógio em 10/02/2027 10:00), antes e depois do toque na busca: 21 transações · 17 pagas · 4 pendentes · 815 no histórico · 2,9 a 3,8 s",
        "telas/celular-transacoes-digitando-01.png a celular-transacoes-digitando-08.png · a busca letra a letra, de c a carnaval (17, 11 e depois 5 transações) · 3,8 a 7,2 s",
        "telas/celular-transacoes-busca-carnaval-alta.png · a mesma tela com carnaval, numa janela alta: as 5 linhas, todas com Carteira do Carnaval · 7,2 a 9,6 s",
        "telas/celular-contas-e-carteiras.png · Contas e carteiras, aberta pelo menu: Carteira do Carnaval, R$ 45,20 · 9,6 a 11,8 s",
        "telas/caixas.json · posições medidas na captura (o campo de busca, a posição de cada letra, o resumo, as linhas) e o texto de cada tela, usados nos anéis, nas teclas e nos assert do roteiro",
    ],
}
