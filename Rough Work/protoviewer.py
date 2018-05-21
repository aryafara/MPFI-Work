# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'protoviewer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        Viewer.setObjectName("Viewer")
        Viewer.resize(918, 812)
        self.centralwidget = QtWidgets.QWidget(Viewer)
        self.centralwidget.setObjectName("centralwidget")
        self.playBttn = QtWidgets.QPushButton(self.centralwidget)
        self.playBttn.setGeometry(QtCore.QRect(0, 695, 111, 81))
        self.playBttn.setObjectName("playBttn")
        self.tiffScrub = QtWidgets.QSlider(self.centralwidget)
        self.tiffScrub.setGeometry(QtCore.QRect(110, 700, 671, 81))
        self.tiffScrub.setOrientation(QtCore.Qt.Horizontal)
        self.tiffScrub.setObjectName("tiffScrub")
        self.settingBttn = QtWidgets.QPushButton(self.centralwidget)
        self.settingBttn.setGeometry(QtCore.QRect(780, 705, 141, 71))
        self.settingBttn.setObjectName("settingBttn")
        self.tiffDisplay = QtWidgets.QGraphicsView(self.centralwidget)
        self.tiffDisplay.setGeometry(QtCore.QRect(0, 0, 921, 711))
        self.tiffDisplay.setObjectName("tiffDisplay")
        Viewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Viewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 38))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuImage = QtWidgets.QMenu(self.menubar)
        self.menuImage.setObjectName("menuImage")
        Viewer.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(Viewer)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(Viewer)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose = QtWidgets.QAction(Viewer)
        self.actionClose.setObjectName("actionClose")
        self.actionColor = QtWidgets.QAction(Viewer)
        self.actionColor.setObjectName("actionColor")
        self.actionTransform = QtWidgets.QAction(Viewer)
        self.actionTransform.setObjectName("actionTransform")
        self.actionHyperStacks = QtWidgets.QAction(Viewer)
        self.actionHyperStacks.setObjectName("actionHyperStacks")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.actionColor)
        self.menuImage.addAction(self.actionTransform)
        self.menuImage.addAction(self.actionHyperStacks)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())

        self.retranslateUi(Viewer)
        QtCore.QMetaObject.connectSlotsByName(Viewer)

    def retranslateUi(self, Viewer):
        _translate = QtCore.QCoreApplication.translate
        Viewer.setWindowTitle(_translate("Viewer", "MainWindow"))
        self.playBttn.setText(_translate("Viewer", "Play"))
        self.settingBttn.setText(_translate("Viewer", "Play settings"))
        self.menuFile.setTitle(_translate("Viewer", "File"))
        self.menuView.setTitle(_translate("Viewer", "View"))
        self.menuImage.setTitle(_translate("Viewer", "Image"))
        self.actionOpen.setText(_translate("Viewer", "Open..."))
        self.actionSave_as.setText(_translate("Viewer", "Save as..."))
        self.actionClose.setText(_translate("Viewer", "Close"))
        self.actionColor.setText(_translate("Viewer", "Color?"))
        self.actionTransform.setText(_translate("Viewer", "Transform"))
        self.actionHyperStacks.setText(_translate("Viewer", "Hyperstacks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Viewer = QtWidgets.QMainWindow()
    ui = Ui_Viewer()
    ui.setupUi(Viewer)
    Viewer.show()
    sys.exit(app.exec_())

