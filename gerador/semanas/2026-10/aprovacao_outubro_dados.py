# -*- coding: utf-8 -*-
"""Outubro de 2026 inteiro para aprovação: 13 posts novos ($O/dados) e os 7 já agendados (repositório)."""
import glob, importlib.util, os

O = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/claude/timtimcash-social"
POSTS_REPO = os.path.join(REPO, "posts")
FUSO = "horário de Brasília (America/Sao_Paulo, UTC−3)"

def _mod(caminho):
    s = importlib.util.spec_from_file_location("m" + str(abs(hash(caminho))), caminho)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m

CURTOS = {
    "2026-10-02_rendeu-em-dolar-e-em-reais": "Rendeu 10% em dólar. E em reais?",
    "2026-10-03_outubro-comecou": "Outubro começou",
    "2026-10-05_quanto-fica-com-voce": "Quanto do salário fica com você",
    "2026-10-06_reel-o-timtimcash-em-20-segundos": "O timtimcash em 20 segundos",
    "2026-10-07_cambio-de-equilibrio": "Câmbio de equilíbrio",
    "2026-10-08_reel-extrato-com-categoria-sugerida": "Extrato já com as categorias",
    "2026-10-09_seus-dados-entram-e-saem-com-voce": "Seus dados entram e saem com você",
    "2026-10-06_orcamento-pela-sua-media": "Orçamento pela sua média",
    "2026-10-14_reel-rendimento-ano-a-ano": "Rendimento ano a ano",
    "2026-10-15_reserva-em-meses": "Reserva em meses",
    "2026-10-16_reel-quanto-vai-para-o-mercado": "Quanto vai para o mercado",
    "2026-10-19_cartao-fechamento-e-vencimento": "Cartão: o melhor dia de compra",
    "2026-10-20_reel-o-que-vence-esta-semana": "O que vence esta semana",
    "2026-10-08_e-se-a-maior-renda-parar": "E se a maior renda parar",
    "2026-10-22_reel-ritmo-do-retorno": "Rendeu 11,8%. Em quanto tempo?",
    "2026-10-23_sua-planilha-vem-junto": "Sua planilha vem junto",
    "2026-10-26_parcela-que-cabe-hoje": "A parcela cabe hoje?",
    "2026-10-27_reel-ocultar-valores": "Ocultar valores",
    "2026-10-29_cambio-efetivo": "Câmbio efetivo",
    "2026-10-30_reel-13-salario": "O 13º vem aí",
}

# ---------------------------------------------------------------- já agendados (repositório)
existentes = []
leg = _mod(os.path.join(REPO, "gerador/semanas/2026-09-30_legendas.py"))
v2 = _mod(os.path.join(REPO, "gerador/semanas/2026-10-05_v2_dados.py"))
for p in leg.POSTS + v2.POSTS:
    if not p["pasta"].startswith("2026-10-"):
        continue
    q = {k: v for k, v in p.items() if not k.startswith("grade")}
    q.update(tipo="carrossel", imagens_dir=POSTS_REPO, status_tipo="mantem", status_atual="Já agendado · mantém a data")
    if p["pasta"] == "2026-10-06_orcamento-pela-sua-media":
        q.update(data_longa="terça-feira, 13 de outubro de 2026", data_curta="terça-feira, 13/10/2026", data_mockup="13 de outubro",
                 iso="2026-10-13T10:00:00", status_tipo="muda", status_atual="Já agendado · muda de 06/10 para 13/10")
    if p["pasta"] == "2026-10-08_e-se-a-maior-renda-parar":
        q.update(data_longa="quarta-feira, 21 de outubro de 2026", data_curta="quarta-feira, 21/10/2026", data_mockup="21 de outubro",
                 iso="2026-10-21T10:00:00", status_tipo="muda", status_atual="Já agendado · muda de 08/10 para 21/10")
    q.setdefault("iso", {"2026-10-02_rendeu-em-dolar-e-em-reais": "2026-10-02T10:00:00",
                         "2026-10-03_outubro-comecou": "2026-10-03T10:00:00"}.get(p["pasta"], ""))
    existentes.append(q)

# ---------------------------------------------------------------- novos ($O/dados)
novos = []
for arq in sorted(glob.glob(os.path.join(O, "dados", "*.py"))):
    p = dict(_mod(arq).POST)
    p.update(status_tipo="novo", status_atual="Novo")
    if p["tipo"] == "reel":
        for c in ("video", "capa", "previa"):
            p[c] = os.path.join(O, p[c])
    else:
        p["imagens_dir"] = os.path.join(O, "saida")
    novos.append(p)

POSTS = sorted(existentes + novos, key=lambda p: p["iso"])
for i, p in enumerate(POSTS, 1):
    p["n"] = i
    p["titulo_curto"] = CURTOS[p["pasta"]]
assert len(POSTS) == 20, len(POSTS)
assert sum(p["tipo"] == "reel" for p in POSTS) == 8

def _capa(p):
    return p["capa"] if p["tipo"] == "reel" else os.path.join(p["imagens_dir"], p["pasta"], "01.jpg")

itens = [("fixado", os.path.join(POSTS_REPO, "2026-09-30_comece-por-aqui/01.jpg"), "fixado")]
itens += [(p["data_curta"].split(", ")[1][:5], _capa(p), p["tipo"]) for p in reversed(POSTS)]
itens += [("30/09", os.path.join(POSTS_REPO, "2026-09-30_reel-salario-6-meses/capa.jpg"), "reel"),
          ("30/09", os.path.join(POSTS_REPO, "2026-09-30_hoje-o-mes-fecha/01.jpg"), "carrossel"),
          ("29/09", os.path.join(POSTS_REPO, "2026-09-29_conheca-o-timtimcash/01.jpg"), "carrossel")]

fontes, vistos = [], set()
for t, u in ([("Metricool · Diferenças entre os planos Free e Premium (até 20 publicações por mês)",
               "https://help.metricool.com/pt/article/principais-diferencas-entre-os-planos-free-e-premium-1l9y9oj/")]
             + [f for p in novos for f in p.get("fontes", [])]):
    if u not in vistos:
        vistos.add(u); fontes.append((t, u))

CONFIG = {
    "titulo_pagina": "Outubro no Instagram · timtimcash",
    "eyebrow": "Proposta para aprovação · enviada em 30/09/2026",
    "h1": "Outubro inteiro: 20 posts, 8 Reels",
    "sub": "Os 13 posts novos e os 7 que já estavam agendados, na ordem do mês, com o calendário e a prévia da grade do perfil. Nada novo é agendado antes da sua resposta.",
    "chave": "timtimcash-aprovacao-outubro-2026-v1",
    "resumo_titulo": "Avaliação dos posts de outubro de 2026 do timtimcash (proposta de 30/09/2026)",
    "largura_imagens": 720,
    "aprovar_todos": True,
    "notas": [
        ("Como avaliar", "Marque Aprovado, Reprovado ou Solicitar alteração em cada post e escreva o que quiser mudar. O botão “Aprovar todos os pendentes”, na barra do topo, marca de uma vez os que você ainda não avaliou. No fim, copie a avaliação e cole na conversa."),
        ("20 posts, não 22", "O Metricool gratuito publica até 20 posts por mês. Com os de 02 e 03/10, sobram 18: duas semanas com 5 posts e duas com 4, sem o feriado de 12/10 e sem a quarta 28/10. Todos às 10h, o melhor horário de todos os dias no Metricool."),
        ("Os 8 Reels", "Nunca dois seguidos. Aqui os vídeos estão em qualidade reduzida e sem som, para o arquivo ficar leve; o que vai ao ar é 1080 × 1920. Vão sem música: se quiser trilha, me mande um arquivo livre de direitos. Cada Reel tem capa própria na grade."),
        ("Duas mudanças de data", "“Orçamento pela sua média” sai de 06/10 para 13/10, e “E se a maior renda parar” sai de 08/10 para 21/10, três semanas depois do Reel de 30/09, que usa o mesmo teste. Os outros cinco já agendados ficam como estão."),
        ("Capas", "Os fundos alternam entre papel, tinta, verde suave e verde, com no máximo uma capa verde por semana e nunca duas iguais lado a lado. As capas de 02 e 03/10 são do modelo anterior. O post fixado também é verde: no dia em que um post de capa verde é o mais recente, os dois ficam lado a lado no topo da grade até o post seguinte. Se preferir evitar, troco as capas verdes de 06, 16, 23 e 30/10 por tinta ou verde suave."),
        ("Telas reais", "Todos os posts de produto usam telas reais do site numa conta fictícia, com o aviso “Tela real do timtimcash, com dados de exemplo”. No Reel de 14/10, o câmbio do fim de cada ano é a PTAX real."),
    ],
    "fontes": fontes,
    "grade_mes": {"titulo": "Prévia da grade do perfil", "legenda": "Como o perfil fica em 31/10",
                  "nota": "A grade mostra as capas em 3:4. O post fixado (“Comece por aqui”) fica no topo; o ícone de play marca os Reels.",
                  "itens": itens},
}
