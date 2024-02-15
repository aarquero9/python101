import os

print(os.getcwd())

os.mkdir("hola") #Makes new folder
os.chdir("hola") #Enters the new folder
with open("filetest.txt", "w") as f: #Creates new txt file writing hola
    f.write("hola") 
d1 = "dir1"
d2 = "dir2"
d3 = "dir3"
f1 = "file.txt"
print(os.path.join(d1,d2,d3,f1))
os.remove("filetest.txt")
os.chdir("..") #Enters the new folder
os.rmdir("hola")
print(os.listdir())
