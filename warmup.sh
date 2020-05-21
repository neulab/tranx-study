#!/bin/bash

# enable web during the warmup
if pgrep -x "mitmdump" > /dev/null
then
    echo "Proxy already running."
    pkill mitmdump
fi
echo "Starting web proxy."
/usr/local/bin/mitmdump -q --set stream_large_bodies=1 &

python3 manual.py dummy helloworld 1
