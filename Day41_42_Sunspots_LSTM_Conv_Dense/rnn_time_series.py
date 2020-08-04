# Sequence to sequence RNN
model = keras.models.Sequential([
    keras.layers.SimpleRNN(20, return_sequences = True, input_shape = [None, 1]),  # return_sequences = True means it outputs a sequence which is fed to the next layer
    keras.layers.SimpleRNN(20, return_sequences = True),
    keras.layers.Dense(1)
])

# the first shape is none, here tensorflow assumes that the rnn can have sequences of any length, last is one because we are using a univariate time series
model = keras.models.Sequential([
    keras.layers.SimpleRNN(20, return_sequences = True, input_shape = [None, 1]),  # return_sequences = True means it outputs a sequence which is fed to the next layer
    keras.layers.SimpleRNN(20), # It will give the output to a single dense
    keras.layers.Dense(1)
])

# Lambda layers (allows to perform arbitrary operations to expand the functionality of tensorflow keras)
model = keras.models.Sequential([
    keras.layers.Lambda(lambda x: tf.expand_dims(x, axis = -1), input_shape = [None]), # using lambda we expand the array by 1 dimension (Batch_size, no_of_timestamps, series_dimensionality), input_shape = [None] means model can take sequences of any length
    keras.layers.SimpleRNN(20, return_sequences = True),
    keras.layers.SimpleRNN(20),
    keras.layers.Dese(1),
    keras.layers.Lambda(lambda x: x * 100.0)  # By scaling the output by 100, we can help training (Default function in RNN is tanh)
])


