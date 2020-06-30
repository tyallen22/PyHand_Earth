import os
import time
import subprocess
import psutil
from keyboard_commands import KeyboardCommands

class GoogleEarth():
    """
    This is a class that starts Google Earth and performs operations
    on the Google Earth window.

    Attributes:
        keyboard_commands : Instantiates keyboard command class object for sending
                            commands to Google Earth
        screen_position (list) : Position values for moving and resizing windows based
                                 on screen resolution
        resolution (string) : Resolution of the current monitor
    """
    def __init__(self):
        """
        Please see help(GoogleEarth) for more info
        """
        self.keyboard_commands = KeyboardCommands()
        self.screen_position = []
        self.resolution = ''

    def check_process_running(self, process_name):
        """
        Checks if there are any processes currently running that contain a given name.

        Parameters:
        process_name (string) : Name of the process to be checked

        Returns:
        bool: Returns True if process found, else returns False
        """
        for proc in psutil.process_iter():
            try:
                if process_name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def initialize_google_earth(self):
        """
        Checks if Google Earth is running and starts Google Earth if it is not running.
        Following start up, closes two Google Earth toolbars.
        """
        #Checking if Google Earth is already running
        if self.check_process_running('google-earth'):
            self.start_google_earth()

        else:
            #Start Google Earth if it is not already running and resize window
            os.system("nohup google-earth-pro </dev/null >/dev/null 2>&1 &")
            time.sleep(2)
            self.start_google_earth()

        self.toggle_buttons_off()

    def start_google_earth(self):
        """
        Gets the current screen resolution and starts Google Earth. Repositions Google Earth
        in the center of the screen with a size determined by the current screen resolution.
        """
        self.set_screen_resolution()
        comm = "wmctrl -r 'Google Earth' -e 0," + str(int(self.resolution[0])) + "," + \
                str(int(self.resolution[1])) + "," + str(self.screen_position[0]) + "," + \
                str(self.screen_position[1])
        os.system(comm)
        time.sleep(2)

    def set_screen_resolution(self):
        """
        Sets the current screen resolution and screen position.
        """
        output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', shell=True,
                                  stdout=subprocess.PIPE).communicate()[0]
        self.resolution = output.split()[0].split(b'x')

        self.screen_position.append(int((int(self.resolution[0])*(2/5))))
        self.screen_position.append(int((int(self.resolution[1])*(2/5))))
        self.resolution[0] = (int(self.resolution[0])/2)-(self.screen_position[0]/2)
        self.resolution[1] = (int(self.resolution[1])/2)-(self.screen_position[1]/2)

    def toggle_buttons_off(self):
        """
        Toggles two toolbars in Google Earth that cause problems when sending commands
        to the Google Earth window.
        """
        sidebar_coords = self.keyboard_commands.locate_image('close.png')

        if sidebar_coords:
            self.keyboard_commands.click_with_location(sidebar_coords)
            time.sleep(2)

        sidebar_coords = self.keyboard_commands.locate_image('clicked_sidebar.png')

        if sidebar_coords:
            self.keyboard_commands.click_with_location(sidebar_coords)
            time.sleep(2)

    def get_screen_resolution(self):
        """
        Returns the current screen resolution.

        Returns:
            resolution (str) : Current monitor resolution.
        """
        return self.resolution

    def get_screen_position(self):
        """
        Returns the current screen position markers based on current screen resolution. Used
        for positioning windows.

        Returns:
            screen_position (list) : X and Y positions determined by current screen resolution.
        """
        return self.screen_position

    def close_earth(self):
        """
        Closes the Google Earth window.
        """
        os.system("wmctrl -c Google Earth Pro")
