import sys
import subprocess

import requests

from utils import update_plugin_config, switch_plugin_on, switch_plugin_off, set_current_user_task, \
    read_current_user_task

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Args: opname userid")
        exit(-1)
    op = sys.argv[1]
    userid = sys.argv[2]
    if op == 'show':
        response = requests.post('http://moto.clab.cs.cmu.edu:8081/get_user_status', json={'userid': userid})
        user_status = response.json()
        if not user_status:
            print("No assignments found for user:", userid)
        else:
            usi, task = read_current_user_task()
            assert usi == userid, "ERROR: Inconsistent userid"
            print("Showing task assignment status for user:", userid)

            current_task_submitted = 0
            for task_status in user_status:
                if task_status['task'] == task and task_status['completion_status']:
                    current_task_submitted = 1
                print(task_status['task'] + '\tUse plugin? ' + str(task_status['use_plugin']) +
                      '\tCompleted? ' + str(task_status['completion_status']))
            if task is not None and not current_task_submitted:
                print("The user is currently working on :", task)
            else:
                print("The user is currently working on nothing, please './start-task.sh userid' to get a new task.")

    elif op == 'assign':
        response = requests.post('http://moto.clab.cs.cmu.edu:8081/assign_task', json={'userid': userid})
        assignments = response.json()
        if assignments:
            task = assignments[0]['task']
            use_plugin = assignments[0]['use_plugin']
            print('User:', userid, 'Assigned:', task, 'Use plugin?', use_plugin)
            update_plugin_config(userid)
            if use_plugin:
                switch_plugin_on()
            else:
                switch_plugin_off()

            set_current_user_task(userid, task)
            subprocess.Popen(["/opt/pycharm-community-2020.1.1/bin/pycharm.sh /vagrant/" + task + " >pycharm.log 2>&1"], shell=True)
        else:
            print("You have completed all your assigned task. Thank you!")
            print("Please complete the post-study survey to share your evaluation at link:")
            print("https://forms.gle/DYTW8QW4Ggjs5YwM8")
            exit(1)

    elif op == 'resume':
        usi, task = read_current_user_task()
        if task is not None:
            subprocess.Popen(["/opt/pycharm-community-2020.1.1/bin/pycharm.sh /vagrant/" + task + " >pycharm.log 2>&1"], shell=True)
        else:
            print("No task currently running")
            exit(1)
    else:
        print("Not a valid opname")
