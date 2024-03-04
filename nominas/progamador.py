import empleado

class Programador(empleado.Empleado):

    def __init__(self, nombre, salario, idiomasConocidos, lenguaje):
        super().__init__(nombre, salario)
        self.idiomasConocidos = idiomasConocidos
        self.lenguaje = lenguaje

    def modificadores(self):
        return round(self.idiomasConocidos / 2) 