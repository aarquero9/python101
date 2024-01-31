'''
QUIEN? Metereologo en practicas
QUIERE un programa para pasar fahrenheit a grados
PARA QUE para no pensar mucho
'''

# importamos sys para coger los argumentos
import sys
# Recogemos las variables del usuario
arg = sys.argv
match arg[1]:
    case 'c':
         result = (int(arg[2]) - 32) * 5/9
    case 'f':
        result = (int(arg[2]) * 9/5) + 32
    case _:
        result = "No has enviado los datos correctos"

print(f"El resultado es {result} ")