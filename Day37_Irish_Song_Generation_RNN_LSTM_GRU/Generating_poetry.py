data = open('/tmp/irish-lyrics-eof.txt').read()

model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len - 1))
model.add(Bidirectional(LSTM(150)))
model.add(Dense(total_words, activation='softmax'))
adam = Adam(lr = 0.01)  # Instead of default, creating own adam optimizer
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
model.fit(xs, ys, epochs = 100, verbose=1)



