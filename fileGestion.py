import os
import shutil

#Listado de archivos a crear
files = ["file1.txt","file2.txt","file3.txt","file4.txt",]

#CONSTANTES
USERS = "users"
COMMON = "common"

#Creacion de las carpetas basicas y archivos en caso de que no existan
if(os.path.exists(USERS) == False):
    os.mkdir(USERS)
    
if(os.path.exists(COMMON) == False):
    os.mkdir(COMMON)

if len(os.listdir(COMMON)) == 0:
    os.chdir(COMMON)
    for i in files:
        with open( i , "w") as f:
            f.write("")
    os.chdir("..")

#Get username from user
username = input("Quien eres?")
#Creamos variable del path a la carpeta del usuario
pathToUser = os.path.join(USERS,username)

#Si no existe el usuario creamos la carpeta
if os.path.exists(pathToUser) == False:
     os.makedirs(pathToUser)
     print(f"Perfecto te hemos creado una carpeta nueva {username}")
else:
    print(f"Bienvenido de vuelta {username}")

#Funcion para mostrar los archivos disponibles recibiendo el path
def archivosDisponibles(path):
    archivosDisponibles = os.listdir(path)
    for i in archivosDisponibles:
                print(i)

accion = ""
while accion != "q":
    archivosUsuario = os.listdir(pathToUser)
    print("1--->Copiar archivos a mi carpeta personal")
    print("2--->Copiar TODOS los archivos disponibles a carpeta personal")
    print("3--->Ver quer archivos hay disponibles")
    print("4--->Ver mis archivos")
    print("5--->Borrar uno de mis archivos")
    print("q--->Salir de la app")
    match accion:
        case "1":
            fileName = input("Que archivo quieres copiar?")
            pathToFile = os.path.join(COMMON,fileName)
            if os.path.exists(pathToFile):
                shutil.copy(pathToFile,pathToUser)
            else: print("No existe el archivo que has dicho")
            accion = ""
        case "2":
                archivosComunes = os.listdir(COMMON)
                for i in archivosComunes:
                    pathToFile = os.path.join(COMMON,i)
                    shutil.copy(pathToFile,pathToUser)
                accion = ""
        case "3":
                archivosDisponibles(COMMON)
                accion = ""
        case "4":
                archivosDisponibles(pathToUser)
                accion = ""
        case "5":
                fileName = input("Que archivo quieres borrar?")
                pathToFile = os.path.join(pathToUser,fileName)
                confirm = input("Estas seguro de que quieres borrar el archivo? escribe 'y' para confirmar")
                if os.path.exists(pathToFile) and confirm == "y":
                    os.remove(pathToFile)
                else:
                    print("Operacion cancelada")
                accion = ""
        case _:
            accion = input("Que quieres hacer?")
print('Adios y gracias!')
