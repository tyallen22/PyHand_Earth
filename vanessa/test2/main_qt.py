import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, \
     QPushButton, QWidget, QApplication
from PyQt5.QtGui import QPixmap

from hand_recognition import HandRecognition
from keyboard_commands import KeyboardCommands
from google_earth import GoogleEarth

# class Worker(QRunnable):
#     '''
#     Worker thread

#     Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

#     :param callback: The function callback to run on this worker thread. Supplied args and
#                      kwargs will be passed through to the runner.
#     :type callback: function
#     :param args: Arguments to pass to the callback function
#     :param kwargs: Keywords to pass to the callback function

#     '''

#     def __init__(self, fn, *args, **kwargs):
#         super(Worker, self).__init__()
#         # Store constructor arguments (re-used for processing)
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs

#     @pyqtSlot()
#     def run(self):
#         '''
#         Initialise the runner function with passed args, kwargs.
#         '''
#         self.fn(*self.args, **self.kwargs)
#         while True:
#             print("")

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.cv_window = HandRecognition()
        # self.commands = KeyboardCommands()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setGeometry(QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
            QtCore.QSize(900, 100),
            QtWidgets.qApp.desktop().availableGeometry()))

        self.setWindowTitle("My App")

        # self.threadpool = QThreadPool()
        # self.threadpool.setMaxThreadCount(10)
        # print(self.threadpool.maxThreadCount())

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        label_dict = dict()

        for x in range(0, 6):

            label = QLabel(self)
            pixmap = QPixmap('click.png')
            pixmap = pixmap.scaledToWidth(100)
            label.setPixmap(pixmap)

            label_dict[x] = label

            layout2.addWidget(label_dict[x])

        # worker_one = Worker(cv_window.run_camera)
        # worker_two = Worker(self.send_output)

        start_button = QPushButton("Start")
        # start_button.pressed.connect(self.start_opencv_thread)

        stop_button = QPushButton("Stop")
        # stop_button.pressed.connect(self.stop_opencv_thread)

        layout3.addWidget(start_button)
        layout3.addWidget(stop_button)

        layout.addLayout(layout2)
        layout.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    # def start_opencv_thread(self):
    #     print("Pressed")
    #     worker = Worker(self.cv_window.run_camera)
    #     QThreadPool.globalInstance().start(worker)
    #     worker_one = Worker(self.cv_window.run_camera)
    #     worker_two = Worker(self.send_output)

    #     self.threadpool.start(worker_one)
    #     self.threadpool.start(worker_two)

    # def stop_opencv_thread(self, w1, w2):
    #     self.threadpool.stop(w1)
    #     self.threadpool.stop(w2)

class Output():

    def __init__(self, cv_window):
        self.commands = KeyboardCommands()
        self.cv_window = cv_window

    def send_output(self):
        try:
            while True:
                self.commands.set_command(self.cv_window.get_output())
                self.commands.send_command()
        except KeyboardInterrupt:
            pass

def main():
    app = QApplication(sys.argv)

    # cv_window = HandRecognition()

    # send_out = Output(cv_window)

    google_earth = GoogleEarth()
    google_earth.start_google_earth()

    window = MainWindow()
    window.show()
    window.move(930, 979)

    app.exec_()

if __name__ == '__main__':
    main()
