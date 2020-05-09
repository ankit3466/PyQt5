from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QSizeGrip
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QButton Group"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("pyqt.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        vbox=QVBoxLayout()
        size=QSizeGrip(self)
        vbox.addWidget(size)

        self.setLayout(vbox)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())