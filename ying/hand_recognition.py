"""Stand-alone program that uses OpenCV to capture live webcam images
and test TensorFlow model predictions using saved model"""

import cv2
import numpy as np
from keras.models import load_model

class HandRecognition(object):

    def __init__(self):
        #self.model = load_model('pyearth_cnn_model_200612_1744.h5')
        self.model = load_model('pyearth_cnn_model_new.h5')
        self.class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']
        self.camera = cv2.VideoCapture(0)
        self.camera_height = 500
        self.width = 96
        self.height = 96
        self.output = ''

    def run_camera(self):

        while True:
            # Read a new frame
            _, frame = self.camera.read()

            # Flip the frameq
            frame = cv2.flip(frame, 1)

            # Rescaling camera output
            aspect = frame.shape[1] / float(frame.shape[0])
            res = int(aspect * self.camera_height) # landscape orientation - wide image
            frame = cv2.resize(frame, (res, self.camera_height))

            # Add rectangle
            cv2.rectangle(frame, (300, 75), (650, 425), (240, 100, 0), 2)

            # Get ROI
            roi = frame[75+2:425-2, 300+2:650-2]

            # Parse BGR to RGB
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

            # Resize
            roi = cv2.resize(roi, (self.width, self.height))

            # Predict!
            roi_x = np.expand_dims(roi, axis=0)

            predictions = self.model.predict(roi_x)
            print(predictions)
            INDEX_UP_pred, V_SIGN_pred, THUMB_LEFT_pred, THUMB_RIGHT_pred, FIST_pred, FIVE_WIDE_pred, PALM_pred, SHAKA_pred, NOTHING_pred = predictions[0]

            # Add text
            INDEX_UP_text = '{}: {}%'.format(self.class_names[0], int(INDEX_UP_pred*100))
            cv2.putText(frame, INDEX_UP_text, (70, 140),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            V_SIGN_text = '{}: {}%'.format(self.class_names[1], int(V_SIGN_pred*100))
            cv2.putText(frame, V_SIGN_text, (70, 170),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            THUMB_LEFT_text = '{}: {}%'.format(self.class_names[2], int(THUMB_LEFT_pred*100))
            cv2.putText(frame, THUMB_LEFT_text, (70, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            THUMB_RIGHT_text = '{}: {}%'.format(self.class_names[3], int(THUMB_RIGHT_pred*100))
            cv2.putText(frame, THUMB_RIGHT_text, (70, 230),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            FIST_text = '{}: {}%'.format(self.class_names[4], int(FIST_pred*100))
            cv2.putText(frame, FIST_text, (70, 260),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            FIVE_WIDE_text = '{}: {}%'.format(self.class_names[5], int(FIVE_WIDE_pred*100))
            cv2.putText(frame, FIVE_WIDE_text, (70, 290),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            PALM_text = '{}: {}%'.format(self.class_names[6], int(PALM_pred*100))
            cv2.putText(frame, PALM_text, (70, 320),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            SHAKA_text = '{}: {}%'.format(self.class_names[7], int(SHAKA_pred*100))
            cv2.putText(frame, SHAKA_text, (70, 350),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Add text
            NOTHING_text = '{}: {}%'.format(self.class_names[8], int(NOTHING_pred*100))
            cv2.putText(frame, NOTHING_text, (70, 380),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2)

            # Show the frame
            cv2.imshow("Test out", frame)

            #=======================================================
            # Below code section is for output to pautogui keyboard shortcuts

            if INDEX_UP_pred > 0.90:
                self.output = 'up'
            elif V_SIGN_pred > 0.90:
                self.output = 'down'
            elif THUMB_LEFT_pred > 0.90:
                self.output = 'left'
            elif THUMB_RIGHT_pred > 0.90:
                self.output = 'right'
            elif FIST_pred > 0.90:
                self.output = '='  # ZOOM IN
            elif FIVE_WIDE_pred > 0.90:
                self.output = '-'  # ZOOM OUT
            elif PALM_pred > 0.90:
                self.output = 'tilt_up'
            elif SHAKA_pred > 0.90:
                self.output = 'tilt_down'
            else:
                self.output = 'none'

            #=======================================================

            key = cv2.waitKey(1)

            # Quit camera if 'q' key is pressed
            if key & 0xFF == ord("q"):
                break

        self.camera.release()
        cv2.destroyAllWindows()

    def get_output(self):
        return self.output
