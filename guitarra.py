class Guitarra:
    def __init__(self, marca: str, cuerdas: int):
        self.marca = marca
        self.cuerdas = cuerdas
        self._precio = 100

    def tocar(self):
        print(f"Suena la musica de marca {self.marca}")


# MAIN------------------------------------->

cuerdas = input("Cuantas cuerdas tiene tu guitarra?")
marca = input("Quer marca es tu guitarra?")
guitarra = Guitarra(marca, cuerdas)
