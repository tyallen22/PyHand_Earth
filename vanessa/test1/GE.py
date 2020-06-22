import psutil
import os

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def startGE():
    if checkIfProcessRunning('google-earth'):
    # print('Yes google-earth process was running')
        try:
            os.system("wmctrl -a Google Earth Pro")
        except:
            print('something went wrong')

    else:
        # print('No google-earth process was running')
        os.system("nohup google-earth-pro &")
        os.system("wmctrl -a Google Earth Pro")
        # os.system("exit")

def commands():
    print("q to quit s to start\n")


if __name__ == "__main__":

    while True:
        
        commands()
        choice = input("\ncommand: ")

        if choice in ("s", "q"):
            if choice == "q":
                os.system("pkill google")
                break

            elif choice == "s":
                startGE()

        else: 
            print("invalid choice")