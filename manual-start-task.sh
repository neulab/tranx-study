#!/bin/bash

if [ "$#" -ne 3 ]
  then
    echo "Usage: ./start-task.sh USERID TASK USE_PLUGIN(0 or 1)"
    exit -1
fi

## Stop any open IDEs
if pgrep -x "java" > /dev/null
then
    echo "IDE already running? Killing."
    pkill java
fi

## kill browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    echo "Monitoring already running? Killing."
    pkill mitmdump
fi

# manual set userid, task, use_plugin, open IDE
python3 manual.py $1 ${2%/} $3

## start browser monitoring process
echo "Starting monitoring."
mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py >/dev/null 2>&1 &

## start keylogger
if pgrep -f "keylogger.py" > /dev/null
then
    echo "Keylogger already running? Killing."
    kill $(pgrep -f keylogger.py)
fi
nohup python3 keylogger.py >/dev/null 2>&1 &

## log
python3 log_user_event_timeline.py manual_start