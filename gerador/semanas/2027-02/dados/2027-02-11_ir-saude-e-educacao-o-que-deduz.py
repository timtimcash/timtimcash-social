# -*- coding: utf-8 -*-
"""Quinta 11/02/2027 · carrossel "Saúde e educação: o que entra no IR?" (educação, IR, capa verde suave). Equipe fa.
Artes: saida/2027-02-11_ir-saude-e-educacao-o-que-deduz/01.jpg a 07.jpg, geradas por equipes/fa/posts.py (post_ir).
Telas reais em saida/2027-02-11_ir-saude-e-educacao-o-que-deduz/telas/, capturadas por equipes/fa/captura.py na cópia
da conta (igual à base, sem mudança), build 2026-10-19.5, relógio em 11/02/2027 10:00.

Fatos (FATOS.md, seção 5, e notas do revisor): Lei 9.250/1995, art. 8º, II, "a": dedução sem limite de valor para
médicos, dentistas, psicólogos, fisioterapeutas, fonoaudiólogos, terapeutas ocupacionais, hospitais, exames
laboratoriais, serviços radiológicos, aparelhos ortopédicos e próteses ortopédicas e dentárias; § 2º, I: plano de
saúde; II: só o tratamento do contribuinte e dos dependentes; IV: despesa reembolsada não entra. Remédio de farmácia
não está na lista da lei (a exceção da conta do hospital NÃO é afirmada: a pergunta 392 do P&R não pôde ser lida).
Receita Federal (perguntas frequentes do IRPF): teste de Covid feito em farmácia não entra; uniforme, material,
transporte escolar, idioma e cursos preparatórios não entram; música, dança, natação, ginástica e tênis não entram;
declarar o valor total da educação, mesmo acima do limite. Limite de educação: R$ 3.561,50 por pessoa no ano (Lei
9.250/1995, art. 8º, II, "b", 10; vale para o ano-calendário 2026, página "Tributação de 2026" da Receita).
Números das telas (asserts em posts.py): Transações, Ano 2026, busca "exame": 1 transação, R$ 150,00 (Exame de rotina,
24/09/2026); busca "farmácia": 23 transações, R$ 3.279,44; categoria Educação: 12 transações, R$ 17.400,00 (Escola,
12 × R$ 1.450). Acima do limite: 17.400 − 3.561,50 = R$ 13.838,50.
O post diz, no slide 6 e na legenda, que o timtimcash organiza os números e não faz a declaração, e pede para conferir
com um contador."""

POST = {
    "pasta": "2027-02-11_ir-saude-e-educacao-o-que-deduz",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Saúde e educação no IR de 2027: o que a lei deixa deduzir em saúde (sem limite, só a lista), o que fica de fora (remédio de farmácia, teste em farmácia, o reembolsado), o limite de R$ 3.561,50 por pessoa na educação e o que não entra, com duas buscas em Transações no Ano 2026 e o aviso para conferir com um contador",
    "pilar": "Educação · imposto de renda, com fonte oficial e produto",
    "data_longa": "quinta-feira, 11 de fevereiro de 2027",
    "data_curta": "quinta-feira, 11/02/2027",
    "data_mockup": "11 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-11T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · IMPOSTO DE RENDA · Saúde e educação: o que entra no IR? · Dois recibos desenhados, inclinados: o da esquerda (Consulta, Exame) com um visto verde no canto; o da direita (Farmácia, Remédio) com os itens riscados, um traço coral atravessado e um X coral no canto.",
        "SAÚDE · SEM LIMITE DE VALOR · Entra o que está na lista da lei. · Doze selos com visto: Médicos, Dentistas, Psicólogos, Fisioterapeutas, Fonoaudiólogos, Terapeutas ocupacionais, Hospitais, Exames laboratoriais, Serviços radiológicos, Aparelhos ortopédicos, Próteses ortopédicas e dentárias, Plano de saúde. · Cartão: Só o seu tratamento e o dos seus dependentes na declaração. · Nota: Lei 9.250/1995, art. 8º, II, “a”, e § 2º, I a IV.",
        "SAÚDE · O QUE FICA DE FORA · Remédio de farmácia não entra. · Ele não está entre as despesas médicas da lei. · Cartão “Também ficam de fora”, com X: Teste de Covid feito em farmácia (diz a Receita Federal); O que o plano reembolsou (despesa ressarcida não entra). · Selo: Na conta de exemplo, R$ 3.279,44 em farmácia em 2026. · Nota: Lei 9.250/1995, art. 8º, II, “a”, e § 2º, IV; Receita Federal, perguntas frequentes do IRPF.",
        "EDUCAÇÃO · COM LIMITE · Até R$ 3.561,50 por pessoa no ano. · Escola entra até esse teto. Material e uniforme, não. · Cartão “Escola em 2026 · conta de exemplo”, R$ 17.400,00: barra com R$ 3.561,50 em verde (entra) e R$ 13.838,50 listrado (acima do limite). Não entra: Material, Uniforme, Transporte escolar, Idioma, Cursinho, Música, dança e esportes. · Nota: Declare o valor total, mesmo acima do limite (Receita Federal). Lei 9.250/1995, art. 8º, II, “b”. Escola de 2026: Transações, categoria Educação.",
        "NO TIMTIMCASH · O seu 2026 em duas buscas. · Em Transações, no Ano 2026: “exame” e “farmácia”. · Selo verde “Exame, R$ 150: entra” sobre a tela real da busca “exame” (1 transação · 1 paga · 0 pendentes · somam R$ 150,00); selo coral “Farmácia, R$ 3.279,44: fora da lista” sobre a tela real da busca “farmácia” (23 transações · 23 pagas · 0 pendentes · somam R$ 3.279,44). Relógio em 11/02/2027. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "ANTES DE DECLARAR · Confira com um contador. · O timtimcash organiza os números. A declaração é sua. · Cartão “O timtimcash faz”: Soma por busca e por categoria, no ano que você escolher; Exporta a lista filtrada em Excel ou CSV, para levar ao contador. “Não faz”: A declaração do imposto de renda.",
        "Fechamento (fundo verde) · Seu ano de saúde e escola, somado. · Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Saúde e educação entram no IR como dedução, mas cada uma tem a sua regra.\n\n"
        "Saúde não tem limite de valor, mas só entra o que está na lista da lei: médicos, dentistas, psicólogos, fisioterapeutas, fonoaudiólogos, terapeutas ocupacionais, hospitais, exames laboratoriais, serviços radiológicos, aparelhos ortopédicos e próteses, além do plano de saúde. Remédio de farmácia não está na lista, e o que foi reembolsado não entra.\n\n"
        "Educação tem limite de R$ 3.561,50 por pessoa no ano. Material, uniforme, transporte escolar, idioma e cursinho não entram. Declare o total, mesmo acima do limite.\n\n"
        "No timtimcash, duas buscas no Ano 2026 da conta de exemplo: exame, R$ 150; farmácia, R$ 3.279,44. A lista filtrada sai em Excel ou CSV para o contador. O timtimcash organiza os números e não faz a declaração: confira o seu caso com um contador.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Lei 9.250/1995, art. 8º; Receita Federal.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#impostoderenda #irpf #saude #educacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Em fevereiro chegam os informes de rendimentos (até 26/02) e começa a arrumação dos recibos de 2026 para a declaração de 2027. Saber o que entra como dedução antes de juntar os papéis evita retrabalho."),
        ("O que desperta interesse", "Uma dúvida de quase todo mundo (remédio entra? material escolar entra?), respondida com a lista da lei, e o contraste visual entre o que conta e o que não conta, com os números da conta de exemplo."),
        ("Benefício para o público", "Sabe o que é dedutível em saúde e em educação, conhece o limite de R$ 3.561,50, sabe que o reembolsado não entra e aprende a somar o ano por busca e exportar a lista para o contador."),
        ("Como contribui para o perfil", "Abre a série de IR de fevereiro com fonte oficial e deixa claro o papel do timtimcash: organiza os números e não faz a declaração. Prepara os posts de 19/02 (exterior na declaração) e 22/02 (informe de rendimentos)."),
    ],
    "alt": [
        "Imposto de renda. Saúde e educação: o que entra no IR? Dois recibos desenhados: o da esquerda, com consulta e exame, tem um visto verde; o da direita, com farmácia e remédio, está riscado em coral e tem um X.",
        "Saúde, sem limite de valor: entra o que está na lista da lei. Selos com visto: médicos, dentistas, psicólogos, fisioterapeutas, fonoaudiólogos, terapeutas ocupacionais, hospitais, exames laboratoriais, serviços radiológicos, aparelhos ortopédicos, próteses ortopédicas e dentárias e plano de saúde. Só o seu tratamento e o dos seus dependentes na declaração. Lei 9.250 de 1995, artigo 8º.",
        "Saúde, o que fica de fora: remédio de farmácia não entra. Ele não está entre as despesas médicas da lei. Também ficam de fora o teste de Covid feito em farmácia, segundo a Receita Federal, e o que o plano reembolsou. Na conta de exemplo, foram R$ 3.279,44 em farmácia em 2026.",
        "Educação, com limite: até R$ 3.561,50 por pessoa no ano. Escola entra até esse teto; material e uniforme, não. Na conta de exemplo, a escola custou R$ 17.400 em 2026: R$ 3.561,50 entram e R$ 13.838,50 ficam acima do limite. Não entram material, uniforme, transporte escolar, idioma, cursinho, música, dança e esportes. Declare o valor total, mesmo acima do limite.",
        "No timtimcash, o seu 2026 em duas buscas, em Transações, no Ano 2026. Telas reais do celular, com dados de exemplo: a busca exame mostra 1 transação que soma R$ 150, que entra; a busca farmácia mostra 23 transações que somam R$ 3.279,44, fora da lista.",
        "Antes de declarar, confira com um contador. O timtimcash organiza os números; a declaração é sua. O timtimcash faz: soma por busca e por categoria, no ano que você escolher, e exporta a lista filtrada em Excel ou CSV, para levar ao contador. Não faz: a declaração do imposto de renda.",
        "Seu ano de saúde e escola, somado. Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Planalto · Lei nº 9.250/1995, art. 8º, II, “a” e “b”, e § 2º (despesas médicas e com instrução; limite de R$ 3.561,50; dependentes; reembolso)", "https://www.planalto.gov.br/ccivil_03/leis/l9250.htm"),
        ("Receita Federal · Tributação de 2026 (limite anual de despesa com instrução: R$ 3.561,50)", "https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026"),
        ("Receita Federal · Perguntas frequentes do IRPF (teste de Covid em farmácia; uniforme, material, transporte, idioma e cursinho; música, dança e esportes; declarar o total da educação)", "https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/imposto-de-renda/dirpf"),
    ],
    "telas": [
        "telas/celular-busca-exame-2026-11-02.png · Transações no celular (390 × 1000 em escala 3), relógio em 11/02/2027 10:00, build 2026-10-19.5, cópia da conta igual à base: período “Ano atual” e a seta para Ano 2026, busca “exame”: “1 transação · 1 paga · 0 pendentes · somam R$ 150,00 · 815 no histórico”; 24/09/2026 “Exame de rotina” −R$ 150,00 · slide 5 (recorte do resumo à busca)",
        "telas/celular-busca-farmacia-2026-11-02.png · a mesma tela, busca “farmácia”: “23 transações · 23 pagas · 0 pendentes · somam R$ 3.279,44” · slide 5 (recorte do resumo à busca) e número do slide 3",
        "telas/celular-educacao-2026-11-02.png · a mesma tela, sem busca, com a categoria Educação: “12 transações · 12 pagas · 0 pendentes · somam R$ 17.400,00” (Escola, R$ 1.450 por mês) · número do slide 4 (a tela não aparece no carrossel)",
    ],
}
