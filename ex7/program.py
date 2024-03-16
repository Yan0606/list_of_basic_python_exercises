distancia = float(input("Digite a distância percorrida (em km): "))
combustivel = float(input("Digite a quantidade de combustível (em litros): "))

consumomedio = distancia / combustivel

if consumomedio < 8:
  print("Venda seu carro AGORA!")
elif consumomedio >= 8 and consumomedio <= 12:
  print("Pense em vender o carro!")
elif consumomedio > 12:
  print("Relativamente econômico! ")
else:
  print("erro")
