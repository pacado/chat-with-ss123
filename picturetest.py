import streamlit as st

st.set_page_config(layout="centered")
st.title("Take a picture")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
