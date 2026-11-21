# -*- coding: utf-8 -*-
"""Tempos (s) do vídeo 2 (Premium), usados pelo vídeo (video2.py) e pela trilha (trilha2.py).
88 batidas por minuto: um compasso (4 batidas) a cada 2,727 s. Cada pergunta ocupa um compasso."""
BPM = 88
B = 60 / BPM
BAR = 4 * B
Q = [BAR * k for k in range(1, 6)]     # as cinco perguntas: Relatórios, Comparar, Resultado (DRE), Simulação futura, Remessas
ANEL = B               # o anel de cada tela entra na 2ª batida do compasso
RESP = 1.5 * B         # a resposta salta no contratempo, com o bumbo e as duas notas da resposta
GRAFICO = 2 * B        # na pergunta 4, a lista dá lugar ao gráfico dos dois cenários
PRECO = BAR * 6
FIM = BAR * 7
TIM_TIM = [FIM + .45, FIM + .58]
DUR = 22.6
