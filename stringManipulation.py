# # texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# # print("X"+texto.strip()+ "X")

# # print(texto.count("hola"))

# # print(texto[0:20])

# # print(len(texto))

# # print(texto[-5:])

# s="    122,Python,es,64,un,777,65,lenguaje,222,de,66,55,programación "

# s = s.strip()
# stringList = s.split(",")
# truelist = []
# for i in stringList:
#     if not i.isnumeric():
#         truelist.append(i)
# resultado = " ".join(truelist)
# print(resultado)

# print(resultado.upper())
# trueResultado = []
# resultadoList = resultado.split(" ")
# for i in resultadoList:
#     trueResultado.append(i.capitalize())

# trueResultado = " ".join(trueResultado)
# print(trueResultado)
#o title
# texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
# texto = texto.replace("Pitón", "Python")
# print(texto)
texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "
countPython = texto.lower().count("python")
print(f"Hay un total de {countPython} en el texto")
print(texto.find("Python"))
print(texto[47:].find("Python"))
if 'código' in texto:
    print("La palabra código esta en el texto")

upperPython = texto.replace("Python", "PYTHON")
print(upperPython)