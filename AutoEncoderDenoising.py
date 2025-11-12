#whenver you add some noise to image, the image will be blurred

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist #images/ collections of handwritten digits
from tensorflow.keras.models import Model 
from tensorflow.keras.layers import Input, Dense 
from tensorflow.keras.optimizers import Adam

#Load and Normalize MNIST data- 
(x_train, _), (x_test, _) = mnist.load_data()
x_train = x_train.astype("float32") / 255.
x_test = x_test.astype("float32") / 255.
x_train = x_train.reshape((len(x_train), 784))
x_test = x_test.reshape((len(x_test), 784))
#sample output: Downloading data from........


#Add Gaussian Noise
noise_factor = 0.5
x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape)
x_test_noisy = x_test + noise_factor * np.random.normal(loc = 0.0, scale= 1.0, size=x_test.shape)
x_train_noisy = np.clip(x_train_noisy,0.,1.)
x_test_noisy = np.clip(x_test_noisy , 0. ,1.)

#Define autoencoder model
input_img = Input(shape=(784,))
encoded = Dense(128, activation = 'relu')(input_img)
encoded = Dense(64, activation = 'relu')(encoded)
encoded = Dense(32, activation = 'relu')(encoded)

decoded = Dense(64, activation='relu')(encoded)
decoded =Dense(128, activation ='relu')(decoded)
decoded = Dense(784, activation = 'sigmoid')(decoded)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer=Adam(), loss='mse')

#Train the model
autoencoder.fit(x_train_noisy, x_train,
                epochs = 20,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test_noisy, x_test))

#Predictions using autoencoder model
decoded_imgs = autoencoder.predict(x_test_noisy)

#plot original, noisy, and denoised images
n = 10
plt.figure(figsize=(18,6))
for i in range(n):
    #original
    ax = plt.subplot(3, n, i + 1)
    plt.imshow(x_test[i].reshape(28,28), cmap='gray')
    plt.title("Original")
    plt.axis('off')

    #Noisy
    ax = plt.subplot(3, n, i + 1 + n)
    plt.imshow(x_test_noisy[i].reshape(28, 28), cmap = 'gray')
    plt.title("Noisy")
    plt.axis('off')

    #Denoised
    ax = plt.subplot(3, n, i + 1 + 2 * n)
    plt.imshow(decoded_imgs[i].reshape(28,28),cmap='gray')
    plt.title("Denoised")
    plt.axis('off')

plt.tight_layout()
plt.show()