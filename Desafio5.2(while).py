from time import sleep
def contagem_regressiva(num1):
    while num1 > 0:
        num1 = num1 -1
        print (num1)
        sleep(1)

n1 = int(input("Contagem a partir de: "))
print(n1)
sleep(1)
contagem_regressiva(n1)