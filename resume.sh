#!/bin/bash

## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    echo "Monitoring already running? Killing."
    pkill mitmdump
fi

echo "Starting monitoring."
mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py &

## Retrieve task and configure & start pycharm
python3 retrieve_assignments.py resume not_used

## start keylogger
if pgrep -f "keylogger.py" > /dev/null
then
    echo "Keylogger already running? Killing."
    kill $(pgrep -f keylogger.py)
fi
nohup python3 keylogger.py >/dev/null 2>&1 &

## log
python3 log_user_event_timeline.py resume