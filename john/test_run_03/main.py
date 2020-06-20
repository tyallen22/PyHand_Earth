"""
This version is a stand-alone file that embeds an OpenCV window, together with
the TensorFlow training model.  Not included is the PyAutoGui manipulation
feature. It is still in a very rudimentary form.  Note that the Start button at
the bottom of the screen will pause/restart the image capturing.

You must include the .h5 Keras training model file in the same directory, as
well as the PyQt helper module interface.py.
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


# import "helper" module, which must be present in same directory
from ui2 import *

# import multiple modules used in earlier deep learning program
import os
import random
from glob import glob

# import Opencv module
import cv2

# import other needed modules
import numpy as np
import matplotlib.pyplot as plt
from keras import preprocessing

from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Flatten, Dense
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import Adam

from keras.models import load_model

# This Keras .h5 file is the training model and needs to reside in the same
#    directory as the program
model = load_model('pyearth_cnn_model_200612_1744.h5')

import time
import pyautogui          # For keyboard shortcuts

class_names = ['INDEX_UP', 'FIST', 'PALM', 'THUMB_LEFT', 'THUMB_RIGHT',
    'FIVE_WIDE']


# PyQt class for the main window displayed
class MainWindow(QWidget):

    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function

        self.ui.control_bt.clicked.connect(self.controlTimer)

    # view camera
    def viewCam(self):
        
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image info
        height, width, channel = image.shape
        
        # flip the image
        image = cv2.flip(image, 1)
        camera_height = 500
        aspect = width / height
        res = int(aspect * camera_height)
        
        # resize image
        image = cv2.resize(image, (res, camera_height))
        
        # draw a rectangle
        cv2.rectangle(image, (300, 75), (650, 425), (240, 100, 0), 2)
        
        # draw region of interest, which is area inside rectangle
        roi = image[75+2:425-2, 300+2:650-2]
        roi = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 96, 96 represents 'resized' height and width of ROI (can't remember
        #   which order)
        roi = cv2.resize(image, (96, 96))
        
        # Predict    
        roi_X = np.expand_dims(roi, axis=0)
        predictions = model.predict(roi_X)
        type_1_pred, type_2_pred, type_3_pred, type_4_pred, type_5_pred, \
            type_6_pred = predictions[0]

        # Add text
        type_1_text = '{}: {}%'.format(class_names[0], int(type_1_pred*100))
        cv2.putText(image, type_1_text, (70, 170), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        tipe_2_text = '{}: {}%'.format(class_names[1], int(type_2_pred*100))
        cv2.putText(image, tipe_2_text, (70, 200), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
        
        # Add text
        tipe_3_text = '{}: {}%'.format(class_names[2], int(type_3_pred*100))
        cv2.putText(image, tipe_3_text, (70, 230), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
        
        # Add text
        tipe_4_text = '{}: {}%'.format(class_names[3], int(type_4_pred*100))
        cv2.putText(image, tipe_4_text, (70, 260), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
        
        # Add text
        tipe_5_text = '{}: {}%'.format(class_names[4], int(type_5_pred*100))
        cv2.putText(image, tipe_5_text, (70, 290), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)
        
        # Add text
        tipe_6_text = '{}: {}%'.format(class_names[5], int(type_6_pred*100))
        cv2.putText(image, tipe_6_text, (70, 320), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        """ This is where we depart from what we did previously because of
        introduction of PyQt. We never use imshow function now."""
        # Show the frame
        #cv2.imshow("Test out", image)
        
        # resize ... again??? ... but does not work without it
        image = cv2.resize(image, (width, height))
        
        # not sure what this does
        step = channel * width
        
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
        
    # saving for possibly moving block of code into this module    
    def predict(self):
        pass
        

    """This methodology is a departure from previous version. I believe that
    most if not all of OpenCV programs capturing video have relied on a
    while loop to keep collecting frames.  So far, I have not been able to make
    a while loop work in PyQt without OpenCV opening a window OUTSIDE of the
    PyQt window.  I am not sure how the timer works but it appears that the
    few different examples I found online rely on it (and not while loops).
    This deserves some more investigating."""
    
    # start/stop timer
    def controlTimer(self):
        
        #self.cap = cv2.VideoCapture(2)
        #self.timer.start(20)
        
        # if timer is stopped ... starts capturing video and changes button
        #   label at bottom of screen to "Stop".
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(2)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
            
            #self.predict()
            
             
        # if timer is started ... pauses capturing video and changes button
        #   label at bottom of screen to "Start".
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())       # This properly terminates program upon exiting
                                #   In previous versions, we used a press of\
                                #   'q' key to quit.  Here, they can click on
                                #   'x' in corner of window, or we can give
                                #   user another option.
