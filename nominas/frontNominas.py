import names
import random
import idiomasProgramacion
import progamador
import sistemaNominas
import analista

empleados = []

for i in range(10):
    name = random.choice(names.NAMES)
    salario = random.randint(500, 1500)
    idiomas = random.randint(1, 5)
    idiomasProgra = random.choice(idiomasProgramacion.IDIOMAS)
    newProgramer = progamador.Programador(name, salario, idiomas, idiomasProgra)
    empleados.append(newProgramer)

for i in range(10):
    name = random.choice(names.NAMES)
    salario = random.randint(500, 1500)
    velocidad = random.randint(20, 1200)
    newAnalista = analista.analista(name, salario, velocidad)
    empleados.append(newAnalista)

nominas = sistemaNominas.Sistema_Nominas()
nominas.calcular_nominas(empleados)
