#!/bin/bash
# Gera os vídeos finais, um de cada vez (a máquina tem 2 processadores e outras equipes também renderizam).
cd "$(dirname "$0")"
for r in 27 20 23 25 18; do
  echo "== $(date +%H:%M:%S) início $r"
  python3 reel_$r.py 2>&1 | tail -2
  echo "== $(date +%H:%M:%S) fim $r"
done
