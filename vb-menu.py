#!/bin/python3
# imports to allow running of shell commands
import subprocess

#def queryip(queryipinput):
#  ipresult = subprocess.run(['ping', '-c 2', queryipinput], capture_output=True, text=True)
#  if (ipresult.stderr != ""):
#    return ipresult.stderr
#  else:
#    return ipresult.stdout

class bcolors:
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


# check that a VirtualBox service exists on the computer.
def vboxInstalled():
  vboxInstalled = subprocess.run(['systemctl', 'status', 'virtualbox'], capture_output=True, text=True)
  if (vboxInstalled.stderr != ""):
    return vboxInstalled.stderr
  else:
    return vboxInstalled.stdout

# return list of VirtualBox running VMs
def runningVM():
  runningVM = subprocess.run(['vboxmanage', 'list', 'runningvms'], capture_output=True, text=True)
  if (runningVM.stderr != ""):
    return runningVM.stderr
  else:
    return runningVM.stdout

# return list of all VirtualBox VMs
def allVM():
  allVM = subprocess.run(['vboxmanage', 'list', 'vms'], capture_output=True, text=True)
  if (allVM.stderr != ""):
    return allVM.stderr
  else:
    return allVM.stdout

# start the selected VM in headless mode
def startVM(selectedVM):
  startVMoutput = subprocess.run(['vboxmanage', 'startvm', selectedVM, '--type=headless'], capture_output=True, text=True)
  if (startVMoutput.stderr != ""):
    return startVMoutput.stderr
  else:
    return startVMoutput.stdout


def main():

  vboxService = vboxInstalled()
  runningVMs = runningVM()
  allVMs = allVM()
  vmList = []

  # print list of VMs found inc running status (red stopped, green running)
  if("active" in vboxService):
    menuCount = 0

    if(allVMs == ""):
      print("No VBox VMs found")
    else:
        print("\n")
        print("See list of current VMs (Green: running, Red: stopped)")
        print("------------------------------------------------------")
        for vm in allVMs.splitlines():
          if(runningVMs == ""):
            vmList.append(vm.split())
            print(bcolors.RED + str(menuCount) + ") " + vm + bcolors.END)
            menuCount += 1
          else:
            for vm2 in runningVMs.splitlines():
              if(vm == vm2):
                #vmList.append(bcolors.GREEN + vm + bcolors.END)
                vmList.append(vm)
                print(bcolors.GREEN + str(menuCount) + ") " + vm + bcolors.END)
                menuCount += 1
              else:
                #vmList.append(bcolors.RED + vm + bcolors.END)
                vmList.append(vm)
                print(bcolors.RED + str(menuCount) + ") " + vm + bcolors.END)
                menuCount += 1
        print("\n")
        vmSelect = input("Which VM would you like to manage (0 - " + str(menuCount-1) +"): ")
        # if an invalid number is entered prompt again ### need to catch non numberic entries
        while(int(vmSelect) < 0 or int(vmSelect) > menuCount - 1):
          vmSelect = input("Invalid selection, try again (0 - " + str(menuCount-1) +"): ")
        
        print("")
        print("Selected VM: " + vmList[int(vmSelect)])
        print("Options:")
        print("-------")
        print("0) Start the VM (headless mode)")
        print("1) Reset the VM")
        print("2) Save the VM state")
        print("3) Power off the VM")
        actionSelect = input("What do you want to do with the selected VM (0 - 3): ")
        # if an invalid number is entered prompt again ### need to catch non numberic entries
        while(int(actionSelect) < 0 or int(actionSelect) > 3):
          actionSelect = input("Invalid selection, try again (0 - 3): ")
        
        # perform the select action on the selected vm
        if(actionSelect == "0"):
            print(startVM(vmList[int(vmSelect)].split(None, 1)[0].strip('\"')))
        elif(actionSelect == "1"):
            print("One")
        elif(actionSelect == "2"):
            print("Two")
        elif(actionSelect == "3"):
            print("Three")
        else:
            print("Invalid selection")


  # report if no VirtualBox service found
  else:
    print("No VBox Service found")
if __name__ == '__main__':
    main()