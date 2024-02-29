import streamlit as st


class player:
    
    def __init__(
        self,
        name,
        raza,
        clase,
        fuerza,
        destreza,
        constitucion,
        inteligencia,
        sabiduria,
        carisma,
        image,
        description="",
    ):
        self.name = name
        self.raza = raza
        self.clase = clase
        self.destreza = destreza
        self.fuerza = fuerza
        self.constitucion = constitucion
        self.inteligencia = inteligencia
        self.sabiduria = sabiduria
        self.carisma = carisma
        self.image = image
        self.description = description

    def showPlayer(self):
        return f"Name: {self.name} Raza: {self.raza} Clase: {self.clase} Destreza: {self.destreza} Fuerza: {self.fuerza} Constitución: {self.constitucion} Inteligencia: {self.inteligencia} Sabiduria: {self.sabiduria} Carisma: {self.carisma} Descripción: {self.description} Image: {self.image}"


with st.form(
    "My form",
    clear_on_submit=True,
):

    st.title("Creación de personaje")
    nombre = st.text_input("Nombre de jugador")
    raza = st.radio(
        "Selecciona una raza:",
        ["Humano", "Enano", "Elfo", "Draconido"],
        horizontal=True,
    )
    clase = st.radio(
        "Selecciona una clase:",
        ["Barbaro", "Bardo", "Guerrero", "Explorador"],
        horizontal=True,
    )
    image = st.file_uploader("Choose your image")
    description = st.text_area("Descripción")
    fuerza = st.number_input("Fuerza", min_value=0, max_value=90)
    destreza = st.number_input("Destreza", min_value=0, max_value=90)
    constitucion = st.number_input("Constitución", min_value=0, max_value=90)
    inteligencia = st.number_input("Inteligencia", min_value=0, max_value=90)
    sabiduria = st.number_input("Sabiduria", min_value=0, max_value=90)
    carisma = st.number_input("Carisma", min_value=0, max_value=90)
    
    if st.form_submit_button("Crear"):
        newPlayer = player(
                    nombre,
                    raza,
                    clase,
                    fuerza,
                    destreza,
                    constitucion,
                    inteligencia,
                    sabiduria,
                    carisma,
                    image,
                    description,
            )
        st.write(newPlayer.showPlayer())
        if 'players' not in st.session_state:
            st.session_state.players = []
        
        st.session_state.players.append(newPlayer)
        