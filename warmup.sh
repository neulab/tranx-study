#!/bin/bash

# enable web during the warmup
if pgrep -x "mitmdump" > /dev/null
then
    echo "Proxy already running."
    pkill mitmdump
fi
echo "Starting web proxy."
mitmdump -q --set stream_large_bodies=1 &

## start keylogger
if pgrep -f "keylogger.py" > /dev/null
then
    echo "Keylogger already running? Killing."
    kill $(pgrep -f keylogger.py)
fi
nohup python3 keylogger.py >/dev/null 2>&1 &

python3 manual.py dummy helloworld 1
