# Using Convolutional layer for time-series analysis

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(filters=32, kernel_size=5, strides = 1, padding='casual', activation = 'relu', input_shape=[None, 1]), # Since we got rid of the Lambda layer, we specify the input_shape in conv1
    tf.keras.layers.LSTM(32, return_sequences=True),
    tf.keras.layers.LSTM(32, return_sequences = True),
    tf.keras.layers.Dense(1),
    tf.keras.layers.Lambda(lambda x: x * 200.0)
])

optimizer = tf.keras.optimizers.SGD(lr=1e-5, momentum = 0.9) # Using 1e-5 as the learning rate

model.compile(loss=tf.keras.losses.Huber(), optmizer = optimizer, metrics=['mae'])

model.fit(dataset, epochs = 500)

# Updating the windowed_dataset function
def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    series = tf.expand_dims(series, axis = -1)  # using tf.expand_dims to expand the dimensions of series before processing it
    
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_reminder = True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-1], w[1:]))
    
    return ds.batch(batch_size).prefetch(1)
    
# Model (Trying to Improve model performance (Adding bidirectional layers) Does overfit the model and greater mae)
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(filters=32, kernel_size=5, strides = 1, padding='casual', activation = 'relu', input_shape=[None, 1]), # Since we got rid of the Lambda layer, we specify the input_shape in conv1
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32, return_sequences=True)),  # Try 16
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32, return_sequences = True)),
    tf.keras.layers.Dense(1),
    tf.keras.layers.Lambda(lambda x: x * 200.0)
])

