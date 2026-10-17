# -*- coding: utf-8 -*-
"""Peças comuns da equipe r3 (Reels de 25/11, 27/11 e 30/11 de 2026), por cima do kit (N/kit/reelkit.py).

- camadas(): várias capturas reais empilhadas na mesma .tela, para trocar de passo com fusão;
- cronometro(): o cronômetro desenhado (traço, pontas redondas), usado no Reel de 25/11 e na capa;
- JS_R3: funções JavaScript extras (opacidade de camada, cronômetro regressivo).
Nada aqui altera captura: as telas só são recortadas, redimensionadas e trocadas por fusão.
"""
import os, sys, math
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, os.path.join(N, "kit"))
import reelkit as K
A = K.A

R3 = os.path.dirname(os.path.abspath(__file__))
MENOS = "−"


def saida(pasta):
    return os.path.join(N, "saida", pasta)


def trabalho(nome):
    return os.path.join(R3, "trabalho", nome)


def camadas(tid, imgs, extra=""):
    """imgs: lista de (id, caminho). A primeira começa visível; as outras, transparentes."""
    ims = "".join(f'<img id="{i}" src="file://{c}" style="opacity:{1 if k == 0 else 0}">' for k, (i, c) in enumerate(imgs))
    return f'<div class="tela" id="{tid}">{ims}{extra}</div>'


def cronometro(ident, rotulo="US$ → R$", cor_arco=None, cor_corpo="#fff", cor_txt=None, cor_trilha=None, digitos="0:30"):
    """Cronômetro de traço (viewBox 200 × 220): coroa, botão lateral, mostrador com 30 marcas, arco do tempo
    que resta, cabeça do arco e os dígitos. ids: <ident>Arco, <ident>Cab, <ident>Dig, <ident>Rot, <ident>Ok."""
    cor_arco = cor_arco or A.BRAND
    cor_txt = cor_txt or A.INK
    cor_trilha = cor_trilha or "#E4F4EC"
    cx, cy, r = 100, 120, 70
    marcas = []
    for i in range(30):
        ang = math.radians(i * 12 - 90)
        r1 = 88 if i % 5 else 84
        r2 = 93
        x1, y1 = cx + r1 * math.cos(ang), cy + r1 * math.sin(ang)
        x2, y2 = cx + r2 * math.cos(ang), cy + r2 * math.sin(ang)
        marcas.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{A.NEUTRO if i % 5 else A.MUTED}" '
                      f'stroke-width="{2.2 if i % 5 else 3.2}" stroke-linecap="round"/>')
    circ = 2 * math.pi * r
    return f"""<svg id="{ident}" viewBox="0 0 200 220" width="100%" height="100%" style="overflow:visible;display:block">
  <rect x="86" y="2" width="28" height="13" rx="6.5" fill="{A.INK}"/>
  <rect x="95" y="12" width="10" height="14" rx="3" fill="{A.INK}"/>
  <g transform="rotate(45 100 120)"><rect x="94" y="11" width="12" height="16" rx="4" fill="{A.INK}"/></g>
  <circle cx="{cx}" cy="{cy}" r="97" fill="{cor_corpo}" stroke="{A.INK}" stroke-width="6"/>
  {"".join(marcas)}
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{cor_trilha}" stroke-width="12"/>
  <circle id="{ident}Arco" cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{cor_arco}" stroke-width="12" stroke-linecap="round"
    stroke-dasharray="{circ:.2f} {circ:.2f}" transform="rotate(-90 {cx} {cy})"/>
  <circle id="{ident}Cab" cx="{cx}" cy="{cy - r}" r="9.5" fill="{cor_arco}" stroke="#fff" stroke-width="3.5"/>
  <text id="{ident}Dig" x="{cx}" y="{cy + 15}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="44"
    letter-spacing="-1.5" fill="{cor_txt}" style="font-variant-numeric:tabular-nums;font-feature-settings:'tnum','cv11','ss01'">{digitos}</text>
  <text id="{ident}Rot" x="{cx}" y="{cy + 44}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="15"
    letter-spacing="0.3" fill="{A.BRAND_DARK}">{rotulo}</text>
  <g id="{ident}Ok" style="opacity:0">
    <circle cx="{cx + 62}" cy="{cy + 62}" r="27" fill="{A.BRAND}" stroke="#fff" stroke-width="6"/>
    <path d="M{cx + 50} {cy + 62} l8 8 l15 -16" fill="none" stroke="#fff" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>"""


CIRC_CRONO = 2 * math.pi * 70

JS_R3 = r"""
// opacidade de uma camada (imagem de captura) dentro da .tela
function op(id, v){ $(id).style.opacity = clamp(v, 0, 1); }
// cronômetro regressivo de `total` s que começa em t0 e para em tPara. A cabeça anda no sentido do relógio
// e "come" o arco do tempo que resta (o arco vai da cabeça até o 12).
const CIRC_CRONO = %(circ).4f;
function cronometro(pre, t, t0, total, tPara){
  const tt = Math.min(t, tPara === undefined ? 1e9 : tPara);
  const resta = clamp(total - (tt - t0), 0, total);
  const seg = Math.ceil(resta - 1e-6);
  $(pre+'Dig').textContent = '0:' + String(seg).padStart(2, '0');
  const f = resta / total, C = CIRC_CRONO;
  const arco = $(pre+'Arco');
  arco.setAttribute('stroke-dasharray', (C*f).toFixed(2) + ' ' + (C+1).toFixed(2));
  arco.setAttribute('stroke-dashoffset', (-C*(1-f)).toFixed(2));
  const th = 2*Math.PI*(1-f);
  $(pre+'Cab').setAttribute('cx', (100 + 70*Math.sin(th)).toFixed(2));
  $(pre+'Cab').setAttribute('cy', (120 - 70*Math.cos(th)).toFixed(2));
  return resta;
}
""" % {"circ": 2 * math.pi * 70}
