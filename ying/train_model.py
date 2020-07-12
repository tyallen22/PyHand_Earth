# IGNORE THIS FILE FOR NOW

import os
import numpy as np
from glob import glob
from keras import preprocessing
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.models import Sequential
#from keras.layers import BatchNormalization
from keras.layers.core import Activation, Dropout, Flatten, Dense
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import Adam, SGD
#from tensorflow.keras import regularizers
#from tensorflow.keras.callbacks import ReduceLROnPlateau
from sklearn.model_selection import train_test_split
from matplotlib.pyplot import imread, imshow, subplots, show

class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']

width = 96
height = 96
color_channels = 3


def load_images(base_path):
    images = []
    path = os.path.join(base_path, '*.png')
    for image_path in glob(path):
        image = preprocessing.image.load_img(image_path,
                                            target_size=(width, height))
        x = preprocessing.image.img_to_array(image)

        images.append(x)
    return images



images_INDEX_UP = load_images('./data/images_INDEX_UP')
images_V_SIGN = load_images('./data/images_V_SIGN')
images_THUMB_LEFT = load_images('./data/images_THUMB_LEFT')
images_THUMB_RIGHT = load_images('./data/images_THUMB_RIGHT')
images_FIST = load_images('./data/images_FIST')
images_FIVE_WIDE = load_images('./data/images_FIVE_WIDE')
images_PALM = load_images('./data/images_PALM')
images_SHAKA = load_images('./data/images_SHAKA')
images_NOTHING = load_images('./data/images_NOTHING')


# Prepare images as tensors
X_INDEX_UP = np.array(images_INDEX_UP)
X_V_SIGN = np.array(images_V_SIGN)
X_THUMB_LEFT = np.array(images_THUMB_LEFT)
X_THUMB_RIGHT = np.array(images_THUMB_RIGHT)
X_FIST = np.array(images_FIST)
X_FIVE_WIDE = np.array(images_FIVE_WIDE)
X_PALM = np.array(images_PALM)
X_SHAKA = np.array(images_SHAKA)
X_NOTHING = np.array(images_NOTHING)

# Build one big array containing all images
X = np.concatenate((X_INDEX_UP, X_V_SIGN, X_THUMB_LEFT, X_THUMB_RIGHT, X_FIST, X_FIVE_WIDE, X_PALM, X_SHAKA, X_NOTHING), axis=0)

# Rescale color pixels from 0-255 to 0-1 to make model work better
X = X.astype('float32')
X = X / 255

# Create a y_train, using nums 0-8 as labels, i.e. 0 to indicate INDEX_UP, and 2 to indicate V_SIGN, etc.
y_INDEX_UP = [0 for item in enumerate(X_INDEX_UP)]
y_V_SIGN = [1 for item in enumerate(X_V_SIGN)]
y_THUMB_LEFT = [2 for item in enumerate(X_THUMB_LEFT)]
y_THUMB_RIGHT = [3 for item in enumerate(X_THUMB_RIGHT)]
y_FIST = [4 for item in enumerate(X_FIST)]
y_FIVE_WIDE = [5 for item in enumerate(X_FIVE_WIDE)]
y_PALM = [6 for item in enumerate(X_PALM)]
y_SHAKA = [7 for item in enumerate(X_SHAKA)]
y_NOTHING = [8 for item in enumerate(X_NOTHING)]

# Build one big array with all y label values
y_train = np.concatenate((y_INDEX_UP, y_V_SIGN, y_THUMB_LEFT, y_THUMB_RIGHT, y_FIST, y_FIVE_WIDE, y_PALM, y_SHAKA, y_NOTHING), axis=0)

# Convert y_train to one_hot encodings
y_train_one_hot = to_categorical(y_train, num_classes=len(class_names))

# X_train, X_test, y_train, y_test = train_test_split(X, y_train_one_hot, test_size=0.15, random_state=42, stratify=??)


# =======================================================
# CONFIGURE CONVOLUTIONAL NETWORK
# =======================================================


def build_model():
    model = Sequential()

    # model.add(Convolution2D(32, (3, 3),
    #                         input_shape=(width, height, color_channels),
    #                         activation='relu',
    #                         padding='same',
    #                         kernel_regularizer=regularizers.l2(0.01)))
    model.add(Convolution2D(16, (3, 3),
                            input_shape=(width, height, color_channels),
                            padding='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(32, (3, 3), activation='relu', padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    # Flatten cube-like format of neurons into one row
    model.add(Flatten())
        
    # Dense FC layer
    model.add(Dense(128))

    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    #model.add(BatchNormalization())

    model.add(Dense(len(class_names)))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(learning_rate=0.001),
                  metrics=['accuracy'])

    return model


np.random.seed(1)  # For reproducibility

model = build_model()
#model = test_build()
model.summary()

#reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, verbose=1, min_lr=0.001)
#model.fit(X, y_train_one_hot, batch_size=32, epochs=20, validation_split=0.2, callbacks=[reduce_lr])

model.fit(X, y_train_one_hot, batch_size=1, epochs=20, validation_split=0.15, verbose=1)

model.save('pyearth_cnn_model_new.h5')
