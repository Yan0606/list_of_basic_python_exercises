cod = str(input("Digite o código: "))

if cod == 1:
  print("Alimento não perecível!") 
elif cod in [2,3]:
  print("Alimento perecível")
elif cod == 4 or 5 or 6:
  print("Vestuário")
elif cod == 8 or 7 or 9:
  print("Limpeza")
elif cod == 10:
  print("Utensílios domésticos")
elif cod == 11 or 12:
  print("Eletrônicos")
else :
  print("Código Inválido")