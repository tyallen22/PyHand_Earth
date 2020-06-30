import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

# This creates a borderless window directly below the position of Google Earth window.
# Currently, can only be run as seperate file. Needs to be integrated into main somehow.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowFlags(
        #   QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint
        #   QtCore.Qt.X11BypassWindowManagerHint
            )
        self.setGeometry(QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
            QtCore.QSize(900, 100),
            QtWidgets.qApp.desktop().availableGeometry()))

def main():
    app = QtWidgets.QApplication(sys.argv)
    my_window = MainWindow()
    my_window.move(900, 937)
    my_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
