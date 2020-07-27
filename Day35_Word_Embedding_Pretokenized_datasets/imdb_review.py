import tensorflow as tf
print(tf.__version__)

# tf.enable_eager_execution()  # For tensorflow 1.x
# Eager execution is enabled by default in tensorflow 2.x

import tensorflow_datasets as tfds
imdb, info = tfds.load("imdb_reviews", with_info = True, as_supervised = True)

# pass imdb_reviews, return data and metadata about it

import numpy as np
train_data, test_data = imdb['train'], imdb['test']

# 25,000 for training, 25,000 for testing

training_sentences = []
training_labels = []

testing_sentences = []
testing_labels = []

# str(s.tonumpy()) is needed is Python3 instead of just s.numpy()

# The value of s and l are tensors, so by calling the numpy() method we extract their value

for s, l in train_data:
    training_sentences.append(str(s.numpy()))
    training_labels.append(l.numpy())
    
for s, l in test_data:
    testing_sentences.append(str(s.numpy()))
    testing_labels.append(l.numpy())
    
tf.Tensor(1, shape=(), dtype = int64)
tf.Tensor(1, shape=(), dtype = int64)
tf.Tensor(1, shape=(), dtype = int64)
tf.Tensor(0, shape=(), dtype = int64)
tf.Tensor(0, shape=(), dtype = int64)
tf.Tensor(1, shape=(), dtype = int64)

# When training the labels are expected to be numpy arrays
training_labels_final = np.array(training_labels)
testing_labels_final = np.array(testing_labels)

# Tokenize the sentences (Hyper-parameters)
vocab_size = 10000
embedding_dim = 16
max_length = 120
truc_type = 'post'
oov_tok = "<OOV>"

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# For training sentences (Tokenizer --> fit_on_texts --> word_index --> texts_to_sequences --> pad_sequences
tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer.fit_on_texts(training_sentences)  # Fit tokenizer onto text
word_index = tokenizer.word_index # Get word index
sequences = tokenizer.texts_to_sequences(training_sentences) # Once we get the word index we can replace the strings containing the words with the token value created for then
padded = pad_sequences(sequences, maxlen = max_length, trucating = trunc_type) # pad sequences (trucating the sentences untill they are the same length to the max_length) parameter

# Convert testing to sequences and padded form
testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(tokenizer_sequences, maxlen = max_length)


# Defining the NN (Embedding is the vectors for each word with their associated sentiment)
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length), # result is a 2D array with the lenght of sentence and the embedding dimension
    # tf.keras.layers.Flatten(),
    tf.keras.layers.GlobalAveragePooling1D(),  # Averages across the vector to flatten it out (Could be used other than flatten, and is a bit more accurate)
    tf.keras.layers.Dense(6, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

# Compiling the model and summary
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.summary()

# Fitting the model
num_epochs = 10
model.fit(padded, 
          training_labels_final, 
          epochs=num_epochs,
          validation_data = (testing_padded,
                        testing_labels_final))
# Note: - 
# Word_index is derived from the training_set, so vocabulary token exit in the test set

# Visualising the Embeddings
e = model.layers[0]
weights = e.get_weights()[0]
print(weights.shape) # shape: (vocab_size, embeddingd_dim)

# Helper function to reverse word embeddings
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Writing vectors and metadata onto files (Plots the vectos in 3-d space to visualize it)
import io

out_v = io.open('vecs.tsv', 'w', encoding='utf-8')
out_m = io.open('meta.tsv', 'w', encoding='utf-8')
for word_num in range(1, vocab_size):
    word = reverse_word_index[word_num]
    embeddings = weights[word_num]
    out_m.write(word + '\n')  # To meta-data array we just write down the words
    out_v.write('\t'.join([str(x) for x in embeddings]) + '\n')  # we write down the value of each item in the array of embeddings ie. the coefficient of each dimension on the vector for this word
    
out_v.close()
out_m.close()


# Colab code to download the two files (vecs.tsv and meta.tsv)

"""
try: 
    from google.colab import files
except ImportError:
    pass
else:
    files.download('vecs.tsv')
    files.download('meta.tsv')
"""
