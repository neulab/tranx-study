#!/bin/bash

## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    pkill mitmdump
else
    echo "Monitoring not started, why pause? Pausing anyways."
fi

## stop pycharm
pkill java

## log
python3 log_user_event_timeline.py pause