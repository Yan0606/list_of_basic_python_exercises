def numero_reverso(n):
    reverso = 0

    while n > 0:
        ultimo_digito = n % 10
        reverso = (reverso * 10) + ultimo_digito
        n //= 10
    return reverso

n = int(input("Digite um número: "))
reverso = numero_reverso(n)
print("O reverso de" , n ,  "é: " , reverso)
