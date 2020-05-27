import time

import questionary
import requests
from retrieve_assignments import read_current_user_task

def read_plugin_status():
    path = '/home/vagrant/.config/JetBrains/PyCharmCE2020.1/disabled_plugins.txt'
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            if line.strip("\n") == "edu.cmu.tranx.tranx_plugin":
                return False
    return True

def upload_survey(results):
    usi, task = read_current_user_task()
    results['userid'] = usi
    results['task'] = task
    results['local_timestamp'] = int(time.time())
    requests.post("http://moto.clab.cs.cmu.edu:8081/post_task_study", json=results, timeout=2.0)


if __name__ == '__main__':
    if read_plugin_status():
        ## used plugin
        results = {'use_plugin': 1}
        results['difficulty'] = questionary.select(
            "How difficult did you feel the task was? (1: very easy to 5: very difficult)",
            choices=list(map(str,range(1,6)))).ask()
        results['performance'] = questionary.select(
            "How would you evaluate your performance on the task? (1: very poor to 5: very good)",
            choices=list(map(str,range(1,6)))).ask()
        results['efficiency'] = questionary.select(
            "Do you think the plugin helped your efficiency, time-wise? (1: not at all to 5: very much)",
            choices=list(map(str,range(1,6)))).ask()
        results['quality'] = questionary.select(
            "Do you think the plugin helped your quality of life, with respect to ease of coding, "
            "concentration, etc.? (1: not at all to 5: very much)",
            choices=list(map(str,range(1,6)))).ask()
        results['help'] = questionary.select(
            "How often did you need to look for help during the task outside of the plugin, "
            "including web search, looking up API references, etc.?  (1: not at all to 5: very often)",
            choices=list(map(str,range(1,6)))).ask()

    else:
        ## not used plugin
        results = {'use_plugin': 0}
        results['difficulty'] = questionary.select(
            "How difficult did you feel the task was? (1: very easy to 5: very difficult)",
            choices=list(map(str,range(1,6)))).ask()
        results['performance'] = questionary.select(
            "How would you evaluate your performance on the task? (1: very poor to 5: very good)",
            choices=list(map(str,range(1,6)))).ask()
        results['help'] = questionary.select(
            "How often did you need to look for help during the task outside of the plugin, "
            "including web search, looking up API references, etc.?  (1: not at all to 5: very often)",
            choices=list(map(str,range(1,6)))).ask()

    upload_survey(results)