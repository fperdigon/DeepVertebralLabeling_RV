# DeepVertebralLabeling_RV
#
# author: Francisco Perdigon Romero
# email: francisco.perdigon@polymtl.ca
#        fperdigon88@gmail.com

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D, concatenate, Input
from keras.losses import mean_squared_error
from keras import backend as K

def deep_vl_rv_model(size_val):
    input_shape = (size_val, size_val, 1)
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(9, 9),
                     activation='relu',
                     strides=(2,2),
                     padding='same',
                     input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(64, (9,9), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(128, (9,9), activation='relu'))
    model.add(Conv2D(128, (5,5), activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='linear'))
    return model

def classic_l2_euclidean(p1=(1,1), p2=(0,0)):
    return(float(math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1],2))))

def euc_dist_keras(y_true, y_pred):
    return ((K.sqrt(K.sum(K.square(y_true - y_pred), axis=-1, keepdims=True))) * size_val)

def mse_dist(y_true, y_pred):
    return (mean_squared_error(y_true, y_pred) * size_val)
