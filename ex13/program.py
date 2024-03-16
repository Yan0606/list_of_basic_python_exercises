number = int(input('Numero: '))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')
elif number == 0:
    print(number, 'é zero')
elif number == 1:
    print(number, 'é um')
else:
    print(number, 'é negativo')