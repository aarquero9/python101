#continue para skipear el resto del bucle
libros = ["libro 1", "libro 2", "libro 3"]
accion = ""
while accion != "q":
    print("1--->Agregar un libro")
    print("2--->Quitar el ultimo libro")
    print("3--->Ver el ultimo libro")
    print("q--->Salir de la biblioteca")
    match accion:
        case "1":
           name = input("Como se llama el libro que quieres agregar?")
           libros.append("name")
           accion= ""
        case "2":
           print("Se ha eliminado el ultimo libro")
           libros.pop()
           accion= ""
        case "3":
            print(libros[-1])
            accion= ""
        case _:
            accion = input("Que quieres hacer?")
print('Adios y gracias!')
