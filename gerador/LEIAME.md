# Gerador das artes

- `artes.py`: biblioteca visual (cores, logo, cabeçalho, rodapé, tipos de slide e ilustrações).
- `MARCA.md`: regras do manual da marca aplicadas às artes.
- `FUNCIONALIDADES.md`: o que o timtimcash faz, com os nomes exatos das telas e dos botões. Só cite o que está lá.
- `telas/`: telas reais do site numa conta fictícia, para usar nos posts (ver `telas/LEIAME.md`).
- `semanas/AAAA-MM-DD.py`: artes de uma semana (data da segunda-feira), com `POSTS = {"AAAA-MM-DD_slug": funcao}`.
- `semanas/AAAA-MM-DD_dados.py`: textos da proposta da semana para o arquivo de aprovação (`CONFIG`, `POSTS` e `FUSO`).
- `avulsos/`: posts fora da rotina semanal. `avulsos/2026-09-30_comece-por-aqui.py` é o modelo de post com telas reais, e `avulsos/2026-09-30_comece-por-aqui_dados.py` é o modelo do arquivo de dados da aprovação.
- `render.py`: `python3 gerador/render.py gerador/semanas/AAAA-MM-DD.py` gera os JPEG 1080 × 1350 em `posts/AAAA-MM-DD_slug/01.jpg, 02.jpg...`. Com `TT_SAIDA=/outra/pasta`, grava fora do repositório.
- `aprovacao.py`: monta o arquivo HTML de aprovação (um arquivo só, que abre sem internet), com a prévia de cada post no Instagram, todos os slides, a legenda, a justificativa e a avaliação de cada post: Aprovado, Reprovado ou Solicitar alteração, com comentários.
- `historico.md`: temas já publicados.

## Fluxo de uma semana

1. Escrever `semanas/AAAA-MM-DD.py` (artes) e `semanas/AAAA-MM-DD_dados.py` (textos da proposta). Se o nome já existir, acrescentar `_v2`, `_v3`...
2. Renderizar fora do repositório, porque nada que não foi aprovado fica público:
   `TT_SAIDA=/tmp/semana-AAAA-MM-DD python3 gerador/render.py gerador/semanas/AAAA-MM-DD.py`
3. Abrir e conferir cada imagem (o render avisa `ATENCAO: texto estourou`). Conferir também as capas juntas: cada uma com fundo e visual diferentes e pouco texto, sem repetir o fundo verde (regra das capas em `MARCA.md`).
4. Montar o arquivo de aprovação:
   `python3 gerador/aprovacao.py gerador/semanas/AAAA-MM-DD_dados.py /tmp/semana-AAAA-MM-DD /tmp/aprovacao/timtimcash-aprovacao-AAAA-MM-DD.html`
   O comando imprime o tamanho e `travessoes: []`. A lista precisa sair vazia.
5. Enviar o arquivo ao Samuel. Ele avalia cada post no navegador e cola na conversa o texto do botão "Copiar todas as avaliações".
6. Só depois da aprovação: copiar para `posts/` as pastas dos posts aprovados, tirar dos arquivos da semana os posts reprovados, fazer commit e push e agendar no Metricool com as URLs raw fixadas no commit.

## Arquivo de dados da aprovação

`CONFIG`:
- `titulo_pagina`, `eyebrow`, `h1` e `sub`: cabeçalho da página.
- `chave`: nome único da proposta (ex.: `timtimcash-aprovacao-2026-10-05-v1`). A avaliação fica salva no navegador com essa chave, então ela muda a cada proposta nova ou reenvio.
- `resumo_titulo`: primeira linha do texto copiado.
- `notas`: lista de (título, texto), em cartões no topo da página.
- `fontes`: lista de (título, URL), no fim da página. Toda informação de fora (dados econômicos, regras do Instagram, melhor horário) precisa de fonte aqui.

Cada item de `POSTS`: `n`, `pasta` (nome da pasta das imagens), `plataforma`, `formato`, `formato_curto`, `tema`, `pilar`, `data_longa`, `data_curta`, `data_mockup`, `hora`, `iso` (data e hora do agendamento), `slides` (texto de cada slide), `legenda`, `justificativa` (lista de (título, texto)), `alt` (texto alternativo de cada slide) e, opcionais, `grade`, `grade_titulo`, `grade_legenda` e `grade_nota` para a prévia da grade do perfil. Em `grade`, cada item é (rótulo, caminho da capa): caminho `None` é o próprio post, rótulo `"fixado"` mostra o alfinete de post fixado, e caminhos relativos partem da raiz do repositório.

`FUSO`: texto do fuso horário, por exemplo `"horário de Brasília (America/Sao_Paulo, UTC−3)"`.
