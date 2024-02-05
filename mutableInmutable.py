
# Variables float,int,string son inmutables no se pueden cambiar se creara otra caja para guardar el valor nuevo
# Lista es mutable
#id para saber la posicion de la caja

"""
Estás trabajando en el área de pruebas para una empresa de finanzas. Crear un programa para confirmar que la variable (inflacion = 3.765) es un tipo float e inmutable. Usar == para comprobar los cambios realizados. Documentar tu código con comentarios. 
"""
inflacion = 22000.34
print(id(inflacion))
inflacionyyuyuyu = 22000.34
print(id(inflacionyyuyuyu))

a = 5
b = 4.32
c = 10
nums = [a,b,c]
sum = 0
for i in nums:
    if(isinstance(i, int)):
        sum = i + sum

print(sum)