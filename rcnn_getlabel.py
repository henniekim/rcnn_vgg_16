import numpy as np

def makeLabel(category):

    if category == 0:
      label = 'person'
    elif category == 1:
      label = 'bird'
    elif category == 2:
      label = 'cat'
    elif category == 3:
      label = 'cow'
    elif category == 4:
      label = 'dog'
    elif category == 5:
      label = 'horse'
    elif category == 6:
      label = 'sheep'
    elif category == 7:
      label = 'aeroplane'
    elif category == 8:
      label = 'bicycle'
    elif category == 9:
      label = 'boat'
    elif category == 10:
      label = 'bus'
    elif category == 11:
      label = 'car'
    elif category == 12:
      label = 'motorbike'
    elif category == 13:
      label = 'train'
    elif category == 14:
      label = 'bottle'
    elif category == 15:
      label = 'chair'
    elif category == 16:
      label = 'diningtable'
    elif category == 17:
      label = 'pottedplant'
    elif category == 18:
      label = 'sofa'
    elif category == 19:
      label = 'tvmonitor'

    return label