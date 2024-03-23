def fibonacci(n):
    if n <= 0:
        return "O valor de n deve ser um número inteiro positivo e maior que zero."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Digite o valor de n para encontrar o n-ésimo termo da Sequência de Fibonacci: "))
resultado = fibonacci(n)
print(f"O {n}-ésimo termo da Sequência de Fibonacci é: {resultado}")
