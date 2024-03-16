def calcular_mrq(x1, x2, x3, x4):
    n = 4
    soma_raizes = (x1 ** 0.5 + x2 ** 0.5 + x3 ** 0.5 + x4 ** 0.5)
    mrq = (soma_raizes / n) ** 2
    return mrq
x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))
x3 = float(input("Digite o valor de x3: "))
x4 = float(input("Digite o valor de x4: "))
mrq = calcular_mrq(x1, x2, x3, x4)
print("A Média da Raiz Quadrada é:", mrq)