import time
import os
import pyautogui

class KeyboardCommands():

    def __init__(self):
        self.__current_command = ''

    def set_command(self, cmd):
        self.__current_command = cmd

    def send_command(self):
        os.system('wmctrl -a Google Earth Pro')
        if self.__current_command == 'tilt_up':
            pyautogui.keyDown('shift')
            pyautogui.keyDown('up')
            time.sleep(1)
            pyautogui.keyUp('up')
            pyautogui.keyUp('shift')
        elif self.__current_command == 'tilt_down':
            pyautogui.keyDown('shift')
            pyautogui.keyDown('down')
            time.sleep(1)
            pyautogui.keyUp('down')
            pyautogui.keyUp('shift')
        else:
            pyautogui.keyDown(self.__current_command)
            time.sleep(2)
            pyautogui.keyUp(self.__current_command)
