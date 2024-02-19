

def mensaje(name:str,surname:str,age:int)->str:
    print(f"Hola {name} {surname} con edad de {age}")
    return name+surname
    
name = input("Quien eres?")
surname = input("Y apellido?")
age = int(input("Y edad?"))
result = mensaje(name,surname,age)

print(result)

    