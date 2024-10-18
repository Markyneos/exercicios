#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []
while True:
  try:
    for i in range(10):
      numeros.append(int(input(f"Digite o {i + 1}° número: ")))

    contador_i = 0
    contador_p = 0

    for i in numeros:
      if i % 2 == 0:
        contador_p += 1
      elif i % 2 != 0:
        contador_i += 1

    print(f"Número de números ímpares: {contador_i}\nNúmero de números pares: {contador_p}")
    break
  except ValueError:
    print("Digite somente números inteiros!")
