# O que o timtimcash faz

Ficha tirada do código do site (versão `2026-09-30.1`, lida em 30/09/2026). Serve para os posts: cite só o que está aqui e use os nomes exatos das telas e dos botões, que aparecem entre aspas. O código do site não fica neste repositório. Quando o site mudar, o Samuel envia a versão nova e esta ficha é refeita.

## Regras para os posts

- O timtimcash é um site, usado no navegador do computador ou do celular. Nunca chamar de app nem falar em baixar ou em loja. Pode dizer que dá para adicionar o site à tela inicial do celular (a própria página do site diz isso).
- "Gratuito" só para o controle financeiro ("Gratuito para o controle financeiro"). Nunca "gratuito para sempre" e nunca ligado a remessas ou investimentos no exterior.
- Não usar, mesmo que apareça na página do site: "o mais completo do Brasil", "o melhor", "funciona offline", "iOS e Android", "conta conjunta", "criptografia de ponta a ponta", "cole o extrato", "orçamento anual", "alerta em 70% e 100%".
- Os Insights são regras fixas. Nunca falar em inteligência artificial.
- Nos exemplos, usar a conta fictícia de `gerador/telas/LEIAME.md`, para os números baterem com as telas reais.

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

Busca global (Cmd+K no computador): encontra transações, contas e telas. Há atalhos de teclado, como N para nova transação e F para o modo foco.

## Primeiros passos

- Cadastro em "Criar conta": nome completo, e-mail (digitado duas vezes), senha (mínimo de 6 caracteres) e o aceite dos termos. Sem cartão de crédito. Não há login com Google, Apple ou Facebook.
- No login seguinte, o site pede o CPF ("Falta o seu CPF"): um CPF por conta, só para identificar a pessoa. O timtimcash não consulta crédito nem se conecta a bancos. Nos posts, "crie sua conta com nome, e-mail e senha" está certo, mas nunca dizer "sem CPF".
- Conta nova: "Bem-vindo", "Guia rápido" e o botão "Adicionar banco ou carteira". Depois, o cartão "Comece por aqui", com 3 passos.
- O tutorial aparece sozinho no primeiro acesso e pode ser revisto em "Preferências".
- "Esqueci minha senha" envia o link para criar uma senha nova.

## Visão geral

- Período: "Mês", "Ano" ou "Personalizado", com setas e calendário (atalhos "Hoje", "Últimos 7d", "Últimos 30d", "Últimos 90d", "Mês atual" e "Ano atual").
- Cálculo: "Realizado" (só o que já entrou e saiu), "Previsto" (inclui o que está pendente) ou "Ambos".
- Indicadores: "Patrimônio", "Receitas", "Despesas" e "Saldo". Em "Ambos" viram "Entrou", "Saiu" e "Sobra do mês". A variação compara com a média dos últimos 12 meses ("vs média"), a partir de 3 meses de histórico.
- No celular: cartão do patrimônio com a variação em relação ao mês anterior e um gráfico pequeno de 12 meses, a frase "Guardou X% da receita" e a linha "Sobrou no período" (ou "Faltou no período").
- Aviso de pendências, com "Ver previsto" e "Ver pendentes".
- Blocos:
  - "Fluxo mensal", com os últimos 12 meses.
  - "Análise do período": "Receita média", "Despesa média", "Saldo acumulado" e "Reserva financeira" (em meses), com o botão "Personalizar".
  - "Por categoria": "Despesas" ou "Receitas", com "Top saídas" ou "Top entradas".
  - "Minhas contas" e "Últimas transações".
  - "Insights" ("Análise automática do período"): até 3 cartões, como categoria acima da média, melhor poupança em 12 meses, orçamentos estourados ou acima de 70%, contas no negativo e lançamentos vencidos.
- "Ocultar valores" (o olho) esconde os valores da tela, inclusive os dos gráficos.
- "Modo foco", só no computador.

## Transações

- "Nova transação": "Despesa", "Receita" ou "Transferência".
  - Campos: "Valor", "Data", "Marcar como pago" (fica pendente até a pessoa confirmar), "Categoria", "Pago via" ou "Recebido em" (conta ou cartão) e uma descrição opcional.
  - Na transferência, os campos são "De" e "Para".
- Enquanto a pessoa digita a descrição, o site sugere a categoria (selo "sugerida") e descrições já usadas.
- "Recorrência":
  - "Única".
  - "Fixa": de diária a anual; os lançamentos futuros ficam pendentes.
  - "Parcelada": de 2 a 120 parcelas; o valor digitado é o total.
  - Ao editar ou excluir uma série, o site pergunta o alcance: só esta, "Esta e as próximas não pagas" ou a série inteira.
- Compra no cartão entra na fatura certa ("Será incluído na fatura que vence ...").
- Lista:
  - Busca por descrição, categoria ou valor.
  - Filtros "Todas", "Pagas", "Pendentes", "Transferências" e por categoria, com ordenação.
  - Resumo com a soma do que está filtrado.
- Ações em lote: "Selecionar", "Recategorizar", "Trocar conta", "Excluir" e marcar como pagas ou pendentes.
- Excluir tem "Desfazer". No celular, arrastar a linha mostra "Editar" e "Excluir".
- Categorias:
  - O cadastro começa com 21 categorias de despesa e 4 de receita.
  - Em "Categorias" dá para criar, renomear, trocar cor e ícone ("Aparência"), criar subcategorias, mover, reordenar e excluir. Para excluir uma categoria com lançamentos, é preciso mover os lançamentos antes.
  - Categorias podem ser exportadas e importadas em planilha.

## Pendentes

- Contas a pagar e a receber: o que não foi pago no período e tudo o que já venceu, de qualquer mês, mais as faturas de cartão não pagas.
- Indicadores "Vencidas", "A pagar", "A receber" e "Total pendente".
- Blocos "Vencidas" e "A vencer", com datas como "Hoje", "Amanhã" e "Em N dias".
- Um toque em "pendente" marca como pago ou recebido. Sem pendências, a tela mostra "Tudo em dia".

## Contas e cartões

- "Contas e carteiras": "Patrimônio consolidado" e o botão "Nova conta".
  - Tipos: "Banco / Digital", "Dinheiro / Carteira", "Cartão de crédito", "Investimento" e "Outro".
  - Campos: nome, tipo, "Saldo atual" (pode ser negativo, para cheque especial), "Incluir no patrimônio total", cor e ícone.
  - No guia de boas-vindas, o botão se chama "Adicionar banco ou carteira".
- "Cartões de crédito":
  - Limite, "Fecha no dia", "Vence no dia" e "Paga com" (a conta de onde sai o pagamento).
  - Em cada cartão: "Próximas faturas", "Limite usado", "Disponível" e "Pagar fatura".
  - No menu lateral, "Considerar faturas abertas" (quando há fatura aberta).
- Transferência entre contas é um tipo de transação, com "De" e "Para".

## Importar

- Botão "Importar": planilha (.xlsx, .xls ou .csv) ou extrato do banco (.ofx). O formato é detectado sozinho.
- Planilha:
  - 6 colunas, em qualquer ordem: data, categoria, descrição, conta ou carteira, valor e pago.
  - Valor positivo é receita; negativo é despesa.
  - Categorias e contas novas são criadas na importação.
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
- Sem limites definidos, o site sugere começar pela média dos últimos 12 meses ("Usar estes limites").
- Cabeçalho: gasto total, porcentagem do limite, sobra ou excesso e quanto dá para gastar por dia nos dias que faltam.
- Faixas: "Já passaram do limite", "Vão estourar no ritmo atual", "No limite", "Tranquilas" e "Sem limite definido".
  - A cor segue a projeção para o fim do mês: amarelo a partir de 90%, vermelho acima de 102% ou quando o limite já foi ultrapassado.
  - Em cada categoria: "Excedeu em R$ ..." e "no ritmo, fecha em R$ ...".
- Sugestões em "Onde definir limite primeiro".

## Fluxo

- Card do período: "Entrou", "Saiu" e "Guardou X% do que entrou" (ou "Faltou").
- Gráfico "Fluxo detalhado": "Receitas" e "Despesas" em barras, "Resultado" em linha e "Saldo acumulado" em área. Por padrão, os últimos 12 meses, com período próprio.
- "Top entradas" e "Top saídas": as 5 maiores categorias.
- Tabela "Resumo mensal": "Entradas", "Saídas", "Resultado" e "Saldo" mês a mês, com o "Total do período".
- Só entram lançamentos pagos ou recebidos. O Fluxo não projeta o futuro; a projeção fica na "Simulação futura".

## Relatórios

Uma página com painéis, com atalhos no topo:
- "Diagnóstico":
  - Taxa de poupança comparada com o próprio padrão da pessoa, e o maior desvio do período.
  - "Receita guardada", "Despesas do período" e "Reserva" (quantos meses o patrimônio cobre os gastos).
  - Metas ajustáveis em "Como o diagnóstico é calculado": taxa de poupança (padrão de 20%) e reserva de emergência (padrão de 6 meses), com janela de 3 a 24 meses.
- "O que mudou": as categorias que mais fugiram da média.
- "Concentração": quantas categorias respondem pela maior parte do gasto.
- Comparativo mensal de receitas e despesas.
- "Cascata do período": da receita ao saldo.
- "Receitas por categoria" e "Despesas por categoria": rosca com subcategorias. Clicar leva às transações.
- "Mapa de calor": gasto por categoria, mês a mês.
- "Maiores variações", contra o período anterior.
- "Recorrentes vs pontuais".
- "Sazonalidade": média de despesas por mês do ano.
- "Saldo acumulado".

## Comparar

- "Comparar períodos":
  - "Janela em foco": "Este mês", "3 meses", "6 meses", "No ano", "12 meses" ou meses escolhidos.
  - "Comparar com": "Período anterior", o mesmo período do ano anterior ou datas escolhidas.
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

- "Simulação de fluxo futuro": cenários do saldo nos próximos meses. Horizontes "6 meses", "1 ano", "2 anos" e "5 anos", ou um mês escolhido.
- Cada cenário tem:
  - Nome e "Saldo de partida" (o saldo atual de todas as contas ou um valor manual).
  - Receitas e despesas estimadas por mês, por categoria.
  - Ajustes: a partir de um mês, todo ano num mês, ou só num mês.
  - "Preencher com média", que usa a média de 3 a 24 meses.
- Resultado:
  - Saldo no fim e quanto sobra por mês.
  - Gráfico a partir de "Hoje".
  - Meta opcional ("Definir uma meta"), com o mês em que é atingida.
  - Linha do tempo.
- "E se...": "Testa um susto sobre o cenário, sem alterar nada."
  - Testes: "Receita −10%", "Despesa +10%", "Perde a maior renda", "Inflação 5% a.a." ou outro valor.
- "Plano contra realidade": compara o plano com a média real dos últimos 6 meses ("Ajustar o plano pelo real").
- Cenário base (selo "base"): cada cartão mostra a diferença para a base.
- "Comparar": até 5 cenários de uma vez, com o saldo projetado mês a mês.
- A simulação não calcula juros nem rendimento sobre o saldo.

## Remessas ao exterior

- Lançar:
  - "Nova remessa" (daqui para fora) ou "Resgate" (de volta para cá).
  - Campos: valor enviado na moeda, data, instituição, moeda, país do investimento, contas de origem e destino, total debitado em R$ e IOF (está no comprovante).
  - A tela calcula o câmbio efetivo, com e sem IOF, e avisa se o IOF ou o câmbio parecerem errados.
  - Também dá para importar uma planilha de remessas.
- 18 moedas e 41 destinos (países e a zona do euro).
- "Atualizar carteira": a pessoa informa quanto tem lá fora (valor total ou por banco), e o câmbio é sugerido.
- Cotação:
  - O site busca sozinho a PTAX de compra do Banco Central, com a data e a hora do boletim.
  - Se ela faltar, usa a taxa de referência do Banco Central Europeu ou a cotação comercial.
  - A cotação é só uma sugestão até a pessoa salvar.
- Cabeçalho: quanto está investido lá fora, o valor em reais ao câmbio de hoje e o resultado na moeda e em reais.
- "Ritmo do retorno": a TIR com as datas reais de cada remessa, no período, ao ano ou ao mês, na moeda e em reais.
- "Rendimento ano a ano": aportes, câmbio médio e posição no fim de cada ano, em dólar e em reais. Cada aporte pesa pelo tempo que ficou investido.
- "Quanto havia no fim de cada ano": saldo de 31/12 e câmbio de cada ano, com a PTAX do fechamento.
- "De onde veio o resultado em reais": você enviou, rendimento, efeito do câmbio e hoje.
- "Câmbio: onde você está": mostra o câmbio de equilíbrio, que zera o resultado em reais (abaixo dele, prejuízo), o câmbio médio da pessoa e o câmbio que empata com o CDI.
- "Contra o CDI": bruto ou líquido de IR, simulando resgatar tudo hoje.
- "A jornada": marcos como a primeira remessa e o maior envio.
- Indicadores "Remetido", "Custo total", "Câmbio médio efetivo" e "IOF pago".
- Tabela "Remessas", por remessa ou por ano, com "Investido há".
- Não tem campo de tarifa ou spread, e não soma várias moedas num total único.

## Exportar, backup e preferências

- "Exportar" ("Exportar transações"): período e contas à escolha, em "Excel" (.xlsx), "PDF" (relatório pronto, que abre para imprimir ou salvar em PDF) ou "CSV".
- "Preferências":
  - Tema "Claro", "Escuro" ou "Auto".
  - Nome, e-mail e CPF.
  - "Exportar backup completo" e "Restaurar de backup".
  - Apagar as transações ou resetar a conta.
- O site salva sozinho ("Salvando...", "Salvo").

## Privacidade

- Não se conecta ao banco (sem Open Finance): a pessoa decide o que entra.
- Sem propaganda.
- A página do site diz "Dados criptografados: no envio e no armazenamento". Pode repetir assim, nunca "de ponta a ponta".
- "Ocultar valores" esconde os números da tela.
- Exporta tudo quando a pessoa quiser: Excel, PDF, CSV e backup completo.

## Frases da página do site que os posts podem ecoar

- "Seu dinheiro deixa pistas todos os dias."
- "Não só o quanto. O porquê." (Comparar)
- "Categorize uma vez, o timtimcash aprende." (regras de importação)
- "Quanto rende o seu dinheiro lá fora." (Remessas)
- "Todo dinheiro, um só lugar." (contas)
- "Quanto entrou, quanto saiu, quanto sobrou." (Resultado)

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
- Exportar DRE, cenários ou remessas.
- Juros sobre o saldo na simulação.
- Tarifa ou spread nas remessas.
