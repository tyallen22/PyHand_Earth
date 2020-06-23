import time
import pyautogui

class KeyboardCommands():

    def __init__(self):
        self.current_command = ''

    def set_command(self, cmd):
        self.current_command = cmd

    def send_command(self):
        #time.sleep(1)
        #print('HERE!' + self.current_command)
        pyautogui.press(self.current_command)
