# -*- coding: utf-8 -*-
"""Semana piloto: 5 a 9 de outubro de 2026 (publicada)."""
from artes import *


def post1():
    T = 6
    s = []
    s.append(slide("green", f"""
<div class='eyebrow'>Orçamento</div>
<div class='h1'>Seu orçamento está furado?</div>
<div class='lead'>3 sinais que quase ninguém percebe.</div>""", 1, T, extra="<div class='bigwater'>3</div>"))
    s.append(slide("light", f"""
<div class='eyebrow'>Sinal 1 de 3</div>
<div class='h2'>O mês acaba antes do salário.</div>
<div class='p'>Você sabe quanto ganha, mas não sabe para onde foi.</div>{v_month_bar()}""", 2, T))
    s.append(slide("light", f"""
<div class='eyebrow'>Sinal 2 de 3</div>
<div class='h2'>A fatura do cartão sempre assusta.</div>
<div class='p'>Se o valor é surpresa, os gastos não estão sendo acompanhados.</div>{v_fatura()}""", 3, T))
    s.append(slide("light", f"""
<div class='eyebrow'>Sinal 3 de 3</div>
<div class='h2'>Gasto pequeno não entra na conta.</div>
<div class='p'>Café, delivery, assinatura. Somados, viram uma categoria inteira.</div>{v_chips()}""", 4, T))
    s.append(slide("light", f"""
<div class='eyebrow'>O primeiro passo</div>
<div class='h2'>Registrar tudo por 30 dias, separado por categoria.</div>
<div class='p'>O padrão aparece sozinho.</div>{v_grid30()}""", 5, T))
    s.append(slide("green", f"""
<div class='h2'>No timtimcash você enxerga isso em um lugar só.</div>
<div class='lead'>Gratuito, no computador ou no celular.</div>{v_cta_pill()}""", 6, T))
    return s

def post2():
    T = 6
    s = []
    s.append(slide("green", f"""
<div class='eyebrow'>Remessas internacionais</div>
<div class='lead' style='margin-top:0;margin-bottom:28px'>Você manda dinheiro para fora.</div>
<div class='h1'>Mas sabe quanto ele está rendendo?</div>{v_fx_cover()}""", 1, T))
    s.append(slide("light", f"""
<div class='eyebrow'>O problema</div>
<div class='h2'>Câmbio variando, remessas em datas diferentes.</div>
<div class='p'>Fazer essa conta na mão é difícil.</div>{v_fx_line()}""", 2, T))
    s.append(slide("light", f"""
<div class='eyebrow'>Como funciona</div>
<div class='h3'>No timtimcash você registra cada remessa e o saldo de fechamento lá fora.</div>{v_rows()}""", 3, T))
    s.append(slide("light", f"""
<div class='eyebrow'>Rendimento ano a ano</div>
<div class='h3'>O site calcula o rendimento ano a ano, considerando a data de cada remessa.</div>{v_years()}""", 4, T))
    s.append(slide("light", f"""
<div class='eyebrow'>Duas moedas</div>
<div class='h2'>Em dólar e em real,</div>
<div class='p'>com a cotação PTAX do Banco Central buscada automaticamente.</div>{v_ptax()}""", 5, T))
    s.append(slide("green", f"""
<div class='h2'>Remessas internacionais no timtimcash.</div>
<div class='lead'>Gratuito, no computador ou no celular.</div>{v_cta_pill()}""", 6, T))
    return s

def post3():
    line = lambda t, last=False: f"<div style='padding:34px 0;border-bottom:{'none' if last else '2px solid ' + FIO};display:flex;align-items:center;gap:30px'><span style='flex:none;width:22px;height:22px;border-radius:50%;background:{BRAND}'></span><span class='h2' style='font-size:66px;white-space:nowrap'>{t}</span></div>"
    body = f"""
<div>{line('Sem propaganda.')}{line('Sem conexão com o banco.')}{line('Sem custo.', True)}</div>
<div class='lead accent' style='margin-top:56px;font-weight:700;font-size:52px'>Seus dados continuam seus.</div>"""
    return [slide("light", body, single=True)]

POSTS = {
    "2026-10-05_orcamento-furado": post1,
    "2026-10-07_remessas-exterior": post2,
    "2026-10-09_sem-propaganda": post3,
}
