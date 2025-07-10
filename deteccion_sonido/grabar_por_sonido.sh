#!/bin/bash
DIR="$HOME/grabaciones_evento"
mkdir -p "$DIR"
TS=$(date +"%Y%m%d_%H%M%S")
OUTFILE="$DIR/evento_$TS.wav"
sox -t alsa hw:2,0 $OUTFILE silence 1 0.1 2% 1 5.0 2%
