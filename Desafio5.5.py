print("Opções: \na. Somar \nb. Multiplicar \nc. Maior número \nd. Menor número")

def soma (x,y):
    total = x + y
    print("Resultado: ",total)
    return ("")

def multi (x,y):
    total = x * y
    print ("Resultado: ",total)
    return ("")

def maior (x,y):
    total = x,y
    print ((max (total)),"é o maior número.")
    return ("")

def menor (x,y):
    total = x,y
    print ((min (total)),"é o menor número.")
    return ("")
    

while True: 
    opções = str (input("Escolha uma opção: "))

    if opções == str ("a"):       
        x = int (input("Digite um número: "))
        y = int (input("Digite outro número: "))
        print(soma(x,y))
        break

    if opções == str ("b"):
        x = int (input("Digite um número: "))
        y = int (input("Digite outro número: "))
        print(multi(x,y))
        break

    if opções == str ("c"):
        x = int (input("Digite um número: "))
        y = int (input("Digite outro número: "))
        print(maior(x,y))
        break

    if opções == str ("d"):
        x = int (input("Digite um número: "))
        y = int (input("Digite outro número: "))
        print(menor(x,y))
        break
    
    else:
        print("Opção inválida.")