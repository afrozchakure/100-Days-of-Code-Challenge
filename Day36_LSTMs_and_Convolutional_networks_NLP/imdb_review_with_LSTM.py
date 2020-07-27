# Without LSTM
imdb, info = tfds.load('imdb_review", with_infor = True, as_supervised = True)

model = tf.keras.Sequential([   
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(6, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

# Trainable parameters = 171,533 parameters

# With LSTM
imdb, info = tfds.load('imdb_review", with_infor = True, as_supervised = True)

model = tf.keras.Sequential([   
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(6, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

# Trainable parameters = 30,129

# Using GRU
imdb, info = tfds.load('imdb_review", with_infor = True, as_supervised = True)

model = tf.keras.Sequential([   
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.GRU(32)),
    tf.keras.layers.Dense(6, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

# Trainable parameters = 169,997 parameters

# With Conv1D
imdb, info = tfds.load('imdb_review", with_infor = True, as_supervised = True)

model = tf.keras.Sequential([   
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
    tf.keras.layers.Conv1D(128, 5, activation ='relu'),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(6, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

# Trainable parameters = 171,149 parameters
