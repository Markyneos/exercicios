#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

if __name__ == '__main__':
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  for i in range(num1 + 1, num2):
    print(i)

#Altere o programa anterior para mostrar no final a soma dos números.

  numeros = [i for i in range(num1 + 1, num2)]
  soma = 0
  for i in numeros:
    soma += i
  print(f"Soma dos números: {soma}")
