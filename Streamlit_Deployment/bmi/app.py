import streamlit as st

st.set_page_config(page_title = "Body-Mass-Index Calculator", layout = "centered")
st.title("Body Mass Index (BMI) Calculator")

st.write("Enter your height and weight to calculate your BMI.")

height = st.number_input("Height (in cm): ", min_value = 50.0, max_value = 250.0, step = 0.1)
weight = st.number_input("weight (in kg): ", min_value = 10.0, max_value= 200.0, step = 0.1)

if st.button("Calculate BMI"):
    if height >0 and weight>0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"**Your BMI is:** {bmi:.2f}")
        if bmi < 18.5:
            st.warning("You are UnderWeight")
        elif 18.5 <= bmi < 24.9:
            st.success("You are Normal weight")
        elif 25<= bmi < 29.9:
            st.info("you are Overweight")
        else:
            st.error("Obese")
    else:
        st.warning("Please enter valid height and weight.")
