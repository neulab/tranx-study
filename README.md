# TranX Developer Study

## Instructions
The goal of the user study is to understand how a code generation and retrieval plugin in IDE could affect the development.

We provision Linux desktop with PyCharm IDE, required Python environment for all the tasks and a Firefox browser installed.

You will be assigned 8 tasks automatically based on your pre-study survey and completing all tasks would take about 4-5 hours so please plan ahead!

**Note that the plugin will be available for you to use only on part of your assigned tasks for controlled study, so please don't panic if you cannot use the plugin for some tasks!**

The plugin is not perfect, so try to use the plugin when you have a question, but feel free to use the web browser **inside the Linux VM** if the plugin is not helpful.

To setup and perform the user study, please follow the below steps to access a VM pre-provisioned with required environments and use PyCharm IDE.

We recommend the following instructions to access our remote desktop environment.
If your Internet connection lag makes the remote environment unusable for development tasks, please try setting up your local user study environment on your machine following [this section](#i-cannot-access-the-remote-environment). Do note that this would require quite some amounts of system resources.

### 1. Access Remote Environment (recommended & easy)
- Start Remote Desktop Client program (RDP client). For Windows users, type "rdp" in start menu and select the remote desktop client. For Mac users, download Microsoft Remote Desktop from App Store (https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466?mt=12). For Linux users, download Remmina (https://remmina.org/).
- Connect to our remote server `5568.duckdns.org`, using the username and password provided in the email.
- Click the "User Study" folder shortcut on the desktop. Enter your folder named by your assigned user ID. **IMPORTANT: Do not enter other user's folder!**
- Enter folder named `tranx-study`, right-click (context menu) and select `Git Bash Here`.
- Run `vagrant up` to bring up the VM.
- Wait until Vagrant automatically download the VM image and start it up through VirtualBox. You should now be able to see a Linux desktop environment inside a VirtualBox window. We advise you to maximize/full-screen the VirtualBox window for your best experience. From now on, please use the Linux VM environment for everything, **including web browsing (Firefox)**.


### 2. Warmup & Familiarize with VM Environment
Starting from this stage, as you start to complete your task, you should maximize or full-screen the VM. All activities including coding in the IDE, web search, etc., should be done within the VM.
- In a terminal in the VM:
    ```
    cd /vagrant
    ./warmup.sh
    ```
    This will start the IDE and enable web browsing to test it out.
- Checkout the README, and familiarize yourself with the environment! For details on how to complete the task with IDE and plugin, please follow the next section. For more help on PyCharm IDE, please visit [JetBrain's help website](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)! Once you are familiar about the IDE, plugin and VM environment, you can start working on the real tasks!
- Python 3.6 is used throughout the study, and can be called from terminal by `python3`.

### 3. Completing Task inside VM
- In a terminal in the VM:
    ```
    cd /vagrant
    ./start-task.sh your_user_id
    ```
    This will retrieve the configuration of one of your assigned task, and automatically start the IDE.
- To start coding the task, please first read the instructions in the `README` file inside the task directory, and then write your program with the `main.py` file. Mac users should use `Control+Options+G` to ask a question with the plugin and `Options+G` to upload edits. Windows/Linux users should use `Ctrl+Alt+G` and `Alt+G` respectively. For more details about the usage of the plugin, please check out [this guide](https://github.com/neulab/tranX-plugin#usage) first.
- To perform web search on those questions related to the task but not appropriate for the purpose of the plugin (e.g. you may want to know if UTC is equivalent to GMT) as it is not directly related to coding itself, you should use the web browser (Firefox) **inside the Linux VM, please do not use browsers on the Windows desktop or your own local computer**. It can be opened from the bottom dock inside the VM. Note that your web browsing activities will be logged inside the VM for user study purposes, so please **DO NOT access any sensitive information in the browser**.
- Although we encourage you to complete one task in one sitting, if you need to take a break during the task, please run `./pause.sh` and `./resume.sh` under `/vagrant/` to pause and resume the task respectively. Note that the behaviors will be recorded.
- If you would like to use libraries that are not preinstalled, please install using `pip3 install package_name` using the terminal inside the VM.

### 4. Submitting Your Task
After you have finished the coding and debugging, please submit your work on the task! To do so, please do the following steps inside the VM:
In a terminal in the VM:
```
cd /vagrant
./submit.sh
```
The script will automatically pack your work and upload to our server for the user study evaluations. If everything goes smoothly, you should see a message `Submission success! All done!`, followed by a post-task survey for our evaluation.
In case you see any errors, probably you have already submitted, or something else is wrong.

Once you have submitted your current assigned task, you should go to step 3 to start a new task assigned to you.
You are welcome to take breaks between tasks (after submission and before starting another assigned task).
If it says there's no task for you, then you are all set! Congratulations!
After completing all tasks, you are prompted in the terminal to take a post-study survey to share your thoughts for our evaluation.

### 5. Useful Scripts
- To check your assigned tasks and their configurations, your current task status, etc., run in a terminal in the VM:
    ```
    cd /vagrant
    ./status.sh your_user_id
    ```
<!-- - To manually start a task with specific configuration, run in a terminal in the VM:
    ```
    cd /vagrant
    ./manual-start-task.sh your_user_id task_name if_use_plugin(0 or 1)
    ``` -->

## FAQs
### I cannot access Internet inside the VM browser.
If you haven't executed `warmup.sh` or `start-task.sh` then it is expected. We route network access through a proxy. Please first start doing a task and then you will be able to access Internet.

### I cannot access the remote environment.
You can use local installation to start up a VM on your own machine, but make sure your machine has enough resources. A machine with more than 4 cores CPU and more than 16GB memory is recommended.
- Install 6.1.10 version of [VirtualBox](https://www.virtualbox.org/wiki/Downloads), available for all platforms. (For MacOS users, in case you encounter error during installation, please check out [this article](https://medium.com/@DMeechan/fixing-the-installation-failed-virtualbox-error-on-mac-high-sierra-7c421362b5b5).)
- Install latest version of [Vagrant](https://www.vagrantup.com/downloads.html), an automatic VM provisioning tool.
- `git clone https://github.com/neulab/tranx-study.git`
- `cd tranx-study`
- (Important) If you have previous versions of the provided VM installed, please remove them first with `vagrant destroy`.
- `vagrant up`
- Wait until Vagrant automatically download the VM and start it up through VirtualBox. You should now be able to see a Linux desktop environment inside a VirtualBox window. The current directory (i.e. this repo) will be automatically mounted in the VM as `/vagrant` so you could find all the tasks, codes, etc. synced.

After you have completed the user study, it is safe to cleanup everything. On your host machine:
- `vagrant destroy` to destroy the VM.
- Delete the repo folder.
- Delete the local VM image caches downloaded previously by deleting the folder `$HOME/.vagrant.d`.
- Uninstall Vagrant and VirtualBox software.

## Task Categories
All the tasks are in their corresponding directory under this repo, e.g `task1-2/`, and read the README file inside for instructions.
Overall, there are 7 different categories as in task1-n to task7-n and you are assigned 4 categories of them based on your expertise in the pre-study survey:
1. Basic Python
2. File 
3. OS
4. Web Scraping (e.g. `beautifulsoup`)
5. Web Server & Client (e.g. `requests`, `flask`, `django`)
6. Data Analysis & Machine Learning (e.g. `pandas`, `sklearn`)
7. Data Visualization (e.g. `matplotlib`)

## Data Collected
- Your interaction with the plugin in PyCharm IDE, including queries and edits.
- Your IDE edit activities.
- Your web search/browsing activities inside the VM's Firefox.
- Your keystrokes.
- Your completed task.
