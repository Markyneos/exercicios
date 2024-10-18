#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

valor = 15
while valor < 0 or valor > 10:
  try:
    print("Digite um valor de 0 a 10")
    valor = int(input())
    if valor < 0 or valor > 10:
      print("Digite um valor válido!")
    else:
      print("Parabéns, você digitou o valor certo")
  except ValueError:
    print("Digite um valor válido!")

