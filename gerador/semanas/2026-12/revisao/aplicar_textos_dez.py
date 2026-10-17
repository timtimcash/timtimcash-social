# -*- coding: utf-8 -*-
"""Correções de texto da revisão de dezembro (16/10/2026). Cada troca precisa acontecer o número exato de vezes."""
import os, sys
N = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(N, "dados")

TROCAS = {
"2026-12-12_oito-siglas-do-seu-dinheiro.py": [
 ("- Rotativo: Resolução CMN nº 4.549/2017, arts. 1º e 2º (o saldo não pago só pode ser financiado no rotativo até o vencimento\n"
  "  da fatura seguinte; depois, pode ir para um parcelamento); taxa média de agosto de 2026, 15,18% ao mês (SGS 25477, FATOS.md).",
  "- CET: Resolução CMN nº 4.881/2020 (\"Dispõe sobre o cálculo e a informação do Custo Efetivo Total (CET)\"): art. 3º, o CET\n"
  "  considera juros, tarifas, tributos, seguros e outras despesas cobradas do tomador; art. 4º, parágrafo único, taxa percentual\n"
  "  anual; art. 7º, informado antes da contratação. Conferido no PDF do Banco Central em 16/10/2026. Na revisão de 16/10, o CET\n"
  "  entrou no lugar do rotativo, que não é sigla.", 1),
 ("Selic, IPCA e rotativo não aparecem no site", "Selic, IPCA e CET não aparecem no site", 1),
 ("PTAX, CDI, Selic, IPCA, IOF, VET, TIR e rotativo, uma frase", "PTAX, CDI, Selic, IPCA, IOF, VET, TIR e CET, uma frase", 1),
 ("IPCA, IOF, VET; TIR, rotativo.\"", "IPCA, IOF, VET; TIR, CET.\"", 1),
 ("\"CUSTOS · Um imposto e o crédito mais caro. · IOF, imposto sobre operações financeiras: incide sobre crédito, câmbio, seguro e títulos e valores mobiliários. No dia a dia: 3,5% numa compra com cartão no exterior; 1,10% numa remessa para investir. · rotativo, do cartão de crédito: o crédito que entra quando a fatura não é paga inteira; vai até a fatura seguinte; depois, o saldo pode ser parcelado. No dia a dia: taxa média de 15,18% ao mês em agosto de 2026. · Nota: Fontes: Decreto 6.306/2007, art. 15-B (Decreto 12.499/2025); Res. CMN 4.549/2017; Banco Central.\"",
  "\"CUSTOS · Um imposto e o custo total do crédito. · IOF, imposto sobre operações financeiras: incide sobre crédito, câmbio, seguro e títulos e valores mobiliários. No dia a dia: 3,5% numa compra com cartão no exterior; 1,10% numa remessa para investir. · CET, custo efetivo total: soma juros, tarifas, tributos, seguros e outras despesas de um crédito, numa taxa ao ano; o banco informa antes de contratar. No dia a dia: duas propostas com os mesmos juros podem ter CET diferente; compare pelo CET. · Nota: Fontes: Decreto 6.306/2007, art. 15-B (Decreto 12.499/2025); Res. CMN 4.881/2020, arts. 3º, 4º e 7º.\"", 1),
 ("\"Oito siglas que aparecem no extrato, no noticiário e no câmbio. Salve para consultar.\\n\\n\"",
  "\"Oito siglas do extrato, do noticiário, do câmbio e do crédito. Salve para consultar.\\n\\n\"", 1),
 ("\"· Rotativo: o crédito da fatura que não foi paga inteira; média de 15,18% ao mês em agosto de 2026.\\n\\n\"",
  "\"· CET: o custo efetivo total de um crédito, com juros, tarifas, tributos e seguros, numa taxa ao ano; compare antes de contratar.\\n\\n\"", 1),
 ("\"Fontes: Banco Central; B3; IBGE; Decreto 6.306/2007.\\n\\n\"", "\"Fontes: Banco Central; B3; IBGE; Decreto 6.306/2007; Res. CMN 4.881/2020.\\n\\n\"", 1),
 ("(Banco Central, B3, IBGE, decreto do IOF)", "(Banco Central, B3, IBGE, decreto do IOF e resolução do CET)", 1),
 ("com as siglas PTAX, CDI, Selic, IPCA, IOF, VET, TIR e rotativo.\"", "com as siglas PTAX, CDI, Selic, IPCA, IOF, VET, TIR e CET.\"", 1),
 ("\"Custos: um imposto e o crédito mais caro. IOF, imposto sobre operações financeiras: incide sobre crédito, câmbio, seguro e títulos e valores mobiliários; por exemplo, 3,5% numa compra com cartão no exterior e 1,10% numa remessa para investir. Rotativo do cartão de crédito: o crédito que entra quando a fatura não é paga inteira, vai até a fatura seguinte e depois o saldo pode ser parcelado; a taxa média foi de 15,18% ao mês em agosto de 2026.\"",
  "\"Custos: um imposto e o custo total do crédito. IOF, imposto sobre operações financeiras: incide sobre crédito, câmbio, seguro e títulos e valores mobiliários; por exemplo, 3,5% numa compra com cartão no exterior e 1,10% numa remessa para investir. CET, custo efetivo total: soma juros, tarifas, tributos, seguros e outras despesas de um crédito, numa taxa ao ano, e o banco informa antes de contratar; duas propostas com os mesmos juros podem ter CET diferente, então compare pelo CET.\"", 1),
 ("        (\"Banco Central · Resolução CMN nº 4.549/2017, arts. 1º e 2º (rotativo até o vencimento da fatura seguinte; depois, parcelamento)\", \"https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50330/Res_4549_v2_L.pdf\"),\n"
  "        (\"Banco Central · Estatísticas monetárias e de crédito, nota de 29/9/2026 (rotativo, 15,18% ao mês em agosto de 2026; SGS 25477)\", \"https://www.bcb.gov.br/content/estatisticas/hist_estatisticasmonetariascredito/202609_Texto_de_estatisticas_monetarias_e_de_credito.pdf\"),\n",
  "        (\"Banco Central · Resolução CMN nº 4.881/2020, arts. 3º, 4º e 7º (CET: juros, tarifas, tributos, seguros e outras despesas, em taxa percentual anual, informado antes da contratação)\", \"https://www.bcb.gov.br/content/estabilidadefinanceira/especialnor/Resolu%C3%A7%C3%A3o4881.pdf\"),\n", 1),
],
"2026-12-18_patrimonio-quanto-voce-tem.py": [
 ("NO TIMTIMCASH · Contas e carteiras soma tudo.", "NO TIMTIMCASH · Contas e carteiras: tudo somado.", 1),
 ("Saiba quanto você tem, de verdade. · Contas e carteiras e Remessas ao exterior no timtimcash, no computador ou no celular.",
  "Saiba quanto você tem, de verdade. · Contas, carteiras e remessas no timtimcash, no computador ou no celular.", 1),
 ("No timtimcash, Contas e carteiras soma tudo. Tela real", "No timtimcash, Contas e carteiras: tudo somado. Tela real", 1),
 ("Saiba quanto você tem, de verdade. Contas e carteiras e Remessas ao exterior no timtimcash, no computador ou no celular. Link na bio.",
  "Saiba quanto você tem, de verdade. Contas, carteiras e remessas no timtimcash, no computador ou no celular. Link na bio.", 1),
],
"2026-12-23_viagem-para-fora-o-iof.py": [
 ("Os US$ 1.000 com IOF, arredondados, dão R$ 5.300. · Tela real", "Os US$ 1.000 com IOF, e uma folga, dão R$ 5.300. · Tela real", 1),
 ("O que muda é o câmbio e as tarifas: ", "O que muda são o câmbio e as tarifas: ", 1),
 ("os US$ 1.000 com IOF, arredondados, dão R$ 5.300. Tela real", "os US$ 1.000 com IOF, e uma folga, dão R$ 5.300. Tela real", 1),
],
"2026-12-06_reel-seu-2026-em-5-numeros.py": [
 ("rendeu lá fora em 2026, em dólar · +3,0% em US$ · em reais, com o câmbio: −6,2% · Recorte",
  "rendeu lá fora em 2026, em dólar · Taxa ao ano: +3,0% em US$ · −6,2% em reais · Recorte", 1),
 ("\"4. Lá fora, a carteira rendeu US$ 350 em 2026, ou 3,0% em dólar. Em reais, com o dólar mais barato, o ano está em −6,2%.\\n\"",
  "\"4. Lá fora, a carteira rendeu US$ 350 em 2026, numa taxa de 3,0% ao ano em dólar. Em reais, com o dólar mais barato, a taxa do ano está em −6,2%.\\n\"", 1),
 ("mais 350 dólares lá fora em 2026, 3,0% em dólar e menos 6,2% em reais por causa do câmbio,",
  "mais 350 dólares lá fora em 2026, numa taxa de 3,0% ao ano em dólar e de menos 6,2% em reais por causa do câmbio,", 1),
],
"2026-12-17_reel-dolar-e-euro.py": [
 ("9,9 a 12,4 s · O euro caiu desde o envio: de R$ 5,7627 para R$ 5,6592. · Painel",
  "9,9 a 12,4 s · Pagou R$ 5,7627 por euro, com IOF. Hoje: R$ 5,6592. · Painel", 1),
 ("\"O euro conta outra história. Os € 2.000 enviados em 1º de dezembro viraram € 2.012: +0,6% em euro. Em reais, −1,2%, porque \"\n"
  "        \"o euro caiu de R$ 5,7627, o câmbio efetivo do envio (com IOF), para R$ 5,6592.\\n\\n\"",
  "\"O euro conta outra história. Os € 2.000 enviados em 1º de dezembro viraram € 2.012: +0,6% em euro. Em reais, −1,2%: \"\n"
  "        \"o envio custou R$ 5,7627 por euro, já com o IOF, e hoje o euro vale R$ 5,6592.\\n\\n\"", 1),
 ("O painel De onde veio o resultado em reais explica que o câmbio caiu de R$ 5,7627 para \"\n"
  "        \"R$ 5,6592 e devolveu R$ 207.",
  "O título diz que o envio custou R$ 5,7627 por euro, com IOF, e que hoje o euro vale \"\n"
  "        \"R$ 5,6592; o painel De onde veio o resultado em reais mostra que o câmbio devolveu R$ 207.", 1),
],
"2026-12-07_janeiro-caro-o-que-chega-junto.py": [
 ("Na conta do exemplo, janeiro só perde para dezembro: em 2026, levou R$ 9.420, com IPVA e IPTU.",
  "Na conta do exemplo, janeiro só perde para dezembro, o mês das festas: em 2026, levou R$ 9.420, com IPVA e IPTU.", 1),
],
"2026-12-10_o-preco-do-dinheiro-emprestado.py": [
 ("No timtimcash, lance o empréstimo como Parcelada em Dívidas e empréstimos: cada parcela aparece em Pendentes.",
  "No timtimcash, lance o total do empréstimo em Dívidas e empréstimos, com a Recorrência Parcelada: cada parcela aparece em Pendentes no mês dela.", 1),
],
"2026-12-27_reel-o-que-mudou-no-seu-ano.py": [
 ("Mercado: +R$ 441,93 acima da média (+29%).", "Mercado: R$ 441,93 acima da média (+29%).", 1),
 ("Lazer e hobbies: −R$ 311,60 (−77%).", "Lazer e hobbies: R$ 311,60 abaixo da média (−77%).", 1),
],
"2026-12-28_anote-quanto-ha-la-fora.py": [
 ("o dólar de fechamento do exemplo caiu de R$ 6,1917 para R$ 5,5018.",
  "a PTAX de compra do fim do ano caiu de R$ 6,1917 (2024) para R$ 5,5018 (2025).", 1),
 ("Fontes: Receita Federal (Perguntas e Respostas IRPF 2026); Lei 14.754/2023.",
  "Fontes: Receita Federal (Perguntas e Respostas IRPF 2026; taxas de câmbio para fins fiscais); Lei 14.754/2023.", 1),
 ("(\"Receita Federal · Taxas de câmbio para fins fiscais (PTAX de compra do último dia útil de 2023 e de 2024, como em FATOS.md)\", \"https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/ecf/taxas-de-cambio-incluindo-valor-do-dolar-para-fins-fiscais-irpj\")",
  "(\"Receita Federal · Taxas de câmbio para fins fiscais, anos anteriores: dólar, compra, R$ 4,8407 em 29/12/2023, R$ 6,1917 em 31/12/2024 e R$ 5,5018 em 31/12/2025 (conferido em 16/10/2026)\", \"https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/ecf/taxas-de-cambio-incluindo-valor-do-dolar-para-fins-fiscais-irpj-AC-anteriores\")", 1),
],
}

erros = 0
for arq, trocas in TROCAS.items():
    cam = os.path.join(D, arq)
    txt = open(cam, encoding="utf-8").read()
    for velho, novo, n in trocas:
        achou = txt.count(velho)
        if achou != n:
            print(f"ERRO {arq}: esperava {n}, achou {achou}: {velho[:90]!r}")
            erros += 1
            continue
        txt = txt.replace(velho, novo)
    if not erros:
        open(cam, "w", encoding="utf-8").write(txt)
        print("ok", arq)
sys.exit(1 if erros else 0)
