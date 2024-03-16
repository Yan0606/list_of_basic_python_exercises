def primo(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

for i in range(a, b + 1):
  if primo(i):
    print(i)