# -*- coding: utf-8 -*-
"""Trilha original do vídeo 1 (o timtimcash), feita inteira em código para este vídeo (instrumentos em som.py).
120 batidas por minuto, Dó maior, no tempo das cenas (tempos.py):
- gancho, em Lá menor: os tiques do número somando, o baque quando ele assenta e duas notas que sobem como pergunta;
- a marca: Fá e Sol, com a marimba subindo até a entrada do aparelho;
- as cinco telas: Dó, Sol, Lá menor e Fá, com marimba, baixo, bumbo, palmas e chocalho; um clique em cada tecla digitada,
  duas notas quando o lançamento é salvo e um sopro em cada troca de tela;
- o Premium: a bateria abre espaço, piano elétrico e um sino para cada tela;
- fechamento: o acorde resolve em Dó e duas taças brindam ("tim-tim").
python3 trilha1.py  ->  trabalho/trilha.wav (48 kHz, estéreo, -14 LUFS)"""
import os, sys
import numpy as np
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI); sys.path.insert(0, os.path.dirname(AQUI))
import som as S
import tempos as T
m = S.Mesa(T.DUR, 20261121); rng = m.rng; B = T.B; mi = S.midi

# ---------------------------------------------------------------- gancho (0 a 2 s)
m.toca(S.pad(rng, [45, 52, 55, 59, 60], 1.9, ataque=.05, solta=.3, corte=1300), 0, g=.5, sala=.4, via="base")
m.toca(S.sub(mi(33), 1.6), 0, g=.26, via="base")
esc = [69, 72, 74, 76, 79, 81, 84, 86, 88, 91, 93, 96, 98, 100]
for i, n in enumerate(esc):                                    # os tiques do número: juntos no começo, espaçados no fim
    s = -.02 + 1.0 * (1 - (1 - (i + 1) / len(esc)) ** (1 / 3)) * .98
    m.toca(S.marimba(mi(n), .25, .06), s, pan=-.5 + i / 13, g=.11 + .006 * i, sala=.5)
m.toca(S.baque(62), 1.0, g=.45); m.toca(S.marimba(mi(57), .9, .3), 1.0, g=.3, sala=.6)
for s, n in [(1.08, 76), (1.3, 81)]:                           # "Para onde foi?": duas notas que sobem
    m.toca(S.marimba(mi(n), 1.0, .32), s, g=.34, sala=.8, eco=.6)
m.toca(S.sopro(rng, .55, 300, 6500, crescendo=True), 1.45, g=.3, sala=.3)

# ---------------------------------------------------------------- a marca (2 a 4 s): Fá e Sol
for a, notas, bx, corrida in [(2.0, [53, 57, 60, 67], 41, [72, 77, 81, 84]), (3.0, [55, 59, 62, 69], 43, [74, 79, 83, 86])]:
    m.toca(S.pad(rng, notas, 1.0, ataque=.04, solta=.25), a, g=.55, sala=.3, via="base")
    m.toca(S.epiano(mi(notas[1] + 12), .9) + S.epiano(mi(notas[2] + 12), .9), a, g=.2, sala=.5)
    m.toca(S.baixo(mi(bx + 12), .6, .3), a, g=.38, via="base")
    m.toca(S.bumbo(rng), a, g=.45); m.abre(a)
    for i, n in enumerate(corrida):
        m.toca(S.marimba(mi(n), .6, .18), a + .25 * i, pan=-.3 + .2 * i, g=.26 + .02 * i, sala=.5, eco=.4)
for s in (3.5, 3.75, 3.875): m.toca(S.palmas(rng), s, g=.22, sala=.3)
m.toca(S.sopro(rng, .5, 500, 7000, crescendo=True), 3.5, g=.22)

# ---------------------------------------------------------------- as telas (4 a 17 s)
AC = {"C": ([48, 55, 60, 64, 67], 36, [72, 79, 76, 79, 84, 79, 76, 79]), "G": ([47, 55, 59, 62, 67], 43, [71, 79, 74, 79, 83, 79, 74, 79]),
      "Am": ([45, 52, 57, 60, 64], 45, [72, 76, 69, 76, 81, 76, 72, 76]), "F": ([45, 53, 57, 60, 65], 41, [72, 77, 69, 77, 81, 77, 72, 77])}
for a, b, nome in [(4, 6, "C"), (6, 8, "G"), (8, 10, "Am"), (10, 12, "F"), (12, 14, "C"), (14, 16, "G"), (16, 17, "F")]:
    notas, bx, arp = AC[nome]
    m.toca(S.pad(rng, notas, b - a, ataque=.2, solta=.3), a, g=.5, sala=.35, via="base")
    k = 0; s = a
    while s < b - 1e-6:                                         # marimba em colcheias, com acento de 3 em 3
        forte = (k % 8) in (0, 3, 6)
        m.toca(S.marimba(mi(arp[k % 8]), .5, .16), s, pan=-.35 if k % 2 == 0 else .35, g=.46 if forte else .28, sala=.45, eco=.5 if forte else .2)
        k += 1; s += B / 2
    for bt, oit in [(0, 0), (1.5, 0), (2, 0), (3.5, 12)]:      # baixo
        s = a + bt * B
        while s < b - 1e-6:
            m.toca(S.baixo(mi(bx + oit + (12 if bx < 40 else 0)), .32, .14), s, g=.36, via="base"); s += 4 * B
s = 4.0; k = 0
while s < T.PREMIUM - 1e-6:
    m.toca(S.bumbo(rng), s, g=.5); m.abre(s)
    if k % 2 == 1: m.toca(S.palmas(rng), s, pan=.05, g=.36, sala=.55)
    m.toca(S.chimbal(rng), s + B / 2, pan=.25 if k % 2 else -.25, g=.32)
    s += B; k += 1
s = T.VEJA
while s < T.PREMIUM - 1e-6:                                     # chocalho em semicolcheias, a partir da Visão geral
    for j in range(4): m.toca(S.chocalho(rng), s + j * B / 4, pan=.4, g=.1 if j % 2 == 0 else .16)
    s += B
for s in (7.75, 7.875, 16.5, 16.75, 16.875): m.toca(S.palmas(rng), s, g=.2, sala=.3)
for s in (T.VEJA, T.ANTECIPE, T.ACOMPANHE, T.PLANEJE):
    m.toca(S.sopro(rng, .32, 900, 6000), s - .2, pan=-.2, g=.12)
    m.toca(S.chimbal(rng, True), s, pan=.2, g=.2)
    m.toca(S.sino(mi(91), .8, .8, .25), s, pan=.2, g=.1, sala=1.0)
# o que acontece na tela
for i, s in enumerate(T.TECLAS_VALOR): m.toca(S.tecla(rng, 2000 + 120 * i), s, pan=-.1, g=.22)
for i, s in enumerate(T.TECLAS_DESC): m.toca(S.tecla(rng, 2300 + 60 * (i % 3)), s, pan=.1, g=.17)
m.toca(S.sino(mi(88), .6, .6, .15), T.SUGERIDA, g=.09, sala=1.0)
m.toca(S.estalo(), T.TOQUE, g=.3)
for s, n in [(T.LANCADA, 79), (T.LANCADA + .12, 84)]: m.toca(S.sino(mi(n), 1.0, 1.0, .35), s, g=.2, sala=.8, eco=.5)
for s in (9.0, 11.55): m.toca(S.sino(mi(96), .5, .6, .12), s, pan=.15, g=.06, sala=.8)

# ---------------------------------------------------------------- o Premium (17 a 20 s): Fá com sétima maior e Sol suspenso
m.toca(S.sopro(rng, .55, 400, 7000, crescendo=True), T.PREMIUM - .5, g=.24, sala=.3)
for a, dur, notas, bx in [(17.0, 1.5, [53, 57, 60, 64], 41), (18.5, 1.5, [55, 60, 62, 65], 43)]:
    m.toca(S.pad(rng, notas, dur, ataque=.1, solta=.3, corte=1500), a, g=.5, sala=.5, via="base")
    for n in notas[1:]: m.toca(S.epiano(mi(n + 12), dur, 1.2), a, g=.2, sala=.6)
    m.toca(S.sub(mi(bx), dur - .1), a, g=.3, via="base")
    m.toca(S.bumbo(rng, 44, .26), a, g=.5); m.abre(a, .5, .12, .35)
for s in (17.75, 19.25): m.toca(S.estalo_dedos(rng), s, pan=.1, g=.3, sala=.7)
for i, (s, n) in enumerate(zip(T.CHIPS, [76, 79, 81, 84, 88])):
    m.toca(S.sino(mi(n), 1.1, 1.0, .4), s, pan=-.4 + .2 * i, g=.17, sala=.9, eco=.5)
m.toca(S.sopro(rng, .6, 400, 8000, crescendo=True), T.FIM - .6, g=.26, sala=.3)

# ---------------------------------------------------------------- fechamento (20 a 24 s): Dó com a nona
m.toca(S.pad(rng, [48, 55, 60, 62, 64, 67], T.DUR - T.FIM - .4, ataque=.06, solta=.6), T.FIM, g=.5, sala=.5, via="base")
for n in [60, 64, 67, 74]: m.toca(S.epiano(mi(n), 3.2, 1.8), T.FIM, g=.2, sala=.6)
m.toca(S.sub(mi(36), 2.4) * np.linspace(1, .5, int((2.4 + .08) * S.SR)), T.FIM, g=.3, via="base")
m.toca(S.bumbo(rng, 44, .28), T.FIM, g=.5); m.abre(T.FIM, .5, .14, .4)
for i, n in enumerate([72, 76, 79, 86, 84, 88]):
    m.toca(S.marimba(mi(n), 1.2, .4), T.FIM + .75 + .25 * i, pan=-.3 if i % 2 else .3, g=.2, sala=.8, eco=.4)
S.tim_tim(m, T.TIM_TIM, mi(88), mi(91))

os.makedirs(os.path.join(AQUI, "trabalho"), exist_ok=True)
arq = os.path.join(AQUI, "trabalho", "trilha.wav")
m.fecha(arq)
for a, b, nome in [(.2, 1.9, "Lá menor"), (2.05, 2.95, "Fá"), (4.1, 5.9, "Dó"), (6.1, 7.9, "Sol"), (8.1, 9.9, "Lá menor"), (10.1, 11.9, "Fá"), (17.1, 18.4, "Fá 7M"), (20.2, 22.5, "Dó")]:
    print(f"{a:5.1f}-{b:4.1f} s · {nome:9s}:", S.notas_fortes(arq, a, b))
