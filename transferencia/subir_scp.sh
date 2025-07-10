#!/bin/bash
SRC="$HOME/grabaciones_auto/*.wav"
DEST="usuario@IP:/ruta/destino/"
scp $SRC $DEST
