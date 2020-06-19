#!/bin/bash

## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    pkill mitmdump
fi

## Stop any open IDEs
if pgrep -x "java" > /dev/null
then
    echo "IDE already running? Killing."
    pkill java
fi

## stop keylogging
if pgrep -f "keylogger.py" > /dev/null
then
    kill $(pgrep -f keylogger.py)
fi

## log
python3 log_user_event_timeline.py pause