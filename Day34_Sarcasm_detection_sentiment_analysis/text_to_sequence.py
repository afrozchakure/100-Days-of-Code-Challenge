import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences  # Adding padding

sentences = [
    'I love my dog', 
    'I love my cat', 
    'You love my dog!', 
    'Do you think my dog is amazing?'
]

tokenizer = Tokenizer(num_words = 100, oov_token='<OOV>') # <OOV> words that are 'out of vocabalary'
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

# Tokenizer called to get texts to sequences and turns them into a set of sequences
sequences = tokenizer.texts_to_sequences(sentences)  

# Passing sequences to pad_sequences
padded = pad_sequences(sequences, padding = 'post', truncating='post', maxlen = 5) 

# Its the new dictionary
print(word_index)

# list of sentences that have been encoded into integer list with token replacing the word
print(sequences)

print("\nPadded Sequence:\n",padded)  # The sentences are padded

# Test Data
test_data = [
    'i really love my dog', 
    'my dog loves my manatee'
]

test_seq = tokenizer.texts_to_sequences(test_data)
print("\nTest Sequence:\n", test_seq)

# Note:
# Padding is after the sentence (can be changed)--> setting max no. of word in sentences to 5, lose information from the end of sentence using truncating = 'post'
