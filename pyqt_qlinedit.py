from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QHBoxLayout, QLineEdit,QWidget
import sys
from PyQt5 import QtGui


class Window(QWidget):
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
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()


        self.line = QLineEdit()
        self.line.returnPressed.connect(self.onpress)
        hbox.addWidget(self.line)
        self.label = QLabel(self)
        hbox.addWidget(self.label)

        self.setLayout(hbox)
        self.show()

    def onpress(self):
        self.label.setText(self.line.text())


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())