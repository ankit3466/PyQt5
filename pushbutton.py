from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self.left = 100
        self.top = 1000
        self.width = 500
        self.height = 500

        self.setGeometry(self.top,self.left,self.width,self.height)
        self.setWindowIcon(QtGui.QIcon("pyqt.png"))
        self.setWindowTitle(self.title)

        self.createbutton()
        self.show()

    def createbutton(self):
        button = QPushButton("Click Me",self)
        #button.move(250,250)
        #button.setGeometry(400,50,100,50)
        button.setGeometry(QRect(100,100,60,50))

App = QApplication(sys.argv)
window=window()
sys.exit(App.exec())