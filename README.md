# TranX Developer Study

## Tasks
You can find all the tasks to complete in their corresponding directory under this repo, e.g `task1-2/`, and read the README file inside for instructions.
Overall, there are 7 different categories as in task1-n to task7-n:
1. Basic Python
2. File 
3. OS
4. Web Scraping (e.g. `beautifulsoup`)
5. Web Server & Client (e.g. `requests`, `flask`, `django`)
6. Data Analysis & Machine Learning (e.g. `pandas`, `sklearn`)
7. Data Visualization (e.g. `matplotlib`)

## Instructions
The goal of the user study is to understand how a code generation and retrieval plugin in IDE could affect the development.

We provision Linux desktop with PyCharm IDE, required Python environment for all the tasks and a Firefox browser installed.

Note that the plugin will be available for you to use only on part of your assigned tasks for controlled study.
The plugin is not perfect, so try to use the plugin when you have a question, but feel free to use the web browser if the plugin is not helpful.

To setup and perform the user study, please follow the below steps to start a VM pre-provisioned with required environments and use PyCharm IDE.

### 1. Installation and Startup
- Install 6.1.10 version of [VirtualBox](https://www.virtualbox.org/wiki/Downloads), available for all platforms. (For MacOS users, in case you encounter error during installation, please check out [this article](https://medium.com/@DMeechan/fixing-the-installation-failed-virtualbox-error-on-mac-high-sierra-7c421362b5b5).)
- Install latest version of [Vagrant](https://www.vagrantup.com/downloads.html), an automatic VM provisioning tool.
- `git clone https://github.com/frankxu2004/tranx-study.git`
- `cd tranx-study`
- (Important) If you have previous versions of the provided VM installed, please remove them first with `vagrant destroy`.
- `vagrant up`
- Wait until Vagrant automatically download the VM and start it up through VirtualBox. You should now be able to see a Linux desktop environment inside a VirtualBox window. The current directory (i.e. this repo) will be automatically mounted in the VM as `/vagrant` so you could find all the tasks, codes, etc. synced.

### 2. Warmup & Familiarize with VM Environment
Starting from this stage, as you start to complete your task, you should maximize or full-screen the VM. All activities including coding in the IDE, web search, etc., should be done within the VM.
- In a terminal in the VM:
    ```
    cd vagrant
    ./warmup.sh
    ```
    This will start the IDE and enable web browsing to test it out.
- Checkout the README, and familiarize yourself with the environment! For details on how to complete the task with IDE and plugin, please follow the next section. For more help on PyCharm IDE, please visit [JetBrain's help website](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)! Once you are familiar about the IDE, plugin and VM environment, you can start working on the real tasks!
- Python 3.6 is used throughout the study, and can be called from terminal by `python3`.

### 3. Completing Task inside VM
- In a terminal in the VM:
    ```
    cd vagrant
    ./start-task.sh your_user_id
    ```
    This will retrieve the configuration of one of your assigned task, and automatically start the IDE.
- To start coding the task, please first read the instructions in the `README` file inside the task directory, and then write your program with the `main.py` file. Mac users should use `Control+Options+G` to ask a question with the plugin and `Options+G` to upload edits. Windows/Linux users should use `Ctrl+Alt+G` and `Alt+G` respectively. For more details about the usage of the plugin, please check out [this guide](https://github.com/neulab/tranX-plugin#usage) first.
- To perform web search on those questions related to the task but not appropriate for the purpose of the plugin (e.g. you may want to know if UTC is equivalent to GMT) as it is not directly related to coding itself, you should use the web browser inside the VM. It can be opened from the bottom dock inside the VM. Note that your web browsing activities will be logged inside the VM for user study purposes, so please DO NOT access any sensitive information in the browser.
- Although we encourage you to complete one task in one sitting, if you need to take a break during the task, please run `./pause.sh` and `./resume.sh` under `/vagrant/` to pause and resume the task respectively. Note that the behaviors will be recorded.
- If you would like to use libraries that are not preinstalled, please install using `pip3 install package_name` using the terminal inside the VM.

### 4. Submitting Your Task
After you have finished the coding and debugging, please submit your work on the task! To do so, please do the following steps inside the VM:
In a terminal in the VM:
```
cd vagrant
./submit.sh
```
The script will automatically pack your work and upload to our server for the user study evaluations. If everything goes smoothly, you should see a message `Submission success! All done!`, followed by a post-task survey for our evaluation.
In case you see any errors, probably you have already submitted, or something else is wrong.

Once you have submitted your current assigned task, you should go to step 3 to start a new task assigned to you.
If it says there's no task for you, then you are all set! Congratulations!
After completing all tasks, please take a post-study survey to share your thoughts for our evaluation.

### 5. Useful Scripts
- To check your assigned tasks and their configurations, your current task status, etc., run in a terminal in the VM:
    ```
    cd vagrant
    ./status.sh your_user_id
    ```
- To manually start a task with specific configuration, run in a terminal in the VM:
    ```
    cd vagrant
    ./manual-start-task.sh your_user_id task_name if_use_plugin(0 or 1)
    ```

## FAQs
### I cannot access Internet inside the VM browser.
If you haven't executed `warmup.sh` or `start-task.sh` then it is expected. We route network access through a proxy. Please first start doing a task and then you will be able to access Internet.

## Data Collected
- Your interaction with the plugin in PyCharm IDE, including queries and edits.
- Your web search/browsing activities inside the VM's Firefox.
- Your completed task.


## Cleanup
After you have completed the user study, it is safe to cleanup everything. On your host machine:
- `vagrant destroy` to destroy the VM.
- Delete the repo folder.
- Delete the local VM image caches downloaded previously by deleting the folder `$HOME/.vagrant.d`.
- Uninstall Vagrant and VirtualBox software.
