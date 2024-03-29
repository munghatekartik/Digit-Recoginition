# -*- coding: utf-8 -*-
"""DigitRecognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gIEocERZDqHxeRe7BXOiBZlcjtkEfBSI
"""

from __future__ import absolute_import, division, print_function, unicode_literals

#import Tensorflow
import tensorflow as tf

"""Load and prepare the MNIST Dataset, Convert the samples from integers to floating point numbers."""

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0

"""Bulid the Sequential model by stacking layers. Choosing an optimizer and loss function for training."""

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation = 'softmax')
])

model.compile(optimizer = 'adam', loss= 'sparse_categorical_crossentropy')

"""Train and evaluate the model"""

model.fit(x_train, y_train, epochs = 50)
model.evaluate(x_test, y_test)

