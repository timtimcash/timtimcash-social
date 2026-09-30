# -*- coding: utf-8 -*-
"""Larguras reais de texto em Inter (carregada), para ajustar títulos: python3 medetexto.py '[[texto, px, peso, espac_em], ...]'"""
import asyncio, sys, json
sys.path.insert(0, "/home/claude/timtimcash-social/gerador")
import artes as A
from playwright.async_api import async_playwright
TXT = json.loads(sys.argv[1])
async def m():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        import os
        arq = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trabalho", "medetexto.html")
        os.makedirs(os.path.dirname(arq), exist_ok=True)
        open(arq, "w").write(f"<!doctype html><meta charset=utf-8><style>{A.font_faces()} body{{font-family:Inter;font-feature-settings:'cv11','ss01'}}</style>" +
                             "".join(f"<span style='font-weight:{w}'>Aa</span>" for w in (400, 500, 600, 700, 800)) + "<div id=x></div>")
        await pg.goto("file://" + arq)
        await pg.evaluate("Promise.all([400,500,600,700,800].map(w => document.fonts.load(w + ' 40px Inter')))")
        await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
        for t, s, w, ls in TXT:
            r = await pg.evaluate("([t,s,w,ls]) => { const e=document.getElementById('x'); e.style.cssText=`display:inline-block;white-space:nowrap;font-size:${s}px;font-weight:${w};letter-spacing:${ls}em`; e.textContent=t; return e.getBoundingClientRect().width; }", [t, s, w, ls])
            print(f"{r:7.1f}  {s}px/{w}  {t}")
        await b.close()
asyncio.run(m())
