# -*- coding: utf-8 -*-
"""Segunda 22/02/2027 · carrossel "Informe de rendimentos: até 26/02" (imposto de renda, capa verde suave). Equipe fb.
Artes: saida/2027-02-22_informe-de-rendimentos-o-que-conferir/01.jpg a 07.jpg, geradas por equipes/fb/posts.py (post_informe).

Fatos:
- prazo: pela regra da Receita (Instrução Normativa RFB 2.060/2021, art. 3º, e Instrução Normativa SRF 698/2006, art. 2º,
  I, citada pela checagem de fatos de 20/10/2026 para o informe dos bancos), o informe sai até o último dia útil de
  fevereiro do ano seguinte ao pagamento; em 2027, sexta-feira, 26/02 (J/FATOS.md 5a.1, 5a.4 e a nota do revisor; o
  endereço da IN SRF 698/2006, idAto=15640, foi conferido no LexML pelo coordenador; assert em posts.py: o último dia útil
  de fevereiro de 2027 é 26/02).
- o que conferir (procurado em fonte oficial em 20/10/2026, porque FATOS.md não lista os campos do informe; não afirmamos os
  quadros do documento, só o que a lei diz de cada valor): os rendimentos do ano, fora os tributados só na fonte, entram
  na base do imposto (Lei 9.250/1995, art. 8º, I; no slide 3, "entra na base", como pediu a checagem de fatos, porque a
  base também tem outros rendimentos e deduções), e a contribuição à Previdência é deduzida (art. 8º, II, "d"); o imposto sobre o
  salário é retido a cada pagamento (Lei 7.713/1988, art. 7º, I e § 1º); o 13º é tributado só na fonte e separado dos
  demais rendimentos (Lei 8.134/1990, art. 16, III). Textos lidos no Planalto (URLs nas fontes).
- novidade: redução anual na declaração de 2027 (Lei 15.270/2025, art. 11-A da Lei 9.250/1995): até R$ 60.000,00 de
  rendimentos tributáveis no ano, redução de até R$ 2.694,15 (imposto zero); de R$ 60.000,01 a R$ 88.200,00, redução
  decrescente; acima, sem redução (FATOS.md 5d.5).
Números da conta de exemplo (assert em posts.py contra estado.py e o texto da tela): em 2026, 14 receitas na categoria
Salário, R$ 125.973,36 = 2 × R$ 9.480,00 (jan e fev) + 10 × R$ 9.960,00 + 13º (R$ 4.980,00 + R$ 2.433,36); a tela diz
"14 transações · 14 pagas · 0 pendentes · somam R$ 125.973,36 · 824 no histórico". O post não diz qual é o bruto da conta de
exemplo: a parte do bruto e do líquido é uma ilustração sem valores.
Tela da conta de base (J/base_app), capturada por equipes/fb/captura.py (salario_2202)."""

POST = {
    "pasta": "2027-02-22_informe-de-rendimentos-o-que-conferir",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Informe de rendimentos até 26/02: o prazo pela regra da Receita, o que conferir com os contracheques (rendimentos, INSS, imposto retido e 13º), por que o informe mostra mais que o extrato, a redução anual da Lei 15.270/2025 na declaração de 2027 e, no timtimcash, o que caiu na conta em 2026 com a busca “salário”",
    "pilar": "Educação · imposto de renda, com fonte oficial e produto",
    "data_longa": "segunda-feira, 22 de fevereiro de 2027",
    "data_curta": "segunda-feira, 22/02/2027",
    "data_mockup": "22 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-22T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · IMPOSTO DE RENDA · Informe de rendimentos: até 26/02. · Um envelope branco desenhado, com uma folha saindo por cima (“INFORME DE RENDIMENTOS”) e, no canto, um selo verde redondo com “26” e “FEV”.",
        "O PRAZO · REGRA DA RECEITA · Até o último dia útil de fevereiro. · Empresa, banco e demais fontes pagadoras entregam o informe de 2026 até sexta-feira, 26/02. · Calendário de fevereiro de 2027 (começando no domingo), com o 26 em verde e os fins de semana em cinza; no alto, “26 · sexta-feira”. · Nota: IN RFB 2.060/2021, art. 3º, e IN SRF 698/2006, art. 2º, I.",
        "O QUE CONFERIR · Compare com os seus contracheques. · Lista com quatro itens e um visto em cada: Rendimentos do ano (o salário antes dos descontos: entra na base do imposto; Lei 9.250/1995, art. 8º, I); INSS descontado (a contribuição à Previdência sai da base do imposto; Lei 9.250/1995, art. 8º, II, d); Imposto retido na fonte (o IR descontado a cada pagamento de salário; Lei 7.713/1988, art. 7º, I e § 1º); 13º salário (tributado só na fonte, separado do resto; Lei 8.134/1990, art. 16, III).",
        "BRUTO E LÍQUIDO · Por que o informe mostra mais que o extrato? · No extrato cai o líquido. O informe mostra os rendimentos e, à parte, o que foi descontado. · Ilustração sem valores: “No informe” (rendimentos, antes dos descontos), uma barra com líquido, INSS e IR; “No extrato” (o que caiu na conta), só a parte do líquido. · Nota: Ilustração, sem valores. O contracheque mostra os descontos de cada mês; o informe soma o ano.",
        "NOVIDADE NA DECLARAÇÃO DE 2027 · Até R$ 60 mil no ano, imposto zero. · Vale para os rendimentos tributáveis de 2026. Por isso, confira o total do informe. · Esquema “Rendimentos tributáveis em 2026”: até R$ 60 mil, a redução zera o imposto; até R$ 88,2 mil, a redução diminui; acima disso, sem redução. · Nota: Esquema sem escala. Lei 15.270/2025, que incluiu o art. 11-A na Lei 9.250/1995: redução anual a partir da declaração de 2027.",
        "NO TIMTIMCASH · O que caiu na conta em 2026. · Em Transações, o Ano 2026 e a busca “salário” somam o que entrou, com o 13º: R$ 125.973,36. · Recortes da tela real de Transações no celular (relógio em 22/02/2027): o período “Ano 2026” e “Todas as contas”; “Transações · filtrado · 14 transações · 14 pagas · 0 pendentes · somam R$ 125.973,36 · 824 no histórico” e a busca “salário”. · Nota: Tela real do timtimcash, com dados de exemplo. · Aviso em âmbar: O timtimcash organiza os números e não faz a declaração. Confira o seu caso com um contador.",
        "Fechamento (fundo verde) · Informe na mão, números no lugar. · Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "O informe de rendimentos chega até 26/02. Antes de guardar, confira.\n\n"
        "Pela regra da Receita, empresa, banco e demais fontes pagadoras entregam o informe até o último dia útil de fevereiro. Em 2027, sexta-feira, 26/02.\n\n"
        "Compare com os seus contracheques: os rendimentos do ano, o INSS, o imposto retido na fonte e o 13º, tributado só na fonte. No extrato cai o líquido; o informe mostra os rendimentos e, à parte, os descontos.\n\n"
        "Novidade na declaração de 2027: com até R$ 60 mil de rendimentos tributáveis em 2026, a redução da Lei 15.270/2025 zera o imposto. Ela diminui até R$ 88,2 mil.\n\n"
        "No timtimcash, o Ano 2026 e a busca “salário”, em Transações, somam o que caiu na conta: R$ 125.973,36 no exemplo, com o 13º. O timtimcash não faz a declaração: confira o seu caso com um contador.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: IN RFB 2.060/2021; IN SRF 698/2006; Leis 9.250/1995, 7.713/1988, 8.134/1990 e 15.270/2025.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#impostoderenda #informederendimentos #irpf #educacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "O prazo dos informes é o último dia útil de fevereiro, sexta-feira, 26/02. O post sai na segunda da mesma semana, quando os informes estão chegando."),
        ("O que desperta interesse", "A data na capa e uma dúvida comum: por que o valor do informe é maior que o que caiu na conta? A resposta vem com a lei de cada item e uma ilustração simples."),
        ("Benefício para o público", "Sabe até quando cobrar o informe, o que conferir em cada um, por que bruto e líquido não batem e como a redução da Lei 15.270/2025 entra na declaração de 2027."),
        ("Como contribui para o perfil", "Abre a temporada do IR com fonte oficial e sem prometer o que o site não faz: o timtimcash organiza os números (a busca soma o ano em segundos) e não faz a declaração."),
    ],
    "alt": [
        "Imposto de renda. Informe de rendimentos: até 26 de fevereiro. Um envelope branco com uma folha saindo por cima, escrita informe de rendimentos, e um selo verde redondo com o número 26 e fevereiro.",
        "O prazo, pela regra da Receita: até o último dia útil de fevereiro. Empresa, banco e demais fontes pagadoras entregam o informe de 2026 até sexta-feira, 26 de fevereiro. Calendário de fevereiro de 2027 com o dia 26 em destaque. Instrução Normativa RFB 2.060/2021, artigo 3º, e Instrução Normativa SRF 698/2006, artigo 2º, inciso I.",
        "O que conferir: compare com os seus contracheques. Rendimentos do ano, o salário antes dos descontos, que entra na base do imposto; INSS descontado, a contribuição à Previdência que sai da base do imposto; imposto retido na fonte, o IR descontado a cada pagamento de salário; 13º salário, tributado só na fonte e separado do resto. Com as leis de cada item.",
        "Por que o informe mostra mais que o extrato? No extrato cai o líquido. O informe mostra os rendimentos e, à parte, o que foi descontado. Ilustração sem valores: no informe, uma barra com o líquido, o INSS e o IR; no extrato, só o líquido.",
        "Novidade na declaração de 2027: até 60 mil reais no ano, imposto zero. Vale para os rendimentos tributáveis de 2026. Esquema: até 60 mil reais, a redução zera o imposto; até 88,2 mil reais, a redução diminui; acima disso, sem redução. Lei 15.270/2025.",
        "No timtimcash: o que caiu na conta em 2026. Em Transações, o Ano 2026 e a busca salário somam o que entrou, com o 13º: 125.973,36 reais. Recortes da tela real com dados de exemplo: período Ano 2026; 14 transações, 14 pagas, somam 125.973,36 reais; a busca salário. Aviso: o timtimcash organiza os números e não faz a declaração. Confira o seu caso com um contador.",
        "Informe na mão, números no lugar. Transações no timtimcash. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Receita Federal · Instrução Normativa RFB nº 2.060/2021, art. 3º (comprovante até o último dia útil de fevereiro do ano seguinte ao pagamento); sistema Normas, página dinâmica; texto do art. 3º conferido em reprodução da norma (J/FATOS.md 5a.1)", "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/122177/visao/multivigente"),
        ("Receita Federal · IN SRF 698/2006, art. 2º, I", "http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=15640"),
        ("LexML · IN SRF 698/2006 (DOU de 22/12/2006)", "https://www.lexml.gov.br/urn/urn:lex:br:ministerio.fazenda;secretaria.receita.federal:instrucao.normativa:2006-12-20;698"),
        ("Planalto · Lei nº 9.250/1995, art. 8º, I (base: os rendimentos do ano, fora os tributados exclusivamente na fonte) e II, \"d\" (dedução das contribuições à Previdência Social), lido em 20/10/2026", "https://www.planalto.gov.br/ccivil_03/leis/l9250.htm"),
        ("Planalto · Lei nº 7.713/1988, art. 7º, I e § 1º (imposto na fonte sobre o trabalho assalariado, retido a cada pagamento), lido em 20/10/2026", "https://www.planalto.gov.br/ccivil_03/leis/l7713.htm"),
        ("Planalto · Lei nº 8.134/1990, art. 16, III (o 13º é tributado exclusivamente na fonte e separadamente dos demais rendimentos), lido em 20/10/2026", "https://www.planalto.gov.br/ccivil_03/leis/l8134.htm"),
        ("Planalto · Lei nº 15.270/2025 (art. 11-A da Lei 9.250/1995: redução anual a partir da declaração de 2027, até R$ 60.000,00 com imposto zero e decrescente até R$ 88.200,00)", "https://planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm"),
        ("Receita Federal · Tabelas de 2026 (redução e tabela anual)", "https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026"),
    ],
    "telas": [
        "telas/celular-transacoes-salario-2026-22-02.png · Transações no celular, relógio em 22/02/2027 10:00, build 2026-10-19.5, conta de base (390 × 1500 em escala 3): toque no período, “Ano atual” e a seta para Ano 2026; a busca “salário” digitada letra a letra; resumo “14 transações · 14 pagas · 0 pendentes · somam R$ 125.973,36 · 824 no histórico” · slide 6 (recortes da barra do período e do cabeçalho com o resumo e a busca)",
    ],
}
