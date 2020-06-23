import time
import questionary
import requests
from utils import read_current_user_task, read_plugin_status


def upload_survey(results):
    usi, task = read_current_user_task()
    results['userid'] = usi
    results['task'] = task
    results['local_timestamp'] = int(time.time())
    requests.post("http://moto.clab.cs.cmu.edu:8081/post_task_study", json=results, timeout=2.0)


def questions():
    print("Please answer the following questions based on your experience with the task you just completed.")
    print("If you need to restart the questionnaire during the process, just press Ctrl-C.")
    use_plugin = read_plugin_status()
    if use_plugin:
        # used plugin
        results = {'use_plugin': 1}
    else:
        results = {'use_plugin': 0}

    results['difficulty'] = questionary.select(
        "How difficult did you feel the task was? (1: very easy to 5: very difficult)",
        choices=list(map(str, range(1, 6)))).ask()
    if results['difficulty'] is None:
        return questions()
    results['performance'] = questionary.select(
        "How would you evaluate your performance on the task? (1: very poor to 5: very good)",
        choices=list(map(str, range(1, 6)))).ask()
    if results['performance'] is None:
        return questions()
    if use_plugin:
        # plugin-related questions
        results['efficiency'] = questionary.select(
            "How do you think the plugin impacted your efficiency timewise, if at all? "
            "(1: hindered significantly, to 3: neither hindered nor helped, to 5: helped significantly)",
            choices=list(map(str, range(1, 6)))).ask()
        if results['efficiency'] is None:
            return questions()
        results['quality'] = questionary.select(
            "How do you think the plugin impacted your quality of life, with respect to ease of coding, "
            "concentration, etc., if at all? "
            "(1: hindered significantly, to 3: neither hindered nor helped, to 5: helped significantly)",
            choices=list(map(str, range(1, 6)))).ask()
        if results['quality'] is None:
            return questions()
    results['help'] = questionary.select(
        "How often did you need to look for help during the task outside of the plugin, "
        "including web search, looking up API references, etc.?  (1: not at all to 5: very often)",
        choices=list(map(str, range(1, 6)))).ask()
    if results['help'] is None:
        return questions()

    return results


if __name__ == '__main__':
    upload_survey(questions())
