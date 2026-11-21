# -*- coding: utf-8 -*-
"""Legendas e textos alternativos dos dois vídeos de 21 e 24/11/2026 (aprovados pelo dono em 21/11/2026)."""
LEGENDA_1 = """Para onde foi o seu dinheiro neste mês?

O timtimcash é um site de finanças pessoais. Você lança cada gasto em segundos, e ele mostra o resto:

Visão geral · receitas, despesas e o resultado do mês numa tela.
Pendentes · o que vence e o que entra nos próximos dias.
Fluxo · mês a mês, em 12 meses.
Orçamentos · limites por categoria, com o ritmo do mês.

Tudo isso está no plano Grátis, sem prazo e sem cartão. Quando quiser ir mais fundo, o timtimcash Premium tem Relatórios, Comparar, Resultado (DRE), Simulação futura e Remessas ao exterior, por R$ 14,90 por mês ou R$ 149 por ano.

Tela real do timtimcash, com dados de exemplo.

Acesse pelo navegador, no computador ou no celular: timtimcash.com

#timtimcash #financaspessoais #controlefinanceiro #orcamentopessoal #organizacaofinanceira"""

ALT_1 = 'Vídeo de 24 segundos com trilha instrumental. Abre em fundo escuro com "Despesas do mês", um contador até R$ 7.331,20 e a pergunta "Para onde foi?". Depois, o logotipo do timtimcash e "O timtimcash mostra." Em seguida, telas reais do site num celular, com dados de exemplo: um gasto de R$ 24,50 lançado na Nova transação; a Visão geral, com 26,4% da receita guardada e resultado de R$ 2.628,80; Pendentes, com o 13º salário em 6 dias; o Fluxo de 12 meses; e Orçamentos, com três limites por categoria. Um painel verde lista o que há no Premium (Relatórios, Comparar, Resultado, Simulação futura e Remessas ao exterior), por R$ 14,90 por mês ou R$ 149 por ano. Fecha com "Comece grátis. Sem prazo e sem cartão."'

LEGENDA_2 = """Cinco perguntas que o timtimcash Premium responde:

1. Guardei mais que o meu normal? Relatórios compara o mês com a sua média.
2. O que mudou em um ano? Comparar põe dois períodos lado a lado.
3. Quanto sobrou, de verdade? Resultado (DRE) mostra receitas menos despesas, linha por linha.
4. E se eu trocar de carro? Simulação futura projeta o saldo de cada cenário.
5. Quanto rendeu lá fora, em reais? Remessas ao exterior separa o rendimento do efeito do câmbio.

Também no Premium: orçamentos e metas sem limite, aviso por e-mail dos vencimentos e importar planilhas sem limite.

R$ 14,90 por mês ou R$ 149 por ano. Desista em até 7 dias e receba tudo de volta. Para assinar, abra Planos no menu do site.

Tela real do timtimcash, com dados de exemplo.

Acesse pelo navegador, no computador ou no celular: timtimcash.com

#timtimcash #financaspessoais #planejamentofinanceiro #controlefinanceiro #investimentonoexterior"""

ALT_2 = 'Vídeo de 23 segundos com trilha instrumental. Abre em fundo verde escuro com o logotipo do timtimcash, uma coroa dourada, o número 5 e "perguntas. O Premium responde." Depois, cinco telas reais do site no tema escuro, num celular, com dados de exemplo, cada uma com uma pergunta e a resposta em destaque: Relatórios (20,1% guardados, contra a média de 15,2%), Comparar (despesas R$ 275 maiores que um ano antes), Resultado (DRE) de outubro (+R$ 2.065,00), Simulação futura (trocar de carro deixa o saldo R$ 17,6 mil menor que o cenário base) e Remessas ao exterior (+11,6% em reais e +10,5% em dólar). Em seguida, a tela Planos: R$ 14,90 por mês ou R$ 149 por ano, com desistência em até 7 dias. Fecha com "timtimcash Premium. Veja o seu dinheiro por inteiro. Assine em Planos, no menu do site."'

if __name__ == "__main__":
    import re
    for nome, s in [("legenda 1", LEGENDA_1), ("alt 1", ALT_1), ("legenda 2", LEGENDA_2), ("alt 2", ALT_2)]:
        assert "\u2014" not in s and "\u2013" not in s, nome
        assert not re.search(r"\bapp\b|aplicativo|intelig[eê]ncia artificial", s, re.I), nome
        print(nome, len(s), "caracteres", len(re.findall(r"#\w+", s)), "hashtags")
    assert len(LEGENDA_1) <= 2200 and len(LEGENDA_2) <= 2200 and len(ALT_1) <= 1000 and len(ALT_2) <= 1000
