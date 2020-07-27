import tensorflow as tf

# Using the imdb_subwords dataset
import tensorflow_datasets as tfds
imdb, infor = tfds.load('imdb_review/subwords8k', with_info = True, as_supervised = True)

# Getting access to train and test data
train_data, test_data = imdb['train'], imdb['test']

# Accessing the subwords tokenizer
tokenizer = info.features['text'].encoder

print(tokenizer.subwords)  # Printing the subwords tokenizer

# To see how it encodes and decodes string

sample_string = 'TensorFlow, from basics to mastery'

tokenized_string = tokenizer.encode(sample_string)
print('Tokenized string is {}'.format(tokenized_string))

original_string = tokenizer.decode(sample_string)
print('The original string: {}'.format(original_string))

# To see value of each token (id ---> token), here puncuation is maintained
for tf in tokenized_string:
    print('{} ---> {}'.format(tf, tokenizer.decode([ts])))
    
# Creating the model (Trying to flatten it will cause tensorflow to crash)  
embedding_dim = 64
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(tokenizer.vocab_size, embedding_dim),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(6, activation = 'relu')
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

# Compile and train the model
num_epochs = 10
model.compile(loss='binary_crossentropy', 
            optimizer = 'adam',
            metrics = ['accuracy'])

history = model.fit(train_data, 
                    epochs = num_epochs, 
                    validation_data = test_data)

# Visualizing the result
import matplotlib.pyplot as plt

def plot_graphs(history, string):
    plt.plot(history.history[string], 
    plt.plot(history.history['val_' + string])
    plt.xlabel('Epochs')
    plt.ylabel(string)
    plt.legend([string, 'val_' + string])
    plt.show()
    
plot_graphs(history, 'acc')
plot_graphs(history, 'loss')

print(model.summary())



