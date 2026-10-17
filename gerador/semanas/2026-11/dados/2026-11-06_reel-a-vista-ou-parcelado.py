# -*- coding: utf-8 -*-
"""Sexta 06/11/2026 · Reel "10% à vista ou 10x sem juros?" (educação: conta rápida, véspera da Black Friday; capa tinta). Equipe r1b (a partir da r1).
Vídeo, capa e prévia gerados por equipes/r1b/reel_06.py (mesmas contas e mesmo roteiro da r1, com os gráficos maiores). Sem tela real.
Contas feitas no gerador, com assert: preço R$ 1.000; à vista R$ 900 (10% de desconto); 10 parcelas de R$ 100, a 1ª em 30 dias.
Juro embutido: a taxa que faz R$ 900 hoje valerem 10 × R$ 100 é de 1,96% ao mês (26,3% ao ano); com a 1ª parcela no ato, 2,42% ao mês.
Com rendimento de 1% ao mês, as 10 parcelas valem hoje R$ 947,13: o desconto que empata é de 5,3% (FATOS.md, contas de exemplo).
Dado do Procon-SP em FATOS.md (consulta divulgada em 26/11/2025: 329 consumidores, 42,55%)."""

POST = {
    "pasta": "2026-11-06_reel-a-vista-ou-parcelado",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "10% à vista ou 10x sem juros? Num exemplo de R$ 1.000, o “sem juros” embute 1,96% ao mês; com o dinheiro rendendo 1% ao mês, à vista ganha, e um desconto acima de 5,3% vence o parcelado",
    "pilar": "Educação (conta rápida, véspera da Black Friday)",
    "data_longa": "sexta-feira, 6 de novembro de 2026",
    "data_curta": "sexta-feira, 06/11/2026",
    "data_mockup": "6 de novembro",
    "hora": "10h00",
    "iso": "2026-11-06T10:00:00",
    "video": "saida/2026-11-06_reel-a-vista-ou-parcelado/reel.mp4",
    "capa": "saida/2026-11-06_reel-a-vista-ou-parcelado/capa.jpg",
    "previa": "saida/2026-11-06_reel-a-vista-ou-parcelado/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · CONTA RÁPIDA · 10% à vista ou 10x sem juros? · As duas etiquetas penduradas num trilho, “R$ 900 à vista” (verde suave) e “10x de R$ 100 sem juros” (âmbar suave), com um “?” verde entre elas.",
        "0 a 2,4 s · Gancho · Qual sai mais barato? · As duas etiquetas entram de lados opostos e balançam no trilho, já no primeiro quadro. · Preço cheio: R$ 1.000.",
        "2,4 a 6,2 s · À vista, R$ 900 hoje. Parcelado, R$ 100 por mês, por 10 meses. · Linha do tempo: a barra verde de R$ 900 no “hoje” e 10 blocos âmbar de R$ 100 caindo, um por mês, do 1 ao 10.",
        "6,2 a 10,2 s · Parcelar é ficar com R$ 900 hoje e devolver R$ 1.000 em 10 meses. · Os blocos voam e se empilham numa torre de R$ 1.000 ao lado da de R$ 900 (chave: +R$ 100); um contador sobe até 1,96% ao mês · o juro embutido no “sem juros” · 26,3% ao ano.",
        "10,2 a 14,2 s · Seu dinheiro rende 1% ao mês? · Régua de 0% a 2,5% ao mês: o pino de 1% (seu rendimento) para abaixo do pino de 1,96% (juro do parcelado), e a diferença fica em âmbar. · Selo “À vista ganha” · Rendendo menos que o juro embutido, o desconto de 10% vale mais que parcelar.",
        "14,2 a 17,3 s · Desconto acima de 5,3% vence um rendimento de 1% ao mês. · Barra de 0% a 10%: “parcelar pode valer” até 5,3% e “à vista ganha” acima, com a marca do exemplo em 10%. · No exemplo, o desconto é de 10%: à vista ganha. Exemplo ilustrativo, com a 1ª parcela em 30 dias.",
        "17,3 a 20 s · Fechamento (verde) · Faça a conta antes de parcelar. · Lance a compra parcelada e veja cada parcela no seu mês. · Link na bio.",
    ],
    "legenda": (
        "10% à vista ou 10x “sem juros”: qual sai mais barato?\n\n"
        "A conta, num exemplo ilustrativo: um produto de R$ 1.000 sai por R$ 900 à vista ou em 10 parcelas de R$ 100, a primeira em 30 dias. "
        "Parcelar é ficar com R$ 900 hoje e devolver R$ 1.000 em 10 meses: um juro de 1,96% ao mês (26,3% ao ano), embutido no “sem juros”.\n\n"
        "Se o seu dinheiro rende 1% ao mês, à vista ganha. A regra do exemplo: com esse rendimento, um desconto acima de 5,3% vale mais que parcelar. "
        "Se a primeira parcela for no ato, o juro embutido sobe para 2,42% ao mês.\n\n"
        "Vale fazer a conta antes da Black Friday: numa consulta do Procon-SP com 329 consumidores, 42,55% descobriram depois que o “parcelamento sem juros” tinha juros.\n\n"
        "Se parcelar, lance a compra parcelada no timtimcash e veja cada parcela no seu mês.\n\n"
        "Fonte: Procon-SP, consulta divulgada em 26/11/2025.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#blackfriday #juros #educacaofinanceira #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Sexta-feira, três semanas antes da Black Friday (27/11): as ofertas começam e a dúvida entre o desconto à vista e o parcelado aparece no caixa."),
        ("O que desperta interesse", "Uma pergunta de todo dia, com duas etiquetas balançando no primeiro segundo; a resposta cabe no vídeo: o “sem juros” do exemplo embute 1,96% ao mês."),
        ("Benefício para o público", "Aprende a comparar o desconto à vista com o rendimento do próprio dinheiro e leva uma regra de bolso: com 1% ao mês de rendimento, desconto acima de 5,3% vence o parcelado."),
        ("Como contribui para o perfil", "Educação financeira com conta conferida e fonte oficial (Procon-SP), no tom do perfil, ligada à função de compra parcelada do timtimcash sem prometer nada além dela."),
    ],
    "alt": [
        "Reel de 20 segundos. Qual sai mais barato? Duas etiquetas balançam num trilho: R$ 900 à vista e 10 vezes de R$ 100 sem juros, para um preço cheio de R$ 1.000. "
        "Numa linha do tempo, a barra de R$ 900 hoje e dez blocos de R$ 100, um por mês. Os blocos se empilham numa torre de R$ 1.000, cem reais acima da de R$ 900, e um contador mostra o juro embutido no sem juros: 1,96% ao mês, 26,3% ao ano. "
        "Numa régua, um rendimento de 1% ao mês fica abaixo de 1,96%: à vista ganha. A regra do exemplo: desconto acima de 5,3% vence um rendimento de 1% ao mês; no exemplo, o desconto é de 10%. "
        "Exemplo ilustrativo, com a primeira parcela em 30 dias. Faça a conta antes de parcelar. Lance a compra parcelada e veja cada parcela no seu mês. Link na bio."
    ],
    "fontes": [
        ("Procon-SP · Consulta inédita sobre a Black Friday, divulgada em 26/11/2025 (329 consumidores; 42,55% descobriram depois que o “parcelamento sem juros” tinha juros)",
         "https://www.procon.sp.gov.br/consulta-inedita-do-procon-sp-revela-que-consumidores-desconfiam-das-ofertas-mas-reagem-aos-gatilhos-de-marketing-da-black-friday/"),
    ],
    "telas": [],
}
