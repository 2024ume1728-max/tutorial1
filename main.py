import streamlit as st
import pandas as pd
st.title("Hello World")
import matplotlib.pyplot as plt
st.title("hello world")
st.subheader("welcome to my app")
st.write("this is my first streamlit app")
feature=st.selectbox("select a feature",["sepal length","sepal width","petal length","petal width"])
st.write(f"You selected {feature}")
option=st.radio("choose an option",["option 1","option 2","option 3"])
if st.button("click me"):
    st.write("button clicked")
checker=st.checkbox("check me")
if checker:
    st.write("checkbox checked!")
    