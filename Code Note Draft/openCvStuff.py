#!/
#Objective: make a test file for opening a .tiff stack, drawing with a given tool (lets say a free form tool that fits to a contour)
#Bonus: build a usable class to use as the backbone for building easy tiff usage and manipulation
#import cv2
import numpy as np
import scipy as sp
#import tifffile as tf
#from random import randint
#from ScanImageTiffReader.share.python import ScanImageTiffReader




"""
drawing = False 
mode = True #toggle for shape
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = not drawing
        ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img,(ix,iy),(x,y),(x,y,randint(0,255)))
            else:
                cv2.circle(img,(x,y),randint(0,255),(x,y,randint(0,255)))
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
"""
"""
class TiffFiles():
    def __init__(self,path2file: str,filename: str,numStacks: 'uint8',grayscale: bool):
        self.stacks = cv2.imreadmulti(path2file)
        self.num = numStacks
        self.name = filename
    def histogram(self,normalize: bool):
        hist = cv2.calcHist()
    
    def view(self):
        pass
    
    def mouseover(self):
        pass
    
"""
