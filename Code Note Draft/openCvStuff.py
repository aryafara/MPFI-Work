#Objective: make a test file for opening a .tiff stack, drawing with a given tool (lets say a free form tool that fits to a contour)
#Bonus: build a usable class to use as the backbone for building easy tiff usage and manipulation
import cv2
import numpy as np
from ScanImageTiffReader import ScanImageTiffReader

with ScanImageTiffReader('rawData_200xDownsampled.tif') as reader:
    print(reader.shape())
"""
class TiffFiles():
    def __init__(self,path2file: str,filename: str,numStacks: 'uint8',grayscale: bool):
        self.stacks = cv2.imreadmulti(path2file)
        self.num = numStacks
        self.name = filename
    def histogram(self,normalize: bool):
        hist = cv2.calcHist()
"""