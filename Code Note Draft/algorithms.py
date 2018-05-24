#demonstrate all the tools to be found and used in our python-imagej knockoff
import cv2
import scipy as sp
import numpy as np
#function for saving ROIs
def saveROIs(image,color):
    ''' 
    function to save selected ROIs of any tools as a mask
    Behavior:
            given a np.array with the coordinates of the ROIs
            will output a mask with just 
    '''
    pass



#freeform select
#simple tool which lets user draw a path that will be closed in all cases
"""
Objectives:
    -Draws n lines on image as a highlight
    -easy to make a polygon
    -spits out information to crop out n-gon
"""
drawing = False
mask = np.zeros(image.shape(),np.uint8)
priorpoint=(-1,-1) #global point to allow linedraw
initpoint =(-1,-1) #for final portion
#begin defining mouse callback fn
def freeform(event,x,y,flags,param):
    ''' 
    simple function to draw a perimeter via freehand mouse
    Behavior:
        line is only drawn while left mouse button is pressed
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
            cv2.line(image,priorpoint,(x,y),color,size)
            #placeholder vars for color and size
            #just for this example
            priorpoint = (x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        if drawing:
            #now done drawing, must close shape before turning off drawing
            cv2.line(image,initpoint,(x,y),color,size)
        drawing = False

cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname,freeform)
'example main loop usage:'
while(1):
    cv2.imshow('windowname',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

''''''

#Zoom select
#simple tool to zoom in on portion        
