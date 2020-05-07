import sys
import os
import subprocess
import xml.etree.ElementTree as ET

import requests

def update_plugin_config(userid):
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/options/TranXConfig.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    for elem in root.iter('option'):
        if elem.get('name') == 'userName':
            elem.set('value', userid)

    tree.write(path)


def switch_plugin_on():
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/disabled_plugins.txt'
    with open(path, "r", encoding='utf-8') as f:
        lines = f.readlines()
    with open(path, "w", encoding='utf-8') as f:
        for line in lines:
            if line.strip("\n") != "edu.cmu.tranx.tranx_plugin":
                f.write(line)

def switch_plugin_off():
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/disabled_plugins.txt'
    with open(path, "r", encoding='utf-8') as f:
        lines = f.readlines()
    with open(path, "w", encoding='utf-8') as f:
        for line in lines:
            if line.strip("\n") != "edu.cmu.tranx.tranx_plugin":
                f.write(line)
        f.write("edu.cmu.tranx.tranx_plugin\n")

def set_current_user_task(userid, task):
    path = '/home/vagrant/.user_study_current_status'
    with open(path, "w", encoding='utf-8') as f:
        f.write(userid + '\n')
        f.write(task + '\n')

def read_current_user_task():
    path = '/home/vagrant/.user_study_current_status'
    if not os.path.exists(path):
        return None, None
    with open(path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        userid = lines[0].strip()
        task = lines[1].strip()
    return userid, task

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
            print("Showing task assignment status for user:", userid)
            if task is not None:
                assert usi == userid, "ERROR: Inconsistent userid"
                print("The user is currently working on :", task)
            for task_status in user_status:
                print(task_status['task'] + '\tUse plugin? ' + str(task_status['use_plugin']) + '\tCompleted? ' + str(task_status['completion_status']))

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
            subprocess.Popen(["/snap/bin/pycharm-community /vagrant/" + task + " >pycharm.log 2>&1"], shell=True)
    elif op == 'resume':
        usi, task = read_current_user_task()
        subprocess.Popen(["/snap/bin/pycharm-community /vagrant/" + task + " >pycharm.log 2>&1"], shell=True)

    else:
        print("Not a valid opname")