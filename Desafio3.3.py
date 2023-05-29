sal = float (input("Informe teu salário: "))
sal1 = float ((sal * 10)/100)
sal2 = float ((sal * 15)/100)

if sal > 8250:
    print("Bônus de: {}\nTeu salário reajustado é: {}".format(sal1,sal+sal1))
else:
    print("Bônus de: {}\nTeu salário reajustado é: {}".format(sal2,sal+sal2))