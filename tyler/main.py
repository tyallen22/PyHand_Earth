import threading
from hand_recognition_a import HandRecognition

# Continously gets output from model and prints to console
def print_output():
    while True:
        print(Window.get_output())

if __name__ == "__main__":
    # Instantiate HandRecognition class
    Window = HandRecognition()

    # Create thread to run the camera and process hand gestures
    first_thread = threading.Thread(target=Window.run_camera)
    first_thread.start()

    # Create second thread to get the output from model
    second_thread = threading.Thread(target=print_output)
    second_thread.start()
