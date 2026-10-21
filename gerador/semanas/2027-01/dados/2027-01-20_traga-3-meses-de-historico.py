# -*- coding: utf-8 -*-
"""Quarta 20/01/2027 · carrossel "Traga 3 meses do passado." (série Comece 2027, organização, capa verde suave). Equipe jb.
Artes: saida/2027-01-20_traga-3-meses-de-historico/01.jpg a 07.jpg, geradas por equipes/jb/posts.py (post_20, contas por assert).
Telas reais em saida/2027-01-20_traga-3-meses-de-historico/telas/, capturadas por equipes/jb/captura.py (c20), celular 390 px em
escala 3, relógio em 20/01/2027 10:00, build 2026-10-19.5.

MUDANÇA NA CONTA (só na cópia jb, J/equipes/jb/<cópia>/estado_jb.py, gerar_novo): a mesma pessoa da conta de exemplo, como se
tivesse começado no timtimcash em 02/01/2027. As mesmas 4 contas, cada uma com o saldo de 31/12/2026 da conta de base como saldo
inicial (Conta corrente R$ 19.063,66; Corretora no exterior R$ 60.000,00; Reserva R$ 22.974,60; Banco na Europa R$ 11.525,40), e
só os lançamentos de 2027 (os pagos e os pendentes), sem remessas e sem cenários. Em 20/01 cada conta tem o mesmo saldo da conta de
base (assert no gerador). Junto, o arquivo de exemplo extrato_conta_corrente_out-dez-2026.ofx: a Conta corrente de 01/10 a
31/12/2026 com os mesmos 93 lançamentos da conta de base (receitas, despesas e as 3 aplicações na reserva), do mais novo para o mais
velho, em maiúsculas como os bancos escrevem (três nomes como o banco escreve: SUPERMERCADO DA VILA, POSTO DE COMBUSTIVEL,
INGRESSO SHOW), e o saldo final do banco em 31/12/2026 (R$ 19.063,66). Nenhum número já usado em outro post mudou.

O que a pessoa faz na tela: Menu > Importar (Planilha, com o formato aberto; Extrato bancário); Escolher arquivo com o .ofx; "Conta
de destino": Conta corrente; "Revisar importação" (93 linhas; 47 com categoria sugerida, 46 "Sem categoria"); tira as 3 linhas
APLICACAO NA RESERVA (transferências para a Reserva, não são gasto); "Importar 90 linhas" (receitas R$ 37.613,36, despesas
R$ 28.043,30, resultado R$ 9.570,06); "O saldo não bate com o banco" (extrato R$ 19.063,66 em 31/12/2026; no timtimcash
R$ 28.633,72, a diferença é o resultado importado); "Ajustar para R$ 19.063,66". As categorias "Sem categoria" ficaram como vieram
(não aparecem nas telas usadas).
Números das telas: antes, Receitas R$ 9.960, Despesas R$ 9.018 e Resultado R$ 941, cada um com o selo "1º mês"; Relatórios,
"Seu primeiro mês no timtimcash · ... Ele começa quando houver 3 meses de histórico antes deste (faltam 3)". Depois, queda de
20,6%, 3,5% e 70,5% e "Comparado com a média por mês de Jan/26 a Dez/26" (a Análise do período diz "Jan/26 a Dez/26 · 3 de 12
meses ativos": a média usa os meses com lançamento). Conferência: médias de out a dez/2026 da conta de base, R$ 37.613,36 ÷ 3 =
R$ 12.537,79 de receitas e R$ 28.043,30 ÷ 3 = R$ 9.347,77 de despesas; 9.960 contra 12.537,79 = −20,6%; 9.018,50 contra 9.347,77
= −3,5%; 941,50 contra 3.190,02 = −70,5%. Sem fato externo."""

POST = {
    "pasta": "2027-01-20_traga-3-meses-de-historico",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Comece 2027 com uma média: por que o site precisa de 3 meses de histórico para comparar o mês com a sua média, os dois caminhos do Importar (extrato .ofx ou planilha), a revisão linha a linha, o ajuste quando o saldo não bate com o banco, e janeiro antes e depois de trazer out, nov e dez",
    "pilar": "Organização · série Comece 2027 · produto (Importar)",
    "data_longa": "quarta-feira, 20 de janeiro de 2027",
    "data_curta": "quarta-feira, 20/01/2027",
    "data_mockup": "20 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-20T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · COMECE 2027 · Traga 3 meses do passado. · Três folhas de extrato desenhadas, OUT, NOV e DEZ de 2026, com linhas de lançamentos em verde e coral, entrando numa pasta verde escura com a frente em tinta onde se lê Importar, com o ícone de envio.",
        "POR QUE 3 MESES · A média começa com 3 meses de histórico. · Sem passado, o site mostra só o mês: cada número vem com o selo 1º mês. · Telas reais no celular (relógio em 20/01/2027, conta que começou em 02/01): Receitas R$ 9.960, Despesas R$ 9.018 e Resultado R$ 941, cada um com “1º mês”; e o Diagnóstico de Relatórios: “Seu primeiro mês no timtimcash · O diagnóstico compara o mês com a sua média. Ele começa quando houver 3 meses de histórico antes deste (faltam 3). Por enquanto, os números do mês:”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "NO MENU, IMPORTAR · Extrato do banco ou planilha. · Tela real das abas “Planilha · .xlsx / .csv” e “Extrato bancário · .ofx”. Dois cartões: Extrato do banco (arquivo .ofx): você escolhe a conta de destino; as categorias chegam sugeridas; o que já entrou vem desmarcado. Sua planilha (.xlsx ou .csv): 6 colunas, em qualquer ordem; há um modelo pronto em Excel; conta nova vem marcada como Nova. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "ANTES DE CONFIRMAR · Você revisa cada linha. · No exemplo, 47 de 93 linhas vieram com categoria. As 3 aplicações na reserva saíram: não são gasto. · Tela real de “Revisar importação”: “Extrato OFX detectado · Conta de destino: Conta corrente. 47 de 93 linhas vieram com categoria sugerida pelo nome do estabelecimento. Confira; 46 ficam como Sem categoria”; e a linha SUPERMERCADO DA VILA, −R$ 298,40, 28/12/2026, Mercado (sugerida), Pago, Conta corrente. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "SE O SALDO NÃO BATER · O site confere com o banco. · Se a conta foi criada com o saldo de hoje, o site oferece o ajuste. As transações não mudam. · Tela real: “O saldo não bate com o banco · O extrato do Conta corrente termina com R$ 19.063,66 em 31/12/2026. No timtimcash, a conta ficou com R$ 28.633,72 nessa data. Isso acontece quando o saldo informado ao criar a conta já incluía estas transações. Ajustar o saldo inicial deixa o timtimcash igual ao banco; as transações não mudam.” Botões Ajustar para R$ 19.063,66 e Manter como está. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "DEPOIS DE IMPORTAR · Pronto: janeiro ganha uma média. · Antes, só janeiro: Receitas R$ 9.960, Despesas R$ 9.018, Resultado R$ 941, com “1º mês”. Depois, com out, nov e dez: os mesmos números com queda de 20,6%, 3,5% e 70,5% e “Comparado com a média por mês de Jan/26 a Dez/26”. · Notas: A média usa os meses com lançamento: no exemplo, out, nov e dez. Janeiro até o dia 20. Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Comece 2027 com uma média. · Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Comece 2027 com uma média: traga 3 meses do passado.\n\n"
        "O timtimcash compara o mês com a sua média, e a média começa quando há 3 meses de histórico. Quem começa em janeiro vê só os "
        "números do mês, com o selo 1º mês.\n\n"
        "No menu, Importar: o extrato do banco em .ofx (você escolhe a conta, e as categorias chegam sugeridas) ou a sua planilha "
        "(6 colunas, em qualquer ordem, com modelo em Excel). Antes de confirmar, você revisa cada linha. No exemplo, 47 das 93 linhas "
        "de out a dez vieram com categoria, e as 3 aplicações na reserva saíram, porque não são gasto. Se o saldo não bater com o do "
        "banco, o site avisa e oferece o ajuste.\n\n"
        "Pronto: janeiro passa a ser comparado com a média de out, nov e dez.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Comece hoje: crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#organizacaofinanceira #controlefinanceiro #financaspessoais #extratobancario #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Na terceira semana de janeiro, quem começou com a série Comece 2027 já tem um mês na conta e nenhuma comparação. Trazer out, nov e dez agora destrava a média antes de janeiro fechar."),
        ("O que desperta interesse", "A capa mostra três extratos entrando na pasta do Importar. Dentro, o antes e depois dos mesmos três números: o selo 1º mês vira a comparação com a média."),
        ("Benefício para o público", "Sabe por que precisa de 3 meses, escolhe entre extrato .ofx e planilha, aprende a revisar (inclusive tirar o que não é gasto) e entende o aviso de saldo que aparece quando se importa o passado."),
        ("Como contribui para o perfil", "Fecha o mês de captação com um passo prático e uma razão concreta para criar a conta, com telas reais novas. Diferente de 08/10 e 23/10 (extrato e planilha): aqui o ângulo é o mínimo de 3 meses e o que ele destrava."),
    ],
    "alt": [
        "Comece 2027. Traga 3 meses do passado. Três folhas de extrato desenhadas, de outubro, novembro e dezembro de 2026, com linhas de lançamentos em verde e coral, entrando numa pasta verde escura; na frente da pasta, o botão Importar com uma seta para cima.",
        "Por que 3 meses: a média começa com 3 meses de histórico. Sem passado, o site mostra só o mês, e cada número vem com o selo 1º mês. Telas reais no celular, com dados de exemplo: receitas de 9.960 reais, despesas de 9.018 e resultado de 941, os três com 1º mês; e o diagnóstico de Relatórios, seu primeiro mês no timtimcash: o diagnóstico compara o mês com a sua média e começa quando houver 3 meses de histórico antes deste; faltam 3.",
        "No menu, Importar: extrato do banco ou planilha. Tela real com as abas Planilha, .xlsx ou .csv, e Extrato bancário, .ofx. Extrato do banco, arquivo .ofx: você escolhe a conta de destino, as categorias chegam sugeridas e o que já entrou vem desmarcado. Sua planilha, .xlsx ou .csv: 6 colunas em qualquer ordem, um modelo pronto em Excel e conta nova marcada como Nova.",
        "Antes de confirmar, você revisa cada linha. No exemplo, 47 de 93 linhas vieram com categoria, e as 3 aplicações na reserva saíram, porque não são gasto. Tela real de Revisar importação: extrato OFX detectado, conta de destino Conta corrente, 47 de 93 linhas com categoria sugerida pelo nome do estabelecimento; e a linha Supermercado da Vila, 298 reais e 40 centavos, 28 de dezembro de 2026, categoria Mercado sugerida, paga, na Conta corrente.",
        "Se o saldo não bater, o site confere com o banco. Tela real do aviso O saldo não bate com o banco: o extrato da Conta corrente termina com 19.063 reais e 66 centavos em 31 de dezembro de 2026, e no timtimcash a conta ficou com 28.633 reais e 72 centavos nessa data. Isso acontece quando o saldo informado ao criar a conta já incluía estas transações; ajustar o saldo inicial deixa o timtimcash igual ao banco, e as transações não mudam. Botões Ajustar para 19.063,66 e Manter como está.",
        "Depois de importar, janeiro ganha uma média. Antes, só janeiro: receitas de 9.960 reais, despesas de 9.018 e resultado de 941, cada um com o selo 1º mês. Depois, com outubro, novembro e dezembro: queda de 20,6% nas receitas, de 3,5% nas despesas e de 70,5% no resultado, comparado com a média por mês. A média usa os meses com lançamento; janeiro vai até o dia 20.",
        "Comece 2027 com uma média. Crie sua conta com nome, e-mail e senha. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-visao-geral-antes.png · Visão geral, relógio em 20/01/2027 10:00, conta que começou em 02/01 (cópia jb), celular 390 × 1700 em escala 3 · slides 2 e 6 (os três mini cartões com 1º mês)",
        "telas/celular-relatorios-antes.png · Relatórios, Diagnóstico de janeiro 2027, “Seu primeiro mês no timtimcash” · slide 2",
        "telas/celular-importar-planilha.png e telas/celular-importar-extrato.png · Menu > Importar, abas Planilha (formato aberto) e Extrato bancário · slide 3 (as abas)",
        "telas/celular-importar-conta-de-destino.png · a escolha da conta de destino do .ofx (Conta corrente) · não usada nas artes",
        "telas/celular-revisar-importacao.png · Revisar importação com as 93 linhas do .ofx de exemplo · slide 4 (a faixa e a linha SUPERMERCADO DA VILA)",
        "telas/celular-revisar-importacao-90-linhas.png · a revisão sem as 3 aplicações na reserva, Importar 90 linhas · conferência",
        "telas/celular-saldo-nao-bate.png · O saldo não bate com o banco, depois de Importar 90 linhas · slide 5",
        "telas/celular-visao-geral-depois.png · Visão geral depois de importar e de Ajustar para R$ 19.063,66 · slide 6 (os três mini cartões e Comparado com a média por mês)",
    ],
}
