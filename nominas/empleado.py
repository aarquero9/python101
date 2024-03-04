class Empleado:

    def __init__(self, name, salario):
        self.name = name
        self.salario = salario

    def calcular_nomina(self):
        return self.salario * self.modificadores()