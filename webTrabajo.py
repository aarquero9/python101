#Inicializamos la accion
accion = ""
#Inicializamos la lista de trabajadores
listaTrabajadores = []
#Iniciamos la lista del trabajador
trabajador = []
#Bucle while para agregar trabajadores
while accion != 'q':
    trabajador = []
    edad = None
    #Bucle para agregar edad correcta
    while edad not in range(18,65):
        edad = int(input("Introduce la edad del trabajador"))
        if edad not in range(18,65):
            print("La edad es incorrecta")
    #Añadimos la edad al trabajador
    trabajador.append(edad)
    nombre = input("Introduce el nombre del trabajador")
    #Añadimos la nombre al trabajador
    trabajador.append(nombre)
    email = input("Introduce el email del trabajador")
    #Añadimos la nombre al trabajador
    trabajador.append(email)
    #Añadimos el trabajador a la lista de trabajadores
    listaTrabajadores.append(trabajador)
    accion = input("Quieres ingresar otro trabajador? si no introduce 'q'")

#Mostramos la lista de trabajadores
for i in listaTrabajadores:
    print('---------------------------')
    print(f'Nombre : {i[1]}')
    print(f'Email : {i[2]}')
    print(f'Edad : {i[0]} años')
    print('---------------------------')