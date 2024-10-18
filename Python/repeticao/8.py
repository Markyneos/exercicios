#Faça um programa que leia 5 números e informe a soma e a média dos números.
from random import randint

escolha = input("Você deseja escolher 5 números ou que sejam aleatórios?(e/a): ")
soma = 0
media = 0
numeros = []

match escolha:
  case 'e':
    for i in range(5):
      numeros.append(int(input(f"Digite o {i + 1}° número: ")))

    for i in numeros:
      soma += i
    media = soma / 5
  case 'a':
    for i in range(5):
      numeros.append(randint(1, 100))

    print(f"Números: {numeros[0]}, {numeros[1]}, {numeros[2]}, {numeros[3]}, {numeros[4]}")

    for i in numeros:
      soma += i
    media = soma / 5

print(f"Soma: {soma}\nMédia: {media}")
