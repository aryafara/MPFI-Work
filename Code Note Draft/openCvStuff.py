#Objective: make a test file for opening a .tiff stack, drawing with a given tool (lets say a free form tool that fits to a contour)
#Bonus: build a usable class to use as the backbone for building easy tiff usage and manipulation
import cv2
import numpy as np
import scipy as sp
import pims
from random import randint
drawing = False 
initpoint = (-1,-1)
priorpoint= (-1,-1)
def freeform(event,x,y,flags,param):
    ''' 
    simple function to draw a perimeter via freehand mouse
    Behavior:
        smoothness of line is determined by resolution,speed-of-drawing and refreshrate
        closes all curves into non-descript shape when done drawing
    Specs for usage:
        color should be maximized for a color that is most visible in image (will make algo)
        size of line should be proportional to definition to prevent poor aliasing
    '''
    global initpoint,priorpoint,drawing
    if event==cv2.EVENT_LBUTTONDOWN: 
        if not drawing:
            initpoint = (x,y)#so we only catch initial point once
            drawing = True
        priorpoint = (x,y)#assign for next step of drawing
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img,priorpoint,(x,y),(x,y,randint(0,255)),3)
            priorpoint = (x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        if drawing:
            drawing = not drawing
            #now done drawing, must close shape before turning off drawing
            cv2.line(img,initpoint,(x,y),(x,y,randint(0,255)),3)
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',freeform)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        #imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #ret, thresh = cv2.threshold(imgray,127,255,0)
        #_, contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #img = cv2.drawContours(img,contours,-1,(0,255,0))
        #cv2.imwrite('test.png',img)
        break
cv2.destroyAllWindows()




