import streamlit as st

if 'players' in st.session_state:
    names= []
    for i in st.session_state.players:
        names.append(i.name)
        st.image(i.image)
    raza = st.radio(
        "Selecciona un personaje:",
        names,
        horizontal=True,
    )
else:
    st.write("No players where created")