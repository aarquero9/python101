import streamlit as st
import sqlite3

with st.form(
    "My form",
    clear_on_submit=True,
):

    st.title("Creación de peliculas")
    nombre = st.text_input("Tiltulo de la pelicula")
    duracion = st.number_input("Duración")
    
    if st.form_submit_button("Crear"):
        conn = sqlite3.connect("pelis.db")
        filmData = (nombre, duracion)
        cur = conn.cursor()
        cur.execute(
                "INSERT INTO PELICULAS (nombre,duracion) VALUES(?,?);", filmData
            )
        conn.commit()
        conn.close()
        