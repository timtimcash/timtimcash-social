# -*- coding: utf-8 -*-
"""Gera $O/dados/<pasta>.py dos 8 Reels de outubro (mesmos campos dos carrosséis, mais video, capa e previa)."""
import os, pprint, subprocess

O = "/tmp/claude-0/-home-claude-timtimcash-social/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/outubro"
FIM = "Acesse pelo navegador, no computador ou no celular: timtimcash.com"
TELA = "Tela real do timtimcash, com dados de exemplo."
DIAS = {6: "terça-feira", 8: "quinta-feira", 14: "quarta-feira", 16: "sexta-feira", 20: "terça-feira", 22: "quinta-feira", 27: "terça-feira", 30: "sexta-feira"}
PTAX = [("Receita Federal · Taxas de câmbio para fins fiscais, anos anteriores (PTAX de 2023 e 2024)",
         "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/ecf/taxas-de-cambio-incluindo-valor-do-dolar-para-fins-fiscais-irpj-AC-anteriores"),
        ("Moed.as · PTAX do dólar em dezembro de 2025", "https://moed.as/ptax/mensal/usd/2025/12.html")]

def dur(pasta):
    f = os.path.join(O, "saida", pasta, "reel.mp4")
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())

def base(dia, pasta, tema, pilar):
    d = round(dur(pasta))
    return {
        "pasta": pasta, "tipo": "reel", "plataforma": "Instagram",
        "formato": f"Reel de {d} segundos (1080 × 1920, 9:16), com capa própria na grade",
        "formato_curto": f"Reel de {d} s", "tema": tema, "pilar": pilar,
        "data_longa": f"{DIAS[dia]}, {dia} de outubro de 2026", "data_curta": f"{DIAS[dia]}, {dia:02d}/10/2026",
        "data_mockup": f"{dia} de outubro", "hora": "10h00", "iso": f"2026-10-{dia:02d}T10:00:00",
        "video": f"saida/{pasta}/reel.mp4", "capa": f"saida/{pasta}/capa.jpg", "previa": f"saida/{pasta}/previa.mp4",
    }

REELS = []

p = base(6, "2026-10-06_reel-o-timtimcash-em-20-segundos", "O timtimcash em 20 segundos: um tour pelas telas reais, da Visão geral às Remessas ao exterior", "Produto em ação")
p.update(slides=[
    "0 a 2,4 s · Capa (verde) · TOUR PELO SITE · O timtimcash em 20 segundos · recorte real da Visão geral no celular.",
    "2,4 a 5 s · VISÃO GERAL · Quanto entrou, quanto saiu, quanto sobrou. · Tela real: patrimônio R$ 104.180, guardou 21,9% da receita.",
    "5 a 7,6 s · ORÇAMENTOS · O que estourou e o que ainda cabe. · Tela real: Bares e restaurantes em 112%, Mercado em 86%, Transporte em 64%.",
    "7,6 a 10,2 s · RELATÓRIOS · Para onde o dinheiro foi. · Tela real: despesas de R$ 7.780,00 em 7 categorias, Casa com R$ 2.300,00 (29,6%).",
    "10,2 a 12,8 s · SIMULAÇÃO FUTURA · Como fecham os próximos meses. · Tela real do cenário base: saldo de R$ 37.720 em set/27.",
    "12,8 a 15,4 s · REMESSAS AO EXTERIOR · Quanto rendeu lá fora, em reais. · Tela real: US$ 13.200,00 na carteira hoje, +R$ 12.600,00 (+21,0% em R$).",
    "15,4 a 17,8 s · Todo dinheiro, um só lugar. · Visão geral · Orçamentos · Relatórios · Simulação futura · Remessas ao exterior.",
    "17,8 a 20 s · Fechamento (verde) · Seu dinheiro, com a clareza que ele merece. · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
], legenda=(
    "O timtimcash em 20 segundos.\n\n"
    "Visão geral: quanto entrou, quanto saiu e quanto sobrou. Orçamentos: o que estourou e o que ainda cabe. Relatórios: para onde o dinheiro foi. "
    "Simulação futura: como fecham os próximos meses. Remessas ao exterior: quanto rendeu lá fora, em reais.\n\n"
    "Tudo num lugar só, sem senha do banco e sem propaganda.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#financaspessoais #controlefinanceiro #organizacaofinanceira #investimentonoexterior #timtimcash"
), justificativa=[
    ("Por que agora", "É o primeiro Reel de outubro. Quem chega ao perfil por um Reel precisa entender o que é o site em poucos segundos, e a terça abre a semana de produto logo depois da taxa de poupança de segunda."),
    ("O que desperta interesse", "A promessa está no título (20 segundos) e o ritmo é de cortes rápidos, uma frase por tela. Tudo é tela real, então a pessoa vê o produto como ele é."),
    ("Benefício para o público", "Em 20 segundos, a pessoa entende as cinco perguntas que o timtimcash responde e decide se vale abrir o site."),
    ("Como contribui para o perfil", "Vira a vitrine em vídeo do produto, complementa o post fixado “Comece por aqui” e leva ao link na bio."),
], alt=["Reel de 20 segundos. O timtimcash em 20 segundos: telas reais do site no celular, com dados de exemplo. Visão geral: quanto entrou, quanto saiu, quanto sobrou, com patrimônio de R$ 104.180. Orçamentos: o que estourou e o que ainda cabe. Relatórios: para onde o dinheiro foi, com despesas de R$ 7.780 em 7 categorias. Simulação futura: como fecham os próximos meses. Remessas ao exterior: quanto rendeu lá fora, em reais. Todo dinheiro, um só lugar. Seu dinheiro, com a clareza que ele merece. Link na bio."],
fontes=[], telas=["celular-dashboard.jpg (Visão geral)", "celular-orcamentos-progresso.jpg (Orçamentos)", "celular-relatorios-despesas-por-categoria.jpg (Relatórios)", "celular-simulacao-cenario-coluna.jpg (Simulação futura)", "celular-remessas.jpg (Remessas ao exterior)"])
REELS.append(p)

p = base(8, "2026-10-08_reel-extrato-com-categoria-sugerida", "Extrato do banco já com as categorias: importar o .ofx sem senha do banco, categorias sugeridas, a regra que aprende e o extrato repetido que vem desmarcado", "Produto em ação")
p.update(slides=[
    "0 a 2,8 s · Capa (papel) · IMPORTAR EXTRATO · Seu extrato do banco, já com as categorias. · Três linhas reais com o selo “sugerida”: Mercado, Transporte e Saúde.",
    "2,8 a 5,4 s · Sem senha do banco: baixe o extrato .ofx e importe. · Tela real de “Importar transações”, aba “Extrato bancário · .ofx”, com o toque em “Escolher arquivo”.",
    "5,4 a 8,6 s · As categorias já chegam sugeridas. · Tela real de “Revisar importação”: Posto Avenida em Transporte e Farmácia São José em Saúde, com o selo “sugerida”.",
    "8,6 a 13 s · Mudou uma categoria? O timtimcash pergunta se deve lembrar. · A farmácia muda para Cuidados pessoais e aparece “Automatizar esta categoria?”, com o toque em “Aplicar e lembrar”.",
    "13 a 14,7 s · Confira e importe. · Toque em “Importar 3 linhas”.",
    "14,7 a 16,9 s · Importou o mesmo extrato de novo? O que já entrou vem desmarcado. · Aviso real: 3 transações já existem no timtimcash e foram desmarcadas.",
    "16,9 a 19 s · E a farmácia já chega na categoria que você escolheu.",
    "19 a 22 s · Categorize uma vez, o timtimcash aprende. · Transações já importadas são detectadas e desmarcadas. · Sem senha do banco · Você revisa antes de importar.",
    "22 a 25 s · Fechamento (verde) · Importar extrato no timtimcash · Link na bio.",
], legenda=(
    "Seu extrato do banco, já com as categorias.\n\n"
    "No timtimcash você não informa a senha do banco: baixa o extrato (.ofx) no seu banco e importa. As categorias chegam sugeridas pelo nome do estabelecimento, e você revisa cada linha antes de confirmar.\n\n"
    "Mudou uma categoria? O timtimcash pergunta se deve lembrar, e da próxima vez ela já chega certa. Se importar o mesmo extrato de novo, o que já entrou vem desmarcado.\n\n"
    "Categorize uma vez, o timtimcash aprende.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#controlefinanceiro #organizacaofinanceira #financaspessoais #extratobancario #timtimcash"
), justificativa=[
    ("Por que agora", "Começo de mês, com o extrato de setembro fechado: é quando mais gente confere os gastos. Mostrar a importação agora dá o caminho mais rápido para quem quer começar."),
    ("O que desperta interesse", "Ataca a maior preguiça do controle financeiro, lançar tudo à mão, e mostra o fluxo real, toque a toque, com as categorias aparecendo sozinhas."),
    ("Benefício para o público", "A pessoa aprende que dá para trazer o extrato sem entregar a senha do banco e que o site aprende as categorias com o uso."),
    ("Como contribui para o perfil", "Mostra dois diferenciais em ação (nenhuma conexão com o banco e regras que aprendem) e prepara o carrossel de 23/10, sobre trazer a planilha."),
], alt=["Reel de 25 segundos. Seu extrato do banco, já com as categorias. Telas reais do timtimcash no celular, com dados de exemplo. Em Importar transações, a aba Extrato bancário .ofx. Na revisão, Posto Avenida chega sugerido em Transporte e Farmácia São José em Saúde. Ao trocar a farmácia para Cuidados pessoais, o site pergunta Automatizar esta categoria?, e o toque é em Aplicar e lembrar. Ao importar o mesmo extrato de novo, as 3 transações que já existem vêm desmarcadas, e a farmácia já chega na categoria escolhida. Categorize uma vez, o timtimcash aprende. Link na bio."],
fontes=[], telas=["celular-importar-1-extrato-ofx.jpg", "celular-importar-2-conta-de-destino.jpg", "celular-importar-3-revisar-importacao.jpg", "celular-importar-4-trocar-categoria.jpg", "celular-importar-5-automatizar-esta-categoria.jpg", "celular-importar-6-regra-salva.jpg", "celular-importar-7-mesmo-extrato-de-novo.jpg"])
REELS.append(p)

p = base(14, "2026-10-14_reel-rendimento-ano-a-ano", "Rendeu em dólar todos os anos. E em reais? O mesmo investimento lá fora, ano a ano, em dólar e em reais, com o câmbio real do fim de cada ano", "Investimento no exterior")
p.update(slides=[
    "0 a 2,5 s · Capa (tinta) · INVESTIMENTO NO EXTERIOR · Rendeu em dólar todos os anos. E em reais? · Tabela de 2023 a 2026 com o rendimento em US$ e um ponto de interrogação em R$.",
    "2,5 a 5,5 s · 2023 · Em dólar, rendeu +6,5%. Em reais, +3,8%. · Tela real de “Rendimento ano a ano”, com 2023 em destaque.",
    "5,5 a 8,5 s · 2024 · Em dólar, rendeu +3,6%. Em reais, +34,4%.",
    "8,5 a 11 s · 2025 · Em dólar, rendeu +3,9%. Em reais, −7,7%.",
    "11 a 13,5 s · 2026 até hoje · Em dólar, rendeu +2,5%. Em reais, +2,4%.",
    "13,5 a 17 s · Em reais, entra também a variação do câmbio no ano. Para fechar cada ano, ele usa o saldo de 31/12 e a PTAX de compra do último dia útil. · A nota da própria tela em destaque.",
    "17 a 20 s · O investimento é o mesmo. O câmbio muda o ano. · Resumo: em US$ +6,5%, +3,6%, +3,9%, +2,5%; em R$ +3,8%, +34,4%, −7,7%, +2,4%.",
    "20 a 23 s · Fechamento (verde) · Remessas ao exterior no timtimcash · Link na bio.",
], legenda=(
    "Rendeu em dólar todos os anos. Em reais, foi outra história.\n\n"
    "No exemplo do vídeo, o mesmo investimento rendeu em dólar todos os anos, de 2,5% a 6,5%. Em reais, 2024 deu +34,4% e 2025 deu −7,7%. "
    "A diferença é o câmbio: o dólar subiu forte em 2024 e caiu em 2025.\n\n"
    "Você informa quanto havia lá fora em 31 de dezembro, e o timtimcash usa a PTAX de compra do último dia útil do ano, do Banco Central. "
    "Assim cada ano mostra o que foi rendimento e o que foi câmbio.\n\n"
    "Exemplo com saldos fictícios e o câmbio real do fim de cada ano, sem IOF e tarifas.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#investimentonoexterior #dolar #cambio #educacaofinanceira #timtimcash"
), justificativa=[
    ("Por que agora", "Meio de outubro, a dois meses do fechamento do ano: bom momento para quem investe lá fora entender como cada ano é medido. Continua a série de exterior do mês com um ângulo novo: vários anos lado a lado, depois do exemplo de um ano (02/10) e do câmbio de equilíbrio (07/10)."),
    ("O que desperta interesse", "O contraste entre +34,4% e −7,7% com o mesmo investimento surpreende, e a capa deixa a pergunta em aberto com os pontos de interrogação na coluna dos reais."),
    ("Benefício para o público", "A pessoa entende que o resultado em reais depende do câmbio de cada fim de ano e passa a olhar as duas colunas antes de concluir se o investimento foi bem."),
    ("Como contribui para o perfil", "Mostra o maior diferencial do timtimcash, o exterior medido em reais ano a ano, com tela real e câmbio oficial do fim de cada ano."),
], alt=["Reel de 23 segundos. Rendeu em dólar todos os anos. E em reais? Tela real de Rendimento ano a ano do timtimcash no celular, com dados de exemplo. 2023: mais 6,5% em dólar e mais 3,8% em reais. 2024: mais 3,6% em dólar e mais 34,4% em reais. 2025: mais 3,9% em dólar e menos 7,7% em reais. 2026 até hoje: mais 2,5% em dólar e mais 2,4% em reais. Em reais, entra também a variação do câmbio no ano. O investimento é o mesmo; o câmbio muda o ano. Link na bio."],
fontes=PTAX, telas=["celular-remessas-rendimento-ano-a-ano.jpg (Rendimento ano a ano)"])
REELS.append(p)

p = base(16, "2026-10-16_reel-quanto-vai-para-o-mercado", "Dia Mundial da Alimentação: quanto do seu mês vai para o mercado? O mercado como fatia do mês, em Relatórios, e acompanhado pelo limite em Orçamentos", "Educação prática com produto")
p.update(slides=[
    "0 a 2,6 s · Capa (verde) · 16/10 · DIA MUNDIAL DA ALIMENTAÇÃO · Quanto do seu mês vai para o mercado? · Anel com 22% no mercado, na conta de exemplo, em setembro.",
    "2,6 a 6,8 s · No exemplo, o mercado levou R$ 1.710 em setembro. · Tela real de “Despesas por categoria”, com a linha do Mercado em destaque.",
    "6,8 a 10,6 s · É 22% de tudo o que saiu no mês: R$ 7.780. · O total no centro do gráfico e o 22% do Mercado em destaque.",
    "10,6 a 14,9 s · Com limite de R$ 2.000, o mercado fechou em 86%. · Tela real do “Progresso por categoria”, com a linha do Mercado em destaque.",
    "14,9 a 18 s · Olhe o mercado em porcentagem do mês. · Com um limite em Orçamentos, você vê no meio do mês onde o gasto vai fechar no ritmo atual.",
    "18 a 21 s · Fechamento (verde) · Relatórios e Orçamentos no timtimcash · Link na bio.",
], legenda=(
    "Hoje é o Dia Mundial da Alimentação. Quanto do seu mês vai para o mercado?\n\n"
    "No exemplo do vídeo, o mercado levou R$ 1.710 em setembro: 22% de tudo o que saiu no mês. Com limite de R$ 2.000, fechou em 86%.\n\n"
    "Olhar em porcentagem ajuda a comparar meses com gastos diferentes. E com um limite em Orçamentos, dá para ver no meio do mês onde o gasto vai fechar no ritmo atual.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#orcamentodomestico #financaspessoais #controlefinanceiro #educacaofinanceira #timtimcash"
), justificativa=[
    ("Por que agora", "16 de outubro é o Dia Mundial da Alimentação, data da FAO. A data dá o gancho para falar do gasto que pesa em quase toda casa: o mercado."),
    ("O que desperta interesse", "Pergunta direta e pessoal na capa, com um número grande (22%) que a pessoa compara na hora com o próprio mês."),
    ("Benefício para o público", "A pessoa aprende a olhar o mercado como fatia do mês, não só em reais, e a acompanhar pelo orçamento antes de o mês acabar."),
    ("Como contribui para o perfil", "Liga uma data do calendário a duas telas reais (Relatórios e Orçamentos) e traz variedade à semana, entre posts de exterior e de planejamento."),
], alt=["Reel de 21 segundos. 16 de outubro, Dia Mundial da Alimentação: quanto do seu mês vai para o mercado? Telas reais do timtimcash no celular, com dados de exemplo. Em Despesas por categoria, o mercado levou R$ 1.710 em setembro, 22% das despesas de R$ 7.780. Em Orçamentos, com limite de R$ 2.000, o mercado fechou em 86%. Olhe o mercado em porcentagem do mês: com um limite em Orçamentos, você vê no meio do mês onde o gasto vai fechar no ritmo atual. Relatórios e Orçamentos no timtimcash. Link na bio."],
fontes=[("FAO · Dia Mundial da Alimentação, 16 de outubro (World Food Day)", "https://www.fao.org/newsroom/detail/pope-leo-xiv-and-world-leaders-mark-world-food-day-and-fao-at-80-in-rome/en")],
telas=["celular-relatorios-despesas-por-categoria.jpg (Relatórios)", "celular-orcamentos-progresso.jpg (Orçamentos)"])
REELS.append(p)

p = base(20, "2026-10-20_reel-o-que-vence-esta-semana", "O que vence esta semana? Pendentes: o que falta pagar e receber numa tela só, com o que venceu primeiro e um toque para marcar como pago", "Produto em ação")
p.update(slides=[
    "0 a 2,6 s · Capa (tinta) · PENDENTES · O que vence esta semana? · Recorte real dos indicadores: Vencidas 1, A pagar R$ 186,40, A receber R$ 320.",
    "2,6 a 6 s · Em Pendentes, tudo o que falta pagar e receber. · Tela real de Pendentes no celular (relógio da página em 05/10/2026).",
    "6 a 8,8 s · O que já venceu aparece primeiro. · A conta de luz de −R$ 186,40, vencida há 5 dias, em destaque.",
    "8,8 a 11 s · Pagou? Um toque em “pendente”.",
    "11 a 13,4 s · Pronto: nada vencido.",
    "13,4 a 16,4 s · E ainda há R$ 320,00 a receber amanhã. · O reembolso de 06/10 em destaque.",
    "16,4 a 19,6 s · O mês só fecha quando nada fica para trás. · Contas a pagar e a receber num lugar só, com o que venceu primeiro. · Vencidas · A pagar · A receber · Total pendente.",
    "19,6 a 23 s · Fechamento (verde) · Pendentes no timtimcash · Link na bio.",
], legenda=(
    "O que vence esta semana? Em Pendentes, o timtimcash responde numa tela só.\n\n"
    "Tudo o que falta pagar e receber fica junto, com o que já venceu primeiro. No exemplo do vídeo, a conta de luz de R$ 186,40 venceu há 5 dias. "
    "Um toque em “pendente” e ela fica paga. E o reembolso de R$ 320,00 aparece para amanhã.\n\n"
    "O mês só fecha quando nada fica para trás.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#contasapagar #organizacaofinanceira #controlefinanceiro #financaspessoais #timtimcash"
), justificativa=[
    ("Por que agora", "Segunda quinzena, quando os vencimentos se acumulam e é fácil esquecer uma conta. Terça é um bom dia para organizar a semana."),
    ("O que desperta interesse", "A pergunta prática da capa e o antes e depois de um toque: a conta vencida some da lista na frente da pessoa."),
    ("Benefício para o público", "Um hábito simples e repetível: olhar uma vez por semana o que vence e o que entra."),
    ("Como contribui para o perfil", "Mostra uma função do dia a dia que ainda não tinha aparecido no perfil e retoma, em vídeo, a pergunta dos pendentes do post de fechamento de 30/09."),
], alt=["Reel de 23 segundos. O que vence esta semana? Tela real de Pendentes do timtimcash no celular, com dados de exemplo: Vencidas, A pagar e A receber. O que já venceu aparece primeiro: a conta de luz de R$ 186,40, vencida há 5 dias. Um toque em pendente e ela fica paga; pronto, nada vencido. E ainda há R$ 320,00 de reembolso a receber amanhã. O mês só fecha quando nada fica para trás. Pendentes no timtimcash. Link na bio."],
fontes=[], telas=["celular-pendentes-indicadores.jpg", "celular-pendentes-antes.jpg", "celular-pendentes-depois.jpg"])
REELS.append(p)

p = base(22, "2026-10-22_reel-ritmo-do-retorno", "Rendeu 11,8%. Em quanto tempo? O Ritmo do retorno (TIR com as datas reais de cada remessa) no período, ao ano e ao mês", "Investimento no exterior")
p.update(slides=[
    "0 a 2,8 s · Capa (verde suave) · RITMO DO RETORNO · Rendeu 11,8%. Em quanto tempo? · Linha do tempo de jul/23 (1ª remessa) a set/26 (valor da carteira).",
    "2,8 a 5,4 s · No período: 11,8% em dólar e 25,1% em reais. · Tela real de “Ritmo do retorno”, no modo “no período”.",
    "5,4 a 7,9 s · Só que esse período tem 3,2 anos. · De 12/07/2023 a 30/09/2026 em destaque.",
    "7,9 a 10,7 s · Ao ano: 3,5% em dólar e 7,2% em reais. · Toque em “ao ano”.",
    "10,7 a 13,4 s · Ao mês: 0,29% em dólar e 0,58% em reais. · Toque em “ao mês”.",
    "13,4 a 16,9 s · A TIR usa a data real de cada remessa. · “Como o retorno é calculado” aberto, com a explicação da própria tela em destaque.",
    "16,9 a 20,6 s · Rendimento no período não é rendimento ao ano. · É o mesmo número, escrito de três jeitos. Para comparar taxas, use a mesma base. · 11,8% no período · 3,5% ao ano · 0,29% ao mês (em dólar, na conta de exemplo).",
    "20,6 a 24 s · Fechamento (verde) · Remessas ao exterior no timtimcash · Link na bio.",
], legenda=(
    "Rendeu 11,8%. Em quanto tempo?\n\n"
    "Sem o prazo, a taxa diz pouco. No exemplo do vídeo, 11,8% em dólar foram em 3,2 anos: dá 3,5% ao ano, ou 0,29% ao mês. Em reais, 25,1% no período viram 7,2% ao ano.\n\n"
    "No timtimcash, o Ritmo do retorno calcula a TIR com a data real de cada remessa: o dinheiro que ficou mais tempo investido pesa mais. "
    "E mostra o mesmo resultado no período, ao ano e ao mês, para você comparar taxas na mesma base.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#investimentonoexterior #rentabilidade #educacaofinanceira #financaspessoais #timtimcash"
), justificativa=[
    ("Por que agora", "Fecha a série de exterior de outubro com a pergunta que sobra depois dos posts de rendimento: em quanto tempo. Vem uma semana depois do ano a ano (14/10), agora com a taxa ao ano."),
    ("O que desperta interesse", "A capa questiona um número que parece bom, e a resposta aparece na tela real em três toques."),
    ("Benefício para o público", "A pessoa aprende a comparar rendimentos na mesma base, ao ano, e entende por que a data de cada remessa muda a conta."),
    ("Como contribui para o perfil", "Mostra uma conta que a planilha raramente faz, a TIR com as datas reais, e reforça o timtimcash como a ferramenta de quem investe lá fora."),
], alt=["Reel de 24 segundos. Rendeu 11,8%. Em quanto tempo? Tela real do Ritmo do retorno do timtimcash no celular, com dados de exemplo. No período, 11,8% em dólar e 25,1% em reais, de 12/07/2023 a 30/09/2026, 3,2 anos. Ao ano, 3,5% em dólar e 7,2% em reais. Ao mês, 0,29% em dólar e 0,58% em reais. A TIR usa a data real de cada remessa. Rendimento no período não é rendimento ao ano: é o mesmo número, escrito de três jeitos. Remessas ao exterior no timtimcash. Link na bio."],
fontes=[], telas=["celular-remessas-ritmo-no-periodo.png", "celular-remessas-ritmo-ao-ano.png", "celular-remessas-ritmo-ao-mes.png", "celular-remessas-ritmo-como-e-calculado.png"])
REELS.append(p)

p = base(27, "2026-10-27_reel-ocultar-valores", "Vai abrir suas finanças em público? “Ocultar valores” esconde os números da tela, inclusive os dos gráficos, com um toque", "Posicionamento · privacidade")
p.update(slides=[
    "0 a 2,6 s · Capa (tinta) · PRIVACIDADE · Vai abrir suas finanças em público? · Olho grande e o patrimônio de R$ 104.180.",
    "2,6 a 5,5 s · Na fila, no ônibus, no trabalho? · Tela real da Visão geral no celular.",
    "5,5 a 8,5 s · Um toque e os valores somem. · Toque no olho do topo.",
    "8,5 a 11,3 s · Toque de novo, e eles voltam.",
    "11,3 a 15 s · Os gráficos também escondem. · Tela real do Fluxo mensal: as médias e o eixo do gráfico somem.",
    "15 a 18 s · Fechamento (verde) · “Ocultar valores” no timtimcash · Link na bio.",
], legenda=(
    "Vai abrir suas finanças na fila, no ônibus ou no trabalho?\n\n"
    "No timtimcash, um toque no olho esconde os valores da tela, inclusive os dos gráficos. Outro toque e eles voltam. A escolha fica guardada no navegador que você usa.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#privacidade #financaspessoais #controlefinanceiro #organizacaofinanceira #timtimcash"
), justificativa=[
    ("Por que agora", "Reta final do mês, quando muita gente confere as contas fora de casa. O post de 09/10 falou de como os dados entram e saem; este mostra a privacidade no dia a dia, em 18 segundos."),
    ("O que desperta interesse", "Uma situação que todo mundo reconhece na capa e a transformação na hora: um toque e os números somem."),
    ("Benefício para o público", "A pessoa descobre que pode abrir as finanças em público sem expor valores."),
    ("Como contribui para o perfil", "Reforça o pilar de privacidade num formato curto, que funciona em repetição e é fácil de compartilhar."),
], alt=["Reel de 18 segundos. Vai abrir suas finanças em público? Na fila, no ônibus, no trabalho? Tela real da Visão geral do timtimcash no celular, com dados de exemplo: um toque no olho do topo e os valores somem; outro toque e eles voltam. Os gráficos também escondem: no Fluxo mensal, as médias e o eixo do gráfico somem. Ocultar valores no timtimcash. Link na bio."],
fontes=[], telas=["movel.png", "movel-ocultar.png", "celular-dashboard-fluxo-mensal.png", "celular-dashboard-fluxo-mensal-ocultar.png"])
REELS.append(p)

p = base(30, "2026-10-30_reel-13-salario", "O 13º vem aí: o que a primeira parcela muda no seu saldo, na Simulação futura, com os prazos da Lei 4.749/1965", "Educação prática com produto")
p.update(slides=[
    "0 a 2,8 s · Capa (verde) · 13º SALÁRIO · O 13º vem aí. O que ele muda no seu saldo? · Quatro meses: out, nov (13º, 1ª parcela), dez, jan (IPVA e IPTU).",
    "2,8 a 5,5 s · No cenário base, o saldo chega a R$ 37.720 em set/27. · Tela real da Simulação futura.",
    "5,5 a 8,2 s · Em janeiro, IPVA e IPTU somam R$ 4.800. · O ajuste de janeiro de 2027 em destaque.",
    "8,2 a 11 s · A 1ª parcela do 13º é metade do salário: R$ 4.980.",
    "11 a 13,8 s · Só em nov/26: R$ 9.960 + R$ 4.980 = R$ 14.940. · Tela real do ajuste “Só em” na receita.",
    "13,8 a 16,7 s · Guardada, a parcela leva o saldo final a R$ 42.700.",
    "16,7 a 20,8 s · Guardada, a 1ª parcela cobre o janeiro caro. · +R$ 4.980 (1ª parcela do 13º, nov/26) · −R$ 4.800 (IPVA e IPTU, jan/27) · +R$ 180 ainda sobra. · Lei 4.749/1965: a 1ª parcela, metade do salário do mês anterior, sai entre fevereiro e novembro; o 13º inteiro, até 20 de dezembro. Valores da conta de exemplo.",
    "20,8 a 24 s · Fechamento (verde) · Simulação futura no timtimcash · Link na bio.",
], legenda=(
    "O 13º vem aí. Antes de ele cair na conta, vale ver o que ele muda no seu saldo.\n\n"
    "Pela lei, a primeira parcela do 13º, metade do salário do mês anterior, é paga entre fevereiro e novembro, e o 13º inteiro até 20 de dezembro. "
    "No exemplo do vídeo, com salário de R$ 9.960, a primeira parcela é de R$ 4.980.\n\n"
    "Na Simulação futura do timtimcash, basta um ajuste “Só em” novembro na receita. Guardada, a parcela leva o saldo final de R$ 37.720 para R$ 42.700 "
    "e cobre os R$ 4.800 de IPVA e IPTU de janeiro do exemplo.\n\n"
    f"{TELA}\n\n{FIM}\n\n"
    "#decimoterceiro #planejamentofinanceiro #financaspessoais #educacaofinanceira #timtimcash"
), justificativa=[
    ("Por que agora", "Fim de outubro, um mês antes do prazo da primeira parcela: dá tempo de decidir o destino do dinheiro antes de ele cair na conta."),
    ("O que desperta interesse", "Um tema de fim de ano que mexe com o planejamento de quem recebe o 13º, e uma conta simples que fecha na tela: R$ 4.980 cobrem R$ 4.800."),
    ("Benefício para o público", "A pessoa entende os prazos da lei e vê, antes de o dinheiro chegar, o efeito de guardar a primeira parcela."),
    ("Como contribui para o perfil", "Fecha outubro com planejamento para o fim do ano e mostra o ajuste de um mês na Simulação futura, que ainda não tinha aparecido no perfil."),
], alt=["Reel de 24 segundos. O 13º vem aí. O que ele muda no seu saldo? Telas reais da Simulação futura do timtimcash no celular, com dados de exemplo. No cenário base, o saldo chega a R$ 37.720 em setembro de 2027. Em janeiro, IPVA e IPTU somam R$ 4.800. A primeira parcela do 13º é metade do salário: R$ 4.980. Com o ajuste só em novembro de 2026, a receita do mês vai a R$ 14.940, e o saldo final sobe para R$ 42.700. Guardada, a primeira parcela cobre o janeiro caro e ainda sobram R$ 180. Pela Lei 4.749 de 1965, a primeira parcela sai entre fevereiro e novembro e o 13º inteiro até 20 de dezembro. Simulação futura no timtimcash. Link na bio."],
fontes=[("Planalto · Lei nº 4.749, de 12 de agosto de 1965 (13º salário, arts. 1º e 2º)", "https://www.planalto.gov.br/ccivil_03/leis/l4749.htm")],
telas=["capturas do cenário base e do ajuste “Só em” de nov/26 (reels-c/capturas/13)"])
REELS.append(p)

for post in REELS:
    arq = os.path.join(O, "dados", post["pasta"] + ".py")
    open(arq, "w", encoding="utf-8").write("# -*- coding: utf-8 -*-\n\"\"\"Reel de outubro de 2026 · dados para o arquivo de aprovação e o agendamento.\"\"\"\n\nPOST = " + pprint.pformat(post, width=140, sort_dicts=False) + "\n")
    txt = open(arq, encoding="utf-8").read()
    assert "\u2014" not in txt and "\u2013" not in txt, arq
    print("ok", arq.split("/")[-1], post["formato_curto"])
