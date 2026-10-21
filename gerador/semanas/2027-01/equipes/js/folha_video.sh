#!/bin/bash
# Folha de contato do vídeo final: quadros nos instantes pedidos + a capa da grade.
# uso: folha_video.sh <pasta de saida/...> <pasta de trabalho> "t1 t2 ..."
SAI=$1; TRAB=$2; TEMPOS=$3
D=$TRAB/final; rm -rf $D; mkdir -p $D
for t in $TEMPOS; do ffmpeg -loglevel error -y -ss $t -i $SAI/reel.mp4 -frames:v 1 $D/q_$(printf "%05.2f" $t).png; done
ffmpeg -loglevel error -y -i $SAI/capa.jpg $D/capa.png
python3 /tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/janfev/equipes/js/folha.py $D $TRAB/folha_final.jpg 6 300
