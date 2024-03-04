import empleado

class analista(empleado.Empleado):

    def __init__(self, nombre, salario, velocidad, lenguaje="Español"):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
        self.velocidad = velocidad

    def modificadores(self):
        a = self.velocidad / 20
        return round(a) 