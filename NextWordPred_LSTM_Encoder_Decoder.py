import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#Input Text Corpus (Train Data)
corpus = [
    "the sun rises in the east",
    "the moon shines at night",
    "the stars twinkle in the sky",
    "the wind blows gently",
    "the rain falls from the clouds"
]

#Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1

#create input-output pairs
input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    print(token_list)
    for i in range(1, len(token_list)):
        input_sequences.append(token_list[:i+1])

#Pad sequences
max_seq_len = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen = max_seq_len, padding='pre')

#split into input and label
X = input_sequences[:, :-1]
y= input_sequences[:, -1]
y= tf.keras.utils.to_categorical(y, num_classes = total_words)

from tensorflow.keras.models import Model 
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense 

input_len = X.shape[1]
#Encoder
encoder_inputs = Input(shape=(input_len,))
embedding_layer = Embedding(total_words, 64)(encoder_inputs)
encoder_lstm = LSTM(64, return_state = True)
_, state_h, state_c = encoder_lstm(embedding_layer)

#Decode
decoder_inputs = Input(shape=(1,))
decoder_embedding = Embedding(total_words, 64)(decoder_inputs)
decoder_lstm = LSTM(64, return_sequences= False, return_state = False)
decoder_output = decoder_lstm(decoder_embedding, initial_state = [state_h, state_c])
output = Dense(total_words, activation = 'softmax')(decoder_output)

model = Model([encoder_inputs, decoder_inputs], output)
model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.summary()

#Training model
decoder_input_data = np.zeros((X.shape[0], 1))
model.fit([X, decoder_input_data], y , epochs = 100, verbose=1)

#creating a function to predict next word
def predict_next_word(seed_text):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen = input_len, padding = 'pre')
    decoder_input = np.zeros((1,1))
    predicted = model.predict([token_list, decoder_input], verbose=0)
    predicted_word_index = np.argmax(predicted, axis=1)[0]
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
        
print(predict_next_word("the sun rises in the"))
print(predict_next_word("the rain falls from the"))