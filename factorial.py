import math
num = int(input("Dame un numero para hacer el factorial"))
result = 0
if num<0:
    print("No sirve numeros negativos")
elif  num == 0 or num==1:
    print(f"El factorial es {num}")
else:
    result = math.factorial(num)
    print(f"eL factorial es {result}")