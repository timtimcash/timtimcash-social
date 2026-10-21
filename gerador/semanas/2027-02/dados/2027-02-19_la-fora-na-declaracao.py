# -*- coding: utf-8 -*-
"""Sexta 19/02/2027 · carrossel "O que vai de lá fora para a declaração" (imposto de renda e exterior, capa papel).
Equipe fb. Artes: saida/2027-02-19_la-fora-na-declaracao/01.jpg a 06.jpg, geradas por equipes/fb/posts.py (post_exterior).
Na revisão de 20/10/2026, este post trocou de dia com "Realizado, Previsto e Ambos" (era 17/02, com capa verde suave),
para não ficar empilhado na grade com o Reel de exterior de 12/02; o fundo da capa segue a data (19/02, papel) e as
telas foram refeitas com o relógio em 19/02.

Fatos (J/FATOS.md, 5e, e as notas do revisor de 20/10/2026, que limitam este post à Lei 14.754/2023 e ao que já saiu em
28/12): a declaração relaciona os bens e direitos, no Brasil ou no exterior, de 31 de dezembro (Receita Federal, Perguntas
e Respostas IRPF 2026, pergunta 007, a mesma fonte do post de 28/12/2026); Lei 14.754/2023: rendimentos de aplicações
financeiras no exterior declarados separadamente na declaração anual, a 15%, sem dedução (art. 2º); a variação cambial
entra nos rendimentos (art. 3º, § 1º, II), com a exceção pedida pela checagem de fatos de 20/10/2026 e conferida no
Planalto: a variação cambial de depósitos em conta-corrente no exterior não é tributada, desde que os depósitos não sejam
remunerados (art. 2º, § 3º); conversão pela cotação de fechamento de venda do Banco Central na data do fato gerador
(art. 15); em vigor desde 1º/01/2024 (art. 47, II). Sem o passo a passo das perguntas 479 e 639 do P&R (não
lidas), com o fechamento só de Remessas (sem a frase do controle financeiro) e sem nenhum valor em reais do fechamento de 2026 (a PTAX de 31/12/2026 ainda não existe).

Números da conta de exemplo (conferidos por assert em posts.py contra estado.py e o texto das telas):
- carteira em dólar em 31/12/2026: US$ 13.380, informada em "Editar fechamentos" desde 29/01/2027 (mudança da conta de
  base pedida pelo coordenador em 20/10, o passo do post de 27/01), com o câmbio vazio; 2025: US$ 12.960 a R$ 5,5018.
- remessa em euro de 01/12/2026: € 2.000 a R$ 5,70 = R$ 11.400,00, mais IOF de 1,10% (R$ 125,40) = R$ 11.525,40;
  câmbio médio efetivo R$ 5,7627 com IOF (R$ 5,7000 sem IOF).
Telas da conta de base (J/base_app), build 2026-10-19.5, capturadas por equipes/fb/captura.py (exterior_1902)."""

POST = {
    "pasta": "2027-02-19_la-fora-na-declaracao",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "O que vai de lá fora para a declaração do IR de 2027: a declaração relaciona os bens e direitos de 31 de dezembro; para aplicações financeiras no exterior, a Lei 14.754/2023 (15% sobre os rendimentos na declaração anual, a variação do câmbio no rendimento, com a exceção da conta-corrente sem rendimento, e a conversão pela cotação de venda do Banco Central); e os números que o timtimcash organiza para levar ao contador (saldo de 31/12 na moeda, remessas com data, reais e IOF), sem fazer a declaração",
    "pilar": "Investimento no exterior · imposto de renda, com fonte oficial e produto",
    "data_longa": "sexta-feira, 19 de fevereiro de 2027",
    "data_curta": "sexta-feira, 19/02/2027",
    "data_mockup": "19 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-19T10:00:00",
    "slides": [
        "Capa (fundo papel) · IMPOSTO DE RENDA · EXTERIOR · O que vai de lá fora para a declaração. · Duas datas grandes, cada uma num cartão: em cima, “31/12/2025” em cinza sobre branco; embaixo, à direita, “31/12/2026” em branco sobre verde escuro; entre as duas, uma linha verde e o rótulo “O SEU 2026”.",
        "BENS E DIREITOS · 31 DE DEZEMBRO · A declaração olha para 31 de dezembro. · Ela relaciona os bens e direitos, no Brasil ou no exterior, que você tinha nesse dia. · Rótulo “No timtimcash · Remessas › Editar fechamentos” e o recorte da tela real no celular (relógio em 19/02/2027): 2025 · 31/12/2025, saldo 12.960,00, câmbio R$ 5,5018; 2026 · 31/12/2026, saldo 13.380,00, câmbio vazio (0,0000), com o botão PTAX. · Notas: Tela real do timtimcash, com dados de exemplo. O câmbio do fechamento mede o rendimento. Para o imposto, vale a regra da lei. Fonte: Receita Federal, Perguntas e Respostas IRPF 2026, pergunta 007.",
        "APLICAÇÕES FINANCEIRAS LÁ FORA · O que diz a Lei 14.754/2023. · Três regras, cada uma com ícone e artigo: 15% sobre os rendimentos (na declaração anual, separados dos outros rendimentos e sem deduções; art. 2º). O câmbio também conta (a variação da moeda em relação ao real entra no rendimento; art. 3º, § 1º, II), com o destaque “Exceção: conta-corrente lá fora sem rendimento (art. 2º, § 3º).” Em reais, pela cotação de venda (de fechamento, do Banco Central, na data do fato gerador; art. 15). · Nota: Regras para aplicações financeiras no exterior, em vigor desde 1º/01/2024 (art. 47).",
        "REMESSAS AO EXTERIOR · Cada envio, com data, reais e IOF. · No exemplo, a remessa de 01/12/2026: € 2.000, que custaram R$ 11.525,40, com R$ 125,40 de IOF. · Recorte da tela real de Remessas em euro no celular (relógio em 19/02/2027): Remetido € 2.000,00 (1 remessa · desde dez/26); Custo total R$ 11.525,40 (tudo que saiu do Brasil, com IOF); Câmbio médio efetivo R$ 5,7627 (com IOF · sem IOF R$ 5,7000); IOF pago R$ 125,40 (1,10% do valor enviado). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "NO TIMTIMCASH · Os números do ano, organizados. · Cartão “Para levar ao contador”: O saldo de 31/12 de cada ano (na moeda de cada conta lá fora); Cada remessa e cada resgate (com a data e o valor na moeda); Quanto custou em reais (com o câmbio efetivo e o IOF de cada envio). · Aviso em âmbar: O timtimcash organiza os números e não faz a declaração. Confira o seu caso com um contador.",
        "Fechamento (fundo verde) · O seu 2026 lá fora, organizado. · Remessas ao exterior no timtimcash, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "O que vai de lá fora para a declaração do IR de 2027?\n\n"
        "A declaração relaciona os bens e direitos, no Brasil ou no exterior, que você tinha em 31 de dezembro. A de 2027 conta o seu 2026.\n\n"
        "Para aplicações financeiras no exterior, vale a Lei 14.754/2023: os rendimentos vão para a declaração anual, separados dos outros, com 15% e sem deduções. A variação do câmbio também é rendimento, com uma exceção: a conta-corrente lá fora sem rendimento. E a conversão para reais usa a cotação de venda do Banco Central na data do fato gerador.\n\n"
        "No timtimcash, as Remessas guardam cada envio com data, valor em reais e IOF, e o Editar fechamentos guarda o saldo de 31/12 de cada ano, na moeda. São os números para levar ao contador. O timtimcash não faz a declaração: confira o seu caso com um contador.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Fontes: Receita Federal (Perguntas e Respostas IRPF 2026); Lei 14.754/2023.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#impostoderenda #investimentonoexterior #irpf #educacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fevereiro é o mês dos informes e de juntar os números antes da declaração de 2027 (a de 2026 abriu em 23/03). Quem tem conta ou investimento lá fora precisa organizar o seu 2026 antes de procurar o contador."),
        ("O que desperta interesse", "As duas datas grandes da capa e uma pergunta que quem investe lá fora faz todo ano: o que entra na declaração? A resposta vem da lei, em três regras curtas."),
        ("Benefício para o público", "Entende que a declaração olha para 31 de dezembro, conhece as três regras da Lei 14.754/2023 (15%, câmbio no rendimento, cotação de venda) e sai com a lista do que levar ao contador."),
        ("Como contribui para o perfil", "Dá continuidade aos posts de 28/12 (anote o 31/12) e 27/01 (informe o saldo), agora com o que a declaração pede, com fonte oficial e sem prometer o que o site não faz: o timtimcash organiza os números e não faz a declaração."),
    ],
    "alt": [
        "Imposto de renda e exterior. O que vai de lá fora para a declaração. Duas datas grandes: 31/12/2025, em cinza num cartão branco, e 31/12/2026, em branco num cartão verde escuro, ligadas por uma linha verde com o rótulo o seu 2026.",
        "A declaração olha para 31 de dezembro: ela relaciona os bens e direitos, no Brasil ou no exterior, que você tinha nesse dia. Recorte da tela real Editar fechamentos, nas Remessas do timtimcash, com dados de exemplo: 2025, saldo de 12.960,00 dólares e câmbio de 5,5018 reais; 2026, saldo de 13.380,00 dólares e o câmbio ainda vazio. O câmbio do fechamento mede o rendimento; para o imposto, vale a regra da lei. Fonte: Receita Federal, Perguntas e Respostas IRPF 2026, pergunta 007.",
        "O que diz a Lei 14.754/2023 sobre aplicações financeiras no exterior: 15% sobre os rendimentos, na declaração anual, separados dos outros rendimentos e sem deduções (artigo 2º); a variação da moeda em relação ao real entra no rendimento (artigo 3º), exceto em conta-corrente lá fora sem rendimento (artigo 2º, parágrafo 3º); a conversão para reais usa a cotação de fechamento de venda do Banco Central na data do fato gerador (artigo 15). Em vigor desde 1º de janeiro de 2024.",
        "Cada envio, com data, reais e IOF. No exemplo, a remessa de 1º de dezembro de 2026: 2.000 euros, que custaram 11.525,40 reais, com 125,40 reais de IOF. Recorte da tela real de Remessas em euro: remetido, 2.000 euros; custo total, 11.525,40 reais; câmbio médio efetivo, 5,7627 reais com IOF e 5,70 sem IOF; IOF pago, 125,40 reais, 1,10% do valor enviado.",
        "Os números do ano, organizados. Para levar ao contador: o saldo de 31 de dezembro de cada ano, na moeda de cada conta lá fora; cada remessa e cada resgate, com a data e o valor na moeda; quanto custou em reais, com o câmbio efetivo e o IOF de cada envio. Aviso: o timtimcash organiza os números e não faz a declaração. Confira o seu caso com um contador.",
        "O seu 2026 lá fora, organizado. Remessas ao exterior no timtimcash, no computador ou no celular. Link na bio.",
    ],
    "fontes": [
        ("Receita Federal · Perguntas e Respostas IRPF 2026, versão 1.0, pergunta 007 (bens e direitos, no Brasil ou no exterior, em 31 de dezembro), a mesma fonte do post de 28/12/2026", "https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf"),
        ("Planalto · Lei nº 14.754/2023: art. 2º (rendimentos de aplicações no exterior na Declaração de Ajuste Anual, separados, a 15%, sem dedução), art. 2º, § 3º (a variação cambial de depósitos não remunerados em conta-corrente no exterior não é tributada, conferido em 20/10/2026), art. 3º, § 1º, II (variação cambial), art. 15 (cotação de fechamento de venda do Banco Central na data do fato gerador) e art. 47, II (desde 1º/01/2024)", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/Lei/L14754.htm"),
    ],
    "telas": [
        "telas/celular-editar-fechamentos-19-02.png · Remessas › “Editar fechamentos” (“Quanto havia no fim de cada ano”) no celular, relógio em 19/02/2027 10:00, build 2026-10-19.5, conta de base (390 × 1250 em escala 3), só aberta e fotografada, sem tocar em PTAX nem salvar: 2025 saldo 12.960,00 e câmbio 5,5018; 2026 saldo 13.380,00 (informado em 29/01/2027 na conta de base) e câmbio vazio · slide 2 (recorte das linhas de 2025 e 2026)",
        "telas/celular-remessas-euro-19-02.png · Remessas, toque em “EUR”, página inteira no celular, relógio em 19/02/2027 10:00 (390 × 3400 em escala 3): Remetido € 2.000,00; Custo total R$ 11.525,40; Câmbio médio efetivo R$ 5,7627 com IOF, sem IOF R$ 5,7000; IOF pago R$ 125,40, 1,10% do valor enviado; remessa de 01/12/2026, Reserva para Banco na Europa · slide 4 (recorte do cartão dos indicadores)",
    ],
}
