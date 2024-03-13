# def sumar(num1, num2):
#     return num1 + num2


# sumar = lambda x, y: x + y

# x = sumar(1, 1)

# print((lambda x, y: x + y)(2, 2))

# up = lambda s: s.upper()

# print(up("hola"))

# kaixo = lambda name: f"Egunon {name}"

# paresOInpare = lambda num: "Par" if num % 2 == 0 else "Impar"

# posOrNegative = lambda num: "Positivo" if num > 0  else "Negativo"

# print(posOrNegative(-1))

import requests
import json
r = requests.get('http://127.0.0.1:5000/peliculas')
myarray = json.loads(r.content)

for i in myarray:
    print(i)