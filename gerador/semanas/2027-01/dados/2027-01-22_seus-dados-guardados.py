# -*- coding: utf-8 -*-
"""Sexta 22/01/2027 · carrossel "Seus dados, guardados todo dia." (segurança, capa papel). Equipe jb.
Artes: saida/2027-01-22_seus-dados-guardados/01.jpg a 07.jpg, geradas por equipes/jb/posts.py (post_22, conferências por assert).
Telas reais em saida/2027-01-22_seus-dados-guardados/telas/, capturadas por equipes/jb/captura.py (c22), celular 390 px em escala 3,
relógio em 22/01/2027 10:00, build 2026-10-19.5, conta de base.

MUDANÇA (só na cópia jb): o Supabase falso da cópia não guarda cópias; para a lista "Cópias no servidor" aparecer, a cópia jb
devolve uma lista de exemplo (window.__TT_SNAPS__, gravada por estado_jb.py, gerar_22; o site/lib/supabase.min.js da cópia lê essa
lista e, sem ela, se comporta como o da base). É uma cópia por dia em que a pessoa abriu o site: de 16 a 22/01 e o último dia aberto
de outubro, novembro e dezembro (30/10, 30/11 e 31/12, os dias em que ela atualizou a carteira na conta de base). O número de
lançamentos e de contas de cada cópia foi medido no navegador, no estado da conta de cada dia: 795 (hoje), 794, 793, 793, 792, 790,
790, 770 (31/12), 742 e 707 (30/11 e 30/10, com 3 contas, antes do Banco na Europa); todas com 0,1 MB. As horas de abertura são de
exemplo. A tela é o próprio site desenhando essa lista (selos "mais nova" e "fim de dezembro/novembro/outubro", que vêm do código:
ficam as cópias mais novas e a última de cada mês anterior).
Telas: Preferências (Backup, "Cópias no servidor", "Restaurar de backup"); "Restaurar" da cópia de ontem, só a confirmação ("Os dados
de agora (795 lançamentos) serão substituídos pelos de 794 lançamentos daquele dia. Uma cópia de agora é guardada antes, então dá
para voltar atrás.", nada restaurado); o aviso "Você ainda está por aqui?" depois de 29 minutos sem nenhum toque (o relógio da página
andou até 10:29; a foto mostra "Você sai em 59 segundos"); "Ocultar valores" (o olho do topo) na Visão geral.
Frases do site: "Dados criptografados: no envio e no armazenamento" (página do site; nunca "de ponta a ponta"); sessão de 30 minutos
sem uso, aviso um minuto antes e 24 horas (FUNCIONALIDADES, Privacidade). Sem fato externo."""

POST = {
    "pasta": "2027-01-22_seus-dados-guardados",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 7 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 7 imagens",
    "tema": "Segurança dos dados no timtimcash: as Cópias no servidor (uma por dia, guardada sozinha ao abrir o site, com baixar e restaurar), restaurar com volta (o site guarda uma cópia de agora antes), o backup completo em arquivo, a sessão que se fecha depois de 30 minutos sem uso e a cada 24 horas, e Ocultar valores, dados criptografados no envio e no armazenamento e sem conexão com o banco",
    "pilar": "Confiança · produto (Preferências e Privacidade)",
    "data_longa": "sexta-feira, 22 de janeiro de 2027",
    "data_curta": "sexta-feira, 22/01/2027",
    "data_mockup": "22 de janeiro",
    "hora": "10h00",
    "iso": "2027-01-22T10:00:00",
    "slides": [
        "Capa (fundo papel) · SEGURANÇA · Seus dados, guardados todo dia. · Folha de calendário de janeiro de 2027 (faixa escura JANEIRO 2027, a semana começando no domingo): de 1 a 21, cada dia em verde suave com um pequeno escudo de traço com um visto; 22 em verde cheio com o escudo branco; de 23 a 31, só o número, em branco.",
        "EM PREFERÊNCIAS · Uma cópia por dia, sozinha. · Guardada quando você abre o site, à parte da versão em uso. · Tela real no celular (relógio em 22/01/2027): Cópias no servidor, “Uma por dia, guardada sozinha quando você abre o timtimcash, à parte da versão em uso.”; Hoje (mais nova), 795 lançamentos · 4 contas · 0,1 MB · 10:00; Ontem, 794 lançamentos · 19:42; e, depois de três pontos, 31/12/2026 (fim de dezembro), 770 lançamentos · 10:05; cada uma com os botões de baixar e Restaurar. Ao lado: Na lista, as cópias dos últimos dias e a do fim de dezembro, novembro e outubro; Em cada uma, baixar como arquivo ou Restaurar. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "RESTAURAR · Restaurar tem volta. · Antes de trocar, o site guarda uma cópia de agora. E pede para você digitar RESTAURAR. · Tela real da confirmação: “Restaurar a cópia de ontem · Os dados de agora (795 lançamentos) serão substituídos pelos de 794 lançamentos daquele dia. Uma cópia de agora é guardada antes, então dá para voltar atrás. Para confirmar, digite a palavra RESTAURAR abaixo:” e o campo “Digite aqui”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "BACKUP COMPLETO · E um arquivo com tudo, quando quiser. · Guarde onde preferir. Para voltar, é só restaurar dele. · Telas reais: “Exportar backup completo · Arquivo JSON com contas, transações, categorias e orçamentos. Guarde em local seguro para restaurar depois.” com o botão Baixar; “Restaurar de backup · Restaura um JSON exportado anteriormente. Atenção: os dados atuais serão substituídos.” com o botão Restaurar. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "SESSÃO · A sessão se fecha sozinha. · Depois de 30 minutos sem uso, com aviso um minuto antes. E a cada 24 horas. · Tela real do aviso: “Você ainda está por aqui? Você sai em 59 segundos.” com Continuar usando e Sair agora. Dois cartões: 30 min, sem uso; 24 h, mesmo em uso. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "MAIS CUIDADOS · Na tela e no servidor. · Tela real da Visão geral com os valores ocultos (Patrimônio ••••••, o olho riscado no topo). Ao lado: Ocultar valores, o olho no topo esconde os números, até nos gráficos; Dados criptografados, no envio e no armazenamento; Sem conexão com o banco, você decide o que entra. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Seus dados, guardados todo dia. · Gratuito para o controle financeiro, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "Seus dados, guardados todo dia.\n\n"
        "Em Preferências ficam as Cópias no servidor: uma por dia, guardada sozinha quando você abre o timtimcash, à parte da versão em "
        "uso. Cada cópia dá para baixar ou restaurar, e antes de restaurar o site guarda uma cópia de agora, então dá para voltar atrás.\n\n"
        "E tem o backup completo: um arquivo JSON com contas, transações, categorias e orçamentos, para guardar onde quiser.\n\n"
        "A sessão se fecha sozinha depois de 30 minutos sem uso, com aviso um minuto antes, e a cada 24 horas. O olho no topo oculta os "
        "valores da tela. Os dados ficam criptografados no envio e no armazenamento, e o site não se conecta ao banco: você decide o que "
        "entra.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Gratuito para o controle financeiro. Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#privacidade #segurancadigital #controlefinanceiro #financaspessoais #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Na quarta semana da campanha Comece 2027, muita gente acabou de pôr a vida financeira no site. É a hora de responder à pergunta que vem junto: e se eu apagar algo sem querer?"),
        ("O que desperta interesse", "A capa mostra o mês com um escudo em cada dia até hoje. Dentro, telas que quase ninguém conhece: a lista de cópias do servidor, a confirmação que guarda uma cópia antes de restaurar e o aviso de sessão."),
        ("Benefício para o público", "Sabe que existe uma cópia por dia e como restaurar sem medo, onde fica o backup em arquivo, quando a sessão se fecha e como esconder os valores em público."),
        ("Como contribui para o perfil", "Reforça a confiança no produto com fatos verificáveis na tela, sem promessa vaga e sem o “ponta a ponta”. Diferente de 09/10 e 20/12 (exportar): o foco são as cópias diárias e a sessão."),
    ],
    "alt": [
        "Segurança. Seus dados, guardados todo dia. Uma folha de calendário de janeiro de 2027: do dia 1 ao 21, cada dia tem um pequeno escudo verde com um visto; o dia 22, hoje, está em verde cheio com o escudo branco; do 23 ao 31, só os números.",
        "Em Preferências: uma cópia por dia, sozinha, guardada quando você abre o site, à parte da versão em uso. Tela real no celular, com dados de exemplo, da lista Cópias no servidor: hoje, a mais nova, 795 lançamentos e 4 contas, às 10h; ontem, 794 lançamentos, às 19h42; e a de 31 de dezembro de 2026, marcada como fim de dezembro, com 770 lançamentos. Cada cópia tem os botões de baixar e Restaurar. Na lista ficam as cópias dos últimos dias e a do fim de dezembro, novembro e outubro.",
        "Restaurar tem volta. Antes de trocar, o site guarda uma cópia de agora e pede para você digitar a palavra restaurar. Tela real da confirmação Restaurar a cópia de ontem: os dados de agora, 795 lançamentos, serão substituídos pelos de 794 lançamentos daquele dia; uma cópia de agora é guardada antes, então dá para voltar atrás.",
        "E um arquivo com tudo, quando quiser: guarde onde preferir e, para voltar, restaure dele. Telas reais de Exportar backup completo, um arquivo JSON com contas, transações, categorias e orçamentos, com o botão Baixar; e de Restaurar de backup, que restaura um JSON exportado antes e avisa que os dados atuais serão substituídos.",
        "A sessão se fecha sozinha: depois de 30 minutos sem uso, com aviso um minuto antes, e a cada 24 horas. Tela real do aviso Você ainda está por aqui? Você sai em 59 segundos, com os botões Continuar usando e Sair agora. Dois cartões: 30 minutos sem uso e 24 horas mesmo em uso.",
        "Mais cuidados, na tela e no servidor. Tela real da Visão geral com os valores ocultos: o patrimônio aparece como pontos e o ícone do olho está riscado. Ao lado: Ocultar valores, o olho no topo esconde os números, até nos gráficos; dados criptografados no envio e no armazenamento; sem conexão com o banco, você decide o que entra.",
        "Seus dados, guardados todo dia. Gratuito para o controle financeiro, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-preferencias-copias.png · Menu > Preferências, relógio em 22/01/2027 10:00, celular 390 × 3000 em escala 3, conta de base com a lista de cópias de exemplo (cópia jb) · slides 2 (Cópias no servidor: Hoje, Ontem e 31/12/2026) e 4 (Exportar backup completo e Restaurar de backup)",
        "telas/celular-restaurar-copia-de-ontem.png · Restaurar na cópia de ontem: a confirmação, sem digitar nada e sem restaurar · slide 3",
        "telas/celular-aviso-30-minutos.png · Visão geral sem nenhum toque; o relógio da página anda 29 minutos (10:29) e aparece o aviso · slide 5",
        "telas/celular-ocultar-valores.png · Visão geral depois de tocar no olho do topo (Ocultar valores) · slide 6",
    ],
}
