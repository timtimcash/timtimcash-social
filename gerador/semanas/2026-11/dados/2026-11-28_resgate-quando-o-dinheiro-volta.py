# -*- coding: utf-8 -*-
"""Sábado 28/11/2026 · carrossel "O dinheiro voltou. E o câmbio?" (investimento no exterior, capa verde suave). Plano A da pauta
(o Resgate de Remessas), não o plano B.
Artes: saida/2026-11-28_resgate-quando-o-dinheiro-volta/01.jpg a 06.jpg, geradas por equipes/c2/posts.py (contas por assert).
Telas reais novas em saida/2026-11-28_resgate-quando-o-dinheiro-volta/telas/, capturadas por equipes/c2/captura.py com o
relógio em 28/11/2026 10:00, na conta de N/base_app (build 2026-10-16.1):
- o botão "Resgate" da tela Remessas abre "Novo resgate" (transferência de Corretora no exterior para Conta corrente) com
  os campos Valor (o que entrou, em R$), Data, "Já foi feita", De, Para, "Resgate do exterior", "Resgatado · o que saiu lá
  fora" (US$), Instituição, País e "+ Teve IOF? Adicionar". Preenchido com R$ 5.020,00 e US$ 1.000,00, mostra
  "Câmbio efetivo R$ 5,0200 por US$ · US$ 1.000 viraram R$ 5.020,00" (foto sem salvar);
- depois, o mesmo resgate salvo SÓ na sessão do navegador da captura (o Supabase da cópia é falso e descarta gravações;
  nenhum arquivo da conta mudou): a lista "Remessas" ganha o cartão RESGATE (−US$ 1.000,00, câmbio R$ 5,0200,
  28/11/2026) e o topo avisa "1 movimentação posterior ao valor informado, fora do ganho", ao lado de "Atualizar · há 29
  dias" (a carteira foi informada em 30/10/2026). O resultado da carteira não muda até atualizar o valor.
Exemplo do slide 3 (ilustrativo, só o efeito do câmbio): US$ 1.000 que foram ao câmbio médio de R$ 5,00 (as 3 remessas
de US$ 4.000 a R$ 4,90, R$ 5,00 e R$ 5,10) custaram R$ 5.000; voltam a R$ 4,50 (R$ 4.500, −R$ 500), a R$ 5,02 (R$ 5.020,
+R$ 20) ou a R$ 5,50 (R$ 5.500, +R$ 500). Nenhuma alíquota de IOF na volta é afirmada."""

POST = {
    "pasta": "2026-11-28_resgate-quando-o-dinheiro-volta",
    "tipo": "carrossel",
    "plataforma": "Instagram",
    "formato": "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)",
    "formato_curto": "Carrossel de 6 imagens",
    "tema": "O dinheiro voltou: todo dólar tem o câmbio da ida e o da volta, e o resultado em reais só se realiza na volta, ao câmbio do dia; o Resgate de Remessas registra a volta com o câmbio efetivo, e a carteira deve ser atualizada depois",
    "pilar": "Investimento no exterior · produto",
    "data_longa": "sábado, 28 de novembro de 2026",
    "data_curta": "sábado, 28/11/2026",
    "data_mockup": "28 de novembro",
    "hora": "10h00",
    "iso": "2026-11-28T10:00:00",
    "slides": [
        "Capa (fundo verde suave) · INVESTIMENTO NO EXTERIOR · O dinheiro voltou. E o câmbio? · Uma seta verde grande em U sai da pílula “US$” (branca, em cima) e volta à pílula “R$” (verde, embaixo); dentro da volta, a etiqueta “câmbio do dia?”.",
        "IDA E VOLTA · Todo dólar tem dois câmbios. · O da ida, que você já pagou. E o da volta, que só se conhece no dia em que o dinheiro volta. · Linha do tempo: 3 idas, câmbio médio R$ 5,00 (R$ 4,90 em 12/07/23, R$ 5,00 em 14/03/24 e R$ 5,10 em 18/04/24); trecho tracejado “lá fora”; 1 volta, R$ 5,02 em 28/11/26. · Nota: Exemplo: as remessas da conta fictícia dos nossos posts e um resgate de US$ 1.000.",
        "NA VOLTA · O mesmo dólar volta valendo outro real. · US$ 1.000 que foram a R$ 5,00 custaram R$ 5.000. Na volta, valem o câmbio do dia. · Barras a partir da linha do custo na ida (R$ 5.000): volta a R$ 4,50, R$ 4.500, −R$ 500 (vermelho); a R$ 5,02, R$ 5.020, +R$ 20; a R$ 5,50, R$ 5.500, +R$ 500 (verde). · Nota: Exemplo ilustrativo: só o efeito do câmbio, sem o rendimento lá fora, sem IOF e sem tarifa.",
        "NO TIMTIMCASH · O Resgate registra a volta. · Em Remessas ao exterior: o que saiu lá fora, o que entrou na conta e o câmbio da volta, na hora. Teve IOF? Informe o do comprovante. · Tela real do “Novo resgate” no celular, sem salvar (relógio em 28/11/2026): Resgatado US$ 1.000,00 (“o que saiu lá fora”); Instituição Corretora no exterior; País Estados Unidos; “+ Teve IOF? Adicionar”; faixa verde “Câmbio efetivo R$ 5,0200 por US$ · US$ 1.000 viraram R$ 5.020,00”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "DEPOIS DA VOLTA · Atualize a carteira. · O resgate entra na lista com o câmbio dele. Até você atualizar o valor da carteira, ele fica fora do ganho. · Dois recortes da tela real de Remessas no celular (relógio em 28/11/2026, resgate salvo só na sessão da captura): o cartão “Corretora no exterior → Conta corrente · RESGATE · −US$ 1.000,00 · custo −R$ 5.020,00 · 28/11/2026 · câmbio R$ 5,0200 · este mês”; e o topo com “Atualizar · há 29 dias” e “1 movimentação posterior ao valor informado, fora do ganho”. · Nota: Tela real do timtimcash, com dados de exemplo.",
        "Fechamento (fundo verde) · Registre a ida e a volta. · Remessas ao exterior no timtimcash, no computador ou no celular. · Botão: Link na bio.",
    ],
    "legenda": (
        "O dinheiro voltou de lá de fora. E o câmbio?\n\n"
        "Todo dólar enviado tem dois câmbios: o da ida, que você já pagou, e o da volta, que só se conhece no dia do resgate. "
        "Até lá, o resultado em reais muda com o câmbio de cada dia.\n\n"
        "No exemplo, US$ 1.000 que foram a R$ 5,00 custaram R$ 5.000. Se voltam a R$ 5,02, viram R$ 5.020. A R$ 4,50, seriam R$ 4.500; a R$ 5,50, R$ 5.500. "
        "Exemplo ilustrativo, só com o efeito do câmbio; o post não recomenda investimento.\n\n"
        "No timtimcash, o botão Resgate, em Remessas ao exterior, registra a volta: o que saiu lá fora e o que entrou na conta, com o câmbio efetivo na hora. "
        "Teve IOF? Informe o do comprovante. Depois, atualize a carteira para o ganho incluir o resgate.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #cambio #dolar #educacaofinanceira #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Último sábado de novembro, com o 13º e a Black Friday mexendo no caixa: é quando muita gente pensa em trazer dinheiro de volta. Fecha o mês de exterior (o câmbio médio em 12/11, o IOF em 16/11 e a carteira atualizada em 25/11) com a outra ponta: a volta."),
        ("O que desperta interesse", "A capa é uma seta de volta, do US$ para o R$, com a pergunta que todo investidor lá fora se faz: com qual câmbio? O slide 3 mostra o mesmo US$ 1.000 virando R$ 4.500 ou R$ 5.500."),
        ("Benefício para o público", "Entende que o resultado em reais só se realiza na volta, ao câmbio do dia, e vê o tamanho desse efeito num exemplo simples. Sem afirmar alíquota de IOF na volta (o que vale é o comprovante) e sem recomendação de investimento."),
        ("Como contribui para o perfil", "Mostra uma função pouco vista, o Resgate de Remessas, com telas reais novas e um cuidado prático que o próprio site lembra: atualizar a carteira depois do resgate. Sem ligar remessas a gratuidade."),
    ],
    "alt": [
        "Investimento no exterior. O dinheiro voltou. E o câmbio? Uma seta verde grande em U sai de uma pílula com US$ e volta a outra com R$; dentro da volta, a etiqueta: câmbio do dia?",
        "Ida e volta: todo dólar tem dois câmbios. O da ida, que você já pagou, e o da volta, que só se conhece no dia em que o dinheiro volta. Linha do tempo com 3 idas, câmbio médio de R$ 5,00: R$ 4,90 em 12 de julho de 2023, R$ 5,00 em 14 de março de 2024 e R$ 5,10 em 18 de abril de 2024; um trecho tracejado, lá fora; e 1 volta, a R$ 5,02, em 28 de novembro de 2026.",
        "Na volta, o mesmo dólar volta valendo outro real. US$ 1.000 que foram a R$ 5,00 custaram R$ 5.000; na volta, valem o câmbio do dia. Volta a R$ 4,50: R$ 4.500, R$ 500 a menos. Volta a R$ 5,02: R$ 5.020, R$ 20 a mais. Volta a R$ 5,50: R$ 5.500, R$ 500 a mais. Exemplo ilustrativo, só com o efeito do câmbio, sem rendimento, sem IOF e sem tarifa.",
        "No timtimcash, o Resgate registra a volta: o que saiu lá fora, o que entrou na conta e o câmbio da volta, na hora; teve IOF, informe o do comprovante. Tela real do Novo resgate no celular, com dados de exemplo: resgatado, US$ 1.000,00, o que saiu lá fora; instituição, Corretora no exterior; país, Estados Unidos; o botão Teve IOF? Adicionar; e a faixa verde: câmbio efetivo de R$ 5,0200 por US$, US$ 1.000 viraram R$ 5.020,00.",
        "Depois da volta, atualize a carteira. O resgate entra na lista com o câmbio dele; até você atualizar o valor da carteira, ele fica fora do ganho. Telas reais de Remessas no celular, com dados de exemplo: o cartão do resgate, de Corretora no exterior para Conta corrente, menos US$ 1.000,00, câmbio de R$ 5,0200, em 28 de novembro de 2026; e o botão Atualizar, há 29 dias, com o aviso: 1 movimentação posterior ao valor informado, fora do ganho.",
        "Registre a ida e a volta. Remessas ao exterior no timtimcash, no computador ou no celular. Link na bio.",
    ],
    "fontes": [],
    "telas": [
        "telas/celular-novo-resgate-preenchido.png · “Novo resgate” aberto pelo botão “Resgate” da tela Remessas ao exterior e preenchido (valor R$ 5.020,00, resgatado US$ 1.000,00, sem IOF), sem salvar; mostra “Câmbio efetivo R$ 5,0200 por US$ · US$ 1.000 viraram R$ 5.020,00”; relógio em 28/11/2026 10:00 (celular, 390 × 1200 em escala 3) · slide 4",
        "telas/celular-remessas-com-resgate.png · a tela Remessas ao exterior depois de salvar o mesmo resgate só na sessão do navegador da captura (nada gravado na conta): o topo com “Atualizar · há 29 dias” e “1 movimentação posterior ao valor informado, fora do ganho”, e a lista “Remessas” com o cartão RESGATE (−US$ 1.000,00, câmbio R$ 5,0200, 28/11/2026); relógio em 28/11/2026 10:00 (celular, 390 × 4600 em escala 3) · slide 5",
    ],
}
