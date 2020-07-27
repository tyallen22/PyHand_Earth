"""Stand-alone program that uses OpenCV to capture live webcam images
and test TensorFlow model predictions using saved model"""

import os
import random
from glob import glob

import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras import preprocessing

# %matplotlib inline

from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Flatten, Dense
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import Adam

from keras.models import load_model
model = load_model('pyearth_cnn_model_200612_1744.h5')

import time
#import pyautogui                        # For keyboard shortcuts
#import pydirectinput                    # For keyboard shortcuts


class_names = ['INDEX_UP', 'FIST', 'PALM', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIVE_WIDE']


# Get the reference to the webcam
camera = cv2.VideoCapture(0)            # 1 = second webcam; default is 0.
camera_height = 500

width = 96
height = 96

#============================================
# Extra temporary pause added for when incorporating pyautogui keyboard
#  shortcuts library
# 
# time.sleep(10)
#============================================

while(True):
    # Read a new frame
    _, frame = camera.read()
    
    # Flip the frameq
    frame = cv2.flip(frame, 1)

    # Rescaling camera output
    aspect = frame.shape[1] / float(frame.shape[0])
    res = int(aspect * camera_height) # landscape orientation - wide image
    frame = cv2.resize(frame, (res, camera_height))

    # Add rectangle
    cv2.rectangle(frame, (300, 75), (650, 425), (240, 100, 0), 2)

    # Get ROI
    roi = frame[75+2:425-2, 300+2:650-2]
    
    # Parse BRG to RGB
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

    # Resize
    roi = cv2.resize(roi, (width, height))
    
    # Predict!
    roi_X = np.expand_dims(roi, axis=0)

    predictions = model.predict(roi_X)
    type_1_pred, type_2_pred, type_3_pred, type_4_pred, type_5_pred, type_6_pred  = predictions[0]

    # Add text
    type_1_text = '{}: {}%'.format(class_names[0], int(type_1_pred*100))
    cv2.putText(frame, type_1_text, (70, 170), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

    # Add text
    tipe_2_text = '{}: {}%'.format(class_names[1], int(type_2_pred*100))
    cv2.putText(frame, tipe_2_text, (70, 200), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
    
    # Add text
    tipe_3_text = '{}: {}%'.format(class_names[2], int(type_3_pred*100))
    cv2.putText(frame, tipe_3_text, (70, 230), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
    
    # Add text
    tipe_4_text = '{}: {}%'.format(class_names[3], int(type_4_pred*100))
    cv2.putText(frame, tipe_4_text, (70, 260), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
    
    # Add text
    tipe_5_text = '{}: {}%'.format(class_names[4], int(type_5_pred*100))
    cv2.putText(frame, tipe_5_text, (70, 290), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
    
    # Add text
    tipe_6_text = '{}: {}%'.format(class_names[5], int(type_6_pred*100))
    cv2.putText(frame, tipe_6_text, (70, 320), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

    # Show the frame
    cv2.imshow("Test out", frame)

    #=======================================================
    # Below code section is for output to pautogui keyboard shortcuts
    """
    if type_1_pred > 0.90:
        pydirectinput.press('up')
    elif type_2_pred > 0.90:
        pydirectinput.press('=')
    elif type_3_pred > 0.90:
        pass
    elif type_4_pred > 0.90:
        pydirectinput.press('left')
    elif type_5_pred > 0.90:
        pydirectinput.press('right')
    elif type_6_pred > 0.90:
        pydirectinput.press('-')
   """    
   #=======================================================

    key = cv2.waitKey(1)
    
    
    # Quit camera if 'q' key is pressed
    if key & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()