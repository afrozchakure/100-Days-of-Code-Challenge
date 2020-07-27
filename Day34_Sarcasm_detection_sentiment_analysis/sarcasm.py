import json  # Allow to load data in json format
    
with open('sarcasm.json', 'r') as f:  
    datastore = json.load(f)
    
sentences = []
labels = []
urls = []
for item in datastore:  # Iterate through the datastore
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])
    
print(datastore)


from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)  # Will generate the word index and will initializer the tokenizer
word_index = tokenizer.word_index  # Returns words that tokenizer saw, when tokenizing sentences

# Creating sequences from text and padding them
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding = 'post')
print('\nSentences:\n', sentences[0])
print('\nPadded form:\n'padded[0])
print('\nPadded shape:\n',padded.shape)
