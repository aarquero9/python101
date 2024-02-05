
#Bucle de confirmar contraseñas
# password = input("Escribe la contraseña ")
# confirmPassword = input("Confirma la contraseña ")
# while password != confirmPassword:
#     if(password != confirmPassword):
#         print("Las contraseñas no son iguales")
#     password = input("Escribe la contraseña ")
#     confirmPassword = input("Confirma la contraseña ")
# else: print("Las contraseñas coinciden")
# number = 0
i = 1
ch = "*"
sumNumber = 2
while i > 0:
    if( i == 9 ):
        print(ch*i)
        print("--------")
        print(ch*i)
        sumNumber = -2
        i+= sumNumber
        continue
    print(ch*i)
    i+= sumNumber
   
 