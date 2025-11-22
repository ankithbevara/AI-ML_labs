import streamlit as st
import re

st.set_page_config(page_title = "Password Strength Checker", layout = "centered")
st.title("Password Strength Checker")

password = st.text_input("Enter your password", type="password")

def check_strength(pwd):
    score = 0
    if len(pwd) >= 8:
        score +=1
    if re.search(r"[A-Z]", pwd):
        score += 1
    if re.search(r"[a-z]", pwd):
        score += 1
    if re.search(r"[0-9]",pwd):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1
    return score

if password:
    strength = check_strength(password)
    st.write(f"Strength Score: {strength}/5")
    if strength <= 2:
        st.error("Weak Password")
    elif strength <=2:
        st.error("Weak Password")
    elif strength == 3:
        st.warning("Moderate Password")
    else:
        st.success("Strong Password")