def maior(x,y,z):
    if x > y and z:
        print(x,"É o maior número!")
    if y > x and z:
        print(y,"É o maior número!")
    if z > x and y:
        print(z,"É o maior número!")
    return ("")

x = int (input("Informe o primeiro numero: "))
y = int (input("Informe o segundo numero: "))
z = int (input("Informe o terceiro numero: "))

print(maior(x,y,z))