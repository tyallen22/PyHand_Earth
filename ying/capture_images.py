import os
import random
from glob import glob

import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras import preprocessing

class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']

camera = cv2.VideoCapture(0)
camera_height = 500
raw_frames_INDEX_UP = []
raw_frames_V_SIGN = []
raw_frames_THUMB_LEFT = []
raw_frames_THUMB_RIGHT = []
raw_frames_FIST = []
raw_frames_FIVE_WIDE = []
raw_frames_PALM = []
raw_frames_SHAKA = []
raw_frames_NOTHING = []


# Captures hand gesture images to create dataset
while(True):
    # Read a new frame
    _, frame = camera.read()
    
    # Flip the frame
    frame = cv2.flip(frame, 1)

    # Rescale camera output
    aspect = frame.shape[1] / float(frame.shape[0])
    res = int(aspect * camera_height) # landscape orientation - wide image
    frame = cv2.resize(frame, (res, camera_height))

    # Add rectangle
    cv2.rectangle(frame, (300, 75), (650, 425), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Capturing frames", frame)

    key = cv2.waitKey(1)

    # Wait for user to press a key, at which point program captures static webcam image
    #  and classifies it under one of the n types of classifications depending on which
    #  number user types.  Camera quits collection process if user presses 'q' key.
    #  Program outputs a message indicating number key user typed.
    if key & 0xFF == ord("q"):
        break
    elif key & 0xFF == ord("1"):
        raw_frames_INDEX_UP.append(frame)
        print('1 key pressed - saved INDEX_UP frame')
    elif key & 0xFF == ord("2"):
        raw_frames_V_SIGN.append(frame)
        print('2 key pressed - Saved V_SIGN frame')
    elif key & 0xFF == ord("3"):
        raw_frames_THUMB_LEFT.append(frame)
        print('3 key pressed - Saved THUMB_LEFT frame')
    elif key & 0xFF == ord("4"):
        raw_frames_THUMB_RIGHT.append(frame)
        print('4 key pressed - Saved THUMB_RIGHT frame')
    elif key & 0xFF == ord("5"):
        raw_frames_FIST.append(frame)
        print('5 key pressed - Saved FIST frame')
    elif key & 0xFF == ord("6"):
        raw_frames_FIVE_WIDE.append(frame)
        print('6 key pressed - Saved FIVE_WIDE frame') 
    elif key & 0xFF == ord("7"):
        raw_frames_PALM.append(frame)
        print('7 key pressed - Saved PALM frame')    
    elif key & 0xFF == ord("8"):
        raw_frames_SHAKA.append(frame)
        print('8 key pressed - Saved SHAKA frame')    
    elif key & 0xFF == ord("9"):
        raw_frames_NOTHING.append(frame)
        print('9 key pressed - Saved NOTHING frame')       

camera.release()
cv2.destroyAllWindows()

save_width = 399
save_height = 399

# for gesture in class_names:
#     name = './data/images_' + gesture
#     os.makedirs(name, exist_ok = True)

for i, frame in enumerate(raw_frames_INDEX_UP):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_INDEX_UP/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_V_SIGN):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_V_SIGN/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    
for i, frame in enumerate(raw_frames_THUMB_LEFT):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_THUMB_LEFT/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_THUMB_RIGHT):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_THUMB_RIGHT/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    
for i, frame in enumerate(raw_frames_FIST):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_FIST/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    
for i, frame in enumerate(raw_frames_FIVE_WIDE):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_FIVE_WIDE/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_PALM):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_PALM/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_SHAKA):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_SHAKA/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_NOTHING):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_NOTHING/{}.png'.format(i+90), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))