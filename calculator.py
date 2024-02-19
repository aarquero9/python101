
import mathBasic

accion = ""

while accion != "q":
    match accion:
        case "1":
            print(f"La suma es {mathBasic.sumar(num1,num2)}")
            accion = ""
        case "2":
            print(f"La resta es {mathBasic.restar(num1,num2)}")
            accion = ""
        case "3":
            print(f"La mutiplicación es {mathBasic.multiply(num1,num2)}")    
            accion = ""
        case "4":
            print(f"La división es {mathBasic.divide(num1,num2)}") 
            accion = ""
        case _:
            print("1--->Sumar")
            print("2--->Restar")
            print("3--->Multiplicar")
            print("4--->Dividir")
            print("q--->Salir de la app")
            accion = input("Que quieres hacer?")
            num1 = int(input("Primer valor? "))
            num2 = int(input("Segundo valor? "))
