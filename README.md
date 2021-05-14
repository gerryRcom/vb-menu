# vb-menu
Basic terminal based menu to simplify remote management of Virtual Box VMs

Using VirtualBox to run VMs I need a quick way to be able to manage the VMs remotely when connected over ssh. The `vboxmanage` command is extremely powerful, but if I'm working remotely I really just need to be able to run a few key commands on a VM, it#s running on my desktop so I generally don't like to leave all VMs running

**Initial commands:**

* Start a VM (*Headless*)
* Restart a VM (*Force*)
* Close a VM (*Saving state*)
* Power off a VM (*Force*)

List is incomplete, just the first few options that come to mind.

**Instructions:**

Just run the python file, it will list VMs on the machine and their current state and let you pick a VM and an action to run on it.
