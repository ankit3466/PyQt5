from PyQt5.QtWidgets import QDialog,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QGroupBox,QGridLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QRect,QSize
import sys

class window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500

        self.setGeometry(self.top,self.left,self.width,self.height)
        self.setWindowIcon(QtGui.QIcon("pyqt.png"))
        self.setWindowTitle(self.title)

        self.creategroup()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)

        self.show()

    def creategroup(self):
        self.groupbox = QGroupBox("It's a Group box which language you like")
        layout = QGridLayout()

        button = QPushButton("python", self)
        button.setMinimumHeight(40)
        button.setIcon(QtGui.QIcon("python.jpg"))
        button.setIconSize(QSize(50, 40))
        layout.addWidget(button,0,0)

        button1 = QPushButton("java", self)
        button1.setMinimumHeight(20)
        button1.setIcon(QtGui.QIcon("java.png"))
        button1.setIconSize(QSize(50, 40))
        layout.addWidget(button1,0,1)

        button2 = QPushButton("cpp", self)
        button2.setMinimumHeight(40)
        button2.setIcon(QtGui.QIcon("cpp.png"))
        button2.setIconSize(QSize(50, 40))
        layout.addWidget(button2,1,0)

        button3 = QPushButton("c#", self)
        button3.setMinimumHeight(40)
        button3.setIcon(QtGui.QIcon("csharp.png"))
        button3.setIconSize(QSize(50, 40))
        layout.addWidget(button3,1,1)
        #self.groupbox.setMaximumHeight(200)
        self.groupbox.setLayout(layout)

App = QApplication(sys.argv)
window=window()
sys.exit(App.exec())