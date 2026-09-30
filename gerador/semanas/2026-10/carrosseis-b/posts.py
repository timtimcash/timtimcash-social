# -*- coding: utf-8 -*-
"""Carrosséis de 23/10/2026 ("Sua planilha vem junto") e 29/10/2026 ("Câmbio efetivo").

Modelo: gerador/semanas/2026-10-05_v2.py (capas capa_*, recorte, NOTA_TELA).
Telas reais novas, capturadas com carrosseis-b/app/captura_b.py na conta fictícia
(build 2026-09-30.1): ficam em saida/<pasta>/telas/ e entram aqui por caminho absoluto.

23/10: planilha de exemplo carrosseis-b/app/arquivos/minha-planilha-2025.csv (setembro de 2025,
antes do histórico da conta, com o salário de R$ 9.480 de antes do reajuste de março de 2026).
29/10: exemplo da pauta, conferido abaixo: US$ 4.000 a R$ 5,10 = R$ 20.400,00; IOF do comprovante
R$ 224,40; total debitado R$ 20.624,40; câmbio efetivo 20.624,40 ÷ 4.000 = R$ 5,1561.
"""
import os as _os
from decimal import Decimal as _D
from artes import *

O = "/tmp/claude-0/-home-claude-timtimcash-social/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/outubro"
TELAS_23 = O + "/saida/2026-10-23_sua-planilha-vem-junto/telas"
TELAS_29 = O + "/saida/2026-10-29_cambio-efetivo/telas"

# ---------------------------------------------------------------- conferência do exemplo de 29/10
ENVIADO_USD = _D("4000.00")
CAMBIO_OPERACAO = _D("5.10")
IOF = _D("224.40")
EM_REAIS = ENVIADO_USD * CAMBIO_OPERACAO
TOTAL = EM_REAIS + IOF
EFETIVO = TOTAL / ENVIADO_USD
IOF_POR_DOLAR = IOF / ENVIADO_USD
assert EM_REAIS == _D("20400.00")
assert TOTAL == _D("20624.40")
assert EFETIVO == _D("5.1561")
assert IOF_POR_DOLAR == _D("0.0561")
assert CAMBIO_OPERACAO + IOF_POR_DOLAR == EFETIVO

# ---------------------------------------------------------------- base visual (a mesma do modelo aprovado)
EXTRA = f"""<style>
.nota{{margin-top:18px;font-size:24px;font-weight:500;color:{MUTED}}}
.sombra{{box-shadow:0 1px 2px rgba(15,20,16,.05),0 22px 48px -22px rgba(15,20,16,.30)}}
.rot{{font-size:28px;font-weight:600;color:{MUTED}}}
.big{{font-weight:700;letter-spacing:-.04em;font-variant-numeric:tabular-nums;color:{INK}}}
</style>"""

NOTA_TELA = "<div class='nota' style='text-align:center'>Tela real do timtimcash, com dados de exemplo.</div>"

DARK_BG = INK
DARK_TEXTO = "#C9D1C8"
EXTRA_CAPA = f"""<style>
.dark{{background:{DARK_BG};color:#fff}}
.dark .count,.dark .foot{{color:{DARK_TEXTO}}}
.dark .eyebrow{{color:{MENTA}}}
.soft{{background:{SOFT};color:{INK}}}
.soft .count,.soft .foot{{color:{BRAND_DEEP}}}
.soft .eyebrow{{color:{BRAND_DEEP}}}
</style>"""

def capa_page(tema, corpo, idx, total, logo_var):
    head = f"<div class='head'><div class='brand'>{logo_horizontal(logo_var, 44)}</div><div class='count'>{idx}/{total}</div></div>"
    return page(EXTRA + EXTRA_CAPA + head + f"<div class='body'>{corpo}</div>" + footer(), tema)

def recorte(caminho, y0, y1, largura=760, x0=0, x1=None):
    """Recorte real de uma tela (caminho absoluto): mostra a faixa [y0, y1) x [x0, x1) em px da imagem original."""
    from PIL import Image
    w = Image.open(caminho).size[0]
    x1 = x1 or w
    esc = largura / (x1 - x0)
    alt = (y1 - y0) * esc
    return f"""<div class='sombra' style='width:{largura}px;height:{alt:.0f}px;overflow:hidden;border-radius:24px;background:#fff;border:1px solid {FIO};margin:0 auto'>
  <img src="file://{caminho}" style='display:block;width:{w * esc:.1f}px;height:auto;margin-top:{-y0 * esc:.1f}px;margin-left:{-x0 * esc:.1f}px'></div>"""

def css_px(v):
    """px CSS das capturas de celular (escala 3) para px da imagem."""
    return int(round(v * 3))

def icone(ip, tam=42, cor=BRAND_DARK, traco=2):
    return f"<svg width='{tam}' height='{tam}' viewBox='0 0 24 24' fill='none' stroke='{cor}' stroke-width='{traco}' stroke-linecap='round' stroke-linejoin='round'>{ip}</svg>"

def seta(tam=40, cor=MUTED):
    return icone('<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>', tam, cor, 2.2)

def item(ip, titulo, sub, ultimo=False):
    """Linha com ícone em azulejo, título e apoio (o mesmo desenho do modelo, post_susto)."""
    az = f"<div class='azulejo' style='width:84px;height:84px;flex:none'>{icone(ip)}</div>"
    return f"""<div style='display:flex;gap:30px;align-items:center;padding:30px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>{az}
  <div><div style='font-size:38px;font-weight:700;letter-spacing:-.03em;line-height:1.15'>{titulo}</div><div style='font-size:28px;color:{MUTED};margin-top:8px;line-height:1.3;text-wrap:balance'>{sub}</div></div></div>"""

MENOS = "−"  # sinal de menos para valores negativos

# ================================================================ sexta 23/10 · posicionamento e produto
# Planilha de exemplo (a mesma do arquivo importado nas telas reais): colunas na ordem da pessoa,
# diferente do modelo do site (data, categoria, descrição, conta/carteira, valor, pago).
PLANILHA = [
    ("02/09/2025", "Mercado da Vila", f"{MENOS}412,80", "Mercado"),
    ("05/09/2025", "Salário", "9.480,00", "Salário"),
    ("10/09/2025", "Aluguel", f"{MENOS}2.300,00", "Casa"),
    ("15/09/2025", "Academia", f"{MENOS}129,90", "Academia"),
]

def v_planilha_capa():
    """Ilustração: a planilha de sempre, com letras de coluna, números de linha, célula selecionada e abas por ano."""
    fio, cinza = "#E2E0D7", "#F2F1EB"
    larg = [54, 180, 250, 170, 168, 74]  # soma 896
    grade = "grid-template-columns:" + " ".join(f"{l}px" for l in larg)
    def cel(txt="", *, fundo="#fff", peso=400, cor=INK, alinhar="left", tam=25, extra=""):
        just = {"left": "flex-start", "right": "flex-end", "center": "center"}[alinhar]
        return (f"<div style='display:flex;align-items:center;justify-content:{just};padding:0 14px;background:{fundo};"
                f"border-right:1.5px solid {fio};border-bottom:1.5px solid {fio};font-size:{tam}px;font-weight:{peso};color:{cor};"
                f"white-space:nowrap;font-variant-numeric:tabular-nums;letter-spacing:-.01em;{extra}'>{txt}</div>")
    letras = cel(fundo=cinza) + "".join(cel(l, fundo=cinza, peso=600, cor=MUTED, alinhar="center", tam=20) for l in "ABCDE")
    linhas = [letras]
    cab = cel("1", fundo=cinza, peso=600, cor=MUTED, alinhar="center", tam=20)
    cab += cel("Data", peso=700) + cel("Descrição", peso=700) + cel("Valor", peso=700, alinhar="right") + cel("Categoria", peso=700) + cel()
    linhas.append(cab)
    for i, (d, desc, v, cat) in enumerate(PLANILHA, 2):
        sel = "box-shadow:inset 0 0 0 3px " + BRAND + ";position:relative" if desc == "Salário" else ""
        alca = f"<i style='position:absolute;right:-6px;bottom:-6px;width:11px;height:11px;background:{BRAND};border:2px solid #fff;display:block'></i>" if sel else ""
        linha = cel(str(i), fundo=cinza, peso=600, cor=MUTED, alinhar="center", tam=20)
        linha += cel(d) + cel(desc) + cel(v + alca, alinhar="right", extra=sel) + cel(cat) + cel()
        linhas.append(linha)
    linhas.append(cel("6", fundo=cinza, peso=600, cor=MUTED, alinhar="center", tam=20) + "".join(cel() for _ in range(5)))
    alturas = "grid-template-rows:44px " + " ".join(["60px"] * (len(linhas) - 1))
    def aba(ano, ativa=False):
        if ativa:
            return (f"<div style='height:100%;display:flex;align-items:center;padding:0 26px;background:#fff;color:{BRAND_DARK};font-size:23px;"
                    f"font-weight:700;box-shadow:inset 0 -4px 0 {BRAND}'>{ano}</div>")
        return f"<div style='height:100%;display:flex;align-items:center;padding:0 26px;color:{MUTED};font-size:23px;font-weight:600'>{ano}</div>"
    abas = f"<div style='height:58px;display:flex;align-items:stretch;background:{cinza};padding-left:54px'>{aba('2023')}{aba('2024')}{aba('2025', True)}</div>"
    return f"""<div style='margin-top:64px;border-radius:26px;overflow:hidden;background:#fff;box-shadow:0 2px 4px rgba(4,47,33,.10),0 44px 80px -36px rgba(4,47,33,.60)'>
  <div style='display:grid;{grade};{alturas}'>{''.join(linhas)}</div>{abas}</div>"""

def capa_planilha(T):
    corpo = f"""<div class='eyebrow'>Importar planilha</div>
<div class='h1' style='font-size:118px'>Sua planilha vem junto.</div>
{v_planilha_capa()}"""
    return capa_page("green", corpo, 1, T, "white")

def v_sinal():
    """Ilustração: o que cada linha da planilha vira na importação."""
    def linha(rotulo, valor, chip, fundo, cor, ultimo=False):
        return f"""<div style='display:flex;align-items:center;gap:26px;padding:30px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div style='width:330px;flex:none'><div class='rot' style='font-size:26px'>{rotulo}</div><div class='big' style='font-size:54px;margin-top:4px'>{valor}</div></div>
  <div style='flex:none'>{seta(44)}</div>
  <div style='margin-left:auto;display:inline-flex;align-items:center;height:72px;padding:0 30px;border-radius:999px;background:{fundo};color:{cor};font-size:32px;font-weight:700;white-space:nowrap'>{chip}</div></div>"""
    return f"""<div class='visual' style='margin-top:48px'><div class='card' style='padding:6px 44px'>
  {linha('valor', '9.480,00', 'receita', SOFT, BRAND_DEEP)}
  {linha('valor', f'{MENOS}2.300,00', 'despesa', '#FBEAEA', RED_TEXT)}
  {linha('categoria nova', 'Academia', 'criada ao importar', '#F2F1EB', INK, True)}
</div><div class='nota'>Exemplo com linhas da planilha da capa.</div></div>"""

def post_planilha():
    T = 7
    s = []
    s.append(capa_planilha(T))

    imp = TELAS_23 + "/celular-importar-planilha.png"
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Para quem vive de planilha</div>
<div class='h3'>Sem recomeçar do zero.</div>
<div class='p' style='margin-top:20px;font-size:36px'>Em Importar, a aba Planilha recebe arquivos .xlsx, .xls e .csv. O formato é detectado sozinho.</div>
<div class='visual' style='margin-top:40px'>{recorte(imp, css_px(629), css_px(1038), largura=520, x0=30, x1=1140)}{NOTA_TELA}</div>""", 2, T))

    fmt = TELAS_23 + "/celular-importar-formato.png"
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Formato esperado</div>
<div class='h3'>Seis colunas, na ordem que você quiser.</div>
<div class='p' style='margin-top:20px;font-size:36px'>Data, categoria, descrição, conta ou carteira, valor e pago, reconhecidas pelo nome do cabeçalho.</div>
<div class='visual' style='margin-top:40px'>{recorte(fmt, css_px(336.5), css_px(719.5), largura=500, x0=30, x1=1140)}{NOTA_TELA}</div>""", 3, T))

    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Receita ou despesa</div>
<div class='h2'>O sinal do valor decide.</div>
<div class='p'>Positivo entra como receita; negativo, como despesa. Categoria ou conta que ainda não existe é criada na importação.</div>
{v_sinal()}""", 4, T))

    rev = TELAS_23 + "/celular-revisar-importacao.png"
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Revisar importação</div>
<div class='h3'>Você revisa cada linha.</div>
<div class='visual' style='margin-top:40px'>{recorte(rev, css_px(57), css_px(646), largura=470, x0=30, x1=1140)}{NOTA_TELA}</div>""", 5, T))

    I_ALVO = '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>'
    I_BARRAS = '<path d="M4 20h16"/><path d="M7 16v-4"/><path d="M12 16V7"/><path d="M17 16v-7"/>'
    I_TENDE = '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>'
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Com o histórico dentro</div>
<div class='h2'>Seus anos de planilha viram ponto de partida.</div>
<div class='visual' style='margin-top:48px'><div class='card' style='padding:6px 44px'>
  {item(I_ALVO, 'Orçamentos', 'O limite sugerido vem da sua média dos últimos 12 meses.')}
  {item(I_BARRAS, 'Visão geral', 'Receitas e despesas contra a sua média, a partir de 3 meses de histórico.')}
  {item(I_TENDE, 'Simulação futura', '“Preencher com média” usa de 3 a 24 meses do seu histórico.', True)}
</div></div>""", 6, T))

    s.append(slide("green", EXTRA + f"""
<div class='h2'>Sua planilha vem junto.<br>E continua sua.</div>
<div class='lead'>Importar no timtimcash. Gratuito para o controle financeiro, no computador ou no celular.</div>{v_cta_pill()}""", 7, T))
    return s

# ================================================================ quinta 29/10 · educação (exterior)
def brl(v, casas=2):
    """R$ no formato brasileiro, a partir de Decimal."""
    q = _D(1).scaleb(-casas)
    s = f"{v.quantize(q):,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

assert brl(TOTAL) == "20.624,40" and brl(EFETIVO, 4) == "5,1561" and brl(IOF_POR_DOLAR, 4) == "0,0561" and brl(EM_REAIS) == "20.400,00"

def capa_efetivo(T):
    card = f"""<div style='margin-top:64px;background:#fff;border-radius:32px;padding:40px 52px 50px;box-shadow:0 1px 2px rgba(6,95,70,.06),0 30px 60px -34px rgba(6,95,70,.45)'>
  <div style='display:flex;align-items:baseline;justify-content:space-between;gap:20px'>
    <div class='rot' style='font-size:30px'>câmbio da operação</div>
    <div class='big' style='font-size:68px;color:{MUTED}'>R$ {brl(CAMBIO_OPERACAO)}</div>
  </div>
  <div style='display:flex;align-items:center;gap:22px;margin:26px 0 30px'>
    <div style='flex:1;height:2px;background:{FIO}'></div>
    <div style='display:inline-flex;align-items:center;height:56px;padding:0 26px;border-radius:999px;background:{SOFT};color:{BRAND_DEEP};font-size:27px;font-weight:700;white-space:nowrap'>+ IOF do comprovante</div>
    <div style='flex:1;height:2px;background:{FIO}'></div>
  </div>
  <div style='font-size:30px;font-weight:700;color:{BRAND_DEEP}'>câmbio efetivo</div>
  <div class='big' style='font-size:160px;line-height:1;margin-top:14px;color:{BRAND_DARK};letter-spacing:-.05em;white-space:nowrap'>R$ {brl(EFETIVO, 4)}</div>
</div>"""
    corpo = f"""<div class='eyebrow'>Câmbio efetivo</div>
<div class='h1' style='font-size:100px'>O câmbio que você pagou de verdade.</div>
{card}"""
    return capa_page("soft", corpo, 1, T, "color")

def post_efetivo():
    T = 6
    s = []
    s.append(capa_efetivo(T))

    def linha(rot, val, forte=False, ultimo=False):
        return f"""<div style='display:flex;align-items:baseline;justify-content:space-between;gap:20px;padding:17px 0;{'' if ultimo else f'border-bottom:2px solid {FIO};'}'>
  <div style='font-size:{34 if forte else 32}px;font-weight:{700 if forte else 500};color:{INK if forte else MUTED};line-height:1.2'>{rot}</div>
  <div class='big' style='font-size:{52 if forte else 42}px;flex:none'>{val}</div></div>"""
    comprovante = f"""<div class='visual' style='margin-top:44px'><div class='card' style='padding:10px 48px 14px'>
  {linha('Valor enviado', f'US$ {brl(ENVIADO_USD)}')}
  {linha('Câmbio da operação', f'R$ {brl(CAMBIO_OPERACAO)}')}
  {linha('Valor em reais', f'R$ {brl(EM_REAIS)}')}
  {linha('IOF (o que está no comprovante)', f'R$ {brl(IOF)}')}
  {linha('Total debitado', f'R$ {brl(TOTAL)}', forte=True, ultimo=True)}
</div><div class='nota'>Exemplo de uma remessa, sem tarifa.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Cotação não é custo</div>
<div class='h2'>O câmbio da operação não é o custo final.</div>
<div class='p'>O que sai da sua conta em reais inclui o IOF e, se houver, a tarifa.</div>{comprovante}""", 2, T))

    conta = f"""<div class='visual' style='margin-top:48px'><div class='card' style='padding:18px 48px 34px'>
  <div style='display:flex;align-items:baseline;justify-content:space-between;padding:20px 0;border-bottom:2px solid {FIO}'>
    <div class='rot' style='font-size:32px'>Total debitado</div><div class='big' style='font-size:58px'>R$ {brl(TOTAL)}</div></div>
  <div style='display:flex;align-items:baseline;justify-content:space-between;padding:20px 0;border-bottom:2px solid {FIO}'>
    <div class='rot' style='font-size:32px'><span style='color:{INK};font-weight:700;font-size:40px;margin-right:6px'>÷</span> Valor enviado</div><div class='big' style='font-size:58px'>US$ {brl(ENVIADO_USD, 0)}</div></div>
  <div style='display:flex;align-items:center;justify-content:space-between;padding-top:24px'>
    <div style='font-size:34px;font-weight:700;color:{INK}'>Câmbio efetivo</div><div class='big' style='font-size:92px;color:{BRAND_DARK}'>R$ {brl(EFETIVO, 4)}</div></div>
</div>
<div style='display:flex;align-items:center;justify-content:center;gap:18px;margin-top:30px;font-size:30px;font-weight:600;color:{MUTED};white-space:nowrap'>
  <span>por dólar:</span>
  <span style='background:#fff;border:2px solid {FIO};border-radius:999px;padding:12px 24px;color:{INK}'>R$ {brl(CAMBIO_OPERACAO)} de câmbio</span>
  <span style='color:{INK};font-weight:700'>+</span>
  <span style='background:{SOFT};border-radius:999px;padding:14px 26px;color:{BRAND_DEEP};font-weight:700'>R$ {brl(IOF_POR_DOLAR, 4)} de IOF</span>
</div>
<div class='nota' style='text-align:center'>Exemplo: US$ 4.000 a R$ 5,10, com o IOF de R$ 224,40 do comprovante.</div></div>"""
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>A conta</div>
<div class='h3'>Total debitado em reais, dividido pelo valor enviado.</div>{conta}""", 3, T))

    I_RESULT = '<path d="M4 20h16"/><path d="M5 15l4-4 3 3 7-7"/><path d="M15 7h4v4"/>'
    I_TROCA = '<path d="M5 8h13"/><path d="M15 5l3 3-3 3"/><path d="M19 16H6"/><path d="M9 13l-3 3 3 3"/>'
    I_BANCO = '<path d="M12 3.5 20.5 8h-17z"/><path d="M5 11v6.5M9.7 11v6.5M14.3 11v6.5M19 11v6.5"/><path d="M3.5 20.5h17"/>'
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Por que importa</div>
<div class='h2'>É o efetivo que mede o seu custo.</div>
<div class='visual' style='margin-top:48px'><div class='card' style='padding:6px 44px'>
  {item(I_RESULT, 'Resultado em reais', 'O ganho se mede contra o que saiu da conta. Pela cotação, o do exemplo pareceria R$ 224,40 maior.')}
  {item(I_TROCA, 'Comparar remessas', 'Datas e instituições diferentes se comparam pelo efetivo, com IOF e tarifa dentro.')}
  {item(I_BANCO, 'Tem nome no Banco Central', 'VET, o Valor Efetivo Total: o custo em reais por unidade de moeda, com câmbio, tarifas e tributos.', True)}
</div></div>""", 4, T))

    nr = TELAS_29 + "/celular-nova-remessa-preenchida.png"
    s.append(slide("light", EXTRA + f"""
<div class='eyebrow'>Remessas ao exterior</div>
<div class='h3'>A Nova remessa faz essa conta na hora.</div>
<div class='p' style='margin-top:20px;font-size:36px'>Você informa o total em reais, o valor enviado e o IOF do comprovante.</div>
<div class='visual' style='margin-top:40px'>{recorte(nr, css_px(690), css_px(993), largura=640, x0=36, x1=1134)}{NOTA_TELA}</div>""", 5, T))

    s.append(slide("green", EXTRA + f"""
<div class='h2'>Saiba quanto cada dólar custou de verdade.</div>
<div class='lead'>Remessas ao exterior no timtimcash. No computador ou no celular.</div>{v_cta_pill()}""", 6, T))
    return s

POSTS = {
    "2026-10-23_sua-planilha-vem-junto": post_planilha,
    "2026-10-29_cambio-efetivo": post_efetivo,
}
