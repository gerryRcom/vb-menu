#!/bin/python3
# imports to allow running of shell commands
import subprocess

# terminal colour text codes (found via a so page)
class bcolors:
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    vmTag = ''

# check that a VirtualBox service exists.
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

# reset the selected VM
def resetVM(selectedVM):
  resetVMoutput = subprocess.run(['vboxmanage', 'controlvm', selectedVM, 'reset'], capture_output=True, text=True)
  if (resetVMoutput.stderr != ""):
    return resetVMoutput.stderr
  else:
    return resetVMoutput.stdout

# Save state of the selected VM and close
def saveVM(selectedVM):
  saveVMoutput = subprocess.run(['vboxmanage', 'controlvm', selectedVM, 'savestate'], capture_output=True, text=True)
  if (saveVMoutput.stderr != ""):
    return saveVMoutput.stderr
  else:
    return saveVMoutput.stdout

# Save state of the selected VM and close
def powerOffVM(selectedVM):
  powerOffVMoutput = subprocess.run(['vboxmanage', 'controlvm', selectedVM, 'poweroff'], capture_output=True, text=True)
  if (powerOffVMoutput.stderr != ""):
    return powerOffVMoutput.stderr
  else:
    return powerOffVMoutput.stdout


def main():
  # check for VirtualBox service
  vboxService = vboxInstalled()

  # check that the VirtualBox service exists, if not end.
  if("active" in vboxService):
    runningVMs = runningVM()
    allVMs = allVM()
    vmList = []
    menuCount = 0

    # if no VMs were found inform the user and end.
    if(allVMs == ""):
      print("No VBox VMs found")
    else:
        # print list of VMs found inc running status (red stopped, green running)
        print("\n")
        print("See list of current VMs (Green: running, Red: stopped)")
        print("------------------------------------------------------")
        for vm in allVMs.splitlines():
          # set default colour for the list of VMs to red
          bcolors.vmTag='\033[91m'
          # if there are no running VMs just list all VMs in red
          if(runningVMs == ""):
            vmList.append(vm)
            print(bcolors.vmTag + str(menuCount) + ") " + vm + bcolors.END)
            menuCount += 1
          else:
            for vm2 in runningVMs.splitlines():
              # if a vm is running change the color to green
              if(vm == vm2):
                bcolors.vmTag='\033[92m'
            
            # print list of vms with appropriate color based on running state
            # build the numeric menu list to allow selection for actions
            print(bcolors.vmTag + str(menuCount) + ") " + vm + bcolors.END)
            vmList.append(vm)
            menuCount += 1
        
        print("\n")
        vmSelect = input("Which VM would you like to manage (0 - " + str(menuCount-1) +"): ")
        # if an invalid entry is entered request input again.
        while(not vmSelect.isdecimal() or vmSelect == "" or int(vmSelect) < 0 or int(vmSelect) > menuCount - 1):
          vmSelect = input("Invalid input, try again (0 - " + str(menuCount-1) +"): ")

        # print options menu      
        print("")
        print("Selected VM: " + vmList[int(vmSelect)])
        print("Options:")
        print("-------")
        print("0) Start the VM (headless mode)")
        print("1) Reset the VM")
        print("2) Save the VM state")
        print("3) Power off the VM")

        actionSelect = input("What do you want to do with the selected VM (0 - 3): ")
        # if a blank or non-numeric value is entered request input again.
        while(not actionSelect.isdecimal() or actionSelect == "" or int(actionSelect) < 0 or int(actionSelect) > 3):
          actionSelect = input("Invalid input, try again (0 - 3): ")

        # perform the selected action on the selected vm, parsing the text to just the VM name
        if(actionSelect == "0"):
            print(startVM(vmList[int(vmSelect)].split(None, 1)[0].strip('\"')))
        elif(actionSelect == "1"):
            print(resetVM(vmList[int(vmSelect)].split(None, 1)[0].strip('\"')))
        elif(actionSelect == "2"):
            print(saveVM(vmList[int(vmSelect)].split(None, 1)[0].strip('\"')))
        elif(actionSelect == "3"):
            print(powerOffVM(vmList[int(vmSelect)].split(None, 1)[0].strip('\"')))
        else:
            print("Invalid selection")

  # report if no VirtualBox service found
  else:
    print("No VirtualBox service found")
if __name__ == '__main__':
    main()