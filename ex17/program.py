def e_palindromo(n):
    return n == numero_reverso(n)

def numero_reverso(n):
    reverso = 0
    numero_original = n
    while n > 0:
        ultimo_digito = n % 10
        reverso = (reverso * 10) + ultimo_digito
        n //= 10
    return reverso

n = int(input("Digite um número inteiro positivo maior ou igual a 10 para verificar se é palíndromo: "))

if n >= 10:
    if e_palindromo(n):
        print(f"{n} é um número palíndromo.")
    else:
        print(f"{n} não é um número palíndromo.")
else:
    print("O número deve ser maior ou igual a 10.")
