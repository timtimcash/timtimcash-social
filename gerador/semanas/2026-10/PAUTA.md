# Outubro de 2026 no @timtimcashcom: pauta e regras de produção

Pasta de trabalho: `/tmp/claude-0/-home-claude-timtimcash-social/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/outubro` (abaixo, `$O`).
Repositório (só leitura para vocês): `/home/claude/timtimcash-social`. NUNCA faça git (add, commit, push), NUNCA mexa no Metricool e NUNCA altere arquivos do repositório. Tudo o que você produzir fica em `$O`.

## Leia antes de começar
1. `/home/claude/timtimcash-social/gerador/MARCA.md` (manual da marca, com a regra das capas).
2. `/home/claude/timtimcash-social/gerador/FUNCIONALIDADES.md` (o que o site faz; cite só o que está lá, com os nomes exatos das telas e botões).
3. `/home/claude/timtimcash-social/gerador/telas/LEIAME.md` (telas reais e a conta fictícia; os números dos posts precisam bater com ela).
4. `/home/claude/timtimcash-social/gerador/artes.py` e o modelo aprovado `/home/claude/timtimcash-social/gerador/semanas/2026-10-05_v2.py` (capas `capa_*`, `recorte`, `NOTA_TELA`) com os textos em `2026-10-05_v2_dados.py`.
5. Para Reels: o Reel aprovado e publicado hoje, `$O/base_app/modelo_reel/reel.py` (gera o vídeo quadro a quadro no Chromium e manda para o ffmpeg), e `$O/base_app/captura_reel.py` (captura estados reais do site com o relógio da página controlado).

## Regras de texto (valem para artes, legendas, roteiros e textos alternativos)
- Português do Brasil. NUNCA use travessão (U+2014) nem meia-risca (U+2013). Para número negativo use o sinal de menos (−, U+2212), como em −R$ 22.040.
- O timtimcash é um SITE, usado no navegador do computador ou do celular. Nunca "app", nunca "baixar", nunca loja.
- "Gratuito" só para o controle financeiro ("Gratuito para o controle financeiro"). Nunca ligado a remessas ou exterior; nunca "para sempre".
- Proibido: funcionalidade inventada, depoimento fictício, promessa de resultado ou de economia, número apresentado como dado real de usuário, concorrente pelo nome, superlativo ("o melhor", "o mais completo"), emojis, inteligência artificial.
- Sem recomendação de investimento específico. Dado econômico ou regra legal só com fonte oficial, com data, e a fonte vai no campo `fontes`.
- Todo slide ou cena com tela real leva a nota "Tela real do timtimcash, com dados de exemplo".
- Nome sempre timtimcash, em minúsculas. Ponto médio (·) separa ideias. Valores no formato brasileiro (R$ 1.014,25; Abr/26).
- Legenda: primeira frase forte (o Instagram corta depois da primeira linha), 2 a 4 parágrafos curtos, fechamento levando ao site ("Acesse pelo navegador, no computador ou no celular: timtimcash.com" ou "Link na bio"), no máximo 5 hashtags no fim, sempre com #timtimcash. Quando o post mostra tela real, uma linha "Tela real do timtimcash, com dados de exemplo."

## Regras visuais
- Siga `MARCA.md`. Inter com cv11 e ss01, títulos em 700, hierarquia sem transparência, logotipos só pelos arquivos oficiais (`artes.logo_horizontal`, `artes.logo_vertical`, `artes.logo`).
- Capa: só sobretítulo, título curto e um visual forte (número grande, recorte de tela real, gráfico, ícones grandes). Sem parágrafo de apoio. O fundo de cada capa está na tabela abaixo e não pode mudar (a grade do perfil alterna os fundos). Fundos: papel = "light" (#FBFAF6), tinta = "dark" (#0F1410, logotipo "dark", sobretítulo em menta #6EE7B7), verde suave = "soft" (#D1FAE5), verde = "green" (#059669, logotipo "white").
- Carrossel: 1080 × 1350, 5 a 7 slides, miolo em papel, último slide em verde com o chamado (como no modelo). Renderize com `TT_SAIDA=$O/saida python3 /home/claude/timtimcash-social/gerador/render.py <seu_arquivo.py>`; o arquivo define `POSTS = {"<pasta>": funcao}` e começa com `from artes import *`. As telas do repositório ficam em `/home/claude/timtimcash-social/gerador/telas/` (use caminho absoluto).
- Reel: 1080 × 1920, 30 quadros por segundo, 18 a 25 segundos, H.264 com trilha AAC silenciosa (use exatamente os parâmetros do ffmpeg do `reel.py` modelo). A primeira cena é a capa em movimento, legível já no quadro 0, com o mesmo fundo da tabela. Depois, cenas de tela real com um título curto em cima e a tela numa janela, com panorâmica, anéis de destaque, toque e troca de estado, como no modelo. Uma cena de conclusão e o fechamento em verde com `logo_vertical("white")`, o nome da funcionalidade, "Acesse pelo navegador, no computador ou no celular." e a pílula "Link na bio". Texto importante entre x 90 e 990 e entre y 200 e 1560 (o Instagram cobre a base e a direita da tela).
  - Entregue em `$O/saida/<pasta>/`: `reel.mp4`, `capa.jpg` (1080 × 1920, a capa que aparece na grade: título e visual dentro da faixa central de y 240 a 1680, porque a grade recorta em 3:4) e `previa.mp4` (`ffmpeg -i reel.mp4 -vf scale=720:1280 -c:v libx264 -crf 28 -preset veryfast -an -movflags +faststart previa.mp4`).
  - Confira com `ffprobe` (h264, 1080x1920, 30 fps, aac) e extraia quadros com o ffmpeg para ver com Read: início, cada cena e fim.
- Confira CADA imagem e os quadros do vídeo com Read: nada estourado, cortado ou sobreposto, texto legível no tamanho do celular, nenhum travessão.

## Telas reais novas (captura)
- Copie o kit para a sua pasta: `cp -r $O/base_app $O/<seu_nome>/app` e trabalhe só na sua cópia (outras pessoas usam o kit ao mesmo tempo).
- O kit abre o `site/index.html` como se fosse https://timtimcash.com, com um cliente falso do Supabase e a conta fictícia de `estado.py` (gera `estado.js`). Veja `captura.py` (`abrir`), `secoes.py` (recorta cartões por título) e `captura_reel.py` (relógio da página controlado; `page.clock.pause_at` recebe datetime, não número). Navegação: `setTab('dashboard'|'transacoes'|'pendentes'|'fluxo'|'relatorios'|'comparar'|'dre'|'orcamentos'|'simulacao'|'remessas')`, cenário `_simAbrir('sim_base')`, extrato `_imp_handleOFX(texto)` com `extrato.ofx` e depois "Conta corrente" no modal "Conta de destino". Para achar outras funções, procure no `site/index.html` (arquivo grande: use Grep com contexto pequeno).
- Celular: viewport 390 de largura, escala 3, `is_mobile=True`. Computador: 1440 × 900, escala 2.
- Se precisar de outro dado na conta fictícia, mude só a SUA cópia do `estado.py`, sem alterar os números que já existem (setembro de 2026, contas, remessas, simulações), e registre a mudança no seu relatório. O index.html nunca vai para lugar nenhum além da sua pasta.
- Guarde as telas usadas em `$O/saida/<pasta>/telas/` (PNG ou JPEG), para irem ao repositório depois da aprovação.

## Arquivo de dados de cada post
Crie `$O/dados/<pasta>.py` com `POST = {...}` e estes campos:
`pasta`, `tipo` ("reel" ou "carrossel"), `plataforma` ("Instagram"), `formato` (ex.: "Reel de 22 segundos (1080 × 1920, 9:16)" ou "Carrossel de 6 imagens no feed (1080 × 1350, 4:5)"), `formato_curto` ("Reel de 22 s" / "Carrossel de 6 imagens"), `tema`, `pilar`, `data_longa` ("terça-feira, 6 de outubro de 2026"), `data_curta` ("terça-feira, 06/10/2026"), `data_mockup` ("6 de outubro"), `hora` ("10h00"), `iso` ("2026-10-06T10:00:00"), `slides` (carrossel: o texto de cada slide, no estilo do modelo; Reel: uma linha por cena, com o tempo, ex.: "0 a 3 s · Capa (tinta) · ..."), `legenda`, `justificativa` (lista de 4 pares: "Por que agora", "O que desperta interesse", "Benefício para o público", "Como contribui para o perfil"), `alt` (carrossel: um texto por slide; Reel: um texto descrevendo o vídeo), `fontes` (lista de (título, URL); vazia se não houver) e `telas` (lista das telas reais usadas).

## Calendário de outubro (20 posts; os 7 marcados "já agendado" existem e não são produzidos por vocês)
| Data | Formato | Fundo da capa | Pasta | Tema |
|---|---|---|---|---|
| 02/10 sex | Carrossel | (verde, antigo) | 2026-10-02_rendeu-em-dolar-e-em-reais | já agendado |
| 03/10 sáb | Carrossel | (verde, antigo) | 2026-10-03_outubro-comecou | já agendado |
| 05/10 seg | Carrossel | papel | 2026-10-05_quanto-fica-com-voce | já agendado (taxa de poupança) |
| 06/10 ter | Reel | verde | 2026-10-06_reel-o-timtimcash-em-20-segundos | NOVO |
| 07/10 qua | Carrossel | tinta | 2026-10-07_cambio-de-equilibrio | já agendado |
| 08/10 qui | Reel | papel | 2026-10-08_reel-extrato-com-categoria-sugerida | NOVO |
| 09/10 sex | Carrossel | verde suave | 2026-10-09_seus-dados-entram-e-saem-com-voce | já agendado |
| 13/10 ter | Carrossel | papel | 2026-10-06_orcamento-pela-sua-media | já agendado, muda de 06/10 |
| 14/10 qua | Reel | tinta | 2026-10-14_reel-rendimento-ano-a-ano | NOVO |
| 15/10 qui | Carrossel | verde suave | 2026-10-15_reserva-em-meses | NOVO |
| 16/10 sex | Reel | verde | 2026-10-16_reel-quanto-vai-para-o-mercado | NOVO |
| 19/10 seg | Carrossel | papel | 2026-10-19_cartao-fechamento-e-vencimento | NOVO |
| 20/10 ter | Reel | tinta | 2026-10-20_reel-o-que-vence-esta-semana | NOVO |
| 21/10 qua | Carrossel | papel | 2026-10-08_e-se-a-maior-renda-parar | já agendado, muda de 08/10 |
| 22/10 qui | Reel | verde suave | 2026-10-22_reel-ritmo-do-retorno | NOVO |
| 23/10 sex | Carrossel | verde | 2026-10-23_sua-planilha-vem-junto | NOVO |
| 26/10 seg | Carrossel | papel | 2026-10-26_parcela-que-cabe-hoje | NOVO |
| 27/10 ter | Reel | tinta | 2026-10-27_reel-ocultar-valores | NOVO |
| 29/10 qui | Carrossel | verde suave | 2026-10-29_cambio-efetivo | NOVO |
| 30/10 sex | Reel | verde | 2026-10-30_reel-13-salario | NOVO |

Já publicados e que não podem se repetir: fechamento do mês em 5 perguntas (30/09); post fixado "Comece por aqui" (30/09); Reel "E se o seu salário parasse por 6 meses?" (30/09, simulação com "Perde a maior renda"). Os temas dos 7 posts já agendados também não se repetem.

## Briefings dos 13 posts novos

### 06/10 · Reel · "O timtimcash em 20 segundos" (produto, capa verde)
Para quem chega pelo Reels e não conhece o site. Gancho: "O timtimcash em 20 segundos". Cortes rápidos por telas reais do celular, cada uma com uma frase curta: Visão geral ("Quanto entrou, quanto saiu, quanto sobrou"), Orçamentos ("O que estourou e o que ainda cabe"), Relatórios ou Fluxo ("Para onde o dinheiro foi"), Simulação futura ("Como fecham os próximos meses"), Remessas ao exterior ("Quanto rendeu lá fora, em reais"). Movimento: a tela entra e rola um pouco em cada cena. Telas: `gerador/telas/biblioteca/celular-*.jpg` e `gerador/telas/secoes/`. Fechamento: "Seu dinheiro, com a clareza que ele merece." e Link na bio.

### 08/10 · Reel · "Extrato do banco, categoria sugerida" (produto, capa papel)
Gancho: "Seu extrato do banco, já com as categorias." Fluxo real no celular: "Importar" > extrato .ofx > "Conta de destino" > "Revisar importação" com as 3 linhas e o selo "sugerida" (Supermercado da Vila em Mercado, Posto Avenida em Transporte, Farmácia São José em Saúde) > trocar a categoria de uma linha e aparecer "Automatizar esta categoria?" com "Aplicar e lembrar" > "Importar 3 linhas". Mensagem final: "Categorize uma vez, o timtimcash aprende." (frase do próprio site) e "Transações já importadas são detectadas e desmarcadas." Sem senha do banco: o extrato é um arquivo que você baixa do banco.

### 14/10 · Reel · "Rendeu em dólar todos os anos. E em reais?" (investimento no exterior, capa tinta)
Tela `gerador/telas/secoes/celular-remessas-rendimento-ano-a-ano.jpg` (e a de computador). Conta: 2023 +6,5% em US$ e +3,8% em R$; 2024 +3,6% e +34,4%; 2025 +3,9% e −7,7%; 2026 até hoje +2,5% e +2,4%. Revele ano a ano com anéis. Cena de conclusão: "O investimento é o mesmo. O câmbio muda o ano." Explique em uma frase que o timtimcash usa o saldo de 31/12 e a PTAX de compra do último dia útil de cada ano. Fontes da PTAX: as de `telas/LEIAME.md`. Não repetir o enfoque do post de 02/10 (rendimento separado do câmbio num exemplo de um ano) nem do de 07/10 (câmbio de equilíbrio).

### 15/10 · Carrossel · "Reserva de emergência: quantos meses você aguentaria?" (educação, capa verde suave)
Educação com o Diagnóstico de Relatórios. A reserva medida em meses de gasto, não em reais. A conta: dinheiro disponível dividido pelo gasto mensal (confira no código como o timtimcash calcula a "Reserva" do Diagnóstico e escreva exatamente isso). Na conta fictícia o Diagnóstico mostra 12,5 meses, com meta de 6 meses (padrão do site, ajustável). Ponto de economista: nem todo patrimônio é reserva; dinheiro investido lá fora ou num imóvel pode demorar para virar dinheiro. Termine ligando ao teste "Perde a maior renda" da Simulação futura (sem repetir o Reel de 30/09). Telas: `gerador/telas/secoes/celular-relatorios-diagnostico.jpg`.

### 16/10 · Reel · "Dia Mundial da Alimentação: quanto do seu mês vai para o mercado?" (educação com produto, capa verde)
16 de outubro é o Dia Mundial da Alimentação (FAO; fonte: https://www.fao.org/newsroom/detail/pope-leo-xiv-and-world-leaders-mark-world-food-day-and-fao-at-80-in-rome/en). Na conta fictícia, Mercado foi R$ 1.710,00 em setembro, 22% das despesas de R$ 7.780,00, e o orçamento de Mercado é R$ 2.000 (86%). Telas reais: o bloco "Por categoria" da Visão geral (capture) e a linha de Mercado em Orçamentos. Dica final prática, sem promessa: olhar o mercado em porcentagem do mês e acompanhar pelo orçamento.

### 19/10 · Carrossel · "Cartão de crédito: fechamento, vencimento e o melhor dia de compra" (educação, capa papel)
Educação pura, com ilustração de calendário (não é tela do produto). Exemplo: cartão que fecha no dia 3 e vence no dia 10. Compra no dia 4 (logo depois do fechamento) entra na fatura seguinte e só é paga no dia 10 do mês seguinte. Compra no dia 2 entra na fatura que vence no dia 10 deste mês. Diga que a regra do dia do fechamento varia entre emissores e que o dia certo está na fatura. Último slide antes do verde: no timtimcash, cada cartão tem "Fecha no dia" e "Vence no dia", e a compra no cartão já mostra "Será incluído na fatura que vence ..." (funcionalidades confirmadas). Sem juros do rotativo, sem números de mercado.

### 20/10 · Reel · "O que vence esta semana?" (produto, capa tinta)
Tela Pendentes no celular: "Vencidas", "A pagar", "A receber", "Total pendente"; conta de luz de R$ 186,40 e reembolso do plano de saúde de +R$ 320,00 (dados da conta fictícia; se precisar, ajuste o relógio da página para uma data que deixe a cena clara e registre a data). Um toque em "pendente" marca como pago; mostre o antes e o depois. Pode mostrar o aviso de pendências da Visão geral com "Ver pendentes". Conclusão: "O mês só fecha quando nada fica para trás."

### 22/10 · Reel · "Rendeu 11,8%. Em quanto tempo?" (investimento no exterior, capa verde suave)
Tela real "Ritmo do retorno" (TIR com as datas reais de cada remessa) com os três modos "no período", "ao ano" e "ao mês": capture cada um tocando no seletor. Na conta fictícia, no período dá 11,8% na moeda e 25,1% em reais (12/07/2023 a 30/09/2026, 3,2 anos); confira e use os valores "ao ano" e "ao mês" que a tela mostrar. Mensagem: rendimento no período não é rendimento ao ano; a TIR considera quando cada remessa entrou. Sem recomendação de investimento.

### 23/10 · Carrossel · "Sua planilha vem junto" (posicionamento e produto, capa verde)
Para quem controla tudo em planilha há anos. Telas reais do modal "Importar transações", aba "Planilha · .xlsx / .csv", "Formato esperado da planilha · 6 colunas" (data, categoria, descrição, conta/carteira, valor, pago), "Baixar modelo em Excel", e a revisão antes de importar. Pontos: colunas em qualquer ordem; valor positivo é receita e negativo é despesa; categorias e contas novas são criadas na importação; você revisa antes de confirmar. Sem dizer que substitui a planilha: ela vem junto e continua sua.

### 26/10 · Carrossel · "A parcela cabe hoje. E daqui a três meses?" (educação com produto, capa papel)
Educação sobre compras parceladas: cada parcela é pequena, mas as parcelas somam e ocupam os meses seguintes. Exemplo coerente com os posts: parcela de R$ 249,90 (compra de R$ 2.499 em 10 vezes, como no post de 30/09). Mostre como três compras parceladas somam por mês até terminarem (exemplo simples, marcado como exemplo). No timtimcash: "Recorrência" "Parcelada", com "Nº parcelas" (de 2 a 120) e o valor total dividido em "N× de R$ X"; cada parcela entra como pendente no mês certo, e a Simulação futura mostra o mês que aperta. Capture a tela real de "Nova transação" com "Parcelada" preenchida.

### 27/10 · Reel · "Vai abrir suas finanças em público?" (privacidade, capa tinta)
Curto (15 a 18 s), que funciona em repetição. Telas `gerador/telas/movel.png` e `gerador/telas/movel-ocultar.png` (Visão geral no celular com e sem os valores; o olho fica em x 311, y 38 em px CSS). Gancho: "Vai abrir suas finanças na fila, no ônibus, no trabalho?" Toque no olho: "Um toque e os valores somem." Toque de novo: voltam. Frase final: "Os gráficos também escondem." (confirmado na ficha: "Ocultar valores" esconde também os valores dos gráficos). Não repetir o carrossel de 09/10, que fala de entrada e saída de dados.

### 29/10 · Carrossel · "Câmbio efetivo: o câmbio que você pagou de verdade" (investimento no exterior, capa verde suave)
Educação: o câmbio da operação não é o custo final; câmbio efetivo = total debitado em reais dividido pelo valor enviado na moeda, com IOF e tarifa dentro. Exemplo (marcado como exemplo): enviou US$ 4.000 com câmbio de R$ 5,10; IOF de R$ 224,40 (o que está no comprovante); total debitado R$ 20.624,40; câmbio efetivo R$ 5,1561. Não afirme alíquota de IOF nem regra tributária: diga "o IOF que está no comprovante". No timtimcash, "Nova remessa" calcula na hora o valor sem IOF, o câmbio sem IOF, o "Câmbio efetivo (com IOF)" e a alíquota, e avisa se algo parecer errado. Capture a tela real do formulário preenchido com esse exemplo (sem salvar, ou salvando só na sua cópia).

### 30/10 · Reel · "O 13º vem aí: veja agora o que ele muda no seu saldo" (educação com produto, capa verde)
Regra legal (fonte: Lei 4.749/1965, https://www.planalto.gov.br/ccivil_03/leis/l4749.htm): a primeira parcela, metade do salário do mês anterior, é paga entre fevereiro e novembro; o 13º inteiro, até 20 de dezembro. Na conta fictícia, salário de R$ 9.960: primeira parcela de R$ 4.980, sem descontos (os descontos de INSS e IR ficam para a segunda parcela; não calcule a segunda). No cenário base da Simulação futura, janeiro de 2027 tem R$ 4.800 de IPVA e IPTU. Mostre, com tela real, o cenário antes e depois de incluir a primeira parcela do 13º em novembro de 2026 (ajuste de um mês na receita, pela interface ou numa cópia do cenário na sua cópia do `estado.py`; confira no código como o ajuste funciona). Mensagem: a primeira parcela, guardada, cobre o janeiro caro do exemplo.
