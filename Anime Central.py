import streamlit as st

st.title("Anime Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("One Piece")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk5OfXgritzcy-BEZTlH4mXjFmvazA4HoWbA&s")
    vote1 = st.button("Vote One Piece")

with col2:
    st.header("Demon Slayer")
    st.image("https://www.pngall.com/wp-content/uploads/13/Demon-Slayer-Logo.png", width=200)
    vote2 = st.button("Vote Demon Slayer")

if vote1:
    st.success("Thanks for voting One Piece")
elif vote2:
    st.success("Thanks for voting Demon Slayer")

name = st.sidebar.text_input("Enter your name")
anime = st.sidebar.selectbox("Choose your Anime", ["One Piece", "Demon Slayer"])

st.write(f"Welcome {name} and your {anime} is here")

with st.expander("Show Info of Anime"):
    st.write("""
    1. Anime Title
    2. Anime Summary
    3. Anime Episodes      
""")
    
st.markdown("### Welcome to Anime Central")
st.markdown(">Animes")






