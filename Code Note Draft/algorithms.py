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


#scrubbing on image tool //DEPRECATED, not using OpenCV for viewing anymore
#tool that takes the horizontal path of user's mouse and selects a frame
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
            if  newframe < numframes and newframe >-1:
                frame = newframe
            elif newframe <=-1:
                frame = frame - newframe
    elif event==cv2.EVENT_LBUTTONUP:
        if toscrub:
            toscrub = not toscrub
#freeform select //DEPRECATED, not using OpenCV for viewing anymore
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
def freeSelect(event,x,y,flags,param):
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
    global priorpoint,drawing
    if event==cv2.EVENT_FLAG_LBUTTON:
        global initpoint
        if drawing:
            #now done drawing, must close shape before turning off drawing
            cv2.line(image,initpoint,(x,y),color,size)
        else: 
            initpoint = (x,y)#so we only catch initial point once
        drawing = not drawing
        priorpoint = (x,y)#assign for next step of drawing
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(image,priorpoint,(x,y),color,size)
            #placeholder vars for color and size
            #just for this example
            priorpoint = (x,y)
cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname,freeSelect)
'example main loop usage:'
while(1):
    cv2.imshow('windowname',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
''''''

#ROI Zoom select //DEPRECATED, not using OpenCV for viewing anymore
#given an ROI, zooms in/out by distance travelled by mouse with button pressed down
#direction travelled does not matter, takes magnitude of distance and applies as scalar to maintain aspect ratio
''' handy dandy zoom mouse-tool, based on free select but modifies a scalar integer rather than draws to screen'''
def zoomSelect(event,x,y,flags,parameter):
    '''
    simple function to handle zoom scale
    Behavior:
        if no mouse, nothing should occur
        if lmb down, records
    '''
    global priorpoint
    if event==cv2.EVENT_LBUTTONDOWN:
        if priorpoint==(-1,-1):# so we only record the start point once
            priorpoint = (x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        global scale #scale is left as an integer so opencv doesnt have a panic
        scale = int(sp.spatial.distance.euclidean((x,y),priorpoint)) #scipy euclidean is more efficient than numpy's linalg.norm and a manual python implementation
        priorpoint = (-1,-1)

def roiZoom(roi,scale):
    pass