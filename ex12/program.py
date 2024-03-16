numero =float(input("Insira o numero para calclar seu fatorial: "))
resultado =1
count = 1

while count <= numero:
    resultado *= count
    count += 1 
    print(resultado)
