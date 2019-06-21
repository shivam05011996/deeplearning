import sys
import json

import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers

def execute():
    tr_f = open(sys.argv[1])
    tr_s, tr_l = get_training_samples(tr_f)
    model = create_model(2)
    model = compile_model(model)
    model = train_model(model, tr_s, tr_l)
    predict_e_o(model, np.array([200, 0]))
    save_model(model)

def save_model(model):
    model.save('even_odd.h5')

def predict_e_o(model, num):
    print(model.predict(num.reshape(1, len(num))))

def train_model(model, features, label):
    model.fit(features, label, epochs=100)

    return model

def compile_model(model):
    model.compile(loss='binary_crossentropy', optimizer='adam')

    return model

def create_model(input_dim):
    model = Sequential()
    model.add(Dense(1, input_shape=(input_dim,), activation='sigmoid'))

    return model

def get_training_samples(train_f):
    train_s, train_l = [], []
    for line in train_f:
        train_sample = json.loads(line)
        train_s.append([train_sample[0], train_sample[1]])
        train_l.append([train_sample[-1]])

    return np.array(train_s), np.array(train_l)

if __name__ == '__main__':
    execute()
