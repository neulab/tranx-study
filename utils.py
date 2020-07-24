import os
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element


def update_plugin_config(userid):
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/options/TranXConfig.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    for elem in root.iter('option'):
        if elem.get('name') == 'userName':
            elem.set('value', userid)

    tree.write(path)


def switch_plugin_on():
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/options/TranXConfig.xml'
    tree = ET.parse(path)
    root = tree.getroot()[0]
    # enable fine-grained edits no matter what
    found = False
    for elem in root.iter('option'):
        if elem.get('name') == 'enableFineGrainedEdit':
            found = True
            elem.set('value', 'true')
    if not found:
        root.append(Element('option', attrib={'name': 'enableFineGrainedEdit', 'value': 'true'}))

    found = False
    for elem in root.iter('option'):
        if elem.get('name') == 'enableQuery':
            found = True
            elem.set('value', 'true')
    if not found:
        root.append(Element('option', attrib={'name': 'enableQuery', 'value': 'true'}))
    tree.write(path)


def switch_plugin_off():
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/options/TranXConfig.xml'
    tree = ET.parse(path)
    root = tree.getroot()[0]
    found = False
    for elem in root.iter('option'):
        if elem.get('name') == 'enableFineGrainedEdit':
            found = True
            elem.set('value', 'true')
    if not found:
        root.append(Element('option', attrib={'name': 'enableFineGrainedEdit', 'value': 'true'}))

    found = False
    for elem in root.iter('option'):
        if elem.get('name') == 'enableQuery':
            found = True
            elem.set('value', 'false')
    if not found:
        root.append(Element('option', attrib={'name': 'enableQuery', 'value': 'false'}))
    tree.write(path)


def read_plugin_status():
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/options/TranXConfig.xml'
    tree = ET.parse(path)
    root = tree.getroot()[0]
    for elem in root.iter('option'):
        if elem.get('name') == 'enableQuery':
            return elem.get('value') == 'true'
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


