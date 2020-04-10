from PyQt5.QtWidgets import QApplication,QDialog,QVBoxLayout,QLabel
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 200

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("pyqt.png"))
        self.setGeometry(self.left,self.top,self.width,self.height)

        vbox = QVBoxLayout()
        label = QLabel("Its Label 1")
        vbox.addWidget(label)

        label2 = QLabel("Its second Label")
        label2.setFont(QtGui.QFont("Arial",30))
        label2.setStyleSheet("color:blue")
        vbox.addWidget(label2)

        self.setLayout(vbox)
        self.show()

App = QApplication(sys.argv)
window=Window()
sys.exit(App.exec())