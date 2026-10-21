# -*- coding: utf-8 -*-
"""Quarta 13/01/2027 · Reel "IPVA: 3% de desconto vale quanto ao mês?" (educação, impostos, com fonte oficial e produto; capa verde
suave). Equipe jr. Vídeo, capa e prévia gerados por equipes/jr/reel_13.py (a regra e a Selic ficam num lugar só, REGRA e SELIC, no
topo do roteiro; a conta tem assert). Tela capturada por equipes/jr/captura_13.py no site build 2026-10-19.5, na cópia da conta da
equipe (igual à da base, sem mudança), no celular (390 × 1000 em escala 3), relógio da página em 13/01/2027 10:00: Pendentes de
janeiro, “EM 7 DIAS · 20/01/2027”, “IPVA 2027 · Impostos e Taxas · Conta corrente · −R$ 1.236,00 · pendente”.
Fatos (FATOS.md, conferidos em 20/10/2026): Decreto estadual 70.087, de 12/11/2025 (IPVA 2026 de SP): veículo usado à vista em janeiro
com 3% de desconto (art. 1º; não vale para veículo com alíquota reduzida), ou 5 parcelas mensais de janeiro a maio, sem desconto, para
débito de 10 UFESPs ou mais (art. 3º). O decreto do IPVA 2027 não tinha saído em 20/10/2026 (os três anteriores saíram entre 12/11 e
12/12, todos com 3%). Selic: 13,75% ao ano, decisão do Copom de 16/09/2026 (Relatório de Política Monetária de setembro de 2026);
ao mês, a comparação é aproximada, pela Selic acumulada em setembro de 2026, 1,08% (série 4390 do Banco Central), como pede a nota do
revisor no fim de FATOS.md (o vídeo e a legenda dizem a data da decisão e chamam o número ao mês de aproximado).
A conta (assert no gerador; é cálculo nosso, não fonte oficial): IPVA 2027 do exemplo à vista R$ 1.236,00 (conta de exemplo, 20/01);
valor cheio 1.236 ÷ 0,97 = R$ 1.274,23; desconto 3% = R$ 38,23; parcelas 1.274,23 ÷ 5 = R$ 254,85 (254,846). Taxa implícita, com a 1ª
parcela no dia do pagamento à vista e as outras de mês em mês: 1.236 = Σ 254,846 ÷ (1 + i)^k, k = 0 a 4 -> i = 1,547% ao mês
(1,548% com as parcelas arredondadas) -> 20,22% ao ano. Na tela: 1,55% ao mês e 20,2% ao ano. 1,55% > cerca de 1,08%: com o dinheiro
na mão, pagar à vista rende mais que a Selic ao mês (antes do IR, que reduziria ainda mais o rendimento).
ANTES DE AGENDAR: conferir o decreto do IPVA 2027 de SP (desconto, parcelas, meses) e a meta da Selic (há Copom em 03-04/11 e
08-09/12/2026 e em 26-27/01/2027) com a Selic acumulada mais recente. Trocar só REGRA e SELIC em reel_13.py, refazer o vídeo e
ajustar esta legenda.
Diferença do que já saiu: 07/12 (janeiro caro) listou IPVA, IPTU e material; 10/12 comparou juros de crédito. Aqui é a conta do
desconto à vista contra o parcelamento, em taxa ao mês, comparada com a Selic."""

POST = {
    "pasta": "2027-01-13_reel-ipva-desconto-a-vista",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "IPVA: quanto vale ao mês o desconto de 3% à vista. No exemplo, R$ 1.236,00 à vista em janeiro ou 5 parcelas de R$ 254,85 (valor cheio R$ 1.274,23): parcelar custa o equivalente a 1,55% ao mês (20,2% ao ano), mais que a Selic de 13,75% ao ano (Copom, 16/09/2026), cerca de 1,08% ao mês; regra de São Paulo em 2026 (Decreto 70.087/2025)",
    "pilar": "Educação · impostos (IPVA), com fonte oficial e produto (Pendentes)",
    "data_longa": "quarta-feira, 13 de janeiro de 2027",
    "data_curta": "quarta-feira, 13/01/2027",
    "data_mockup": "13 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-13T10:00:00",
    "video": "saida/2027-01-13_reel-ipva-desconto-a-vista/reel.mp4",
    "capa": "saida/2027-01-13_reel-ipva-desconto-a-vista/capa.jpg",
    "previa": "saida/2027-01-13_reel-ipva-desconto-a-vista/previa.mp4",
    "slides": [
        "Capa da grade (verde suave) · IPVA · 3% vale quanto? · O número “1,55%” enorme, em verde profundo, e “ao mês” embaixo.",
        "0 a 3,2 s · Gancho (papel) · IPVA · SÃO PAULO · 3% de desconto vale quanto ao mês? · Desde o primeiro quadro, o número conta até 1,55% (em verde) e “ao mês”; depois, “No IPVA do exemplo: à vista com 3% ou em 5 parcelas.” e a pílula “≈ 20,2% ao ano”.",
        "3,3 a 6,4 s · O IPVA do exemplo, de dois jeitos: · Dois cartões: “À vista, em janeiro” R$ 1.236,00, com 3% de desconto; “Em 5 parcelas, de janeiro a maio” 5 × R$ 254,85, valor cheio R$ 1.274,23. · Regra de São Paulo para o IPVA 2026 (Decreto 70.087/2025).",
        "6,5 a 9,7 s · Parcelar custa 1,55% ao mês. · Os meses de janeiro a maio: à vista, um bloco verde de 1.236 em janeiro; parcelado, cinco blocos coral de 254,85. · Quem parcela abre mão de R$ 38,23 de desconto e paga aos poucos. · Pílula: ≈ 20,2% ao ano.",
        "9,8 a 13,3 s · E o dinheiro guardado, rende quanto? · Duas barras: Selic, 13,75% ao ano, ≈ 1,08% (verde); Parcelar o IPVA, 1,55% (coral). · Ao mês. Selic de 13,75% ao ano, decisão do Copom de 16/09/2026; ao mês, cerca de 1,08% (Selic acumulada em setembro de 2026, série 4390 do Banco Central). · Com o dinheiro na mão, o desconto rende mais.",
        "13,4 a 16,3 s · No exemplo, o IPVA à vista já está em Pendentes. · Tela real de Pendentes no celular (13/01/2027), com anel em “EM 7 DIAS · 20/01/2027” e na linha “IPVA 2027 · −R$ 1.236,00 · pendente”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "16,4 a 18,4 s · Regra de SP em 2026: confira a sua. · Ícone de documento · Decreto 70.087/2025: 3% à vista em janeiro ou até 5 parcelas, de janeiro a maio. Confira a regra de 2027 e a do seu estado.",
        "18,5 a 21,2 s · Fechamento (verde) · Pendentes no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "3% de desconto vale quanto ao mês?\n\n"
        "No exemplo do vídeo, o IPVA à vista em janeiro, com 3% de desconto, sai por R$ 1.236,00. Parcelado em 5 vezes, de janeiro a maio, vale o valor cheio: R$ 1.274,23, ou cerca de R$ 254,85 por parcela.\n\n"
        "Quem parcela abre mão de R$ 38,23 e paga aos poucos. Na conta, é como pagar 1,55% ao mês, cerca de 20,2% ao ano. Para comparar, o Copom fixou a Selic em 13,75% ao ano em 16/09/2026, cerca de 1,08% ao mês. Com o dinheiro na mão, o desconto rende mais.\n\n"
        "Regra de São Paulo para o IPVA 2026 (Decreto 70.087/2025): 3% à vista em janeiro para veículo usado, ou até 5 parcelas sem desconto. Confira a regra de 2027 e a do seu estado.\n\n"
        "No timtimcash, o IPVA à vista fica em Pendentes, com a data de pagamento.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Decreto estadual 70.087/2025 (SP); Banco Central (Copom de 16/09/2026; Selic acumulada no mês, série 4390).\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#ipva #ipva2027 #educacaofinanceira #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Meados de janeiro, época do IPVA em São Paulo (em 2026, o pagamento à vista com desconto venceu de 12 a 23/01, pelo final da placa), quando a pessoa decide entre pagar de uma vez ou parcelar."),
        ("O que desperta interesse", "Uma pergunta que pouca gente faz (quanto vale o desconto ao mês) e a resposta já no primeiro segundo, 1,55% ao mês, acima da Selic ao mês."),
        ("Benefício para o público", "Aprende a transformar um desconto à vista em taxa ao mês e a comparar com o que o dinheiro rende, com a regra oficial do estado e o aviso para conferir a de 2027."),
        ("Como contribui para o perfil", "Reforça o pilar de educação com fonte oficial (decreto e Banco Central) e mostra em tela real o IPVA em Pendentes, com a data certa."),
    ],
    "alt": [
        "Reel de 21 segundos. Num fundo claro, a pergunta 3% de desconto vale quanto ao mês? e um número que conta até 1,55% ao mês, cerca de 20,2% ao ano. "
        "Dois cartões mostram o IPVA do exemplo: à vista em janeiro, R$ 1.236,00, com 3% de desconto; ou 5 parcelas de R$ 254,85, de janeiro a maio, com valor cheio de R$ 1.274,23; regra de São Paulo para o IPVA 2026, Decreto 70.087/2025. "
        "Uma grade de janeiro a maio compara um bloco verde à vista com cinco blocos coral das parcelas: parcelar custa 1,55% ao mês, e quem parcela abre mão de R$ 38,23. "
        "Duas barras comparam a Selic, de 13,75% ao ano pela decisão do Copom de 16/09/2026, cerca de 1,08% ao mês, com o custo de parcelar, 1,55%: com o dinheiro na mão, o desconto rende mais. "
        "Na tela real de Pendentes do timtimcash, com dados de exemplo, o IPVA 2027 de R$ 1.236,00 vence em 7 dias, em 20/01/2027. Por fim, o aviso: regra de SP em 2026, confira a de 2027 e a do seu estado. Pendentes no timtimcash. Link na bio."
    ],
    "fontes": [
        ("Alesp · Decreto estadual nº 70.087, de 12/11/2025 (IPVA 2026: 3% de desconto à vista em janeiro, art. 1º; 5 parcelas de janeiro a maio, art. 3º)",
         "https://www.al.sp.gov.br/repositorio/legislacao/decreto/2025/decreto-70087-12.11.2025.html"),
        ("Banco Central · Relatório de Política Monetária de setembro de 2026 (meta da Selic de 13,75% ao ano, decisão do Copom de 16/09/2026, reunião de 15 e 16/09)",
         "https://www.bcb.gov.br/content/ri/relatorioinflacao/202609/rpm202609p.pdf"),
        ("Banco Central · SGS 4390, Selic acumulada no mês: 1,08% em setembro de 2026, usada como aproximação ao mês (lido em 20/10/2026)",
         "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json"),
        ("Sefaz-SP · página do IPVA (o calendário de 2027 ainda não estava publicado em 20/10/2026)", "https://portal.fazenda.sp.gov.br/servicos/ipva"),
    ],
    "telas": [
        "telas/a-pendentes-janeiro.jpg · Pendentes no celular (390 × 1000), Janeiro 2027, site build 2026-10-19.5, cópia da conta sem mudança, relógio em 13/01/2027 10:00: “A pagar R$ 1.659,90 · 4 transações”, “Nada vencido. Tudo dentro do prazo.”, “EM 7 DIAS · 20/01/2027”: Armazenamento na nuvem −R$ 42,00 e IPVA 2027 −R$ 1.236,00, pendente · 13,4 a 16,3 s",
        "telas/caixas.json · posições medidas na captura e o texto da tela, usados nos anéis e nos assert do roteiro",
    ],
}
