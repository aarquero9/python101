
mensage = input("Que acción quieres hacer?")

match mensage:
    case "Encender":
        print("Encendido!")
    case "Mover":
        print("Me estoy moviendo")
    case "Parar":
        print("Ya he parado")
    case _:
        print("No te he entendido")