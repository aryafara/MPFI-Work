# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewtoolbarMK1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ToolWindow(object):
    def setupUi(self, ToolWindow):
        ToolWindow.setObjectName("ToolWindow")
        ToolWindow.resize(1054, 157)
        ToolWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(ToolWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Zoom = QtWidgets.QPushButton(self.centralwidget)
        self.Zoom.setCheckable(True)
        self.Zoom.setObjectName("Zoom")
        self.gridLayout.addWidget(self.Zoom, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.CellMagicWand = QtWidgets.QPushButton(self.centralwidget)
        self.CellMagicWand.setCheckable(True)
        self.CellMagicWand.setObjectName("CellMagicWand")
        self.gridLayout.addWidget(self.CellMagicWand, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.ColorPicker = QtWidgets.QPushButton(self.centralwidget)
        self.ColorPicker.setCheckable(True)
        self.ColorPicker.setObjectName("ColorPicker")
        self.gridLayout.addWidget(self.ColorPicker, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        self.FreeformSelect = QtWidgets.QPushButton(self.centralwidget)
        self.FreeformSelect.setCheckable(True)
        self.FreeformSelect.setObjectName("FreeformSelect")
        self.gridLayout.addWidget(self.FreeformSelect, 0, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 7, 1, 1)
        self.BCmenu = QtWidgets.QPushButton(self.centralwidget)
        self.BCmenu.setCheckable(True)
        self.BCmenu.setObjectName("BCmenu")
        self.gridLayout.addWidget(self.BCmenu, 0, 8, 1, 1)
        ToolWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ToolWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 38))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImage = QtWidgets.QMenu(self.menubar)
        self.menuImage.setObjectName("menuImage")
        self.menuTransform = QtWidgets.QMenu(self.menubar)
        self.menuTransform.setObjectName("menuTransform")
        self.menuROI = QtWidgets.QMenu(self.menubar)
        self.menuROI.setObjectName("menuROI")
        ToolWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ToolWindow)
        self.statusbar.setObjectName("statusbar")
        ToolWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(ToolWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(ToolWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose = QtWidgets.QAction(ToolWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionManager = QtWidgets.QAction(ToolWindow)
        self.actionManager.setObjectName("actionManager")
        self.actionSave_as_2 = QtWidgets.QAction(ToolWindow)
        self.actionSave_as_2.setObjectName("actionSave_as_2")
        self.actionExport = QtWidgets.QAction(ToolWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionHyperStacks = QtWidgets.QAction(ToolWindow)
        self.actionHyperStacks.setObjectName("actionHyperStacks")
        self.actionExport_2 = QtWidgets.QAction(ToolWindow)
        self.actionExport_2.setObjectName("actionExport_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExport_2)
        self.menuROI.addAction(self.actionManager)
        self.menuROI.addAction(self.actionSave_as_2)
        self.menuROI.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menubar.addAction(self.menuROI.menuAction())

        self.retranslateUi(ToolWindow)
        QtCore.QMetaObject.connectSlotsByName(ToolWindow)

    def retranslateUi(self, ToolWindow):
        _translate = QtCore.QCoreApplication.translate
        ToolWindow.setWindowTitle(_translate("ToolWindow", "MainWindow"))
        self.Zoom.setToolTip(_translate("ToolWindow", "<html><head/><body><p>Magnifying glass tool to zoom in by using your scrollwheel</p><p><br/></p></body></html>"))
        self.Zoom.setText(_translate("ToolWindow", "Zoom"))
        self.CellMagicWand.setToolTip(_translate("ToolWindow", "<html><head/><body><p>Cell-MagicWand tool, select a probably position for a cell and it will be highlighted</p></body></html>"))
        self.CellMagicWand.setText(_translate("ToolWindow", "Cell-Wand"))
        self.ColorPicker.setToolTip(_translate("ToolWindow", "<html><head/><body><p>Saves color of mouse clicked point as a string to clipboard in format of &quot;%R:%G:%B&quot;</p></body></html>"))
        self.ColorPicker.setText(_translate("ToolWindow", "Color Picker"))
        self.FreeformSelect.setToolTip(_translate("ToolWindow", "<html><head/><body><p>FreeForm select tool</p></body></html>"))
        self.FreeformSelect.setText(_translate("ToolWindow", "FreeSelect"))
        self.BCmenu.setToolTip(_translate("ToolWindow", "<html><head/><body><p>Brightness and Contrast menu with Histogram and Equalization</p><p><br/></p><p><br/></p></body></html>"))
        self.BCmenu.setText(_translate("ToolWindow", "B&&C"))
        self.menuFile.setTitle(_translate("ToolWindow", "File"))
        self.menuImage.setTitle(_translate("ToolWindow", "Image"))
        self.menuTransform.setTitle(_translate("ToolWindow", "Transform"))
        self.menuROI.setTitle(_translate("ToolWindow", "ROI"))
        self.actionOpen.setText(_translate("ToolWindow", "Open"))
        self.actionOpen.setShortcut(_translate("ToolWindow", "Ctrl+O"))
        self.actionSave_as.setText(_translate("ToolWindow", "Save as..."))
        self.actionSave_as.setShortcut(_translate("ToolWindow", "Ctrl+S"))
        self.actionClose.setText(_translate("ToolWindow", "Close"))
        self.actionManager.setText(_translate("ToolWindow", "Manager"))
        self.actionSave_as_2.setText(_translate("ToolWindow", "Save as..."))
        self.actionSave_as_2.setShortcut(_translate("ToolWindow", "Ctrl+Alt+S"))
        self.actionExport.setText(_translate("ToolWindow", "Export"))
        self.actionHyperStacks.setText(_translate("ToolWindow", "HyperStacks"))
        self.actionExport_2.setText(_translate("ToolWindow", "Export..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToolWindow = QtWidgets.QMainWindow()
    ui = Ui_ToolWindow()
    ui.setupUi(ToolWindow)
    ToolWindow.show()
    sys.exit(app.exec_())

