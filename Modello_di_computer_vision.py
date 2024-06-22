import pandas as pd
import numpy as np

import tensorflow as tf

import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import InputLayer, Input, Conv2D
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.models import Model
from tensorflow.keras.backend import clear_session
from sklearn.metrics import classification_report

cifar10 = tf.keras.datasets.cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
labels = ['airplane','automobile','bird','cat','deer','dog',\
          'frog','horse','ship','truck']

for dataset in [y_train,y_test]:

  for i in range(dataset.shape[0]):
    if labels[dataset[i][0]] in ['airplane','automobile','ship','truck']:
      dataset[i][0] = 1
    else:
      dataset[i][0] = 0

plt.figure(figsize=(2,2))
indx = np.random.choice(range(50000))
plt.imshow(x_train[indx])
plt.title(y_train[indx][0]);

x_train, x_test = x_train / 255.0, x_test / 255.0
y_train, y_test = y_train.flatten(), y_test.flatten()

cnn = Sequential([
    InputLayer(input_shape=(32,32,3)),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPool2D(),

    Conv2D(32, (3, 3), activation='relu', padding='same'),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPool2D(),

    Conv2D(32, (3, 3), activation='relu', padding='same'),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPool2D(),
    Flatten(),
    Dense(1024, activation='relu'),
    Dense(2, activation='softmax')])

cnn.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

hist1 = cnn.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5)

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(hist1.history['accuracy'], label='acc')
plt.plot(hist1.history['val_accuracy'], label='val_acc')
plt.legend()
plt.subplot(1,2,2)
plt.plot(hist1.history['loss'], label='loss')
plt.plot(hist1.history['val_loss'], label='val_loss')
plt.legend()

y_pred = np.argmax(cnn.predict(x_test,verbose=False),axis=1)

y_pred

print(classification_report(y_test,y_pred))

plt.figure(figsize=(2,2))
indx = np.random.choice(range(x_test.shape[0]))
print(np.argmax(cnn.predict(x_test[indx:indx+1,:],verbose=False).reshape(-1)))
plt.imshow(x_test[indx])

