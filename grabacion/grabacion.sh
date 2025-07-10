#!/bin/bash
DIR="$HOME/grabaciones_auto"
mkdir -p "$DIR"
TS=$(date +"%Y%m%d_%H%M%S")
OUTFILE="$DIR/grabacion_$TS.wav"
arecord -D hw:2,0 -f cd -t wav -d 60 -q $OUTFILE
