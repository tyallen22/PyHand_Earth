import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d,max_pool_2d
from tflearn.layers.core import input_data,dropout,fully_connected
from tflearn.layers.estimator import regression
import numpy as np
import cv2
from sklearn.utils import shuffle
import os
from glob import glob
from keras import preprocessing
from keras.utils import to_categorical

class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']


def load_images(base_path):
    images = []
    path = os.path.join(base_path, '*.png')
    count = 0
    for image_path in glob(path):
        image = preprocessing.image.load_img(image_path,
                                            target_size=(width, height))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        x = preprocessing.image.img_to_array(image)

        images.append(x)
        count += 1
        if count > 250:
            break
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


y_INDEX_UP = [0 for item in enumerate(X_INDEX_UP)]
y_V_SIGN = [1 for item in enumerate(X_V_SIGN)]
y_THUMB_LEFT = [2 for item in enumerate(X_THUMB_LEFT)]
y_THUMB_RIGHT = [3 for item in enumerate(X_THUMB_RIGHT)]
y_FIST = [4 for item in enumerate(X_FIST)]
y_FIVE_WIDE = [5 for item in enumerate(X_FIVE_WIDE)]
y_PALM = [6 for item in enumerate(X_PALM)]
y_SHAKA = [7 for item in enumerate(X_SHAKA)]
y_NOTHING = [8 for item in enumerate(X_NOTHING)]

y_train = np.concatenate((y_INDEX_UP, y_V_SIGN, y_THUMB_LEFT, y_THUMB_RIGHT, y_FIST, y_FIVE_WIDE, y_PALM, y_SHAKA), y_NOTHING, axis=0)

y_train_one_hot = to_categorical(y_train, num_classes=len(class_names))



# Define the CNN Model
tf.reset_default_graph()
convnet=input_data(shape=[None,96,96,1],name='input')
convnet=conv_2d(convnet,32,2,activation='relu')
convnet=max_pool_2d(convnet,2)
convnet=conv_2d(convnet,64,2,activation='relu')
convnet=max_pool_2d(convnet,2)

convnet=conv_2d(convnet,128,2,activation='relu')
convnet=max_pool_2d(convnet,2)

convnet=conv_2d(convnet,256,2,activation='relu')
convnet=max_pool_2d(convnet,2)

convnet=conv_2d(convnet,256,2,activation='relu')
convnet=max_pool_2d(convnet,2)

convnet=conv_2d(convnet,128,2,activation='relu')
convnet=max_pool_2d(convnet,2)

convnet=conv_2d(convnet,64,2,activation='relu')
convnet=max_pool_2d(convnet,2)

convnet=fully_connected(convnet,1000,activation='relu')
convnet=dropout(convnet,0.75)

convnet=fully_connected(convnet,3,activation='softmax')

convnet=regression(convnet,optimizer='adam',learning_rate=0.001,loss='categorical_crossentropy',name='regression')

model=tflearn.DNN(convnet,tensorboard_verbose=0)


# Shuffle Training Data
loadedImages, outputVectors = shuffle(loadedImages, outputVectors, random_state=0)

# Train model
model.fit(loadedImages, outputVectors, n_epoch=50,
           validation_set = (testImages, testLabels),
           snapshot_step=100, show_metric=True, run_id='convnet_coursera')

model.save("testmodel.tfl")

