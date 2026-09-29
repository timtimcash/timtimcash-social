# -*- coding: utf-8 -*-
"""Stories do post institucional (1080x1920, 3 telas).

Área segura: 260px livres no topo e na base, onde o Instagram desenha a interface.
"""
import importlib.util, os
from artes import *

_aqui = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("inst", os.path.join(_aqui, "2026-09-29_institucional.py"))
inst = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(inst)

TAMANHO = (1080, 1920)

CSS_STORY = CSS.replace("html,body{width:1080px;height:1350px;overflow:hidden}", "html,body{width:1080px;height:1920px;overflow:hidden}") + """
.slide{height:1920px;padding:260px 92px 260px}
.topo{display:flex;align-items:center;gap:18px}
.rodape{font-size:30px;font-weight:600;text-align:center}
"""

def story(theme, body, rodape="", topo_marca=True):
    v = "color" if theme == "light" else "white"
    topo = f"<div class='topo'>{logo(v, 56)}{wordmark(v)}</div>" if topo_marca else ""
    fim = f"<div class='rodape' style='color:{'rgba(255,255,255,.85)' if theme == 'green' else MUTED}'>{rodape}</div>" if rodape else ""
    return f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS_STORY}</style></head><body><div class='slide {theme}'>{topo}<div class='body'>{body}</div>{fim}</div></body></html>"

CHECK = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'

def lista_funcoes():
    itens = ["Receitas, despesas e cartão", "Orçamentos com alerta", "Visão geral do mês", "Simulação do mês que vem",
             "Relatórios que explicam", "Investimentos lá fora", "Importação de planilhas", "Modo privacidade"]
    linhas = "".join(f"""<div style='display:flex;align-items:center;gap:26px;padding:17px 0;border-bottom:{'none' if i == len(itens) - 1 else '1px solid #efeee8'}'>
  <span style='flex:none;width:56px;height:56px;border-radius:50%;background:{BRAND};display:flex;align-items:center;justify-content:center'>{CHECK}</span>
  <span style='font-size:40px;font-weight:600;letter-spacing:-.01em'>{t}</span></div>""" for i, t in enumerate(itens))
    return f"<div class='card' style='margin-top:52px;padding:10px 44px'>{linhas}</div>"

def stories():
    s = []
    s.append(story("green", f"""
<div class='eyebrow'>Novo no feed</div>
<div class='h1' style='font-size:112px'>Seu dinheiro deixa pistas todos os dias.</div>
<div class='lead' style='color:rgba(255,255,255,.92);font-size:50px'>O timtimcash junta todas elas e conta a história inteira.</div>
{inst.v_pistas()}""", "Veja o carrossel completo no perfil"))
    s.append(story("light", f"""
<div class='eyebrow' style='margin-top:56px'>Tudo num lugar só</div>
<div class='h2' style='font-size:84px'>Oito jeitos de enxergar o seu dinheiro.</div>
{lista_funcoes()}""", "@timtimcashcom"))
    s.append(story("green", f"""
<div style='margin-bottom:56px'>{logo('white', 140)}</div>
<div class='h1' style='font-size:108px'>Seu dinheiro, com a clareza que ele merece.</div>
<div class='lead' style='color:rgba(255,255,255,.92);font-size:50px'>Gratuito para o controle financeiro. No computador ou no celular.</div>
<div style='margin-top:64px'><span class='pill' style='font-size:44px;padding:28px 48px'>timtimcash.com</span></div>""", "Link na bio do @timtimcashcom", topo_marca=False))
    return s

POSTS = {"2026-09-29_conheca-o-timtimcash_stories": stories}
