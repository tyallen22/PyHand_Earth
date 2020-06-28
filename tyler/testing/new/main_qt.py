import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, \
     QPushButton, QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot

from keyboard_commands import KeyboardCommands
from google_earth import GoogleEarth
from hand_recognition_qt import QtCapture

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

class MainWindow(QMainWindow):

    def __init__(self, ge, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Instantiate KeyboardCommands class
        self.commands = KeyboardCommands()
        # Flag for stopping commands to GE window
        self.stop_commands = False
        # Will hold hand_recognition QtCapture class
        self.capture = None
        # Make Qt gesture icon window frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Set geometry of Qt gesture icon window 
        # (this window is the parent of all other Qt windows)
        new_position = ge.get_screen_position()
        self.setGeometry(QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
            # Width of Qt gesture window based on width of GE window
            QtCore.QSize(new_position[0], 100),
            QtWidgets.qApp.desktop().availableGeometry()))

        # self.setWindowTitle("Google Earth Hand Recognition")

        # Initialize threadpool object
        self.threadpool = QThreadPool()
        # Create layouts for organizing Qt gesture icon window
        self.layout = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()

        self.label_dict = dict()
        # Create and add 6 labels containing hand gesture image
        # to layout2. Need different images for all gestures
        for x in range(0, 6):

            self.label = QLabel(self)
            self.pixmap = QPixmap('click.png')
            self.pixmap = self.pixmap.scaledToWidth(100)
            self.label.setPixmap(self.pixmap)

            self.label_dict[x] = self.label

            self.layout2.addWidget(self.label_dict[x])
        # Create start button and connect it to start_opencv function
        self.start_button = QPushButton("Start")
        self.start_button.pressed.connect(self.start_opencv)
        # Create stop button and connect it to stop_opencv function
        self.stop_button = QPushButton("Stop")
        self.stop_button.pressed.connect(self.stop_opencv)
        # Add start and stop button to layout 3
        self.layout3.addWidget(self.start_button)
        self.layout3.addWidget(self.stop_button)
        # Add layout 2 and 3 to layout 1
        self.layout.addLayout(self.layout2)
        self.layout.addLayout(self.layout3)
        # Create widget to hold layout 1, add layout to widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        # Set widget with layouts as central widget
        self.setCentralWidget(self.widget)

    def start_opencv(self):
        # If opencv window not initialized,
        if not self.capture:
            # Instantiate QtCapture class, set parent and window flags
            self.capture = QtCapture()
            self.capture.setParent(self)
            self.capture.setWindowFlags(QtCore.Qt.Tool)
        # Start video capture and show it
        self.capture.start()
        self.capture.show()
        # Set stop command flag, create worker attached to send_output
        # function, start worker as new thread
        self.stop_commands = False
        worker_one = Worker(self.send_output)
        self.threadpool.start(worker_one)

    def stop_opencv(self):
        # Stop timer in hand_recognition, set flag to kill worker thread
        self.capture.stop()
        self.stop_commands = True

    def send_output(self):
        # While stop command false, get commands from hand_recognition
        # and send commands to Google Earth window
        while True:
            self.commands.set_command(self.capture.get_output())
            self.commands.send_command()

            if self.stop_commands:
                break

# class Output():

#     def __init__(self, cv_window):
#         self.commands = KeyboardCommands()
#         self.cv_window = cv_window

#     def send_output(self):
#         try:
#             while True:
#                 self.commands.set_command(self.cv_window.get_output())
#                 self.commands.send_command()
#         except KeyboardInterrupt:
#             pass

def main():
    # Create QApp
    app = QApplication(sys.argv)
    
    # Start Google Earth
    google_earth = GoogleEarth()
    google_earth.initialize_google_earth()
    
    # Create Main Window and show it
    window = MainWindow(google_earth)
    window.show()

    # Reposition main window
    screen_pos = google_earth.get_screen_position()
    screen_res = google_earth.get_screen_resolution()
    # Window moved to x position of GE window, 
    # y position of GE window + height of GE window
    window.move(screen_res[0], screen_res[1] + screen_pos[1])

    app.exec_()

if __name__ == '__main__':
    main()
