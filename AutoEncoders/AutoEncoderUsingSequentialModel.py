import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, RepeatVector, TimeDistributed, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#CHECK AutoEncoderExample.py for all comments

#Sameple Corpus
sentences = [
    "hello how are you",
    "good morning",
    "what is your name",
    "have a nice day",
    "See you soon",
    "thank you very much",
    "how can i help you",
    "nice to meet you"
]

#Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
vocab_size = len(tokenizer.word_index) + 1
max_len = max(len(s.split()) for s in sentences)

sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, maxlen = max_len, padding = 'post')

#prepare target output ( same as input, reshaped for sparse labels )
targets = np.expand_dims(padded, -1)

#Sequential Model
#check AutoEncoderExample to understand what these are
embedding_dim = 50 
latent_dim = 64

model = Sequential([
    Embedding(input_dim = vocab_size, output_dim = embedding_dim, input_length = max_len),
    LSTM(latent_dim),
    RepeatVector(max_len),
    LSTM(latent_dim, return_sequences = True),
    TimeDistributed(Dense(vocab_size, activation='softmax'))
])

model.compile(optimizer = 'adam', loss= 'sparse_categorical_crossentropy')
model.summary()

#Train
model.fit(padded, targets, epochs = 300, verbose = 0)

#predict and decode
preds = model.predict(padded)
decoded_sentences = []
for sentence in preds:
    words=[tokenizer.index_word.get(np.argmax(vec), '') for vec in sentence]
    decoded_sentences.append(' '.join(words).strip())

#Display results
for i, original in enumerate(sentences):
    print(f"Original: {original}")
    print(f"Reconstrcuted: {decoded_sentences[i]}\n")
