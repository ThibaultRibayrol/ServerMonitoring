#!/bin/bash

###
# Une solution est d'utiliser cette command `pidof /usr/local/bin/node`, puis parser les 4 pids et écouter sur les 4.
###

sudo forever restart f0Py

pidArray=`pidof /usr/local/bin/node`

echo $pidArray

A="$(echo $pidArray | cut -d' ' -f1)"
B="$(echo $pidArray | cut -d' ' -f2)"
C="$(echo $pidArray | cut -d' ' -f3)"
D="$(echo $pidArray | cut -d' ' -f4)"

echo $A
echo $B
echo $C
echo $D

nohup `./process_watcher.py --pid $A --pid $B --pid $C --pid $D --to thibault.ribayrol@gmail.com` &
