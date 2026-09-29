# -*- coding: utf-8 -*-
"""Biblioteca visual das artes do Instagram do timtimcash (1080x1350, 4:5).

Uso:  python3 gerador/render.py gerador/semanas/AAAA-MM-DD.py
Cada arquivo de semana define POSTS = {"AAAA-MM-DD_slug": funcao_que_retorna_lista_de_html}.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("INTER_TTF_DIR", "/tmp/inter/extras/ttf")

BRAND = "#059669"
BRAND_DARK = "#047857"
BG = "#fbfaf6"
INK = "#111827"
MUTED = "#5b6472"
SOFT = "#e6f4ee"

HANDLE = "@timtimcashcom"
SITE = "timtimcash.com"

# ---------------------------------------------------------------- marca
def logo(variant="color", size=64):
    if variant == "color":
        eye, dollar, smile = BRAND, "#ffffff", BRAND
    else:
        eye, dollar, smile = "#ffffff", BRAND, "#ffffff"
    w = size * 228 / 142
    return f'''<svg class="logo" width="{w:.0f}" height="{size}" viewBox="14 54 228 142" xmlns="http://www.w3.org/2000/svg" fill="none" aria-label="timtimcash">
<circle cx="80" cy="80" r="22" fill="{eye}"/><text x="80" y="80" text-anchor="middle" dominant-baseline="central" font-size="34" font-weight="800" fill="{dollar}" font-family="Inter">$</text>
<circle cx="176" cy="80" r="22" fill="{eye}"/><text x="176" y="80" text-anchor="middle" dominant-baseline="central" font-size="34" font-weight="800" fill="{dollar}" font-family="Inter">$</text>
<path d="M 30 130 Q 128 230 226 130" stroke="{smile}" stroke-width="24" stroke-linecap="round" fill="none"/></svg>'''

def wordmark(variant="color"):
    a = INK if variant == "color" else "#ffffff"
    b = BRAND if variant == "color" else "#bff0dc"
    return f'<span class="wm"><span style="color:{a}">timtim</span><span style="color:{b}">cash</span></span>'

ARROW = '''<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>'''

# ---------------------------------------------------------------- CSS base
def font_faces():
    faces = []
    for w, f in [(400, "Regular"), (500, "Medium"), (600, "SemiBold"), (700, "Bold"), (800, "ExtraBold")]:
        faces.append(f"@font-face{{font-family:'Inter';font-weight:{w};src:url('file://{FONT_DIR}/Inter-{f}.ttf') format('truetype');}}")
    return "\n".join(faces)

CSS = f"""
{font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;font-feature-settings:'cv11','ss01'}}
.slide{{position:relative;width:1080px;height:1350px;padding:84px 92px;display:flex;flex-direction:column}}
.light{{background:{BG};color:{INK}}}
.green{{background:{BRAND};color:#fff}}
.head{{display:flex;align-items:center;justify-content:space-between;height:64px}}
.brand{{display:flex;align-items:center;gap:18px}}
.wm{{font-weight:800;font-size:38px;letter-spacing:-.02em}}
.count{{font-size:26px;font-weight:600;letter-spacing:.02em;color:{MUTED};font-variant-numeric:tabular-nums}}
.green .count{{color:rgba(255,255,255,.78)}}
.body{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.foot{{display:flex;align-items:center;justify-content:space-between;height:40px;font-size:26px;font-weight:600;color:{MUTED}}}
.green .foot{{color:rgba(255,255,255,.82)}}
.swipe{{display:flex;align-items:center;gap:10px}}
.eyebrow{{font-size:26px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:{BRAND_DARK};margin-bottom:34px}}
.green .eyebrow{{color:#c9f2e0}}
.h1,.h2,.h3,.lead,.p{{text-wrap:balance}}
.h1{{font-size:108px;line-height:1.02;font-weight:800;letter-spacing:-.045em}}
.h2{{font-size:84px;line-height:1.05;font-weight:800;letter-spacing:-.04em}}
.h3{{font-size:66px;line-height:1.08;font-weight:800;letter-spacing:-.035em}}
.lead{{font-size:46px;line-height:1.25;font-weight:500;letter-spacing:-.02em;margin-top:36px}}
.p{{font-size:40px;line-height:1.35;font-weight:400;color:{MUTED};margin-top:34px;letter-spacing:-.01em}}
.green .p{{color:rgba(255,255,255,.88)}}
.accent{{color:{BRAND}}}
.visual{{margin-top:64px}}
.pill{{display:inline-flex;align-items:center;gap:14px;background:#fff;color:{BRAND_DARK};font-weight:800;font-size:38px;padding:24px 40px;border-radius:999px;letter-spacing:-.01em}}
.chip{{display:inline-flex;align-items:center;height:76px;padding:0 34px;border-radius:999px;background:#fff;border:2px solid #e5e7e1;font-size:34px;font-weight:600;color:{INK}}}
.card{{background:#fff;border-radius:32px;box-shadow:0 1px 0 rgba(17,24,39,.04),0 18px 40px -18px rgba(17,24,39,.18);border:1px solid #ecebe4}}
.sk{{height:18px;border-radius:9px;background:#e8e8e1}}
.bigwater{{position:absolute;right:-30px;bottom:-270px;font-size:760px;font-weight:800;letter-spacing:-.06em;line-height:1;color:rgba(255,255,255,.10);pointer-events:none}}
"""

def page(inner, theme="light"):
    return f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='slide {theme}'>{inner}</div></body></html>"

def header(theme, idx=None, total=None):
    v = "color" if theme == "light" else "white"
    right = f"<div class='count'>{idx}/{total}</div>" if idx else ""
    return f"<div class='head'><div class='brand'>{logo(v, 52)}{wordmark(v)}</div>{right}</div>"

def footer(last=False, single=False):
    if single or last:
        right = f"<span>{SITE}</span>"
    else:
        right = f"<span class='swipe'>Arraste {ARROW}</span>"
    return f"<div class='foot'><span>{HANDLE}</span>{right}</div>"

def slide(theme, body, idx=None, total=None, single=False, extra=""):
    last = idx is not None and idx == total
    return page(extra + header(theme, idx, total) + f"<div class='body'>{body}</div>" + footer(last=last, single=single), theme)

# ---------------------------------------------------------------- visuais
def v_month_bar():
    return f"""<div class='visual'>
  <div style='position:relative;height:26px;border-radius:13px;background:#e8e8e1;overflow:hidden'>
    <div style='position:absolute;left:0;top:0;bottom:0;width:63%;background:{BRAND};border-radius:13px'></div>
  </div>
  <div style='position:relative;margin-top:22px;height:40px;font-size:28px;font-weight:600;color:{MUTED}'>
    <span style='position:absolute;left:0'>dia 1</span>
    <span style='position:absolute;left:63%;transform:translateX(-50%);color:{BRAND_DARK}'>acabou</span>
    <span style='position:absolute;right:0'>dia 30</span>
  </div>
</div>"""

def v_fatura():
    return f"""<div class='visual'><div class='card' style='padding:44px 48px;display:flex;align-items:center;justify-content:space-between'>
  <div>
    <div style='font-size:28px;font-weight:600;color:{MUTED}'>Total da fatura</div>
    <div style='font-size:76px;font-weight:800;letter-spacing:-.03em;margin-top:8px'>R$ <span class='accent'>?</span></div>
  </div>
  <svg width="150" height="100" viewBox="0 0 150 100" fill="none"><rect x="1" y="1" width="148" height="98" rx="14" fill="{SOFT}" stroke="{BRAND}" stroke-width="2"/><rect x="18" y="26" width="34" height="26" rx="5" fill="{BRAND}" opacity=".55"/><rect x="18" y="70" width="80" height="8" rx="4" fill="{BRAND}" opacity=".35"/></svg>
</div></div>"""

def v_chips():
    seg = ["#059669", "#10b981", "#6ee7b7"]
    chips = "".join(f"<span class='chip'><span style='width:18px;height:18px;border-radius:50%;background:{c};margin-right:16px'></span>{t}</span>" for t, c in zip(["Café", "Delivery", "Assinatura"], seg))
    return f"""<div class='visual'>
  <div style='display:flex;gap:18px;flex-wrap:wrap'>{chips}</div>
  <div style='display:flex;height:26px;border-radius:13px;overflow:hidden;margin-top:40px;gap:4px'>
    <div style='flex:3;background:{seg[0]}'></div><div style='flex:4;background:{seg[1]}'></div><div style='flex:2;background:{seg[2]}'></div>
  </div>
</div>"""

def v_grid30():
    cols = ["#059669", "#10b981", "#34d399", "#6ee7b7", "#a7f3d0"]
    cells = []
    for i in range(30):
        c = cols[(i * 7 + i // 3) % len(cols)]
        cells.append(f"<div style='height:56px;border-radius:14px;background:{c}'></div>")
    return f"""<div class='visual'>
  <div style='display:grid;grid-template-columns:repeat(10,1fr);gap:12px'>{''.join(cells)}</div>
  <div style='margin-top:22px;font-size:28px;font-weight:600;color:{MUTED}'>30 dias</div>
</div>"""

def v_cta_pill():
    return f"<div class='visual' style='display:flex;align-items:center;gap:30px'><span class='pill'>Link na bio {ARROW}</span></div>"

def v_fx_cover():
    return f"""<div class='visual' style='display:flex;align-items:center;gap:22px'>
  <span class='pill' style='padding:20px 36px'>R$</span>
  <span style='color:#fff;opacity:.9'>{ARROW.replace('width="30" height="30"','width="44" height="44"')}</span>
  <span class='pill' style='padding:20px 36px'>US$</span>
</div>"""

def v_fx_line():
    # linha de câmbio com remessas em datas diferentes (sem valores)
    path = "M0 150 C 60 120, 110 60, 170 90 S 280 170, 340 120 S 450 30, 520 70 S 640 160, 700 110 S 820 40, 896 60"
    pts = [(170, 90), (340, 120), (520, 70), (760, 78)]
    dots = "".join(f"<line x1='{x}' y1='{y}' x2='{x}' y2='210' stroke='{BRAND}' stroke-width='2' stroke-dasharray='5 7' opacity='.5'/><circle cx='{x}' cy='{y}' r='14' fill='{BRAND}' stroke='#fff' stroke-width='5'/>" for x, y in pts)
    return f"""<div class='visual'><div class='card' style='padding:40px 40px 30px'>
  <svg width="100%" viewBox="0 0 896 230" fill="none">
    <line x1="0" y1="210" x2="896" y2="210" stroke="#e5e7e1" stroke-width="2"/>
    <path d="{path}" stroke="{INK}" stroke-opacity=".75" stroke-width="5" stroke-linecap="round" fill="none"/>
    {dots}
  </svg>
  <div style='display:flex;justify-content:space-between;margin-top:14px;font-size:26px;font-weight:600;color:{MUTED}'>
    <span>câmbio</span><span style='display:flex;align-items:center;gap:10px'><span style='width:16px;height:16px;border-radius:50%;background:{BRAND}'></span>remessas</span>
  </div>
</div></div>"""

def v_rows():
    def row(icon, label, w1, w2, strong=False):
        return f"""<div style='display:flex;align-items:center;gap:26px;padding:22px 0;border-bottom:{'none' if strong else '1px solid #efeee8'}'>
  <div style='width:64px;height:64px;border-radius:18px;background:{SOFT};display:flex;align-items:center;justify-content:center;color:{BRAND_DARK}'>{icon}</div>
  <div style='flex:1'><div style='font-size:32px;font-weight:{700 if strong else 600}'>{label}</div><div class='sk' style='width:{w1}px;margin-top:14px'></div></div>
  <div class='sk' style='width:{w2}px;height:24px'></div>
</div>"""
    up = '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg>'
    flag = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/></svg>'
    rows = row(up, "Remessa", 180, 150) + row(up, "Remessa", 150, 170) + row(flag, "Saldo de fechamento", 170, 190, True)
    return f"<div class='visual'><div class='card' style='padding:10px 44px'>{rows}</div></div>"

def v_years():
    bars = [("2022", 46), ("2023", 70), ("2024", 58), ("2025", 88), ("2026", 64)]
    cols = "".join(f"""<div style='flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:16px'>
  <div style='width:100%;height:{h*2.4:.0f}px;border-radius:16px 16px 6px 6px;background:{BRAND if i==3 else '#a7e3c9'}'></div>
  <div style='font-size:28px;font-weight:600;color:{MUTED};font-variant-numeric:tabular-nums'>{y}</div></div>""" for i, (y, h) in enumerate(bars))
    return f"<div class='visual'><div class='card' style='padding:44px 44px 34px'><div style='display:flex;gap:26px;height:270px;align-items:flex-end'>{cols}</div></div></div>"

def v_ptax():
    return f"""<div class='visual'>
  <div style='display:flex;gap:24px'>
    <div class='card' style='flex:1;padding:40px 44px'><div style='font-size:28px;font-weight:600;color:{MUTED}'>em dólar</div><div style='font-size:88px;font-weight:800;letter-spacing:-.04em;margin-top:6px'>US$</div></div>
    <div class='card' style='flex:1;padding:40px 44px'><div style='font-size:28px;font-weight:600;color:{MUTED}'>em real</div><div style='font-size:88px;font-weight:800;letter-spacing:-.04em;margin-top:6px'>R$</div></div>
  </div>
  <div style='display:inline-flex;align-items:center;gap:14px;margin-top:28px;background:{SOFT};color:{BRAND_DARK};font-size:30px;font-weight:700;padding:18px 30px;border-radius:999px'>
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
    PTAX · Banco Central
  </div>
</div>"""
