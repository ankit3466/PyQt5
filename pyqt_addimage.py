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
        self.width = 500
        self.height = 400

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("pyqt.png"))
        self.setGeometry(self.left,self.top,self.width,self.height)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QtGui.QPixmap("football.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)

        self.setLayout(vbox)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())