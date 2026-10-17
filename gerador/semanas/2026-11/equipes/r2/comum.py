# -*- coding: utf-8 -*-
"""Peças comuns dos Reels da equipe r2 (14/11, 18/11 e 22/11 de 2026), por cima do kit (N/kit/reelkit.py, só leitura)."""
import os, sys, json
N = "/tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez"
sys.path.insert(0, os.path.join(N, "kit"))
import reelkit as K
A = K.A
R2 = os.path.join(N, "equipes", "r2")
MENOS = "−"   # sinal de menos, como o site

# JavaScript extra (vale para todos os roteiros da equipe)
JS_EXTRA = r"""
// janela com entrada e saída controladas (opacidade e deslocamento), para qualquer elemento
function entra(id, t, a, b, dy){ dy = dy===undefined ? 70 : dy; const e=$(id); const ent=prog(t,a,a+.55), sai=b ? prog(t,b,b+.4) : 0;
  e.style.opacity=Math.min(ent, 1-sai); e.style.transform=`translateY(${(1-ent)*dy - sai*40}px)`; }
// cena inteira que sai para cima (como a capa de outubro), entre a e a+.45
function saiCima(id, t, a){ const f = prog(t, a, a+.45); $(id).style.transform = `translateY(${-1920*f}px)`; }
// panorâmica em etapas: lista de [início, fim, topo] em px CSS do celular
function panEtapas(id, t, topo0, etapas){ let v = topo0; for (const [a,b,alvo] of etapas){ v += (alvo - v)*prog(t,a,b); } pan(id, v); return v; }
// câmera sobre a tela real: KF = [[_, _, fx, fy, s], [a, b, fx, fy, s], ...]; (fx, fy) em px CSS do celular fica no
// centro da janela (larg x alt px do Reel), com zoom s (1 = 2 px do Reel por px CSS, como no kit)
function camera(id, t, KF, larg, alt){ larg = larg || 780; alt = alt || 1000;
  let fx=KF[0][2], fy=KF[0][3], s=KF[0][4];
  for (let i=1;i<KF.length;i++){ const [a,b,x,y,z] = KF[i]; const p = prog(t,a,b); fx += (x-fx)*p; fy += (y-fy)*p; s += (z-s)*p; }
  $(id).style.transform = `translate(${(larg/2 - s*E*fx).toFixed(2)}px, ${(alt/2 - s*E*fy).toFixed(2)}px) scale(${s.toFixed(4)})`;
  return [fx, fy, s]; }
"""


def _limpa(v):
    if isinstance(v, str):
        return v.replace(" ", " ").replace(" ", " ")
    if isinstance(v, dict):
        return {k: _limpa(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_limpa(x) for x in v]
    return v


def caixas(pasta, nome="caixas.json"):
    """Caixas e textos medidos na captura (espaços não separáveis viram espaços comuns, para conferir os números)."""
    return _limpa(json.load(open(os.path.join(N, "saida", pasta, "telas", nome), encoding="utf-8")))


def pagina(corpo, css, js):
    return K.pagina(corpo, css, JS_EXTRA + js)
