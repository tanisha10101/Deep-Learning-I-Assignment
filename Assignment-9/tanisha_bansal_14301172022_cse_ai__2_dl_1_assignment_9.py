# -*- coding: utf-8 -*-
"""TANISHA_BANSAL_14301172022_CSE-AI _2_DL_1_ASSIGNMENT_9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iQdEh9Ly5ZKdGYqL8cErGOYZ61hC6t9i

**Submitted by:-**

**NAME:- TANISHA BANSAL**

**BATCH:- CSE-AI - 2 (2026)**

**ROLL NO.:- 14301172022**

**COURSE:- DEEP LEARNING PRACTICALS - EXPERIMENT 9**

**AIM: Write a program to implement LSTM and GRU for text classification problem.**
"""

pip install tensorflow

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, GRU, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb

# Parameters
vocab_size = 10000
max_length = 100
embedding_dim = 64
batch_size = 32
epochs = 5

# Load dataset (IMDb)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

# Pad sequences
x_train = pad_sequences(x_train, maxlen=max_length, padding='post', truncating='post')
x_test = pad_sequences(x_test, maxlen=max_length, padding='post', truncating='post')

# Defining LSTM model
def create_lstm_model():
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
        LSTM(64, return_sequences=False),
        Dropout(0.5),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Training and evaluating LSTM model
print("Training LSTM model...")
lstm_model = create_lstm_model()
lstm_model.summary()
lstm_model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
lstm_loss, lstm_accuracy = lstm_model.evaluate(x_test, y_test)
print(f"LSTM Test Loss: {lstm_loss}, Test Accuracy: {lstm_accuracy}")

# Parameters
vocab_size = 10000
max_length = 100
embedding_dim = 64
batch_size = 32
epochs = 5

# Load dataset (IMDb)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

# Pad sequences
x_train = pad_sequences(x_train, maxlen=max_length, padding='post', truncating='post')
x_test = pad_sequences(x_test, maxlen=max_length, padding='post', truncating='post')

# Define GRU model
def create_gru_model():
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
        GRU(64, return_sequences=False),
        Dropout(0.5),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Train and evaluate GRU model
print("Training GRU model...")
gru_model = create_gru_model()
gru_model.summary()
gru_model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
gru_loss, gru_accuracy = gru_model.evaluate(x_test, y_test)
print(f"GRU Test Loss: {gru_loss}, Test Accuracy: {gru_accuracy}")