# Novembro de 2026 · fontes dos 20 posts

Planejados junto com dezembro e aprovados pelo Samuel em 16/10/2026: 20 posts no mês, 10 deles Reels, carrossel e Reel alternados, todos às 10h (horário de Brasília), com post em todo fim de semana. O Reel de 04/11 teve três versões: o Samuel pediu "outro exemplo que não seja o delivery" (16/10) e, na versão com combustível, sugeriu assinaturas (17/10). Como o carrossel de 07/11 já é sobre assinaturas, com a mesma tela e os mesmos números, ele escolheu outro gasto do dia a dia, e a versão com a farmácia foi aprovada em 17/10. A mídia que vai ao ar está em `posts/<pasta>/`; aqui ficam os dados, as telas e os roteiros.

## O que tem aqui
- `dados/`: um arquivo por post, com legenda, texto alternativo, roteiro dos slides ou das cenas, justificativa, fontes e a lista das telas usadas (com o dia do relógio da captura).
- `aprovacao_novembro_dados.py`: monta a página de aprovação do mês (`gerador/aprovacao.py`), com o calendário e a prévia da grade.
- `PAUTA.md`: a pauta de novembro e dezembro, com o calendário, o fundo de cada capa e o roteiro de cada post, como foi planejada.
- `FATOS.md`: leis, taxas, índices e datas oficiais usados nos dois meses, conferidos na fonte, com o link de cada um.
- `kit/`: `reelkit.py` (Reels: cada quadro desenhado no Chromium por `render(t)` e enviado ao ffmpeg, 1080 × 1920, 30 fps, H.264 e AAC com `+faststart`), `carrossel.py` (carrosséis 1080 × 1350, com conferência de layout) e `checar.py` (palavras proibidas, travessão e zona segura dos Reels).
- `equipes/`: os roteiros, por equipe: `c1` e `c2` (carrosséis), `r1b`, `r2` e `r3` (Reels).
- `telas/<pasta>/`: telas reais do timtimcash numa conta fictícia (build `2026-10-16.1`), sem nenhum dado real. A conta está descrita em `gerador/telas/LEIAME.md`.

## Para rodar de novo
Os roteiros apontam para a pasta de trabalho da sessão em que foram feitos (variável `N`). Para gerar de novo, troque `N` pela pasta onde estiverem as telas e as saídas. As capturas foram feitas com uma cópia local do site, que não fica neste repositório público; por isso os roteiros de captura não estão aqui.

## Capas e grade
Os fundos alternam entre papel, tinta, verde suave e verde, com no máximo uma capa verde por semana. Duas capas com o mesmo fundo nunca ficam lado a lado nem a 3 posts de distância (a grade tem 3 colunas, e elas ficariam uma em cima da outra). Regra completa em `gerador/MARCA.md`.

## Reels
Desde novembro, cada Reel abre em movimento, com a pergunta e um número já no primeiro segundo, e tem capa própria para a grade. Em outubro, o tempo médio assistido foi de 3 segundos, e a capa parada no começo segurava pouco. Zona segura: nada importante nos 270 px de cima nem abaixo de 1600 px.
