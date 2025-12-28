import streamlit as st

st.title("Hello, Anime Lovers")
st.subheader("Otakus")
st.text("Welcome to my first interactive app")
st.write("Choose your Favourite Anime")

Anime = st.selectbox("Fav Anime: ", ["Darling in the Franxx", "Oregairu", "Pokemon","Fragrant Flower Blooms with Dignity"])

st.write(f"Your choose {Anime}. Excellent Choice")

st.success("Your Animes Choice deserves an Appreciation Man")