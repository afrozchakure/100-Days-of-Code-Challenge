import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

# Tokenizer helps generate a dictionary of word encodings and creating vectors out of the sentences

sentences = [
    'I love my dog',
    'I, love my cat', 
    'You love my dog!',  # It will ignore ',' and '!'
]  # Sentences as an array

# Creating an instance of the tokenizer (takes 100 words by volume and just encode those)
tokenizer = Tokenizer(num_words = 100) 
 
# Takes in the data and then encodes it
tokenizer.fit_on_texts(sentences)

# It provides the word index property which returns a dictionary containing key-value pair where (key --> word) and (value --> token) for that word
word_index = tokenizer.word_index
print(word_index)

# Note: 
# Tokenizer strips puntuation out

sequences = tokenizer.texts_to_sequences(sentences)
print(sequences)
