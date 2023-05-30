n1 = float (input("Informe a nota 1: "))
n2 = float (input("Informe a nota 2: "))
n3 = float (input("Informe a nota 3: "))

media = round ((n1 + n2 + n3) /3,2)

if media >= 6:
    print("Aprovado!")
elif media >= 5:
    print("Falar com o Juça!")
else:
    print("Reprovado!")

print("A média das tuas notas é: ",media)