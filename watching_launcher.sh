#!/bin/bash

###
# Run this script to watch the four server process.
# If one is down, a mail is send to the email bellow.
###

sudo forever restart f0Py

pidArray=`pidof /usr/local/bin/node`

#echo $pidArray

A="$(echo $pidArray | cut -d' ' -f1)"
B="$(echo $pidArray | cut -d' ' -f2)"
C="$(echo $pidArray | cut -d' ' -f3)"
D="$(echo $pidArray | cut -d' ' -f4)"

nohup `./process_watcher.py --pid $A --pid $B --pid $C --pid $D --to thibault.ribayrol@gmail.com` &
