import cv2
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage

class CaptureThread(QThread):
    updatePixmap = pyqtSignal(QPixmap)
    updateOutput = pyqtSignal(str)

    def __init__(self, earth, model, class_names, camera):
        super(CaptureThread, self).__init__()

        self.camera = camera
        self.output = ""
        self.thread_running = True

        self.model = model
        self.class_names = class_names

        self.earth_commands = earth
        self.new_position = self.earth_commands.get_screen_position()
        self.new_resolution = self.earth_commands.get_screen_resize()

        self.frame_width = int(self.new_resolution[0] * 3/4)
        self.frame_height = int(self.new_resolution[1] * 7/8)

        self.rectangle_start = (int(self.frame_width * 1/2), int(self.frame_height * 1/8))
        self.rectangle_end = (int(self.frame_width * 31/32), int(self.frame_height * 7/8))

        self.text_start = (int(self.frame_width * 1/32), int(self.frame_height * 1/4))

        self.camera_height = 500
        self.width = 96
        self.height = 96
        self.output = ''

    def run(self):

        while self.thread_running:
            _, frame = self.camera.read()

            if frame is not None:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                frame = cv2.flip(frame, 1)

                # Rescaling camera output
                frame = cv2.resize(frame, (self.frame_width, self.frame_height))

                # Add rectangle
                cv2.rectangle(frame, self.rectangle_start, self.rectangle_end, (240, 100, 0), 2)

                # Get ROI
                roi = frame[self.rectangle_start[1]:self.rectangle_end[1],
                            self.rectangle_start[0]:self.rectangle_end[0]]

                # Parse BRG to RGB
                #roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB) #AHHHHHHHHHHHHHHHHHH

                # Resize
                roi = cv2.resize(roi, (self.width, self.height))

                # Predict!
                roi_x = np.expand_dims(roi, axis=0)

                predictions = self.model.predict(roi_x)
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

                # Convert frame to PyQt format
                img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pix = QPixmap.fromImage(img)
                
                # Emit PyQt signal, sending frame as a QPixmap
                self.updatePixmap.emit(pix)

                #=======================================================
                # Below code section is for output to pyautogui keyboard shortcuts
                
                if INDEX_UP_pred > 0.90:
                    self.updateOutput.emit('up')
                elif V_SIGN_pred > 0.90:
                    self.updateOutput.emit('down')
                elif THUMB_LEFT_pred > 0.90:
                    self.updateOutput.emit('left')
                elif THUMB_RIGHT_pred > 0.90:
                    self.updateOutput.emit('right')
                elif FIST_pred > 0.90:
                    self.updateOutput.emit('=')  # ZOOM IN
                elif FIVE_WIDE_pred > 0.90:
                    self.updateOutput.emit('-')  # ZOOM OUT
                elif PALM_pred > 0.90:
                    self.updateOutput.emit('tilt_up')
                elif SHAKA_pred > 0.90:
                    self.updateOutput.emit('tilt_down')
                else:
                    self.updateOutput.emit('none')

    def stop_thread(self):
        self.thread_running = False

    def release_camera(self):
        self.camera.release()
