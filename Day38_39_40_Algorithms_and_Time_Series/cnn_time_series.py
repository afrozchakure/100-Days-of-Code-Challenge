def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift = 1, drop_remainder = True)
    dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))  # Flatten the dataset to the size of our window
    # Using a shuffle buffer speeds things up, fills the element with 1st 1000 elements (say 100,000 total) and randomly picks again
    dataset = dataset.shuffle(shuffle_buffer).map(lambda window: (window[:-1], window[-1]))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset
    
# Spliting dataset into Train, Test and Validation set
split_time = 1000
time_train = time[:split_time]
x_train = series[:split_time]
time_valid = time[split_time:]
x_valid = series[split_time:]

# Performing simple linear regression
window_size = 20
batch_size = 32
shuffle_buffer_size = 1000

dataset = windowed_dataset(series, window_size, batch_size, shuffle_buffer_size)
l0 = tf.keras.layers.Dense(1, input_shape = [window_size])
model = tf.keras.models.Sequential([l0])

# Compiling compile and fit the model
model.compile(loss='mse', optimizer = tf.keras.optimizers.SGD(lr=1e-6, momentum=0.9))
model.fit(dataset, epochs=100, verbose=(0))  # 100 epochs

# Inspecting the different weights
print("Layer weights {}".format(l0.get_weights()))

# Making prediction
print(series[1:21])
model.predict(series[1:21][np.newaxis]) # np.newaxis reshapes it to the new dimension used by the model

# Making forecast for our model
forecast = []
for time in range(len(series) - window_size):
    forecast.append(model.predict(series[time:time + window_size][np.newaxis]))  # Adding the result to the forecast list
    
forecast = forecast[split_time - window_size:] # Taking forecast after the split time and loading into numpy array for charting
results = np.array(forecast)[:, 0, 0]

tf.keras.metrics.mean_absolute_error(x_valid, results).numpy()
