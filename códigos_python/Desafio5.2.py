from time import sleep

def contagem_regressiva (num):
    if num > 0:
        for i in range (num,-1,-1):
            print(i)
            sleep(1)
        return ("Fim.")
    else:
        return ("ERRO.")

num = int(input("Informe um numero: "))
print(contagem_regressiva(num))