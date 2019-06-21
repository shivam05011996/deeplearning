import sys
import json

import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers


def get_training_samples(train_f):
    train_s, train_l = [], []
    for line in train_f:
        train_sample = json.loads(line)
        train_s.append([train_sample[0], train_sample[1]])
        train_l.append([train_sample[-1]])

    return np.array(train_s), np.array(train_l)

def create_model(input_dim):
    model = Sequential()
    model.add(Dense(2, input_shape=(input_dim,), activation='softplus'))
    model.add(Dense(1, input_shape=(input_dim,), activation='softplus'))

    return model

def compile_model(model):
    model.compile(loss='mse', optimizer='adam')

    return model

def train_model(model, features, label):
    model.fit(features, label, epochs=50)

    return model

def predict_sum(model, t):
    print(model.predict(t.reshape(1, len(t))))

def save_model(model):
    model.save('summation.h5')


def execute():
    tr_f = open(sys.argv[1])
    tr_s, tr_l = get_training_samples(tr_f)
    model = create_model(2)
    model = compile_model(model)
    model = train_model(model, tr_s, tr_l)
    predict_sum(model, np.array([89, 100]))
    save_model(model)

if __name__ == '__main__':
    execute()


