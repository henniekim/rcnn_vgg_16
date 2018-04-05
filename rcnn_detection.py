from keras.models import load_model

import numpy as np
import cv2
import os
from rcnn_ss import *
from rcnn_getlabel import *

os.environ["CUDA_VISIBLE_DEVICES"]="0"

sgd_batch_size = 64
sgd_epoch = 10
filepath = './model/vgg_16_fine_tune_'+'batchsize_'+str(sgd_batch_size)+'epoch_'+str(sgd_epoch)
image_path = './samples/test_aero.jpg'

font = cv2.FONT_HERSHEY_SIMPLEX

result = []

model = load_model(filepath)

inputdata = cv2.imread(image_path)
outputdata = inputdata
rects = selective_search(inputdata)
endOfProposal = (len(rects))
print(' The number of proposal : ' + str(endOfProposal))

for i in range (endOfProposal) :
    x = rects[i,0]
    y = rects[i,1]
    w = rects[i,2]
    h = rects[i,3]

    crop = inputdata[y:y +h, x:x+w]

    resize = cv2.resize(crop, dsize=(224, 224))

    #resize = resize.reshape(1, 224, 224, 3)

    result.append(resize)

result = np.asarray(result)
result = result.reshape(-1, 224, 224, 3)
output = model.predict( x = result, batch_size = 64)

for j in range (endOfProposal):
    x = rects[j, 0]
    y = rects[j, 1]

    temp_softmax = output[j,:]
    temp_category = np.argmax(temp_softmax)
    temp_accuracy = temp_softmax[temp_category]

    if temp_accuracy < 0.99 :
        continue
    temp_label = makeLabel(temp_category)


    cv2.rectangle(outputdata, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(outputdata, temp_label, (x, y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)



cv2.imwrite('./result/result.jpg', outputdata)
cv2.imshow('result', outputdata)
cv2.waitKey(300)

