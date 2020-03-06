import keras as kr
import numpy as np
from keras.models import load_model

def abstractPredic(image, model):
    # Get the model to predict
    prediction = model.predict(image)

    # Get the array of outputs
    getPredict = np.array(prediction[0])

    # Predicted number is the index of highest value
    return np.argmax(getPredict)