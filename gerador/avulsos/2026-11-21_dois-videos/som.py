# -*- coding: utf-8 -*-
"""Instrumentos e mesa de som das trilhas originais dos vídeos de 20/11/2026.

Tudo é sintetizado aqui, amostra por amostra, com numpy e scipy: senoides, ondas somadas harmônico a harmônico e ruído
filtrado. Não há música, gravação, amostra nem efeito de terceiros. As harmonias são sequências comuns de acordes, que não
pertencem a ninguém; as melodias, os baixos e as baterias são escritos em trilha1.py e trilha2.py.
"""
import os, json, subprocess
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def tt(n):
    return np.arange(n) / SR


def lp(x, fc, ordem=2):
    b, a = signal.butter(ordem, fc / (SR / 2), "low"); return signal.lfilter(b, a, x, axis=-1)


def hp(x, fc, ordem=2):
    b, a = signal.butter(ordem, fc / (SR / 2), "high"); return signal.lfilter(b, a, x, axis=-1)


def bp(x, f1, f2, ordem=2):
    b, a = signal.butter(ordem, [f1 / (SR / 2), f2 / (SR / 2)], "band"); return signal.lfilter(b, a, x, axis=-1)


class Mesa:
    """Quatro vias: seco, base (acordes e baixo, que abrem espaço para o bumbo), sala (vai para a reverberação) e eco."""

    def __init__(self, dur, semente):
        self.dur = dur; self.N = int(dur * SR); self.rng = np.random.default_rng(semente)
        self.seco, self.base, self.sala, self.eco = (np.zeros((2, self.N)) for _ in range(4))
        self.duck = np.ones(self.N)

    def poe(self, via, x, t0, pan=0.0, g=1.0):
        buf = getattr(self, via); i0 = int(round(t0 * SR)); n = x.shape[-1]
        if i0 >= self.N or i0 + n <= 0: return
        if x.ndim == 1:
            a = np.pi / 4 * (pan + 1); x = np.vstack([x * np.cos(a), x * np.sin(a)]) * np.sqrt(2)
        j0, j1 = max(0, i0), min(self.N, i0 + n)
        buf[:, j0:j1] += g * x[:, j0 - i0:j1 - i0]

    def toca(self, x, t0, pan=0.0, g=1.0, sala=0.0, eco=0.0, via="seco"):
        self.poe(via, x, t0, pan, g)
        if sala: self.poe("sala", x, t0, pan * .5, g * sala)
        if eco: self.poe("eco", x, t0, pan, g * eco)

    def abre(self, t0, fundo=.45, tempo=.09, dur=.25):
        """O bumbo em t0 abaixa a via base por um instante."""
        i = int(t0 * SR); m = min(self.N - i, int(dur * SR))
        if m > 0: self.duck[i:i + m] = np.minimum(self.duck[i:i + m], 1 - fundo * np.exp(-tt(m) / tempo))

    def fecha(self, caminho, eco_s=.375, sala_s=1.7, sala_g=.55, saida=1.1):
        N = self.N; d = int(eco_s * SR)
        for k, g in [(1, .32), (2, .19), (3, .1)]:                      # eco em pingue-pongue
            if k * d < N: self.seco[0 if k % 2 else 1, k * d:] += g * self.eco[1 if k % 2 else 0, :N - k * d]
        n_ir = int((sala_s + .7) * SR); t = tt(n_ir)
        ir = self.rng.normal(0, 1, (2, n_ir)) * np.exp(-t * 6.9 / sala_s); ir = lp(ir, 5200, 1); ir[:, :int(.018 * SR)] = 0
        ir /= np.sqrt((ir ** 2).sum(axis=1, keepdims=True))
        molhado = np.vstack([signal.fftconvolve(hp(self.sala[c], 180), ir[c])[:N] for c in range(2)]) * sala_g
        m = hp(self.seco + self.base * self.duck + molhado, 28, 2)
        fade = np.ones(N); f0 = int(.004 * SR); fade[:f0] = np.linspace(0, 1, f0)
        fi = int((self.dur - saida) * SR); fade[fi:] = np.cos(np.linspace(0, np.pi / 2, N - fi)) ** 2
        m *= fade; m = np.tanh(1.15 * m / np.max(np.abs(m))) / np.tanh(1.15) * 10 ** (-1 / 20)
        bruto = caminho.replace(".wav", "_bruto.wav")
        wavfile.write(bruto, SR, m.T.astype(np.float32))
        # volume: duas passagens do loudnorm (EBU R128) para -14 LUFS e pico real de -1,5 dB
        med = subprocess.run(["ffmpeg", "-hide_banner", "-i", bruto, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                             capture_output=True, text=True).stderr
        js = json.loads(med[med.rindex("{"):med.rindex("}") + 1])
        filtro = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:"
                  f"measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true:print_format=summary")
        r = subprocess.run(["ffmpeg", "-hide_banner", "-y", "-i", bruto, "-af", filtro, "-ar", "48000", "-c:a", "pcm_s16le", caminho], capture_output=True, text=True)
        fim = r.stderr[r.stderr.find("Output Integrated"):]
        print("antes:", js["input_i"], "LUFS · depois:", " ".join(fim.split()[:8]))
        return m


# ---------------------------------------------------------------- instrumentos
def serra(f, n, teto=5200.0, fase=0.0):
    t = tt(n); x = np.zeros(n)
    for k in range(1, max(2, int(teto / f)) + 1): x += np.sin(2 * np.pi * k * f * t + k * fase) / k
    return x * (2 / np.pi)


def pad(rng, notas, dur, ataque=.35, solta=.5, corte=1700):
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
    return lp(np.vstack([L, R]), corte, 2) / (len(notas) * 2.4)


def sino(f, dur=.9, brilho=1.0, decai=.32):
    n = int(dur * SR); t = tt(n)
    x = np.sin(2 * np.pi * f * t + brilho * 1.6 * np.exp(-t / .07) * np.sin(2 * np.pi * 2 * f * t))
    x += .22 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / (decai * .5))
    return x * np.minimum(t / .003, 1) * np.exp(-t / decai)


def marimba(f, dur=.7, decai=.2):
    """Tecla de madeira: a fundamental, o parcial de 4 vezes (o da marimba) e um toque curto de baqueta."""
    n = int(dur * SR); t = tt(n)
    x = np.sin(2 * np.pi * f * t) * np.exp(-t / decai)
    if 4 * f < 18000: x += .32 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / (decai * .22))
    if 9.2 * f < 18000: x += .1 * np.sin(2 * np.pi * 9.2 * f * t) * np.exp(-t / .015)
    return x * np.minimum(t / .0015, 1)


def epiano(f, dur=1.6, decai=1.3, brilho=1.0):
    """Piano elétrico macio: uma senoide modulada de leve por outra igual, com o "tine" curto no ataque."""
    n = int((dur + .25) * SR); t = tt(n)
    ind = brilho * (.9 * np.exp(-t / .3) + .25)
    x = np.sin(2 * np.pi * f * t + ind * np.sin(2 * np.pi * f * t))
    if 14 * f < 18000: x += .07 * brilho * np.sin(2 * np.pi * 14 * f * t) * np.exp(-t / .035)
    env = np.minimum(t / .004, 1) * np.exp(-t / decai) * np.where(t < dur, 1.0, np.exp(-(t - dur) / .06))
    trem = 1 + .06 * np.sin(2 * np.pi * 4.6 * t)
    return np.vstack([x * env * trem, x * env * (2 - trem)]) * .5


def baixo(f, dur, decai=.16):
    n = int(dur * SR); t = tt(n)
    x = np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * 2 * f * t) + .12 * np.sin(2 * np.pi * 3 * f * t)
    return np.tanh(1.6 * x * np.minimum(t / .006, 1) * np.exp(-t / decai)) * .8


def sub(f, dur):
    """Baixo grave e redondo, que sustenta e solta."""
    n = int((dur + .08) * SR); t = tt(n)
    x = np.sin(2 * np.pi * f * t) + .45 * np.sin(2 * np.pi * 2 * f * t) + .22 * np.sin(2 * np.pi * 3 * f * t) + .1 * np.sin(2 * np.pi * 4 * f * t)   # harmônicos para o baixo existir no alto-falante do celular
    env = np.minimum(t / .012, 1) * (.75 + .25 * np.exp(-t / .25)) * np.where(t < dur, 1.0, np.exp(-(t - dur) / .03))
    return np.tanh(1.3 * x * env) * .8


def bumbo(rng, grave=48, decai=.2):
    n = int(.45 * SR); t = tt(n)
    x = np.sin(2 * np.pi * np.cumsum(grave + 105 * np.exp(-t / .028)) / SR) * np.exp(-t / decai)
    x[:int(.002 * SR)] += rng.normal(0, .35, int(.002 * SR))
    return np.tanh(1.4 * x)


def palmas(rng):
    n = int(.35 * SR); x = np.zeros(n)
    for d in (0, .011, .022):
        i = int(d * SR); m = n - i; x[i:] += rng.normal(0, 1, m) * np.exp(-tt(m) / (.012 if d < .02 else .11))
    return bp(x, 900, 3200) * .9


def estalo_dedos(rng):
    n = int(.22 * SR); x = np.zeros(n)
    for d, g in ((0, .6), (.012, 1.0)):
        i = int(d * SR); m = n - i; x[i:] += g * rng.normal(0, 1, m) * np.exp(-tt(m) / .028)
    return bp(x, 1500, 4800) * 1.1


def chimbal(rng, aberto=False):
    n = int((.32 if aberto else .07) * SR)
    return hp(rng.normal(0, 1, n), 7000, 2) * np.exp(-tt(n) / (.11 if aberto else .022)) * .5


def chocalho(rng):
    n = int(.09 * SR); t = tt(n)
    return hp(rng.normal(0, 1, n), 5500, 2) * np.minimum(t / .012, 1) * np.exp(-t / .03) * .5


def tecla(rng, f=2200):
    """Toque de tecla: um clique curto e seco."""
    n = int(.03 * SR); t = tt(n)
    return (np.sin(2 * np.pi * f * t) * np.exp(-t / .004) + .5 * hp(rng.normal(0, 1, n), 3000) * np.exp(-t / .003)) * .8


def sopro(rng, dur=.38, f0=500, f1=5200, sobe=True, crescendo=False):
    """Sopro de passagem: ruído numa faixa que corre de f0 a f1 (filtro de estado variável, sem saltos)."""
    n = int(dur * SR); t = tt(n); x = rng.normal(0, 1, n)
    fc = f0 * (f1 / f0) ** (t / dur) if sobe else f1 * (f0 / f1) ** (t / dur)
    g = np.tan(np.pi * np.minimum(fc, SR * .45) / SR); k = 1 / 1.2
    y = np.zeros(n); s1 = s2 = 0.0
    for i in range(n):
        gi = g[i]; h = (x[i] - (k + gi) * s1 - s2) / (1 + gi * (k + gi))
        v1 = gi * h; b_ = v1 + s1; s1 = b_ + v1; v2 = gi * b_; s2 = v2 + s2 + v2; y[i] = b_
    env = (t / dur) ** 2 * np.minimum((dur - t) / .03, 1) if crescendo else np.sin(np.pi * t / dur) ** 1.6
    return y * env * .6


def estalo():
    n = int(.09 * SR); t = tt(n)
    return np.sin(2 * np.pi * np.cumsum(300 + 900 * np.exp(-t / .012)) / SR) * np.exp(-t / .025)


def baque(f=70):
    """Baque grave e curto (o número que assenta)."""
    n = int(.5 * SR); t = tt(n)
    return np.tanh(1.5 * np.sin(2 * np.pi * np.cumsum(f + 60 * np.exp(-t / .04)) / SR) * np.exp(-t / .16))


def taca(rng, f0, forca=1.0):
    """Taça de vidro tocada: os parciais desarmônicos do vidro, cada um com o seu tempo, e o toque no ataque."""
    n = int(2.4 * SR); t = tt(n); x = np.zeros(n)
    for r, a, d in [(1.0, 1.0, 1.15), (2.32, .5, .55), (4.25, .26, .26), (5.98, .14, .14), (8.1, .07, .08)]:
        f = f0 * r
        if f < 20000: x += a * (np.sin(2 * np.pi * f * t) + .6 * np.sin(2 * np.pi * f * 1.0016 * t + 1.1)) * np.exp(-t / d)
    m = int(.004 * SR); x[:m] += hp(rng.normal(0, 1, m), 4000, 2) * 1.2
    return x * np.minimum(t / .0007, 1) * forca * .5


def tim_tim(mesa, tempos, f_a, f_b, g=.30):
    """O brinde, som do nome: duas taças, duas vezes."""
    for k, s in enumerate(tempos):
        for f0, pan in [(f_a, -.25), (f_b, .25)]:
            mesa.toca(taca(mesa.rng, f0, 1.0 if k == 0 else .78), s, pan, g, sala=1.05)


def notas_fortes(caminho, a, b, fmax=420, k=6):
    """As notas mais fortes de um trecho do arquivo (para conferir o acorde sem ouvir)."""
    sr, x = wavfile.read(caminho); m = x.astype(np.float64).mean(axis=1)
    s = m[int(a * sr):int(b * sr)]; s = s * np.hanning(len(s)); S = np.abs(np.fft.rfft(s)); f = np.fft.rfftfreq(len(s), 1 / sr)
    sel = (f > 60) & (f < fmax); out = []
    nomes = ["Dó", "Dó#", "Ré", "Ré#", "Mi", "Fá", "Fá#", "Sol", "Sol#", "Lá", "Lá#", "Si"]
    for fr in f[sel][np.argsort(S[sel])[::-1]]:
        n = int(round(69 + 12 * np.log2(fr / 440))); nm = nomes[n % 12] + str(n // 12 - 1)
        if nm not in out: out.append(nm)
        if len(out) >= k: break
    return out
