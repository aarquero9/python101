# for _ in range(0,101,1):
    #print(_)

#Redondea hcia abajo
    # x = 45.43
    # y = int(x)
    # print(y)

#Imprime 0? Efectivamente
    # loggedIn = False
    # print(int(loggedIn))

    # a = {10,20,30,40}
    # b = {40,50,60,70}
#Muestra los que son iguales entre sets
    #print(a.intersection(b))
#Muestra las diferencias entre el primero y el segundo
    #print(a.difference(b))
#Muestra las diferencias entre los dos sets
    #print(a.symmetric_difference(b))

#Agregar un dato a un set
    # a = set()
    # dato = input("Dame un dato para meter en un set")
    # a.add(dato)
    # print(a)

#Agregar un dato a un frozen set // No existe la funcion add en un frozen set
    # a = frozenset()
    # dato = input("Dame un dato para meter en un set")
    # a.add(dato)
    # print(a)

#Tipo de datos si es set // Obiamente es un tipo set??
    # a = set()
    # print(type(a))

    # developers = {'Maria', 'Pedro'}
    # empleados = {'Maria', 'Pedro', 'Jon', 'Henry'}
    # gym = {'Jon', 'Maria', 'Henry'}

#Resultados de esto
    # empleados.difference(developers, gym)     # qué resultado consigues? // Jon y Henry //No funciona :V
    # gym.intersection(developers)    # qué resultado consigues?

    # print(empleados.difference(developers))
    # print(gym.difference(developers))

#Setear una lista
    # lista = [34,67,4,"Hola","Pedro"]
    # set = set(lista)
    # print(set) #Muestra la lista

#Resultados? 

    #print(f"{0:.3f}") #Error? Matematicas? formatear a decimales (agregar decimales)

    # x= 45.87868
    # print(f"{x:.2f}") #Solo dos decimales

    # valores = range(0,100)

    # for x in valores:
    #     print(x) #del 0 al 99

    # s = "Python es genial!"
    # x = "Python" in s
    # print(x) #true?/1

    # s = "Python es genial"
    # print(s[3]) #t? fun h empieza desde 0

    # listadoAlumnos = ['jon', 'martin', 'hola']
    # print("jon" not in listadoAlumnos) #false

    # a = 5
    # print(bin(a)) #binario de 5

    # number = ('hola')
    # try:
    #     float(number)
    # except ValueError as e:
    #     print(e) #El mensaje de error de no se puede comvertir un string a float?

    # x = 0b1111
    # print(x) #porque es 15 en binario?
    # print(bin(x))
    
    # nombre = input("¿Cúal es tu nombre?")
    # for i in range(0,50):
    #     print(f" {nombre} {i}")

    # decision = input("Contamos para arriba o para abajo?")
    # if(decision == 'up'):
    #     step = 1
    #     max = 5
    # else: 
    #     step = -1
    #     max = -5
    # for i in range(0,max,step):
    #     print(i)

    # x = [10, 50, 20, "Hola", "Agur", 99]
    # print(x[2:4]) #mostramos posicion 2min y antes del 4?
    #print(x[::2]) #muestra los atributos en huecos pares
    # print(x[3::]) # Muestra los tres ultimos
    #print(x[::]) #Mostramos todo?

    # x = [10, 20, 30, 30, 50]
    # y = [50, 60, 70, 80]
    # print(x+y) #suma los arrays
# import timeit
# print(timeit.timeit(stmt='("red", "green", "blue")')),

compra = ["manzana", "Manzana", "kiwis"]
compra.sort()
print(compra)
compraMayus = []
for i in compra:
    compraMayus.append(i.capitalize())

compraMayus.sort()
print(compraMayus)
