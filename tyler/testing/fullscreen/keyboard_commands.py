#import time
import os
import pyautogui

class KeyboardCommands():

    def __init__(self):
        self.__current_command = ''

    def set_command(self, cmd):
        self.__current_command = cmd

    def send_command(self):
        os.system("wmctrl -a Google Earth Pro")
        pyautogui.press(self.__current_command)

    def locate_image(self, img):
        try:
            location = pyautogui.locateOnScreen(img)
            return location
        except OSError:
            print(img + " Not Found")
            return False

    def click_with_location(self, location):
        pyautogui.click(location)

    def click_without_location(self):
        pyautogui.click()

    def drag_mouse(self, x_offset, y_offset, duration):
        pyautogui.dragRel(x_offset, y_offset, duration)

    def move_mouse_to_coords(self, coords):
        pyautogui.moveTo(coords)
