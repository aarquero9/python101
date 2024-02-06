#Dinero total del usuario
dinero = 1000
#Inicializamos la accion tomada por el usuario
action = ""
#Inicializamos la lista de movimientos 
movements = []
#Realizamos un bucle while que se terminara si pulsa el usuario 'q'
while action != 'q':
    match action:
        #Mostramos dinero total y reset de accion
        case "1":
           print(dinero)
           action= ""
        #Preguntamos cuanto dinero quiere ingresar y lo añadimos a la cuenta y a los movimientos
        case "2":
           ingreso = float(input("Cuanto quieres ingresar? "))
           dinero += ingreso
           movements.append(ingreso)
           action= ""
        #Preguntamos cuanto dinero quiere retirar y lo añadimos a la cuenta y a los movimientos
        case "3":
            retiro = float(input("Cuanto quieres retirar? "))
            dinero -= retiro
            movements.append(retiro*-1)
            action= ""
        #Resultado default mostramos las opciones y pedimos accion
        case _:
            print("1--->Ver dinero total")
            print("2--->Ingresar dinero")
            print("3--->Retirar dinero")
            print("q--->Salir del banco")
            action = input("Que quieres hacer? ")

print("Has realizado estas acciones:")
#Inicializamos la media
media = 0
#Mostramos todas las acciones realizadas por el usuario
for i in movements:
    media += i
    if i < 0:
        print(f"Has retirado {i:.2f} €")
    else: print(f"Has ingresado {i:.2f} €")
#Calculamos la media
media = media / len(movements)
#Mostramos la media de las acciones
print(f"La media de tus movimientos ha sido {media:.2f} €")