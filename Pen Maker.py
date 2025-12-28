import streamlit as st

st.title("Pen Maker App")

if st.button("Make a Pen"):
    st.success("Your Pen has been Made")

add_ink = st.checkbox("Add Ink")

if add_ink:
    st.write("Added Ink in the Pen")

pen_type = st.radio("Pick your Pen: ", ["Cello Gripper", "Cello Butterflow", "Hauser XO"])
st.write(f"Selected Pen: {pen_type}")

Colour = st.selectbox("Choose Ink of Colour: ", ["Blue", "Black", "Red"])
st.write(f"Selected Colour: {Colour}")

name = st.text_input("Enter your Name")
if name:
    st.write(f"Welcome, {name} ! You Order is on the way")

Rating = st.slider("Rating", 0, 5, 3)
st.write(f"Rating: {Rating}")

dob = st.date_input("Selct your date of birth")