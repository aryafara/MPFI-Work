import numpy as np
import scipy as sp
import cv2
import pims
from time import sleep
import matplotlib.pyplot as plt

class TiffStacks(pims.TiffStack):
    def __init__(self,filename: str):
        super(TiffStacks,self).__init__(filename)
        self.name = filename
        self.contrasts = np.zeros(len(self),dtype='uint16')    

    def addContrast(self,frame):
        if self.contrasts[frame] == 0:
            self.contrasts[frame] = 65535./np.amax(self[frame])

    def histogram(self,frame):#WIP
        images = self
        im8b = (images[frame]*images.contrasts[frame])*(255./65535)
        im8b = im8b.astype(np.uint8)
        #hist = cv2.calcHist(im8b)
        #plt.plot(range(256),hist)

    def view(self,frame,window:str):
        images = self
        im8b = (images[frame]*images.contrasts[frame])*(255./65535)
        im8b = im8b.astype(np.uint8)
        cv2.imshow(window,im8b)

    

images = TiffStacks('rawData_200xDownsampled.tif')

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
'''
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