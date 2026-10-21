# -*- coding: utf-8 -*-
"""Quinta 25/02/2027 · Reel "Nova remessa: o câmbio na hora" (investimento no exterior e produto; capa tinta). Equipe fs.
Trocou de dia com "Meta de receita" a pedido da revisão (este era o de 23/02, longe dos outros posts de exterior de fevereiro);
capturado de novo com o relógio em 25/02.
Vídeo, capa e prévia gerados por equipes/fs/reel_25.py (com assert nos textos lidos da tela e na conta); telas capturadas por
equipes/fs/captura_25.py no site build 2026-10-19.5, no celular (390 × 1000 em escala 3), relógio da página em 25/02/2027 10:00, na
cópia da conta da equipe fs (estado.py igual ao da base, com o fechamento de 2026 informado em 29/01). A remessa NÃO é salva (no
fim, "Cancelar"; a conta continua com as mesmas 4 remessas): nada muda na conta e nenhuma tela de Remessas ao exterior aparece.
Passo a passo real: Remessas -> "Nova remessa" (a folha abre com a última remessa como sugestão, em euro) -> moeda "USD · Dólar
americano" -> De "Conta corrente" -> Para "Corretora no exterior" -> Instituição "Corretora no exterior" -> País "Estados Unidos" ->
valores de EXEMPLO, redondos, digitados tecla a tecla: Valor (o total que saiu da conta) R$ 10.110,00, Enviado US$ 2.000,00 e IOF
R$ 110,00 (o do comprovante). A linha da folha termina em "Câmbio efetivo R$ 5,0550 por US$ · IOF 1,10% · US$ 2.000 custaram
R$ 10.110,00". Revisão: enquanto os dólares e o IOF são digitados, a linha passa por valores sem sentido (como "R$ 505500,0000 por
US$" com US$ 0,02); o vídeo corta do toque no campo direto para o valor final, e esses quadros não aparecem. As fotos tecla a
tecla desses dois campos também saíram da pasta telas/ (ficam em equipes/fs/trabalho/fora_da_entrega_25/, só para registro).
Conta (assert no gerador): 10.110 ÷ 2.000 = 5,0550; 10.110 − 110 = 10.000 = 2.000 × 5,00; 110 ÷ 10.000 = 1,10% (o site calcula o IOF
em % sobre o valor sem o IOF). O vídeo e a legenda dizem que os valores são de exemplo. Post de exterior: nenhuma menção a preço do site. A legenda
não cita regra de IOF: o valor é o do comprovante.
Diferença do que já saiu: 29/10 explicou o câmbio efetivo num carrossel e 16/11 tratou do IOF da remessa; aqui é o gesto de lançar,
ao vivo, com a conta aparecendo enquanto se digita."""

POST = {
    "pasta": "2027-02-25_reel-nova-remessa-cambio-na-hora",
    "tipo": "reel",
    "plataforma": "Instagram",
    "formato": "Reel de 20 segundos (1080 × 1920, 9:16), com capa própria na grade",
    "formato_curto": "Reel de 20 s",
    "tema": "Quanto custou cada dólar: na Nova remessa, o total que saiu da conta, os dólares que chegaram e o IOF do comprovante; o câmbio efetivo aparece na hora (valores de exemplo)",
    "pilar": "Investimento no exterior · produto (Remessas ao exterior, Nova remessa)",
    "data_longa": "quinta-feira, 25 de fevereiro de 2027",
    "data_curta": "quinta-feira, 25/02/2027",
    "data_mockup": "25 de fevereiro",
    "hora": "10h00",
    "iso": "2027-02-25T10:00:00",
    "video": "saida/2027-02-25_reel-nova-remessa-cambio-na-hora/reel.mp4",
    "capa": "saida/2027-02-25_reel-nova-remessa-cambio-na-hora/capa.jpg",
    "previa": "saida/2027-02-25_reel-nova-remessa-cambio-na-hora/previa.mp4",
    "slides": [
        "Capa da grade (tinta) · REMESSAS AO EXTERIOR · Quanto custou cada dólar? · “R$ 5,0550” grande em menta, “por dólar, já com o IOF” e o selo “valores de exemplo”.",
        "0 a 2,8 s · Gancho (tinta) · REMESSAS AO EXTERIOR · Quanto custou cada dólar? · Desde o primeiro quadro, “R$ 10.110 ÷ US$ 2.000 =”; em 0,3 s o resultado “R$ 5,0550” salta na tela, já no valor final · por dólar, já com o IOF · valores de exemplo.",
        "3,0 a 5,55 s · Na Nova remessa, digite o total que saiu da conta. · Tela real da “Nova remessa” em dólar no celular (fevereiro de 2027, Conta corrente para Corretora no exterior): R$ 10.110,00 digitado tecla a tecla no Valor (anel). A nota diz “Tela real do timtimcash, com dados de exemplo · valores de exemplo”.",
        "5,7 a 8,55 s · Depois, os dólares que chegaram: o câmbio aparece na hora. · A folha rolada até “Enviado”; o toque no campo e US$ 2.000,00; a linha do site mostra “Câmbio efetivo R$ 5,0550 por US$ · US$ 2.000 custaram R$ 10.110,00” (anel).",
        "8,7 a 11,0 s · E o IOF do comprovante: 1,10%. · O toque no IOF e R$ 110,00; a linha ganha “IOF 1,10%” (anel).",
        "11,0 a 14,55 s · Cada dólar saiu por R$ 5,0550, já com o IOF. · A linha do câmbio de perto e a conta: US$ 2.000 a R$ 5,00 = R$ 10.000,00; IOF do comprovante + R$ 110,00; saiu da conta R$ 10.110,00; ÷ US$ 2.000 = R$ 5,0550 · Valores de exemplo.",
        "14,75 a 17,15 s · Cada remessa entra no seu câmbio médio, em Remessas. (tinta) · Lance com o total, os dólares e o IOF do comprovante. O câmbio de cada envio fica guardado.",
        "17,15 a 19,95 s · Fechamento (verde) · Remessas ao exterior no timtimcash · Acesse pelo navegador, no computador ou no celular. · Link na bio.",
    ],
    "legenda": (
        "Quanto custou cada dólar da sua remessa? A conta aparece na hora.\n\n"
        "No timtimcash, a Nova remessa pede o total que saiu da conta em reais, o valor que chegou lá fora e o IOF que está no "
        "comprovante. Preenchidos os campos, uma linha mostra o câmbio efetivo, o IOF em % e quanto os dólares custaram.\n\n"
        "No vídeo, com valores de exemplo: saíram R$ 10.110 da conta, chegaram US$ 2.000 e o IOF do comprovante foi de R$ 110. "
        "Cada dólar custou R$ 5,0550, já com o IOF.\n\n"
        "Cada remessa lançada entra no seu câmbio médio efetivo, em Remessas ao exterior.\n\n"
        "Tela real do timtimcash, com dados de exemplo.\n\n"
        "Acesse pelo navegador, no computador ou no celular: timtimcash.com\n\n"
        "#investimentonoexterior #cambio #dolar #remessa #timtimcash"
    ),
    "justificativa": [
        ("Por que agora", "Fim de mês, quando muita gente faz o aporte lá fora; o post fica longe dos outros posts de exterior de fevereiro e responde à pergunta que todo mundo faz depois de uma remessa."),
        ("O que desperta interesse", "A pergunta com número no primeiro segundo (“Quanto custou cada dólar?” e R$ 10.110 ÷ US$ 2.000 = R$ 5,0550) e a conta que o site faz sozinho, na tela real."),
        ("Benefício para o público", "Saber o custo real de cada dólar, já com o IOF, sem calculadora, e guardar esse número em cada remessa para comparar os envios."),
        ("Como contribui para o perfil", "Mostra o gesto de lançar uma remessa, que o perfil ainda não tinha mostrado em vídeo, com valores ditos como exemplo e sem falar de preço num post de exterior."),
    ],
    "alt": [
        "Reel de 20 segundos. Fundo escuro: quanto custou cada dólar? R$ 10.110 dividido por US$ 2.000 dá R$ 5,0550 por dólar, já com o IOF; "
        "valores de exemplo. Telas reais do timtimcash no celular, com dados de exemplo. Na Nova remessa em dólar, o total que saiu da conta, "
        "R$ 10.110,00, é digitado; depois, os dólares que chegaram, US$ 2.000,00, e a linha do site mostra o câmbio efetivo, "
        "R$ 5,0550 por US$; com o IOF do comprovante, R$ 110,00, a linha mostra IOF 1,10%. A linha aparece de perto, com a conta: "
        "US$ 2.000 a R$ 5,00 dão R$ 10.000,00, mais R$ 110,00 de IOF, R$ 10.110,00, divididos por US$ 2.000, R$ 5,0550. Cada remessa entra "
        "no seu câmbio médio, em Remessas. Remessas ao exterior no timtimcash. Link na bio."
    ],
    "fontes": [],
    "telas": [
        "telas/celular-remessa-2-dolar.jpg · a Nova remessa em dólar, vazia (De Conta corrente, Para Corretora no exterior, Estados Unidos), depois de trocar a moeda, as contas, a instituição e o país (celular 390 × 1000 em escala 3, build 2026-10-19.5, relógio da página em 25/02/2027 10:00) · 3,0 a 3,75 s",
        "telas/celular-remessa-3-valor-1.jpg a celular-remessa-3-valor-7.jpg · o Valor digitado tecla a tecla até R$ 10.110,00 · 3,75 a 5,6 s",
        "telas/celular-remessa-4-embaixo.jpg · a folha rolada até Enviado, IOF e a linha do câmbio (“Informe o valor em US$ para ver o câmbio da remessa.”) · 5,6 a 6,6 s",
        "telas/celular-remessa-5-enviado-6.jpg · Enviado US$ 2.000,00 e a linha “Câmbio efetivo R$ 5,0550 por US$ · US$ 2.000 custaram R$ 10.110,00” · 6,6 a 9,25 s (as fotos tecla a tecla deste campo, em que a linha passa por valores sem sentido, ficam fora do vídeo e fora da pasta telas/)",
        "telas/celular-remessa-6-iof-5.jpg · IOF R$ 110,00 e “IOF 1,10%” na linha · 9,25 a 11,0 s (as fotos tecla a tecla do IOF também ficam fora do vídeo e da pasta)",
        "telas/celular-remessa-7-pronta.jpg · a folha preenchida (sem salvar); a linha do câmbio, recortada e ampliada · 11,35 a 14,55 s",
        "telas/celular-remessa-0-remessas.jpg e celular-remessa-1-sugestao.jpg · Remessas antes do toque em Nova remessa e a folha com a sugestão da última remessa (em euro); só para conferência, não entram no vídeo",
        "telas/caixas.json · posições medidas na captura, o texto de cada tela, os valores dos campos e a linha do câmbio a cada tecla",
    ],
}
