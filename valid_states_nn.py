import tensorflow as tf
import numpy as np
from tensorflow import keras
from data_manip import data_manip

model = keras.Sequential([
    keras.layers.Dense(units = 9,
                       kernel_regularizer = keras.regularizers.l2(0.001),
                       input_shape = [9]),
    keras.layers.Dense(units = 100,
                       kernel_regularizer = keras.regularizers.l2(0.001),
                       activation = 'relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(units = 1000,
                       kernel_regularizer = keras.regularizers.l2(0.001),
                       activation = 'relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(units = 100,
                       kernel_regularizer = keras.regularizers.l2(0.001),
                       activation = 'relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(units = 1, activation = 'sigmoid'),
], name = 'TicTacToe Neural Network')
model.summary()

model.compile(optimizer = 'adam',
              loss = 'binary_crossentropy',
              metrics = ['accuracy', 'binary_crossentropy'])

manip = data_manip()
states = np.asarray(manip.load_states())
labels = np.asarray(manip.load_labels())
print('States shape: {}'.format(states.shape))
print('Labels shape: {}'.format(labels.shape))

cut = len(states) - len(states) // 5
print('Cut off point: {}'.format(cut))
train_states = states[:cut]
test_states = states[cut:]
print('Train states shape: {}'.format(train_states.shape))
print('Test states shape: {}'.format(test_states.shape))
train_labels = labels[:cut]
test_labels = labels[cut:]
print('Train labels shape: {}'.format(train_labels.shape))
print('Test labels shape: {}'.format(test_labels.shape))

checkpoint_path = 'weights/tictactoe'
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 save_weights_only = True,
                                                 verbose = 1)

model.load_weights(checkpoint_path)
'''
model.fit(train_states,
          train_labels,
          epochs = 10,
          batch_size = 64,
          validation_data = (test_states, test_labels),
          verbose = 2,
          callbacks = [cp_callback])
'''
predictions = model.predict(states)
print('Prediction vector shape: {}'.format(predictions.shape))

fname = 'predictions.txt'
outfile = open(fname, 'w')
for prediction in predictions:
    if prediction > 0.5:
        val = 1
    else:
        val = 0
    outfile.write(str(val) + '\n')
outfile.close()
