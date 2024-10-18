#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

from random import randint

numeros = []
escolha = input("Você deseja escolher um conjunto de números?(y/n): ")

if escolha == 'y':
  quantidade = int(input("Quantos números você deseja escolher?: "))
  for i in range(quantidade):
    numeros.append(int(input(f"Digite o {i + 1}° número: ")))
    if numeros[i] > 1000 or numeros[i] < 0:
      raise ValueError('Só podem ser aceitos valores entre 0 e 1000')
    
  menor = numeros[0]
  maior = numeros[-1]
  soma = 0

  for i in range(len(numeros)):
    if menor > numeros[i]:
      menor = numeros[i]
    if maior < numeros[i]:
      maior = numeros[i]
    soma += numeros[i]

  

  print(f"Soma: {soma} | Menor número: {menor} | Maior número: {maior}")

elif escolha == 'n':
  quantidade = int(input("Quantos números você deseja escolher?: "))
  for i in range(quantidade):
    numeros.append(randint(1, 100))
  menor = numeros[0]
  maior = numeros[-1]
  soma = 0

  for i in range(len(numeros)):
    if menor > numeros[i]:
      menor = numeros[i]
    if maior < numeros[i]:
      maior = numeros[i]
    soma += numeros[i]
  print("Números:")
  for i in numeros:
    print(i)
  print(f"Soma: {soma} | Menor número: {menor} | Maior número: {maior}")
else:
  print("Digite valores válidos!")

#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
