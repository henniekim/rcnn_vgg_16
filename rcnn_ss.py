# !/usr/bin/env python3
# Have to use python3!
import sys
import cv2

def selective_search(input):
    cv2.setUseOptimized(True)
    cv2.setNumThreads(4)

    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(input)
    ss.switchToSingleStrategy()
    #ss.switchToSelectiveSearchFast()

    rects = ss.process()
    return rects
