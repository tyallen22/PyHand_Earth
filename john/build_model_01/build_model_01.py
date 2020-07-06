import os
import random
from glob import glob

import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras import preprocessing

# matplotlib inline

class_names = ['INDEX_UP', 'FIST', 'PALM', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIVE_WIDE']

# Get the reference to the webcam
camera = cv2.VideoCapture(2)     # The passed arg of 1 represents the webcam (second webcam); default is 0 (laptop built-in webcam).
camera_height = 500
raw_frames_type_1 = []           # Each type represents 1 of n types of images
raw_frames_type_2 = []
raw_frames_type_3 = []
raw_frames_type_4 = []
raw_frames_type_5 = []
raw_frames_type_6 = []


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

    # Show the frame
    cv2.imshow("Capturing frames", frame)

    key = cv2.waitKey(1)

    # Wait for user to press a key, at which point program captures static webcam image
    #  and classifies it under one of the n types of classifications depending on which
    #  number user types.  Camera quits collection process if user presses 'q' key.
    #  Program outputs a message indicating number key user typed.
    if key & 0xFF == ord("q"):
        break
    elif key & 0xFF == ord("1"):
        # save the frame
        raw_frames_type_1.append(frame)
        print('1 key pressed - saved TYPE_1 frame')
    elif key & 0xFF == ord("2"):
        # save the frame
        raw_frames_type_2.append(frame)
        print('2 key pressed - Saved TYPE_2 frame')
    elif key & 0xFF == ord("3"):
        # save the frame
        raw_frames_type_3.append(frame)
        print('3 key pressed - Saved TYPE_3 frame')
    elif key & 0xFF == ord("4"):
        # save the frame
        raw_frames_type_4.append(frame)
        print('4 key pressed - Saved TYPE_4 frame')
    elif key & 0xFF == ord("5"):
        # save the frame
        raw_frames_type_5.append(frame)
        print('5 key pressed - Saved TYPE_5 frame')
    elif key & 0xFF == ord("6"):
        # save the frame
        raw_frames_type_6.append(frame)
        print('6 key pressed - Saved TYPE_6 frame')     

camera.release()
cv2.destroyAllWindows()


save_width = 399
save_height = 399

for i in range(1, 7):
    name = './data/images_type_{}'.format(i)
    os.makedirs(name, exist_ok=True)

for i, frame in enumerate(raw_frames_type_1):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_type_1/{}.png'.format(i), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_type_2):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_type_2/{}.png'.format(i), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    
for i, frame in enumerate(raw_frames_type_3):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_type_3/{}.png'.format(i), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_type_4):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_type_4/{}.png'.format(i), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    
for i, frame in enumerate(raw_frames_type_5):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_type_5/{}.png'.format(i), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    
for i, frame in enumerate(raw_frames_type_6):
    roi = frame[75+2:425-2, 300+2:650-2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('./data/images_type_6/{}.png'.format(i), cv2.cvtColor(roi,cv2.COLOR_BGR2RGB))
    
width = 96
height = 96

# Reimport libraries (although redundant here).
import os
import random
from glob import glob
from keras import preprocessing

def load_images(base_path):
    images = []
    path = os.path.join(base_path, '*.png')
    for image_path in glob(path):
        image = preprocessing.image.load_img(image_path,
                                             target_size=(width, height))
        x = preprocessing.image.img_to_array(image)

        images.append(x)
    return images


    
images_type_1 = load_images('./data/images_type_1')
images_type_2 = load_images('./data/images_type_2')
images_type_3 = load_images('./data/images_type_3')
images_type_4 = load_images('./data/images_type_4')
images_type_5 = load_images('./data/images_type_5')
images_type_6 = load_images('./data/images_type_6')


# TRAINING

X_type_1 = np.array(images_type_1)
X_type_2 = np.array(images_type_2)
X_type_3 = np.array(images_type_3)
X_type_4 = np.array(images_type_4)
X_type_5 = np.array(images_type_5)
X_type_6 = np.array(images_type_6)

print(X_type_1.shape)
print(X_type_2.shape)
print(X_type_3.shape)
print(X_type_4.shape)
print(X_type_5.shape)
print(X_type_6.shape)

X = np.concatenate((X_type_1, X_type_2, X_type_3, X_type_4, X_type_5, X_type_6), axis=0)


X = X / 255.

X.shape


from keras.utils import to_categorical

y_type_1 = [0 for item in enumerate(X_type_1)]
y_type_2 = [1 for item in enumerate(X_type_2)]
y_type_3 = [2 for item in enumerate(X_type_3)]
y_type_4 = [3 for item in enumerate(X_type_4)]
y_type_5 = [4 for item in enumerate(X_type_5)]
y_type_6 = [5 for item in enumerate(X_type_6)]


y = np.concatenate((y_type_1, y_type_2, y_type_3, y_type_4, y_type_5, y_type_6), axis=0)

y = to_categorical(y, num_classes=len(class_names))

print(y.shape)

from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Flatten, Dense
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import Adam

# Default parameters
conv_1 = 16
conv_1_drop = 0.2
conv_2 = 32
conv_2_drop = 0.2
dense_1_n = 1024
dense_1_drop = 0.2
dense_2_n = 512
dense_2_drop = 0.2
lr = 0.001

epochs = 30
batch_size = 32
color_channels = 3

def build_model(conv_1_drop=conv_1_drop, conv_2_drop=conv_2_drop,
                dense_1_n=dense_1_n, dense_1_drop=dense_1_drop,
                dense_2_n=dense_2_n, dense_2_drop=dense_2_drop,
                lr=lr):
    model = Sequential()

    model.add(Convolution2D(conv_1, (3, 3),
                            input_shape=(width, height, color_channels),
                            activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(conv_1_drop))

    model.add(Convolution2D(conv_2, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(conv_2_drop))
        
    model.add(Flatten())
        
    model.add(Dense(dense_1_n, activation='relu'))
    model.add(Dropout(dense_1_drop))

    model.add(Dense(dense_2_n, activation='relu'))
    model.add(Dropout(dense_2_drop))

    model.add(Dense(len(class_names), activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=lr),
                  metrics=['accuracy'])

    return model


import numpy as np
np.random.seed(1)             # For reproducibility

# Model with base parameters
model = build_model()

model.summary()

epochs = 20

model.fit(X, y, epochs=epochs)

# OVERWRITES OLD FILE .... BE CAREFUL
model.save('pyearth_cnn_model_200612_1744.h5')









    



