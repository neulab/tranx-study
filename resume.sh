#!/bin/bash

## Stop any open IDEs
if pgrep -x "java" > /dev/null
then
    echo "IDE already running? Killing."
    pkill java
fi

## Retrieve task and configure & start pycharm
python3 retrieve_assignments.py resume not_used
status=$?

if [ $status -eq 1 ]
then
   ## exit code 1: no new assignments, end study
   ## remove status file
   rm -f .user_study_current_status
   exit -1
fi


## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    echo "Monitoring already running? Killing."
    pkill mitmdump
fi

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
python3 log_user_event_timeline.py resume