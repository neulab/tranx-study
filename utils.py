import os
from xml.etree import ElementTree as ET


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


def read_plugin_status():
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/disabled_plugins.txt'
    if not os.path.exists(path):
        return True
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            if line.strip("\n") == "edu.cmu.tranx.tranx_plugin":
                return False
    return True


def set_current_user_task(userid, task):
    path = '/vagrant/.user_study_current_status'
    with open(path, "w", encoding='utf-8') as f:
        f.write(userid + '\n')
        f.write(task + '\n')


def read_current_user_task():
    path = '/vagrant/.user_study_current_status'
    if not os.path.exists(path):
        return None, None
    with open(path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        userid = lines[0].strip()
        task = lines[1].strip()
    return userid, task


