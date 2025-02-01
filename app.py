import streamlit as st

# Title
st.title("My First Streamlit App")

# Text input
name = st.text_input("Enter your name:", "")

# Display greeting
if name:
    st.write(f"Hello, {name}! Welcome to my Streamlit app.")