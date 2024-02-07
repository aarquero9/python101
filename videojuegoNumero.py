#Importamos la biblioteca de generar randoms
import random
#Pedimos los valores minimos y maximos del valor random que vamos a generar
print("Intenta adivinar el numero aleatorio generado")
minValue = int(input("Dame valor minimo"))
maxValue = int(input("Dame valor maximo"))
#Generamos el numero aleatorio
RNG = random.randint(minValue, maxValue)
#Comenzamos a pedir al usuario el numero que ha salido
playerValue = int(input("Cual crees que es el numero aleatorio?"))
while playerValue != RNG:
    #Dependiendo de si es mayor o menor mostramos un texto
    if playerValue > RNG:
        print("Tu numero es mayor al generado")
    else: print("Tu numero es menor al generado")
    playerValue = int(input("Cual crees que es el numero aleatorio?"))
#Se ha hacertado el valor
print( "Lo has logrado")