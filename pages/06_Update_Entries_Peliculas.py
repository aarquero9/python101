import streamlit as st
import sqlite3

with st.form(
    "My form",
    clear_on_submit=True,
):

    st.title("Update Entries ")
    selection = st.text_input("Select ID especifico")
    loaded = False
    if st.form_submit_button("Load entry") or selection:
        loaded = True
        conn = sqlite3.connect("pelis.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Peliculas WHERE id = ?;", (selection,))
        rows = cur.fetchall()
        nombre = st.text_input("Tiltulo de la pelicula", value=rows[0][1], key=1)
        duracion = st.text_input("Duración", value=rows[0][2], key=2)
        conn.close()

    if st.form_submit_button("Update"):
        conn = sqlite3.connect("pelis.db")
        filmData = (nombre, duracion, selection)
        cur = conn.cursor()
        cur.execute(
            "UPDATE PELICULAS SET nombre = ?, duracion = ?  WHERE id = ?;",
            filmData,
        )
        conn.commit()
        conn.close()
