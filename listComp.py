# frutas = ["MANZANAS", "pera", "NARANJA", "uva", "MELON"]
# # nuevas_frutas = []

# nuevas_frutas = [i for i in frutas if i.isupper()]
# for i in frutas:
#     if i.isupper():
#         nuevas_frutas.append(i)

# numeros = [3, 54, -12, 4, -67, 99, -120]
# new_numbers = [i for i in numeros if i > 0]

# print(new_numbers)

numbers = [2, 6, 7, 3, 4, 8]

# new_number = [i for i in numbers if i%2 == 0]

# print ( new_number)

new_numbers = ["Par" if i % 2 == 0 else "Inpar" for i in numbers]

print(new_numbers)
