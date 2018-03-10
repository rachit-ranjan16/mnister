import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np
from configparser import ConfigParser
import os
from celery import shared_task

MNIST = 'mnist'
LEARNING_RATE = 'learning_rate'
BATCH_SIZE = 'batch_size'
EPOCHS = 'epochs'


# TODO Add Logging

class DeepLearn:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
            os.sep +
            'config' +
            os.sep +
            'appConfig.ini')
        self.score = 0
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        self.model = Sequential()

    # Asynchronous Driver Method
    @shared_task
    def init_deep_learning(self):
        self.process_data()
        self.create_model()
        self.train_model()

    def process_data(self):
        self.x_train = self.x_train.reshape(len(self.x_train), 28 * 28)
        self.x_test = self.x_test.reshape(len(self.x_test), 28 * 28)

        self.x_train = self.x_train.astype('float32')
        self.x_test = self.x_test.astype('float32')

        self.x_train /= 255
        self.x_test /= 255

        num_classes = 10
        self.y_train = keras.utils.to_categorical(self.y_train, num_classes)
        self.y_test = keras.utils.to_categorical(self.y_test, num_classes)

    def create_model(self):
        self.model.add(Dense(400, activation='relu', input_shape=(784,)))
        self.model.add(Dropout(0.4))
        self.model.add(Dense(300, activation='relu'))
        self.model.add(Dropout(0.3))
        self.model.add(Dense(10, activation='softmax'))

        learning_rate = self.config.get(MNIST, LEARNING_RATE)
        self.model.compile(loss='categorical_crossentropy',
                           optimizer=RMSprop(lr=learning_rate),
                           metrics=['accuracy'])

    def train_model(self):
        batch_size = self.config.get(MNIST, BATCH_SIZE)  # mini-batch with 128 examples
        epochs = self.config.get(MNIST, EPOCHS)
        self.model.fit(
            self.x_train, self.y_train,
            batch_size=batch_size,
            epochs=epochs,
            verbose=0,
            validation_data=(self.x_test, self.y_test))
        self.score = self.model.evaluate(self.x_test, self.y_test)

    def get_accuracy(self):
        return self.score[1]

    def predict(self, idx):
        # TODO Refactor limits into Appconfig
        if idx >= 70000:
            # TODO Refactor into logging
            print("Passed Index Out of Range")
        # TODO Refactor limits into Appconfig
        elif 0 <= idx < 60000:
            return self.model.predict(np.array([self.x_train[idx]])).argmax()
        # TODO Refactor limits into Appconfig
        elif 60000 <= idx < 70000:
            idx %= self.x_train.shape[0]
            return self.model.predict(np.array([self.x_test[idx]])).argmax()
