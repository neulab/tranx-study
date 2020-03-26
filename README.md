# TranX Developer Study 
## Tasks
See Google Doc: 
https://docs.google.com/document/d/1McVCxT_2Hd6cZs6YwQvURogHHCxhK2UXakgMXYtO-Bk/edit?usp=sharing

## User Study Environments
We provision Linux desktop with PyCharm IDE, required Python environment for all the tasks and a Google Chrome browser installed (although not encouraged to use).

### Method 1: Remote Ubuntu Linux Desktop
The first method to connect to our provisioned user study environment is through a cross-platform Remote Desktop Protocol (RDP) to access a Linux desktop environment.
This method requires least client configuration for the user to attend the study, but will inevitable induce lags during operation as it is a cloud-based desktop.

1. Install RDP client. 
   1. Windows: Already installed with the OS; Start Menu - Type "Remote Desktop".
   2. macOS: Install [Microsoft RDP Client](https://apps.apple.com/us/app/microsoft-remote-desktop-10/id1295203466?mt=12) from App Store. 
   3. Linux: [Remmina](https://remmina.org/), [freerdp](http://www.freerdp.com/), etc.
2. Connect to our server `5568.duckdns.org` with port the default `3389`.
3. When prompt to login, use username `neulab`  and password `tranxuserstudy`.
4. Viola, you have come to our provisioned desktop on the cloud.

### Method 2: Local VM
The second method is to automatically fire up a VM using Vagrant and VirtualBox with our provided image and access to your own local VM that is provisioned with the same development environment as above.
This method will be significantly more responsive than the first one, but requires some machine resources and setup steps.

1. Install latest version (6.1) of [VirtualBox](https://www.virtualbox.org/wiki/Downloads), available for all platforms.
2. Install latest version of [Vagrant](https://www.vagrantup.com/downloads.html), an automatic VM provisioning tool.
3. 