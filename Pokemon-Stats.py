import streamlit as st
import pandas as pd

st.title("Pokemon Stats")

file = st.file_uploader("Upload your csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
else:
    df = pd.read_csv("Files/FirstGenPokemon.csv")

st.subheader("Data Preview")
st.dataframe(df)

if file:
    st.subheader("Summary stats")
    st.write(df.describe())