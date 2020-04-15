from PyQt5.QtWidgets import QApplication,QDialog,QVBoxLayout,QLabel,QGroupBox,QHBoxLayout,QCheckBox
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
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sansrif",13))
        #vbox.addWidget(label)

        self.Radiobutton()
        vbox.addWidget(self.groupbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def Radiobutton(self):
        self.groupbox = QGroupBox("Choose your language!")
        self.groupbox.setFont(QtGui.QFont("Sansrif",13))

        hboxlayout = QHBoxLayout()

        self.button1 = QCheckBox("Python")
        self.button1.setIcon(QtGui.QIcon("python.jpg"))
        self.button1.setIconSize(QtCore.QSize(40,40))
        self.button1.setFont(QtGui.QFont("Sansrif",10))
        self.button1.toggled.connect(self.onselect)
        hboxlayout.addWidget(self.button1)

        self.button2 = QCheckBox("C#")
        self.button2.setIcon(QtGui.QIcon("csharp.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setFont(QtGui.QFont("Sansrif", 10))
        self.button2.toggled.connect(self.onselect)
        hboxlayout.addWidget(self.button2)

        self.button3 = QCheckBox("C++")
        self.button3.setIcon(QtGui.QIcon("cpp.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setFont(QtGui.QFont("Sansrif", 10))
        self.button3.toggled.connect(self.onselect)
        hboxlayout.addWidget(self.button3)

        self.groupbox.setLayout(hboxlayout)

    def onselect(self):
        if self.button1.isChecked():
            self.label.setText("You selected "+ self.button1.text())
        if self.button2.isChecked():
            self.label.setText("You selected "+self.button2.text())
        if self.button3.isChecked():
            self.label.setText("you selected "+self.button3.text())


App = QApplication(sys.argv)
window=Window()
sys.exit(App.exec())