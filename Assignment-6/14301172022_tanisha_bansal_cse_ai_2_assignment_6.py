# -*- coding: utf-8 -*-
"""14301172022_TANISHA_BANSAL_CSE_AI_2_ASSIGNMENT-6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19KO2-emmyFxZxJcDEjn5cPB_vCbOhH2c

**Submitted by:-**

**NAME:- TANISHA BANSAL**

**BATCH:- CSE-AI - 2 (2026)**

**ROLL NO.:- 14301172022**

**COURSE:- DEEP LEARNING PRACTICALS - EXPERIMENT 6**

**AIM: Write a program to implement AlexNet for image classification.**
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

# Load and preprocess the CIFAR-10 dataset
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Normalize pixel values to range [0, 1]
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# One-hot encode labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Define the AlexNet model
def create_alexnet(input_shape, num_classes):
    model = Sequential([
        # Layer 1
        Conv2D(96, (11, 11), strides=(4, 4), activation='relu', input_shape=input_shape, padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same'),

        # Layer 2
        Conv2D(256, (5, 5), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same'),

        # Layer 3
        Conv2D(384, (3, 3), activation='relu', padding='same'),
        Conv2D(384, (3, 3), activation='relu', padding='same'),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same'),

        # Flatten and Fully Connected Layers
        Flatten(),
        Dense(4096, activation='relu'),
        Dropout(0.5),
        Dense(4096, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax'),
    ])
    return model

# Create the model
input_shape = X_train.shape[1:]  # Extract input shape from training data
num_classes = 10  # Number of classes (e.g., for CIFAR-10 dataset)

alexnet = create_alexnet(input_shape, num_classes)

# Compile the model
alexnet.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Summary of the model
alexnet.summary()

# Evaluate the model
test_loss, test_accuracy = alexnet.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Save the model
alexnet.save('alexnet_cifar10.h5')

# Train the model
history = alexnet.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2,
    verbose=1
)