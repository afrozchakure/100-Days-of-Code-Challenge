# Generating our dataset
dataset = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=[window_size], activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss='mse', optimizer = tf.keras.optimizers.SGD(lr=1e-6, momentum = 0.9))
model.fit(dataset, epochs = 100, verbose = 0)

tf.keras.metrics.mean_absolute_error(x_valid, results).numpy()

# Picking the optimal learning rate
dataset = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=[window_size], activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dense(1)
])

lr_schedule = tf.keras.callbacks.LearningRateScheduler(
    lambda epoch: 1e-8 * 10 ** (epoch / 20)

optimizer = tf.keras.optimizers.SGD(lr = 1e-8, momentum = 0.9)
model.compile(loss='mse', optimizer = optimizer)
history = model.fit(dataset, epochs = 100, callbacks = [lr_schedule])

## Plotting the loss per epoch against the learning rate per epoch 
lrs = 1e-8  * (10 ** (np.arange(100) / 20))
plt.semilogx(lrs, history.history['loss'])
plt.axis([1e-8, 1e-3, 0, 300])
# (Here pick the lowest point of the curve where it is relatively stable)

# Updating the learning rate
window_size = 30
dataset = windowed_dataset(x_train, window_size, batch_size, shuffle_buffer_size)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=[window_size], activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dense(1)
])


optimizer = tf.keras.optimizers.SGD(lr = 7e-6, momentum = 0.9)
model.compile(loss='mse', optimizer = optimizer)
history = model.fit(dataset, epochs = 500)

# Plot the loss calculated during the training
loss = history.history['loss']
epochs = range(len(acc))
plt.plt(epochs, loss, 'b', label = 'Training Loss')
plt.show()

# Plot all but the first 10 epochs
loss = history.history['loss']
epochs = range(10, len(acc))
plot_loss = loss[10:]
print(plot_loss)
plt.plot(epochs, plot_loss, 'b', label='Training Loss')
plt.show()

tf.keras.metrics.mean_absolute_error(x_valid, results).numpy()
