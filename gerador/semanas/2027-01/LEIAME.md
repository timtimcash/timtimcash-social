# Janeiro de 2027 · fontes dos 20 posts

Planejados junto com fevereiro e aprovados pelo Samuel em 21/10/2026, todos os 20: 10 carrosséis e 10 Reels, alternados, às 10h (horário de Brasília), com post em todo fim de semana (sábados 02, 16, 23 e 30 e domingo 10). Sem post em 1º/01. Agendados no Metricool no mesmo dia, com a mídia do commit `efd3906`. A mídia que vai ao ar está em `posts/<pasta>/`; aqui ficam os dados, as telas e os roteiros. A pauta, os fatos conferidos e as notas dos dois meses ficam nesta pasta.

## A campanha
"Comece 2027 organizado": o post de 02/01 apresenta 4 passos, um por post, com o selo numerado da série (04, 10, 14 e 18/01: o retrato, o caminho, os limites e a rota), e a revisão de sábado (30/01) fecha a série. Em volta, posts para quem começa agora e os temas da época: material escolar (06/01), IPVA (13/01) e o fechamento de 2026 lá fora (29/01).

## O que tem aqui
- `dados/`: um arquivo por post, com legenda, texto alternativo, roteiro, justificativa, fontes e as telas usadas.
- `aprovacao_janeiro_dados.py` e `aprovacao_notas.py`: montam a página de aprovação do mês, com o calendário, a grade e as notas enviadas ao Samuel.
- `PAUTA.md`, `FATOS.md` e `FATOS_2.md`: a pauta dos dois meses e os fatos oficiais, conferidos na fonte, com as "Notas do revisor" que os posts seguem.
- `equipes/`: os roteiros, por equipe: `ja` e `jb` (carrosséis), `jr` e `js` (Reels). O selo da série está em `ja/selo_comece2027.py`.
- `revisao/`: `conferir.py` (fundo de cada capa, hashtags, palavras proibidas, duração dos Reels e folhas de contato) e `grade_final.py` (os fundos das capas e as regras da grade).
- `telas/<pasta>/`: telas reais do timtimcash numa conta fictícia (build `2026-10-19.5`), sem nenhum dado real.

## O que mudou na revisão, antes da aprovação
- Datas: quatro carrosséis trocaram de dia para separar os temas na grade (remessas por ano em 11/01, o que se repete em 16/01, categorias em 27/01 e o fechamento de 2026 em 29/01). Os três de exterior ficam um em cada semana.
- Conta: a partir de 29/01, a conta fictícia tem o saldo de 31/12/2026 informado em "Editar fechamentos" (US$ 13.380 e € 2.014), com o câmbio vazio, como ensina o post de 29/01.
- Fatos: uma revisão independente conferiu cada fato na fonte. Entraram, entre outros: a mediana de 66 dias vale para os 39 participantes que o modelo descreveu bem (Lally e colegas, 2010); a pesquisa do Procon-SP foi divulgada em janeiro de 2026, com preços de dezembro de 2025; e a exceção das apostilas vale para a loja e para a marca.
- 08/01: "Daqui a 66 dias: 15 de março." (contando hoje como dia 1, o dia 66 seria 14/03).

## Números com data
- 13/01 (IPVA): regra de São Paulo de 2026 (Decreto 70.087/2025) e a Selic de 13,75% fixada pelo Copom em 16/09/2026. As constantes `REGRA` e `SELIC` ficam no topo de `equipes/jr/reel_13.py`.
- 06/01 (material escolar): pesquisa de preços divulgada pelo Procon-SP em janeiro de 2026.
- 29/01 (fechamento de 2026 lá fora): mostra 2026 só em dólar, porque a PTAX do fim de 2026 só existe a partir do fechamento de 30/12/2026. Em 31/12/2025, o Banco Central divulgou às 10h um boletim com as mesmas taxas do dólar de 30/12 e as outras moedas calculadas naquela manhã (InfoMoney, 24/11/2025): o euro do último boletim pode ser outro.

Combinado com o Samuel em 21/10/2026, quando ele aprovou e mandou agendar os 40 posts: quando saírem os números novos, os posts são refeitos e vão para a aprovação dele; sem resposta até a véspera, fica o que está agendado. Duas tarefas agendadas fazem a conferência: em 11/12/2026, o decreto do IPVA 2027 de São Paulo e a Selic da reunião do Copom de 08 e 09/12 (13/01); em 04/01/2027, a PTAX de compra do último boletim de 2026 (slides 5 e 6 de 29/01 e o Reel de 12/02), a pesquisa de preços de material escolar do Procon-SP (06/01; a de 2026 saiu em 02/01/2026) e a portaria do ponto facultativo de 2027 (01/02).

### Para refazer
1. `python3 gerador/restaurar_pasta.py <pasta> janfev` remonta a pasta de trabalho a partir deste repositório.
2. Mude os números no roteiro do post e nos `dados/`, rode `python3 revisao/conferir.py` e monte a página de aprovação.
3. Telas novas precisam da cópia local do site e da conta fictícia, que ficam fora deste repositório público.
