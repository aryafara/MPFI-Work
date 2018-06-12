# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playbarMK1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlayBar(object):
    def setupUi(self, PlayBar):
        PlayBar.setObjectName("PlayBar")
        PlayBar.resize(186, 419)
        self.verticalLayout = QtWidgets.QVBoxLayout(PlayBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playBttn = QtWidgets.QPushButton(PlayBar)
        self.playBttn.setObjectName("playBttn")
        self.verticalLayout.addWidget(self.playBttn)
        self.Scrubber = QtWidgets.QSlider(PlayBar)
        self.Scrubber.setMinimumSize(QtCore.QSize(22, 0))
        self.Scrubber.setMaximumSize(QtCore.QSize(22, 16777215))
        self.Scrubber.setOrientation(QtCore.Qt.Vertical)
        self.Scrubber.setObjectName("Scrubber")
        self.verticalLayout.addWidget(self.Scrubber, 0, QtCore.Qt.AlignHCenter)
        self.settingsBttn = QtWidgets.QPushButton(PlayBar)
        self.settingsBttn.setObjectName("settingsBttn")
        self.verticalLayout.addWidget(self.settingsBttn)

        self.retranslateUi(PlayBar)
        self.playBttn.toggled['bool'].connect(self.Scrubber.update)
        self.Scrubber.sliderPressed.connect(self.playBttn.toggle)
        QtCore.QMetaObject.connectSlotsByName(PlayBar)

    def retranslateUi(self, PlayBar):
        _translate = QtCore.QCoreApplication.translate
        PlayBar.setWindowTitle(_translate("PlayBar", "Form"))
        self.playBttn.setText(_translate("PlayBar", "Play"))
        self.settingsBttn.setText(_translate("PlayBar", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlayBar = QtWidgets.QWidget()
    ui = Ui_PlayBar()
    ui.setupUi(PlayBar)
    PlayBar.show()
    sys.exit(app.exec_())

