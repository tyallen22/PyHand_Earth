"""Stand-alone program that uses OpenCV to capture live webcam images
and test TensorFlow model predictions using saved model"""
import os
import cv2
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QImage
from keras.models import load_model

# Suppress TensorFlow info and warnings. Errors still displayed.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class QtCapture(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(QtCapture, self).__init__(*args, **kwargs)

        self.model = load_model('pyearth_cnn_model_200612_1744.h5')
        self.class_names = ['INDEX_UP', 'FIST', 'PALM', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIVE_WIDE']

        self.fps = 24
        self.camera = cv2.VideoCapture(-1)

        self.video_frame = QLabel(self)
        self.layout_one = QVBoxLayout()
        self.layout_one.setContentsMargins(0, 0, 0, 0)
        self.layout_one.addWidget(self.video_frame)
        self.setLayout(self.layout_one)

        self.camera_height = 500
        self.width = 96
        self.height = 96
        self.output = ''

        self.timer = QTimer()

    def nextFrameSlot(self):
        _, frame = self.camera.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame = cv2.flip(frame, 1)

        # # Rescaling camera output
        # aspect = frame.shape[1] / float(frame.shape[0])
        # res = int(aspect * self.camera_height) # landscape orientation - wide image
        # frame = cv2.resize(frame, (res, self.camera_height))

        # Add rectangle
        cv2.rectangle(frame, (300, 75), (650, 425), (240, 100, 0), 2)

        # Get ROI
        roi = frame[75+2:425-2, 300+2:650-2]

        # Parse BRG to RGB
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

        # Resize
        roi = cv2.resize(roi, (self.width, self.height))

        # Predict!
        roi_x = np.expand_dims(roi, axis=0)

        predictions = self.model.predict(roi_x)
        type_1_pred, type_2_pred, type_3_pred, type_4_pred, type_5_pred, type_6_pred = predictions[0]

        # Add text
        type_1_text = '{}: {}%'.format(self.class_names[0], int(type_1_pred*100))
        cv2.putText(frame, type_1_text, (70, 170),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        type_2_text = '{}: {}%'.format(self.class_names[1], int(type_2_pred*100))
        cv2.putText(frame, type_2_text, (70, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        type_3_text = '{}: {}%'.format(self.class_names[2], int(type_3_pred*100))
        cv2.putText(frame, type_3_text, (70, 230),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        type_4_text = '{}: {}%'.format(self.class_names[3], int(type_4_pred*100))
        cv2.putText(frame, type_4_text, (70, 260),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        type_5_text = '{}: {}%'.format(self.class_names[4], int(type_5_pred*100))
        cv2.putText(frame, type_5_text, (70, 290),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        type_6_text = '{}: {}%'.format(self.class_names[5], int(type_6_pred*100))
        cv2.putText(frame, type_6_text, (70, 320),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Show the frame
        #cv2.imshow("Test out", frame)

        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)

        #=======================================================
        # Below code section is for output to pautogui keyboard shortcuts

        if type_1_pred > 0.90:
            self.output = 'up'
        elif type_2_pred > 0.90:
            self.output = '+'
        elif type_3_pred > 0.90:
            pass
        elif type_4_pred > 0.90:
            self.output = 'left'
        elif type_5_pred > 0.90:
            self.output = 'right'
        elif type_6_pred > 0.90:
            self.output = '-'

    def start(self):
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./self.fps)

    def stop(self):
        self.timer.stop()

    def get_output(self):
        return self.output
