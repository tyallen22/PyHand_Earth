import threading
from hand_recognition import HandRecognition
from keyboard_commands import KeyboardCommands
from google_earth import GoogleEarth

# Continously gets output from model and executes as keyboard command to current window
def print_output():
    while True:
        Commands.set_command(Window.get_output())
        #Enable the call below to constantly set Google Earth as active window before sending a command
        #Start.set_window()
        Commands.send_command()

if __name__ == "__main__":
    # Instantiate HandRecognition class
    Start = GoogleEarth()
    Window = HandRecognition()
    Commands = KeyboardCommands()

#    app = QtWidgets.QApplication(sys.argv)
#    QtWindow = MainWindow()
#    QtWindow.move(950, 950)
#    QtWindow.show()
#    sys.exit(app.exec_())

    #Starts Google Earth and positions it at fixed location with default size
    Start.start_google_earth()

    # Create thread to run the camera and process hand gestures
    first_thread = threading.Thread(target=Window.run_camera)
    first_thread.start()

    # Create second thread to get the output from model
    second_thread = threading.Thread(target=print_output)
    second_thread.start()
