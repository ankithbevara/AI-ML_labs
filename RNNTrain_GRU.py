import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense

#Load IMDB Dataset
vocab_size = 10000 #only consider the top 10,000 words
maxlen = 200 #cut reviews after 200 words

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = vocab_size)

# Pad sequences to ensure uniform input length
x_train = pad_sequences(x_train, maxlen= maxlen)
x_test = pad_sequences(x_test, maxlen= maxlen)

# Build the LSTM Model
model = Sequential([
    Embedding(input_dim= vocab_size, output_dim = 128, input_length=maxlen),  #giving input to embedding layer given to GRU
    GRU(64, dropout=0.2, recurrent_dropout = 0.2), #64 neurons, dropout is used in order to avoid the overfitting of models) why 64? (it is hyper parameter, you can take 50 0r 120 doesnt matter)
    Dense(1, activation = 'sigmoid') #Output Layer (Binary Classificaition) #1 neuron, sigmoid is a activation function for binary classification
])


#Note: In case of multi class classification, we use softmax funtion

#Compiling the model
model.compile(loss= 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy']) #solving using adam's optimizer

#Train the model
model.fit(x_train,y_train, epochs=5, batch_size=64, validation_split = 0.2)

#Evaluating the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")