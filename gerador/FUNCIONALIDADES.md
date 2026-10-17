# O que o timtimcash faz

Ficha tirada do código do site, versão `2026-10-16.1` (16/10/2026), lida em 17/10/2026. Ela agora vale para esse build e substitui a do build `2026-09-30.1`. Serve para os posts: cite só o que está aqui e use os nomes exatos das telas e dos botões, que aparecem entre aspas. O código do site não fica neste repositório. Quando o site mudar, o Samuel envia a versão nova e esta ficha é refeita.

## O que mudou desde o build 2026-09-30.1

- O quarto número da Visão geral e de Transações agora é "Resultado" (era "Saldo"). No modo "Ambos", os cartões mantêm "Receitas", "Despesas" e "Resultado" (eram "Entrou", "Saiu" e "Sobra do mês"). No celular, "Sobrou no período" virou "Resultado do período".
- Saiu a faixa de pendências do topo da Visão geral e de Transações, com "Ver previsto", "Ver pendentes" e "Conciliar tudo". As pendências ficam na tela "Pendentes".
- O "vs média" e as médias da "Análise do período" usam só meses fechados, sem o mês em curso, como o "Diagnóstico".
- A taxa de poupança agora se chama "Receita guardada" em todo o site. O Insight "Melhor poupança em 12 meses" virou "Maior receita guardada em 12 meses". Os Insights e a cor da reserva seguem as metas definidas em Relatórios.
- "Nova conta" não oferece mais o tipo "Cartão de crédito": a linha "É cartão de crédito?" leva ao cadastro do cartão.
- Transferência não tem mais recorrência. A recorrência de uma série já lançada não muda na edição.
- Na "Nova transação", Cmd+Enter (ou Ctrl+Enter) lança ou salva. No celular, a edição termina com "Excluir transação", e o botão Voltar fecha a janela aberta.
- Pendentes: transferência pendente aparece como transferência ("Marcar como feita"), e marcar como paga mostra "Desfazer".
- Sessão: além de sair depois de 30 minutos sem uso, o site pede para entrar de novo a cada 24 horas (eram 7 dias).
- Sem internet, a alteração é salva quando a conexão volta, se a página continuar aberta. Ao voltar para a aba, o site confere se outro aparelho mudou os dados.
- Nomes: "Bem-vindo" virou "Boas-vindas"; no calendário do topo, "Mês atual" virou "Este mês"; em Relatórios, a "Cascata do período" vai "Da receita ao resultado".
- Página do site: saíram "o mais completo do Brasil", "O melhor gerenciador", "Cole o extrato" e a pergunta sobre casal e família. Orçamentos agora fala em "aviso em 70% e 100%".

## Regras para os posts

- O timtimcash é um site, usado no navegador do computador ou do celular. Nunca chamar de app nem falar em baixar ou em loja. Pode dizer que dá para adicionar o site à tela inicial do celular (a própria página do site diz isso).
- "Gratuito" só para o controle financeiro ("Gratuito para o controle financeiro"). Nunca "gratuito para sempre" (nem "gratuito e segue assim", que está nas perguntas frequentes da página) e nunca ligado a remessas ou investimentos no exterior.
- Não usar, mesmo que apareça na página do site: "o mais completo do Brasil", "o melhor", "funciona offline", "iOS e Android", "conta conjunta", "criptografia de ponta a ponta", "cole o extrato", "orçamento anual", "alerta em 70% e 100%". Na página de 16/10 ainda aparecem "Funciona offline após primeiro acesso" e "iOS, Android" (nos dados para buscadores) e "Orçamentos com alerta", com "aviso em 70% e 100%"; os outros saíram.
- Sobre 70% e 100%: o que existe são cartões nos Insights da Visão geral ("N orçamentos acima de 70%" e "N orçamentos estourados"). Não é notificação, e a cor da barra em "Orçamentos" segue outra regra (ver Orçamentos).
- Nomes da tela: receitas menos despesas do período é "Resultado" (não "Saldo" nem "Sobra do mês"), e a taxa de poupança aparece como "Receita guardada". O post pode explicar a taxa de poupança, mas na tela o nome é esse.
- Os Insights são regras fixas. Nunca falar em inteligência artificial.
- Nos exemplos, usar a conta fictícia de `gerador/telas/LEIAME.md`, para os números baterem com as telas reais. As telas da raiz de `gerador/telas/` são do build `2026-09-30.1` e podem mostrar nomes que mudaram; as de novembro e dezembro são do `2026-10-16.1`.

## Onde fica cada coisa

No computador, menu lateral:
- "Menu": "Visão geral", "Transações", "Pendentes" (com contador), "Fluxo", "Relatórios", "Comparar", "Resultado (DRE)", "Orçamentos", "Simulação futura" e "Remessas ao exterior".
- Botões "Importar" e "Exportar".
- "Configurar": "Contas e carteiras", "Cartões de crédito", "Categorias" e "Preferências".
- Lista das contas com o saldo de cada uma e o "Total geral".
- Barra do topo: período, filtro "Todas as contas", busca, "Modo foco", "Ocultar valores" e "Nova".

No celular:
- O botão "Menu" abre o mesmo menu.
- No topo ficam o nome da tela, "Ocultar valores" e o ícone de "Pendentes" (quando há pendências).
- O botão "+" abre "Nova transação".
- Duas telas têm nome curto: "Comparar" e "Remessas".
- O botão Voltar do celular fecha a janela aberta antes de sair do site.

Busca global (Cmd+K no computador): encontra telas, ações, contas, categorias e transações. Há atalhos de teclado, como N para nova transação, F para o modo foco e Cmd+Enter (ou Ctrl+Enter) para lançar ou salvar a transação; "?" mostra a lista.

## Primeiros passos

- Cadastro em "Criar conta": nome completo, e-mail (digitado duas vezes), senha (mínimo de 6 caracteres) e o aceite dos termos. Sem cartão de crédito. Não há login com Google, Apple ou Facebook.
- No login seguinte, o site pede o CPF ("Falta o seu CPF"): um CPF por conta, só para identificar a pessoa. O timtimcash não consulta crédito nem se conecta a bancos. Nos posts, "crie sua conta com nome, e-mail e senha" está certo, mas nunca dizer "sem CPF".
- Conta nova: "Boas-vindas", "Guia rápido" e o botão "Adicionar banco ou carteira". Depois, o cartão "Comece por aqui", com 3 passos.
- O tutorial aparece sozinho só no primeiro acesso. Numa conta vazia, são 3 passos, e o último leva a "Adicionar primeira conta". O tutorial de atalhos fica em "Preferências" ("Tutorial de atalhos").
- "Esqueci minha senha" envia o link para criar uma senha nova.

## Visão geral

- Período: "Mês", "Ano" ou "Personalizado", com setas e calendário (atalhos "Hoje", "Últimos 7d", "Últimos 30d", "Últimos 90d", "Este mês" e "Ano atual", ou as datas digitadas).
- Cálculo: "Realizado" (só o que já entrou e saiu; é o padrão sempre que o site abre), "Previsto" (inclui o que está pendente) ou "Ambos" (o que já aconteceu e quanto falta para o mês fechar).
- Indicadores: "Patrimônio", "Receitas", "Despesas" e "Resultado", com os mesmos nomes nos três modos. A variação compara com a média dos meses fechados, até 12 antes do mês atual ("vs média"), a partir de 3 meses de histórico. O cartão "Patrimônio" mostra quanto ele mudou no mês ("Este mês").
- Embaixo de "Receitas" e "Despesas", o site diz quantos lançamentos pendentes ficaram de fora (ou "inclusos", no Previsto). Não há mais faixa de pendências no topo.
- No celular: cartão do patrimônio com a variação em relação ao fim do mês anterior e um gráfico pequeno de 12 meses, a frase "Guardou X% da receita" e a linha "Resultado do período" (ou "Resultado negativo do período").
- Blocos:
  - "Fluxo mensal", com os últimos 12 meses.
  - "Análise do período": "Receita média" e "Despesa média" (dos meses fechados), "Saldo acumulado" e "Reserva financeira" (em meses), com o botão "Personalizar" (3, 6, 12 ou 24 meses, contas e categorias).
  - "Por categoria": "Despesas" ou "Receitas", com "Top saídas" ou "Top entradas".
  - "Minhas contas" e "Últimas transações".
  - "Insights" ("Análise automática do período"): até 3 cartões, como categoria acima da média, conta fixa que mudou de valor, "Maior receita guardada em 12 meses", "Receita guardada: N%" comparada com a meta, orçamentos estourados ou acima de 70%, contas no negativo e lançamentos vencidos. Cada cartão tem um X para dispensar no mês.
- "Ocultar valores" (o olho) esconde os valores da tela, inclusive os dos gráficos.
- "Modo foco", só no computador.

## Transações

- "Nova transação": "Despesa", "Receita" ou "Transferência".
  - Campos: "Valor", "Data", o interruptor de pagamento, "Categoria", "Pago via" ou "Recebido em" (conta ou cartão) e uma descrição opcional.
  - O interruptor nasce ligado: "Já foi pago" ("Afeta o saldo real da conta agora"). Desligado, vira "Marcar como pago" ("Fica como pendente até você confirmar"). Na receita, "Já foi recebido" ou "Marcar como recebido"; na transferência, "Já foi feita" ou "Marcar como feita". Compra no cartão não tem o interruptor: segue a fatura.
  - Na transferência, os campos são "De" e "Para", sem recorrência.
  - Botão final: "Lançar despesa", "Lançar receita" ou "Registrar transferência" ("Salvar" na edição). Cmd+Enter (ou Ctrl+Enter) faz o mesmo.
- Enquanto a pessoa digita a descrição, o site sugere a categoria (selo "sugerida") e descrições já usadas. A sugestão vem de uma lista de palavras; escolher a categoria à mão desliga a sugestão.
- "Recorrência":
  - "Única".
  - "Fixa": de "Diário" a "Anual"; os lançamentos futuros ficam pendentes.
  - "Parcelada": de 2 a 120 parcelas ("Nº parcelas" e "A cada"); o valor digitado é o total, e o site mostra "N× de R$ ...".
  - Ao editar uma série, o site pergunta: "Apenas esta ocorrência" (ou "Apenas esta parcela") ou "Esta e as próximas não pagas". Ao excluir, há também "A série inteira" (ou "Todas as parcelas").
  - A recorrência de uma série já lançada não muda na edição: é preciso excluir e lançar de novo.
- Compra no cartão entra na fatura certa ("Será incluído na fatura que vence ...").
- No topo da tela: "Saldo acumulado" na data final do período, com "Ver detalhes" para "Receitas", "Despesas" e "Resultado".
- Lista:
  - Busca ("Buscar..."): olha a descrição, a categoria e o valor, sem diferença de acento. Vários termos valem juntos ("100 taxi"). No valor, vale o começo dos números: "100" acha R$ 100,00 e R$ 1.000,00; "100,50" acha só R$ 100,50. A busca não olha o nome da conta nem a data.
  - Filtros "Todas", "Pagas", "Pendentes", "Transferências" e "Todas as categorias" (dá para marcar várias), com "Ordenar" ("Data", "Descrição", "Conta", "Categoria" ou "Valor").
  - Resumo abaixo do título: "N transações · N pagas · N pendentes · somam R$ ... · N no histórico". O "somam" só aparece com filtro ativo (busca, status, categoria ou conta) e é a soma dos valores da lista, não um saldo. Com compras futuras no cartão, entra também "N futuras no cartão". "No histórico" é o total de lançamentos da conta inteira.
  - Com filtro ativo, a faixa "Agir sobre as N filtradas" traz "Recategorizar todas", "Trocar conta" e "Limpar filtro".
  - "Exportar" da lista baixa exatamente o que está filtrado, em "Excel (.xlsx)" ou "CSV".
- Ações em lote: "Selecionar", com "Selecionar tudo", "Pagas", "Pendentes", "Recategorizar", "Trocar conta" e "Excluir".
- Excluir tem "Desfazer". No celular, arrastar a linha mostra "Editar" e "Excluir", e a edição termina com "Excluir transação".
- Categorias:
  - O cadastro começa com 21 categorias de despesa e 4 de receita.
  - Em "Categorias" dá para criar, renomear, trocar cor e ícone ("Aparência"), criar subcategorias, mover, reordenar e excluir. Para excluir uma categoria com lançamentos, é preciso mover os lançamentos antes.
  - Categorias podem ser exportadas e importadas em planilha.

## Pendentes

- Contas a pagar e a receber: o que não foi pago no período e tudo o que já venceu, de qualquer mês, mais as faturas de cartão não pagas (agrupadas por fatura).
- Indicadores "A pagar" e "A receber", mais "Vencidas" (quando há) ou "Total pendente" (quando nada venceu).
- Blocos "Vencidas" ("Resolva primeiro: pague, receba ou reagende"), com o botão "Marcar transações como pagas" (ou "como recebidas", conforme o tipo), e "A vencer". Sem vencidas, aparece "Nada vencido. Tudo dentro do prazo." Datas como "Hoje", "Amanhã", "Ontem", "Em N dias" e "Há N dias".
- Um toque em "pendente" marca como paga ou recebida, e o aviso traz "Desfazer". Transferência pendente aparece como transferência ("Marcar como feita").
- Sem pendências, a tela mostra "Tudo em dia". Conta sem nenhuma pendência e sem cartão vê "Contas a pagar e a receber", com o botão "Lançar conta a pagar".

## Contas e cartões

- "Contas e carteiras": "Patrimônio consolidado" (soma das contas que entram no total) e o botão "Nova conta".
  - Tipos: "Banco / Digital", "Dinheiro / Carteira", "Investimento" e "Outro". Conta nova não nasce como cartão: a linha "É cartão de crédito?" ("fatura e limite ficam em Cartões") abre o cadastro do cartão. Contas antigas do tipo "Cartão de crédito" continuam assim.
  - Campos: nome, tipo, "Saldo atual" ("quanto tem na conta hoje"; pode ser negativo, para cheque especial), "Incluir no patrimônio total", cor e ícone. Na edição, o saldo aparece como "Saldo inicial".
  - No guia de boas-vindas, o botão se chama "Adicionar banco ou carteira".
- "Cartões de crédito":
  - Limite, "Fecha no dia", "Vence no dia" e "Paga com" (a conta de onde sai o pagamento).
  - Em cada cartão: "Próximas faturas", "Limite usado", "Disponível" e "Pagar fatura".
  - No menu lateral, "Considerar faturas abertas" (quando há fatura aberta).
- Transferência entre contas é um tipo de transação, com "De" e "Para".

## Importar

- Botão "Importar" ("Importar transações"): planilha (.xlsx, .xls ou .csv) ou extrato do banco (.ofx). O formato é detectado sozinho.
- Planilha:
  - 6 colunas, em qualquer ordem: data, categoria, descrição, conta ou carteira, valor e pago.
  - Valor positivo é receita; negativo é despesa.
  - Categorias e contas novas são criadas na importação. Na revisão, a conta que ainda não existe aparece como "Nova: " seguido do nome.
  - Botão "Baixar modelo em Excel".
- Extrato .ofx:
  - A pessoa escolhe a conta de destino.
  - As categorias chegam sugeridas pelo nome do estabelecimento.
  - Transações já importadas são detectadas e desmarcadas.
- "Revisar importação", antes de confirmar:
  - Ajusta descrição, valor, categoria, status e conta de cada linha, ou tira a linha.
  - Selos "sugerida" e "automático".
  - Botão final "Importar N linhas".
- Regras: ao categorizar uma linha, o site pergunta "Automatizar esta categoria?" ("Aplicar e lembrar" ou "Só esta linha"). As regras ficam em "Regras de importação" e nunca mudam o que a pessoa escolheu à mão.
- Depois de um .ofx, se o saldo não bater com o do banco, aparece "O saldo não bate com o banco", com a opção de ajustar.
- A importação é só por arquivo. Não dá para colar o extrato nem importar PDF.

## Orçamentos

- Limite mensal por categoria de despesa e meta mensal de receita ("Metas de receita"). Na visão do ano, o limite mensal é multiplicado pelos meses.
- "Definir limites" abre "Definir orçamentos" ("Despesas" e "Receitas").
- Sem limites definidos, o site sugere começar pela média dos 12 meses fechados ("Comece pela sua média dos últimos 12 meses"), com "Usar estes limites" ou "Definir do zero".
- Cabeçalho: "Gasto total no período", o ritmo do mês ("N de M dias · X% do período"), a porcentagem do limite e uma barra com a marca de hoje. Embaixo, "Limite definido", "Usado do limite" e "Sobra do limite" (ou "Acima do limite"), com quanto dá para gastar por dia nos dias que faltam.
- "Progresso por categoria", em ordem de "Risco", "Maior gasto" ou "A a Z", com o filtro "Só com limite":
  - Faixas: "Já passaram do limite", "Vão estourar no ritmo atual", "No limite", "Tranquilas" e "Sem limite definido".
  - Ritmo: a marca vertical é hoje, e a barra à esquerda dela está dentro do ritmo. A projeção só aparece depois de 15% do período.
  - A cor segue a projeção para o fim do mês: amarelo a partir de 90%, vermelho acima de 102% ou quando o limite já foi ultrapassado.
  - Em cada categoria: "Excedeu em R$ ..." e "no ritmo, fecha em R$ ...".
- Sugestões em "Onde definir limite primeiro" ("Usar R$ ..." ou "outro valor").

## Fluxo

- Card do período: "Entrou", "Saiu" e "Guardou X% do que entrou" (ou "Faltou").
- Gráfico "Fluxo detalhado": "Receitas" e "Despesas" em barras, "Resultado" em linha e "Saldo acumulado" em área. Por padrão, os últimos 12 meses, com período próprio.
- "Top entradas" e "Top saídas": as 5 maiores categorias.
- Tabela "Resumo mensal": "Entradas", "Saídas", "Resultado" e "Saldo" mês a mês, com o "Total do período".
- Só entram lançamentos pagos ou recebidos. O Fluxo não projeta o futuro; a projeção fica na "Simulação futura".

## Relatórios

Uma página com painéis e uma faixa de atalhos no topo ("Diagnóstico", "O que mudou", "Concentração", "Receitas × Despesas", "Cascata", "Receitas", "Despesas", "Mapa de calor", "Variações", "Recorrentes", "Sazonalidade" e "Saldo"). No computador, a faixa tem setas. O filtro "Todas as categorias" vale para a página, e só entram lançamentos pagos ou recebidos.
- "Diagnóstico":
  - A "Receita guardada" do período (quanto da receita sobrou) comparada com a média da própria pessoa ("Comparado com seus últimos 12 meses"), e o maior desvio do período.
  - "Receita guardada", "Despesas do período" e "Reserva" (quantos meses o patrimônio cobre os gastos).
  - "Ajustar cálculo" abre "Como o diagnóstico é calculado": janela de 3, 6, 12 ou 24 meses, "Ignorar meses vazios" e as metas de "Receita guardada" (padrão de 20%) e "Reserva de emergência" (padrão de 6 meses).
  - Com menos de 3 meses de histórico, não compara com a média.
- "O que mudou": as categorias que mais fugiram da média ("Maiores desvios em relação à sua média de N meses").
- "Concentração": quantas categorias respondem pela maior parte do gasto.
- "Receitas vs Despesas": comparativo mensal, em barras ou linha.
- "Cascata do período": da receita ao resultado.
- "Receitas por categoria" e "Despesas por categoria": rosca com subcategorias. Clicar leva às transações.
- "Mapa de calor": gasto por categoria, mês a mês.
- "Maiores variações", contra o período anterior.
- "Recorrentes vs pontuais": "Recorrente", "Recorrente/mês" e "Maior compromisso".
- "Sazonalidade": média de despesas por mês do ano (precisa de dois meses fechados com despesas).
- "Saldo acumulado".

## Comparar

- "Comparar períodos":
  - "Janela em foco": "Este mês", "3 meses", "6 meses", "No ano", "12 meses" ou "Escolher meses…".
  - "Comparar com": "Período anterior", "Mesmo período em" (o ano anterior) ou "Escolher datas…".
- Despesas ou receitas, com filtro de categorias.
- Com o mês em curso, compara até o mesmo dia do mês anterior ("Cortar no mesmo dia"), para a conta ser justa. Janelas de tamanhos diferentes podem ser comparadas por média diária.
- Painéis:
  - Diferença em R$ e em %, com uma frase que aponta a causa ("Quase toda a alta veio de ...").
  - "Ponte de variação": o que causou a diferença.
  - Cada categoria nos dois períodos ("Halteres" ou "Espelhado").
  - O ritmo dentro do período.
  - Cada painel traz uma leitura em texto ("Leia assim").

## Resultado (DRE)

- "Demonstrativo de resultado": receitas menos despesas, por categoria e subcategoria, com a "% da receita".
- "Consolidado" ou "Mês a mês" (quando o período tem mais de um mês).

## Simulação futura

- "Simulação de fluxo futuro": cenários do saldo nos próximos meses. Horizontes "6 meses", "1 ano", "2 anos" e "5 anos", ou um mês escolhido (até 10 anos).
- Cada cenário tem:
  - Nome e "Saldo de partida" (o saldo atual de todas as contas ou um valor manual).
  - Receitas e despesas estimadas por mês, por categoria.
  - "Regras": "+ A partir de um mês", "+ Um mês do ano" e "+ Um mês específico".
  - "Preencher com média", que usa a média de 3, 6, 12 ou 24 meses.
- Resultado:
  - Saldo no fim e quanto sobra por mês.
  - Gráfico a partir de "Hoje".
  - Meta opcional ("Definir uma meta"), com o mês em que é atingida.
  - Linha do tempo.
- "E se…": "Testa um susto sobre o cenário, sem alterar nada."
  - Testes: "Receita −10%", "Despesa +10%", "Perde a maior renda", "Inflação 5% a.a." ou outro valor.
- "Plano contra realidade": compara quanto o plano prevê que sobre por mês com quanto sobrou de fato nos últimos 6 meses fechados. "Ajustar o plano pelo real" troca os valores base pela média dos últimos 12 meses (só os meses com movimento).
- Cenário base (selo "base"): cada cartão mostra a diferença para a base.
- "Comparar": até 5 cenários de uma vez, com o saldo projetado mês a mês.
- A simulação não calcula juros nem rendimento sobre o saldo.

## Remessas ao exterior

- Lançar:
  - "Nova remessa" (daqui para fora) ou "Resgate" (de volta para cá), os dois botões do topo.
  - Campos: valor enviado na moeda, data, instituição, moeda, país do investimento, contas de origem e destino, total debitado em R$ e IOF (está no comprovante).
  - Uma remessa nova abre dentro da "Nova transação" (título "Nova remessa"). Ao preencher, uma linha mostra o câmbio efetivo ("Câmbio efetivo R$ X por US$"), o IOF em % e quanto os dólares custaram em reais. Não mostra o câmbio sem IOF nem avisos.
  - Ao editar uma remessa já salva ("Editar remessa"), aparece o cálculo completo ("Calculado na hora": valor antes do IOF, câmbio sem IOF, câmbio efetivo e alíquota) e um aviso quando o câmbio ou a alíquota do IOF parecem fora do usual.
  - No menu de três pontos ("Mais ações"): "Importar planilha" e "Baixar planilha modelo".
- 18 moedas e 41 destinos (países e a zona do euro). Com mais de uma moeda em uso, botões no topo trocam a moeda em foco.
- "Atualizar carteira": a pessoa informa quanto tem lá fora (valor total ou por banco, com "Adicionar banco"), e o câmbio é sugerido. O botão "Atualizar" diz há quantos dias foi a última vez.
- Cotação:
  - O site busca sozinho a PTAX de compra do Banco Central, com a data e a hora do boletim.
  - Se ela faltar, usa a taxa de referência do Banco Central Europeu ou a cotação comercial.
  - A cotação é só uma sugestão até a pessoa salvar.
- Cabeçalho: "Investido no exterior", o valor "na carteira hoje", o valor em reais ao câmbio de hoje e o resultado na moeda e em reais.
- "De onde veio o resultado em reais": você enviou, rendimento, efeito do câmbio e hoje.
- "Câmbio: onde você está": mostra o câmbio de equilíbrio, que zera o resultado em reais (abaixo dele, prejuízo), o câmbio médio da pessoa e o câmbio que empata com o CDI.
- "A jornada": o enviado acumulado e a trajetória da carteira, com os marcos "Primeira remessa", "Envios", "Maior envio" e "Média por envio".
- "Ritmo do retorno": a TIR (taxa interna de retorno) com as datas reais de cada remessa, "no período", "ao ano" ou "ao mês", na moeda e em reais.
- "Contra o CDI": "Bruto" ou "Líquido de IR" (o líquido simula resgatar tudo hoje).
- "Rendimento ano a ano": aportes, câmbio médio e posição no fim de cada ano, em dólar e em reais. Cada aporte pesa pelo tempo que ficou investido.
- "Editar fechamentos" (ou "Informar fechamentos") abre "Quanto havia no fim de cada ano": saldo de 31/12 e câmbio de cada ano. O botão "PTAX" busca a PTAX de compra do fim do ano no Banco Central.
- Indicadores "Remetido", "Custo total", "Câmbio médio efetivo" e "IOF pago".
- Tabela "Remessas", "Por remessa" ou "Por ano", com "Investido há".
- Não tem campo de tarifa ou spread, e não soma várias moedas num total único.

## Exportar, backup e preferências

- "Exportar" ("Exportar transações"): período ("Período atual filtrado", "Ano atual", "Todas as transações" ou "Personalizado"), contas à escolha e formato "Excel" (.xlsx), "PDF" ("Relatório pronto") ou "CSV".
- O PDF abre numa aba nova o "Relatório financeiro": período, data de geração, quantidade de transações e o nome (ou o e-mail) da pessoa no cabeçalho; "Receitas", "Despesas", "Resultado" e "Lançamentos"; "Despesas por categoria" (as 8 maiores); e a tabela "Transações do período". A janela de impressão abre sozinha, e o botão "Imprimir / Salvar PDF" fica no canto. O navegador precisa permitir pop-ups.
- "Preferências":
  - Tema "Claro", "Escuro" ou "Auto".
  - Nome, e-mail e CPF, e o botão "Sair".
  - "Tutorial de atalhos" e "Ver atalhos".
  - "Exportar backup completo" (arquivo JSON) e "Restaurar de backup".
  - "Cópias no servidor": uma por dia, guardada sozinha quando a pessoa abre o site. Cada cópia pode ser baixada ou restaurada, e antes de restaurar o site guarda uma cópia de agora.
  - "Zona de risco": "Apagar todas as transações", "Resetar conta completamente" e "Excluir minha conta" (pedido por e-mail; apaga o acesso, o CPF e os dados).
- O site salva sozinho ("Salvando...", "Salvo"). Se a conexão cair, a alteração é salva quando ela voltar, com a página aberta. Se outro aparelho ou aba mudou os dados, a tela é atualizada e o aviso diz o que não foi salvo.

## Privacidade

- Não se conecta ao banco (sem Open Finance): a pessoa decide o que entra.
- Sem propaganda.
- A página do site diz "Dados criptografados: no envio e no armazenamento". Pode repetir assim, nunca "de ponta a ponta".
- "Ocultar valores" esconde os números da tela.
- Por segurança, a sessão termina sozinha depois de 30 minutos sem uso (com o aviso "Você ainda está por aqui?" um minuto antes) e a cada 24 horas, mesmo em uso.
- Exporta tudo quando a pessoa quiser: Excel, PDF, CSV e backup completo.

## Frases da página do site que os posts podem ecoar

- "Seu dinheiro deixa pistas todos os dias."
- "Não só o quanto. O porquê." (Comparar)
- "Categorize uma vez, o timtimcash aprende." (regras de importação)
- "Quanto rende o seu dinheiro lá fora." (Remessas)
- "Todo dinheiro, um só lugar." (contas)
- "Quanto entrou, quanto saiu, quanto sobrou." (Resultado)
- "Saiba quando está chegando no limite." (Orçamentos)
- "E se o próximo ano fosse diferente?" (Simulação futura)

## O que não existe (não citar)

- Conexão com banco ou Open Finance (a ausência é o diferencial).
- Aplicativo em loja; login com Google, Apple ou Facebook.
- Notificações, e-mails ou lembretes de vencimento.
- Anexos, fotos de recibo, observações ou etiquetas nos lançamentos.
- Colar extrato ou importar PDF.
- Orçamento anual.
- Uso compartilhado por casal ou família.
- Outra moeda principal (tudo é em reais, fora das remessas).
- Inteligência artificial.
- Transferência recorrente (fixa ou parcelada).
- Mudar a recorrência de uma série já lançada (só excluindo e lançando de novo).
- Exportar DRE, cenários ou remessas em planilha ou PDF (cenários e remessas só saem no backup completo, em JSON).
- Juros sobre o saldo na simulação.
- Tarifa ou spread nas remessas.
