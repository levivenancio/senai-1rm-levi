#outra forma de fazer o exercício 3.3

sal = float (input("Informe teu salário: "))
por = float (input("Informe a porcentagem do aumento: "))
sal1 = float ((sal * por)/100)
sal2 = float ((sal * por)/100)

if sal > 8250:
    print("Bônus de: {}\nTeu salário reajustado é: {}".format(sal1,sal+sal1))
else:
    print("Bônus de: {}\nTeu salário reajustado é: {}".format(sal2,sal+sal2))