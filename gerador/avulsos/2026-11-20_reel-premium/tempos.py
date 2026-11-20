# -*- coding: utf-8 -*-
"""Tempos (s) do Reel do Premium, usados pelo vídeo (reel_premium.py) e pela trilha (trilha.py).
Andamento da trilha: 120 batidas por minuto (uma batida a cada 0,5 s; um compasso de 4 batidas a cada 2 s).
As trocas de cena caem nas batidas, para o corte e o som andarem juntos."""
BPM = 120
BATIDA = 60 / BPM

G_SAI = 2.95            # o gancho (painel verde do Premium) sai para cima; a cena das telas entra
JANELA_ENTRA = 3.0
SELO = 3.45             # anel no selo PREMIUM do menu
VARRE = (4.35, 5.0)     # o anel desce pelas cinco telas com a coroa
TROCAS = [5.5, 7.5, 9.5, 11.5, 13.5]   # Relatórios, Comparar, Resultado (DRE), Simulação futura, Remessas ao exterior
ANEL_ATRASO = 0.55      # o anel de cada tela entra meio segundo depois da troca
JANELA_SAI = 15.5
MAIS = [15.75, 16.0, 16.25]            # as três linhas de "E mais"
PRECO = 17.0            # a tela Planos com os preços
PRECO_ANEL = 17.55
FIM = 19.5              # fechamento verde
TIM_TIM = [19.95, 20.08]  # o brinde ("tim-tim") quando o fechamento assenta
DUR = 22.0
