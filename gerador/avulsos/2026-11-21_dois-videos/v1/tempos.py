# -*- coding: utf-8 -*-
"""Tempos (s) do vídeo 1 (o timtimcash), usados pelo vídeo (video1.py) e pela trilha (trilha1.py).
120 batidas por minuto: uma batida a cada 0,5 s, um compasso (4 batidas) a cada 2 s. As cenas trocam nos compassos."""
BPM = 120
B = 60 / BPM
GANCHO_SAI = 2.0          # o gancho (tinta) sai; entra a marca
MARCA_SAI = 3.7
FONE = 3.75               # o aparelho entra
LANCE, VEJA, ANTECIPE, ACOMPANHE, PLANEJE = 4.0, 8.0, 11.0, 13.0, 15.0
TECLAS_VALOR = [4.7, 4.9, 5.1, 5.3]                    # R$ 24,50, tecla a tecla
TECLAS_DESC = [5.9 + .1 * i for i in range(7)]         # "Padaria", letra a letra
SUGERIDA = 6.8            # a categoria sugerida aparece
TOQUE = 7.3               # toque em "Lançar despesa"
LANCADA = 7.45            # "Transação adicionada"
PREMIUM = 17.0            # o painel do Premium sobe
CHIPS = [17.7 + .14 * i for i in range(5)]
FIM = 20.0                # fechamento verde
TIM_TIM = [20.45, 20.58]
DUR = 24.0
