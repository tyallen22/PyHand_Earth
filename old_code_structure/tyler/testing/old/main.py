import threading
from hand_recognition import HandRecognition
from keyboard_commands import KeyboardCommands
from google_earth import GoogleEarth

# Continously gets output from model and executes as keyboard command to the
# Google Earth window
def send_output():
    # This try catch will kill the commands being sent if ctrl + c is used
    # in the terminal. It doesn't work w/ Google Earth window open because
    # the Google Earth window is constantly being targeted. Temporary.
    try:
        while True:
            commands.set_command(cv_window.get_output())
            commands.send_command()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    # Instantiate classes
    google_earth = GoogleEarth()
    cv_window = HandRecognition()
    commands = KeyboardCommands()

    #Starts Google Earth and positions it at fixed location with default size
    google_earth.start_google_earth()

    # Create thread to run the camera and process hand gestures
    first_thread = threading.Thread(target=cv_window.run_camera)
    first_thread.start()

    # Create second thread to get the output from model
    second_thread = threading.Thread(target=send_output)
    second_thread.start()
