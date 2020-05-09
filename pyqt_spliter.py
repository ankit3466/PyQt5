from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFrame,QLineEdit,QSplitter,QVBoxLayout
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
        self.setStyleSheet("background-color:yellow")

        hbox=QHBoxLayout()

        frame1=QFrame()
        frame1.setFrameShape(QFrame.StyledPanel)


        frame2 = QFrame()
        frame2.setFrameShape(QFrame.StyledPanel)

        linedit = QLineEdit()
        linedit.setStyleSheet("background-color:green")

        spliter1 = QSplitter(QtCore.Qt.Horizontal)
        spliter1.addWidget(frame1)
        spliter1.addWidget(linedit)
        spliter1.setStyleSheet("background-color:red")

        spliter2 = QSplitter(QtCore.Qt.Vertical)
        spliter2.addWidget(spliter1)
        spliter2.addWidget(frame2)

        hbox.addWidget(spliter2)

        self.setLayout(hbox)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())