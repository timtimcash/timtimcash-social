#!/bin/bash
# renderiza um ou mais posts e monta a folha de contato de cada um em prev/
cd /tmp/claude-0/-home-claude/916e4bf9-d759-5190-a3f0-b5ebef025bc2/scratchpad/novdez/equipes/c1
timeout 600 python3 posts.py "$@" 2>&1 | grep -v "agent-proxy\|connect_rejected\|Allowed hosts\|For details"
for p in "$@"; do python3 folha.py prev/f_${p:0:10}.jpg 4 420 ../../saida/$p/0*.jpg > /dev/null; done
