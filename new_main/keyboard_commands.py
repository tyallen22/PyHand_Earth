<<<<<<< HEAD
||||||| 8b4a22b9
#import time
=======
import time
>>>>>>> 58f9f9d7960b32958f6a32b2a8fc7973a37ad788
import os
import pyautogui

class KeyboardCommands():
    pyautogui.FAILSAFE = False

    def __init__(self):
        self.__current_command = ''

    def set_command(self, cmd):
        self.__current_command = cmd

    def send_command(self):
        os.system("wmctrl -a Google Earth Pro")
<<<<<<< HEAD
        if self.__current_command == 'tilt_up':
            pyautogui.keyDown('shift')
            pyautogui.keyDown('up')
        elif self.__current_command == 'tilt_down':
            pyautogui.keyDown('shift')
            pyautogui.keyDown('down')
        else:
            pyautogui.keyDown(self.__current_command)

    def end_command(self):
        os.system("wmctrl -a Google Earth Pro")
        if self.__current_command == 'tilt_up':
            pyautogui.keyUp('shift')
            pyautogui.keyUp('up')
        elif self.__current_command == 'tilt_down':
            pyautogui.keyUp('shift')
            pyautogui.keyUp('down')
        else:
            pyautogui.keyUp(self.__current_command)
||||||| 8b4a22b9
        pyautogui.press(self.__current_command)
=======
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
>>>>>>> 58f9f9d7960b32958f6a32b2a8fc7973a37ad788

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
