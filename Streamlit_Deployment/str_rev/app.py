import streamlit as st

st.title("Text Reverser App")
st.write("Enter text below to see it reversed:")

user_input = st.text_input("Your Text")

def reverse_text(text):
    return text[::-1]

if user_input:
    st.success(f"Reversed: {reverse_text(user_input)}")