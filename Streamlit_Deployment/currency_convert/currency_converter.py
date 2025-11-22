import streamlit as st
from forex_python.converter import CurrencyRates

st.set_page_config(page_title= "Currency Converter", layout = "centered")
st.title("Currency Converter")

c = CurrencyRates()

amount = st.number_input("Enter amount:", min_value = 0.0, format = "%.2f")
from_currency = st.selectbox("From currency: ", ["USD", "EUR", "INR", "GBP", "JPY"])
to_currency = st.selectbox("To currency: ", ["USD", "EUR", "INR", "GBP", "JPY"])

if st.button("Convert"):
    try:
        result = c.convert(from_currency, to_currency, amount)
        st.success(f"{amount: .2f} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        st.error(f"Conversion failed: {e}")