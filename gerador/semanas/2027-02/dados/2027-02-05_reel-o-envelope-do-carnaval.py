# -*- coding: utf-8 -*-
"""Sexta 05/02/2027 · Reel "O envelope do Carnaval" (Carnaval e produto: Contas e carteiras e transferência; capa verde). Equipe fr.
Primeiro da dupla com o Reel de 10/02 ("Quanto custou o seu Carnaval?"): o mesmo envelope desenhado aparece nos dois vídeos e nas
duas capas, antes da folia (R$ 500 entram) e depois (sobram R$ 45,20). Os sobretítulos dos ganchos são "Antes do Carnaval" e
"Depois do Carnaval"; nenhum dos dois promete o outro post, para cada um funcionar sozinho.
Vídeo, capa e prévia gerados por equipes/fr/reel_05.py (assert nos números lidos da tela); telas capturadas por
equipes/fr/captura_05.py no site build 2026-10-19.5, na conta de base (J/base_app, sem mudança: a conta "Carteira do Carnaval"
(Dinheiro / Carteira, no patrimônio), criada em 04/02, e a transferência de R$ 500 "Dinheiro para a folia" já estão nela), no celular
(390 px em escala 3), relógio da página em 05/02/2027 10:00, tudo pela interface:
- Menu › "Contas e carteiras": "Carteira do Carnaval · Dinheiro / Carteira · No total · R$ 410,10";
- Transações › toque na transferência: "Editar transação", Transferência, R$ 500,00, Data "Ontem 04/02", "Já foi feita · Afeta o
  saldo das duas contas agora", De "Conta corrente", Para "Carteira do Carnaval" (aberta só para mostrar, sem salvar);
- toque na fantasia: "Editar transação", Despesa, R$ 89,90, "Lazer e hobbies", "Pago via" "Carteira do Carnaval" (sem salvar);
- filtro de contas só com a Carteira do Carnaval: a fantasia (−R$ 89,90, paga, 04/02) e a transferência (R$ 500,00);
  "Saldo acumulado" R$ 410,10. O resumo dessa tela diz "somam R$ 589,90" (soma dos valores da lista, não um saldo): fica fora do anel.
Conta: 500,00 − 89,90 = 410,10.
Datas do Carnaval de 2027 (08 e 09/02) e ponto facultativo: não citados no post (FATOS.md, 6.1 a 6.4).
Diferença do que já saiu: 03/12 falou de presentes com teto antes da loja; aqui o teto é físico, numa conta separada, e a
transferência aparece como o gesto que não é gasto. O carrossel de 13/02 (fa) aprofunda "guardar não é gastar" com a reserva."""

POST = {
    "pasta": "2027-02-05_reel-o-envelope-do-carnaval",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Carnaval com envelope: uma conta Dinheiro / Carteira só para a folia, R$ 500 passados para ela com uma transferência (que não é gasto, o dinheiro só muda de lugar), os gastos pagos por ela e o saldo que sobra (R$ 410,10 depois da fantasia)",
    "pilar": "Carnaval · produto (Contas e carteiras, transferência, Pago via)",
    "data_longa": "sexta-feira, 5 de fevereiro de 2027",
    "data_curta": "sexta-feira, 05/02/2027",
    "data_mockup": "5 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-05T10:00:00",
    "video": "saida/2027-02-05_reel-o-envelope-do-carnaval/reel.mp4",
    "capa": "saida/2027-02-05_reel-o-envelope-do-carnaval/capa.jpg",
    "previa": "saida/2027-02-05_reel-o-envelope-do-carnaval/previa.mp4",
    "slides": [
        "Capa da grade (verde, logotipo negativo) · CARNAVAL · O envelope da folia. · Um envelope grande desenhado em traço branco, aberto, com a pílula branca “R$ 500” entrando nele.",
        "0 a 2,8 s · Gancho (papel) · ANTES DO CARNAVAL · Carnaval com envelope: quando acabar, acabou. · Desde o primeiro quadro, a pílula verde “R$ 500” desce, entra no envelope desenhado, a aba fecha e o valor fica escrito nele; embaixo, “Carteira do Carnaval”.",
        "2,9 a 5,2 s · Em Contas e carteiras, uma conta só para a folia. · Tela real de Contas e carteiras no celular (05/02/2027); anel em “Carteira do Carnaval · Dinheiro / Carteira · No total”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "5,4 a 7,6 s · Passe R$ 500 para ela, com uma transferência. · A transferência “Dinheiro para a folia” aberta: anel em “Transferência” e depois em De “Conta corrente” e Para “Carteira do Carnaval”, R$ 500,00.",
        "7,7 a 9,9 s · Transferência não é gasto: o dinheiro só muda de lugar. · Anel em “Já foi feita · Afeta o saldo das duas contas agora”.",
        "10,1 a 12,3 s · Cada gasto da folia sai da carteira. · A fantasia aberta (Despesa, R$ 89,90, Lazer e hobbies): anel em “Pago via · Carteira do Carnaval”.",
        "12,4 a 14,8 s · Na carteira, sobram R$ 410,10. · Transações só da Carteira do Carnaval: anéis na fantasia (−R$ 89,90) e na transferência (R$ 500,00); a câmera sobe até “Saldo acumulado R$ 410,10” (anel).",
        "15,0 a 17,8 s · Quando acabar, acabou. · O mesmo envelope do gancho: a pílula “−R$ 89,90 fantasia” sai dele e o valor vai de R$ 500,00 a R$ 410,10; embaixo, “R$ 500 − R$ 89,90 = R$ 410,10”.",
        "17,8 a 20,6 s · Fechamento (verde) · Contas e carteiras no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Carnaval com envelope: quando acabar, acabou.\n\n"
        "O método é antigo: separar o dinheiro da folia antes de ela começar. No timtimcash, o envelope é uma conta do tipo Dinheiro / "
        "Carteira. No exemplo do vídeo, a Carteira do Carnaval recebeu R$ 500 da conta corrente, com uma transferência.\n\n"
        "Transferência não é gasto: o dinheiro só muda de lugar, e o mês não fica mais caro por isso. Cada gasto da folia é lançado com "
        "Pago via Carteira do Carnaval. A fantasia de R$ 89,90 já saiu dela, e sobram R$ 410,10.\n\n"
        "Dica: escreva Carnaval na descrição de cada gasto. Depois da folia, a busca em Transações junta tudo e mostra a soma.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#carnaval #controledegastos #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Sexta-feira antes da folia: é o último momento para decidir quanto vai para o Carnaval, antes de os gastos começarem."),
        ("O que desperta interesse", "Uma regra fácil de lembrar (quando acabar, acabou) e um valor redondo entrando no envelope já no primeiro segundo."),
        ("Benefício para o público", "Aprende um jeito simples de pôr teto num período de gastos: uma conta só para isso, uma transferência (que não é gasto) e o saldo que mostra quanto ainda pode gastar."),
        ("Como contribui para o perfil", "Mostra três funções reais num só gesto (Contas e carteiras, Transferência e Pago via) e abre a dupla com o Reel de 10/02, que mostra quanto o Carnaval custou."),
    ],
    "alt": [
        "Reel de 21 segundos. Em fundo claro, a frase Carnaval com envelope: quando acabar, acabou, e uma pílula verde de R$ 500 que entra num envelope "
        "desenhado; a aba fecha e o valor fica escrito nele, com o nome Carteira do Carnaval. Depois, telas reais do timtimcash no celular, com dados de exemplo: "
        "em Contas e carteiras, a conta Carteira do Carnaval, do tipo Dinheiro / Carteira; a transferência de R$ 500, Dinheiro para a folia, da Conta corrente "
        "para a Carteira do Carnaval, com a frase Afeta o saldo das duas contas agora, e o título Transferência não é gasto: o dinheiro só muda de lugar; "
        "a fantasia de R$ 89,90 com Pago via Carteira do Carnaval; e as transações da carteira, com saldo acumulado de R$ 410,10. No fim, o mesmo envelope: "
        "sai a fantasia, de R$ 89,90, e sobram R$ 410,10. Quando acabar, acabou. Contas e carteiras no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-contas-e-carteiras.png · Contas e carteiras no celular, aberta pelo menu (site build 2026-10-19.5, conta de base, relógio em 05/02/2027 10:00): 5 contas, Carteira do Carnaval, Dinheiro / Carteira, No total, R$ 410,10 · 2,9 a 5,3 s",
        "telas/celular-editar-transferencia.png · Editar transação da transferência Dinheiro para a folia: Transferência, R$ 500,00, Ontem 04/02, Já foi feita, De Conta corrente, Para Carteira do Carnaval (sem salvar) · 5,3 a 10,0 s",
        "telas/celular-editar-fantasia.png · Editar transação da Fantasia de Carnaval: Despesa, R$ 89,90, Lazer e hobbies, Pago via Carteira do Carnaval (sem salvar) · 10,0 a 12,4 s",
        "telas/celular-transacoes-so-carteira.png · Transações, Fevereiro 2027, só a Carteira do Carnaval (filtro de contas): a fantasia e a transferência; Saldo acumulado R$ 410,10 · 12,4 a 14,8 s",
        "telas/celular-visao-geral.png, celular-menu.png, celular-transacoes-fevereiro.png e celular-filtro-so-carteira.png · os passos até essas telas (menu e filtro de contas) · conferência, não aparecem no vídeo",
        "telas/caixas.json · posições medidas na captura e o texto de cada tela, usados nos anéis e nos assert do roteiro",
    ],
}
