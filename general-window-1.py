from PyQt5 import QtGui
import PyQt5
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("pyqt.png"))
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

App = QApplication(sys.argv)
window=Window()
sys.exit(App.exec())