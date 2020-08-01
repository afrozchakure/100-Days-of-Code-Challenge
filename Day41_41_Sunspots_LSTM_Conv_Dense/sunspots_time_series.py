import csv
time_steps = []
sunspots = []

with open('/tmp/sunspots.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader)  # Reads the first line and throws it away
    for row in reader: # Loops through the reader, reading the file line-by-line
        sunspots.append(float(row[2]))  # Converting it to float and appending it to sunspots list
        time_step.append(int(row[0]))
        
# Converting our lists to numpy arrays
series = np.array(sunspots)
time = np.array(time_steps)

# Splitting our series into training and validation
split_time = 3000 # We have 3500 items of data (1000 is a bad split)
time_train = time[:split_time]
x_train = series[:split_time]
time_valid = time[split_time:]
x_valid = series[split_time:]

window_size = 20 # Changing the window size to 132, which is 11 year worth of data
batch_size = 32
shuffle_buffer_size = 1000

# Creating windowed dataset (To turn series into a dataset we can train on)
def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    dataset = tf.data.Dataset.from_tensor_slice(series)
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder = True),
    dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer).map(lambda window: (window[:-1], window[-1]))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset
    
# Trian and tune the model
dataset = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=[window_size], activation = 'relu'),  # Try value 30
    tf.keras.layers.Dense(10, activation = 'relu'), # Try value 15
    tf.keras.layers.Dense(1)
])

model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-6, momentum=0.9))
model.fit(dataset, epochs = 10, verbose = 0) # changing lr to 1e-7

# Note: We don't need a big window size like 132, we should look for a lot closer window size like 30
# Increasing the number of units in dense layer wasn't worth the time and effort

# Making prediction
model.predict(series[3205:3235][np.newaxis])

# Improving predictions (different setup)
split_time = 3000
window_size = 60

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(20, input_shape=[window_size], activatin = 'relu'),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-7, momentum = 0.9))
