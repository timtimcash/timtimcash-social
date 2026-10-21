#!/bin/bash
# Gera os vídeos finais da equipe jr um por vez (um navegador e um ffmpeg por vez): bash renderiza.sh 04 07 10 13 15
cd "$(dirname "$0")"
for r in "$@"; do
  echo "inicio $r $(date +%T)" >> trabalho/render.log
  python3 reel_$r.py > trabalho/$r/video.log 2>&1
  echo "fim $r $(date +%T) codigo $?" >> trabalho/render.log
done
echo "tudo $(date +%T)" >> trabalho/render.log
