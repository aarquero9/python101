# productos = ["raqueta", "balon", "guantes", "pelota"]

# cap = lambda x: x.capitalize()


# # productoC = [ cap(i) for i in productos]

# print(list(map(cap,productos)))
# print(productoC)
import math

numList = [5, 6, 8, 9]
list2 = list(map(lambda x: x + 2, numList))
list3 = list(map(lambda x: math.sqrt(x), numList))

print(list(map(lambda x, y, u: x * y * u, numList, list2, list3)))
