# -*- coding: utf-8 -*-
"""Trilha original do vídeo 2 (Premium), feita inteira em código para este vídeo (instrumentos em som.py).
88 batidas por minuto, meio tempo, de Lá menor a Dó maior, um acorde por pergunta (tempos.py):
- gancho: um acorde que cresce, o baque do "5", os brilhos da coroa e cinco sinos para os cinco números;
- as perguntas: piano elétrico, baixo grave, bumbo na 1ª batida e no contratempo, estalo de dedos na 3ª e chimbal leve;
  quando a resposta salta, duas notas respondem; um sopro em cada troca de tela;
- o preço: Sol suspenso, que pede resolução;
- fechamento: o acorde resolve em Dó com a nona e duas taças brindam ("tim-tim").
python3 trilha2.py  ->  trabalho/trilha.wav (48 kHz, estéreo, -14 LUFS)"""
import os, sys
import numpy as np
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI); sys.path.insert(0, os.path.dirname(AQUI))
import som as S
import tempos as T
m = S.Mesa(T.DUR, 20261124); rng = m.rng; B, BAR = T.B, T.BAR; mi = S.midi

# ---------------------------------------------------------------- gancho (1º compasso): Lá menor com a nona
m.toca(S.pad(rng, [45, 52, 60, 64, 67, 71], BAR - .1, ataque=.9, solta=.3, corte=1500), 0, g=.6, sala=.5, via="base")
m.toca(S.baque(55), .1, g=.5); m.toca(S.sub(mi(45), 1.8), .1, g=.3, via="base")
for n in [57, 64, 71]: m.toca(S.epiano(mi(n), 2.2, 1.6), .1, g=.24, sala=.7)
for i, n in enumerate([88, 93, 95, 100]):                       # os brilhos da coroa
    m.toca(S.sino(mi(n), 1.2, 1.2, .45), .32 + .1 * i, pan=-.6 + .4 * i, g=.12, sala=1.2)
m.toca(S.epiano(mi(76), 1.0, .9) + S.epiano(mi(79), 1.0, .9), .8, g=.14, sala=.7)       # "O Premium responde."
for i, n in enumerate([81, 84, 86, 88, 91]):                    # os cinco números
    m.toca(S.sino(mi(n), .9, 1.0, .3), 1.25 + .12 * i, pan=-.4 + .2 * i, g=.16, sala=.9, eco=.4)
m.toca(S.sopro(rng, .7, 300, 7000, crescendo=True), T.Q[0] - .75, g=.3, sala=.3)

# ---------------------------------------------------------------- as perguntas e o preço (compassos 2 a 7)
# (baixo, acorde do piano elétrico, as duas notas da resposta)
AC = [(45, [60, 64, 67, 71], (76, 83)), (41, [57, 60, 64, 67], (72, 79)), (40, [55, 59, 62, 64], (74, 79)),
      (38, [53, 57, 60, 64], (69, 76)), (41, [57, 60, 64, 69], (76, 84)), (43, [53, 57, 60, 62], None)]
INI = T.Q + [T.PRECO]
for k, (a, (bx, notas, resp)) in enumerate(zip(INI, AC)):
    m.toca(S.pad(rng, [bx + 12] + notas, BAR - .05, ataque=.25, solta=.3, corte=1400), a, g=.36, sala=.5, via="base")
    for bt, dur, g in [(0, 1.4, .27), (1.5, .9, .21), (3, .7, .15)]:               # piano elétrico: acorde e duas respostas curtas
        for j, n in enumerate(notas): m.toca(S.epiano(mi(n), dur * B, 1.4), a + bt * B + .006 * j, g=g, sala=.55, eco=.25 if bt else 0)
    for bt, dur, oit in [(0, 1.3, 0), (1.5, 1.2, 0), (3, .8, 12 if k % 2 else 0)]:   # baixo grave
        m.toca(S.sub(mi(bx if bx >= 40 else bx + 0) * (2 ** (oit / 12)), dur * B), a + bt * B, g=.3, via="base")
    for bt in ([0, 1.5] + ([3.5] if k % 2 else [])):                               # bumbo
        m.toca(S.bumbo(rng, 44, .24), a + bt * B, g=.52); m.abre(a + bt * B, .5, .12, .32)
    m.toca(S.estalo_dedos(rng), a + 2 * B, pan=.08, g=.36, sala=.8)                 # estalo de dedos na 3ª batida
    for j in range(8):                                                              # chimbal em colcheias, leve
        m.toca(S.chimbal(rng), a + j * B / 2, pan=.3 if j % 2 else -.3, g=.26 if j % 2 else .14)
    if k % 2: 
        for s in (3.25, 3.75): m.toca(S.chimbal(rng), a + s * B, pan=.3, g=.13)
    m.toca(S.chimbal(rng, True), a + 3.5 * B, pan=.2, g=.14)
    m.toca(S.sopro(rng, .34, 800, 6000), a - .22, pan=-.2, g=.13)                   # a tela nova desliza
    m.toca(S.sino(mi(96), .5, .6, .12), a + T.ANEL, pan=.15, g=.07, sala=.9)        # o anel
    if resp:                                                                        # a resposta salta
        for j, n in enumerate(resp): m.toca(S.sino(mi(n), 1.3, 1.0, .45), a + T.RESP + .11 * j, pan=-.15 + .3 * j, g=.27, sala=.9, eco=.5)
m.toca(S.sino(mi(91), .6, .7, .18), T.Q[3] + T.GRAFICO, g=.09, sala=.9)             # a lista vira o gráfico
m.toca(S.sino(mi(98), .5, .6, .12), T.PRECO + 1.45, pan=.15, g=.07, sala=.9)        # o segundo anel do preço
for j in range(8): m.toca(S.chocalho(rng), T.PRECO + 2 * B + j * B / 4, pan=.35, g=.06 + .018 * j)   # o preço cresce para o fechamento
m.toca(S.sopro(rng, .7, 400, 8000, crescendo=True), T.FIM - .7, g=.28, sala=.3)

# ---------------------------------------------------------------- fechamento: Dó com a sétima maior e a nona
F = T.FIM
m.toca(S.pad(rng, [48, 52, 55, 59, 62, 67], T.DUR - F - .5, ataque=.06, solta=.6, corte=1600), F, g=.55, sala=.6, via="base")
for j, n in enumerate([52, 55, 59, 62, 67, 74]): m.toca(S.epiano(mi(n), 3.0, 2.0), F + .012 * j, g=.22, sala=.7)
m.toca(S.sub(mi(36), 2.2) * np.linspace(1, .45, int((2.2 + .08) * S.SR)), F, g=.32, via="base")
m.toca(S.bumbo(rng, 44, .28), F, g=.5); m.abre(F, .5, .14, .4)
for i, n in enumerate([79, 83, 86, 91, 95]):
    m.toca(S.sino(mi(n), 1.6, .7, .6), F + .95 + .17 * i, pan=-.4 + .2 * i, g=.11, sala=1.0, eco=.4)
S.tim_tim(m, T.TIM_TIM, mi(88), mi(91))

os.makedirs(os.path.join(AQUI, "trabalho"), exist_ok=True)
arq = os.path.join(AQUI, "trabalho", "trilha.wav")
m.fecha(arq, eco_s=1.5 * B / 2 * 1.0, sala_s=2.0, sala_g=.6, saida=1.2)
nomes = ["Lá menor 9", "Lá menor 9", "Fá 7M9", "Dó/Mi", "Ré menor 9", "Fá 7M", "Sol sus", "Dó 7M9"]
for k, nome in enumerate(nomes):
    a = k * BAR + .15; print(f"{a:5.1f}-{a + BAR - .4:4.1f} s · {nome:11s}:", S.notas_fortes(arq, a, a + BAR - .4, fmax=500, k=7))
