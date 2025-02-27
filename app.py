import streamlit as st
from PIL import Image 

st.title("Mi primera app")

st.header("en este espacio comienzo a desarrollar mis apliacaciones para interfaces multimodales")
st.write("me encantan los campos de lavanda.")
image = Image.open('lavanda.jpeg')

st.image(image, caption = 'lavanda')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)





whit col1:
st.subheader(Esta es la primera columna")
ST.write("Las interfaces multimodales mejoran la experiencia de usuario")
respecto = st.checbox('Estoy de acuerdo)
if resp:
                      st.write('Correcto')
                      
whit col2:
                      st.subheader("Esta es la segunda columna")
                      modo = st.radio ("que modalidad es la principal en tu interfaz", ('visual', 'auditiva'. 'tactil))
                      if modo == 'visual':
                          st.write('La vista es fundamentalpara tu interfaz')
                      if modo == 'auditiva':
                          st. write('la audicion es fundamental para tu interfaz')
                      if modo == 'Tactil'
                          st.write('El tacto es fundametal para tu interfaz')
