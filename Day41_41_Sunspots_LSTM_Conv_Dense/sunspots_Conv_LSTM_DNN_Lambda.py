window_size = 60
batch_size = 64
train_set = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(filters=32, kernel_size=5, strides = 1, padding='causal', activation='relu', input_shape = [None, 1]),
    # Output from above fed to 2 LSTMs
    tf.keras.layers.LSTM(32, return_sequences = True),
    tf.keras.layers.LSTM(32, return_sequences = True),
    # Output from above fed to 3 Dense
    tf.keras.layers.Dense(30, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dense(1),
    # As our numbers are in 1 to 400 range, multiplying x by 400
    tf.keras.layers.Lambda(lambda x: x * 400)
])

lr_schedule = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-8 * 10**(epoch/20))
optimizer = tf.keras.optimizers.SGD(lr=1e-8, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(), optimizer=optimizer, metrics=['mae'])
history = model.fit(train_set, epochs = 100, callbacks=[lr_schedule])

# Since there is a lot of noise in training loss (changing batch_size to 256
window_size = 60
train_set = windowed_dataset(x_train, window_size, batch_size=256, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(filters=32, kernel_size=5, strides = 1, padding='causal', activation='relu', input_shape = [None, 1]),
    # Output from above fed to 2 LSTMs
    tf.keras.layers.LSTM(32, return_sequences = True),
    tf.keras.layers.LSTM(32, return_sequences = True),
    # Output from above fed to 3 Dense
    tf.keras.layers.Dense(30, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dense(1),
    # As our numbers are in 1 to 400 range, multiplying x by 400
    tf.keras.layers.Lambda(lambda x: x * 400)
])

lr_schedule = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-8 * 10**(epoch/20))
optimizer = tf.keras.optimizers.SGD(lr=1e-8, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(), optimizer=optimizer, metrics=['mae'])
history = model.fit(train_set, epochs = 100, callbacks=[lr_schedule])

# The training loss needs to be regularized (since the rows are 3000 and not evenly divisible by 2, changing the window size to satisfy divisiblity - Noise increased a bit in training loss
train_set = windowed_dataset(x_train, window_size=60, batch_size=250, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(filters=60, kernel_size=5, strides = 1, padding='causal', activation='relu', input_shape = [None, 1]),
    # Output from above fed to 2 LSTMs
    tf.keras.layers.LSTM(60, return_sequences = True),
    tf.keras.layers.LSTM(60, return_sequences = True),
    # Output from above fed to 3 Dense
    tf.keras.layers.Dense(30, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dense(1),
    # As our numbers are in 1 to 400 range, multiplying x by 400
    tf.keras.layers.Lambda(lambda x: x * 400)
])

lr_schedule = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-8 * 10**(epoch/20))
optimizer = tf.keras.optimizers.SGD(lr=1e-8, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(), optimizer=optimizer, metrics=['mae'])
history = model.fit(train_set, epochs = 100, callbacks=[lr_schedule])


# Note: 
"""
If the Training loss shows a lot of fluctuations, try changing the batch size, it reduces those fluctuations a bit
"""
