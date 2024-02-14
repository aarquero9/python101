import os

print(os.getcwd())

os.mkdir("hola") #Makes new folder
os.chdir("hola") #Enters the new folder
with open("filetest.txt", "w") as f: #Creates new txt file writing hola
    f.write("hola") 

os.remove("filetest.txt")
os.chdir("..") #Enters the new folder
os.rmdir("hola")
print(os.listdir())
