def e_palindromo(n):
    # Verifica se o número é igual ao seu reverso
    return n == numero_reverso(n)

def numero_reverso(n):
    reverso = 0
    numero_original = n
    while n > 0:
        # Extrai o último dígito do número original
        ultimo_digito = n % 10
        # Adiciona o último dígito ao número reverso (deslocando os dígitos anteriores uma casa para a esquerda)
        reverso = (reverso * 10) + ultimo_digito
        # Remove o último dígito do número original
        n //= 10
    return reverso

# Exemplo de uso:
n = int(input("Digite um número inteiro positivo maior ou igual a 10 para verificar se é palíndromo: "))

if n >= 10:
    if e_palindromo(n):
        print(f"{n} é um número palíndromo.")
    else:
        print(f"{n} não é um número palíndromo.")
else:
    print("O número deve ser maior ou igual a 10.")
