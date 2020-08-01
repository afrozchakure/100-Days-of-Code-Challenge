train_set = windowed_dataset(x_train, window_size, batch_size = 128, shuffle_buffer = shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis = -1), input_shape = [None]),
    tf.keras.layers.SimpleRNN(40, return_sequences = True),
    tf.keras.layers.SimpleRNN(40),
    tf.keras.layers.Dense(1),
    tf.keras.layers.Lambda(lamda x: x*100.0)d
])

lr_schedule = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-8 * 10**(epoch / 20))

optimizer = tf.keras.optimizers.SGD(lr = 1e-8, momentum = 0.9)
model.compile(loss = tf.keras.losses.Huber(),optimizer = optimizer, metrics = ['mae']) # Huber loss function is less sensitive to outliers

history = model.fit(train_set, epochs = 100, callbacks = [lr_schedule])

# Plot the result (We find model is optimal at lr=5e-5)

optimizer = tf.keras.optimizers.SGD(lr=5e-5, momentum=0.9)
history = model.compile(loss=tf.keras.losses.Huber(), optimizer = optimizer, metrics = ['mae'])
model.fit(dataset, epochs = 500)
