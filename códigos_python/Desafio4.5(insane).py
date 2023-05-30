num = int(input("Informe um numero: "))
resultado = 1


for i in range (num,0,-1):
    resultado *= i
    print(i,resultado, end = "")

print()