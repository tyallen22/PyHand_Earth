#import time
import os
import pyautogui

class KeyboardCommands():

    def __init__(self):
        self.__current_command = ''

    def set_command(self, cmd):
        self.__current_command = cmd

    def send_command(self):
        #time.sleep(1)
        os.system("wmctrl -a Google Earth Pro")
        pyautogui.press(self.__current_command)
