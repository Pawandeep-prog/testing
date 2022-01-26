import streamlit as st 

st.title("Welcome to Flower Prediction app")

a = st.text_input("Field 1")
b = st.text_input("Field 2")

btn = st.button("predict")

if btn:
	st.text("button is clicked ")
	st.text("you enetered : " + a + "  " + b)