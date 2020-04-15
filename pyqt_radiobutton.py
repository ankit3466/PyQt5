from PyQt5.QtWidgets import QApplication,QDialog,QVBoxLayout,QLabel,QGroupBox,QHBoxLayout,QRadioButton
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

        hboxlayout = QVBoxLayout()

        radiobutton1 = QRadioButton("Python")
        radiobutton1.setIcon(QtGui.QIcon("python.jpg"))
        radiobutton1.setIconSize(QtCore.QSize(40,40))
        radiobutton1.setFont(QtGui.QFont("Sansrif",10))
        radiobutton1.setChecked(True)
        radiobutton1.toggled.connect(self.onselect)
        hboxlayout.addWidget(radiobutton1)

        radiobutton2 = QRadioButton("C#")
        radiobutton2.setIcon(QtGui.QIcon("csharp.png"))
        radiobutton2.setIconSize(QtCore.QSize(40, 40))
        radiobutton2.setFont(QtGui.QFont("Sansrif", 10))
        radiobutton2.toggled.connect(self.onselect)
        hboxlayout.addWidget(radiobutton2)

        radiobutton3 = QRadioButton("C++")
        radiobutton3.setIcon(QtGui.QIcon("cpp.png"))
        radiobutton3.setIconSize(QtCore.QSize(40, 40))
        radiobutton3.setFont(QtGui.QFont("Sansrif", 10))
        radiobutton3.toggled.connect(self.onselect)
        hboxlayout.addWidget(radiobutton3)

        self.groupbox.setLayout(hboxlayout)

    def onselect(self):
        radiobtn = self.sender()

        if radiobtn.isChecked():
            self.label.setText("You selected " + radiobtn.text())


App = QApplication(sys.argv)
window=Window()
sys.exit(App.exec())