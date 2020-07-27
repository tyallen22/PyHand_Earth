from keras import preprocessing
from keras.models import load_model
import numpy as np
import random

class_names = ['INDEX_UP', 'V_SIGN', 'THUMB_LEFT', 'THUMB_RIGHT', 'FIST', 'FIVE_WIDE', 'PALM', 'SHAKA', 'NOTHING']
model = load_model('pyearth_cnn_model_0724.h5')

for counter, gesture in enumerate(class_names):
    num = random.randint(0, 99)
    oh = preprocessing.image.load_img(f'./data/testing/{counter+1}-{gesture}/{num}.png')
    yea = np.expand_dims(oh, axis=0)
    predictions = model.predict(yea)
    print(f'The type predicted is {class_names[np.argmax(predictions)]}')
