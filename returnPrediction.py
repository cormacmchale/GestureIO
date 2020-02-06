import keras as kr
import numpy as np
from keras.models import load_model
def abstractPredic(image, model):
    #get the model to predict
    prediction = model.predict(image)
    #get the array of outputs
    getPredict = np.array(prediction[0])
    #predicted number is the index of highest value
    return np.argmax(getPredict)