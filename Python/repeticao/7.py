#Faça um programa que leia 5 números e informe o maior número.

from random import randint

if __name__ == '__main__':
  escolha = input("Você deseja escolher os 5 números? Caso não, serão gerados números aleatórios(y/n): ")
  if escolha == 'y':
    numeros = []
    for i in range(5):
      numeros.append(int(input(f"Digite o {i + 1}° número: ")))

    maior = numeros[0]

    for i in range(len(numeros)):
      if maior < numeros[i]:
        maior = numeros[i]
    print(f"O maior número de todos os inputs é: {maior}")
  if escolha == 'n':
    numeros = []
    for i in range(5):
      numeros.append(randint(1, 100))

    print(f"Números: {numeros[0]}, {numeros[1]}, {numeros[2]}, {numeros[3]}, {numeros[4]}")
    maior = numeros[0]

    for i in range(len(numeros)):
      if maior < numeros[i]:
        maior = numeros[i]
    print(f"O maior número de todos os inputs é: {maior}")
