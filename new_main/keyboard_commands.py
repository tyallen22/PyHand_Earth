import os
import pyautogui

class KeyboardCommands():
    pyautogui.FAILSAFE = False

    def __init__(self):
        self.__current_command = ''

    def set_command(self, cmd):
        self.__current_command = cmd

    def send_single_command(self, cmd):
        os.system("wmctrl -a Google Earth Pro")
        pyautogui.press(cmd)
        
    def send_command(self):
        os.system("wmctrl -a Google Earth Pro")
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

    def close_sidebar(self):
        os.system("wmctrl -a Google Earth Pro")
        pyautogui.hotkey('ctrlleft','Alt','b')

    def send_hotkey_two(self, first, second):
        os.system("wmctrl -a Google Earth Pro")
        pyautogui.hotkey(first, second)

    def send_hotkey_three(self, first, second, third):
        os.system("wmctrl -a Google Earth Pro")
        pyautogui.hotkey(first, second, third)

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
