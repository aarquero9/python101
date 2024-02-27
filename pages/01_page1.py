import streamlit as st
from datetime import datetime

st.session_state.count = 0

def increment_counter():
	st.session_state.count += 1
 
with st.form("My form", clear_on_submit=True):
    st.title("Soporte Tecnico")
    nombre = st.text_input("Nombre de usuario")
    description = st.text_area("Descripción")

    if st.form_submit_button("Agregar problema"):
        description = nombre + " - " + description + " - " + str(datetime.now())
        with open("problemas.txt", "a") as f:  # Creates new txt file writing hola
            f.write(description + "\n")
        st.write("Problema agregado")
        
if st.button("Generar informe"):
    with open("problemas.txt", "r") as f:  # Creates new txt file writing hola
        st.write(f.readlines())

if 'counter' not in st.session_state:
	st.session_state.counter = 0

if st.button("Contar"):
    st.session_state.counter +=1

st.write(f'{st.session_state.counter} veces que contamos')