import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title= "QR CODE GENERATOR", layout = "centered")
st.title("QR Code Generator")

text = st.text_input("Enter text or URL to encode: ")

if st.button("Generate QR Code"):
    if text:
        qr = qrcode.QRCode(version = 1, box_size= 6, border =4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "black", back_color = "white")

        buf = BytesIO()
        img.save(buf, format = "PNG")
        st.image(buf.getvalue(), caption= "Your QR Code", use_column_width = True)
    else:
        st.warning("Please enter some text or a URL.")