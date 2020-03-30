# TranX Developer Study

## Tasks
You can find all the tasks to complete in their corresponding directory under this repo, e.g `task1-2/`, and read the README file inside for instructions.


## Instructions
We provision Linux desktop with PyCharm IDE, required Python environment for all the tasks and a Google Chrome browser installed (although not encouraged to use).
To setup and perform the user study, please follow the below steps to start a VM pre-provisioned with required environments and use PyCharm IDE.


1. Install latest version (6.1) of [VirtualBox](https://www.virtualbox.org/wiki/Downloads), available for all platforms.
2. Install latest version of [Vagrant](https://www.vagrantup.com/downloads.html), an automatic VM provisioning tool.
3. (Optional but strongly recommended) Install Vagrant plugin with command `vagrant plugin install vagrant-vbguest` for automatically updating the VirtualBox Guest plugin inside the VM to provide the best experience on your host depending on the VirtualBox version.
4. `git clone https://github.com/frankxu2004/tranx-study.git`
5. `cd tranx-study`
6. `vagrant up`
7. Wait until Vagrant automatically download the VM and start it up through VirtualBox. You should now be able to see a Linux desktop environment inside a VirtualBox window. The current directory (i.e. this repo) will be automatically mounted in the VM as `/vagrant` so you could find all the tasks, codes, etc. synced.
9. Inside the VM, start PyCharm IDE from top-left menu `Applications - Development - PyCharm Community Edition`.
10. To open your task directory, use `File - Open Project` and navigate to `/vagrant` and select the task directory you are to complete. Find all the tasks included in this repo under `/vagrant`, which is a mounted directory for the current directory on the host (where the `Vagrantfile` is).
11. Before completing the task, make sure to setup your provided user ID in the PyCharm IDE. Go to `File - Settings`, find `TranX plugin setting` under `Tools` category. Make sure to enter a unique user name for identification and data collection purposes.
12. Please start coding the task by first reading the instructions in the `README` file inside task directory, and then write your program inside the `main.py`. Mac users should use `Control+Options+G` to ask a question with the plugin and `Options+G` to upload edits. Windows/Linux users should use `Ctrl+Alt+G` and `Alt+G` respectively.
13. To submit your completed task, please ... (TODO: add submission process)


## Alternative Access: Remote Ubuntu Linux Desktop
Just in case the above method does not work for you, you could try our alternate method. 
You are expected to connect to our provisioned user study environment  through a cross-platform Remote Desktop Protocol (RDP) to access a Linux desktop environment.
This method requires least client configuration for the user to attend the study, but will inevitable induce lags during operation as it is a cloud-based desktop.

1. Install RDP client. 
   1. Windows: Already installed with the OS; Start Menu - Type "Remote Desktop".
   2. macOS: Install [Microsoft RDP Client](https://apps.apple.com/us/app/microsoft-remote-desktop-10/id1295203466?mt=12) from App Store. 
   3. Linux: [Remmina](https://remmina.org/), [freerdp](http://www.freerdp.com/), etc.
2. Connect to our server `5568.duckdns.org` with port the default `3389`.
3. When prompt to login, use username `neulab`  and password `tranxuserstudy`.
4. Viola, you have come to our provisioned desktop on the cloud, and please follow the above instructions for completing the tasks.