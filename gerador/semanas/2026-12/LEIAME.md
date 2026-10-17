# Dezembro de 2026 · fontes dos 20 posts

Planejados junto com novembro e aprovados pelo dono em 16/10/2026, todos os 20: 10 carrosséis e 10 Reels, alternados, às 10h (horário de Brasília), com post em todo fim de semana (domingos 06, 20 e 27 e sábado 12). Sem post em 24, 25 e 31/12. A mídia que vai ao ar está em `posts/<pasta>/`; aqui ficam os dados, as telas e os roteiros. A pauta, os fatos conferidos e o kit dos dois meses estão em `../2026-11/`.

## O que tem aqui
- `dados/`: um arquivo por post, com legenda, texto alternativo, roteiro, justificativa, fontes e as telas usadas.
- `aprovacao_dezembro_dados.py`: monta a página de aprovação do mês, com o calendário, a grade e as notas enviadas ao dono.
- `equipes/`: os roteiros, por equipe: `dc1` e `dc2` (carrosséis), `dr1` e `dr2` (Reels).
- `revisao/`: as folhas de contato da revisão (`folhas.py`) e as correções de texto aplicadas depois dela (`aplicar_textos_dez.py`).
- `telas/<pasta>/`: telas reais do timtimcash numa conta fictícia (build `2026-10-16.1`).

## O que mudou na revisão, antes da aprovação
- 12/12: "rotativo" não é sigla; no glossário, entrou o CET (custo efetivo total, Resolução CMN 4.881/2020).
- 17/12: o título dizia que o euro caiu de R$ 5,7627, mas esse valor já inclui o IOF. Agora: "Pagou R$ 5,7627 por euro, com IOF. Hoje: R$ 5,6592."
- 06/12: o 3,0% do site é a taxa ao ano (no período, a carteira subiu 2,7%); o Reel e a legenda dizem "ao ano".
- 20/12: o Reel mostra a aba do relatório em PDF de verdade. A página pede ao Google Fonts a DM Serif Display e a Inter; a captura usou as mesmas fontes, locais (licença OFL), sem mudar o conteúdo.
- Textos menores em 07, 10, 18, 23, 27 e 28/12. A PTAX de compra de 31/12/2025 (R$ 5,5018) foi conferida na tabela da Receita Federal.

## Números com data
Quatro posts usam o dado mais recente de 16/10/2026 e podem ganhar um número novo antes de ir ao ar: juros médios de agosto de 2026 (10 e 11/12), IPCA de setembro (16/12) e as regras do IPVA de 2026 (07/12). Combinado com o dono em 17/10: quando saírem os números novos, esses posts são refeitos e vão para a aprovação dele; sem resposta até a véspera, fica o que está agendado. O Banco Central publica os juros de outubro no fim de novembro, o IBGE divulga o IPCA de novembro em 11/12/2026 e o calendário do IPVA de 2027 de São Paulo costuma sair em novembro.

### Para refazer
1. `python3 gerador/restaurar_pasta.py <pasta>` remonta a pasta de trabalho a partir deste repositório e baixa a Inter 4.1, se faltar. Conferido em 17/10/2026: os 21 slides de 07, 10 e 16/12 saem iguais, pixel a pixel, aos aprovados, e o Reel de 11/12 sai com os mesmos quadros.
2. Números: `equipes/dc1/posts.py` (`post_janeiro` e `post_juros`), `equipes/dr1/reel_11.py` (cena 4) e `equipes/dc2/posts.py` (`post_inflacao`), e também a legenda, o texto alternativo e as fontes em `dados/`. As contas são conferidas por assert.
3. O slide 6 de 10/12 mostra uma tela real com o total das 12 parcelas no crédito pessoal à taxa média. Se a taxa mudar, essa tela precisa ser capturada de novo, com a cópia local do site, que fica fora deste repositório.
4. `python3 kit/checar.py tudo` e a página de aprovação. Aprovado: as artes novas vão para `posts/<pasta>/`, e o post agendado no Metricool é atualizado com os links do novo commit.

## Para o site
No relatório em PDF (Exportar), os percentuais de "Despesas por categoria" saem com ponto ("30.1%"). O Reel de 20/12 não mostra esses percentuais.
