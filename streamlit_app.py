import streamlit as st
import mathBasic as math
from streamlit_modal import Modal
import pandas as pd

modal = Modal(key="Demo Key",title="Add")              
def calculate(action,num1,num2):
    match action:
        case "Sumar":
            result = math.sumar(num1,num2)
        case "Restar":
            result = math.restar(num1,num2)
        case "Multiplicar":
            result = math.multiply(num1,num2)
        case "Dividir":
            result = math.divide(num1,num2)
    st.write(f"El resultado de tu {action} es {result}")
    

st.markdown("# Calculadora")

    

left_comlum, right_column = st.columns(2)

with left_comlum:
    num1 = st.number_input("Introducir el primer numero", min_value=0, max_value=9999)
    num2 = st.number_input("Introducir el segundo numero", min_value=0, max_value=9999)

    oper = st.radio("Selecciona una operacion:",["Sumar", "Restar", "Multiplicar", "Dividir"])

    calculate(oper,num1,num2)
    if st.button("Calcular"):
        st.write(f"The result is = {calculate(oper,num1,num2)}")
        with modal.container():
            st.video('https://www.youtube.com/watch?v=5Od0aOse1wc&ab_channel=Temu')

with right_column:
    video_bytes = st.video('https://youtu.be/FVsvrFAWDTM') 
    

add_slider = st.sidebar.slider("Select a range of valors", 0.0, 100.0,(25.0,75.0))
st.sidebar.video("https://www.youtube.com/watch?v=Ahi-btqB8N4&ab_channel=UFC")

df2 = pd.read_csv("https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/pokemon.csv")

st.data_editor(df2)
# st.write(oper)
# def testingFuntion(edad): 
#     if edad :
#         st.write(f"Tu edad es {int(edad * -6)}")
#  aaa
# st.title("Este es el proyecto de Arquero")

# animales = ("Perro", "Gato", "Lagarto")
# name = st.text_input("Que animal te gusta?")

# if name in animales:
#     st.write("Eres un tio que sabe")
# elif name:
#     st.write("Tienes mal gusto")

# edad = st.number_input("Que edad tienes?")

# st.button("TEST", on_click = testingFuntion(edad))

