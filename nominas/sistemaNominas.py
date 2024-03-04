class Sistema_Nominas:

    def calcular_nominas(self, empleados):
        print("Calculando nominas")
        print("===================")
        for empleado in empleados:
            print(f"Nomina para : {empleado.name} - {empleado.lenguaje}")
            print(f"- $ : {empleado.calcular_nomina()}")
            print("")