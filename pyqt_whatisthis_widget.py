from PyQt5.QtWidgets import QApplication,QDialog,QLabel,QHBoxLayout,QPushButton
import sys
from PyQt5 import QtGui

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

        hbox = QHBoxLayout()
        label = QLabel("press shift+f1")
        hbox.addWidget(label)
        
        button = QPushButton("Click me")
        button.setWhatsThis("This is a demo button")
        hbox.addWidget(button)

        self.setLayout(hbox)
        self.show()


App = QApplication(sys.argv)
window=Window()
sys.exit(App.exec())