# -*- coding: utf-8 -*-
"""Domingo 20/12/2026 · Reel "Seu ano num arquivo" (produto: Exportar e backup; capa verde). Equipe dr2.
Vídeo, capa e prévia gerados por equipes/dr2/reel_20.py (com assert nos textos lidos da tela e na conta); telas capturadas por
equipes/dr2/captura_20.py no site build 2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular (390 × 844 em escala 3,
a tela de um iPhone 12 a 14, para a janela "Exportar transações" aparecer inteira sem rolar a página), relógio em 20/12/2026 10:00.
Interação real, toque a toque: Menu -> Exportar -> "Ano atual · 2026" (o contador da janela passa de "24 lançamentos", o período
filtrado de dezembro, para "328 lançamentos") -> a janela rolada até "Contas" e "Formato" -> PDF -> Exportar. O site abre o relatório
numa aba nova ("Relatório financeiro", "Período: 01/01/2026 até 31/12/2026", 328 transações) e mostra o aviso "Relatório de 328
transações gerado". Depois, Menu -> Preferências, rolada até "Backup" ("Exportar backup completo · Arquivo JSON com contas, transações,
categorias e orçamentos."); a captura confere que a linha do CPF da conta de exemplo ficou fora da tela.
Revisão de 16/10: a aba do relatório em PDF entra no vídeo, capturada por revisao/captura_20_relatorio.py na mesma conta e no mesmo
relógio. A página pede ao Google Fonts a DM Serif Display e a Inter; a captura entrega essas mesmas fontes, locais (Inter do site e
DM Serif Display do repositório oficial google/fonts, licença OFL), e nada do conteúdo muda. No celular, a aba abre com a página de
980 px reduzida à largura da tela e o botão "Imprimir / Salvar PDF" fixo no canto de baixo. O vídeo aproxima o cabeçalho
("Relatório financeiro", período, receitas e despesas) e depois o botão, com anel. Observação para o Samuel, fora do post: nessa
página os percentuais saem com ponto ("30.1%"), e não com vírgula.
O gancho desenha os 328 lançamentos de 2026 da conta de exemplo, um traço por lançamento, mês a mês (jan 28, fev 27, mar 25, abr 27,
mai 27, jun 27, jul 28, ago 27, set 26, out 30, nov 32, dez 24), na cor do tipo (receita verde, despesa coral, transferência cinza),
contados em base_app/estado_2026-12-20.js: o mesmo total que o site conta em "Ano atual"."""

POST = {
    "pasta": "2026-12-20_reel-seu-ano-num-arquivo",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 22 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 22 s",
    "tema": "Seu ano num arquivo: Exportar com o ano inteiro e todas as contas, em Excel, PDF ou CSV, e o backup completo em Preferências; seus dados saem com você",
    "pilar": "Produto (Exportar e backup) · privacidade",
    "data_longa": "domingo, 20 de dezembro de 2026",
    "data_curta": "domingo, 20/12/2026",
    "data_mockup": "20 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-20T10:00:00",
    "video": "saida/2026-12-20_reel-seu-ano-num-arquivo/reel.mp4",
    "capa": "saida/2026-12-20_reel-seu-ano-num-arquivo/capa.jpg",
    "previa": "saida/2026-12-20_reel-seu-ano-num-arquivo/previa.mp4",
    "slides": [
        "Capa da grade (verde) · EXPORTAR · Seu ano num arquivo · Um arquivo desenhado em traço branco, com a dobra no canto e “2026” dentro.",
        "0 a 2,6 s · Gancho (papel) · EXPORTAR · 2026 inteiro, num arquivo só. · Desde o primeiro quadro, os 328 lançamentos de 2026 da conta de exemplo sobem mês a mês, um traço por lançamento (verde receita, coral despesa, cinza transferência), e o contador vai a 328 lançamentos; em 1,5 s todos voam para dentro de um arquivo desenhado com “2026”.",
        "2,9 a 4,9 s · No menu, toque em Exportar. · Tela real da Visão geral; toque em Menu; o menu abre, o anel marca Exportar e vem o toque.",
        "5,1 a 7,6 s · Escolha o ano: são 328 lançamentos de 2026. · Janela “Exportar transações”; toque em “Ano atual · 2026”; o contador passa de 24 para 328 lançamentos (anel).",
        "7,9 a 10,2 s · Todas as contas, em Excel, PDF ou CSV. · A janela rolada até Contas e Formato: anel em “Todas as contas” e nos três formatos (Excel · .xlsx · editável; PDF · Relatório pronto; CSV · Texto universal); toque em PDF.",
        "10,5 a 13,8 s · PDF: o relatório abre pronto para imprimir ou salvar. · PDF marcado; toque em Exportar; abre a aba do relatório no celular (Relatório financeiro, período de 01/01/2026 a 31/12/2026, receitas, despesas, resultado, 328 lançamentos e despesas por categoria); a câmera aproxima o cabeçalho e depois o botão “Imprimir / Salvar PDF”, em anel.",
        "14,0 a 16,4 s · E o backup completo fica em Preferências. · Preferências › Backup: “Exportar backup completo · Arquivo JSON com contas, transações, categorias e orçamentos.” com o botão Baixar, em anel.",
        "16,6 a 19,3 s · Cena em tinta · Seus dados saem com você. · Quatro arquivos desenhados em menta: Excel (.xlsx), PDF (.pdf), CSV (.csv) e Backup (.json). · Quando quiser, no computador ou no celular.",
        "19,3 a 22,0 s · Fechamento (verde) · Exportar no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "2026 inteiro, num arquivo só.\n\n"
        "No menu, toque em Exportar e escolha o período. No exemplo do vídeo, o ano atual tem 328 lançamentos. Dá para levar todas as "
        "contas ou só as que você quiser, em Excel (editável), PDF (relatório pronto para imprimir ou salvar) ou CSV (texto universal).\n\n"
        "Em Preferências fica o backup completo: um arquivo JSON com contas, transações, categorias e orçamentos, para guardar e "
        "restaurar depois.\n\n"
        "Seus dados saem com você, quando você quiser.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#financaspessoais #controlefinanceiro #organizacaofinanceira #planilha #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de ano é quando as pessoas fecham as contas, guardam o ano e começam outro; domingo, 20/12, é um bom dia para salvar 2026 inteiro antes das festas."),
        ("O que desperta interesse", "Os 328 lançamentos do ano subindo mês a mês e entrando num arquivo só, já no primeiro segundo, e o passo a passo real em poucos toques."),
        ("Benefício para o público", "A pessoa aprende a tirar o ano inteiro do site em Excel, PDF ou CSV e onde fica o backup completo, e vê que os dados não ficam presos."),
        ("Como contribui para o perfil", "Reforça um diferencial do posicionamento (sem conexão com o banco, sem propaganda, exporta tudo) com tela real de uma função que ainda não tinha aparecido no perfil."),
    ],
    "alt": [
        "Reel de 22 segundos. 2026 inteiro, num arquivo só: os 328 lançamentos de 2026 da conta de exemplo sobem mês a mês, um traço por "
        "lançamento, e entram num arquivo desenhado com 2026. Telas reais do timtimcash no celular, com dados de exemplo. Na Visão geral, um "
        "toque em Menu e outro em Exportar. Na janela Exportar transações, um toque em Ano atual 2026 muda o contador de 24 para 328 "
        "lançamentos. Com todas as contas, os formatos são Excel, PDF e CSV; um toque em PDF e outro em Exportar, e abre o "
        "relatório: Relatório financeiro de 2026, com receitas, despesas, resultado, 328 lançamentos e despesas por categoria, e o botão "
        "Imprimir ou Salvar PDF. Em Preferências, a seção Backup tem Exportar backup completo, um arquivo JSON com contas, transações, "
        "categorias e orçamentos. Seus dados saem com você: Excel, PDF, CSV e Backup. Exportar no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-exportar-1-visao-geral.jpg · Visão geral de dezembro de 2026, antes do toque em Menu (celular 390 × 844 em escala 3, build 2026-10-16.1, relógio da página em 20/12/2026 10:00) · 2,8 a 3,6 s",
        "telas/celular-exportar-2-menu.jpg · o menu aberto, com Importar e Exportar no fim (mesmo relógio) · 3,6 a 5,0 s",
        "telas/celular-exportar-3-janela.jpg · “Exportar transações” ao abrir: “Período atual filtrado · Dezembro 2026”, 24 lançamentos (mesmo relógio) · 5,0 a 6,0 s",
        "telas/celular-exportar-4-ano.jpg · depois do toque em “Ano atual · 2026”: 328 lançamentos (mesmo relógio) · 6,0 a 7,8 s",
        "telas/celular-exportar-5-formatos.jpg · a janela rolada até Contas (“Todas as contas”) e Formato (Excel, PDF, CSV) · 7,8 a 10,4 s",
        "telas/celular-exportar-6-pdf.jpg · depois do toque em PDF · 10,4 a 12,0 s",
        "telas/celular-exportar-7b-relatorio-aba.jpg · depois do toque em Exportar: a aba do relatório no celular (página de 980 px reduzida à tela de 390 × 844, com o botão “Imprimir / Salvar PDF”), capturada por revisao/captura_20_relatorio.py com as fontes que a página pede · 12,0 a 13,9 s",
        "telas/celular-relatorio-pdf-topo.png · o topo da mesma aba em tamanho real (980 px, escala 3), para conferência; relatorio_pdf.json traz o texto da página e as fontes carregadas",
        "telas/celular-exportar-7-relatorio-gerado.jpg · o aviso “Relatório de 328 transações gerado” na aba de origem (conferido no código; não entra mais no vídeo)",
        "telas/celular-preferencias-backup.jpg · Preferências rolada até Backup: “Exportar backup completo”, “Cópias no servidor”, “Restaurar de backup”; o CPF da conta de exemplo fica fora da tela · 13,9 a 16,8 s",
        "telas/caixas.json · posições medidas na captura, os textos de cada tela, o texto da aba do relatório e a conferência de que o CPF não aparece",
    ],
}
