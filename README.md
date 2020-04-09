# TranX Developer Study

## Tasks
You can find all the tasks to complete in their corresponding directory under this repo, e.g `task1-2/`, and read the README file inside for instructions.


## Instructions
We provision Linux desktop with PyCharm IDE, required Python environment for all the tasks and a Google Chrome browser installed (although not encouraged to use unless absolutely necessary).
To setup and perform the user study, please follow the below steps to start a VM pre-provisioned with required environments and use PyCharm IDE.

### 1. Installation and Startup
1. Install latest version (6.1) of [VirtualBox](https://www.virtualbox.org/wiki/Downloads), available for all platforms. (For MacOS users, in case you encounter error during installation, please check out [this article](https://medium.com/@DMeechan/fixing-the-installation-failed-virtualbox-error-on-mac-high-sierra-7c421362b5b5).)
2. Install latest version of [Vagrant](https://www.vagrantup.com/downloads.html), an automatic VM provisioning tool.
3. (Optional but strongly recommended) Install Vagrant plugin with command `vagrant plugin install vagrant-vbguest` for automatically updating the VirtualBox Guest plugin inside the VM to provide the best experience on your host depending on the VirtualBox version.
4. `git clone https://github.com/frankxu2004/tranx-study.git`
5. `cd tranx-study`
6. (Important) If you have previous versions of the provided VM installed, please remove them first with `vagrant destroy`.
6. `vagrant up`
7. Wait until Vagrant automatically download the VM and start it up through VirtualBox. You should now be able to see a Linux desktop environment inside a VirtualBox window. The current directory (i.e. this repo) will be automatically mounted in the VM as `/vagrant` so you could find all the tasks, codes, etc. synced.

### 2. Completing Task inside VM
1. At this stage, as you start to complete your task, you should maximize or full-screen the VM. All activities including coding, web search, etc., should be done within the VM.
2. Open a terminal by clicking the terminal icon in the bottom dock inside VM, and start the user study monitoring process by command `cd /vagrant && ./start-monitoring.sh`.
2. Start PyCharm IDE from top-left menu `Applications - Development - PyCharm Community Edition`.
3. To open your task directory, use `File - Open Project` and navigate to `/vagrant` and select the task directory you are to complete. Find all the tasks included in this repo in their respective subdirectories under `/vagrant`, which is a mounted directory for the current directory on the host (where the `Vagrantfile` is).
4. Before working on your task, make sure to setup your provided user ID in the PyCharm IDE. Go to `File - Settings`, find `Tools - TranX Plugin`. Make sure to enter the unique user ID designated to you for identification and data collection purposes.
5. To start coding the task, please first read the instructions in the `README` file inside the task directory, and then write your program with the `main.py` file. Mac users should use `Control+Options+G` to ask a question with the plugin and `Options+G` to upload edits. Windows/Linux users should use `Ctrl+Alt+G` and `Alt+G` respectively. For more details about the usage of the plugin, please check out [this guide](https://github.com/neulab/tranX-plugin#usage) first.
6. To perform web search on those questions related to the task but not appropriate for the purpose of the plugin (e.g. you may want to know if UTC is equivalent to GMT) as it is not directly related to coding itself, you should use the Chrome web browser inside the VM. It can be opened with the Internet icon in the bottom dock inside the VM. Note that your web browsing activities will be logged inside the VM for user study purposes, so please DO NOT access any sensitive information in the browser.

### 3. Submitting Your Finished Task
After you have finished the coding and debugging, please submit your work on the task! To do so, please do the following steps inside the VM:
1. Open a terminal by clicking the terminal icon in the bottom dock inside VM.
2. `cd /vagrant`
3. `./submit.sh <userid> <task>`, where `<userid>` is your designated user ID and `<task>` is the name of the task you want to submit, which is the subdirectory name for the task in this repo, e.g. `task1-2`.
4. The script will automatically pack your work and upload to our server for the user study evaluations. If everything goes smoothly, you should see a message `Submission success! All done!`. In case you see errors, please make sure the `<userid>` and `<task>` given as arguments are correct.


## Data Collected
1. Your interaction with the plugin in PyCharm IDE, including queries and edits.
2. Your web search/browsing activities inside the VM's Chrome.
3. Your completed task.


## Cleanup
After you have completed the user study, it is safe to cleanup everything.
1. `vagrant destroy` to destroy the VM.
2. Delete the repo folder.
3. Delete the local VM image caches downloaded previously by deleting the folder `$HOME/.vagrant.d`.
4. Uninstall Vagrant and VirtualBox software.
