#!/bin/bash
# gera os vídeos finais um por vez (um navegador e um ffmpeg por vez)
cd "$(dirname "$0")"
for r in "$@"; do
  python3 reel_$r.py > trabalho/$r/video.log 2>&1
done
echo fim > trabalho/render_fim.log
