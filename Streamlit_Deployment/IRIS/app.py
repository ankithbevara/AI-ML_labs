import streamlit as st
import pandas as pd
from model import train_model

st.title("Iris Flower Classifier")

model, iris = train_model()

#Input
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

#Prediction
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns = iris.feature_names)
prediction = model.predict(input_data)[0]
st.success(f"Predicted Class: {iris.target_names[prediction]}")