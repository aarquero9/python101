import streamlit as st
import sqlite3

with st.form(
    "My form",
    clear_on_submit=True,
):

    st.title("Show Entries ")
    selection = st.text_input("ID especifico")

    if st.form_submit_button("Show"):
        if selection:
            conn = sqlite3.connect("pelis.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Peliculas WHERE id = ?;", (selection,))

            rows = cur.fetchall()
            st.write(rows)
        else:
            conn = sqlite3.connect("pelis.db")
            cur = conn.cursor()

            cur.execute("SELECT * FROM Peliculas")

            rows = cur.fetchall()
            st.write(rows)
        conn.close()
