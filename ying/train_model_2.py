# IGNORE THIS FILE FOR NOW

from PIL import Image
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split

import keras
from keras.models import Sequential
from keras.layers import Activation, BatchNormalization, Dense, Dropout, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from tensorflow.keras.utils import plot_model

# Setting random seeds for reproducibility
seed_value = 1

# Create a data generator
# datagen = ImageDataGenerator(rescale=1/.255,
#                              width_shift_range=0.2,
#                              height_shift_range=0.2,
#                              brightness_range=(0.1, 0.9),
#                              zoom_range=[0.5, 1.5],
#                              channel_shift_range=150.0,
#                              validation_split=0.2)

# Initialize parameters
TRAIN_DIR = './data/training'
TEST_DIR = './data/testing'
datagen = ImageDataGenerator(rescale=1/.255,
                             validation_split=0.2)
                             
class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']
batch_size=32
nb_epochs=50
width = 96
height = 96
color_channels = 3

# Load and iterate training dataset
train_it = datagen.flow_from_directory(TRAIN_DIR, 
                                       target_size=(96, 96), 
                                       class_mode='categorical', 
                                       batch_size=batch_size,
                                       subset='training',
                                       seed=seed_value)

# Load and iterate validation dataset
validation_it = datagen.flow_from_directory(TRAIN_DIR,
                                     target_size=(96, 96),
                                     class_mode='categorical',
                                     batch_size=batch_size,
                                     subset='validation',
                                     seed=seed_value)

# Load and iterate testing dataset
test_it = datagen.flow_from_directory(TEST_DIR,
                                     target_size=(96, 96),
                                     class_mode='categorical',
                                     batch_size=batch_size,
                                     seed=seed_value)

# BUILD MODEL
model = Sequential()

# model.add(Convolution2D(16, (3, 3),
#                         input_shape=(width, height, color_channels),
#                         padding='same'))                      
# model.add(Activation('relu'))
# model.add(BatchNormalization())
# model.add(Convolution2D(16, (3, 3),
#                         input_shape=(width, height, color_channels),
#                         padding='same'))                      
# model.add(Activation('relu'))
# model.add(BatchNormalization())   
# model.add(Convolution2D(32, (3, 3), activation='relu', padding='same'))
# model.add(Activation('relu'))
# model.add(BatchNormalization()) 
# model.add(Convolution2D(32, (3, 3), activation='relu', padding='same'))
# model.add(Activation('relu'))
# model.add(BatchNormalization())   
# model.add(Convolution2D(64, (3, 3), activation='relu', padding='same'))
# model.add(Activation('relu'))
# model.add(BatchNormalization())
# model.add(Convolution2D(64, (3, 3), activation='relu', padding='same'))
# model.add(Activation('relu'))
# model.add(BatchNormalization())
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))

# # Flatten cube-like format of neurons into one row
# model.add(Flatten())
    
# # Dense FC layer
# model.add(Dense(128))
# model.add(Activation('relu'))
# model.add(Dropout(0.5))


# model.add(Dense(len(class_names)))
# model.add(Activation('softmax'))

model.add(Convolution2D(16, (3, 3),
                        input_shape=(width, height, color_channels),
                        activation='relu',
                        padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))

model.add(Convolution2D(32, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
    
model.add(Flatten())
    
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(len(class_names), activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001),
              metrics=['accuracy'])

model.summary()
#steps_per_epoch = number of images in whole dataset / batch_size
model.fit(train_it, 
          steps_per_epoch=train_it.samples // batch_size,
          validation_data=validation_it, 
          validation_steps=validation_it.samples // batch_size,
          epochs=nb_epochs)

print('EVALUATING MODEL WITH TESTING SET.....')
score = model.evaluate(test_it)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save('pyearth_cnn_model_ugh.h5')
