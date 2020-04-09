#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Please run '$0 <userid> <task>' to submit! <userid> is your designated user ID and <task> is the name of the task you want to submit, which is the subdirectory name for each, e.g. 'task1-2'."
    exit 1
fi

USERID=$1
TASKNAME=$2

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
sleep 1

pushd $TASKNAME
rm -f browser_requests.log
popd

cp browser_requests.log $TASKNAME
zip -r $ZIPNAME $TASKNAME

echo "Submitting $ZIPNAME"

STATUS=`curl -s -o /dev/null -w "%{http_code}" -F "file=@${ZIPNAME}" http://moto.clab.cs.cmu.edu:8081/task_submission`

if [ $STATUS -eq 200 ]; then
    echo "Submission success! All done!"
else
    echo "Submission failed! Check your UserID or Internet connection!"
fi

echo "Clean up..."
rm -f $ZIPNAME
