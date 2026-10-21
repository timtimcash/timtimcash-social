# -*- coding: utf-8 -*-
"""O envelope da dupla de Carnaval (Reels de 05/02 e 10/02/2027, e as duas capas): o mesmo desenho nos dois vídeos.

Desenho próprio, de traço (corpo de cantos redondos e a aba em V), sem imagem de dinheiro. Em camadas, para o valor
"entrar" no envelope: aba aberta atrás, o que entra no meio, corpo e aba fechada na frente. A aba gira no eixo de cima
(scaleY de -1, aberta, a 1, fechada). Texto sem travessão nem meia-risca.
"""


def partes(larg, cor, traco, fundo):
    """Devolve (corpo, aba): dois SVGs do mesmo tamanho (larg x altura), para empilhar em camadas.
    A aba aponta para baixo (fechada); aberta, é a mesma aba com scaleY(-1) no eixo de cima (y = 0 do corpo)."""
    w = larg
    h = round(larg * 0.66)
    t = traco
    vb = f"{-t} {-t} {w + 2 * t} {h + 2 * t}"
    corpo = (f'<svg width="{w + 2 * t}" height="{h + 2 * t}" viewBox="{vb}" style="display:block;overflow:visible">'
             f'<rect x="0" y="0" width="{w}" height="{h}" rx="{w * .07:.1f}" fill="{fundo}" stroke="{cor}" stroke-width="{t}" stroke-linejoin="round"/></svg>')
    aba = (f'<svg width="{w + 2 * t}" height="{h + 2 * t}" viewBox="{vb}" style="display:block;overflow:visible">'
           f'<path d="M{w * .035:.1f} {t * .15:.1f} L{w / 2:.1f} {h * .55:.1f} L{w * .965:.1f} {t * .15:.1f}" fill="{fundo}" stroke="{cor}" '
           f'stroke-width="{t}" stroke-linejoin="round" stroke-linecap="round"/></svg>')
    return corpo, aba, w, h


def html(prefixo, larg, cor, traco, fundo, x, y, meio="", rotulo=""):
    """Envelope em camadas na posição (x, y) do Reel (canto de cima do corpo), com ids:
    {p}AbaAtras (aba aberta, atrás), {p}Meio (o que entra), {p}Corpo, {p}Rot (o valor no corpo), {p}AbaFrente (aba fechada, na frente).
    `meio`: HTML do que entra no envelope (posicionado pelo roteiro); `rotulo`: HTML do valor escrito no corpo."""
    corpo, aba, w, h = partes(larg, cor, traco, fundo)
    t = traco
    base = f"position:absolute;left:{x - t}px;top:{y - t}px;width:{w + 2 * t}px;height:{h + 2 * t}px"
    origem = f"transform-origin:{t + w / 2:.1f}px {t}px"
    return (f'<div id="{prefixo}AbaAtras" style="{base};{origem};transform:scaleY(-1)">{aba}</div>'
            f'<div id="{prefixo}Meio" style="position:absolute;left:0;top:0;width:1080px;height:1920px">{meio}</div>'
            f'<div id="{prefixo}Corpo" style="{base}">{corpo}</div>'
            f'<div id="{prefixo}Rot" style="position:absolute;left:{x}px;top:{y + h * .58:.0f}px;width:{w}px;text-align:center">{rotulo}</div>'
            f'<div id="{prefixo}AbaFrente" style="{base};{origem};transform:scaleY(1);opacity:0">{aba}</div>')


# JavaScript: abre e fecha a aba. v = 1 (fechada) ... -1 (aberta); entre 0 e -1 a aba fica atrás, entre 0 e 1 na frente.
JS = r"""
function aba(p, v){ const atras = $(p+'AbaAtras'), frente = $(p+'AbaFrente');
  if (v < 0){ atras.style.opacity = 1; atras.style.transform = `scaleY(${v.toFixed(3)})`; frente.style.opacity = 0; }
  else { atras.style.opacity = 0; frente.style.opacity = 1; frente.style.transform = `scaleY(${Math.max(v, 0.001).toFixed(3)})`; } }
"""
