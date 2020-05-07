from retrieve_assignments import *

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Args: userid task use_plugin(0 or 1)")
        exit(-1)
    userid = sys.argv[1]
    task = sys.argv[2]
    use_plugin = int(sys.argv[3])

    set_current_user_task(userid, task)
    update_plugin_config(userid)
    if use_plugin:
        switch_plugin_on()
    else:
        switch_plugin_off()

    subprocess.Popen(["/snap/bin/pycharm-community /vagrant/" + task + " >pycharm.log 2>&1"], shell=True)
