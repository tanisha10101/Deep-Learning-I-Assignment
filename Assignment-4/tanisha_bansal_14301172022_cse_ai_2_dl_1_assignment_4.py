# -*- coding: utf-8 -*-
"""TANISHA_BANSAL_14301172022_CSE-AI-2_DL-1_ASSIGNMENT-4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18U4OxyG_SNo3WZEucLhTha_xVlOq6rAu

**SUBMITTED BY:- TANISHA BANSAL**

**ROLL NO:- 14301172022**

**BATCH:- CSE-AI-2**

**COURSE:- DL-1 ASSIGNMENT-4**

**Write a program to implement different neural networks for MNIST dataset by
varying number of neurons and layers.**
"""

pip install tensorflow

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Loading the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizing the input data
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encode the labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

def create_model(num_layers, num_neurons):
    model = Sequential()

    # Flattening the input layer (28x28 images to a 784-dimensional vector)
    model.add(Flatten(input_shape=(28, 28)))

    # Adding hidden layers
    for _ in range(num_layers):
        model.add(Dense(num_neurons, activation='relu'))

    # Output layer (10 neurons for 10 classes)
    model.add(Dense(10, activation='softmax'))

    # Compiling the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model

#Now, we will train it
def train_and_evaluate(num_layers_list, num_neurons_list, epochs=10):
    results = {}

    for num_layers in num_layers_list:
        for num_neurons in num_neurons_list:
            print(f"\nTraining model with {num_layers} layers and {num_neurons} neurons per layer")
            model = create_model(num_layers, num_neurons)

            # Training the model
            model.fit(x_train, y_train, epochs=epochs, batch_size=128, verbose=1, validation_data=(x_test, y_test))

            # Evaluating the model on test data
            loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

            # Storing our results
            results[(num_layers, num_neurons)] = accuracy
            print(f"Test accuracy: {accuracy:.4f}")

    return results

num_layers_list = [1, 2, 3] #layers
num_neurons_list = [32, 64, 128]  # numbers of neurons in each layer

# Train and evaluate the models
results = train_and_evaluate(num_layers_list, num_neurons_list, epochs=5)

# Display the results
print("\nSummary of results:")
for config, accuracy in results.items():
    print(f"Layers: {config[0]}, Neurons: {config[1]} --> Test Accuracy: {accuracy:.4f}")