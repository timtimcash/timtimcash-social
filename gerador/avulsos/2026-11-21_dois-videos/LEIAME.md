# Dois vídeos de 21 e 24/11/2026: o timtimcash e o Premium

Aprovados pelo dono em 21/11/2026. Os vídeos e as capas estão em `posts/2026-11-21_reel-o-timtimcash/` e `posts/2026-11-24_reel-premium-5-perguntas/`.

- `kitv.py`: o aparelho, os títulos, o cartão de resposta, a coroa e o fundo do Premium, por cima de `kit/reelkit.py` e `equipes/js/comum.py` (pasta de trabalho de janeiro e fevereiro, `gerador/restaurar_pasta.py <pasta> janfev`; o caminho no começo do arquivo aponta para ela).
- `som.py`: instrumentos, mesa, eco, sala e nível das trilhas. As trilhas são feitas inteiras em código, sem música, amostra, gravação ou efeito de terceiros, com o volume em −14 LUFS.
- `v1/` (o timtimcash, 24 s, capa papel) e `v2/` (o Premium, 22,6 s, capa verde suave): `tempos.py`, o roteiro (`video1.py`, `video2.py`), a trilha (`trilha1.py`, `trilha2.py`) e as telas usadas, em `telas/`.
- `dados.py`: legendas e textos alternativos.

Telas reais do build 2026-11-20.8, numa conta de exemplo: no vídeo 1, conta no plano Grátis (3 limites); no vídeo 2, conta no Premium, no tema escuro do site.

Para refazer: `python3 video1.py`, `python3 trilha1.py` e
`ffmpeg -i saida/mudo.mp4 -i trabalho/trilha.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 -t 24.0 -movflags +faststart -use_editlist 0 saida/reel.mp4`
(o mesmo em `v2/`, com 22.6 s).
