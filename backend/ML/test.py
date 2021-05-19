# -*- coding: utf-8 -*-
"""running_wav

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J4b6w-ChZJBrmlym16Sko8YGSYjGZ0Ni
"""

# mount drive


import keras
from keras.layers import Activation, Dense, Dropout, Conv2D, \
                         Flatten, MaxPooling2D
from keras.models import Sequential
from keras.models import load_model
import librosa
import librosa.display
import numpy as np
import pandas as pd
import time

class machine_learning:
  def detecting(audio_path):
    #path of model
    model = load_model('./classify_wav.h5')
    y, sr = librosa.load(audio_path,offset=0, duration=0.72)
    ps = librosa.feature.melspectrogram(y=y, sr=sr)
    D = []
    D.append( (ps,1) )
    X_train, y_train = zip(*D)
    X_train = np.array([x.reshape( (128, 32, 1) ) for x in X_train])
    y_train = np.array(keras.utils.to_categorical(y_train, 10))
    score = model.evaluate(
	  x=X_train,
	  y=y_train,verbose=0)
    return score[0]

m = machine_learning
print(m.detecting('test.wav'))

