# capitales = {"Australia" : "Camberra", "España" : "Madrid"}

# print(capitales["Australia"])

# capitales.update({"Mexico" : "Ciudad de mexico"})
# capitales.pop("Mexico")
# capitales.popitem()
# capitales.clear()
# capitales["Euskadi"] = "Donosti"
# print(capitales)

# for k,v in capitales.items():
#     print(k,v)

# for v in capitales.values():
#     print(v)

# for v in capitales.keys():
#     print(v)
import uuid

favoriteFoods = {}
ids = []

for i in range(3):
    print(f"Usuario numero {i+1}")
    name = input("Cual es tu nombre? ")
    favoriteFood = input("Cual es tu comida favorita? ")
    id = uuid.uuid1()
    ids.append(id)
    favoriteFoods[id] = {"food" : favoriteFood, "name" : name}

for i in range(len(ids)):
    for j in favoriteFoods[ids[i]].items():
       print(i)
       print(j)

# print(favoriteFoods)