#!/bin/bash

HOST=$1
HOSTPATH=$2
LOCALFOLDER=$3
COMMAND=$4

while true; do
	ssh $HOST inotifywait -e close_write $HOSTPATH
	scp -r $HOST:$HOSTPATH $LOCALFOLDER
	eval $COMMAND
done