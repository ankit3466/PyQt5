from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFrame,QPushButton
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

        frame=QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color:green")
        frame.setLineWidth(0.4)

        button = QPushButton("click Me")
        button.setStyleSheet("background-color:red")

        hbox.addWidget(frame)
        hbox.addWidget(button)
        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())