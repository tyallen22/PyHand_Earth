import os
import time
import psutil
import pyautogui

class GoogleEarth():

    def __init__(self):
        self.current_command = ''

    def check_process_running(self, process_name):
        #testing
        #Check if there is any running process that contains the given name processName.
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if process_name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def start_google_earth(self):

        #Checking if Google Earth is already running
        if self.check_process_running('google-earth'):
            #resize window
            os.system("wmctrl -r 'Google Earth' -e 0,900,300,-1,-1")
            time.sleep(2)

        else:
            #Start Google Earth if it is not already running and resize window
            os.system("nohup google-earth-pro </dev/null >/dev/null 2>&1 &")
            time.sleep(2)
            os.system("wmctrl -r 'Google Earth' -e 0,900,300,-1,-1")
            time.sleep(2)
            
            sidebarCoords = pyautogui.locateOnScreen('clicked_sidebar.png')

            if  sidebarCoords is not None:
                pyautogui.click(sidebarCoords)
                time.sleep(2)
                pyautogui.dragRel(80,200, duration = 1)
                pyautogui.click()
            else:
                
                os.system("wmctrl -a Google Earth Pro")
                Coords = pyautogui.locateOnScreen('unclicked_sidebar.png')
                pyautogui.moveTo(Coords)
                pyautogui.dragRel(80,200, duration = 1)
                pyautogui.click()

#   #Basic commands for buttons
#   def commands(self):
#       print("q to quit s to start\n")


#if __name__ == "__main__":
#
#    while True:
#
#       commands()
#       choice = input("\ncommand: ")
#
#        if choice in ("s", "q"):
#
#            #Closes Google Earth window
#            if choice == "q":
#                os.system("wmctrl -c 'Google Earth'")
#                break
#
#           #Starts Google Earth
#            elif choice == "s":
#                start_google_earth()
#
#        #else:
#            #print("invalid choice")
