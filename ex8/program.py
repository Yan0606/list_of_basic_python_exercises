media = float(input("Digite a média final: "))
falta = float(input("Digite a quantidade de faltas: "))

if media >= 9 and falta <= 14:
  print("A")
elif media >= 9 and falta >= 14:
  print("B")
elif media >= 7.5 and media < 9 and falta <= 14:
  print("B")
elif media >= 7.5 and media < 9 and falta >= 14:
  print("C")
elif media >= 6 and media < 7.5 and falta <= 14:
  print("C")
elif media >= 6 and media < 7.5 and falta >= 14:
  print("D")
elif media >= 4 and media < 6 and falta <=14:
  print("D")
elif media >= 4 and media < 6 and falta >=14:
  print("E")
elif media >= 0 and media < 4 and falta <= 14:
  print("E")
elif media >= 0 and media < 4 and falta >= 14:
  print("E")
else:
  print("ERRO")