"""
Crear una lista para gestionar tu compra. Por ejemplo, 
compras = [“platanos”, “manzanas”, “leche”]

Añadir “galletas” y “zumo” a la lista de compras
Mostrar todo la lista
Mostrar el segundo y tercer elemento
Mostrar los últimos 2 elementos - “galletas” y “zumo”
Cambiar “zumo” por “zumo de naranja”
Quitar la última compra que has añadido a la lista
Insertar “limones” en una posición del medio de la lista
Mostrar la lista en orden alfabético	

"""

compras = ["platanos", "manzanas", "leche"]
otralista = ["galletas", "zumo"]
finalList = compras + otralista

for i in finalList:
    print(i)
x = len(finalList)
print(finalList[x - 2 : x])
print(finalList[int(x / 2)])
finalList[4] = "zumo de naranja"
print(finalList)
finalList.pop()
print(finalList)

midpoint = len(finalList) // 2
print(finalList[midpoint])

print(midpoint)
finalList = finalList[0:midpoint] + ["limones"] + finalList[midpoint:]
finalList.insert(2, "pera")
finalList.sort()
print(finalList)
