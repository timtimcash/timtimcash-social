# Outubro de 2026 · fontes dos 13 posts novos

Aprovados pelo Samuel em 30/09/2026, junto com os 7 que já estavam agendados: 20 posts no mês, 8 deles Reels, todos às 10h (horário de Brasília). A mídia que vai ao ar está em `posts/<pasta>/`; aqui ficam os dados e os roteiros usados para gerá-la.

## O que tem aqui
- `dados/`: um arquivo por post, com legenda, texto alternativo de cada imagem, roteiro dos slides ou das cenas, justificativa e fontes.
- `aprovacao_outubro_dados.py`: monta a página de aprovação do mês (`gerador/aprovacao.py`), com os 13 novos e os 7 já agendados.
- `PAUTA.md`: a pauta do mês, com o calendário e o motivo de cada data, como foi aprovada. Depois da aprovação, quatro posts foram para o fim de semana (05/10 para 04/10, 13/10 para 11/10, 19/10 para 17/10 e 26/10 para 25/10); as datas finais estão em `gerador/historico.md`.
- `carrosseis-a/`, `carrosseis-b/`: geradores dos 5 carrosséis (15, 19, 23, 26 e 29/10).
- `reels-a/` (06, 14 e 27/10), `reels-b/` (08 e 20/10), `reels-c/` (22 e 30/10) e `reels-d/` (16/10, com o kit de `reels-b/`): um `reelkit.py` por pasta e um roteiro por Reel. Cada quadro é desenhado no Chromium por `render(t)` e vai direto para o ffmpeg (1080 × 1920, 30 fps, H.264 e AAC, com `+faststart`).
- `telas/<pasta>/`, `reels-c/capturas/` e `carrosseis-a/telas_novas/`: telas reais do timtimcash numa conta fictícia, sem nenhum dado real.

## Para rodar de novo
Os roteiros apontam para a pasta de trabalho da sessão em que foram feitos (variável `O`). Para gerar de novo, troque `O` pela pasta onde estiverem as telas e as saídas. As capturas foram feitas com uma cópia local do site, que não fica neste repositório público.

## Zona segura dos Reels
No Reel de 30/09, o nome do perfil e a linha do áudio, que o Instagram põe no topo do vídeo, ficaram em cima da logo da capa. Desde então, nada importante fica nos 270 px de cima (14% da altura): o título das cenas começa em 280 px e a logo da capa em 290 px. Regra completa em `gerador/MARCA.md`.
