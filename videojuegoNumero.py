import random
print("Intenta adivinar el numero aleatorio generado")
minValue = int(input("Dame valor minimo"))
maxValue = int(input("Dame valor maximo"))
RNG = random.randint(minValue, maxValue)
print(RNG)
playerValue = int(input("Cual crees que es el numero aleatorio?"))
while playerValue != RNG:
    if playerValue > RNG:
        print("Tu numero es mayor al generado")
    else: print("Tu numero es menor al generado")
    playerValue = int(input("Cual crees que es el numero aleatorio?"))

print( "Lo has logrado")