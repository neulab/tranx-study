#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: ./start-task.sh USERID"
    exit -1
fi


## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    echo "Monitoring already running? Killing."
    pkill mitmdump
fi

echo "Starting monitoring."
mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py &


## Retrieve task and configure & start pycharm
python3 retrieve_assignments.py assign $1

## start keylogger
nohup python3 keylogger.py >/dev/null 2>&1 &

## log
python3 log_user_event_timeline.py start