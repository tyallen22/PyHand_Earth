import os
import random
from glob import glob

import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras import preprocessing

class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']

# Create directories to store image data
for counter, gesture in enumerate(class_names):
    training = f'./data/training/{counter+1}-{gesture}'
    os.makedirs(training, exist_ok = True)
    validation = f'./data/validation/{counter+1}-{gesture}'
    os.makedirs(validation, exist_ok = True)
    testing = f'./data/testing/{counter+1}-{gesture}'
    os.makedirs(testing, exist_ok = True)

camera = cv2.VideoCapture(2)
mode = 'training'
# bg = None
# accumWeight = 0.5
# num_frames = 0
# calibrated = False


# # Find running average over background
# def run_avg(frame, accumWeight):
#     global bg
#     if bg is None:
#         bg = frame.copy().astype('float')
#     cv2.accumulateWeighted(frame, bg, accumWeight)


# # Segment region of hand in frame
# def segment(frame, threshold=30):
#     global bg
#     diff = cv2.absdiff(bg.astype('uint8'), frame)
#     th = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
#     contours, _ = cv2.findContours(th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     if len(contours) == 0:
#         return
#     else:
#         segmented = max(contours, key=cv2.contourArea)
#         return th, segmented


# Capture hand gesture images to create dataset
while(True):
    # Read a new frame
    _, frame = camera.read()
    
    # Flip the frame
    frame = cv2.flip(frame, 1)

    # # Clone a copy
    # clone = frame.copy()

    # Text for instructions
    cv2.putText(frame, 'Press "a" to capture images for TRAINING SET', (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    cv2.putText(frame, 'Press "b" to capture images for VALIDATION SET', (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    cv2.putText(frame, 'Press "c" to capture images for TESTING SET', (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    cv2.putText(frame, 'Press "q" to quit', (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    cv2.putText(frame, 'Press "1-9" to capture images for corresponding hand gesture', (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

    cv2.putText(frame, f'{mode.upper()} SET', (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Get count of existing images and print to the screen
    count = {}
    y_coord = 180
    for counter, gesture in enumerate(class_names):
        count.update({gesture : len(os.listdir(f'./data/{mode}/{counter+1}-{gesture}'))})
        cv2.putText(frame, f'{counter+1} - {gesture}: {count[gesture]}', (10, y_coord), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        y_coord += 20

    # Set coordinates of the ROI
    x1 = 270
    y1 = 115
    x2 = x1+336
    y2 = y1+336

    # Draw the ROI
    cv2.rectangle(frame, (x1-2, y1-2), (x2+2, y2+2), (0, 255, 0), 2)

    # Extract the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (96, 96))

    # Show the frame
    cv2.imshow('Capturing dataset', frame)

    # # Image processing
    # roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # roi = cv2.GaussianBlur(roi, (7, 7), 0)

    # if num_frames < 30:
    #     run_avg(roi, accumWeight)
    # else:
    #     hand = segment(roi)
        
    #     if hand is not None:
    #         th, segmented = hand
    #         cv2.imshow('Thresholded', th)

    # # Draw segmented hand
    # cv2.rectangle(clone, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # num_frames += 1

    # cv2.imshow('ROI', roi)

    # Data collection
    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break
    elif key & 0xff == ord('a'):
        mode = 'training'
    elif key & 0xff == ord('b'):
        mode = 'validation'
    elif key & 0xff == ord('c'):
        mode = 'testing'
    elif key & 0xFF == ord('1'):
        cv2.imwrite(f'./data/{mode}/1-{class_names[0]}/{str(count[class_names[0]])}.png', roi)
    elif key & 0xFF == ord('2'):
        cv2.imwrite(f'./data/{mode}/2-{class_names[1]}/{str(count[class_names[1]])}.png', roi)
    elif key & 0xFF == ord('3'):
        cv2.imwrite(f'./data/{mode}/3-{class_names[2]}/{str(count[class_names[2]])}.png', roi)
    elif key & 0xFF == ord('4'):
        cv2.imwrite(f'./data/{mode}/4-{class_names[3]}/{str(count[class_names[3]])}.png', roi)
    elif key & 0xFF == ord('5'):
        cv2.imwrite(f'./data/{mode}/5-{class_names[4]}/{str(count[class_names[4]])}.png', roi)
    elif key & 0xFF == ord('6'):
        cv2.imwrite(f'./data/{mode}/6-{class_names[5]}/{str(count[class_names[5]])}.png', roi)
    elif key & 0xFF == ord('7'):
        cv2.imwrite(f'./data/{mode}/7-{class_names[6]}/{str(count[class_names[6]])}.png', roi) 
    elif key & 0xFF == ord('8'):
        cv2.imwrite(f'./data/{mode}/8-{class_names[7]}/{str(count[class_names[7]])}.png', roi)
    elif key & 0xFF == ord('9'):
        cv2.imwrite(f'./data/{mode}/9-{class_names[8]}/{str(count[class_names[8]])}.png', roi)

camera.release()
cv2.destroyAllWindows()
