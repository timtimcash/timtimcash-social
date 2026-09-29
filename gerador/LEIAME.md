# Gerador das artes

- `artes.py`: biblioteca visual (cores, logo, cabeçalho, rodapé, tipos de slide e ilustrações).
- `semanas/AAAA-MM-DD.py`: conteúdo de uma semana, com `POSTS = {"AAAA-MM-DD_slug": funcao}`.
- `render.py`: `python3 gerador/render.py gerador/semanas/AAAA-MM-DD.py` gera os JPEG 1080x1350 em `posts/AAAA-MM-DD_slug/01.jpg, 02.jpg...`.
- `historico.md`: temas já publicados.
