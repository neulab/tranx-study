#!/bin/bash

## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    pkill mitmdump
else
    echo "Monitoring not started, why pause? Maybe an ERROR."
fi

## stop pycharm
pkill java

## log
TIMESTAMP=`date +"%s"`
echo -e "${TIMESTAMP}\tTask paused" >> /vagrant/timeline.log
