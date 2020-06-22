import os
import pyautogui

#checks if google earth is running
processname = 'google-earth'
tmp = os.popen("ps -Af").read()
proccount = tmp.count(processname)

#if google earth is not running already, it starts it 
#also focuses on google earth window
if (proccount == 0):
    os.system("google-earth-pro")
    os.system("wmctrl -a Google Earth Pro")
    pyautogui.hotkey('Alt', 'f10')

else: 
    os.system("wmctrl -a Google Earth Pro")
    pyautogui.hotkey('Alt', 'f10')





