class Taza:
    def __init__(self, volumen, liquido, cantidad=100):
        self.volumen = volumen
        self.liquido = liquido
        self.cantidad = cantidad

    def llenar(self):
        self.cantidad = 100
        self._verTaza()

    def beber(self, cantidad):
        if cantidad > 0 and self.cantidad > cantidad:
            self.cantidad -= cantidad
        else:
            print("No has podido beber")
        self.verTaza()

    def vaciar(self):
        self.cantidad = 0
        self.verTaza()

    def verTaza(self):
        print(f"Tengo un volumen de {self.volumen}")
        print(f"Tengo liquido de tipo {self.liquido}")
        print(f"Tengo de cantidad {self.cantidad}")

    def __str__(self):
        self.verTaza()
        return "Objeto taza"

class tazaPoderosa(Taza):
    def __init__(self, volumen, liquido, graduacion , cantidad=100):
        self.volumen = volumen
        self.liquido = liquido
        self.cantidad = cantidad
        self.graduacion = graduacion
# Main ------------------------------------------------>
# bebidas = []
# for i in range(3):
#     liquido = input("Que quieres tomar?")
#     volumen = input("De que tamaño?")
#     miTaza = Taza(volumen, liquido)
#     bebidas.append(miTaza)

# for i in bebidas:
#     i.verTaza()

taza1 = tazaPoderosa('pequena','cafe',30)

print(taza1.graduacion)
# cantidad = int(input("Cuanto quieres beber?"))
# miTaza.beber(cantidad)

# miTaza.llenar()

# miTaza.vaciar()
