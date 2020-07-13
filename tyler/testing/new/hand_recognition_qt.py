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

    def __init__(self, earth, *args, **kwargs):
        super(QtCapture, self).__init__(*args, **kwargs)
        self.model = load_model('pyearth_cnn_model_0712.h5')
        self.class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']

        self.earth_commands = earth
        self.new_position = self.earth_commands.get_screen_position()
        self.new_resolution = self.earth_commands.get_screen_resize()

        self.frame_width = int(self.new_resolution[0] * 3/4)
        self.frame_height = int(self.new_resolution[1] * 7/8)

        self.rectangle_start = (int(self.frame_width * 1/2), int(self.frame_height * 1/8))
        self.rectangle_end = (int(self.frame_width * 31/32), int(self.frame_height * 7/8))

        self.text_start = (int(self.frame_width * 1/32), int(self.frame_height * 1/4))

        self.fps = 30
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

        frame = cv2.flip(frame, 1)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Rescaling camera output
        frame = cv2.resize(frame, (self.frame_width, self.frame_height))

        # Add rectangle
        cv2.rectangle(frame, self.rectangle_start, self.rectangle_end, (240, 100, 0), 2)

        # Get ROI
        roi = frame[self.rectangle_start[1]:self.rectangle_end[1],
                    self.rectangle_start[0]:self.rectangle_end[0]]

        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

        # Resize
        roi = cv2.resize(roi, (self.width, self.height))

        # TESTING
        cv2.imshow('testing roi', roi)

        # Predict!
        roi_x = np.expand_dims(roi, axis=0)

        predictions = self.model.predict(roi_x)
        print(predictions)
        INDEX_UP_pred, V_SIGN_pred, THUMB_LEFT_pred, THUMB_RIGHT_pred, FIST_pred, FIVE_WIDE_pred, PALM_pred, SHAKA_pred, NOTHING_pred = predictions[0]

        # Add text
        INDEX_UP_text = '{}: {}%'.format(self.class_names[0], int(INDEX_UP_pred*100))
        cv2.putText(frame, INDEX_UP_text, self.text_start,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        V_SIGN_text = '{}: {}%'.format(self.class_names[1], int(V_SIGN_pred*100))
        cv2.putText(frame, V_SIGN_text, (self.text_start[0], self.text_start[1] + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        THUMB_LEFT_text = '{}: {}%'.format(self.class_names[2], int(THUMB_LEFT_pred*100))
        cv2.putText(frame, THUMB_LEFT_text, (self.text_start[0], self.text_start[1] + 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        THUMB_RIGHT_text = '{}: {}%'.format(self.class_names[3], int(THUMB_RIGHT_pred*100))
        cv2.putText(frame, THUMB_RIGHT_text, (self.text_start[0], self.text_start[1] + 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        FIST_text = '{}: {}%'.format(self.class_names[4], int(FIST_pred*100))
        cv2.putText(frame, FIST_text, (self.text_start[0], self.text_start[1] + 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        FIVE_WIDE_text = '{}: {}%'.format(self.class_names[5], int(FIVE_WIDE_pred*100))
        cv2.putText(frame, FIVE_WIDE_text, (self.text_start[0], self.text_start[1] + 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        PALM_text = '{}: {}%'.format(self.class_names[6], int(PALM_pred*100))
        cv2.putText(frame, PALM_text, (self.text_start[0], self.text_start[1] + 180),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        SHAKA_text = '{}: {}%'.format(self.class_names[7], int(SHAKA_pred*100))
        cv2.putText(frame, SHAKA_text, (self.text_start[0], self.text_start[1] + 210),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

        # Add text
        NOTHING_text = '{}: {}%'.format(self.class_names[8], int(NOTHING_pred*100))
        cv2.putText(frame, NOTHING_text, (self.text_start[0], self.text_start[1] + 240),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

     
        # Show the frame
        #cv2.imshow("Test out", frame)

        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)

        #=======================================================
        # Below code section is for output to pyautogui keyboard shortcuts

        if INDEX_UP_pred > 0.90:
            self.output = 'up'
        elif V_SIGN_pred > 0.90:
            self.output = 'down'
        elif THUMB_LEFT_pred > 0.90:
            self.output = 'left'
        elif THUMB_RIGHT_pred > 0.90:
            self.output = 'right'
        elif FIST_pred > 0.90:
            self.output = '+'  # ZOOM IN
        elif FIVE_WIDE_pred > 0.90:
            self.output = '-'  # ZOOM OUT
        elif PALM_pred > 0.90:
            self.output = 'tilt_up'
        elif SHAKA_pred > 0.90:
            self.output = 'tilt_down'
        else:
            self.output = 'none'

    def start(self):
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./self.fps)

    def stop(self):
        self.timer.stop()

    def get_output(self):
        return self.output
