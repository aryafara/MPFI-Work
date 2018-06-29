import numpy as np
import scipy as sp
import cv2
from pims import TiffStacks
import read_roi
from read_roi import read_roi_zip, read_roi_file
"""
useful docs:
pims:   http://soft-matter.github.io/pims/v0.4/
numpy:  https://docs.scipy.org/doc/numpy/reference/
opencv: https://docs.opencv.org/3.3.1/d6/d00/tutorial_py_root.html
matplotlib: https://matplotlib.org/

can't help you with finding pyqt resources, most are private, pyside is illegible.
I reccommend using http://gen.lib.rus.ec/ to find some useful books maybe.
"""



#The following class should be initialized in any opening of a tiff stack for python work
class TiffStacks(TiffStack): #parent class is credit to pims, gives slicing and iteration, as well as lazyloading and other useful things
    def __init__(self,filename: str,frame=0,rois = None):
        super(TiffStacks,self).__init__(filename)
        self.rois = rois #rois are loaded as orderedDict type, more info in relevant methods
        self.name = filename #name preserved for debugging objects
        self.contrast = 10 #generic multiplier
        self.currentframe =  (self[frame]*self.contrast*(255./65535)).astype(np.uint8) #squeezes into a 8bit view (numpy array) 

    def roi_view(self,highlight=(150,0,0)):
        if not self.rois:
            raise FileNotFoundError #if no rois are loaded, raise error
        for dicts in self.rois.items():



    

images = TiffStacks('rawData_200xDownsampled.tif')




'''
#####scrub on image
frame = 0
toscrub = False
ix = -1
width = images[0].shape[1]
numframes = len(images)
def mousescrubber(event,x,y,_ignore,__ignore):
    global toscrub,ix
    if event==cv2.EVENT_LBUTTONDOWN:
        if not toscrub:
            ix = x #grab initial position
            toscrub = True 
    elif event==cv2.EVENT_MOUSEMOVE:
        if toscrub:
            global numframes,width,frame
            newframe =int((numframes)*(float(x-ix)/width)) #rescales mouse position so as to be an integer from 0 to numframes-1
            if    newframe < numframes and  newframe > -1:
                frame =  newframe
            elif -newframe < numframes and -newframe > -1:
                frame = -newframe
    elif event==cv2.EVENT_LBUTTONUP:
        if toscrub:
            toscrub = not toscrub
###

images.histogram(frame)

cv2.namedWindow('tifffle')
cv2.setMouseCallback('tifffle',mousescrubber)
while(1):
    images.addContrast(frame)
    images.view(frame,'tifffle')
    k = cv2.waitKey(1) & 0xFF
    if k == 27 :
        break
cv2.destroyAllWindows()
'''
'''
if __name__=="__main__":
    import sys



    sys.exit()

'''
'''    
def histogram(stack,contrasts,frame):
    im8b = (stack[frame]*contrasts[frame])*(255./65535)
    im8b = im8b.astype(np.uint8)
    hist = cv2.calcHist(im8b)
    plt.plot(hist)

def view(stack,contrasts,frame,window:str):
        im8b = (stack[frame]*contrasts[frame])*(255./65535)
        im8b = im8b.astype(np.uint8)
        cv2.imshow(window,im8b)'''
