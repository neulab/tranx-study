#!/bin/bash

# enable web during the warmup
if pgrep -x "mitmdump" > /dev/null
then
    echo "Proxy already running."
else
    echo "Starting."
    /usr/local/bin/mitmdump -q --set stream_large_bodies=1 &
fi

python3 manual.py dummy helloworld 1
