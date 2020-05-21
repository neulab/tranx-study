#!/bin/bash

STUDY_CONFIG_FILE="/vagrant/.user_study_current_status"
if [[ ! -f $STUDY_CONFIG_FILE ]]
then
    echo "ERROR: study config file not found!"
    exit 1
fi

#if [ "$#" -ne 2 ]; then
#    echo "Please run '$0 <userid> <task>' to submit! <userid> is your designated user ID and <task> is the name of the task you want to submit, which is the subdirectory name for each, e.g. 'task1-2'."
#    exit 1
#fi
readarray -t line < $STUDY_CONFIG_FILE

USERID=${line[0]}
TASKNAME=${line[1]}

if [ ! -d $TASKNAME ]; then
    echo "Task directory $TASKNAME does not exist!"
    exit 1
fi

echo "UserID: $USERID"
echo "Task directory: $TASKNAME"
echo "Zipping..."


TIMESTAMP=`date +"%s"`

ZIPNAME="${USERID}_${TASKNAME%/}_${TIMESTAMP}.zip"

pkill mitmdump
## stop pycharm
pkill java

sleep 1

pushd $TASKNAME
rm -f pycharm.log
popd
#
#if [[ -f browser_requests.log ]]
#then
#    cp browser_requests.log $TASKNAME
#else
#    echo "Warning: browser_requests.log file not found!"
#fi

cp pycharm.log $TASKNAME

zip -r $ZIPNAME $TASKNAME

echo "Submitting $ZIPNAME"

STATUS=`curl -s -o /dev/null -w "%{http_code}" -F "file=@${ZIPNAME}" http://moto.clab.cs.cmu.edu:8081/task_submission`

if [ $STATUS -eq 200 ]; then
    echo "Submission success! All done!"
else
    echo "Submission failed! Check your UserID or Internet connection, or maybe you have already submitted this task."
fi

echo "Clean up..."
rm -f $ZIPNAME

## log
python3 log_user_event_timeline.py submit