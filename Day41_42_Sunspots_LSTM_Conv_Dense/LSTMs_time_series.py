tf.keras.backend.clear_session()  # It Clears any external variables
dataset = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)), # making a bidirectional LSTM
    tf.keras.layers.Dense(1),  # To get our output predictiona
    tf.keras.layers.Lambda(lambda x: x * 100.0)
])

model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-6, momentum=0.9))
model.fit(dataset, epochs = 100, verbose = 0)

# 2 LSTM layers (better prediction)
tf.keras.backend.clear_session()  # It Clears any external variables
dataset = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32, return_sequences=True)), # making a bidirectional LSTM
tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32))
    tf.keras.layers.Dense(1),  # To get our output prediction
    tf.keras.layers.Lambda(lambda x: x * 100.0)
])

model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-6, momentum=0.9))
model.fit(dataset, epochs = 100, verbose = 0)

# 3 LSTM layers
tf.keras.backend.clear_session()  # It Clears any external variables
dataset = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32, return_sequences=True)), # making a bidirectional LSTM
tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32,return_sequences=True))
tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(1),  # To get our output predictiona
    tf.keras.layers.Lambda(lambda x: x * 100.0)
])

model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-6, momentum=0.9))
model.fit(dataset, epochs = 100, verbose = 0)


