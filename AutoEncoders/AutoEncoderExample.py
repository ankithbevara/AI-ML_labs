import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, LSTM, RepeatVector, TimeDistributed, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

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

#LSTM Autoecoder
embedding_dim = 50 #Dimension that determine length of the actual word vector
latent_dim = 64 #Dimension that is used inside a embedding layer

#Encoder
inputs = Input(shape=(max_len,)) #max_len is int, but max_len, makes it tuple
embed = Embedding(input_dim = vocab_size, output_dim = embedding_dim, input_length = max_len)(inputs)
encoded = LSTM(latent_dim)(embed)

#Decoder
decoded = RepeatVector(max_len)(encoded)
decoded = LSTM(latent_dim, return_sequences = True)(decoded)
outputs = TimeDistributed(Dense(vocab_size, activation='softmax'))(decoded)

#Auto encoders
autoencoder = Model(inputs, outputs)
autoencoder.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy')

#Prepare target output (same as input but reshaped for sparse labels)
targets = np.expand_dims(padded, -1)

#Train
autoencoder.fit(padded, targets, epochs=300, verbose=0)

#Predict and decode
preds = autoencoder.predict(padded)
decoded_sentences = []
for sentence in preds:
    words = [tokenizer.index_word.get(np.argmax(vec), '') for vec in sentence]
    decoded_sentences.append(' '.join(words).strip())

#displaying results
for i, original in enumerate(sentences):
    print(f"Original: {original}")
    print(f"Reconstrcuted: {decoded_sentences[i]}\n")