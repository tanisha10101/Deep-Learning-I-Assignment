# -*- coding: utf-8 -*-
"""TANISHA_BANSAL_14301172022_CSE-AI _2_DL_1_ASSIGNMENT_10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kdqwAsn9ruY6UEYfq-Er73LCtLbYNZa_

**Submitted by:-**

**NAME:- TANISHA BANSAL**


**BATCH:- CSE-AI - 2 (2026)**


**ROLL NO.:- 14301172022**


**COURSE:- DEEP LEARNING PRACTICALS - EXPERIMENT 10**

##AIM: Write a program to implement the pre-trained LSTM and GRU models for text classification problem.
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, GRU, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Loading the IMDB dataset (train/test split)
max_features = 10000  # Limit the vocabulary size
maxlen = 500  # Maximum length of each text sequence

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# Padding the sequences to ensure they have the same length
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# Defining the LSTM model
def create_lstm_model():
    model = Sequential()
    model.add(Embedding(input_dim=max_features, output_dim=128, input_length=maxlen))
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation='sigmoid'))  # Binary classification
    model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    return model

# Creating LSTM model
lstm_model = create_lstm_model()

# Training the LSTM model
lstm_model.summary()
lstm_model.fit(x_train, y_train, epochs=3, batch_size=64, validation_data=(x_test, y_test))

# Define the GRU model
def create_gru_model():
    model = Sequential()
    model.add(Embedding(input_dim=max_features, output_dim=128, input_length=maxlen))
    model.add(GRU(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation='sigmoid'))  # Binary classification
    model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    return model

# Create GRU model
gru_model = create_gru_model()

# Train the GRU model
gru_model.summary()
gru_model.fit(x_train, y_train, epochs=3, batch_size=64, validation_data=(x_test, y_test))

# Evaluate LSTM Model
lstm_score = lstm_model.evaluate(x_test, y_test)
print("LSTM Model Accuracy:", lstm_score[1])

# Evaluate GRU Model
gru_score = gru_model.evaluate(x_test, y_test)
print("GRU Model Accuracy:", gru_score[1])

# Loading pre-trained GloVe embeddings
embedding_matrix = np.zeros((max_features, 128))
embedding_layer = Embedding(input_dim=max_features, output_dim=128, weights=[embedding_matrix], input_length=maxlen, trainable=False)