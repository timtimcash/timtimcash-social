# Fevereiro de 2027 · fontes dos 20 posts

Planejados junto com janeiro e aprovados pelo dono em 21/10/2026, todos os 20: 10 carrosséis e 10 Reels, alternados, às 10h (horário de Brasília), com post em todo fim de semana (sábados 06, 13, 20 e 27). Sem post no Carnaval (08 e 09/02). A mídia que vai ao ar está em `posts/<pasta>/`; aqui ficam os dados, as telas e os roteiros. A pauta, os fatos conferidos e as notas dos dois meses estão em `../2027-01/`.

## O mês
O ano escolar numa conta (03/02), o Carnaval com envelope (05 e 10/02), o começo do Imposto de Renda (saúde e educação em 11/02, exterior em 19/02 e o informe de rendimentos em 22/02), dívidas (24/02) e o fechamento do mês com as contas de março (26 e 27/02). Recursos do site que estreiam no perfil: atalhos no computador (18/02), recategorizar de uma vez (20/02) e a meta de receita (23/02).

## O que tem aqui
- `dados/`: um arquivo por post, com legenda, texto alternativo, roteiro, justificativa, fontes e as telas usadas.
- `aprovacao_fevereiro_dados.py`: monta a página de aprovação do mês (as notas ficam em `../2027-01/aprovacao_notas.py`).
- `equipes/`: os roteiros, por equipe: `fa` e `fb` (carrosséis), `fr` e `fs` (Reels).
- `telas/<pasta>/`: telas reais do timtimcash numa conta fictícia (build `2026-10-19.5`), sem nenhum dado real.

## O que mudou na revisão, antes da aprovação
- Datas: dois pares trocaram de dia para os posts de exterior ficarem um em cada semana (Realizado, Previsto e Ambos em 17/02 e Lá fora na declaração em 19/02; Meta de receita em 23/02 e Nova remessa em 25/02).
- Contas separadas: a renda extra (23/02) e as três dívidas (24/02) usam uma conta só com o próprio exemplo, para não contradizer os números do mês nos outros posts.
- 13/02: o slide 5 trocou o Carnaval (já nos Reels de 05 e 10/02) pela volta da reserva ("Tirou da reserva? Não é receita.").
- 12/02: os quadros das tabelas foram aproximados para a leitura no celular, e o indicador "IOF pago R$ 0,00" das remessas em dólar ficou fora do recorte.
- Fatos: uma revisão independente conferiu cada fato na fonte. Entraram a IN SRF 698/2006 (informe dos bancos), a exceção da conta-corrente sem rendimento na Lei 14.754/2023 (art. 2º, § 3º), "entra na base do imposto" e o achado de Gal e McShane (2012) como no artigo: fechar dívidas inteiras, qualquer que seja o valor.

## Números com data
- 01/02: o Carnaval como ponto facultativo no governo federal segue a Portaria MGI 11.460/2025, de 2026.
- 12/02: 2026 aparece em dólar, com "falta o câmbio de 31/12" em reais, até a PTAX do fim de 2026 sair.

### Para refazer
`python3 gerador/restaurar_pasta.py <pasta> janfev`, como em `../2027-01/LEIAME.md`.
