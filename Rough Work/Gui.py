from PyQt5 import QtCore, QtGui, QtWidgets
from protoviewer import Ui_Viewer

class firstviewer(Ui_Viewer):
    def __init__(self):
        super().__init__()
        self.setupUi("MainWindow")

        self.actionClose.clicked.connect(self.closeFile())
        self.actionOpen.clicked.connect(self.openFile())
        self.actionColor.clicked.connect(self.colorMenu())
        self.actionHyperStacks.clicked.connect(self.hyperStacksMenu())
        self.actionSave_as.clicked.connect(self.saveFile())
        self.actionTransform.clicked.connect(self.transformMenu())

        self.playBttn.clicked.connect(self.playTiff())
        self.settingBttn.clicked.connect(self.playSettings())
    def closeFile(self):
        pass
    def openFile(self):
        pass
    def saveFile(self):
        pass
    
    def colorMenu(self):
        pass
    def transformMenu(self):
        pass
    def hyperStacksMenu(self):
        pass

    def playTiff(self):
        pass
    def playSettings(self):
        pass