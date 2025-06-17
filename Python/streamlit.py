'''
    Streamlit is a Python library that lets you turn Python scripts into interactive web apps — quickly and easily, 
    especially for data science, machine learning, and dashboards.
'''
import streamlit as st
import time
import pandas as pd
import numpy as np

### To runt his file open 'Git Bash' in terminal and go to the specifed folder then type stramlit run streamlit.py

## Reference: https://docs.streamlit.io/develop/api-reference

## Tittle
st.title("Hello Streamlit")

## Display some text
st.write("This is my first Streamlit app 🎉.")

## Simple DF
data=pd.DataFrame(
    {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [23, 24, 22]
    }
)
st.write(data)

### ------------------------------------------------------------------------
## Code
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

### -------------------------------------------------------------------------------
## Widgets
st.title("Streamlit text input")

name=st.text_input("Enter your name: ")

if name:
    st.write(f"Hey {name}.")

## Slider for numeric
age=st.slider("Select your age", 0, 100, 25) # from 0 to 100, 25 is the default
age_rng=st.slider("Your age range is", 0, 80, (20,35))

## Selectbox and radio
gender=st.radio(
    "Select your gender:", options=["Male", "Female", "Other"]
)

role=st.selectbox(
    "Select your role:", 
    options=["DA", "DS", "ML"]
)

st.write(f"Hey {name} your age is {age}. You are a {gender} working as {role}.")

# File uploader
file_upload=st.file_uploader("Choose your csv file", type="csv")
if file_upload is not None:
    df=pd.read_csv(file_upload)
    st.write(df)


with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")