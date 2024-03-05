import empleado


# Clase analista que hereda de empleado y que tiene lenguaje y velocidad
class analista(empleado.Empleado):

    def __init__(self, nombre, salario, velocidad, lenguaje="Español"):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
        self.velocidad = velocidad

    # Calculamos los modificadores segun la velocidad del analista
    def modificadores(self):
        a = self.velocidad / 50
        return round(a)
