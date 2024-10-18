#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1=120

# def fatorial(n: int) -> int:
#   fatorial = 1
#   while n != 0:
#     fatorial *= n
#     n -= 1
#   return fatorial
#
# numero = int(input("Digite um número para descobrir seu fatorial: "))
#
# print(fatorial(numero))

#20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

def fatorial_limitado(n: int) -> int | None:
  if 0 <= int(n) < 16:
    fatorial = 1
    while n != 0:
      fatorial *= n
      n -= 1
    return fatorial
  else:
    raise ValueError("O número deve ser um inteiro positivo menor que 16")
print("Caso deseja sair do programa, digite 0")
while True:
  numero = int(input("Digite um número para descobrir seu fatorial: "))
  print(fatorial_limitado(numero))
  if numero == 0:
    break
