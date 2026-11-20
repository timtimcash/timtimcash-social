# -*- coding: utf-8 -*-
"""Legenda e texto alternativo do Reel do lançamento do Premium (para aprovação em 20/11/2026)."""
LEGENDA = """Chegou o timtimcash Premium, para você ver o seu dinheiro por inteiro.

No Premium, você tem Relatórios, Comparar, Resultado (DRE) e Diagnóstico, Simulação futura e Remessas ao exterior, com TIR. E mais: orçamentos e metas sem limite, aviso por e-mail dos vencimentos e importação de planilhas sem limite.

R$ 14,90 por mês ou R$ 149 por ano (sai a R$ 12,42 por mês). O pagamento é no cartão de crédito, pela Stripe. Cancele quando quiser: o Premium segue até o fim do período pago, sem devolução proporcional. Se desistir em até 7 dias, recebe tudo de volta, pelo próprio site.

O Grátis continua, sem prazo e sem cartão: lançamentos, contas, cartões e categorias sem limite; Visão geral, Transações, Pendentes e Fluxo; 3 orçamentos e 3 metas; 1 planilha importada por mês.

Criou sua conta até o lançamento, em 19/11? Ela é fundadora: tudo liberado, sem custo e sem prazo.

Para assinar, abra Planos, no menu do site.

Tela real do timtimcash, com dados de exemplo.

Acesse pelo navegador, no computador ou no celular: timtimcash.com

#timtimcash #financaspessoais #controlefinanceiro #organizacaofinanceira #planejamentofinanceiro"""

ALT = ("Reel de 22 segundos. Em fundo verde, o logotipo do timtimcash, uma coroa dourada e a frase Chegou o Premium, com o preço: "
       "R$ 14,90 por mês, ou R$ 149 por ano, com 2 meses grátis. Quer ver o seu dinheiro por inteiro? Depois, telas reais do timtimcash "
       "no celular, com dados de exemplo: o menu, com o selo Premium e a coroa em Relatórios, Comparar, Resultado (DRE), Simulação futura "
       "e Remessas ao exterior; os Relatórios de outubro, acima do seu padrão; Comparar, outubro de 2026 contra outubro de 2025, "
       "diferença de mais R$ 275; o Resultado (DRE) de outubro, mais R$ 2.065,00; a Simulação futura, em que trocar de carro deixa "
       "R$ 17,6 mil a menos que o cenário base; e Remessas ao exterior, mais 10,5% em dólar e mais 11,6% em reais. E mais: orçamentos "
       "e metas sem limite, aviso por e-mail dos vencimentos e importar planilhas sem limite. Na tela Planos, Mensal R$ 14,90 e Anual "
       "R$ 149. timtimcash Premium. Assine em Planos, no menu do site. Link na bio.")

if __name__ == "__main__":
    import re
    print("legenda:", len(LEGENDA), "caracteres ·", len(re.findall(r"#\w+", LEGENDA)), "hashtags · texto alternativo:", len(ALT))
    for nome, s in [("legenda", LEGENDA), ("alt", ALT)]:
        assert "—" not in s and "–" not in s, nome
        assert not re.search(r"\bapp\b|aplicativo|intelig[eê]ncia artificial", s, re.I), nome
    assert len(LEGENDA) <= 2200 and len(ALT) <= 1000
