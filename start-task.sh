#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: ./start-task.sh USERID"
    exit -1
fi

## Start browser monitoring process
pkill mitmdump
sleep 1

rm -f browser_requests.log
/usr/local/bin/mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py &

## Retrieve task and configure & start pycharm

python3 retrieve_assignments.py assign $1
