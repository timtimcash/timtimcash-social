# Telas reais do timtimcash

Capturas do próprio site (build `2026-09-30.1`, capturado em 30/09/2026) numa **conta fictícia**. Nenhum dado real aparece. Use nos posts no lugar de maquetes sempre que uma delas servir, com a nota "Tela real do timtimcash, com dados de exemplo".

## Como usar num roteiro

```python
import os
TELAS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "telas")
def tela(nome): return "file://" + os.path.join(TELAS, nome)
# <img src="{tela('biblioteca/celular-remessas.jpg')}" style="width:100%">
```

Para recortar só um pedaço de uma tela, use uma caixa com `overflow:hidden` e a imagem posicionada dentro, ou recorte com o Pillow antes. As telas do computador têm 2880 × 1800 px (1440 × 900 em escala 2); as do celular, 1170 × 2223 px (390 × 741 em escala 3).

## Conta fictícia (a mesma dos posts)

- Setembro de 2026: receitas R$ 9.960,00 (salário), despesas R$ 7.780,00, sobra de R$ 2.180,00 (guardou 21,9%).
- Despesas de setembro: Casa R$ 2.300,00 (aluguel), Mercado R$ 1.710,00, Educação R$ 1.450,00 (escola), Transporte R$ 1.245,00, Bares e restaurantes R$ 672,00, Saúde R$ 283,20, Assinaturas e serviços R$ 119,80.
- Agosto de 2026: despesas de R$ 8.285,00. Salário de R$ 9.480,00 até fevereiro e R$ 9.960,00 a partir de março de 2026.
- Contas: Conta corrente R$ 14.180,00; Reserva; Corretora no exterior. Patrimônio de R$ 104.180.
- Pendente: conta de luz de R$ 186,40, vence 30/09. A receber: reembolso do plano de saúde, R$ 320,00, em 06/10.
- Orçamentos: Mercado R$ 2.000, Transporte R$ 1.950, Bares e restaurantes R$ 600 (estourou, 112%), Lazer R$ 400, Saúde R$ 500.
- Exterior: 3 remessas de US$ 4.000 (câmbio de R$ 4,90, R$ 5,00 e R$ 5,10) = R$ 60.000 por US$ 12.000; carteira de US$ 13.200 a R$ 5,50 = R$ 72.600; rendimento +R$ 6.600 e câmbio +R$ 6.000 (+10% em dólar, +21% em reais). Sem IOF e tarifas.
- Simulação: "Cenário base" parte de R$ 14.180 e chega a R$ 37,7 mil em set/27 (IPVA e IPTU de R$ 4.800 em janeiro); "Trocar de carro" soma parcela de R$ 1.600 a partir de novembro e chega a R$ 20,1 mil.

## Arquivos

Na raiz (usados no post fixado de 30/09/2026):

| Arquivo | O que mostra |
|---|---|
| `desktop.png` | Visão geral no computador |
| `movel.png` | Visão geral no celular |
| `movel-ocultar.png` | Visão geral no celular com "Ocultar valores" ligado |
| `remessas-resultado.png` | Remessas · "De onde veio o resultado em reais" (cascata) |
| `importacao-recorte.png` | Revisão da importação de um extrato .ofx, com 3 categorias sugeridas |

Em `biblioteca/`, cada seção no computador e no celular (`computador-*.jpg` e `celular-*.jpg`): `dashboard` (Visão geral), `transacoes`, `pendentes`, `fluxo`, `relatorios` (Diagnóstico), `comparar` (set/26 contra ago/26), `dre` (Resultado), `orcamentos`, `simulacao` (lista de cenários), `simulacao-cenario` (cenário base aberto, com gráfico e testes "E se...") e `remessas`.

## Atualizar

As telas mudam quando o site muda. Para capturar de novo, o Samuel envia o `index.html` mais recente; ele nunca entra neste repositório.
