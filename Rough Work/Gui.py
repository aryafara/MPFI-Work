#Objective, load in the various windows and have functionality for opening images
import pims
import sys
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class TiffStacks(pims.TiffStack):

    def __init__(self,filename: str):
        super(TiffStacks,self).__init__(filename)
        self.name = filename
        self.frame = 0
        self.currentframe = self[self.frame]
        self.contrast = 10 
        '''
    def histogram(self,grayscale = False,color=0):
        outframe = ((self.currentframe*self.contrast)*(255./65535))
        if grayscale:
            im8b = cv2.cvtColor(outframe,cv2.COLOR_BGR2GRAY)
            plt.plot(cv2.calcHist([im8b],[0],None,[256],[0,256]))
        else:
            plt.plot(cv2.calcHist([self.currentframe],[0],None,[256],[0,256]))
        plt.show()'''
    def view(self):
        return ((self.currentframe*self.contrast)*(255./65535)).astype(np.uint8)




'''
class Controller(dict):
    def __init__(self):
        super(Controller,self).__init__()
        '''
'''
        reasoning for using dict:
            get/set methods
            beats using a stack with pairs due to how every menu is connected to main
            makes new menus easy to implement
        '''
'''
        self['main'] = MainWindow()
        self['main'].start_view.connect(self.show_View)
        self['main'].show()
    
    def show_playBar(self,filename):
        #self['play'] = playBar(filename)
        self['play'].switch_window.connect(self['main']._show)
        #self['play'].show()
    
    def show_window(self,windowclass:'Window Class',window:str,windowattr = None): #generalized show fn for the windows#
        self[window] = window(windowattr) #during garbage collection will check if signal emits correctly
        self[window].connect_to_main.connect(self['main']._show)
        #self[window].show()
'''
class Controller:
    def __init__(self):
        pass
    def show_main(self):
        self.window = MainWindow()
        self.window.start_view.connect(self._view)
        self.window.show()
    def _view(self,filename):
        try:
            self.viewer = Test(filename)
        except:
            raise Exception('File Error Found')
        self.viewer.show()

class MainWindow(QtWidgets.QWidget):
    start_view = QtCore.pyqtSignal(str)
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle('Wilkommen')

        layout = QtWidgets.QGridLayout()
        self.button = QtWidgets.QPushButton('Open a file')
        self.button.clicked.connect(self.OpenButtonPressed)
        
        layout.addWidget(self.button)
        
        self.setLayout(layout)

    def OpenButtonPressed(self):
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(self,'Open a TIFF',"C:/Users/firea/Desktop")
        self.start_view.emit(filename)



class Test(QtWidgets.QWidget):                                                                   
 def __init__(self,filename):                                                                                                                                                                                        
    super(QtWidgets.QWidget,self).__init__()
    layout = QtWidgets.QGridLayout()

    imstack = TiffStacks(filename)

    pixmap_label = QtWidgets.QLabel()                                                                                                                                                                                
    pixmap_label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)                                                                                                                                   
    pixmap_label.resize(imstack[0].shape[0],imstack[0].shape[1])                                                                                                                                                                           
    
    im_np   = imstack.view()                                                                                                                                                                      
    qimage  = QtGui.QImage(im_np, im_np.shape[1], im_np.shape[0],QtGui.QImage.Format_RGB888)                                                                                                                                                                 
    pixmap  = QtGui.QPixmap(qimage)                                                                                                                                                                               
    pixmap  = pixmap.scaled(im_np.shape[0],im_np.shape[1], QtCore.Qt.KeepAspectRatio)                                                                                                                                                    
    pixmap_label.setPixmap(pixmap)

    layout.addWidget(pixmap_label)
        
    self.setLayout(layout)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())