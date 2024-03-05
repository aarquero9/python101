import empleado


# Clase programador que hereda de empleado y tiene atributos nuevos idiomas conocidos y lenguaje
class Programador(empleado.Empleado):

    def __init__(self, nombre, salario, idiomasConocidos, lenguaje):
        super().__init__(nombre, salario)
        self.idiomasConocidos = idiomasConocidos
        self.lenguaje = lenguaje

    # Calculamos los modificadores segun cuantos idiomas conozcan
    def modificadores(self):
        return round(self.idiomasConocidos / 2)
