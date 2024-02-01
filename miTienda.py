"""
Gestión de una tienda
Se podría extender la idea de arriba para crear una aplicación para gestionar la compra de productos en una tienda.

“Bienvenidos a mi tienda. Hoy tenemos especiales de:
manzanas
zumos
leche

Introducir “1” para ver todos los productos, “2” para hacer una compra…”, “3” para borrar un producto, …

Al introducir “2”, mostrar el precio (igual para todos, excepto los productos especiales - % menos) y pedir al usuario dinero (por ejemplo, te dará 20 euros). Dáslo el producto al usuario y la diferencia de dinero (lo que te ha dado menos el coste).
"""

import time
productos = [["Manzanas", 2.4, "€",25],["Peras", 4.23, "€",254],["Piñas", 6, "€",23]]
cartera = 9999999999 
accion = ""
carrito = []
print("Bienvenidos a mi tienda tienes estas opciones disponibles:")
while accion != "q":
    print("1--->Mostrar todos los productos")
    print("2--->Hacer una compra")
    print("3--->Mostrar carrito")
    print("q--->Salir de la tienda")
    print(f"Dinero actual {cartera} €")
    match accion:
        case "1":
            #Mostramos todos los productos
            for i in range(len(productos)):
                print(f"Producto num {i+1} que es {productos[i][0]} con valor de {productos[i][1]} {productos[i][2]}")
                accion = ""
            time.sleep(5)
        case "2":
            print("Selecciona por el orden de los productos")
            productoSeleccionado = input("Que producto quieres comprar?")
            #Tenemos el producto
            if(int(productoSeleccionado) in range(0,len(productos))):
                print(f"Has seleccionado {productos[int(productoSeleccionado)][0]}")
                cantidad = input("Cuantos quieres?")
                precio = productos[int(productoSeleccionado)][1] * productos[int(productoSeleccionado)][3]
                print(f"El total de la compra es {int(precio)}")
                print("Escribes CONFIRMAR")
                confirm = input("Quieres confirmar la compra?")
                if(confirm == "CONFIRMAR"):
                    #Tiene suficiente dinero y hay suficientes productos
                    if(precio < cartera and productos[int(productoSeleccionado)][3] >= int(cantidad) ):
                        #Actualizar los productos
                        productos[int(productoSeleccionado)][3] = productos[int(productoSeleccionado)][3] - float(cantidad)
                        #Actualizar monedero de cliente
                        cartera = cartera - precio
                        #Actualizar carrito
                        producto = productos[int(productoSeleccionado)]
                        producto[3] = int(cantidad)
                        carrito.append(producto)
                    else: print("No se ha podido efectuar la compra")
                else: print("Has cancelado la compra")
            accion = ""
        case "3":
            for i in carrito:
                print(f"Tienes {i[3]} de {i[0]}")
            time.sleep(5)
            accion = ""
        case _:
            accion = input("Que quieres hacer?")
print('Adios y gracias!')