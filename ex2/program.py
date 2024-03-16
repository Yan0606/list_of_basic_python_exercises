import math

catl1 = float(input("Digite o primeiro cateto"))
catl2 = float(input("Digite o segundo cateto"))

hip = math.sqrt(pow(catl1,2) + pow(catl2,2))
print ("O valor da hipotenusa é: " + str(hip))
