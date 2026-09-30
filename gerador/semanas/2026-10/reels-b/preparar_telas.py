# -*- coding: utf-8 -*-
"""Copia as telas capturadas (app/importar, app/pendentes, app/capas) para $O/saida/<pasta>/telas/
em JPEG, com nomes que dizem o que cada uma mostra. Os Reels leem as telas dessas pastas,
então o que vai para o repositório é exatamente o que aparece nos vídeos."""
import os
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
O = os.path.dirname(AQUI)
APP = os.path.join(AQUI, "app")
P08 = os.path.join(O, "saida", "2026-10-08_reel-extrato-com-categoria-sugerida", "telas")
P20 = os.path.join(O, "saida", "2026-10-20_reel-o-que-vence-esta-semana", "telas")

TELAS = [
    (P08, "importar/a_importar_ofx.png", "celular-importar-1-extrato-ofx.jpg", None),
    (P08, "importar/b_conta_destino.png", "celular-importar-2-conta-de-destino.jpg", None),
    (P08, "importar/c_revisar.png", "celular-importar-3-revisar-importacao.jpg", None),
    (P08, "importar/d_seletor.png", "celular-importar-4-trocar-categoria.jpg", None),
    (P08, "importar/e_cartao.png", "celular-importar-5-automatizar-esta-categoria.jpg", None),
    (P08, "importar/f_regra_salva.png", "celular-importar-6-regra-salva.jpg", None),
    (P08, "importar/i_de_novo.png", "celular-importar-7-mesmo-extrato-de-novo.jpg", None),
    # coluna "Categoria" da revisão no computador (escala 4), sem as bordas das colunas vizinhas
    (P08, "capas/importar-categorias.png", "computador-importar-categorias-sugeridas.jpg", (32, 0, 1040, 912)),
    (P20, "pendentes/01_antes.png", "celular-pendentes-antes.jpg", None),
    (P20, "pendentes/02_depois.png", "celular-pendentes-depois.jpg", None),
    (P20, "capas/pendentes-indicadores.png", "celular-pendentes-indicadores.jpg", None),
]

for pasta, orig, nome, corte in TELAS:
    os.makedirs(pasta, exist_ok=True)
    im = Image.open(os.path.join(APP, orig)).convert("RGB")
    if corte:
        im = im.crop(corte)
    im.save(os.path.join(pasta, nome), "JPEG", quality=93, optimize=True)
    print(nome, im.size)
