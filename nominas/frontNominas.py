import names
import random
import idiomasProgramacion
import progamador
import sistemaNominas
import analista
import languages

empleados = []

# Genereamos un listado de programadores aleatorios
for i in range(10):
    name = random.choice(names.NAMES)
    salario = random.randint(500, 1500)
    idioma = random.randint(2, 5)
    idiomasProgra = random.choice(idiomasProgramacion.IDIOMAS)
    newProgramer = progamador.Programador(name, salario, idioma, idiomasProgra)
    empleados.append(newProgramer)
# Genereamos un listado de analistas aleatorios
for i in range(10):
    name = random.choice(names.NAMES)
    salario = random.randint(500, 1500)
    velocidad = random.randint(50, 120)
    idioma = random.choice(languages.IDIOMAS)
    newAnalista = analista.analista(name, salario, velocidad, idioma)
    empleados.append(newAnalista)

random.shuffle(empleados)
# Instanciamos un sitema de nominas
nominas = sistemaNominas.Sistema_Nominas()
# Calculamos las nominas y las mostramos
nominas.calcular_nominas(empleados)
