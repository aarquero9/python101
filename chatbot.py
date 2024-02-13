import re

respuesta = input("Hola como estas? Soy Elisa y tu? ")

respuesta = input("Cuantos anos tienes? ")

while respuesta.endswith(" anos tengo")!= True:
    print("Pista: ... anos tengo")
    respuesta = input("Cuantos anos tienes? ")
    print(respuesta)

print("Que bien me alegro por ti!")
respuesta = input("¿Dónde estás? ")

while not re.match(r"^(E|e)stoy en [A-Za-z]+$", respuesta):
    respuesta = input("Pista: ¿Estoy en...? ")

print("Me alegro que estes en algun lado")