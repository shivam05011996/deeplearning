from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model
import matplotlib.pyplot as plt
from basescript import BaseScript

from prep_tr_te import prep_train_set, prep_test_set


train_x, train_l = prep_train_set(num_sample=100)
test_x, test_l = prep_test_set()

class CopyIntegers(BaseScript):
    DESC = 'Train a model to learn copying the integers'

    def build_model_architecture(self):
        model = Sequential()
        model.add(Dense(1, input_dim=1, activation='linear'))
        model.compile(loss='mse', optimizer='adam', metrics=['accuracy'], validation_split=0.20, shuffle=True)

        return model

    def train_model(self, model, train_x, train_l):
        model_history = model.fit(train_x, train_x, epochs=10)
        return model_history

    def evaluate_model(self, model, test_x, test_l):
        scores = model.evaluate(test_x, test_x)

        return scores

    def plot_training(self, history):
        import pdb; pdb.set_trace()
        plt.plot(history.history['acc'])
        plt.plot(history.history['loss'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()
        pass

    def run(self):
        model_arch = self.build_model_architecture()
        model_trained = self.train_model(model_acrh, train_x, train_l)
        self.plot_training(model_trained)

        scores = evaluate_model(model_trained, test_x, test_l)

if __name__ == '__main__':
    CopyIntegers().start()
