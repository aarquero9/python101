import streamlit as st
import sqlite3

with st.form(
    "My form",
    clear_on_submit=True,
):

    st.title("Delete Entries ")
    selection = st.text_input("Select ID especifico")
    loaded = False

    if st.form_submit_button("Delete"):
        conn = sqlite3.connect("pelis.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM PELICULAS WHERE id = ?;", (selection,))
        conn.commit()
        conn.close()
