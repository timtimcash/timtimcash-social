# -*- coding: utf-8 -*-
"""Quinta 03/12/2026 · Reel "Presentes: o teto antes da loja" (produto: Orçamentos; capa tinta, destaque âmbar). Equipe dr1.
Vídeo, capa e prévia gerados por equipes/dr1/reel_03.py; telas reais capturadas por equipes/dr1/capturas/captura03.py no site
build 2026-10-16.1, na conta de base (N/base_app, sem mudança), no celular (390 px CSS, escala 3), tudo pela interface:
- relógio em 03/12/2026 10:00: Orçamentos › "Definir limites" › busca "Presentes" (letra a letra) › campo de "Presentes e doações"
  › 8-0-0-0-0 (o campo preenche como caixa eletrônico até R$ 800,00) › "Salvar" ("Orçamentos salvos") › rolar até a linha nova;
- relógio em 17/12/2026 e em 21/12/2026: o mesmo limite de R$ 800, definido de novo pela interface, e a página de Orçamentos.
Números da tela (assert no gerador): 03/12 "Presentes e doações R$ 0 de R$ 800 0%" (Tranquilas; LIMITE TOTAL POR MÊS 6 categorias
R$ 6.250,00); 17/12 "VÃO ESTOURAR NO RITMO ATUAL · R$ 774 de R$ 800 · 97% · no ritmo, fecha em R$ 1.412"; 21/12 "JÁ PASSARAM
DO LIMITE · R$ 972 de R$ 800 · 122% · Excedeu em R$ 172 · e, no ritmo, fecha em R$ 1.435". Gancho: Transações, Dezembro 2025,
busca "Presentes": "1 transação · somam R$ 980,00". Conta (assert): 120 + 389,90 + 264,50 = 774,40; + 198 = 972,40; 972,40 − 800 = 172,40.
Limite escolhido: R$ 800 (o da pauta); com ele, a tela conta a história inteira (cabe no dia 3, o aviso do ritmo no dia 17 e o
excesso no dia 21) e diz a verdade: os presentes do exemplo passaram do teto."""

POST = {
    "pasta": "2026-12-03_reel-presentes-o-teto-antes-da-loja",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 21 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 21 s",
    "tema": "Presentes: o teto antes da loja. Em Orçamentos, um limite de R$ 800 para Presentes e doações, definido no dia 3; a faixa mostra o ritmo no dia 17 e o excesso de R$ 172 no dia 21",
    "pilar": "Produto (Orçamentos) · sazonal (Natal)",
    "data_longa": "quinta-feira, 3 de dezembro de 2026",
    "data_curta": "quinta-feira, 03/12/2026",
    "data_mockup": "3 de dezembro",
    "hora": "10h00",
    "iso": "2026-12-03T10:00:00",
    "video": "saida/2026-12-03_reel-presentes-o-teto-antes-da-loja/reel.mp4",
    "capa": "saida/2026-12-03_reel-presentes-o-teto-antes-da-loja/capa.jpg",
    "previa": "saida/2026-12-03_reel-presentes-o-teto-antes-da-loja/previa.mp4",
    "slides": [
        "Capa da grade (tinta, logotipo de fundo escuro) · ORÇAMENTOS · Presentes: o teto antes da loja (“teto” em âmbar) · Uma linha tracejada âmbar atravessa a capa com a pílula “TETO R$ 800”; embaixo, um presente desenhado em traço branco, com o laço.",
        "0 a 3,3 s · Gancho (tinta) · Dezembro passado: · Desde o primeiro quadro, uma etiqueta de presente de contorno âmbar balança presa por um fio, com “R$ 980 em presentes” (o “R$” menor, como no site). Em 1,35 s entra “E este ano?”, em menta.",
        "3,3 a 6,3 s · Em Orçamentos: Definir limites e a busca “Presentes”. · Tela real de Orçamentos no celular (03/12/2026): toque em “Definir limites”, a folha “Definir orçamentos” abre, toque na busca e “Presentes” digitado letra a letra (uma foto real por letra); toque no campo de “Presentes e doações” (média R$ 580). · Nota: Tela real do timtimcash, com dados de exemplo.",
        "6,4 a 9,6 s · Teto de R$ 800, antes da primeira compra. · O valor digitado como no caixa eletrônico (R$ 0,08, R$ 0,80, R$ 8,00, R$ 80,00, R$ 800,00) e o rodapé “LIMITE TOTAL POR MÊS · 6 categorias · R$ 6.250,00”; toque em “Salvar”, o aviso “Orçamentos salvos” e a linha nova “Presentes e doações · R$ 0 de R$ 800 · 0%”, que salta da tela com anel verde.",
        "9,7 a 12,8 s · Dia 17: R$ 774 de R$ 800. No ritmo, vai passar. · Um copo desenhado com a linha tracejada do teto (TETO R$ 800) recebe os presentes como blocos verdes: R$ 120,00 (08/12 · amigo secreto), R$ 389,90 (12/12 · Natal) e R$ 264,50 (17/12 · Natal); o contorno fica âmbar. Embaixo, o recorte real de 17/12: “VÃO ESTOURAR NO RITMO ATUAL · Presentes e doações · R$ 774 de R$ 800 · 97% · no ritmo, fecha em R$ 1.412 · 77% ACIMA”, com anel em 97%.",
        "12,8 a 15,9 s · Dia 21: mais R$ 198. Passou R$ 172. · O bloco de R$ 198,00 (21/12 · Natal) cai e passa da linha: a parte acima do teto fica vermelha e o copo também. O recorte real troca para 21/12: “JÁ PASSARAM DO LIMITE · Presentes e doações · R$ 972 de R$ 800 · 122% · Excedeu em R$ 172 · e, no ritmo, fecha em R$ 1.435 · 79% ACIMA”, com anel em “Excedeu em R$ 172”.",
        "16,0 a 18,6 s · Lição (tinta) · O teto não proíbe a compra. Mostra quanto ainda cabe. (“quanto ainda cabe” em menta), palavra por palavra, com a linha tracejada âmbar do teto se desenhando embaixo.",
        "18,6 a 21,3 s · Fechamento (verde) · Orçamentos no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Dezembro passado: R$ 980 em presentes. E este ano?\n\n"
        "O teto vem antes da loja. Em Orçamentos, toque em Definir limites, busque “Presentes” e escreva o valor. No exemplo do vídeo, R$ 800, definidos no dia 3, antes do primeiro presente.\n\n"
        "Depois, cada presente lançado entra na faixa da categoria. No dia 17, R$ 774 de R$ 800, e o site já mostra que, no ritmo, vai passar. No dia 21, mais R$ 198: passou R$ 172,40.\n\n"
        "O teto não proíbe a compra. Ele mostra quanto ainda cabe, na hora, e não só em janeiro.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#presentesdenatal #orcamento #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Começo de dezembro, antes do amigo secreto e das compras de Natal: é a hora de decidir quanto os presentes podem levar, e não depois da fatura."),
        ("O que desperta interesse", "Um número de dezembro passado (R$ 980) e a pergunta “E este ano?” já no primeiro segundo; depois, uma história com começo, meio e fim na tela real: o teto definido, o aviso do ritmo no dia 17 e o excesso no dia 21."),
        ("Benefício para o público", "Aprende a definir um limite por categoria em segundos (Definir limites, busca, valor, Salvar) e a ler a faixa que mostra quanto ainda cabe, inclusive quando o ritmo indica que vai passar."),
        ("Como contribui para o perfil", "Mostra Orçamentos com a interface de verdade e sem esconder o resultado: o exemplo passa do teto, e o site mostra isso com clareza. Reforça o timtimcash como ferramenta honesta para o fim de ano."),
    ],
    "alt": [
        "Reel de 21 segundos. Num fundo escuro, uma etiqueta de presente balança: dezembro passado, R$ 980 em presentes. E este ano? "
        "Depois, a tela real de Orçamentos do timtimcash no celular, com dados de exemplo: toque em Definir limites, a busca Presentes digitada letra a letra, o valor de R$ 800 digitado na categoria Presentes e doações e o toque em Salvar. A linha nova aparece: R$ 0 de R$ 800. "
        "Um copo desenhado com a linha tracejada do teto de R$ 800 recebe os presentes de dezembro: R$ 120 do amigo secreto e R$ 389,90 e R$ 264,50 de Natal. No dia 17, a tela real mostra R$ 774 de R$ 800 e o aviso de que, no ritmo, vai passar. "
        "No dia 21, mais R$ 198: o bloco passa da linha e fica vermelho, e a tela real mostra Já passaram do limite, R$ 972 de R$ 800, excedeu em R$ 172. "
        "Fecha com a frase: o teto não proíbe a compra, mostra quanto ainda cabe. Orçamentos no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/a0-orcamentos-progresso.png · Orçamentos no celular, Dezembro 2026, rolado até “Progresso por categoria” (botão “Definir limites”), site build 2026-10-16.1, conta de base, relógio em 03/12/2026 10:00 · 3,3 a 4,3 s",
        "telas/a1-definir-orcamentos.png · a folha “Definir orçamentos” depois do toque em “Definir limites” · 4,3 a 5,0 s",
        "telas/a2-busca-01-p.png a a2-busca-09-presentes.png · uma foto real depois de cada letra de “Presentes” na busca da folha · 5,0 a 6,2 s",
        "telas/a3-campo-tocado.png e a4-valor-1.png a a4-valor-5.png · o campo de “Presentes e doações” tocado e o valor digitado dígito a dígito até R$ 800,00 (rodapé: 6 categorias, R$ 6.250,00) · 6,2 a 7,8 s",
        "telas/a5-salvo.png · depois do toque em “Salvar”, com o aviso “Orçamentos salvos” · 7,8 a 8,1 s",
        "telas/a6-orcamentos-rolado-ate-presentes.png · a página rolada até a linha nova “Presentes e doações R$ 0 de R$ 800 0%” (Tranquilas) · 8,1 a 9,6 s, também no recorte ampliado",
        "telas/a7-orcamentos-03-12-alta.png · a mesma página numa foto alta (390 × 1700 px CSS), referência · não aparece no vídeo",
        "telas/b-orcamentos-17-12-alta.png · relógio em 17/12/2026 10:00, o mesmo limite definido pela interface: “VÃO ESTOURAR NO RITMO ATUAL · R$ 774 de R$ 800 · 97%” · recorte de 11,2 a 13,2 s",
        "telas/c-orcamentos-21-12-alta.png · relógio em 21/12/2026 10:00, o mesmo limite: “JÁ PASSARAM DO LIMITE · R$ 972 de R$ 800 · 122% · Excedeu em R$ 172” · recorte de 13,2 a 15,9 s",
        "telas/d-transacoes-dezembro-2025-presentes.png · relógio em 03/12/2026: Transações, “‹” até Dezembro 2025 e a busca “Presentes”: “1 transação · somam R$ 980,00” · conferência do gancho, não aparece no vídeo",
    ],
}
