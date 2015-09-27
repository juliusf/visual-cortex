#!/bin/bash


REMOTEIP=192.168.237.217
REMOTEPATH=/home/jules/inet-private/examples/webrtc/simple_rtp/results/General-0.vec
LOCALPATH=/tmp/General-0.vec
DATAFILE=$LOCALPATH.data
EXECUTESCRIPT="toolbox/extractvectors $LOCALPATH $DATAFILE  -splitall\
   \"Currently Measured Output Rate\"    \
   \"Currently Selected VideoQuality\" \
   \"Frame size before adjustment\" \
   \"EncoderTransitionTimestamps\" \
   \"ccTargetBitrate\" \
   \"RTPDelay\"  \
   && ./plotscripts/plot_inet_NADA.py $DATAFILE"
echo $EXECUTESCRIPT


while true; do
	ssh $REMOTEIP inotifywait -e close_write $REMOTEPATH
	scp -r $REMOTEIP:$REMOTEPATH $LOCALPATH
	eval $EXECUTESCRIPT
done

