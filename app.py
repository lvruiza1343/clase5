import streamlit as st
from PIL import Image 

st.title("Mi primera app")

st.header("en este espacio comienzo a desarrollar mis apliacaciones para interfaces multimodales")
st.write("me encantan los campos de lavanda.")
image = Image.open('lavanda.jpeg')

st.image(image, caption = 'lavanda')
