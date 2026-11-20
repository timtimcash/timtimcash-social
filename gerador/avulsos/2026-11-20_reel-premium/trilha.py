# -*- coding: utf-8 -*-
"""Trilha original do Reel do Premium (20/11/2026), feita inteira em código para este vídeo.

Nenhuma música, amostra, gravação ou efeito de terceiros: cada som é sintetizado aqui, nota por nota, com numpy
(senoides, ondas dente de serra somadas harmônico a harmônico e ruído filtrado). A harmonia é uma sequência comum
(Ré, Lá, Si menor, Sol), que não pertence a ninguém; o arpejo, o baixo e a bateria são escritos abaixo.
120 batidas por minuto, em Ré maior, no tempo das cenas (tempos.py):
- gancho: acorde e arpejo desde o primeiro quadro, brilho quando a coroa aparece, estalo quando o preço salta;
- as telas: bateria entra no menu; um sopro em cada troca de tela; notas que sobem enquanto o anel desce pelas coroas;
- "E mais": três notas; o preço: acorde suspenso que pede resolução;
- fechamento: a bateria para, o acorde resolve em Ré e duas taças brindam ("tim-tim"), o som do nome.
Saída: trabalho/trilha.wav (48 kHz, estéreo, 32 bits) e trabalho/trilha_norm.wav (volume ajustado com o loudnorm do ffmpeg).
python3 trilha.py
"""
import os, sys, json, subprocess
import numpy as np
from scipy import signal
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import tempos as T

SR = 48000
N = int(T.DUR * SR)
rng = np.random.default_rng(20261120)
B = T.BATIDA


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def tt(n):
    return np.arange(n) / SR


def mix(buf, x, t0, pan=0.0, g=1.0):
    """Soma x (mono ou estéreo) em buf a partir de t0 s, com pan de -1 (esquerda) a 1 (direita)."""
    i0 = int(round(t0 * SR))
    if i0 >= N or i0 + (x.shape[-1] if x.ndim > 1 else len(x)) <= 0:
        return
    if x.ndim == 1:
        a = np.pi / 4 * (pan + 1)
        x = np.vstack([x * np.cos(a), x * np.sin(a)]) * np.sqrt(2)
    n = x.shape[1]
    j0, j1 = max(0, i0), min(N, i0 + n)
    buf[:, j0:j1] += g * x[:, j0 - i0:j1 - i0]


def lp(x, fc, ordem=2):
    b, a = signal.butter(ordem, fc / (SR / 2), "low")
    return signal.lfilter(b, a, x, axis=-1)


def hp(x, fc, ordem=2):
    b, a = signal.butter(ordem, fc / (SR / 2), "high")
    return signal.lfilter(b, a, x, axis=-1)


def bp(x, f1, f2, ordem=2):
    b, a = signal.butter(ordem, [f1 / (SR / 2), f2 / (SR / 2)], "band")
    return signal.lfilter(b, a, x, axis=-1)


# ---------------------------------------------------------------- instrumentos
def serra(f, n, teto=5200.0, fase=0.0):
    """Dente de serra somada harmônico a harmônico até o teto (sem serrilhado)."""
    t = tt(n); x = np.zeros(n)
    for k in range(1, max(2, int(teto / f)) + 1):
        x += np.sin(2 * np.pi * k * f * t + k * fase) / k
    return x * (2 / np.pi)


def pad(notas, dur, ataque=.35, solta=.5):
    n = int((dur + solta) * SR); t = tt(n)
    env = np.clip(t / ataque, 0, 1) * np.where(t < dur, 1.0, np.exp(-(t - dur) / (solta / 3)))
    L = np.zeros(n); R = np.zeros(n)
    for m in notas:
        f = midi(m)
        for cents, lado in [(-9, "L"), (0, "C"), (9, "R")]:
            v = serra(f * 2 ** (cents / 1200), n, fase=rng.uniform(0, 2 * np.pi)) * env
            if lado == "L": L += v
            elif lado == "R": R += v
            else: L += .7 * v; R += .7 * v
    st = lp(np.vstack([L, R]), 1700, 2) / (len(notas) * 2.4)
    return st


def sino(f, dur=.9, brilho=1.0, decai=.32):
    """Sino macio (FM): o modulador some depressa e deixa a senoide, com um pouco da oitava."""
    n = int(dur * SR); t = tt(n)
    ind = brilho * 1.6 * np.exp(-t / .07)
    x = np.sin(2 * np.pi * f * t + ind * np.sin(2 * np.pi * 2 * f * t))
    x += .22 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / (decai * .5))
    env = np.minimum(t / .003, 1) * np.exp(-t / decai)
    return x * env


def baixo(f, dur):
    n = int(dur * SR); t = tt(n)
    x = np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * 2 * f * t) + .12 * np.sin(2 * np.pi * 3 * f * t)
    env = np.minimum(t / .006, 1) * np.exp(-t / .16)
    return np.tanh(1.6 * x * env) * .8


def bumbo():
    n = int(.42 * SR); t = tt(n)
    fq = 48 + 105 * np.exp(-t / .028)
    fase = 2 * np.pi * np.cumsum(fq) / SR
    x = np.sin(fase) * np.exp(-t / .2)
    x[:int(.002 * SR)] += rng.normal(0, .35, int(.002 * SR))
    return np.tanh(1.4 * x)


def palmas():
    n = int(.35 * SR); t = tt(n); x = np.zeros(n)
    for d in (0, .011, .022):
        i = int(d * SR); m = n - i
        x[i:] += rng.normal(0, 1, m) * np.exp(-tt(m) / (.012 if d < .02 else .11))
    return bp(x, 900, 3200) * .9


def chimbal(aberto=False):
    n = int((.32 if aberto else .07) * SR); t = tt(n)
    return hp(rng.normal(0, 1, n), 7000, 2) * np.exp(-t / (.11 if aberto else .022)) * .5


def sopro(dur=.38, f0=500, f1=5200, sobe=True):
    """Sopro de passagem: ruído numa faixa que corre de f0 a f1."""
    n = int(dur * SR); t = tt(n); x = rng.normal(0, 1, n)
    fc = f0 * (f1 / f0) ** (t / dur) if sobe else f1 * (f0 / f1) ** (t / dur)
    # filtro passa-faixa de estado variável (forma TPT), com a frequência mudando a cada amostra, sem saltos
    g = np.tan(np.pi * np.minimum(fc, SR * .45) / SR); k = 1 / 1.2
    y = np.zeros(n); s1 = s2 = 0.0
    for i in range(n):
        gi = g[i]; hp_ = (x[i] - (k + gi) * s1 - s2) / (1 + gi * (k + gi))
        v1 = gi * hp_; bp_ = v1 + s1; s1 = bp_ + v1
        v2 = gi * bp_; lp_ = v2 + s2; s2 = lp_ + v2
        y[i] = bp_
    env = np.sin(np.pi * t / dur) ** 1.6
    return y * env * .6


def estalo():
    n = int(.09 * SR); t = tt(n)
    f = 300 + 900 * np.exp(-t / .012)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .025)


def taca(f0, forca=1.0):
    """Taça de vidro tocada: parciais desarmônicos do vidro, cada um com seu tempo, e um toque curto no ataque."""
    n = int(2.4 * SR); t = tt(n); x = np.zeros(n)
    for r, a, d in [(1.0, 1.0, 1.15), (2.32, .5, .55), (4.25, .26, .26), (5.98, .14, .14), (8.1, .07, .08)]:
        f = f0 * r
        x += a * (np.sin(2 * np.pi * f * t) + .6 * np.sin(2 * np.pi * f * 1.0016 * t + 1.1)) * np.exp(-t / d)
    m = int(.004 * SR)
    x[:m] += hp(rng.normal(0, 1, m), 4000, 2) * 1.2
    return x * np.minimum(t / .0007, 1) * forca * .5


# ---------------------------------------------------------------- partitura
seco = np.zeros((2, N)); sala = np.zeros((2, N)); eco = np.zeros((2, N)); base = np.zeros((2, N))
# acordes (início, fim, notas do acorde, baixo, arpejo de oito colcheias)
AC = [(0, 2, [50, 57, 62, 66], 38, [74, 81, 78, 81, 86, 81, 78, 81]),
      (2, 4, [49, 57, 61, 64], 33, [73, 81, 76, 81, 85, 81, 76, 81]),
      (4, 6, [50, 54, 59, 62], 35, [74, 83, 78, 83, 86, 83, 78, 83]),
      (6, 8, [50, 55, 59, 62], 31, [74, 83, 79, 83, 86, 83, 79, 83]),
      (8, 10, [50, 57, 62, 66], 38, [74, 81, 78, 81, 86, 81, 78, 81]),
      (10, 12, [49, 57, 61, 64], 33, [73, 81, 76, 81, 85, 81, 76, 81]),
      (12, 14, [50, 54, 59, 62], 35, [74, 83, 78, 83, 86, 83, 78, 83]),
      (14, 16, [50, 55, 59, 62], 31, [74, 83, 79, 83, 86, 83, 79, 83]),
      (16, 17.5, [50, 55, 59, 64], 40, [74, 83, 79, 83, 88, 83, 79, 83]),
      (17.5, 18.5, [50, 57, 62, 64], 33, [74, 81, 76, 81, 86, 81, 76, 81]),
      (18.5, 19.5, [49, 57, 61, 64], 33, [73, 81, 76, 81, 85, 81, 76, 81])]
FIM, DUR = T.FIM, T.DUR
for a, b, notas, bx, arp in AC:
    p = pad(notas, b - a, ataque=.05 if a == 0 else .3)
    mix(base, p, a, g=.55); mix(sala, p, a, g=.22)
    # arpejo em colcheias (meia batida), mais baixo no gancho e crescendo no primeiro segundo
    k = 0; s = a
    while s < b - 1e-6:
        m = arp[k % 8]
        g = .26 * (.55 + .45 * min(1, s / 1.0))
        x = sino(midi(m), .8, brilho=.8, decai=.24)
        pan = -.35 if k % 2 == 0 else .35
        mix(seco, x, s, pan, g); mix(eco, x, s, pan, g * .9); mix(sala, x, s, pan, g * .5)
        k += 1; s += B / 2
    # baixo pulsando em colcheias, a partir de 1 s, até o fechamento
    s = max(a, 1.0)
    while s < min(b, FIM) - 1e-6:
        mix(base, baixo(midi(bx + 12), B / 2 + .05), s, 0, .42)
        s += B / 2

# fechamento: acorde de Ré com a nona (resolve) e o arpejo mais lento
p = pad([50, 57, 62, 64, 66, 69], DUR - FIM - .3, ataque=.08, solta=.6)
mix(base, p, FIM, g=.5); mix(sala, p, FIM, g=.3)
mix(base, baixo(midi(38), 1.6) * np.linspace(1, .6, int(1.6 * SR)), FIM, 0, .45)
for i, m in enumerate([74, 78, 81, 86, 88, 86, 81]):
    s = FIM + .55 + i * B * .5
    if s < DUR - .6:
        x = sino(midi(m), 1.4, .6, .5); mix(seco, x, s, -.3 if i % 2 else .3, .2); mix(sala, x, s, 0, .25)

# bateria: bumbo de 1 s ao fechamento; palmas e chimbal a partir do menu
bum = bumbo(); duck = np.ones(N)
s = 1.0
while s < FIM - 1e-6:
    mix(seco, bum, s, 0, .75)
    i = int(s * SR); m = min(N - i, int(.25 * SR))
    duck[i:i + m] = np.minimum(duck[i:i + m], 1 - .45 * np.exp(-tt(m) / .09))
    s += B
s = T.JANELA_ENTRA
while s < FIM - 1e-6:
    bat = round((s - T.JANELA_ENTRA) / B)
    if bat % 2 == 1:
        pal = palmas(); mix(seco, pal, s, .05, .32); mix(sala, pal, s, 0, .2)
    mix(seco, chimbal(), s + B / 2, .25 if bat % 2 else -.25, .3)
    s += B
for s in (15.0, 15.25, 15.375):                       # virada antes de "E mais"
    mix(seco, palmas(), s, 0, .22)
mix(seco, chimbal(True), T.JANELA_SAI, .2, .3)
base *= duck  # o acorde e o baixo abrem espaço para o bumbo

# efeitos no tempo das cenas
for i, m in enumerate([86, 90, 93, 98]):              # brilho da coroa
    x = sino(midi(m), 1.2, 1.2, .45); s = .3 + .045 * i
    mix(seco, x, s, -.6 + .4 * i, .16); mix(sala, x, s, 0, .3)
mix(seco, estalo(), .75, 0, .35); mix(seco, sino(midi(81), .9, 1, .3), .75, 0, .18)    # o preço salta
mix(sala, sino(midi(93), 1, 1, .35), T.SELO, .3, .22); mix(seco, sino(midi(93), 1, 1, .35), T.SELO, .3, .12)   # anel no selo
for i, m in enumerate([78, 81, 83, 86, 88]):          # o anel desce pelas cinco coroas
    s = T.VARRE[0] + i * (T.VARRE[1] - T.VARRE[0]) / 5
    x = sino(midi(m), .9, 1, .28); mix(seco, x, s, -.4 + .2 * i, .17); mix(sala, x, s, 0, .2)
for s in [T.G_SAI - .05, T.FIM - .1]:                  # passagens grandes
    w = sopro(.5, 400, 7000); mix(seco, w, s, 0, .2); mix(sala, w, s, 0, .15)
for s in T.TROCAS + [T.JANELA_SAI, T.PRECO]:          # trocas de tela
    w = sopro(.32, 900, 6000); mix(seco, w, s - .2, -.2, .11)
for s in [x + T.ANEL_ATRASO for x in T.TROCAS] + [T.PRECO_ANEL]:   # cada anel
    mix(seco, sino(midi(98), .5, .6, .12), s, .15, .07)
for i, (s, m) in enumerate(zip(T.MAIS, [86, 90, 93])):  # as três linhas de "E mais"
    x = sino(midi(m), .9, 1, .3); mix(seco, x, s, -.3 + .3 * i, .17); mix(sala, x, s, 0, .2)
for m in [81, 85, 88]:                                 # o anel nos preços
    x = sino(midi(m), 1.2, .7, .5); mix(seco, x, T.PRECO_ANEL, 0, .09); mix(sala, x, T.PRECO_ANEL, 0, .12)
# o brinde: duas taças, duas vezes ("tim-tim"), no tom do acorde final (Fá sustenido e Lá)
for k, s in enumerate(T.TIM_TIM):
    forca = 1.0 if k == 0 else .78
    for f0, pan in [(midi(90), -.25), (midi(93), .25)]:
        x = taca(f0, forca); mix(seco, x, s, pan, .30); mix(sala, x, s, 0, .32)

# ---------------------------------------------------------------- eco, sala e mistura
d = int(.375 * SR)
for k, g in [(1, .32), (2, .19), (3, .1)]:             # eco em pingue-pongue (colcheia pontuada)
    src = eco[1] if k % 2 else eco[0]
    lado = 0 if k % 2 else 1
    seco[lado, k * d:] += g * src[:N - k * d]

ir_n = int(2.4 * SR); t_ir = tt(ir_n)
ir = rng.normal(0, 1, (2, ir_n)) * np.exp(-t_ir * 6.9 / 1.7)
ir = lp(ir, 5200, 1); ir[:, :int(.018 * SR)] = 0
ir /= np.sqrt((ir ** 2).sum(axis=1, keepdims=True))
molhado = np.vstack([signal.fftconvolve(hp(sala[c], 180), ir[c])[:N] for c in range(2)]) * .55

master = hp(seco + base + molhado, 28, 2)
fade = np.ones(N); f0 = int(.004 * SR); fade[:f0] = np.linspace(0, 1, f0)
fi = int((DUR - 1.1) * SR); fade[fi:] = np.cos(np.linspace(0, np.pi / 2, N - fi)) ** 2
master *= fade
master = np.tanh(1.15 * master / np.max(np.abs(master))) / np.tanh(1.15)
master *= 10 ** (-1 / 20)

os.makedirs(os.path.join(AQUI, "trabalho"), exist_ok=True)
bruto = os.path.join(AQUI, "trabalho", "trilha.wav")
from scipy.io import wavfile
wavfile.write(bruto, SR, master.T.astype(np.float32))
# volume: duas passagens do loudnorm (EBU R128) para -14 LUFS e pico real de -1,5 dB
med = subprocess.run(["ffmpeg", "-hide_banner", "-i", bruto, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
js = json.loads(med[med.rindex("{"):med.rindex("}") + 1])
filtro = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:"
          f"measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true:print_format=summary")
saida = os.path.join(AQUI, "trabalho", "trilha_norm.wav")
r = subprocess.run(["ffmpeg", "-hide_banner", "-y", "-i", bruto, "-af", filtro, "-ar", "48000", "-c:a", "pcm_s16le", saida], capture_output=True, text=True)
print("antes:", js["input_i"], "LUFS, pico", js["input_tp"], "dBTP")
print(r.stderr[r.stderr.find("Input Integrated"):][:600])
