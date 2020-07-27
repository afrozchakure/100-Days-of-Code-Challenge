tokenizer = Tokenizer()

data = "In the town of Athy one "
corpus = data.lower().split("\n")  # Gets list of data in lowercase

tokenizer.fit_on_texts(corpus)  # Creates dictionary of words in the overall corpus (key, value (Token for the word) pair)
total_words = len(tokenizer.word_index) + 1 

# Creating training data
input_sequences = []
for line in corpus: 
    token_list = tokenizer.texts_to_sequences([line])[0]  # Generating a token list
    for i in range(1, len(token_list)):  # Iterating over the list of tokens
        n_gram_sequences = token_list[:i+1]
        input_sequences.append(n_gram_sequences)
        
# Finding the longest sentence in the corpus
max_sequence_len = max([len(x) for x in input_sequences])

# Pre-Padding the sequences so that they are of same length (easier to extract the label this way)
input_sequences = np.array(pad_sequences(input_sequences, maxlen = max_sequence_len, padding = 'pre'))

# Turning the input_sequences into input(X) and Label(Y)
xs = input_sequences[:, :-1]
labels = input_sequences[:, -1]

# One-hot encoding the labels (list to categorical)
ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

# Creating the model (Our LSTM is carrying context forward only)
model = Sequential()
model.add(Embedding(total_words, 64, input_length=max_sequence_len - 1))
model.add((LSTM(20)))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimzer='adam', metrics=['accuracy'])
model.fit(xs, ys, epochs = 500, verbose=1)

# Creating a Bidirectional LSTM
model = Sequential()
model.add(Embedding(total_words, 64, input_length=max_sequence_len - 1))
model.add(Bidirectional(LSTM(20)))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(xs, ys, epochs = 500, verbose=1)


### Training model

seed_text = 'Laurence went to dublin'
next_words = 10

# Making predictions for next 10 words  
for _ in range(next_words):
    # Creating a token list for the words
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len -1 , padding='pre') # Padding the sequence so it matches the ones in the training set

    # Making predictions (Gives the token of the word most likely to be next in the sequence)
    predicted = model.predict_classes(token_list, verbose = 0)
    output_word = ""

    # Turn token back into a word and adding that to seed text
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " "  + output_word

print(seed_text)


# Note: The more words you predict the more likely you'll get gibberish (larger corpus of words help)
