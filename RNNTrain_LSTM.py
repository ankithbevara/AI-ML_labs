import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
'''
#Load IMDB Dataset
vocab_size = 10000 #only consider the top 10,000 words
maxlen = 200 #cut reviews after 200 words

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = vocab_size)

# Pad sequences to ensure uniform input length
x_train = pad_sequences(x_train, maxlen= maxlen)
x_test = pad_sequences(x_test, maxlen= maxlen)

# Build the LSTM Model
model = Sequential([
    Embedding(input_dim= vocab_size, output_dim = 128, input_length=maxlen),  #giving input to embedding layer given to LSTM
    LSTM(64, dropout=0.2, recurrent_dropout = 0.2), #64 neurons, dropout is used in order to avoid the overfitting of models) why 64? (it is hyper parameter, you can take 50 0r 120 doesnt matter)
    Dense(1, activation = 'sigmoid') #Output Layer (Binary Classificaition) #1 neuron, sigmoid is a activation function for binary classification
])


#Note: In case of multi class classification, we use softmax funtion

#Compiling the model
model.compile(loss= 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy']) #solving using adam's optimizer

#Train the model
model.fit(x_train,y_train, epochs=10, batch_size=64, validation_split = 0.2)

#Evaluating the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")
'''

import numpy as np #to create data
import matplotlib.pyplot as plt #to visualize
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense #dense layer available in tensorflow

#Generate Synthetic sine wave data
def generate_data(seq_length=50, total_samples=1000):
    x = np.linspace(0, 100, total_samples)
    y = np.sin(x)
    data = []
    labels= []
    for i in range(len(y) - seq_length):
        data.append(y[i:i+seq_length])
        labels.append(y[i+seq_length])
    return np.array(data), np.array(labels)

#prepare data
seq_length = 50
X, y = generate_data(seq_length)
X = X.reshape((X.shape[0],X.shape[1],1)) #Reshape for LSTM input

#Split into train and test
split = int(0.8 * len(X)) #80-20 to rain data
X_train, X_test = X[:split], X[:split]
y_train, y_test = y[:split], y[:split]

#Building LSTM Layer
model = Sequential([ #it doesnt required embedding layer because we are dealing with time data not text data
    LSTM(64, input_shape=(seq_length, 1)),
    Dense(1) #Liner Activation
])

#Compiling Model
model.compile(optimizer='adam', loss='mse') #since we are dealing with numerics, we will use mean square error(mse)
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1) #0.1=10%

#Predict and Plotting
y_pred = model.predict(X_test)
plt.plot(y_test, label = 'True')
plt.plot(y_pred, label = 'predicted')
plt.legend()
plt.title('LSTM Time Series Forecasting')
plt.show()